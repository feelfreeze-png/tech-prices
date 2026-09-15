# tech-prices

Дневные котировки (OHLCV) за 2 года по 18 тикерам с Yahoo Finance. Обновляются GitHub Actions по будням после закрытия рынка США (расписание 22:00 UTC, GitHub может запускать с задержкой).

Формат: `tech/<TICKER>.csv`, колонки `date,open,high,low,close,adjclose,volume`. Время последнего обновления — `tech/_updated.txt`.

## Прямые ссылки

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/NVDA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/MRVL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/ANET.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/GEV.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/VRT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/ETN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/AVGO.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/TSM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/AMD.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/MPWR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/ON.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/PWR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/DELL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/VST.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/ADI.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/TXN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/MU.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/tech/SPY.csv

## Крипта

Дневные котировки (OHLCV) за 2 года по 19 монетам с Yahoo Finance (`<COIN>-USD`). Обновляются каждый день (расписание 00:30 UTC, GitHub может запускать с задержкой).

Формат: `crypto/<COIN>.csv`, колонки те же. Последняя строка каждого файла — текущие сутки UTC, ещё не закрытые. В `crypto/_updated.txt` — число скачанных монет и время обновления, в `crypto/_missing.txt` — монеты, которые не скачались.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/BTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ETH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ZEC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/DASH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ZEN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/DUSK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/LINK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/SOL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/XRP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ADA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/DOGE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/LTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/XMR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/AVAX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/DOT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ATOM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/BCH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/ETC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto/FIL.csv
