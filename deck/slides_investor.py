"""Slides for the SCANVAS investor deck (October 2026), Freesia template, 10 x 5.625 in grid.
Imported after build_deck_investor.py swaps deck.content for deck.content_investor."""
import math

from PIL import Image
from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import theme as T
from .helpers import (L, C, MID, R, text, title, rect, card, oval, pic, icon, icon_circle, num_circle, chip, img_size,
                      arrow_chips, notes)

STATUS = {'live': (T.MINT, T.GREEN), 'validating': (T.PALEY, T.AMBER_DARK), 'pilot': (T.PALEY, T.AMBER_DARK),
          'future': (T.LAV2, T.DEEP), 'planned': (T.LAV2, T.DEEP)}


def _lines(t, size, w, k=0.5):
    return max(1, math.ceil(len(t) * size * k / 72 / w))


def _bullets(s, items, x, y, w, step, size=9.5, ic='check', color='purple', fg=T.INK):
    for i, it in enumerate(items):
        yy = y + i * step
        icon(s, ic, color, x, yy + 0.05, 0.15)
        text(s, x + 0.22, yy, w - 0.22, step, it, size=size, color=fg, spacing=1.0)


def _qr(s, x, y, d):
    qr, _, _ = pic(s, T.ASSETS / K.SLIDE_4_SOLUTION['qr'], x, y, w=d, h=d, alt='QR code to the Scanvas digital trial')
    qr.click_action.hyperlink.address = K.SLIDE_4_SOLUTION['qr_url']


# ---------------------------------------------------------------- 2
def s_problem(s):
    c = K.PROBLEM
    title(s, c['title'], 0.6, 0.4, 8.8, 0.8, size=21)
    for i, (who, ic, need, today) in enumerate(c['buyers']):
        x = 0.6 + i * 4.5
        card(s, x, 1.38, 4.3, 2.05, radius=0.16)
        icon_circle(s, ic, x + 0.18, 1.52, 0.44)
        text(s, x + 0.75, 1.6, 3.3, 0.28, who, size=11, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
        text(s, x + 0.2, 2.05, 3.9, 0.18, 'NEEDS', size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.2, 2.23, 3.9, 0.55, need, size=10.5, font=T.LABEL_FONT, spacing=1.05)
        text(s, x + 0.2, 2.8, 3.9, 0.18, 'TODAY', size=7, font=T.LABEL_FONT, color=T.BODY)
        text(s, x + 0.2, 2.98, 3.9, 0.42, today, size=9.5, color=T.BODY, spacing=1.05)
    for j, (lbl, items, fill, fg) in enumerate([(c['observed_title'], c['observed'], T.MINT, T.GREEN),
                                                (c['assumed_title'], c['assumed'], T.PALEY, T.AMBER_DARK)]):
        x = 0.6 + j * 4.5
        rect(s, x, 3.58, 4.3, 1.4, fill=fill, radius=0.16)
        text(s, x + 0.2, 3.68, 3.9, 0.2, lbl, size=7.5, font=T.LABEL_FONT, color=fg)
        _bullets(s, items, x + 0.2, 3.95, 3.95, 0.48, size=9.5, ic='check' if j == 0 else 'flask-conical',
                 color='green' if j == 0 else 'yellow')
    notes(s, c['notes'])


# ---------------------------------------------------------------- 3
def s_product(s):
    c = K.PRODUCT
    title(s, c['title'], 0.6, 0.4, 7.4, 0.8, size=21)
    tw, gap, ty, th = 1.6, 0.22, 1.4, 1.75
    for i, (lbl, cap, img, fit) in enumerate(c['steps']):
        x = 0.6 + i * (tw + gap)
        card(s, x, ty, tw, th)
        w, h = img_size(img, w=tw - 0.06) if fit == 'w' else img_size(img, h=th - 0.1)
        if h > th - 0.1:
            w, h = img_size(img, h=th - 0.1)
        pic(s, img, x + (tw - w) / 2, ty + (th - h) / 2, w=w, h=h, alt=f'{lbl} step')
        num_circle(s, i + 1, x - 0.08, ty - 0.12, 0.34, size=11)
        text(s, x, ty + th + 0.12, tw, 0.28, lbl, size=13, font=T.TITLE_FONT, color=T.DEEP)
        text(s, x, ty + th + 0.42, tw, 0.5, cap, size=9.5, color=T.BODY, spacing=1.05)
        if i < 3:
            rect(s, x + tw + 0.06, ty + th / 2 - 0.13, 0.1, 0.26, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    rect(s, 8.15, 0.42, 1.25, 1.25, fill=T.WHITE, line=T.BORDER, radius=0.12, lw=0.75)
    _qr(s, 8.22, 0.49, 1.11)
    chip(s, c['qr_label'], 8.775, 1.72, bg=T.PURPLE, fg=T.WHITE, size=7, h=0.22, align='c')
    cx = 0.6
    for lbl in c['live']:
        _, w = chip(s, lbl, cx, 4.82, bg=T.MINT, fg=T.GREEN, size=8, h=0.28, ic=('check', 'green'))
        cx += w + 0.1
    notes(s, c['notes'])


# ---------------------------------------------------------------- 4
def s_traction(s):
    c = K.TRACTION
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    mw = (5.0 - 0.3) / 4
    for i, (v, lbl) in enumerate(c['metrics']):
        x = 0.6 + i * (mw + 0.1)
        card(s, x, 1.05, mw, 1.0, radius=0.14)
        text(s, x, 1.09, mw, 0.46, v, size=22 if len(v) > 3 else 26, font=T.TITLE_FONT, color=T.DEEP, align=C,
             anchor=MID)
        text(s, x + 0.06, 1.55, mw - 0.12, 0.48, lbl, size=8, font=T.LABEL_FONT, align=C, spacing=1.0)
    card(s, 0.6, 2.17, 5.0, 1.2, radius=0.14)
    for j, (head, items, done) in enumerate([('SHIPPED', c['shipped'], True), ('BUILDING', c['building'], False)]):
        x = 0.78 + j * 2.45
        chip(s, head, x, 2.28, bg=T.MINT if done else T.LAV2, fg=T.GREEN if done else T.DEEP, size=7.5, h=0.24)
        _bullets(s, items, x, 2.6, 2.3, 0.25, size=9, ic='check' if done else 'arrow-right',
                 color='green' if done else 'purple')
    for j, (lbl, items, fill, fg) in enumerate([(c['proved_title'], c['proved'], T.MINT, T.GREEN),
                                                (c['next_title'], c['next'], T.PALEY, T.AMBER_DARK)]):
        x = 0.6 + j * 2.55
        rect(s, x, 3.5, 2.45, 1.65, fill=fill, radius=0.14)
        text(s, x + 0.14, 3.58, 2.17, 0.2, lbl, size=7, font=T.LABEL_FONT, color=fg)
        _bullets(s, items, x + 0.14, 3.82, 2.17, 0.32, size=8.5, ic='check' if j == 0 else 'arrow-right',
                 color='green' if j == 0 else 'yellow')
    pic(s, c['photo'], 5.8, 1.05, w=3.6, h=3.6 * 9 / 16, alt='Scanvas demo with children during the TPA pilot')
    for i, a in enumerate(K.PILOT_ART):
        pic(s, a, 5.8 + i * 0.92, 3.17, w=0.84, h=0.84, alt='Artwork colored by a child in the pilot')
    text(s, 5.8, 4.08, 3.6, 0.36, c['caption'], size=8, font=T.LABEL_FONT, color=T.PURPLE, spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 5
def s_market(s):
    c = K.MARKET
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    card(s, 0.6, 1.05, 5.1, 2.35, radius=0.16)
    text(s, 0.78, 1.14, 4.8, 0.2, c['inst_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    for i, (lbl, v, place) in enumerate(c['inst']):
        x = 0.78 + i * 1.62
        fill = [T.PURPLE, T.LAV2, T.LAV][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, 1.42, 1.5, 1.55, fill=fill, radius=0.14)
        chip(s, lbl, x + 0.12, 1.52, bg=T.WHITE if i == 0 else T.PURPLE, fg=T.DEEP if i == 0 else T.WHITE, size=7,
             h=0.22)
        text(s, x + 0.12, 1.84, 1.3, 0.42, v, size=20, font=T.TITLE_FONT, color=T.WHITE if i == 0 else T.DEEP,
             anchor=MID)
        text(s, x + 0.12, 2.3, 1.3, 0.6, place, size=9, font=T.LABEL_FONT, color=fg, spacing=1.0)
    text(s, 0.78, 3.04, 4.8, 0.24, c['inst_unit'], size=8.5, color=T.BODY, anchor=MID)
    rect(s, 5.9, 1.05, 3.5, 2.35, fill=T.LAV2, radius=0.16)
    text(s, 6.08, 1.14, 3.2, 0.2, c['fam_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    text(s, 6.08, 1.42, 3.2, 0.55, c['fam_value'], size=30, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
    text(s, 6.08, 2.0, 3.15, 0.4, c['fam_unit'], size=9, font=T.LABEL_FONT, spacing=1.0)
    text(s, 6.08, 2.48, 3.15, 0.8, c['fam_note'], size=9, color=T.BODY, spacing=1.05)
    card(s, 0.6, 3.52, 8.8, 1.02, radius=0.16)
    text(s, 0.78, 3.6, 5.0, 0.2, c['share_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    for i, (v, lbl) in enumerate(c['share']):
        x = 0.78 + i * 4.3
        text(s, x, 3.82, 4.1, 0.28, v, size=12, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
        text(s, x, 4.1, 4.1, 0.4, lbl, size=8.5, color=T.BODY, spacing=1.0)
    text(s, 0.6, 4.62, 8.8, 0.24, c['rule'], size=9, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
    text(s, 0.6, 4.88, 8.8, 0.3, c['source'], size=7, color=T.BODY, spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 6
def s_business(s):
    c = K.BUSINESS
    title(s, c['title'], 0.6, 0.4, 8.0, 0.8, size=21)
    card(s, 0.6, 1.25, 8.8, 3.05, radius=0.16)
    cols = [(0.8, 2.6, L), (3.45, 2.1, L), (5.6, 1.1, R), (6.75, 1.1, R), (7.9, 1.35, R)]
    for (x, w, a), h in zip(cols, c['head']):
        text(s, x, 1.36, w, 0.22, h.upper(), size=7.5, font=T.LABEL_FONT, color=T.PURPLE, align=a)
    for i, (key, status, style) in enumerate(c['offers']):
        name, price, cost, _ = K.UNITS[key]
        y = 1.68 + i * 0.64
        rect(s, 0.75, y - 0.06, 8.5, 0.01, fill=T.BORDER)
        bg, fg = STATUS[style]
        text(s, 0.8, y, 2.6, 0.52, name, size=10.5, font=T.TITLE_FONT, anchor=MID, spacing=1.0)
        chip(s, status, 3.45, y + 0.13, bg=bg, fg=fg, size=6.5, h=0.24)
        unit = ' / year' if key == 'license' else ''
        vals = [K.rpu(price) + unit, K.rpu(cost),
                f'{K.rpu(round(price - cost, 3))} · {round(100 * (price - cost) / price)}%']
        for (x, w, a), v in zip(cols[2:], vals):
            text(s, x, y, w, 0.52, v, size=10.5, font=T.TITLE_FONT if x > 7 else T.BODY_FONT,
                 color=T.DEEP if x > 7 else T.INK, align=a, anchor=MID)
    text(s, 0.6, 4.36, 8.8, 0.36, c['bundle'], size=8.5, font=T.LABEL_FONT, color=T.DEEP, spacing=1.0)
    rect(s, 0.6, 4.78, 8.8, 0.36, fill=T.PALEY, radius=0.18)
    text(s, 0.6, 4.78, 8.8, 0.36, c['footer'], size=9.5, font=T.LABEL_FONT, color=T.AMBER_DARK, align=C, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 7
def s_competition(s):
    c = K.COMPETITION
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    card(s, 0.6, 1.0, 8.8, 3.55, radius=0.16)
    lx, lw, cw = 0.78, 2.85, 1.42
    for j, (p, ex) in enumerate(zip(c['players'], c['examples'])):
        x = lx + lw + j * cw
        if j == 0:
            rect(s, x + 0.04, 1.06, cw - 0.08, 3.43, fill=T.LAV2, radius=0.1)
        text(s, x, 1.1, cw, 0.42, p, size=10.5 if j == 0 else 8.5, font=T.TITLE_FONT,
             color=T.DEEP if j == 0 else T.INK, align=C, anchor=MID, spacing=0.95)
        if ex:
            text(s, x + 0.04, 1.52, cw - 0.08, 0.36, ex, size=6.5, color=T.BODY, align=C, spacing=1.0)
    for i, (cap, st, cells) in enumerate(c['rows']):
        y = 1.95 + i * 0.42
        rect(s, lx, y - 0.02, 8.45, 0.01, fill=T.BORDER)
        text(s, lx, y, lw - 0.1, 0.4, cap, size=9, font=T.LABEL_FONT, anchor=MID, spacing=1.0)
        bg, fg = STATUS[st]
        chip(s, c['status_label'][st], lx + lw + cw / 2, y + 0.08, bg=bg, fg=fg, size=7, h=0.24, align='c')
        for j, v in enumerate(cells):
            x = lx + lw + (j + 1) * cw
            if v == 'yes':
                icon(s, 'check', 'green', x + cw / 2 - 0.09, y + 0.11, 0.18)
            elif v == 'no':
                text(s, x, y, cw, 0.4, '—', size=9, color=T.GRAY, align=C, anchor=MID)
            else:
                text(s, x, y, cw, 0.4, v, size=7.5, color=T.BODY, align=C, anchor=MID)
    rect(s, 0.6, 4.66, 8.8, 0.48, fill=T.LAV2, radius=0.14)
    text(s, 0.78, 4.66, 8.45, 0.48, c['statement'], size=9.5, font=T.LABEL_FONT, color=T.DEEP, anchor=MID,
         spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 8
def s_gtm(s):
    c = K.GTM
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    for i, (ic, name, steps, measure, repeat, math_) in enumerate(c['funnels']):
        y = 0.98 + i * 1.74
        card(s, 0.6, y, 8.8, 1.66, radius=0.16)
        icon_circle(s, ic, 0.76, y + 0.12, 0.4)
        text(s, 1.24, y + 0.12, 1.6, 0.4, name, size=12.5, font=T.TITLE_FONT, anchor=MID)
        arrow_chips(s, steps, 2.75, y + 0.17, h=0.3, size=7.5, gap=0.16, bg=T.LAV2, fg=T.DEEP,
                    last=(T.PURPLE, T.WHITE))
        text(s, 0.78, y + 0.6, 1.2, 0.18, 'MEASURE', size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, 0.78, y + 0.78, 4.2, 0.26, measure, size=9, anchor=MID)
        text(s, 5.1, y + 0.6, 1.6, 0.18, 'SECOND PURCHASE', size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, 5.1, y + 0.78, 4.15, 0.26, repeat, size=9, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
        rect(s, 0.72, y + 1.08, 8.56, 0.52, fill=T.LAV, radius=0.1)
        text(s, 0.84, y + 1.1, 1.2, 0.16, 'YEAR-1 MATH', size=6.5, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, 0.84, y + 1.25, 8.35, 0.34, math_, size=7.5, color=T.INK, anchor=MID, spacing=1.0)
    text(s, 0.6, 4.47, 6.0, 0.18, c['targets_title'], size=7, font=T.LABEL_FONT, color=T.PURPLE)
    tw = (8.8 - 0.3) / 4
    for i, (v, lbl) in enumerate(c['targets']):
        x = 0.6 + i * (tw + 0.1)
        rect(s, x, 4.67, tw, 0.5, fill=T.PALEY, radius=0.12)
        text(s, x + 0.1, 4.67, 0.95, 0.5, v, size=12 if len(v) > 4 else 15, font=T.TITLE_FONT, color=T.INK,
             anchor=MID)
        text(s, x + 1.02, 4.67, tw - 1.08, 0.5, lbl, size=8, color=T.AMBER_DARK, anchor=MID, spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 9
def s_team(s):
    c = K.TEAM
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    for i, (name, role, photo, focus, creds) in enumerate(c['team']):
        x = 0.6 + i * 4.5
        card(s, x, 1.0, 4.3, 3.65, radius=0.18)
        pw = Image.open(T.GEN / photo).size
        ph = 1.15
        pic(s, photo, x + 0.18, 1.12, w=ph * pw[0] / pw[1], h=ph, alt=name)
        tx = x + 1.45
        text(s, tx, 1.14, 2.75, 0.34, name, size=13.5, font=T.TITLE_FONT, anchor=MID)
        chip(s, role, tx, 1.52, bg=T.LAV2, fg=T.DEEP, size=7, h=0.26)
        text(s, tx, 1.86, 2.75, 0.4, focus, size=8.5, color=T.BODY, spacing=1.0)
        _bullets(s, creds, x + 0.2, 2.42, 3.95, 0.43, size=8.5, ic='star', color='purple')
    rect(s, 0.6, 4.76, 8.8, 0.38, fill=T.PURPLE, radius=0.19)
    text(s, 0.6, 4.76, 8.8, 0.38, c['proof'], size=11, font=T.TITLE_FONT, color=T.WHITE, align=C, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 10
def s_plan(s):
    c = K.PLAN
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=19)
    w, gap = 2.08, 0.16
    for i, (period, head, items, gate) in enumerate(c['stages']):
        x = 0.6 + i * (w + gap)
        fill = [T.PURPLE, T.LAV2, T.WHITE, T.WHITE][i]
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, 1.0, w, 3.6, fill=fill, line=T.BORDER if i >= 2 else None, radius=0.16, lw=0.75)
        chip(s, period, x + 0.14, 1.12, bg=T.WHITE if i < 2 else T.LAV2, fg=T.DEEP, size=7.5, h=0.26)
        text(s, x + 0.14, 1.46, w - 0.28, 0.5, head, size=12, font=T.TITLE_FONT, color=fg, spacing=0.95)
        _bullets(s, items, x + 0.14, 2.02, w - 0.28, 0.36, size=9, ic='check' if i == 0 else 'arrow-right',
                 color='white' if i == 0 else 'purple', fg=fg)
        rect(s, x + 0.1, 3.18, w - 0.2, 1.32, fill=T.WHITE if i < 2 else T.PALEY, radius=0.1)
        text(s, x + 0.2, 3.24, w - 0.4, 1.2, gate, size=8.5, font=T.LABEL_FONT,
             color=T.DEEP if i < 2 else T.AMBER_DARK, anchor=MID, spacing=1.02)
        if i < 3:
            rect(s, x + w + 0.03, 2.65, 0.1, 0.26, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    rect(s, 0.6, 4.72, 8.8, 0.42, fill=T.LAV2, radius=0.21)
    text(s, 0.6, 4.72, 8.8, 0.42, c['footer'], size=10.5, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 11
def s_vision(s):
    c = K.VISION
    title(s, c['title'], 0.6, 0.4, 8.4, 0.8, size=21)
    w, gap = 1.68, 0.11
    for i, (yr, head, items, rev) in enumerate(c['years']):
        x = 0.6 + i * (w + gap)
        fill = T.PURPLE if i == 0 else T.LAV2 if i < 3 else T.WHITE
        fg = T.WHITE if i == 0 else T.INK
        rect(s, x, 1.3, w, 1.95, fill=fill, line=T.BORDER if i >= 3 else None, radius=0.14, lw=0.75)
        text(s, x + 0.12, 1.38, w - 0.24, 0.2, yr, size=7.5, font=T.LABEL_FONT, color=T.LAV2 if i == 0 else T.PURPLE)
        text(s, x + 0.12, 1.58, w - 0.24, 0.32, head, size=12 if len(head) > 10 else 13, font=T.TITLE_FONT, color=fg)
        y = 1.96
        for it in items:
            n = _lines(it, 8.5, w - 0.24)
            text(s, x + 0.12, y, w - 0.24, 0.16 * n + 0.06, it, size=8.5, color=fg, spacing=1.0)
            y += 0.16 * n + 0.12
        text(s, x + 0.12, 2.94, w - 0.24, 0.26, rev, size=8, font=T.LABEL_FONT, color=T.LAV2 if i == 0 else T.DEEP)
    text(s, 0.6, 3.36, 6.0, 0.2, c['revenue_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    top = max(K.BASE['revenue'])
    colors = {'pack': T.BLOB_LIGHT, 'session': T.BLOB_MAIN, 'course': T.PURPLE, 'license': T.DEEP}
    for i in range(5):
        x = 0.6 + i * (w + gap) + 0.35
        y = 4.78
        for k in ('pack', 'session', 'course', 'license'):
            hh = 1.1 * K.BASE['rev'][k][i] / top
            if hh > 0.004:
                y -= hh
                rect(s, x, y, w - 0.7, hh, fill=colors[k])
        text(s, x - 0.35, y - 0.22, w, 0.2, K.rp(K.BASE['revenue'][i]), size=8.5, font=T.TITLE_FONT, color=T.DEEP,
             align=C, anchor=MID)
    lx = 0.6
    for k, lbl in (('pack', 'Packs'), ('session', 'Sessions'), ('course', 'Course'), ('license', 'Licenses')):
        rect(s, lx, 4.92, 0.14, 0.14, fill=colors[k])
        text(s, lx + 0.2, 4.86, 0.9, 0.26, lbl, size=8, color=T.BODY, anchor=MID)
        lx += 1.05
    text(s, 4.9, 4.86, 4.5, 0.26, c['note'], size=8, font=T.LABEL_FONT, color=T.DEEP, align=R, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 12 (summary: revenue, operating result, funding)
def s_fin(s):
    c = K.FIN
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=22)
    w, gap = 1.68, 0.11
    for i in range(5):
        x = 0.6 + i * (w + gap)
        res = K.BASE['result'][i]
        card(s, x, 1.02, w, 2.45, radius=0.14)
        text(s, x + 0.14, 1.1, w - 0.28, 0.2, f'YEAR {i + 1}', size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.14, 1.32, w - 0.28, 0.18, 'REVENUE', size=6.5, font=T.LABEL_FONT, color=T.BODY)
        text(s, x + 0.14, 1.5, w - 0.28, 0.42, K.rp(K.BASE['revenue'][i]), size=17, font=T.TITLE_FONT,
             color=T.DEEP, anchor=MID)
        rect(s, x + 0.1, 2.0, w - 0.2, 0.72, fill=T.MINT if res > 0 else T.PALEY, radius=0.1)
        text(s, x + 0.2, 2.04, w - 0.4, 0.18, 'OPERATING RESULT', size=6.5, font=T.LABEL_FONT,
             color=T.GREEN if res > 0 else T.AMBER_DARK)
        text(s, x + 0.2, 2.24, w - 0.4, 0.42, K.rp(res, sign=True), size=14, font=T.TITLE_FONT,
             color=T.GREEN if res > 0 else T.AMBER_DARK, anchor=MID)
        text(s, x + 0.14, 2.8, w - 0.28, 0.18, 'CASH AT YEAR END', size=6.5, font=T.LABEL_FONT, color=T.BODY)
        text(s, x + 0.14, 2.98, w - 0.28, 0.4, K.rp(K.BASE['cash'][i]), size=12, font=T.LABEL_FONT, anchor=MID)
    rect(s, 0.6, 3.6, 8.8, 0.62, fill=T.PURPLE, radius=0.16)
    icon(s, 'rocket', 'white', 0.8, 3.78, 0.26)
    text(s, 1.2, 3.6, 8.05, 0.62, c['funding'], size=10.5, font=T.LABEL_FONT, color=T.WHITE, anchor=MID, spacing=1.0)
    rect(s, 0.6, 4.32, 8.8, 0.46, fill=T.PALEY, radius=0.14)
    text(s, 0.78, 4.32, 8.45, 0.46, c['cons'], size=9, font=T.LABEL_FONT, color=T.AMBER_DARK, anchor=MID,
         spacing=1.0)
    text(s, 0.6, 4.86, 8.8, 0.3, c['note'], size=7.5, color=T.BODY, spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- 13
def s_ask(s):
    c = K.ASK
    title(s, c['title'], 0.6, 0.38, 8.0, 0.5, size=24)
    text(s, 0.6, 0.9, 8.8, 0.3, c['statement'], size=11.5, font=T.LABEL_FONT, color=T.DEEP, anchor=MID)
    top = 1.3
    rect(s, 0.6, top, 3.0, 2.05, fill=T.PURPLE, radius=0.18)
    text(s, 0.8, top + 0.1, 2.6, 0.6, c['amount'], size=34, font=T.TITLE_FONT, color=T.WHITE, anchor=MID)
    text(s, 0.8, top + 0.7, 2.6, 0.28, c['equity'], size=11.5, font=T.LABEL_FONT, color=T.WHITE, anchor=MID)
    rect(s, 0.8, top + 1.06, 2.6, 0.01, fill=T.LAV2)
    text(s, 0.8, top + 1.12, 2.6, 0.28, c['valuation'], size=9.5, color=T.LAV2, anchor=MID)
    text(s, 0.8, top + 1.42, 2.6, 0.55, c['period'], size=9.5, color=T.LAV2, spacing=1.0)
    card(s, 3.75, top, 2.8, 2.05, radius=0.16)
    text(s, 3.92, top + 0.08, 2.5, 0.2, c['use_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    for j, (pct, use, amt) in enumerate(c['use']):
        y = top + 0.32 + j * 0.28
        text(s, 3.92, y, 0.5, 0.26, pct, size=10, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
        text(s, 4.42, y, 1.45, 0.26, use, size=9, anchor=MID)
        text(s, 5.75, y, 0.7, 0.26, amt, size=8.5, color=T.BODY, align=R, anchor=MID)
    card(s, 6.7, top, 2.7, 2.05, radius=0.16)
    text(s, 6.86, top + 0.08, 2.4, 0.2, c['milestones_title'], size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    _bullets(s, c['milestones'], 6.86, top + 0.32, 2.42, 0.34, size=8.5)
    rect(s, 0.6, 3.5, 8.8, 1.65, fill=T.LAV2, radius=0.18)
    pic(s, T.LOGO, 0.85, 3.7, h=0.5, alt='Scanvas logo')
    text(s, 0.85, 4.26, 3.0, 0.4, 'Let’s build it together.', size=15, font=T.TITLE_FONT, color=T.DEEP, anchor=MID)
    text(s, 0.85, 4.68, 3.4, 0.3, c['contact_extra'], size=9, font=T.LABEL_FONT, color=T.INK, anchor=MID)
    for j, (who, mail) in enumerate(c['contacts']):
        y = 3.72 + j * 0.62
        text(s, 4.4, y, 3.4, 0.24, who, size=10, font=T.TITLE_FONT, anchor=MID)
        text(s, 4.4, y + 0.25, 3.4, 0.26, mail, size=9.5, color=T.DEEP, anchor=MID)
    _qr(s, 8.15, 3.68, 1.05)
    text(s, 7.9, 4.76, 1.55, 0.22, 'TRY THE DEMO', size=7, font=T.LABEL_FONT, color=T.PURPLE, align=C, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- appendix A: unit costs, volumes, annual cash
def s_appx_fin(s):
    c = K.APPX_FIN
    title(s, c['title'], 0.6, 0.4, 8.6, 0.5, size=20)
    card(s, 0.6, 0.98, 8.8, 1.4, radius=0.14)
    cols = [(0.75, 2.2, L), (2.95, 0.7, R), (3.7, 0.75, R), (4.65, 4.6, L)]
    for (x, w, a), h in zip(cols, c['unit_head']):
        text(s, x, 1.04, w, 0.2, h.upper(), size=7, font=T.LABEL_FONT, color=T.PURPLE, align=a)
    for i, (key, (name, price, cost, covers)) in enumerate(K.UNITS.items()):
        y = 1.27 + i * 0.27
        vals = [name.split(' (')[0] + (' / yr' if key == 'license' else ''), K.rpu(price), K.rpu(cost), covers]
        for (x, w, a), v in zip(cols, vals):
            text(s, x, y, w, 0.26, v, size=7.5 if x > 4 else 8, font=T.LABEL_FONT if x < 1 else T.BODY_FONT,
                 align=a, anchor=MID)
    card(s, 0.6, 2.48, 3.75, 1.38, radius=0.14)
    vcols = [(0.75, 1.15)] + [(1.9 + j * 0.48, 0.44) for j in range(5)]
    for (x, w), h in zip(vcols, c['vol_head']):
        text(s, x, 2.54, w, 0.2, h.upper(), size=7, font=T.LABEL_FONT, color=T.PURPLE, align=L if x < 1 else R)
    for i, key in enumerate(K.UNITS):
        y = 2.78 + i * 0.26
        text(s, 0.75, y, 1.15, 0.25, K.SHORT[key], size=8, font=T.LABEL_FONT, anchor=MID)
        for j, v in enumerate(K.VOLUME[key]):
            text(s, vcols[j + 1][0], y, 0.44, 0.25, f'{v:,}' if v else '—', size=7.5, align=R, anchor=MID)
    _bullets(s, c['assumptions'], 0.6, 3.95, 3.75, 0.3, size=7.5, ic='arrow-right')
    card(s, 4.5, 2.48, 4.9, 2.66, radius=0.14)
    rows = [('Revenue', K.BASE['revenue'], ''), ('Contribution', K.BASE['contribution'], ''),
            ('Operating expenses', [-x for x in K.OPEX], ''), ('Operating result', K.BASE['result'], 'sum'),
            ('Capex', [-x for x in K.CAPEX], ''), ('Change in working capital', [-x for x in K.BASE['dwc']], ''),
            ('Funding in (Y2 planned)', K.FUNDING, ''), ('Cash at year end · base', K.BASE['cash'], 'sum'),
            ('Operating result · conservative', K.CONS['result'], 'cons'),
            ('Cash at year end · conservative', K.CONS['cash'], 'cons')]
    for j in range(5):
        text(s, 6.25 + j * 0.62, 2.54, 0.6, 0.18, f'Y{j + 1}', size=7, font=T.LABEL_FONT, color=T.PURPLE, align=R)
    for i, (lbl, vals, style) in enumerate(rows):
        y = 2.76 + i * 0.232
        if style == 'sum':
            rect(s, 4.58, y - 0.01, 4.74, 0.23, fill=T.LAV, radius=0.05)
        text(s, 4.66, y, 1.6, 0.21, lbl, size=7, font=T.LABEL_FONT if style else T.BODY_FONT,
             color=T.AMBER_DARK if style == 'cons' else T.INK, anchor=MID)
        for j, v in enumerate(vals):
            txt = '—' if abs(v) < 0.05 else K.rp(v)
            text(s, 6.25 + j * 0.62, y, 0.6, 0.21, txt.replace('Rp', ''), size=7,
                 color=T.AMBER_DARK if v < 0 and style else T.INK, align=R, anchor=MID)
    notes(s, c['notes'])


# ---------------------------------------------------------------- appendix B: monthly cash
def s_appx_cash(s):
    c = K.APPX_CASH
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=21)
    card(s, 0.6, 1.0, 6.3, 4.15, radius=0.14)
    x0, base_y, ch = 1.05, 4.3, 2.8
    lo = min(min(K.CASH_M), min(K.monthly(0)), 0)
    hi = max(K.CASH_M + [200])
    scale = ch / (hi - lo)
    zero_y = base_y - (0 - lo) * scale
    bw, step = 0.17, 0.235
    for m, v in enumerate(K.CASH_M):
        x = x0 + m * step
        h = v * scale
        rect(s, x, zero_y - h if h > 0 else zero_y, bw, abs(h), fill=T.PURPLE if m < 12 else T.BLOB_MAIN)
    for m, v in enumerate(K.monthly(0)):            # path without the year-2 raise
        if m >= 12:
            oval(s, x0 + m * step + bw / 2 - 0.035, zero_y - v * scale - 0.035, 0.07, fill=T.AMBER_DARK)
    rect(s, x0 - 0.05, zero_y, 24 * step, 0.008, fill=T.INK)
    by = zero_y - K.BUFFER * scale
    for k in range(24):                             # dashed buffer line
        rect(s, x0 + k * step, by, step * 0.55, 0.012, fill=T.GREEN)
    for m in (0, 5, 11, 12, 17, 23):
        text(s, x0 + m * step - 0.1, base_y + 0.06, 0.4, 0.18, f'M{m + 1}', size=7, color=T.BODY, align=C)
    for v in (0, 100, 200):
        y = zero_y - v * scale
        text(s, 0.65, y - 0.09, 0.36, 0.18, str(v), size=7, color=T.BODY, align=R, anchor=MID)
    text(s, 0.75, 1.08, 5.5, 0.2, 'CASH BALANCE AT MONTH END (Rp JUTA)', size=7, font=T.LABEL_FONT, color=T.PURPLE)
    rect(s, 0.8, 4.68, 0.14, 0.14, fill=T.PURPLE)
    text(s, 1.0, 4.62, 2.2, 0.26, f'Base, with Rp{K.Y2_RAISE}M planned in month 13', size=7.5, color=T.BODY, anchor=MID)
    oval(s, 3.35, 4.71, 0.08, fill=T.AMBER_DARK)
    text(s, 3.5, 4.62, 1.6, 0.26, 'Without the year-2 raise', size=7.5, color=T.BODY, anchor=MID)
    rect(s, 5.05, 4.74, 0.25, 0.015, fill=T.GREEN)
    text(s, 5.35, 4.62, 1.5, 0.26, f'Buffer Rp{K.BUFFER:.1f}M', size=7.5, color=T.GREEN, anchor=MID)
    # right column: findings + assumptions
    low, low_m = K.LOW_NO_RAISE
    rect(s, 7.05, 1.0, 2.35, 1.95, fill=T.PALEY, radius=0.14)
    text(s, 7.2, 1.08, 2.1, 0.2, 'WHY THE YEAR-2 RAISE', size=7, font=T.LABEL_FONT, color=T.AMBER_DARK)
    text(s, 7.2, 1.3, 2.1, 1.6, [f'Without it, cash turns negative in month {K.FIRST_NEGATIVE} and reaches '
                                 f'{K.rp(low)} in month {low_m}.',
                                 f'A planned, not committed Rp{K.Y2_RAISE}M keeps cash above a {K.BUFFER_MONTHS}-month opex buffer.',
                                 f'Conservative case still dips to {K.rp(min(K.CASH_M_CONS))}.'],
         size=8.5, color=T.INK, spacing=1.05)
    card(s, 7.05, 3.05, 2.35, 2.1, radius=0.14)
    text(s, 7.2, 3.12, 2.1, 0.2, 'ASSUMPTIONS', size=7, font=T.LABEL_FONT, color=T.PURPLE)
    _bullets(s, c['assumptions'], 7.2, 3.36, 2.12, 0.35, size=7.5, ic='arrow-right')
    notes(s, c['notes'])


# ---------------------------------------------------------------- appendix C: sales engine
def s_appx_sales(s):
    c = K.APPX_SALES
    title(s, c['title'], 0.6, 0.4, 8.0, 0.5, size=21)
    card(s, 0.6, 0.98, 8.8, 4.17, radius=0.14)
    cols = [(0.75, 1.45), (2.25, 1.65), (3.95, 1.85), (5.85, 1.7), (7.6, 1.7)]
    for (x, w), h in zip(cols, c['head']):
        text(s, x, 1.05, w, 0.22, h.upper(), size=7, font=T.LABEL_FONT, color=T.PURPLE)
    for i, row in enumerate(c['rows']):
        y = 1.32 + i * 0.76
        if i:
            rect(s, 0.72, y - 0.05, 8.56, 0.008, fill=T.BORDER)
        if i < 2:
            rect(s, 0.68, y - 0.03, 1.5, 0.7, fill=T.LAV2, radius=0.08)
        for j, ((x, w), v) in enumerate(zip(cols, row)):
            text(s, x, y, w - 0.08, 0.68, v, size=8.5 if j == 0 else 7.5, font=T.TITLE_FONT if j == 0 else T.BODY_FONT,
                 color=T.DEEP if j == 0 else T.INK, anchor=MID, spacing=1.0)
    notes(s, c['notes'])


# ---------------------------------------------------------------- appendix G: course as a learning product
def s_appx_course(s):
    c = K.APPX_COURSE
    title(s, c['title'], 0.6, 0.4, 8.8, 0.5, size=19)
    card(s, 0.6, 1.0, 4.15, 4.15, radius=0.14)
    for i, (lesson, skill) in enumerate(zip(c['lessons'], c['skills'])):
        y = 1.1 + i * 0.4
        pilot = i < 3
        if pilot:
            rect(s, 0.68, y - 0.02, 3.99, 0.37, fill=T.LAV2, radius=0.08)
        num_circle(s, i + 1, 0.76, y + 0.04, 0.26, size=8, bg=T.PURPLE if pilot else T.GRAY)
        text(s, 1.1, y, 1.75, 0.34, lesson, size=8.5, font=T.LABEL_FONT, anchor=MID)
        text(s, 2.85, y, 1.55, 0.34, skill, size=7.5, color=T.BODY, anchor=MID)
        text(s, 4.35, y, 0.3, 0.34, 'ABCDEFGHIJ'[i], size=8, font=T.TITLE_FONT, color=T.DEEP, align=R, anchor=MID)
    for k, (head, body) in enumerate(c['boxes']):
        x, y = 4.9 + (k % 2) * 2.27, 1.0 + (k // 2) * 1.5
        rect(s, x, y, 2.18, 1.4, fill=T.LAV if k % 3 == 0 else T.WHITE, line=None if k % 3 == 0 else T.BORDER,
             radius=0.12, lw=0.75)
        text(s, x + 0.12, y + 0.08, 1.95, 0.2, head, size=7, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.12, y + 0.3, 1.97, 1.08, body, size=8, color=T.INK, spacing=1.03)
    rect(s, 4.9, 4.05, 4.5, 1.1, fill=T.PALEY, radius=0.14)
    text(s, 5.06, 4.12, 4.2, 0.2, c['gate_title'] + ' · PILOT LESSONS 1–3 FIRST', size=7, font=T.LABEL_FONT,
         color=T.AMBER_DARK)
    text(s, 5.06, 4.34, 4.2, 0.74, c['gate'], size=10.5, font=T.TITLE_FONT, color=T.INK, anchor=MID, spacing=1.0)
    notes(s, c['notes'])
