# MCP Tools Usage Guide

> Metadata-first rules, tool combination patterns, best practices for various scenarios

---

## Metadata-First Rules

Before calling tools that require parameter values, first get available values through `tradingview_get_metadata`. For complete metadata dictionary, see `api-documentation.md` (search for `Market Codes`, `Asset Types and Tabs`).

### When to Call Metadata

| Scenario | Call Method | Parameters Obtained |
|----------|------------|-------------------|
| Query stock leaderboard | `tradingview_get_metadata(type='markets')` | market_code (e.g., america, china) |
| Query any leaderboard | `tradingview_get_metadata(type='tabs', asset_type='stocks')` | tab (e.g., gainers, losers) |
| Need non-overview data | `tradingview_get_metadata(type='columnsets')` | columnset (e.g., valuation, dividends) |
| Unsure about exchanges | `tradingview_get_metadata(type='exchanges')` | 353+ exchange list |
| Need valid languages | `tradingview_get_metadata(type='languages')` | lang values for news and ideas |
| Need macro indicator slugs | `tradingview_get_world_economy_indicator_metadata` or `tradingview_get_metadata(type='world_economy_indicators')` | world economy indicator ids |

### Common market_code Quick Reference

No need to call metadata every time, here are common values:

- **North America**: america, canada
- **Europe**: uk, germany, france, switzerland, spain, italy
- **Asia**: china, hong-kong, japan, korea, india, taiwan, singapore
- **Others**: australia, brazil

### Common columnset Quick Reference

| columnset | Data Included | Use Cases |
|-----------|--------------|-----------|
| overview | Price, change percentage, market cap, volume | Default overview |
| performance | 1W/1M/3M/6M/1Y/YTD returns | Performance comparison, sector rotation |
| valuation | PE, PB, PS, EV/EBITDA | Valuation screening |
| dividends | Dividend yield, payout ratio, ex-dividend date | High dividend strategy |
| profitability | ROE, ROA, gross margin, net margin | Profitability screening |
| income_statement | Revenue, net profit, EPS | Financial analysis |
| balance_sheet | Total assets, debt ratio, current ratio | Financial health |
| cash_flow | Operating/investing/financing cash flow | Cash flow analysis |
| technical | RSI, Beta, SMA, ATR | Technical overview |

---

## Tool Combination Patterns

### Pattern 1: Deep Individual Stock Analysis

```
1. tradingview_search_market(query="company name") → Get accurate symbol
2. tradingview_get_quote(symbol) → Real-time price, change, volume
3. tradingview_get_ohlcv(symbol, timeframe='D', range=120) → Real daily candles
4. tradingview_get_ta(symbol, include_indicators=true) → Detailed technical indicators
5. tradingview_get_news(symbol=symbol, lang='zh-Hans') → Related news
6. tradingview_get_calendar(type='earnings', from/to) → Upcoming earnings dates
7. tradingview_get_price_events(symbol, timeframe='D', range=120) → Earnings/dividend/split markers
```

### Pattern 2: Smart Stock Screening (Technical + Fundamental)

```
1. tradingview_get_metadata(type='markets') → Confirm market_code
2. tradingview_get_metadata(type='tabs', asset_type='stocks') → Confirm tab
3. tradingview_get_leaderboard(asset_type='stocks', tab='gainers', market_code, columnset='overview') → Candidate pool
4. tradingview_get_leaderboard(same, columnset='valuation') → Valuation data
5. tradingview_get_leaderboard(same, columnset='profitability') → Profitability data
6. For Top candidates: tradingview_get_ta(symbol, include_indicators=true) → Technical verification
7. For Top candidates: tradingview_get_ohlcv(symbol, timeframe='D', range=60) → K-line verification
```

### Pattern 3: Multi-Timeframe Trend Confirmation

```
1. tradingview_get_ohlcv(symbol, timeframe='M', range=24) → Monthly trend
2. tradingview_get_ohlcv(symbol, timeframe='W', range=52) → Weekly trend
3. tradingview_get_ohlcv(symbol, timeframe='D', range=120) → Daily trend
4. tradingview_get_ohlcv(symbol, timeframe='60', range=100) → 60-minute details
5. tradingview_get_ta(symbol, include_indicators=true) → Multi-period TA signals
```

Signal consistency: Monthly/weekly/daily trend direction consistent → High confidence

### Pattern 4: Sector Rotation Analysis

```
1. tradingview_get_metadata(type='tabs', asset_type='stocks') → Get all tabs
2. tradingview_get_leaderboard(tab='best-performing', columnset='performance') → Sector performance
3. Compare performance columnset data from different tabs
4. tradingview_get_news(market='stock', market_country='CN') → News confirm hotspots
```

### Pattern 5: Fundamental Screening

```
1. tradingview_get_leaderboard(tab='high-dividend', columnset='dividends') → High dividend
2. tradingview_get_leaderboard(tab='all-stocks', columnset='valuation') → Low valuation
3. tradingview_get_leaderboard(tab='all-stocks', columnset='profitability') → High ROE
4. Cross-filter above results → Value stock candidates
```

### Pattern 6: Market Review

```
1. tradingview_get_leaderboard(tab='gainers', market_code, count=50) → Gainers
2. tradingview_get_leaderboard(tab='losers', market_code, count=50) → Losers
3. tradingview_get_leaderboard(tab='active', market_code) → Active stocks
4. tradingview_get_leaderboard(tab='unusual-volume', market_code) → Unusual volume
5. tradingview_get_news(market_country='CN', lang='zh-Hans', limit=10) → News
6. For each news: tradingview_get_news_detail(news_id) → Full content
```

### Pattern 7: Fundamental Data Deep Dive

```
1. tradingview_search_market(query="company name") → Accurate symbol
2. tradingview_get_market_data(symbol, category='company') → Company profile
3. tradingview_get_market_data(symbol, category='indicators') → Valuation snapshot
4. tradingview_get_market_data(symbol, category='financials_quarterly') + financials_annual → Financial statements
5. tradingview_get_market_data(symbol, category='dividend') + analyst_recommendations → Capital return and expectations
6. tradingview_get_quote(symbol) + tradingview_get_ohlcv(symbol, timeframe='D', range=120) → Price context
```

### Pattern 8: Advanced Screener

```
1. tradingview_get_metadata(type='markets') → Confirm market
2. tradingview_get_screener_presets(asset_type='stock') → Select preset_fields
3. tradingview_get_screener_filter_options(asset_type='stock', lang='en') → Discover field ids and operations
4. tradingview_screen_assets(...) → Run custom scan
5. Top results: tradingview_get_quote + tradingview_get_ta → Secondary verification
```

### Pattern 9: Community Sentiment

```
1. tradingview_get_ideas_hot or tradingview_get_ideas_editors_picks → Broad discovery
2. tradingview_get_ideas_by_symbol(symbol) → Symbol-specific idea feed
3. tradingview_get_minds(symbol) → Community direction
4. tradingview_get_idea_detail(image_url) → Read representative idea details
5. tradingview_get_ta(symbol) + tradingview_get_ohlcv(symbol) → Compare narrative vs chart
```

### Pattern 10: Macro Dashboard

```
1. tradingview_get_world_economy_indicator_metadata → Confirm indicator slugs
2. tradingview_get_world_economy_indicators(indicator, region='g20') → Ranking data
3. tradingview_get_calendar(type='economic', from/to, market='america,china') → Upcoming macro events
4. tradingview_get_news(market='economic', lang='en') → Macro headlines
5. Summarize impact on equities, bonds, FX, and crypto
```

---

## Key Parameter Description

### tradingview_get_ohlcv vs tradingview_get_price

| Need | Tool |
|------|------|
| Real OHLC for returns, stops, targets, backtests, breakout levels | `tradingview_get_ohlcv` / `tradingview_get_ohlcv_batch` |
| Heikin-Ashi or Range chart visualization | `tradingview_get_price` / `tradingview_get_price_batch` with `type` |

`tradingview_get_ohlcv` always returns standard Japanese candles. Do not use `tradingview_get_price` for volatility or P&L math unless `type='Japanese'` is set.

### tradingview_get_price_events

Chart markers derived from earnings, dividends, and splits. Use with a symbol after calendar/news:

```
tradingview_get_price_events(symbol, timeframe='D', range=100)
```

Returns event type, label, time, candle index, and event-specific details when available.

### tradingview_get_ohlcv / tradingview_get_price Timeframe Selection

| timeframe | Meaning | Typical range | Use Cases |
|-----------|---------|--------------|-----------|
| 1 | 1 minute | 60-240 | Intraday trading |
| 5 | 5 minutes | 48-120 | Short-term analysis |
| 15 | 15 minutes | 48-96 | Short-term analysis |
| 60 | 1 hour | 48-168 | Swing analysis |
| 240 | 4 hours | 30-90 | Swing analysis |
| D | Daily | 60-250 | Medium-term analysis |
| W | Weekly | 52-104 | Medium-long term analysis |
| M | Monthly | 24-60 | Long-term trend |

### tradingview_get_price Chart Types

- `type='Japanese'`: Standard K-line
- `type='HeikinAshi'`: Heikin-Ashi, filters noise, clearer trend direction

### tradingview_get_ta include_indicators Return Fields

Key fields returned when setting `include_indicators=true`:

- **RSI(14)**: Relative Strength Index (>70 overbought, <30 oversold)
- **MACD**: Trend momentum (DIF, DEA, histogram)
- **Stoch**: Stochastic Oscillator (K, D values)
- **CCI(20)**: Commodity Channel Index
- **ADX(14)**: Trend Strength (>25 trending, >50 strong trend)
- **SMA/EMA**: Simple/Exponential Moving Average
- **Pivot Points**: Pivot points (support/resistance levels)

### tradingview_get_news Language Codes

| Market | lang | market_country |
|---------|------|----------------|
| China | zh-Hans | CN |
| United States | en | US |
| Japan | ja | JP |
| Hong Kong | zh-Hans or en | HK |
| South Korea | ko | KR |

### Symbol Format and Resolution

- Standard format is `EXCHANGE:TICKER`, such as `NASDAQ:AAPL`, `BINANCE:BTCUSDT`, `HKEX:9988`
- If the user gives a company name or shorthand, use `tradingview_search_market` first
- For macro indicators, symbols can also appear as `ECONOMICS:*`

### Fundamental Data Categories

Use `tradingview_get_market_data` with `category`:
- `company`
- `current`
- `indicators`
- `ttm`
- `financials_quarterly`
- `financials_annual`
- `history_quarterly`
- `history_annual`
- `dividend`
- `analyst_recommendations`
- `enterprise_value`
- `credit_ratings`
- `cash_flow`

### Screener Workflow Reminder

When using the screener, always follow this order:
1. pick `asset_type`
2. `tradingview_get_screener_presets`
3. `tradingview_get_screener_filter_options`
4. `tradingview_screen_assets`
5. verify top results with `tradingview_get_quote` / `tradingview_get_ta`

### tradingview_get_calendar Timestamps

Calendar queries require Unix timestamps (seconds), time span not exceeding 40 days:

```javascript
// Current time
const now = Math.floor(Date.now() / 1000);
// 7 days later
const weekLater = now + 7 * 24 * 60 * 60;
// 14 days later
const twoWeeksLater = now + 14 * 24 * 60 * 60;
```

---

## Multi-Asset Type Support

MCP supports 8 asset types, each with different tabs and columnsets:

| Asset Type | asset_type | Tabs Count | Columnsets | Requires market_code |
|------------|-----------|------------|------------|-------------------|
| Stocks | stocks | 25 | 9 types (including fundamentals) | Yes |
| Indices | indices | 11 | 3 types | No |
| Cryptocurrency | crypto | 20 | 3 types | No |
| Futures | futures | 7 | 2 types | No |
| Forex | forex | 10 | 3 types | No |
| Government Bonds | bonds | 17 | 2 types | No |
| Corporate Bonds | corporate_bonds | 6 | 1 type | No |
| ETF/Funds | etfs | 40 | 3 types | No |

### Crypto-Specific Tabs

DeFi, TVL ranking, address count, volume, supply, etc. → Use `tradingview_get_metadata(type='tabs', asset_type='crypto')` to see complete list.

### ETF-Specific Tabs

By strategy: bitcoin, gold, fixed-income, leveraged, inverse, sector, etc. 40 categories.

### Additional MCP Tool Families

- **Market Data**: `tradingview_get_market_data` — fundamentals, valuation, analyst expectations, financial statements
- **Ideas**: `tradingview_get_ideas_hot`, `tradingview_get_ideas_editors_picks`, `tradingview_get_ideas_by_symbol`, `tradingview_get_minds`, `tradingview_get_idea_detail`
- **World Economy**: `tradingview_get_world_economy_indicator_metadata`, `tradingview_get_world_economy_indicators`
- **Screener**: `tradingview_get_screener_presets`, `tradingview_get_screener_filter_options`, `tradingview_screen_assets`
- **Standard OHLCV**: `tradingview_get_ohlcv`, `tradingview_get_ohlcv_batch`
- **Chart events**: `tradingview_get_price_events`
