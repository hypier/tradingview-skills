# Install hosted TradingView MCP

Public one-click page: https://www.tradingviewapi.com/mcp/

Hosted URL: `https://mcp.tradingviewapi.com/mcp` (`"type": "http"`). After install, sign in with Console in the browser. Do **not** put a Console or RapidAPI key on that URL.

Plans: **Basic** (testing), **Ultra** / **Mega** (production). **Pro does not include MCP.** Account: https://console.tvapis.com/start.

Give the user **only the client they are using**. Detect Cursor, VS Code, Claude Code, Claude Desktop, Codex, Gemini, or Windsurf from the session. If unknown, ask which client.

Local `npx -y @ivotoby/openapi-mcp-server` exposes REST-shaped tools, not hosted `tradingview_*`. This skill needs the hosted tools.

## Cursor

One-click (adds the server, then sign in): [Add to Cursor](cursor://anysphere.cursor-deeplink/mcp/install?name=tradingview&config=eyJ0eXBlIjoiaHR0cCIsInVybCI6Imh0dHBzOi8vbWNwLnRyYWRpbmd2aWV3YXBpLmNvbS9tY3AifQ==)

Or paste into `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "tradingview": {
      "type": "http",
      "url": "https://mcp.tradingviewapi.com/mcp"
    }
  }
}
```

Reload MCP (or restart Cursor) and complete Console login.

## VS Code / GitHub Copilot

One-click: [Install in VS Code](vscode:mcp/install?%7B%22name%22%3A%22tradingview%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A//mcp.tradingviewapi.com/mcp%22%7D) · [VS Code Insiders](vscode-insiders:mcp/install?%7B%22name%22%3A%22tradingview%22%2C%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A//mcp.tradingviewapi.com/mcp%22%7D)

Then use Copilot **Agent** mode.

```bash
code --add-mcp '{"name":"tradingview","type":"http","url":"https://mcp.tradingviewapi.com/mcp"}'
```

Workspace file `.vscode/mcp.json` uses `servers`, not `mcpServers`:

```json
{
  "servers": {
    "tradingview": {
      "type": "http",
      "url": "https://mcp.tradingviewapi.com/mcp"
    }
  }
}
```

## Claude Code

```bash
claude mcp add --transport http tradingview https://mcp.tradingviewapi.com/mcp
```

In the session run `/mcp` and finish the browser login.

## Claude Desktop / claude.ai

1. Open https://claude.ai/settings/connectors
2. Customize → Connectors → Add custom connector
3. Paste `https://mcp.tradingviewapi.com/mcp` and sign in with Console

macOS config (same JSON as Cursor): `~/Library/Application Support/Claude/claude_desktop_config.json`

## Codex

```bash
codex mcp add tradingview --url https://mcp.tradingviewapi.com/mcp
codex mcp login tradingview
```

The second command opens Console in the browser.

## Gemini CLI

```bash
gemini mcp add --transport http tradingview https://mcp.tradingviewapi.com/mcp
```

If Gemini asks to authenticate: `/mcp auth tradingview`

## Windsurf

Edit `~/.codeium/windsurf/mcp_config.json`. The remote field is `serverUrl`, not `url`:

```json
{
  "mcpServers": {
    "tradingview": {
      "serverUrl": "https://mcp.tradingviewapi.com/mcp"
    }
  }
}
```

Older clients may use `"type": "streamable-http"` instead of `"http"`. The URL is the same.

## JWT fallback (no OAuth)

Mint a token, then paste `exampleConfig` into the client:

```bash
curl --request POST \
  --url 'https://api.tradingviewapi.com/api/mcp/generate' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_KEY' \
  --data '{}'
```

RapidAPI: `POST https://tradingview-data1.p.rapidapi.com/api/mcp/generate` with `x-rapidapi-host` / `x-rapidapi-key`.
