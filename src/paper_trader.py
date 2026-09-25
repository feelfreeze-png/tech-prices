#!/usr/bin/env python3
"""Бумажная торговля эксперимента «10% в неделю»: два правила, журнал в journal/.

Правило A «лидеры в тренде» (по воскресному закрытию, раз в неделю):
  если BTC выше средней за 50 дней и вырос за 50 дней — купить 3 монеты с лучшим ростом за 7 дней
  из 50 самых торгуемых монет пула (медиана оборота за 30 дней), по $45; через неделю закрыть.
Правило L «против новых листингов» (каждый день):
  продать новый контракт по закрытию 8-го дня торгов, по $20, не больше 10 сразу,
  если средний оборот первых 7 дней ≥ $5 млн; закрыть через 28 дней или при росте цены
  вдвое (при 1× это ликвидация: убыток = вся ставка); выплаты финансирования учитываются.
Стоп счёта: −20% от максимума — всё закрыть, новых сделок нет.

Запуск каждое утро после обновления данных:
  python3 src/paper_trader.py --repo .            обработать все новые закрытые дни, записать journal/
  python3 src/paper_trader.py --repo . --dry-run  посчитать и напечатать, ничего не записывая
  python3 src/paper_trader.py --repo . --init     создать journal/ с начальным состоянием (один раз)
Только стандартная библиотека Python 3.8+.
"""
import argparse, csv, json, os, sys, statistics
from datetime import date, datetime, timedelta, timezone

START_EQUITY = 1000.0
INITIAL_REALIZED = 7.38          # итог первого набора 15–22.09.2026
STOP_DD = 0.20
COST_SIDE = 0.001                # издержки на каждую сторону сделки
A_SIZE, A_UNIVERSE, A_TOP, A_LOOK, A_MA = 45.0, 50, 3, 7, 50
L_SIZE, L_ENTRY_ROW, L_HOLD, L_MINLIQ, L_MAX, L_LIQ = 20.0, 7, 28, 5e6, 10, 2.0
# позиции, открытые до запуска журнала (набор «лидеров» 21.09.2026 по фактическим ценам 04:00 UTC)
SEED = [("A", "AVAXUSDT", "long", 65.0, "2026-09-20", 11.288),
        ("A", "ZECUSDT", "long", 65.0, "2026-09-20", 1516.49),
        ("A", "ZENUSDT", "long", 65.0, "2026-09-20", 7.752)]
POS_COLS = ["rule", "symbol", "side", "size_usd", "entry_date", "entry_price", "last_date", "last_close", "funding_usd", "pnl_usd"]
TR_COLS = ["rule", "symbol", "side", "size_usd", "entry_date", "entry_price", "exit_date", "exit_price", "funding_usd", "cost_usd", "pnl_usd", "pnl_pct", "reason"]
EQ_COLS = ["date", "realized", "unrealized", "equity", "peak", "drawdown_pct", "open_positions", "stopped"]
RULE_NAME = {"A": "лидеры в тренде", "L": "против новых листингов"}

def d(s): return date.fromisoformat(s[:10])
def ms_to_date(ms): return datetime.fromtimestamp(int(ms) / 1000, tz=timezone.utc).date()
def read_csv(p): 
    with open(p, newline="") as f: return list(csv.DictReader(f))
def write_csv(p, cols, rows):
    tmp = p + ".tmp"
    with open(tmp, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n"); w.writeheader(); w.writerows(rows)
    os.replace(tmp, p)

class Data:
    def __init__(self, repo):
        self.repo = repo; self.pool = {}; self.live = {}; self.live_fund = {}; self.listings = {}
        pdir = os.path.join(repo, "binance_1d")
        for fn in sorted(os.listdir(pdir)):
            if not fn.endswith(".csv"): continue
            rows = [(d(r["open_time_utc"]), float(r["high"]), float(r["close"]), float(r["quote_volume"])) for r in read_csv(os.path.join(pdir, fn)) if r["close"]]
            self.pool[fn[:-4]] = rows
        ldir = os.path.join(repo, "binance_live")
        self.has_live = os.path.isfile(os.path.join(ldir, "_listings.csv"))
        if self.has_live:
            for r in read_csv(os.path.join(ldir, "_listings.csv")): self.listings[r["symbol"]] = int(r["onboard_time_ms"])
            for s in self.listings:
                kp = os.path.join(ldir, "klines_1d", s + ".csv"); fp = os.path.join(ldir, "funding", s + ".csv")
                if os.path.isfile(kp):
                    self.live[s] = [(ms_to_date(r["open_time_ms"]), float(r["high"]), float(r["close"]), float(r["quote_volume"])) for r in read_csv(kp) if r["close"] and float(r["volume"] or 0) > 0]
                if os.path.isfile(fp):
                    self.live_fund[s] = [(int(r["funding_time_ms"]), float(r["rate"])) for r in read_csv(fp) if r["rate"]]
    def series(self, s, upto):
        rows = self.live.get(s) or self.pool.get(s) or []
        return [x for x in rows if x[0] <= upto]
    def bar(self, s, day):
        for x in reversed(self.series(s, day)):
            if x[0] == day: return x
        return None
    def last_day(self): return self.pool["BTCUSDT"][-1][0]
    def funding(self, s, day):  # выплаты за сутки day: (day 00:00, day+1 00:00] UTC
        lo = int(datetime(day.year, day.month, day.day, tzinfo=timezone.utc).timestamp() * 1000)
        hi = lo + 86400000
        return sum(rt for t, rt in self.live_fund.get(s, []) if lo < t <= hi)

class Journal:
    def __init__(self, repo, dry):
        self.dir = os.path.join(repo, "journal"); self.dry = dry
        self.pos = read_csv(self.p("positions_open.csv")); self.trades = read_csv(self.p("trades_closed.csv")); self.eq = read_csv(self.p("equity.csv"))
        for r in self.pos:
            for k in ("size_usd", "entry_price", "last_close", "funding_usd", "pnl_usd"): r[k] = float(r[k] or 0)
        last = self.eq[-1] if self.eq else None
        self.realized = float(last["realized"]) if last else INITIAL_REALIZED
        self.peak = float(last["peak"]) if last else START_EQUITY + INITIAL_REALIZED
        self.stopped = bool(last and last["stopped"] == "1")
        self.last_date = d(open(self.p("_last_run.txt")).read().strip()) if os.path.isfile(self.p("_last_run.txt")) else None
        self.actions = []
    def p(self, fn): return os.path.join(self.dir, fn)

def init_journal(repo, asof):
    jd = os.path.join(repo, "journal"); os.makedirs(os.path.join(jd, "signals"), exist_ok=True)
    if os.path.isfile(os.path.join(jd, "positions_open.csv")): sys.exit("journal/ уже существует — --init не нужен")
    rows = [dict(rule=r, symbol=s, side=sd, size_usd=sz, entry_date=ed, entry_price=ep, last_date=ed, last_close=ep, funding_usd=0.0, pnl_usd=0.0) for r, s, sd, sz, ed, ep in SEED]
    write_csv(os.path.join(jd, "positions_open.csv"), POS_COLS, rows)
    write_csv(os.path.join(jd, "trades_closed.csv"), TR_COLS, [])
    write_csv(os.path.join(jd, "equity.csv"), EQ_COLS, [])
    with open(os.path.join(jd, "_last_run.txt"), "w") as f: f.write(asof.isoformat() + "\n")
    print(f"journal/ создан: {len(rows)} открытых позиций, реализовано ${INITIAL_REALIZED}, обработка начнётся с {asof + timedelta(days=1)}")

def price_pnl(p, price):
    if p["side"] == "long": return p["size_usd"] * (price / p["entry_price"] - 1)
    return max(p["size_usd"] * (1 - price / p["entry_price"]), -p["size_usd"])

def close_pos(J, p, day, price, reason, liquidated=False):
    pp = -p["size_usd"] if liquidated else price_pnl(p, price)
    c1 = p["size_usd"] * COST_SIDE
    J.realized += pp + p["funding_usd"] - c1           # издержки входа уже списаны при открытии
    pnl = pp + p["funding_usd"] - 2 * c1               # итог сделки целиком
    J.trades.append(dict(rule=p["rule"], symbol=p["symbol"], side=p["side"], size_usd=p["size_usd"], entry_date=p["entry_date"], entry_price=p["entry_price"],
                         exit_date=day.isoformat(), exit_price=price, funding_usd=round(p["funding_usd"], 4), cost_usd=round(2 * c1, 4),
                         pnl_usd=round(pnl, 4), pnl_pct=round(100 * pnl / p["size_usd"], 2), reason=reason))
    J.actions.append((day, f"Закрыть {p['symbol']} ({RULE_NAME[p['rule']]}, {'покупка' if p['side']=='long' else 'ставка на падение'} ${p['size_usd']:.0f}) — {reason}; итог ${pnl:+.2f}"))

def open_pos(J, rule, s, side, size, day, price, note=""):
    J.realized -= size * COST_SIDE
    J.pos.append(dict(rule=rule, symbol=s, side=side, size_usd=size, entry_date=day.isoformat(), entry_price=price, last_date=day.isoformat(), last_close=price, funding_usd=0.0, pnl_usd=0.0))
    J.actions.append((day, f"{'Купить' if side=='long' else 'Продать (ставка на падение)'} {s} на ${size:.0f} — {RULE_NAME[rule]}; ориентир — закрытие {day:%d.%m}: {price:g}{note}"))

def btc_trend(D, day):
    c = [x[2] for x in D.series("BTCUSDT", day)]
    if len(c) < A_MA + 1: return False, None, None
    ma = sum(c[-A_MA:]) / A_MA; r50 = c[-1] / c[-A_MA - 1] - 1
    return (c[-1] > ma and r50 > 0), 100 * (c[-1] / ma - 1), 100 * r50

def process_day(D, J, day):
    # 1) переоценка, выплаты, ликвидации и выходы по сроку
    keep = []
    for p in J.pos:
        b = D.bar(p["symbol"], day)
        if b is None: keep.append(p); continue
        if p["side"] == "short" and day > d(p["entry_date"]):
            p["funding_usd"] += p["size_usd"] * D.funding(p["symbol"], day)
        p["last_date"], p["last_close"] = day.isoformat(), b[2]
        if p["rule"] == "L" and b[1] >= L_LIQ * p["entry_price"]:
            close_pos(J, p, day, b[1], "цена выросла вдвое — ликвидация при 1×", liquidated=True); continue
        if p["rule"] == "L" and (day - d(p["entry_date"])).days >= L_HOLD:
            close_pos(J, p, day, b[2], f"{L_HOLD} дней прошло"); continue
        p["pnl_usd"] = price_pnl(p, b[2]) + p["funding_usd"]; keep.append(p)
    J.pos = keep
    # 2) правило A — по воскресному закрытию
    if day.weekday() == 6 and not J.stopped:
        for p in [p for p in J.pos if p["rule"] == "A"]:
            b = D.bar(p["symbol"], day); close_pos(J, p, day, b[2] if b else p["last_close"], "недельная смена набора")
        J.pos = [p for p in J.pos if p["rule"] != "A"]
        on, vs_ma, r50 = btc_trend(D, day)
        if on:
            ranked = []
            for s, rows in D.pool.items():
                rr = [x for x in rows if x[0] <= day]
                if len(rr) < 30 or rr[-1][0] != day: continue
                ranked.append((statistics.median(x[3] for x in rr[-30:]), s, rr))
            ranked.sort(reverse=True); cand = []
            for _, s, rr in ranked[:A_UNIVERSE]:
                prev = [x for x in rr if x[0] == day - timedelta(days=A_LOOK)]
                if prev: cand.append((rr[-1][2] / prev[0][2] - 1, s, rr[-1][2]))
            cand.sort(reverse=True)
            for r7, s, px in cand[:A_TOP]:
                open_pos(J, "A", s, "long", A_SIZE, day, px, f" (рост за 7 дней {100*r7:+.1f}%)")
        else:
            J.actions.append((day, f"Лидеры в тренде: BTC не в тренде ({vs_ma:+.1f}% к средней за 50 дней, {r50:+.1f}% за 50 дней) — набор не открываем"))
    # 3) правило L — новые листинги, вход по закрытию 8-го дня торгов
    if D.has_live and not J.stopped:
        open_l = {p["symbol"] for p in J.pos if p["rule"] == "L"}
        for s in sorted(D.listings, key=lambda z: D.listings[z]):
            if s in open_l or len(open_l) >= L_MAX: continue
            rr = [x for x in D.live.get(s, []) if x[0] <= day]
            if len(rr) != L_ENTRY_ROW + 1 or rr[-1][0] != day: continue
            liq = sum(x[3] for x in rr[1:L_ENTRY_ROW + 1]) / L_ENTRY_ROW
            if liq < L_MINLIQ: continue
            open_pos(J, "L", s, "short", L_SIZE, day, rr[-1][2], f" (оборот первой недели ${liq/1e6:.1f} млн/день)"); open_l.add(s)
    # 4) счёт и стоп
    unreal = sum(p["pnl_usd"] for p in J.pos)
    eq = START_EQUITY + J.realized + unreal; J.peak = max(J.peak, eq)
    if not J.stopped and eq <= J.peak * (1 - STOP_DD):
        for p in list(J.pos):
            b = D.bar(p["symbol"], day); close_pos(J, p, day, b[2] if b else p["last_close"], f"стоп счёта −{int(STOP_DD*100)}% от максимума")
        J.pos = []; J.stopped = True; unreal = 0.0; eq = START_EQUITY + J.realized
        J.actions.append((day, "СТОП: счёт упал на 20% от максимума — всё закрыто, новых сделок нет до решения владельца"))
    J.eq.append(dict(date=day.isoformat(), realized=round(J.realized, 4), unrealized=round(unreal, 4), equity=round(eq, 4), peak=round(J.peak, 4),
                     drawdown_pct=round(100 * (eq / J.peak - 1), 3), open_positions=len(J.pos), stopped=int(J.stopped)))

def signals_md(D, J, asof, days):
    L = [f"# Действия на утро {asof + timedelta(days=1):%d.%m.%Y} — по закрытию {asof:%d.%m.%Y} (UTC)", ""]
    upd = os.path.join(D.repo, "binance_live", "_updated.txt")
    live = open(upd).read().split("\n")[-2] if os.path.isfile(upd) else "нет папки binance_live/ — правило «против новых листингов» не считается"
    L += [f"Данные: последний закрытый день пула {D.last_day():%d.%m.%Y}; binance_live: {live}.", ""]
    if len(days) > 1: L += [f"Пропущенные дни обработаны: {days[0]:%d.%m}–{days[-1]:%d.%m}. Действия ниже — за все эти дни.", ""]
    L += ["## Сделать сегодня утром", ""]
    acts = [a for dd, a in J.actions]
    L += [f"- {a}" for a in acts] if acts else ["- Действий нет."]
    L += ["", "## Открытые позиции", "", "| Правило | Монета | Сторона | Ставка | Вход | Цена входа | Последнее закрытие | Итог сейчас |", "|---|---|---|---|---|---|---|---|"]
    for p in J.pos:
        L.append(f"| {RULE_NAME[p['rule']]} | {p['symbol']} | {'покупка' if p['side']=='long' else 'на падение'} | ${p['size_usd']:.0f} | {p['entry_date']} | {p['entry_price']:g} | {p['last_close']:g} | ${p['pnl_usd']:+.2f} |")
    if not J.pos: L.append("| — | — | — | — | — | — | — | — |")
    e = J.eq[-1]
    money = lambda x: f"{float(x):,.2f}".replace(",", " ")
    L += ["", "## Счёт", "", f"- Счёт: ${money(e['equity'])} (реализовано ${float(e['realized']):+.2f}, в открытых позициях ${float(e['unrealized']):+.2f})",
          f"- Максимум: ${money(e['peak'])}; просадка от максимума {float(e['drawdown_pct']):+.2f}% (стоп при −20%)",
          f"- Статус: {'СТОП — торговля остановлена' if J.stopped else 'работаем'}", ""]
    return "\n".join(L)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--repo", default="."); ap.add_argument("--asof"); ap.add_argument("--init", action="store_true"); ap.add_argument("--dry-run", action="store_true"); ap.add_argument("--no-seed", action="store_true", help="для проверок: начать без стартовых позиций")
    a = ap.parse_args(); D = Data(a.repo)
    asof = d(a.asof) if a.asof else D.last_day()
    if a.init:
        if a.no_seed: SEED.clear()
        init_journal(a.repo, asof); return
    if not os.path.isdir(os.path.join(a.repo, "journal")): sys.exit("нет journal/ — сначала запустить с --init")
    J = Journal(a.repo, a.dry_run)
    if J.last_date and asof <= J.last_date: print(f"день {asof} уже обработан (последний {J.last_date}) — изменений нет"); return
    start = (J.last_date + timedelta(days=1)) if J.last_date else asof
    days = [start + timedelta(days=i) for i in range((asof - start).days + 1)]
    for day in days: process_day(D, J, day)
    md = signals_md(D, J, asof, days)
    if a.dry_run: print(md); return
    write_csv(J.p("positions_open.csv"), POS_COLS, [{k: (round(v, 6) if isinstance(v, float) else v) for k, v in p.items()} for p in J.pos])
    write_csv(J.p("trades_closed.csv"), TR_COLS, J.trades); write_csv(J.p("equity.csv"), EQ_COLS, J.eq)
    os.makedirs(J.p("signals"), exist_ok=True)
    with open(J.p(f"signals/{asof + timedelta(days=1)}.md"), "w") as f: f.write(md)
    with open(J.p("signals/latest.md"), "w") as f: f.write(md)
    with open(J.p("_last_run.txt"), "w") as f: f.write(asof.isoformat() + "\n")
    print(md.split("## Открытые")[0])

if __name__ == "__main__": main()
