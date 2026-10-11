"""Investor-only slides for the Antler edition (market sizing, the ask). Same helpers and look as slides.py.
Imported after build_deck_antler.py swaps deck.content for deck.content_antler."""
from . import content as K
from . import theme as T
from .helpers import C, MID, text, title, rect, card, oval, icon_circle, num_circle, chip, chip_width, notes


def s_market(s):
    c = K.SLIDE_MARKET
    title(s, c['title'], 0.6, 0.4, 7.2, 0.95, size=24)
    text(s, 0.6, 1.38, 7.0, 0.3, c['message'], size=10.5, color=T.BODY)
    # nested circles, bottom-aligned: TAM > SAM > SOM
    base, cx = 5.0, 2.35
    # nested circles, bottom-aligned: outer = expansion, inner = today's wedge
    circles = [(3.2, T.LAV2, T.DEEP, 0.3), (2.15, T.LAV3, T.DEEP, 0.24), (1.1, T.PURPLE, T.WHITE, 0.36)]
    for (d, fill, fg, ly), (lbl, *_rest) in zip(circles, reversed(c['layers'])):
        oval(s, cx - d / 2, base - d, d, fill=fill)
        text(s, cx - 0.55, base - d + ly, 1.1, 0.36, lbl, size=12, font=T.TITLE_FONT, color=fg, align=C, anchor=MID)
    styles = [(T.PURPLE, T.WHITE), (T.LAV3, T.DEEP), (T.LAV2, T.DEEP)]
    for i, (lbl, where, desc, proof) in enumerate(c['layers']):
        y = 1.8 + i * 1.08
        card(s, 4.35, y, 5.05, 0.96, radius=0.14)
        w = chip_width(lbl, 7.5, 0.26)
        chip(s, lbl, 4.52, y + 0.14, bg=styles[i][0], fg=styles[i][1], size=7.5, h=0.26, w=w)
        text(s, 4.52 + w + 0.12, y + 0.12, 4.6 - w, 0.3, where, size=11.5, font=T.TITLE_FONT, anchor=MID)
        text(s, 4.52, y + 0.46, 4.75, 0.22, desc, size=8.5, color=T.BODY)
        text(s, 4.52, y + 0.68, 4.75, 0.22, proof, size=7.5, font=T.LABEL_FONT, color=T.PURPLE)
    notes(s, c['notes'])


def s_ask(s):
    c = K.SLIDE_ASK
    title(s, c['title'], 0.6, 0.45, 6.0, 0.6, size=28)
    # left: amount + use of funds
    card(s, 0.6, 1.3, 4.25, 3.72, radius=0.18)
    text(s, 0.85, 1.48, 2.0, 0.24, c['raise_label'], size=9.5, font=T.LABEL_FONT, color=T.PURPLE)
    rect(s, 0.85, 1.76, 3.75, 0.66, fill=T.LAV2, radius=0.12)
    text(s, 0.85, 1.76, 3.75, 0.66, c['amount'], size=20, font=T.TITLE_FONT, color=T.DEEP, align=C, anchor=MID)
    text(s, 0.85, 2.5, 3.8, 0.26, c['round'], size=9.5, color=T.BODY)
    text(s, 0.85, 2.92, 3.8, 0.26, c['funds_title'], size=11.5, font=T.TITLE_FONT)
    for i, (ic, use) in enumerate(c['funds']):
        y = 3.28 + i * 0.42
        icon_circle(s, ic, 0.85, y, 0.32)
        text(s, 1.27, y, 3.4, 0.32, use, size=9.5, anchor=MID)
    # right: milestones
    card(s, 5.1, 1.3, 4.3, 3.72, radius=0.18)
    text(s, 5.35, 1.48, 3.8, 0.3, c['milestones_title'], size=13, font=T.TITLE_FONT)
    for i, m in enumerate(c['milestones']):
        y = 1.95 + i * 0.58
        num_circle(s, i + 1, 5.35, y, 0.38, size=11.5)
        text(s, 5.88, y - 0.04, 3.35, 0.46, m, size=10.5, anchor=MID)
    text(s, 1.2, 5.1, 8.2, 0.26, c['why'], size=8.5, font=T.LABEL_FONT, color=T.INK)
    notes(s, c['notes'])
