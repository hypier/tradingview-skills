# MCP setup

Public guide: https://www.tradingviewapi.com/mcp/

Hosted MCP exposes **25** `tradingview_*` tools (search, quotes, OHLCV, TA, news, calendars, leaderboards, screener, fundamentals, ideas, world economy, metadata). Argument details and REST equivalents: [mcp-tools.md](../mcp-tools.md).

Recommended: add the hosted URL and **sign in with Console**. No JWT in the config file. Use a JWT or local RapidAPI OpenAPI MCP only when the client cannot complete OAuth.

Plans that include MCP: **Basic** (testing), **Ultra** / **Mega** (production). **Pro does not include MCP**. Get a Console account at https://console.tvapis.com/start.

Do **not** send a Console API key or RapidAPI key to `https://mcp.tradingviewapi.com/mcp`. The hosted URL accepts Console OAuth or an MCP JWT from `POST /api/mcp/generate`.

## Install (OAuth)

Per-IDE one-click links, CLI commands, and JSON configs (Cursor, VS Code, Claude Code, Claude Desktop, Codex, Gemini, Windsurf): **[mcp-install.md](../mcp-install.md)**.

After install, the first connection opens Console in the browser. The client stores refresh credentials. Older clients may use `"type": "streamable-http"` instead of `"http"`. Transport is Streamable HTTP (JSON-RPC 2.0): POST for `initialize` / `tools/list` / `tools/call`; GET opens the MCP session SSE stream (not market quote streaming).

## JWT fallback

Use when the client cannot complete OAuth, when testing at https://www.tradingviewapi.com/mcp-test/, or when a RapidAPI subscriber wants the hosted `tradingview_*` tools.

`POST /api/mcp/generate`

Console:

```bash
curl --request POST \
	--url 'https://api.tradingviewapi.com/api/mcp/generate' \
	--header 'Content-Type: application/json' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--data '{}'
```

RapidAPI:

```bash
curl -X POST https://tradingview-data1.p.rapidapi.com/api/mcp/generate \
  -H "x-rapidapi-host: tradingview-data1.p.rapidapi.com" \
  -H "x-rapidapi-key: YOUR_RAPIDAPI_KEY"
```

Response includes `token`, `mcpUrl`, `expiresIn` (Basic 30 minutes, Ultra 15 days, Mega 30 days), `exampleConfig` (`type: http`), and `exampleConfigStreamableHttp`.

Put the JWT on the **hosted** URL. OAuth clients set headers for you. Manual JWT headers:

```
Content-Type: application/json
Accept: application/json, text/event-stream
mcp-protocol-version: 2025-03-26
Authorization: Bearer YOUR_TOKEN
```

```json
{
  "mcpServers": {
    "tradingview": {
      "type": "http",
      "url": "https://mcp.tradingviewapi.com/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN_HERE",
        "Accept": "application/json, text/event-stream"
      }
    }
  }
}
```

OAuth refresh renews the session. Manual JWTs must be regenerated before `expiresAt`. `POST /api/mcp/generate` caps: Basic 50 / month, Ultra 1,000 / month, Mega unlimited. Hosted MCP tool calls are not billed as REST quota.

## Local OpenAPI MCP (RapidAPI only)

For RapidAPI subscribers without Console. Local `npx` process, RapidAPI quota, OpenAPI tool names — **not** hosted `tradingview_*`. Cursor / VS Code / Claude should use the hosted install above instead.

```json
{
  "mcpServers": {
    "tradingview-data": {
      "command": "npx",
      "args": ["-y", "@ivotoby/openapi-mcp-server"],
      "env": {
        "API_BASE_URL": "https://tradingview-data1.p.rapidapi.com",
        "OPENAPI_SPEC_PATH": "https://www.tradingviewapi.com/openapi.json",
        "API_HEADERS": "x-rapidapi-host:tradingview-data1.p.rapidapi.com,x-rapidapi-key: YOUR_RAPIDAPI_KEY"
      }
    }
  }
}
```
