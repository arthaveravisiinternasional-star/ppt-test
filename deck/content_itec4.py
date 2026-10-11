"""ITEC SEA 2026 · official-template edition (v4), Digital Culture Track.

Built by build_deck_itec4.py on the committee's template (assets/template/itec_official.pptx: blue/green frame, ITEC
2026 logo on the cover). Copy = ITEC v3 final (content_itec3.py), mapped onto the committee's section order:
Problem, Solution, Product, About, Target Market, Market Size, Competitors, UVP, Competitive Advantage, Business Model,
Team, Roadmap, The Ask, Contact, Supporting slides.

Honesty rules (same as v3): live product, 2 worlds, one completed 30-child pilot, pre-revenue. No LMS, no China
partner, no paid customers, no recurring revenue, no validated pricing, no proprietary AI, no funding amount.
Use of funds and exit strategy use the founders' 12-month financial model (Sep 2026, same numbers as the DSC deck):
capital need Rp200M; pack Rp49K and session Rp1M are test assumptions, labelled as such.
"""
from .content_itec3 import *  # noqa: F401,F403  (v3 copy is the base; overrides below)
from . import content_itec2 as V2
from . import content_itec3 as V3

SLIDE_REPEAT = {**V3.SLIDE_REPEAT, 'cols': [
    (*col[:4], [[(t, {**o, 'font': 'Roboto Condensed SemiBold'}) for t, o in b] if isinstance(b, list) else b
                for b in col[4]], *col[5:]) for col in V3.SLIDE_REPEAT['cols']]}   # template typography
SLIDE_4_SOLUTION = {**V3.SLIDE_4_SOLUTION, 'qr_y': 0.62}   # clear the section label
SLIDE_5_PRODUCT = {**V2.SLIDE_5_PRODUCT, 'title': 'Scanvas Runs Live\nin Any Browser', 'qr_label': 'TRY IT LIVE'}

# Live demo: the digital trial recorded end to end on the live product (production build, real input), no edits to
# the app. Video and poster in assets/video; the poster is what PDF readers and an unplayed slide show.
SLIDE_DEMO = {
    'tag': 'LIVE DEMO',
    'title': 'See the Digital Trial\nin 37 Seconds',
    'video': 'video/trial_digital_itec.mp4',
    'poster': 'video/trial_digital_itec_poster.png',
    'steps': [
        ('Pick a drawing', 'Free, in any browser'),
        ('Color it in the browser', 'Tap inside the lines'),
        ('Watch it come alive', 'The child\u2019s own colors swim'),
        ('It joins a shared ocean', 'One living world for every drawing'),
        ('Learn a fact, hear its sound', 'Play turns into learning'),
    ],
    'caption': 'Recorded on the live product: no app, no account. Click the video to play.',
    'chips': ['No app', 'No account', 'Any browser'],
    'notes': ('A 37-second walk through the free digital trial, recorded on the live product. A child picks the whale, '
              'colors it in the browser, brings it to life, sees it swim in a shared ocean, then reads a fact and '
              'hears the whale. Click the video to play; it runs without sound until the whale\u2019s call at the end.'),
}

# ---------------------------------------------------------------- 1 cover (template slide 1)
COVER = {
    'label': 'PITCH DECK',
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity\nComes Alive',
    # template: project summary, not more than 15 words
    'summary': 'Children turn their own paper drawings into interactive characters and worlds, directly in the browser.',
    'presenters': [('Haikal Hilmi', 'CEO & Co-Founder'), ('Salsabila Khoirunnisa', 'CMO & Co-Founder')],
    'company': 'Scanvas · scanvas.id',
    'proof': V3.SLIDE_1_COVER['proof'],
    'notes': V3.SLIDE_1_COVER['notes'],
}

# ---------------------------------------------------------------- 5 about your company
SLIDE_ABOUT = {
    'title': 'Scanvas Builds a Physical-to-Digital\nCreation Engine for Children',
    'summary': 'Children aged 3–10 color a printed Scanvas sheet, scan it in the browser, and their own artwork becomes '
               'an animated character inside an interactive world with sound, stories, and facts.',
    'mission': 'Our mission: children do not only consume digital culture — they participate in creating it.',
    'facts': [('globe', 'Live product', 'scanvas.id · public digital trial · no app required'),
              ('compass', '2 interactive worlds', 'Ocean + Vehicle'),
              ('users', 'First 30-child pilot', 'One TPA in D.I. Yogyakarta · five product changes from feedback'),
              ('flask-conical', 'Pre-revenue', 'Pricing and repeat value are being validated')],
    'image': 'ph_world.png',
    'notes': 'What Scanvas does in one breath, then the four facts that are true today.',
}

# ---------------------------------------------------------------- 7 target market
SLIDE_TARGET = {
    'title': 'Two Buyers, One User: Children Aged 3–10',
    'user': 'USER · children aged 3–10 who create first',
    # (tag, heading, image, rows of (label, text), reach flow)
    'markets': [('TARGET MARKET 1 · FIRST BEACHHEAD', 'Institutions', 'm_session.png',
                 [('Buyer', 'PAUD / TK / TPA owner or principal · school or activity organizer'),
                  ('Use case', 'Creative classroom or activity session'),
                  ('Why they buy', 'A ready-made creative activity that ends with every child’s artwork alive')],
                 ['Demo', 'Pilot', 'Paid session', 'Repeat'], 'Target acquisition loop'),
                ('TARGET MARKET 2 · AVAILABLE NOW', 'Families', 'm_pack.png',
                 [('Buyer', 'Parents of children aged 3–10'),
                  ('Use case', 'Creative play at home with a physical pack'),
                  ('Why they buy', 'Screen time that starts with their child creating, not swiping')],
                 ['Short video', 'Digital trial', 'Creative pack', 'New world'], 'How we reach them')],
    'notes': 'Institutions are the first distribution beachhead (demo, pilot, paid session, repeat is the target '
             'loop, not history). Families can buy packs today.',
}

# ---------------------------------------------------------------- 8 market size (staircase, TAM/SAM/SOM)
SLIDE_MARKET_SIZE = {
    'title': 'Start With a Reachable Beachhead,\nThen Scale Distribution',
    'method': 'Bottom-up: count of PAUD + primary-school units (our institutional buyers), plus a BPS-based estimate '
              'of children aged 3–10.',
    # (stage, size label, geography, value, unit, description)
    'stages': [('WEDGE', 'SOM', 'D.I. Yogyakarta', '7,123', 'PAUD + primary schools',
                'First institutional beachhead, where our first pilot ran.'),
               ('SCALE', 'SAM', 'Central Java + DIY', '62,797', 'PAUD + primary schools',
                'School sessions, events, and Scanvas Studio.'),
               ('NATIONAL', 'TAM', 'Indonesia', '420,886', 'PAUD + primary schools',
                '≈35.3M children aged 3–10.*'),
               ('EXPAND', '', 'Southeast Asia', 'SEA', 'same engine, local content',
                'New languages, worlds, cultural content, partners.')],
    'footer': V3.SLIDE_MARKET['footer'],
    'source': V3.SLIDE_MARKET['source'],
    'notes': V3.SLIDE_MARKET['notes'],
}

# ---------------------------------------------------------------- 9 competitors (direct / indirect header on the table)
SLIDE_COMPETITION = {
    **V3.SLIDE_COMPETITION,
    'title': 'Competitors Prove the Category; Scanvas Combines\nWeb Access, Personalisation, and Shared Worlds',
    'title_size': 19,
    'groups': [('DIRECT', 1, 3), ('INDIRECT', 4, 4)],   # (label, first player column, last player column)
    'source': 'Indirect competition also includes video and game apps that compete for screen time. Evidence checked '
              'Sep 2026 on each product’s official site.',
}

# ---------------------------------------------------------------- 10 unique value proposition
SLIDE_UVP = {
    'title': 'Why Choose Scanvas?',
    'lead': 'The child’s own drawing becomes an interactive character in a shared world — in the browser, with no app '
            'to install.',
    # (heading, text) for the three circles
    'circles': [('Own creation', 'The child’s artwork is the character, not a stock one'),
                ('Web access', 'Works in the browser on a phone or laptop'),
                ('Shared worlds', 'Characters live together in interactive worlds')],
    'proof': 'Among the products we compared (Faber-Castell ARt Alive, Quiver, WAGZAK JUMP, teamLab Sketch Aquarium), '
             'Scanvas is the only one combining all three.',
    'notes': 'UVP = the overlap of own creation, web access, and shared worlds. Scope of the claim: the four products '
             'in our comparison table.',
}

# ---------------------------------------------------------------- 15 team
SLIDE_TEAM = {
    'title': 'Complementary Founders: Business and Technology',
    'team': [('Haikal Hilmi', 'CEO & Co-Founder', 'founder_hh.png',
              ['Product & engineering', 'Computer vision', 'Interactive platform']),
             ('Salsabila Khoirunnisa', 'CMO & Co-Founder', 'founder_sk.png',
              ['Business & partnerships', 'Customer discovery', 'Go-to-market'])],
    'closing': V2.SLIDE_NEXT['closing'],
    'notes': 'Two co-founders: Salsabila leads business, partnerships, and GTM; Haikal leads product, engineering, and '
             'computer vision.',
}

# ---------------------------------------------------------------- 16 roadmap (ask moves to its own slide)
SLIDE_NEXT = {**V3.SLIDE_NEXT, 'ask': []}

# ---------------------------------------------------------------- 17 the ask
SLIDE_ASK = {
    'title': 'Through ITEC, We Want to Find',
    'lead': 'Our ask: Rp200M for 12 months of validation (next slide), plus partners and guidance through ITEC.',
    # (icon, heading, detail, roadmap stage it unlocks)
    'asks': [('layers', 'Content & IP partners',
              'Children’s content, cultural, and character partners to co-create new worlds.', 'SCALE'),
             ('school', 'Institutional distribution partners',
              'School networks, PAUD / TK / TPA groups, and activity organizers for demo → pilot.', 'NEXT'),
             ('globe', 'ASEAN / China pilot opportunities',
              'Partner-led localisation pilots: language, cultural themes, children’s content.', 'SCALE'),
             ('rocket', 'Commercialisation & market entry',
              'Guidance on pricing validation, go-to-market, and regional entry.', 'NEXT')],
    'notes': 'No funding amount in this deck. The ask is partners and guidance, each tied to a roadmap stage.',
}

# ---------------------------------------------------------------- 18 the ask: use of funds (founders' model, Sep 2026)
# Single source of truth: the financial-model comment block in content_dsc.py (Rp200M, base case Rp77.4M).
SLIDE_FUNDS = {
    'title': 'Rp200M Funds 12 Months to Prove\nPaid, Repeat Use',
    'label': '12-MONTH CAPITAL NEED',
    'amount': 'Rp200M',
    'usd': '≈ US$12K (at Rp16,500 / US$, indicative)',
    'purpose': 'Founder runway, scan reliability, Scanvas Studio, school acquisition, production, and new worlds, '
               'so the next round is raised on proven repeat use.',
    'alloc_title': 'USE OF FUNDS',
    # (icon, use, detail, Rp million)
    'alloc': [('users', 'Team & operations', 'Two founders at Rp4M / month each', 96),
              ('school', 'Go-to-market', 'School pilots, demos, community activation', 30),
              ('scan-line', 'Product & technology', 'Infrastructure, scan reliability, Studio', 24),
              ('palette', 'Production', 'Packs, samples, demo materials', 20),
              ('book-open', 'Content', '2 → 4 interactive worlds', 20),
              ('shield-check', 'Legal & contingency', 'Administration, accounting, contracts', 10)],
    'unlocks_title': 'MILESTONES IT UNLOCKS · 12 MONTHS',
    'unlocks': ['48 paid school / event sessions', '1,440 children in paid sessions', '600 family packs',
                '4 interactive worlds', 'Scanvas Studio operational', '≥20% repeat purchase / rebooking',
                'Rp77.4M first-year revenue (base case)'],
    'basis': 'Founders’ 12-month financial model, Sep 2026. Base case assumes family pack Rp49K and managed session '
             'Rp1M (up to 30 children): current test assumptions, not yet validated at commercial volume.',
    'notes': 'Why Rp200M when year-1 revenue is Rp77.4M? The first 12 months build the repeatable system and prove '
             'repeat use; unit contribution is positive (pack 59%, session 75%). Team is Rp4M per founder per month.',
}

# ---------------------------------------------------------------- 19 exit strategy (indicative)
SLIDE_EXIT = {
    'title': 'Exit Strategy: Build a Content & IP Engine\nThat Strategic Buyers Want',
    'lead': 'Indicative path, not a commitment: build proven value first, keep exit options open.',
    # (period, heading, detail)
    'timeline': [('0–12 MONTHS', 'Prove repeat use', '48 paid sessions · ≥20% repeat · Rp77.4M base case'),
                 ('YEARS 1–3', 'Scale distribution', 'More worlds, school networks, ASEAN localisation'),
                 ('YEARS 3–5', 'Content & IP platform', 'Licensing, partner content, regional institutions'),
                 ('YEAR 5+', 'Exit window', 'Strategic acquisition or later-stage buyout')],
    # (tag, heading, detail, primary)
    'options': [('PRIMARY', 'Strategic acquisition',
                 'Edtech platforms, children’s publishers, stationery and toy brands, or media / IP companies gain '
                 'a ready engine, a content library, and school distribution.', True),
                ('BRIDGE', 'Licensing & partnerships',
                 'License the engine and worlds to brands and publishers: revenue now, acquirer relationships later.',
                 False),
                ('ALTERNATIVE', 'Secondary sale',
                 'Later-stage investors buy early shareholders out as Scanvas scales across ASEAN.', False),
                ('LONG-TERM', 'IPO',
                 'Only at regional scale; not part of the near-term plan.', False)],
    'value': 'What makes Scanvas acquirable: reusable world engine · child-generated content format · institutional '
             'distribution · privacy-by-design child data',
    'notes': 'Exit is indicative. Most realistic: strategic acquisition by a company that wants the engine, the '
             'content, and school distribution. No acquirer talks exist today.',
}

# ---------------------------------------------------------------- 20 contact
SLIDE_CONTACT = {
    'title': 'CONTACT US',
    'rows': [('globe', 'Website', 'scanvas.id', 'https://www.scanvas.id/'),
             ('message-circle', 'WhatsApp', '+62 895-3675-97379', 'https://wa.me/62895367597379')],
    'people': 'Haikal Hilmi · CEO   |   Salsabila Khoirunnisa · CMO',
    'qr': 'qr_scanvas_trial.png',
    'qr_label': 'TRY IT LIVE · scanvas.id/trial',
    'notes': 'Contacts from the public website (scanvas.id).',
}

SUPPORTING = 'SUPPORTING SLIDES'
