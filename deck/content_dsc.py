"""Founders Arena / DSC Season 17 edition (branched from the Antler edition).

Built by build_deck_dsc.py, which swaps this module in for deck.content. Follows the DSC Season 17 deck guideline
order: Cover, Business Overview, Problem & Opportunity, Solution, Market, Business Model, Traction, GTM,
ESG/Impact, Financial, Funding, Team, Roadmap, Closing (+ appendix). English copy; team = Haikal CEO, Salsabila CMO.

Honesty rules: market numbers come from cited public data (see SLIDE_SOURCES). Financial numbers come from the
founders' model (block above SLIDE_BUSINESS); any '[X]' left renders yellow. Revenue to date is Rp0 (pre-revenue).
"""

TRACK = 'DSC Season 17 · Founders Arena'
WEBSITE = 'scanvas.id'

# ---------------------------------------------------------------- 1 cover (shared s1_cover)
SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'An interactive educational toy that turns children’s coloring into a living learning experience.',
    'age_chip': 'Category: Education',
    'founder_name': 'Scanvas Co-Founders',
    'founder_role': 'Haikal H. · Salsabila K.',
    'notes': 'Scanvas: children color a sheet, photograph it in the browser, and their own drawing comes alive.',
}

# ---------------------------------------------------------------- 2 business overview (slides_dsc.s_overview)
SLIDE_OVERVIEW = {
    'tag': 'LIVE · scanvas.id · pre-revenue',
    'title': 'Physical Creativity Meets\nDigital Learning',
    'blocks': [('palette', 'Product',
                'Children color a Scanvas sheet, photograph it in the browser, and the artwork comes alive with '
                'motion, sound, and facts.'),
               ('users', 'Customers',
                'B2C: parents of children aged 3–10. B2B: PAUD/TK, TPA, schools, and children’s activity '
                'organizers.'),
               ('wand-sparkles', 'Value proposition',
                'Hands-on creativity stays at the center; technology extends it into interactive learning, with '
                'no app to install.')],
    'phones': [('ph_home.png', 'Landing page'), ('ph_scan.png', 'Scan / upload'), ('ph_world.png', 'Alive in the world')],
    'notes': 'The product is live today with two worlds and a public digital trial. Revenue has not started yet.',
}

# ---------------------------------------------------------------- 3 problem & opportunity (shared s2_problem)
SLIDE_2_PROBLEM = {
    'title': 'Creativity Often Stops at the Paper',
    'message': 'Children love drawing and coloring, but once the page is finished, the learning moment ends. '
               'Many screen-based activities are designed around watching and swiping rather than creating.',
    'paper': {'head': 'On paper', 'sub': 'Creative and hands-on, but it ends when the page is done.',
              'loop': ['Create', 'Finished', 'Stop']},
    'screen': {'head': 'On screens', 'sub': 'Engaging, but children mostly watch instead of make.',
               'loop': ['Watch', 'Swipe', 'Watch']},
    'closing': 'Opportunity: activities that join hands-on creativity, digital play, and learning.',
    'notes': 'Parents and educators need activities that combine hands-on creativity, digital engagement, and '
             'learning, not another passive screen experience.',
}

# ---------------------------------------------------------------- 4 solution (s4 + USP strip)
SLIDE_4_SOLUTION = {
    'title': 'Their Creation Becomes the Character',
    'message': 'Children color a printed sheet, scan it through the website, and watch their own artwork become an '
               'animated character with sound, motion, and educational content.',
    'steps': [('Color', 'Kids color a Scanvas paper sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Snap or upload a photo in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork comes alive in seconds', 'alive_whale.png', 'w'),
              ('Explore', 'It swims inside a living world', 'ph_world.png', 'h'),
              ('Learn', 'A short story, sounds, and facts', 'tab_result.png', 'w')],
    'usp': 'Not a generic animation: the child’s own artwork.',
    'trio': [('Movement', 'move'), ('Sound', 'music'), ('Learning Facts', 'book-open')],
    'notes': 'Color, Scan, Come Alive, Explore, Learn. The unique part: the character is the child’s own drawing.',
}

# ---------------------------------------------------------------- 5 market (slides_dsc.s_market)
SLIDE_MARKET = {
    'title': 'Market Size & Target Market',
    # (icon, segment, description)
    'personas': [('user-round', 'Primary user', 'Children aged 3–10 (≈35M in Indonesia*)'),
                 ('house', 'B2C buyer', 'Parents who want creative, educational activities at home'),
                 ('school', 'B2B buyer', 'PAUD/TK, TPA, primary schools, and children’s activity organizers')],
    'why': 'Why start here: schools buy for many children at once; families validate demand directly.',
    # outer -> inner: (label, geography, value, unit)
    'layers': [('TAM', 'Addressable institutions, Indonesia', '420,886', 'PAUD & primary schools'),
               ('SAM', 'Institutions, Central Java + DIY', '62,797', 'PAUD & primary schools'),
               ('SOM', 'Institutions, DIY (beachhead)', '7,123', 'PAUD & primary schools')],
    'source': 'Sources: Kemendikdasmen Data Referensi Pendidikan (PAUD, SD), accessed Sep 2026 · '
              '*estimated from BPS population by 5-year age group, 2022.',
    'notes': 'Counts are education units, the B2B buyers. Children 3-10 estimated as 2/5 of age 0-4 + age 5-9 + '
             '1/5 of age 10-14 (BPS 2022). D.I. Yogyakarta is the beachhead because local delivery is already '
             'offered there. See Appendix B for the breakdown.',
}

# ---------------------------------------------------------------- financial model (single source of truth, Sep 2026)
# B2C pack Rp49,000 (10 A5 sheets): print+packaging Rp10,000 + DIY delivery subsidy Rp10,000 -> contribution Rp29,000 (59%)
# B2B managed session Rp1,000,000 (up to 30 children): direct cost Rp250,000 -> contribution Rp750,000 (75%)
# 12 months: conservative 300 packs + 24 sessions = Rp38.7M revenue; base 600 packs + 48 sessions = Rp77.4M
# direct costs Rp12M / Rp24M -> gross contribution Rp26.7M / Rp53.4M (69%); OPEX Rp158M -> net -Rp131.3M / -Rp104.6M
# 12-month capital need Rp200M: team 96 · GTM 30 · product 24 · production 20 · content 20 · legal 10
# Platform-only (per drawing) revenue is NOT in the projection (upside).

# ---------------------------------------------------------------- 6 business model (slides_dsc.s_business)
SLIDE_BUSINESS = {
    'title': 'Business Model & Revenue Streams',
    # (segment, heading, description, price, detail, image, (tag, style))  style: live|validating|building|future
    'offers': [('B2C · PHYSICAL PACKS', 'Families',
                '10 A5 coloring sheets per world. Repeat purchase through new worlds.',
                'Rp49,000 / pack', 'Order via website → WhatsApp · transfer or QRIS', 'm_pack.png',
                ('AVAILABLE NOW', 'live')),
               ('B2B · MANAGED SESSIONS', 'Schools & Events',
                'A complete Scanvas activity run by our team for classrooms and events.',
                'From Rp1,000,000 / session', 'Up to 30 children · pilot pricing may vary', 'm_session.png',
                ('VALIDATING', 'validating')),
               ('B2B · PLATFORM', 'Self-Operated Institutions',
                'Bulk drawing processing through Scanvas Studio; the institution runs the activity.',
                'Rp2,000–3,000 / drawing', 'Rp3,000 (25+) · Rp2,500 (50+) · Rp2,000 (1,000+)', 'm_studio.png',
                ('IN DEVELOPMENT', 'building')),
               ('FUTURE · CONTENT', 'Learning Content',
                'New worlds, creative classes, and learning add-ons on the same engine.',
                'Subscriptions & add-ons', 'Priced after B2C and B2B validation', 'm_lesson.png',
                ('FUTURE', 'future'))],
    'notes': 'Two B2B products, kept separate: managed sessions (we run the activity: setup, operator, materials) and '
             'platform-only processing (the institution runs it). Projections use packs and managed sessions only.',
}

# ---------------------------------------------------------------- 7 traction (slides_dsc.s_traction)
SLIDE_TRACTION = {
    'title': 'Traction & Validation',
    'stage': 'Stage: live product · pre-revenue',
    'metrics': [('2', 'interactive worlds live'), ('30', 'children in first TPA pilot'),
                ('5', 'improvements from pilot feedback')],
    'loop': ['Built', 'Tested', 'Learned', 'Shipped'],
    'feedback_title': 'Pilot feedback already changed the product',
    'feedback': [('shipped', 'Larger world for more creations'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing uploads'),
                 ('progress', 'Learning space after play'),
                 ('progress', 'More worlds, e.g. a land version')],
    'status_label': {'shipped': 'Shipped', 'progress': 'In progress'},
    'proof': 'Live at scanvas.id · public digital trial · Ocean & Vehicle worlds',
    'notes': 'Pilot participants were not paying customers. The value of the pilot: five product improvements, '
             'two already shipped.',
}

# ---------------------------------------------------------------- 8 GTM (slides_dsc.s_gtm)
SLIDE_GTM = {
    'title': 'Marketing & Go-To-Market',
    # (chip, audience, funnel steps, channels)
    'tracks': [('B2C', 'Families', ['Short video', 'Digital trial', 'Creative pack', 'New world pack'],
                'Instagram & TikTok · parent communities · referrals · website → WhatsApp order'),
               ('B2B', 'Schools & events', ['Direct outreach', 'Demo', 'Small pilot', 'Paid session', 'Repeat use'],
                'PAUD/TK & TPA · event organizers · activity centers · partnerships')],
    'pillars': [('sparkles', 'Acquisition', 'Show the “color → scan → alive” moment in short videos and live demos.'),
                ('users', 'Community', 'Parent groups, teachers, and children’s activity communities.'),
                ('repeat', 'Retention', 'New worlds and learning content bring children back.')],
    'notes': 'B2C validates demand with low-cost digital channels; B2B is the priority growth channel through demos '
             'and pilots.',
}

# ---------------------------------------------------------------- 9 impact (slides_dsc.s_impact)
SLIDE_IMPACT = {
    'title': 'Impact: Turning Screen Time\nInto Active Creative Learning',
    'sdg': 'SDG 4 · Quality Education',
    'pillars': [('palette', 'Creativity', 'Children create first, before any digital experience.'),
                ('book-open', 'Learning', 'Every creation unlocks sounds, stories, and facts about the object.'),
                ('globe', 'Accessibility', 'Browser-based: no special app to install.')],
    'beneficiaries': 'Beneficiaries: children aged 3–10, parents, teachers, and PAUD/schools',
    'governance': 'Governance: minimal child data, with consent handled by adults',
    'kpis_title': 'Impact measurement planned',
    'kpis': ['Children reached per session', 'Completion rate (drawing → alive)', 'School sessions held',
             'Repeat participation', 'Simple learning recall', 'Teacher & parent satisfaction'],
    'notes': 'We do not claim measured learning outcomes yet; these are the indicators we will track from the next '
             'pilots.',
}

# ---------------------------------------------------------------- 10 financial (slides_dsc.s_financial)
SLIDE_FINANCIAL = {
    'title': 'Financial Overview',
    'stage': [('Revenue to date', 'Rp0'), ('Stage', 'Pre-revenue')],
    # (heading, [(label, value)], margin tile)
    'units': [('B2C pack', [('Price', 'Rp49K'), ('Direct cost', 'Rp20K'), ('Contribution', 'Rp29K')], '59% margin'),
              ('Managed B2B\nsession', [('Price', 'Rp1M'), ('Direct cost', 'Rp250K'), ('Contribution', 'Rp750K')],
               '75% margin')],
    'units_note': 'Direct cost: print + packaging Rp10K and DIY delivery Rp10K · session operator, transport, materials.',
    'scenario_title': '12-month projection',
    'scenario_head': ['', 'Conservative', 'Base'],
    # (label, conservative, base, emphasize)
    'scenario': [('B2C packs', '300', '600', False),
                 ('Paid sessions', '24', '48', False),
                 ('Customer revenue', 'Rp38.7M', 'Rp77.4M', True),
                 ('Direct costs', 'Rp12.0M', 'Rp24.0M', False),
                 ('Gross contribution', 'Rp26.7M', 'Rp53.4M', True),
                 ('Contribution margin', '69%', '69%', False),
                 ('Growth operating expenses', 'Rp158M', 'Rp158M', False)],
    'footer': 'Year 1 prioritizes validation and repeatability over profitability: the planned operating loss is '
              'funded by growth capital (full P&L in Appendix C).',
    'notes': 'Unit economics are healthy; the open question is repeatable demand. Grant money is financing, never '
             'counted as revenue.',
}

# ---------------------------------------------------------------- 11 funding (slides_dsc.s_funding)
SLIDE_FUNDING = {
    'title': 'Funding Needs & Use of Funds',
    'label': '12-month capital requirement',
    'amount': 'Rp200M',
    'purpose': 'Requested support to fund 12 months of product validation and commercial growth.',
    'alloc_title': 'Use of funds, in priority order',
    # (icon, use, detail, share)
    'alloc': [('users', 'Team & Operations', 'Rp96M · lean founder & team compensation', '48%'),
              ('school', 'Go-to-Market', 'Rp30M · school pilots, demos, community activation', '15%'),
              ('scan-line', 'Product & Technology', 'Rp24M · infrastructure, scan reliability, AI tools', '12%'),
              ('palette', 'Production', 'Rp20M · inventory, samples, demo materials', '10%'),
              ('book-open', 'Learning Content', 'Rp20M · 2 → 4 worlds: art, sound, facts', '10%'),
              ('shield-check', 'Legal & Contingency', 'Rp10M · administration, accounting, contracts', '5%')],
    'unlocks_title': 'What this funding unlocks in 12 months',
    'unlocks': ['48+ paid school/event sessions', '1,440+ children in paid B2B sessions', '600 B2C packs sold',
                '4 active learning worlds', 'Scanvas Studio operational', '≥20% repeat purchase / institutional rebooking target',
                'Rp77.4M first-year customer revenue'],
    'notes': 'Why Rp200M when year-1 revenue is Rp77.4M? The first 12 months are not optimized for profitability. '
             'Unit economics are already positive; the capital builds the repeatable system: founder runway, reliable '
             'infrastructure, Scanvas Studio, school acquisition, production capacity, and new worlds, so we can '
             'validate repeat purchase and institutional rebooking and scale on proven economics next year. '
             'Why Rp96M for team? Rp4M per founder per month for two founders: lean, below market salary.',
}

# ---------------------------------------------------------------- 12 team (shared s12_team)
SLIDE_12_TEAM = {
    'title': 'The Team Behind Scanvas',
    'team': [('HH', 'Haikal Hilmi', 'CEO & Co-Founder',
              'Technical founder · product & company strategy · partnerships · built the core technology',
              'founder_hh.png'),
             ('SK', 'Salsabila Khoirunnisa', 'CMO & Co-Founder',
              'Brand · marketing · customer discovery · community · go-to-market', 'founder_sk.png')],
    'closing': 'A technical CEO who built the core product, and a CMO who brings it to families and schools.',
    'final': 'We shipped the live product and ran our first pilot.',
    'notes': 'Haikal built the scan-to-animation technology and leads company and product direction; Salsabila '
             'leads marketing, customer discovery, and go-to-market.',
}

# ---------------------------------------------------------------- 13 roadmap (slides_dsc.s_roadmap)
SLIDE_ROADMAP = {
    'title': 'Milestones & Growth Roadmap',
    # (label, icon, style, items)
    'columns': [('NOW · ACHIEVED', 'check', 'done', ['Live product', 'Ocean + Vehicle worlds', 'Public digital trial',
                                                     'First 30-child pilot']),
                ('0–6 MONTHS', 'rocket', 'next', ['Paid institutional pilots', 'Validate B2C & B2B pricing',
                                                  'Improve scan reliability', 'Launch Scanvas Studio MVP']),
                ('6–12 MONTHS', 'graduation-cap', 'later', ['48 cumulative paid sessions', '600 B2C packs',
                                                            '4 active worlds', 'Repeatable school sales model',
                                                            'Wider local distribution'])],
    'kpis_title': '12-month KPIs',
    'kpis': ['48 paid sessions', '1.4K participants', '≥20% repeat', 'Rp77.4M revenue', '≥95% scan success'],
    'notes': 'Build, validate, launch, grow. KPIs equal the base case on slides 10 and 11.',
}

# ---------------------------------------------------------------- 14 closing (slides_dsc.s_closing)
SLIDE_CLOSING = {
    'headline': 'A child’s creativity shouldn’t end\nwhen the coloring is finished.',
    'sub': 'Scanvas turns every creation into another chance to play, explore, and learn.',
    'line': 'From Indonesia, starting with families and classrooms.',
    'cta': 'Support Scanvas to make creative learning repeatable for schools and families.',
    'names': 'Haikal Hilmi · Salsabila Khoirunnisa',
    'notes': 'One thing to remember: the child’s own drawing becomes the learning experience.',
}

# ---------------------------------------------------------------- appendix
SLIDE_7_DIFFERENT = {
    'title': 'Appendix A · Technology Edge',
    'items': [('Computer-Vision Scan', 'Four printed markers guide perspective correction, cropping, and '
                                       'masking of the photo.'),
              ('Personalized Animation', 'The extracted artwork, not a stock character, is animated in the world.'),
              ('Code-Linked Sheets', 'Each printed sheet carries a unique access code tied to its template.'),
              ('Reusable Content Engine', 'New worlds are new sheet templates plus world assets on the same '
                                          'pipeline, so content scales without rebuilding the product.')],
    'notes': 'Defensibility: ArUco-marker detection, perspective warp, crop and mask, then browser animation.',
}

SLIDE_SOURCES = {
    'title': 'Appendix B · Market Data',
    'head': ['Figure', 'Value', 'How it is calculated / source'],
    'rows': [('PAUD units, Indonesia', '243,604', 'TK 134,789 + KB 86,429 + TPA 2,684 + SPS 19,702 · Kemendikdasmen'),
             ('Primary schools (SD sederajat), Indonesia', '177,282', 'Kemendikdasmen Data Referensi Pendidikan'),
             ('TAM: PAUD + SD, Indonesia', '420,886', '243,604 + 177,282'),
             ('SAM: Central Java + D.I. Yogyakarta', '62,797', 'PAUD 32,839 + 5,071 · SD 22,835 + 2,052'),
             ('SOM: D.I. Yogyakarta', '7,123', 'PAUD 5,071 + SD 2,052'),
             ('Children aged 3–10, Indonesia', '≈35.3M', '2/5 × 22,094,426 (0–4) + 22,013,768 (5–9) + '
                                                         '1/5 × 22,088,673 (10–14) · BPS 2022')],
    'footnote': 'Kemendikdasmen: referensi.data.kemendikdasmen.go.id (PAUD & Dikdas per province), accessed Sep 2026. '
                'BPS: Jumlah Penduduk Menurut Kelompok Umur, Long Form SP2020 (2022). TPA in Kemendikdasmen data = '
                'Taman Penitipan Anak.',
    'notes': 'Single-year ages are not published in this table, so ages 3-10 are a proportional estimate.',
}


SLIDE_PNL = {
    'title': 'Appendix C · 12-Month P&L',
    'head': ['', 'Conservative', 'Base'],
    # (label, conservative, base, emphasize)
    'rows': [('B2C revenue', 'Rp14.7M', 'Rp29.4M', False),
             ('B2B managed sessions', 'Rp24.0M', 'Rp48.0M', False),
             ('Customer revenue', 'Rp38.7M', 'Rp77.4M', True),
             ('Direct costs', '−Rp12.0M', '−Rp24.0M', False),
             ('Gross contribution (69%)', 'Rp26.7M', 'Rp53.4M', True),
             ('Team compensation', '−Rp96.0M', '−Rp96.0M', False),
             ('Go-to-market', '−Rp24.0M', '−Rp24.0M', False),
             ('Product, infra & tools', '−Rp18.0M', '−Rp18.0M', False),
             ('Content creation', '−Rp15.0M', '−Rp15.0M', False),
             ('Legal & admin', '−Rp5.0M', '−Rp5.0M', False),
             ('Net result', '−Rp131.3M', '−Rp104.6M', True)],
    'assump_title': 'Assumptions',
    'assumptions': ['B2C Rp49K/pack; direct cost Rp20K (print & packaging Rp10K, DIY delivery Rp10K)',
                    'Managed session Rp1M, up to 30 children; direct cost Rp250K',
                    'Volume: 25–50 packs and 2–4 sessions per month',
                    'Founders Rp4M/month each (lean, not market salary)',
                    'Platform-only revenue excluded (upside)',
                    'Grant is financing, not revenue; unused inventory and contingency stay as capital'],
    'notes': 'Operating expenses are Rp158M of the Rp200M capital need; production (Rp20M) is covered through direct '
             'costs and inventory, and contingency is held back.',
}


# ---------------------------------------------------------------- competitive landscape (slides_dsc.s_competition)
# Evidence checked Sep 2026 (see SLIDE_COMPETITORS). Cells: 'yes' -> check icon, 'no' -> dash, anything else -> text.
SLIDE_COMPETITION = {
    'title': 'Competitive Landscape',
    'sub': 'A proven category, differentiated by access, shared worlds, and institutional use.',
    'players': ['Scanvas', 'Faber-Castell\nARt Alive', 'Quiver', 'WAGZAK\nJUMP', 'teamLab Sketch\nAquarium'],
    # (criterion, [Scanvas, Faber-Castell, Quiver, WAGZAK, teamLab])
    'rows': [('Paper coloring → digital', ['yes', 'yes', 'yes', 'yes', 'yes']),
             ('No app required', ['yes', 'no', 'no', 'no', 'Venue only']),
             ('Shared interactive world', ['yes', 'no', 'no', 'no', 'yes']),
             ('Educational content', ['yes', 'Some', 'yes', 'yes', 'Some']),
             ('Managed school / event session', ['Pilot', 'no', 'no', 'no', 'Installation']),
             ('Institution workflow', ['Building', 'no', 'Edu dashboard', 'School license', 'no']),
             ('Indonesia-first pricing', ['yes', 'yes', 'no', 'no', 'no'])],
    'wins_title': 'Where they win',
    'wins': [('Faber-Castell', 'brand & retail'), ('Quiver', 'content library, 26M+ downloads'),
             ('WAGZAK', 'curriculum, 30 languages'), ('teamLab', 'immersive group play')],
    'position': 'Scanvas: the accessibility of a web product, the shared-world magic of an installation, and the '
                'repeatability of an education platform.',
    'notes': 'We do not claim to be first: color, scan, alive is a proven behavior. Our bet is lower friction '
             '(browser, no app), shared worlds, and an affordable B2B workflow for Indonesian schools and events.',
}

SLIDE_COMPETITORS = {
    'title': 'Appendix D · Competitor Evidence',
    'head': ['Product', 'What it is', 'Model & price', 'Source (checked Sep 2026)'],
    'rows': [('Faber-Castell ARt Alive', 'Coloring products + Art Alive mobile app; drawings become 3D AR with games',
              'Drawing Alive / Colouring 3D Alive: Rp105,900', 'faber-castell.co.id/colouring3dalive'),
             ('Quiver', 'Print, color, scan with the app; artwork animates in interactive 3D',
              'Free + premium packs; education subscriptions (10–500 seats); 26M+ downloads', 'quivervision.com'),
             ('WAGZAK JUMP', 'Mobile app; colored drawings come alive in 3D/AR lessons',
              '100+ lessons, 30 languages; US$9.99/yr household; school licenses', 'circuscompany.com/wagzak-jump'),
             ('teamLab Sketch Aquarium', 'Installation: color a sea creature, scan it, it swims in a shared aquarium',
              'Venue / museum visit (e.g. ArtScience Museum, Singapore)', 'futurepark.team-lab.cn'),
             ('Osmo Monster', 'Drawings join an animated character’s world via iPad + Osmo base',
              'Hardware kit + iPad required', 'playosmo.com')],
    'notes': 'Indirect analogues not in the main matrix: Osmo (hardware) and Octaland 4D+ (AR coloring book app).',
}
