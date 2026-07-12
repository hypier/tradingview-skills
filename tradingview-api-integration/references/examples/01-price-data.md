# Price Data

- Source: `openapi.json`
- Live Requests: `enabled`

## Get Price History

`GET /api/price/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/price/BINANCE:BTCUSDT?timeframe=1&range=10' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "symbol": "BINANCE:BTCUSDT",
    "current": {
      "time": 1781237220,
      "open": 63443.36,
      "close": 63439.42,
      "max": 63443.36,
      "min": 63439.41,
      "volume": 5.52
    },
    "history": [
      {
        "time": 1781237220,
        "open": 63443.36,
        "close": 63439.42,
        "max": 63443.36,
        "min": 63439.41,
        "volume": 5.52
      },
      {
        "time": 1781237160,
        "open": 63498.01,
        "close": 63443.36,
        "max": 63498.01,
        "min": 63443.35,
        "volume": 3.73
      },
      {
        "time": 1781237100,
        "open": 63514,
        "close": 63498,
        "max": 63514,
        "min": 63498,
        "volume": 1.58
      },
      "... +7 more items (truncated)"
    ],
    "info": {
      "series_id": "ser_1",
      "source2": {
        "country": "MT",
        "description": "Binance",
        "exchange-type": "exchange",
        "id": "BINANCE",
        "name": "Binance",
        "url": "https://www.binance.com/en"
      },
      "currency_code": "USDT",
      "source_id": "BINANCE",
      "subsession_id": "regular",
      "provider_id": "binance",
      "base_currency_id": "XTVCBTC",
      "base_currency": "BTC",
      "currency_id": "XTVCUSDT",
      "format": "price",
      "formatter": "price",
      "pro_perm": "",
      "volume_type": "base",
      "measure": "price",
      "allowed_adjustment": "none",
      "short_description": "Bitcoin / TetherUS",
      "variable_tick_size": "",
      "name": "BTCUSDT",
      "full_name": "BINANCE:BTCUSDT",
      "pro_name": "BINANCE:BTCUSDT",
      "base_name": [
        "BINANCE:BTCUSDT"
      ],
      "description": "Bitcoin / TetherUS",
      "exchange": "Binance",
      "pricescale": 100,
      "pointvalue": 1,
      "minmov": 1,
      "session": "24x7",
      "session_display": "24x7",
      "subsessions": [
        {
          "description": "Regular Trading Hours",
          "id": "regular",
          "private": false,
          "session": "24x7",
          "session-display": "24x7"
        }
      ],
      "type": "spot",
      "typespecs": [
        "crypto",
        "defi"
      ],
      "has_intraday": true,
      "fractional": false,
      "listed_exchange": "BINANCE",
      "legs": [
        "BINANCE:BTCUSDT"
      ],
      "is_tradable": true,
      "minmove2": 0,
      "timezone": "Etc/UTC",
      "aliases": [],
      "alternatives": [],
      "is_replayable": true,
      "has_adjustment": false,
      "has_extended_hours": false,
      "bar_source": "trade",
      "bar_transform": "none",
      "bar_fillgaps": false,
      "visible_plots_set": "ohlcv",
      "is-tickbars-available": true,
      "exchange_listed_name": "Binance"
    }
  },
  "msg": "Success"
}
```

## Get Batch Price History

`POST /api/price/batch`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/price/batch' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"requests":[{"symbol":"BINANCE:BTCUSDT","timeframe":"60","range":20}]}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "total": 1,
    "successful": 1,
    "failed": 0,
    "data": [
      {
        "success": true,
        "symbol": "BINANCE:BTCUSDT",
        "current": {
          "time": 1781236800,
          "open": 63524.81,
          "close": 63435.36,
          "max": 63524.82,
          "min": 63431.08,
          "volume": 36.92
        },
        "history": [
          {
            "time": 1781236800,
            "open": 63524.81,
            "close": 63435.36,
            "max": 63524.82,
            "min": 63431.08,
            "volume": 36.92
          },
          {
            "time": 1781233200,
            "open": 63624.07,
            "close": 63524.82,
            "max": 63649.99,
            "min": 63357.7,
            "volume": 280.55
          },
          {
            "time": 1781229600,
            "open": 63446.02,
            "close": 63624.07,
            "max": 63779.11,
            "min": 63442.81,
            "volume": 396.72
          },
          "... +17 more items (truncated)"
        ],
        "info": {
          "series_id": "ser_1",
          "source2": {
            "country": "MT",
            "description": "Binance",
            "exchange-type": "exchange",
            "id": "BINANCE",
            "name": "Binance",
            "url": "https://www.binance.com/en"
          },
          "currency_code": "USDT",
          "source_id": "BINANCE",
          "subsession_id": "regular",
          "provider_id": "binance",
          "base_currency_id": "XTVCBTC",
          "base_currency": "BTC",
          "currency_id": "XTVCUSDT",
          "format": "price",
          "formatter": "price",
          "pro_perm": "",
          "volume_type": "base",
          "measure": "price",
          "allowed_adjustment": "none",
          "short_description": "Bitcoin / TetherUS",
          "variable_tick_size": "",
          "name": "BTCUSDT",
          "full_name": "BINANCE:BTCUSDT",
          "pro_name": "BINANCE:BTCUSDT",
          "base_name": [
            "BINANCE:BTCUSDT"
          ],
          "description": "Bitcoin / TetherUS",
          "exchange": "Binance",
          "pricescale": 100,
          "pointvalue": 1,
          "minmov": 1,
          "session": "24x7",
          "session_display": "24x7",
          "subsessions": [
            {
              "description": "Regular Trading Hours",
              "id": "regular",
              "private": false,
              "session": "24x7",
              "session-display": "24x7"
            }
          ],
          "type": "spot",
          "typespecs": [
            "crypto",
            "defi"
          ],
          "has_intraday": true,
          "fractional": false,
          "listed_exchange": "BINANCE",
          "legs": [
            "BINANCE:BTCUSDT"
          ],
          "is_tradable": true,
          "minmove2": 0,
          "timezone": "Etc/UTC",
          "aliases": [],
          "alternatives": [],
          "is_replayable": true,
          "has_adjustment": false,
          "has_extended_hours": false,
          "bar_source": "trade",
          "bar_transform": "none",
          "bar_fillgaps": false,
          "visible_plots_set": "ohlcv",
          "is-tickbars-available": true,
          "exchange_listed_name": "Binance"
        }
      }
    ]
  },
  "msg": "Success"
}
```
