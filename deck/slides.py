"""One function per slide: layout only. Copy comes from content.py, colors/fonts from theme.py."""
import math

from pptx.enum.shapes import MSO_SHAPE

from . import content as K
from . import theme as T
from .helpers import (L, C, R, MID, rgb, text, title, rect, card, oval, pic, img_size, icon, icon_circle, num_circle,
                      chip, chip_width, arrow_chips, notes)


def s1_cover(s):
    c = K.SLIDE_1_COVER
    pic(s, T.LOGO, 0.6, 0.78, h=0.62, alt='Scanvas logo')
    title(s, c['title'], 0.58, 1.5, 4.0, 0.8, size=48)
    text(s, 0.6, 2.32, 3.4, 0.8, c['subtitle'], size=19, color=T.PURPLE, font=T.TITLE_FONT, spacing=0.95)
    text(s, 0.6, 3.22, 3.05, 0.9, c['body'], size=11, color=T.BODY, spacing=1.15)
    chip(s, c['age_chip'], 0.6, 4.28, bg=T.LAV2, fg=T.DEEP, size=8.5, h=0.3, ic=('palette', 'purple'))
    # hero: colored paper -> scan -> alive on phone
    # layout follows the user's own edit of the cover (2026-09-14): QR to scanvas.id under the hero
    pic(s, 'paper_whale_tilt.png', 3.84, 0.0, w=2.75, alt='Child-colored Scanvas whale sheet')
    pic(s, 'tab_result.png', 5.3, 1.62, w=4.45, alt='The same whale scanned and alive in Scanvas')
    rect(s, 4.42, 3.4, 1.81, 1.78, fill=T.WHITE, line=T.BORDER, radius=0.17, lw=0.75)
    pic(s, T.ASSETS / 'qr_scanvas.png', 4.53, 3.53, w=1.59, h=1.59, alt='QR code to scanvas.id')
    link = rect(s, 4.42, 5.26, 1.81, 0.3, fill=T.WHITE, line=T.BORDER, radius=0.05, lw=0.75)
    text(s, 0, 0, 0, 0, K.WEBSITE, size=18, font=T.TITLE_FONT, color=T.BLUE, align=C, anchor=MID, shape=link)
    run = link.text_frame.paragraphs[0].runs[0]
    run.hyperlink.address = 'https://www.scanvas.id/'
    run.font.underline = True
    bw = c.get('name_box_w', 1.56)   # wider box when both founders are listed
    rect(s, 9.67 - bw, 4.6, bw, 0.52, fill=T.WHITE, radius=0.12)
    text(s, 9.67 - bw, 4.62, bw - 0.12, 0.48, [
        [(c['founder_name'], {'size': 9.5, 'font': T.LABEL_FONT})],
        [(c['founder_role'], {'size': 8, 'color': T.BODY})]], align=R, anchor=MID)
    text(s, 0.6, 5.12, 3.2, 0.2, K.TRACK, size=7, font=T.LABEL_FONT, color=T.BODY, anchor=MID)   # small footer
    notes(s, c['notes'])


def s2_problem(s):
    c = K.SLIDE_2_PROBLEM
    title(s, c['title'], 0.6, 0.45, 8.0, 0.6, size=28)
    text(s, 0.6, 1.25, 8.2, 0.55, c['message'], size=10.5, color=T.BODY, spacing=1.15)
    for i, key in enumerate(('paper', 'screen')):
        d = c[key]
        x = 0.6 + i * 4.5
        card(s, x, 2.08, 4.3, 2.45, radius=0.18)
        if i == 0:
            pic(s, 'm_kidcolor.png', x + 0.22, 2.28, w=1.55, alt='Child coloring a Scanvas sheet')
        else:
            rect(s, x + 0.22, 2.28, 1.55, 1.35, fill=T.SLATE2, radius=0.13)
            rect(s, x + 0.67, 2.41, 0.65, 1.1, fill=T.WHITE, line=T.GRAY, radius=0.1, lw=2)
            icon(s, 'monitor-play', 'gray', x + 0.79, 2.76, 0.42)
        text(s, x + 1.98, 2.32, 2.15, 0.35, d['head'], size=15, font=T.TITLE_FONT)
        text(s, x + 1.98, 2.74, 2.1, 0.9, d['sub'], size=10, color=T.BODY, spacing=1.15)
        arrow_chips(s, d['loop'], x + 0.22, 3.92, h=0.34, size=9,
                    bg=T.LAV2 if i == 0 else T.SLATE2, fg=T.DEEP if i == 0 else T.MUTED,
                    last=(T.WHITE, T.MUTED) if i == 0 else None, arrow='purple' if i == 0 else 'gray')
    text(s, 0.6, 4.7, 8.8, 0.4, c['closing'], size=14, color=T.PURPLE, font=T.TITLE_FONT, align=C)
    notes(s, c['notes'])


def s3_insight(s):
    c = K.SLIDE_3_INSIGHT
    title(s, c['title'], 4.75, 1.18, 4.75, 0.85, size=22)
    text(s, 4.75, 2.0, 4.6, 0.6, c['message'], size=10.5, color=T.BODY, spacing=1.15)
    for i, (ic, lead, desc) in enumerate(c['points']):
        y = 2.72 + i * 0.56
        icon_circle(s, ic, 4.75, y + 0.02, 0.42)
        text(s, 5.32, y - 0.01, 4.15, 0.25, lead, size=10.5, font=T.LABEL_FONT)
        text(s, 5.32, y + 0.23, 4.15, 0.25, desc, size=9.5, color=T.BODY)
    # learning loop on a lavender disc over the template blob
    cx, cy, rr = 2.35, 3.0, 1.4
    oval(s, cx - rr - 0.42, cy - rr - 0.42, 2 * rr + 0.84, fill=T.WHITE)
    oval(s, cx - rr, cy - rr, 2 * rr, line=T.PURPLE, lw=2.25)
    for ang in (45, 135, 225, 315):
        a = math.radians(ang)
        tx, ty = cx + rr * math.sin(a), cy - rr * math.cos(a)
        rect(s, tx - 0.1, ty - 0.1, 0.2, 0.2, fill=T.PURPLE, shape=MSO_SHAPE.ISOSCELES_TRIANGLE, rot=ang + 90)
    text(s, cx - 0.55, cy - 0.3, 1.1, 0.6, [[(t, {})] for t in c['loop_center']], size=11, color=T.DEEP,
         font=T.TITLE_FONT, align=C, anchor=MID, spacing=0.95)
    pos = [(cx, cy - rr), (cx + rr, cy), (cx, cy + rr), (cx - rr, cy)]
    for (lbl, ic), (px, py) in zip(c['loop'], pos):
        two = ' ' in lbl and len(lbl) > 9          # long labels wrap to 2 lines to stay inside the slide
        h = 0.58 if two else 0.4
        w = chip_width(max(lbl.split(), key=len) if two else lbl, 9, 0.4, True) + (0.2 if two else 0)
        chip(s, lbl.replace(' ', '\n', 1) if two else lbl, px, py - h / 2, bg=T.WHITE, fg=T.INK, size=9, h=h, w=w,
             line=T.BORDER, ic=(ic, 'purple'), align='c')
    notes(s, c['notes'])


def s4_solution(s):
    c = K.SLIDE_4_SOLUTION
    title(s, c['title'], 0.6, 0.45, c.get('title_w', 8.0), 0.9, size=c.get('title_size', 28))
    text(s, 0.6, 1.25, 8.3, 0.55, c['message'], size=10.5, color=T.BODY, spacing=1.15)
    tw, gap, ty, th, x0 = 1.5, 0.26, 2.1, 1.75, 0.86
    for i, (lbl, cap, img, fit) in enumerate(c['steps']):
        x = x0 + i * (tw + gap)
        card(s, x, ty, tw, th)
        w, h = img_size(img, w=tw - 0.04) if fit == 'w' else img_size(img, h=th - 0.08)
        pic(s, img, x + (tw - w) / 2, ty + (th - h) / 2 + 0.03, w=w, h=h, alt=f'{lbl} step')
        num_circle(s, i + 1, x - 0.08, ty - 0.12, 0.34, size=11)
        text(s, x, ty + th + 0.12, tw, 0.3, lbl, size=13, font=T.TITLE_FONT)
        text(s, x, ty + th + 0.44, tw, 0.5, cap, size=9, color=T.BODY, spacing=1.1)
        if i < len(c['steps']) - 1:
            rect(s, x + tw + 0.07, ty + th / 2 - 0.13, 0.12, 0.26, fill=T.PURPLE, shape=MSO_SHAPE.CHEVRON)
    notes(s, c['notes'])


def s5_product(s):
    c = K.SLIDE_5_PRODUCT
    chip(s, c['tag'], 0.6, 0.45, bg=T.MINT, fg=T.GREEN, size=8.5, h=0.3, ic=('check', 'green'))
    title(s, c['title'], 0.6, 0.88, c.get('title_w', 3.7), 0.85, size=c.get('title_size', 24))
    step = min(0.6, 3.0 / len(c['capabilities']))
    for i, (ic, head, detail) in enumerate(c['capabilities']):
        y = 1.95 + i * step
        icon_circle(s, ic, 0.6, y + 0.02, 0.42)
        text(s, 1.15, y - 0.01, 3.1, 0.25, head, size=10.5, font=T.LABEL_FONT)
        text(s, 1.15, y + 0.23, 3.1, 0.25, detail, size=9.5, color=T.BODY)
    for i, (img, lbl) in enumerate(c['phones']):
        x = 4.4 + i * 1.72
        pic(s, img, x, 0.2, h=3.2, alt=lbl)
        text(s, x, 3.37, 1.64, 0.22, lbl, size=8.5, font=T.LABEL_FONT, color=T.BODY, align=C)
    for i, (img, lbl) in enumerate(c['screens']):
        x = 4.45 + i * 2.58
        pic(s, img, x, 3.62, w=2.5, alt=lbl)
        chip(s, lbl, x + 0.25, 3.79, bg=T.WHITE, fg=T.INK, size=7.5, h=0.24)
    notes(s, c['notes'])


def s6_magic(s):
    c = K.SLIDE_6_MAGIC
    title(s, c['title'], 0.6, 0.45, 6.6, 0.6, size=28, color=T.ON_BLOB)
    text(s, 0.6, 1.2, 6.2, 0.5, c['message'], size=10.5, color=T.ON_BLOB, spacing=1.15)
    pic(s, 'paper_whale_tilt.png', 0.72, 1.92, w=2.5, alt='Before: whale colored on paper')
    chip(s, c['before'], 0.9, 2.0, bg=T.WHITE, fg=T.INK, size=8.5, h=0.3)
    icon_circle(s, 'wand-sparkles', 3.62, 2.86, 0.72, bg=T.YELLOW, ic='ink', ratio=0.5)
    pic(s, 'tab_result.png', 4.7, 1.78, w=4.75, alt='After: the same whale scanned and alive in Scanvas')
    chip(s, c['after'], 5.15, 2.18, bg=T.PURPLE, fg=T.WHITE, size=8.5, h=0.3)
    x = 0.72
    for lbl, ic in c['trio']:
        w = chip_width(lbl, 10, 0.44, True)
        chip(s, lbl, x, 4.72, bg=T.WHITE, fg=T.DEEP, size=10, h=0.44, w=w, ic=(ic, 'purple'))
        x += w + 0.16
    notes(s, c['notes'])


def s7_different(s):
    c = K.SLIDE_7_DIFFERENT
    title(s, c['title'], 0.75, 0.42, c.get('title_w', 7.2), 0.8, size=c.get('title_size', 22))
    oval(s, 3.65, 1.45, 2.7, fill=T.LAV2)
    pic(s, 'ph_world.png', 4.0, 1.12, h=3.95, alt='The scanned whale swimming in the Ocean world on a phone')
    for i, (h, d) in enumerate(c['items']):
        x = 0.75 if i % 2 == 0 else 6.3
        y = 1.35 + (i // 2) * 1.85
        card(s, x, y, 2.95, 1.6)
        num_circle(s, i + 1, x + 0.22, y + 0.2, 0.42, size=13)
        text(s, x + 0.76, y + 0.16, 2.05, 0.5, h, size=12.5, font=T.TITLE_FONT, anchor=MID, spacing=0.95)
        text(s, x + 0.22, y + 0.76, 2.55, 0.8, d, size=9.5, color=T.BODY, spacing=1.12)
    notes(s, c['notes'])


def s8_roadmap(s):
    c = K.SLIDE_8_ROADMAP
    title(s, c['title'], 0.6, 0.42, 6.0, 0.95)
    text(s, 0.6, 1.42, 5.8, 0.5, c['message'], size=10.5, color=T.BODY, spacing=1.15)
    # (block top, fill, flow color, desc color, chip bg, chip fg, chip line)
    styles = [(3.1, T.PURPLE, T.WHITE, T.LAV2, T.MINT, T.GREEN, None),
              (2.45, T.LAV2, T.DEEP, T.BODY, T.PURPLE, T.WHITE, None),
              (1.8, T.WHITE, T.DEEP, T.BODY, T.WHITE, T.DEEP, T.DEEP)]
    for i, ((lbl, flow, desc, ic), (top, bg, ffg, dfg, cbg, cfg, cl)) in enumerate(zip(c['stages'], styles)):
        x = 0.85 + i * 2.9
        rect(s, x, top, 2.75, 4.95 - top, fill=bg, radius=0.18, line=[T.WHITE, None, T.BORDER][i],
             lw=2.5 if i == 0 else 0.75)
        icon_circle(s, ic, x + 0.22, top - 0.32, 0.62, bg=T.WHITE, ic='purple', line=T.BORDER if i else None)
        chip(s, lbl, x + 2.55, top + 0.18, bg=cbg, fg=cfg, size=8, h=0.28, align='r', line=cl)
        lines = 1 if len(flow) < 26 else 2
        text(s, x + 0.22, top + 0.58, 2.35, 0.34 * lines, flow, size=11.5, font=T.TITLE_FONT, color=ffg, spacing=1.0)
        text(s, x + 0.22, top + 0.7 + 0.34 * lines, 2.35, 1.2, desc, size=9.5, color=dfg, spacing=1.15)
    notes(s, c['notes'])


def s9_class(s):
    c = K.SLIDE_9_CLASS
    chip(s, c['tag'], 0.6, 0.45, bg=T.WHITE, fg=T.DEEP, size=8, h=0.28, line=T.DEEP)
    title(s, c['title'], 0.6, 0.86, 4.6, 0.55, size=28)
    text(s, 0.6, 1.42, 4.4, 0.3, c['sub'], size=10.5, color=T.BODY)
    text(s, 0.6, 1.85, 4.6, 0.3, [[(c['lesson_label'] + '  ', {'color': T.BODY}),
                                  (c['lesson'], {'color': T.PURPLE, 'font': T.LABEL_FONT})]], size=10.5)
    for i, t in enumerate(c['steps']):
        x = 0.6 + (i // 3) * 2.3
        y = 2.3 + (i % 3) * 0.52
        num_circle(s, i + 1, x, y, 0.34, size=10.5)
        text(s, x + 0.44, y - 0.04, 1.8, 0.44, t, size=9.5, anchor=MID, spacing=1.05)
    text(s, 0.6, 4.0, 3, 0.25, c['loop_label'], size=8.5, font=T.LABEL_FONT, color=T.BODY)
    arrow_chips(s, c['loop'], 0.6, 4.28, h=0.3, size=8, gap=0.2)
    pic(s, 'tab_lesson.png', 5.2, 1.0, w=4.45, alt='Concept mockup of a Scanvas Creative Class lesson on a tablet')
    notes(s, c['notes'])


TAG_STYLE = {'live': (T.MINT, T.GREEN, None), 'building': (T.PURPLE, T.WHITE, None), 'future': (T.WHITE, T.DEEP, T.DEEP)}


def s10_market(s):
    c = K.SLIDE_10_MARKET
    title(s, c['title'], 0.6, 0.45, 7.6, 0.6, size=28)
    for i, (seg, head, desc, rev, img, (tag, style)) in enumerate(c['segments']):
        x = 0.8 + i * 2.92
        tbg, tfg, tl = TAG_STYLE[style]
        card(s, x, 1.55, 2.76, 3.45)
        pic(s, img, x, 1.55, w=2.76, alt=head)
        chip(s, tag, x + 0.14, 1.69, bg=tbg, fg=tfg, size=7.5, h=0.26, line=tl)
        text(s, x + 0.2, 3.08, 2.4, 0.22, seg, size=8.5, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 0.2, 3.3, 2.4, 0.34, head, size=14, font=T.TITLE_FONT)
        text(s, x + 0.2, 3.68, 2.4, 0.8, desc, size=9.2, color=T.BODY, spacing=1.12)
        text(s, x + 0.2, 4.36, 2.4, 0.56, [[(rev[0], {'size': 7.5, 'font': T.LABEL_FONT, 'color': T.BODY})],
                                           [(rev[1], {})]], size=8.5, font=T.LABEL_FONT, color=T.DEEP, spacing=1.05)
    notes(s, c['notes'])


def s11_validation(s):
    c = K.SLIDE_11_VALIDATION
    title(s, c['title'], 0.6, 0.42, 6.2, 0.95)
    card(s, 0.8, 1.5, 3.85, 3.62, radius=0.18)
    text(s, 1.02, 1.64, 3.5, 0.3, c['snapshot_title'], size=13, font=T.TITLE_FONT)
    chip(s, c['facts'], 1.02, 1.98, bg=T.MINT, fg=T.GREEN, size=7.5, h=0.27, w=3.42, ic=('check', 'green'))  # verified
    for i, (v, lbl) in enumerate(c['metrics']):   # real pilot numbers
        x = 1.02 + i * 1.16
        rect(s, x, 2.36, 1.06, 0.9, fill=T.LAV2, radius=0.12)
        text(s, x, 2.38, 1.06, 0.4, v, size=20, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
        text(s, x + 0.05, 2.78, 0.96, 0.42, lbl, size=7.5, font=T.LABEL_FONT, color=T.INK, align=C, spacing=1.0)
    text(s, 1.02, 3.34, 3.5, 0.24, c['feedback_title'], size=9.5, font=T.LABEL_FONT, color=T.INK)
    for i, (st, f) in enumerate(c['feedback']):
        y = 3.64 + i * 0.285
        shipped = st == 'shipped'
        chip(s, c['status_label'][st], 1.02, y, bg=T.MINT if shipped else T.LAV2, fg=T.GREEN if shipped else T.DEEP,
             size=7, h=0.22, w=0.78)
        text(s, 1.88, y - 0.02, 2.7, 0.26, f, size=8.5, anchor=MID)
    rect(s, 5.2, 1.95, 0.04, 2.5, fill=T.BORDER)
    for i, (p, h, d) in enumerate(c['phases']):
        y = 1.55 + i * 1.22
        num_circle(s, i + 1, 4.98, y + 0.2, 0.48, bg=[T.PURPLE, T.DEEP, T.LAV2][i],
                   fg=T.WHITE if i < 2 else T.DEEP, size=14)
        card(s, 5.65, y, 3.75, 1.08, radius=0.14)
        text(s, 5.85, y + 0.12, 3.4, 0.22, p, size=8, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, 5.85, y + 0.32, 3.4, 0.3, h, size=13, font=T.TITLE_FONT)
        text(s, 5.85, y + 0.64, 3.42, 0.42, d, size=9, color=T.BODY, spacing=1.1)
    notes(s, c['notes'])


def s12_team(s):
    c = K.SLIDE_12_TEAM
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(T.BLOB_MAIN)
    title(s, c['title'], 0.6, 0.45, 8.8, 0.6, size=26, color=T.ON_BLOB, align=C)
    for i, (ini, name, role, focus, photo) in enumerate(c['team']):
        x = 0.6 + i * 4.5
        rect(s, x, 1.3, 4.3, 1.5, fill=T.WHITE, radius=0.18)
        if photo:   # boxes from the user's edit: photo sizes differ per founder so faces match in scale
            px, py, pw, ph = {'founder_sk.png': (0.139, 1.335, 1.267, 1.43),
                              'founder_hh.png': (0.07, 1.316, 1.38, 1.47)}[photo]
            pic(s, photo, x + px, py, w=pw, h=ph, alt=name)
        else:
            num_circle(s, ini, x + 0.24, 1.55, 1.0, bg=T.LAV2, fg=T.DEEP, size=22)
        text(s, x + 1.45, 1.47, 2.75, 0.34, name, size=13.5, font=T.TITLE_FONT, anchor=MID)
        text(s, x + 1.45, 1.82, 2.75, 0.26, role, size=10, font=T.LABEL_FONT, color=T.PURPLE)
        text(s, x + 1.45, 2.12, 2.7, 0.6, focus, size=8.5, color=T.BODY, spacing=1.12)
    icon(s, 'quote', 'deep', 0.6, 3.12, 0.36)
    text(s, 1.1, 3.05, 8.2, 0.8, c['closing'], size=17, font=T.LABEL_FONT, color=T.ON_BLOB, spacing=1.1)
    text(s, 1.1, 3.95, 8.2, 0.4, c['final'], size=14, font=T.TITLE_FONT, color=T.DEEP)
    rect(s, 1.1, 4.62, 0.5, 0.5, fill=T.WHITE, radius=0.12)
    pic(s, T.LOGO, 1.15, 4.67, h=0.4, alt='Scanvas logo')
    text(s, 1.72, 4.62, 1.3, 0.5, K.WEBSITE, size=12, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    oval(s, 3.05, 4.84, 0.06, fill=T.ON_BLOB)
    text(s, 3.25, 4.62, 3.6, 0.5, K.TRACK, size=9, font=T.LABEL_FONT, color=T.ON_BLOB, anchor=MID)
    notes(s, c['notes'])


SLIDES = [s1_cover, s2_problem, s3_insight, s4_solution, s5_product, s6_magic, s7_different, s8_roadmap,
          s9_class, s10_market, s11_validation, s12_team]
