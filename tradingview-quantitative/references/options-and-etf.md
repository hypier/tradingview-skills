# Options Chain and ETF Holdings

Use this when the question is listed strikes, covered-call / overlay structure, “does this have options?”, fund AUM/NAV, or look-through holdings. Do not treat a stock quote as an option chain or `related_etfs` as a holdings table.

## Options

1. Resolve the **underlying** (`NASDAQ:AAPL`), not a guessed OPRA id.
2. Call `tradingview_get_options` with optional `expiration` (`YYYY-MM-DD` or `YYYYMMDD`). Prefer one expiry in a UI or report.
3. Read `has_options` and `families[].series[]`: `strikes` are **dollar** strikes, `calls`/`puts` are contract codes in the same order.
4. Price a contract with `tradingview_get_quote` on an OPRA id such as `OPRA:AAPL261218C330.0`, `fields=enhanced`. Identity lives on the contract (`type=option`, `strike`, `expiration`, `option-type`, `option-style`, `lotsize`, `underlying-symbol`) next to `lp` / `bid` / `ask` / `volume` — there is no nested `options` object.

Do not look for `has_options` or `families` on `tradingview_get_quote` of the underlying. `fields=enhanced` on the stock still does not return the chain.

This API does **not** provide implied volatility, delta/gamma/theta/vega, or open interest. Do not invent Greeks. `update_mode` on OPRA quotes is often delayed (~15 minutes).

Contract format: `{prefix}:{root}{YYMMDD}{C|P}{strike}`. Integer strikes keep `.0`. Do not quote `NASDAQ:AAPL261218C330.0`.

No listed chain: `has_options=false` and `families=[]` (e.g. `BINANCE:BTCUSDT`). Listed underlying but expiry not listed: `has_options=true` and empty `families`.

## ETF

1. Resolve the fund (`AMEX:SPY`; QQQ is `NASDAQ:QQQ`).
2. Call `tradingview_get_etf` (`limit` default 20, max 100). Use `holdings_count` for the full book; the array is truncated.
3. Non-funds return `is_etf=false` and empty holdings.

`tradingview_get_market_data` `category=related_etfs` lists **related tickers**, not this fund’s holdings. Quote `fields=enhanced` can include `aum` / `nav` / `expense_ratio` without the holdings list.

For a portfolio of ETFs, pull look-through holdings before treating the ticker as a single name. For equity research on a company that is also an ETF holding, still research the company on its own quote and fundamentals.
