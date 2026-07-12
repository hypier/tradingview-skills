# News

- Source: `openapi.json`
- Live Requests: `disabled`

## Table of Contents

- [Get News List](#get-news-list)
- [Get Bond News](#get-bond-news)
- [Get Crypto News](#get-crypto-news)
- [Get Economic News](#get-economic-news)
- [Get ETF News](#get-etf-news)
- [Get Forex News](#get-forex-news)
- [Get Futures News](#get-futures-news)
- [Get Index News](#get-index-news)
- [Get Stock News](#get-stock-news)
- [Get News Details](#get-news-details)

## Get News List

`GET /api/news`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news?symbol=NASDAQ%3AAAPL&lang=en&market=stock&market_country=US' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "tag:reuters.com,2026:newsml_L1N41401E:0",
        "title": "Apple's new CEO is a product perfectionist taking on the AI age",
        "published": 1776765600,
        "urgency": 2,
        "permission": "headline",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:MSFT",
            "logoid": "microsoft"
          },
          {
            "symbol": "NASDAQ:NVDA",
            "logoid": "nvidia"
          }
        ],
        "storyPath": "/news/reuters.com,2026:newsml_L1N41401E:0-apple-s-new-ceo-is-a-product-perfectionist-taking-on-the-ai-age/",
        "provider": {
          "id": "reuters",
          "name": "Reuters",
          "logo_id": "reuters"
        }
      },
      {
        "id": "DJN_DN20260421001775:0",
        "title": "Tim Cook Told Me His Advice for Apple's Next CEO — WSJ",
        "published": 1776763800,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260421001775:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "DJN_DN20260421001551:0",
        "title": "How Apple Stock Has Fared Under Tim Cook — WSJ",
        "published": 1776761940,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260421001551:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      }
    ],
    "streaming": {
      "channel": "64e27170d46efffb047e96cec6c2"
    },
    "pagination": {
      "cursor": "eyJfaWQiOiJ0YWc6cmV1dGVycy5jb20sMjAyNjpuZXdzbWxfTDROM1pLMU4xIiwicHViZGF0ZSI6MTc3MTk1MDM0NzAwMH0="
    }
  },
  "msg": "Success"
}
```

## Get Bond News

`GET /api/news/bond`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/bond?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "leverage_shares:48fb3b495094b:0",
        "title": "2 Markets 2 Different Tales",
        "published": 1697126697,
        "urgency": 2,
        "link": "https://leverageshares.com/en/insights/2-markets-2-different-tales/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:META",
            "logoid": "meta-platforms"
          },
          {
            "symbol": "NASDAQ:AMZN",
            "logoid": "amazon"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/leverage_shares:48fb3b495094b:0-2-markets-2-different-tales/",
        "provider": {
          "id": "leverage_shares",
          "name": "Leverage Shares",
          "logo_id": "leverage-shares",
          "url": "https://leverageshares.com/en/"
        }
      },
      {
        "id": "leverage_shares:1cbc6e181094b:0",
        "title": "The time for bonds is now",
        "published": 1686832868,
        "urgency": 2,
        "link": "https://leverageshares.com/en/insights/the-time-for-bonds-is-now/",
        "relatedSymbols": [
          {
            "symbol": "LSE:5TLT",
            "logoid": "leverage-shares"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "LSE:1BRN",
            "logoid": "leverage-shares"
          }
        ],
        "storyPath": "/news/leverage_shares:1cbc6e181094b:0-the-time-for-bonds-is-now/",
        "provider": {
          "id": "leverage_shares",
          "name": "Leverage Shares",
          "logo_id": "leverage-shares",
          "url": "https://leverageshares.com/en/"
        }
      },
      {
        "id": "leverage_shares:5763ac7d0094b:0",
        "title": "Bonds vs Equities and the Debt Deal: Is a Winter Coming?",
        "published": 1686031200,
        "urgency": 2,
        "link": "https://leverageshares.com/en/insights/bonds-vs-equities-and-the-debt-deal-is-a-winter-coming/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:QQQ",
            "logoid": "invesco"
          },
          {
            "symbol": "LSE:1BRN",
            "logoid": "leverage-shares"
          }
        ],
        "storyPath": "/news/leverage_shares:5763ac7d0094b:0-bonds-vs-equities-and-the-debt-deal-is-a-winter-coming/",
        "provider": {
          "id": "leverage_shares",
          "name": "Leverage Shares",
          "logo_id": "leverage-shares",
          "url": "https://leverageshares.com/en/"
        }
      }
    ],
    "streaming": {
      "channel": "6ad4500e3ef6a056ee4a96ba7c4c"
    }
  },
  "msg": "Success"
}
```

## Get Crypto News

`GET /api/news/crypto`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/crypto?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "u_today:239b5fe7b094b:0",
        "title": "Breaking: Crypto Holder Tim Cook Resigns as Apple CEO",
        "published": 1776717235,
        "urgency": 2,
        "link": "https://u.today/breaking-crypto-holder-tim-cook-resigns-as-apple-ceo",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/u_today:239b5fe7b094b:0-breaking-crypto-holder-tim-cook-resigns-as-apple-ceo/",
        "provider": {
          "id": "u_today",
          "name": "U.Today",
          "logo_id": "u-today",
          "url": "https://u.today"
        }
      },
      {
        "id": "cointelegraph:bd44c0a64094b:0",
        "title": "Kraken debuts tokenized stock perpetual futures for non-US traders",
        "published": 1771969283,
        "urgency": 2,
        "link": "https://cointelegraph.com/news/kraken-launches-regulated-tokenized-equity-perpetual-futures-for-global-traders?utm_source=rss_feed&utm_medium=rss-trading-view&utm_campaign=rss_partner_inbound",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:TSLA",
            "logoid": "tesla"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:KRAKEN",
            "logoid": "kraken"
          }
        ],
        "storyPath": "/news/cointelegraph:bd44c0a64094b:0-kraken-debuts-tokenized-stock-perpetual-futures-for-non-us-traders/",
        "provider": {
          "id": "cointelegraph",
          "name": "Cointelegraph",
          "logo_id": "cointelegraph-en",
          "url": "https://cointelegraph.com"
        }
      },
      {
        "id": "the_block:a4af798fa094b:0",
        "title": "Kraken rolls out round-the-clock perps for gold, major indexes and stocks like Apple, Nvidia and Tesla",
        "published": 1771954134,
        "urgency": 2,
        "link": "https://www.theblock.co/post/391089/kraken-rolls-out-round-the-clock-perps-gold-major-indexes-stocks-nvidia-apple-tesla?utm_source=tradingview&utm_medium=rss",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:TSLA",
            "logoid": "tesla"
          },
          {
            "symbol": "NASDAQ:KRAKEN",
            "logoid": "kraken"
          }
        ],
        "storyPath": "/news/the_block:a4af798fa094b:0-kraken-rolls-out-round-the-clock-perps-for-gold-major-indexes-and-stocks-like-apple-nvidia-and-tesla/",
        "provider": {
          "id": "the_block",
          "name": "The Block",
          "logo_id": "the-block",
          "url": "https://www.theblock.co/?utm_medium=rss&utm_source=tradingview"
        }
      }
    ],
    "streaming": {
      "channel": "405134b70020975aebf7e607b497"
    }
  },
  "msg": "Success"
}
```

## Get Economic News

`GET /api/news/economic`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/economic?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "invezz:59a983d12094b:0",
        "title": "What’s behind Apple’s strong iPhone growth in China market?",
        "published": 1776414277,
        "urgency": 2,
        "link": "https://invezz.com/news/2026/04/17/how-did-apple-boost-iphone-shipments-despite-china-market-slump/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/invezz:59a983d12094b:0-what-s-behind-apple-s-strong-iphone-growth-in-china-market/",
        "provider": {
          "id": "invezz",
          "name": "Invezz",
          "logo_id": "invezz",
          "url": "https://invezz.com/"
        }
      },
      {
        "id": "invezz:ebe27eb38094b:0",
        "title": "Apple cuts App Store fees in China to 25% amid antitrust pressure",
        "published": 1773385537,
        "urgency": 2,
        "link": "https://invezz.com/news/2026/03/13/apple-cuts-app-store-fees-in-china-as-regulatory-pressure-on-apple-tax-grows/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/invezz:ebe27eb38094b:0-apple-cuts-app-store-fees-in-china-to-25-amid-antitrust-pressure/",
        "provider": {
          "id": "invezz",
          "name": "Invezz",
          "logo_id": "invezz",
          "url": "https://invezz.com/"
        }
      },
      {
        "id": "invezz:62c8d69e5094b:0",
        "title": "Dow Jones Index futures today: eyes all-time high ahead of key catalysts",
        "published": 1769519760,
        "urgency": 2,
        "link": "https://invezz.com/news/2026/01/27/dow-jones-index-futures-today-eyes-all-time-high-ahead-of-key-catalysts/",
        "relatedSymbols": [
          {
            "symbol": "NYSE:UNH",
            "logoid": "unitedhealth"
          },
          {
            "symbol": "NASDAQ:MSFT",
            "logoid": "microsoft"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/invezz:62c8d69e5094b:0-dow-jones-index-futures-today-eyes-all-time-high-ahead-of-key-catalysts/",
        "provider": {
          "id": "invezz",
          "name": "Invezz",
          "logo_id": "invezz",
          "url": "https://invezz.com/"
        }
      }
    ],
    "streaming": {
      "channel": "e704e17892b81c1cf92834d1e355"
    }
  },
  "msg": "Success"
}
```

## Get ETF News

`GET /api/news/etf`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/etf?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "stocktwits:9cafd3a72094b:0",
        "title": "Nasdaq, S&P 500 Futures Steady As Iran Talks, Warsh Hearing Set Market Tone: Why AAPL, AMZN, POET, FRMI, IBRX Are In Focus",
        "published": 1776760781,
        "urgency": 2,
        "link": "https://stocktwits.com/news-articles/markets/equity/nasdaq-sp500-futures-rise-aapl-amzn-poet-frmi-ibrx-stocks-to-watch/cZBIfgmRICh",
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:AMZN",
            "logoid": "amazon"
          },
          {
            "symbol": "BCBA:SPY",
            "logoid": "spdr-sandp500-etf-tr"
          }
        ],
        "storyPath": "/news/stocktwits:9cafd3a72094b:0/",
        "provider": {
          "id": "stocktwits",
          "name": "Stocktwits",
          "logo_id": "stocktwits",
          "url": "https://stocktwits.com/"
        }
      },
      {
        "id": "stocktwits:5692ebe19094b:0",
        "title": "Apple's New CEO Led A Silicon 'Brain Transplant' — Analyst Says That's Exactly Why John Ternus Is Right For Next AI Phase",
        "published": 1776757050,
        "urgency": 2,
        "link": "https://stocktwits.com/news-articles/markets/equity/apple-s-new-ceo-led-a-silicon-brain-transplant-analyst-says-that-s-exactly-why-john-ternus-is-right-for-next-ai-phase/cZBI9pwRICa",
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/stocktwits:5692ebe19094b:0/",
        "provider": {
          "id": "stocktwits",
          "name": "Stocktwits",
          "logo_id": "stocktwits",
          "url": "https://stocktwits.com/"
        }
      },
      {
        "id": "stocktwits:99c909d7b094b:0",
        "title": "Apple After Tim Cook: Analysts See Continuity Pick, Not Vision Play Under New CEO John Ternus",
        "published": 1776740903,
        "urgency": 2,
        "link": "https://stocktwits.com/news-articles/markets/equity/apple-after-tim-cook-analysts-see-continuity-pick-not-vision-play-under-new-ceo-john-ternus/cZBIPluRIzz",
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/stocktwits:99c909d7b094b:0/",
        "provider": {
          "id": "stocktwits",
          "name": "Stocktwits",
          "logo_id": "stocktwits",
          "url": "https://stocktwits.com/"
        }
      }
    ],
    "streaming": {
      "channel": "2cc85ad3d7cfbe99f680dc8a9b32"
    },
    "pagination": {
      "cursor": "eyJfaWQiOiJ6YWNrczpjN2U1NDZjMmUwOTRiIiwicHViZGF0ZSI6MTczMzQ4NDAwNzAwMH0="
    }
  },
  "msg": "Success"
}
```

## Get Forex News

`GET /api/news/forex`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/forex?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "invezz:5bb71649d094b:0",
        "title": "European stocks fall as Trump proposes 50% tariff on EU imports; says talks with them ‘going nowhere’",
        "published": 1748007559,
        "urgency": 2,
        "link": "https://invezz.com/news/2025/05/23/european-stocks-fall-as-trump-proposes-50-tariff-on-eu-imports-says-talks-with-them-going-nowhere/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/invezz:5bb71649d094b:0-european-stocks-fall-as-trump-proposes-50-tariff-on-eu-imports-says-talks-with-them-going-nowhere/",
        "provider": {
          "id": "invezz",
          "name": "Invezz",
          "logo_id": "invezz",
          "url": "https://invezz.com/"
        }
      },
      {
        "id": "invezz:4deb6e0a7094b:0",
        "title": "Apple and Meta face €1.8B enforcement action for EU DMA breaches",
        "published": 1745408010,
        "urgency": 2,
        "link": "https://invezz.com/news/2025/04/23/apple-and-meta-face-e1-8b-enforcement-action-for-eu-dma-breaches/",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "FX:EURUSD",
            "currency-logoid": "country/US",
            "base-currency-logoid": "country/EU"
          }
        ],
        "storyPath": "/news/invezz:4deb6e0a7094b:0-apple-and-meta-face-1-8b-enforcement-action-for-eu-dma-breaches/",
        "provider": {
          "id": "invezz",
          "name": "Invezz",
          "logo_id": "invezz",
          "url": "https://invezz.com/"
        }
      }
    ],
    "streaming": {
      "channel": "b69b9baeb07bb717724e553c947c"
    }
  },
  "msg": "Success"
}
```

## Get Futures News

`GET /api/news/futures`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/futures?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "DJN_DN20260227008205:0",
        "title": "How to Fight AI? The 'Rolex Effect' Could Lift Apple and Other Consumer Brands — Barrons.com",
        "published": 1772213100,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NYSE:MCD",
            "logoid": "mcdonalds"
          },
          {
            "symbol": "NASDAQ:WMT",
            "logoid": "walmart"
          }
        ],
        "storyPath": "/news/DJN_DN20260227008205:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "DJN_DN20260217003591:0",
        "title": "Gold Buying Is Most Crowded Trade, BofA Survey Says — Market Talk",
        "published": 1771331160,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:GOOG",
            "logoid": "alphabet"
          },
          {
            "symbol": "NASDAQ:AMZN",
            "logoid": "amazon"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260217003591:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "tag:reuters.com,2025:newsml_L1N3X20U6:0",
        "title": "US group sues Apple over Congo conflict minerals",
        "published": 1764193852,
        "urgency": 2,
        "permission": "headline",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:TSLA",
            "logoid": "tesla"
          }
        ],
        "storyPath": "/news/reuters.com,2025:newsml_L1N3X20U6:0-us-group-sues-apple-over-congo-conflict-minerals/",
        "provider": {
          "id": "reuters",
          "name": "Reuters",
          "logo_id": "reuters"
        }
      }
    ],
    "streaming": {
      "channel": "769c5fc64e9c84c9374f4c551d2d"
    }
  },
  "msg": "Success"
}
```

## Get Index News

`GET /api/news/index`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/index?symbol=NASDAQ%3AAAPL&lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "DJN_DN20260420009019:0",
        "title": "How Apple Stock Has Fared Under Tim Cook — WSJ",
        "published": 1776724080,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260420009019:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "DJN_DN20260417005980:0",
        "title": "Stocks Hit Records on Iran Truce Hopes. Why the Rally May Have Further to Run. — Barrons.com",
        "published": 1776451200,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:GOOG",
            "logoid": "alphabet"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:META",
            "logoid": "meta-platforms"
          }
        ],
        "storyPath": "/news/DJN_DN20260417005980:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "DJN_SN20260417006000:0",
        "title": "These two sectors have been boosted by AI hopes. Why investors should buy one, and trim exposure to the other.",
        "published": 1776432720,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:NVDA",
            "logoid": "nvidia"
          },
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:MSFT",
            "logoid": "microsoft"
          }
        ],
        "storyPath": "/news/DJN_SN20260417006000:0/",
        "provider": {
          "id": "market-watch",
          "name": "MarketWatch",
          "logo_id": "marketwatch"
        }
      }
    ],
    "streaming": {
      "channel": "f2ed8d1af7cc2ff3c73125e1153b"
    }
  },
  "msg": "Success"
}
```

## Get Stock News

`GET /api/news/stock`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/stock?symbol=NASDAQ%3AAAPL&lang=en&market_country=US' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "items": [
      {
        "id": "tag:reuters.com,2026:newsml_L1N41401E:0",
        "title": "Apple's new CEO is a product perfectionist taking on the AI age",
        "published": 1776765600,
        "urgency": 2,
        "permission": "headline",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          },
          {
            "symbol": "NASDAQ:MSFT",
            "logoid": "microsoft"
          },
          {
            "symbol": "NASDAQ:NVDA",
            "logoid": "nvidia"
          }
        ],
        "storyPath": "/news/reuters.com,2026:newsml_L1N41401E:0-apple-s-new-ceo-is-a-product-perfectionist-taking-on-the-ai-age/",
        "provider": {
          "id": "reuters",
          "name": "Reuters",
          "logo_id": "reuters"
        }
      },
      {
        "id": "DJN_DN20260421001775:0",
        "title": "Tim Cook Told Me His Advice for Apple's Next CEO — WSJ",
        "published": 1776763800,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260421001775:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      },
      {
        "id": "DJN_DN20260421001551:0",
        "title": "How Apple Stock Has Fared Under Tim Cook — WSJ",
        "published": 1776761940,
        "urgency": 2,
        "permission": "provider",
        "relatedSymbols": [
          {
            "symbol": "NASDAQ:AAPL",
            "logoid": "apple"
          }
        ],
        "storyPath": "/news/DJN_DN20260421001551:0/",
        "provider": {
          "id": "dow-jones",
          "name": "Dow Jones Newswires",
          "logo_id": "dow-jones-newswires"
        }
      }
    ],
    "streaming": {
      "channel": "64e27170d46efffb047e96cec6c2"
    },
    "pagination": {
      "cursor": "eyJfaWQiOiJ0YWc6cmV1dGVycy5jb20sMjAyNjpuZXdzbWxfTDROM1pLMU4xIiwicHViZGF0ZSI6MTc3MTk1MDM0NzAwMH0="
    }
  },
  "msg": "Success"
}
```

## Get News Details

`GET /api/news/{newsId}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/news/tag%3Areuters.com%2C2025%3Anewsml_L1N3XK042%3A0?lang=en' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "shortDescription": "At least 10 people were killed and 20 were injured after a bus carrying school children fell off a cliff in rural area in northern Colombia, the local governor said on Sunday.In a post on X, the governor of Antioquia, Andres Julian, said the bus was traveling from the Caribbean town of Tolu to Mede…",
    "astDescription": {
      "type": "root",
      "children": [
        {
          "type": "p",
          "children": [
            "At least 10 people were killed and 20 were injured after a bus carrying school children fell off a cliff in rural area in northern Colombia, the local governor said on Sunday."
          ]
        },
        {
          "type": "p",
          "children": [
            "In a post on X, the governor of Antioquia, Andres Julian, said the bus was traveling from the Caribbean town of Tolu to Medellin after a school trip and was carrying students from the Antioqueño High School. "
          ]
        },
        {
          "type": "p",
          "children": [
            "\"Until now, there are more than 10 dead and 20 injured, Julian said. \"The whole hospital network is ready to attend and support this emergency.\" "
          ]
        }
      ]
    },
    "language": "en",
    "tags": [
      {
        "title": "Reuters",
        "args": [
          {
            "id": "provider",
            "value": "reuters"
          }
        ]
      }
    ],
    "copyright": "Copyright Thomson Reuters 2025. Click For Restrictions - https://agency.reuters.com/en/copyright.html",
    "id": "tag:reuters.com,2025:newsml_L1N3XK042:0",
    "title": "Over 10 dead after school bus accident in Colombia",
    "published": 1765728766,
    "urgency": 2,
    "permission": "headline",
    "storyPath": "/news/reuters.com,2025:newsml_L1N3XK042:0-over-10-dead-after-school-bus-accident-in-colombia/",
    "read_time": 22,
    "provider": {
      "id": "reuters",
      "name": "Reuters",
      "logo_id": "reuters"
    },
    "distributor": {
      "id": "refinitiv",
      "name": "Refinitiv",
      "logo_id": "refinitiv"
    }
  },
  "msg": "Success"
}
```
