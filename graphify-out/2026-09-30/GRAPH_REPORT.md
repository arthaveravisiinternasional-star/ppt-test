# Graph Report - PPT  (2026-09-29)

## Corpus Check
- 28 files · ~26,117 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 190 nodes · 671 edges · 13 communities (11 shown, 2 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- content.py
- icon
- theme.py
- make_pilot_art.py
- capture_screens.py
- slides.py
- Arrow Chip Rows
- rect
- title
- card
- text

## God Nodes (most connected - your core abstractions)
1. `text()` - 61 edges
2. `title()` - 52 edges
3. `notes()` - 48 edges
4. `rect()` - 46 edges
5. `chip()` - 39 edges
6. `card()` - 37 edges
7. `pic()` - 25 edges
8. `icon_circle()` - 24 edges
9. `icon()` - 23 edges
10. `num_circle()` - 18 edges

## Surprising Connections (you probably didn't know these)
- `Creative Class lesson mockup (HTML template)` --conceptually_related_to--> `s9_class()`  [INFERRED]
  tools/lesson_mockup.html → deck/slides.py
- `Build commands (--render N, --pdf)` --references--> `build()`  [EXTRACTED]
  README.md → build_deck.py
- `Build commands (--render N, --pdf)` --references--> `powerpoint()`  [EXTRACTED]
  README.md → build_deck.py
- `Honesty rules: live vs roadmap, [X]/[TBD] placeholders` --references--> `SLIDE_10_MARKET copy (Market & business model)`  [EXTRACTED]
  README.md → deck/content.py
- `Honesty rules: live vs roadmap, [X]/[TBD] placeholders` --references--> `SLIDE_11_VALIDATION copy (Validation & roadmap)`  [EXTRACTED]
  README.md → deck/content.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Asset generation flow** — tools_capture_screens, tools_make_mockups, tools_render_icons, tools_lesson_mockup [EXTRACTED 1.00]
- **Deck build pipeline** — build_deck_build, deck_slides, deck_content, deck_theme, deck_helpers [EXTRACTED 1.00]

## Communities (13 total, 2 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.21
Nodes (19): Creative Class lesson mockup (HTML template), all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone() (+11 more)

### Community 1 - "content.py"
Cohesion: 0.15
Nodes (15): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow), SLIDE_5_PRODUCT copy (Product today (live)) (+7 more)

### Community 2 - "icon"
Cohesion: 0.40
Nodes (5): icon(), color: purple | white | ink | green | gray | yellow | deep, s_competition(), s_roadmap(), s_next()

### Community 3 - "theme.py"
Cohesion: 0.06
Nodes (25): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,…, build() (+17 more)

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 6 - "slides.py"
Cohesion: 0.16
Nodes (25): SLIDE_12_TEAM copy (Team & closing), SLIDE_7_DIFFERENT copy (Differentiators), TRACK / WEBSITE constants, chip(), chip_width(), _frame(), img_size(), num_circle() (+17 more)

### Community 8 - "rect"
Cohesion: 0.19
Nodes (20): pic(), path: file name inside assets/gen, or an absolute Path., rect(), s_business(), s_closing(), s_live(), _art_row(), _flow() (+12 more)

### Community 9 - "title"
Cohesion: 0.25
Nodes (16): icon_circle(), notes(), Fill the layout's own title placeholder (keeps slide outline / accessibility)., title(), s_impact(), s_market(), s_overview(), Slides specific to the ITEC SEA 2026 Top 30 (v2) edition. Same helpers and look… (+8 more)

### Community 11 - "card"
Cohesion: 0.33
Nodes (9): arrow_chips(), card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s_gtm(), s_traction(), s_problem(), s_pipeline() (+1 more)

### Community 12 - "text"
Cohesion: 0.30
Nodes (11): paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), _is_placeholder(), Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and…, Number tile: real value = violet, founder-supplied placeholder = yellow., s_competitors(), s_financial(), s_funding() (+3 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `content.py`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `content.py` to `theme.py`, `slides.py`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `title` to `make_mockups.py`, `content.py`, `slides.py`, `rect`, `card`, `text`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `content.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14705882352941177 - nodes in this community are weakly interconnected._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06342494714587738 - nodes in this community are weakly interconnected._