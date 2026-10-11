"""Slides specific to the ITEC SEA 2026 final (v3) edition. Visual base = v2 (slides_itec2.py), same helpers.
Imported after build_deck_itec3.py swaps deck.content for deck.content_itec3."""
from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import slides as S
from . import slides_dsc as D
from . import theme as T
from .helpers import (C, MID, R, text, title, rect, card, oval, pic, icon, icon_circle, num_circle, chip, arrow_chips, notes)
from .slides_itec2 import TAG_STYLE


def _art_row(s, x, y, d, gap=0.1):
    """Real sheets colored by children in the TPA pilot (QR/access codes cropped out)."""
    for i, a in enumerate(K.PILOT_ART):
        pic(s, a, x + i * (d + gap), y, w=d, h=d, alt='Artwork colored by a child in the Scanvas TPA pilot')
    return x + len(K.PILOT_ART) * (d + gap) - gap


def _flow(s, t, x, y, w, h=0.34, bg=T.LAV2, fg=T.DEEP, size=8.5):
    rect(s, x, y, w, h, fill=bg, radius=h / 2)
    text(s, x, y, w, h, t, size=size, font=T.LABEL_FONT, color=fg, align=C, anchor=MID)


def s_cover(s):
    c = K.SLIDE_1_COVER
    S.s1_cover(s)
    text(s, 0.6, 4.72, 3.7, 0.24, c['proof'], size=7.5, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)


def s_problem(s):
    c = K.SLIDE_PROBLEM
    title(s, c['title'], 0.6, 0.38, 8.8, 0.9, size=23)
    for i, (head, sub, loop, img) in enumerate(c['cards']):
        x = 0.6 + i * 4.5
        card(s, x, 1.38, 4.3, 2.3, radius=0.18)
        if img:
            pic(s, img, x + 0.2, 1.53, w=1.62, alt='Child coloring a Scanvas sheet')
        else:
            rect(s, x + 0.2, 1.53, 1.62, 1.41, fill=T.SLATE2, radius=0.12)
            rect(s, x + 0.68, 1.66, 0.66, 1.15, fill=T.WHITE, line=T.GRAY, radius=0.08, lw=2)
            icon(s, 'monitor-play', 'gray', x + 0.79, 2.03, 0.44)
        text(s, x + 2.0, 1.55, 2.15, 0.3, head, size=14, font=T.TITLE_FONT)
        text(s, x + 2.0, 1.9, 2.15, 1.0, sub, size=10, color=T.BODY, spacing=1.12)
        arrow_chips(s, loop, x + 0.2, 3.14, h=0.34, size=9, bg=T.LAV2 if i == 0 else T.SLATE2,
                    fg=T.DEEP if i == 0 else T.MUTED, last=(T.WHITE, T.MUTED) if i == 0 else None,
                    arrow='purple' if i == 0 else 'gray')
    # evidence strip: what we have tested (real pilot artwork)
    card(s, 0.6, 3.83, 8.8, 0.78, radius=0.14)
    icon_circle(s, 'flask-conical', 0.76, 3.99, 0.46)
    text(s, 1.35, 3.95, 3.9, 0.22, c['evidence_label'], size=8, font=T.LABEL_FONT, color=T.PURPLE)
    text(s, 1.35, 4.17, 3.9, 0.3, c['evidence'], size=12, font=T.TITLE_FONT)
    text(s, 5.3, 3.9, 1.35, 0.64, c['evidence_art'], size=7.5, color=T.BODY, align=R, anchor=MID,
         spacing=1.0)
    _art_row(s, 6.73, 3.9, 0.64, gap=0.03)
    # closing question
    text(s, 0.6, 4.73, 8.8, 0.4, c['closing'], size=13.5, font=T.TITLE_FONT, color=T.PURPLE, anchor=MID)
    notes(s, c['notes'])


def s_solution(s):
    c = K.SLIDE_4_SOLUTION
    S.s4_solution(s)
    qy = c.get('qr_y', 0.42)
    rect(s, 8.5, qy, 0.9, 0.9, fill=T.WHITE, line=T.BORDER, radius=0.1, lw=0.75)
    qr, _, _ = pic(s, T.ASSETS / c['qr'], 8.55, qy + 0.05, w=0.8, h=0.8, alt='QR code to the Scanvas digital trial')
    qr.click_action.hyperlink.address = c['qr_url']
    chip(s, c['qr_label'], 8.95, qy + 0.97, bg=T.PURPLE, fg=T.WHITE, size=7.5, h=0.24, align='c')
    rect(s, 0.86, 4.9, 8.28, 0.38, fill=T.LAV2, radius=0.19)
    text(s, 0.86, 4.9, 8.28, 0.38, c['usp'], size=11, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)


def s_traction(s):
    """Same content as slides_dsc.s_traction, re-laid out: metrics + feedback left, real pilot photos right."""
    c = K.SLIDE_TRACTION
    title(s, c['title'], 0.6, 0.45, c['title_w'], 0.7, size=c['title_size'])
    step = 4.5 / len(c['metrics'])
    for i, (v, lbl) in enumerate(c['metrics']):
        x, w = 0.6 + i * step, step - 0.12
        card(s, x, 1.4, w, 1.08, radius=0.14)
        text(s, x, 1.45, w, 0.5, v, size=26, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
        text(s, x + 0.08, 1.96, w - 0.16, 0.48, lbl, size=8, font=T.LABEL_FONT, align=C, spacing=1.0)
    arrow_chips(s, c['loop'], 0.6, 2.62, h=0.32, size=9, gap=0.24)
    card(s, 0.6, 3.1, 4.5, 2.0, radius=0.16)
    text(s, 0.8, 3.18, 4.1, 0.3, c['feedback_title'], size=11.5, font=T.TITLE_FONT, anchor=MID)
    for i, (st, f) in enumerate(c['feedback']):
        y = 3.54 + i * 0.3
        done = st == 'shipped'
        chip(s, c['status_label'][st], 0.8, y, bg=T.MINT if done else T.LAV2, fg=T.GREEN if done else T.DEEP,
             size=7.5, h=0.26, w=0.9)
        text(s, 1.85, y - 0.02, 3.1, 0.3, f, size=9.5, anchor=MID)
    # real pilot photos (16:9): scan demo large, coloring moments below cropped to 4:3
    big, *small = c['photos']
    pic(s, big, 5.3, 1.4, w=4.1, h=4.1 * 9 / 16, alt='Scanvas demo with children during the TPA pilot')
    sw = (4.1 - 0.1 * (len(small) - 1)) / len(small)
    for i, p in enumerate(small):
        ph, _, _ = pic(s, p, 5.3 + i * (sw + 0.1), 3.79, w=sw, h=sw * 3 / 4,
                       alt='Children coloring Scanvas sheets in the pilot')
        ph.crop_left = ph.crop_right = (1 - (4 / 3) / (16 / 9)) / 2
    text(s, 5.3, 4.86, 4.1, 0.24, c['photo_caption'], size=8, font=T.LABEL_FONT, color=T.PURPLE, anchor=MID)
    notes(s, c['notes'])


def s_tech(s):
    c = K.SLIDE_7_DIFFERENT
    title(s, c['title'], 0.75, 0.4, 8.5, 0.5, size=24)
    text(s, 0.75, 0.92, 8.5, 0.3, c['sub'], size=11, color=T.BODY)
    oval(s, 3.85, 1.6, 2.3, fill=T.LAV2)
    pic(s, 'ph_world.png', 4.1, 1.38, h=3.1, alt='The scanned whale swimming in the Ocean world on a phone')
    for i, (h, d) in enumerate(c['items']):
        x = 0.75 if i % 2 == 0 else 6.3
        y = 1.42 + (i // 2) * 1.6
        card(s, x, y, 2.95, 1.42)
        num_circle(s, i + 1, x + 0.2, y + 0.18, 0.4, size=12.5)
        text(s, x + 0.72, y + 0.14, 2.1, 0.48, h, size=12, font=T.TITLE_FONT, anchor=MID, spacing=0.95)
        text(s, x + 0.2, y + 0.7, 2.6, 0.66, d, size=9.5, color=T.BODY, spacing=1.12)
    # differentiators strip
    w, gap = 2.06, 0.08
    for i, (ic, lbl) in enumerate(c['diffs']):
        x = 0.75 + i * (w + gap)
        rect(s, x, 4.72, w, 0.44, fill=T.PURPLE if i == 0 else T.WHITE, line=None if i == 0 else T.BORDER,
             radius=0.22, lw=0.75)
        icon(s, ic, 'white' if i == 0 else 'purple', x + 0.16, 4.83, 0.22)
        text(s, x + 0.45, 4.72, w - 0.5, 0.44, lbl, size=8.5, font=T.LABEL_FONT,
             color=T.WHITE if i == 0 else T.DEEP, anchor=MID)
    notes(s, c['notes'])


def s_repeat(s):
    c = K.SLIDE_REPEAT
    title(s, c['title'], 0.6, 0.4, 8.8, 0.5, size=24)
    text(s, 0.6, 0.92, 8.3, 0.5, c['lead'], size=11, color=T.BODY, spacing=1.1)
    widths, gap, top, h = [2.6, 3.4, 2.4], 0.2, 1.58, 3.18
    x = 0.6
    for i, (tag, style, head, flow, body, blabel, btext) in enumerate(c['cols']):
        w = widths[i]
        hi = i == 1
        tbg, tfg, tl = TAG_STYLE[style]
        if hi:
            rect(s, x, top, w, h, fill=T.LAV2, line=T.PURPLE, radius=0.18, lw=1.5)
        else:
            card(s, x, top, w, h, radius=0.18)
        chip(s, tag, x + 0.18, top + 0.16, bg=tbg, fg=tfg, size=7.5, h=0.26, line=tl)
        text(s, x + 0.18, top + 0.5, w - 0.36, 0.36, head, size=15, font=T.TITLE_FONT)
        _flow(s, flow, x + 0.14, top + 0.92, w - 0.28, bg=T.WHITE if hi else T.LAV2, size=8 if hi else 8.5)
        y = top + 1.36
        if style == 'future':
            for j, it in enumerate(body):
                icon(s, 'arrow-right', 'purple', x + 0.2, y + j * 0.245 + 0.05, 0.14)
                text(s, x + 0.42, y + j * 0.245, w - 0.6, 0.24, it, size=9.5, anchor=MID)
        else:
            text(s, x + 0.18, y, w - 0.36, 0.9, body, size=9.5, color=T.BODY, spacing=1.12)
        by = top + h - 0.72
        rect(s, x + 0.14, by, w - 0.28, 0.58, fill=T.WHITE if hi else T.LAV, radius=0.1)
        text(s, x + 0.26, by + 0.05, w - 0.5, 0.18, blabel, size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.26, by + 0.23, w - 0.5, 0.34, btext, size=8.5, font=T.LABEL_FONT, spacing=1.0)
        if i < 2:
            rect(s, x + w + 0.04, top + h / 2 - 0.13, 0.12, 0.26, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
        x += w + gap
    icon(s, 'palette', 'purple', 0.6, 4.88, 0.24)
    text(s, 0.92, 4.84, 8.4, 0.32, c['footer'], size=10.5, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
    notes(s, c['notes'])


def s_business(s):
    c = K.SLIDE_BUSINESS
    title(s, c['title'], 0.6, 0.38, 8.8, 0.5, size=24)
    text(s, 0.6, 0.9, 8.8, 0.3, c['lead'], size=11, color=T.BODY)
    w, gap, top = 2.8, 0.2, 1.3
    bottom = 4.55 if c.get('pricing') else 5.2
    for i, (tag, style, head, offer, model, llabel, items) in enumerate(c['paths']):
        x = 0.6 + i * (w + gap)
        tbg, tfg, tl = TAG_STYLE[style]
        card(s, x, top, w, bottom - top, radius=0.16)
        chip(s, tag, x + 0.18, top + 0.15, bg=tbg, fg=tfg, size=7.5, h=0.26, line=tl)
        text(s, x + 0.18, top + 0.5, w - 0.36, 0.32, head, size=13, font=T.TITLE_FONT)
        text(s, x + 0.18, top + 0.86, w - 0.36, 0.58, offer, size=8.5, color=T.BODY, spacing=1.08)
        rect(s, x + 0.14, top + 1.48, w - 0.28, 0.58, fill=T.LAV, radius=0.1)
        text(s, x + 0.24, top + 1.52, w - 0.48, 0.18, 'Revenue model', size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.24, top + 1.7, w - 0.48, 0.34, model, size=8.5, font=T.LABEL_FONT, spacing=1.0)
        text(s, x + 0.18, top + 2.16, w - 0.36, 0.2, llabel, size=7, font=T.LABEL_FONT, color=T.PURPLE)
        step = min(0.26, (bottom - top - 2.5) / len(items))
        for j, it in enumerate(items):
            y = top + 2.38 + j * step
            icon(s, 'check' if style == 'live' else 'arrow-right', 'purple', x + 0.2, y + 0.04, 0.14)
            text(s, x + 0.42, y, w - 0.6, 0.22, it, size=8.5, anchor=MID)
    if c.get('pricing'):
        head, body = c['pricing']
        rect(s, 0.6, 4.68, 8.8, 0.5, fill=T.PALEY, radius=0.12)
        text(s, 0.8, 4.68, 4.2, 0.5, head, size=8, font=T.LABEL_FONT, color=T.AMBER_DARK, anchor=MID)
        text(s, 5.0, 4.68, 4.25, 0.5, body, size=10, font=T.TITLE_FONT, color=T.INK, anchor=MID)
    notes(s, c['notes'])


def s_market(s):
    c = K.SLIDE_MARKET
    title(s, c['title'], 0.6, 0.38, 8.8, 0.45, size=20)
    # initial customer strip
    card(s, 0.6, 0.98, 8.8, 0.82, radius=0.14)
    chip(s, c['icp_label'], 0.75, 1.25, bg=T.PURPLE, fg=T.WHITE, size=7.5, h=0.28, ic=('target', 'white'))
    cols = [(2.66, 2.3), (5.1, 0.85), (6.08, 1.3), (7.5, 1.85)]
    for (x, w), (lbl, v) in zip(cols, c['icp']):
        rect(s, x - 0.1, 1.1, 0.01, 0.58, fill=T.BORDER)
        text(s, x, 1.1, w, 0.18, lbl, size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x, 1.3, w, 0.42, v, size=8.5, font=T.LABEL_FONT if lbl != 'Buyer' else T.BODY_FONT,
             color=T.DEEP if lbl.endswith('cquisition loop') else T.INK, spacing=1.0)
    # geography staircase
    w, gap = 2.05, 0.2
    for i, (stage, geo, value, unit, desc) in enumerate(c['stages']):
        x = 0.6 + i * (w + gap)
        top = 2.42 - i * 0.14
        last = i == len(c['stages']) - 1
        fill = [T.PURPLE, T.LAV2, T.WHITE, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, top, w, 4.62 - top, fill=fill, line=T.BORDER if i >= 2 else None, radius=0.16, lw=0.75)
        chip(s, stage, x + 0.16, top + 0.14, bg=T.WHITE if i == 0 else T.LAV2, fg=T.DEEP, size=7.5, h=0.26)
        text(s, x + 0.16, top + 0.46, w - 0.3, 0.24, geo, size=10, font=T.LABEL_FONT, color=fg)
        text(s, x + 0.16, top + 0.72, w - 0.3, 0.46, value, size=23, font=T.TITLE_FONT,
             color=T.WHITE if i == 0 else (T.PURPLE if last else T.DEEP))
        text(s, x + 0.16, top + 1.18, w - 0.3, 0.2, unit, size=8, font=T.LABEL_FONT,
             color=T.LAV2 if i == 0 else T.BODY)
        text(s, x + 0.16, top + 1.42, w - 0.3, 0.6, desc, size=8.5, color=T.WHITE if i == 0 else T.BODY,
             spacing=1.08)
        if i < 3:
            rect(s, x + w + 0.04, 3.45, 0.12, 0.26, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    text(s, 0.6, 4.7, 8.8, 0.3, c['footer'], size=9, font=T.LABEL_FONT, color=T.DEEP, spacing=1.0)
    text(s, 0.6, 5.02, 8.8, 0.22, c['source'], size=6.5, color=T.BODY)
    notes(s, c['notes'])


def s_culture(s):
    c = K.SLIDE_CULTURE
    title(s, c['title'], 0.6, 0.4, 8.8, 0.5, size=24)
    w, gap, top, h = 2.7, 0.35, 1.08, 2.3
    for i, (step, head, desc, chips, ic) in enumerate(c['layers']):
        x = 0.6 + i * (w + gap)
        fill = [T.WHITE, T.LAV2, T.PURPLE][i]
        fg = T.WHITE if i == 2 else T.INK
        rect(s, x, top, w, h, fill=fill, line=T.BORDER if i == 0 else None, radius=0.18, lw=0.75)
        icon_circle(s, ic, x + 0.18, top + 0.16, 0.44, bg=T.WHITE if i else T.LAV2, ic='purple')
        chip(s, step, x + 0.72, top + 0.24, bg=T.LAV2 if i != 1 else T.WHITE, fg=T.DEEP, size=8, h=0.28)
        text(s, x + 0.18, top + 0.72, w - 0.36, 0.3, head, size=13, font=T.TITLE_FONT, color=fg)
        text(s, x + 0.18, top + 1.04, w - 0.36, 0.42, desc, size=9.5, color=T.WHITE if i == 2 else T.BODY,
             spacing=1.08)
        cx, cy = x + 0.18, top + 1.5
        for ch in chips:
            cw = len(ch) * 7.5 * 0.62 / 72 + 0.3
            if cx + cw > x + w - 0.15:
                cx, cy = x + 0.18, cy + 0.27
            chip(s, ch, cx, cy, bg=T.WHITE if i else T.LAV, fg=T.DEEP, size=7.5, h=0.23, w=cw)
            cx += cw + 0.06
        if i < 2:
            rect(s, x + w + 0.1, top + h / 2 - 0.15, 0.15, 0.3, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    # regional row: hypotheses to validate through ITEC
    ry, rh = 3.55, 1.12
    rect(s, 0.6, ry, 8.8, rh, fill=T.LAV, line=T.BORDER, radius=0.16, lw=0.75)
    icon_circle(s, 'globe', 0.75, ry + 0.16, 0.4, bg=T.LAV2)
    text(s, 1.22, ry + 0.14, 1.55, 0.44, c['region_title'], size=9, font=T.TITLE_FONT, spacing=0.95)
    chip(s, c['region_tag'], 0.75, ry + 0.68, bg=T.PALEY, fg=T.AMBER_DARK, size=6.5, h=0.3, w=2.02)
    rw, rx0 = 2.07, 2.93
    for i, (region, desc) in enumerate(c['regions']):
        x = rx0 + i * (rw + 0.08)
        card(s, x, ry + 0.12, rw, rh - 0.24, radius=0.12)
        text(s, x + 0.14, ry + 0.2, rw - 0.28, 0.22, region, size=9, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.14, ry + 0.42, rw - 0.28, 0.46, desc, size=8, color=T.BODY, spacing=1.05)
    rect(s, 0.6, 4.8, 8.8, 0.4, fill=T.LAV2, radius=0.2)
    text(s, 0.6, 4.8, 8.8, 0.4, c['closing'], size=12.5, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
    notes(s, c['notes'])


def s_next(s):
    c = K.SLIDE_NEXT
    title(s, c['title'], 0.6, 0.36, 8.8, 0.72, size=20)
    w, gap, top, h = 2.1, 0.133, 1.2, 2.88
    for i, (tag, head, desc, items, ic, blabel, btext) in enumerate(c['stages']):
        x = 0.6 + i * (w + gap)
        fill = [T.PURPLE, T.LAV2, T.WHITE, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, top, w, h, fill=fill, line=T.BORDER if i >= 2 else None, radius=0.16, lw=0.75)
        chip(s, tag, x + 0.15, top + 0.14, bg=T.WHITE if i == 0 else (T.WHITE if i == 1 else T.LAV2), fg=T.DEEP,
             size=7.5, h=0.26)
        text(s, x + 0.15, top + 0.48, w - 0.3, 0.3, head, size=12, font=T.TITLE_FONT, color=fg)
        y = top + 0.8
        if desc:
            text(s, x + 0.15, y, w - 0.3, 0.4, desc, size=8.5, color=T.LAV2 if i == 0 else T.BODY, spacing=1.05)
            y += 0.46
        for j, it in enumerate(items):
            yy = y + j * 0.25
            icon(s, ic, 'white' if i == 0 else 'purple', x + 0.15, yy + 0.04, 0.15)
            text(s, x + 0.37, yy, w - 0.5, 0.23, it, size=8.5, color=fg, anchor=MID)
        if blabel:
            bh = 0.95 if i == 1 else 0.62
            by = top + h - bh - 0.12
            rect(s, x + 0.12, by, w - 0.24, bh, fill=T.WHITE if i < 2 else T.LAV, radius=0.1)
            text(s, x + 0.22, by + 0.06, w - 0.44, 0.18, blabel, size=7, font=T.LABEL_FONT, color=T.PURPLE)
            text(s, x + 0.22, by + 0.24, w - 0.44, bh - 0.28, btext, size=8, font=T.LABEL_FONT, spacing=1.0)
    # one engine -> many paths (full width when the ask has its own slide, as in the itec4 edition)
    if not c['ask']:
        rect(s, 0.6, 4.3, 8.8, 0.6, fill=T.PURPLE, radius=0.16)
        icon(s, 'layers', 'white', 0.82, 4.45, 0.3)
        text(s, 1.25, 4.3, 8.0, 0.6, c['engine'], size=12, font=T.TITLE_FONT, color=T.WHITE, anchor=MID)
        notes(s, c['notes'])
        return
    rect(s, 0.6, 4.22, 2.9, 0.96, fill=T.PURPLE, radius=0.16)
    icon(s, 'layers', 'white', 0.78, 4.4, 0.3)
    text(s, 1.18, 4.22, 2.2, 0.96, c['engine'], size=10, font=T.TITLE_FONT, color=T.WHITE, anchor=MID, spacing=1.0)
    # ITEC ask
    rect(s, 3.65, 4.22, 5.75, 0.96, fill=T.LAV2, radius=0.16)
    text(s, 3.82, 4.28, 5.4, 0.2, c['ask_title'], size=8, font=T.LABEL_FONT, color=T.DEEP)
    for j, (ic, a) in enumerate(c['ask']):
        x = 3.82 + (j % 2) * 2.78
        y = 4.52 + (j // 2) * 0.3
        icon(s, ic, 'purple', x, y + 0.04, 0.18)
        text(s, x + 0.25, y, 2.5, 0.26, a, size=8.5, font=T.LABEL_FONT, anchor=MID)
    notes(s, c['notes'])


def s_competition(s):
    c = K.SLIDE_COMPETITION
    D.s_competition(s)
    y = 1.35 + 0.62 + len(c['rows']) * 0.33
    rect(s, 0.6, y, 8.8, 0.5, fill=T.LAV2, radius=0.12)
    text(s, 0.78, y, 8.45, 0.5, c['statement'], size=9, font=T.LABEL_FONT, color=T.INK, anchor=MID, spacing=1.0)
    text(s, 0.6, y + 0.56, 8.8, 0.22, c['source'], size=7.5, color=T.BODY)


def s_pipeline(s):
    c = K.SLIDE_PIPELINE
    title(s, c['title'], 0.6, 0.38, 8.8, 0.72, size=20)
    n = len(c['steps'])
    w, gap, top, h = 1.14, 0.12, 1.25, 2.25
    for i, (head, lines, ic) in enumerate(c['steps']):
        x = 0.6 + i * (w + gap)
        hi = i in (2, 4)
        card(s, x, top, w, h, fill=T.LAV2 if hi else T.WHITE, radius=0.14)
        num_circle(s, i + 1, x + 0.1, top + 0.12, 0.3, size=9)
        icon_circle(s, ic, x + w - 0.44, top + 0.1, 0.34, bg=T.WHITE if hi else T.LAV2)
        text(s, x + 0.1, top + 0.54, w - 0.16, 0.44, head, size=9.5, font=T.TITLE_FONT, spacing=0.95)
        y = top + 1.0
        for ln in lines:
            nl = 1 + int(len(ln) * 8 * 0.5 / 72 / (w - 0.2))
            text(s, x + 0.1, y, w - 0.16, nl * 0.15, ln, size=8, color=T.BODY, spacing=1.0)
            y += nl * 0.15 + 0.1
        if i < n - 1:
            rect(s, x + w + 0.02, top + h / 2 - 0.09, 0.08, 0.18, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    # responsible child data + validation principle
    by, bh = 3.68, 1.5
    card(s, 0.6, by, 4.3, bh, radius=0.16)
    icon_circle(s, 'shield-check', 0.76, by + 0.16, 0.42)
    text(s, 1.3, by + 0.2, 3.4, 0.34, c['privacy_title'], size=11, font=T.TITLE_FONT, anchor=MID)
    text(s, 0.78, by + 0.66, 3.95, 0.66, c['privacy'], size=9, color=T.BODY, spacing=1.1)
    rect(s, 5.1, by, 4.3, bh, fill=T.LAV2, radius=0.16)
    icon_circle(s, 'repeat', 5.26, by + 0.16, 0.42, bg=T.WHITE)
    text(s, 5.8, by + 0.2, 3.4, 0.34, c['validation_title'], size=11, font=T.TITLE_FONT, anchor=MID)
    arrow_chips(s, c['validation_flow'], 5.28, by + 0.68, h=0.26, size=7.5, gap=0.2, bg=T.WHITE, fg=T.DEEP)
    text(s, 5.28, by + 1.02, 3.95, 0.46, c['validation'], size=8.5, color=T.BODY, spacing=1.05)
    notes(s, c['notes'])
