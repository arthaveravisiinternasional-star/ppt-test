"""Slides specific to the ITEC SEA 2026 Top 30 (v2) edition. Same helpers and look as slides.py.
Imported after build_deck_itec2.py swaps deck.content for deck.content_itec2."""
from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import slides as S
from . import slides_dsc as D
from . import theme as T
from .helpers import (C, MID, text, title, rect, card, pic, icon, icon_circle, num_circle, chip, arrow_chips, notes)

TAG_STYLE = {'live': (T.MINT, T.GREEN, None), 'validating': (T.PALEY, T.AMBER_DARK, None),
             'future': (T.WHITE, T.DEEP, T.DEEP)}


def s_problem(s):
    c = K.SLIDE_PROBLEM
    title(s, c['title'], 0.6, 0.42, 8.8, 0.9, size=23)
    for i, (head, sub, loop, img) in enumerate(c['cards']):
        x = 0.6 + i * 4.5
        card(s, x, 1.55, 4.3, 3.45, radius=0.18)
        if img:
            pic(s, img, x + 0.25, 1.8, w=2.05, alt='Child coloring a Scanvas sheet')
        else:
            rect(s, x + 0.25, 1.8, 2.05, 1.79, fill=T.SLATE2, radius=0.13)
            rect(s, x + 0.86, 1.98, 0.83, 1.43, fill=T.WHITE, line=T.GRAY, radius=0.1, lw=2)
            icon(s, 'monitor-play', 'gray', x + 1.0, 2.45, 0.55)
        text(s, x + 2.5, 1.85, 1.65, 0.6, head, size=14, font=T.TITLE_FONT, spacing=0.95)
        text(s, x + 2.5, 2.5, 1.65, 1.1, sub, size=10, color=T.BODY, spacing=1.12)
        arrow_chips(s, loop, x + 0.25, 4.1, h=0.36, size=9.5,
                    bg=T.LAV2 if i == 0 else T.SLATE2, fg=T.DEEP if i == 0 else T.MUTED,
                    last=(T.WHITE, T.MUTED) if i == 0 else None, arrow='purple' if i == 0 else 'gray')
    notes(s, c['notes'])


def s_live(s):
    c = K.SLIDE_5_PRODUCT
    S.s5_product(s)
    rect(s, 3.5, 0.9, 0.8, 0.8, fill=T.WHITE, line=T.BORDER, radius=0.1, lw=0.75)
    pic(s, T.ASSETS / 'qr_scanvas.png', 3.54, 0.94, w=0.72, h=0.72, alt='QR code to scanvas.id')
    text(s, 3.25, 1.74, 1.3, 0.2, c['qr_label'], size=7, font=T.LABEL_FONT, color=T.DEEP, align=C)


def s_tech(s):
    c = K.SLIDE_7_DIFFERENT
    S.s7_different(s)


def s_culture(s):
    c = K.SLIDE_CULTURE
    title(s, c['title'], 0.6, 0.42, 8.8, 0.9, size=24)
    w, gap = 2.7, 0.35
    for i, (step, head, desc, chips, ic) in enumerate(c['layers']):
        x = 0.6 + i * (w + gap)
        fill = [T.WHITE, T.LAV2, T.PURPLE][i]
        fg = T.WHITE if i == 2 else T.INK
        rect(s, x, 1.5, w, 3.55, fill=fill, line=T.BORDER if i == 0 else None, radius=0.18, lw=0.75)
        icon_circle(s, ic, x + 0.2, 1.7, 0.5, bg=T.WHITE if i else T.LAV2, ic='purple')
        chip(s, step, x + 0.82, 1.8, bg=T.LAV2 if i != 1 else T.WHITE, fg=T.DEEP, size=8, h=0.28)
        text(s, x + 0.2, 2.4, w - 0.4, 0.55, head, size=13.5, font=T.TITLE_FONT, color=fg, spacing=0.95)
        text(s, x + 0.2, 3.0, w - 0.4, 0.6, desc, size=10, color=T.WHITE if i == 2 else T.BODY, spacing=1.1)
        cx, cy = x + 0.2, 3.85
        for ch in chips:
            cw = len(ch) * 7.5 * 0.62 / 72 + 0.3
            if cx + cw > x + w - 0.15:
                cx, cy = x + 0.2, cy + 0.3
            chip(s, ch, cx, cy, bg=T.WHITE if i else T.LAV, fg=T.DEEP, size=7.5, h=0.24, w=cw)
            cx += cw + 0.06
        if i < 2:
            rect(s, x + w + 0.1, 3.12, 0.15, 0.3, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    notes(s, c['notes'])


def s_market(s):
    c = K.SLIDE_MARKET
    title(s, c['title'], 0.6, 0.38, 8.8, 0.9, size=22)
    w, gap = 2.05, 0.2
    for i, (stage, geo, value, unit, desc) in enumerate(c['stages']):
        x = 0.6 + i * (w + gap)
        top = 2.6 - i * 0.42
        last = i == len(c['stages']) - 1
        fill = [T.PURPLE, T.LAV2, T.WHITE, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, top, w, 4.75 - top, fill=fill, line=T.BORDER if i >= 2 else None, radius=0.16, lw=0.75)
        chip(s, stage, x + 0.16, top + 0.16, bg=T.WHITE if i == 0 else T.LAV2, fg=T.DEEP, size=7.5, h=0.26)
        text(s, x + 0.16, top + 0.5, w - 0.3, 0.26, geo, size=10, font=T.LABEL_FONT, color=fg)
        text(s, x + 0.16, top + 0.8, w - 0.3, 0.5, value, size=24, font=T.TITLE_FONT,
             color=T.WHITE if i == 0 else (T.PURPLE if last else T.DEEP))
        text(s, x + 0.16, top + 1.3, w - 0.3, 0.22, unit, size=8, font=T.LABEL_FONT,
             color=T.LAV2 if i == 0 else T.BODY)
        text(s, x + 0.16, top + 1.58, w - 0.3, 0.8, desc, size=8.5, color=T.WHITE if i == 0 else T.BODY,
             spacing=1.08)
    text(s, 0.6, 4.9, 8.8, 0.36, c['source'], size=7, color=T.BODY, spacing=1.05)
    notes(s, c['notes'])


def s_business(s):
    c = K.SLIDE_BUSINESS
    title(s, c['title'], 0.6, 0.35, 8.8, 0.9, size=22)
    w, gap = 2.8, 0.2
    for i, (tag, style, head, desc, model, flow) in enumerate(c['paths']):
        x = 0.6 + i * (w + gap)
        tbg, tfg, tl = TAG_STYLE[style]
        card(s, x, 1.25, w, 3.95, radius=0.16)
        chip(s, tag, x + 0.18, 1.42, bg=tbg, fg=tfg, size=7.5, h=0.26, line=tl)
        text(s, x + 0.18, 1.8, w - 0.36, 0.34, head, size=13, font=T.TITLE_FONT)
        text(s, x + 0.18, 2.18, w - 0.36, 0.72, desc, size=8.5, color=T.BODY, spacing=1.08)
        rect(s, x + 0.14, 2.95, w - 0.28, 0.62, fill=T.LAV, radius=0.1)
        text(s, x + 0.24, 2.98, w - 0.48, 0.2, 'Revenue model', size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.24, 3.16, w - 0.48, 0.4, model, size=8.5, font=T.LABEL_FONT, color=T.INK, spacing=1.0)
        text(s, x + 0.18, 3.72, w - 0.36, 0.2, 'How we reach them' if i < 2 else 'How it grows', size=7,
             font=T.LABEL_FONT, color=T.PURPLE)
        for j, f in enumerate(flow):
            y = 3.96 + j * 0.24
            icon(s, 'arrow-right', 'purple', x + 0.2, y + 0.04, 0.14)
            text(s, x + 0.42, y, w - 0.6, 0.22, f, size=8.5, anchor=MID)
    notes(s, c['notes'])


def s_next(s):
    c = K.SLIDE_NEXT
    title(s, c['title'], 0.6, 0.38, 8.8, 0.55, size=19)
    for i, (ph, head, items) in enumerate(c['phases']):
        x = 0.6 + i * 2.97
        fill = [T.PURPLE, T.LAV2, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, 1.08, 2.8, 1.95, fill=fill, line=T.BORDER if i == 2 else None, radius=0.16, lw=0.75)
        text(s, x + 0.18, 1.16, 2.4, 0.2, ph, size=7.5, font=T.LABEL_FONT, color=T.LAV2 if i == 0 else T.PURPLE)
        text(s, x + 0.18, 1.36, 2.4, 0.32, head, size=12.5, font=T.TITLE_FONT, color=fg)
        for j, it in enumerate(items):
            y = 1.76 + j * 0.3
            icon(s, 'check' if i == 0 else 'arrow-right', 'white' if i == 0 else 'purple', x + 0.18, y + 0.05,
                 0.16)
            text(s, x + 0.42, y, 2.3, 0.26, it, size=8.5, color=fg, anchor=MID)
    # team
    card(s, 0.6, 3.22, 5.1, 1.95, radius=0.16)
    boxes = {'founder_sk.png': (0.06, 1.16), 'founder_hh.png': (0.0, 1.26)}
    for i, (name, role, focus, photo) in enumerate(c['team']):
        y = 3.3 + i * 0.93
        dx, pw = boxes[photo]
        pic(s, photo, 0.72 + dx, y, h=0.86, alt=name)
        text(s, 1.72, y + 0.04, 3.9, 0.26, name, size=11, font=T.TITLE_FONT)
        text(s, 1.72, y + 0.3, 3.9, 0.22, role, size=9, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, 1.72, y + 0.52, 3.9, 0.3, focus, size=8, color=T.BODY)
    # closing
    rect(s, 5.9, 3.22, 3.5, 1.95, fill=T.LAV2, radius=0.16)
    icon(s, 'quote', 'deep', 6.08, 3.36, 0.3)
    text(s, 6.08, 3.72, 3.15, 0.95, c['closing'], size=11.5, font=T.TITLE_FONT, color=T.INK, spacing=1.05)
    text(s, 6.08, 4.7, 3.15, 0.36, c['itec'], size=8, font=T.LABEL_FONT, color=T.DEEP, spacing=1.0)
    notes(s, c['notes'])


def s_pipeline(s):
    c = K.SLIDE_PIPELINE
    title(s, c['title'], 0.6, 0.42, 8.8, 0.8, size=20)
    n = len(c['steps'])
    w, gap = 1.14, 0.12
    for i, (head, lines, ic) in enumerate(c['steps']):
        x = 0.6 + i * (w + gap)
        hi = i in (2, 4)
        card(s, x, 1.45, w, 3.6, fill=T.LAV2 if hi else T.WHITE, radius=0.14)
        num_circle(s, i + 1, x + 0.12, 1.6, 0.32, size=9.5)
        icon_circle(s, ic, x + w - 0.48, 1.57, 0.38, bg=T.WHITE if hi else T.LAV2)
        text(s, x + 0.12, 2.1, w - 0.2, 0.55, head, size=10.5, font=T.TITLE_FONT, spacing=0.95)
        for j, ln in enumerate(lines):
            text(s, x + 0.12, 2.75 + j * 0.5, w - 0.2, 0.46, ln, size=9, color=T.BODY, spacing=1.0)
        if i < n - 1:
            rect(s, x + w + 0.02, 3.1, 0.08, 0.18, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    notes(s, c['notes'])
