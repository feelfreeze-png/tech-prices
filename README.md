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

## Рынки помимо крипты и акций

89 рынков с Yahoo Finance: индексы стран и секторы США, облигации, сырьё (фьючерсы, фонды и добытчики — металлы, энергия, зерно, скот, уран, литий, редкие земли, сталь, углеродные квоты), процентные фьючерсы, валюты, VIX. Кремния на бирже вне Китая нет, поэтому вместо него — производители Ferroglobe (GSM) и Daqo (DQ). Полная история дневных баров: SPY с 1993 года, ^VIX с 1990, индекс доллара с 1971, фьючерсы примерно с 2000, валюты примерно с 2003. Обновляются по будням в 22:47 и 23:47 UTC, после закрытия рынка США; GitHub может запускать с задержкой.

Формат: `macro/<ТИКЕР>.csv`, колонки `date,open,high,low,close,adjclose,volume`. В имени файла `=` заменён на `_`, `^` убран: `CL=F` → `CL_F.csv`, `EURUSD=X` → `EURUSD_X.csv`, `^VIX` → `VIX.csv`. Дата — дата торговой сессии по времени биржи. Если запустить выгрузку среди дня, последняя строка — незакрытая сессия. В старых данных встречаются строки без цен (у индекса доллара их много в 1970–80-х, у VIX — в 1990-х).

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/_missing.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/AUDUSD_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/BZ_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/CL_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/DBA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/DBC.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/DIA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/DX-Y.NYB.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EEM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EFA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ES_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EURUSD_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWA.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWG.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWJ.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWU.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWY.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/EWZ.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/FXI.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/GBPUSD_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/GC_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/GLD.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/HG_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/HYG.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/IEF.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/IWM.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/KC_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/LQD.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/NG_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/NQ_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/PL_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/QQQ.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/SB_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/SHY.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/SI_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/SLV.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/SPY.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/TIP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/TLT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/UNG.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/USDCAD_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/USDCHF_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/USDJPY_X.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/USO.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/VIX.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLB.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLE.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLF.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLI.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLK.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLP.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLU.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLV.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/XLY.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ZB_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ZC_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ZN_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ZS_F.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/macro/ZW_F.csv


## Binance: свечи, ставки, открытый интерес, лонги/шорты

Данные Binance по пулу из 99 монет: всё, что есть на Binance, выгружается автоматически. Список, что есть на споте, что на фьючерсах и чего нет, — в `_meta/binance_pool.md`. Обновляются ежедневно в 04:30 UTC с того же сервера. **Только закрытые данные:** последняя строка дневного файла — вчерашний день UTC, часового — 23:00 UTC вчера; незакрытые сутки и час не пишутся никогда. Повторный запуск в тот же день файлы не меняет.

Имена файлов — символ Binance: `BTCUSDT.csv`. Переименованные монеты записаны под новым тикером: FTM → `SUSDT` (Sonic), MKR → `SKYUSDT`, EOS → `AUSDT` (Vaulta); история у них начинается с переименования. XMR на споте Binance нет — свечи `XMRUSDT` взяты с фьючерсов. У SHIB фьючерс `1000SHIBUSDT`: ставки, OI и long/short лежат под этим именем. Числа — ровно как их отдаёт Binance, без округления.

- `binance_1d/<SYMBOL>.csv` — дневные свечи за всю историю с листинга. Колонки `open_time_utc,open,high,low,close,volume,quote_volume,trades,taker_buy_base,taker_buy_quote`; `quote_volume` — объём в USDT, `taker_buy_quote` — объём агрессивных покупок в USDT. Сутки открываются в 00:00 UTC.
- `binance_1h/<SYMBOL>.csv` — часовые свечи за скользящие 120 дней, те же колонки, `open_time_utc` вида `2026-09-22T23:00Z` (начало часа).
- `binance_funding/<SYMBOL>.csv` — ставки финансирования с начала контракта, `funding_time_utc,funding_rate,mark_price`. Шаг у разных контрактов разный (8, 4 или 1 час) и сохранён как есть; ставку за период перед сравнением нужно пересчитать на один шаг. У старых выплат `mark_price` пустой — Binance его не отдаёт.
- `binance_oi/<SYMBOL>.csv` — открытый интерес, `date_utc,sum_open_interest,sum_open_interest_value` (в монетах и в USDT). Binance хранит только ~30 дней, поэтому история копится с 2026-09-24.
- `binance_ls/<SYMBOL>.csv` — соотношение аккаунтов в лонгах и шортах, `date_utc,long_short_ratio,long_account,short_account`, тоже копится с 2026-09-24.
- В `binance_oi/` и `binance_ls/` строка — **снимок на 00:00 UTC даты `date_utc`**, то есть на закрытие предыдущих суток: строка `2026-09-24` описывает конец дня 2026-09-23.
- Монеты только со спота (сейчас DCR, SC, DGB, GLMR) — без файлов ставок, OI и long/short.

Для утреннего скана — одним запросом:

- `_meta/binance_latest.csv` — срез на последний закрытый день по всем символам: `symbol,date_utc,close,prev_close,change_pct,quote_volume,quote_volume_30d_median,funding_rate_last,open_interest,long_short_ratio`. `change_pct` — изменение close к предыдущему соседнему дню в процентах; если между днями пропуск, поле пустое. `quote_volume_30d_median` — медиана дневного объёма в USDT за последние 30 закрытых дней. `open_interest` — в USDT, снимок на 00:00 UTC сегодня (конец дня `date_utc`). Для монет только со спота последние три поля пустые.
- `_meta/binance_updated.txt` — время последнего обновления, число символов и последний закрытый день BTC.
- `_meta/binance_status.json` — по каждому символу: последний закрытый день, число строк, пропуски (`gaps`), есть ли спот и фьючерсы, `status` (`ok`, `gaps`, `absent` — нет на Binance, `error`).
- `_meta/logs/binance.log` — строка на каждое обновление.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/_meta/binance_updated.txt
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/_meta/binance_latest.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/_meta/binance_status.json
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/_meta/binance_pool.md
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_1d/BTCUSDT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_1h/BTCUSDT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_funding/BTCUSDT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_oi/BTCUSDT.csv
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_ls/BTCUSDT.csv

Для других монет — тот же адрес с другим символом из `binance_latest.csv`.

## Binance: архив всех бессрочных контрактов, включая закрытые

Разовая выгрузка из публичного архива `data.binance.vision`: **860 контрактов** USDT-перпетуалов, которые когда-либо торговались, из них 31 закрыт (LUNAUSDT заканчивается 2022-05). Нужна, чтобы проверять правила без ошибки выжившего: монеты, умершие при отрицательных ставках, здесь есть. Выгружено 2026-09-24, не обновляется.

Месячный архив Binance начинается с 2020-01, поэтому сентября–декабря 2019 в нём нет (ставки за те месяцы есть в `crypto_funding_full/`). У 130 контрактов месяцев ставок меньше, чем месяцев свечей — это пропуски самого архива.

Файлы по образцу: `https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/klines_1d/<SYMBOL>.csv` и `https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/funding/<SYMBOL>.csv`, где `<SYMBOL>` — из первой колонки `_symbols.csv`. Колонки свечей: `open_time_ms,open,high,low,close,volume,quote_volume` (время UTC в миллисекундах). Колонки ставок: `funding_time_ms,interval_hours,rate` — ставка за свой интервал, шаг 1, 4 или 8 часов, для суточной суммы складываются.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/_symbols.csv — список контрактов: первый и последний месяц, число месяцев, статус active или closed
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/_missing.txt — контракты, у которых чего-то не хватает (сейчас пусто)
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/_updated.txt — время выгрузки
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/README.md — описание папки
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/klines_1d/BTCUSDT.csv — пример: свечи с 2020-01
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/funding/BTCUSDT.csv — пример: ставки с 2020-01
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/klines_1d/LUNAUSDT.csv — пример закрытого контракта
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/binance_um/funding/LUNAUSDT.csv — пример закрытого контракта

## Акции: S&P 500 и техноветка

505 тикеров: весь текущий состав S&P 500, 17 компаний техноветки (MRVL и TSM в индекс не входят) и SPY. Дневные бары за 10 лет, цены округлены до 4 знаков. Обновляются по будням в 22:57 и 23:57 UTC, плюс перезапуск в 10:57 UTC — на случай, когда Yahoo отдаёт закрытие дня пустым.

Формат: `stocks/<ТИКЕР>.csv`, колонки `date,open,high,low,close,adjclose,volume`. Точка в тикере заменена на дефис, как у Yahoo: `BRK.B` → `BRK-B.csv`. Файлов много, поэтому ссылки не перечислены: адрес собирается по образцу `https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/<ТИКЕР>.csv`, а полный список тикеров — в `_tickers.txt`.

- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/_tickers.txt — список всех 505 тикеров, по одному на строку
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/_updated.txt — сколько скачалось и когда
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/_missing.txt — тикеры, которые не скачались
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/SPY.csv — пример: эталонный индексный фонд
- https://raw.githubusercontent.com/feelfreeze-png/tech-prices/main/stocks/AAPL.csv — пример: компания из индекса

