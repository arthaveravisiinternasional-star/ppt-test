# Graph Report - PPT  (2026-10-05)

## Corpus Check
- 37 files · ~44,885 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 263 nodes · 1016 edges · 14 communities (11 shown, 3 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- slides.py
- title
- recolor.py
- make_pilot_art.py
- text
- slides_dsc.py
- Arrow Chip Rows
- rect
- capture_screens.py
- notes
- make_pitch_prep.py
- make_fonts.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 91 edges
2. `title()` - 80 edges
3. `rect()` - 76 edges
4. `notes()` - 75 edges
5. `chip()` - 61 edges
6. `card()` - 54 edges
7. `pic()` - 43 edges
8. `icon()` - 38 edges
9. `icon_circle()` - 34 edges
10. `num_circle()` - 23 edges

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

## Communities (14 total, 3 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.21
Nodes (19): Creative Class lesson mockup (HTML template), all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone() (+11 more)

### Community 1 - "slides.py"
Cohesion: 0.10
Nodes (38): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow) (+30 more)

### Community 2 - "title"
Cohesion: 0.17
Nodes (27): chip(), _frame(), icon(), Inches(), color: purple | white | ink | green | gray | yellow | deep, Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., Fill the layout's own title placeholder (keeps slide outline / accessibility)., title() (+19 more)

### Community 3 - "recolor.py"
Cohesion: 0.06
Nodes (24): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,…, build(), Build the ITEC SEA 2026 final (v3) edition: 10 main slides + 3 appendix,… (+16 more)

### Community 5 - "text"
Cohesion: 0.20
Nodes (17): pic(), path: file name inside assets/gen, or an absolute Path., paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), s_business(), s_closing(), s_overview(), s_live() (+9 more)

### Community 6 - "slides_dsc.py"
Cohesion: 0.08
Nodes (26): Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, _background(), build(), Build the ITEC SEA 2026 official-template edition (v4) on the committee's…, _background(), build(), Build the ITEC SEA 2026 7-minute pitch edition (v5): 12 main slides + appendix…, Founders Arena / DSC Season 17 edition (branched from the Antler edition).… (+18 more)

### Community 8 - "rect"
Cohesion: 0.18
Nodes (18): rect(), _alpha(), Slides for the ITEC SEA 2026 official-template edition (v4). Coordinates stay…, Committee section name, top-right, in the template's blue., slides.s5_product re-spaced to clear the template's top bar, plus the TRY IT…, s_about(), s_ask(), s_competition() (+10 more)

### Community 9 - "capture_screens.py"
Cohesion: 0.24
Nodes (8): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Rasterize lucide icons (from the Scanvas frontend's lucide-react) into…

### Community 11 - "notes"
Cohesion: 0.19
Nodes (21): card(), notes(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., s_competitors(), s_financial(), s_pnl(), s_sources(), s_traction() (+13 more)

### Community 12 - "make_pitch_prep.py"
Cohesion: 0.28
Nodes (15): Pt(), build(), heading(), inline(), page_number_footer(), para(), Printable DOCX + PDF of the ITEC pitch prep page (script, Q&A, numbers, answer…, Embed fonts into the DOCX and export the PDF through Word. (+7 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Pt()` connect `make_pitch_prep.py` to `rect`, `slides_dsc.py`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Why does `rect()` connect `rect` to `slides.py`, `title`, `text`, `slides_dsc.py`, `notes`, `make_pitch_prep.py`?**
  _High betweenness centrality (0.102) - this node is a cross-community bridge._
- **Why does `Asset pipeline (shots -> mockups -> icons)` connect `capture_screens.py` to `make_mockups.py`, `slides.py`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `slides.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0975609756097561 - nodes in this community are weakly interconnected._
- **Should `recolor.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06282051282051282 - nodes in this community are weakly interconnected._
- **Should `slides_dsc.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08333333333333333 - nodes in this community are weakly interconnected._