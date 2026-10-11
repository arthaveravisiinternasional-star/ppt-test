"""ITEC SEA 2026 · final edition (v3), Digital Culture Track. 10 main slides + 3 appendix.

Built by build_deck_itec3.py (swaps this module in for deck.content). Visual base = v2 (content_itec2.py); copy follows
the founders' V3 spec (Sep 2026): magic -> repeat value -> business -> beachhead -> digital culture -> roadmap + ITEC ask.

Honesty rules: live product, 2 worlds, one completed 30-child pilot, pre-revenue. No LMS / course-platform claim, no
China partner, no paid customers, no recurring revenue, no validated pricing, no proprietary AI.
Team as submitted to ITEC: Salsabila CEO, Haikal CTO.
"""
from . import content_itec2 as V2

TRACK = 'ITEC SEA 2026 · Digital Culture Track'
WEBSITE = 'scanvas.id'
PILOT_ART = ['pilot_art_1.png', 'pilot_art_2.png', 'pilot_art_3.png', 'pilot_art_4.png']   # tools/make_pilot_art.py

# ---------------------------------------------------------------- 1 cover (shared s1_cover + proof strip)
SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'Children turn their own paper drawings into characters, interactive worlds, and stories — directly in '
            'the browser.',
    'age_chip': 'For children aged 3–10',
    'proof': 'LIVE PRODUCT · 2 WORLDS · 30-CHILD PILOT · NO APP REQUIRED',
    'founder_name': 'Salsabila Khoirunnisa · CEO & Co-Founder',
    'founder_role': 'Haikal Hilmi · CTO & Co-Founder',
    'name_box_w': 3.1,
    'notes': 'Scanvas: a child’s own paper drawing becomes an interactive character in a digital world, in the '
             'browser. Live today, 2 worlds, one completed 30-child pilot, no app required.',
}

# ---------------------------------------------------------------- 2 problem (slides_itec3.s_problem)
SLIDE_PROBLEM = {
    'title': 'Creativity Starts With the Child —\nBut Often Stops at the Page',
    'cards': [('Physical creativity', 'Children draw, color, and imagine. But when the page is finished, the '
                                      'experience usually ends.', ['CREATE', 'FINISHED', 'STOP'], 'm_kidcolor.png'),
              ('Digital entertainment', 'Engaging, but children often watch, swipe, and consume someone else’s '
                                        'content.', ['WATCH', 'SWIPE', 'WATCH'], None)],
    'evidence_label': 'WHAT WE HAVE TESTED',
    'evidence': '30 children · 1 real-world TPA pilot · D.I. Yogyakarta',
    'evidence_art': 'Sheets colored by children in the pilot',
    'closing': 'What if the child’s own creation became the starting point of the digital experience?',
    'notes': 'Physical creativity has no digital life; digital entertainment rarely lets children create. We tested '
             'this with 30 children in one TPA in D.I. Yogyakarta; the sheets shown are their real artwork.',
}

# ---------------------------------------------------------------- 3 how it works (shared s4_solution + QR + line)
SLIDE_4_SOLUTION = {
    'title': 'A Child’s Own Drawing Becomes\nan Interactive Character in Seconds',
    'title_size': 26,
    'title_w': 7.4,
    'message': '',
    'steps': [('Color', 'Child colors a Scanvas sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Photograph or upload it in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork is extracted and animated', 'alive_whale.png', 'w'),
              ('Explore', 'Their character enters an interactive world', 'ph_world.png', 'h'),
              ('Discover', 'Stories, sounds, and facts extend it', 'tab_result.png', 'w')],
    'usp': 'Not a stock character. The child’s own creation becomes part of the world.',
    'qr': 'qr_scanvas_trial.png',
    'qr_url': 'https://www.scanvas.id/trial',
    'qr_label': 'TRY IT LIVE',
    'notes': 'Color, Scan, Come Alive, Explore, Discover. The QR opens the public digital trial at scanvas.id/trial.',
}

# ---------------------------------------------------------------- 4 traction (slides_dsc.s_traction)
SLIDE_TRACTION = {
    'title': 'Our First 30-Child Pilot\nAlready Changed the Product',
    'title_w': 4.6,
    'title_size': 22,
    'stage': '',
    'metrics': [('2', 'interactive worlds live'), ('30', 'children in first real-world pilot'),
                ('1', 'TPA pilot completed'), ('5', 'product improvements from feedback')],
    'loop': ['BUILT', 'TESTED', 'LEARNED', 'SHIPPED'],
    'feedback_title': 'FEEDBACK → PRODUCT',
    'feedback': [('shipped', 'Larger interactive world'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing processing'),
                 ('progress', 'Story & learning space'),
                 ('progress', 'Additional worlds')],
    'status_label': {'shipped': 'SHIPPED', 'progress': 'BUILDING'},
    'proof': '',
    'photos': ['pilot_photo_4.jpg', 'pilot_photo_1.jpg', 'pilot_photo_2.jpg', 'pilot_photo_3.jpg'],   # assets/pilot-project
    'photo_caption': 'First real-world pilot · TPA, D.I. Yogyakarta',
    'notes': 'Pilot participants were not paying customers. Its value: five product improvements, two already '
             'shipped. Pre-revenue.',
}

# ---------------------------------------------------------------- 5 technology (slides_itec3.s_tech)
SLIDE_7_DIFFERENT = {
    'title': 'One Core Engine. Many Interactive Worlds.',
    'sub': 'New content reuses the same scanning, personalization, and interactive-world pipeline.',
    'items': [('Computer-Vision Scan', 'Printed markers guide perspective correction, cropping, and object '
                                       'extraction.'),
              ('Personalized Output', 'The child’s extracted artwork, not a stock character, enters the world.'),
              ('Code-Linked Physical Content', 'Each printed sheet links to its template and digital experience.'),
              ('Reusable World Engine', 'Animals · vehicles · nature · culture · characters · stories.')],
    'diffs': [('globe', 'WEB ACCESS'), ('wand-sparkles', 'PERSONALIZED CONTENT'), ('compass', 'SHARED WORLDS'),
              ('layers', 'REUSABLE ENGINE')],
    'notes': 'The pipeline is the asset: physical input, computer-vision processing, personalized asset, interactive '
             'runtime, content system. New worlds reuse it.',
}

# ---------------------------------------------------------------- 6 repeat value (slides_itec3.s_repeat) NEW
SLIDE_REPEAT = {
    'title': 'From a Magic Moment to Repeatable Value',
    'lead': 'The magic gets attention. The next question is whether children want to create again — and whether '
            'parents will pay for that repeat value.',
    # (tag, style, heading, flow, body lines, box label, box text)
    'cols': [('TODAY', 'live', 'Magic', 'CREATE → SCAN → ALIVE',
              ['A child’s own artwork becomes a character in a live interactive world.'],
              'EVIDENCE', '2 worlds · 30-child pilot'),
             ('NEXT', 'validating', 'Repeat', 'LEARN → CREATE → ALIVE → PROGRESS → NEXT',
              [[('Ocean Artist — 3-lesson pilot', {'font': 'Fredoka SemiBold'})],
               'Each lesson teaches one creative skill, then the child’s artwork comes alive. A focused pilot, not '
               'a generic LMS.'],
              'MEASURE', 'Next-lesson start · repeat creation · parent willingness to pay'),
             ('LATER', 'future', 'Engage', 'PLAY → STORY → DISCOVER',
              ['Missions', 'Shared worlds', 'Interactive stories', 'Discovery'],
              'GATE', 'Built only after repeat usage is proven')],
    'footer': 'The core Scanvas experience remains unchanged: the child creates first, and their own artwork comes '
              'alive.',
    'notes': 'Today we prove the magic. Next we test repeat value with a 3-lesson Ocean Artist pilot and measure '
             'next-lesson start, repeat creation, and willingness to pay. Later layers wait for that evidence.',
}

# ---------------------------------------------------------------- 7 business model (slides_itec3.s_business)
SLIDE_BUSINESS = {
    'title': 'A Business Model We Can Test and Scale',
    'lead': 'Pre-revenue today. Each path has a validation gate before we scale it.',
    # (tag, style, heading, offer, revenue, list label, list)
    'paths': [('AVAILABLE NOW', 'live', 'B2C · Families',
               'Creative packs + the Scanvas digital experience. Repeat-value experiment: levels · worlds · programs.',
               'Per-pack purchase', 'Validate by',
               ['Pack purchase', 'Course activation', 'Completion', 'Repeat purchase']),
              ('UNDER VALIDATION', 'validating', 'B2B · Schools & Events',
               'Pilot sessions today → Scanvas Studio for repeatable institutional use.',
               'Per session · per participant · usage-based', 'Validate by',
               ['Demo → pilot', 'Pilot → second session', 'Participants per session', 'Operating cost per session']),
              ('FUTURE', 'future', 'Content & IP',
               'New content built on the same engine.',
               'Content add-ons · subscriptions · partnerships / licensing', 'Offer',
               ['New worlds', 'Original characters', 'Cultural themes', 'Creative programs', 'Partner content',
                'Licensed collaborations'])],
    # Pricing box stays off until the founders confirm it for ITEC. To show it, set e.g.:
    # 'pricing': ('Current test assumptions — not yet validated at commercial volume',
    #             'Family pack Rp49K · Managed session from Rp1M'),
    'pricing': None,
    'notes': 'Revenue models only; no nominal prices because pricing is not validated. B2C is available now, B2B is '
             'under validation, Content & IP is future.',
}

# ---------------------------------------------------------------- 8 market + beachhead (slides_itec3.s_market)
SLIDE_MARKET = {
    'title': 'Start With a Reachable Beachhead, Then Scale Distribution',
    'icp_label': 'INITIAL CUSTOMER',
    'icp': [('Buyer', 'PAUD / TK / TPA owner or principal · school / activity organizer · parent'),
            ('User', 'Children 3–10'),
            ('Use case', 'Creative classroom / activity session'),
            ('Target acquisition loop', 'DEMO → PILOT → PAID SESSION → REPEAT')],
    'stages': [('WEDGE', 'D.I. Yogyakarta', '7,123', 'PAUD + primary schools',
                'First institutional beachhead, where our first pilot ran.'),
               ('SCALE', 'Central Java + DIY', '62,797', 'PAUD + primary schools',
                'School sessions, events, and Scanvas Studio.'),
               ('NATIONAL', 'Indonesia', '420,886', 'PAUD + primary schools',
                '≈35.3M children aged 3–10.*'),
               ('EXPAND', 'Southeast Asia', 'SEA', 'same engine, local content',
                'New languages, worlds, cultural content, partners.')],
    'footer': 'Institution counts represent the first distribution beachhead — not the entire Scanvas market. '
              'Families, events, and content expand beyond it.',
    'source': 'Sources: Kemendikdasmen Data Referensi Pendidikan (PAUD, SD), accessed Sep 2026 · *estimated from BPS '
              'population by 5-year age group, 2022. Details in Appendix B.',
    'notes': 'Initial buyer is the PAUD/TK/TPA owner or organizer; the loop is demo, pilot, paid session, repeat. '
             'School counts are the beachhead, not the whole market.',
}

# ---------------------------------------------------------------- 9 digital culture + regional (slides_itec3.s_culture)
SLIDE_CULTURE = {
    'title': 'From Child Creativity to Digital Culture',
    'layers': V2.SLIDE_CULTURE['layers'][:2] + [('CONTENT & IP', 'Scalable worlds & IP',
                                                 *V2.SLIDE_CULTURE['layers'][2][2:])],
    'region_title': 'SAME CORE ENGINE, LOCALISED CONTENT',
    'region_tag': 'What we want to validate through ITEC',
    'regions': [('INDONESIA', 'Current worlds + local themes'),
                ('ASEAN', 'Local languages · cultural themes · distribution / content partners'),
                ('CHAOYANG / CHINA', 'Mandarin localisation · partner-led pilot · children’s content / IP '
                                     'collaboration')],
    'closing': 'Children do not only consume digital culture — they participate in creating it.',
    'notes': 'Regional row = hypotheses to validate through ITEC. We have no China partner today; we want to explore '
             'a partner-led pilot.',
}

# ---------------------------------------------------------------- 10 roadmap + ITEC ask (slides_itec3.s_next)
SLIDE_NEXT = {
    'title': 'Prove the Magic → Prove Repeat Value →\nExpand the Experience → Scale Content',
    # (tag, heading, description, items, item icon, box label, box text)
    'stages': [('NOW', 'Prove the Magic', 'Reliable CREATE → SCAN → ALIVE',
                ['Product live', '2 worlds', 'First 30-child pilot'], 'check',
                'MEASURE', 'Scan success · time-to-magic · recovery'),
               ('NEXT', 'Prove Repeat Value', 'Collection + 3-lesson creative pilot', [], None,
                'MEASURE', 'Second creation · next-lesson start · 3-lesson completion · willingness to pay · repeat '
                           'purchase / Level 2 intent'),
               ('THEN', 'Expand the Experience', 'Artwork children play with, return to, and explore',
                ['Missions', 'Shared World', 'Interactive Story', 'Discovery'], 'arrow-right', None, None),
               ('SCALE', 'Content & IP Platform', '',
                ['Additional worlds', 'Original characters', 'Cultural themes', 'Classroom format',
                 'Partner / licensed content', 'ASEAN localisation'], 'arrow-right', None, None)],
    'engine': 'ONE CONTENT ENGINE → MULTIPLE DISTRIBUTION & REVENUE PATHS',
    'ask_title': 'THROUGH ITEC, WE WANT TO FIND',
    'ask': [('layers', 'Content & IP partners'), ('school', 'Institutional distribution partners'),
            ('globe', 'ASEAN / China pilot opportunities'), ('rocket', 'Commercialisation and market-entry guidance')],
    'notes': 'Each stage is gated by the previous one. Through ITEC we want partners, distribution, pilot '
             'opportunities, and commercialisation guidance, not a claimed partnership.',
}

# ---------------------------------------------------------------- appendix A competition (slides_itec3.s_competition)
SLIDE_COMPETITION = {
    **V2.SLIDE_COMPETITION,
    'title': 'Competitors Prove the Category; Scanvas Combines\nWeb Access, Personalisation, and Shared Worlds',
    'title_size': 20,
    'rows': [r for r in V2.SLIDE_COMPETITION['rows'] if r[0] != 'Indonesia-first'],
    'legend': '',
    'statement': 'Scanvas does not need to replace these products. The opportunity is to combine a low-friction web '
                 'experience, child-generated characters, shared worlds, and a reusable content engine.',
    'source': 'Appendix A · rows include axes where competitors lead. Evidence checked Sep 2026 on each product’s '
              'official site.',
}

# ---------------------------------------------------------------- appendix B market evidence (slides_dsc.s_sources)
SLIDE_SOURCES = {
    **V2.SLIDE_SOURCES,
    'title': 'Market Figures Use Indonesian Education Data\nand a BPS-Based Child Population Estimate',
}

# ---------------------------------------------------------------- appendix C tech + privacy + validation
SLIDE_PIPELINE = {
    'title': 'One Pipeline, Responsible Child Data,\nand a Validation Gate Before Every Build',
    'steps': V2.SLIDE_PIPELINE['steps'],
    'privacy_title': 'RESPONSIBLE CHILD DATA',
    'privacy': 'Collect only what is necessary. No child name, parent identity, email, phone, precise location, or '
               'artwork itself as analytics payload by default.',
    'validation_title': 'VALIDATION PRINCIPLE',
    'validation_flow': ['Build', 'Measure', 'Gate', 'Expand'],
    'validation': 'Do not build the full course before a 3-lesson pilot validates progression and willingness to pay. '
                  'Do not build large Mission/Story/AI layers before repeat usage is proven.',
    'notes': 'Backend detects ArUco markers, corrects perspective, and extracts the object; the frontend shows it '
             'with motion, sound, and facts. Child data is minimised by default.',
}
