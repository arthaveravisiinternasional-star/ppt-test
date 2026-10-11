"""Colors, fonts, and asset paths shared by every slide."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
TEMPLATE = ASSETS / 'template' / 'freesia_template.pptx'
GEN = ASSETS / 'gen'          # mockups built by tools/make_mockups.py
ICONS = ASSETS / 'icons'      # lucide icons rendered by tools/render_icons.py
LOGO = Path(os.environ.get('SCANVAS_LOGO', 'D:/Personal Bisnis/logo/main.png'))   # env override for other machines
OUTPUT = ROOT / 'output'

# Scanvas design system (website/frontend/DESIGN.md). Violet tints are the ramp of magic-purple.
INK = '172033'          # Tinta Utama
MUTED = '526078'        # Tinta Pendamping (only for deliberately passive/inactive UI)
BODY = INK              # all readable copy uses Tinta Utama
PURPLE = '7C3AED'       # Ungu Keajaiban (magic-purple)
DEEP = '5B21B6'         # Ungu Keajaiban Dalam
VIOLET_500 = '8B5CF6'
VIOLET_400 = 'A78BFA'
VIOLET_300 = 'C4B5FD'
LAV3 = 'DDD6FE'         # violet-200
LAV2 = 'EDE9FE'         # violet-100: chips, selected tint
LAV = 'F5F3FF'          # violet-50
# Soft decoration tier (template blobs): tints of magic-purple, low contrast against canvas
BLOB_MAIN = VIOLET_400  # A78BFA
BLOB_DARK = VIOLET_500  # 8B5CF6
BLOB_LIGHT = VIOLET_300  # C4B5FD (also hatch/dot patterns)
ON_BLOB = INK           # text on a soft-violet slide background (ink on A78BFA = 6:1)
CANVAS = 'F7F8FC'       # Kanvas Tenang: slide background
WHITE = 'FFFFFF'        # Permukaan Putih: cards
BORDER = 'D9DEEA'       # Garis Lembut: card outline
BLUE = '2563EB'         # Biru Petunjuk
YELLOW = 'FACC15'
GREEN = '15803D'
MINT = 'DCFCE7'
PALEY = 'FEF3C7'
AMBER = 'B45309'
AMBER_DARK = '92400E'
SLATE = 'F1F5F9'
SLATE2 = 'E2E8F0'
GRAY = '94A3B8'

# DESIGN.md typography: Fredoka (display/label) + Varela Round (body).
# Static TTFs in assets/fonts (installed per-user; embedded into the PPTX by tools/render.ps1 on --pdf/--embed).
TITLE_FONT = 'Fredoka'            # used with bold=True -> Fredoka Bold (700)
LABEL_FONT = 'Fredoka SemiBold'   # 600
BODY_FONT = 'Varela Round'
BOLD_FONTS = {TITLE_FONT}
FONT_ALIAS = {}   # font token -> typeface written to the file (itec4: 'Roboto Condensed Bold' -> family + bold)

# Template layout per slide (names from the Freesia slide master)
LAYOUT = {
    1: 'TITLE', 2: 'TITLE_ONLY_3_2', 3: 'ONE_COLUMN_TEXT', 4: 'TITLE_ONLY', 5: 'TITLE_ONLY_3_1_1_1',
    6: 'CAPTION_ONLY', 7: 'TITLE_ONLY_2_1', 8: 'BLANK_1_1', 9: 'TITLE_AND_BODY_1_1', 10: 'TITLE_AND_BODY',
    11: 'TITLE_ONLY_3_1_2', 12: 'SECTION_HEADER_1_1',
}
