"""Antler (pre-seed VC) edition of the deck copy.

Built by build_deck_antler.py, which swaps this module in for deck.content. Reuses the shared slide functions
(same keys/tuple shapes as content.py) plus two investor slides from deck/slides_antler.py (SLIDE_MARKET, SLIDE_ASK).
GESAwards (content.py) and ITEC (content_itec.py) copy are untouched.

Order is an investor story: cover, problem, solution, live product, magic, tech edge, market, business model,
traction + 9-month plan, vision, team, ask. No placeholders and no invented numbers: market is a
qualitative wedge until sizing is sourced. Team: Haikal CEO (technical), Salsabila CMO.
"""

TRACK = 'Pre-Seed Pitch · Antler'
WEBSITE = 'scanvas.id'

SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'Children’s paper drawings become interactive characters in the browser, starting in Indonesia.',
    'age_chip': 'For children aged 3–10',
    'founder_name': 'Scanvas Co-Founders',
    'founder_role': 'Haikal H. · Salsabila K.',
    'notes': 'One line: Scanvas turns a child’s own drawing into an interactive character, in the browser, '
             'with no app install. Live today, first pilot done, raising pre-seed.',
}

SLIDE_2_PROBLEM = {
    'title': 'Creativity Often Stops at the Paper',
    'message': 'Children love drawing and coloring, but once the page is finished, the moment ends. '
               'Many screen-based activities are designed around watching and swiping rather than creating.',
    'paper': {'head': 'On paper', 'sub': 'Creative and hands-on, but it ends when the page is done.',
              'loop': ['Create', 'Finished', 'Stop']},
    'screen': {'head': 'On screens', 'sub': 'Engaging, but children mostly watch instead of make.',
               'loop': ['Watch', 'Swipe', 'Watch']},
    'closing': 'What if a child’s own drawing became the starting point of play and learning?',
    'notes': 'Paper play is creative but ends at the page; screen time is engaging but mostly passive.',
}

SLIDE_4_SOLUTION = {
    'title': 'Solution: Paper Comes Alive',
    'message': 'Children color a printed sheet, scan it through the website, and watch their own artwork become an '
               'animated character with sound, motion, and short educational content.',
    'steps': [('Color', 'Kids color a Scanvas paper sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Snap or upload a photo in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork comes alive in seconds', 'alive_whale.png', 'w'),
              ('Explore', 'It swims inside a living world', 'ph_world.png', 'h'),
              ('Learn', 'A short story, sounds, and facts', 'tab_result.png', 'w')],
    'notes': 'Color, Scan, Come Alive, Explore, Learn. Everything runs in the browser.',
}

SLIDE_5_PRODUCT = {
    'tag': 'LIVE TODAY · scanvas.id',
    'title': 'Already Live.\nNo App Required.',
    'capabilities': [('scan-line', 'Physical → Digital', 'Paper coloring + photo/upload processing'),
                     ('compass', 'Interactive worlds', 'Ocean & Vehicle worlds'),
                     ('wand-sparkles', 'Personalized animation', 'The child’s own artwork comes alive'),
                     ('music', 'Learning layer', 'Object sounds + short stories and facts'),
                     ('palette', 'Digital trial', 'Try the experience before buying paper')],
    'phones': [('ph_home.png', 'Landing page'), ('ph_scan.png', 'Scan / upload'), ('ph_world.png', 'Alive in the world')],
    'screens': [('tab_world_bus.png', 'Vehicle world'), ('tab_result.png', 'Story & sound')],
    'notes': 'Not a prototype on slides: everything shown is live at scanvas.id.',
}

SLIDE_6_MAGIC = {
    'title': 'Their Creation. Their Character.',
    'message': 'Unlike generic videos or static worksheets, Scanvas makes the child’s own colored artwork the '
               'center of the digital experience.',
    'before': 'Before: on paper',
    'after': 'After: alive in Scanvas',
    'trio': [('Movement', 'move'), ('Sound', 'music'), ('Learning Facts', 'book-open')],
    'notes': 'The hook that drives engagement: the child is playing with their own creation.',
}

SLIDE_7_DIFFERENT = {
    'title': 'Product & Technology Edge',
    'items': [('Computer-Vision Scan', 'Four printed markers guide perspective correction, cropping, and '
                                       'masking of the photo.'),
              ('Personalized Animation', 'The extracted artwork, not a stock character, is animated in the world.'),
              ('Code-Linked Sheets', 'Each printed sheet carries a unique access code tied to its template.'),
              ('Reusable Content Engine', 'New worlds are new sheet templates plus world assets on the same '
                                          'pipeline, so content scales without rebuilding the product.')],
    'notes': 'ArUco-marker detection, perspective warp, crop and mask, then browser animation. Access codes link '
             'each printed sheet to the digital experience.',
}

SLIDE_MARKET = {
    'title': 'Market: Start With\na Clear Wedge',
    'message': 'Start where we already pilot, scale through schools, then expand across Southeast Asia.',
    # (circle/chip label, heading, who, proof or next step) - qualitative until sizing is sourced
    'layers': [('WEDGE', 'Indonesia initial wedge',
                'TK/PAUD, TPA, children activity providers, and families with kids 3–10',
                'Where we already pilot: 30 children in our first TPA'),
               ('SCALE', 'Indonesia schools & events',
                'Schools and event organizers running creative sessions',
                'Distribution through Scanvas Studio'),
               ('EXPAND', 'Southeast Asia',
                'Family learning and creative-play market across the region',
                'New worlds and languages on the same engine')],
    'notes': 'No TAM number yet on purpose: we start with a wedge we can reach and prove, then size with sourced data.',
}

SLIDE_10_MARKET = {
    'title': 'Demand → Distribution → Retention',
    'segments': [('B2C · VALIDATES DEMAND', 'Families',
                  'Creative packs let us validate family demand directly.',
                  ('Revenue model', 'Per-pack purchase'), 'm_pack.png', ('AVAILABLE NOW', 'live')),
                 ('B2B · SCALABLE DISTRIBUTION', 'Schools & Events',
                  'Scanvas Studio runs sessions for many children at once: bulk processing, shared screens.',
                  ('Model under validation', 'Per session / per participant'),
                  'm_studio.png', ('IN DEVELOPMENT', 'building')),
                 ('RETENTION · LIFETIME VALUE', 'Learning Content',
                  'New worlds and learning activities bring children back again.',
                  ('Potential model', 'Subscriptions and content add-ons'), 'm_lesson.png', ('FUTURE', 'future'))],
    'notes': 'One core: children create physically, Scanvas makes it interactive. B2C validates family demand, B2B gives '
             'scalable distribution, learning content drives repeat usage. B2B is the priority channel.',
}

SLIDE_11_VALIDATION = {
    'title': 'Traction &\nNext 9 Months',
    'snapshot_title': 'Early validation',
    'facts': 'Live product · 2 worlds · scan-to-animation working',
    'metrics': [('30', 'children in first TPA pilot'), ('1', 'real-world pilot (TPA)'), ('5', 'improvements from feedback')],
    'feedback_title': 'Built → tested → learned → shipped',
    'feedback': [('shipped', 'Larger world for more creations'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing uploads'),
                 ('progress', 'Learning space after play (Next stage)'),
                 ('progress', 'More worlds, e.g. a land version')],
    'status_label': {'shipped': 'Shipped', 'progress': 'In progress'},
    # right column = milestone plan toward a seed round (fill [X] with committed targets)
    'phases': [('MONTH 1–3', 'Prove Demand', 'Turn the TPA pilot into paid sessions with more schools and TPA/PAUD.'),
               ('MONTH 4–6', 'Prove Distribution', 'Studio and bulk uploads for repeatable school and event sessions.'),
               ('MONTH 7–9', 'Seed-Ready', 'Learning layer live; repeat-usage and revenue data for a seed round.')],
    'notes': 'Honest early traction: 30 pilot participants at one TPA, five product improvements, two shipped. '
             'The plan converts that into paid pilots and repeat usage within nine months.',
}

SLIDE_8_ROADMAP = {
    'title': 'Vision: From Magic Moment\nto Learning Platform',
    'message': 'Today, Scanvas uses the child’s creation to trigger curiosity and discovery. '
               'Next, we build structured learning and a growing library of worlds.',
    'stages': [('CURRENT · LIVE', 'Color → Scan → Alive', 'Today’s magical coloring experience.',
                'wand-sparkles'),
               ('NEXT', 'Create → Explore → Story → Quiz',
                'An interactive learning layer with stories, guided questions, and simple quizzes.', 'book-open'),
               ('FUTURE', 'Learn → Practice → Create → Bring It Alive',
                'Digital drawing classes and a content library of worlds, from Indonesia to the region.',
                'graduation-cap')],
    'notes': 'Only the first stage is live. Engagement engine today; learning platform and content library next.',
}

SLIDE_12_TEAM = {
    'title': 'The Team Behind Scanvas',
    'team': [('HH', 'Haikal Hilmi', 'CEO & Co-Founder',
              'Technical founder · product & company strategy · partnerships · built the core technology', 'founder_hh.png'),
             ('SK', 'Salsabila Khoirunnisa', 'CMO & Co-Founder',
              'Brand · marketing · customer discovery · community · go-to-market', 'founder_sk.png')],
    'closing': 'A technical CEO who built the core product, and a CMO who brings it to families and schools.',
    'final': 'We shipped the live product and ran our first pilot.',
    'notes': 'Haikal built the scan-to-animation technology himself and leads company and product direction; '
             'Salsabila leads marketing, customer discovery, and go-to-market.',
}

SLIDE_ASK = {
    'title': 'The Ask',
    'raise_label': 'Seeking',
    'amount': 'Antler pre-seed investment',
    'round': 'To make a live, piloted product repeatable',
    'funds_title': 'Where it goes',
    # (icon, use)
    'funds': [('scan-line', 'Product & scan reliability'),
              ('school', 'Go-to-market: schools, TPA, events'),
              ('book-open', 'Learning layer & new worlds'),
              ('users', 'Team to ship faster')],
    'milestones_title': 'What this unlocks in 9 months',
    'milestones': ['Paid sessions with more schools and TPA/PAUD',
                   'Families buying packs repeatedly',
                   'Scanvas Studio for sessions live',
                   'Learning layer (Next stage) launched',
                   'Seed round with repeat-usage data'],
    'why': 'Why Antler: prove traction fast in the Jakarta residency, then scale from Indonesia to the region.',
    'notes': 'Antler sets the pre-seed terms; the ask is focus and speed. Milestones mirror the 9-month plan.',
}
