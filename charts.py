"""Small HTML/CSS chart components for the visual project pages.

Charts are plain HTML (bars, columns, waterfalls) or HTML + a stretched SVG polyline (lines),
so text never shrinks on phones. Every mark carries a `data-tip` for the hover/tap tooltip, and
every chart ships a "View data" table. Palette validated for colour-blind separation:
C1 blue, C2 copper, C3 teal; single-series charts use C1 with C2 as the highlight.
"""
import html

C1, C2, C3 = "#2f5597", "#b4541a", "#00927f"
TOTAL = "#172340"   # navy, for totals and subtotals
SOFT = "#c3ccda"    # de-emphasised bars


def esc(s) -> str:
    return html.escape(str(s))


def fmt(v, f="{:,}", pre="", suf="") -> str:
    s = f.format(abs(v)) if v < 0 else f.format(v)
    return f"{'−' if v < 0 else ''}{pre}{s}{suf}"


def data_table(headers, rows) -> str:
    th = "".join(f"<th>{esc(h)}</th>" for h in headers)
    trs = "".join("<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>" for r in rows)
    return (f'<details class="dt"><summary>View data</summary>'
            f'<table><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></details>')


def legend(series) -> str:
    items = "".join(f'<span><i style="background:{c}"></i>{esc(n)}</span>' for n, c in series)
    return f'<div class="legend">{items}</div>'


def hbars(rows, f="{:,}", pre="", suf="", max_value=None, highlight=(), ref=None, ref_label=""):
    """Horizontal bars. rows = [(label, value)]. highlight = labels drawn in copper."""
    mx = max_value or max(v for _, v in rows) * 1.08
    out = ['<div class="hb">']
    for label, v in rows:
        col = C2 if label in highlight else C1
        val = fmt(v, f, pre, suf)
        out.append(
            f'<div class="hb-row"><span class="hb-l">{esc(label)}</span>'
            f'<span class="hb-t"><i style="width:{v / mx * 100:.2f}%;background:{col}" '
            f'data-tip="{esc(label)}: {esc(val)}" tabindex="0"></i></span>'
            f'<span class="hb-v">{esc(val)}</span></div>')
    if ref is not None:
        out.append(f'<div class="hb-ref" style="--x:{ref / mx * 100:.2f}%"><span>{esc(ref_label)}</span></div>')
    out.append("</div>")
    out.append(data_table(["Item", "Value"], [(l, fmt(v, f, pre, suf)) for l, v in rows]))
    return "".join(out)


def dbars(rows, f="{:.1f}", suf="", highlight=()):
    """Diverging horizontal bars around a grey zero line. Positive blue, negative copper."""
    mx = max(abs(v) for _, v in rows) * 1.15 or 1
    out = ['<div class="db">']
    for label, v in rows:
        col = C1 if v >= 0 else C2
        w = abs(v) / mx * 50
        side = f"left:50%;width:{w:.2f}%" if v >= 0 else f"right:50%;width:{w:.2f}%"
        val = ("+" if v > 0 else "") + fmt(v, f, "", suf)
        cls = " hl" if label in highlight else ""
        out.append(
            f'<div class="db-row{cls}"><span class="hb-l">{esc(label)}</span>'
            f'<span class="db-t"><i style="{side};background:{col}" data-tip="{esc(label)}: {esc(val)}" tabindex="0"></i></span>'
            f'<span class="hb-v">{esc(val)}</span></div>')
    out.append("</div>")
    out.append(data_table(["Item", "Change"], [(l, ("+" if v > 0 else "") + fmt(v, f, "", suf)) for l, v in rows]))
    return "".join(out)


def stacked_hbars(rows, names, colors, f="{:,}", pre="", suf="", max_total=100):
    """rows = [(label, [v1, v2, ...])]; bar widths are relative to max_total."""
    out = [legend(list(zip(names, colors))), '<div class="hb">']
    for label, vals in rows:
        segs = "".join(
            f'<i style="width:{v / max_total * 100:.2f}%;background:{c}" data-tip="{esc(label)}, {esc(n)}: {esc(fmt(v, f, pre, suf))}" tabindex="0"></i>'
            for v, n, c in zip(vals, names, colors))
        out.append(f'<div class="hb-row"><span class="hb-l">{esc(label)}</span>'
                   f'<span class="hb-t stack">{segs}</span><span class="hb-v">{esc(fmt(sum(vals), f, pre, suf))}</span></div>')
    out.append("</div>")
    out.append(data_table(["Item"] + list(names) + ["Total"],
                          [[l] + [fmt(v, f, pre, suf) for v in vals] + [fmt(sum(vals), f, pre, suf)] for l, vals in rows]))
    return "".join(out)


def columns(rows, f="{:,}", pre="", suf="", highlight=(), height=220, note=""):
    """Vertical columns. rows = [(label, value)]."""
    mx = max(v for _, v in rows) * 1.12
    cols = []
    for label, v in rows:
        col = C2 if label in highlight else C1
        val = fmt(v, f, pre, suf)
        cols.append(
            f'<div class="col"><span class="cv">{esc(val)}</span>'
            f'<i style="height:{v / mx * 100:.2f}%;background:{col}" data-tip="{esc(label)}: {esc(val)}" tabindex="0"></i></div>')
    labels = "".join(f"<span>{esc(l)}</span>" for l, _ in rows)
    return (f'<div class="sx"><div class="sx-in" style="--n:{len(rows)}"><div class="cols" style="--h:{height}px">{"".join(cols)}</div><div class="cols-x">{labels}</div></div></div>'
            + data_table(["Item", "Value"], [(l, fmt(v, f, pre, suf)) for l, v in rows]))


def waterfall(steps, f="{:.1f}", pre="", suf="", height=240):
    """steps = [(label, delta)] or [(label, None, 'total')] for a running subtotal/total column."""
    run, bars = 0.0, []
    for s in steps:
        label, delta = s[0], s[1]
        if len(s) > 2 and s[2] == "total":
            bars.append((label, 0.0, run, run, "total"))
        else:
            lo, hi = sorted((run, run + delta))
            bars.append((label, lo, hi, delta, "up" if delta >= 0 else "down"))
            run += delta
    top = max(b[2] for b in bars) * 1.15
    cols, table = [], []
    for label, lo, hi, val, kind in bars:
        col = TOTAL if kind == "total" else (C1 if kind == "up" else C2)
        txt = fmt(val, f, pre, suf) if kind == "total" else ("+" if val > 0 else "") + fmt(val, f, pre, suf)
        cols.append(
            f'<div class="wf-c"><i style="bottom:{lo / top * 100:.2f}%;height:{max(hi - lo, top * .004) / top * 100:.2f}%;background:{col}" '
            f'data-tip="{esc(label)}: {esc(txt)}" tabindex="0"><span>{esc(txt)}</span></i></div>')
        table.append((label, txt))
    labels = "".join(f'<span class="{"tot" if b[4] == "total" else ""}">{esc(b[0])}</span>' for b in bars)
    return (f'<div class="sx"><div class="sx-in" style="--n:{len(bars)}"><div class="wf" style="--h:{height}px">{"".join(cols)}</div><div class="cols-x">{labels}</div></div></div>'
            + data_table(["Component", "Value"], table))


def line(series, xticks, xmin, xmax, ymin, ymax, yticks, f="{:,}", suf="", vline=None, height=240):
    """series = [(name, color, [(x, y), ...])]; xticks = [(x, label)]; vline = (x, label)."""
    def px(x): return (x - xmin) / (xmax - xmin) * 100
    def py(y): return (y - ymin) / (ymax - ymin) * 100
    parts = []
    for t in yticks:
        parts.append(f'<div class="gl" style="bottom:{py(t):.2f}%"><span>{esc(fmt(t, f, "", suf))}</span></div>')
    if vline:
        parts.append(f'<div class="vl" style="left:{px(vline[0]):.2f}%"><span>{esc(vline[1])}</span></div>')
    polys = "".join(
        f'<polyline fill="none" stroke="{c}" stroke-width="2" vector-effect="non-scaling-stroke" '
        f'stroke-linejoin="round" points="{" ".join(f"{px(x):.2f},{100 - py(y):.2f}" for x, y in pts)}"/>'
        for _, c, pts in series)
    parts.append(f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">{polys}</svg>')
    xl = dict(xticks)
    for name, c, pts in series:
        for x, y in pts:
            tip = f"{name + ', ' if len(series) > 1 else ''}{xl.get(x, x)}: {fmt(y, f, '', suf)}"
            parts.append(f'<i class="dot" style="left:{px(x):.2f}%;bottom:{py(y):.2f}%;background:{c}" '
                         f'data-tip="{esc(tip)}" tabindex="0"></i>')
    for x, label in xticks:
        parts.append(f'<span class="xl" style="left:{px(x):.2f}%">{esc(label)}</span>')
    head = legend([(n, c) for n, c, _ in series]) if len(series) > 1 else ""
    xs = sorted({x for _, _, pts in series for x, _ in pts})
    rows = [[xl.get(x, x)] + [next((fmt(y, f, "", suf) for px_, y in pts if px_ == x), "") for _, _, pts in series] for x in xs]
    return (head + f'<div class="lc" style="--h:{height}px"><div class="plot">{"".join(parts)}</div></div>'
            + data_table([""] + [n for n, _, _ in series], rows))
