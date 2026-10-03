#!/usr/bin/env python3
"""Все американские акции (NASDAQ, NYSE, AMEX): снимок доходностей по всем и история по ликвидным.

Список тикеров — открытый ежедневный набор rreichel3/US-Stock-Symbols на GitHub (около 7 000 символов),
из него отсеиваются варранты, юниты, права, привилегированные акции и облигации (остаётся около 5 800).
Цены — Yahoo Finance, дневные бары за 2 года.

Пишет в us_all/:
  _universe.csv  — символ, название, биржа, сектор, отрасль, капитализация, страна, год IPO
  _snapshot.csv  — по каждому символу: последняя закрытая сессия, цена, рост за 7/14/30/182/365 дней,
                   средний дневной оборот в $ за 20 сессий, капитализация, сектор
  hist/<SYM>.csv — дневная история за 2 года для акций с оборотом от HIST_MIN_USD (по умолчанию $10 млн в день)
  _missing.txt, _updated.txt
Только стандартная библиотека Python 3.8+.
"""
import csv, json, os, re, sys, time, random, urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone, timedelta

LIST_BASE = os.environ.get("LIST_BASE", "https://raw.githubusercontent.com/rreichel3/US-Stock-Symbols/main")
HOSTS = os.environ.get("YAHOO_HOSTS", "https://query1.finance.yahoo.com,https://query2.finance.yahoo.com").split(",")
OUT = os.environ.get("OUT", "us_all"); WORKERS = int(os.environ.get("WORKERS", "4"))
HIST_MIN = float(os.environ.get("HIST_MIN_USD", "10000000")); LIMIT = int(os.environ.get("LIMIT", "0"))
UA = {"User-Agent": "Mozilla/5.0"}
BAD_NAME = re.compile(r"\b(Warrant|Warrants|Unit|Units|Right|Rights|Preferred|Depositary Shares? Representing|Notes due|Debentures|Trust Preferred|% )", re.I)

def get(url, tries=5):
    for a in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception:
            time.sleep(2 * (a + 1) + random.random() * 2)
    return None

def universe():
    rows = []
    for ex in ("nasdaq", "nyse", "amex"):
        data = get(f"{LIST_BASE}/{ex}/{ex}_full_tickers.json")
        if not data: sys.exit(f"не скачался список {ex}")
        for r in data:
            s = str(r.get("symbol", "")).strip(); n = str(r.get("name", ""))
            if not s or "^" in s or ("/" in s and not re.match(r"^[A-Z]+/[A-Z]$", s)): continue
            if BAD_NAME.search(n): continue
            if re.search(r"(W|WS|U|R)$", s) and re.search(r"Warrant|Unit|Right", n, re.I): continue
            try: cap = float(str(r.get("marketCap", "")).replace(",", "") or 0)
            except ValueError: cap = 0.0
            rows.append(dict(symbol=s, yahoo=s.replace("/", "-"), name=n, exchange=ex.upper(), sector=r.get("sector", ""),
                             industry=r.get("industry", ""), market_cap=cap, country=r.get("country", ""), ipo_year=r.get("ipoyear", "")))
    seen = set(); out = []
    for r in rows:
        if r["symbol"] not in seen: seen.add(r["symbol"]); out.append(r)
    return out[:LIMIT] if LIMIT else out

def bar_closed(day, off, now):
    """Сессия day закрыта, если по времени биржи уже прошло 16:00.
    off — смещение биржи из ответа Yahoo: летом −14400 (20:00 UTC), зимой −18000 (21:00 UTC).
    Фиксированные часы UTC здесь не годятся: в летнее время прогон между 20:00 и 21:00 UTC
    выбрасывал бы уже закрытую сессию и last_session отставал бы на день."""
    close = datetime(day.year, day.month, day.day, tzinfo=timezone.utc) + timedelta(seconds=16 * 3600 - off)
    return now >= close

def fetch(u):
    host = random.choice(HOSTS)
    d = get(f"{host}/v8/finance/chart/{u['yahoo']}?range=2y&interval=1d")
    if not d or not d.get("chart", {}).get("result"): return u, None
    r = d["chart"]["result"][0]; ts = r.get("timestamp") or []; q = r["indicators"]["quote"][0]
    adj = ((r["indicators"].get("adjclose") or [{}])[0].get("adjclose")) or q.get("close")
    off = (r.get("meta") or {}).get("gmtoffset") or 0
    now = datetime.now(timezone.utc); today = now.date(); rows = []
    for i, t in enumerate(ts):
        c = q["close"][i]; a = adj[i] if adj and i < len(adj) else c
        if c is None or a is None: continue
        dt = datetime.fromtimestamp(t + off, timezone.utc).date()
        if dt == today and not bar_closed(dt, off, now): continue   # незакрытая сессия
        rows.append((dt, q["open"][i], q["high"][i], q["low"][i], c, a, q["volume"][i] or 0))
    return u, rows

def ret(rows, days):
    last_d, last_a = rows[-1][0], rows[-1][5]; ref = None
    for r in reversed(rows):
        if r[0] <= last_d - timedelta(days=days): ref = r; break
    if not ref or (last_d - ref[0]).days > days + 7 or ref[5] <= 0: return ""
    return round(last_a / ref[5] - 1, 6)

def main():
    os.makedirs(os.path.join(OUT, "hist"), exist_ok=True)
    U = universe(); print(f"символов после отсева: {len(U)}")
    with open(os.path.join(OUT, "_universe.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(U[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(U)
    snap = []; miss = []; hist_keep = set()
    with ThreadPoolExecutor(WORKERS) as ex:
        for u, rows in ex.map(fetch, U):
            if not rows or len(rows) < 5: miss.append(u["symbol"]); continue
            adv = sum(r[4] * r[6] for r in rows[-20:]) / min(20, len(rows))
            snap.append(dict(symbol=u["symbol"], last_date=rows[-1][0].isoformat(), close=round(rows[-1][4], 4),
                             r7=ret(rows, 7), r14=ret(rows, 14), r30=ret(rows, 30), r182=ret(rows, 182), r365=ret(rows, 365),
                             adv20_usd=round(adv), market_cap=u["market_cap"], sector=u["sector"], industry=u["industry"], exchange=u["exchange"], name=u["name"]))
            if adv >= HIST_MIN:
                fn = u["yahoo"]; hist_keep.add(fn + ".csv")
                with open(os.path.join(OUT, "hist", fn + ".csv"), "w", newline="") as f:
                    w = csv.writer(f, lineterminator="\n"); w.writerow(["date", "open", "high", "low", "close", "adjclose", "volume"])
                    for r in rows: w.writerow([r[0].isoformat()] + [("" if v is None else round(v, 4)) for v in r[1:6]] + [r[6]])
    for fn in os.listdir(os.path.join(OUT, "hist")):
        if fn not in hist_keep: os.remove(os.path.join(OUT, "hist", fn))
    if not snap: sys.exit(f"ни одной акции не скачалось из {len(U)} — ничего не записываю")
    snap.sort(key=lambda r: r["symbol"])
    with open(os.path.join(OUT, "_snapshot.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(snap[0].keys()), lineterminator="\n"); w.writeheader(); w.writerows(snap)
    open(os.path.join(OUT, "_missing.txt"), "w").write("\n".join(sorted(miss)) + ("\n" if miss else ""))
    last = max(r["last_date"] for r in snap)
    open(os.path.join(OUT, "_updated.txt"), "w").write(f"ok={len(snap)} of {len(U)} hist={len(hist_keep)} last_session={last}\n{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ}\n")
    print(f"готово: {len(snap)} из {len(U)}, с историей {len(hist_keep)}, пропусков {len(miss)}, последняя сессия {last}")
    if len(miss) > 0.10 * len(U): sys.exit(f"слишком много пропусков: {len(miss)}")

if __name__ == "__main__": main()
