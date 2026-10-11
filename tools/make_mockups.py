"""Build every image in assets/gen from assets/shots + Scanvas project files.

    python tools/make_mockups.py            # all mockups
    python tools/make_mockups.py lesson     # re-render only the Creative Class lesson mockup
    python tools/make_mockups.py sheet      # re-cut the paper whale from assets/whale.png
    python tools/make_mockups.py founders   # circular founder portraits from assets/founder
"""
import asyncio
import random
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SHOTS = ROOT / 'assets' / 'shots'
GEN = ROOT / 'assets' / 'gen'
BIZ = Path('D:/Personal Bisnis')
FRONT = BIZ / 'website' / 'frontend'


# ---------------------------------------------------------------- primitives
def rr_mask(size, r):
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], r, fill=255)
    return m


def rounded(img, r):
    img = img.convert('RGBA')
    out = Image.new('RGBA', img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), rr_mask(img.size, r))
    return out


def with_shadow(img, blur=28, off=(0, 18), alpha=70, pad=60):
    W, H = img.size
    c = Image.new('RGBA', (W + 2 * pad, H + 2 * pad), (0, 0, 0, 0))
    sh = Image.new('RGBA', c.size, (0, 0, 0, 0))
    shape = Image.new('RGBA', img.size, (23, 32, 51, 255))
    shape.putalpha(img.split()[3].point(lambda v: v * alpha // 255))
    sh.paste(shape, (pad + off[0], pad + off[1]), shape)
    c.alpha_composite(sh.filter(ImageFilter.GaussianBlur(blur)))
    c.alpha_composite(img, (pad, pad))
    return c


def phone(src, out, width=700, centering=(0.5, 0)):
    """Portrait phone frame around a 390x844@3x screenshot (wider shots are cropped at `centering`)."""
    s = ImageOps.fit(Image.open(src).convert('RGB'), (1170, 2532), Image.LANCZOS, centering=centering)
    bez = 46
    W, H = 1170 + 2 * bez, 2532 + 2 * bez
    f = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(f)
    d.rounded_rectangle([0, 0, W - 1, H - 1], 170, fill=(23, 20, 40, 255))
    d.rounded_rectangle([6, 6, W - 7, H - 7], 165, outline=(70, 60, 110, 255), width=4)
    scr = rounded(s, 130)
    f.paste(scr, (bez, bez), scr)
    ImageDraw.Draw(f).rounded_rectangle([W // 2 - 170, bez + 26, W // 2 + 170, bez + 120], 50, fill=(23, 20, 40, 255))
    f = f.resize((width, int(width * H / W)), Image.LANCZOS)
    with_shadow(f, blur=22, off=(0, 14), alpha=80, pad=40).save(GEN / out)


def tablet(src, out, crop=None, size=(1600, 900), width=1100, bez=40):
    """Landscape device frame."""
    s = Image.open(src).convert('RGB')
    if crop:
        s = s.crop(crop)
    s = ImageOps.fit(s, size)
    W, H = size[0] + 2 * bez, size[1] + 2 * bez
    f = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(f).rounded_rectangle([0, 0, W - 1, H - 1], 70, fill=(23, 20, 40, 255))
    scr = rounded(s, 34)
    f.paste(scr, (bez, bez), scr)
    f = f.resize((width, int(width * H / W)), Image.LANCZOS)
    with_shadow(f, blur=24, off=(0, 16), alpha=80, pad=44).save(GEN / out)


def card(src, out, crop=None, r=36, width=1000):
    s = Image.open(src).convert('RGB')
    if crop:
        s = s.crop(crop)
    rounded(s.resize((width, int(width * s.size[1] / s.size[0])), Image.LANCZOS), r).save(GEN / out)


def fitcard(src, out, aspect, r=30, width=900, crop=None, centering=(0.5, 0.5)):
    s = Image.open(src).convert('RGB')
    if crop:
        s = s.crop(crop)
    rounded(ImageOps.fit(s, (width, int(width / aspect)), centering=centering), r).save(GEN / out)


# ---------------------------------------------------------------- colored paper sheet
SHEET = ROOT / 'assets' / 'whale.png'          # real crayon-colored Scanvas whale sheet
SHEET_CROP = (400, 60, 2060, 1680)             # 4 corner markers only; QR + access code (bottom-right) cut off


def real_sheet():
    """Paper visual from the real colored sheet. The crop hides the QR/access code so it never ships in the deck."""
    sheet = Image.open(SHEET).convert('RGB').crop(SHEET_CROP)
    sheet = rounded(sheet.resize((1000, int(1000 * sheet.size[1] / sheet.size[0])), Image.LANCZOS), 10)
    with_shadow(sheet, blur=20, off=(0, 14), alpha=70, pad=50).save(GEN / 'paper_whale.png')
    with_shadow(sheet.rotate(-7, expand=True, resample=Image.BICUBIC), blur=20, off=(0, 14), alpha=70,
                pad=50).save(GEN / 'paper_whale_tilt.png')


# ---------------------------------------------------------------- founder portraits (slide 12)
FOUNDERS = ROOT / 'assets' / 'founder'
# Matches the user's own edit of slide 12 (2026-09-14): white-background photos, ellipse crop, no ring.
# source file -> (crop fractions left, top, right, bottom as in PowerPoint's srcRect, output name)
PORTRAITS = {'salsa_whitebg.jpg': ((0.0, 0.0, 0.0, 0.19355), 'founder_sk.png'),
             'haikal-hilmi-profile - Copy.jpg': ((0.20901, 0.07336, 0.22348, 0.32182), 'founder_hh.png')}


def founders():
    """Ellipse-masked portraits on transparent background (the white photo backgrounds melt into the white card)."""
    for src, ((l, t, r, b), out) in PORTRAITS.items():
        im = ImageOps.exif_transpose(Image.open(FOUNDERS / src)).convert('RGBA')
        W, H = im.size
        im = im.crop((round(W * l), round(H * t), round(W * (1 - r)), round(H * (1 - b))))
        m = Image.new('L', im.size, 0)
        ImageDraw.Draw(m).ellipse([0, 0, im.size[0] - 1, im.size[1] - 1], fill=255)
        im.putalpha(m)
        im.save(GEN / out)


def colored_sheet():
    """Flood-fill the real Scanvas whale sheet (template A) in the same colors used in the live demo."""
    im = Image.open(BIZ / 'templates' / 'A.png').convert('RGBA')
    bg = Image.new('RGBA', im.size, 'white')
    bg.alpha_composite(im)
    g = bg.convert('L').point(lambda v: 0 if v < 160 else 255).convert('RGB')
    purple, yellow, dark = (139, 92, 246), (250, 204, 21), (109, 40, 217)
    seeds = [((500, 420), purple), ((640, 420), purple)] + \
            [(p, yellow) for p in [(380, 525), (420, 545), (470, 562), (300, 510), (560, 535), (350, 530), (265, 488)]] + \
            [(p, dark) for p in [(600, 600), (490, 605), (930, 320), (830, 270), (670, 330), (540, 505)]]
    for (x, y), col in seeds:                      # seeds measured on a half-size preview
        if g.getpixel((x * 2, y * 2)) == (255, 255, 255):
            ImageDraw.floodfill(g, (x * 2, y * 2), col, thresh=40)
    random.seed(3)
    noise = Image.effect_noise(g.size, 40).convert('L').filter(ImageFilter.GaussianBlur(1.2))
    noise = noise.point(lambda v: 200 + int(v * 55 / 255))
    tex = Image.merge('RGB', (noise, noise, noise))
    mask = ImageChops.difference(g, Image.new('RGB', g.size, 'white')).convert('L').point(lambda v: 255 if v > 30 else 0)
    g = Image.composite(ImageChops.multiply(g, tex), g, mask)
    g = ImageChops.multiply(g, Image.new('RGB', g.size, (253, 252, 248)))
    sheet = g.crop((380, 40, 2100, 1710))
    sheet = rounded(sheet.resize((1000, int(1000 * sheet.size[1] / sheet.size[0]))), 10)
    with_shadow(sheet, blur=20, off=(0, 14), alpha=70, pad=50).save(GEN / 'paper_whale.png')
    with_shadow(sheet.rotate(-7, expand=True, resample=Image.BICUBIC), blur=20, off=(0, 14), alpha=70,
                pad=50).save(GEN / 'paper_whale_tilt.png')


# ---------------------------------------------------------------- lesson mockup (HTML -> PNG)
def lesson():
    from playwright.async_api import async_playwright
    guide = Image.open(FRONT / 'public/trial/digital/paus.png').convert('RGBA')
    b = Image.new('RGBA', guide.size, (255, 255, 255, 255))
    b.alpha_composite(guide)
    a = b.convert('L').point(lambda v: 0 if v > 150 else 255)
    g = Image.new('RGBA', guide.size, (196, 181, 253, 0))
    g.putalpha(a)
    g.save(GEN / 'whale_guide.png')
    html = (ROOT / 'tools' / 'lesson_mockup.html').read_text(encoding='utf-8')
    html = html.replace('LOGO', (BIZ / 'logo/main.png').as_uri()).replace('GUIDE', (GEN / 'whale_guide.png').as_uri()) \
               .replace('WORLD', (GEN / 'alive_whale.png').as_uri()).replace('TRACE', (FRONT / 'public/trial/digital/paus.png').as_uri())
    tmp = ROOT / 'tools' / '_lesson_render.html'
    tmp.write_text(html, encoding='utf-8')

    async def run():
        async with async_playwright() as p:
            br = await p.chromium.launch()
            pg = await br.new_page(viewport={'width': 1200, 'height': 860}, device_scale_factor=1.5)
            await pg.goto(tmp.as_uri(), wait_until='networkidle')
            await pg.wait_for_timeout(800)
            await pg.screenshot(path=str(SHOTS / 'lesson.png'))
            await br.close()
    asyncio.run(run())
    tmp.unlink()
    tablet(SHOTS / 'lesson.png', 'tab_lesson.png', size=(1600, 1147))
    fitcard(SHOTS / 'lesson.png', 'm_lesson.png', 2.8 / 1.4, centering=(0.3, 0.4))


def all_mockups():
    GEN.mkdir(parents=True, exist_ok=True)
    real_sheet()             # colored_sheet() = old digital flood-fill version
    # blue crayon whale (assets/whale.png) scanned on live scanvas.id -> result screen + world
    card(SHOTS / 'scan_result_1280.png', 'alive_whale.png', crop=(330, 430, 1330, 1000), width=900)
    tablet(SHOTS / 'scan_result_1280.png', 'tab_result.png')
    card(SHOTS / 'bus_alive_1280.png', 'alive_bus.png', crop=(512, 36, 2048, 996))
    for src, out in [('en_home', 'ph_home'), ('en_play', 'ph_play'), ('en_play2', 'ph_scan'),
                     ('x_trial_color', 'ph_color')]:
        phone(SHOTS / f'{src}.png', f'{out}.png')
    # whale swimming in Ocean world (user screenshot, 633x855): crop centred on the whale, hides dev badge
    phone(SHOTS / 'whale_world_phone.png', 'ph_world.png', centering=(0.8, 0))
    tablet(SHOTS / 'bus_world8_1280.png', 'tab_world_bus.png')
    tablet(SHOTS / 'bus_colored_1280.png', 'tab_color_bus.png')
    tablet(FRONT / '.codex-tmp/studio-desktop.png', 'tab_studio.png', crop=(0, 0, 1440, 900), size=(1600, 1000))
    fitcard(FRONT / 'public/shop/aquarium.png', 'm_pack.png', 2.8 / 1.4)
    fitcard(FRONT / '.codex-tmp/studio-desktop.png', 'm_studio.png', 2.8 / 1.4, crop=(0, 0, 1440, 820), centering=(0, 0))
    fitcard(FRONT / 'public/homepage.png', 'm_kidcolor.png', 1.55 / 1.35, crop=(0, 215, 1160, 840), r=26, width=700)
    founders()
    lesson()
    print('mockups ->', GEN)


if __name__ == '__main__':
    {'lesson': lesson, 'sheet': real_sheet, 'founders': founders}.get((sys.argv[1:] or [''])[0], all_mockups)()
