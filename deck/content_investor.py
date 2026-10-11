"""SCANVAS investor deck, October 2026 (SCANVAS_Investor_Oct2026). 13 main slides + 7 appendix.

Branch of the DSC S17 deck (content_dsc.py: business, GTM, funding structure), updated with ITEC v5 (product, pilot,
validation order, council feedback), the new product roadmap (roadmap_new.md, Sep 2026: Scanvas Learn / Ocean
Artist course, 3-lesson pilot gate, Classroom), and the founders' CVs (Oct 2026). Revised after a mentor-style review
(Oct 2026): monthly cash flow with capex and working capital, sales engine per target, numeric gates, defined repeat
metrics, cost coverage per offer, course learning design.

Honesty rules: live product, 2 worlds, one completed 30-child pilot (participation, not measured completion),
pre-revenue. Course, Studio/Classroom, and licenses are PLANNED and labelled as such. Every price, cost, volume,
conversion, gate threshold, and the five-year model are a working scenario (Oct 2026), not an approved forecast; the
year-2 raise is sized by the model, not committed. Ask: Rp200M for 12% (post-money); a 15% negotiation range is
internal only and never appears in the deck.
Team: Haikal Hilmi CEO (60% pre-investment), Salsabila Khoirunnisa CMO (40%), as in the ITEC application.
"""
import math

from .content_itec3 import PILOT_ART, SLIDE_4_SOLUTION, SLIDE_COMPETITION as _COMP, SLIDE_PIPELINE as _PIPE, \
    SLIDE_SOURCES as _SRC

TRACK = 'Investor deck · October 2026'
WEBSITE = 'scanvas.id'

# ================================================================ working model (all money in Rp juta)
# unit economics: (name, price, direct cost, what the direct cost covers)
UNITS = {
    'pack':    ('Family creative pack', 0.049, 0.020,
                'Printing & packaging Rp10K + delivery Rp10K per pack'),
    'session': ('Managed school / event session', 1.000, 0.250,
                'Facilitator fee, transport, printed sheets for up to 30 children (not in opex)'),
    'course':  ('Ocean Artist digital course', 0.099, 0.020,
                'Video hosting, payment fee, customer support (cash costs only; lesson production is in opex)'),
    'license': ('Studio / Classroom license (per year)', 2.400, 0.240,
                'Hosting & scan quota (up to 3,000 scans/yr), teacher onboarding, support; content updates in opex'),
}
SHORT = {'pack': 'Family packs', 'session': 'Sessions', 'course': 'Courses', 'license': 'Licenses'}
# base-case yearly volumes
VOLUME = {'pack': [600, 1200, 2500, 5000, 10000],
          'session': [48, 96, 200, 360, 600],
          'course': [100, 500, 1500, 4000, 10000],
          'license': [0, 0, 25, 80, 250]}
OPEX = [180, 210, 330, 660, 1200]       # team, GTM, product, content, legal (sessions' facilitators sit in direct cost)
CAPEX = [15, 5, 15, 30, 50]             # devices & session kits (Y1 M1, Y2 M13), then servers/devices as volumes grow
CONSERVATIVE = 0.6                      # conservative case: 60% of base volumes, same costs

# months 1-24: volumes per month (sum to the year-1 and year-2 volumes above)
M_SESSION = [2, 3, 4, 4, 4, 4, 4, 5, 5, 5, 4, 4] + [8] * 12
M_PACK = [20, 30, 40, 40, 50, 50, 50, 60, 60, 70, 70, 60] + [100] * 12
M_COURSE = [0] * 7 + [10, 15, 20, 25, 30] + [30, 32, 35, 38, 40, 42, 44, 45, 46, 48, 50, 50]
M_PRINT = {1: 200, 5: 200, 9: 200, 13: 300, 16: 300, 19: 300, 22: 300}   # packs printed in prepaid batches
M_CAPEX = {1: CAPEX[0], 13: CAPEX[1]}
SESSION_PAY_LAG = 1                     # schools pay one month after the session
BUFFER_MONTHS = 3                       # keep at least 3 months of opex in the bank


def monthly(raise2, scale=1.0):
    """Cash balance at the end of months 1-24 (Rp200M arrives in month 1, the year-2 raise in month 13)."""
    cash, out = 0.0, []
    for m in range(1, 25):
        i = m - 1
        s, p, c = (v[i] * scale for v in (M_SESSION, M_PACK, M_COURSE))      # fractional: a scenario is an exact %
        paid_sessions = M_SESSION[i - SESSION_PAY_LAG] * scale if i >= SESSION_PAY_LAG else 0
        cash_in = p * UNITS['pack'][1] + c * UNITS['course'][1] + paid_sessions * UNITS['session'][1]
        cash_out = (p * 0.010 + c * UNITS['course'][2] + s * UNITS['session'][2]          # delivery at sale
                    + M_PRINT.get(m, 0) * scale * 0.010                               # printing, prepaid
                    + M_CAPEX.get(m, 0) + OPEX[i // 12] / 12)
        cash += (200 if m == 1 else raise2 if m == 13 else 0) + cash_in - cash_out
        out.append(cash)
    return out


_NO_RAISE = monthly(0)
BUFFER = BUFFER_MONTHS * OPEX[1] / 12
Y2_RAISE = max(0, math.ceil((BUFFER - min(_NO_RAISE[12:])) / 25) * 25)   # sized from the monthly low point
FUNDING = [200, Y2_RAISE, 0, 0, 0]
CASH_M = monthly(Y2_RAISE)
CASH_M_CONS = monthly(Y2_RAISE, CONSERVATIVE)
LOW_NO_RAISE = (min(_NO_RAISE), _NO_RAISE.index(min(_NO_RAISE)) + 1)
FIRST_NEGATIVE = next((m + 1 for m, v in enumerate(_NO_RAISE) if v < 0), None)


def _wc_monthly(scale, month):
    """Working capital at the end of a model month: unpaid sessions + printed-but-unsold pack stock."""
    receivable = sum(M_SESSION[i] * scale for i in range(month - SESSION_PAY_LAG, month)) * UNITS['session'][1]
    printed = sum(n * scale for m, n in M_PRINT.items() if m <= month)
    sold = sum(M_PACK[i] * scale for i in range(month))
    return receivable + (printed - sold) * 0.010


def _wc(scale, i):
    """Working capital at a year end. Years 1-2 come from the monthly model; years 3-5 assume one month of B2B
    receivables and two months of pack print stock."""
    if i < 2:
        return _wc_monthly(scale, 12 * (i + 1))
    vol = {k: VOLUME[k][i] * scale for k in VOLUME}
    return (vol['session'] * UNITS['session'][1] + vol['license'] * UNITS['license'][1]) / 12 \
        + vol['pack'] * 0.010 * 2 / 12


def _model(scale=1.0, cash_m=None):
    vol = {k: [VOLUME[k][i] * scale for i in range(5)] for k in UNITS}
    for k, months in (('pack', M_PACK), ('session', M_SESSION), ('course', M_COURSE)):   # monthly plan = yearly volume
        for y in (0, 1):
            assert sum(months[12 * y:12 * y + 12]) == VOLUME[k][y], (k, y)
    rev = {k: [vol[k][i] * UNITS[k][1] for i in range(5)] for k in UNITS}
    con = {k: [vol[k][i] * (UNITS[k][1] - UNITS[k][2]) for i in range(5)] for k in UNITS}
    revenue = [sum(rev[k][i] for k in UNITS) for i in range(5)]
    contribution = [sum(con[k][i] for k in UNITS) for i in range(5)]
    result = [contribution[i] - OPEX[i] for i in range(5)]
    wc = [_wc(scale, i) for i in range(5)]
    dwc = [wc[0]] + [wc[i] - wc[i - 1] for i in range(1, 5)]      # change in working capital
    cash, c = [], 0.0
    for i in range(5):                              # every row shown in Appendix A, nothing hidden
        c += FUNDING[i] + result[i] - CAPEX[i] - dwc[i]
        cash.append(c)
    for y in (0, 1):                                # the annual table must equal the monthly chart
        assert abs(cash[y] - cash_m[12 * y + 11]) < 0.05, (y, cash[y], cash_m[12 * y + 11])
    return {'vol': vol, 'rev': rev, 'revenue': revenue, 'contribution': contribution, 'result': result,
            'dwc': dwc, 'cash': cash}


BASE, CONS = _model(1.0, CASH_M), _model(CONSERVATIVE, CASH_M_CONS)


def rp(v, sign=False):
    """Rp juta -> 'Rp87.3M' / 'Rp1.19B'."""
    s = '−' if v < 0 else ('+' if sign and v > 0 else '')
    v = abs(v)
    return f'{s}Rp{v / 1000:.2f}B' if v >= 1000 else f'{s}Rp{v:.1f}M'


def rpu(v):
    """Unit price in Rp juta -> 'Rp49K' / 'Rp1M' / 'Rp2.4M'."""
    if v < 1:
        return f'Rp{v * 1000:.0f}K'
    return f'Rp{v:g}M'


# ================================================================ 1 cover (shared slides.s1_cover)
SLIDE_1_COVER = {
    'title': 'SCANVAS',
    'subtitle': 'Where Children’s Creativity Comes Alive',
    'body': 'Children turn their paper artwork into interactive characters and learning experiences, directly in the '
            'browser.',
    'age_chip': 'Top 30 · ITEC SEA 2026',
    'founder_name': 'Haikal Hilmi · CEO & Co-Founder',
    'founder_role': 'Salsabila Khoirunnisa · CMO & Co-Founder',
    'name_box_w': 3.1,
    'notes': 'Scanvas turns a child’s paper artwork into an interactive character in the browser. Top 30 at ITEC SEA '
             '2026. Live product, two worlds, one completed 30-child pilot, pre-revenue.',
}

# ================================================================ 2 customer problem
PROBLEM = {
    'title': 'Parents and Schools Need Creative Activities\nThat Are Easy to Run and Worth Repeating',
    'buyers': [('PARENTS', 'house', 'A creative activity they can easily accompany at home, that their child wants to '
                                    'do again.',
                'Coloring ends with the page; screens offer ready-made characters to watch.'),
               ('SCHOOLS & TPA', 'school', 'A group activity that is easy to run, engages every child, and fits a school '
                                          'budget.',
                'Teachers prepare materials themselves; digital options often need apps or devices per child.')],
    'observed_title': 'WHAT WE OBSERVED IN THE PILOT',
    'observed': ['30 children participated in a color → scan → alive session at one TPA',
                 'Feedback asked for a larger world, a trial before buying, and faster group processing'],
    'assumed_title': 'WHAT WE STILL ASSUME (TO VALIDATE)',
    'assumed': ['Parents pay for a repeatable creative activity',
                'Schools rebook sessions and later license a classroom format'],
    'notes': 'Separate what we saw from what we assume: 30 children took part in the pilot (participation, not a '
             'measured completion rate); willingness to pay and repeat use are hypotheses we test next.',
}

# ================================================================ 3 product experience
PRODUCT = {
    'title': 'The Child Creates First; Technology Extends What They Created',
    'steps': [('COLOR', 'Child colors a printed Scanvas sheet.', 'paper_whale.png', 'w'),
              ('SCAN', 'Parent or teacher photographs it in the browser.', 'ph_scan.png', 'h'),
              ('COME ALIVE', 'The child’s own artwork is extracted and animated.', 'alive_whale.png', 'w'),
              ('EXPLORE', 'It joins an interactive world with sound and facts.', 'tab_result.png', 'w')],
    'live': ['Ocean + Vehicle worlds', 'No app installation', 'Free digital trial'],
    'qr_label': 'TRY THE LIVE DEMO',
    'notes': 'Real product screenshots. The QR opens the free digital trial at scanvas.id/trial.',
}

# ================================================================ 4 traction & pilot learning
TRACTION = {
    'title': 'Live Product, First Pilot, and Clear Next Proofs',
    'metrics': [('30', 'children took part in first real-world pilot'), ('2', 'interactive worlds live'),
                ('5', 'product priorities from feedback'), ('Top 30', 'ITEC SEA 2026')],
    'shipped': ['Larger interactive world', 'Digital trial before purchase'],
    'building': ['Bulk drawing processing', 'Story and learning space', 'Additional worlds'],
    'proved_title': 'PROVEN',
    'proved': ['Product runs live in the browser', 'Children used it in a real group setting',
               'Feedback turns into shipped changes'],
    'next_title': 'NEXT PROOFS · FROM JUDGE FEEDBACK',
    'next': ['Paid demand: first paid sessions and packs', 'Repeat: rebooking and second purchase (defined on slide 8)',
             'Scan reliability ≥95% in group sessions', 'Delivery cost measured from real sessions'],
    'photo': 'pilot_photo_4.jpg',
    'caption': 'First real-world pilot · TPA, D.I. Yogyakarta · pre-revenue',
    'notes': 'We say "took part", not "completed": the pilot recorded participation, not a completion rate. ITEC '
             'Council feedback (Oct 2026) asked for financial clarity, unit economics, and validated demand.',
}

# ================================================================ 5 customers & market
MARKET = {
    'title': 'Two Customer Channels, Sized Separately',
    'inst_title': 'INSTITUTIONS · sessions now, licenses later',
    'inst': [('BEACHHEAD', '7,123', 'D.I. Yogyakarta'), ('NEXT', '62,797', 'Central Java + DIY'),
             ('NATIONAL', '420,886', 'Indonesia')],
    'inst_unit': 'PAUD + primary-school units',
    'fam_title': 'FAMILIES · packs now, course later',
    'fam_value': '≈35.3M',
    'fam_unit': 'children aged 3–10 in Indonesia (BPS-based estimate)',
    'fam_note': 'Start where we can reach: families of children in our partner schools and online in Yogyakarta.',
    'share_title': 'YEAR-5 SALES TARGETS',
    'share': [('250 licenses', '≈0.4% of Central Java + DIY school units'),
              ('10,000 course + 10,000 pack sales', 'Sales, not unique children: buyer share is measured once repeat '
                                                     'rates are known')],
    'rule': 'The two channels are not added together: a family reached through a school is counted once.',
    'source': 'Sources: Kemendikdasmen Data Referensi Pendidikan (PAUD, SD), accessed Sep 2026 · BPS population by age '
              'group 2022, ages 3–10 estimated. Details in Appendix D.',
    'notes': 'Institution counts are market coverage, not demand. Pack and course numbers are transactions, so no '
             'penetration of unique children is claimed.',
}

# ================================================================ 6 business model & unit economics
BUSINESS = {
    'title': 'Start With Packs and Sessions; Add Course and Licenses When Proven',
    'head': ['Offer', 'Status', 'Price', 'Direct cost', 'Contribution'],
    'offers': [('pack', 'LIVE · TEST PRICE', 'live'), ('session', 'VALIDATING', 'validating'),
               ('course', 'PLANNED · AFTER 3-LESSON PILOT', 'future'), ('license', 'PLANNED · YEAR 3', 'future')],
    'bundle': 'Bundle rule: a course buyer who also wants a physical kit buys a pack, counted once in pack revenue. '
              'What each direct cost covers: Appendix A.',
    'footer': 'All prices and costs are commercial-testing assumptions (Oct 2026), not validated at scale.',
    'notes': 'Session direct cost covers the facilitator, transport, and printed sheets, so it is not repeated in opex. '
             'License cost covers hosting and a scan quota, onboarding, and support; content updates are opex.',
}

# ================================================================ 7 competition & differentiation
COMPETITION = {
    'title': 'A Proven Category; Scanvas Combines What Others Split',
    'players': ['Scanvas', 'Coloring-to-\nanimation apps', 'Guided creative\nlessons', 'Venue / class\nactivities'],
    'examples': ['', 'Faber-Castell ARt Alive · Quiver', 'WAGZAK JUMP · video tutorials',
                 'teamLab Sketch Aquarium · art classes'],
    'rows': [('Child’s own artwork becomes the character', 'live', ['yes', 'Some', 'Venue only']),
             ('Runs in the browser, no app', 'live', ['no', 'Some', 'no']),
             ('Shared interactive worlds', 'live', ['no', 'no', 'yes']),
             ('Facilitated group sessions', 'pilot', ['no', 'Some', 'yes']),
             ('Guided lessons with progress', 'planned', ['no', 'yes', 'yes']),
             ('Classroom license / Studio', 'planned', ['Edu plans', 'School license', 'no'])],
    'status_label': {'live': 'LIVE', 'pilot': 'PILOT', 'planned': 'PLANNED'},
    'statement': 'Competitors validate demand for each piece. Our bet is that one engine combining them earns paid, '
                 'repeat use. Evidence per product in Appendix E.',
    'notes': 'We separate what Scanvas does today (live) from what is planned.',
}

# ================================================================ 8 go-to-market & repeat purchase
GTM = {
    'title': 'Two Funnels, Each Built for a Second Purchase',
    # (icon, name, steps, measure, repeat, year-1 math)
    'funnels': [('school', 'Schools & TPA', ['Outreach', 'Demo session', 'Paid session', 'Rebooking', 'License'],
                 'Demo → paid conversion · cost per session · scan success',
                 'Rebooking each term; license once Studio is ready',
                 '400 schools contacted (5.6% of DIY) → 100 demos (25%) → 40 paying schools (40%) + 8 rebookings (20%) '
                 '= 48 sessions · demos ≈Rp12M (≈Rp300K per paying school) · Salsabila + 1 facilitator from month 4'),
                ('house', 'Families', ['Short video', 'Free trial', 'Pack (WhatsApp)', 'Level 1 course', 'Level 2'],
                 'Trial → pack conversion · course activation · next-lesson start',
                 'Next pack or Level 2; school sessions feed family trials',
                 '≈200K views → 10,000 trials (5%) → 500 first buyers (5%) + 100 repeat packs (20%) = 600 packs; 100 courses · '
                 'ads + content ≈Rp18M (≈Rp36K per first buyer; payback via repeat + course is a hypothesis to test)')],
    'targets_title': 'YEAR-1 TARGETS · REPEAT DEFINED PER CHANNEL',
    'targets': [('48', 'paid sessions: 40 first + 8 rebooked'), ('500 + 100', 'first buyers + repeat packs = 600; 100 courses'),
                ('≥20%', 'of paying schools rebook within 90 days'),
                ('≥20%', 'of pack buyers buy again within 90 days')],
    'notes': 'Conversion rates are planning assumptions to be measured, not results. GTM budget: schools ≈Rp12M + '
             'families ≈Rp18M = Rp30M (use of funds). First-buyer CAC (≈Rp36K) exceeds one pack’s contribution '
             '(Rp29K); per first buyer we expect ≈Rp51K (pack + 20% repeat + 1-in-5 course) — a hypothesis to test.',
}

# ================================================================ 9 founding team
TEAM = {
    'title': 'Founders Who Have Built, Shipped, and Run Programs',
    'team': [('Haikal Hilmi', 'CEO & Co-Founder · 60% pre-investment', 'founder_hh.png',
              'Product, engineering, computer vision, company strategy',
              ['Information Engineering, Universitas Gadjah Mada',
               'Backend Engineer Intern, ByteDance: Go service at 100K+ requests/s',
               'Data engineer for a major Indonesian airline’s reporting pipelines',
               'Engineering PM, Gadjah Mada Aerospace Team: 40+ engineers; 3rd place Teknofest (Türkiye)',
               '1st in Indonesia, 2nd in SEA, PwC Hack-A-Day']),
             ('Salsabila Khoirunnisa', 'CMO & Co-Founder · 40% pre-investment', 'founder_sk.png',
              'Brand, customers, partnerships, go-to-market',
              ['Politics & Government student (8th semester), Universitas Gadjah Mada',
               'Exchange at Korea University, Hyundai CMK scholar (2024–2025)',
               'Chief of Social Impact, Gifood: partnerships with 7+ communities; platform reached 6,000+ users',
               'Program Manager, Sedekah Baju Yogyakarta: led 200+ volunteers, 20+ partner organizations',
               '1st place, Global Social Enterprise Competition (Thailand, 2024)'])],
    'proof': 'Together: live product, 2 worlds, first 30-child pilot, Top 30 ITEC SEA 2026.',
    'notes': 'Credentials as listed in each founder’s CV (Oct 2026). Numbers under Salsabila are results of the programs '
             'and teams she led. Ownership shown is before this round.',
}

# ================================================================ 10 12-month execution plan (numeric gates)
PLAN = {
    'title': '12-Month Plan With a Numeric Gate Before Each Build',
    # (period, heading, items, gate)
    'stages': [('MONTHS 1–3', 'Prove paid demand', ['First paid sessions', 'Test pack and session pricing',
                                                    'Scan reliability in groups'],
                'Gate · 90 days: ≥12 paid sessions from ≥8 schools; ≥95% scan success over ≥300 scans'),
               ('MONTHS 4–6', 'Studio MVP + 3-lesson pilot', ['Scanvas Studio MVP in ≥3 schools',
                                                             'Ocean Artist 3-lesson pilot', 'Real paid offer'],
                'Gate · 30 days, ≥30 children: ≥60% start lesson 2; ≥40% finish 3; ≥20% of parents pay'),
               ('MONTHS 7–9', 'Lessons 4–10 (only if gate passes)', ['Ocean Artist Level 1 (10 lessons)',
                                                                     'Course launch to pilot families',
                                                                     'Rebooking offers to schools'],
                'Gate · 90 days: ≥50 paid courses; ≥20% of paying schools rebook'),
               ('MONTHS 10–12', 'Scale what works', ['48 paid sessions cumulative', '600 packs · 100 courses',
                                                     '2 → 4 worlds'],
                'Year-1 target: Rp87.3M revenue; delivery cost per session measured')],
    'footer': 'If a gate fails, we do not build the next layer: we fix the offer or the price first.',
    'notes': 'Thresholds are proposals for the founders to confirm. Order from the roadmap: magic first (P0), then '
             'course foundation and the 3-lesson pilot, then lessons 4–10 only after the decision gate.',
}

# ================================================================ 11 five-year growth vision
VISION = {
    'title': 'From One Engine to a Course Catalog and Classroom Distribution',
    'years': [('YEAR 1', 'Validate', ['Packs + sessions', 'Ocean Artist pilot → Level 1'], 'Packs · sessions'),
              ('YEAR 2', 'Repeat', ['Level 2 + more worlds', 'More schools in DIY'], '+ courses'),
              ('YEAR 3', 'Classroom', ['Studio / Classroom licenses', 'Central Java cities'], '+ licenses'),
              ('YEAR 4', 'Catalog', ['Course catalog (new themes)', 'Distribution partners'], 'All four'),
              ('YEAR 5', 'Regional option', ['ASEAN via partners', 'Only if Indonesia is operating-positive and '
                                                                   'repeat targets hold'], 'Option, not in base')],
    'revenue_title': 'BASE-CASE REVENUE BY YEAR (INDONESIA ONLY)',
    'note': 'Course and licenses are planned; each starts only after its validation gate.',
    'notes': 'ASEAN is an option after the Indonesian model is proven, with a local partner; the base-case revenue '
             'is Indonesia only.',
}

# ================================================================ 12 financial projections (summary)
FIN = {
    'title': 'Operating-Positive From Year 3 in the Base Case',
    'funding': f'Funding: Rp200M this round · planned additional funding in year 2: Rp{Y2_RAISE}M, not committed '
               f'(sized from the monthly cash low point plus a {BUFFER_MONTHS}-month buffer, Appendix B)',
    'cons': 'Conservative case (60% of volumes, same costs): operating result stays negative until year 5 and needs '
            'more capital or lower costs from year 2.',
    'note': 'Working scenario, Oct 2026: not an approved forecast. Cash includes capex and working capital; pre-tax. '
            'Full table in Appendix A.',
    'notes': 'Show three lines live: revenue, operating result, and funding need. Details stay in the appendix.',
}

# ================================================================ 13 investment ask
ASK = {
    'title': 'Investment Ask: Rp200M for 12%',
    'statement': 'This round buys proof: customers pay, buy again, and can be served at a measured cost.',
    'amount': 'Rp200M',
    'equity': 'for 12% equity (post-money)',
    'valuation': 'Implied post-money valuation ≈ Rp1.67B',
    'period': '12-month runway to the milestones below',
    'use_title': 'USE OF FUNDS',
    'use': [('48%', 'Team & operations', 'Rp96M'), ('15%', 'Go-to-market', 'Rp30M'),
            ('12%', 'Product & technology', 'Rp24M'), ('10%', 'Production', 'Rp20M'), ('10%', 'Content & course', 'Rp20M'),
            ('5%', 'Legal & contingency', 'Rp10M')],
    'milestones_title': 'WHAT IT PROVES IN 12 MONTHS',
    'milestones': ['Paid demand: 48 sessions · 600 packs', 'Repeat: ≥20% of schools rebook, ≥20% of buyers buy again',
                   'Delivery cost per session measured', 'Ocean Artist pilot gate passed → Level 1',
                   '≥95% scan success in groups'],
    'contacts': [('Haikal Hilmi · CEO', 'haikal.hilmi02@gmail.com'),
                 ('Salsabila Khoirunnisa · CMO', 'salsabilakhn22@gmail.com')],
    'contact_extra': 'scanvas.id · WhatsApp +62 895-3675-97379',
    'notes': 'Rp200M for 12% post-money. Implied post-money ≈ Rp1.67B (200 / 0.12), pre-money ≈ Rp1.47B. After the '
             'round: Haikal 52.8%, Salsabila 35.2%, investor 12%. (Internal only: negotiation room to 15%.)',
}

# ================================================================ appendix
APPX_FIN = {
    'title': 'Appendix A · Unit Costs, Volumes, and Annual Cash Flow',
    'unit_head': ['Offer', 'Price', 'Direct cost', 'What the direct cost covers'],
    'vol_head': ['Base volumes', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5'],
    'assumptions': ['Year-1 opex Rp180M: founders Rp4M/month each, GTM, product, content, legal',
                    'Working capital: Y1–2 from the monthly model; Y3–5 = 1 month of receivables + 2 months of print stock',
                    'Capex: devices and session kits; servers and devices as volumes grow',
                    'Pre-tax; per-drawing platform revenue and grants excluded'],
    'notes': 'Every number on this slide comes from the model at the top of content_investor.py.',
}

APPX_CASH = {
    'title': 'Appendix B · Monthly Cash, Months 1–24',
    'assumptions': ['Rp200M arrives in month 1',
                    'Schools pay 30 days after each session',
                    'Packs printed in prepaid batches (200, then 300)',
                    'Devices and session kits: Rp15M in month 1, Rp5M in month 13',
                    'Opex Rp15.0M/month in year 1, Rp17.5M/month in year 2'],
    'notes': 'The year-2 raise is planned, not committed: the amount that keeps cash above a 3-month opex buffer at '
             'the monthly low point.',
}

APPX_SALES = {
    'title': 'Appendix C · Sales Engine and Team Capacity',
    'head': ['Target', 'Channel', 'Conversion (assumed)', 'Acquisition cost', 'Team capacity'],
    'rows': [('Y1 · 48 paid sessions', 'Direct outreach + demo sessions in DIY',
              '25% contact → demo; 40% demo → paid (40 schools); 20% rebook (8)', '≈Rp12M demos (≈Rp300K per paying school)',
              'Salsabila + 1 freelance facilitator from month 4'),
             ('Y1 · 600 packs, 100 courses', 'Short videos, free trial, WhatsApp orders',
              '5% view → trial; 5% trial → 500 first buyers; 20% buy again (100); 1 in 5 → course',
              '≈Rp18M (≈Rp36K per first buyer; payback is a hypothesis)',
              'Salsabila (content + orders)'),
             ('Y5 · 600 sessions (50/month)', 'School network + rebooking in DIY and Central Java',
              '≥50% of sessions from rebooking', 'Target ≤Rp150K per new paying school',
              '4 freelance facilitators (~16 sessions/month each; fee in direct cost)'),
             ('Y5 · 10,000 courses (≈833/month)', 'Partner-school family trials + digital ads',
              '≥25% of Level 1 finishers buy Level 2', 'Ceiling ≤Rp40K per course (half of contribution)',
              '2 content & growth staff (opex)'),
             ('Y5 · 250 licenses', 'Schools that already rebooked sessions', 'Session → license after 2+ rebookings',
              'Sales by school-success staff (opex)', '2 school-success staff, ≈10 onboardings/month')],
    'notes': 'All conversion and cost figures are planning assumptions to be replaced by measured values in year 1.',
}

SLIDE_SOURCES = {**_SRC, 'title': 'Appendix D · Market Figures Use Kemendikdasmen Data\nand a BPS-Based Estimate'}
SLIDE_COMPETITION = {**_COMP, 'title': 'Appendix E · Competitor Evidence',
                     'title_size': 22, 'source': 'Evidence checked Sep 2026 on each product’s official site.'}
SLIDE_PIPELINE = {**_PIPE, 'title': 'Appendix F · Technology, Delivery, and Child Data'}

APPX_COURSE = {
    'title': 'Appendix G · Course MVP: Ocean Artist Level 1 as a Learning Product',
    'lessons': ['Kenalan dengan Warna', 'Mewarnai Lebih Rapi', 'Kombinasi Warna', 'Pola Seru', 'Terang dan Gelap',
                'Campur Warna', 'Tekstur', 'Warna Imajinasi', 'Tema dan Suasana', 'Ocean Masterpiece'],
    'skills': ['choose colors, experiment', 'hand control', '2–3 colors', 'lines, dots, stripes', 'pressure and tone',
               'simple blending', 'scales, spots', 'beyond realistic', 'palette by theme', 'combine all skills'],
    # (heading, text)
    'boxes': [('LEARNING OUTCOMES', 'By lesson 10 the child chooses and combines colors on purpose, controls strokes, '
                                    'makes patterns and textures, and explains their own design choices.'),
              ('AGE & ROLES', 'Main target 5–9 (to validate); 3–4 with an adult. Parent sets up and scans; teacher '
                              'runs the classroom version. The child decides the final artwork.'),
              ('HOW PROGRESS IS SEEN', 'A simple skill checklist per lesson, filled by parent or teacher, plus the '
                                       'child’s artwork collection in My World, lesson by lesson.'),
              ('WHY LEVEL 2', 'New skills that build on Level 1, and a portfolio that shows the child’s growth; new '
                              'characters are a bonus, not the reason.')],
    'gate_title': 'GATE 3 → 10 LESSONS',
    'gate': '≥60% start lesson 2 · ≥40% finish 3 · ≥20% of parents pay · Level 2 requests',
    'notes': 'From roadmap_new (P1D): do not produce lessons 4–10 before the 3-lesson pilot passes. Age target and '
             'checklist are proposals to validate in the pilot.',
}
