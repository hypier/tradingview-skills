# TradingView MCP Structured Data Reference

Workflow-facing index for the `equity-research-analyst` skill. **Live numeric data comes from hosted `tradingview_*` MCP tools.** Do not ask for an API key and do not construct REST curls. Use Web Search only for narrative content (MD&A, forward guidance, earnings call transcripts, segment breakdowns, risk factors).

## Quick Navigation

1. [Connect MCP](#connect-mcp)
2. [Tool map](#tool-map)
3. [Symbol Format](#symbol-format)
4. [Scenario A: Quarterly Earnings Analysis](#scenario-a-quarterly-earnings-analysis-earnings-analysis-earnings-preview)
5. [Scenario B: Initiation Report](#scenario-b-initiation-report-initiating-coverage)
6. [Scenario C: Catalyst Calendar](#scenario-c-catalyst-calendar-catalyst-calendar)
7. [Scenario D: Morning Note](#scenario-d-morning-note-morning-note)
8. [Scenario E: Screening / Idea Generation](#scenario-e-screening--idea-generation-idea-generation)
9. [Scenario F: Sector Overview](#scenario-f-sector-overview-sector-overview)
10. [Scenario G: Model Update](#scenario-g-model-update-model-update)
11. [Scenario H: Thesis Tracker](#scenario-h-thesis-tracker-thesis-tracker)
12. [Ticker Resolution](#ticker-resolution-generic-preflight)
13. [Citation Convention](#citation-convention)
14. [Fallback Strategy](#fallback-strategy)

## Use

This file maps research questions to hosted MCP tools and helps interpret returned fields. The MCP tool schema and returned payload are authoritative; this skill does not bundle REST or OpenAPI snapshots.

### Parameter discipline

- Match the tool family to the symbol family. Example: news with `market='crypto'` should use crypto symbols such as `BINANCE:BTCUSDT`, not stock tickers.
- For `tradingview_search_market`, set `filter` to the actual asset class (`stock`, `crypto`, `forex`, `futures`, `index`, `funds`, `bond`, `options`).
- For `tradingview_get_quote`, prefer `session='regular'` and `fields='all'` unless the workflow needs a different session.
- Calendar `from` / `to` are Unix-seconds **integers**. Never pass empty strings, `"now"`, or date labels.
- Leaderboard `columnset` is camelCase (`incomeStatement`, `balanceSheet`, `cashFlow`, `technicals`). Screener `preset_fields` stay snake_case (`income_statement`, `technicals`).
- Real prices and report charts: `tradingview_get_ohlcv`. Use `tradingview_get_price` only for Heikin-Ashi or Range.

### Common pitfalls

- Quote fields are nested under `data.data`, not flat at the top level.
- `tradingview_get_market_data(..., category='analyst_recommendations')` returns a single object at `data.analyst_recommendations`, not an array.
- Treat the request symbol or preflight search result as canonical. Do not rebuild the listing from `data.company.ticker` / `data.company.exchange`.
- Leaderboard does not filter by sector. Use `tradingview_screen_assets` after discovering sector enums.
- `NASDAQ:AAPL` sector is `Electronic Technology`, not `Technology`.

---

## Connect MCP

No API key is required when hosted MCP is connected.

- Console: add `https://mcp.tradingviewapi.com/mcp` with `"type": "http"` and sign in. Install: https://www.tradingviewapi.com/mcp/
- Older clients: `"type": "streamable-http"`.
- RapidAPI without Console: `POST https://api.tradingviewapi.com/api/mcp/generate` and paste `exampleConfig` (JWT).
- Local OpenAPI MCP (`npx -y @ivotoby/openapi-mcp-server`) is the wrong tool set. Use `tradingview-api-integration` instead of this skill.

If `tradingview_*` tools are missing, stop and tell the user to connect MCP. Do not fall back to curl.

---

## Tool map

| Need | Tool | Key arguments |
|---|---|---|
| Resolve a name to a ticker | `tradingview_search_market` | query, filter=`stock` |
| Company / financials / consensus | `tradingview_get_market_data` | symbol, category (`all`, `company`, `ipo`, `ttm`, `current`, `overview`, `indicators`, `financials_quarterly`, `financials_annual`, `history_quarterly`, `history_annual`, `dividend`, `analyst_recommendations`, `forecast`, `enterprise_value`, `credit_ratings`, `cash_flow`, `related_bonds`, `related_etfs`) |
| Live quote | `tradingview_get_quote` / `tradingview_get_quote_batch` | symbol, session=`regular`, fields=`all` |
| Real OHLCV for charts | `tradingview_get_ohlcv` | symbol, timeframe=`D`, range=252 |
| Technicals | `tradingview_get_ta` | symbol, include_indicators=`true` for RSI/MACD/MAs |
| Earnings / dividend / IPO / macro calendar | `tradingview_get_calendar` | type, from, to (Unix seconds integers, span ≤ 40 days), market |
| News | `tradingview_get_news` / `tradingview_get_news_detail` | market, market_country, lang, symbol |
| Ranked lists (gainers, high dividend) | `tradingview_get_leaderboard` | asset_type=`stocks`, tab, market_code, columnset |
| Sector / factor screens | `tradingview_get_screener_filter_options` then `tradingview_screen_assets` | asset_type=`stock`, market, filters, preset_fields |
| Community ideas | `tradingview_get_ideas_hot` / `tradingview_get_ideas_by_symbol` / `tradingview_get_minds` | lang=`en` |
| Macro series | `tradingview_get_world_economy_indicators` | indicator slug, region |
| Parameter dictionaries | `tradingview_get_metadata` | type=`markets` / `tabs` / `columnsets` / `languages` / `exchanges` / `screener_filters` |

Call `tradingview_get_metadata` before a leaderboard when you are unsure of `market_code`, `tab`, or `columnset`. Common US defaults: `market_code='america'`, `market_country='US'`, `lang='en'`.

---

## Symbol Format

All `{symbol}` parameters use `EXCHANGE:TICKER` format:

- Stocks: `NASDAQ:AAPL`, `NYSE:JPM`, `NASDAQ:TSLA`
- ETFs: `AMEX:SPY`, `NASDAQ:QQQ`
- Crypto: `BINANCE:BTCUSDT`
- Indices: `SP:SPX`, `NASDAQ:NDX`
- Forex: `FX:EURUSD`
- Futures: `CME_MINI:ES1!`

If the ticker is ambiguous, resolve it first via `tradingview_search_market(query, filter='stock')`.

Pick the `filter` that matches the asset class you are researching:

- Equities / ETFs for this skill's default workflows: `filter='stock'`
- Crypto pairs: `filter='crypto'`
- FX pairs: `filter='forex'`
- Futures: `filter='futures'`
- Indices: `filter='index'`

**Observed response shape:**

```
tradingview_search_market(query='NVIDIA', filter='stock')
```

Use `data.markets[]`, not `data[]`.

| Needed field | JSON path |
|---|---|
| First resolved symbol | `data.markets[0].id` |
| Short ticker | `data.markets[0].symbol` |
| Exchange | `data.markets[0].exchange` |
| Description | `data.markets[0].description` |

---

## Scenario A: Quarterly Earnings Analysis (`earnings-analysis`, `earnings-preview`)

### One-shot fetch (highest information density)

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
```

**Observed symbol / fiscal-label caveats:**

- Treat the request symbol (for example `NASDAQ:NVDA`) or the preflight search result as canonical.
- Do not rely on `data.company.ticker` or `data.company.exchange` as the canonical listing fields; they may be null or may show a quote venue such as `Cboe One`.
- Treat `data.current.fiscal_period_current` as a provider-side structured label. If it conflicts with the company's own IR / SEC quarter naming, use the latest primary-source quarter label in narrative output and keep the API label only as a structured-data citation detail.

Returns 5 blocks that populate the following report fields:

| Report field | JSON path |
|---|---|
| Company description | `data.company.business_description` |
| CEO | `data.company.ceo` |
| Employee count | `data.company.number_of_employees` |
| Sector / industry | `data.company.sector`, `data.company.industry` |
| Market cap | `data.indicators.market_cap_basic` |
| P/E TTM | `data.indicators.price_earnings` |
| 52-week high / low | `data.indicators.price_52_week_high`, `price_52_week_low` |
| Beta (1y / 3y / 5y) | `data.indicators.beta_1_year`, `beta_3_year`, `beta_5_year` |
| Latest earnings date | `data.indicators.earnings_release_date` (Unix seconds) |
| Next earnings date | `data.indicators.earnings_release_next_date` |
| **Past 8 earnings-release timestamps** | `data.indicators.earnings_release_date_h[]` |
| TTM revenue | `data.ttm.total_revenue_ttm` |
| **Past 8 quarters TTM revenue (for charts)** | `data.ttm.total_revenue_ttm_h[]` |
| TTM net income | `data.ttm.net_income_ttm` |
| **Past 8 quarters net income** | `data.ttm.net_income_ttm_h[]` |
| TTM EBITDA | `data.ttm.ebitda_ttm` |
| **Past 8 quarters EBITDA** | `data.ttm.ebitda_ttm_h[]` |
| TTM gross profit | `data.ttm.gross_profit_ttm`, `gross_profit_ttm_h[]` |
| TTM free cash flow | `data.ttm.free_cash_flow_ttm`, `free_cash_flow_ttm_h[]` |
| TTM diluted EPS | `data.ttm.earnings_per_share_diluted_ttm`, `earnings_per_share_diluted_ttm_h[]` |
| TTM gross margin | `data.ttm.gross_margin_ttm` |
| TTM operating margin | `data.ttm.operating_margin_ttm` |
| TTM net margin | `data.ttm.net_margin_ttm` |
| TTM EBITDA margin | `data.ttm.ebitda_margin_ttm` |
| TTM ROE | `data.ttm.return_on_common_equity_ttm` |
| TTM ROIC | `data.ttm.return_of_invested_capital_percent_ttm` |
| TTM R&D expense | `data.ttm.research_and_dev_ttm` |
| TTM capex | `data.ttm.capital_expenditures_ttm`, `capital_expenditures_unchanged_ttm_h[]` |
| Current fiscal period | `data.current.fiscal_period_current` (e.g. `"2026-Q1"`) |
| Current P/E, P/B, P/S | `data.current.price_earnings_current`, `price_book_current`, `price_sales_current` |
| Current EV | `data.current.enterprise_value_current` |
| Current EV/EBITDA | `data.current.enterprise_value_ebitda_current` |
| Current dividend yield | `data.current.dividends_yield_current` |
| Current D/E | `data.current.debt_to_equity_current` |
| Current-quarter EPS actual | `data.financials_quarterly.earnings_per_share_fq` |
| **Next-quarter EPS consensus** ⭐ | `data.financials_quarterly.earnings_per_share_forecast_next_fq` |

**Key insight**: The 8-element `*_ttm_h[]` arrays are the direct data source for earnings-analysis-required charts like "quarterly revenue progression", "quarterly EPS progression", and "quarterly margin trends".

### Beat / miss analysis

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='analyst_recommendations')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='financials_quarterly')
```

The analyst payload is a single object under `data.analyst_recommendations`, not an array.

| Needed field | JSON path |
|---|---|
| Recommendation score | `data.analyst_recommendations.recommendation_mark` |
| Total analysts | `data.analyst_recommendations.recommendation_total` |
| Buy / overweight / hold / underweight / sell | `data.analyst_recommendations.recommendation_buy`, `recommendation_over`, `recommendation_hold`, `recommendation_under`, `recommendation_sell` |
| Average / median / high / low target price | `data.analyst_recommendations.price_target_average`, `price_target_median`, `price_target_high`, `price_target_low` |
| Price-target snapshot date | `data.analyst_recommendations.price_target_date` |

### Price chart and technicals

```
tradingview_get_ohlcv(symbol='NASDAQ:AAPL', timeframe='D', range=252)
tradingview_get_quote(symbol='NASDAQ:AAPL', session='regular', fields='all')
tradingview_get_ta(symbol='NASDAQ:AAPL', include_indicators=true)
```

| Needed field | JSON path |
|---|---|
| Symbol | `data.symbol` |
| Last price | `data.data.lp` |
| Daily change | `data.data.ch` |
| Daily change % | `data.data.chp` |
| Volume | `data.data.volume` |
| Market cap | `data.data.market_cap_basic` |
| Session status | `data.data.current_session` |

---

## Scenario B: Initiation Report (`initiating-coverage`)

**Task 1 — Company Research:**

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='company')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='ipo')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='credit_ratings')
```

**Task 2 — Financial Modeling:**

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='financials_annual')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='history_annual')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='cash_flow')
```

**Task 3 — Valuation:**

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='enterprise_value')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='ttm')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='analyst_recommendations')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='dividend')
```

**Task 4 — Chart Generation:**

Use `tradingview_get_ohlcv` plus the `*_h[]` arrays from `tradingview_get_market_data`. No external price vendor is needed.

**Sections still requiring Web Search (~10%):**

- Deep business description, product-line detail → company website + 10-K Item 1
- Management bios → LinkedIn + Proxy Statement (DEF 14A)
- Risk factors → 10-K Item 1A
- Segment breakdown (segment revenue) → 10-K / 10-Q footnotes
- Industry research → Gartner / Forrester / IDC

---

## Scenario C: Catalyst Calendar (`catalyst-calendar`)

`from` and `to` are required Unix-seconds integers. Compute them; never leave them blank and never pass `"now"`. A single window must be ≤ 40 days.

```
from = Math.floor(Date.now() / 1000)
to = from + 30 * 86400

tradingview_get_calendar(type='earnings', from=from, to=to, market='america')
tradingview_get_calendar(type='revenue', from=from, to=to, market='america')
tradingview_get_calendar(type='ipo', from=from, to=to, market='america')
tradingview_get_calendar(type='economic', from=from, to=to, market='america')
```

Use `market='america,china'` for economic events only when the user asked for China / A-share macro. English/US prompts stay `america`.

For a single name's next print, prefer `tradingview_get_market_data(symbol, category='indicators')` and read `earnings_release_next_date`.

---

## Scenario D: Morning Note (`morning-note`)

```
from = Math.floor(Date.now() / 1000)
to = from + 2 * 86400   # today + tomorrow; still ≤ 40 days

tradingview_get_news(market='stock', lang='en', market_country='US')
tradingview_get_news(market='economic', lang='en')
tradingview_get_news(symbol='NASDAQ:AAPL', lang='en', market='stock', market_country='US')
tradingview_get_quote(symbol='NASDAQ:AAPL', session='premarket', fields='all')
tradingview_get_calendar(type='economic', from=from, to=to, market='america')
tradingview_get_calendar(type='earnings', from=from, to=to, market='america')
```

For multi-name coverage universes, use `tradingview_get_quote_batch` instead of one quote per name.

---

## Scenario E: Screening / Idea Generation (`idea-generation`)

Leaderboard is for ranked slices (gainers, losers, high dividend). It is **not** a sector filter.

```
tradingview_get_metadata(type='tabs', asset_type='stocks')
tradingview_get_leaderboard(asset_type='stocks', tab='gainers', market_code='america', count=50)
tradingview_get_leaderboard(asset_type='stocks', tab='losers', market_code='america', count=50)
tradingview_get_leaderboard(asset_type='stocks', tab='high-dividend', market_code='america', columnset='dividends', count=50)

tradingview_get_ideas_hot(lang='en')
tradingview_get_ideas_by_symbol(symbol='NASDAQ:AAPL', lang='en')
tradingview_get_minds(symbol='NASDAQ:AAPL', lang='en')
```

For a sector, factor, or "stocks like X" screen, discover enums then scan:

```
tradingview_get_screener_filter_options(asset_type='stock', lang='en', ids=['sector'])
tradingview_get_screener_presets(asset_type='stock')
tradingview_screen_assets(
  asset_type='stock',
  market='america',
  lang='en',
  range=[0, 50],
  preset_fields=['overview', 'valuation', 'profitability'],
  filters={
    'sector': {
      'operation': 'in_range',
      'value': ['Electronic Technology', 'Technology Services', 'Technology']
    }
  },
  sort={'sortBy': 'market_cap_basic', 'sortOrder': 'desc'}
)
```

Do not guess sector strings. `NASDAQ:AAPL` is `Electronic Technology`. Pass every matching enum returned by filter options when the user says "tech".

Follow-up diligence on shortlisted names:

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
tradingview_get_quote(symbol='NASDAQ:AAPL', session='regular', fields='all')
tradingview_get_ta(symbol='NASDAQ:AAPL', include_indicators=true)
```

Keep shortlists to 10–20 names. Do not scan hundreds of symbols through quote / market-data / TA.

---

## Scenario F: Sector Overview (`sector-overview`)

Build the peer universe with the screener, not with `tab='all_stocks'` plus a guessed sector string.

```
tradingview_get_screener_filter_options(asset_type='stock', lang='en', ids=['sector'])
tradingview_screen_assets(
  asset_type='stock',
  market='america',
  lang='en',
  range=[0, 100],
  preset_fields=['overview', 'valuation', 'profitability', 'performance'],
  filters={
    'sector': { 'operation': 'in_range', 'value': ['<discovered sector enums>'] }
  },
  sort={'sortBy': 'market_cap_basic', 'sortOrder': 'desc'}
)
```

Then drill into representative companies:

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
tradingview_get_market_data(symbol='NASDAQ:MSFT', category='analyst_recommendations')
tradingview_get_world_economy_indicators(indicator='full-year-gdp-growth', region='g20')
```

---

## Scenario G: Model Update (`model-update`)

```
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='financials_quarterly')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='analyst_recommendations')
tradingview_get_quote(symbol='NASDAQ:AAPL', session='regular', fields='all')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='enterprise_value')
```

Use Web Search only for updated guidance wording, transcript commentary, and one-off disclosures that are not represented in the structured payload.

---

## Scenario H: Thesis Tracker (`thesis-tracker`)

```
from = Math.floor(Date.now() / 1000)
to = from + 30 * 86400

tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='ttm')
tradingview_get_market_data(symbol='NASDAQ:AAPL', category='analyst_recommendations')
tradingview_get_calendar(type='earnings', from=from, to=to, market='america')
tradingview_get_news(symbol='NASDAQ:AAPL', lang='en', market='stock', market_country='US')
```

This scenario is best for maintaining a structured thesis scorecard: earnings cadence, valuation anchor, estimate dispersion, and fresh confirming/disconfirming data points.

---

## Ticker Resolution (generic preflight)

If the user supplies only a company name (e.g. "Apple"), resolve it to `EXCHANGE:TICKER` first:

```
tradingview_search_market(query='Apple', filter='stock')
# Returns: { data: { markets: [ { id: "NASDAQ:AAPL", symbol: "AAPL", description: "Apple Inc.", ... } ] } }
```

---

## Citation Convention

When citing data obtained from MCP in a report:

```
Source: Structured data via TradingView MCP; fetched [YYYY-MM-DD]
        Tool: tradingview_get_market_data(symbol='NASDAQ:AAPL', category='all')
        Fiscal Period: data.current.fiscal_period_current = "2026-Q1"
```

SEC filings (10-Q / 10-K) must still be cited separately with EDGAR hyperlinks. When consensus data comes from MCP, cite `category='analyst_recommendations'` explicitly instead of a generic terminal label.

---

## Fallback Strategy

1. **`tradingview_*` tools missing** → stop; tell the user to connect `https://mcp.tradingviewapi.com/mcp` and sign in with Console. Do not request an API key.
2. **Missing field** (company has no such metric) → keep field as "N/A"; do not fabricate
3. **Stale data** (`fiscal_period_current` > 90 days behind current quarter) → mark as "last reported" and Web Search to confirm whether a newer release exists
4. **Ticker resolution fails** → ask the user to specify `EXCHANGE:TICKER` explicitly
