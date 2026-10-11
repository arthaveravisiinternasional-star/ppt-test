"""Capture real product screenshots from the live site into assets/shots (needs internet + Chrome).

    python tools/capture_screens.py pages          # landing / choose-world / scan-upload (mobile, EN)
    python tools/capture_screens.py trial whale    # color the whale in Digital Trial -> alive -> world -> story
    python tools/capture_screens.py trial bus      # same for the bus (Vehicle City)

Output names match what tools/make_mockups.py expects. World frames are saved as <kind>_world<i>_<w>.png;
pick the best frame and copy it to the name used in make_mockups.py (e.g. whale_world1_1280.png).
"""
import asyncio
import sys
from pathlib import Path

from playwright.async_api import async_playwright

SHOTS = Path(__file__).resolve().parent.parent / 'assets' / 'shots'
SITE = 'https://scanvas.id'
GPU = ['--enable-gpu', '--use-angle=d3d11', '--ignore-gpu-blocklist', '--enable-unsafe-swiftshader']

# Fill-tool taps as fractions of the coloring canvas (color hex -> points)
PLAN = {
    'whale': [('#2563EB', [(0.43, 0.47), (0.55, 0.45)]), ('#FACC15', [(0.316, 0.617), (0.25, 0.58)]),
              ('#7C3AED', [(0.475, 0.697), (0.712, 0.262), (0.559, 0.343), (0.836, 0.311), (0.367, 0.737)])],
    'bus': [('#FACC15', [(0.453, 0.56), (0.25, 0.56), (0.811, 0.52), (0.5, 0.33), (0.62, 0.56)]),
            ('#2563EB', [(0.189, 0.411), (0.292, 0.411), (0.392, 0.411), (0.491, 0.411), (0.590, 0.411),
                         (0.684, 0.427), (0.684, 0.548)]),
            ('#DC2626', [(0.5, 0.476), (0.5, 0.52)])],
}


async def english(pg):
    await pg.get_by_role('button', name='EN', exact=True).first.click()
    await pg.wait_for_timeout(1200)


async def pages():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        ctx = await b.new_context(viewport={'width': 390, 'height': 844}, device_scale_factor=3, is_mobile=True,
                                  has_touch=True)
        pg = await ctx.new_page()
        await pg.goto(SITE, wait_until='networkidle')
        await english(pg)
        await pg.screenshot(path=str(SHOTS / 'en_home.png'))
        await pg.goto(SITE + '/play', wait_until='networkidle')
        await pg.wait_for_timeout(1500)
        await pg.screenshot(path=str(SHOTS / 'en_play.png'))
        await pg.locator('button, a').filter(has_text='Ocean').first.click()
        await pg.wait_for_timeout(2500)
        await pg.screenshot(path=str(SHOTS / 'en_play2.png'))
        await b.close()


async def trial(kind, W=1280, H=720, scale=2):
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome', args=GPU)
        ctx = await b.new_context(viewport={'width': W, 'height': H}, device_scale_factor=scale, is_mobile=True,
                                  has_touch=True)
        pg = await ctx.new_page()
        shot = lambda tag: pg.screenshot(path=str(SHOTS / f'{kind}_{tag}_{W}.png'))
        await pg.goto(SITE + '/trial', wait_until='networkidle')
        await english(pg)
        await pg.locator('button, a').filter(has_text=f'Color the {kind}').first.click()
        await pg.wait_for_timeout(2500)
        cv = pg.locator('canvas').first
        for color, pts in PLAN[kind]:
            await pg.get_by_role('button', name=f'Color {color}').click()
            await pg.evaluate('window.scrollTo(0,0)')
            bb = await cv.bounding_box()
            for fx, fy in pts:
                await pg.mouse.click(bb['x'] + fx * bb['width'], bb['y'] + fy * bb['height'])
                await pg.wait_for_timeout(350)
        await shot('colored')
        await pg.get_by_role('button', name='Bring my picture to life').click()
        await pg.wait_for_timeout(5000)
        await shot('alive')
        await pg.get_by_role('button', name='Play in a world').click()
        await pg.wait_for_timeout(1500)
        await pg.get_by_role('button', name='Create a new world').click()
        await pg.wait_for_timeout(4000)
        for i in range(10):
            await pg.wait_for_timeout(1800)
            await shot(f'world{i}')
        await pg.goto(pg.url.split('?')[0] + '/story', wait_until='networkidle')
        await pg.wait_for_timeout(4000)
        await shot('story')
        await b.close()


async def scan(sheet, code):
    """Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access code.
    WARNING: this binds `code` to a new world on production. The result screen becomes scan_result_1280.png."""
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        ctx = await b.new_context(viewport={'width': 1280, 'height': 720}, device_scale_factor=2, is_mobile=True,
                                  has_touch=True)
        pg = await ctx.new_page()
        await pg.goto(SITE + '/play', wait_until='networkidle')
        await english(pg)
        await pg.locator('button, a').filter(has_text='Ocean').first.click()
        await pg.wait_for_timeout(3000)
        await pg.locator('input[type=file]').first.set_input_files(sheet)
        await pg.wait_for_timeout(9000)
        ok = pg.get_by_role('button', name='OK')
        if await ok.count():
            await ok.first.click()
        inp = pg.locator('input[type=text]').first
        await inp.scroll_into_view_if_needed()
        await inp.fill(code)
        await pg.locator('button').filter(has_text='Check').first.click(force=True)
        await pg.wait_for_timeout(5000)
        await pg.get_by_role('button', name='Bring my drawing to life').click()
        await pg.wait_for_timeout(10000)
        await pg.screenshot(path=str(SHOTS / 'scan_result_1280.png'))
        print('room:', pg.url)   # open this room on a phone viewport for whale_world_mobile.png
        await b.close()


if __name__ == '__main__':
    SHOTS.mkdir(parents=True, exist_ok=True)
    if sys.argv[1] == 'pages':
        asyncio.run(pages())
    elif sys.argv[1] == 'scan':        # python tools/capture_screens.py scan assets/whale.png <ACCESS_CODE>
        asyncio.run(scan(sys.argv[2], sys.argv[3]))
    else:
        asyncio.run(trial(sys.argv[2]))
