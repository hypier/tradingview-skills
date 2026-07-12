# Logo Proxy

- Source: `openapi.json`
- Live Requests: `disabled`

## Proxy TradingView Logo by URL

`GET /logo`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/logo?url=apple.svg&big=true' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--output apple.svg
```

### Response

OpenAPI example / fallback

```text
[binary image response: image/svg+xml or image/png]
```

## Proxy TradingView Logo by Path

`GET /logo/{path}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/logo/apple.svg' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--output apple.svg
```

### Response

OpenAPI example / fallback

```text
[binary image response: image/svg+xml or image/png]
```
