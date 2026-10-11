# Graph Report - PPT  (2026-09-14)

## Corpus Check
- 18 files · ~11,750 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 123 nodes · 327 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- content.py
- helpers.py
- recolor.py
- s2_problem
- capture_screens.py
- chip
- Arrow Chip Rows
- slides.py
- s1_cover
- rect

## God Nodes (most connected - your core abstractions)
1. `text()` - 22 edges
2. `title()` - 21 edges
3. `chip()` - 19 edges
4. `notes()` - 17 edges
5. `rect()` - 15 edges
6. `card()` - 12 edges
7. `pic()` - 12 edges
8. `s12_team()` - 12 edges
9. `num_circle()` - 11 edges
10. `oval()` - 10 edges

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

## Communities (12 total, 1 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.22
Nodes (18): all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone(), Build every image in assets/gen from assets/shots + Scanvas project files.… (+10 more)

### Community 1 - "content.py"
Cohesion: 0.14
Nodes (16): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow), SLIDE_5_PRODUCT copy (Product today (live)) (+8 more)

### Community 2 - "helpers.py"
Cohesion: 0.31
Nodes (10): _frame(), Thin python-pptx helpers. All coordinates are inches on the 10 x 5.625 in…, Add styled run(s); a newline inside t becomes a soft line break, arrows use…, paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, Fill the layout's own title placeholder (keeps slide outline / accessibility)., rgb(), _run(), text() (+2 more)

### Community 3 - "recolor.py"
Cohesion: 0.10
Nodes (16): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout,…, powerpoint(), Build the SCANVAS GESAwards 2026 pitch deck from the Freesia template. python…, Antler (pre-seed VC) edition of the deck copy. Built by build_deck_antler.py,…, ITEC SEA 2026 · Digital Culture Track edition of the deck copy (same layout as… (+8 more)

### Community 4 - "s2_problem"
Cohesion: 0.50
Nodes (5): arrow_chips(), icon(), color: purple | white | ink | green | gray | yellow | deep, Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s2_problem()

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 6 - "chip"
Cohesion: 0.40
Nodes (10): chip(), chip_width(), icon_circle(), notes(), Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., Investor-only slides for the Antler edition (market sizing, the ask). Same…, s_market(), s3_insight() (+2 more)

### Community 8 - "slides.py"
Cohesion: 0.38
Nodes (10): img_size(), num_circle(), oval(), pic(), path: file name inside assets/gen, or an absolute Path., One function per slide: layout only. Copy comes from content.py, colors/fonts…, s10_market(), s12_team() (+2 more)

### Community 9 - "s1_cover"
Cohesion: 0.67
Nodes (3): SLIDE_1_COVER copy (Cover), TRACK / WEBSITE constants, s1_cover()

### Community 12 - "rect"
Cohesion: 0.60
Nodes (5): card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., rect(), s_ask(), s11_validation()

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `content.py`?**
  _High betweenness centrality (0.252) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `content.py` to `slides.py`, `helpers.py`, `recolor.py`?**
  _High betweenness centrality (0.199) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `content.py` to `slides.py`, `helpers.py`, `s2_problem`, `chip`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `content.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13725490196078433 - nodes in this community are weakly interconnected._
- **Should `recolor.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10461538461538461 - nodes in this community are weakly interconnected._