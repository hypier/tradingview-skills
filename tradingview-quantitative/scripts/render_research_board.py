#!/usr/bin/env python3
"""Render a tradingview-quantitative research board to a single HTML file."""

from __future__ import annotations

import argparse
import html
import json
import math
import sys
from pathlib import Path
from typing import Any

KINDS = {"equity", "event", "screening", "portfolio", "market"}
TONES = {"success", "danger", "warning", "info", "neutral"}
BLOCK_TYPES = {"h2", "h3", "text", "kpis", "chart", "table", "cards", "callout", "matrix"}
CHART_TYPES = {"line", "bar", "hbar"}
TONE_COLOR = {
    "info": "#2563eb",
    "danger": "#dc2626",
    "success": "#059669",
    "warning": "#d97706",
    "neutral": "#64748b",
}
SERIES_FALLBACK = ["#2563eb", "#0f766e", "#b45309", "#7c3aed", "#be123c"]
CSS = """
:root {
  --bg: #f8fafc;
  --surface: #ffffff;
  --text: #0f172a;
  --muted: #475569;
  --faint: #64748b;
  --line: #e2e8f0;
  --fill: #f1f5f9;
  --accent: #2563eb;
  --danger: #dc2626;
  --success: #059669;
  --warning: #d97706;
  --info: #2563eb;
  font-family: "IBM Plex Sans", "Noto Sans SC", "PingFang SC", sans-serif;
}
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0f172a;
    --surface: #1e293b;
    --text: #f1f5f9;
    --muted: #cbd5e1;
    --faint: #94a3b8;
    --line: #334155;
    --fill: #334155;
  }
}
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: var(--bg); color: var(--text); }
body { line-height: 1.5; }
.board { max-width: 960px; margin: 0 auto; padding: 32px 20px 64px; }
h1 { font-size: 24px; font-weight: 650; margin: 0 0 8px; }
h2 { font-size: 18px; font-weight: 650; margin: 28px 0 10px; }
h3 { font-size: 15px; font-weight: 650; margin: 20px 0 8px; }
p { margin: 0 0 12px; }
.muted { color: var(--muted); font-size: 13px; }
.faint { color: var(--faint); font-size: 12px; }
.pills { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 12px; }
.pill {
  display: inline-block; padding: 2px 8px; border: 1px solid var(--line);
  border-radius: 999px; font-size: 12px; color: var(--muted);
}
.pill.active { background: var(--fill); color: var(--text); border-color: var(--text); }
.kpis { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 16px 0; }
.kpi { padding: 0; }
.kpi .value { font-size: 22px; font-weight: 650; display: block; }
.kpi .label { font-size: 12px; color: var(--muted); }
.callout, .card, .meta, table.framed {
  border: 1px solid var(--line); background: var(--surface); border-radius: 8px;
}
.callout { padding: 12px 14px; margin: 12px 0 16px; }
.callout .title { font-weight: 650; margin-bottom: 4px; }
.callout.warning { border-color: var(--warning); }
.callout.danger { border-color: var(--danger); }
.callout.success { border-color: var(--success); }
.callout.info { border-color: var(--info); }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 12px 0; }
.card { padding: 0; overflow: hidden; }
.card-h { display: flex; justify-content: space-between; gap: 8px; padding: 8px 12px; border-bottom: 1px solid var(--line); font-size: 12px; }
.card-b { padding: 12px; font-size: 14px; }
.chart { margin: 8px 0 4px; }
.chart svg { width: 100%; height: auto; display: block; }
.caption { color: var(--faint); font-size: 12px; margin: 0 0 16px; }
table { width: 100%; border-collapse: collapse; font-size: 13px; margin: 8px 0 4px; }
th, td { text-align: left; padding: 8px 10px; border-bottom: 1px solid var(--line); vertical-align: top; }
th { color: var(--muted); font-weight: 600; }
td.right, th.right { text-align: right; }
td.center, th.center { text-align: center; }
.dot { display: inline-block; width: 7px; height: 7px; border-radius: 50%; margin-right: 6px; background: var(--faint); }
.dot.success { background: var(--success); }
.dot.danger { background: var(--danger); }
.dot.warning { background: var(--warning); }
.dot.info { background: var(--info); }
.tone-success { color: var(--success); }
.tone-danger { color: var(--danger); }
.tone-warning { color: var(--warning); }
.tone-info { color: var(--info); }
.invalidation { padding: 12px 14px; margin: 12px 0; }
.invalidation li { margin: 0 0 8px; }
details.meta { padding: 10px 14px; margin-top: 20px; }
details.meta summary { cursor: pointer; font-size: 13px; color: var(--muted); }
.matrix td { text-align: center; }
@media (max-width: 800px) {
  .kpis, .cards { grid-template-columns: 1fr 1fr; }
}
@media (max-width: 560px) {
  .kpis, .cards { grid-template-columns: 1fr; }
}
"""


class BoardError(ValueError):
    pass


def esc(value: Any) -> str:
    return html.escape("" if value is None else str(value), quote=True)


def tone_class(tone: Any) -> str:
    if tone in TONES and tone != "neutral":
        return f" tone-{tone}"
    return ""


def require(obj: dict[str, Any], key: str, ctx: str) -> Any:
    if key not in obj:
        raise BoardError(f"{ctx} missing '{key}'")
    return obj[key]


def as_dict(value: Any, ctx: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise BoardError(f"{ctx} must be an object")
    return value


def as_list(value: Any, ctx: str) -> list[Any]:
    if not isinstance(value, list):
        raise BoardError(f"{ctx} must be an array")
    return value


def validate(board: dict[str, Any]) -> None:
    if board.get("version") != 1:
        raise BoardError("version must be 1")
    kind = require(board, "kind", "board")
    if kind not in KINDS:
        raise BoardError(f"kind must be one of {sorted(KINDS)}")
    for key in ("language", "title"):
        require(board, key, "board")
    thesis = as_dict(require(board, "thesis", "board"), "thesis")
    require(thesis, "body", "thesis")
    meta = as_dict(require(board, "meta", "board"), "meta")
    for key in ("timestamp", "session", "symbols", "window", "limitations", "assumptions"):
        require(meta, key, "meta")
    blocks = as_list(require(board, "blocks", "board"), "blocks")
    if not blocks:
        raise BoardError("blocks must not be empty")
    for i, block in enumerate(blocks):
        block = as_dict(block, f"blocks[{i}]")
        btype = require(block, "type", f"blocks[{i}]")
        if btype not in BLOCK_TYPES:
            raise BoardError(f"blocks[{i}].type {btype!r} is not supported")


def nice_ticks(lo: float, hi: float, count: int = 5) -> list[float]:
    if not math.isfinite(lo) or not math.isfinite(hi) or lo == hi:
        mid = lo if math.isfinite(lo) else 0.0
        return [mid - 1, mid, mid + 1]
    span = hi - lo
    raw = span / max(count - 1, 1)
    mag = 10 ** math.floor(math.log10(raw))
    for step in (1.0, 2.0, 2.5, 5.0, 10.0):
        nice = step * mag
        if nice >= raw * 0.8:
            start = math.floor(lo / nice) * nice
            ticks = []
            v = start
            while v <= hi + nice * 0.01 and len(ticks) < 8:
                ticks.append(v)
                v += nice
            return ticks or [lo, hi]
    return [lo, hi]


def finite_values(data: list[Any]) -> list[float]:
    out: list[float] = []
    for item in data:
        if item is None:
            continue
        try:
            num = float(item)
        except (TypeError, ValueError):
            continue
        if math.isfinite(num):
            out.append(num)
    return out


def chart_domain(chart: dict[str, Any]) -> tuple[float, float]:
    nums: list[float] = []
    for series in chart.get("series") or []:
        nums.extend(finite_values(series.get("data") or []))
    for line in chart.get("referenceLines") or []:
        try:
            nums.append(float(line["value"]))
        except (KeyError, TypeError, ValueError):
            continue
    if not nums:
        raise BoardError(f"chart {chart.get('title')!r} has no numeric values")
    lo, hi = min(nums), max(nums)
    if chart.get("yMin") is not None:
        lo = float(chart["yMin"])
    if chart.get("yMax") is not None:
        hi = float(chart["yMax"])
    if chart.get("beginAtZero", chart.get("type") != "line"):
        lo = min(0.0, lo)
        hi = max(0.0, hi)
    if lo == hi:
        pad = abs(lo) * 0.05 or 1.0
        lo, hi = lo - pad, hi + pad
    return lo, hi


def svg_line(chart: dict[str, Any]) -> str:
    cats = as_list(chart.get("categories") or [], "chart.categories")
    series = as_list(chart.get("series") or [], "chart.series")
    width, height = 720, 280
    l, r, t, b = 52, 16, 16, 36
    pw, ph = width - l - r, height - t - b
    lo, hi = chart_domain(chart)
    n = max(len(cats), max((len(s.get("data") or []) for s in series), default=1), 1)

    def x_at(i: int) -> float:
        if n == 1:
            return l + pw / 2
        return l + pw * i / (n - 1)

    def y_at(v: float) -> float:
        return t + ph * (1 - (v - lo) / (hi - lo))

    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(chart.get("title") or "chart")}">']
    for tick in nice_ticks(lo, hi):
        y = y_at(tick)
        parts.append(
            f'<line x1="{l}" y1="{y:.1f}" x2="{width - r}" y2="{y:.1f}" stroke="var(--line)" />'
            f'<text x="{l - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="10" fill="var(--faint)">{esc(fmt_num(tick, chart))}</text>'
        )
    step = 1 if n <= 12 else max(1, math.ceil(n / 8))
    for i, cat in enumerate(cats):
        if i % step and i != n - 1:
            continue
        parts.append(
            f'<text x="{x_at(i):.1f}" y="{height - 8}" text-anchor="middle" font-size="10" fill="var(--faint)">{esc(cat)}</text>'
        )
    for line in chart.get("referenceLines") or []:
        try:
            value = float(line["value"])
        except (KeyError, TypeError, ValueError):
            continue
        y = y_at(value)
        color = TONE_COLOR.get(line.get("tone"), TONE_COLOR["neutral"])
        parts.append(
            f'<line x1="{l}" y1="{y:.1f}" x2="{width - r}" y2="{y:.1f}" stroke="{color}" stroke-dasharray="4 3" />'
        )
        if line.get("label"):
            parts.append(
                f'<text x="{width - r}" y="{y - 4:.1f}" text-anchor="end" font-size="10" fill="{color}">{esc(line["label"])}</text>'
            )
    legend_x = l
    for si, series_item in enumerate(series):
        color = TONE_COLOR.get(series_item.get("tone")) or SERIES_FALLBACK[si % len(SERIES_FALLBACK)]
        data = series_item.get("data") or []
        pts: list[str] = []
        for i, raw in enumerate(data):
            try:
                val = float(raw)
            except (TypeError, ValueError):
                continue
            if not math.isfinite(val):
                continue
            pts.append(f"{x_at(i):.1f},{y_at(val):.1f}")
        if pts:
            parts.append(
                f'<polyline fill="none" stroke="{color}" stroke-width="2" points="{" ".join(pts)}" />'
            )
        name = series_item.get("name")
        if name:
            parts.append(
                f'<rect x="{legend_x}" y="2" width="8" height="8" fill="{color}" />'
                f'<text x="{legend_x + 12}" y="10" font-size="11" fill="var(--muted)">{esc(name)}</text>'
            )
            legend_x += 12 + min(len(str(name)) * 7, 160) + 16
    parts.append("</svg>")
    return "".join(parts)


def svg_bars(chart: dict[str, Any], horizontal: bool) -> str:
    cats = as_list(chart.get("categories") or [], "chart.categories")
    series = as_list(chart.get("series") or [], "chart.series")
    n = len(cats)
    if n == 0:
        raise BoardError(f"chart {chart.get('title')!r} has no categories")
    lo, hi = chart_domain({**chart, "beginAtZero": chart.get("beginAtZero", True)})
    width = 720
    height = max(220, 28 * n + 48) if horizontal else 240
    l = 120 if horizontal else 48
    r, t, b = 24, 20, 36
    pw, ph = width - l - r, height - t - b
    parts = [f'<svg viewBox="0 0 {width} {height}" role="img" aria-label="{esc(chart.get("title") or "chart")}">']
    s_count = max(len(series), 1)
    if horizontal:
        for i, cat in enumerate(cats):
            y = t + ph * (i + 0.15) / n
            bh = ph * 0.7 / n / s_count
            parts.append(
                f'<text x="{l - 8}" y="{y + (ph / n) * 0.45:.1f}" text-anchor="end" font-size="11" fill="var(--muted)">{esc(cat)}</text>'
            )
            for si, series_item in enumerate(series):
                color = TONE_COLOR.get(series_item.get("tone")) or SERIES_FALLBACK[si % len(SERIES_FALLBACK)]
                data = series_item.get("data") or []
                try:
                    val = float(data[i])
                except (IndexError, TypeError, ValueError):
                    continue
                zero = l + pw * (0 - lo) / (hi - lo)
                x = l + pw * (val - lo) / (hi - lo)
                x0, x1 = sorted((zero, x))
                yy = y + si * bh * 1.1
                parts.append(
                    f'<rect x="{x0:.1f}" y="{yy:.1f}" width="{max(x1 - x0, 0.5):.1f}" height="{bh:.1f}" fill="{color}" />'
                )
    else:
        for tick in nice_ticks(lo, hi):
            y = t + ph * (1 - (tick - lo) / (hi - lo))
            parts.append(
                f'<line x1="{l}" y1="{y:.1f}" x2="{width - r}" y2="{y:.1f}" stroke="var(--line)" />'
                f'<text x="{l - 6}" y="{y + 4:.1f}" text-anchor="end" font-size="10" fill="var(--faint)">{esc(fmt_num(tick, chart))}</text>'
            )
        group_w = pw / n
        bar_w = group_w * 0.7 / s_count
        for i, cat in enumerate(cats):
            parts.append(
                f'<text x="{l + group_w * (i + 0.5):.1f}" y="{height - 8}" text-anchor="middle" font-size="10" fill="var(--faint)">{esc(cat)}</text>'
            )
            for si, series_item in enumerate(series):
                color = TONE_COLOR.get(series_item.get("tone")) or SERIES_FALLBACK[si % len(SERIES_FALLBACK)]
                data = series_item.get("data") or []
                try:
                    val = float(data[i])
                except (IndexError, TypeError, ValueError):
                    continue
                zero = t + ph * (1 - (0 - lo) / (hi - lo))
                y = t + ph * (1 - (val - lo) / (hi - lo))
                y0, y1 = sorted((zero, y))
                x = l + group_w * i + group_w * 0.15 + si * bar_w
                parts.append(
                    f'<rect x="{x:.1f}" y="{y0:.1f}" width="{bar_w:.1f}" height="{max(y1 - y0, 0.5):.1f}" fill="{color}" />'
                )
    legend_x = l
    for si, series_item in enumerate(series):
        name = series_item.get("name")
        if not name:
            continue
        color = TONE_COLOR.get(series_item.get("tone")) or SERIES_FALLBACK[si % len(SERIES_FALLBACK)]
        parts.append(
            f'<rect x="{legend_x}" y="4" width="8" height="8" fill="{color}" />'
            f'<text x="{legend_x + 12}" y="12" font-size="11" fill="var(--muted)">{esc(name)}</text>'
        )
        legend_x += 28 + min(len(str(name)) * 7, 160)
    parts.append("</svg>")
    return "".join(parts)


def fmt_num(value: float, chart: dict[str, Any]) -> str:
    prefix = chart.get("valuePrefix") or ""
    suffix = chart.get("valueSuffix") or ""
    if abs(value) >= 100 or abs(value - round(value)) < 0.05:
        body = f"{value:.0f}"
    elif abs(value) >= 10:
        body = f"{value:.1f}"
    else:
        body = f"{value:.2f}"
    return f"{prefix}{body}{suffix}"


def render_chart(chart: dict[str, Any]) -> str:
    chart = as_dict(chart, "chart")
    ctype = require(chart, "type", "chart")
    if ctype not in CHART_TYPES:
        raise BoardError(f"chart.type {ctype!r} is not supported")
    title = chart.get("title")
    caption = chart.get("caption")
    if ctype == "line":
        svg = svg_line(chart)
    else:
        svg = svg_bars(chart, horizontal=ctype == "hbar")
    bits = ['<figure class="chart">']
    if title:
        bits.append(f"<h3>{esc(title)}</h3>")
    bits.append(svg)
    if caption:
        bits.append(f'<figcaption class="caption">{esc(caption)}</figcaption>')
    bits.append("</figure>")
    return "".join(bits)


def render_kpis(items: list[Any]) -> str:
    items = [as_dict(item, "kpi") for item in items if item]
    if not items:
        return ""
    cols = min(len(items), 4)
    bits = [f'<div class="kpis" style="grid-template-columns:repeat({cols},minmax(0,1fr))">']
    for item in items:
        bits.append(
            f'<div class="kpi"><span class="value{tone_class(item.get("tone"))}">{esc(item.get("value"))}</span>'
            f'<span class="label">{esc(item.get("label"))}</span></div>'
        )
    bits.append("</div>")
    return "".join(bits)


def render_table(block: dict[str, Any]) -> str:
    headers = as_list(block.get("headers") or [], "table.headers")
    rows = as_list(block.get("rows") or [], "table.rows")
    if not headers or not rows:
        return ""
    align = block.get("columnAlign") or []
    tones = block.get("rowTone") or []
    bits = ['<table class="framed"><thead><tr>']
    for i, header in enumerate(headers):
        cls = align[i] if i < len(align) and align[i] in {"left", "center", "right"} else "left"
        bits.append(f'<th class="{cls}">{esc(header)}</th>')
    bits.append("</tr></thead><tbody>")
    for ri, row in enumerate(rows):
        row = as_list(row, f"table.rows[{ri}]")
        tone = tones[ri] if ri < len(tones) else None
        bits.append("<tr>")
        for i, cell in enumerate(row):
            cls = align[i] if i < len(align) and align[i] in {"left", "center", "right"} else "left"
            prefix = f'<span class="dot {esc(tone)}"></span>' if i == 0 and tone in TONES else ""
            bits.append(f'<td class="{cls}">{prefix}{esc(cell)}</td>')
        bits.append("</tr>")
    bits.append("</tbody></table>")
    if block.get("caption"):
        bits.append(f'<p class="caption">{esc(block["caption"])}</p>')
    return "".join(bits)


def mix_hex(hex_color: str, t: float) -> str:
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    r = round(r + (255 - r) * (1 - t))
    g = round(g + (255 - g) * (1 - t))
    b = round(b + (255 - b) * (1 - t))
    return f"#{r:02x}{g:02x}{b:02x}"


def render_matrix(block: dict[str, Any]) -> str:
    headers = as_list(block.get("headers") or [], "matrix.headers")
    rows = as_list(block.get("rows") or [], "matrix.rows")
    if not headers or not rows:
        return ""
    lo = float(block.get("min", -1))
    hi = float(block.get("max", 1))
    bits = ['<table class="framed matrix"><thead><tr>']
    for header in headers:
        bits.append(f"<th>{esc(header)}</th>")
    bits.append("</tr></thead><tbody>")
    for ri, row in enumerate(rows):
        row = as_list(row, f"matrix.rows[{ri}]")
        bits.append("<tr>")
        for cell in row:
            if isinstance(cell, dict):
                text = cell.get("text", "")
                value = cell.get("value")
            else:
                text, value = cell, None
            style = ""
            if value is not None:
                try:
                    num = float(value)
                    intensity = abs(num) / max(abs(lo), abs(hi), 1e-9)
                    hex_c = "059669" if num >= 0 else "dc2626"
                    color = mix_hex(hex_c, min(1.0, 0.25 + 0.75 * intensity))
                    style = f' style="background:{color}"'
                except (TypeError, ValueError):
                    pass
            bits.append(f"<td{style}>{esc(text)}</td>")
        bits.append("</tr>")
    bits.append("</tbody></table>")
    if block.get("caption"):
        bits.append(f'<p class="caption">{esc(block["caption"])}</p>')
    return "".join(bits)


def render_cards(items: list[Any]) -> str:
    items = [as_dict(item, "card") for item in items if item]
    if not items:
        return ""
    cols = 3 if len(items) == 3 else 2
    bits = [f'<div class="cards" style="grid-template-columns:repeat({cols},minmax(0,1fr))">']
    for item in items:
        badge = item.get("badge")
        badge_html = f'<span class="pill{" active" if item.get("active") else ""}">{esc(badge)}</span>' if badge else ""
        bits.append(
            f'<section class="card"><div class="card-h"><span>{esc(item.get("title"))}</span>{badge_html}</div>'
            f'<div class="card-b">{esc(item.get("body"))}</div></section>'
        )
    bits.append("</div>")
    return "".join(bits)


def render_callout(block: dict[str, Any]) -> str:
    tone = block.get("tone") if block.get("tone") in TONES else "neutral"
    title = f'<div class="title">{esc(block["title"])}</div>' if block.get("title") else ""
    return f'<aside class="callout {esc(tone)}">{title}<div>{esc(block.get("body"))}</div></aside>'


def render_block(block: dict[str, Any]) -> str:
    btype = block["type"]
    if btype == "h2":
        return f"<h2>{esc(block.get('text'))}</h2>"
    if btype == "h3":
        return f"<h3>{esc(block.get('text'))}</h3>"
    if btype == "text":
        return f"<p>{esc(block.get('text'))}</p>"
    if btype == "kpis":
        return render_kpis(as_list(block.get("items") or [], "kpis.items"))
    if btype == "chart":
        return render_chart(block.get("chart"))
    if btype == "table":
        return render_table(block)
    if btype == "cards":
        return render_cards(as_list(block.get("items") or [], "cards.items"))
    if btype == "callout":
        return render_callout(block)
    if btype == "matrix":
        return render_matrix(block)
    return ""


def render_board(board: dict[str, Any]) -> str:
    validate(board)
    pills = "".join(
        f'<span class="pill{" active" if i == 0 else ""}">{esc(p)}</span>'
        for i, p in enumerate(board.get("pills") or [])
    )
    thesis = board["thesis"]
    kpis = render_kpis(board.get("kpis") or [])
    body = "".join(render_block(as_dict(block, "block")) for block in board["blocks"])
    inv = board.get("invalidation") or {}
    inv_html = ""
    if inv.get("items"):
        items = "".join(f"<li>{esc(item)}</li>" for item in inv["items"])
        inv_html = (
            f'<section class="invalidation card"><div class="card-h">{esc(inv.get("title") or "Invalidation")}</div>'
            f'<div class="card-b"><ul>{items}</ul></div></section>'
        )
    conf = board.get("confidence")
    conf_html = render_callout(conf) if conf and conf.get("body") else ""
    meta = board["meta"]
    meta_title = "研究元数据" if str(board.get("language", "")).startswith("zh") else "Research metadata"
    meta_html = f"""<details class="meta" open>
<summary>{esc(meta_title)}</summary>
<p class="muted">Analysis timestamp: {esc(meta['timestamp'])}</p>
<p class="muted">Market/session: {esc(meta['session'])}</p>
<p class="muted">Symbols and universe: {esc(meta['symbols'])}</p>
<p class="muted">Historical window: {esc(meta['window'])}</p>
<p class="muted">Data limitations: {esc(meta['limitations'])}</p>
<p class="muted">Key assumptions: {esc(meta['assumptions'])}</p>
</details>"""
    question = f'<p class="muted">{esc(board["question"])}</p>' if board.get("question") else ""
    disclaimer = f'<p class="faint">{esc(board["disclaimer"])}</p>' if board.get("disclaimer") else ""
    return f"""<!DOCTYPE html>
<html lang="{esc(board.get("language") or "en")}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(board["title"])}</title>
<style>{CSS}</style>
</head>
<body>
<article class="board">
  <header>
    <h1>{esc(board["title"])}</h1>
    <div class="pills">{pills}</div>
    {question}
    {disclaimer}
  </header>
  {render_callout(thesis)}
  {kpis}
  {body}
  {inv_html}
  {conf_html}
  {meta_html}
</article>
</body>
</html>
"""


def write_board(src: Path, dest: Path) -> None:
    board = json.loads(src.read_text(encoding="utf-8"))
    if not isinstance(board, dict):
        raise BoardError("JSON root must be an object")
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(render_board(board), encoding="utf-8")


def self_test(fixture_dir: Path) -> int:
    import tempfile

    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        for path in sorted(fixture_dir.glob("*.json")):
            out = tmp_path / path.with_suffix(".html").name
            try:
                write_board(path, out)
                html_text = out.read_text(encoding="utf-8")
                board = json.loads(path.read_text(encoding="utf-8"))
                if board["title"] not in html_text:
                    raise BoardError("rendered HTML missing title")
                if "<svg" not in html_text:
                    raise BoardError("rendered HTML missing charts")
                print(f"ok  {path.name} ({out.stat().st_size} bytes)")
            except Exception as exc:  # noqa: BLE001 - report every fixture
                failures += 1
                print(f"fail {path.name}: {exc}", file=sys.stderr)
    return 1 if failures else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("json_path", nargs="?", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    here = Path(__file__).resolve().parent
    if args.self_test:
        return self_test(here / "fixtures")
    if not args.json_path:
        parser.error("json_path is required unless --self-test")
    dest = args.output or args.json_path.with_suffix(".html")
    try:
        write_board(args.json_path, dest)
    except (OSError, json.JSONDecodeError, BoardError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(dest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
