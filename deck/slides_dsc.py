"""Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and look as slides.py.
Imported after build_deck_dsc.py swaps deck.content for deck.content_dsc."""
from . import content as K
from . import slides as S
from . import theme as T
from .helpers import (L, C, R, MID, text, title, rect, card, oval, pic, icon, icon_circle, num_circle, chip,
                      chip_width, arrow_chips, notes)


def _is_placeholder(v):
    return '[' in v


def value_tile(s, x, y, w, h, v, size=13, align=C):
    """Number tile: real value = violet, founder-supplied placeholder = yellow."""
    ph = _is_placeholder(v)
    rect(s, x, y, w, h, fill=T.PALEY if ph else T.LAV2, radius=min(0.12, h / 2))
    text(s, x + (0.1 if align == L else 0), y, w - (0.2 if align == L else 0), h, v, size=size, font=T.TITLE_FONT,
         color=T.AMBER if ph else T.DEEP, align=align, anchor=MID)


def s_overview(s):
    c = K.SLIDE_OVERVIEW
    chip(s, c['tag'], 0.6, 0.45, bg=T.MINT, fg=T.GREEN, size=8.5, h=0.3, ic=('check', 'green'))
    title(s, c['title'], 0.6, 0.88, 4.0, 0.85, size=21)
    for i, (ic, head, body) in enumerate(c['blocks']):
        y = 1.95 + i * 1.02
        icon_circle(s, ic, 0.6, y, 0.44)
        text(s, 1.18, y - 0.02, 3.0, 0.26, head, size=11.5, font=T.TITLE_FONT)
        text(s, 1.18, y + 0.26, 3.1, 0.7, body, size=9, color=T.BODY, spacing=1.1)
    for i, (img, lbl) in enumerate(c['phones']):
        x = 4.4 + i * 1.74
        pic(s, img, x, 0.75, h=3.4, alt=lbl)
        text(s, x, 4.18, 1.73, 0.24, lbl, size=8.5, font=T.LABEL_FONT, color=T.BODY, align=C)
    notes(s, c['notes'])


def s_solution(s):
    c = K.SLIDE_4_SOLUTION
    S.s4_solution(s)
    rect(s, 0.6, 4.72, 8.8, 0.52, fill=T.WHITE, line=T.BORDER, radius=0.14, lw=0.75)
    icon(s, 'wand-sparkles', 'purple', 0.78, 4.84, 0.28)
    text(s, 1.16, 4.72, 4.3, 0.52, c['usp'], size=10, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
    x = 9.28
    for lbl, ic in reversed(c['trio']):
        w = chip_width(lbl, 8.5, 0.32, True)
        x -= w
        chip(s, lbl, x, 4.82, bg=T.LAV2, fg=T.DEEP, size=8.5, h=0.32, w=w, ic=(ic, 'purple'))
        x -= 0.1


def s_market(s):
    c = K.SLIDE_MARKET
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=26)
    # left: target customers
    for i, (ic, seg, desc) in enumerate(c['personas']):
        y = 1.35 + i * 0.82
        card(s, 0.6, y, 3.65, 0.7, radius=0.14)
        icon_circle(s, ic, 0.76, y + 0.14, 0.42)
        text(s, 1.3, y + 0.08, 3.1, 0.26, seg, size=11, font=T.TITLE_FONT)
        text(s, 1.3, y + 0.33, 2.85, 0.34, desc, size=8.5, color=T.BODY, spacing=1.05)
    text(s, 0.6, 3.86, 3.65, 0.5, c['why'], size=9.5, font=T.LABEL_FONT, color=T.DEEP, spacing=1.1)
    # right: TAM / SAM / SOM rings + figures
    base, cx = 4.95, 6.05
    rings = [(3.3, T.LAV2, T.DEEP), (2.2, T.LAV3, T.DEEP), (1.15, T.PURPLE, T.WHITE)]
    offs = [0.26, 0.2, 0.28]
    for (d, fill, fg), (lbl, *_x), dy in zip(rings, c['layers'], offs):
        oval(s, cx - d / 2, base - d, d, fill=fill)
        text(s, cx - 0.5, base - d + dy, 1.0, 0.3, lbl, size=11, font=T.TITLE_FONT, color=fg, align=C, anchor=MID)
    for i, (lbl, geo, value, unit) in enumerate(c['layers']):
        y = 1.42 + i * 1.1
        text(s, 7.85, y, 1.6, 0.22, f'{lbl} · {geo}', size=8, font=T.LABEL_FONT, color=T.PURPLE, spacing=1.0)
        text(s, 7.85, y + 0.36, 1.6, 0.38, value, size=20, font=T.TITLE_FONT, color=T.INK)
        text(s, 7.85, y + 0.72, 1.6, 0.36, unit, size=7.5, color=T.BODY, spacing=1.0)
    text(s, 0.6, 5.2, 8.8, 0.22, c['source'], size=6.5, color=T.BODY)
    notes(s, c['notes'])


def s_traction(s):
    c = K.SLIDE_TRACTION
    title(s, c['title'], 0.6, 0.45, c.get('title_w', 6.0), 0.7, size=c.get('title_size', 26))
    if c.get('stage'):
        chip(s, c['stage'], 0.6, 1.2, bg=T.LAV2, fg=T.DEEP, size=9, h=0.32, ic=('check', 'purple'))
    step = min(1.5, 4.5 / len(c['metrics']))
    for i, (v, lbl) in enumerate(c['metrics']):
        x, w = 0.6 + i * step, step - 0.12
        card(s, x, 1.75, w, 1.3, radius=0.14)
        text(s, x, 1.85, w, 0.6, v, size=30, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
        text(s, x + 0.1, 2.48, w - 0.2, 0.5, lbl, size=8.5, font=T.LABEL_FONT, align=C, spacing=1.0)
    arrow_chips(s, c['loop'], 0.6, 3.35, h=0.34, size=9.5, gap=0.24)
    text(s, 0.6, 3.95, 4.4, 0.5, c['proof'], size=9.5, color=T.BODY, spacing=1.1)
    card(s, 5.3, 1.2, 4.1, 3.85, radius=0.18)
    text(s, 5.52, 1.38, 3.7, 0.5, c['feedback_title'], size=12, font=T.TITLE_FONT, spacing=1.0)
    for i, (st, f) in enumerate(c['feedback']):
        y = 2.1 + i * 0.56
        done = st == 'shipped'
        chip(s, c['status_label'][st], 5.52, y, bg=T.MINT if done else T.LAV2, fg=T.GREEN if done else T.DEEP,
             size=8, h=0.28, w=0.95)
        text(s, 6.6, y - 0.04, 2.65, 0.36, f, size=10, anchor=MID)
    notes(s, c['notes'])


def s_gtm(s):
    c = K.SLIDE_GTM
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=26)
    for i, (tag, aud, steps, channels) in enumerate(c['tracks']):
        y = 1.3 + i * 1.3
        card(s, 0.6, y, 8.8, 1.15, radius=0.16)
        chip(s, tag, 0.8, y + 0.16, bg=T.PURPLE if i else T.LAV2, fg=T.WHITE if i else T.DEEP, size=9, h=0.3, w=0.62)
        text(s, 1.55, y + 0.14, 3.0, 0.34, aud, size=13, font=T.TITLE_FONT, anchor=MID)
        arrow_chips(s, steps, 0.8, y + 0.58, h=0.3, size=8.5, gap=0.22, bg=T.LAV if i == 0 else T.LAV2)
        text(s, 5.3 if i == 0 else 6.2, y + 0.14, 3.95 if i == 0 else 3.05, 0.34, channels, size=8,
             color=T.BODY, align=R, anchor=MID, spacing=1.0)
    for i, (ic, head, body) in enumerate(c['pillars']):
        x = 0.6 + i * 2.97
        icon_circle(s, ic, x, 4.0, 0.42)
        text(s, x + 0.54, 3.96, 2.3, 0.26, head, size=11, font=T.TITLE_FONT)
        text(s, x + 0.54, 4.22, 2.3, 0.7, body, size=8.5, color=T.BODY, spacing=1.08)
    notes(s, c['notes'])


def s_impact(s):
    c = K.SLIDE_IMPACT
    title(s, c['title'], 0.75, 0.42, 6.6, 0.95, size=22)
    chip(s, c['sdg'], 0.75, 1.45, bg=T.PURPLE, fg=T.WHITE, size=9.5, h=0.34, ic=('graduation-cap', 'white'))
    for i, (ic, head, body) in enumerate(c['pillars']):
        x = 0.75 + i * 1.95
        card(s, x, 2.0, 1.82, 1.9, radius=0.16)
        icon_circle(s, ic, x + 0.18, 2.16, 0.46)
        text(s, x + 0.18, 2.72, 1.5, 0.3, head, size=12, font=T.TITLE_FONT)
        text(s, x + 0.18, 3.04, 1.5, 0.84, body, size=8.5, color=T.BODY, spacing=1.08)
    text(s, 0.75, 4.08, 5.7, 0.26, c['beneficiaries'], size=9.5, font=T.LABEL_FONT, color=T.INK)
    text(s, 0.75, 4.36, 5.7, 0.26, c['governance'], size=9, color=T.BODY)
    card(s, 6.75, 1.45, 2.65, 3.3, radius=0.16)
    text(s, 6.93, 1.58, 2.35, 0.3, c['kpis_title'], size=11, font=T.TITLE_FONT)
    for i, k in enumerate(c['kpis']):
        y = 2.0 + i * 0.44
        icon(s, 'check', 'purple', 6.95, y + 0.05, 0.2)
        text(s, 7.25, y, 2.05, 0.32, k, size=8.5, anchor=MID, spacing=1.0)
    notes(s, c['notes'])


TAG_STYLE = {'live': (T.MINT, T.GREEN, None), 'validating': (T.PALEY, T.AMBER_DARK, None),
             'building': (T.PURPLE, T.WHITE, None), 'future': (T.WHITE, T.DEEP, T.DEEP)}


def s_business(s):
    c = K.SLIDE_BUSINESS
    title(s, c['title'], 0.6, 0.45, 7.6, 0.6, size=26)
    w, gap = 2.1, 0.13
    for i, (seg, head, desc, price, detail, img, (tag, style)) in enumerate(c['offers']):
        x = 0.6 + i * (w + gap)
        tbg, tfg, tl = TAG_STYLE[style]
        card(s, x, 1.3, w, 3.85, radius=0.16)
        pic(s, img, x, 1.3, w=w, h=w / 2, alt=head)
        chip(s, tag, x + 0.12, 1.42, bg=tbg, fg=tfg, size=7, h=0.24, line=tl)
        text(s, x + 0.16, 2.46, w - 0.3, 0.22, seg, size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.16, 2.68, w - 0.3, 0.5, head, size=12, font=T.TITLE_FONT, spacing=0.95)
        text(s, x + 0.16, 3.2, w - 0.3, 0.8, desc, size=8.5, color=T.BODY, spacing=1.08)
        rect(s, x + 0.12, 4.08, w - 0.24, 0.94, fill=T.LAV, radius=0.1)
        text(s, x + 0.22, 4.13, w - 0.44, 0.44, price, size=10.5, font=T.TITLE_FONT, color=T.DEEP, anchor=MID,
             spacing=0.95)
        text(s, x + 0.22, 4.56, w - 0.44, 0.44, detail, size=7.5, color=T.INK, spacing=1.0)
    notes(s, c['notes'])


def s_financial(s):
    c = K.SLIDE_FINANCIAL
    title(s, c['title'], 0.6, 0.45, 6.0, 0.6, size=26)
    for i, (lbl, v) in enumerate(c['stage']):
        x = 0.6 + i * 2.0
        card(s, x, 1.25, 1.88, 0.86, radius=0.14)
        text(s, x + 0.16, 1.32, 1.6, 0.24, lbl, size=8, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.16, 1.56, 1.6, 0.46, v, size=18, font=T.TITLE_FONT, anchor=MID)
    # unit economics
    for i, (head, rows, margin) in enumerate(c['units']):
        x = 0.6 + i * 2.0
        card(s, x, 2.25, 1.88, 2.55, radius=0.14)
        text(s, x + 0.14, 2.34, 1.6, 0.44, head, size=10, font=T.TITLE_FONT, spacing=0.95)
        for j, (lbl, v) in enumerate(rows):
            y = 2.84 + j * 0.42
            text(s, x + 0.14, y, 1.62, 0.2, lbl, size=7.5, color=T.BODY)
            text(s, x + 0.14, y + 0.17, 1.62, 0.24, v, size=11, font=T.TITLE_FONT)
        value_tile(s, x + 0.14, 4.18, 1.6, 0.46, margin, size=11)
    text(s, 0.6, 4.9, 3.9, 0.22, c['units_note'], size=7.5, color=T.BODY)
    # 12-month scenario
    card(s, 4.7, 1.25, 4.7, 3.55, radius=0.16)
    text(s, 4.9, 1.36, 2.4, 0.3, c['scenario_title'], size=11, font=T.TITLE_FONT)
    for j, h in enumerate(c['scenario_head'][1:]):
        text(s, 6.95 + j * 1.2, 1.4, 1.1, 0.22, h, size=8, font=T.LABEL_FONT, color=T.PURPLE, align=C)
    for i, (lbl, a, b, strong) in enumerate(c['scenario']):
        y = 1.8 + i * 0.42
        rect(s, 4.9, y - 0.05, 4.3, 0.01, fill=T.BORDER)
        f = T.TITLE_FONT if strong else T.BODY_FONT
        text(s, 4.9, y, 2.0, 0.34, lbl, size=9, font=T.LABEL_FONT if strong else T.BODY_FONT, anchor=MID)
        for j, v in enumerate((a, b)):
            text(s, 6.95 + j * 1.2, y, 1.1, 0.34, v, size=11 if strong else 9.5, font=f,
                 color=T.DEEP if strong else T.INK, align=C, anchor=MID)
    text(s, 4.7, 4.9, 4.7, 0.36, c['footer'], size=7.5, font=T.LABEL_FONT, color=T.INK, spacing=1.05)
    notes(s, c['notes'])


def s_funding(s):
    c = K.SLIDE_FUNDING
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=26)
    card(s, 0.6, 1.2, 4.6, 3.95, radius=0.18)
    text(s, 0.82, 1.32, 4.2, 0.24, c['label'], size=9, font=T.LABEL_FONT, color=T.PURPLE)
    value_tile(s, 0.82, 1.58, 1.7, 0.56, c['amount'], size=22)
    text(s, 2.65, 1.58, 2.4, 0.56, c['purpose'], size=8.5, color=T.INK, anchor=MID, spacing=1.05)
    text(s, 0.82, 2.28, 4.0, 0.26, c['alloc_title'], size=10.5, font=T.TITLE_FONT)
    for i, (ic, use, detail, share) in enumerate(c['alloc']):
        y = 2.62 + i * 0.41
        icon_circle(s, ic, 0.82, y, 0.32)
        text(s, 1.24, y - 0.04, 2.95, 0.22, use, size=9, font=T.LABEL_FONT)
        text(s, 1.24, y + 0.16, 2.95, 0.2, detail, size=7.5, color=T.BODY)
        value_tile(s, 4.3, y + 0.02, 0.72, 0.28, share, size=9)
    card(s, 5.4, 1.2, 4.0, 3.95, radius=0.18)
    text(s, 5.62, 1.32, 3.6, 0.5, c['unlocks_title'], size=11, font=T.TITLE_FONT, spacing=1.0)
    for i, u in enumerate(c['unlocks']):
        y = 1.9 + i * 0.44
        num_circle(s, i + 1, 5.62, y, 0.32, size=9.5)
        text(s, 6.05, y - 0.04, 3.2, 0.4, u, size=9.5, anchor=MID)
    notes(s, c['notes'])


ROAD_STYLE = {'done': (T.PURPLE, T.WHITE, T.LAV2), 'next': (T.LAV2, T.DEEP, T.DEEP), 'later': (T.WHITE, T.DEEP, T.BODY)}


def s_roadmap(s):
    c = K.SLIDE_ROADMAP
    title(s, c['title'], 0.6, 0.42, 6.0, 0.6, size=26)
    for i, (lbl, ic, style, items) in enumerate(c['columns']):
        x = 0.6 + i * 2.97
        bg, head, body = ROAD_STYLE[style]
        rect(s, x, 1.3, 2.8, 2.95, fill=bg, line=T.BORDER if style == 'later' else None, radius=0.18, lw=0.75)
        icon_circle(s, ic, x + 0.2, 1.46, 0.46, bg=T.WHITE, ic='purple')
        text(s, x + 0.78, 1.46, 1.9, 0.46, lbl, size=10.5, font=T.TITLE_FONT, color=head, anchor=MID)
        step = min(0.47, 2.0 / len(items))
        for j, it in enumerate(items):
            y = 2.1 + j * step
            icon(s, 'check' if style == 'done' else 'arrow-right', 'white' if style == 'done' else 'purple',
                 x + 0.22, y + 0.06, 0.2)
            text(s, x + 0.52, y, 2.2, 0.34, it, size=9.5, color=head if style == 'done' else T.INK, anchor=MID)
    text(s, 0.6, 4.45, 1.3, 0.3, c['kpis_title'], size=10, font=T.TITLE_FONT, anchor=MID)
    x = 1.85
    for k in c['kpis']:
        _, w = chip(s, k, x, 4.45, bg=T.LAV2, fg=T.DEEP, size=7.5, h=0.3)
        x += w + 0.06
    notes(s, c['notes'])


def s_pnl(s):
    c = K.SLIDE_PNL
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=24)
    card(s, 0.6, 1.2, 5.3, 3.95, radius=0.16)
    for j, h in enumerate(c['head']):
        text(s, 0.8 if j == 0 else 3.2 + (j - 1) * 1.3, 1.32, 2.3 if j == 0 else 1.2, 0.24, h, size=8.5,
             font=T.LABEL_FONT, color=T.PURPLE, align=L if j == 0 else R)
    for i, (lbl, a, b, strong) in enumerate(c['rows']):
        y = 1.6 + i * 0.31
        rect(s, 0.8, y - 0.03, 4.9, 0.01, fill=T.BORDER)
        f = T.TITLE_FONT if strong else T.BODY_FONT
        text(s, 0.8, y, 2.4, 0.3, lbl, size=9, font=T.LABEL_FONT if strong else T.BODY_FONT, anchor=MID)
        for j, v in enumerate((a, b)):
            text(s, 3.2 + j * 1.3, y, 1.2, 0.3, v, size=9.5, font=f, color=T.DEEP if strong else T.INK, align=R,
                 anchor=MID)
    card(s, 6.1, 1.2, 3.3, 3.95, radius=0.16)
    text(s, 6.3, 1.32, 2.9, 0.26, c['assump_title'], size=10.5, font=T.TITLE_FONT)
    for i, a in enumerate(c['assumptions']):
        y = 1.7 + i * 0.42
        oval(s, 6.32, y + 0.1, 0.07, fill=T.PURPLE)
        text(s, 6.5, y, 2.8, 0.4, a, size=8, color=T.INK, spacing=1.0)
    notes(s, c['notes'])


def s_closing(s):
    c = K.SLIDE_CLOSING
    title(s, c['headline'], 0.6, 0.7, 5.1, 1.3, size=23, color=T.ON_BLOB)
    text(s, 0.6, 2.15, 4.9, 0.6, c['sub'], size=13, font=T.LABEL_FONT, color=T.DEEP, spacing=1.1)
    text(s, 0.6, 2.9, 4.9, 0.3, c['line'], size=10.5, color=T.ON_BLOB)
    rect(s, 0.6, 3.45, 4.9, 0.62, fill=T.WHITE, radius=0.14)
    text(s, 0.8, 3.45, 4.5, 0.62, c['cta'], size=10, font=T.LABEL_FONT, color=T.INK, anchor=MID, spacing=1.05)
    pic(s, 'paper_whale_tilt.png', 6.2, 0.3, w=2.3, alt='A child’s colored whale on paper')
    pic(s, 'tab_result.png', 6.55, 1.75, w=3.1, alt='The same whale alive in Scanvas')
    rect(s, 0.6, 4.35, 0.95, 0.95, fill=T.WHITE, radius=0.12)
    pic(s, T.ASSETS / 'qr_scanvas.png', 0.66, 4.41, w=0.83, h=0.83, alt='QR code to scanvas.id')
    text(s, 1.7, 4.4, 3.5, 0.4, K.WEBSITE, size=18, font=T.TITLE_FONT, color=T.ON_BLOB, anchor=MID)
    text(s, 1.7, 4.82, 3.8, 0.3, c['names'], size=10, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    notes(s, c['notes'])


def s_sources(s):
    c = K.SLIDE_SOURCES
    title(s, c['title'], 0.6, 0.45, c.get('title_w', 7.0), 0.75, size=c.get('title_size', 24))
    card(s, 0.6, 1.25, 8.8, 3.55, radius=0.16)
    cols = [(0.8, 2.75), (3.6, 0.95), (4.65, 4.6)]
    for (x, w), h in zip(cols, c['head']):
        text(s, x, 1.38, w, 0.26, h, size=8.5, font=T.LABEL_FONT, color=T.PURPLE)
    for i, row in enumerate(c['rows']):
        y = 1.72 + i * 0.5
        rect(s, 0.8, y - 0.04, 8.4, 0.01, fill=T.BORDER)
        for j, ((x, w), v) in enumerate(zip(cols, row)):
            text(s, x, y, w, 0.44, v, size=9.5 if j == 1 else 8.5, font=T.TITLE_FONT if j == 1 else T.BODY_FONT,
                 color=T.INK if j < 2 else T.BODY, anchor=MID, spacing=1.0)
    text(s, 0.6, 4.9, 8.8, 0.45, c['footnote'], size=7, color=T.BODY, spacing=1.05)
    notes(s, c['notes'])


def s_competition(s):
    c = K.SLIDE_COMPETITION
    title(s, c['title'], 0.6, 0.38, c.get('title_w', 7.0), 0.8, size=c.get('title_size', 26))
    if c.get('sub'):
        text(s, 0.6, 0.95, 7.6, 0.3, c['sub'], size=10.5, font=T.LABEL_FONT, color=T.DEEP)
    lx, lw, cw, top, rh = 0.6, 2.35, 1.33, 1.35, 0.33
    n = len(c['players'])
    card(s, lx, top, lw + n * cw + 0.1, 0.5 + len(c['rows']) * rh + 0.1, radius=0.14)
    if c.get('highlight_own', True):
        rect(s, lx + lw + 0.05, top + 0.06, cw - 0.1, 0.44 + len(c['rows']) * rh + 0.04, fill=T.LAV2, radius=0.1)
    for j, p in enumerate(c['players']):
        x = lx + lw + j * cw
        text(s, x, top + 0.06, cw, 0.44, p, size=8.5 if j else 11, font=T.TITLE_FONT,
             color=T.DEEP if j == 0 else T.INK, align=C, anchor=MID, spacing=0.95)
    for i, (crit, cells) in enumerate(c['rows']):
        y = top + 0.52 + i * rh
        rect(s, lx + 0.15, y, lw + n * cw - 0.2, 0.01, fill=T.BORDER)
        text(s, lx + 0.18, y, lw - 0.2, rh, crit, size=8.5, font=T.LABEL_FONT, anchor=MID)
        for j, v in enumerate(cells):
            x = lx + lw + j * cw
            if v == 'yes':
                icon(s, 'check', 'purple' if j == 0 else 'green', x + cw / 2 - 0.1, y + rh / 2 - 0.1, 0.2)
            elif v == 'no':
                text(s, x, y, cw, rh, '—', size=9, color=T.GRAY, align=C, anchor=MID)
            else:
                text(s, x, y, cw, rh, v, size=7.5, font=T.LABEL_FONT if j == 0 else T.BODY_FONT,
                     color=T.DEEP if j == 0 else T.BODY, align=C, anchor=MID)
    y0 = top + 0.72 + len(c['rows']) * rh
    if c.get('wins'):
        text(s, 0.6, y0 + 0.02, 1.3, 0.28, c['wins_title'], size=9, font=T.TITLE_FONT, anchor=MID)
    x = 1.8
    for who, what in c.get('wins', []):
        lbl = f'{who}: {what}'
        w = len(lbl) * 7 * 0.52 / 72 + 0.26
        chip(s, lbl, x, y0 + 0.02, bg=T.WHITE, fg=T.INK, size=7, h=0.28, w=w, line=T.BORDER)
        x += w + 0.05
    if c.get('position'):
        text(s, 0.6, y0 + 0.4, 8.8, 0.36, c['position'], size=9.5, font=T.LABEL_FONT, color=T.DEEP, spacing=1.05)
    if c.get('legend'):
        text(s, 0.6, 5.12, 8.8, 0.24, c['legend'], size=7.5, color=T.BODY)
    notes(s, c['notes'])


def s_competitors(s):
    c = K.SLIDE_COMPETITORS
    title(s, c['title'], 0.6, 0.45, 7.5, 0.6, size=24)
    card(s, 0.6, 1.2, 8.8, 3.95, radius=0.16)
    cols = [(0.8, 1.55), (2.4, 2.75), (5.2, 2.35), (7.6, 1.7)]
    for (x, w), h in zip(cols, c['head']):
        text(s, x, 1.32, w, 0.26, h, size=8.5, font=T.LABEL_FONT, color=T.PURPLE)
    for i, row in enumerate(c['rows']):
        y = 1.66 + i * 0.68
        rect(s, 0.8, y - 0.04, 8.4, 0.01, fill=T.BORDER)
        for j, ((x, w), v) in enumerate(zip(cols, row)):
            text(s, x, y, w, 0.62, v, size=8.5 if j == 0 else 7.5, font=T.TITLE_FONT if j == 0 else T.BODY_FONT,
                 color=T.INK if j < 3 else T.PURPLE, anchor=MID, spacing=1.0)
    notes(s, c['notes'])
