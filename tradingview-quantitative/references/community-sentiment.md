---
description: Community sentiment workflow - Track hot ideas, symbol minds, and crowd narratives from TradingView ideas
---

# Community Sentiment Workflow

Use TradingView community ideas to understand crowd narratives, recurring setups, and directional bias around a symbol or asset class.

## Execution Steps

### Step 1: Identify the Scope

Determine whether the user wants:
- Broad market sentiment
- Symbol-specific sentiment
- High-quality discretionary trade ideas
- A comparison between community narrative and quantitative signals

### Step 2: Get the Main Idea Feed

For broad discovery:

```
tradingview_get_ideas_hot(page=1, lang='en')
tradingview_get_ideas_editors_picks(page=1, lang='en')
```

Collect:
- Idea title
- Symbol
- Publish time
- Likes and comment count
- Author quality signals

### Step 3: Get Symbol-Specific Views

For a single instrument:

```
tradingview_get_ideas_by_symbol(symbol, page=1, per_page=20, lang='en')
tradingview_get_minds(symbol, lang='en')
```

Use these to measure:
- Bullish vs bearish balance
- Repeated support/resistance zones
- Common timeframe and setup type

### Step 4: Inspect High-Signal Idea Details

If a list response returns `image_url`, fetch the detail page:

```
tradingview_get_idea_detail(image_url)
```

Read for:
- Thesis clarity
- Risk management rules
- Time horizon
- Whether the idea is analysis, education, or pure opinion

### Step 5: Cross-Check with Market Data

Never rely on ideas alone. Compare them with:

```
tradingview_get_quote(symbol)
tradingview_get_ta(symbol, include_indicators=true)
tradingview_get_ohlcv(symbol, timeframe='D', range=90)
```

### Step 6: Summarize Narrative vs Reality

Return:
- Dominant community direction
- Most cited catalysts or chart levels
- Where community view aligns with TA
- Where sentiment looks crowded or low quality

## Example

**User**: "What is TradingView community sentiment on BTCUSDT right now?"

**Execution**:
1. `tradingview_get_ideas_by_symbol(symbol='BINANCE:BTCUSDT', page=1, per_page=20, lang='en')`
2. `tradingview_get_minds(symbol='BINANCE:BTCUSDT', lang='en')`
3. Fetch 2-3 representative idea details with `tradingview_get_idea_detail`
4. Compare with `tradingview_get_ta` and daily price data
5. Return sentiment summary plus contrarian risks
