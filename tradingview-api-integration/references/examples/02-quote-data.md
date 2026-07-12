# Quote Data

- Source: `openapi.json`
- Live Requests: `disabled`

## Get Batch Quotes

`POST /api/quote/batch`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/quote/batch' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"symbols":["BINANCE:BTCUSDT","BINANCE:ETHUSDT"],"session":"regular","fields":"all"}'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "total": 2,
    "successful": 2,
    "failed": 0,
    "data": [
      {
        "success": true,
        "symbol": "BINANCE:BTCUSDT",
        "data": {
          "bid": 76513.71,
          "ask": 76513.72,
          "type": "spot",
          "update_mode": "streaming",
          "price_52_week_high": 126199.63,
          "short_name": "BTCUSDT",
          "pro_name": "BINANCE:BTCUSDT",
          "rchp": null,
          "provider_id": "binance",
          "currency_code": "USDT",
          "ch": 672.74,
          "current_session": "market",
          "low_price": 75474.77,
          "fractional": false,
          "lp_time": 1776767645,
          "rch": null,
          "prev_close_price": 75840.97,
          "rtc": null,
          "price_percent_change_52_week": -10.994979527875573,
          "rtc_time": null,
          "currency-logoid": "crypto/XTVCUSDT",
          "volume": 5596.58292,
          "all_time_high": 126199.63,
          "description": "Bitcoin / TetherUS",
          "chp": 0.89,
          "minmov": 1,
          "original_name": "BINANCE:BTCUSDT",
          "average_volume": 16106.735055000001,
          "price_52_week_low": 60000,
          "high_price": 76927.57,
          "format": "price",
          "open_price": 75840.97,
          "is_tradable": true,
          "exchange": "Binance",
          "base-currency-logoid": "crypto/XTVCBTC",
          "pricescale": 100,
          "all_time_low": 2817,
          "minmove2": 0,
          "timezone": "Etc/UTC",
          "lp": 76513.71
        }
      },
      {
        "success": true,
        "symbol": "BINANCE:ETHUSDT",
        "data": {
          "bid": 2328.82,
          "ask": 2328.83,
          "type": "spot",
          "update_mode": "streaming",
          "price_52_week_high": 4956.78,
          "short_name": "ETHUSDT",
          "pro_name": "BINANCE:ETHUSDT",
          "rchp": null,
          "provider_id": "binance",
          "currency_code": "USDT",
          "ch": 14.98,
          "current_session": "market",
          "low_price": 2300.01,
          "fractional": false,
          "lp_time": 1776767645,
          "rch": null,
          "prev_close_price": 2313.85,
          "rtc": null,
          "price_percent_change_52_week": 45.81380405201091,
          "rtc_time": null,
          "currency-logoid": "crypto/XTVCUSDT",
          "volume": 63494.7373,
          "all_time_high": 4956.78,
          "description": "Ethereum / TetherUS",
          "chp": 0.65,
          "minmov": 1,
          "original_name": "BINANCE:ETHUSDT",
          "average_volume": 306645.37034,
          "price_52_week_low": 1722.9,
          "high_price": 2338.75,
          "format": "price",
          "open_price": 2313.84,
          "is_tradable": true,
          "exchange": "Binance",
          "base-currency-logoid": "crypto/XTVCETH",
          "pricescale": 100,
          "all_time_low": 81.79,
          "minmove2": 0,
          "timezone": "Etc/UTC",
          "lp": 2328.83
        }
      }
    ]
  },
  "msg": "Success"
}
```

## Get Quote

`GET /api/quote/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/quote/NASDAQ:AAPL?session=regular&fields=all' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "symbol": "NASDAQ:AAPL",
    "data": {
      "bid": 272.15,
      "ask": 272.3,
      "earnings_per_share_basic_ttm": 7.9334,
      "type": "stock",
      "update_mode": "streaming",
      "price_52_week_high": 288.62,
      "local_description": "Apple Inc.",
      "short_name": "AAPL",
      "pro_name": "NASDAQ:AAPL",
      "rchp": -0.3,
      "provider_id": "ice",
      "currency_code": "USD",
      "ceo": "Timothy Donald Cook",
      "ch": 2.82,
      "current_session": "pre_market",
      "language": "en",
      "total_shares_outstanding_current": 14681100000,
      "low_price": 270.29,
      "fractional": false,
      "lp_time": 1776729598,
      "rch": -0.81,
      "prev_close_price": 270.23,
      "rtc": 272.24,
      "price_percent_change_52_week": 38.4634888438134,
      "rtc_time": 1776767619,
      "currency-logoid": "country/US",
      "total_revenue": 416161000000,
      "volume": 36590169,
      "earnings_release_date": 1769722200,
      "all_time_high": 288.62,
      "description": "Apple Inc.",
      "sector": "Electronic Technology",
      "logoid": "apple",
      "recommendation_mark": 1.443396,
      "beta_1_year": 1.1557966,
      "chp": 1.04,
      "minmov": 1,
      "original_name": "BATS:AAPL",
      "average_volume": 43846173.29999931,
      "market_cap_basic": 4008685001793,
      "price_52_week_low": 193.25,
      "web_site_url": "http://www.apple.com",
      "high_price": 274.275,
      "price_earnings_ttm": 34.18988334725069,
      "industry": "Telecommunications Equipment",
      "open_price": 270.33,
      "is_tradable": true,
      "business_description": "Apple, Inc. engages in the design, manufacture, and sale of smartphones, personal computers, tablets, wearables and accessories, and other varieties of related services. It operates through the following geographical segments: Americas, Europe, Greater China, Japan, and Rest of Asia Pacific. The Ame... (605 more chars truncated)",
      "price_earnings": 34.18988334725069,
      "exchange": "Cboe One",
      "pricescale": 100,
      "all_time_low": 0.049107,
      "minmove2": 0,
      "timezone": "America/New_York",
      "lp": 273.05,
      "earnings_release_next_date": 1777581000,
      "founded": 1976,
      "dividends_yield": 0.38088262223036073,
      "country_code": "US",
      "basic_eps_net_income": 7.4931
    }
  },
  "msg": "Success"
}
```
