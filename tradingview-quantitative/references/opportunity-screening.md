# Opportunity Discovery Workflow

Turn a market view or investment hypothesis into a candidate universe, then verify a small number of candidates in depth.

Define the universe, liquidity floor, factor definitions, exclusions, ranking rule, and output before screening. Combine technical, fundamental, valuation, performance, dividend, sentiment, or sector data only when each factor has a role in the hypothesis. Spot-check leading candidates with independent market data and record false-positive risks.

Return a ranked shortlist with why each candidate passed, what still needs verification, and conditions that remove it from the list. A screen is a research starting point, not a trade recommendation. Formal reports also write a `screening` HTML board; see `visual-report.md`.

## MCP composition

Use `tradingview_get_metadata` when discovering leaderboard or screener values, then compose `tradingview_get_leaderboard` or `tradingview_screen_assets` with `tradingview_get_quote_batch`, `tradingview_get_ohlcv_batch`, and individual `tradingview_get_ta` checks for the shortlist.
