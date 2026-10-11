# Graph Report - PPT  (2026-09-15)

## Corpus Check
- 21 files · ~16,710 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 147 nodes · 455 edges · 11 communities (10 shown, 1 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- content.py
- slides.py
- theme.py
- title
- capture_screens.py
- Arrow Chip Rows
- notes
- text
- slides_dsc.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 37 edges
2. `title()` - 34 edges
3. `notes()` - 30 edges
4. `chip()` - 27 edges
5. `rect()` - 24 edges
6. `card()` - 22 edges
7. `icon_circle()` - 17 edges
8. `pic()` - 16 edges
9. `oval()` - 13 edges
10. `num_circle()` - 13 edges

## Surprising Connections (you probably didn't know these)
- `Creative Class lesson mockup (HTML template)` --conceptually_related_to--> `s9_class()`  [INFERRED]
  tools/lesson_mockup.html → deck/slides.py
- `Build commands (--render N, --pdf)` --references--> `build()`  [EXTRACTED]
  README.md → build_deck.py
- `Build commands (--render N, --pdf)` --references--> `powerpoint()`  [EXTRACTED]
  README.md → build_deck.py
- `lesson()` --references--> `Creative Class lesson mockup (HTML template)`  [EXTRACTED]
  tools/make_mockups.py → tools/lesson_mockup.html
- `Honesty rules: live vs roadmap, [X]/[TBD] placeholders` --references--> `SLIDE_10_MARKET copy (Market & business model)`  [EXTRACTED]
  README.md → deck/content.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Asset generation flow** — tools_capture_screens, tools_make_mockups, tools_render_icons, tools_lesson_mockup [EXTRACTED 1.00]
- **Deck build pipeline** — build_deck_build, deck_slides, deck_content, deck_theme, deck_helpers [EXTRACTED 1.00]

## Communities (11 total, 1 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.22
Nodes (18): all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone(), Build every image in assets/gen from assets/shots + Scanvas project files.… (+10 more)

### Community 1 - "content.py"
Cohesion: 0.16
Nodes (14): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow) (+6 more)

### Community 2 - "slides.py"
Cohesion: 0.17
Nodes (25): arrow_chips(), chip(), chip_width(), _frame(), icon(), icon_circle(), img_size(), oval() (+17 more)

### Community 3 - "theme.py"
Cohesion: 0.08
Nodes (20): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout,…, powerpoint(), Build the SCANVAS GESAwards 2026 pitch deck from the Freesia template. python… (+12 more)

### Community 4 - "title"
Cohesion: 0.36
Nodes (8): card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., Fill the layout's own title placeholder (keeps slide outline / accessibility)., title(), s_gtm(), s_impact(), s_market(), s_traction()

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 8 - "notes"
Cohesion: 0.33
Nodes (10): TRACK / WEBSITE constants, notes(), pic(), path: file name inside assets/gen, or an absolute Path., s_business(), s_overview(), s10_market(), s12_team() (+2 more)

### Community 9 - "text"
Cohesion: 0.48
Nodes (7): num_circle(), paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), s_ask(), s11_validation(), s4_solution(), s7_different()

### Community 12 - "slides_dsc.py"
Cohesion: 0.30
Nodes (11): rect(), _is_placeholder(), Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and…, Number tile: real value = violet, founder-supplied placeholder = yellow., s_closing(), s_financial(), s_funding(), s_pnl() (+3 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `theme.py`?**
  _High betweenness centrality (0.204) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `theme.py` to `content.py`, `slides.py`?**
  _High betweenness centrality (0.171) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `slides.py` to `notes`, `content.py`, `title`, `text`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._