# SCANVAS — GESAwards 2026 pitch deck

12-slide deck built with python-pptx on top of the Freesia (Slidesgo) template.

```
python build_deck.py                # -> output/SCANVAS_GESAwards2026.pptx
python build_deck.py --render 3 7   # + PNG preview of slides 3 and 7 (output/preview, needs PowerPoint)
python build_deck.py --render --pdf # full preview + PDF
```

## Where to edit

| Change | File |
|---|---|
| Any wording, bullet, placeholder (`[X]`, `[TBD]`), speaker note | `deck/content.py` (one dict per slide) |
| Position / size / look of one slide | `deck/slides.py` (`s1_cover` … `s12_team`) |
| Colors, fonts, which template layout each slide uses | `deck/theme.py` (palette = `website/frontend/DESIGN.md`) |
| Template re-skin (Freesia theme slots, hatch/dot PNGs, canvas bg) | `deck/recolor.py` (runs at build, template file untouched) |
| Shared drawing helpers (chips, icon circles, pictures) | `deck/helpers.py` |
| Founder photo | `SLIDE_12_TEAM['team']` 5th field: path to a square photo (else initials) |

## Fonts

Fredoka Bold / SemiBold + Varela Round (DESIGN.md). Static TTFs live in `assets/fonts/` (OFL, from github.com/google/fonts;
Fredoka statics cut from the variable font) and are installed per-user on this PC. `--pdf` re-saves the PPTX with the
fonts embedded, so it opens correctly on other machines. On a new PC: double-click the 3 TTFs → Install, then build.

## Assets

- `assets/template/freesia_template.pptx` — master + layouts (blobs come from the layouts).
- `assets/shots/` — real screenshots from scanvas.id. Refresh: `python tools/capture_screens.py pages` / `trial whale` / `trial bus`.
- `assets/gen/` — phone/tablet mockups, colored paper sheet, lesson concept. Rebuild: `python tools/make_mockups.py` (or `lesson`).
- `assets/icons/` — lucide icons in 7 colors. Add one: `python tools/render_icons.py rocket`.

## Honesty rules baked into the copy

- Slides 5 and 11 list only verified, live facts. Slide 8 marks Current / Next / Future; slide 9 is tagged Concept.
- Slide 3 is design philosophy, not a research claim. Slide 10 shows revenue models only (no prices until validated;
  Rp35k pack promo ended 30 Apr 2026). Slide 11: 30 pilot participants, 1 real-world pilot (TPA), 5 improvements from feedback.
- The paper whale is the real crayon sheet `assets/whale.png` (QR/access code cropped out); its "alive" screens come from
  scanning that sheet on live scanvas.id (room fish-07b96372) plus the user's world screenshot.

## ITEC SEA 2026 edition (Digital Culture Track)

Same template, layout, assets, and helpers; only the copy differs.

```
python build_deck_itec.py --render --pdf   # -> output/itec/SCANVAS_ITEC_SEA2026.pptx (+ .pdf, previews in output/itec/preview)
```

- Copy: `deck/content_itec.py` (same keys as `deck/content.py`). `build_deck_itec.py` swaps it in for `deck.content`
  before importing the slides, so the GESAwards files are never modified.
- Framed against ITEC Industry/Special-track criteria (itecsea.com/judging-criteria): market & customer evidence,
  product/technology & defensibility, business model, traction, team, sector fit. No Female Founders framing.
- `tools/render.ps1` loads the TTFs from `assets/fonts/` itself before PowerPoint opens, so builds render Fredoka /
  Varela Round even when Windows has not loaded the per-user fonts after a reboot.

## Antler edition (pre-seed VC)

```
python build_deck_antler.py --render --pdf   # -> output/antler/SCANVAS_Antler_PreSeed.pptx (+ .pdf)
```

- Copy: `deck/content_antler.py`; investor-only slides (Market TAM/SAM/SOM, The Ask): `deck/slides_antler.py`.
- Slide order is set in `DECK` inside `build_deck_antler.py` (investor story; philosophy and class-concept slides dropped).
- No placeholders ("no deck > unfinished deck"): market is a qualitative wedge → scale → expand until sizing is sourced;
  the ask is Antler's pre-seed with qualitative 9-month milestones.
- Team differs from GESA/ITEC: Haikal = CEO & Co-Founder (technical CEO), Salsabila = CMO & Co-Founder.

## Founders Arena / DSC Season 17 edition (branched from Antler)

```
python build_deck_dsc.py --render --pdf   # -> output/dsc/SCANVAS_DSC_S17.pptx (+ .pdf), 14 main slides + 2 appendix
```

- Copy: `deck/content_dsc.py`; DSC-only slides (overview, market, traction, GTM, impact, financial, funding, roadmap,
  closing, sources): `deck/slides_dsc.py`. Order follows the DSC Season 17 guideline in `DECK` inside `build_deck_dsc.py`.
- Market figures are sourced (Kemendikdasmen PAUD/SD unit counts, BPS population by age group 2022; breakdown in Appendix B).
- Financial model (founders' assumptions, Sep 2026) is written once as a comment block above `SLIDE_BUSINESS` and
  feeds slides 6, 10, 11, 13 and Appendix C: pack Rp49K, session Rp1M, base 600 packs + 48 sessions = Rp77.4M,
  capital need Rp200M. Change a number there and update every slide that quotes it.

## Founders Arena / DSC Season 17 v4.1 (Oct 2026)

```
python build_deck_dsc4.py --render --pdf   # -> output/dsc4/SCANVAS_DSC_S17_v4.1.pptx (+ .pdf), 15 main + 4 appendix
```

- Copy: `deck/content_dsc4.py`; new layouts (problem strip, business lead, GTM, financial, funding, roadmap, closing,
  P&L + cash): `deck/slides_dsc4.py`. Market, competition and traction reuse `slides_itec3`. DSC v3 files untouched.
- v4 = DSC v3 + ITEC v3 validation story (Prove Magic -> Prove Repeat Value -> Validate Commercial Model -> Scale),
  after the judges' feedback of 8 Oct 2026. B2B-first, B2C = direct sales + validation. Team: Haikal CEO, Salsabila CMO.
- Market sized by institutions and geography (DIY -> Central Java -> Indonesia) plus a base-case target of about 40
  paying institutions; no TAM/SAM/SOM rings. Studio per-drawing price is a hypothesis and is not shown as a price.
- v4.1 (founders' copy): slide 2 customers = target customers, not paying ones; slide 11 stops at the projected net
  result (no cash balance, funding not secured); slide 12 treats Rp200M as the total 12-month capital plan with a
  funding strategy (DSC contribution within program limits, unconfirmed financing not counted) and milestone-based
  deployment, no DSC amount yet; slide 13 founder bios; Appendix C keeps month-12 cash only as an illustrative scenario
  "if the full Rp200M is secured". v4 output kept as `output/dsc4/SCANVAS_DSC_S17_v4.*`.
- Financial numbers are the unchanged DSC v3 model.
- `theme.LOGO` reads the `SCANVAS_LOGO` env var when set, so the deck can be built on machines without
  `D:/Personal Bisnis`. The committed PDF/previews were rendered with LibreOffice; re-run `--render --pdf` on Windows
  for the PowerPoint-rendered, font-embedded final.

## ITEC SEA 2026 Top 30 edition (v2)

```
python build_deck_itec2.py --render --pdf   # -> output/itec2/SCANVAS_ITEC_SEA2026_v2.pptx (+ .pdf), 10 main + 3 appendix
```

- Copy: `deck/content_itec2.py`; v2-only slides (problem+loop, live+QR, tech statement, digital culture, market
  staircase, business+GTM, roadmap+team, pipeline): `deck/slides_itec2.py`. Reuses DSC traction, competition, sources.
- Backbone = ITEC v1 story; market numbers from DSC; wedge -> scale -> expand from Antler. No prices, no funding ask.
- Team shown here (Salsabila CEO, Haikal CTO) was WRONG for ITEC: the ITEC application lists Haikal Hilmi CEO (60%)
  and Salsabila Khoirunnisa CMO (40%). Fixed in v4 and v5 (Oct 2026); v1-v3 still carry the old titles. ITEC v1 files (`build_deck_itec.py`) are untouched.
- Slide rules applied 2026-09-27 (carnot-tech/consulting-pptx-skill `slide-rules.md`, relevant parts only): titles are
  claim sentences that read as one story, no subtitle lines, no bottom message bands, competitor table includes axes
  where competitors lead. Pre-rules output kept as `output/itec2/*_before-rules.*`.

## ITEC SEA 2026 final edition (v3)

```
python build_deck_itec3.py --render --pdf   # -> output/itec3/SCANVAS_ITEC_SEA2026_v3.pptx (+ .pdf), 10 main + 3 appendix
```

- Copy: `deck/content_itec3.py` (founders' V3 spec, Sep 2026); layouts: `deck/slides_itec3.py`. Visual base = v2; v1/v2
  files and outputs are untouched. No shared slide function was changed for v3.
- Story: cover + proof strip → problem + tested evidence → magic + TRY IT LIVE QR (`assets/qr_scanvas_trial.png` →
  scanvas.id/trial) → pilot → engine → repeat value (Ocean Artist 3-lesson pilot) → business model with validation
  gates → beachhead + initial customer → digital culture + regional row → roadmap + ITEC ask.
- Pilot artwork (slides 2, 4) = real sheets colored in the TPA pilot, cropped without QR/access codes:
  `python tools/make_pilot_art.py` (source `D:/Personal Bisnis/TPA/result`).
- Slide 4 pilot photos come from `assets/pilot-project/` (letterbox bars stripped, sheet QR/access code blurred) via the
  same script -> `assets/gen/pilot_photo_1..4.jpg`.
- Slide 7 pricing box is off (`SLIDE_BUSINESS['pricing'] = None`); the commented tuple turns it on once confirmed.

## ITEC SEA 2026 official-template edition (v4)

```
python build_deck_itec4.py --render --pdf   # -> output/itec4/SCANVAS_ITEC_SEA2026_v4.pptx (+ .pdf), 18 main + divider + 2 appendix
```

- Base file = the committee's template `assets/template/itec_official.pptx` (copy of `ITEC PITCH DECK.pptx`, 20 x 11.25 in):
  its cover (blue/green bars + ITEC 2026 logo) is kept, every other slide gets a copy of its frame bars.
- Copy = ITEC v3 (`deck/content_itec4.py` imports `content_itec3` and adds Target Market, About, UVP, Team, Ask,
  Contact); layouts in `deck/slides_itec4.py`, the rest reused from `slides_itec3` / `slides_dsc`.
- Slide order and the small blue section label on each slide follow the committee's sections (`DECK` in
  `build_deck_itec4.py`). Use of funds (Rp200M / 12 months) and Exit Strategy (indicative) reuse the founders'
  financial model from `content_dsc.py`; change a number there and in `SLIDE_FUNDS` / `SLIDE_EXIT` together.
- `helpers.SCALE` (default 1.0) is set to 2.0 by this build, so slide code keeps the 10 x 5.625 in grid.
- Slide 5 "Live Demo" (`s_demo`, copy in `SLIDE_DEMO`) embeds `assets/video/trial_digital_itec.mp4`, a 37-second
  recording of the digital trial on the live product, with `trial_digital_itec_poster.png` as the poster frame that
  PDF readers and an unplayed slide show. The video plays on click and adds about 7 MB to the deck. Its source
  project and recording scripts live outside this repo (`D:/Personal Bisnis/video/scanvas-promo` for the Reels cut).
- Typography matches the committee template: Roboto Condensed (Regular / SemiBold / Bold). Static cuts made from the
  Google Fonts variable font by `python tools/make_fonts.py` (OFL, `assets/fonts/OFL-robotocondensed.txt`), installed
  per-user and loaded by `tools/render.ps1`. The build overrides `theme` fonts before importing helpers;
  `theme.FONT_ALIAS` writes 'Roboto Condensed Bold' as family + bold so PowerPoint embeds it. Arrows stay Segoe UI
  (Roboto Condensed has no → glyph).

## ITEC SEA 2026 7-minute pitch edition (v5)

```
python build_deck_itec5.py --render --pdf   # -> output/itec5/SCANVAS_ITEC_SEA2026_v5.pptx (+ .pdf), 12 main + appendix
```

- Same machinery as v4 (committee template, Roboto Condensed, `helpers.SCALE = 2`). Copy: `deck/content_itec5.py`
  (founders' 12-slide spec, Oct 2026); layouts: `deck/slides_itec5.py`. Timing per slide is in the speaker notes
  (about 6:30 total incl. the 37-second demo video on slide 4; backup MP4 in `assets/video/`).
- Revised after the ITEC Council assessment (Oct 2026): Haikal CEO 60% / Salsabila CMO 40%, slide 6 TAM/SAM/beachhead,
  slide 11 unit economics + base case + Rp200M, slide 12 concrete partner-led Chaoyang pilot. Appendix: competitor
  matrix, market expansion, market data, technology & child data, 12-month financial projection with cash plan
  (`FINANCIALS5`, numbers from the DSC model), Chaoyang pilot. Exit strategy dropped from v5 (still in v4).
  Pre-council version kept as `output/itec5/*_before-council.*`.
- Funding title says "Seeking"; switch `FUNDS5['title']` to "Rp200 Million Capital Plan for the Next 12 Months" if
  the founders are not raising now.
- Pitch prep (script per slide, 41 judge questions with answers, numbers, answer rules): source page
  `docs/pitch_prep_itec5.html` (also published as a private artifact). Printable A4 copies:
  `python tools/make_pitch_prep.py` -> `output/itec5/SCANVAS_ITEC_pitch_prep.docx` + `.pdf` (Word embeds the fonts).
  Yellow highlights = facts only the founders can fill in.

## Investor deck, October 2026 (branch of DSC S17)

```
python build_deck_investor.py --render --pdf   # -> output/investor/SCANVAS_Investor_Oct2026.pptx (+ .pdf), 13 main + 7 appendix
```

- Copy: `deck/content_investor.py`; layouts: `deck/slides_investor.py` (Freesia template, Fredoka/Varela). Appendix D-F
  reuse `slides_dsc.s_sources`, `slides_itec3.s_competition`, `slides_itec3.s_pipeline`.
- Sources: DSC S17 (business, GTM, funding), ITEC v5 (product, pilot, validation order, council feedback), the course
  roadmap (`roadmap_new.md`, Ocean Artist Level 1, 3 -> 10 lesson gate), founders' CVs (team slide).
- Working model at the top of `content_investor.py`: unit economics + what each direct cost covers (`UNITS`), yearly
  volumes, opex, capex, a 24-month cash model (`M_SESSION`, `M_PACK`, `M_COURSE`, print batches, 30-day school
  payment lag) and working capital. The year-2 raise (`Y2_RAISE`, currently Rp75M) is computed from the monthly cash
  low point plus a 3-month opex buffer. Slides 6, 11, 12 and Appendix A-B are all computed from it.
- Ask: Rp200M for 12% post-money (≈Rp1.67B post-money). The 15% negotiation range is internal and never in the deck.
