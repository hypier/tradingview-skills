# Hosted TradingView MCP tools

25 `tradingview_*` tools on `https://mcp.tradingviewapi.com/mcp`. Same data as REST. Arguments use snake_case; REST paths use kebab-case.

Public install guide: https://www.tradingviewapi.com/mcp/. Client configs, OAuth, JWT, and RapidAPI local setup: `examples/10-mcp.md`.

All tools accept optional `response_format`: `json` (default) or `markdown`. List tools paginate with `limit` default 20, max 100, unless noted.

## When to use REST instead

No MCP tool for: `GET /api/symbols`, `/logo`, `POST /api/token/generate`, SSE, WebSocket, `/health`, news `sector` extra query keys, search `hl` / `exchange` / `sort_by_country` / `enable_grouping`, related-asset `start`/`count`, OHLCV `strictTo`.

Local `npx -y @ivotoby/openapi-mcp-server` is OpenAPI REST tools, not this table.

## Tool map

| Need | MCP tool | REST |
|------|----------|------|
| Search instruments | `tradingview_search_market` | `GET /api/search/market/{query}` |
| Metadata dictionaries | `tradingview_get_metadata` | `GET /api/metadata/*` and screener filter-options |
| News list | `tradingview_get_news` | `GET /api/news` or `/api/news/{market}` |
| News article | `tradingview_get_news_detail` | `GET /api/news/{newsId}` |
| Calendar | `tradingview_get_calendar` | `GET /api/calendar/{type}` |
| TA summary / indicators | `tradingview_get_ta` | `GET /api/ta/{symbol}` + optional `/indicators` |
| Leaderboard | `tradingview_get_leaderboard` | `GET /api/leaderboard/{asset}` or `/data` |
| Heikin-Ashi / Range candles | `tradingview_get_price` / `_batch` | `GET /api/price/{symbol}` / `POST /api/price/batch` |
| Chart event markers | `tradingview_get_price_events` | `GET /api/price/{symbol}/events` |
| Japanese OHLCV | `tradingview_get_ohlcv` / `_batch` | `GET /api/price/ohlcv/{symbol}` / `POST /api/price/ohlcv/batch` |
| Quote | `tradingview_get_quote` / `_batch` | `GET /api/quote/{symbol}` / `POST /api/quote/batch` |
| Fundamentals | `tradingview_get_market_data` | `GET /api/market-data/{symbol}/...` |
| Hot ideas | `tradingview_get_ideas_hot` | `GET /api/ideas/hot` |
| Editors' picks | `tradingview_get_ideas_editors_picks` | `GET /api/ideas/editors-picks` |
| Symbol ideas | `tradingview_get_ideas_by_symbol` | `GET /api/ideas/list/{symbol}` |
| Community minds | `tradingview_get_minds` | `GET /api/ideas/{symbol}/minds` |
| Idea detail | `tradingview_get_idea_detail` | `GET /api/ideas/{imageUrl}` |
| WE indicator list | `tradingview_get_world_economy_indicator_metadata` | `GET /api/metadata/world-economy/indicators` |
| WE rankings | `tradingview_get_world_economy_indicators` | `GET /api/world-economy/indicators/{slug}` |
| Screener scan | `tradingview_screen_assets` | `POST /api/screener/{asset}/scan` |
| Screener presets | `tradingview_get_screener_presets` | `GET /api/screener/presets` |
| Screener filters | `tradingview_get_screener_filter_options` | `GET /api/screener/filter-options` |

## Arguments that differ from REST

### Search — `tradingview_search_market`

`query` (max 200), `filter` (`stock`/`crypto`/`forex`/`futures`/`index`/`funds`/`bond`/`options`), `lang` (default `en`), `limit`/`offset`. No `hl`, `exchange`, `sort_by_country`, or `enable_grouping`.

### Metadata — `tradingview_get_metadata`

`type`: `markets`, `tabs`, `columnsets`, `languages`, `exchanges`, `screener_filters`, `world_economy_indicators`. For `tabs`, pass `asset_type` (`stocks`/`indices`/`crypto`/`futures`/`forex`/`bonds`/`corporate_bonds`/`etfs`). `screener_filters` also uses `lang`.

### Price vs OHLCV

- `tradingview_get_ohlcv` / `_batch`: Japanese candles only. Use for real prices, returns, stops, backtests. `timeframe` `1`/`5`/`15`/`30`/`60`/`240`/`D`/`W`/`M`, `range` max 500, `from`/`to` Unix seconds (`from` wins if both), `adjustment` `splits` (default) or `dividends`. Batch 1–10.
- `tradingview_get_price` / `_batch`: default chart type is **HeikinAshi**. Pass `type='Japanese'` only if you must use this tool for real OHLC; prefer `tradingview_get_ohlcv`. Also `HeikinAshi` and `Range`.
- `tradingview_get_price_events`: earnings/dividend/split markers. `timeframe` default `D`, `range` default 100, max 500.

### Quote

`session`: `regular` (default) / `extended` / `premarket` / `postmarket`. `fields` default `all`. Batch `symbols` 1–10.

### Market data — `tradingview_get_market_data`

`category` default `all`: `company`, `ipo`, `indicators`, `ttm`, `current`, `overview`, `financials_quarterly`, `financials_annual`, `history_quarterly`, `history_annual`, `dividend`, `analyst_recommendations`, `forecast`, `enterprise_value`, `credit_ratings`, `cash_flow`, `related_bonds`, `related_etfs`. MCP does not expose related `start`/`count` (REST defaults: bonds 24, ETFs 100, max 150).

### TA — `tradingview_get_ta`

`include_indicators=true` for RSI/MACD/etc. `interval` for the indicator slice: `1`/`5`/`15`/`60`/`120`/`240`/`1D`/`1W`/`1M` (aliases `1h`/`2h`/`4h`). Default interval for indicators is `1D`.

### Leaderboard — `tradingview_get_leaderboard`

`mode` `by_asset` (default) or `by_config`. For `by_asset`: `asset_type`, `tab`, `market_code` (required for stocks), `columnset`. `count` max 150. `columnset` is camelCase (`incomeStatement`, `balanceSheet`, `cashFlow`, `technicals`). Bonds / corporate bonds have no columnset. Fetch `tab` / `market_code` / `columnset` from metadata when unsure. Tabs accept kebab-case or underscore (`all-stocks` / `all_stocks`).

### Screener

`asset_type` `stock`/`crypto`/`etf`/`bond`/`cex`/`dex`. Scan `range` is `[start, endExclusive]`, page size ≤ 500. Stock `market` from metadata (default on REST if omitted is `china` / `zh` — always set `market` and `lang` explicitly). Preset ids are snake_case (`income_statement`, `balance_sheet`, `cash_flow`).

### Calendar — `tradingview_get_calendar`

`type` `economic`/`earnings`/`revenue`/`ipo`. `from`/`to` Unix **seconds** integers, span ≤ 40 days. Never `"now"`. `revenue` is the dividend calendar. `market` comma-separated; default `america` except economic.

### News

`lang` examples include `en`, `zh-Hans`, `ja`. REST metadata codes are `zh_CN` / `zh_TW`; both forms work for news. `market` `stock`/`crypto`/`forex`/`futures`/`bond`/`etf`/`index`/`economic`. No `sector` on MCP.

### Ideas

`tradingview_get_idea_detail` takes `image_url` from list results (e.g. `LfKFTY2N`). `tradingview_get_ideas_by_symbol` `per_page` max 100.

### World economy

`region`: `g20` (default), `world`, `north-america`, `europe`, `middle-east-africa`, `latin-america`, `asia-pacific`. Discover slugs with `tradingview_get_world_economy_indicator_metadata` (or metadata `type='world_economy_indicators'`).
