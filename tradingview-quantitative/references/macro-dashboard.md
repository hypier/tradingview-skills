---
description: Macro dashboard workflow - Combine world economy indicators, macro calendar, and news into a top-down market view
---

# Macro Dashboard Workflow

Build a top-down macro view by combining world economy rankings, economic calendars, and market-moving macro news.

## Execution Steps

### Step 1: Define the Macro Question

Examples:
- Which G20 economies are accelerating?
- What are the most important macro events in the next two weeks?
- How should I compare inflation, rates, and growth across regions?

### Step 2: Confirm Valid Indicator Slugs

Get the available world-economy indicator list first:

```
tradingview_get_world_economy_indicator_metadata()
```

Typical indicators include GDP growth, inflation, unemployment, interest rates, industrial production, and retail sales.

### Step 3: Pull World Economy Rankings

```
tradingview_get_world_economy_indicators(indicator, region='g20')
```

Useful regions:
- `g20`
- `world`
- `north-america`
- `europe`
- `asia-pacific`
- `latin-america`
- `middle-east-africa`

### Step 4: Pull Upcoming Economic Events

```
tradingview_get_calendar(type='economic', from=now, to=now+14days, market='america,china,euro-area')
```

Prioritize:
- CPI / PPI
- GDP
- Employment / non-farm payrolls
- PMI / ISM
- Central bank decisions

### Step 5: Pull Supporting Macro News

```
tradingview_get_news(market='economic', lang='en', limit=10)
```

Optionally compare multiple countries with `market_country`.

### Step 6: Build the Dashboard

Recommended output:

```markdown
# Macro Dashboard

## Growth Rankings
## Inflation and Rates
## Next 2 Weeks Calendar
## Key Macro Headlines
## Market Implications for Equities, FX, Bonds, and Crypto
```

### Step 7: Translate Macro into Trading Impact

Tie the macro view back to tradable assets:
- Stronger growth + sticky inflation -> rates and FX sensitivity
- Falling inflation + weak growth -> defensives, bonds, gold
- Divergent country momentum -> regional allocation ideas

## Example

**User**: "Build me a G20 macro dashboard for next week"

**Execution**:
1. `tradingview_get_world_economy_indicator_metadata`
2. Pull 2-4 ranking indicators such as GDP growth and inflation with `tradingview_get_world_economy_indicators`
3. Pull next-week economic calendar with `tradingview_get_calendar`
4. Pull macro news headlines with `tradingview_get_news`
5. Return a concise top-down report with asset implications
