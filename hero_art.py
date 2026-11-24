"""Animated hero illustrations for the visual project pages (one per project).

Pure SVG strings. Animation classes (.flow, .draw, .pulse, .rise, .fade, .scan) are defined in
templates/visual.html and switched off for prefers-reduced-motion. All numbers are illustrative.
"""
MINT, AMBER, VIOLET = "#5eead4", "#ffb547", "#a5a1ff"
LINE, FAINT, TXT, SUB = "rgba(255,255,255,.14)", "rgba(255,255,255,.06)", "#e6f2ef", "#8a9a96"
MONO = "font-family:'JetBrains Mono',ui-monospace,monospace"


def _svg(body: str, label: str) -> str:
    return (f'<svg class="art" viewBox="0 0 460 360" role="img" aria-label="{label}">'
            f'<defs><radialGradient id="glow" cx="50%" cy="50%" r="50%">'
            f'<stop offset="0" stop-color="{MINT}" stop-opacity=".45"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/>'
            f'</radialGradient><linearGradient id="area" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{MINT}" stop-opacity=".35"/><stop offset="1" stop-color="{MINT}" stop-opacity="0"/>'
            f'</linearGradient></defs>{body}</svg>')


def _node(x, y, w, h, title, sub, delay=0):
    return (f'<g class="fade" style="animation-delay:{delay}s">'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{FAINT}" stroke="{LINE}"/>'
            f'<text x="{x + 14}" y="{y + 21}" fill="{TXT}" font-size="13" style="{MONO};font-weight:600">{title}</text>'
            f'<text x="{x + 14}" y="{y + 38}" fill="{SUB}" font-size="11" style="{MONO}">{sub}</text></g>')


def _tag(x, y, text, color, delay=0):
    w = 9 + len(text) * 7.4
    return (f'<g class="fade" style="animation-delay:{delay}s"><rect x="{x}" y="{y}" width="{w:.0f}" height="22" rx="11" '
            f'fill="#0b0f14" stroke="{color}"/><text x="{x + w / 2:.0f}" y="{y + 15}" text-anchor="middle" fill="{color}" '
            f'font-size="11.5" style="{MONO};font-weight:600">{text}</text></g>')


def sci() -> str:
    paths = ["M150 74 C 240 74, 240 180, 322 180", "M150 184 L 322 180", "M150 294 C 240 294, 240 180, 322 180"]
    body = "".join(f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2"/>'
                   f'<path class="flow" d="{d}" fill="none" stroke="{MINT}" stroke-width="2" style="animation-delay:{i * .4}s"/>'
                   for i, d in enumerate(paths))
    body += _node(20, 50, 130, 48, "EPOS", "what was bought", .1)
    body += _node(20, 160, 130, 48, "PAYMENT", "how it was paid", .25)
    body += _node(20, 270, 130, 48, "LOYALTY", "who bought it", .4)
    body += (f'<circle cx="372" cy="180" r="90" fill="url(#glow)"/>'
             f'<circle class="pulse" cx="372" cy="180" r="50" fill="none" stroke="{MINT}" stroke-width="1.5"/>'
             f'<circle cx="372" cy="180" r="50" fill="#0b0f14" stroke="{MINT}" stroke-width="2"/>'
             f'<text x="372" y="176" text-anchor="middle" fill="{TXT}" font-size="13" style="{MONO};font-weight:700">ID·0001</text>'
             f'<text x="372" y="194" text-anchor="middle" fill="{SUB}" font-size="10.5" style="{MONO}">one customer</text>')
    body += _tag(206, 96, "conf 0.85", MINT, 1.0) + _tag(206, 250, "conf 0.61", AMBER, 1.3)
    return _svg(body, "Three source systems linking into one customer record")


def clv() -> str:
    xs = [40 + i * 76 for i in range(6)]
    def pts(vals): return " ".join(f"{x},{300 - 240 * v:.1f}" for x, v in zip(xs, vals))
    fans = [1, .80, .66, .55, .46, .39]
    body = "".join(f'<line x1="40" x2="420" y1="{y}" y2="{y}" stroke="{FAINT}"/>' for y in (60, 120, 180, 240, 300))
    body += "".join(f'<text x="{x}" y="324" text-anchor="middle" fill="{SUB}" font-size="11" style="{MONO}">'
                    f'{"NOW" if i == 0 else "Y" + str(i)}</text>' for i, x in enumerate(xs))
    body += f'<polygon class="fade" style="animation-delay:1.4s" points="40,300 {pts(fans)} 420,300" fill="url(#area)"/>'
    body += (f'<polyline class="draw" pathLength="1" points="{pts([1, .86, .75, .66, .58, .52])}" fill="none" stroke="{VIOLET}" stroke-width="2" stroke-opacity=".7"/>'
             f'<polyline class="draw" pathLength="1" style="animation-delay:.2s" points="{pts([1, .55, .38, .27, .19, .13])}" fill="none" stroke="{AMBER}" stroke-width="2" stroke-opacity=".8"/>'
             f'<polyline class="draw" pathLength="1" style="animation-delay:.4s" points="{pts(fans)}" fill="none" stroke="{MINT}" stroke-width="3"/>')
    body += "".join(f'<circle class="fade" style="animation-delay:{1 + i * .12:.2f}s" cx="{x}" cy="{300 - 240 * v:.1f}" r="4.5" fill="#0b0f14" stroke="{MINT}" stroke-width="2"/>'
                    for i, (x, v) in enumerate(zip(xs, fans)))
    body += _tag(318, 176, "CLV €954", MINT, 1.8) + _tag(56, 22, "P(still active)", SUB, .2)
    return _svg(body, "Predicted customer survival curves over five years")


def fleet() -> str:
    regions = [("ESA", "litres · cpl", 50), ("ANZ", "litres · cpl", 160), ("US", "gallons · cpg", 270)]
    body = ""
    for i, (r, u, y) in enumerate(regions):
        d = f"M150 {y + 24} C 210 {y + 24}, 220 {130 + i * 50}, 262 {130 + i * 50}"
        body += (f'<path d="{d}" fill="none" stroke="{LINE}" stroke-width="2"/>'
                 f'<path class="flow" style="animation-delay:{i * .3}s" d="{d}" fill="none" stroke="{MINT}" stroke-width="2"/>')
        body += _node(20, y, 130, 48, r, u, .1 + i * .15)
    body += (f'<rect class="fade" style="animation-delay:.6s" x="262" y="80" width="180" height="200" rx="14" fill="#0b0f14" stroke="{MINT}" stroke-width="1.5"/>'
             f'<text x="280" y="108" fill="{MINT}" font-size="11" style="{MONO};font-weight:700;letter-spacing:1px">GLOBAL · 1 VIEW</text>'
             f'<line x1="280" x2="424" y1="120" y2="120" stroke="{LINE}"/>')
    for i, (r, v) in enumerate([("ESA", 2.0), ("ANZ", -2.3), ("US", -6.5)]):
        y = 146 + i * 46
        w = abs(v) * 7
        x = 360 if v >= 0 else 360 - w
        body += (f'<text x="280" y="{y + 4}" fill="{TXT}" font-size="12" style="{MONO}">{r}</text>'
                 f'<line x1="360" x2="360" y1="{y - 12}" y2="{y + 12}" stroke="{SUB}"/>'
                 f'<rect class="rise" style="animation-delay:{1 + i * .15}s" x="{x}" y="{y - 7}" width="{w}" height="14" rx="4" fill="{MINT if v >= 0 else AMBER}"/>'
                 f'<text x="{424}" y="{y + 4}" text-anchor="end" fill="{SUB}" font-size="11" style="{MONO}">{"+" if v > 0 else "−"}{abs(v)}%</text>')
    return _svg(body, "Three regional fleet reports converging into one global view")


def inventory() -> str:
    hot = {(1, 5): 67, (3, 2): 58, (4, 6): 51, (0, 1): 47}
    body = '<g class="scan"><rect x="30" y="40" width="400" height="3" rx="1.5" fill="' + MINT + '" opacity=".55"/></g>'
    for r in range(6):
        for c in range(8):
            x, y = 60 + c * 48, 70 + r * 46
            if (r, c) in hot:
                body += (f'<circle class="pulse" cx="{x}" cy="{y}" r="9" fill="none" stroke="{AMBER}" stroke-width="1.5"/>'
                         f'<circle cx="{x}" cy="{y}" r="7" fill="{AMBER}"/>')
            else:
                body += f'<circle class="fade" style="animation-delay:{(r + c) * .04:.2f}s" cx="{x}" cy="{y}" r="5" fill="rgba(255,255,255,.22)"/>'
    body += _tag(300, 322, "4 outliers · ranked", AMBER, 1.2) + _tag(30, 322, "$ loss / day", SUB, .4)
    return _svg(body, "A grid of stores with four outlier stores highlighted")


def fuel() -> str:
    steps = [("MKT", 7.0), ("BRAND", 10.0), ("PREM", -8.5), ("TERMS", -1.2), ("VOL", 1.3), ("OTH", -0.1), ("STD", None)]
    unit, base, run, body = 13, 300, 0.0, ""
    body += "".join(f'<line x1="24" x2="436" y1="{base - t * unit}" y2="{base - t * unit}" stroke="{FAINT}"/>' for t in (0, 5, 10, 15))
    for i, (lab, d) in enumerate(steps):
        x = 30 + i * 58
        if d is None:
            lo, hi, col, txt = 0, run, "#e6f2ef", f"{run:.1f}"
        else:
            lo, hi = sorted((run, run + d)); col = MINT if d >= 0 else AMBER
            txt = f"{'+' if d > 0 else '−'}{abs(d):.1f}"; run += d
        h = max(hi - lo, .15) * unit
        body += (f'<rect class="rise" style="animation-delay:{.2 + i * .14:.2f}s" x="{x}" y="{base - hi * unit:.1f}" width="40" height="{h:.1f}" rx="4" fill="{col}"/>'
                 f'<text class="fade" style="animation-delay:{.6 + i * .14:.2f}s;{MONO}" x="{x + 20}" y="{base - hi * unit - 8:.1f}" text-anchor="middle" fill="{TXT}" font-size="11">{txt}</text>'
                 f'<text x="{x + 20}" y="{base + 20}" text-anchor="middle" fill="{SUB}" font-size="10" style="{MONO}">{lab}</text>')
    body += _tag(24, 34, "cents per gallon", SUB, .2)
    return _svg(body, "A fuel margin waterfall building up to the standard margin")
