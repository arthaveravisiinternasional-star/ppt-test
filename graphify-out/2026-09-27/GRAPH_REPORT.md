# Graph Report - PPT  (2026-09-27)

## Corpus Check
- 24 files · ~20,993 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 165 nodes · 552 edges · 13 communities (12 shown, 1 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- content.py
- notes
- theme.py
- title
- capture_screens.py
- helpers.py
- Arrow Chip Rows
- slides.py
- text
- icon
- slides_dsc.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 48 edges
2. `title()` - 43 edges
3. `notes()` - 39 edges
4. `rect()` - 35 edges
5. `chip()` - 33 edges
6. `card()` - 29 edges
7. `pic()` - 20 edges
8. `icon_circle()` - 20 edges
9. `icon()` - 17 edges
10. `num_circle()` - 15 edges

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

## Communities (13 total, 1 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.21
Nodes (19): Creative Class lesson mockup (HTML template), all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone() (+11 more)

### Community 1 - "content.py"
Cohesion: 0.15
Nodes (15): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow), SLIDE_5_PRODUCT copy (Product today (live)) (+7 more)

### Community 2 - "notes"
Cohesion: 0.36
Nodes (13): chip(), icon_circle(), notes(), Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., s_gtm(), s_impact(), s_overview(), s_roadmap() (+5 more)

### Community 3 - "theme.py"
Cohesion: 0.07
Nodes (22): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,…, Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout,… (+14 more)

### Community 4 - "title"
Cohesion: 0.31
Nodes (15): card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., Fill the layout's own title placeholder (keeps slide outline / accessibility)., rect(), title(), s_ask(), s_business(), s_competition() (+7 more)

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 6 - "helpers.py"
Cohesion: 0.18
Nodes (16): SLIDE_12_TEAM copy (Team & closing), SLIDE_7_DIFFERENT copy (Differentiators), TRACK / WEBSITE constants, chip_width(), num_circle(), oval(), Thin python-pptx helpers. All coordinates are inches on the 10 x 5.625 in…, Add styled run(s); a newline inside t becomes a soft line break, arrows use… (+8 more)

### Community 8 - "slides.py"
Cohesion: 0.32
Nodes (7): pic(), path: file name inside assets/gen, or an absolute Path., s_closing(), s_live(), One function per slide: layout only. Copy comes from content.py, colors/fonts…, s10_market(), s1_cover()

### Community 9 - "text"
Cohesion: 0.38
Nodes (6): _frame(), paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), Slides specific to the ITEC SEA 2026 Top 30 (v2) edition. Same helpers and look…, s_market(), s_tech()

### Community 11 - "icon"
Cohesion: 0.32
Nodes (8): arrow_chips(), icon(), color: purple | white | ink | green | gray | yellow | deep, Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s_traction(), s_problem(), s2_problem(), s9_class()

### Community 12 - "slides_dsc.py"
Cohesion: 0.43
Nodes (6): _is_placeholder(), Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and…, Number tile: real value = violet, founder-supplied placeholder = yellow., s_financial(), s_funding(), value_tile()

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `content.py`?**
  _High betweenness centrality (0.179) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `content.py` to `slides.py`, `theme.py`, `helpers.py`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `icon` to `make_mockups.py`, `content.py`, `notes`, `title`, `helpers.py`, `slides.py`, `text`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `content.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14705882352941177 - nodes in this community are weakly interconnected._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07112375533428165 - nodes in this community are weakly interconnected._