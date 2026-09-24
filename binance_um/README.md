# binance_um — разовый архив бессрочных USDT-контрактов Binance

Источник: data.binance.vision (публичный архив Binance), месячные файлы, включая закрытые контракты.

- `klines_1d/<SYMBOL>.csv` — дневные свечи контракта: open_time_ms (UTC, мс), open, high, low, close, volume, quote_volume
- `funding/<SYMBOL>.csv` — ставки финансирования: funding_time_ms (UTC, мс), interval_hours, rate
- `_symbols.csv` — первый и последний месяц, число месяцев, статус active/closed
- `_missing.txt` — контракты без свечей или без ставок в архиве

Папка не обновляется; последний месяц — последний полный месяц на дату выгрузки (`_updated.txt`).
