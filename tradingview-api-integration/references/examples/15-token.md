# Token

- Source: `openapi.json`
- Live Requests: `disabled`

## Generate JWT Token

`POST /api/token/generate`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/token/generate' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
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
  "wsUrl": "ws://localhost:8080",
  "sseUrl": "https://ws.tradingviewapi.com/sse/stream",
  "sseExample": "curl --location 'https://ws.tradingviewapi.com/sse/stream?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY3Njc2NzMsImV4cCI6MTc3Njc2OTQ3Mywic291cmNlIjoid3Mtand0IiwidXNlcklkIjoidXNlcl8xNzc2NzY3NjczNzczX3AwcGFtMHJ6ZiJ9.H60ARnQ1EAVfwI0rHznQgehmz-_ZMHxWqtz-jZJwflU&symbols=BINANCE:BTCUSDT,BINANC... (10 more chars truncated)"
}
```
