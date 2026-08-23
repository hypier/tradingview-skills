# MCP

- Source: `openapi.json`
- Live Requests: `disabled`

Recommended for Cursor / VS Code / Claude: add the hosted URL with `"type": "http"` and sign in with Console. No JWT in the config file.

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

Older clients may use `"type": "streamable-http"` instead of `"http"`. The URL is the same.

This example mints a JWT for clients that cannot complete OAuth, the MCP tester, or RapidAPI users who want the hosted `tradingview_*` tools. RapidAPI subscribers can also run a local OpenAPI MCP with `npx -y @ivotoby/openapi-mcp-server` (OpenAPI tools, not hosted `tradingview_*`).

## Generate MCP JWT Token

`POST /api/mcp/generate`

### Request

Console:

```bash
curl --request POST \
	--url 'https://api.tradingviewapi.com/api/mcp/generate' \
	--header 'Content-Type: application/json' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--data '{"token-jwt-type": 2, "userId": "user123"}'
```

RapidAPI:

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/mcp/generate' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"token-jwt-type": 2, "userId": "user123"}'
```

### Response

OpenAPI example / fallback. `exampleConfig` uses `"type": "http"` (Cursor / VS Code). Older clients can copy `exampleConfigStreamableHttp`.

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY2OTYyMDUsImV4cCI6MTc3Nzk5MjIwNSwic291cmNlIjoibWNwLWp3dCIsInVzZXJJZCI6InVzZXIxMjMifQ.lN6USNXNryLZ36mD9PqmivsfwBok0lUQu6nEq7cua_Q",
  "expiresIn": "15 days",
  "expiresAt": 1777992205000,
  "mcpUrl": "http://localhost:3001/mcp",
  "exampleConfig": {
    "mcpServers": {
      "tradingview": {
        "type": "http",
        "url": "http://localhost:3001/mcp",
        "headers": {
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY2OTYyMDUsImV4cCI6MTc3Nzk5MjIwNSwic291cmNlIjoibWNwLWp3dCIsInVzZXJJZCI6InVzZXIxMjMifQ.lN6USNXNryLZ36mD9PqmivsfwBok0lUQu6nEq7cua_Q",
          "Accept": "application/json, text/event-stream"
        }
      }
    }
  },
  "exampleConfigStreamableHttp": {
    "mcpServers": {
      "tradingview": {
        "type": "streamable-http",
        "url": "http://localhost:3001/mcp",
        "headers": {
          "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY2OTYyMDUsImV4cCI6MTc3Nzk5MjIwNSwic291cmNlIjoibWNwLWp3dCIsInVzZXJJZCI6InVzZXIxMjMifQ.lN6USNXNryLZ36mD9PqmivsfwBok0lUQu6nEq7cua_Q",
          "Accept": "application/json, text/event-stream"
        }
      }
    }
  }
}
```
