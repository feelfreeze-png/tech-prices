# tech-prices

Дневные котировки (OHLCV) за 2 года по 18 тикерам с Yahoo Finance. Обновляются GitHub Actions по будням после закрытия рынка США (расписание 22:00 UTC, GitHub может запускать с задержкой).

Формат: `tech/<TICKER>.csv`, колонки `date,open,high,low,close,adjclose,volume`. Время последнего обновления — `tech/_updated.txt`.

## Прямые ссылки

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/NVDA MRVL ANET GEV VRT ETN AVGO TSM AMD MPWR ON PWR DELL VST ADI TXN MU SPY.csv
