---
name: tradingview-api-integration
description: Use when integrating with, troubleshooting, or querying the TradingView Data API on api.tradingviewapi.com (Console, recommended) or RapidAPI, including live market data, screeners, calendar data, metadata, streaming, endpoint selection, and API parameter validation.
---

# TradingView API Integration

Help developers integrate the TradingView Data API and answer data questions by calling it live.

**Recommended (Console)**

- Base URL: `https://api.tradingviewapi.com`
- Auth: `Authorization: Bearer <KEY>` (equivalent: `X-API-Key: <KEY>`)
- Get a key at https://console.tvapis.com/start

**Alternate (RapidAPI)**

- Base URL: `https://tradingview-data1.p.rapidapi.com`
- Auth: `x-rapidapi-host: tradingview-data1.p.rapidapi.com` and `x-rapidapi-key: <KEY>`
- Console and RapidAPI keys are billed separately. Paths after the host are the same.

Prefer Console for new integrations and generated examples. Use RapidAPI only when the user already has a RapidAPI subscription or asks for it.

## API key workflow (required for live calls)

`scripts/tv_api.py` defaults to Console. It resolves the key in this order:

1. `--key` CLI argument
2. `TRADINGVIEW_API_KEY` environment variable
3. `RAPIDAPI_KEY` environment variable (legacy RapidAPI)
4. `.api-key` file in this skill's root directory
5. `.rapidapi-key` file in this skill's root directory (legacy)

If the only available key came from `RAPIDAPI_KEY` or `.rapidapi-key`, the script uses the RapidAPI host automatically. `--backend console|rapid` or `--rapid` overrides that.

If none is available, ask the user for a Console API key.

When the user provides a key, ask whether to save it for future sessions. **Only after explicit consent**, save it:

```bash
python3 scripts/tv_api.py --save-key 'THE_KEY'
```

This writes `.api-key` (chmod 600) to the skill root so future calls need no key prompt.

## Making live requests

Use `scripts/tv_api.py` (stdlib only, handles key resolution and JSON pretty-printing):

```bash
python3 scripts/tv_api.py GET '/api/quote/NASDAQ:AAPL'
python3 scripts/tv_api.py GET '/api/price/BINANCE:BTCUSDT?timeframe=60&range=20'
python3 scripts/tv_api.py POST '/api/screener/scan' --body '{"market":"america","range":[0,20],"filters":{"market_cap_basic":{"operation":"greater_or_equal","value":1e10}}}'
python3 scripts/tv_api.py --rapid GET '/api/quote/NASDAQ:AAPL'
```

Equivalent Console curl:

```bash
curl --location 'https://api.tradingviewapi.com/api/quote/NASDAQ:AAPL' \
  --header 'Authorization: Bearer YOUR_API_KEY'
```

## Choosing the right endpoint

Map the user's need to an endpoint family:

| User wants | Endpoint(s) | Example file |
|------------|-------------|--------------|
| Find a symbol / "what's the ticker for X" | `GET /api/search/market/{query}?filter=stock\|crypto\|...` | `03-market-search.md` |
| Current price, change, volume | `GET /api/quote/{symbol}` or `POST /api/quote/batch` (≤10) | `02-quote-data.md` |
| Candlesticks / OHLCV history | `GET /api/price/{symbol}?timeframe=&range=` or `POST /api/price/batch` | `01-price-data.md` |
| Buy/Sell signals, RSI, MACD | `GET /api/ta/{symbol}` (summary) or `/api/ta/{symbol}/indicators` (detail) | `04-technical-analysis.md` |
| Company profile, PE, financials, dividends, analyst ratings | `GET /api/market-data/{symbol}/...` (15 category sub-endpoints) | `12-market-data.md` |
| Top gainers/losers, rankings by asset class | `GET /api/leaderboard/{stocks\|crypto\|etfs\|forex\|futures\|indices\|bonds\|corporate-bonds}` | `05-leaderboards.md` |
| Custom filtering ("US stocks with PE < 15 and RSI < 30") | `POST /api/screener/.../scan` (see screener workflow below) | `16-screener.md` |
| News | `GET /api/news/{stock\|crypto\|forex\|...}`, detail via `GET /api/news/{newsId}` | `06-news.md` |
| Trading ideas / community sentiment | `GET /api/ideas/hot`, `/api/ideas/list/{symbol}`, `/api/ideas/{symbol}/minds` | `13-ideas.md` |
| Earnings / IPO / dividend / macro event dates | `GET /api/calendar/{earnings\|ipo\|revenue\|economic}?from=&to=` (Unix seconds, ≤40-day window) | `08-calendar.md` |
| GDP, inflation, interest rates by country | `GET /api/world-economy/indicators/{slug}?region=` | `14-world-economy.md` |
| Symbol logo image | `GET /logo?url={logoid}` (public, no key) | `09-logo.md` |
| Live streaming updates | `POST /api/token/generate` → SSE `/sse/stream` or WebSocket | `15-token.md`, `11-websocket.md` |
| MCP for Cursor / VS Code / Claude | Hosted `https://mcp.tradingviewapi.com/mcp` + Console OAuth (`"type": "http"`). JWT via `POST /api/mcp/generate`. RapidAPI local OpenAPI MCP | `10-mcp.md` |
| Valid parameter values (markets, tabs, columnsets, …) | `GET /api/metadata/...` (see metadata section below) | `07-metadata.md` |

Full parameter tables, enums, and request/response shapes: read **[references/endpoint-catalog.md](references/endpoint-catalog.md)**.

A machine-readable OpenAPI 3.0 spec snapshot is at `references/openapi.json` (~870 KB, 72 paths — too large to read whole; query it instead):

```bash
# List all paths
python3 -c "import json; print('\n'.join(json.load(open('references/openapi.json'))['paths']))"
# Dump one endpoint's full schema
python3 -c "import json; print(json.dumps(json.load(open('references/openapi.json'))['paths']['/api/quote/{symbol}'], indent=2))"
```

The live, always-current version is at `https://www.tradingviewapi.com/openapi.json` (public, no key). Fetch it to a temporary path when the snapshot seems stale or an endpoint is missing; update the bundled snapshot only when intentionally maintaining this skill:

```bash
curl -fsSL https://www.tradingviewapi.com/openapi.json -o /tmp/tradingview-openapi.json
```

Captured request/response examples live in `references/examples/` (file names listed in the table above; also `10-mcp.md`). Consult the example file before parsing a response shape you haven't seen. In the examples, repeated result rows and long string values are truncated with explicit `(truncated)` markers; all response fields are preserved. The real responses contain the full data.

## Parameters that come from metadata

Many parameters must be valid values fetched from metadata endpoints (all public):

- `market_code` / calendar `market` / screener `market` → `GET /api/metadata/markets`
- leaderboard `tab` → `GET /api/metadata/tabs?type={stocks|indices|crypto|futures|currencies|bonds|corporate_bonds|etfs}`
- leaderboard `columnset` → `GET /api/metadata/columnsets`
- `lang` → `GET /api/metadata/languages`
- world-economy `indicator` slug → `GET /api/metadata/world-economy/indicators`
- exchange names for screener filters → `GET /api/metadata/exchanges`

When unsure whether a parameter value is valid, fetch the metadata endpoint first instead of guessing.

## Screener workflow

The screener is the most powerful but most complex endpoint. Always follow this order:

1. Pick asset type: `stock`, `crypto`, `etf`, `bond`, `cex`, `dex`
2. `GET /api/screener/presets?asset_type=...` → choose `preset_fields` (column groups)
3. `GET /api/screener/filter-options?asset_type=...&lang=en` → discover filter field ids, operations, and enum values
4. `POST /api/screener/{...}/scan` with body `{ market, range, preset_fields, filters, sort }`

Filter syntax: array = multi-select, `{ "operation": "greater_or_equal", "value": n }` = comparison, scalar = equality. Details in the catalog.

## MCP (AI assistants)

Recommended for Cursor, VS Code, and Claude: add the hosted URL and sign in with Console. No JWT in the config file.

```json
{
  "mcpServers": {
    "tradingview": {
      "type": "http",
      "url": "https://mcp.tradingviewapi.com/mcp"
    }
  }
}
```

Older clients may use `"type": "streamable-http"`. JWT fallback: `POST /api/mcp/generate`, then copy `exampleConfig` (`http`) or `exampleConfigStreamableHttp`. RapidAPI local OpenAPI MCP: `npx -y @ivotoby/openapi-mcp-server` (OpenAPI tools, not hosted `tradingview_*`). Details: **[references/examples/10-mcp.md](references/examples/10-mcp.md)**.

## Symbol format

Always `EXCHANGE:TICKER` (e.g. `NASDAQ:AAPL`, `BINANCE:BTCUSDT`, `HKEX:9988`). If the user gives a bare name ("Apple", "比亚迪"), resolve it via `/api/search/market/` first.

## Answering data questions

When the user asks a data question (not an integration question):

1. Ensure a key is available (see key workflow)
2. Resolve symbols via search if needed
3. Fetch required metadata for parameter values
4. Call the endpoint(s) with `scripts/tv_api.py`
5. Summarize the result; cite which endpoint(s) you used so the developer can reproduce the call
