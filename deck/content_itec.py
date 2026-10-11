"""ITEC SEA 2026 · Digital Culture Track edition of the deck copy (same layout as content.py).

Built by build_deck_itec.py, which swaps this module in for deck.content; the GESAwards copy in
content.py is untouched. Keys and tuple shapes must match content.py exactly.

Framing follows the ITEC Industry/Special-track judging dimensions (itecsea.com/judging-criteria):
A market & customer evidence (2, 10) · B product, technology & defensibility (4-7) · C business model (10)
· D traction & learning (11) · E team (12) · F digital-culture fit & regional potential (3, 8, 9).
Credibility rules: every claim verifiable, no market-size numbers, no unvalidated prices.
"""

TRACK = 'ITEC SEA 2026 · Digital Culture Track'
WEBSITE = 'scanvas.id'

SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'Interactive digital culture for children: their own paper drawings become animated characters, '
            'worlds, and stories in the browser.',
    'age_chip': 'For children aged 3–10',
    'founder_name': 'Scanvas Co-Founders',
    'founder_role': 'Salsabila K. · Haikal H.',
    'notes': 'Scanvas is a phygital (physical + digital) interactive-entertainment platform: a child colors a printed '
             'sheet, scans it in the browser, and their artwork comes alive as a character in a digital world.',
}

SLIDE_2_PROBLEM = {
    'title': 'Creativity Often Stops at the Paper',
    'message': 'Printed coloring content ends when the page is finished. Most children’s digital entertainment is '
               'designed to be watched and swiped, not created.',
    'paper': {'head': 'Printed content', 'sub': 'Creative and hands-on, but it ends when the page is done.',
              'loop': ['Create', 'Finished', 'Stop']},
    'screen': {'head': 'Digital media', 'sub': 'Engaging, but children mostly watch instead of make.',
               'loop': ['Watch', 'Swipe', 'Watch']},
    'closing': 'What if a child’s own drawing became their character in a digital world?',
    'notes': 'Two gaps: printed creative content has no digital life, and digital entertainment rarely lets children '
             'create. Scanvas connects the two.',
}

SLIDE_3_INSIGHT = {
    'title': 'Children Should Create\nDigital Culture',
    'message': 'Scanvas is built around a simple idea: children should use technology to create, explore, '
               'and discover, not only consume.',
    # design philosophy, not research claims: (icon, lead, description)
    'points': [('hand', 'Create first', 'The story starts with the child’s own imagination on paper.'),
               ('user-round', 'Make it personal', 'Their artwork becomes the character, not a stock asset.'),
               ('compass', 'Interactive, not passive', 'Movement, sound, stories, and facts extend the play.'),
               ('globe', 'Keep access simple', 'Open it in a browser, with no app installation required.')],
    'loop_center': ['Create,', 'not only watch'],
    'loop': [('Create', 'palette'), ('Explore', 'compass'), ('Discover', 'lightbulb'), ('Create Again', 'repeat')],
    'notes': 'Design philosophy, not a research claim: children as creators of digital content, not only consumers.',
}

SLIDE_4_SOLUTION = {
    'title': 'From Paper to Interactive Worlds',
    'message': 'Children color a printed sheet, scan it through the website, and watch their own artwork become an '
               'animated character with sound, motion, and story content.',
    # (label, caption, image in assets/gen, fit by 'w' or 'h')
    'steps': [('Color', 'Kids color a Scanvas paper sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Snap or upload a photo in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork comes alive in seconds', 'alive_whale.png', 'w'),
              ('Explore', 'It swims inside a living world', 'ph_world.png', 'h'),
              ('Discover', 'A short story, sounds, and facts', 'tab_result.png', 'w')],
    'notes': 'One loop: Color, Scan, Come Alive, Explore, Discover. Everything runs in the browser.',
}

SLIDE_5_PRODUCT = {
    'tag': 'LIVE TODAY · scanvas.id',
    'title': 'Already Live.\nNo App Required.',
    # (icon, heading, detail) - only features that exist in the product today
    'capabilities': [('scan-line', 'Physical → Digital', 'Printed sheets + photo/upload processing'),
                     ('compass', 'Interactive worlds', 'Ocean & Vehicle worlds'),
                     ('wand-sparkles', 'Personalized animation', 'The child’s own artwork comes alive'),
                     ('music', 'Story & sound layer', 'Object sounds + short stories and facts'),
                     ('palette', 'Digital trial', 'Try the experience before buying paper')],
    'phones': [('ph_home.png', 'Landing page'), ('ph_scan.png', 'Scan / upload'), ('ph_world.png', 'Alive in the world')],
    'screens': [('tab_world_bus.png', 'Vehicle world'), ('tab_result.png', 'Story & sound')],
    'notes': 'Everything on this slide is live today at scanvas.id: real screenshots from the current product.',
}

SLIDE_6_MAGIC = {
    'title': 'Their Creation. Their Character.',
    'message': 'Unlike generic videos or static printed pages, Scanvas makes the child’s own colored artwork the '
               'character of the digital experience.',
    'before': 'Before: on paper',
    'after': 'After: alive in Scanvas',
    'trio': [('Movement', 'move'), ('Sound', 'music'), ('Story & Facts', 'book-open')],
    'notes': 'The emotional core of the product: the child is not watching a character, they are playing with their '
             'own creation.',
}

SLIDE_7_DIFFERENT = {
    'title': 'One Engine, Many Interactive Worlds',
    'items': [('Computer-Vision Scan', 'Four printed markers guide perspective correction, cropping, and '
                                       'masking of the photo.'),
              ('Personalized Animation', 'The extracted artwork, not a stock character, is animated in the world.'),
              ('Code-Linked Sheets', 'Each printed sheet carries a unique access code tied to its template.'),
              ('Reusable Content Engine', 'New worlds are new sheet templates plus world assets on the same '
                                          'pipeline: animals, vehicles, culture, and more.')],
    'notes': 'Product and technology: ArUco-marker detection, perspective warp, crop and mask, then animation in a '
             'browser world. Sheets are tied to access codes, which links the printed product to the digital one.',
}

SLIDE_8_ROADMAP = {
    'title': 'From Magic Moment\nto Content Platform',
    'message': 'Today, Scanvas turns a child’s creation into an interactive character. Next, we build story and '
               'learning layers and a growing library of worlds.',
    # (stage chip, flow, description, icon)
    'stages': [('CURRENT · LIVE', 'Color → Scan → Alive', 'Today’s interactive coloring experience.',
                'wand-sparkles'),
               ('NEXT', 'Create → Explore → Story → Quiz',
                'An interactive layer with stories, guided questions, and simple quizzes.', 'book-open'),
               ('FUTURE', 'Learn → Practice → Create → Bring It Alive',
                'Digital drawing classes and new content worlds, from nature to local culture and '
                'original Scanvas characters.', 'graduation-cap')],
    'notes': 'Only the first stage is live. Next and Future are roadmap: story/learning layers and a content library.',
}

SLIDE_9_CLASS = {
    'tag': 'FUTURE ROADMAP · CONCEPT',
    'title': 'Learn by Creating',
    'sub': 'Guided drawing classes that end inside a Scanvas world.',
    'lesson_label': 'Example lesson',
    'lesson': 'Ocean Artist: Let’s Draw a Whale',
    'steps': ['Learn the basic shape', 'Draw step-by-step', 'Practice digitally', 'Color and personalize',
              'Bring it alive', 'Discover whale sounds, habitat, and facts'],
    'loop_label': 'Core loop',
    'loop': ['Learn', 'Practice', 'Create', 'Experience', 'Discover'],
    'notes': 'A future content format: guided drawing classes that end with the child’s creation entering a world.',
}

SLIDE_10_MARKET = {
    'title': 'Who Pays: Families, Schools, and Events',
    # (segment, heading, description, (revenue label, revenue model), image, (tag, style))  style: live|building|future
    'segments': [('B2C', 'Families',
                  'Printed creative packs that unlock the Scanvas digital experience with a code per sheet.',
                  ('Revenue model', 'Per-pack purchase'), 'm_pack.png', ('AVAILABLE NOW', 'live')),
                 ('B2B', 'Schools & Events',
                  'Scanvas Studio for organized sessions, participant management, bulk processing, and shared '
                  'screens.',
                  ('Revenue model under validation', 'Per session / per participant / usage-based'),
                  'm_studio.png', ('IN DEVELOPMENT', 'building')),
                 ('B2C + B2B', 'Content Library',
                  'New worlds, character packs, creative classes, and licensed content collaborations.',
                  ('Potential model', 'Subscriptions and content add-ons'), 'm_lesson.png', ('FUTURE', 'future'))],
    'notes': 'Families buy packs today. School and event pricing is being validated with the pilot before we commit '
             'to numbers. Content library is the future platform model.',
}

SLIDE_11_VALIDATION = {
    'title': 'Early Traction →\nWhat We Learned',
    'snapshot_title': 'Early validation',
    'facts': 'Live product · 2 worlds · scan-to-animation working',
    # real pilot data, each label says exactly what it counts (TPA = Taman Pendidikan Anak-anak)
    'metrics': [('30', 'pilot participants'), ('1', 'real-world pilot (TPA)'), ('5', 'improvements from feedback')],
    'feedback_title': 'Feedback already changed the product',
    # (status: shipped | progress, what changed)
    'feedback': [('shipped', 'Larger world for more creations'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing uploads'),
                 ('progress', 'Story & learning space after play'),
                 ('progress', 'More worlds, e.g. a land version')],
    'status_label': {'shipped': 'Shipped', 'progress': 'In progress'},
    'phases': [('PHASE 1', 'Validate the Magic', 'Improve scan reliability; grow from 1 TPA pilot to more families and schools.'),
               ('PHASE 2', 'Build the Layers', 'Stories, quizzes, guided creative lessons, session tools for schools.'),
               ('PHASE 3', 'Scale Content', 'World library, Scanvas Studio, partnerships, and regional content.')],
    'notes': 'First real-world pilot: 30 participants at one TPA (Taman Pendidikan Anak-anak). The pilot surfaced five '
             'product improvements; two are shipped (larger world, digital trial) and three are in progress.',
}

SLIDE_12_TEAM = {
    'title': 'The Team Behind Scanvas',
    # (initials, name, role, focus, photo in assets/gen or None -> initials)
    'team': [('SK', 'Salsabila Khoirunnisa', 'CEO & Co-Founder',
              'Business · partnerships · customer discovery · go-to-market', 'founder_sk.png'),
             ('HH', 'Haikal Hilmi', 'CTO & Co-Founder',
              'Product · engineering · computer vision · interactive platform', 'founder_hh.png')],
    'closing': 'We want children to use technology not only to consume, but to imagine, create, and play.',
    'final': 'Scanvas — From imagination to interactive worlds.',
    'notes': 'Complementary founders: Salsabila leads business, partnerships and go-to-market; Haikal leads product, '
             'engineering and the computer-vision pipeline.',
}
