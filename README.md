# tech-prices

Дневные котировки (OHLCV) за 2 года по 18 тикерам с Yahoo Finance. Обновляются GitHub Actions по будням после закрытия рынка США (расписание 22:37 UTC и резервный запуск 23:37 UTC; GitHub может запускать с задержкой до нескольких часов).

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

Дневные котировки (OHLCV) за 2 года по 19 монетам с Yahoo Finance (`<COIN>-USD`). Обновляются с сервера: полный прогон в 00:15 UTC, дальше каждый час с 05:05 до 23:05 UTC идёт проверка — как только Yahoo заполнит вчерашний бар, файлы обновляются в течение часа. GitHub Actions оставлен запасным (00:41 и 17:41 UTC, с задержкой до нескольких часов).

Формат: `crypto/<COIN>.csv`, колонки те же. Последняя строка каждого файла — текущие сутки UTC, ещё не закрытые. В `crypto/_updated.txt` — число скачанных монет и время обновления, в `crypto/_missing.txt` — монеты, которые не скачались, и пустые бары строкой `BTC empty 2026-09-16`.

Вчерашний дневной бар Yahoo заполняет с опозданием: примерно до 10:00 UTC он пустой у всех монет. Закрытый вчерашний бар появляется после запуска в 11:41 UTC. Утром вчерашний день можно собрать из часовых баров (ниже), но цены там отличаются от дневного бара примерно на 0,05%, а объёмы не сходятся совсем.

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

## Крипта: полная история

Дневные бары за всю историю Yahoo: BTC и LTC — с 2014-09-17, большинство монет — с 2017-11-09. Обновляются дважды в сутки: 00:25 и 12:25 UTC.

Формат: `crypto_full/<COIN>.csv`, колонки те же. Последняя строка — текущие сутки UTC, ещё не закрытые.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/BTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ETH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ZEC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/DASH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ZEN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/DUSK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/LINK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/SOL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/XRP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ADA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/DOGE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/LTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/XMR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/AVAX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/DOT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ATOM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/BCH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/ETC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_full/FIL.csv

## Крипта: часовые бары

Часовые бары за последние 730 дней. Обновляются дважды в сутки: 00:25 и 12:25 UTC.

Формат: `crypto_1h/<COIN>.csv`, колонки `datetime_utc,open,high,low,close,volume` (начало часа, UTC). Последняя строка — текущий час, ещё не закрытый. Около 1% часов у Yahoo пустые (больше всего — ноябрь 2025): в таких строках цены не заполнены.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/BTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ETH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ZEC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/DASH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ZEN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/DUSK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/LINK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/SOL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/XRP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ADA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/DOGE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/LTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/XMR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/AVAX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/DOT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ATOM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/BCH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/ETC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_1h/FIL.csv

## Крипта: ставки финансирования

Ставки финансирования бессрочных контрактов Binance (`<COIN>USDT`) за 730 дней, все 19 монет. Обновляются ежедневно в 03:41 UTC с того же сервера: с серверов GitHub Binance не отвечает.

Формат: `crypto_funding/<COIN>.csv`, колонки `funding_time_utc,rate` — время выплаты в UTC и ставка за период. Шаг обычно 8 часов; у DUSK часть истории идёт с шагом 4 часа и 1 час. Время выгрузки — в `crypto_funding/_updated.txt`, монеты, которые не скачались, — в `crypto_funding/_missing.txt` (сейчас пусто).

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/BTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ETH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ZEC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/DASH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ZEN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/DUSK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/LINK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/SOL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/XRP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ADA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/DOGE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/LTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/XMR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/AVAX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/DOT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ATOM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/BCH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/ETC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding/FIL.csv

## Крипта: ставки финансирования за всю историю

Ставки финансирования Binance (`<COIN>USDT`) с начала торгов каждого контракта: BTC — с 2019-09-10, большинство монет — с начала 2020, SOL, AVAX, DOT, DOGE, FIL и ZEN — с середины или конца 2020, DUSK — с 2022-01-06. Выгружены один раз 2026-09-21 и не обновляются: свежие ставки идут в `crypto_funding/`.

Формат тот же, что в `crypto_funding/`: `funding_time_utc,rate`. Пропусков больше 8 часов нет ни у одной монеты. Шаг обычно 8 часов, но у SOL и DUSK местами 1–4 часа — такую ставку перед сравнением с 8-часовой нужно пересчитать на 8 часов.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/BTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ETH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ZEC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/DASH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ZEN.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/DUSK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/LINK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/SOL.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/XRP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ADA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/DOGE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/LTC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/XMR.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/AVAX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/DOT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ATOM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/BCH.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/ETC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/crypto_funding_full/FIL.csv

