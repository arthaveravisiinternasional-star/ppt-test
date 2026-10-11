# Graph Report - PPT  (2026-09-27)

## Corpus Check
- 24 files · ~21,092 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 165 nodes · 549 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- slides.py
- theme.py
- text
- capture_screens.py
- chip
- Arrow Chip Rows
- notes
- rect
- icon_circle
- slides_dsc.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 47 edges
2. `title()` - 43 edges
3. `notes()` - 39 edges
4. `rect()` - 34 edges
5. `chip()` - 32 edges
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

## Communities (12 total, 1 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.21
Nodes (19): Creative Class lesson mockup (HTML template), all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone() (+11 more)

### Community 1 - "slides.py"
Cohesion: 0.11
Nodes (22): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow) (+14 more)

### Community 3 - "theme.py"
Cohesion: 0.07
Nodes (22): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,…, Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout,… (+14 more)

### Community 4 - "text"
Cohesion: 0.35
Nodes (12): num_circle(), paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, Fill the layout's own title placeholder (keeps slide outline / accessibility)., text(), title(), s_ask(), s_competitors(), s_market() (+4 more)

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 6 - "chip"
Cohesion: 0.24
Nodes (14): chip(), chip_width(), _frame(), oval(), Thin python-pptx helpers. All coordinates are inches on the 10 x 5.625 in…, Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., Add styled run(s); a newline inside t becomes a soft line break, arrows use…, rgb() (+6 more)

### Community 8 - "notes"
Cohesion: 0.39
Nodes (8): notes(), pic(), path: file name inside assets/gen, or an absolute Path., s_business(), s_closing(), s_overview(), s10_market(), s2_problem()

### Community 9 - "rect"
Cohesion: 0.33
Nodes (8): rect(), Slides specific to the ITEC SEA 2026 Top 30 (v2) edition. Same helpers and look…, s_business(), s_culture(), s_live(), s_market(), s_next(), s_pipeline()

### Community 11 - "icon_circle"
Cohesion: 0.29
Nodes (10): arrow_chips(), icon(), icon_circle(), color: purple | white | ink | green | gray | yellow | deep, Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s_gtm(), s_impact(), s_roadmap() (+2 more)

### Community 12 - "slides_dsc.py"
Cohesion: 0.29
Nodes (11): card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., _is_placeholder(), Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and…, Number tile: real value = violet, founder-supplied placeholder = yellow., s_competition(), s_financial(), s_funding() (+3 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `slides.py`?**
  _High betweenness centrality (0.179) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `slides.py` to `theme.py`, `chip`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `text` to `make_mockups.py`, `slides.py`, `chip`, `notes`, `icon_circle`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `slides.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11333333333333333 - nodes in this community are weakly interconnected._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07112375533428165 - nodes in this community are weakly interconnected._