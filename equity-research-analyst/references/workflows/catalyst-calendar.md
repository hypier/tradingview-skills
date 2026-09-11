# Catalyst Calendar

description: Build and maintain a calendar of upcoming catalysts across a coverage universe — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position ahead of events. Triggers on "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", or "catalyst tracker".

## ⭐ Structured Data Source

Use hosted TradingView MCP for structured catalyst data (see `../tradingviewapi.md` Scenario C):

```
from = Math.floor(Date.now() / 1000)
to = from + 30 * 86400   # required Unix-seconds integers; span ≤ 40 days

tradingview_get_calendar(type='earnings', from=from, to=to, market='america')
tradingview_get_calendar(type='revenue', from=from, to=to, market='america')
tradingview_get_calendar(type='ipo', from=from, to=to, market='america')
tradingview_get_calendar(type='economic', from=from, to=to, market='america')
tradingview_get_market_data(symbol, category='indicators')  # earnings_release_next_date
```

Never pass empty `from`/`to`, `"now"`, or date labels. Use `market='america,china'` for economic events only when the user asked for China macro. Web Search is still needed for unstructured catalysts such as product launches, FDA decisions, M&A milestones, management transitions, and lockup expirations.

## Workflow

### Step 1: Define Coverage Universe

- List of companies to track (tickers or names)
- Sector / industry focus
- Include macro events? (Fed meetings, economic data, regulatory deadlines)
- Time horizon (next 2 weeks, month, quarter)

### Step 2: Gather Catalysts

For each company, identify upcoming events:

**Earnings & Financial Events**
- Quarterly earnings date and time (pre/post market)
- Annual shareholder meeting
- Investor day / analyst day
- Capital markets day
- Debt maturity / refinancing dates

**Corporate Events**
- Product launches or announcements
- FDA approvals / regulatory decisions
- Contract renewals or expirations
- M&A milestones (close dates, regulatory approvals)
- Management transitions
- Insider trading windows (lockup expirations)

**Industry Events**
- Major conferences (dates, which companies presenting)
- Trade shows and expos
- Regulatory comment periods or rulings
- Industry data releases (monthly sales, traffic, etc.)

**Macro Events**
- Fed meetings (FOMC dates)
- Jobs report, CPI, GDP releases
- Central bank decisions (ECB, BOJ, etc.)
- Geopolitical events with market impact

### Step 3: Calendar View

| Date | Event | Company/Sector | Type | Impact (H/M/L) | Our Positioning | Notes |
|------|-------|---------------|------|-----------------|----------------|-------|
| | | | Earnings/Corp/Industry/Macro | | Long/Short/Neutral | |

### Step 4: Weekly Preview

Each week, generate a forward-looking summary:

**This Week's Key Events:**
1. [Day]: [Company] Q[X] earnings — consensus [$X EPS], our estimate [$X], key focus: [metric]
2. [Day]: [Event] — why it matters for [stocks]
3. [Day]: [Macro release] — expectations and positioning

**Next Week Preview:**
- Early heads-up on important events coming

**Position Implications:**
- Events that could move specific positions
- Any pre-positioning recommended
- Risk management ahead of binary events

### Step 5: Output

- Excel workbook with calendar view and sortable columns
- Weekly preview email/note (markdown)
- Optional: integration with Google Calendar

## Important Notes

- Earnings dates shift — verify against company IR pages and other up-to-date primary / market sources closer to the date
- Pre-announce risk: track companies with a history of pre-announcing (positive or negative)
- Conference attendance lists are valuable — which companies are presenting and which are conspicuously absent?
- Some catalysts are recurring (monthly industry data) — build a template and auto-populate
- Color-code by impact level: Red = high impact, Yellow = moderate, Green = routine
- Archive past catalysts with the actual outcome — builds pattern recognition over time
