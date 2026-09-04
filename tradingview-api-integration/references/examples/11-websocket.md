# Streaming (SSE & WebSocket)

- Source: product docs + handlers
- Live Requests: `disabled` (`tv_api.py` is REST-only; streaming needs a persistent connection)

Streaming is **not** on `https://api.tradingviewapi.com`. Mint a JWT on the REST host, then connect to `ws.tradingviewapi.com`.

```text
POST https://api.tradingviewapi.com/api/token/generate   →  token, wsUrl, sseUrl
GET  https://ws.tradingviewapi.com/sse/stream?token=JWT&symbols=...
WS   wss://ws.tradingviewapi.com/ws?token=JWT
```

Do not call `/sse/stream` on the REST host. Do not send RapidAPI headers to `api.tradingviewapi.com` or `ws.tradingviewapi.com`.

## 1. Mint a stream JWT

`POST /api/token/generate` — see `15-token.md`. Console: `Authorization: Bearer YOUR_API_KEY`, body `{}`. Lifetime follows the Console plan.

```bash
curl --request POST \
  --url 'https://api.tradingviewapi.com/api/token/generate' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data '{}'
```

Use `token` from the JSON. Prefer the returned `sseUrl` / `wsUrl` when they are production hosts; otherwise use the URLs below.

## 2. SSE

`GET https://ws.tradingviewapi.com/sse/stream`

Query:

| Param | Required | Notes |
|-------|----------|--------|
| `token` | yes | JWT. Required for `EventSource` (browsers cannot set Authorization) |
| `symbols` | yes | Comma-separated `EXCHANGE:TICKER` |
| `type` | no | `quote` (default) or `price` (fixed 5-minute candles) |

```bash
curl --request GET \
  --url 'https://ws.tradingviewapi.com/sse/stream?token=YOUR_JWT&symbols=BINANCE:BTCUSDT,NASDAQ:AAPL&type=quote' \
  --header 'Accept: text/event-stream' \
  --no-buffer
```

```javascript
const tokenRes = await fetch('https://api.tradingviewapi.com/api/token/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
  },
  body: JSON.stringify({})
});
const { token, sseUrl } = await tokenRes.json();
const streamUrl = sseUrl || 'https://ws.tradingviewapi.com/sse/stream';

const eventSource = new EventSource(
  `${streamUrl}?token=${token}&symbols=BINANCE:BTCUSDT,NASDAQ:AAPL&type=quote`
);
eventSource.addEventListener('connected', (e) => console.log(JSON.parse(e.data)));
eventSource.addEventListener('quote_update', (e) => {
  const update = JSON.parse(e.data);
  console.log(update.symbol, update.data?.lp);
});
```

Events: `connected`, `quote_update` / `price_update`, `error`, `auth_expiring`, `auth_expired`. Heartbeats are SSE comments (`: heartbeat`), not named events.

## 3. WebSocket

`wss://ws.tradingviewapi.com/ws?token=YOUR_JWT`

After connect, send JSON `{ "action": ... }`.

| action | fields | server `type` |
|--------|--------|----------------|
| `subscribe` | `symbol`, optional `timeframe` (default `5`) | `update` |
| `subscribe_quote` | `symbols` (array or string, ≤10) | `quote_update` |
| `ping` | — | `pong` |
| `status` | — | `status` |
| `unsubscribe` / `unsubscribe_quote` | `id` | `unsubscribed` |

```javascript
import WebSocket from 'ws';

const tokenRes = await fetch('https://api.tradingviewapi.com/api/token/generate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_API_KEY'
  },
  body: JSON.stringify({})
});
const { token, wsUrl } = await tokenRes.json();
const streamUrl = wsUrl || 'wss://ws.tradingviewapi.com/ws';

const ws = new WebSocket(`${streamUrl}?token=${token}`);

ws.on('open', () => {
  ws.send(JSON.stringify({
    action: 'subscribe',
    id: 'price_btc',
    symbol: 'BINANCE:BTCUSDT',
    timeframe: '5'
  }));
  ws.send(JSON.stringify({
    action: 'subscribe_quote',
    id: 'quote_btc',
    symbols: ['BINANCE:BTCUSDT']
  }));
});

ws.on('message', (raw) => {
  const message = JSON.parse(raw.toString());
  if (message.type === 'update') {
    console.log('Price update:', message.symbol, message.data);
  } else if (message.type === 'quote_update') {
    console.log('Quote update:', message.symbol, message.data?.lp);
  }
});
```

```bash
# After minting a JWT:
websocat "wss://ws.tradingviewapi.com/ws?token=YOUR_JWT"
# then send:
# {"action":"subscribe_quote","id":"quote_btc","symbols":["BINANCE:BTCUSDT"]}
```

Limits: ≤10 subscriptions per connection, ≤10 symbols per quote subscription.

Interactive testers: https://www.tradingviewapi.com/ws-test/ and https://www.tradingviewapi.com/sse-test/
