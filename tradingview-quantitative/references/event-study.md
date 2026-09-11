# Event Study Workflow

Measure an event’s market impact instead of only summarizing it.

Define the event, affected universe, event date or window, comparison asset, and pre/post periods. Combine calendar or news records with historical prices, volume, volatility, and sector or market benchmarks. For recurring events, compare a meaningful historical sample and report its size.

Output event facts, abnormal or relative performance, volatility and volume response, affected beneficiaries or losers, scenario risks, and invalidation conditions. Distinguish scheduled information from surprise information.

## MCP composition

Use `tradingview_get_calendar` or `tradingview_get_news` to identify events, `tradingview_get_price_events` for historical markers, and `tradingview_get_ohlcv` or `_batch` plus benchmark quotes for pre/post calculations. Use `tradingview_search_market` when the affected universe is described by name.
