---
description: Advanced screener workflow - Build custom TradingView screener queries with presets and filter options
---

# Advanced Screener Workflow

Use the TradingView screener flow to build precise cross-factor queries such as "US stocks with PE < 15 and RSI < 30" or "large-cap crypto with strong momentum and active addresses growth".

## Execution Steps

### Step 1: Clarify the Screening Target

Extract four things from the user request:
- **Asset type**: `stock`, `crypto`, `etf`, `bond`, `cex`, `dex`
- **Market scope**: market code, exchange, country, sector, or symbol universe
- **Filter conditions**: valuation, profitability, technical, liquidity, on-chain, dividend, etc.
- **Output preference**: sort field, top N, and fields to display

### Step 2: Confirm Metadata and Valid Values

Always fetch valid parameter values before building the final scan:

```
tradingview_get_metadata(type='markets')        # stock market codes
tradingview_get_metadata(type='exchanges')      # exchange names for filter enums
tradingview_get_metadata(type='languages')      # optional language selection
```

### Step 3: Get Screener Presets

Choose the most relevant field groups first:

```
tradingview_get_screener_presets(asset_type='stock')
```

Typical preset groups:
- `overview`
- `performance`
- `valuation`
- `dividends`
- `profitability`
- `income_statement`
- `balance_sheet`
- `cash_flow`
- `technicals`

### Step 4: Discover Filter Fields and Operators

Fetch filter definitions before writing the scan body:

```
tradingview_get_screener_filter_options(asset_type='stock', lang='en')
```

Check for:
- Exact field ids
- Supported operations such as `greater_or_equal`, `less_or_equal`, `between`
- Enum values for exchange, sector, country, or category filters

### Step 5: Build the Scan Payload

Pass `market`, `range`, `preset_fields`, `filters`, and optional `sort` to `tradingview_screen_assets`.

```
tradingview_screen_assets(
  asset_type='stock',
  market='america',
  range=[0, 50],
  preset_fields=['overview', 'valuation', 'profitability', 'technicals'],
  filters={
    'market_cap_basic': { 'operation': 'greater_or_equal', 'value': 10000000000 },
    'price_earnings_ttm': { 'operation': 'less_or_equal', 'value': 15 },
    'RSI': { 'operation': 'less_or_equal', 'value': 30 }
  },
  sort={'sortBy': 'market_cap_basic', 'sortOrder': 'desc'}
)
```

### Step 6: Run the Scan and Validate the Results

```
tradingview_screen_assets(...)
```

Validation checklist:
- Result count is large enough for ranking
- Returned fields match the chosen presets
- Filter logic matches the user intent
- Top results still make sense after spot-checking quotes or TA

### Step 7: Add Secondary Verification

For the top 5-10 results, use:

```
tradingview_get_quote(symbol)
tradingview_get_ta(symbol, include_indicators=true)
tradingview_get_ohlcv(symbol, timeframe='D', range=60)
```

This avoids over-trusting one screener snapshot.

## Example

**User**: "Screen US dividend stocks with PE below 20, ROE above 15%, and RSI under 40"

**Execution**:
1. `tradingview_get_metadata(type='markets')` -> confirm `america`
2. `tradingview_get_screener_presets(asset_type='stock')`
3. `tradingview_get_screener_filter_options(asset_type='stock', lang='en')`
4. `tradingview_screen_assets` with valuation + profitability + technical filters
5. Spot-check top results with `tradingview_get_quote` and `tradingview_get_ta`
6. Return ranked results with reasons and risks
