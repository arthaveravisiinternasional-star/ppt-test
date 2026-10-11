"""Slides specific to the DSC Season 17 v4 edition. Same helpers and look as slides_dsc.py.
Imported after build_deck_dsc4.py swaps deck.content for deck.content_dsc4."""
from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import slides as S
from . import slides_dsc as D
from . import theme as T
from .helpers import (L, C, R, MID, text, title, rect, card, oval, pic, icon, icon_circle, chip, arrow_chips, notes)
from .helpers import rgb
from .slides_dsc import value_tile


def s_overview(s):
    """slides_dsc.s_overview with block spacing fitted to the longer Customers copy."""
    c = K.SLIDE_OVERVIEW
    chip(s, c['tag'], 0.6, 0.45, bg=T.MINT, fg=T.GREEN, size=8.5, h=0.3, ic=('check', 'green'))
    title(s, c['title'], 0.6, 0.88, 4.0, 0.85, size=21)
    for (ic, head, body), y, h in zip(c['blocks'], (1.85, 2.78, 4.02), (0.62, 0.95, 0.62)):
        icon_circle(s, ic, 0.6, y, 0.44)
        text(s, 1.18, y - 0.02, 3.0, 0.26, head, size=11.5, font=T.TITLE_FONT)
        text(s, 1.18, y + 0.25, 3.15, h, body, size=8.5, color=T.BODY, spacing=1.08)
    for i, (img, lbl) in enumerate(c['phones']):
        x = 4.4 + i * 1.74
        pic(s, img, x, 0.75, h=3.4, alt=lbl)
        text(s, x, 4.18, 1.73, 0.24, lbl, size=8.5, font=T.LABEL_FONT, color=T.BODY, align=C)
    notes(s, c['notes'])


def s_problem(s):
    """Shared problem slide; the closing line becomes an institutional-problem strip (hypothesis being validated)."""
    c = K.SLIDE_2_PROBLEM
    S.s2_problem(s)
    rect(s, 0.6, 4.66, 8.8, 0.62, fill=T.WHITE, line=T.BORDER, radius=0.14, lw=0.75)
    icon_circle(s, 'school', 0.74, 4.76, 0.42)
    chip(s, c['inst_tag'], 1.28, 4.72, bg=T.PALEY, fg=T.AMBER_DARK, size=7, h=0.22)
    text(s, 1.28, 4.95, 4.65, 0.3, c['inst'], size=8, color=T.INK, anchor=MID, spacing=1.0)
    rect(s, 6.05, 4.74, 0.01, 0.46, fill=T.BORDER)
    text(s, 6.2, 4.66, 3.1, 0.62, c['opportunity'], size=10.5, font=T.TITLE_FONT, color=T.PURPLE, anchor=MID,
         spacing=1.0)


def s_business(s):
    c = K.SLIDE_BUSINESS
    D.s_business(s)
    text(s, 0.6, 0.95, 8.8, 0.3, c['lead'], size=10, color=T.BODY)


def s_gtm(s):
    c = K.SLIDE_GTM
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=26)
    for i, (tag, aud, steps, channels) in enumerate(c['tracks']):
        y = 1.3 + i * 1.3
        card(s, 0.6, y, 8.8, 1.15, radius=0.16)
        chip(s, tag, 0.8, y + 0.16, bg=T.PURPLE if i == 0 else T.LAV2, fg=T.WHITE if i == 0 else T.DEEP, size=9,
             h=0.3, w=0.62)
        text(s, 1.55, y + 0.14, 3.2, 0.34, aud, size=13, font=T.TITLE_FONT, anchor=MID)
        arrow_chips(s, steps, 0.8, y + 0.62, h=0.3, size=8.5, gap=0.22, bg=T.LAV2 if i == 0 else T.LAV,
                    last=(T.PURPLE, T.WHITE))
        text(s, 4.9, y + 0.14, 4.35, 0.34, channels, size=8, color=T.BODY, align=R, anchor=MID, spacing=1.0)
    for i, (ic, head, body) in enumerate(c['pillars']):
        x = 0.6 + i * 2.97
        icon_circle(s, ic, x, 4.0, 0.42)
        text(s, x + 0.54, 3.96, 2.3, 0.26, head, size=11, font=T.TITLE_FONT)
        text(s, x + 0.54, 4.22, 2.3, 0.7, body, size=8.5, color=T.BODY, spacing=1.08)
    notes(s, c['notes'])


def s_financial(s):
    c = K.SLIDE_FINANCIAL
    title(s, c['title'], 0.6, 0.45, 6.0, 0.6, size=26)
    for i, (lbl, v) in enumerate(c['stage']):
        x = 0.6 + i * 2.0
        card(s, x, 1.25, 1.88, 0.86, radius=0.14)
        text(s, x + 0.16, 1.32, 1.6, 0.24, lbl, size=8, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.16, 1.54, 1.6, 0.5, v, size=18 if '\n' not in v else 11.5, font=T.TITLE_FONT, anchor=MID,
             spacing=0.95)
    for i, (head, rows, margin) in enumerate(c['units']):
        x = 0.6 + i * 2.0
        card(s, x, 2.25, 1.88, 2.55, radius=0.14)
        text(s, x + 0.14, 2.34, 1.6, 0.44, head, size=10, font=T.TITLE_FONT, spacing=0.95)
        for j, (lbl, v) in enumerate(rows):
            y = 2.84 + j * 0.42
            text(s, x + 0.14, y, 1.62, 0.2, lbl, size=7.5, color=T.BODY)
            text(s, x + 0.14, y + 0.17, 1.62, 0.24, v, size=11, font=T.TITLE_FONT)
        value_tile(s, x + 0.14, 4.18, 1.6, 0.46, margin, size=11)
    text(s, 0.6, 4.9, 3.9, 0.36, c['units_note'], size=7.5, color=T.BODY, spacing=1.0)
    # 12-month projection down to the net result (no cash balance: funding not secured yet)
    card(s, 4.7, 1.25, 4.7, 3.55, radius=0.16)
    text(s, 4.9, 1.34, 2.4, 0.3, c['scenario_title'], size=11, font=T.TITLE_FONT, anchor=MID)
    chip(s, c['scenario_tag'], 4.9, 1.66, bg=T.PALEY, fg=T.AMBER_DARK, size=6.5, h=0.2)
    for j, h in enumerate(c['scenario_head'][1:]):
        text(s, 6.95 + j * 1.2, 1.5, 1.1, 0.22, h, size=8, font=T.LABEL_FONT, color=T.PURPLE, align=C)
    for i, (lbl, a, b, style) in enumerate(c['scenario']):
        y = 2.0 + i * 0.36
        if style == 'cash':
            rect(s, 4.85, y - 0.02, 4.4, 0.34, fill=T.LAV2, radius=0.08)
        else:
            rect(s, 4.9, y - 0.03, 4.3, 0.01, fill=T.BORDER)
        strong = style in ('sum', 'cash')
        text(s, 4.95, y, 2.0, 0.3, lbl, size=7.5 if style == 'sub' else 8.5,
             font=T.LABEL_FONT if strong else T.BODY_FONT, color=T.BODY if style == 'sub' else T.INK, anchor=MID,
             spacing=1.0)
        for j, v in enumerate((a, b)):
            text(s, 6.95 + j * 1.2, y, 1.1, 0.3, v, size=10.5 if strong else 9, font=T.TITLE_FONT if strong else
                 T.BODY_FONT, color=T.DEEP if strong else T.INK, align=C, anchor=MID)
    text(s, 4.9, 4.5, 4.3, 0.24, [[(c['disclaimer'], {'italic': True})]], size=7, color=T.BODY, anchor=MID)
    text(s, 4.7, 4.88, 4.7, 0.4, c['footer'], size=7.5, font=T.LABEL_FONT, color=T.INK, spacing=1.05)
    notes(s, c['notes'])


def s_funding(s):
    """Rp200M = total 12-month capital plan (not a grant request): allocation | funding strategy | phased deployment,
    base-case outcomes underneath."""
    c = K.SLIDE_FUNDING
    title(s, c['title'], 0.6, 0.42, 7.0, 0.6, size=26)
    top, bot = 1.15, 4.42
    # 1 capital plan + allocation
    card(s, 0.6, top, 2.9, bot - top, radius=0.16)
    text(s, 0.78, top + 0.1, 2.6, 0.22, c['label'], size=8.5, font=T.LABEL_FONT, color=T.PURPLE)
    value_tile(s, 0.78, top + 0.36, 1.45, 0.5, c['amount'], size=20)
    text(s, 0.78, top + 0.92, 2.6, 0.5, c['purpose'], size=7.5, color=T.INK, spacing=1.0)
    text(s, 0.78, top + 1.46, 2.6, 0.24, c['alloc_title'], size=9.5, font=T.TITLE_FONT, anchor=MID)
    rows = c['alloc'] + [c['total']]
    for i, (cat, budget, share) in enumerate(rows):
        y = top + 1.74 + i * 0.205
        last = i == len(rows) - 1
        if last:
            rect(s, 0.72, y - 0.01, 2.66, 0.21, fill=T.LAV2, radius=0.05)
        else:
            rect(s, 0.78, y - 0.01, 2.54, 0.005, fill=T.BORDER)
        f = T.LABEL_FONT if last else T.BODY_FONT
        text(s, 0.8, y, 1.55, 0.2, cat, size=7.5, font=f, anchor=MID)
        text(s, 2.3, y, 0.55, 0.2, budget, size=7.5, font=T.TITLE_FONT if last else T.LABEL_FONT, color=T.DEEP,
             align=R, anchor=MID)
        text(s, 2.85, y, 0.45, 0.2, share, size=7.5, font=f, color=T.DEEP, align=R, anchor=MID)
    # 2 funding strategy
    card(s, 3.62, top, 2.7, bot - top, radius=0.16)
    text(s, 3.8, top + 0.1, 2.4, 0.26, c['strategy_title'], size=10.5, font=T.TITLE_FONT, anchor=MID)
    for i, (ic, head, body) in enumerate(c['strategy']):
        y = top + 0.5 + i * 0.9
        icon_circle(s, ic, 3.8, y, 0.34)
        text(s, 4.22, y, 1.95, 0.34, head, size=9, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
        text(s, 3.8, y + 0.38, 2.38, 0.5, body, size=7.5, color=T.INK, spacing=1.0)
    # 3 milestone-based deployment
    card(s, 6.44, top, 2.96, bot - top, radius=0.16)
    text(s, 6.62, top + 0.1, 2.6, 0.26, c['phases_title'], size=10.5, font=T.TITLE_FONT, anchor=MID)
    for i, (when, head, body) in enumerate(c['phases']):
        y = top + 0.5 + i * 0.9
        chip(s, when, 6.62, y + 0.02, bg=T.PURPLE if i == 0 else T.LAV2, fg=T.WHITE if i == 0 else T.DEEP, size=7,
             h=0.24, w=0.58)
        text(s, 7.28, y, 2.0, 0.28, head, size=8.5, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
        text(s, 6.62, y + 0.32, 2.65, 0.56, body, size=7.5, color=T.INK, spacing=1.0)
    # base-case outcomes
    text(s, 0.6, 4.52, 8.8, 0.24, c['outcomes_title'], size=9.5, font=T.TITLE_FONT, anchor=MID)
    ws = [len(o) * 7 * 0.5 / 72 + 0.3 for o in c['outcomes']]
    gap = (8.8 - sum(ws)) / (len(ws) - 1)
    x = 0.6
    for o, w in zip(c['outcomes'], ws):
        chip(s, o, x, 4.8, bg=T.LAV2, fg=T.DEEP, size=7, h=0.28, w=w)
        x += w + gap
    text(s, 0.6, 5.12, 8.8, 0.2, [[(c['outcomes_note'], {'italic': True})]], size=7, color=T.BODY, anchor=MID)
    notes(s, c['notes'])


def s_team(s):
    """slides.s12_team with room for the longer founder bios (smaller focus text, smaller final line)."""
    c = K.SLIDE_12_TEAM
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(T.BLOB_MAIN)
    title(s, c['title'], 0.6, 0.45, 8.8, 0.6, size=26, color=T.ON_BLOB, align=C)
    for i, (ini, name, role, focus, photo) in enumerate(c['team']):
        x = 0.6 + i * 4.5
        rect(s, x, 1.3, 4.3, 1.62, fill=T.WHITE, radius=0.18)
        px, py, pw, ph = {'founder_sk.png': (0.139, 1.335, 1.267, 1.43),
                          'founder_hh.png': (0.07, 1.316, 1.38, 1.47)}[photo]
        pic(s, photo, x + px, py + 0.06, w=pw, h=ph, alt=name)
        text(s, x + 1.45, 1.4, 2.75, 0.3, name, size=13, font=T.TITLE_FONT, anchor=MID)
        text(s, x + 1.45, 1.71, 2.75, 0.24, role, size=9.5, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 1.45, 1.98, 2.72, 0.9, focus, size=7.5, color=T.BODY, spacing=1.08)
    icon(s, 'quote', 'deep', 0.6, 3.17, 0.36)
    text(s, 1.1, 3.1, 8.2, 0.8, c['closing'], size=15, font=T.LABEL_FONT, color=T.ON_BLOB, spacing=1.1)
    text(s, 1.1, 3.98, 8.2, 0.36, c['final'], size=11.5, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
    rect(s, 1.1, 4.62, 0.5, 0.5, fill=T.WHITE, radius=0.12)
    pic(s, T.LOGO, 1.15, 4.67, h=0.4, alt='Scanvas logo')
    text(s, 1.72, 4.62, 1.3, 0.5, K.WEBSITE, size=12, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    oval(s, 3.05, 4.84, 0.06, fill=T.ON_BLOB)
    text(s, 3.25, 4.62, 3.6, 0.5, K.TRACK, size=9, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    notes(s, c['notes'])


def s_roadmap(s):
    c = K.SLIDE_ROADMAP
    title(s, c['title'], 0.6, 0.38, 8.8, 0.5, size=26)
    text(s, 0.6, 0.92, 8.8, 0.3, c['sub'], size=10.5, font=T.LABEL_FONT, color=T.PURPLE)
    w, gap, top, h = 2.1, 0.133, 1.36, 2.82
    for i, (tag, head, items, blabel, btext) in enumerate(c['stages']):
        x = 0.6 + i * (w + gap)
        fill = [T.PURPLE, T.LAV2, T.WHITE, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, top, w, h, fill=fill, line=T.BORDER if i >= 2 else None, radius=0.16, lw=0.75)
        chip(s, tag, x + 0.15, top + 0.14, bg=T.WHITE if i < 2 else T.LAV2, fg=T.DEEP, size=7.5, h=0.26)
        text(s, x + 0.15, top + 0.46, w - 0.3, 0.46, head, size=12, font=T.TITLE_FONT, color=fg, spacing=0.95)
        for j, it in enumerate(items):
            yy = top + 1.0 + j * 0.27
            icon(s, 'check' if i == 0 else 'arrow-right', 'white' if i == 0 else 'purple', x + 0.15, yy + 0.05, 0.15)
            text(s, x + 0.37, yy, w - 0.5, 0.25, it, size=8.5, color=fg, anchor=MID)
        bh = 0.72
        by = top + h - bh - 0.12
        rect(s, x + 0.12, by, w - 0.24, bh, fill=T.WHITE if i < 2 else T.LAV, radius=0.1)
        text(s, x + 0.22, by + 0.06, w - 0.44, 0.18, blabel, size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.22, by + 0.24, w - 0.44, bh - 0.28, btext, size=8, font=T.LABEL_FONT, spacing=1.0)
        if i < 3:
            rect(s, x + w + 0.012, top + h / 2 - 0.1, 0.11, 0.2, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    text(s, 0.6, 4.36, 8.8, 0.26, c['kpis_title'], size=10, font=T.TITLE_FONT, anchor=MID)
    x = 0.6
    for k in c['kpis']:
        _, w = chip(s, k, x, 4.66, bg=T.LAV2, fg=T.DEEP, size=7.5, h=0.3, w=1.4)
        x += 1.48
    text(s, 0.6, 5.04, 8.8, 0.24, c['footnote'], size=7.5, color=T.BODY, anchor=MID)
    notes(s, c['notes'])


def s_closing(s):
    c = K.SLIDE_CLOSING
    title(s, c['headline'], 0.6, 0.55, 5.1, 1.2, size=23, color=T.ON_BLOB)
    text(s, 0.6, 1.85, 4.9, 0.6, c['sub'], size=12.5, font=T.LABEL_FONT, color=T.DEEP, spacing=1.1)
    rect(s, 0.6, 2.55, 4.9, 1.62, fill=T.WHITE, radius=0.14)
    text(s, 0.8, 2.62, 4.5, 0.28, c['why_title'], size=10.5, font=T.TITLE_FONT, color=T.PURPLE, anchor=MID)
    for i, w in enumerate(c['why']):
        y = 2.94 + i * 0.27
        icon(s, 'check', 'purple', 0.82, y + 0.05, 0.16)
        text(s, 1.06, y, 4.2, 0.26, w, size=9.5, font=T.LABEL_FONT, color=T.INK, anchor=MID)
    text(s, 0.8, 3.76, 4.5, 0.38, c['cta'], size=8.5, color=T.BODY, anchor=MID, spacing=1.0)
    pic(s, 'paper_whale_tilt.png', 6.2, 0.3, w=2.3, alt='A child’s colored whale on paper')
    pic(s, 'tab_result.png', 6.55, 1.75, w=3.1, alt='The same whale alive in Scanvas')
    rect(s, 0.6, 4.35, 0.95, 0.95, fill=T.WHITE, radius=0.12)
    pic(s, T.ASSETS / 'qr_scanvas.png', 0.66, 4.41, w=0.83, h=0.83, alt='QR code to scanvas.id')
    text(s, 1.7, 4.4, 3.5, 0.4, K.WEBSITE, size=18, font=T.TITLE_FONT, color=T.ON_BLOB, anchor=MID)
    text(s, 1.7, 4.82, 3.8, 0.3, c['names'], size=10, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    notes(s, c['notes'])


def s_pnl(s):
    """P&L (+ illustrative cash rows) left; assumptions and the illustrative funding scenario right."""
    c = K.SLIDE_PNL
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=24)
    card(s, 0.6, 1.2, 4.75, 3.95, radius=0.16)
    for j, h in enumerate(c['head']):
        text(s, 0.78 if j == 0 else 2.95 + (j - 1) * 1.15, 1.3, 2.2 if j == 0 else 1.05, 0.24, h, size=8.5,
             font=T.LABEL_FONT, color=T.PURPLE, align=L if j == 0 else R)
    step = min(0.31, 3.45 / len(c['rows']))
    for i, (lbl, a, b, strong) in enumerate(c['rows']):
        y = 1.56 + i * step
        rect(s, 0.78, y - 0.02, 4.4, 0.01, fill=T.BORDER)
        f = T.TITLE_FONT if strong else T.BODY_FONT
        text(s, 0.78, y, 2.3, step - 0.02, lbl, size=8, font=T.LABEL_FONT if strong else T.BODY_FONT, anchor=MID)
        for j, v in enumerate((a, b)):
            text(s, 2.95 + j * 1.15, y, 1.05, step - 0.02, v, size=8.5, font=f, color=T.DEEP if strong else T.INK,
                 align=R, anchor=MID)
    x0, w0 = 5.5, 3.9
    card(s, x0, 1.2, w0, 3.95, radius=0.16)
    text(s, x0 + 0.18, 1.28, 3.5, 0.26, c['assump_title'], size=10, font=T.TITLE_FONT, anchor=MID)
    for i, a in enumerate(c['assumptions']):
        y = 1.58 + i * 0.3
        oval(s, x0 + 0.2, y + 0.09, 0.06, fill=T.PURPLE)
        text(s, x0 + 0.36, y, w0 - 0.5, 0.3, a, size=7.5, color=T.INK, spacing=1.0)
    by = 3.14
    rect(s, x0 + 0.12, by, w0 - 0.24, 1.9, fill=T.LAV2, radius=0.12)
    text(s, x0 + 0.26, by + 0.06, w0 - 0.5, 0.22, c['scenario_title'], size=9, font=T.TITLE_FONT, color=T.DEEP,
         anchor=MID)
    text(s, x0 + 0.26, by + 0.3, w0 - 0.5, 0.38, c['scenario_lead'], size=7, color=T.INK, spacing=1.0)
    for i, (lbl, v) in enumerate(c['scenario']):
        y = by + 0.72 + i * 0.22
        oval(s, x0 + 0.3, y + 0.07, 0.06, fill=T.PURPLE)
        text(s, x0 + 0.44, y, 1.0, 0.2, lbl, size=7.5, font=T.LABEL_FONT, anchor=MID)
        text(s, x0 + 1.45, y, 2.0, 0.2, v, size=7.5, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
    text(s, x0 + 0.26, by + 1.18, w0 - 0.5, 0.68, [[(c['scenario_note'], {'italic': True})]], size=6.5,
         color=T.BODY, spacing=1.0)
    notes(s, c['notes'])
