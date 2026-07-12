# Technical Analysis

- Source: `openapi.json`
- Live Requests: `disabled`

## Get Technical Analysis

`GET /api/ta/{symbol}`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ta/BINANCE:BTCUSDT' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "1": {
      "Other": -0.364,
      "All": 0.352,
      "MA": 1.066
    },
    "5": {
      "Other": 0,
      "All": 0.8,
      "MA": 1.6
    },
    "15": {
      "Other": 0.364,
      "All": 1.116,
      "MA": 1.866
    },
    "60": {
      "Other": 0.182,
      "All": 0.89,
      "MA": 1.6
    },
    "240": {
      "Other": 0.364,
      "All": 1.116,
      "MA": 1.866
    },
    "1D": {
      "Other": 0.364,
      "All": 0.848,
      "MA": 1.334
    },
    "1W": {
      "Other": 0.182,
      "All": -0.042,
      "MA": -0.266
    },
    "1M": {
      "Other": 0.364,
      "All": 0.028,
      "MA": -0.308
    }
  },
  "msg": "Success"
}
```

## Get Technical Indicators

`GET /api/ta/{symbol}/indicators`

### Request

```bash
curl --request GET \
	--url 'https://tradingview-data1.p.rapidapi.com/api/ta/BINANCE:BTCUSDT/indicators' \
	--header 'x-rapidapi-host: tradingview-data1.p.rapidapi.com' \
	--header 'x-rapidapi-key: YOUR_RAPIDAPI_KEY'
```

### Response

OpenAPI example / fallback

```json
{
  "success": true,
  "data": {
    "ADX": 19.652487681663818,
    "ADX+DI": 24.161442624343998,
    "ADX+DI[1]": 24.107709917495246,
    "ADX-DI": 15.05945224768997,
    "ADX-DI[1]": 15.715010661700024,
    "AO": 5023.2678823530005,
    "AO[1]": 4773.818411764762,
    "AO[2]": 4652.421588235346,
    "BBPower": 3981.3408482531813,
    "CCI20": 100.11052098023349,
    "CCI20[1]": 86.76734493591583,
    "EMA10": 74737.38969492068,
    "EMA100": 75326.92229783579,
    "EMA20": 73217.74048133395,
    "EMA200": 82716.66996703345,
    "EMA30": 72368.08882100371,
    "EMA50": 72121.6629370694,
    "HullMA9": 75657.53885185186,
    "Ichimoku.BLine": 71666.5,
    "MACD.macd": 1744.5528285901528,
    "MACD.signal": 1382.1135122461487,
    "Mom": 3474.399999999994,
    "Mom[1]": 2878.279999999999,
    "Pivot.M.Camarilla.Middle": 69761.49333333333,
    "Pivot.M.Camarilla.R1": 69292.81333333332,
    "Pivot.M.Camarilla.R2": 70301.14666666667,
    "Pivot.M.Camarilla.R3": 71309.48,
    "Pivot.M.Camarilla.S1": 67276.14666666667,
    "Pivot.M.Camarilla.S2": 66267.81333333332,
    "Pivot.M.Camarilla.S3": 65259.479999999996,
    "Pivot.M.Classic.Middle": 69761.49333333333,
    "Pivot.M.Classic.R1": 74522.98666666666,
    "Pivot.M.Classic.R2": 80761.49333333333,
    "Pivot.M.Classic.R3": 91761.49333333333,
    "Pivot.M.Classic.S1": 63522.986666666664,
    "Pivot.M.Classic.S2": 58761.49333333333,
    "Pivot.M.Classic.S3": 47761.49333333333,
    "Pivot.M.Demark.Middle": 71321.12,
    "Pivot.M.Demark.R1": 77642.23999999999,
    "Pivot.M.Demark.S1": 66642.23999999999,
    "Pivot.M.Fibonacci.Middle": 69761.49333333333,
    "Pivot.M.Fibonacci.R1": 73963.49333333333,
    "Pivot.M.Fibonacci.R2": 76559.49333333333,
    "Pivot.M.Fibonacci.R3": 80761.49333333333,
    "Pivot.M.Fibonacci.S1": 65559.49333333333,
    "Pivot.M.Fibonacci.S2": 62963.49333333333,
    "Pivot.M.Fibonacci.S3": 58761.49333333333,
    "Pivot.M.Woodie.Middle": 69392.245,
    "Pivot.M.Woodie.R1": 73784.48999999999,
    "Pivot.M.Woodie.R2": 80392.245,
    "Pivot.M.Woodie.R3": 84784.48999999999,
    "Pivot.M.Woodie.S1": 62784.48999999999,
    "Pivot.M.Woodie.S2": 58392.244999999995,
    "Pivot.M.Woodie.S3": 51784.48999999999,
    "RSI": 61.82380259524976,
    "RSI[1]": 60.33441551235267,
    "Rec.BBPower": 0,
    "Rec.HullMA9": 1,
    "Rec.Ichimoku": 0,
    "Rec.Stoch.RSI": 0,
    "Rec.UO": 0,
    "Rec.VWMA": 1,
    "Rec.WR": 0,
    "Recommend.All": 0.4242424242424242,
    "Recommend.MA": 0.6666666666666666,
    "Recommend.Other": 0.18181818181818182,
    "SMA10": 74817.88899999997,
    "SMA100": 74026.97649999989,
    "SMA20": 72401.07099999985,
    "SMA200": 86126.64559999997,
    "SMA30": 71054.4153333333,
    "SMA50": 70724.1136,
    "Stoch.D": 71.76148025655341,
    "Stoch.D[1]": 66.97928657906914,
    "Stoch.K": 70.22421715944361,
    "Stoch.K[1]": 58.75843873494322,
    "Stoch.RSI.K": 47.9155229090232,
    "UO": 53.173206181041856,
    "VWMA": 72547.21213218366,
    "W.R": -23.07664929452145,
    "close": 76517.56
  },
  "msg": "Success"
}
```
