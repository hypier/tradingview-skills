# Leaderboards

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get Stock Leaderboard](#get-stock-leaderboard)
- [Get Index Leaderboard](#get-index-leaderboard)
- [Get Crypto Leaderboard](#get-crypto-leaderboard)
- [Get Futures Leaderboard](#get-futures-leaderboard)
- [Get Forex Leaderboard](#get-forex-leaderboard)
- [Get Government Bond Leaderboard](#get-government-bond-leaderboard)
- [Get Corporate Bond Leaderboard](#get-corporate-bond-leaderboard)
- [Get ETF Leaderboard](#get-etf-leaderboard)
- [Get Generic Leaderboard Data](#get-generic-leaderboard-data)

## Get Stock Leaderboard

`GET /api/leaderboard/stocks`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/stocks?tab=gainers&market_code=america&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 2081,
    "data": [
      {
        "rank": 1,
        "symbol": "NASDAQ:ENVB",
        "description": "Enveric Biosciences, Inc.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "enveric-biosciences",
          "style": "single"
        },
        "logoid": "enveric-biosciences",
        "name": "ENVB",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 100.54945054945054,
        "price": 3.65,
        "currency": "USD",
        "volume": 158694731,
        "relativevolume": 125.31953277558104,
        "marketcap": 6889503.000000001,
        "pricetoearnings": null,
        "epsdiluted": -40.8497,
        "epsdilutedgrowth": 84.04362197207438,
        "dividendsyield": 0,
        "sector": "Health technology",
        "analystrating": "NoRating"
      },
      {
        "rank": 2,
        "symbol": "NASDAQ:FGI",
        "description": "FGI Industries Ltd.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "fgi-industries-ltd",
          "style": "single"
        },
        "logoid": "fgi-industries-ltd",
        "name": "FGI",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 50.615384615384606,
        "price": 9.79,
        "currency": "USD",
        "volume": 2517949,
        "relativevolume": 23.441360036047172,
        "marketcap": 18868522,
        "pricetoearnings": null,
        "epsdiluted": -3.1998,
        "epsdilutedgrowth": -408.3081810961081,
        "dividendsyield": 0,
        "sector": "Producer manufacturing",
        "analystrating": "StrongBuy"
      },
      {
        "rank": 3,
        "symbol": "NASDAQ:PBM",
        "description": "Psyence Biomedical Ltd.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "psyence",
          "style": "single"
        },
        "logoid": "psyence",
        "name": "PBM",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 48.68421052631581,
        "price": 11.3,
        "currency": "USD",
        "volume": 42269832,
        "relativevolume": 4.045649231514533,
        "marketcap": 11550600,
        "pricetoearnings": null,
        "epsdiluted": null,
        "epsdilutedgrowth": null,
        "dividendsyield": null,
        "sector": "Health technology",
        "analystrating": "NoRating"
      }
    ],
    "metadata": {
      "asset_type": "stocks",
      "tab": {
        "id": "stocks_market_movers.gainers",
        "title": "Top gainers"
      },
      "market": {
        "name": "United States",
        "market_code": "america",
        "exchanges": [
          "NASDAQ",
          "NYSE",
          "NYSE ARCA"
        ]
      },
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Index Leaderboard

`GET /api/leaderboard/indices`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/indices?tab=major&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 25,
    "data": [
      {
        "rank": 1,
        "symbol": "SP:SPX",
        "base-currency-logoid": null,
        "description": "S&P 500",
        "exchange": "SP",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "indices/s-and-p-500",
          "style": "single"
        },
        "logoid": "indices/s-and-p-500",
        "name": "SPX",
        "type": "index",
        "typespecs": [
          "main",
          "cfd"
        ],
        "price": 7109.13,
        "currency": "USD",
        "change": -0.237438693245207,
        "changeabs": -16.920000000000073,
        "high": 7122.65,
        "low": 7084.41,
        "technicalrating": "Buy"
      },
      {
        "rank": 2,
        "symbol": "TVC:IXIC",
        "base-currency-logoid": null,
        "description": "US Composite Index",
        "exchange": "TVC",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "indices/nasdaq-composite",
          "style": "single"
        },
        "logoid": "indices/nasdaq-composite",
        "name": "IXIC",
        "type": "index",
        "typespecs": [
          "cfd"
        ],
        "price": 24404.3934,
        "currency": "USD",
        "change": -0.26191655122154434,
        "changeabs": -64.08699999999953,
        "high": 24435.9243,
        "low": 24221.5308,
        "technicalrating": "Buy"
      },
      {
        "rank": 3,
        "symbol": "DJ:DJI",
        "base-currency-logoid": null,
        "description": "Dow Jones Industrial Average Index",
        "exchange": "DJ",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "indices/dow-30",
          "style": "single"
        },
        "logoid": "indices/dow-30",
        "name": "DJI",
        "type": "index",
        "typespecs": [
          "main",
          "cfd"
        ],
        "price": 49442.57,
        "currency": "USD",
        "change": -0.009848841517382132,
        "changeabs": -4.870000000002619,
        "high": 49489.63,
        "low": 49245.6,
        "technicalrating": "Buy"
      }
    ],
    "metadata": {
      "asset_type": "indices",
      "tab": {
        "id": "indices_quotes.major",
        "title": "Major world indices"
      },
      "market": null,
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Crypto Leaderboard

`GET /api/leaderboard/crypto`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/crypto?tab=gainers&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 150,
    "data": [
      {
        "rank": 82,
        "symbol": "CRYPTO:RAVEDUSD",
        "base-currency-logoid": "crypto/XTVCRAVED",
        "description": "RaveDAO",
        "exchange": "CRYPTO",
        "logo": {
          "logoid": "crypto/XTVCRAVED",
          "style": "single"
        },
        "name": "RAVE",
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "price": 1.80104,
        "currency": "USD",
        "changecrypto": 128.7733761553732,
        "marketcapcalc": 446737887.7230609,
        "volume24hcoin": 709259270.9241372,
        "supplycirculating": 248044400.858982,
        "volumetomarketcap": 1.587640740612126,
        "socialdominance": null,
        "cryptocategory": [
          "Social media and content",
          "DAO"
        ],
        "technicalrating": "Sell"
      },
      {
        "rank": 21,
        "symbol": "CRYPTO:MEMECOREUSD",
        "base-currency-logoid": "crypto/XTVCMEMECORE",
        "description": "MemeCore",
        "exchange": "CRYPTO",
        "logo": {
          "logoid": "crypto/XTVCMEMECORE",
          "style": "single"
        },
        "name": "M",
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "price": 4.1013,
        "currency": "USD",
        "changecrypto": 19.43836296231426,
        "marketcapcalc": 5301451650.655042,
        "volume24hcoin": 21060537.21436149,
        "supplycirculating": 1292627130.5817769,
        "volumetomarketcap": 0.003972598186717268,
        "socialdominance": 0.05678098571791206,
        "cryptocategory": [
          "Memes",
          "Layer 1"
        ],
        "technicalrating": "StrongBuy"
      },
      {
        "rank": 107,
        "symbol": "CRYPTO:SPX6USD",
        "base-currency-logoid": "crypto/XTVCSPX6",
        "description": "SPX6900",
        "exchange": "CRYPTO",
        "logo": {
          "logoid": "crypto/XTVCSPX6",
          "style": "single"
        },
        "name": "SPX",
        "type": "spot",
        "typespecs": [
          "crypto",
          "cryptoasset",
          "synthetic"
        ],
        "price": 0.359,
        "currency": "USD",
        "changecrypto": 10.522748975757024,
        "marketcapcalc": 334226519.33513,
        "volume24hcoin": 9932211.40528916,
        "supplycirculating": 930993090.07,
        "volumetomarketcap": 0.02971700577514647,
        "socialdominance": 0.7318067041643843,
        "cryptocategory": [
          "Memes"
        ],
        "technicalrating": "Buy"
      }
    ],
    "metadata": {
      "asset_type": "crypto",
      "tab": {
        "id": "crypto_coins.gainers",
        "title": "Gainers"
      },
      "market": null,
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Futures Leaderboard

`GET /api/leaderboard/futures`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/futures?tab=all&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 489,
    "data": [
      {
        "rank": 1,
        "symbol": "CBOT_MINI:10Y1!",
        "base-currency-logoid": null,
        "description": "10-Year Yield Futures",
        "exchange": "CBOT_MINI",
        "kind": "delay",
        "kind-delay": 600,
        "logo": {
          "logoid": "indices/micro-10-year",
          "style": "single"
        },
        "logoid": "indices/micro-10-year",
        "name": "10Y1!",
        "type": "futures",
        "typespecs": [
          "continuous",
          "micro",
          "synthetic"
        ],
        "price": 4.252,
        "currency": "USD",
        "change": 0.04705882352940658,
        "changeabs": 0.0019999999999997797,
        "high": 4.261,
        "low": 4.239,
        "technicalrating": "Sell"
      },
      {
        "rank": 2,
        "symbol": "COMEX:1OZ1!",
        "base-currency-logoid": null,
        "description": "1-Ounce Gold Futures",
        "exchange": "COMEX",
        "kind": "delay",
        "kind-delay": 600,
        "logo": {
          "logoid": "metal/gold",
          "style": "single"
        },
        "logoid": "metal/gold",
        "name": "1OZ1!",
        "type": "futures",
        "typespecs": [
          "continuous",
          "synthetic"
        ],
        "price": 4803,
        "currency": "USD",
        "change": -0.5332643023556821,
        "changeabs": -25.75,
        "high": 4857,
        "low": 4791,
        "technicalrating": "Buy"
      },
      {
        "rank": 3,
        "symbol": "CBOT_MINI:2YY1!",
        "base-currency-logoid": null,
        "description": "2-Year Yield Futures",
        "exchange": "CBOT_MINI",
        "kind": "delay",
        "kind-delay": 600,
        "logo": {
          "logoid": "indices/micro-2-year",
          "style": "single"
        },
        "logoid": "indices/micro-2-year",
        "name": "2YY1!",
        "type": "futures",
        "typespecs": [
          "continuous",
          "micro",
          "synthetic"
        ],
        "price": 3.806,
        "currency": "USD",
        "change": 0,
        "changeabs": 0,
        "high": 3.806,
        "low": 3.806,
        "technicalrating": "Buy"
      }
    ],
    "metadata": {
      "asset_type": "futures",
      "tab": {
        "id": "futures.quotes_all",
        "title": "All futures"
      },
      "market": null,
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Forex Leaderboard

`GET /api/leaderboard/forex`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/forex?tab=major&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 7,
    "data": [
      {
        "rank": 1,
        "symbol": "FX_IDC:EURUSD",
        "base-currency-logoid": "country/EU",
        "currency-logoid": "country/US",
        "description": "EURO / U.S. DOLLAR",
        "exchange": "FX_IDC",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/EU",
          "logoid2": "country/US",
          "style": "pair"
        },
        "logoid": "",
        "name": "EURUSD",
        "type": "forex",
        "typespecs": [
          ""
        ],
        "price": 1.17603,
        "currency": "USD",
        "change": -0.20958845990667746,
        "changeabs": -0.0024700000000001943,
        "bid": 1.17602,
        "ask": 1.17603,
        "high": 1.1791,
        "low": 1.17566,
        "technicalrating": "Buy"
      },
      {
        "rank": 2,
        "symbol": "FX_IDC:USDJPY",
        "base-currency-logoid": "country/US",
        "currency-logoid": "country/JP",
        "description": "U.S. DOLLAR / JAPANESE YEN",
        "exchange": "FX_IDC",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/US",
          "logoid2": "country/JP",
          "style": "pair"
        },
        "logoid": "",
        "name": "USDJPY",
        "type": "forex",
        "typespecs": [
          ""
        ],
        "price": 159.19,
        "currency": "JPY",
        "change": 0.2771653543307072,
        "changeabs": 0.4399999999999977,
        "bid": 159.184,
        "ask": 159.203,
        "high": 159.254,
        "low": 158.744,
        "technicalrating": "Buy"
      },
      {
        "rank": 3,
        "symbol": "FX_IDC:GBPUSD",
        "base-currency-logoid": "country/GB",
        "currency-logoid": "country/US",
        "description": "BRITISH POUND / U.S. DOLLAR",
        "exchange": "FX_IDC",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/GB",
          "logoid2": "country/US",
          "style": "pair"
        },
        "logoid": "",
        "name": "GBPUSD",
        "type": "forex",
        "typespecs": [
          ""
        ],
        "price": 1.3508,
        "currency": "USD",
        "change": -0.17735737511084523,
        "changeabs": -0.0023999999999999577,
        "bid": 1.3507,
        "ask": 1.3508,
        "high": 1.3539,
        "low": 1.3483,
        "technicalrating": "Buy"
      }
    ],
    "metadata": {
      "asset_type": "forex",
      "tab": {
        "id": "currencies_rates.major",
        "title": "Major"
      },
      "market": null,
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Government Bond Leaderboard

`GET /api/leaderboard/bonds`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/bonds?tab=major&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 17,
    "data": [
      {
        "rank": 1,
        "symbol": "TVC:US10Y",
        "description": "United States 10 Year Government Bonds Yield",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/US",
          "style": "single"
        },
        "logoid": "country/US",
        "name": "US10Y",
        "type": "bond",
        "typespecs": [
          "government",
          "yield",
          "benchmark"
        ],
        "coupon": 4.125,
        "bondyield": 4.254,
        "maturitydate": 20360215,
        "timetomaturity": 3587,
        "bondprice": 98.96875,
        "currency": "PCTPAR",
        "change": -0.0939408172851209,
        "bondchangeabs": -0.004000000000000448
      },
      {
        "rank": 2,
        "symbol": "TVC:CA10Y",
        "description": "Canada 10 Year Government Bonds Yield",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/CA",
          "style": "single"
        },
        "logoid": "country/CA",
        "name": "CA10Y",
        "type": "bond",
        "typespecs": [
          "government",
          "yield",
          "benchmark"
        ],
        "coupon": 3.25,
        "bondyield": 3.439,
        "maturitydate": 20351201,
        "timetomaturity": 3511,
        "bondprice": 98.461,
        "currency": "PCTPAR",
        "change": 0,
        "bondchangeabs": 0
      },
      {
        "rank": 3,
        "symbol": "TVC:GB10Y",
        "description": "United Kingdom 10 Year Government Bonds Yield",
        "kind": "rt",
        "kind-delay": 0,
        "logo": {
          "logoid": "country/GB",
          "style": "single"
        },
        "logoid": "country/GB",
        "name": "GB10Y",
        "type": "bond",
        "typespecs": [
          "government",
          "yield",
          "benchmark"
        ],
        "coupon": 4.75,
        "bondyield": 4.84,
        "maturitydate": 20351022,
        "timetomaturity": 3471,
        "bondprice": 99.318,
        "currency": "PCTPAR",
        "change": 0.08271298593878328,
        "bondchangeabs": 0.0039999999999995595
      }
    ],
    "metadata": {
      "asset_type": "bonds",
      "tab": {
        "id": "government_bonds.major_10y",
        "title": "Major 10Y"
      },
      "market": null,
      "columnset": null
    }
  },
  "msg": "Success"
}
```

## Get Corporate Bond Leaderboard

`GET /api/leaderboard/corporate-bonds`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/corporate-bonds?tab=highest-yield&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 627,
    "data": [
      {
        "rank": 1,
        "symbol": "SWB:US71654QDD16",
        "ticker": "US71654QDD16",
        "currency": "USD",
        "yieldtomaturity": 8.49617538719687,
        "issuercountry": "Mexico",
        "bondclose": 91.645,
        "volume1d": 0,
        "currentcoupon": 7.69,
        "maturitydate": 20500123,
        "outstandingamount": 8047831000,
        "facevalue": 1000,
        "minimumdenominationamount": 10000
      },
      {
        "rank": 2,
        "symbol": "LUXSE:US40049JBC09",
        "ticker": "US40049JBC09",
        "currency": "USD",
        "yieldtomaturity": 8.479468404049362,
        "issuercountry": "Mexico",
        "bondclose": 77.554,
        "volume1d": 1,
        "currentcoupon": 6.125,
        "maturitydate": 20460131,
        "outstandingamount": 879572000,
        "facevalue": 1000,
        "minimumdenominationamount": 200000
      },
      {
        "rank": 3,
        "symbol": "FINRA:TV4837441",
        "ticker": "TV4837441",
        "currency": "USD",
        "yieldtomaturity": 8.4404706366076,
        "issuercountry": "Mexico",
        "bondclose": 67.75,
        "volume1d": 1000000,
        "currentcoupon": 5.25,
        "maturitydate": 20490524,
        "outstandingamount": 660928000,
        "facevalue": 1000,
        "minimumdenominationamount": 200000
      }
    ],
    "metadata": {
      "asset_type": "corporate_bonds",
      "tab": {
        "id": "corporate_bonds.rates_highest_yield",
        "title": "Highest yield"
      },
      "market": null,
      "columnset": null
    }
  },
  "msg": "Success"
}
```

## Get ETF Leaderboard

`GET /api/leaderboard/etfs`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/etfs?tab=largest&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 5943,
    "data": [
      {
        "rank": 1,
        "symbol": "AMEX:VOO",
        "description": "Vanguard S&P 500 ETF",
        "exchange": "AMEX",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "vanguard",
          "style": "single"
        },
        "logoid": "vanguard",
        "name": "VOO",
        "type": "fund",
        "typespecs": [
          "etf"
        ],
        "assetsundermanagement": 908262081825.198,
        "currency": "USD",
        "price": 651.54,
        "change": -0.18995680014706473,
        "volumeprice": 4159486089.3599997,
        "relativevolume": 1.0299532403509462,
        "navtotalreturn": 79.09250267149382,
        "expenseratio": 0.03,
        "assetclass": "Equity",
        "focus": "Large cap"
      },
      {
        "rank": 2,
        "symbol": "AMEX:IVV",
        "description": "iShares Core S&P 500 ETF",
        "exchange": "AMEX",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "ishares",
          "style": "single"
        },
        "logoid": "ishares",
        "name": "IVV",
        "type": "fund",
        "typespecs": [
          "etf"
        ],
        "assetsundermanagement": 783684064948,
        "currency": "USD",
        "price": 712.09,
        "change": -0.17803072782325638,
        "volumeprice": 3576911384.53,
        "relativevolume": 0.9925793037669888,
        "navtotalreturn": 79.11221282393261,
        "expenseratio": 0.03,
        "assetclass": "Equity",
        "focus": "Large cap"
      },
      {
        "rank": 3,
        "symbol": "AMEX:SPY",
        "description": "SPDR S&P 500 ETF TRUST",
        "exchange": "AMEX",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "spdr-sandp500-etf-tr",
          "style": "single"
        },
        "logoid": "spdr-sandp500-etf-tr",
        "name": "SPY",
        "type": "fund",
        "typespecs": [
          "etf"
        ],
        "assetsundermanagement": 714796356873.986,
        "currency": "USD",
        "price": 708.72,
        "change": -0.19996057115497776,
        "volumeprice": 30861987739.68,
        "relativevolume": 0.7274399436694816,
        "navtotalreturn": 78.17864756902947,
        "expenseratio": 0.0945,
        "assetclass": "Equity",
        "focus": "Large cap"
      }
    ],
    "metadata": {
      "asset_type": "etfs",
      "tab": {
        "id": "etfs_funds.largest",
        "title": "Largest"
      },
      "market": null,
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```

## Get Generic Leaderboard Data

`GET /api/leaderboard/data`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/leaderboard/data?id=stocks_market_movers.gainers&market_code=america&columnset=overview&start=0&count=5&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "totalCount": 2081,
    "data": [
      {
        "rank": 1,
        "symbol": "NASDAQ:ENVB",
        "description": "Enveric Biosciences, Inc.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "enveric-biosciences",
          "style": "single"
        },
        "logoid": "enveric-biosciences",
        "name": "ENVB",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 100.54945054945054,
        "price": 3.65,
        "currency": "USD",
        "volume": 158694731,
        "relativevolume": 125.31953277558104,
        "marketcap": 6889503.000000001,
        "pricetoearnings": null,
        "epsdiluted": -40.8497,
        "epsdilutedgrowth": 84.04362197207438,
        "dividendsyield": 0,
        "sector": "Health technology",
        "analystrating": "NoRating"
      },
      {
        "rank": 2,
        "symbol": "NASDAQ:FGI",
        "description": "FGI Industries Ltd.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "fgi-industries-ltd",
          "style": "single"
        },
        "logoid": "fgi-industries-ltd",
        "name": "FGI",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 50.615384615384606,
        "price": 9.79,
        "currency": "USD",
        "volume": 2517949,
        "relativevolume": 23.441360036047172,
        "marketcap": 18868522,
        "pricetoearnings": null,
        "epsdiluted": -3.1998,
        "epsdilutedgrowth": -408.3081810961081,
        "dividendsyield": 0,
        "sector": "Producer manufacturing",
        "analystrating": "StrongBuy"
      },
      {
        "rank": 3,
        "symbol": "NASDAQ:PBM",
        "description": "Psyence Biomedical Ltd.",
        "exchange": "NASDAQ",
        "kind": "delay",
        "kind-delay": 900,
        "logo": {
          "logoid": "psyence",
          "style": "single"
        },
        "logoid": "psyence",
        "name": "PBM",
        "type": "stock",
        "typespecs": [
          "common"
        ],
        "change": 48.68421052631581,
        "price": 11.3,
        "currency": "USD",
        "volume": 42269832,
        "relativevolume": 4.045649231514533,
        "marketcap": 11550600,
        "pricetoearnings": null,
        "epsdiluted": null,
        "epsdilutedgrowth": null,
        "dividendsyield": null,
        "sector": "Health technology",
        "analystrating": "NoRating"
      }
    ],
    "metadata": {
      "asset_type": "stocks",
      "tab": {
        "id": "stocks_market_movers.gainers",
        "title": "Top gainers"
      },
      "market": {
        "name": "United States",
        "market_code": "america",
        "exchanges": [
          "NASDAQ",
          "NYSE",
          "NYSE ARCA"
        ]
      },
      "columnset": {
        "id": "overview",
        "title": "Overview"
      }
    }
  },
  "msg": "Success"
}
```
