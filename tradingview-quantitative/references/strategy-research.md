# Strategy Research and Backtesting

Translate a trading idea into explicit rules and test it with historical data before discussing deployment.

Define the universe, signal, entry, exit, holding period, rebalance schedule, sizing, long/short constraints, benchmark, and costs. Use standard OHLCV history and technical or fundamental observations available through MCP. Calculate trade count, return, expectancy, hit rate, average win/loss, volatility, maximum drawdown, turnover, and benchmark-relative performance. Separate development and validation periods where possible.

Stress the strategy across timeframes, markets, parameters, and fees. Record look-ahead, survivorship, stale fundamental data, corporate-action, and liquidity limitations. A strategy result is evidence for a hypothesis, not a promise of future performance.

## MCP composition

Use `tradingview_search_market` or `tradingview_get_metadata` to define the universe, `tradingview_get_ohlcv` or `tradingview_get_ohlcv_batch` for price history, `tradingview_get_ta` for indicator inputs, and `tradingview_get_quote` for current execution context. Use `tradingview_get_market_data` only when the strategy includes fundamentals. Option overlays need `tradingview_get_options` then contract quotes; do not backtest Greeks this API does not return. MCP supplies observations; return and risk statistics must be calculated from the retrieved history.
