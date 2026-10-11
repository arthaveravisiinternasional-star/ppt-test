"""Slides specific to the DSC Season 17 v4 edition. Same helpers and look as slides_dsc.py.
Imported after build_deck_dsc4.py swaps deck.content for deck.content_dsc4."""
from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import slides as S
from . import slides_dsc as D
from . import theme as T
from .helpers import (L, C, R, MID, text, title, rect, card, oval, pic, icon, icon_circle, chip, arrow_chips, notes)
from .slides_dsc import value_tile


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
        text(s, x + 0.16, 1.56, 1.6, 0.46, v, size=18, font=T.TITLE_FONT, anchor=MID)
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
    # 12-month projection incl. net result and cash
    card(s, 4.7, 1.25, 4.7, 3.55, radius=0.16)
    text(s, 4.9, 1.34, 2.0, 0.3, c['scenario_title'], size=11, font=T.TITLE_FONT, anchor=MID)
    chip(s, c['scenario_tag'], 4.9, 1.66, bg=T.PALEY, fg=T.AMBER_DARK, size=6.5, h=0.2)
    for j, h in enumerate(c['scenario_head'][1:]):
        text(s, 6.95 + j * 1.2, 1.5, 1.1, 0.22, h, size=8, font=T.LABEL_FONT, color=T.PURPLE, align=C)
    for i, (lbl, a, b, style) in enumerate(c['scenario']):
        y = 1.98 + i * 0.35
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
    text(s, 4.7, 4.9, 4.7, 0.36, c['footer'], size=7.5, font=T.LABEL_FONT, color=T.INK, spacing=1.05)
    notes(s, c['notes'])


def s_funding(s):
    c = K.SLIDE_FUNDING
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=26)
    # left: amount, sources, use of funds
    card(s, 0.6, 1.2, 4.6, 3.95, radius=0.18)
    text(s, 0.82, 1.3, 4.2, 0.24, c['label'], size=9, font=T.LABEL_FONT, color=T.PURPLE)
    value_tile(s, 0.82, 1.56, 1.7, 0.56, c['amount'], size=22)
    text(s, 2.65, 1.52, 2.4, 0.36, c['purpose'], size=8, color=T.INK, spacing=1.0)
    x = 2.65
    for lbl, v in c['sources']:
        text(s, x, 1.9, 0.75, 0.22, lbl, size=7, font=T.LABEL_FONT, color=T.BODY, anchor=MID)
        value_tile(s, x + 0.72, 1.9, 0.5, 0.22, v, size=7)
        x += 1.25
    text(s, 0.82, 2.26, 4.0, 0.26, c['alloc_title'], size=10.5, font=T.TITLE_FONT)
    for i, (ic, use, detail, share) in enumerate(c['alloc']):
        y = 2.6 + i * 0.41
        icon_circle(s, ic, 0.82, y, 0.32)
        text(s, 1.24, y - 0.04, 2.95, 0.22, use, size=9, font=T.LABEL_FONT)
        text(s, 1.24, y + 0.16, 2.95, 0.2, detail, size=7.5, color=T.BODY)
        value_tile(s, 4.3, y + 0.02, 0.72, 0.28, share, size=9)
    # right: reconciliation with the P&L + validation gates
    card(s, 5.4, 1.2, 4.0, 3.95, radius=0.18)
    text(s, 5.6, 1.3, 3.6, 0.3, c['recon_title'], size=10.5, font=T.TITLE_FONT, anchor=MID)
    for i, (lbl, v, style) in enumerate(c['recon']):
        y = 1.68 + i * 0.36
        if style == 'cash':
            rect(s, 5.55, y - 0.02, 3.7, 0.34, fill=T.LAV2, radius=0.08)
        else:
            rect(s, 5.6, y - 0.03, 3.6, 0.01, fill=T.BORDER)
        text(s, 5.65, y, 2.3, 0.3, lbl, size=7.5, font=T.LABEL_FONT if style else T.BODY_FONT, anchor=MID,
             spacing=1.0)
        text(s, 7.95, y, 1.25, 0.3, v, size=9.5 if style else 10, font=T.TITLE_FONT, color=T.DEEP, align=R,
             anchor=MID)
    text(s, 5.6, 3.22, 3.6, 0.3, c['gates_title'], size=10.5, font=T.TITLE_FONT, anchor=MID)
    for i, (when, what) in enumerate(c['gates']):
        y = 3.6 + i * 0.47
        chip(s, when, 5.6, y + 0.05, bg=T.PURPLE if i == 0 else T.LAV2, fg=T.WHITE if i == 0 else T.DEEP, size=7.5,
             h=0.26, w=0.68)
        text(s, 6.36, y, 2.9, 0.38, what, size=8.5, anchor=MID, spacing=1.0)
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
    """slides_dsc.s_pnl with row spacing fitted to the row count (P&L + cash rows)."""
    c = K.SLIDE_PNL
    title(s, c['title'], 0.6, 0.45, 7.0, 0.6, size=24)
    card(s, 0.6, 1.2, 5.3, 3.95, radius=0.16)
    for j, h in enumerate(c['head']):
        text(s, 0.8 if j == 0 else 3.2 + (j - 1) * 1.3, 1.3, 2.3 if j == 0 else 1.2, 0.24, h, size=8.5,
             font=T.LABEL_FONT, color=T.PURPLE, align=L if j == 0 else R)
    step = min(0.31, 3.45 / len(c['rows']))
    for i, (lbl, a, b, strong) in enumerate(c['rows']):
        y = 1.56 + i * step
        rect(s, 0.8, y - 0.02, 4.9, 0.01, fill=T.BORDER)
        f = T.TITLE_FONT if strong else T.BODY_FONT
        text(s, 0.8, y, 2.4, step - 0.02, lbl, size=8.5, font=T.LABEL_FONT if strong else T.BODY_FONT, anchor=MID)
        for j, v in enumerate((a, b)):
            text(s, 3.2 + j * 1.3, y, 1.2, step - 0.02, v, size=9, font=f, color=T.DEEP if strong else T.INK, align=R,
                 anchor=MID)
    card(s, 6.1, 1.2, 3.3, 3.95, radius=0.16)
    text(s, 6.3, 1.32, 2.9, 0.26, c['assump_title'], size=10.5, font=T.TITLE_FONT)
    step = min(0.42, 3.4 / len(c['assumptions']))
    for i, a in enumerate(c['assumptions']):
        y = 1.7 + i * step
        oval(s, 6.32, y + 0.1, 0.07, fill=T.PURPLE)
        text(s, 6.5, y, 2.8, step, a, size=8, color=T.INK, spacing=1.0)
    notes(s, c['notes'])
