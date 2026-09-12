# Options Chain

- Source: `openapi.json`
- Live Requests: `disabled`

Listed expirations, strikes, and OPRA-style contract codes for an underlying. Directory only — not live bid/ask. Quote a contract with `GET /api/quote/OPRA:AAPL261218C330.0` (`fields=enhanced` for `strike` / `expiration` / `option-type`).

MCP: `tradingview_get_options`.

## Get Option Chain

`GET /api/options/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://api.tradingviewapi.com/api/options/NASDAQ:AAPL?expiration=2026-12-18' \
	--header 'Authorization: Bearer YOUR_API_KEY'
```

### Response

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "has_options": true,
    "families": [
      {
        "name": "AAPL",
        "prefix": "OPRA",
        "exercise": "american",
        "series": [
          {
            "expiration": "2026-12-18",
            "lot_size": 100,
            "strikes": [330, 335],
            "calls": ["OPRA:AAPL261218C330.0", "OPRA:AAPL261218C335.0"],
            "puts": ["OPRA:AAPL261218P330.0", "OPRA:AAPL261218P335.0"]
          }
        ]
      }
    ]
  },
  "msg": "Success"
}
```

`strikes` are dollar strikes, not percents. Contract format: `{prefix}:{root}{YYMMDD}{C|P}{strike}` with integer strikes as `330.0`.

Underlyings without listed options (`BINANCE:BTCUSDT`) return HTTP 200 with `"has_options": false` and `"families": []`. Filter to an expiry that is not listed → `"has_options": true` and `"families": []`.
