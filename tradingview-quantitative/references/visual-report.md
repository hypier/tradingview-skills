# Visual Research Board

Formal reports write a portable HTML board. Do not treat a Cursor canvas as the deliverable: `.canvas.tsx` only works inside Cursor.

Skip the board for a quote lookup, a missing-MCP failure, or when the user asks for a short prose answer. If `python3` is unavailable or the workspace cannot be written, fall back to `output-templates.md` in chat.

## Workflow

1. Finish the analysis with the mode reference and `analysis-framework.md`.
2. Write JSON that matches the schema below. Use the user's language in every string.
3. Render:

```bash
python3 {skill_dir}/scripts/render_research_board.py {json_path} -o {html_path}
```

`{skill_dir}` is the directory that contains this skill's `SKILL.md`. Default HTML path: `reports/<slug>-research-board.html` in the current workspace, not inside the skill folder.

4. Reply with a short conclusion and the HTML path. Keep observed, derived, interpreted, and actionable statements separate in both the JSON and the chat summary.

## Schema

Top-level object:

| Field | Required | Notes |
| --- | --- | --- |
| `version` | yes | `1` |
| `kind` | yes | `equity`, `event`, `screening`, `portfolio`, `market` |
| `language` | yes | BCP 47, usually `zh` or `en` |
| `title` | yes | Page heading |
| `pills` | no | Short tags such as `NASDAQ:TSLA` |
| `question` | no | Research question and decision |
| `disclaimer` | no | Keep the skill's non-advice scope visible |
| `thesis` | yes | `{title, body, tone}` where tone is `warning`, `info`, `success`, `danger`, or `neutral` |
| `kpis` | no | Up to four `{value, label, tone?}` |
| `blocks` | yes | Ordered body; omit a block if it has no data |
| `invalidation` | no | `{title, items[]}` |
| `confidence` | no | `{title, body, tone?}` |
| `meta` | yes | `{timestamp, session, symbols, window, limitations, assumptions}` |

Never send empty charts, empty tables, or placeholder copy. Escape is the renderer's job; still pass plain text, not HTML.

### Blocks

```text
{ "type": "h2" | "h3", "text": "..." }
{ "type": "text", "text": "..." }
{ "type": "kpis", "items": [{ "value", "label", "tone?" }] }
{ "type": "chart", "chart": { ... } }
{ "type": "table", "headers": [], "rows": [], "columnAlign?": [], "rowTone?": [], "caption?": "" }
{ "type": "cards", "items": [{ "title", "body", "badge?", "active?" }] }
{ "type": "callout", "title?", "body", "tone?" }
{ "type": "matrix", "headers": [], "rows": [[{ "text", "value?" }]], "caption?": "", "min?": -1, "max?": 1 }
```

`rowTone` / KPI / callout / series `tone`: `success`, `danger`, `warning`, `info`, `neutral`.

### Charts

```text
{
  "type": "line" | "bar" | "hbar",
  "title": "...",
  "caption": "...",
  "categories": ["..."],
  "series": [{ "name": "...", "data": [0], "tone?": "info" }],
  "valuePrefix?": "$",
  "valueSuffix?": "%",
  "beginAtZero?": true,
  "yMin?": 0,
  "yMax?": 100,
  "referenceLines?": [{ "value": 0, "label": "...", "tone?": "neutral" }]
}
```

Use `line` for price or relative-return paths, `bar` for EPS / factor scores, `hbar` for weights or ratings. `matrix` is for correlation or heatmaps, not a chart type.

## Mode boards

Fill only the blocks that the evidence supports. Shared tail: invalidation, confidence, meta.

**equity** — thesis; KPI strip (price, post-event return, valuation, next catalyst); price path with reference lines; event or valuation tables; competing-thesis cards; catalysts/risks table.

**event** — thesis; KPI strip (T+1, window return, vol change, sample size); pre/post path versus a benchmark; event facts and abnormal-return table; beneficiaries/losers if the universe has more than one name.

**screening** — hypothesis as thesis; KPI strip (universe, passed, median factor, exclusions); ranked shortlist table; optional factor bar chart; false-positive risks and follow-up.

**portfolio** — thesis; KPI strip (volatility, max drawdown, concentration, largest weight); weight `hbar`; holdings table; correlation `matrix` when there are at least two names; stress and sizing conditions.

**market** — regime as thesis; KPI strip (index return, breadth, leader, next event); relative-performance line; rotation or indicator table; bull/base/bear cards; what would change the regime.

Signal validation, strategy research, execution, and monitoring do not have a separate board. Map them onto the closest kind above, or reuse the same blocks under that kind.

## Renderer fixtures

`scripts/fixtures/` holds regression JSON. `equity-tesla.json` is a real worked example. The other fixtures only prove layout coverage; do not treat them as live market research.