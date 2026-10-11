"""Build the Founders Arena / DSC Season 17 edition, branched from the Antler edition: same template, look, helpers
and assets; slide order follows the DSC Season 17 pitch deck guideline (14 main slides + appendix).
GESAwards, ITEC and Antler editions are not touched.

    python build_deck_dsc.py                  # -> output/dsc/SCANVAS_DSC_S17.pptx
    python build_deck_dsc.py --render 5 10    # previews in output/dsc/preview
    python build_deck_dsc.py --render --pdf   # final: embed fonts + PDF
"""
import argparse
import subprocess
import sys

from pptx import Presentation

import deck
from deck import content_dsc

sys.modules['deck.content'] = content_dsc   # swap copy before slide modules import it
deck.content = content_dsc

from deck import recolor, slides as S, slides_dsc as D  # noqa: E402
from deck import theme as T  # noqa: E402

OUT_DIR = T.OUTPUT / 'dsc'
OUT = OUT_DIR / 'SCANVAS_DSC_S17.pptx'

# (slide function, Freesia layout) in DSC guideline order
DECK = [(S.s1_cover, 'TITLE'),                      # 1 Cover
        (D.s_overview, 'TITLE_ONLY_3_1_1_1'),       # 2 Business Overview
        (S.s2_problem, 'TITLE_ONLY_3_2'),           # 3 Problem & Opportunity
        (D.s_solution, 'TITLE_ONLY'),               # 4 Solution
        (D.s_market, 'TITLE_AND_BODY_1_1'),         # 5 Market Size & Target Market
        (D.s_competition, 'TITLE_ONLY'),            # 6 Competitive Landscape
        (D.s_business, 'TITLE_AND_BODY'),           # 6 Business Model & Revenue Streams
        (D.s_traction, 'TITLE_ONLY_3_1_2'),         # 7 Traction / Validation
        (D.s_gtm, 'TITLE_ONLY'),                    # 8 Marketing & GTM
        (D.s_impact, 'TITLE_ONLY_2_1'),             # 9 ESG / SDGs / Impact
        (D.s_financial, 'TITLE_AND_BODY'),          # 10 Financial Overview
        (D.s_funding, 'TITLE_ONLY_3_2'),            # 11 Funding Needs & Use of Funds
        (S.s12_team, 'SECTION_HEADER_1_1'),         # 12 Team
        (D.s_roadmap, 'BLANK_1_1'),                 # 13 Milestone & Growth Roadmap
        (D.s_closing, 'CAPTION_ONLY'),              # 14 Closing
        (S.s7_different, 'TITLE_ONLY_2_1'),         # A Technology edge
        (D.s_sources, 'TITLE_ONLY_3_1_2'),          # B Market data sources
        (D.s_pnl, 'TITLE_ONLY_3_2'),                # C 12-month P&L and assumptions
        (D.s_competitors, 'TITLE_ONLY_3_1_2')]      # D Competitor evidence


def build(out=OUT):
    prs = Presentation(str(T.TEMPLATE))
    recolor.apply(prs)
    layouts = {L.name: L for m in prs.slide_masters for L in m.slide_layouts}
    ids = prs.slides._sldIdLst
    for sid in list(ids):
        prs.part.drop_rel(sid.rId)
        ids.remove(sid)
    for fn, layout in DECK:
        s = prs.slides.add_slide(layouts[layout])
        for ph in list(s.placeholders):
            if ph.placeholder_format.idx != 0:
                ph._element.getparent().remove(ph._element)
        fn(s)
    out.parent.mkdir(parents=True, exist_ok=True)
    prs.save(str(out))
    print('saved', out)
    return out


def powerpoint(out, mode, slides=()):
    cmd = ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', str(T.ROOT / 'tools' / 'render.ps1'),
           '-File', str(out), '-Mode', mode, '-Dir', str(OUT_DIR / 'preview')]
    if slides:
        cmd += ['-Slides', ','.join(map(str, slides))]
    subprocess.run(cmd, check=True)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--render', nargs='*', type=int)
    ap.add_argument('--pdf', action='store_true')
    ap.add_argument('--out', help='output .pptx path relative to project root')
    a = ap.parse_args()
    out = build(T.ROOT / a.out if a.out else OUT)
    if a.render is not None:
        powerpoint(out, 'png', a.render)
    if a.pdf:
        powerpoint(out, 'embed')
        powerpoint(out, 'pdf')
