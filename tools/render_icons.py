"""Rasterize lucide icons (from the Scanvas frontend's lucide-react) into assets/icons/<name>_<color>.png.

    python tools/render_icons.py palette rocket     # add icons (then use icon(s, 'rocket', 'purple', ...))
    python tools/render_icons.py                    # re-render everything listed in assets/icons/nodes.json
"""
import asyncio
import json
import subprocess
import sys
from pathlib import Path

from playwright.async_api import async_playwright

ICONS = Path(__file__).resolve().parent.parent / 'assets' / 'icons'
NODES = ICONS / 'nodes.json'
COLORS = {'purple': '#7C3AED', 'white': '#FFFFFF', 'ink': '#172033', 'green': '#15803D', 'gray': '#94A3B8',
          'yellow': '#FACC15', 'deep': '#5B21B6'}
EXTRACT = r"""
const base = 'file:///D:/Personal%20Bisnis/website/frontend/node_modules/lucide-react/dist/esm/icons/';
const out = {};
for (const n of process.argv.slice(1)) {
  const m = await import(base + n + '.js');
  out[n] = m.__iconNode.map(([t, a]) => '<' + t + ' ' + Object.entries(a).filter(([k]) => k !== 'key')
    .map(([k, v]) => `${k}="${v}"`).join(' ') + '/>').join('');
}
console.log(JSON.stringify(out));
"""


async def rasterize(nodes):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 300, 'height': 300})
        for n, inner in nodes.items():
            for cn, c in COLORS.items():
                svg = (f'<svg id="i" xmlns="http://www.w3.org/2000/svg" width="256" height="256" viewBox="0 0 24 24" '
                       f'fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                       f'{inner}</svg>').replace('fill="currentColor"', f'fill="{c}"')
                await pg.set_content(f'<html><body style="margin:0;background:transparent">{svg}</body></html>')
                await pg.locator('#i').screenshot(path=str(ICONS / f'{n}_{cn}.png'), omit_background=True)
        await b.close()


if __name__ == '__main__':
    nodes = json.loads(NODES.read_text()) if NODES.exists() else {}
    new = sys.argv[1:]
    if new:
        r = subprocess.run(['node', '--input-type=module', '-e', EXTRACT, *new], capture_output=True, text=True, check=True)
        add = json.loads(r.stdout)
        nodes.update(add)
        NODES.write_text(json.dumps(nodes))
        asyncio.run(rasterize(add))
    else:
        asyncio.run(rasterize(nodes))
    print(len(nodes), 'icons in', ICONS)
