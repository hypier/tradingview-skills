---
name: tradingview-quantitative
description: Use when current TradingView data must be retrieved through available MCP tools for quantitative market analysis, including screening, technical analysis, risk assessment, event analysis, market review, or multi-symbol comparisons.
---

# Quantitative Investment Analysis Expert

Use available TradingView MCP tools to retrieve current data, then apply the relevant quantitative workflow. For direct Console/RapidAPI integration, endpoint debugging, or requests without those MCP tools, use `tradingview-api-integration` instead.

**This skill only runs when hosted `tradingview_*` MCP tools are available.** If those tools are missing, stop and tell the user to connect MCP before analyzing.

- Console (required for this skill): add `https://mcp.tradingviewapi.com/mcp` with `"type": "http"` and sign in with Console. Install steps: https://www.tradingviewapi.com/mcp/. Older clients may use `"type": "streamable-http"`.
- RapidAPI / no Console login: `POST https://api.tradingviewapi.com/api/mcp/generate` with the API key, then paste `exampleConfig` (JWT). Local `npx -y @ivotoby/openapi-mcp-server` exposes REST-shaped tools, not `tradingview_*` — switch to `tradingview-api-integration` instead of this skill.

## Core Rules

### Metadata First Principle

**Before calling `tradingview_get_leaderboard`, you must first call `tradingview_get_metadata` to get parameter values:**

1. `type='markets'` → Get `market_code` (required for stock leaderboard)
2. `type='tabs'` + `asset_type` → Get available `tab` values
3. `type='columnsets'` → Get available `columnset` values

Read [references/api-documentation.md](references/api-documentation.md) for the complete metadata dictionary (market codes, tabs, columnsets, and exchanges).

### Price Data Rule

- Real market prices, returns, stops, targets, backtests, and pattern levels: `tradingview_get_ohlcv` / `tradingview_get_ohlcv_batch` (Japanese candles only; never Heikin-Ashi)
- Synthetic chart styles: `tradingview_get_price` / `tradingview_get_price_batch` with `type='HeikinAshi'` or `Range`

### Parameter Names

- Leaderboard `columnset` is camelCase: `incomeStatement`, `balanceSheet`, `cashFlow`, `technicals`. Screener presets are snake_case: `income_statement`, `balance_sheet`, `cash_flow`, `technicals`.
- Tabs accept kebab-case or underscore (`all-stocks` / `all_stocks`).
- Calendar `from` / `to` are Unix seconds integers. Never pass `"now"` or `"now+14days"`. Max span 40 days: `from=Math.floor(Date.now()/1000)`, `to=from+14*86400`.
- Match `market_code` to the user request. English/US prompts default to `america`, `market_country='US'`, `lang='en'`. Use `china` only for A-shares.

### Rate Limits and Scan Size

Do not scan hundreds of symbols. Use leaderboard or screener first, then call quote / OHLCV / TA on the top 10–20. Pattern scans: at most 15 symbols (or analyze `AMEX:SPY` for S&P 500). On `rate_limit_exceeded`, wait and retry; do not fan out more calls.

### Tool Selection Quick Reference

| Need | Tool | Key Parameters |
|------|------|---------|
| Search instruments | `tradingview_search_market` | query, filter(stock/crypto/forex...) |
| Real-time quotes | `tradingview_get_quote` / `tradingview_get_quote_batch` | symbol, session |
| Standard OHLCV | `tradingview_get_ohlcv` / `tradingview_get_ohlcv_batch` | symbol, timeframe(1/5/15/30/60/240/D/W/M), range(max 500) |
| Chart-style candles | `tradingview_get_price` / `tradingview_get_price_batch` | same timeframes; `type='HeikinAshi'` or `Japanese` |
| Chart events | `tradingview_get_price_events` | symbol, timeframe(D), range — earnings/dividends/splits markers |
| Technical analysis | `tradingview_get_ta` | symbol, **include_indicators=true for detailed indicators** |
| Company fundamentals | `tradingview_get_market_data` | symbol, category(company/indicators/financials_quarterly/dividend/analyst_recommendations/forecast/overview/related_bonds/related_etfs...) |
| Leaderboard | `tradingview_get_leaderboard` | asset_type, tab, market_code, **columnset**(overview/performance/valuation/dividends/profitability/incomeStatement/balanceSheet/cashFlow/technicals) |
| Advanced screener | `tradingview_get_screener_presets` + `tradingview_get_screener_filter_options` + `tradingview_screen_assets` | asset type, preset fields (`income_statement` snake_case), filter operators, market |
| News | `tradingview_get_news` / `tradingview_get_news_detail` | market_country, lang(zh-Hans/en/ja), symbol |
| Community ideas | `tradingview_get_ideas_hot` / `tradingview_get_ideas_editors_picks` / `tradingview_get_ideas_by_symbol` / `tradingview_get_minds` / `tradingview_get_idea_detail` | symbol, lang, image_url |
| Economic calendar | `tradingview_get_calendar` | type(economic/earnings/revenue/ipo), from/to(**Unix seconds integers**, max 40 days), market |
| World economy | `tradingview_get_world_economy_indicators` | indicator slug, region |
| Metadata | `tradingview_get_metadata` / `tradingview_get_world_economy_indicator_metadata` | type(markets/tabs/columnsets/languages/exchanges/screener_filters/world_economy_indicators) |

## Workflows

Read the relevant workflow reference before performing a multi-step analysis:

### Core Analysis
- [deep-stock-analysis.md](references/deep-stock-analysis.md) - Deep individual stock analysis (quote + ohlcv multi-timeframe + ta + news + calendar + price events)
- [smart-screening.md](references/smart-screening.md) - Smart stock screening (leaderboard multi-columnset + ta + ohlcv)
- [fundamental-screening.md](references/fundamental-screening.md) - Fundamental screening (leaderboard valuation/profitability/dividends columnsets)
- [fundamental-data-dive.md](references/fundamental-data-dive.md) - Company fundamentals deep dive (`tradingview_get_market_data`)
- [pattern-recognition.md](references/pattern-recognition.md) - Technical pattern recognition (ohlcv + ta + pattern-library)
- [multi-timeframe-analysis.md](references/multi-timeframe-analysis.md) - Multi-timeframe trend confirmation (ohlcv D/W/M + ta)
- [advanced-screener.md](references/advanced-screener.md) - Advanced custom screener (`tradingview_screen_assets`)

### Market & Sectors
- [market-review.md](references/market-review.md) - Market review (leaderboard gainers/losers + news)
- [sector-rotation.md](references/sector-rotation.md) - Sector rotation analysis (leaderboard performance columnset)
- [news-briefing.md](references/news-briefing.md) - Financial news briefing (`tradingview_get_news` / `tradingview_get_news_detail`)
- [community-sentiment.md](references/community-sentiment.md) - Community sentiment (hot/editors-picks/minds/idea detail)
- [macro-dashboard.md](references/macro-dashboard.md) - Macro dashboard (world-economy indicators + economic calendar + macro news)

### Risk & Events
- [risk-assessment.md](references/risk-assessment.md) - Risk assessment (ohlcv history + quote + volatility)
- [event-analysis.md](references/event-analysis.md) - Event-driven analysis (calendar + news + `tradingview_get_price_events`)
- [calendar-tracking.md](references/calendar-tracking.md) - Calendar event tracking (calendar 4 types + chart event markers)

### Quotes & Search
- [symbol-search.md](references/symbol-search.md) - Instrument search (`tradingview_search_market`)
- [realtime-monitor.md](references/realtime-monitor.md) - Real-time quote monitoring (`tradingview_get_quote` / `tradingview_get_quote_batch`)
- [multi-symbol-analysis.md](references/multi-symbol-analysis.md) - Multi-instrument batch analysis (`tradingview_get_quote_batch` + `tradingview_get_ohlcv_batch` + `tradingview_get_ta`)
- [exchange-overview.md](references/exchange-overview.md) - Exchange overview (`tradingview_get_metadata`)

## Reference Knowledge Base

Read these references only when their subject is required:

- [api-documentation.md](references/api-documentation.md) - REST parameter dictionary (market codes/tabs/columnsets/exchanges). Live calls use `tradingview_*` MCP tools
- [mcp-tools-guide.md](references/mcp-tools-guide.md) - MCP tools usage guide (ohlcv vs price, metadata-first, screener/fundamentals/macro)
- [technical-analysis.md](references/technical-analysis.md) - Technical analysis methodology (search: `comprehensive scoring model`, `RSI`, `MACD`)
- [pattern-library.md](references/pattern-library.md) - Pattern recognition library (search: `double bottom`, `head and shoulders`, `triangle`)
- [risk-management.md](references/risk-management.md) - Risk management system (search: `Kelly formula`, `volatility`, `stop loss take profit`)
- [china-a-stock-examples.md](references/china-a-stock-examples.md) - China A-share practical cases
- [us-stock-examples.md](references/us-stock-examples.md) - US stock practical cases

## Disclaimer

The analysis and recommendations provided by this Skill are **for reference only** and do not constitute investment advice. Investing involves risks; decisions should be made cautiously.
