# Graph Report - PPT  (2026-10-08)

## Corpus Check
- 40 files · ~53,917 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 301 nodes · 1198 edges · 16 communities (12 shown, 4 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- slides.py
- slides_dsc.py
- build_deck.py
- make_pilot_art.py
- build_deck_itec5.py
- title
- Arrow Chip Rows
- rect
- pic
- text
- make_pitch_prep.py
- section
- content_investor.py
- make_fonts.py

## God Nodes (most connected - your core abstractions)
1. `text()` - 111 edges
2. `title()` - 99 edges
3. `rect()` - 95 edges
4. `notes()` - 94 edges
5. `card()` - 70 edges
6. `chip()` - 70 edges
7. `pic()` - 48 edges
8. `icon()` - 45 edges
9. `icon_circle()` - 33 edges
10. `num_circle()` - 27 edges

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

## Communities (16 total, 4 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.22
Nodes (18): all_mockups(), card(), colored_sheet(), fitcard(), founders(), lesson(), phone(), Build every image in assets/gen from assets/shots + Scanvas project files.… (+10 more)

### Community 1 - "slides.py"
Cohesion: 0.09
Nodes (41): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow), SLIDE_5_PRODUCT copy (Product today (live)) (+33 more)

### Community 2 - "slides_dsc.py"
Cohesion: 0.06
Nodes (30): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the SCANVAS investor deck (October 2026): 13 main slides + 7 appendix,…, build(), Build the ITEC SEA 2026 Top 30 (v2) edition: 10 main slides + 3 appendix,… (+22 more)

### Community 3 - "build_deck.py"
Cohesion: 0.11
Nodes (14): build(), Build the ITEC SEA 2026 (Digital Culture Track) edition: same template, layout,…, powerpoint(), Build the SCANVAS GESAwards 2026 pitch deck from the Freesia template. python…, ITEC SEA 2026 · Digital Culture Track edition of the deck copy (same layout as…, Asset pipeline (shots -> mockups -> icons), Build commands (--render N, --pdf), english() (+6 more)

### Community 5 - "build_deck_itec5.py"
Cohesion: 0.33
Nodes (4): _background(), build(), Build the ITEC SEA 2026 7-minute pitch edition (v5): 12 main slides + appendix…, ITEC SEA 2026 · 7-minute pitch edition (v5), Digital Culture Track. 12 main…

### Community 6 - "title"
Cohesion: 0.18
Nodes (34): card(), img_size(), notes(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., Fill the layout's own title placeholder (keeps slide outline / accessibility)., title(), s_business(), s_competition() (+26 more)

### Community 8 - "rect"
Cohesion: 0.15
Nodes (29): chip(), _frame(), Pill label. ic=(icon_name, icon_color). align l/r/c anchors x., rect(), s_culture(), s_market(), _flow(), s_culture() (+21 more)

### Community 9 - "pic"
Cohesion: 0.11
Nodes (24): SLIDE_2_PROBLEM copy (Problem), arrow_chips(), pic(), path: file name inside assets/gen, or an absolute Path., Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., s_closing(), s_gtm(), s_overview() (+16 more)

### Community 11 - "text"
Cohesion: 0.16
Nodes (27): icon(), Inches(), color: purple | white | ink | green | gray | yellow | deep, paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, text(), s_roadmap(), s_solution(), s_competition() (+19 more)

### Community 12 - "make_pitch_prep.py"
Cohesion: 0.28
Nodes (15): Pt(), build(), heading(), inline(), page_number_footer(), para(), Printable DOCX + PDF of the ITEC pitch prep page (script, Q&A, numbers, answer…, Embed fonts into the DOCX and export the PDF through Word. (+7 more)

### Community 14 - "content_investor.py"
Cohesion: 0.20
Nodes (10): _model(), monthly(), SCANVAS investor deck, October 2026 (SCANVAS_Investor_Oct2026). 13 main slides…, Rp juta -> 'Rp87.3M' / 'Rp1.19B'., Unit price in Rp juta -> 'Rp49K' / 'Rp1M' / 'Rp2.4M'., Cash balance at the end of months 1-24 (Rp200M arrives in month 1, the year-2…, Working capital at a year end: one month of B2B receivables + two months of…, rp() (+2 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `rect()` connect `rect` to `slides.py`, `slides_dsc.py`, `title`, `pic`, `text`, `make_pitch_prep.py`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Why does `Pt()` connect `make_pitch_prep.py` to `rect`, `slides.py`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Why does `text()` connect `text` to `slides.py`, `slides_dsc.py`, `title`, `rect`, `pic`, `section`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `slides.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0927536231884058 - nodes in this community are weakly interconnected._
- **Should `slides_dsc.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._
- **Should `build_deck.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10822510822510822 - nodes in this community are weakly interconnected._