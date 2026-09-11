# Thesis Tracker

description: Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones over time. Use when updating a thesis with new information, reviewing position rationale, or checking if a thesis is still intact. Triggers on "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", or "review my positions".

## Structured Data Source

Use hosted TradingView MCP to keep the thesis scorecard data-driven:

```
from = Math.floor(Date.now() / 1000)
to = from + 30 * 86400

tradingview_get_market_data(symbol, category='all')
tradingview_get_market_data(symbol, category='ttm')
tradingview_get_market_data(symbol, category='analyst_recommendations')
tradingview_get_calendar(type='earnings', from=from, to=to, market='america')
tradingview_get_news(symbol=symbol, lang='en', market='stock', market_country='US')
```

Never pass empty calendar `from`/`to`. Use `market='america'` unless the user asked for another market.

Web Search is still needed for original management wording, deep product / regulatory developments, and thesis inputs that rely on channel checks or alternative data.

## Execution Notes

- Resolve the company to `EXCHANGE:TICKER` first via `tradingview_search_market(query, filter='stock')` and keep that symbol as canonical in the thesis record.
- Treat `data.current.fiscal_period_current` as a provider label only. If the company's own quarter naming differs in the latest release or filing, use the primary-source label in thesis updates.
- If you pull live market context, prefer `tradingview_get_quote(symbol, session='regular', fields='all')`; quote metrics are nested under `data.data`.

## Workflow

### Step 1: Define or Load Thesis

If creating a new thesis:
- **Company**: Name and ticker
- **Position**: Long or Short
- **Thesis statement**: 1-2 sentence core thesis (e.g., "Long ACME — margin expansion from pricing power + operating leverage as mix shifts to software")
- **Key pillars**: 3-5 supporting arguments
- **Key risks**: 3-5 risks that would invalidate the thesis
- **Catalysts**: Upcoming events that could prove/disprove the thesis (earnings, product launches, regulatory decisions)
- **Target price / valuation**: What's it worth if the thesis plays out
- **Stop-loss trigger**: What would make you exit

If updating an existing thesis, ask the user for the new data point or development, then refresh the structured baseline before scoring the change.

### Step 2: Update Log

For each new data point or development:

- **Date**: When this happened
- **Data point**: What changed (earnings beat, management departure, competitor move, etc.)
- **Thesis impact**: Does this strengthen, weaken, or neutralize a specific pillar?
- **Action**: No change / Increase position / Trim / Exit
- **Updated conviction**: High / Medium / Low

Typical structured updates to log:
- Revenue / margin / FCF progress from `tradingview_get_market_data` (`all` or `ttm`)
- Price-target or recommendation drift from `/analyst-recommendations`
- New earnings date from `tradingview_get_calendar(type='earnings', from, to)` or `earnings_release_next_date`
- News items that confirm or challenge the thesis from `tradingview_get_news`

### Step 3: Thesis Scorecard

Maintain a running scorecard:

| Pillar | Original Expectation | Current Status | Trend |
|--------|---------------------|----------------|-------|
| Revenue growth >20% | On track | Q3 was 22% | Stable |
| Margin expansion | Behind | Margins flat YoY | Concerning |
| New product launch | Pending | Delayed to Q2 | Watch |

Populate the scorecard with the latest structured metrics wherever possible instead of freehand status labels only.

### Step 4: Catalyst Calendar

Track upcoming catalysts:

| Date | Event | Expected Impact | Notes |
|------|-------|-----------------|-------|
| | | | |

Seed this table from `tradingview_get_calendar(type='earnings', from, to)` for earnings dates and from recent `tradingview_get_news` items for company-specific follow-up events.

### Step 5: Output

Thesis summary suitable for:
- Morning meeting discussion
- Portfolio review
- Risk committee presentation

Format: Concise markdown or Word doc with the scorecard, recent updates, and current conviction level.

## Important Notes

- A thesis should be falsifiable — if nothing could disprove it, it's not a thesis
- Track disconfirming evidence as rigorously as confirming evidence
- Review theses at least quarterly, even when nothing dramatic has happened
- If the user manages multiple positions, offer to do a full portfolio thesis review
- Store thesis data in a structured format so it can be referenced across sessions and refreshed against MCP
