"""ITEC SEA 2026 · Top 30 edition (v2), Digital Culture Track.

Built by build_deck_itec2.py (swaps this module in for deck.content). Backbone = ITEC v1 (content_itec.py) story and
Digital Culture positioning; commercial evidence from DSC (market numbers, competitors, GTM, traction), growth story
from Antler (wedge -> scale -> expand), future loop from GESA. 10 main slides + 3 appendix.

Honesty rules: no prices (B2C/B2B pricing still under validation), no funding ask, pre-revenue stated.
Team as submitted to ITEC: Salsabila CEO, Haikal CTO.
"""

TRACK = 'ITEC SEA 2026 · Digital Culture Track'
WEBSITE = 'scanvas.id'

# ---------------------------------------------------------------- 1 cover (shared s1_cover)
SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'Children turn their own paper drawings into characters, interactive worlds, and stories, directly in '
            'the browser.',
    'age_chip': 'For children aged 3–10',
    'founder_name': 'Salsabila Khoirunnisa · CEO & Co-Founder',
    'founder_role': 'Haikal Hilmi · CTO & Co-Founder',
    'name_box_w': 3.1,
    'notes': 'Scanvas is a physical-to-digital creation engine: a child’s own drawing becomes an interactive '
             'character in a digital world, in the browser.',
}

# ---------------------------------------------------------------- 2 problem (slides_itec2.s_problem)
SLIDE_PROBLEM = {
    'title': 'A child’s creativity ends with the finished page,\nand screens mostly ask children to watch',
    'cards': [('Physical creativity', 'Children draw, color, and imagine. But when the page is finished, the '
                                      'experience usually ends.', ['Create', 'Finished', 'Stop'], 'm_kidcolor.png'),
              ('Digital entertainment', 'Engaging, but children often watch, swipe, and consume someone else’s '
                                        'content.', ['Watch', 'Swipe', 'Watch'], None)],
    'scanvas_loop': ['Create', 'Explore', 'Discover', 'Create Again'],
    'closing': 'What if a child’s own creation became the starting point of a digital world?',
    'notes': 'Two gaps: physical creativity has no digital life, and digital entertainment rarely lets children '
             'create. Scanvas connects the two.',
}

# ---------------------------------------------------------------- 3 how it works (slides_dsc.s_solution)
SLIDE_4_SOLUTION = {
    'title': 'A child’s own drawing becomes\nan animated character in seconds',
    'title_size': 26,
    'message': '',
    'steps': [('Color', 'Child colors a Scanvas sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Photograph or upload it in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork is extracted and animated', 'alive_whale.png', 'w'),
              ('Explore', 'Their character enters an interactive world', 'ph_world.png', 'h'),
              ('Discover', 'Stories, sounds, and facts extend it', 'tab_result.png', 'w')],
    'usp': 'Not a stock character. The child’s own creation.',
    'trio': [('Movement', 'move'), ('Sound', 'music'), ('Story & Facts', 'book-open')],
    'notes': 'Color, Scan, Come Alive, Explore, Discover. Photo or upload, marker detection, processing, then an '
             'interactive world with motion, audio, and short facts.',
}

# ---------------------------------------------------------------- 4 product proof (shared s5_product + QR)
SLIDE_5_PRODUCT = {
    'tag': 'LIVE TODAY · scanvas.id',
    'title': 'Scanvas runs live\nin any browser',
    'title_size': 22,
    'capabilities': [('scan-line', 'Physical → Digital', 'Print → photo/upload → interactive'),
                     ('compass', '2 interactive worlds', 'Ocean + Vehicle'),
                     ('wand-sparkles', 'Personalized animation', 'The child’s own artwork is the character'),
                     ('music', 'Story & sound', 'Objects unlock sound, story, and facts'),
                     ('palette', 'Digital trial', 'Try the experience before buying a pack'),
                     ('globe', 'Browser-based', 'No mandatory app installation')],
    'phones': [('ph_home.png', 'Landing page'), ('ph_scan.png', 'Scan / upload'), ('ph_world.png', 'Alive in the world')],
    'screens': [('tab_world_bus.png', 'Vehicle world'), ('tab_result.png', 'Story & sound')],
    'qr_label': 'Scan to try live',
    'notes': 'Everything on this slide is live today at scanvas.id: real screenshots from the current product.',
}

# ---------------------------------------------------------------- 5 technology (shared s7_different + statement)
SLIDE_7_DIFFERENT = {
    'title': 'One scanning engine powers every world,\nso new content needs no rebuild',
    'title_w': 8.5,
    'items': [('Computer-Vision Scan', 'Four printed markers guide perspective correction, cropping, and object '
                                       'extraction.'),
              ('Personalized Animation', 'The extracted artwork, not a stock character, enters the world.'),
              ('Code-Linked Sheets', 'Each physical sheet links to its template and digital experience.'),
              ('Reusable Content Engine', 'The same engine supports new animals, vehicles, nature, culture, '
                                          'characters, and stories.')],
    'statement': 'New content does not require rebuilding the platform.',
    'notes': 'The moat is not the website; it is the pipeline: physical input, computer-vision processing, '
             'personalized asset, interactive runtime, content system.',
}

# ---------------------------------------------------------------- 6 why digital culture (slides_itec2.s_culture)
SLIDE_CULTURE = {
    'title': 'Children stop only consuming digital culture\nand start creating it',
    # (step, heading, description, chips, icon)
    'layers': [('CREATE', 'Child-generated creativity', 'Children begin with their own imagination and physical '
                'artwork.', ['Drawing', 'Coloring', 'Imagination'], 'palette'),
               ('EXPERIENCE', 'Interactive digital worlds', 'Their creation becomes part of a living world.',
                ['Animation', 'Sound', 'Stories', 'Interaction', 'Discovery'], 'compass'),
               ('CONTENT & IP', 'Scalable worlds and characters', 'The same platform expands into new content.',
                ['Nature', 'Vehicles', 'Local culture', 'Characters', 'Partners'], 'layers')],
    'statement': 'Children do not only consume digital culture: they participate in creating it.',
    'notes': 'Digital Culture fit: child-generated content becomes interactive media, and the engine scales into '
             'worlds, characters, and IP.',
}

# ---------------------------------------------------------------- 7 market (slides_itec2.s_market)
SLIDE_MARKET = {
    'title': 'Scanvas starts with 7,123 schools in Yogyakarta\nand scales the same engine to Indonesia and SEA',
    # (stage, geography, value, unit, description)
    'stages': [('WEDGE', 'D.I. Yogyakarta', '7,123', 'PAUD + primary schools',
                'First institutional beachhead, where our first pilot ran.'),
               ('SCALE', 'Central Java + DIY', '62,797', 'PAUD + primary schools',
                'School sessions, events, and Scanvas Studio.'),
               ('NATIONAL', 'Indonesia', '420,886', 'PAUD + primary schools',
                '≈35M children aged 3–10.*'),
               ('EXPAND', 'Southeast Asia', 'SEA', 'replicate the engine',
                'New languages, new worlds, local cultural content, partners.')],
    'source': 'School counts are the institutional beachhead only; families, events, and content add to it. '
              'Sources: Kemendikdasmen Data Referensi Pendidikan (PAUD, SD), accessed Sep 2026 · *estimated from BPS '
              'population by 5-year age group, 2022. Details in Appendix B.',
    'notes': 'Numbers count PAUD and primary-school units, our institutional buyers; they are not the whole market.',
}

# ---------------------------------------------------------------- 8 business model + GTM (slides_itec2.s_business)
SLIDE_BUSINESS = {
    'title': 'Families buy today, schools and events come next,\nand content and IP grow the same platform',
    # (tag, style, heading, description, model, flow)
    'paths': [('AVAILABLE NOW', 'live', 'B2C · Families',
               'Physical creative packs that unlock the Scanvas digital experience.', 'Per-pack purchase',
               ['Short video', 'Digital trial', 'Creative pack', 'New world']),
              ('VALIDATING', 'validating', 'B2B · Schools & Events',
               'Managed sessions today, then Scanvas Studio for repeatable institutional use.',
               'Per session · per participant · usage-based (under validation)',
               ['Outreach', 'Demo', 'Pilot', 'Paid session', 'Repeat use']),
              ('FUTURE', 'future', 'Content & IP',
               'Interactive worlds, character packs, creative lessons, stories, cultural content, licensed '
               'collaborations.', 'Subscriptions · content add-ons · partnerships',
               ['New worlds', 'Characters', 'Partners'])],
    'notes': 'Revenue models only: pack and session prices are still being validated, so no nominal prices here.',
}

# ---------------------------------------------------------------- 9 traction (slides_dsc.s_traction)
SLIDE_TRACTION = {
    'title': 'Our first 30-child pilot led to five product changes,\ntwo of them already shipped',
    'title_w': 8.8,
    'title_size': 20,
    'stage': '',
    'metrics': [('2', 'interactive worlds live'), ('30', 'children in first real-world pilot'),
                ('1', 'TPA pilot completed'), ('5', 'product improvements from feedback')],
    'loop': ['Built', 'Tested', 'Learned', 'Shipped'],
    'feedback_title': 'Feedback already changed the product',
    'feedback': [('shipped', 'Larger interactive world'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing processing'),
                 ('progress', 'Story & learning space'),
                 ('progress', 'Additional worlds')],
    'status_label': {'shipped': 'Shipped', 'progress': 'Building'},
    'proof': 'Live at scanvas.id · public digital trial · pre-revenue',
    'notes': 'Pilot participants were not paying customers. The value of the pilot: five product improvements, '
             'two already shipped.',
}

# ---------------------------------------------------------------- 10 roadmap + team (slides_itec2.s_next)
SLIDE_NEXT = {
    'title': 'Next, Scanvas makes the magic repeatable and scales content',
    'phases': [('PHASE 1', 'Validate the Magic', ['Improve scan reliability', 'More family testing',
                                                  'More school / TPA pilots', 'Validate willingness to pay']),
               ('PHASE 2', 'Make It Repeatable', ['Bulk processing', 'Scanvas Studio', 'School / event sessions',
                                                  'Stories, quizzes, guided activities']),
               ('PHASE 3', 'Scale the Content', ['Additional worlds', 'Original Scanvas characters',
                                                 'Cultural themes & partners', 'Regional content'])],
    'team': [('Salsabila Khoirunnisa', 'CEO & Co-Founder', 'Business · partnerships · customer discovery · GTM',
              'founder_sk.png'),
             ('Haikal Hilmi', 'CTO & Co-Founder', 'Product · engineering · computer vision · interactive platform',
              'founder_hh.png')],
    'closing': 'Scanvas turns children from digital-content consumers into creators inside interactive worlds.',
    'itec': 'With ITEC SEA: partners · commercialization · regional expansion',
    'notes': 'Next 12 months: validate, make repeatable, scale content. Complementary founders: business and '
             'technology.',
}

# ---------------------------------------------------------------- appendix A competition (slides_dsc.s_competition)
SLIDE_COMPETITION = {
    'title': 'Competitors prove the category; Scanvas differs\nby browser access and shared worlds',
    'title_w': 8.8,
    'title_size': 22,
    'highlight_own': False,
    'legend': 'Appendix A · rows include axes where competitors lead. Evidence checked Sep 2026 on each '
              'product’s official site.',
    'players': ['Scanvas', 'Faber-Castell\nARt Alive', 'Quiver', 'WAGZAK\nJUMP', 'teamLab Sketch\nAquarium'],
    'rows': [('Paper coloring → digital', ['yes', 'yes', 'yes', 'yes', 'yes']),
             ('Child’s artwork becomes character', ['yes', 'yes', 'yes', 'yes', 'yes']),
             ('No app required (web)', ['yes', 'no', 'no', 'no', 'Venue only']),
             ('Shared interactive worlds', ['yes', 'no', 'no', 'no', 'yes']),
             ('Educational / story content', ['yes', 'Some', 'yes', 'yes', 'Some']),
             ('Institutional sessions', ['Pilot', 'no', 'Edu subscription', 'School license', 'Installation']),
             ('Indonesia-first', ['yes', 'yes', 'no', 'no', 'no']),
             ('Large ready-made content library', ['2 worlds', 'no', 'yes', '100+ lessons', 'no']),
             ('Brand & distribution reach', ['Early', 'Retail brand', '26M+ downloads', '30 languages', 'Museums'])],
    'notes': 'We do not claim no competitors: they prove the category exists. Evidence checked Sep 2026 on each '
             'product’s official site.',
}

# ---------------------------------------------------------------- appendix B market evidence (slides_dsc.s_sources)
SLIDE_SOURCES = {
    'title': 'Market figures come from Kemendikdasmen school counts\nand a BPS-based estimate of children aged 3–10',
    'title_w': 8.8,
    'title_size': 20,
    'head': ['Figure', 'Value', 'How it is calculated / source'],
    'rows': [('PAUD units, Indonesia', '243,604', 'TK 134,789 + KB 86,429 + TPA 2,684 + SPS 19,702 · Kemendikdasmen'),
             ('Primary schools (SD sederajat), Indonesia', '177,282', 'Kemendikdasmen Data Referensi Pendidikan'),
             ('PAUD + primary schools, Indonesia', '420,886', '243,604 + 177,282'),
             ('Central Java + D.I. Yogyakarta', '62,797', 'PAUD 32,839 + 5,071 · SD 22,835 + 2,052'),
             ('D.I. Yogyakarta', '7,123', 'PAUD 5,071 + SD 2,052'),
             ('Children aged 3–10, Indonesia', '≈35.3M', '2/5 × 22,094,426 (0–4) + 22,013,768 (5–9) + '
                                                         '1/5 × 22,088,673 (10–14) · BPS 2022')],
    'footnote': 'Kemendikdasmen: referensi.data.kemendikdasmen.go.id (PAUD & Dikdas per province), accessed Sep 2026. '
                'BPS: Jumlah Penduduk Menurut Kelompok Umur, Long Form SP2020 (2022). TPA in Kemendikdasmen data = '
                'Taman Penitipan Anak.',
    'notes': 'Single-year ages are not published in this table, so ages 3-10 are a proportional estimate.',
}

# ---------------------------------------------------------------- appendix C pipeline (slides_itec2.s_pipeline)
SLIDE_PIPELINE = {
    'title': 'Every drawing moves from paper through computer vision\ninto a reusable interactive world',
    # (heading, lines, icon)
    'steps': [('Physical creation', ['Child colors a Scanvas sheet'], 'palette'),
              ('Capture', ['Camera or photo upload'], 'camera'),
              ('Computer vision', ['Marker detection', 'Perspective correction', 'Crop', 'Object extraction'],
               'scan-line'),
              ('Digital asset', ['Child’s artwork becomes the character'], 'wand-sparkles'),
              ('Interactive runtime', ['Animation', 'Movement', 'Sounds', 'Interactive world'], 'play'),
              ('Content layer', ['Story', 'Facts', 'Discovery'], 'book-open'),
              ('Reusable world engine', ['Ocean', 'Vehicles', 'Future: culture, nature, characters'], 'layers')],
    'statement': 'Physical input → CV processing → personalized asset → interactive runtime → content system',
    'notes': 'Backend detects ArUco markers, corrects perspective, and extracts the object; the frontend shows it '
             'with motion, sound, and facts.',
}
