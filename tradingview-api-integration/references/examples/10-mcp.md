# MCP

- Source: `openapi.json`
- Live Requests: `disabled`

## Generate MCP JWT Token

`POST /api/mcp/generate`

### Request

```bash
curl --request POST \
	--url 'https://api.tradingviewapi.com/api/mcp/generate' \
	--header 'Content-Type: application/json' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--data '{"token-jwt-type": 2, "userId": "user123"}'
```

### Response

OpenAPI example / fallback

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
