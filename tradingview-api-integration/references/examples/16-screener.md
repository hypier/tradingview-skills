# Screener

- Source: `openapi.json`
- Live Requests: `enabled`

## Table of Contents

- [Scan Stock Assets](#scan-stock-assets)
- [Get Screener Preset Field Groups](#get-screener-preset-field-groups)
- [Get Screener Filter Option Metadata](#get-screener-filter-option-metadata)
- [Scan ETF Assets](#scan-etf-assets)
- [Scan Bond Assets](#scan-bond-assets)
- [Scan CEX Assets](#scan-cex-assets)
- [Scan DEX Assets](#scan-dex-assets)
- [Scan Crypto Assets](#scan-crypto-assets)

## Scan Stock Assets

`POST /api/screener/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"market":"america","lang":"en","range":[0,50],"preset_fields":["overview","technicals"],"fields":["change_abs","Perf.1W"],"extra_fields":["RSI","SMA50"],"filters":{"market_cap_basic":{"operation":"greater_or_equal","value":10000000000},"volume":{"operation":"greater_or_equal","value":1000000}},"sort":{"sortBy":"market_cap_basic","sortOrder":"desc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 611,
    "data": [
      {
        "rank": 1,
        "symbol": "NASDAQ:NVDA",
        "ticker_view": {
          "description": "NVIDIA Corporation",
          "exchange": "NASDAQ",
          "kind": "delay",
          "kind-delay": 900,
          "logo": {
            "logoid": "nvidia",
            "style": "single"
          },
          "logoid": "nvidia",
          "name": "NVDA",
          "type": "stock",
          "typespecs": [
            "common"
          ]
        },
        "close": 204.87,
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "pricescale": 100,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "change": 2.220337291687465,
        "volume": 158640086,
        "relative_volume_10d_calc": 0.8482233100599401,
        "market_cap_basic": 4957853954704.124,
        "fundamental_currency_code": "USD",
        "price_earnings_ttm": 31.374620968482958,
        "earnings_per_share_diluted_ttm": 6.5298,
        "earnings_per_share_diluted_yoy_growth_ttm": 110.33338701884364,
        "dividends_yield_current": 0.0199580880151681,
        "sector_tr": "Electronic technology",
        "market": "america",
        "sector": "Electronic Technology",
        "analystrating": "StrongBuy",
        "analystrating_tr": "Strong buy",
        "recommend_all": 0.04848484848484849,
        "rsi": 44.961050306617786,
        "macd_macd": -0.723115667638865,
        "macd_signal": 1.84678470211662,
        "stoch_k": 15.64460635498885,
        "stoch_d": 15.282475126589125,
        "ema20": 211.77835484870295,
        "sma50": 206.3227999999998,
        "sma200": 189.1428,
        "change_abs": 4.450000000000017,
        "perf_1w": null
      },
      {
        "rank": 2,
        "symbol": "NASDAQ:AAPL",
        "ticker_view": {
          "description": "Apple Inc.",
          "exchange": "NASDAQ",
          "kind": "delay",
          "kind-delay": 900,
          "logo": {
            "logoid": "apple",
            "style": "single"
          },
          "logoid": "apple",
          "name": "AAPL",
          "type": "stock",
          "typespecs": [
            "common"
          ]
        },
        "close": 295.63,
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "pricescale": 100,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "change": 1.388984155291862,
        "volume": 42572478,
        "relative_volume_10d_calc": 0.7423300763859485,
        "market_cap_basic": 4342022985970.1855,
        "fundamental_currency_code": "USD",
        "price_earnings_ttm": 35.762414564809774,
        "earnings_per_share_diluted_ttm": 8.2665,
        "earnings_per_share_diluted_yoy_growth_ttm": 29.004822172630675,
        "dividends_yield_current": 0.360107003223815,
        "sector_tr": "Electronic technology",
        "market": "america",
        "sector": "Electronic Technology",
        "analystrating": "Buy",
        "analystrating_tr": "Buy",
        "recommend_all": 0.13636363636363635,
        "rsi": 48.119842126736465,
        "macd_macd": 3.306175593595867,
        "macd_signal": 6.634297774937306,
        "stoch_k": 16.941380365674203,
        "stoch_d": 21.028068444965097,
        "ema20": 300.0133273469859,
        "sma50": 284.7822,
        "sma200": 266.5606999999998,
        "change_abs": 4.050000000000011,
        "perf_1w": null
      },
      {
        "rank": 3,
        "symbol": "NASDAQ:GOOG",
        "ticker_view": {
          "description": "Alphabet Inc.",
          "exchange": "NASDAQ",
          "kind": "delay",
          "kind-delay": 900,
          "logo": {
            "logoid": "alphabet",
            "style": "single"
          },
          "logoid": "alphabet",
          "name": "GOOG",
          "type": "stock",
          "typespecs": [
            "common"
          ]
        },
        "close": 356.56,
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "pricescale": 100,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "change": 0.9170157364428873,
        "volume": 28771279,
        "relative_volume_10d_calc": 1.008689959763824,
        "market_cap_basic": 4340688005785.801,
        "fundamental_currency_code": "USD",
        "price_earnings_ttm": 27.199426352686302,
        "earnings_per_share_diluted_ttm": 13.1091,
        "earnings_per_share_diluted_yoy_growth_ttm": 46.187815730487436,
        "dividends_yield_current": 0.237744820559266,
        "sector_tr": "Technology services",
        "market": "america",
        "sector": "Technology Services",
        "analystrating": "StrongBuy",
        "analystrating_tr": "Strong buy",
        "recommend_all": -0.13333333333333333,
        "rsi": 42.122078621842746,
        "macd_macd": -2.211163518577905,
        "macd_signal": 2.0186742772701374,
        "stoch_k": 17.011479575924923,
        "stoch_d": 17.057581673914086,
        "ema20": 368.2420041932052,
        "sma50": 358.2177999999999,
        "sma200": 306.76289999999995,
        "change_abs": 3.240000000000009,
        "perf_1w": null
      },
      "... +47 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```

## Get Screener Preset Field Groups

`GET /api/screener/presets`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/presets?asset_type=stock' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": [
    {
      "id": "overview",
      "fields": [
        "ticker-view",
        "close",
        "type",
        "... +20 more items (truncated)"
      ]
    },
    {
      "id": "performance",
      "fields": [
        "ticker-view",
        "close",
        "change",
        "... +9 more items (truncated)"
      ]
    },
    {
      "id": "extended_hours",
      "fields": [
        "ticker-view",
        "close",
        "change",
        "... +5 more items (truncated)"
      ]
    },
    "... +8 more items (truncated)"
  ],
  "msg": "Success"
}
```

## Get Screener Filter Option Metadata

`GET /api/screener/filter-options`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/filter-options?asset_type=stock&lang=en&id=stocks_market_movers.gainers' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "fields": [],
    "enumValues": {}
  },
  "msg": "Success"
}
```

## Scan ETF Assets

`POST /api/screener/etf/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/etf/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"lang":"en","range":[0,30],"preset_fields":["overview","classification"],"fields":["fund_flows.1M","etf_holdings_count"],"extra_fields":["nav","leverage.tr"],"filters":{"aum":{"operation":"greater_or_equal","value":500000000},"expense_ratio":{"operation":"less_or_equal","value":0.5},"technical_rating":["Buy","StrongBuy"]},"sort":{"sortBy":"aum","sortOrder":"desc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 3398,
    "data": [
      {
        "rank": 1,
        "symbol": "SGX:S27",
        "ticker_view": {
          "description": "State Street SPDR S&P 500 ETF",
          "exchange": "SGX",
          "kind": "delay",
          "kind-delay": 600,
          "logo": {
            "logoid": "spdr-sandp500-etf-tr",
            "style": "single"
          },
          "logoid": "spdr-sandp500-etf-tr",
          "name": "S27",
          "type": "fund",
          "typespecs": [
            "etf"
          ]
        },
        "close": 739.8,
        "change": 1.0186525384384197,
        "volume": 84,
        "aum": 776896309202.647,
        "expense_ratio": 0.0945,
        "asset_class_tr": "Equity",
        "focus_tr": "Large cap",
        "issuer_tr": "State Street Corp.",
        "index_tracked": "S&P 500",
        "actively_managed_tr": "Passive",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "brand_tr": "SPDR",
        "leverage_tr": "Non-leveraged",
        "fund_flows_1m": 14480936112.399998,
        "etf_holdings_count": 505,
        "nav": 725.484792
      },
      {
        "rank": 2,
        "symbol": "TSE:1557",
        "ticker_view": {
          "description": "State Street SPDR S&P 500 ETF",
          "exchange": "TSE",
          "kind": "delay",
          "kind-delay": 1200,
          "logo": {
            "logoid": "spdr-sandp500-etf-tr",
            "style": "single"
          },
          "logoid": "spdr-sandp500-etf-tr",
          "name": "1557",
          "type": "fund",
          "typespecs": [
            "etf"
          ]
        },
        "close": 118400,
        "change": 1.0670081092616304,
        "volume": 1648,
        "aum": 776896309202.647,
        "expense_ratio": 0.0945,
        "asset_class_tr": "Equity",
        "focus_tr": "Large cap",
        "issuer_tr": "State Street Corp.",
        "index_tracked": "S&P 500",
        "actively_managed_tr": "Passive",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "brand_tr": "SPDR",
        "leverage_tr": "Non-leveraged",
        "fund_flows_1m": 14427663300.655869,
        "etf_holdings_count": 505,
        "nav": 725.484792
      },
      {
        "rank": 3,
        "symbol": "ASX:SPY",
        "ticker_view": {
          "description": "SPDR S&P 500 ETF",
          "exchange": "ASX",
          "kind": "delay",
          "kind-delay": 1200,
          "logo": {
            "logoid": "spdr-sandp500-etf-tr",
            "style": "single"
          },
          "logoid": "spdr-sandp500-etf-tr",
          "name": "SPY",
          "type": "fund",
          "typespecs": [
            "etf"
          ]
        },
        "close": 1049.47,
        "change": 0.9338693544664189,
        "volume": 639,
        "aum": 771853643853.1222,
        "expense_ratio": 0.0945,
        "asset_class_tr": "Equity",
        "focus_tr": "Large cap",
        "issuer_tr": "State Street Corp.",
        "index_tracked": "S&P 500",
        "actively_managed_tr": "Passive",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "brand_tr": "SPDR",
        "leverage_tr": "Non-leveraged",
        "fund_flows_1m": 14296086610.89061,
        "etf_holdings_count": null,
        "nav": 722.7777643232399
      },
      "... +27 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```

## Scan Bond Assets

`POST /api/screener/bond/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/bond/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"lang":"en","range":[0,25],"preset_fields":["overview","ratings"],"fields":["yield_to_call","yield_to_worst"],"extra_fields":["snp_rating_long_term.tr","fitch_outlook.tr"],"filters":{"yield_to_maturity":{"operation":"greater_or_equal","value":4},"days_to_maturity":{"operation":"less_or_equal","value":3650}},"sort":{"sortBy":"yield_to_maturity","sortOrder":"desc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 65801,
    "data": [
      {
        "rank": 1,
        "symbol": "DUS:XS238891027",
        "ticker_view": {
          "description": "Branicks Group AG 2.25% 22-SEP-2026",
          "kind": "delay",
          "kind-delay": 900,
          "logo": {
            "logoid": "dic-asset-ag",
            "style": "single"
          },
          "logoid": "dic-asset-ag",
          "name": "XS238891027",
          "type": "bond",
          "typespecs": [
            "corporate"
          ]
        },
        "close": 60.25,
        "yield_to_maturity": 495.8531259818097,
        "current_coupon": 2.25,
        "coupon_type_general_tr": "Fixed",
        "maturity_type_tr": "Regular",
        "issue_status_tr": "Current",
        "bond_issuer": "Branicks Group AG",
        "days_to_maturity": 103,
        "techrating_1d": null,
        "techrating_1d_tr": null,
        "snp_rating_long_term_tr": null,
        "fitch_rating_long_term_tr": null,
        "snp_issuer_rating_long_term_tr": null,
        "fitch_issuer_rating_long_term_tr": null,
        "snp_outlook_tr": null,
        "fitch_outlook_tr": null,
        "yield_to_call": null,
        "yield_to_worst": 495.8531259818097
      },
      {
        "rank": 2,
        "symbol": "HAM:XS238891027",
        "ticker_view": {
          "description": "Branicks Group AG 2.25% 22-SEP-2026",
          "kind": "delay",
          "kind-delay": 900,
          "logo": {
            "logoid": "dic-asset-ag",
            "style": "single"
          },
          "logoid": "dic-asset-ag",
          "name": "XS238891027",
          "type": "bond",
          "typespecs": [
            "corporate"
          ]
        },
        "close": 60.3,
        "yield_to_maturity": 494.1456071981933,
        "current_coupon": 2.25,
        "coupon_type_general_tr": "Fixed",
        "maturity_type_tr": "Regular",
        "issue_status_tr": "Current",
        "bond_issuer": "Branicks Group AG",
        "days_to_maturity": 103,
        "techrating_1d": null,
        "techrating_1d_tr": null,
        "snp_rating_long_term_tr": null,
        "fitch_rating_long_term_tr": null,
        "snp_issuer_rating_long_term_tr": null,
        "fitch_issuer_rating_long_term_tr": null,
        "snp_outlook_tr": null,
        "fitch_outlook_tr": null,
        "yield_to_call": null,
        "yield_to_worst": 494.1456071981933
      },
      {
        "rank": 3,
        "symbol": "TASE:EL.D28-I",
        "ticker_view": {
          "description": "Israel Electric Corp. Ltd. 4.25% 14-AUG-2028",
          "kind": "delay",
          "kind-delay": 900,
          "logo": null,
          "logoid": "",
          "name": "EL.D28-I",
          "type": "bond",
          "typespecs": [
            "corporate"
          ]
        },
        "close": 1,
        "yield_to_maturity": 493.1690160474301,
        "current_coupon": 4.25,
        "coupon_type_general_tr": "Fixed",
        "maturity_type_tr": "Regular",
        "issue_status_tr": "Current",
        "bond_issuer": "Israel Electric Corp. Ltd.",
        "days_to_maturity": 795,
        "techrating_1d": null,
        "techrating_1d_tr": null,
        "snp_rating_long_term_tr": null,
        "fitch_rating_long_term_tr": null,
        "snp_issuer_rating_long_term_tr": null,
        "fitch_issuer_rating_long_term_tr": null,
        "snp_outlook_tr": null,
        "fitch_outlook_tr": null,
        "yield_to_call": null,
        "yield_to_worst": 493.1690160474301
      },
      "... +22 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```

## Scan CEX Assets

`POST /api/screener/cex/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/cex/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"lang":"en","range":[0,25],"preset_fields":["overview","market_data"],"fields":["Perf.1W"],"extra_fields":["RSI","MACD.macd"],"filters":{"exchange":["HTX"],"technical_rating":["Buy"]},"sort":{"sortBy":"24h_vol_cmc","sortOrder":"desc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 96,
    "data": [
      {
        "rank": 1,
        "symbol": "HTX:FFUSDT",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCFF",
          "currency-logoid": "crypto/XTVCUSDT",
          "description": "FF / Tether USD",
          "exchange": "HTX",
          "logo": {
            "logoid": "crypto/XTVCFF",
            "style": "single"
          },
          "name": "FFUSDT",
          "type": "spot",
          "typespecs": [
            "crypto",
            "defi"
          ]
        },
        "exchange": "HTX",
        "close": 0.09016,
        "24h_close_change_5": 16.59761781460383,
        "24h_vol_cmc": null,
        "market_cap_calc": null,
        "base_currency_id": "XTVCFF",
        "currency_id": "XTVCUSDT",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "perf_1w": null,
        "rsi": 51.02786164918869,
        "macd_macd": -0.0002837108880790473
      },
      {
        "rank": 2,
        "symbol": "HTX:ATOMUSDT",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCATOM",
          "currency-logoid": "crypto/XTVCUSDT",
          "description": "Cosmos / Tether USD",
          "exchange": "HTX",
          "logo": {
            "logoid": "crypto/XTVCATOM",
            "style": "single"
          },
          "name": "ATOMUSDT",
          "type": "spot",
          "typespecs": [
            "crypto",
            "defi"
          ]
        },
        "exchange": "HTX",
        "close": 2.003,
        "24h_close_change_5": 9.429632867132872,
        "24h_vol_cmc": null,
        "market_cap_calc": null,
        "base_currency_id": "XTVCATOM",
        "currency_id": "XTVCUSDT",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "perf_1w": null,
        "rsi": 55.99958321732737,
        "macd_macd": -0.035597497414079804
      },
      {
        "rank": 3,
        "symbol": "HTX:QQQUSDT.P",
        "ticker_view": {
          "base-currency-logoid": null,
          "currency-logoid": "crypto/XTVCUSDT",
          "description": "QQQ Perpetual LinearSwap Contract",
          "exchange": "HTX",
          "logo": {
            "logoid": "invesco",
            "style": "single"
          },
          "name": "QQQUSDT.P",
          "type": "swap",
          "typespecs": [
            "crypto",
            "perpetual",
            "defi"
          ]
        },
        "exchange": "HTX",
        "close": 717.8,
        "24h_close_change_5": 2.786608242403403,
        "24h_vol_cmc": null,
        "market_cap_calc": null,
        "base_currency_id": "",
        "currency_id": "XTVCUSDT",
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy",
        "perf_1w": null,
        "rsi": 52.444497276727695,
        "macd_macd": 0.8979168721434689
      },
      "... +22 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```

## Scan DEX Assets

`POST /api/screener/dex/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/dex/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"lang":"en","range":[0,25],"preset_fields":["overview","trading_activity"],"fields":["Perf.1W"],"extra_fields":["TechRating_1D","TechRating_1D.tr"],"filters":{"exchange":["UNISWAP","PANCAKESWAP"],"dex_trading_volume_24h":{"operation":"greater_or_equal","value":1000000},"dex_buyers_24h":{"operation":"greater_or_equal","value":200}},"sort":{"sortBy":"dex_trading_volume_24h","sortOrder":"desc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 23,
    "data": [
      {
        "rank": 1,
        "symbol": "PANCAKESWAP:SKYAIWBNB_BC4214.USD",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCSKYAI2",
          "description": "SKYAI / WBNB",
          "exchange": "PANCAKESWAP",
          "logo": {
            "logoid": "crypto/XTVCSKYAI2",
            "style": "single"
          },
          "name": "SKYAI",
          "type": "spot",
          "typespecs": [
            "crypto"
          ]
        },
        "exchange": "PANCAKESWAP",
        "close": 0.27162725,
        "24h_close_change_5": 26.75585577469537,
        "dex_trading_volume_24h": 21431316,
        "dex_buyers_24h": 2208,
        "dex_sellers_24h": 1541,
        "dex_created_time": 1745120523,
        "base_currency_id": "XTVCSKYAI2",
        "currency_id": "USD",
        "perf_1w": null,
        "techrating_1d": "StrongBuy",
        "techrating_1d_tr": "Strong buy"
      },
      {
        "rank": 2,
        "symbol": "PANCAKESWAP:PROUSDT_63844B.USD",
        "ticker_view": {
          "base-currency-logoid": "",
          "description": "Pro Token / USDT",
          "exchange": "PANCAKESWAP",
          "logo": null,
          "name": "PRO",
          "type": "spot",
          "typespecs": [
            "crypto"
          ]
        },
        "exchange": "PANCAKESWAP",
        "close": 59.96499507,
        "24h_close_change_5": -0.1261824884627014,
        "dex_trading_volume_24h": 9055996,
        "dex_buyers_24h": 9307,
        "dex_sellers_24h": 7513,
        "dex_created_time": 1768151905,
        "base_currency_id": "XTVCPROTOKE",
        "currency_id": "USD",
        "perf_1w": null,
        "techrating_1d": "Buy",
        "techrating_1d_tr": "Buy"
      },
      {
        "rank": 3,
        "symbol": "PANCAKESWAP:ARKUSDT_CAAF3C.USD",
        "ticker_view": {
          "base-currency-logoid": "",
          "description": "ARK / USDT",
          "exchange": "PANCAKESWAP",
          "logo": null,
          "name": "ARK",
          "type": "spot",
          "typespecs": [
            "crypto"
          ]
        },
        "exchange": "PANCAKESWAP",
        "close": 9.78154115,
        "24h_close_change_5": -5.222055152561915,
        "dex_trading_volume_24h": 7890447,
        "dex_buyers_24h": 13753,
        "dex_sellers_24h": 12784,
        "dex_created_time": 1756206977,
        "base_currency_id": "XTVCARKD",
        "currency_id": "USD",
        "perf_1w": null,
        "techrating_1d": "Sell",
        "techrating_1d_tr": "Sell"
      },
      "... +20 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```

## Scan Crypto Assets

`POST /api/screener/crypto/scan`

### Request

```bash
curl --request POST \
	--url 'https://tradingview-data1.p.rapidapi.com/api/screener/crypto/scan' \
	--header 'Content-Type: application/json' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY' \
	--data '{"lang":"zh","range":[0,25],"preset_fields":["overview","sentiment"],"fields":["Perf.1W"],"extra_fields":["RSI","MACD.macd"],"filters":{"market_cap_calc":{"operation":"greater_or_equal","value":500000000},"technical_rating":["Buy","StrongBuy"]},"sort":{"sortBy":"crypto_total_rank","sortOrder":"asc"}}'
```

### Response

HTTP `200`

```json
{
  "success": true,
  "data": {
    "totalCount": 33,
    "data": [
      {
        "rank": 1,
        "symbol": "CRYPTO:USDCUSD",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCUSDC",
          "description": "USDC",
          "exchange": "CRYPTO",
          "logo": {
            "logoid": "crypto/XTVCUSDC",
            "style": "single"
          },
          "name": "USDC",
          "type": "spot",
          "typespecs": [
            "crypto",
            "cryptoasset",
            "synthetic"
          ]
        },
        "crypto_total_rank": 5,
        "close": 0.99995,
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "pricescale": 100000,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "24h_close_change_5": -0.007999680012807488,
        "market_cap_calc": 74917565434.44568,
        "fundamental_currency_code": "USD",
        "24h_vol_cmc": 11669802340.908743,
        "circulating_supply": 74921311500.02068,
        "24h_vol_to_market_cap": 0.15576857407519532,
        "socialdominance": 4.0404,
        "crypto_common_categories_tr": [
          "稳定币",
          "资产支持的稳定币",
          "美国制造",
          "... +2 more items (truncated)"
        ],
        "techrating_1d": "Buy",
        "techrating_1d_tr": "买入",
        "perf_1w": null,
        "rsi": 53.08718698093679,
        "macd_macd": 2.79091031381018e-05
      },
      {
        "rank": 2,
        "symbol": "CRYPTO:HYPEHUSD",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCHYPEH",
          "description": "Hyperliquid",
          "exchange": "CRYPTO",
          "logo": {
            "logoid": "crypto/XTVCHYPEH",
            "style": "single"
          },
          "name": "HYPE",
          "type": "spot",
          "typespecs": [
            "crypto",
            "cryptoasset",
            "synthetic"
          ]
        },
        "crypto_total_rank": 9,
        "close": 58.902,
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "pricescale": 1000,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "24h_close_change_5": 7.528707304160509,
        "market_cap_calc": 14935320810.686533,
        "fundamental_currency_code": "USD",
        "24h_vol_cmc": 958282609.324525,
        "circulating_supply": 253562201.8044639,
        "24h_vol_to_market_cap": 0.06416217110240136,
        "socialdominance": 3.7116,
        "crypto_common_categories_tr": [
          "去中心化交易所",
          "衍生品",
          "第一层级",
          "交易所代币"
        ],
        "techrating_1d": "Buy",
        "techrating_1d_tr": "买入",
        "perf_1w": null,
        "rsi": 50.51564079499676,
        "macd_macd": 1.6025422246690582
      },
      {
        "rank": 3,
        "symbol": "CRYPTO:XMRUSD",
        "ticker_view": {
          "base-currency-logoid": "crypto/XTVCXMR",
          "description": "Monero",
          "exchange": "CRYPTO",
          "logo": {
            "logoid": "crypto/XTVCXMR",
            "style": "single"
          },
          "name": "XMR",
          "type": "spot",
          "typespecs": [
            "crypto",
            "cryptoasset",
            "synthetic"
          ]
        },
        "crypto_total_rank": 12,
        "close": 374.21,
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "pricescale": 100,
        "minmov": 1,
        "fractional": "false",
        "minmove2": 0,
        "currency": "USD",
        "24h_close_change_5": 8.671511627906971,
        "market_cap_calc": 7021597366.007139,
        "fundamental_currency_code": "USD",
        "24h_vol_cmc": 184355610.35694492,
        "circulating_supply": 18763788.69086112,
        "24h_vol_to_market_cap": 0.026255508646714033,
        "socialdominance": 0.3864,
        "crypto_common_categories_tr": [
          "隐私",
          "加密货币",
          "第一层级"
        ],
        "techrating_1d": "Buy",
        "techrating_1d_tr": "买入",
        "perf_1w": null,
        "rsi": 53.501172553508816,
        "macd_macd": -9.51652427988023
      },
      "... +22 more items (truncated)"
    ]
  },
  "msg": "Success"
}
```
