---
description: Smart stock screening workflow - Filter quality targets based on multi-factor model
---

# Smart Stock Screening Workflow

Based on multi-factor model, filter quality targets from the market that meet technical and fundamental conditions, providing comprehensive scoring and buy recommendations.

## Execution Steps

### Step 1: Understand Screening Criteria

Extract from user input:
- **Market scope**: Country/region (determine market_code), asset type
- **Technical conditions**: Trend direction, RSI range, MACD status, volume
- **Fundamental conditions**: PE, PB, ROE, market cap, dividend yield, etc.
- **Sorting preference**: Change percentage, market cap, volume, etc.

### Step 2: Get Metadata (Metadata First)

```
tradingview_get_metadata(type='markets')  # Get market_code
tradingview_get_metadata(type='tabs', asset_type='stocks')  # Get available tabs
```

### Step 3: Get Candidate Pool

Match `market_code` to the user's market (`america` for US, `china` for A-shares). Do not copy a hardcoded market from these examples if the user asked about a different region.

Choose appropriate tab and columnset based on screening direction. Leaderboard `columnset` must be one of: `overview`, `performance`, `valuation`, `dividends`, `profitability`, `incomeStatement`, `balanceSheet`, `cashFlow`, `technicals`.

For a sector such as technology, prefer the screener instead of filtering leaderboard rows after the fact:

```
tradingview_get_screener_filter_options(asset_type='stock', ids=['sector'])
tradingview_screen_assets(
  asset_type='stock',
  market='america',
  range=[0, 50],
  preset_fields=['overview', 'valuation', 'profitability', 'technicals'],
  filters={
    'sector': {
      'operation': 'in_range',
      'value': ['Technology', 'Electronic Technology', 'Technology Services']
    }
  },
  sort={'sortBy': 'market_cap_basic', 'sortOrder': 'desc'}
)
```

Then:

```
# Technical screening - Use technical-related tabs
tradingview_get_leaderboard(
  asset_type='stocks', tab='gainers',  # or active/unusual-volume/best-performing
  market_code='america', columnset='overview', count=100
)

# Fundamental data - Switch columnset
tradingview_get_leaderboard(
  asset_type='stocks', tab='all-stocks',
  market_code='america', columnset='valuation', count=100
)

# Profitability
tradingview_get_leaderboard(
  asset_type='stocks', tab='all-stocks',
  market_code='america', columnset='profitability', count=100
)
```

### Step 4: Technical Screening

For Top 10–15 in the candidate pool, call individually (do not scan 100 names; that hits rate limits):

```
tradingview_get_ta(symbol, include_indicators=true)
```

Screening criteria (see `technical-analysis.md` scoring model):
- TA multi-timeframe signal is Buy
- RSI in healthy range 30-70
- MACD golden cross or DIF > 0
- ADX > 25 (trend exists)

### Step 5: K-line Data Verification

For Top 10 that pass technical screening, get K-line confirmation:

```
tradingview_get_ohlcv(symbol, timeframe='D', range=60)
```

Verify:
- Moving average arrangement (bullish/bearish)
- Volume coordination (volume increase on rise)
- Distance from support level

### Step 6: Comprehensive Scoring and Ranking

Calculate total score (100-point system) according to `technical-analysis.md` scoring model:
- Trend strength 30 points
- Momentum indicators 25 points
- Pattern recognition 20 points
- Support resistance 15 points
- Market sentiment 10 points

### Step 7: Generate Detailed Report

```markdown
# Smart Stock Screening Results - [Market/Sector]

## Screening Criteria
- [List technical and fundamental conditions]

## Qualified Stocks (Total N stocks)

### 1. [Stock Name] (Code) ⭐⭐⭐⭐⭐
**Comprehensive Score**: XX/100
- Technical: RSI=XX, MACD=XX, Trend=XX
- Fundamental: PE=XX, ROE=XX%
- Buy Recommendation: ¥XX-XX
- Stop Loss: ¥XX
- Target Price: ¥XX
```

## Example

**User**: "Screen for strong stocks in the US technology sector"

**Execution**:
1. `tradingview_get_screener_filter_options(asset_type='stock', ids=['sector'])` → confirm sector enum values
2. `tradingview_screen_assets(market='america', filters.sector in_range Electronic Technology / Technology Services / Technology)` → candidate pool
3. Top 10–15 `tradingview_get_ta(include_indicators=true)` → technical screening
4. Top 8 `tradingview_get_ohlcv(timeframe='D', range=60)` → K-line verification
5. Comprehensive scoring → Output Top 8 report

For China A-shares, use `market_code='china'` / `market='china'` instead.
