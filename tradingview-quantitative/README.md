# TradingView Quantitative

TradingView Quantitative is a quantitative trading research and decision-support skill powered by TradingView MCP.

It does not duplicate MCP API documentation. Instead, it combines quotes, historical prices, technical indicators, fundamentals, news, events, macro data, and community data into practical research workflows. MCP retrieves the data; the skill frames the research question, organizes evidence, calculates metrics, tests hypotheses, and produces the report.

## Core capabilities

The skill currently provides nine thematic capabilities:

1. **Equity research**: Combine fundamental, technical, event, and valuation evidence to assess a company and its invalidation conditions.
2. **Opportunity discovery**: Turn an investment hypothesis into a multi-factor screen, then verify a focused candidate list.
3. **Market and macro research**: Analyze market regime, breadth, sector rotation, macro drivers, and cross-asset effects.
4. **Event studies**: Compare price, volume, and volatility before and after earnings, macro releases, policy events, or news shocks.
5. **Portfolio and risk**: Evaluate exposures, concentration, correlation, volatility, drawdown, and risk contribution.
6. **Signal validation**: Test whether technical, fundamental, or event signals have historical evidence.
7. **Strategy research and backtesting**: Convert trading rules into measurable strategies and assess returns, drawdown, turnover, and robustness.
8. **Trade execution analysis**: Assess spread, liquidity, slippage, market impact, and trading-session risks.
9. **Monitoring and signal triggers**: Monitor price, volume, technical state, events, and portfolio risk for meaningful state changes.

## Requirements

This skill requires a working hosted TradingView MCP connection. If `tradingview_*` tools are not visible in the client, read the [MCP setup guide](references/mcp-install.md), configure authentication, and verify the connection before starting research.

The setup guide covers connection and basic verification only. MCP tools provide their own data-access parameters and schemas.

## How it works

Each analysis follows these principles:

- Define the research question, instrument, market, timeframe, and decision objective first.
- Choose one primary research mode and combine other modes only when needed.
- Cross-check important conclusions with multiple data types instead of relying on one indicator.
- Separate observed facts, derived calculations, interpretations, and actionable conditions.
- Record the analysis time, market session, historical window, missing data, and key assumptions.
- Report confidence, counter-evidence, and conditions that would invalidate the conclusion.
- Control request size and use batch MCP tools when comparing candidate instruments.

See [analysis-framework.md](references/analysis-framework.md) for evidence and confidence rules, and [output-templates.md](references/output-templates.md) for report structures.

## MCP data composition

Each thematic workflow combines MCP tools according to the research question. Examples include:

- Equity research: instrument search, real-time quotes, OHLCV, technical analysis, fundamentals, news, and events.
- Opportunity discovery: metadata, leaderboards or screeners, batch quotes, batch history, and candidate verification.
- Strategy research: historical OHLCV, technical indicators, fundamental fields, and current market context.
- Portfolio analysis: batch quotes, batch historical data, and material fundamental or event information for major holdings.
- Monitoring: batch quotes, batch history, technical state, calendars, news, and event markers.

The skill does not claim data that MCP did not return, such as a complete order book, actual fills, or native backtest performance.

## Directory structure

```text
tradingview-quantitative/
├── SKILL.md
├── README.md
└── references/
    ├── analysis-framework.md
    ├── equity-research.md
    ├── opportunity-screening.md
    ├── market-macro-research.md
    ├── event-study.md
    ├── portfolio-risk.md
    ├── signal-validation.md
    ├── strategy-research.md
    ├── execution-analysis.md
    ├── monitoring-and-alerts.md
    ├── output-templates.md
    ├── mcp-install.md
    ├── technical-analysis.md
    ├── pattern-library.md
    └── risk-management.md
```

`SKILL.md` handles thematic routing and shared rules. Files in `references/` are loaded only when the relevant research mode needs them. The technical analysis, pattern library, and risk management files provide methodology; they are not separate interface skills.

## Example requests

```text
Analyze NASDAQ:AAPL, focusing on post-earnings trend, valuation, and risk.

Screen large-cap US stocks for reasonable valuation, improving profitability, and strengthening momentum.

Compare the performance of the Nasdaq, the US dollar, and long-term Treasuries before and after a CPI release.

Check whether my portfolio has excessive sector concentration or correlated risk.

Validate an RSI oversold-reversal strategy over the past three years, including maximum drawdown.
```

## Scope and limitations

This project provides quantitative research and decision support. It is not personalized investment advice and does not guarantee future returns. Historical tests can be affected by sample selection, slippage, transaction costs, liquidity, look-ahead bias, and survivorship bias; reports should state these limitations.
