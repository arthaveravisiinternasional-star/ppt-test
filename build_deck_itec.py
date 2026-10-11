"""Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout, and assets as build_deck.py,
with copy from deck/content_itec.py. The GESAwards edition (build_deck.py / deck/content.py) is not touched.

    python build_deck_itec.py                  # -> output/itec/SCANVAS_ITEC_SEA2026.pptx
    python build_deck_itec.py --render 7 10    # previews in output/itec/preview
    python build_deck_itec.py --render --pdf   # final: embed fonts + PDF
"""
import argparse
import subprocess
import sys

import deck
from deck import content_itec

# swap the copy module before deck.slides imports it
sys.modules['deck.content'] = content_itec
deck.content = content_itec

import build_deck  # noqa: E402  (imports deck.slides, which now reads content_itec)
from deck import theme as T  # noqa: E402

OUT_DIR = T.OUTPUT / 'itec'
OUT = OUT_DIR / 'SCANVAS_ITEC_SEA2026.pptx'


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
    out = build_deck.build(T.ROOT / a.out if a.out else OUT)
    if a.render is not None:
        powerpoint(out, 'png', a.render)
    if a.pdf:
        powerpoint(out, 'embed')
        powerpoint(out, 'pdf')
