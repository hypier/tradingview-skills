# Token

- Source: `openapi.json`
- Live Requests: `disabled`

This JWT is for SSE and WebSocket only. Connect to `ws.tradingviewapi.com` — see `11-websocket.md`. Do not use this token as a REST `Authorization` header.

## Generate JWT Token

`POST /api/token/generate`

### Request

```bash
curl --request POST \
	--url 'https://api.tradingviewapi.com/api/token/generate' \
	--header 'Content-Type: application/json' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--data '{}'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY3Njc2NzMsImV4cCI6MTc3Njc2OTQ3Mywic291cmNlIjoid3Mtand0IiwidXNlcklkIjoidXNlcl8xNzc2NzY3NjczNzczX3AwcGFtMHJ6ZiJ9.H60ARnQ1EAVfwI0rHznQgehmz-_ZMHxWqtz-jZJwflU",
  "expiresIn": "30 minutes",
  "expiresAt": 1776769473000,
  "wsUrl": "wss://ws.tradingviewapi.com/ws",
  "sseUrl": "https://ws.tradingviewapi.com/sse/stream",
  "sseExample": "curl --location 'https://ws.tradingviewapi.com/sse/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY3Njc2NzMsImV4cCI6MTc3Njc2OTQ3Mywic291cmNlIjoid3Mtand0IiwidXNlcklkIjoidXNlcl8xNzc2NzY3NjczNzczX3AwcGFtMHJ6ZiJ9.H60ARnQ1EAVfwI0rHznQgehmz-_ZMHxWqtz-jZJwflU&symbols=BINANCE:BTCUSDT,BINANC... (10 more chars truncated)"
}
```
