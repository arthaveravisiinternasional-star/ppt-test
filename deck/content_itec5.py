"""ITEC SEA 2026 · 7-minute pitch edition (v5), Digital Culture Track. 12 main slides + appendix.

Built by build_deck_itec5.py on the committee template (same machinery as v4). Revised after the ITEC Council
assessment (Oct 2026: 71/100, "Adequate"): leadership as in the application (Haikal CEO 60%, Salsabila CMO 40%),
unit economics + 12-month projection + cash plan (slide 11, appendix), and a concrete partner-led Chaoyang pilot
(slide 12, appendix). Previous version kept as output/itec5/*_before-council.*.

Honesty rules: live product, 2 worlds, one completed 30-child pilot, pre-revenue. Prices (Rp49K pack, Rp1M session),
direct costs, targets, and every Rp figure in the projection are founders' planning assumptions (Sep 2026 model, same
as the DSC deck) and are labelled as such. CAC and LTV are not claimed. Chaoyang is a pilot to explore with a partner,
not an existing partner. No learning-outcome claims.
"""
from .content_itec4 import *  # noqa: F401,F403  (v4 copy feeds the appendix slides)
from .content_itec4 import SLIDE_DEMO, SLIDE_MARKET_SIZE

FOUNDERS = [('Haikal Hilmi', 'CEO & Co-Founder'), ('Salsabila Khoirunnisa', 'CMO & Co-Founder')]

# ---------------------------------------------------------------- 1 cover
COVER5 = {
    'label': 'PITCH DECK',
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity\nComes Alive',
    'summary': 'Children turn their paper artwork into interactive characters and learning experiences, directly in '
               'the browser.',
    'presenters': FOUNDERS,
    'track': 'ITEC SEA 2026 · Digital Culture Track',
    'website': 'scanvas.id',
    'notes': '0:15 · Scanvas: where children’s creativity comes alive. I am Salsabila, co-founder and CMO; with me is '
             'Haikal, our CEO.',
}

# ---------------------------------------------------------------- 2 problem
PROBLEM5 = {
    'title': 'Creativity Starts With the Child, But Often Stops at the Page',
    'problems': [('PHYSICAL CREATIVITY ENDS', 'Children draw, color, and imagine, but once the page is finished, the '
                                              'experience often ends.'),
                 ('DIGITAL EXPERIENCES ARE OFTEN PASSIVE', 'Many digital activities give children ready-made '
                                                           'characters to watch, swipe, and consume.'),
                 ('LEARNING AND CREATING STAY SEPARATE', 'Animals, nature, and other topics are often learned through '
                                                         'worksheets or content created by someone else.')],
    'question': 'What if the child’s own creation became the starting point of play and learning?',
    'tested': 'Tested with 30 children in our first real-world TPA pilot in D.I. Yogyakarta.',
    'photo': 'pilot_photo_3.jpg',
    'caption': 'From our pilot at a TPA in D.I. Yogyakarta',
    'notes': '0:35 · Physical creativity ends with the page; screens are passive; learning and creating stay '
             'separate. What if the child’s own creation became the starting point? (No learning-outcome claims.)',
}

# ---------------------------------------------------------------- 3 solution
SOLUTION5 = {
    'title': 'Their Artwork Becomes the Character',
    'steps': [('COLOR', 'Create on a printed Scanvas sheet.', 'paper_whale.png', 'w'),
              ('SCAN', 'Photograph or upload the artwork in the browser.', 'ph_scan.png', 'h'),
              ('COME ALIVE', 'The child’s own artwork is extracted and animated.', 'alive_whale.png', 'w'),
              ('EXPLORE & LEARN', 'It enters an interactive world with movement, sound, stories, and facts.',
               'tab_result.png', 'w')],
    'statement': 'The child creates first. Technology extends what they created.',
    'chip': 'No app installation required',
    'notes': '0:25 · Color, scan, come alive, explore and learn. The child creates first; technology extends it.',
}

# ---------------------------------------------------------------- 4 product demo (video)
DEMO5 = {
    'tag': 'LIVE DEMO · 37 SECONDS',
    'title': 'See Scanvas\nin Action',
    'video': SLIDE_DEMO['video'],
    'poster': SLIDE_DEMO['poster'],
    'body': ['Our free digital trial lets families experience the core Scanvas moment before purchasing a physical '
             'pack.'],
    'live_title': 'LIVE TODAY',
    'live': ['Ocean World', 'Vehicle World', 'Paper artwork scanning', 'Digital coloring trial',
             'Personalized animation', 'Character sounds and facts'],
    'caption': 'COLOR → SCAN → COME ALIVE → EXPLORE',
    'notes': '0:55 incl. video · Say before playing: "This video shows our digital trial. Our physical packs use the '
             'same animation experience after children photograph their paper artwork." Backup: the MP4 file '
             'assets/video/trial_digital_itec.mp4.',
}

# ---------------------------------------------------------------- 5 traction
TRACTION5 = {
    'title': 'Our First Pilot Already Changed the Product',
    'metrics': [('30', 'children in first real-world pilot'), ('1', 'TPA pilot completed'),
                ('2', 'interactive worlds live'), ('5', 'product priorities from feedback')],
    'shipped': ['Larger interactive world', 'Digital trial before purchase'],
    'building': ['Bulk drawing processing', 'Story and learning space', 'Additional worlds'],
    'proved_label': 'WHAT WE PROVED',
    'proved': 'Children can complete the Scanvas experience in a real setting.',
    'next_label': 'WHAT WE MUST PROVE NEXT',
    'next': 'Paid demand and repeat use.',
    'stage': 'PRE-REVENUE',
    'photos': ['pilot_photo_4.jpg', 'pilot_photo_1.jpg', 'pilot_photo_2.jpg'],
    'caption': 'First real-world pilot · TPA, D.I. Yogyakarta',
    'notes': '0:30 · 30 children, one TPA pilot, two worlds live, five priorities from feedback: two shipped, three '
             'building. Proved: children complete the experience in a real setting. Next: paid demand and repeat '
             'use. Pre-revenue.',
}

# ---------------------------------------------------------------- 6 market size (TAM / SAM / beachhead)
MARKET5 = {
    'title': 'Start With a Reachable Beachhead, Then Scale',
    # (label, value, unit, place)
    'tiers': [('TAM', '420,886', 'PAUD + primary schools', 'Indonesia'),
              ('SAM', '62,797', 'PAUD + primary schools', 'Central Java + D.I. Yogyakarta'),
              ('SOM · BEACHHEAD', '7,123', 'PAUD + primary schools', 'D.I. Yogyakarta')],
    'why': 'Why here: our first real-world pilot was already conducted in D.I. Yogyakarta.',
    'buyer': ('BUYER', 'Principals · teachers · activity coordinators'),
    'user': ('USER', 'Children aged 3–10'),
    'target_label': 'YEAR-1 COMMERCIAL TARGET',
    'target': '48 paid sessions',
    'target_note': 'Transaction target, not 48 unique institutions.',
    'source': 'Source: Kemendikdasmen education reference data (public and private units), accessed September 2026. '
              'Institution counts describe market coverage, not confirmed demand. Breakdown in the appendix.',
    'notes': '0:30 · TAM 420,886 PAUD and primary schools in Indonesia; SAM 62,797 in Central Java and DIY; our '
             'beachhead is DIY with 7,123, where we already piloted. Buyers: principals, teachers, coordinators; '
             'users: children 3–10. Year-1 target: 48 paid sessions, a transaction target.',
}

# ---------------------------------------------------------------- 7 competition
COMPETITION5 = {
    'title': 'A Proven Category, With a Different Access Model',
    'intro': 'Paper-to-digital coloring already has established alternatives, including:',
    'alternatives': [('Faber-Castell ARt Alive', 'Mobile app'), ('Quiver', 'Mobile app'),
                     ('WAGZAK JUMP', 'Mobile app'), ('teamLab Sketch Aquarium', 'Venue-based')],
    'callouts': ['Child’s artwork is the character', 'Runs in the browser', 'Shared ocean world'],
    'combines_title': 'SCANVAS COMBINES',
    'combines': ['Child-generated artwork as the character', 'Browser-based: no app installation',
                 'Shared interactive worlds', 'Reusable engine for new themes',
                 'Designed toward repeat institutional use'],
    'next_test': 'Competitors validate the category. Our question is whether this combination creates paid, repeat use.',
    'notes': '0:25 · Faber-Castell, Quiver, WAGZAK need an app; teamLab is a venue. They validate the category. '
             'Scanvas combines the child’s artwork, browser access, shared worlds, and a reusable engine. Our '
             'question: does this combination create paid, repeat use?',
}

# ---------------------------------------------------------------- 8 business model
BUSINESS5 = {
    'title': 'Paid Sessions First. Family Packs Alongside.',
    # (tag, style, heading, sub, price, flow, validate)
    'paths': [('B2B · PRIMARY VALIDATION', 'primary', 'Managed School / Event Session', 'Up to 30 children',
               'Rp1,000,000 / session', ['Direct outreach', 'Demo', 'Paid session', 'Rebooking'],
               'Paid booking · delivery cost · rebooking'),
              ('B2C · ALONGSIDE', 'second', 'Family Creative Pack', 'For use at home', 'Rp49,000 / pack',
               ['Short video', 'Free trial', 'WhatsApp order', 'Repeat purchase'],
               'Conversion · contribution margin · repeat purchase')],
    'footer': 'Both prices are commercial-testing assumptions and are not yet validated at scale.',
    'notes': '0:30 · B2B first: a managed session for up to 30 children at a test price of Rp1M; we validate paid '
             'booking, delivery cost, rebooking. B2C alongside: a family pack at Rp49K via short video, free trial, '
             'WhatsApp order. Both prices are test assumptions.',
}

# ---------------------------------------------------------------- 9 team (roles + equity as in the ITEC application)
TEAM5 = {
    'title': 'Two Founders Cover Product and Go-to-Market',
    'team': [('Haikal Hilmi', 'CEO & Co-Founder', 'founder_hh.png',
              ['Product and company strategy', 'Product and engineering', 'Computer-vision scanning',
               'Interactive web platform', 'Partnership strategy']),
             ('Salsabila Khoirunnisa', 'CMO & Co-Founder', 'founder_sk.png',
              ['Brand and marketing', 'Customer discovery', 'Institutional outreach', 'Community',
               'Go-to-market'])],
    'equity': 'Equity: Haikal 60% · Salsabila 40%',
    'execution_title': 'EXECUTION TO DATE',
    'execution': 'Live product · 2 interactive worlds · first 30-child pilot',
    'next_title': 'NEXT CAPABILITY TO STRENGTHEN',
    'next': 'Institutional sales and repeatable session delivery.',
    'notes': '0:35 · Haikal, CEO with 60%, leads product, strategy, and technology; Salsabila, CMO with 40%, leads '
             'brand, customers, and go-to-market. Together: live product, two worlds, first pilot.',
}

# ---------------------------------------------------------------- 10 roadmap
ROADMAP5 = {
    'title': 'Prove Paid Demand → Prove Repeat Use → Expand',
    # (tag, heading, items, done)
    'stages': [('COMPLETED', 'Built & tested', ['Live product', 'Ocean + Vehicle worlds', 'First 30-child pilot',
                                                'Digital trial'], True),
               ('MONTHS 1–3', 'Prove paid demand', ['Test B2B session pricing', 'Test B2C pack pricing',
                                                    'Measure delivery cost', 'Begin paid sessions',
                                                    'Measure scan reliability'], False),
               ('MONTHS 4–6', 'Prove repeat use', ['Pilot Scanvas Studio', 'Run a 3-lesson creative pilot',
                                                   'Measure institutional rebooking', 'Measure family repeat purchase',
                                                   'Measure 3-lesson progression'], False),
               ('MONTHS 7–12', 'Scale what works', ['48 cumulative paid sessions', '600 family packs', '2 → 4 worlds',
                                                    'Scanvas Studio operational', 'Partner-led localization pilot'],
                False)],
    'footer': 'Expansion happens only after evidence of paid demand and repeat use.',
    'notes': '0:30 · Months 1–3 prove paid demand; months 4–6 prove repeat use; months 7–12 scale what works: 48 '
             'sessions, 600 packs, four worlds, Studio, a partner-led localization pilot.',
}

# ---------------------------------------------------------------- 11 economics + ask (founders' model, Sep 2026)
FUNDS5 = {
    'title': 'Rp200M to Prove Repeatable Economics',
    # (heading, rows, margin)
    'units': [('B2C PACK · TEST ECONOMICS', [('Price', 'Rp49K'), ('Direct cost', 'Rp20K'), ('Contribution', 'Rp29K')],
               '59% contribution margin'),
              ('MANAGED SESSION · TEST ECONOMICS', [('Price', 'Rp1M'), ('Direct cost', 'Rp250K'),
                                                    ('Contribution', 'Rp750K')], '75% contribution margin')],
    'base_title': '12-MONTH BASE CASE',
    'base_volume': '600 packs · 48 paid sessions',
    'base_rows': [('Revenue', 'Rp77.4M'), ('Direct costs', 'Rp24.0M'), ('Gross contribution', 'Rp53.4M')],
    'base_margin': '69% contribution margin',
    'capital_title': 'CAPITAL REQUIRED',
    'capital': 'Rp200M',
    'capital_period': '12 months',
    'use': [('48%', 'Team & operations'), ('15%', 'Go-to-market'), ('12%', 'Product & technology'),
            ('10%', 'Production'), ('10%', 'Content'), ('5%', 'Legal & contingency')],
    'cac': 'CAC and LTV are not yet claimed as proven metrics. This validation period is designed to measure '
           'acquisition cost, repeat purchase, and institutional rebooking before scaling.',
    'notes': '0:40 · Test economics: pack Rp49K, direct cost Rp20K, 59%; session Rp1M, direct cost Rp250K, 75%. Base '
             'case: 600 packs and 48 sessions, Rp77.4M revenue, Rp53.4M contribution. We need Rp200M for 12 months; '
             'half is founder time. CAC and LTV are what this period measures. Full projection in the appendix.',
}

# ---------------------------------------------------------------- 12 ITEC / Chaoyang
CLOSING5 = {
    'title': 'What We Want to Validate Through ITEC',
    'asks': [('school', 'Institutional pilot partners', 'Schools and activity organizers for paid, repeatable '
                                                        'sessions.'),
             ('layers', 'Content & localization partners', 'Children’s content creators and cultural partners for '
                                                          'localized worlds.')],
    'pilot_title': 'A small partner-led Chaoyang pilot',
    'steps': [('LOCAL PARTNER', 'Select one institution or activity partner'),
              ('LOCALIZE', 'Mandarin interface + one adapted Scanvas theme'),
              ('PILOT', 'Proposed small session with 20–30 children'),
              ('MEASURE & DECIDE', 'Completion · partner feedback · willingness to repeat or pay · localization '
                                   'effort')],
    'resources_title': 'RESOURCES',
    'resources': ['Scanvas product and founder lead', 'Local partner / translator', 'Localized print templates',
                  'Adapted digital content'],
    'principle_title': 'FUNDING PRINCIPLE',
    'principle': 'Initial localization is a validation experiment funded from the go-to-market and content budget. '
                 'We do not commit to a broader China rollout until the pilot shows demand.',
    'closing': 'Validate locally. Adapt with a partner. Expand only with evidence.',
    'people': FOUNDERS,
    'website': 'scanvas.id',
    'qr_label': 'TRY IT',
    'notes': '0:40 · Through ITEC: institutional pilot partners, content and localization partners, and a small '
             'partner-led Chaoyang pilot: one partner, Mandarin interface and one adapted theme, 20–30 children, then '
             'measure and decide. Funded from our GTM and content budget; no broader China rollout before evidence. '
             '(No partner or commitment exists yet.)',
}

# ---------------------------------------------------------------- appendix
SUPPORTING_SUB = 'For Q&A · competition · market data · technology · financial assumptions · Chaoyang pilot'
# geographic expansion logic: no TAM / SAM / SOM chips here (slide 6 explains them)
SLIDE_MARKET_SIZE = {**SLIDE_MARKET_SIZE, 'stages': [(st[0], '', *st[2:]) for st in SLIDE_MARKET_SIZE['stages']]}

# 12-month projection: founders' model (content_dsc.py financial-model block), plus the cash plan it implies
FINANCIALS5 = {
    'title': '12-Month Financial Projection',
    'head': ['', 'Conservative', 'Base'],
    # (label, conservative, base, style) style: '' row · 'sum' subtotal · 'sub' indented detail · 'cash' highlight
    'rows': [('B2C packs sold', '300', '600', 'sub'),
             ('Paid sessions', '24', '48', 'sub'),
             ('B2C pack revenue', 'Rp14.7M', 'Rp29.4M', ''),
             ('B2B session revenue', 'Rp24.0M', 'Rp48.0M', ''),
             ('Customer revenue', 'Rp38.7M', 'Rp77.4M', 'sum'),
             ('Direct costs', '−Rp12.0M', '−Rp24.0M', ''),
             ('Gross contribution (69%)', 'Rp26.7M', 'Rp53.4M', 'sum'),
             ('Team (2 founders × Rp4M × 12)', '−Rp96.0M', '−Rp96.0M', 'sub'),
             ('Go-to-market', '−Rp24.0M', '−Rp24.0M', 'sub'),
             ('Product, infrastructure & tools', '−Rp18.0M', '−Rp18.0M', 'sub'),
             ('Content creation', '−Rp15.0M', '−Rp15.0M', 'sub'),
             ('Legal & admin', '−Rp5.0M', '−Rp5.0M', 'sub'),
             ('Operating expenses', '−Rp158.0M', '−Rp158.0M', ''),
             ('Net result, year 1', '−Rp131.3M', '−Rp104.6M', 'sum'),
             ('Cash at month 12 with Rp200M', 'Rp68.7M', 'Rp95.4M', 'cash')],
    'cash_title': 'CASH PLAN',
    'cash': ['Operating burn ≈ Rp13.2M per month (Rp158M / 12).',
             'With Rp200M, cash at month 12 stays positive in both cases.',
             'Remaining cash covers inventory (production budget), contingency, and runway into year 2.'],
    'assump_title': 'ASSUMPTIONS',
    'assumptions': ['Pack Rp49K; direct cost Rp20K (print & packaging Rp10K, delivery Rp10K)',
                    'Session Rp1M, up to 30 children; direct cost Rp250K',
                    'Volume: 25–50 packs and 2–4 sessions per month',
                    'Platform-only (per-drawing) revenue excluded',
                    'CAC and LTV measured during validation, not assumed'],
    'basis': 'Founders’ 12-month financial model, Sep 2026. All prices, costs, and volumes are planning assumptions, '
             'not validated at commercial volume. Grant or prize money would be financing, never revenue.',
    'notes': 'If asked for 18 months: months 13–18 are not projected yet; the plan is to re-forecast from real '
             'conversion, rebooking, and delivery cost after the first six months.',
}

CHAOYANG5 = {
    'title': 'Chaoyang Pilot: Validation Before Expansion',
    'objective_title': 'OBJECTIVE',
    'objective': 'Test whether Scanvas can transfer to a new language and cultural context through a local partner.',
    'scope_title': 'SCOPE',
    'scope': ['One partner', 'One localized theme', 'Mandarin adaptation', 'Small child session',
              'No permanent China operation'],
    'measure_title': 'MEASURE',
    'measure': ['Activation / completion', 'Scan success', 'Children’s engagement', 'Partner willingness to repeat',
                'Parent / institution willingness to pay', 'Localization cost and effort'],
    'gate_title': 'GO / NO-GO GATE',
    'gate': 'Scale only if demand, repeat intent, and localization economics justify the next pilot.',
    'notes': 'A proposal, not a commitment: no partner exists yet. Funded from the GTM and content budget.',
}
