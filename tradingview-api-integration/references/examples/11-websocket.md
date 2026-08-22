# Streaming

- Source: `openapi.json`
- Live Requests: `disabled`

## Open SSE Stream

`GET /sse/stream`

### Request

```bash
curl --request GET \
	--url 'https://api.tradingviewapi.com/sse/stream?symbols=NASDAQ%3AAAPL%2CBINANCE%3ABTCUSDT&type=quote' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--no-buffer
```

### Response

OpenAPI example / fallback

```text
data: {"type":"connected","clientId":"sse_123","symbols":["NASDAQ:AAPL"],"timestamp":1234567890}

data: {"type":"quote_update","symbol":"NASDAQ:AAPL","data":{"lp":150.25},"timestamp":1234567890}
```
