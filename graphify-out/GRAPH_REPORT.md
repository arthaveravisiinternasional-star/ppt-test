# Graph Report - PPT  (2026-10-08)

## Corpus Check
- 40 files · ~54,144 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 303 nodes · 1201 edges · 13 communities (10 shown, 3 thin omitted)
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 21 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- make_mockups.py
- slides.py
- theme.py
- make_pilot_art.py
- text
- Arrow Chip Rows
- chip
- slides_dsc.py
- pic
- make_pitch_prep.py
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
- `Honesty rules: live vs roadmap, [X]/[TBD] placeholders` --references--> `SLIDE_10_MARKET copy (Market & business model)`  [EXTRACTED]
  README.md → deck/content.py
- `Honesty rules: live vs roadmap, [X]/[TBD] placeholders` --references--> `SLIDE_11_VALIDATION copy (Validation & roadmap)`  [EXTRACTED]
  README.md → deck/content.py

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Asset generation flow** — tools_capture_screens, tools_make_mockups, tools_render_icons, tools_lesson_mockup [EXTRACTED 1.00]
- **Deck build pipeline** — build_deck_build, deck_slides, deck_content, deck_theme, deck_helpers [EXTRACTED 1.00]

## Communities (13 total, 3 thin omitted)

### Community 0 - "make_mockups.py"
Cohesion: 0.11
Nodes (27): Asset pipeline (shots -> mockups -> icons), english(), pages(), Capture real product screenshots from the live site into assets/shots (needs…, Real scan: upload a colored sheet photo to /play (Ocean) and redeem an access…, scan(), trial(), Creative Class lesson mockup (HTML template) (+19 more)

### Community 1 - "slides.py"
Cohesion: 0.10
Nodes (31): All deck copy lives here. Edit text in this file only; layout lives in…, SLIDE_10_MARKET copy (Market & business model), SLIDE_11_VALIDATION copy (Validation & roadmap), SLIDE_12_TEAM copy (Team & closing), SLIDE_1_COVER copy (Cover), SLIDE_2_PROBLEM copy (Problem), SLIDE_3_INSIGHT copy (Insight), SLIDE_4_SOLUTION copy (Solution flow) (+23 more)

### Community 2 - "theme.py"
Cohesion: 0.06
Nodes (28): build(), Build the Antler (pre-seed VC) edition: same template, look, helpers and…, build(), build(), Build the Founders Arena / DSC Season 17 edition, branched from the Antler…, build(), Build the SCANVAS investor deck (October 2026): 13 main slides + 7 appendix,…, build() (+20 more)

### Community 6 - "text"
Cohesion: 0.14
Nodes (64): card(), notes(), DESIGN.md card: white surface on canvas, one Garis Lembut hairline, no shadow., paras: str | [str, ...] | [[(text, {size,color,font}), ...], ...] (one inner…, Fill the layout's own title placeholder (keeps slide outline / accessibility)., rect(), text(), title() (+56 more)

### Community 8 - "chip"
Cohesion: 0.09
Nodes (31): _background(), build(), Build the ITEC SEA 2026 official-template edition (v4) on the committee's…, _background(), build(), Build the ITEC SEA 2026 7-minute pitch edition (v5): 12 main slides + appendix…, ITEC SEA 2026 · 7-minute pitch edition (v5), Digital Culture Track. 12 main…, chip() (+23 more)

### Community 9 - "slides_dsc.py"
Cohesion: 0.19
Nodes (11): arrow_chips(), Row of chips joined by arrow icons. last=(bg, fg) restyles the final chip., _is_placeholder(), Slides specific to the Founders Arena / DSC Season 17 edition. Same helpers and…, Number tile: real value = violet, founder-supplied placeholder = yellow., s_gtm(), s_overview(), s_traction() (+3 more)

### Community 11 - "pic"
Cohesion: 0.13
Nodes (31): icon(), oval(), pic(), path: file name inside assets/gen, or an absolute Path., color: purple | white | ink | green | gray | yellow | deep, _art_row(), _flow(), Slides specific to the ITEC SEA 2026 final (v3) edition. Visual base = v2… (+23 more)

### Community 12 - "make_pitch_prep.py"
Cohesion: 0.28
Nodes (15): Pt(), build(), heading(), inline(), page_number_footer(), para(), Printable DOCX + PDF of the ITEC pitch prep page (script, Q&A, numbers, answer…, Embed fonts into the DOCX and export the PDF through Word. (+7 more)

### Community 14 - "content_investor.py"
Cohesion: 0.18
Nodes (12): _model(), monthly(), SCANVAS investor deck, October 2026 (SCANVAS_Investor_Oct2026). 13 main slides…, Rp juta -> 'Rp87.3M' / 'Rp1.19B'., Unit price in Rp juta -> 'Rp49K' / 'Rp1M' / 'Rp2.4M'., Cash balance at the end of months 1-24 (Rp200M arrives in month 1, the year-2…, Working capital at the end of a model month: unpaid sessions + printed-but-…, Working capital at a year end. Years 1-2 come from the monthly model; years 3-5… (+4 more)

## Knowledge Gaps
- **1 isolated node(s):** `SCANVAS pitch deck (python-pptx)`
  These have ≤1 connection - possible missing edges or undocumented components.
- **3 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `rect()` connect `text` to `slides.py`, `chip`, `slides_dsc.py`, `pic`, `make_pitch_prep.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Why does `Pt()` connect `make_pitch_prep.py` to `chip`, `text`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Why does `text()` connect `text` to `chip`, `slides.py`, `pic`, `slides_dsc.py`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **What connects `SCANVAS pitch deck (python-pptx)` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `make_mockups.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11397849462365592 - nodes in this community are weakly interconnected._
- **Should `slides.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10338680926916222 - nodes in this community are weakly interconnected._
- **Should `theme.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05714285714285714 - nodes in this community are weakly interconnected._