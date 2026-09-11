# Monitoring and Signal Triggers

Turn a strategy, portfolio limit, or event plan into observable state changes.

Define the baseline, polling interval, trigger threshold, cooldown, and notification condition. Monitor only signals that can be computed from MCP data: price and percentage moves, support or resistance breaks, volume or volatility changes, technical-state changes, upcoming events, and portfolio risk limits. Notify on meaningful state changes, failure, or required action; remain quiet while unchanged.

## MCP composition

Use `tradingview_get_quote_batch` for current state, `tradingview_get_ohlcv_batch` and `tradingview_get_ta` for trend or volatility changes, and `tradingview_get_calendar`, `tradingview_get_news`, or `tradingview_get_price_events` for catalysts. Monitoring schedules and notifications are handled by the surrounding automation system; MCP provides the observations.
