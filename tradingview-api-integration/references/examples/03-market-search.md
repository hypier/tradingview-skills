# Market Search

- Source: `openapi.json`
- Live Requests: `disabled`

## Search Markets

`GET /api/search/market/{query}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/search/market/AAPL?filter=stock' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "markets": [
      {
        "symbol": "AAPL",
        "description": "Apple Inc.",
        "type": "stock",
        "exchange": "NASDAQ",
        "found_by_isin": false,
        "found_by_cusip": false,
        "cusip": "037833100",
        "isin": "US0378331005",
        "cik_code": "0000320193",
        "currency_code": "USD",
        "currency-logoid": "country/US",
        "logoid": "apple",
        "logo": {
          "style": "single",
          "logoid": "apple"
        },
        "provider_id": "ice",
        "source_logoid": "source/NASDAQ",
        "source2": {
          "id": "NASDAQ",
          "name": "Nasdaq Stock Market",
          "description": "Nasdaq Stock Market"
        },
        "source_id": "NASDAQ",
        "country": "US",
        "is_primary_listing": true,
        "typespecs": [
          "common"
        ],
        "id": "NASDAQ:AAPL",
        "fullExchange": "NASDAQ",
        "full_name": "NASDAQ:AAPL"
      },
      {
        "symbol": "AAPL",
        "description": "APPLE INC / US DOLLAR",
        "type": "stock",
        "exchange": "Pyth",
        "found_by_isin": false,
        "found_by_cusip": false,
        "currency_code": "USD",
        "currency-logoid": "country/US",
        "provider_id": "pyth",
        "source_logoid": "provider/pyth",
        "source2": {
          "id": "PYTH",
          "name": "Pyth",
          "description": "Pyth"
        },
        "source_id": "PYTH",
        "typespecs": [
          "crypto",
          "oracle"
        ],
        "prefix": "PYTH",
        "id": "PYTH:AAPL",
        "fullExchange": "Pyth",
        "full_name": "PYTH:AAPL"
      },
      {
        "symbol": "AAPL",
        "description": "Apple Inc. Shs Cert Deposito Arg Repr 0.05 Shs",
        "type": "dr",
        "exchange": "BYMA",
        "found_by_isin": false,
        "found_by_cusip": false,
        "isin": "ARDEUT116183",
        "currency_code": "ARS",
        "currency-logoid": "country/AR",
        "logoid": "apple",
        "logo": {
          "style": "single",
          "logoid": "apple"
        },
        "provider_id": "ice",
        "source_logoid": "source/BCBA",
        "source2": {
          "id": "BCBA",
          "name": "Buenos Aires Stock Exchange",
          "description": "Buenos Aires Stock Exchange"
        },
        "source_id": "BCBA",
        "country": "AR",
        "prefix": "BCBA",
        "id": "BCBA:AAPL",
        "fullExchange": "BYMA",
        "full_name": "BCBA:AAPL"
      }
    ],
    "count": 50
  },
  "msg": "Success"
}
```
