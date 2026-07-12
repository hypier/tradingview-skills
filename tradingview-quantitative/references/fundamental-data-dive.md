---
description: Fundamental data deep dive workflow - Analyze company profile, financials, dividends, and analyst views
---

# Fundamental Data Deep Dive Workflow

Use the market-data endpoint family to build a fundamentals-first view of a company, including profile, valuation, historical financials, dividends, and analyst expectations.

## Execution Steps

### Step 1: Resolve the Symbol

If the user gives a company name, first confirm the exact symbol:

```
tradingview_search_market(query="Apple", filter="stock")
```

### Step 2: Get Company Snapshot

Start with a profile-level overview:

```
GET /api/market-data/{symbol}/company
GET /api/market-data/{symbol}/current
GET /api/market-data/{symbol}/indicators
GET /api/market-data/{symbol}/ttm
```

Focus on:
- Sector, industry, exchange, website, employee count
- Market cap, PE, PB, PS, EPS, beta, 52-week range
- TTM profitability, margins, free cash flow, return on equity

### Step 3: Read Financial Statements

Pull both annual and quarterly views:

```
GET /api/market-data/{symbol}/financials-quarterly
GET /api/market-data/{symbol}/financials-annual
GET /api/market-data/{symbol}/history-quarterly
GET /api/market-data/{symbol}/history-annual
GET /api/market-data/{symbol}/cash-flow
```

Check for:
- Revenue trend
- Net income trend
- Margin stability
- Operating cash flow vs net income
- Debt burden and liquidity

### Step 4: Review Capital Return and Analysts

```
GET /api/market-data/{symbol}/dividend
GET /api/market-data/{symbol}/analyst-recommendations
GET /api/market-data/{symbol}/enterprise-value
GET /api/market-data/{symbol}/credit-ratings
```

Look at:
- Dividend yield and payout sustainability
- Analyst rating distribution and target prices
- EV-based multiples
- Credit quality for highly leveraged firms

### Step 5: Add Price Context

Combine fundamentals with market behavior:

```
tradingview_get_quote(symbol)
tradingview_get_price(symbol, timeframe='D', range=120)
tradingview_get_ta(symbol, include_indicators=true)
```

This helps answer whether a fundamentally strong company is extended, cheap, or deteriorating in price action.

### Step 6: Generate the Report

Suggested structure:

```markdown
# [Company] Fundamental Deep Dive

## Business Profile
## Valuation Snapshot
## Growth and Profitability
## Balance Sheet and Cash Flow
## Dividend and Shareholder Return
## Analyst Expectations
## Technical Context
## Overall View and Risks
```

## Example

**User**: "Do a fundamentals-first analysis of Apple"

**Execution**:
1. `search_market(query='Apple', filter='stock')` -> `NASDAQ:AAPL`
2. Pull company/current/indicators/ttm
3. Pull quarterly and annual financials
4. Pull dividend and analyst recommendation data
5. Cross-check with quote and price trend
6. Return a concise bull vs bear thesis
