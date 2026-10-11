# Graph Report - PPT  (2026-09-11)

## Corpus Check
- 13 files · ~7,598 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 108 nodes · 281 edges · 13 communities (12 shown, 1 thin omitted)
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- content.py
- s9_class
- recolor.py
- text
- capture_screens.py
- chip
- Arrow Chip Rows
- slides.py
- pic
- helpers.py
- s12_team

## God Nodes (most connected - your core abstractions)
1. `text()` - 19 edges
2. `title()` - 18 edges
3. `chip()` - 17 edges
4. `notes()` - 14 edges
5. `rect()` - 13 edges
6. `pic()` - 12 edges
7. `s12_team()` - 12 edges
8. `s1_cover()` - 10 edges
9. `s2_problem()` - 10 edges
10. `s3_insight()` - 10 edges

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
Cohesion: 0.18
Nodes (13): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow), SLIDE_5_PRODUCT copy (Product today (live)) (+5 more)

### Community 2 - "s9_class"
Cohesion: 0.40
Nodes (5): arrow_chips(), icon(), color: purple | white | ink | green | gray | yellow | deep, Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s9_class()

### Community 3 - "recolor.py"
Cohesion: 0.14
Nodes (14): build(), powerpoint(), Build the SCANVAS GESAwards 2026 pitch deck from the Freesia template. python…, apply(), Re-skin the Freesia template with the Scanvas design system…, Hatch/dot textures are PNGs painted template dark green (#003300). Repaint dark…, _recolor_pattern_images(), _recolor_theme() (+6 more)

### Community 4 - "text"
Cohesion: 0.32
Nodes (8): SLIDE_1_COVER copy (Cover), TRACK / WEBSITE constants, _frame(), paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, Fill the layout's own title placeholder (keeps slide outline / accessibility)., text(), title(), s1_cover()

### Community 5 - "capture_screens.py"
Cohesion: 0.43
Nodes (6): english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial()

### Community 6 - "chip"
Cohesion: 0.44
Nodes (9): chip(), chip_width(), icon_circle(), notes(), Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., s3_insight(), s5_product(), s6_magic() (+1 more)

### Community 8 - "slides.py"
Cohesion: 0.44
Nodes (8): card(), img_size(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., rect(), One function per slide: layout only. Copy comes from content.py, colors/fonts…, s11_validation(), s2_problem(), s4_solution()

### Community 9 - "pic"
Cohesion: 0.67
Nodes (3): pic(), path: file name inside assets/gen, or an absolute Path., s10_market()

### Community 11 - "helpers.py"
Cohesion: 0.40
Nodes (4): Thin python-pptx helpers. All coordinates are inches on the 10 x 5.625 in…, Add styled run(s); a newline inside t becomes a soft line break, arrows use…, rgb(), _run()

### Community 12 - "s12_team"
Cohesion: 0.83
Nodes (4): num_circle(), oval(), s12_team(), s7_different()

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `recolor.py` to `make_mockups.py`, `capture_screens.py`?**
  _High betweenness centrality (0.279) - this node is a cross-community bridge._
- **Why does `Where to edit map (content / slides / theme / helpers)` connect `recolor.py` to `slides.py`, `content.py`, `helpers.py`?**
  _High betweenness centrality (0.203) - this node is a cross-community bridge._
- **Why does `s9_class()` connect `s9_class` to `make_mockups.py`, `content.py`, `text`, `chip`, `slides.py`, `pic`, `s12_team`?**
  _High betweenness centrality (0.158) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `recolor.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1368421052631579 - nodes in this community are weakly interconnected._