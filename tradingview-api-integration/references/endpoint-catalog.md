# TradingView Data API — Endpoint Catalog

Complete reference of every endpoint: parameters, defaults, enums, and where parameter values come from.

- Base URL: `https://tradingview-data1.p.rapidapi.com`
- Auth headers (all requests): `x-rapidapi-host: tradingview-data1.p.rapidapi.com` and `x-rapidapi-key: <KEY>`
- Response envelope (most endpoints): `{ "success": true|false, "data": ..., "msg": "Success" }`

## Table of Contents

1. [Conventions (symbol format, enums, metadata cross-reference)](#conventions)
2. [Price Data `/api/price`](#1-price-data)
3. [Real-time Quote `/api/quote`](#2-real-time-quote)
4. [Market Data (fundamentals) `/api/market-data`](#3-market-data)
5. [Market Search `/api/search`](#4-market-search)
6. [Technical Analysis `/api/ta`](#5-technical-analysis)
7. [News `/api/news`](#6-news)
8. [Community Ideas `/api/ideas`](#7-community-ideas)
9. [Leaderboards `/api/leaderboard`](#8-leaderboards)
10. [Screener `/api/screener`](#9-screener)
11. [Metadata `/api/metadata`](#10-metadata)
12. [World Economy `/api/world-economy`](#11-world-economy)
13. [Economic Calendar `/api/calendar`](#12-economic-calendar)
14. [Logo Proxy `/logo`](#13-logo-proxy)
15. [Token & MCP](#14-token--mcp)
16. [Realtime: SSE & WebSocket](#15-realtime-sse--websocket)

---

## Conventions

### Symbol format

- Standard: `EXCHANGE:TICKER` — e.g. `NASDAQ:AAPL`, `BINANCE:BTCUSDT`, `HKEX:9988`, `ECONOMICS:USGDP`
- The server also accepts `EXCHANGE-TICKER` (first `-` is converted to `:`), useful when `:` is awkward in URLs
- Find valid symbols with `GET /api/search/market/{query}`

### Common enums

| Name | Values |
|------|--------|
| `timeframe` / `interval` | `1`, `5`, `15`, `30`, `60`, `240`, `D`, `W`, `M` (minutes / Day / Week / Month) |
| chart `type` | `HeikinAshi`, `Range` (optional) |
| quote `session` | `regular` (default), `extended`, `premarket`, `postmarket` |
| search `filter` | `stock`, `crypto`, `forex`, `futures`, `index`, `funds`, `bond`, `options` (empty = all) |
| world-economy `region` | `g20` (default), `world`, `north-america`, `europe`, `middle-east-africa`, `latin-america`, `asia-pacific` |
| screener `asset_type` | `stock`, `crypto`, `etf`, `bond`, `cex`, `dex` |
| `lang` | 19 codes: `en`, `zh_CN`, `zh_TW`, `de`, `fr`, `es`, `it`, `pl`, `tr`, `ru`, `pt`, `id`, `ms`, `th`, `vi`, `ja`, `ko`, `ar`, `he` |

### Metadata cross-reference (where parameter values come from)

| Parameter | Used by | Source endpoint |
|-----------|---------|-----------------|
| `market` / `market_code` | leaderboard (stocks), calendar, screener (stock) | `GET /api/metadata/markets` |
| `tab` | leaderboard | `GET /api/metadata/tabs?type=<assetType>` (use `path` short id or full `id`) |
| `columnset` | leaderboard | `GET /api/metadata/columnsets` |
| `lang` | news, ideas, leaderboard, screener, calendar | `GET /api/metadata/languages` |
| `exchange` (filter value) | screener filters | `GET /api/metadata/exchanges` |
| `indicator` (slug) | world-economy | `GET /api/metadata/world-economy/indicators` |
| `preset_fields` | screener scan | `GET /api/screener/presets?asset_type=<type>` |
| filter field ids & enum values | screener scan | `GET /api/screener/filter-options?asset_type=<type>&lang=<lang>` |
| `id` | `GET /api/leaderboard/data` | `id` from `GET /api/metadata/tabs` (e.g. `stocks_market_movers.gainers`) |

> Note: metadata `/tabs` uses `currencies` as the type for forex; the leaderboard route is `/forex`.

---

## 1. Price Data

Examples: `examples/01-price-data.md`

### `GET /api/price/{symbol}`

Historical candlesticks (OHLCV) for one symbol.

| Param | In | Required | Default | Notes |
|-------|----|----------|---------|-------|
| `symbol` | path | yes | — | `EXCHANGE:TICKER` |
| `timeframe` | query | no | `5` | see timeframe enum |
| `range` | query | no | `10` | number of candles; positive = into the past |
| `to` | query | no | — | Unix seconds; anchor for historical query |
| `type` | query | no | — | `HeikinAshi` or `Range` |
| `inputs` | query | no | — | JSON string of chart inputs |

### `POST /api/price/batch`

Up to 10 symbols per request.

```json
{ "requests": [ { "symbol": "BINANCE:BTCUSDT", "timeframe": "60", "range": 20 } ] }
```

Each item supports the same fields as the GET version (`symbol` required).

---

## 2. Real-time Quote

Examples: `examples/02-quote-data.md`

### `GET /api/quote/{symbol}`

Real-time quote with 100+ fields (price, change, volume, fundamentals snapshot).

| Param | Required | Default | Notes |
|-------|----------|---------|-------|
| `symbol` (path) | yes | — | |
| `session` | no | `regular` | `regular`/`extended`/`premarket`/`postmarket` |
| `fields` | no | `all` | `all` or comma-separated field names |

### `POST /api/quote/batch`

```json
{ "symbols": ["NASDAQ:AAPL", "NASDAQ:MSFT"], "session": "regular", "fields": "all" }
```

`symbols` required, max 10.

---

## 3. Market Data

Fundamentals split by category. Examples: `examples/12-market-data.md`

All endpoints take only the path `symbol` (no query params):

| Endpoint | Returns |
|----------|---------|
| `GET /api/market-data/{symbol}` | everything, categorized |
| `.../company` | company profile (sector, industry, employees, website) |
| `.../ipo` | IPO info |
| `.../indicators` | valuation/fundamental indicators (PE, PB, EPS...) |
| `.../ttm` | trailing-twelve-month metrics (`*_ttm`) |
| `.../current` | live price/volume (lp, ch, bid, ask...) |
| `.../financials-quarterly` | quarterly financials (`*_fq`) |
| `.../financials-annual` | annual financials (`*_fy`) |
| `.../history-quarterly` | quarterly history arrays (`*_fq_h`) |
| `.../history-annual` | annual history arrays (`*_fy_h`) |
| `.../dividend` | dividend data |
| `.../analyst-recommendations` | analyst ratings & price targets |
| `.../enterprise-value` | EV metrics |
| `.../credit-ratings` | credit ratings |
| `.../cash-flow` | cash flow analysis |

---

## 4. Market Search

Examples: `examples/03-market-search.md`

### `GET /api/search/market/{query}`

| Param | Required | Default | Notes |
|-------|----------|---------|-------|
| `query` (path) | yes | — | keyword or `EXCHANGE:TICKER` |
| `filter` | no | all types | `stock`, `crypto`, `forex`, `futures`, `index`, `funds`, `bond`, `options` |

Returns matching symbols with exchange, type, description, logo ids (usable with `/logo`).

---

## 5. Technical Analysis

Examples: `examples/04-technical-analysis.md`

### `GET /api/ta/{symbol}`

Multi-timeframe Buy/Sell/Neutral summary. Response keyed by timeframe: `1`, `5`, `15`, `60`, `240`, `1D`, `1W`, `1M`.

### `GET /api/ta/{symbol}/indicators`

Detailed indicator values (RSI, MACD, SMA/EMA, Stochastic, pivot points, etc.).

---

## 6. News

Examples: `examples/06-news.md`

Common query params for all list endpoints:

| Param | Required | Default | Notes |
|-------|----------|---------|-------|
| `symbol` | no | — | filter by `EXCHANGE:TICKER` |
| `lang` | no | `en` | from `/api/metadata/languages` |
| `market_country` | no | — | country code e.g. `US`, `CN` |

| Endpoint | Category |
|----------|----------|
| `GET /api/news` | general (optional `market` query) |
| `GET /api/news/stock` | stocks |
| `GET /api/news/crypto` | crypto |
| `GET /api/news/forex` | forex |
| `GET /api/news/futures` | futures |
| `GET /api/news/index` | indices |
| `GET /api/news/bond` | bonds |
| `GET /api/news/etf` | ETFs |
| `GET /api/news/economic` | macro/economic |

### `GET /api/news/{newsId}`

Full article detail. `newsId` comes from the `id` field of list results. Query: `lang` (default `en`).

---

## 7. Community Ideas

Examples: `examples/13-ideas.md`

| Endpoint | Params |
|----------|--------|
| `GET /api/ideas/hot` | `page` (default 1), `lang` (default `en`) |
| `GET /api/ideas/editors-picks` | `page`, `lang` |
| `GET /api/ideas/{symbol}/minds` | symbol in path, `lang` |
| `GET /api/ideas/list/{symbol}` | `page`, `per_page` (default 20), `lang` |
| `GET /api/ideas/{imageUrl}` | idea detail; `imageUrl` is the `image_url` id from list results (e.g. `LfKFTY2N`) |

---

## 8. Leaderboards

Examples: `examples/05-leaderboards.md`

### Common query parameters

| Param | Required | Default | Source |
|-------|----------|---------|--------|
| `tab` | yes | — | short path (e.g. `gainers`) or full id; see enums below or `GET /api/metadata/tabs?type=...` |
| `market_code` | stocks only: yes | — | `GET /api/metadata/markets` (e.g. `america`, `china`, `japan`) |
| `columnset` | no | `overview` | `GET /api/metadata/columnsets` |
| `start` | no | `0` | pagination offset |
| `count` | no | `20` | max 150 |
| `lang` | no | `en` | |

### Per-asset routes and tab enums

- `GET /api/leaderboard/stocks` — tabs: `all_stocks`, `gainers`, `losers`, `large_cap`, `small_cap`, `largest_employers`, `high_dividend`, `highest_net_income`, `highest_cash`, `highest_profit_per_employee`, `highest_revenue_per_employee`, `active`, `unusual_volume`, `most_volatile`, `high_beta`, `best_performing`, `highest_revenue`, `most_expensive`, `penny_stocks`, `overbought`, `oversold`, `ath`, `atl`, `52wk_high`, `52wk_low`. Columnsets: `overview`, `performance`, `valuation`, `dividends`, `profitability`, `incomeStatement`, `balanceSheet`, `cashFlow`, `technicals`.
- `GET /api/leaderboard/indices` — tabs: `all`, `major`, `us`, `snp`, `currency`, `americas`, `europe`, `asia`, `pacific`, `middle_east`, `africa`. Columnsets: `overview`, `performance`, `technicals`.
- `GET /api/leaderboard/crypto` — tabs: `all`, `highest_total_value_locked`, `defi`, `gainers`, `losers`, `large_cap`, `small_cap`, `most_traded`, `most_addresses_with_balance`, `most_addresses_active`, `most_transactions`, `highest_transaction_volume`, `lowest_supply`, `highest_supply`, `most_expensive`, `most_volatile`, `all_time_high`, `all_time_low`, `52_week_high`, `52_week_low`. Columnsets: `overview`, `performance`, `valuation`, `addresses`, `transactions`, `sentiment`, `technicals`.
- `GET /api/leaderboard/futures` — tabs: `all`, `agricultural`, `energy`, `currencies`, `metals`, `world_indices`, `interest_rates`. Columnsets: `overview`, `performance`, `technicals`.
- `GET /api/leaderboard/forex` — tabs: `all`, `major`, `minor`, `exotic`, `americas`, `europe`, `asia`, `pacific`, `middle_east`, `africa`. Columnsets: `overview`, `performance`, `technicals`.
- `GET /api/leaderboard/bonds` — tabs: `all`, `all_10_year`, `major`, `americas`, `europe`, `asia`, `pacific`, `middle_east`, `africa`, `usa`, `uk`, `eu`, `germany`, `france`, `china`, `india`, `japan`. No columnset.
- `GET /api/leaderboard/corporate-bonds` — tabs: `highest_yield`, `long_term`, `short_term`, `floating_rate`, `fixed_coupon`, `zero_coupon`. No columnset.
- `GET /api/leaderboard/etfs` — tabs: `largest`, `highest_aum_growth`, `highest_returns`, `biggest_losers`, `equity`, `bitcoin`, `ethereum`, `gold`, `fixed_income`, `real_estate`, `total_market`, `commodities`, `asset_allocation`, `inverse_etfs`, `leveraged_etfs`, `most_traded`, `largest_inflows`, `largest_outflows`, `highest_discount`, `highest_premium`, `highest_yield`, `dividend`, `monthly_distributions`, `highest_diversification`, `actively_managed`, `sector_etfs`, `highest_beta`, `lowest_beta`, `negative_beta`, `highest_expense_ratio`, `all_time_high`, `all_time_low`, `52_week_high`, `52_week_low`, `usa`, `canada`, `uk`, `germany`, `japan`, `australia`. Columnsets: `overview`, `performance`, `extendedHours`, `fundFlows`, `dividends`, `navPerformance`, `holdings`, `risk`, `technicals`.

### `GET /api/leaderboard/data` (generic)

Use a full config `id` from `GET /api/metadata/tabs` (e.g. `stocks_market_movers.gainers`). Params: `id` (required), `market_code` (for stocks), `columnset`, `start`, `count`, `lang`.

---

## 9. Screener

Examples: `examples/16-screener.md`

### Helper endpoints (call these first)

- `GET /api/screener/presets?asset_type={stock|crypto|etf|bond|cex|dex}` — preset field groups. Stock preset ids: `overview`, `performance`, `extended_hours`, `valuation`, `dividends`, `profitability`, `income_statement`, `balance_sheet`, `cash_flow`, `per_share`, `technicals`.
- `GET /api/screener/filter-options?asset_type=...&lang=en[&id=field1,field2]` — filter field definitions, operations, and enum value dictionaries.

### Scan endpoints (POST, JSON body optional)

| Endpoint | asset_type | Default market | Default lang | Default sort |
|----------|------------|----------------|--------------|--------------|
| `POST /api/screener/scan` | stock | `china` | `zh` | `market_cap_basic` desc |
| `POST /api/screener/crypto/scan` | crypto | — | `zh` | `crypto_total_rank` asc |
| `POST /api/screener/etf/scan` | etf | `global` | `en` | `aum` desc |
| `POST /api/screener/bond/scan` | bond | `global` | `en` | `yield_to_maturity` desc |
| `POST /api/screener/cex/scan` | cex | — | `en` | `24h_vol_cmc` desc |
| `POST /api/screener/dex/scan` | dex | — | `en` | `dex_trading_volume_24h` desc |

### Scan body structure

```json
{
  "market": "america",
  "lang": "en",
  "range": [0, 50],
  "preset_fields": ["overview", "technicals"],
  "fields": ["change_abs", "Perf.1W"],
  "extra_fields": ["RSI", "SMA50"],
  "filters": {
    "market_cap_basic": { "operation": "greater_or_equal", "value": 10000000000 },
    "volume": { "operation": "greater_or_equal", "value": 1000000 },
    "technical_rating": ["Buy", "StrongBuy"],
    "exchange": ["NASDAQ"]
  },
  "sort": { "sortBy": "market_cap_basic", "sortOrder": "desc" }
}
```

| Field | Default | Notes |
|-------|---------|-------|
| `market` | per-route | stock only; values from `/api/metadata/markets` plus `global` |
| `range` | `[0, 100]` | `[start, endExclusive]`, max 500 per page |
| `preset_fields` | — | string or array, ids from `/presets` |
| `fields` / `extra_fields` | — | extra column ids |
| `filters` | `{}` | see syntax below |
| `sort` | per-route | `{ sortBy, sortOrder: "asc"|"desc" }` |

Filter value forms:

1. Array → multi-select / in-range (e.g. `"exchange": ["NASDAQ","NYSE"]`, `"technical_rating": ["Buy","StrongBuy"]`)
2. Object `{ "operation": "...", "value": ... }` — operations include `greater`, `less`, `greater_or_equal`, `less_or_equal`, `equal`, `in_range`
3. Scalar → equality

Field ids, valid operations, and enum values all come from `GET /api/screener/filter-options`.

Recommended flow: presets → filter-options → scan.

---

## 10. Metadata

All public. Examples: `examples/07-metadata.md`

| Endpoint | Returns |
|----------|---------|
| `GET /api/metadata/markets` | market codes (`america`, `china`, `japan`, ...) |
| `GET /api/metadata/tabs?type={stocks\|indices\|crypto\|futures\|currencies\|bonds\|corporate_bonds\|etfs\|all}` | leaderboard tab configs `{ id, path, url, title, type }` |
| `GET /api/metadata/columnsets` | columnset ids per asset type |
| `GET /api/metadata/languages` | 19 language codes |
| `GET /api/metadata/exchanges` | 350+ exchanges `{ name, value, group, country }` |
| `GET /api/metadata/world-economy/indicators[?category=gdp,...]` | indicator slugs + categories |

---

## 11. World Economy

Examples: `examples/14-world-economy.md`

### `GET /api/world-economy/indicators/{indicator}`

Country rankings for a macro indicator.

| Param | Required | Default | Source |
|-------|----------|---------|--------|
| `indicator` (path) | yes | — | slug from `/api/metadata/world-economy/indicators` (e.g. `gdp`, `inflation-rate`, `unemployment-rate`, `interest-rate`, `balance-of-trade`, `full-year-gdp-growth`) |
| `region` | no | `g20` | `g20`, `world`, `north-america`, `europe`, `middle-east-africa`, `latin-america`, `asia-pacific` |

---

## 12. Economic Calendar

Examples: `examples/08-calendar.md`

Time constraints for all: `from` / `to` are Unix **seconds**, `to > from`, and the window must be ≤ 40 days.

| Endpoint | Purpose | `market` param |
|----------|---------|----------------|
| `GET /api/calendar/economic?from=&to=[&market=]` | macro events (rates, CPI, NFP...) | optional, comma-separated market codes; default all |
| `GET /api/calendar/earnings?from=&to=[&market=]` | earnings calendar | default `america` |
| `GET /api/calendar/revenue?from=&to=[&market=]` | dividend calendar (named "revenue") | default `america` |
| `GET /api/calendar/ipo?from=&to=[&market=]` | IPO calendar | default `america` |

`market` values from `GET /api/metadata/markets`.

---

## 13. Logo Proxy

Public (no key required). Examples: `examples/09-logo.md`

- `GET /logo?url={logoPath}[&big=true]` — proxy a TradingView logo; auto-appends `.svg` when no extension
- `GET /logo/{path}` — same via path

Logo ids come from search results / quote fields (e.g. `logoid`, `currency-logoid`).

---

## 14. Token & MCP

Examples: `examples/15-token.md`, `examples/10-mcp.md`

### `POST /api/token/generate`

JWT for WebSocket/SSE connections. Body: `token-jwt-type` (`1`=30min, `2`=6h, `3`=24h; default 1), optional `userId`. Returns `token`, `wsUrl`, `sseUrl`.

### `POST /api/mcp/generate`

JWT for the MCP (Model Context Protocol) server. Body: `token-jwt-type` (`1`=30min, `2`=15d, `3`=30d, `4`=365d; required), optional `userId`. Returns `token`, `mcpUrl`, `exampleConfig`.

---

## 15. Realtime: SSE & WebSocket

Examples: `examples/11-websocket.md`

### SSE: `GET /sse/stream?symbols=SYM1,SYM2&type={quote|price}&token=<jwt>`

- Auth: JWT from `/api/token/generate` (as `?token=`) or API key headers
- `type=quote` (default): quote updates; `type=price`: 5-minute candle updates
- Events: `connected`, `quote_update`, `price_update`, `error`, heartbeat comments

### WebSocket: connect to the API host with auth headers or `?token=<jwt>`

Client → server messages (JSON `{ "action": ... }`):

| action | fields | purpose |
|--------|--------|---------|
| `ping` | — | heartbeat |
| `status` | — | list subscriptions |
| `subscribe` | `symbol`, `timeframe?` (default `5`), `range?`, `type?`, `inputs?`, `indicators?` | candle/indicator stream |
| `unsubscribe` | `id?` | cancel |
| `subscribe_quote` | `symbols` (≤10), `fields?` | quote stream |
| `unsubscribe_quote` | `id` | cancel |
| `subscribe_quote_fast` | `symbol` | fast quote |

Server → client `type` values: `connected`, `pong`, `status`, `subscribed`, `update`, `history`, `quote_subscribed`, `quote_update`, `quote_fast_update`, `unsubscribed`, `subscriptions_reset`, `error`.

Limits: ≤10 subscriptions per connection, ≤10 symbols per quote subscription, 100 msgs/min.
