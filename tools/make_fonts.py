"""Cut static TTFs from Google Fonts variable fonts in assets/fonts (PowerPoint embeds statics, not variable fonts).

    python tools/make_fonts.py   # Roboto Condensed Regular / Bold (one family) + 'Roboto Condensed SemiBold'

Source: github.com/google/fonts ofl/robotocondensed (OFL, license in assets/fonts/OFL-robotocondensed.txt).
"""
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

FONTS = Path(__file__).resolve().parent.parent / 'assets' / 'fonts'
SRC = FONTS / 'RobotoCondensed[wght].ttf'
# (weight, family, style, file)
CUTS = [(400, 'Roboto Condensed', 'Regular', 'RobotoCondensed-Regular.ttf'),
        (700, 'Roboto Condensed', 'Bold', 'RobotoCondensed-Bold.ttf'),
        (600, 'Roboto Condensed SemiBold', 'Regular', 'RobotoCondensed-SemiBold.ttf')]


def cut(weight, family, style, out):
    f = instantiateVariableFont(TTFont(SRC), {'wght': weight})
    full = f'{family} {style}' if style != 'Regular' else family
    ps = (family.replace(' ', '') + '-' + style).replace('SemiBold-Regular', '-SemiBold')
    name = f['name']
    for nid in (16, 17, 21, 22, 25):          # drop typographic/variation names so Office sees plain RIBBI
        name.removeNames(nameID=nid)
    for nid, val in ((1, family), (2, style), (3, f'{ps};static'), (4, full), (6, ps)):
        name.setName(val, nid, 3, 1, 0x409)
        name.setName(val, nid, 1, 0, 0)
    os2 = f['OS/2']
    os2.usWeightClass = weight
    bold = style == 'Bold'
    os2.fsSelection = (os2.fsSelection & ~0b1100001) | (0b100000 if bold else 0b1000000)
    f['head'].macStyle = 1 if bold else 0
    f.save(FONTS / out)
    print('saved', FONTS / out, '|', family, style)


if __name__ == '__main__':
    for c in CUTS:
        cut(*c)
