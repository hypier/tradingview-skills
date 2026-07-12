# World Economy

- Source: `openapi.json`
- Live Requests: `disabled`

## Get World Economy Indicator Rankings

`GET /api/world-economy/indicators/{indicator}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/world-economy/indicators/full-year-gdp-growth?region=g20' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "indicator": "full-year-gdp-growth",
    "region": "g20",
    "total": 20,
    "rows": [
      {
        "symbol": "INFYGDPG",
        "full_symbol": "ECONOMICS:INFYGDPG",
        "name": "India Full Year GDP Growth",
        "country_code": "IN",
        "logoid": "country/IN",
        "latest": 7.6,
        "previous": 7.1,
        "observation": "2026",
        "unit": "Percent",
        "frequency": "Annual"
      },
      {
        "symbol": "IDFYGDPG",
        "full_symbol": "ECONOMICS:IDFYGDPG",
        "name": "Indonesia Full Year GDP Growth",
        "country_code": "ID",
        "logoid": "country/ID",
        "latest": 5.11,
        "previous": 5.03,
        "observation": "2025",
        "unit": "Percent",
        "frequency": "Annual"
      },
      {
        "symbol": "CNFYGDPG",
        "full_symbol": "ECONOMICS:CNFYGDPG",
        "name": "China Full Year GDP Growth",
        "country_code": "CN",
        "logoid": "country/CN",
        "latest": 5,
        "previous": 5,
        "observation": "2025",
        "unit": "Percent",
        "frequency": "Annual"
      }
    ]
  },
  "msg": "Success"
}
```
