"""Founders Arena / DSC Season 17, v4 (Oct 2026). 15 main slides + 4 appendix, same order and look as DSC v3.

Built by build_deck_dsc4.py, which swaps this module in for deck.content. v4 = DSC v3 + the ITEC v3 validation
strategy (prove magic -> prove repeat value -> validate commercial model -> scale) + clearer commercial and financial
evidence, after the judges' feedback of 8 Oct 2026. DSC v3 files (content_dsc.py, slides_dsc.py) are untouched.

Locked decisions: interactive educational toy growing into a creative learning platform · live, early validation,
pre-revenue · B2B-first, B2C as direct sales + validation channel · Ocean Artist 3-lesson pilot before any LMS ·
Studio built as institutional pilots need it · DIY -> Central Java -> Indonesia · Rp200M 12-month capital plan.
Team for DSC: Haikal Hilmi CEO, Salsabila Khoirunnisa CMO (confirmed by the founders, Oct 2026).

Honesty rules: no LMS / course claim, no validated pricing, per-drawing platform price is a test hypothesis only (not
shown as a price). All projections are the founders' Sep 2026 model (content_dsc.py) and are labelled as projections.
'[TBD]' renders yellow where a value tile is used and must stay until the founders confirm it.
"""
from . import content_dsc as V3
from . import content_itec2 as I2
from . import content_itec3 as I3

TRACK = 'DSC Season 17 · Founders Arena'
WEBSITE = 'scanvas.id'
PILOT_ART = I3.PILOT_ART

# ---------------------------------------------------------------- financial model (unchanged from DSC v3, Sep 2026)
# B2C pack Rp49,000: direct cost Rp20,000 -> contribution Rp29,000 (59%)
# B2B managed session Rp1,000,000 (up to 30 children): direct cost Rp250,000 -> contribution Rp750,000 (75%)
# 12 months: conservative 300 packs + 24 sessions = Rp38.7M; base 600 packs + 48 sessions = Rp77.4M
# direct costs Rp12M / Rp24M -> gross contribution Rp26.7M / Rp53.4M; OPEX Rp158M -> net -Rp131.3M / -Rp104.6M
# cash at month 12 with Rp200M = 200 + revenue - direct costs - OPEX = Rp68.7M / Rp95.4M
# Rp200M plan lines: team 96 · GTM 30 · product 24 · production 20 · content 20 · legal & contingency 10
# vs P&L OPEX 158 (team 96 · GTM 24 · product 18 · content 15 · legal 5): production 20 funds direct costs before
# revenue arrives; the other 22 (GTM 6 · product 6 · content 5 · legal/contingency 5) is headroom held for the gates.

# ---------------------------------------------------------------- 1 cover (shared s1_cover) · Keep
SLIDE_1_COVER = {
    **V3.SLIDE_1_COVER,
    'founder_name': 'Haikal Hilmi · CEO & Co-Founder',
    'founder_role': 'Salsabila Khoirunnisa · CMO & Co-Founder',
    'name_box_w': 3.1,
}

# ---------------------------------------------------------------- 2 business overview (slides_dsc.s_overview) · Minor
SLIDE_OVERVIEW = {
    **V3.SLIDE_OVERVIEW,
    'tag': 'LIVE · scanvas.id · early validation · pre-revenue',
    'blocks': [('palette', 'Product',
                'Children color a Scanvas sheet, photograph it in the browser, and their own artwork comes alive '
                'with motion, sound, and facts.'),
               ('school', 'Customers · B2B-first',
                'Schools, PAUD/TK, TPA, and event organizers buy sessions for many children. Parents buy packs: '
                'our direct sales and validation channel.'),
               ('wand-sparkles', 'Value proposition',
                'Hands-on creativity stays at the center; technology extends it into interactive learning, with '
                'no app to install.')],
    'notes': 'Live today with two worlds and a public digital trial; one 30-child pilot done. Pre-revenue. Our '
             'commercial focus is B2B first, with B2C packs as direct sales and demand validation.',
}

# ---------------------------------------------------------------- 3 problem & opportunity (slides_dsc4.s_problem) · Minor
SLIDE_2_PROBLEM = {
    **V3.SLIDE_2_PROBLEM,
    'message': 'Children love drawing and coloring, but once the page is finished, the learning moment ends. '
               'Many screen-based activities are built around watching and swiping, not creating.',
    'closing': '',
    'inst_tag': 'FOR SCHOOLS & ORGANIZERS · VALIDATING',
    'inst': 'Creative sessions for 20–30 children need ready-made activities that are engaging, educational, and '
            'easy for teachers to run.',
    'opportunity': 'Opportunity: join hands-on creativity, digital play, and learning.',
    'notes': 'Families: creativity stops at the paper; screens are passive. Institutions: we are validating whether '
             'schools and organizers struggle to run engaging creative sessions for whole groups. This second problem '
             'is a hypothesis from our pilot conversations, not a measured finding.',
}

# ---------------------------------------------------------------- 4 solution (slides_dsc.s_solution) · Keep
SLIDE_4_SOLUTION = V3.SLIDE_4_SOLUTION

# ---------------------------------------------------------------- 5 market (slides_itec3.s_market) · Major
SLIDE_MARKET = {
    'title': 'Market Size & Target Market',
    'icp_label': 'INITIAL CUSTOMER',
    'icp': [('Buyer', 'PAUD / TK / TPA owner or principal · school or event organizer · parent'),
            ('User', 'Children 3–10'),
            ('Use case', 'Creative classroom / activity session'),
            ('Target acquisition loop', 'DEMO → PILOT → PAID SESSION → REPEAT')],
    'stages': [('BEACHHEAD', 'D.I. Yogyakarta', '7,123', 'PAUD + primary schools',
                'Where our first pilot ran and where we deliver locally.'),
               ('NEXT', 'Central Java + DIY', '62,797', 'PAUD + primary schools',
                'Same team, reachable by road; sessions and events.'),
               ('NATIONAL', 'Indonesia', '420,886', 'PAUD + primary schools',
                '≈35.3M children aged 3–10.*'),
               ('12-MONTH TARGET', 'Base case', '≈40', 'paying institutions',
                '48 paid sessions with ≥20% rebooking · plus 600 family packs.')],
    'footer': 'Institution counts are the education units we can reach, not paying customers. The 12-month target is '
              '≈0.6% of DIY institutions.',
    'source': 'Sources: Kemendikdasmen Data Referensi Pendidikan (PAUD, SD), accessed Sep 2026 · *estimated from BPS '
              'population by 5-year age group, 2022. Details in Appendix B.',
    'notes': 'We size by institutions and geography instead of TAM/SAM/SOM. DIY first, then Central Java, then '
             'Indonesia. The realistic 12-month target: about 40 paying institutions (48 sessions / 1.2 with 20% '
             'rebooking), about 0.6% of DIY units, plus 600 family packs. This is the base case, not a forecast we '
             'have proven.',
}

# ---------------------------------------------------------------- 6 competition (slides_itec3.s_competition) · Major
SLIDE_COMPETITION = {
    **I3.SLIDE_COMPETITION,
    'title': 'Competitive Landscape',
    'title_size': 26,
    'title_w': 7.0,
    'sub': 'Competitors prove the category; Scanvas combines web access, the child’s own character, and shared worlds.',
    'wins': [],
    'source': 'Rows include axes where competitors lead. Evidence checked Sep 2026 on each product’s official site '
              '(Appendix D).',
    'notes': 'We do not claim to be first: color, scan, alive is a proven behavior. Competitors lead on content '
             'library, brand, and reach; we lead on browser access, shared worlds, and an affordable institutional '
             'session format for Indonesian schools.',
}

# ---------------------------------------------------------------- 7 business model (slides_dsc4.s_business) · Major
SLIDE_BUSINESS = {
    'title': 'Business Model & Revenue Streams',
    'lead': 'Pre-revenue. B2B-first; B2C is our direct sales and validation channel. Each stream has a clear status.',
    # (segment, heading, description, price, detail, image, (tag, style))  style: live|validating|building|future
    'offers': [('B2C · PHYSICAL PACKS', 'Coloring Packs',
                '10 A5 coloring sheets per world plus the digital experience. Ordered via website → WhatsApp.',
                'Rp49,000 / pack', 'Conversion and repeat purchase still to be proven', 'm_pack.png',
                ('AVAILABLE · PRE-REVENUE', 'live')),
               ('B2B · MANAGED SESSIONS', 'Educational Sessions',
                'A complete Scanvas activity run by our team for classrooms and events.',
                'From Rp1,000,000 / session', 'Up to 30 children · target: paid session + rebooking',
                'm_session.png', ('VALIDATING', 'validating')),
               ('B2B · STUDIO', 'Self-Operated Platform',
                'Bulk drawing processing, session management, and a shared world; the institution runs it.',
                'Usage-based', 'Per-drawing price is a test hypothesis, set in pilots', 'm_studio.png',
                ('IN DEVELOPMENT', 'building')),
               ('LEARNING · CONTENT', 'Lessons & New Worlds',
                'Creative lessons, programs, and new worlds. Starts with the Ocean Artist 3-lesson pilot.',
                'Subscription later', 'Only if the 3-lesson pilot proves repeat use', 'm_lesson.png',
                ('FUTURE · PILOT PLANNED', 'future'))],
    'notes': 'Four streams, each with an honest status. Packs are offered at Rp49K but have no proven conversion yet. '
             'Managed sessions are offered from Rp1M for up to 30 children and are being validated. Studio is in '
             'development; per-drawing pricing is only a test assumption. Learning content starts with a 3-lesson '
             'pilot; we do not build a full LMS before that pilot shows repeat use. Projections use packs and managed '
             'sessions only.',
}

# ---------------------------------------------------------------- 8 traction (slides_itec3.s_traction) · Major
SLIDE_TRACTION = {
    **I3.SLIDE_TRACTION,
    'title': 'Traction & Validation',
    'title_w': 4.6,
    'title_size': 26,
    'metrics': [('30', 'children in first TPA pilot'), ('2', 'interactive worlds live'),
                ('2', 'improvements shipped'), ('3', 'improvements in progress')],
    'photo_caption': 'First real-world pilot · TPA, D.I. Yogyakarta · live product, pre-revenue',
    'notes': 'One pilot at a TPA with 30 children; they were not paying customers. Feedback produced five product '
             'changes: two shipped (larger world, digital trial), three in progress. Pre-revenue.',
}

# ---------------------------------------------------------------- 9 GTM (slides_dsc4.s_gtm) · Minor
SLIDE_GTM = {
    'title': 'Marketing & Go-To-Market',
    # (chip, audience, funnel steps, channels)
    'tracks': [('B2B', 'Schools & events · priority', ['Outreach', 'Live demo', 'Small pilot', 'Paid session',
                                                       'Repeat booking'],
                'PAUD/TK & TPA · event organizers · activity centers · partnerships'),
               ('B2C', 'Families · validation', ['Short video', 'Digital trial', 'First pack', 'Repeat purchase'],
                'Instagram & TikTok · parent communities · referrals · website → WhatsApp')],
    'pillars': [('sparkles', 'Acquisition', 'Show the “color → scan → alive” moment in live demos and short videos.'),
                ('target', 'Conversion', 'Every demo asks for a paid session; every digital trial points to a pack.'),
                ('repeat', 'Retention', 'Ocean Artist lessons and new worlds give children a reason to come back.')],
    'notes': 'B2B is the priority: demo, pilot, paid session, then repeat booking. B2C validates demand directly: '
             'trial, first pack, repeat purchase. We measure each step.',
}

# ---------------------------------------------------------------- 10 impact (slides_dsc.s_impact) · Keep
SLIDE_IMPACT = {
    **V3.SLIDE_IMPACT,
    'governance': 'Minimal child data, consent by adults · learning outcomes not yet measured',
    'kpis_title': 'Indicators we will track',
    'kpis': ['Children reached per session', 'Scan success (drawing → alive)', 'Lesson completion (pilot)',
             'Repeat participation', 'Simple learning recall', 'Teacher & parent satisfaction'],
    'notes': 'We do not claim measured learning outcomes yet. These indicators start with the Ocean Artist lesson '
             'pilot and the next school sessions.',
}

# ---------------------------------------------------------------- 11 financial (slides_dsc4.s_financial) · Major
SLIDE_FINANCIAL = {
    'title': 'Financial Overview',
    'stage': [('Revenue to date', 'Rp0'), ('Stage', 'Pre-revenue')],
    'units': V3.SLIDE_FINANCIAL['units'],
    'units_note': V3.SLIDE_FINANCIAL['units_note'],
    'scenario_title': '12-month projection',
    'scenario_tag': 'PROJECTION · NOT ACTUALS',
    'scenario_head': ['', 'Conservative', 'Base'],
    # (label, conservative, base, style) style: '' row · 'sum' bold · 'sub' small · 'cash' highlight
    'scenario': [('B2C packs (≈25 / ≈50 a month)', '300', '600', 'sub'),
                 ('Paid sessions (2 / 4 a month)', '24', '48', 'sub'),
                 ('Customer revenue', 'Rp38.7M', 'Rp77.4M', 'sum'),
                 ('Direct costs', '−Rp12.0M', '−Rp24.0M', ''),
                 ('Gross contribution (69%)', 'Rp26.7M', 'Rp53.4M', 'sum'),
                 ('Operating expenses', '−Rp158M', '−Rp158M', ''),
                 ('Net result, year 1', '−Rp131.3M', '−Rp104.6M', 'sum'),
                 ('Cash at month 12 with Rp200M', 'Rp68.7M', 'Rp95.4M', 'cash')],
    'footer': 'Year 1 is a planned loss while we validate repeat demand. The loss, not the full Rp200M, is what '
              'capital covers. Full P&L in Appendix C.',
    'notes': 'Same model as before, now shown in full. Base case means about 50 packs and 4 sessions a month. Year-1 '
             'net result is minus Rp104.6M (base) or minus Rp131.3M (conservative); with Rp200M, cash stays positive '
             'at month 12. These are projections, not results. Grant money is financing, never revenue.',
}

# ---------------------------------------------------------------- 12 funding (slides_dsc4.s_funding) · Major
SLIDE_FUNDING = {
    'title': 'Funding Needs & Use of Funds',
    'label': '12-month capital plan',
    'amount': 'Rp200M',
    'purpose': 'Funds 12 months of validation, released stage by stage as each gate is passed.',
    'sources': [('DSC support', '[TBD]'), ('Other sources', '[TBD]')],
    'alloc_title': 'Use of funds',
    # (icon, use, detail, share)
    'alloc': [('users', 'Team & Operations', 'Rp96M · 2 founders × Rp4M × 12 months', '48%'),
              ('school', 'Go-to-Market', 'Rp30M · demos, school pilots, community', '15%'),
              ('scan-line', 'Product & Technology', 'Rp24M · scan reliability, infrastructure, Studio', '12%'),
              ('palette', 'Production', 'Rp20M · packs, samples, session materials', '10%'),
              ('book-open', 'Learning Content', 'Rp20M · lesson pilot, worlds by demand', '10%'),
              ('shield-check', 'Legal & Contingency', 'Rp10M · administration, accounting', '5%')],
    'recon_title': 'How Rp200M links to the P&L',
    # (label, value, style)
    'recon': [('Operating expenses in the P&L', 'Rp158M', ''),
              ('Production: funds direct costs until sales come in', 'Rp20M', ''),
              ('Headroom in GTM, product, content, legal', 'Rp22M', ''),
              ('Cash left at month 12 (base / conservative)', 'Rp95M / Rp69M', 'cash')],
    'gates_title': 'Spending follows validation gates',
    'gates': [('M1–3', 'Scan reliability + Ocean Artist 3-lesson pilot'),
              ('M3–6', 'Paid sessions, rebooking, B2C conversion'),
              ('M6–12', 'Scale GTM and content only where data supports')],
    'notes': 'Rp200M is a 12-month plan, not a loss: Rp158M is operating expense, Rp20M funds production until sales '
             'come in, Rp22M is headroom held for the gates. Customer revenue covers direct costs, so the base case ends '
             'the year with about Rp95M. We are not asking DSC to fund all of it; the split between DSC support and '
             'other sources is still to be confirmed against the competition rules, including whether founder '
             'compensation is an eligible use.',
}

# ---------------------------------------------------------------- 13 team (shared s12_team) · Minor
SLIDE_12_TEAM = {
    **V3.SLIDE_12_TEAM,
    'team': [('HH', 'Haikal Hilmi', 'CEO & Co-Founder',
              'Built the core scan-to-animation technology · ex-ByteDance backend intern · Information '
              'Engineering, UGM', 'founder_hh.png'),
             ('SK', 'Salsabila Khoirunnisa', 'CMO & Co-Founder',
              'Brand, customers & go-to-market · ran community programs with 200+ volunteers and 20+ partners · UGM',
              'founder_sk.png')],
    'closing': 'A technical CEO who built and shipped the product, and a CMO who has run community programs at '
               'scale.',
    'final': 'Live product, first pilot, two improvements shipped from it.',
    'notes': 'Haikal: built the scan-to-animation technology; backend intern at ByteDance; engineering PM of the Gadjah '
             'Mada Aerospace Team. Salsabila: Chief of Social Impact at Gifood (7+ community partners), Program '
             'Manager at Sedekah Baju Yogyakarta (200+ volunteers, 20+ partner organizations).',
}

# ---------------------------------------------------------------- 14 roadmap (slides_dsc4.s_roadmap) · Major
SLIDE_ROADMAP = {
    'title': 'Milestones & Growth Roadmap',
    'sub': 'Prove the Magic → Prove Repeat Value → Validate the Commercial Model → Scale What Works',
    # (tag, heading, items, box label, box text)
    'stages': [('NOW', 'Prove the Magic',
                ['Product live', '2 interactive worlds', '1 TPA pilot · 30 children'],
                'IMPROVE', 'Scan success · first-time experience'),
               ('MONTH 1–3', 'Prove Repeat Value',
                ['Ocean Artist 3-lesson pilot', 'Not a full LMS'],
                'MEASURE', 'Lesson completion · next-lesson start · repeat creation · willingness to pay'),
               ('MONTH 3–6', 'Validate the Commercial Model',
                ['Paid B2B sessions', 'B2C pack conversion', 'Studio MVP as pilots need it'],
                'MEASURE', 'Repeat booking · margin per session'),
               ('MONTH 6–12', 'Scale What Works',
                ['More institutions', 'Content by demand', 'Base-case sales targets'],
                'GATE', 'Only if validation supports it')],
    'kpis_title': '12-month base-case targets',
    'kpis': ['48 paid sessions', '600 B2C packs', 'Up to 1,440 children*', '≥20% rebooking', '≥95% scan success',
             'Rp77.4M revenue'],   # base case of slides 11-12
    'footnote': '*Maximum capacity: 48 sessions × 30 children, not a guaranteed number. At an average of 25 children '
                'per session: 1,200.',
    'notes': 'Each stage is gated by the one before. More worlds stay on the roadmap but come after retention is '
             'proven. Targets equal the base case on slides 11 and 12.',
}

# ---------------------------------------------------------------- 15 closing (slides_dsc4.s_closing) · Minor
SLIDE_CLOSING = {
    **V3.SLIDE_CLOSING,
    'why_title': 'Why support Scanvas now',
    'why': ['Live product, first pilot done', 'Next 12 months prove repeat value', 'Every rupiah released by a '
                                                                                   'validation gate'],
    'cta': 'Support Scanvas to turn one magic moment into repeatable creative learning for schools and families.',
    'notes': 'One thing to remember: the child’s own drawing becomes the learning experience. Why now: the product '
             'works and has been piloted; the next 12 months decide whether it brings children and schools back.',
}

# ---------------------------------------------------------------- appendix A technology (shared s7_different)
SLIDE_7_DIFFERENT = {
    **V3.SLIDE_7_DIFFERENT,
    'items': [('Computer-Vision Scan', 'Four printed markers guide perspective correction, cropping, and '
                                       'masking of the photo.'),
              ('Personalized Animation', 'The child’s extracted artwork, not a stock character, is animated in the '
                                         'world.'),
              ('Code-Linked Sheets', 'Each printed sheet links to its template and its digital world.'),
              ('Reusable Content Engine', 'New worlds are new sheet templates plus world assets on the same '
                                          'pipeline, so content scales without rebuilding the product.')],
}

# ---------------------------------------------------------------- appendix B market data (slides_dsc.s_sources)
SLIDE_SOURCES = {
    **I2.SLIDE_SOURCES,
    'title': 'Appendix B · Market Data',
    'title_w': 7.0,
    'title_size': 24,
    'footnote': 'Counts are populations of education units, not potential paying customers. Kemendikdasmen: '
                'referensi.data.kemendikdasmen.go.id, accessed Sep 2026. BPS: Jumlah Penduduk Menurut Kelompok Umur, '
                'Long Form SP2020 (2022). TPA here = Taman Penitipan Anak.',
}

# ---------------------------------------------------------------- appendix C P&L (slides_dsc4.s_pnl)
SLIDE_PNL = {
    'title': 'Appendix C · 12-Month P&L and Cash',
    'head': ['', 'Conservative', 'Base'],
    'rows': V3.SLIDE_PNL['rows'] + [('Capital plan', 'Rp200.0M', 'Rp200.0M', False),
                                    ('Cash at month 12', 'Rp68.7M', 'Rp95.4M', True)],
    'assump_title': 'Assumptions',
    'assumptions': ['Projection from the founders’ model (Sep 2026), not actual results',
                    'Pack Rp49K; direct cost Rp20K (print & packaging Rp10K, DIY delivery Rp10K)',
                    'Managed session Rp1M, up to 30 children; direct cost Rp250K',
                    'Volume: 25–50 packs and 2–4 sessions a month',
                    'Founders Rp4M a month each (lean, below market)',
                    'Studio and lesson revenue excluded (upside)',
                    'Grant money is financing, never revenue'],
    'notes': 'Cash at month 12 = Rp200M + customer revenue − direct costs − operating expenses. The Rp20M production '
             'line and Rp22M headroom in the capital plan are not extra P&L costs; see slide 12.',
}

# ---------------------------------------------------------------- appendix D competitor evidence (slides_dsc.s_competitors)
SLIDE_COMPETITORS = V3.SLIDE_COMPETITORS
