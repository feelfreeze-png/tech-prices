#!/usr/bin/env bash
# Разовая выгрузка истории всех бессрочных USDT-контрактов Binance (включая закрытые)
# из публичного архива data.binance.vision: дневные свечи + ставки финансирования.
# Запуск: bash src/binance_archive.sh --dry-run   (только подсчёт, ничего не пишет)
#         bash src/binance_archive.sh             (выгрузка в папку binance_um/)
# CACHE=/путь — держать скачанные zip между запусками, чтобы обрыв не начинал всё заново.
set -euo pipefail
export LIST="${LIST:-https://s3-ap-northeast-1.amazonaws.com/data.binance.vision}"
export BASE="${BASE:-https://data.binance.vision}"
OUT="${OUT:-binance_um}"; PAR="${PAR:-8}"; DRY=0
[ "${1:-}" = "--dry-run" ] && DRY=1
if [ -n "${CACHE:-}" ]; then export TMP="$CACHE"; mkdir -p "$TMP"
else export TMP; TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT; fi
mkdir -p "$TMP/k" "$TMP/f" "$TMP/dl"

# список «папок» (prefixes) или файлов (keys) по префиксу, с листанием страниц S3
s3ls() {
  local marker="" url page
  while :; do
    url="$LIST/?delimiter=/&prefix=$1"; [ -n "$marker" ] && url="$url&marker=$marker"
    page=$(curl -fsS --retry 3 --retry-delay 2 "$url") || return 1
    if [ "$2" = prefixes ]; then
      printf '%s' "$page" | grep -o '<Prefix>[^<]*</Prefix>' | sed 's/<[^>]*>//g' | grep -v "^$1\$" || true
    else
      printf '%s' "$page" | grep -o '<Key>[^<]*</Key>' | sed 's/<[^>]*>//g' || true
    fi
    printf '%s' "$page" | grep -q '<IsTruncated>true</IsTruncated>' || break
    marker=$(printf '%s' "$page" | grep -o '<NextMarker>[^<]*</NextMarker>' | sed 's/<[^>]*>//g' || true)
    [ -n "$marker" ] || break
  done
}
# файл со списком появляется только если листинг прошёл целиком: оборванную страницу
# (у S3 бывает «Connection reset by peer») переспрашиваем, а не берём обрезанный список
list_one() {
  local out
  if out=$(s3ls "data/futures/um/monthly/klines/$1/1d/" keys); then
    printf '%s\n' "$out" | grep '\.zip$' > "$TMP/k/$1.txt" || : > "$TMP/k/$1.txt"
  fi
  if out=$(s3ls "data/futures/um/monthly/fundingRate/$1/" keys); then
    printf '%s\n' "$out" | grep '\.zip$' > "$TMP/f/$1.txt" || : > "$TMP/f/$1.txt"
  fi
}
export -f s3ls list_one

echo "1/4 список контрактов…"
s3ls "data/futures/um/monthly/klines/" prefixes | sed 's#.*/klines/##; s#/$##' | grep -E '^[A-Z0-9]+USDT$' | sort -u > "$TMP/symbols.txt" || true
NS=$(wc -l < "$TMP/symbols.txt" | tr -d ' ')
[ "$NS" -gt 0 ] || { echo "Ошибка: архив не отдал список контрактов" >&2; exit 1; }
echo "   контрактов: $NS"

echo "2/4 список файлов по каждому контракту (параллельно $PAR)…"
xargs -P "$PAR" -n 1 bash -c 'list_one "$0"' < "$TMP/symbols.txt"
for pass in 1 2 3; do
  while read -r S; do [ -f "$TMP/k/$S.txt" ] && [ -f "$TMP/f/$S.txt" ] || echo "$S"; done < "$TMP/symbols.txt" > "$TMP/relist.txt"
  LEFT=$(wc -l < "$TMP/relist.txt" | tr -d ' '); [ "$LEFT" -gt 0 ] || break
  echo "   повтор листинга $pass: $LEFT контрактов"
  xargs -P "$PAR" -n 1 bash -c 'list_one "$0"' < "$TMP/relist.txt"
done
while read -r S; do [ -f "$TMP/k/$S.txt" ] || echo "   ВНИМАНИЕ: не получен список для $S"; done < "$TMP/symbols.txt"

# сводка: символ, первый и последний месяц, число месяцев свечей и ставок
LASTALL=$(cat "$TMP"/k/*.txt | sed -E 's/.*-([0-9]{4}-[0-9]{2})\.zip$/\1/' | sort | tail -n 1)
{ printf 'symbol,first_month,last_month,kline_months,funding_months,status\n'
  while read -r S; do
    NK=$(wc -l < "$TMP/k/$S.txt" | tr -d ' '); NF=$(wc -l < "$TMP/f/$S.txt" | tr -d ' ')
    [ "$NK" -gt 0 ] || continue
    F=$(head -n 1 "$TMP/k/$S.txt" | sed -E 's/.*-([0-9]{4}-[0-9]{2})\.zip$/\1/')
    L=$(tail -n 1 "$TMP/k/$S.txt" | sed -E 's/.*-([0-9]{4}-[0-9]{2})\.zip$/\1/')
    ST=active; [ "$L" \< "$LASTALL" ] && ST=closed
    printf '%s,%s,%s,%s,%s,%s\n' "$S" "$F" "$L" "$NK" "$NF" "$ST"
  done < "$TMP/symbols.txt"; } > "$TMP/symbols.csv"
NK=$(cat "$TMP"/k/*.txt | wc -l | tr -d ' '); NF=$(cat "$TMP"/f/*.txt | wc -l | tr -d ' ')
NC=$(grep -c ',closed$' "$TMP/symbols.csv" || true); N20=$(awk -F, 'NR>1 && $2<="2021-12"' "$TMP/symbols.csv" | wc -l | tr -d ' ')
echo "   с историей свечей: $(($(wc -l < "$TMP/symbols.csv")-1)), из них закрытых: $NC, начавшихся до 2022 года: $N20"
echo "   файлов: свечи $NK, ставки $NF; последний полный месяц в архиве: $LASTALL"
echo "   примеры закрытых: $(grep ',closed$' "$TMP/symbols.csv" | cut -d, -f1,2,3 | head -n 8 | tr '\n' ' ')"
if [ "$DRY" = 1 ]; then echo "Проверка без выгрузки завершена — ничего не записано."; exit 0; fi

echo "3/4 скачивание $((NK+NF)) файлов (параллельно $PAR)…"
cat "$TMP"/k/*.txt "$TMP"/f/*.txt | sed "s#^#$BASE/#" > "$TMP/urls.txt"
# три круга: во втором и третьем качаем только то, чего не хватает после предыдущего
for round in 1 2 3; do
  awk -F/ '{print $NF"\t"$0}' "$TMP/urls.txt" | while IFS=$'\t' read -r name url; do
    [ -s "$TMP/dl/$name" ] || printf '%s\n' "$url"
  done > "$TMP/todo.txt"
  LEFT=$(wc -l < "$TMP/todo.txt" | tr -d ' ')
  [ "$LEFT" -gt 0 ] || break
  echo "   круг $round: осталось $LEFT"
  ( cd "$TMP/dl" && xargs -P "$PAR" -n 1 curl -fsS --retry 3 --retry-delay 2 -O < "$TMP/todo.txt" ) || true
done
GOT=$(ls "$TMP/dl" | wc -l | tr -d ' ')

echo "4/4 сборка CSV…"
mkdir -p "$OUT/klines_1d" "$OUT/funding"; : > "$OUT/_missing.txt"
while read -r S; do
  # в _missing.txt пишем не только «совсем нет», но и «скачалось меньше, чем в архиве»
  EK=$(wc -l < "$TMP/k/$S.txt" | tr -d ' '); GK=$(ls "$TMP/dl/$S-1d-"*.zip 2>/dev/null | wc -l | tr -d ' ')
  EF=$(wc -l < "$TMP/f/$S.txt" | tr -d ' '); GF=$(ls "$TMP/dl/$S-fundingRate-"*.zip 2>/dev/null | wc -l | tr -d ' ')
  if [ "$GK" -gt 0 ]; then
    { printf 'open_time_ms,open,high,low,close,volume,quote_volume\n'
      for z in "$TMP/dl/$S-1d-"*.zip; do unzip -p "$z"; done | tr -d '\r' | grep -E '^[0-9]' | cut -d, -f1-6,8; } > "$OUT/klines_1d/$S.csv"
    [ "$GK" -eq "$EK" ] || echo "$S klines $GK/$EK" >> "$OUT/_missing.txt"
  else echo "$S klines" >> "$OUT/_missing.txt"; fi
  if [ "$GF" -gt 0 ]; then
    { printf 'funding_time_ms,interval_hours,rate\n'
      for z in "$TMP/dl/$S-fundingRate-"*.zip; do unzip -p "$z"; done | tr -d '\r' | grep -E '^[0-9]'; } > "$OUT/funding/$S.csv"
    [ "$GF" -eq "$EF" ] || echo "$S funding $GF/$EF" >> "$OUT/_missing.txt"
  else echo "$S funding" >> "$OUT/_missing.txt"; fi
done < <(tail -n +2 "$TMP/symbols.csv" | cut -d, -f1)
cp "$TMP/symbols.csv" "$OUT/_symbols.csv"
date -u +%Y-%m-%dT%H:%M:%SZ > "$OUT/_updated.txt"
cat > "$OUT/README.md" << 'MD'
# binance_um — разовый архив бессрочных USDT-контрактов Binance

Источник: data.binance.vision (публичный архив Binance), месячные файлы, включая закрытые контракты.

- `klines_1d/<SYMBOL>.csv` — дневные свечи контракта: open_time_ms (UTC, мс), open, high, low, close, volume, quote_volume
- `funding/<SYMBOL>.csv` — ставки финансирования: funding_time_ms (UTC, мс), interval_hours, rate
- `_symbols.csv` — первый и последний месяц, число месяцев, статус active/closed
- `_missing.txt` — контракты без свечей или без ставок в архиве

Папка не обновляется; последний месяц — последний полный месяц на дату выгрузки (`_updated.txt`).
MD
echo "Готово: $GOT из $((NK+NF)) файлов, контрактов $(($(wc -l < "$OUT/_symbols.csv")-1)), пропуски — в $OUT/_missing.txt"
