# Trade Execution Analysis

Assess whether a signal can be traded at an acceptable cost and risk.

Combine current quote, bid/ask, volume, historical volatility, trading session, and position size. Estimate spread, slippage, market impact, fill uncertainty, and the risk of trading around openings, closings, halts, and scheduled events. Compare order styles and split large orders when liquidity requires it.

Output an executable price range, size constraint, cost assumptions, preferred session or order style, and conditions under which the trade should be skipped.

## MCP composition

Use `tradingview_get_quote` or `tradingview_get_quote_batch` for bid/ask and session context, `tradingview_get_ohlcv` for volume and volatility history, `tradingview_get_calendar` and `tradingview_get_price_events` for event risk, and `tradingview_get_news` for material breaking information. For option contracts, list codes with `tradingview_get_options` then quote the OPRA id (`fields=enhanced`); OPRA prints are often delayed. Do not claim a fill, order-book depth, implied volatility, or Greeks that the returned MCP data does not provide.
