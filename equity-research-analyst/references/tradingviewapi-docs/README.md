# tradingviewapi Reference Bundle

This directory contains bundled payload examples for the `equity-research-analyst` skill. Use it to look up JSON field names and response shapes. **Do not copy the REST curls or OpenAPI paths as live requests.** Live data comes from hosted `tradingview_*` MCP tools (see `../tradingviewapi.md`).

## Recommended Reading Order

1. Read `../tradingviewapi.md` first for the research-task → MCP-tool mapping.
2. Open `examples/*.md` when you need a concrete JSON field path or sample payload after a tool call.
3. Open `openapi.json` only for field names or enum spelling. Never build REST curls from it.
4. If `../tradingviewapi.md` disagrees with a curl in this folder, trust the MCP tool names and arguments.

## Reference Priority

1. `../tradingviewapi.md` — which MCP tool to call and which arguments to pass.
2. `examples/*.md` — typical response payload structure.
3. `openapi.json` — field names, defaults, and enums.

If these sources disagree:

- Trust `../tradingviewapi.md` for live calls.
- Treat `examples/*.md` as illustrative payloads. The request headers and `YOUR_API_KEY` curls are historical captures, not the workflow.

## Search Tips

- Prefer `rg "earnings_release_next_date" references/tradingviewapi-docs/examples`
- Prefer `rg "analyst_recommendations" references/tradingviewapi-docs/examples`
- Prefer `rg "GET /api/market-data/{symbol}"` only to find the payload example file, then map it to `tradingview_get_market_data`.
- Open the smallest matching example file instead of loading the largest example bundle wholesale.

## What Is In This Folder

- `openapi.json`: bundled OpenAPI spec, useful for field names only.
- `examples/`: grouped sample responses by endpoint family.
- `README.md`: this short navigation note.

The most frequently useful example files for this skill are:

- `examples/10-market-data.md` for company, TTM, quarterly, annual, analyst, and valuation data.
- `examples/08-calendar.md` for earnings, dividend, IPO, and macro calendars.
- `examples/01-price-data.md`, `02-quote-data.md`, and `04-technical-analysis.md` for charting and trading context. Prefer `tradingview_get_ohlcv` for real Japanese candles used in reports.
- `examples/06-news.md` and `11-ideas.md` for market news and community idea flows.

## Connect MCP (no API key)

This skill does not use REST API keys.

1. Add `https://mcp.tradingviewapi.com/mcp` with `"type": "http"` and sign in with Console.
2. If `tradingview_*` tools are missing, stop and tell the user to connect MCP.
3. RapidAPI without Console: mint a JWT via `POST https://api.tradingviewapi.com/api/mcp/generate` and paste `exampleConfig`.
4. Local OpenAPI MCP is the wrong tool set — use `tradingview-api-integration` instead.

Do not store credentials in this skill folder or packaged `.skill` artifact.

## Maintenance Notes

- This repo no longer includes `sync-tradingviewapi-docs.sh`.
- If these bundled references become stale, refresh the affected files manually.
- Keep detailed tool mapping in `../tradingviewapi.md`; keep this file short and navigational.
