# Graph Report - PPT  (2026-10-04)

## Corpus Check
- 31 files · ~30,263 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 217 nodes · 806 edges · 13 communities (11 shown, 2 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- slides.py
- text
- theme.py
- make_pilot_art.py
- capture_screens.py
- slides_itec3.py
- Arrow Chip Rows
- rect
- title
- notes
- slides_dsc.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 75 edges
2. `title()` - 64 edges
3. `rect()` - 60 edges
4. `notes()` - 59 edges
5. `chip()` - 49 edges
6. `card()` - 44 edges
7. `pic()` - 34 edges
8. `icon_circle()` - 29 edges
9. `icon()` - 28 edges
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

### Community 1 - "slides.py"
Cohesion: 0.10
Nodes (32): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow) (+24 more)

### Community 2 - "text"
Cohesion: 0.19
Nodes (16): chip(), _frame(), Inches(), Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), s_overview(), s_solution() (+8 more)

### Community 3 - "theme.py"
Cohesion: 0.06
Nodes (26): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,…, build() (+18 more)

### Community 5 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 6 - "slides_itec3.py"
Cohesion: 0.27
Nodes (9): arrow_chips(), Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., Slides specific to the ITEC SEA 2026 final (v3) edition. Visual base = v2…, Same content as slides_dsc.s_traction, re-laid out: metrics + feedback left,…, s_cover(), s_pipeline(), s_problem(), s_solution() (+1 more)

### Community 8 - "rect"
Cohesion: 0.22
Nodes (16): rect(), _flow(), s_repeat(), _alpha(), Slides for the ITEC SEA 2026 official-template edition (v4). Coordinates stay…, slides.s5_product re-spaced to clear the template's top bar, plus the TRY IT…, s_ask(), s_competition() (+8 more)

### Community 9 - "title"
Cohesion: 0.20
Nodes (16): card(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., Fill the layout's own title placeholder (keeps slide outline / accessibility)., title(), s_ask(), s_business(), s_closing(), s_competitors() (+8 more)

### Community 11 - "notes"
Cohesion: 0.27
Nodes (13): icon(), notes(), color: purple | white | ink | green | gray | yellow | deep, s_competition(), s_impact(), s_roadmap(), s_business(), s_next() (+5 more)

### Community 12 - "slides_dsc.py"
Cohesion: 0.14
Nodes (21): _background(), build(), Build the ITEC SEA 2026 official-template edition (v4) on the committee's…, chip_width(), icon_circle(), oval(), Pt(), Thin python-pptx helpers. All coordinates are inches on the 10 x 5.625 in… (+13 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **2 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `slides.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `slides.py` to `theme.py`, `slides_dsc.py`?**
  _High betweenness centrality (0.123) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `slides.py` to `make_mockups.py`, `text`, `slides_itec3.py`, `title`, `notes`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `slides.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09759759759759759 - nodes in this community are weakly interconnected._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06183574879227053 - nodes in this community are weakly interconnected._
- **Should `slides_dsc.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14461538461538462 - nodes in this community are weakly interconnected._