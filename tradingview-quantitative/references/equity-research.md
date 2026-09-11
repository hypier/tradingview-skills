# Equity Research Workflow

Answer: what is changing in the company and price, why might it matter, and what would disprove the thesis?

Combine instrument resolution, current quote, multi-timeframe prices, technical indicators, fundamentals, news, and upcoming events as appropriate. Compare price action with earnings, cash flow, valuation, and expectations rather than treating one data type in isolation.

Output a concise thesis, supporting and counter-evidence, catalysts, risks, key levels or conditions, and confidence. Include a separate risk plan when the user supplies capital, position, or loss limits. Formal reports also write an `equity` HTML board; see `visual-report.md`.

## MCP composition

Use `tradingview_search_market` for resolution, then combine `tradingview_get_quote`, `tradingview_get_ohlcv`, `tradingview_get_ta`, `tradingview_get_market_data`, `tradingview_get_news`, `tradingview_get_calendar`, and `tradingview_get_price_events` according to the hypothesis. Do not call every source by default.
