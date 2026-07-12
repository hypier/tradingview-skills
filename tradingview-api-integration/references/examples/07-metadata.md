# Metadata

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get Market List](#get-market-list)
- [Get World Economy Indicator Metadata](#get-world-economy-indicator-metadata)
- [Get Tab Metadata](#get-tab-metadata)
- [Get Columnset Metadata](#get-columnset-metadata)
- [Get Language List](#get-language-list)
- [Get Exchange List](#get-exchange-list)

## Get Market List

`GET /api/metadata/markets`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/markets' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": [
    "america",
    "canada",
    "austria"
  ],
  "msg": "Success"
}
```

## Get World Economy Indicator Metadata

`GET /api/metadata/world-economy/indicators`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/world-economy/indicators?category=gdp' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "total": 25,
    "category": [
      "gdp"
    ],
    "categories": [
      {
        "category": "bsnss",
        "label": "Business"
      },
      {
        "category": "clmt",
        "label": "Climate"
      },
      {
        "category": "cnsm",
        "label": "Consumer"
      }
    ],
    "indicators": [
      {
        "slug": "economic-activity-index",
        "label": "Economic Activity Index",
        "categories": [
          "gdp"
        ]
      },
      {
        "slug": "full-year-gdp-growth",
        "label": "Full Year GDP Growth",
        "categories": [
          "gdp"
        ]
      },
      {
        "slug": "gdp",
        "label": "GDP",
        "categories": [
          "gdp"
        ]
      }
    ]
  },
  "msg": "Success"
}
```

## Get Tab Metadata

`GET /api/metadata/tabs`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/tabs?type=stocks' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": [
    {
      "id": "stocks_market_movers.all_stocks",
      "path": "all_stocks",
      "url": "/markets/stocks-china/market-movers-all-stocks/",
      "title": "All stocks",
      "type": "stocks"
    },
    {
      "id": "stocks_market_movers.gainers",
      "path": "gainers",
      "url": "/markets/stocks-china/market-movers-gainers/",
      "title": "Top gainers",
      "type": "stocks"
    },
    {
      "id": "stocks_market_movers.losers",
      "path": "losers",
      "url": "/markets/stocks-china/market-movers-losers/",
      "title": "Biggest losers",
      "type": "stocks"
    }
  ],
  "msg": "Success"
}
```

## Get Columnset Metadata

`GET /api/metadata/columnsets`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/columnsets' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": [
    {
      "type": "stocks",
      "columnsets": [
        "overview",
        "performance",
        "valuation"
      ]
    },
    {
      "type": "indices",
      "columnsets": [
        "overview",
        "performance",
        "technicals"
      ]
    },
    {
      "type": "crypto",
      "columnsets": [
        "overview",
        "performance",
        "valuation"
      ]
    }
  ],
  "msg": "Success"
}
```

## Get Language List

`GET /api/metadata/languages`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/languages' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": [
    {
      "code": "en",
      "name": "English"
    },
    {
      "code": "zh_CN",
      "name": "简体中文"
    },
    {
      "code": "de",
      "name": "Deutsch"
    }
  ],
  "msg": "Success"
}
```

## Get Exchange List

`GET /api/metadata/exchanges`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/metadata/exchanges' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalExchanges": 353,
    "exchanges": [
      {
        "name": "LBank",
        "value": "LBANK",
        "desc": "LBank",
        "flag": "bitcoin",
        "group": "Cryptocurrency",
        "country": "",
        "provider_id": "lbank"
      },
      {
        "name": "LFJ V2.2 (Avalanche)",
        "value": "LFJ2DOT2",
        "desc": "LFJ V2.2 (Avalanche)",
        "flag": "bitcoin",
        "group": "Cryptocurrency",
        "country": "",
        "provider_id": "lfj2dot2"
      },
      {
        "name": "BCHAIN (Nasdaq Data Link)",
        "value": "BCHAIN",
        "desc": "BCHAIN (Nasdaq Data Link)",
        "flag": "bitcoin",
        "group": "Cryptocurrency",
        "country": "",
        "provider_id": "quandl_bchain"
      }
    ]
  },
  "msg": "Success"
}
```
