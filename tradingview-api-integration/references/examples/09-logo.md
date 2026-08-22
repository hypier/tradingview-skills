# Logo Proxy

- Source: `openapi.json`
- Live Requests: `disabled`

## Proxy TradingView Logo by URL

`GET /logo`

### Request

```bash
curl --request GET \
	--url 'https://api.tradingviewapi.com/logo?url=apple.svg&big=true' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
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
	--url 'https://api.tradingviewapi.com/logo/apple.svg' \
	--header 'Authorization: Bearer YOUR_API_KEY' \
	--output apple.svg
```

### Response

OpenAPI example / fallback

```text
[binary image response: image/svg+xml or image/png]
```
