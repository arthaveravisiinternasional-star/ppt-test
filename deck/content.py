"""All deck copy lives here. Edit text in this file only; layout lives in slides.py.

Each SLIDE_N dict maps to one slide function in slides.py. Keep items short:
titles are sized for 1-2 lines, body copy for 1-2 lines. Credibility rules: no research claims
without a source, no unvalidated prices, every metric states what it counts.
"""

TRACK = 'GESAwards 2026 · Female Founders Track'
WEBSITE = 'scanvas.id'

SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'A creative learning platform that transforms children’s drawings into interactive digital experiences.',
    'age_chip': 'For children aged 3–10',
    'founder_name': 'Salsabila Khoirunnisa',
    'founder_role': 'CEO & Co-Founder',
    'notes': 'Scanvas turns a child’s own coloring sheet into an interactive experience: color on paper, '
             'scan in the browser, and the artwork comes alive.',
}

SLIDE_2_PROBLEM = {
    'title': 'Creativity Often Stops at the Paper',
    'message': 'Children love drawing and coloring, but once the paper is finished, the learning moment often ends. '
               'Many screen-based activities are designed around watching and swiping rather than creating.',
    'paper': {'head': 'On paper', 'sub': 'Creative and hands-on, but it ends when the page is done.',
              'loop': ['Create', 'Finished', 'Stop']},
    'screen': {'head': 'On screens', 'sub': 'Engaging, but children mostly watch instead of make.',
               'loop': ['Watch', 'Swipe', 'Watch']},
    'closing': 'What if children’s own creations became the starting point of learning?',
    'notes': 'Paper creativity is hands-on but ends at the page. Screens are engaging but mostly passive. '
             'Scanvas connects the two.',
}

SLIDE_3_INSIGHT = {
    'title': 'Learning Should Start\nWith Creating',
    'message': 'Scanvas is built around a simple idea: children should use digital technology to create, explore, '
               'and discover, not only consume.',
    # design philosophy, not research claims: (icon, lead, description)
    'points': [('hand', 'Create first', 'Start with the child’s own imagination.'),
               ('user-round', 'Make it personal', 'Their own artwork becomes the experience.'),
               ('compass', 'Explore through interaction', 'Movement, sound, stories, and facts extend the activity.'),
               ('globe', 'Keep access simple', 'Open it in a browser, with no app installation required.')],
    'loop_center': ['Learn by', 'making'],
    'loop': [('Create', 'palette'), ('Explore', 'compass'), ('Discover', 'lightbulb'), ('Create Again', 'repeat')],
    'notes': 'This is our design philosophy, not a research claim: create first, make it personal, explore through '
             'interaction, keep access simple.',
}

SLIDE_4_SOLUTION = {
    'title': 'From Paper to Interactive Learning',
    'message': 'Children color a physical sheet, scan it through the website, and watch their own artwork become an '
               'animated character with sound, motion, and educational content.',
    # (label, caption, image in assets/gen, fit by 'w' or 'h')
    'steps': [('Color', 'Kids color a Scanvas paper sheet', 'paper_whale.png', 'w'),
              ('Scan', 'Snap or upload a photo in the browser', 'ph_scan.png', 'h'),
              ('Come Alive', 'The artwork comes alive in seconds', 'alive_whale.png', 'w'),
              ('Explore', 'It swims inside a living world', 'ph_world.png', 'h'),
              ('Learn', 'A short story, sounds, and facts', 'tab_result.png', 'w')],
    'notes': 'One simple loop: Color, Scan, Come Alive, Explore, Learn. Everything runs in the browser.',
}

SLIDE_5_PRODUCT = {
    'tag': 'LIVE TODAY · scanvas.id',
    'title': 'Already Live.\nNo App Required.',
    # (icon, heading, detail) - only features that exist in the product today
    'capabilities': [('scan-line', 'Physical → Digital', 'Paper coloring + photo/upload processing'),
                     ('compass', 'Interactive worlds', 'Ocean & Vehicle worlds'),
                     ('wand-sparkles', 'Personalized animation', 'The child’s own artwork comes alive'),
                     ('music', 'Learning layer', 'Object sounds + short stories and facts'),
                     ('palette', 'Digital trial', 'Try the experience before buying paper')],
    'phones': [('ph_home.png', 'Landing page'), ('ph_scan.png', 'Scan / upload'), ('ph_world.png', 'Alive in the world')],
    'screens': [('tab_world_bus.png', 'Vehicle world'), ('tab_result.png', 'Story & sound')],
    'notes': 'Everything on this slide is live today at scanvas.id: real screenshots from the current product.',
}

SLIDE_6_MAGIC = {
    'title': 'Their Creation. Their Character.',
    'message': 'Unlike generic videos or static worksheets, Scanvas makes the child’s own colored artwork the '
               'center of the digital experience.',
    'before': 'Before: on paper',
    'after': 'After: alive in Scanvas',
    'trio': [('Movement', 'move'), ('Sound', 'music'), ('Learning Facts', 'book-open')],
    'notes': 'The emotional core: the child is not watching a character, they are watching their own creation.',
}

SLIDE_7_DIFFERENT = {
    'title': 'One Engine, Many Learning Experiences',
    'items': [('Physical-Digital Bridge', 'Children start with real paper and their own hands.'),
              ('Personalized Output', 'The scanned artwork, not a stock character, enters the experience.'),
              ('Low-Friction Access', 'Browser-based, with no mandatory app installation.'),
              ('Reusable Learning Engine', 'The same processing and interactive-world system can support animals, '
                                           'vehicles, nature, creative classes, and future themes.')],
    'notes': 'Why Scanvas can grow: one scan-to-animation engine, reused across many learning worlds.',
}

SLIDE_8_ROADMAP = {
    'title': 'From Magic Moment\nto Learning Platform',
    'message': 'Today, Scanvas uses the child’s creation to trigger curiosity and discovery. '
               'Next, we are building structured learning activities around that engagement.',
    # (stage chip, flow, description, icon)
    'stages': [('CURRENT · LIVE', 'Color → Scan → Alive', 'Today’s magical coloring experience.',
                'wand-sparkles'),
               ('NEXT', 'Create → Explore → Story → Quiz',
                'An interactive learning layer with stories, guided questions, and simple quizzes.', 'book-open'),
               ('FUTURE', 'Learn → Practice → Create → Bring It Alive',
                'Digital drawing and coloring classes: learn step-by-step, practice digitally, and bring the '
                'creation into Scanvas worlds.', 'graduation-cap')],
    'notes': 'Engagement engine exists today; structured learning comes next. Only the first step is live.',
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
    'notes': 'A future product: guided drawing classes that end with the child’s creation entering a Scanvas world.',
}

SLIDE_10_MARKET = {
    'title': 'One Platform, Multiple Paths to Scale',
    # (segment, heading, description, (revenue label, revenue model), image, (tag, style))  style: live|building|future
    'segments': [('B2C', 'Families',
                  'Physical creative packs combining coloring sheets with the Scanvas digital experience.',
                  ('Revenue model', 'Per-pack purchase'), 'm_pack.png', ('AVAILABLE NOW', 'live')),
                 ('B2B', 'Schools & Events',
                  'Scanvas Studio for organized sessions, participant management, bulk processing, and shared '
                  'experiences.',
                  ('Revenue model under validation', 'Per session / per participant / usage-based'),
                  'm_studio.png', ('IN DEVELOPMENT', 'building')),
                 ('B2C + B2B', 'Digital Learning',
                  'Creative classes, learning worlds, content packs, and additional learning modules.',
                  ('Potential model', 'Subscriptions and content add-ons'), 'm_lesson.png', ('FUTURE', 'future'))],
    'notes': 'Families buy packs today. School and event pricing is being validated with the pilot before we '
             'commit to numbers.',
}

SLIDE_11_VALIDATION = {
    'title': 'Early Validation →\nScalable Learning Worlds',
    'snapshot_title': 'Early validation',
    'facts': 'Live product · 2 worlds · scan-to-animation working',
    # real pilot data, each label says exactly what it counts (TPA = Taman Pendidikan Anak-anak)
    'metrics': [('30', 'pilot participants'), ('1', 'real-world pilot (TPA)'), ('5', 'improvements from feedback')],
    'feedback_title': 'Feedback already changed the product',
    # (status: shipped | progress, what changed)
    'feedback': [('shipped', 'Larger world for more creations'),
                 ('shipped', 'Digital trial before purchase'),
                 ('progress', 'Bulk drawing uploads'),
                 ('progress', 'Learning space after play (Next stage)'),
                 ('progress', 'More worlds, e.g. a land version')],
    'status_label': {'shipped': 'Shipped', 'progress': 'In progress'},
    'phases': [('PHASE 1', 'Validate the Magic', 'Improve scan reliability; grow from 1 TPA pilot to more families and schools.'),
               ('PHASE 2', 'Build Learning', 'Stories, quizzes, guided creative lessons, teacher and session tools.'),
               ('PHASE 3', 'Scale Platform', 'Content library, Scanvas Studio, school partnerships, new learning worlds.')],
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
    'closing': 'We want children to use technology not only to consume, but to imagine, create, and learn.',
    'final': 'Scanvas — From imagination to interactive learning.',
    'notes': 'Salsabila leads business, partnerships, customer discovery and go-to-market; Haikal leads product, '
             'engineering and the computer-vision pipeline. Close on the vision: children as creators.',
}
