# Ideas

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get Hot Ideas](#get-hot-ideas)
- [Get Editor's Picks](#get-editors-picks)
- [Get Symbol Minds](#get-symbol-minds)
- [Get Symbol Idea List](#get-symbol-idea-list)
- [Get Idea Details](#get-idea-details)

## Get Hot Ideas

`GET /api/ideas/hot`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ideas/hot?page=1&lang=en' \
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
      "id": 21844366,
      "image_url": "fiTFLfEh",
      "name": "Bitcoin - LifeTime Opportunity! (right now, watch this)",
      "description": "I see a lifetime opportunity on the chart of Bitcoin! First, let's take a look at technical analysis. The price of Bitcoin has been inside this red bearish flag for around 10 weeks, and soon we will see either an explosive pump or a critical dump. Bitcoin has been in a pretty strong bear market sinc... (1445 more chars truncated)",
      "created_at": "2026-04-20T07:25:18+00:00",
      "updated_at": null,
      "date_timestamp": 1776669918,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/BTCUSDT/fiTFLfEh-Bitcoin-LifeTime-Opportunity-right-now-watch-this/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 84,
      "views_count": 0,
      "symbol": {
        "name": "BINANCE:BTCUSDT",
        "full_name": "BINANCE:BTCUSDT",
        "short_name": "BTCUSDT",
        "exchange": "BINANCE",
        "type": "spot",
        "logo": {
          "style": "single",
          "logoid": "crypto/XTVCBTC"
        },
        "logo_id": null,
        "currency_logo_id": "crypto/XTVCUSDT",
        "base_currency_logo_id": "crypto/XTVCBTC",
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/crypto/XTVCBTC.svg",
          "https://s3-symbol-logo.tradingview.com/crypto/XTVCUSDT.svg"
        ],
        "interval": "720",
        "direction": 2,
        "badge": {
          "label": "BINANCE:BTCUSDT",
          "url": "/symbols/BTCUSDT/"
        }
      },
      "user": {
        "id": 10265490,
        "username": "Xanrox",
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/10265490-BhuM.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/10265490-BhuM_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/f/fiTFLfEh_big.png",
        "middle": "https://s3.tradingview.com/f/fiTFLfEh_mid.png",
        "middle_webp": "https://s3.tradingview.com/f/fiTFLfEh_mid.webp",
        "bg_color": "#ffffff"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 313
    },
    {
      "id": 21845001,
      "image_url": "me9hKsbv",
      "name": "EURUSD Rebound from Support – Targeting Higher Levels",
      "description": "Hello traders! Here’s my technical outlook based on the current EURUSD (1H) chart structure. EURUSD previously moved inside a descending channel, forming lower highs and confirming bearish pressure. After a breakout from this structure, price found a bottom and initiated a recovery phase. The market... (490 more chars truncated)",
      "created_at": "2026-04-20T09:23:28+00:00",
      "updated_at": "2026-04-21T08:31:21+00:00",
      "date_timestamp": 1776677008,
      "updated_date_timestamp": 1776760281,
      "chart_url": "https://www.tradingview.com/chart/EURUSD/me9hKsbv-EURUSD-Rebound-from-Support-Targeting-Higher-Levels/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 17,
      "views_count": 0,
      "symbol": {
        "name": "FOREXCOM:EURUSD",
        "full_name": "FOREXCOM:EURUSD",
        "short_name": "EURUSD",
        "exchange": "FOREXCOM",
        "type": "forex",
        "logo": {
          "style": "pair",
          "logoid": "country/EU",
          "logoid2": "country/US"
        },
        "logo_id": null,
        "currency_logo_id": "country/US",
        "base_currency_logo_id": "country/EU",
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/country/EU.svg",
          "https://s3-symbol-logo.tradingview.com/country/US.svg"
        ],
        "interval": "60",
        "direction": 1,
        "badge": {
          "label": "FOREXCOM:EURUSD",
          "url": "/symbols/EURUSD/"
        }
      },
      "user": {
        "id": 50479193,
        "username": "LegionQ8",
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/50479193-AP0U.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/50479193-AP0U_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/m/me9hKsbv_big.png",
        "middle": "https://s3.tradingview.com/m/me9hKsbv_mid.png",
        "middle_webp": "https://s3.tradingview.com/m/me9hKsbv_mid.webp",
        "bg_color": "#b9dbad"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 27
    },
    {
      "id": 21845365,
      "image_url": "juScwUN8",
      "name": "Gold: Institutional Distribution at the Apex.",
      "description": "The Macro View: The \"Peace Premium\" Unwinds 🛰️\nFollowing the historic April 8 ceasefire agreement, the safe-haven demand that drove Gold toward $5,000 earlier this year is starting to evaporate. While the Singapore Peace Talks provide a glimmer of hope, the \"higher-for-longer\" interest rate environm... (1447 more chars truncated)",
      "created_at": "2026-04-20T10:27:52+00:00",
      "updated_at": null,
      "date_timestamp": 1776680872,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/XAUUSD/juScwUN8-Gold-Institutional-Distribution-at-the-Apex/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 20,
      "views_count": 0,
      "symbol": {
        "name": "OANDA:XAUUSD",
        "full_name": "OANDA:XAUUSD",
        "short_name": "XAUUSD",
        "exchange": "OANDA",
        "type": "commodity",
        "logo": {
          "style": "single",
          "logoid": "metal/gold"
        },
        "logo_id": "metal/gold",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/metal/gold.svg"
        ],
        "interval": "240",
        "direction": 2,
        "badge": {
          "label": "OANDA:XAUUSD",
          "url": "/symbols/XAUUSD/"
        }
      },
      "user": {
        "id": 6991428,
        "username": "Lingrid",
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/6991428-YT1U.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/6991428-YT1U_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/j/juScwUN8_big.png",
        "middle": "https://s3.tradingview.com/j/juScwUN8_mid.png",
        "middle_webp": "https://s3.tradingview.com/j/juScwUN8_mid.webp",
        "bg_color": "#ffffff"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 48
    }
  ],
  "msg": "Success"
}
```

## Get Editor's Picks

`GET /api/ideas/editors-picks`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ideas/editors-picks?page=1&lang=en' \
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
      "id": 21844919,
      "image_url": "B7m1wZ3G",
      "name": "Dogecoin (DOGE) Update bullish potential ",
      "description": "Dogecoin is currently consolidating within a tight local range, signaling a potential expansion move on the horizon as volatility continues to compress.\n\nPrice action has been accompanied by declining volume, which typically precedes a breakout scenario. As the range tightens, the market is building... (980 more chars truncated)",
      "created_at": "2026-04-20T09:07:25+00:00",
      "updated_at": null,
      "date_timestamp": 1776676045,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/DOGEUSDT/B7m1wZ3G-Dogecoin-DOGE-Update-bullish-potential/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": true,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 24,
      "views_count": 0,
      "symbol": {
        "name": "BINANCE:DOGEUSDT",
        "full_name": "BINANCE:DOGEUSDT",
        "short_name": "DOGEUSDT",
        "exchange": "BINANCE",
        "type": "spot",
        "logo": {
          "style": "single",
          "logoid": "crypto/XTVCDOGE"
        },
        "logo_id": null,
        "currency_logo_id": "crypto/XTVCUSDT",
        "base_currency_logo_id": "crypto/XTVCDOGE",
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/crypto/XTVCDOGE.svg",
          "https://s3-symbol-logo.tradingview.com/crypto/XTVCUSDT.svg"
        ],
        "interval": "1D",
        "direction": 1,
        "badge": {
          "label": "BINANCE:DOGEUSDT",
          "url": "/symbols/DOGEUSDT/"
        }
      },
      "user": {
        "id": 1648190,
        "username": "The_Alchemist_Trader_",
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/1648190-4kyx.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/1648190-4kyx_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/b/B7m1wZ3G_big.png",
        "middle": "https://s3.tradingview.com/b/B7m1wZ3G_mid.png",
        "middle_webp": "https://s3.tradingview.com/b/B7m1wZ3G_mid.webp",
        "bg_color": "#dadada"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 16
    },
    {
      "id": 21845323,
      "image_url": "EBBTkbEQ",
      "name": "Nasdaq Soars 20% in Three Weeks. Boom Just in Time for Earnings?",
      "description": "The tech-heavy Nasdaq Composite  NASDAQ:IXIC  has climbed nearly 20% from its March 30 low, delivering the fastest rebound traders have seen this year. Moves of that size usually arrive alongside strong catalysts, shifting expectations, or a sudden improvement in global mood.\n\nThis time the spark ca... (3735 more chars truncated)",
      "created_at": "2026-04-20T10:22:38+00:00",
      "updated_at": null,
      "date_timestamp": 1776680558,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/IXIC/EBBTkbEQ-Nasdaq-Soars-20-in-Three-Weeks-Boom-Just-in-Time-for-Earnings/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": true,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 12,
      "views_count": 0,
      "symbol": {
        "name": "NASDAQ:IXIC",
        "full_name": "NASDAQ:IXIC",
        "short_name": "IXIC",
        "exchange": "NASDAQ",
        "type": "index",
        "logo": {
          "style": "single",
          "logoid": "indices/nasdaq-composite"
        },
        "logo_id": "indices/nasdaq-composite",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/indices/nasdaq-composite.svg"
        ],
        "interval": "1D",
        "direction": 0,
        "badge": {
          "label": "NASDAQ:IXIC",
          "url": "/symbols/NASDAQ-IXIC/"
        }
      },
      "user": {
        "id": 6171439,
        "username": "TradingView",
        "badges": [
          {
            "name": "employee",
            "verbose_name": "TradingView employee"
          },
          {
            "name": "moderator",
            "verbose_name": "TradingView moderator"
          },
          {
            "name": "pro:pro_premium_expert",
            "verbose_name": "Ultimate"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/6171439-mFQX.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/6171439-mFQX_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium_expert",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/e/EBBTkbEQ_big.png",
        "middle": "https://s3.tradingview.com/e/EBBTkbEQ_mid.png",
        "middle_webp": "https://s3.tradingview.com/e/EBBTkbEQ_mid.webp",
        "bg_color": "#ffffff"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 114
    },
    {
      "id": 21843137,
      "image_url": "CQpkz6PH",
      "name": "IREN | Weekly",
      "description": "NASDAQ:IREN   — Quantum Model Projection  \nBullish Outlook | Projected Extension Underway\n IREN  has advanced 62% since late March, firmly supported by the  Q-Structure λₛ  at precise confluence, as projected—reinforcing the Primary degree Extension in Wave ⓹ now underway.\n\n Wave Analysis \nThis impu... (704 more chars truncated)",
      "created_at": "2026-04-20T03:04:57+00:00",
      "updated_at": null,
      "date_timestamp": 1776654297,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/IREN/CQpkz6PH-IREN-Weekly/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": true,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 13,
      "views_count": 0,
      "symbol": {
        "name": "NASDAQ:IREN",
        "full_name": "NASDAQ:IREN",
        "short_name": "IREN",
        "exchange": "NASDAQ",
        "type": "stock",
        "logo": {
          "style": "single",
          "logoid": "iris-energy"
        },
        "logo_id": "iris-energy",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/iris-energy.svg"
        ],
        "interval": "1W",
        "direction": 0,
        "badge": {
          "label": "NASDAQ:IREN",
          "url": "/symbols/NASDAQ-IREN/"
        }
      },
      "user": {
        "id": 3586699,
        "username": "ElliottChart",
        "badges": [],
        "picture_url": "https://s3.tradingview.com/userpics/3586699-k384.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/3586699-k384_mid.png",
        "is_pro": false,
        "pro_plan": "",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/c/CQpkz6PH_big.png",
        "middle": "https://s3.tradingview.com/c/CQpkz6PH_mid.png",
        "middle_webp": "https://s3.tradingview.com/c/CQpkz6PH_mid.webp",
        "bg_color": "#ffffff"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 70
    }
  ],
  "msg": "Success"
}
```

## Get Symbol Minds

`GET /api/ideas/{symbol}/minds`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ideas/NASDAQ:AAPL/minds?lang=en' \
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
      "symbols": {
        "AAPL": "NASDAQ:AAPL"
      },
      "uid": "3rdYQ6DKRhCutEzz5uRvmA",
      "url": "https://www.tradingview.com/symbols/NASDAQ-AAPL/minds/?mind=3rdYQ6DKRhCutEzz5uRvmA",
      "text_ast": {
        "type": "root",
        "children": [
          {
            "type": "symbol",
            "params": {
              "text": "AAPL",
              "symbol": "NASDAQ:AAPL",
              "pageUrl": "/symbols/NASDAQ-AAPL/",
              "logo": {
                "style": "single",
                "logoid": "apple"
              },
              "logoId": "apple",
              "baseCurrencyLogoId": null,
              "currencyLogoId": "country/US"
            }
          },
          " 🧊 248 — we are heading there."
        ]
      },
      "author": {
        "username": "DmitriiPaninDP",
        "uri": "/u/DmitriiPaninDP/",
        "is_broker": false,
        "avatars": {
          "small": "https://s3.tradingview.com/userpics/93393724-DEpA.png",
          "mid": "https://s3.tradingview.com/userpics/93393724-DEpA_mid.png",
          "big": "https://s3.tradingview.com/userpics/93393724-DEpA_big.png",
          "orig": "https://s3.tradingview.com/userpics/93393724-DEpA_orig.png"
        },
        "badges": [
          {
            "name": "pro:pro",
            "verbose_name": "Essential"
          }
        ],
        "is_followed": false
      },
      "created": "2026-04-20T23:28:17.311820+00:00",
      "hidden": false,
      "aliases": [
        "stock@pn@NASDAQ:AAPL"
      ],
      "total_likes": 4,
      "total_comments": 3,
      "text": "$AAPL 🧊 248 — we are heading there."
    },
    {
      "symbols": {
        "AAPL": "NASDAQ:AAPL"
      },
      "uid": "AHV9n5wdRd-7pQqsuvhw5g",
      "url": "https://www.tradingview.com/symbols/NASDAQ-AAPL/minds/?mind=AHV9n5wdRd-7pQqsuvhw5g",
      "text_ast": {
        "type": "root",
        "children": [
          {
            "type": "symbol",
            "params": {
              "text": "AAPL",
              "symbol": "NASDAQ:AAPL",
              "pageUrl": "/symbols/NASDAQ-AAPL/",
              "logo": {
                "style": "single",
                "logoid": "apple"
              },
              "logoId": "apple",
              "baseCurrencyLogoId": null,
              "currencyLogoId": "country/US"
            }
          },
          " Ignoring the news and buying the breakout .. lets see if goes down will add more but I doubt it will"
        ]
      },
      "author": {
        "username": "IDONTKNOW2",
        "uri": "/u/IDONTKNOW2/",
        "is_broker": false,
        "avatars": {
          "small": "data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220,0,20,20%22%20width=%2239%22%20height=%2239%22%3E%3Crect%20height=%2220%22%20width=%2220%22%20fill=%22hsl%28201,25%25,50%25%29%22/%3E%3Ctext%20fill=%22white%22%20x=%2210%22%20y=%2214.8%22%20font-size=%2214%22%20font-fam... (134 more chars truncated)",
          "mid": "data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220,0,20,20%22%20width=%2296%22%20height=%2296%22%3E%3Crect%20height=%2220%22%20width=%2220%22%20fill=%22hsl%28201,25%25,50%25%29%22/%3E%3Ctext%20fill=%22white%22%20x=%2210%22%20y=%2214.8%22%20font-size=%2214%22%20font-fam... (134 more chars truncated)",
          "big": "data:image/svg+xml,%3Csvg%20xmlns=%22http://www.w3.org/2000/svg%22%20viewBox=%220,0,20,20%22%20width=%22320%22%20height=%22320%22%3E%3Crect%20height=%2220%22%20width=%2220%22%20fill=%22hsl%28201,25%25,50%25%29%22/%3E%3Ctext%20fill=%22white%22%20x=%2210%22%20y=%2214.8%22%20font-size=%2214%22%20font-f... (136 more chars truncated)"
        },
        "badges": [
          {
            "name": "pro:pro",
            "verbose_name": "Essential"
          }
        ],
        "is_followed": false
      },
      "created": "2026-04-20T22:22:22.884910+00:00",
      "hidden": false,
      "aliases": [
        "stock@pn@NASDAQ:AAPL"
      ],
      "total_likes": 1,
      "total_comments": 0,
      "text": "$AAPL Ignoring the news and buying the breakout .. lets see if goes down will add more but I doubt it will"
    },
    {
      "symbols": {
        "AAPL": "NASDAQ:AAPL"
      },
      "uid": "JuQEZfYiShGBH7HI9T1WZg",
      "url": "https://www.tradingview.com/symbols/NASDAQ-AAPL/minds/?mind=JuQEZfYiShGBH7HI9T1WZg",
      "text_ast": {
        "type": "root",
        "children": [
          {
            "type": "symbol",
            "params": {
              "text": "AAPL",
              "symbol": "NASDAQ:AAPL",
              "pageUrl": "/symbols/NASDAQ-AAPL/",
              "logo": {
                "style": "single",
                "logoid": "apple"
              },
              "logoId": "apple",
              "baseCurrencyLogoId": null,
              "currencyLogoId": "country/US"
            }
          },
          " isnt it good news that he is gone for good?"
        ]
      },
      "author": {
        "username": "FI101581416151811",
        "uri": "/u/FI101581416151811/",
        "is_broker": false,
        "avatars": {
          "small": "https://s3.tradingview.com/userpics/76808800-xefb.png",
          "mid": "https://s3.tradingview.com/userpics/76808800-xefb_mid.png",
          "big": "https://s3.tradingview.com/userpics/76808800-xefb_big.png",
          "orig": "https://s3.tradingview.com/userpics/76808800-xefb_orig.png"
        },
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "is_followed": false
      },
      "created": "2026-04-20T21:01:22.058563+00:00",
      "hidden": false,
      "aliases": [
        "stock@pn@NASDAQ:AAPL"
      ],
      "total_likes": 8,
      "total_comments": 0,
      "text": "$AAPL isnt it good news that he is gone for good?"
    }
  ],
  "msg": "Success"
}
```

## Get Symbol Idea List

`GET /api/ideas/list/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ideas/list/NASDAQ:AAPL?page=1&per_page=5&lang=en' \
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
      "id": 21851695,
      "image_url": "WgdZsc11",
      "name": "Apple Inc (AAPL): Stock Approaches Resistance, Anticipate Sell",
      "description": "Apple (AAPL) stock is trading around $271-$273, with a market cap of over $4 trillion. the major news shaking the market is that CEO Tim Cook will step down on Sept. 1 to  become executive chairman, with John Ternus taking over as CEO, causing a slight dip in Apple stock.\n\nTechnical outlook:\nThe sto... (374 more chars truncated)",
      "created_at": "2026-04-21T09:18:52+00:00",
      "updated_at": null,
      "date_timestamp": 1776763132,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/AAPL/WgdZsc11-Apple-Inc-AAPL-Stock-Approaches-Resistance-Anticipate-Sell/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 0,
      "views_count": 0,
      "symbol": {
        "name": "NASDAQ:AAPL",
        "full_name": "NASDAQ:AAPL",
        "short_name": "AAPL",
        "exchange": "NASDAQ",
        "type": "stock",
        "logo": {
          "style": "single",
          "logoid": "apple"
        },
        "logo_id": "apple",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/apple.svg"
        ],
        "interval": "240",
        "direction": 2,
        "badge": {
          "label": "NASDAQ:AAPL",
          "url": "/symbols/NASDAQ-AAPL/"
        }
      },
      "user": {
        "id": 34169602,
        "username": "Blaisefxacademy",
        "badges": [],
        "picture_url": "https://s3.tradingview.com/userpics/34169602-B4G7.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/34169602-B4G7_mid.png",
        "is_pro": false,
        "pro_plan": "",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/w/WgdZsc11_big.png",
        "middle": "https://s3.tradingview.com/w/WgdZsc11_mid.png",
        "middle_webp": "https://s3.tradingview.com/w/WgdZsc11_mid.webp",
        "bg_color": "#131722"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 1
    },
    {
      "id": 21848515,
      "image_url": "8LnGpJNe",
      "name": "APPLE: Last short opportunity of the Bear Cycle.",
      "description": "Apple is bullish on its 1D technical outlook (RSI = 66.506, MACD = 2.180, ADX = 26.987) but this move is reaching its end as the price is almost at the top of the Bear Cycle's Channel Down. That is the exact same pattern of start of the 2022 Bear Cycle. All patterns and sequences that led to both Ch... (368 more chars truncated)",
      "created_at": "2026-04-20T19:39:19+00:00",
      "updated_at": null,
      "date_timestamp": 1776713959,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/AAPL/8LnGpJNe-APPLE-Last-short-opportunity-of-the-Bear-Cycle/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": false,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 0,
      "views_count": 0,
      "symbol": {
        "name": "NASDAQ:AAPL",
        "full_name": "NASDAQ:AAPL",
        "short_name": "AAPL",
        "exchange": "NASDAQ",
        "type": "stock",
        "logo": {
          "style": "single",
          "logoid": "apple"
        },
        "logo_id": "apple",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/apple.svg"
        ],
        "interval": "1W",
        "direction": 2,
        "badge": {
          "label": "NASDAQ:AAPL",
          "url": "/symbols/NASDAQ-AAPL/"
        }
      },
      "user": {
        "id": 2935073,
        "username": "InvestingScope",
        "badges": [
          {
            "name": "pro:pro_premium",
            "verbose_name": "Premium"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/2935073-szBu.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/2935073-szBu_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium",
        "is_broker": false,
        "broker_name": null,
        "broker_plan": null
      },
      "image": {
        "big": "https://s3.tradingview.com/8/8LnGpJNe_big.png",
        "middle": "https://s3.tradingview.com/8/8LnGpJNe_mid.png",
        "middle_webp": "https://s3.tradingview.com/8/8LnGpJNe_mid.webp",
        "bg_color": "#ffffff"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 4
    },
    {
      "id": 21847066,
      "image_url": "ePkX43HZ",
      "name": "Apple Wave Analysis – 20 April 2026 \t",
      "description": "\t\n- Apple broke weekly Triangle\n- Likely to rise to resistance level 280.00\n\nApple recently broke the resistance area between the long-term resistance level 265.0, resistance trendline of the weekly Triangle from 2025 and the 50% Fibonacci correction of the downward impulse from December.\n\t\nThe brea... (262 more chars truncated)",
      "created_at": "2026-04-20T15:11:48+00:00",
      "updated_at": null,
      "date_timestamp": 1776697908,
      "updated_date_timestamp": null,
      "chart_url": "https://www.tradingview.com/chart/AAPL/ePkX43HZ-Apple-Wave-Analysis-20-April-2026/",
      "is_public": true,
      "is_visible": true,
      "is_video": false,
      "is_education": false,
      "is_script": false,
      "is_picked": false,
      "is_hot": true,
      "is_platinum_broker_idea": true,
      "script_type": null,
      "script_access": null,
      "script_id_part": null,
      "version": null,
      "script_package_id": null,
      "video_duration": "0",
      "video_cam": false,
      "video_filename": null,
      "comments_count": 0,
      "views_count": 0,
      "symbol": {
        "name": "NASDAQ:AAPL",
        "full_name": "NASDAQ:AAPL",
        "short_name": "AAPL",
        "exchange": "NASDAQ",
        "type": "stock",
        "logo": {
          "style": "single",
          "logoid": "apple"
        },
        "logo_id": "apple",
        "currency_logo_id": "country/US",
        "base_currency_logo_id": null,
        "logo_urls": [
          "https://s3-symbol-logo.tradingview.com/apple.svg"
        ],
        "interval": "1D",
        "direction": 1,
        "badge": {
          "label": "NASDAQ:AAPL",
          "url": "/symbols/NASDAQ-AAPL/"
        }
      },
      "user": {
        "id": 52419268,
        "username": "FxPro",
        "badges": [
          {
            "name": "broker:platinum",
            "verbose_name": "Platinum partner"
          }
        ],
        "picture_url": "https://s3.tradingview.com/userpics/52419268-747g.png",
        "mid_picture_url": "https://s3.tradingview.com/userpics/52419268-747g_mid.png",
        "is_pro": true,
        "pro_plan": "pro_premium_expert",
        "is_broker": true,
        "broker_name": "FxPro",
        "broker_plan": "platinum"
      },
      "image": {
        "big": "https://s3.tradingview.com/e/ePkX43HZ_big.png",
        "middle": "https://s3.tradingview.com/e/ePkX43HZ_mid.png",
        "middle_webp": "https://s3.tradingview.com/e/ePkX43HZ_mid.webp",
        "bg_color": "#0d1421"
      },
      "reputation": null,
      "actions": null,
      "is_liked": false,
      "likes_count": 2
    }
  ],
  "msg": "Success"
}
```

## Get Idea Details

`GET /api/ideas/{imageUrl}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ideas/LfKFTY2N' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "id": 21599612,
    "uuid": "LfKFTY2N",
    "chart_url": "/chart/XAUUSD/LfKFTY2N-XAUUSD-Rejection-From-5-240-May-Send-Price-to-5-090/",
    "is_script": false,
    "name": "XAUUSD Rejection From 5,240 May Send Price to 5,090",
    "description": "Hello traders! Here’s my technical outlook based on the current XAUUSD (3H) chart structure. Gold previously moved in a bullish ascending channel, forming higher highs and higher lows while respecting the rising support line. The rally eventually reached the 5,240 Seller Zone, where strong resistanc... (818 more chars truncated)",
    "interval": "180",
    "direction": 2,
    "webp_url": "https://s3.tradingview.com/l/LfKFTY2N_mid.webp",
    "user": {
      "username": "LegionQ8",
      "uri": "/u/LegionQ8/",
      "is_broker": false,
      "avatars": {
        "small": "https://s3.tradingview.com/userpics/50479193-AP0U.png",
        "mid": "https://s3.tradingview.com/userpics/50479193-AP0U_mid.png",
        "big": "https://s3.tradingview.com/userpics/50479193-AP0U_big.png",
        "orig": "https://s3.tradingview.com/userpics/50479193-AP0U_orig.png"
      },
      "badges": [
        {
          "name": "pro:pro_premium",
          "verbose_name": "Premium"
        }
      ]
    },
    "symbol": {
      "pro_symbol": "FOREXCOM:XAUUSD",
      "short_name": "XAUUSD",
      "exchange": "FOREXCOM",
      "type": "commodity",
      "typespecs": [
        "cfd"
      ],
      "tv_symbol_page_url_force_exchange": [
        "/symbols/XAUUSD/",
        "?exchange=FOREXCOM"
      ],
      "ticker_title": "Gold Spot / U.S. Dollar",
      "instrument_name": "Gold Spot / U.S. Dollar",
      "medium_logo_urls": [
        "https://s3-symbol-logo.tradingview.com/metal/gold.svg"
      ],
      "logo": {
        "style": "single",
        "logoid": "metal/gold"
      },
      "logo_id": "metal/gold",
      "currency_logo_id": "country/US",
      "country": ""
    },
    "video": {},
    "flags": {
      "is_education": false,
      "is_public": true,
      "is_visible": true,
      "is_suggested": true,
      "is_picked": false,
      "is_favored": false,
      "is_voted": false,
      "is_author_followed": false
    },
    "created_at": "2026-03-11T09:56:40.427365+00:00",
    "updated_at": "2026-03-13T09:41:37.879948+00:00",
    "likes_count": 146,
    "comments_count": 42,
    "views": 8025,
    "description_ast": {
      "type": "root",
      "children": [
        "Hello traders! Here’s my technical outlook based on the current XAUUSD (3H) chart structure. Gold previously moved in a bullish ascending channel, forming higher highs and higher lows while respecting the rising support line. The rally eventually reached the 5,240 Seller Zone, where strong resistanc... (818 more chars truncated)"
      ]
    },
    "user_signature_socials": {
      "socials_list": [
        "Twitter",
        "Youtube",
        "Facebook"
      ],
      "twitter_username": "",
      "instagram_username": "",
      "youtube_channel": "",
      "facebook_username": "",
      "website": "https://bit.ly/4g4wovR",
      "signature": "🔷Join my telegram channel for free - www.bit.ly/4g4wovR\r\n\r\n💰Want receive more profitable signals for Crypto & Forex market, write me  PM 👉 www.bit.ly/4fNijD8\r\n\r\nThinkMarkets Ambassador Join & explore: https://bit.ly/3S4HwPq",
      "signature_ast": {
        "type": "root",
        "children": [
          "🔷Join my telegram channel for free - ",
          {
            "type": "url",
            "params": {
              "url": "https://www.bit.ly/4g4wovR",
              "linkText": "bit.ly/4g4wovR",
              "relFollow": false
            }
          },
          "\r\n\r\n💰Want receive more profitable signals for Crypto & Forex market, write me  PM 👉 "
        ]
      }
    },
    "updates": [
      {
        "id": 8156714,
        "created_at": "2026-03-12T09:47:42.573272+00:00",
        "description": "The price of gold was gradually falling but buyers came in. I think this will be a small correction, after which the movement will resume to our target.",
        "description_ast": {
          "type": "root",
          "children": [
            "The price of gold was gradually falling but buyers came in. I think this will be a small correction, after which the movement will resume to our target."
          ]
        },
        "type": "trading",
        "value": "active",
        "label": "Trade active",
        "could_be_modified": false
      },
      {
        "id": 8160583,
        "created_at": "2026-03-13T09:41:37.879948+00:00",
        "description": "Our analysis worked perfectly for gold. As we expected, gold continued to form lower highs and squeezed closer to the support zone. Our target was achieved!",
        "description_ast": {
          "type": "root",
          "children": [
            "Our analysis worked perfectly for gold. As we expected, gold continued to form lower highs and squeezed closer to the support zone. Our target was achieved!"
          ]
        },
        "type": "close_position",
        "value": "target_reached",
        "label": "Trade closed: target reached",
        "could_be_modified": false
      }
    ],
    "tags": [
      {
        "tag": "analysis",
        "title": "analysis",
        "script_full_url": "/scripts/analysis/",
        "idea_full_url": "/ideas/analysis/"
      },
      {
        "tag": "breakout",
        "title": "breakout",
        "script_full_url": "/scripts/breakout/",
        "idea_full_url": "/ideas/breakout/"
      },
      {
        "tag": "forex",
        "title": "Forex",
        "script_full_url": "/scripts/forex/",
        "idea_full_url": "/ideas/forex/"
      }
    ],
    "related": [],
    "script_terms": "",
    "preview_image_urls": {
      "original": "https://s3.tradingview.com/l/LfKFTY2N.png",
      "thumb": "https://s3.tradingview.com/l/LfKFTY2N_171_121.png",
      "crop": "https://s3.tradingview.com/l/LfKFTY2N_big.png",
      "mid": "https://s3.tradingview.com/l/LfKFTY2N_mid.png"
    },
    "language": "en",
    "page_title": "XAUUSD Rejection From 5,240 May Send Price to 5,090 for FOREXCOM:XAUUSD by LegionQ8",
    "webp_size": {
      "width": 466,
      "height": 275
    },
    "content": "{\"name\":\"Vlad\",\"layout\":\"s\",\"charts\":[{\"panes\":[{\"sources\":[{\"type\":\"MainSeries\",\"id\":\"_seriesId\",\"zorder\":0,\"haStyle\":{\"studyId\":\"BarSetHeikenAshi@tv-basicstudies-60\"},\"renkoStyle\":{\"studyId\":\"BarSetRenko@tv-prostudies-73\"},\"pbStyle\":{\"studyId\":\"BarSetPriceBreak@tv-prostudies-34\"},\"kagiStyle\":{\"stu... (82142 more chars truncated)"
  },
  "msg": "Success"
}
```
