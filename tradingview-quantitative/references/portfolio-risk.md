# Portfolio and Risk Workflow

Evaluate the portfolio as a system, then translate the result into position-level controls.

Collect holdings, weights, cost basis, currency, and user risk limits when available. Combine current quotes and historical prices to calculate exposure, concentration, correlation, volatility, drawdown, and contribution to risk. Add fundamentals, technicals, and events only when they change the risk decision.

Output exposures, largest risk contributors, concentration or correlation problems, stress scenarios, sizing constraints, and measurable rebalance or stop conditions. Keep assumptions visible; no sizing formula is universally suitable. Formal reports also write a `portfolio` HTML board; see `visual-report.md`.

## MCP composition

Resolve unknown holdings with `tradingview_search_market`, then use `tradingview_get_quote_batch` and `tradingview_get_ohlcv_batch` for portfolio calculations. For ETF positions, call `tradingview_get_etf` to look through AUM and top holdings before treating the ticker as one name. Add `tradingview_get_market_data`, `tradingview_get_ta`, `tradingview_get_news`, or `tradingview_get_calendar` only for material position risks. Option overlays: `options-and-etf.md`.
