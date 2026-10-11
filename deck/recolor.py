"""Re-skin the Freesia template with the Scanvas design system (website/frontend/DESIGN.md).

Runs at build time on the loaded Presentation, so the template file stays untouched:
- theme color scheme -> Scanvas violet ramp + ink (blobs pick these up through schemeClr)
- layout hatch/dot patterns (template dark green `dk1`) -> magic-purple-deep
- white slide backgrounds -> Kanvas Tenang (canvas)
"""
import io
import re

import numpy as np
from PIL import Image
from pptx.opc.constants import RELATIONSHIP_TYPE as RT
from pptx.oxml.ns import qn

from . import theme as T

# Freesia theme slot -> Scanvas DESIGN.md token ("purple + neutral": only magic-purple, its deep
# hover shade, and DESIGN neutrals; no invented tints)
THEME_SLOTS = {
    'dk1': T.INK,              # was 043403 dark green
    'lt1': T.BLOB_DARK,        # was 6238CE
    'dk2': T.BORDER,           # was A586FA light blob
    'lt2': T.BORDER,           # was EAD7FF lightest blob
    'accent1': T.BLOB_MAIN,    # was 8E2EF1 main blob + purple slide background
    'accent2': T.BLOB_DARK,    # was 541CBB dark blob
    'accent3': T.BLOB_LIGHT,   # was A677FC mid blob
    'accent4': T.BORDER,       # was BA84EE light blob
    'accent5': T.BLOB_LIGHT,   # was 9F34F5 mid blob
    'accent6': T.BORDER,       # was B29CF0 light blob
    'hlink': T.BLUE,
}
PATTERN_FROM, PATTERN_TO = 'dk1', 'accent3'   # decorative hatches/dots only (inside cSld shapes)
PATTERN_RGB = tuple(int(T.BLOB_LIGHT[i:i + 2], 16) for i in (0, 2, 4))   # PNG textures -> soft violet


def _recolor_theme(master):
    part = master.part.part_related_by(RT.THEME)
    xml = part.blob.decode('utf-8')
    for slot, hexv in THEME_SLOTS.items():
        xml = re.sub(rf'(<a:{slot}>)\s*<a:(?:srgbClr|sysClr)[^>]*?/>', rf'\1<a:srgbClr val="{hexv}"/>', xml, count=1)
    part._blob = xml.encode('utf-8')


def _recolor_tree(el):
    csld = el.find(qn('p:cSld'))
    for c in csld.iter(qn('a:schemeClr')):
        if c.get('val') == PATTERN_FROM:
            c.set('val', PATTERN_TO)
    bg = csld.find(qn('p:bg'))
    if bg is not None:
        for c in bg.iter(qn('a:srgbClr')):
            if c.get('val').upper() == 'FFFFFF':
                c.set('val', T.CANVAS)


def _recolor_pattern_images(part, done):
    """Hatch/dot textures are PNGs painted template dark green (#003300). Repaint dark pixels
    in PATTERN_RGB and keep alpha; white hatches stay white."""
    for rel in part.rels.values():
        if rel.reltype != RT.IMAGE or rel.is_external:
            continue
        img = rel.target_part
        if img.partname in done:
            continue
        done.add(img.partname)
        a = np.array(Image.open(io.BytesIO(img.blob)).convert('RGBA'))
        dark = (a[..., 3] > 0) & (a[..., :3].max(axis=2) < 110)
        if not dark.any():
            continue
        a[dark, :3] = PATTERN_RGB
        buf = io.BytesIO()
        Image.fromarray(a).save(buf, 'PNG', optimize=True)
        img._blob = buf.getvalue()


def apply(prs):
    done = set()
    for master in prs.slide_masters:
        _recolor_theme(master)
        _recolor_tree(master._element)
        _recolor_pattern_images(master.part, done)
        for layout in master.slide_layouts:
            _recolor_tree(layout._element)
            _recolor_pattern_images(layout.part, done)
