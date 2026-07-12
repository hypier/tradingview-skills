---
name: tradingview-quantitative
description: >
  Professional quantitative investment analysis system based on TradingView data.
  Provides intelligent stock screening, technical pattern recognition, market review,
  risk management, and event-driven analysis with multi-factor scoring and trading strategies.
---

# Quantitative Investment Analysis Expert

Professional quantitative investment analysis system based on TradingView MCP tools providing insights and decision recommendations.

## Core Rules

### Metadata First Principle

**Before calling `tradingview_get_leaderboard`, you must first call `tradingview_get_metadata` to get parameter values:**

1. `type='markets'` → Get `market_code` (required for stock leaderboard)
2. `type='tabs'` + `asset_type` → Get available `tab` values
3. `type='columnsets'` → Get available `columnset` values

Read [references/api-documentation.md](references/api-documentation.md) for the complete metadata dictionary (market codes, tabs, columnsets, and exchanges).

### Tool Selection Quick Reference

| Need | Tool | Key Parameters |
|------|------|---------|
| Search instruments | `search_market` | query, filter(stock/crypto/forex...) |
| Real-time quotes | `get_quote` / `get_quote_batch` | symbol, session |
| K-line data | `get_price` / `get_price_batch` | symbol, timeframe(1/5/15/30/60/240/D/W/M), range(max 500) |
| Technical analysis | `get_ta` | symbol, **include_indicators=true for detailed indicators** |
| Company fundamentals | `GET /api/market-data/{symbol}/...` | symbol, category(company/indicators/financials/dividend/analyst...) |
| Leaderboard | `get_leaderboard` | asset_type, tab, market_code, **columnset**(overview/performance/valuation/dividends/profitability/income_statement/balance_sheet/cash_flow/technical) |
| Advanced screener | `search_market` + `get_metadata` + REST screener flow | asset type, preset fields, filter operators, market |
| News | `get_news` / `get_news_detail` | market_country, lang(zh-Hans/en/ja), symbol |
| Community ideas | `GET /api/ideas/...` | hot/editors-picks/list/minds, symbol, lang |
| Economic calendar | `get_calendar` | type(economic/earnings/revenue/ipo), from/to(Unix seconds), market |
| World economy | `GET /api/world-economy/indicators/{slug}` | indicator slug, region |
| Metadata | `get_metadata` + `GET /api/metadata/world-economy/indicators` | type(markets/tabs/columnsets/languages/exchanges) and macro indicator slugs |

## Workflows

Read the relevant workflow reference before performing a multi-step analysis:

### Core Analysis
- [deep-stock-analysis.md](references/deep-stock-analysis.md) - Deep individual stock analysis (combine quote + price multi-timeframe + ta detailed indicators + news + calendar)
- [smart-screening.md](references/smart-screening.md) - Smart stock screening (leaderboard multi-columnset + ta + price)
- [fundamental-screening.md](references/fundamental-screening.md) - Fundamental screening (leaderboard valuation/profitability/dividends columnsets)
- [fundamental-data-dive.md](references/fundamental-data-dive.md) - Company fundamentals deep dive (market-data company + indicators + financials + dividends + analysts)
- [pattern-recognition.md](references/pattern-recognition.md) - Technical pattern recognition (price + ta + pattern-library reference)
- [multi-timeframe-analysis.md](references/multi-timeframe-analysis.md) - Multi-timeframe trend confirmation (price D/W/M + ta multi-period)
- [advanced-screener.md](references/advanced-screener.md) - Advanced custom screener workflow (presets + filter-options + scan payload design)

### Market & Sectors
- [market-review.md](references/market-review.md) - Market review (leaderboard gainers/losers + news)
- [sector-rotation.md](references/sector-rotation.md) - Sector rotation analysis (leaderboard performance columnset + multi-sector comparison)
- [news-briefing.md](references/news-briefing.md) - Financial news briefing (news + news_detail, supports multi-country multi-language)
- [community-sentiment.md](references/community-sentiment.md) - Community sentiment and idea tracking (hot ideas + symbol minds + idea detail)
- [macro-dashboard.md](references/macro-dashboard.md) - Macro dashboard (world-economy indicators + economic calendar + macro news)

### Risk & Events
- [risk-assessment.md](references/risk-assessment.md) - Risk assessment (price historical data + quote + volatility calculation)
- [event-analysis.md](references/event-analysis.md) - Event-driven analysis (calendar + news + search)
- [calendar-tracking.md](references/calendar-tracking.md) - Calendar event tracking (calendar 4 types)

### Quotes & Search
- [symbol-search.md](references/symbol-search.md) - Instrument search (search_market)
- [realtime-monitor.md](references/realtime-monitor.md) - Real-time quote monitoring (quote / quote_batch)
- [multi-symbol-analysis.md](references/multi-symbol-analysis.md) - Multi-instrument batch analysis (quote_batch + price_batch + ta)
- [exchange-overview.md](references/exchange-overview.md) - Exchange overview (metadata exchanges/markets/tabs)

## Reference Knowledge Base

Read these references only when their subject is required:

- [api-documentation.md](references/api-documentation.md) - Complete TradingView API documentation (endpoints, parameters, metadata dictionary: market codes/tabs/columnsets/exchanges, search keywords: `Market Codes`, `Asset Types and Tabs`, `Column Sets`, `Supported Languages`)
- [mcp-tools-guide.md](references/mcp-tools-guide.md) - MCP tools usage guide (tool combination patterns, metadata-first rules, screener/fundamentals/macro best practices)
- [technical-analysis.md](references/technical-analysis.md) - Technical analysis methodology (comprehensive scoring model, trend/momentum/pattern/support-resistance scoring, search keywords: `comprehensive scoring model`, `RSI`, `MACD`, `support resistance`)
- [pattern-library.md](references/pattern-library.md) - Pattern recognition library (classic patterns, recognition algorithms, success rate statistics, search keywords: `double bottom`, `head and shoulders`, `triangle`, `flag`, `candlestick patterns`)
- [risk-management.md](references/risk-management.md) - Risk management system (position management, stop-loss strategies, portfolio management, search keywords: `Kelly formula`, `volatility`, `stop loss take profit`, `batch position building`)
- [china-a-stock-examples.md](references/china-a-stock-examples.md) - China A-share practical cases (stock screening, pattern analysis, market review output examples)

## Disclaimer

The analysis and recommendations provided by this Skill are **for reference only** and do not constitute investment advice. Investing involves risks; decisions should be made cautiously.
