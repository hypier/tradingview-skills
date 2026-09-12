# ETF Holdings

- Source: `openapi.json`
- Live Requests: `disabled`

ETF AUM, NAV, expense ratio, and top holdings. This is not `GET /api/market-data/{symbol}/related/etfs`, which lists related ETF tickers.

MCP: `tradingview_get_etf`.

## Get ETF Profile

`GET /api/etf/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://api.tradingviewapi.com/api/etf/AMEX:SPY?limit=20' \
	--header 'Authorization: Bearer YOUR_API_KEY'
```

### Response

```json
{
  "success": true,
  "data": {
    "symbol": "AMEX:SPY",
    "is_etf": true,
    "aum": 804000000000,
    "nav": 757.82,
    "nav_discount_premium": 0.01,
    "expense_ratio": 0.0945,
    "holdings_count": 505,
    "holdings": [
      {
        "name": "NVIDIA Corp",
        "symbol": "NVDA",
        "weight": 8.08,
        "shares": 1200,
        "change_1m": 0.12
      }
    ],
    "region_exposure": [{ "name": "United States", "weight": 99.4 }],
    "asset_type_exposure": [{ "name": "Equity", "weight": 100 }],
    "issuer": "State Street",
    "brand": "SPDR",
    "launch_date": 19930122,
    "index_tracked": "S&P 500",
    "focus": "Large Cap"
  },
  "msg": "Success"
}
```

Non-ETF symbols return HTTP 200 with `"is_etf": false` and an empty holdings list. `limit` defaults to 20 and caps at 100; `holdings_count` is the full count. QQQ is `NASDAQ:QQQ`, not `AMEX:QQQ`.
