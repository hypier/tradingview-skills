# Calendar

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get Economic Calendar Events](#get-economic-calendar-events)
- [Get Earnings Calendar](#get-earnings-calendar)
- [Get Revenue Calendar](#get-revenue-calendar)
- [Get IPO Calendar](#get-ipo-calendar)

## Get Economic Calendar Events

`GET /api/calendar/economic`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/calendar/economic?from=1781193600&to=1781798400&market=america' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "status": "ok",
    "result": [
      {
        "id": "397829",
        "title": "ADP Employment Change Weekly",
        "country": "US",
        "indicator": "ADP Employment Change Weekly",
        "comment": "The preliminary estimate of the ADP National Employment Report reflects weekly changes in private employment and includes a four-week moving average of total private employment variation.",
        "category": "lbr",
        "period": "",
        "referenceDate": "2026-04-04T00:00:00Z",
        "source": "Automatic Data Processing, Inc.",
        "source_url": "https://adpemploymentreport.com/",
        "actual": null,
        "previous": 39,
        "forecast": null,
        "actualRaw": null,
        "previousRaw": 39000,
        "forecastRaw": null,
        "currency": "USD",
        "scale": "K",
        "importance": 0,
        "date": "2026-04-21T12:15:00.000Z"
      },
      {
        "id": "397925",
        "title": "Retail Sales MoM",
        "country": "US",
        "indicator": "Retail Sales MoM",
        "ticker": "ECONOMICS:USRSMM",
        "comment": "Retail sales report in the US provides aggregated measure of sales of retail goods and services over a period of a month. There are thirteen major types of retailers: Motor vehicle & parts dealers (20% of total sales), Nonstore retailers (17%), Food services & drinking places (14%), Food & beverage ... (384 more chars truncated)",
        "category": "cnsm",
        "period": "Mar",
        "referenceDate": "2026-03-31T00:00:00Z",
        "source": "Census Bureau",
        "source_url": "https://www.census.gov/",
        "actual": null,
        "previous": 0.6,
        "forecast": 1.4,
        "actualRaw": null,
        "previousRaw": 0.6,
        "forecastRaw": 1.4,
        "currency": "USD",
        "unit": "%",
        "importance": 1,
        "date": "2026-04-21T12:30:00.000Z"
      },
      {
        "id": "398445",
        "title": "Retail Sales Ex Autos MoM",
        "country": "US",
        "indicator": "Retail Sales Ex Autos",
        "ticker": "ECONOMICS:USRSEA",
        "comment": "Retail Sales Ex Autos report in the US provides aggregated measure of sales of retail goods and services excluding the automobile sector over a period of a month.",
        "category": "cnsm",
        "period": "Mar",
        "referenceDate": "2026-03-31T00:00:00Z",
        "source": "Census Bureau",
        "source_url": "http://www.census.gov",
        "actual": null,
        "previous": 0.5,
        "forecast": 1.4,
        "actualRaw": null,
        "previousRaw": 0.5,
        "forecastRaw": 1.4,
        "currency": "USD",
        "unit": "%",
        "importance": 0,
        "date": "2026-04-21T12:30:00.000Z"
      }
    ]
  },
  "msg": "Success"
}
```

## Get Earnings Calendar

`GET /api/calendar/earnings`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/calendar/earnings?from=1781193600&to=1781798400&market=america' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 741,
    "data": [
      {
        "symbol": "NYSE:PIPR",
        "rank": 1,
        "earnings_release_next_date": 1777032000,
        "earnings_release_date": 1770379200,
        "logoid": "",
        "name": "PIPR",
        "description": "Piper Sandler Companies",
        "earnings_per_share_fq": 1.72,
        "earnings_per_share_forecast_next_fq": 0.909375,
        "eps_surprise_fq": 0.534375,
        "eps_surprise_percent_fq": 45.071164997364264,
        "revenue_fq": 634997000,
        "revenue_forecast_next_fq": 436301500,
        "market_cap_basic": 6498773097.999999,
        "earnings_release_time": -1,
        "earnings_release_next_time": 0,
        "earnings_per_share_forecast_fq": 1.185625,
        "revenue_forecast_fq": 518164500,
        "fundamental_currency_code": "USD",
        "market": "america",
        "earnings_publication_type_fq": 21,
        "earnings_publication_type_next_fq": 10,
        "revenue_surprise_fq": 116832500,
        "revenue_surprise_percent_fq": 22.547376364069713,
        "typespecs": [
          "common"
        ],
        "type": "stock",
        "exchange": "NYSE"
      },
      {
        "symbol": "NASDAQ:NICM",
        "rank": 2,
        "earnings_release_next_date": 1777032000,
        "earnings_release_date": 1764757800,
        "logoid": "",
        "name": "NICM",
        "description": "Nicola Mining Inc.",
        "earnings_per_share_fq": -0.014338,
        "earnings_per_share_forecast_next_fq": 0.014615,
        "eps_surprise_fq": -0.028596,
        "eps_surprise_percent_fq": -200.5610885117127,
        "revenue_fq": 396216,
        "revenue_forecast_next_fq": 7205743,
        "market_cap_basic": 129028547.0272,
        "earnings_release_time": -1,
        "earnings_release_next_time": 0,
        "earnings_per_share_forecast_fq": 0.014258,
        "revenue_forecast_fq": 5478025,
        "fundamental_currency_code": "USD",
        "market": "america",
        "earnings_publication_type_fq": 21,
        "earnings_publication_type_next_fq": 10,
        "revenue_surprise_fq": -5081809,
        "revenue_surprise_percent_fq": -92.767174300957,
        "typespecs": [
          ""
        ],
        "type": "dr",
        "exchange": "NASDAQ"
      },
      {
        "symbol": "NASDAQ:PSTV",
        "rank": 3,
        "earnings_release_next_date": 1776772800,
        "earnings_release_date": 1773346560,
        "logoid": "",
        "name": "PSTV",
        "description": "PLUS THERAPEUTICS, Inc.",
        "earnings_per_share_fq": -0.833575,
        "earnings_per_share_forecast_next_fq": -0.846,
        "eps_surprise_fq": -0.03357499999999991,
        "eps_surprise_percent_fq": -4.196874999999989,
        "revenue_fq": 1363000,
        "revenue_forecast_next_fq": 974000,
        "market_cap_basic": 50092796,
        "earnings_release_time": 1,
        "earnings_release_next_time": 0,
        "earnings_per_share_forecast_fq": -0.8,
        "revenue_forecast_fq": 1232000,
        "fundamental_currency_code": "USD",
        "market": "america",
        "earnings_publication_type_fq": 22,
        "earnings_publication_type_next_fq": 10,
        "revenue_surprise_fq": 131000,
        "revenue_surprise_percent_fq": 10.633116883116884,
        "typespecs": [
          "common"
        ],
        "type": "stock",
        "exchange": "NASDAQ"
      }
    ]
  },
  "msg": "Success"
}
```

## Get Revenue Calendar

`GET /api/calendar/revenue`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/calendar/revenue?from=1781193600&to=1781798400&market=america' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 328,
    "data": [
      {
        "symbol": "OTC:RMVEY",
        "rank": 1,
        "dividend_ex_date_recent": 1758887940,
        "dividend_ex_date_upcoming": 1777031940,
        "logoid": "",
        "name": "RMVEY",
        "description": "Rightmove Plc",
        "dividends_yield": 1.7863514064410926,
        "dividend_payment_date_recent": 1762775940,
        "dividend_payment_date_upcoming": 1779969540,
        "dividend_amount_recent": 0.0860930011,
        "dividend_amount_upcoming": 0.178930998,
        "fundamental_currency_code": "USD",
        "market": "america",
        "typespecs": [
          ""
        ],
        "type": "dr",
        "exchange": "OTC"
      },
      {
        "symbol": "NASDAQ:QFIN",
        "rank": 2,
        "dividend_ex_date_recent": 1757332740,
        "dividend_ex_date_upcoming": 1776859140,
        "logoid": "360-finance",
        "name": "QFIN",
        "description": "Qfin Holdings, Inc.",
        "dividends_yield": 10.849393290506782,
        "dividend_payment_date_recent": 1759233540,
        "dividend_payment_date_upcoming": 1778759940,
        "dividend_amount_recent": 0.75,
        "dividend_amount_upcoming": 0.769999981,
        "fundamental_currency_code": "USD",
        "market": "america",
        "typespecs": [
          ""
        ],
        "type": "dr",
        "exchange": "NASDAQ"
      },
      {
        "symbol": "OTC:AAVMY",
        "rank": 3,
        "dividend_ex_date_recent": 1755518340,
        "dividend_ex_date_upcoming": 1777291140,
        "logoid": "abn-amro",
        "name": "AAVMY",
        "description": "Abn Amro BK N V",
        "dividends_yield": 3.2728889139760664,
        "dividend_payment_date_recent": 1758715140,
        "dividend_payment_date_upcoming": 1780919940,
        "dividend_amount_recent": 0.487489015,
        "dividend_amount_upcoming": 0.868694007,
        "fundamental_currency_code": "USD",
        "market": "america",
        "typespecs": [
          ""
        ],
        "type": "dr",
        "exchange": "OTC"
      }
    ]
  },
  "msg": "Success"
}
```

## Get IPO Calendar

`GET /api/calendar/ipo`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/calendar/ipo?from=1781193600&to=1781798400&market=america' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 3,
    "data": [
      {
        "symbol": "NYSE:EMI",
        "rank": 1,
        "logoid": "encore-medical",
        "name": "EMI",
        "description": "Encore Medical Inc.",
        "typespecs": [
          "common",
          "pre-ipo"
        ],
        "type": "stock",
        "exchange": "NYSE",
        "market": "america",
        "ipo_offer_time": 1776864600,
        "ipo_offer_price_usd": null,
        "ipo_offer_status": "pending",
        "ipo_offer_status.tr": "Pending",
        "ipo_offered_shares": 3000000,
        "ipo_deal_amount_usd": 15000000,
        "ipo_market_cap_usd": null,
        "ipo_price_range_usd": null,
        "source-logoid": "source/NYSE"
      },
      {
        "symbol": "NASDAQ:YSWY",
        "rank": 2,
        "logoid": "",
        "name": "YSWY",
        "description": "Yesway Inc.",
        "typespecs": [
          "common",
          "pre-ipo"
        ],
        "type": "stock",
        "exchange": "NASDAQ",
        "market": "america",
        "ipo_offer_time": 1776864600,
        "ipo_offer_price_usd": null,
        "ipo_offer_status": "pending",
        "ipo_offer_status.tr": "Pending",
        "ipo_offered_shares": 13953488,
        "ipo_deal_amount_usd": 320930224,
        "ipo_market_cap_usd": null,
        "ipo_price_range_usd": "20.00 - 23.00",
        "source-logoid": "source/NASDAQ"
      },
      {
        "symbol": "NASDAQ:OPTHFU",
        "rank": 3,
        "logoid": "optimi-health",
        "name": "OPTHFU",
        "description": "Optimi Health Corp.",
        "typespecs": [
          "common",
          "pre-ipo"
        ],
        "type": "stock",
        "exchange": "NASDAQ",
        "market": "america",
        "ipo_offer_time": 1776951000,
        "ipo_offer_price_usd": null,
        "ipo_offer_status": "pending",
        "ipo_offer_status.tr": "Pending",
        "ipo_offered_shares": 2500000,
        "ipo_deal_amount_usd": 20000000,
        "ipo_market_cap_usd": null,
        "ipo_price_range_usd": "6.00 - 8.00",
        "source-logoid": "source/NASDAQ"
      }
    ]
  },
  "msg": "Success"
}
```
