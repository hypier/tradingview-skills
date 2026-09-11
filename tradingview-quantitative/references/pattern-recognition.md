---
description: Pattern Recognition Workflow - Automatically identify classic technical patterns and provide trading strategies
---

# Pattern Recognition Workflow

Based on candlestick data and technical indicators, identify classic technical patterns, provide confidence assessment and trading strategy recommendations.

Pattern recognition algorithms and success rate statistics can be found in `pattern-library.md`.

There is no S&P 500 constituent API. For "S&P 500" requests, analyze `AMEX:SPY` (or `NASDAQ:QQQ` for Nasdaq-100), or screener/large-cap a **maximum of 15 symbols**. Do not pull OHLCV for 500 names.

Pattern detection is local: compare OHLCV + TA against `pattern-library.md`. It is not a server-side pattern endpoint.

## Execution Steps

### Step 1: Get Historical Candlestick Data

Get sufficiently long daily data for pattern recognition:

```
tradingview_get_ohlcv(symbol, timeframe='D', range=120)
```

For short-term patterns (candlestick combinations), additionally get hourly data:
```
tradingview_get_ohlcv(symbol, timeframe='60', range=100)
```

Optional: `tradingview_get_price(..., type='HeikinAshi')` for clearer trend structure visualization. Do not use Heikin-Ashi prices for breakout levels or measured moves.

### Step 2: Get Technical Indicators

```
tradingview_get_ta(symbol, include_indicators=true)
```

Key indicators for pattern confirmation:
- **RSI**: Overbought/oversold status, divergence signals
- **MACD**: Golden cross/death cross, momentum direction
- **Volume**: Volume cooperation during pattern breakout
- **ADX**: Trend strength

### Step 3: Identify Patterns

Identify patterns based on candlestick data (see `pattern-library.md`):

**Reversal Patterns** (appear at trend ends):
- Double Bottom/Top: Two lows/highs close together, neckline breakout confirmation
- Head and Shoulders Bottom/Top: Three lows/highs, middle is lowest/highest
- Rounding Bottom/Top: Gradual reversal

**Continuation Patterns** (appear during trend continuation):
- Ascending/Descending Triangle: One side horizontal, one side diagonal
- Flag/Wedge: Narrow channel
- Rectangle: Horizontal channel

**Candlestick Patterns** (1-3 candle combinations):
- Hammer/Inverted Hammer
- Bullish/Bearish Engulfing
- Morning Star/Evening Star

### Step 4: Calculate Confidence

Confidence factors (0-100%):
- Pattern completeness (whether shape is standard)
- Volume cooperation (volume expansion on breakout adds points)
- Technical indicator confirmation (RSI/MACD direction consistency adds points)
- Time span (longer pattern duration is more reliable)
- Retest position (standing firm after neckline retest adds points)

### Step 5: Generate Trading Strategy

Calculate key price levels based on pattern type:

```
Entry price = Neckline breakout price (or pattern breakout price)
Stop loss = Below pattern lowest point (reversal) / Below channel lower boundary (continuation)
Target price = Entry price + Pattern height (measured move)
Risk-reward ratio = (Target - Entry) / (Entry - Stop loss)
```

Only recommend trades when risk-reward ratio > 1.5.

### Step 6: Output Analysis Report

```markdown
# [Symbol] Technical Pattern Analysis

## Identified Pattern
### [Pattern Name] (Confidence: XX%)
- Pattern description: ...
- Key levels: Neckline ¥XX
- Volume cooperation: [Expansion/Contraction/Normal]

## Technical Indicator Confirmation
- RSI(14): XX ([Overbought/Oversold/Healthy])
- MACD: [Golden cross/Death cross], DIF=[Positive/Negative]
- ADX: XX ([Trending/Non-trending])

## Trading Strategy
- Direction: [Long/Short/Wait]
- Entry price: ¥XX (Condition: [Breakout neckline/Pullback confirmation])
- Stop loss: ¥XX
- Target price: ¥XX
- Risk-reward ratio: 1:X.X

## Risk Warnings
- [List failure scenarios for this pattern]
```

## Example

**User**: "Analyze SPY for double bottom and flag patterns"

**Execution**:
1. `tradingview_get_ohlcv(symbol='AMEX:SPY', timeframe='D', range=120)` → Daily candles
2. `tradingview_get_ta(symbol='AMEX:SPY', include_indicators=true)` → Technical indicators
3. Analyze candlestick data to identify patterns (refer to `pattern-library.md`)
4. Calculate confidence and key price levels
5. Generate trading strategy report

Do not loop OHLCV across the S&P 500 membership list. If the user insists on multiple names, cap at 15 large-caps from the screener.
