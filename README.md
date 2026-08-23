# TradingView Quantitative Skills

A collection of Agent Skills for TradingView data retrieval, quantitative market analysis, and institutional-style equity research. Each directory is an independent skill package. Select the single package that best matches the task to avoid loading overlapping guidance.

## Included Skills

| Skill | Use it for | Data access |
| --- | --- | --- |
| `equity-research-analyst` | Initiation reports, earnings notes and previews, catalyst calendars, morning notes, sector reports, model updates, and investment idea generation | TradingView Data API first; public primary sources for narrative and filings |
| `tradingview-api-integration` | Integrating with, troubleshooting, or directly querying the TradingView Data API, including quotes, financials, screeners, calendars, metadata, and streaming | Console (`api.tradingviewapi.com`) with `TRADINGVIEW_API_KEY`; RapidAPI remains an alternate |
| `tradingview-quantitative` | Retrieving current data through configured TradingView MCP tools, then performing screening, technical, risk, event, or multi-symbol analysis | TradingView MCP tools |
| `tradingview-openclaw` | Applying reusable TradingView-based analysis workflows and data-interpretation methods in OpenClaw | Uses user-provided or existing data; does not make live API calls |

## Install

Install a single skill from its repository subdirectory. For example, install the quantitative-analysis skill at [`tradingview-quantitative`](https://github.com/hypier/tradingview-skills/tree/main/tradingview-quantitative):

```bash
npx skills add hypier/tradingview-skills/tradingview-quantitative
```

Choose the package that matches the task:

```bash
npx skills add hypier/tradingview-skills/equity-research-analyst
npx skills add hypier/tradingview-skills/tradingview-api-integration
npx skills add hypier/tradingview-skills/tradingview-quantitative
npx skills add hypier/tradingview-skills/tradingview-openclaw
```

Restart the agent session after installation. Invoke a skill explicitly, for example `$tradingview-api-integration`, or describe a matching task in natural language.

### Local Development and Offline Distribution

To install a single local package into a Codex-style skills directory:

```bash
ROOT="$(pwd)"
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills"
cp -R "$ROOT/tradingview-api-integration" "$CODEX_HOME/skills/"
```

To package a local skill for a client that imports `.skill` archives:

```bash
mkdir -p dist
python3 /Users/barry/.agents/skills/skill-creator/scripts/package_skill.py \
  tradingview-api-integration dist
```

Replace `tradingview-api-integration` with the desired directory name in either command.

## Prerequisites

- **API integration and equity research:** Set `TRADINGVIEW_API_KEY` and call `https://api.tradingviewapi.com` with `Authorization: Bearer`. RapidAPI (`RAPIDAPI_KEY`) remains supported as an alternate. `tradingview-api-integration` can save a key to `.api-key` only after explicit consent.
- **Quantitative analysis:** Configure hosted TradingView MCP in the agent runtime: `"type": "http"` and `https://mcp.tradingviewapi.com/mcp`, then sign in with Console. JWT (`POST /api/mcp/generate`) and RapidAPI local OpenAPI MCP are fallbacks. Without MCP tools, use `tradingview-api-integration` for direct API access.
- **OpenClaw frameworks:** Supply market, financial, or news data when current information is required. The skill does not treat templates or historical examples as live market data.
- **Equity research:** Prefer exchange-qualified tickers such as `NASDAQ:AAPL` or `HKEX:9988`. Cite the retrieval date and endpoint for live data used in a report.

## Examples

```text
Use $tradingview-api-integration to retrieve the latest NASDAQ:AAPL quote and 60 daily bars.

Use $tradingview-quantitative to perform a multi-timeframe trend, RSI, and risk assessment for BINANCE:BTCUSDT.

Use $tradingview-openclaw to design a non-live-data analysis framework for high-dividend China A-share screening.

Use $equity-research-analyst to write an earnings-preview report for NYSE:JPM.
```

## Maintain

Validate every package after changes, then rebuild any distribution archives:

```bash
for skill in equity-research-analyst tradingview-api-integration tradingview-openclaw tradingview-quantitative; do
  python3 /Users/barry/.agents/skills/skill-creator/scripts/quick_validate.py "$skill"
done
```

OpenAPI snapshots and API examples are on-demand references. Download a candidate update to a temporary file, review it, and only then replace the bundled snapshot deliberately.
