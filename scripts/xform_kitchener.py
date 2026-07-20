"""
xform_kitchener.py — turn the House Lyft master report into the Kitchener lead
report for Saleem Sial, 479 Connaught Street, Kitchener, ON.

Kitchener has NO city adapter in property_lookup_v2, so this is a
"researched-live / needs-review" report per THE PRIME RULE: full report,
figures hedged, tagged report-needs-review.

Scope (GHL field EPzqHHy5AU2iIvHIAhKf) = "Secondary Suite" -> units_added = 1,
render mode = scoped. Programs cleared at 1 unit in Kitchener/Ontario:
  - Bill 23 development-charge exemption for additional residential units (<=2)
  - Region of Waterloo Ontario Renovates secondary-suite forgivable loan
    (researched live; figures hedged)
  - GST/HST PBRH rebate clears only at 4+ units -> moves into the 4-unit upside
Toronto DC waiver, MLI Select, Prefab Plus, Simcoe, Mississauga, Alberta/
Edmonton and MHRTC are all gated out and do NOT appear.

Zoning grounding (researched live 2026-07-20, official City of Kitchener sources):
  - Kitchener Zoning By-law 2019-051 (low-rise RES zones, Section 7).
  - 25 Mar 2024 Official Plan + ZBL amendments: up to 4 dwelling units on
    residential lots city-wide (beyond the provincial 3-unit floor / Bill 23).
  - Parking: 2 for the principal dwelling + 1 for the additional unit; all
    three may be tandem. Attached ADU must connect to full municipal services.
    1.1 m unobstructed walkway to an entrance not facing the street.

Imagery: engine OIWMS province-wide fallback (© King's Printer for Ontario),
two zoom levels for a genuine lot view + wider context view.

Anchors are ASCII-only (regex / literal) so unicode in the master text cannot
break matching. Each replacement asserts it fired exactly once; a leftover
grep runs at the end.
"""
import re

PATH = "report_kitchener.html"
s = open(PATH).read()

# ---- imagery: real OIWMS aerials (lot ~167 m across, context ~333 m across) --
IMG_BLOCK = (
    '<div class="imgrow" style="margin-top:0;">\n'
    '    <div style="flex:1;position:relative;height:148px;overflow:hidden;'
    'border:1px solid var(--line);">'
    '<img src="gen/aerial_lot.jpg" alt="Aerial view of 479 Connaught Street" '
    'style="width:100%;height:148px;object-fit:cover;display:block;">'
    '<span style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);'
    "color:#fff;font-family:'Lato',Arial,sans-serif;font-size:7.4pt;padding:3px 7px;\">"
    'Aerial view — approx. 167&nbsp;m across</span></div>\n'
    '    <div style="flex:1;position:relative;height:148px;overflow:hidden;'
    'border:1px solid var(--line);">'
    '<img src="gen/aerial_ctx.jpg" alt="Neighbourhood context around 479 Connaught Street" '
    'style="width:100%;height:148px;object-fit:cover;display:block;">'
    '<span style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);'
    "color:#fff;font-family:'Lato',Arial,sans-serif;font-size:7.4pt;padding:3px 7px;\">"
    'Neighbourhood context — approx. 333&nbsp;m across</span></div>\n'
    '  </div>\n'
    '  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">'
    'Imagery: Ontario Imagery Web Map Service, © King’s Printer for Ontario '
    '(open data, used with attribution).</div>'
)

# ---- property table 2 (municipality / neighbourhood / bylaw / lot) -----------
PROP2 = (
    '    <tr><td>Municipality</td><td>Kitchener (Region of Waterloo)</td></tr>\n'
    '    <tr><td>Neighbourhood</td><td>Vanier</td></tr>\n'
    '    <tr><td>Region</td><td>Region of Waterloo</td></tr>\n'
    '    <tr><td>Waste Collection</td><td>Region of Waterloo curbside schedule</td></tr>\n'
    '    <tr><td>Current Bylaw</td><td>City of Kitchener Zoning By-law 2019-051</td></tr>\n'
    '    <tr><td>Legal Description</td><td>To be confirmed</td></tr>\n'
    '    <tr><td>Year Built</td><td>To be confirmed</td></tr>\n'
    '    <tr><td>Lot size</td><td>To be confirmed (Phase 2)</td></tr>\n'
    '    <tr><td>Development Goals</td><td>Interior secondary suite (primary); '
    'second additional unit / up to 4 units (optional upside)</td></tr>'
)

SPOTLIGHT = (
    '<div class="ct">Neighbourhood Spotlight</div>\n'
    '    479 Connaught Street is in the Vanier neighbourhood of central Kitchener — '
    'an established, low-rise residential area within the Region of Waterloo:\n'
    '    <ul>\n'
    '      <li>Established residential streets — the kind of neighbourhood stock that '
    'holds value and rents steadily</li>\n'
    '      <li>A neighbourhood school and open green space sit nearby, directly across '
    'the street (visible in the aerial above)</li>\n'
    '      <li>Central Kitchener location with quick access to the Conestoga Parkway '
    '(Highway 8) and the regional road network</li>\n'
    '      <li>Steady rental demand across Waterloo Region, anchored by major employers '
    'and post-secondary institutions (University of Waterloo, Wilfrid Laurier University, '
    'Conestoga College)</li>\n'
    '      <li>Served by Grand River Transit, with ION light rail running through central '
    'Kitchener (exact stops and routes confirmed in Phase 2)</li>\n'
    '    </ul>\n'
    '    <div style="font-size:8pt;color:#7a818f;margin-top:6px;">Illustrative context, '
    'not a valuation.</div>'
)

ZONING = (
    '<tr><td>Current Zoning</td><td>Low Rise Residential (RES zone), City of Kitchener '
    'Zoning By-law 2019-051 — exact zone designation confirmed in Phase 2</td></tr>\n'
    '    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (municipal '
    'water &amp; sewer) in a zone that permits single detached, semi-detached or street '
    'townhouse dwellings — the criteria Kitchener applies for additional dwelling units.</td></tr>\n'
    '    <tr><td>Recent Changes</td><td>On March 25, 2024, Kitchener Council approved '
    'Official Plan and Zoning By-law amendments enabling up to <strong>4 dwelling units</strong> '
    'on residential lots city-wide — beyond the provincial floor of 3 units (Bill 23). '
    'No rezoning required.</td></tr>\n'
    '    <tr><td>Permitted Uses</td><td>An interior secondary suite (an additional dwelling '
    'unit within the home or an addition) is permitted as-of-right; up to 4 units total may '
    'be possible, subject to minimum lot width, servicing and site standards. '
    'Confirmed in Phase 2.</td></tr>\n'
    '    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to '
    'Step 2 — <strong>Builder Ready Package™</strong></td></tr>'
)

MEANS = (
    '<li><strong>Interior Secondary Suite:</strong> a self-contained additional dwelling '
    'unit inside the existing home (for example, a basement suite) — your primary goal</li>\n'
    '      <li><strong>Attached Additional Unit:</strong> an additional dwelling unit '
    'created through an addition to the home</li>\n'
    '      <li><strong>Detached Backyard Home (ADU):</strong> a separate self-contained '
    'suite in the rear yard</li>\n'
    '      <li><strong>Up to 4 Units:</strong> Kitchener permits up to four dwelling units '
    'on a qualifying residential lot — combinations of the above, subject to site standards</li>'
)

TIMESENS = (
    '<div class="d"><div class="dt">Development-Charge Exemption — In Effect</div>'
    '<div class="dx">Under Ontario’s Bill 23 (More Homes Built Faster Act), additional '
    'residential units are exempt from municipal development charges — covering the first '
    'two additional units on your lot. This is a meaningful per-unit saving on a secondary '
    'suite, applied without a separate application. Confirmed for your project in Phase 2.</div></div>\n'
    '    <div class="d"><div class="dt">Region of Waterloo Secondary Suite Funding<br>'
    '<small>budget-limited</small></div><div class="dx">The Region of Waterloo has offered '
    'a forgivable loan of up to $25,000 toward creating a secondary suite through its Ontario '
    'Renovates program (reported as a 15-year forgivable term, with an affordable-rent '
    'commitment and income criteria). These programs are budget-limited and open and close — '
    'current availability and exact terms are confirmed in Phase 2.</div></div>\n'
    '    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing '
    'Corporation (CMHC) policy changes can occur at any time, potentially affecting financing '
    'options. It is recommended to submit your application as early as possible to reduce '
    'any risk.</div></div>'
)

TWOCARD = (
    '<div class="twocard">\n'
    '    <div class="card2"><div class="ct">Additional units — up to four</div>'
    'Kitchener’s 2024 zoning amendments permit up to four dwelling units on a qualifying '
    'residential lot without rezoning, subject to lot width, servicing and site standards.</div>\n'
    '    <div class="card2"><div class="ct">Detached backyard home</div>A detached additional '
    'dwelling unit (backyard home) is permitted in Kitchener’s residential zones as-of-right, '
    'subject to the by-law’s siting and size standards.</div>\n'
    '  </div>'
)

REZ_PARA = (
    '<p>Because 479 Connaught Street already permits a secondary suite under existing zoning, '
    'no rezoning application is contemplated in this analysis. Your project advances directly '
    'to design and permitting. The comparison above shows what that avoids. This assessment '
    'reflects the by-laws in force at the date of this report and is subject to technical '
    'review of site conditions. Because Kitchener is a newly researched municipality for this '
    'report, the exact zone designation and site-specific standards should be double-checked '
    'in Phase 2.</p>'
)

AMBER = (
    '<div class="co-amber"><b>Two items to confirm early: the lot’s minimum width and its '
    'servicing.</b><br><span class="sub">Kitchener notes that some lots support only one or '
    'two units due to minimum lot width, servicing capacity, or natural-hazard constraints. '
    'An attached additional unit must connect to full municipal services. Both are confirmed '
    'in Phase 2.</span></div>'
)

OPT_A_OD = (
    '<div class="od">A self-contained additional dwelling unit inside the existing home — for '
    'example, a basement suite — rented for ongoing income while you keep the property. This is '
    'your stated goal and is permitted as-of-right under Kitchener Zoning By-law 2019-051 on a '
    'serviced residential lot; no rezoning. Parking for the property is set at two spaces for the '
    'principal dwelling plus one for the additional unit, and Kitchener permits all three to be '
    'arranged in tandem (one behind another). An attached additional unit must connect to full '
    'municipal services. Where the unit’s entrance does not face the street, the by-law '
    'requires a 1.1 m unobstructed walkway to that entrance. Exact suite size and layout are '
    'confirmed in Phase 2.</div>'
)

OPT_B_OD = (
    '<div class="od">Pair the interior secondary suite with a second additional unit — either a '
    'further unit within the building or a detached backyard home — for up to three units on the '
    'lot. This is permitted as-of-right where the lot supports it, and the first two additional '
    'units are exempt from development charges under Bill 23. It increases rental income while you '
    'keep ownership of the property. Eligibility, unit sizes and parking are confirmed in Phase 2.</div>'
)

OPT_C_OD = (
    '<div class="od">Kitchener permits up to four dwelling units on a qualifying residential lot. '
    'Building to four self-contained rental units changes the financing picture: at four or more '
    'rental units, the federal GST/HST Purpose-Built Rental Housing rebate opens up (a rebate of '
    'the 5% federal GST, with Ontario mirroring the 8% provincial component on qualifying '
    'purpose-built rental) — a program that does not apply to a single secondary suite. Whether '
    'four units fit depends on the lot’s width and servicing, confirmed in Phase 2. This is '
    'presented as upside, not a recommendation — your stated goal is the secondary suite in '
    'Option A.</div>'
)

GOAL_SUMMARY = (
    '<div class="barhead" style="text-align:left;">Secondary Suite (Additional Dwelling Unit)</div>\n'
    '  <p>479 Connaught Street is a serviced residential lot in Kitchener where an interior '
    'secondary suite is permitted as-of-right under Zoning By-law 2019-051 — matching your goal '
    'of adding rental income while keeping the property. <strong>The secondary suite is the clear '
    'primary recommendation</strong>, with a second additional unit, or a build up to Kitchener’s '
    'four-unit maximum, as optional upside where the lot supports it.</p>'
)

SUMMARY8 = (
    '<p>479 Connaught Street is a serviced residential lot in Kitchener’s Vanier '
    'neighbourhood. Under City of Kitchener Zoning By-law 2019-051, an interior secondary suite '
    'is <strong>permitted as-of-right</strong> — matching your stated goal — and the lot may '
    'support up to four dwelling units, subject to lot width, servicing and site standards.</p>\n'
    '  <ul>\n'
    '    <li><strong>The Secondary-Suite Advantage:</strong> an additional dwelling unit adds a '
    'rental income stream using space you already own — no rezoning, no public hearing, no '
    'Council approval required. The exact suite size and layout are confirmed in Phase 2.</li>\n'
    '    <li><strong>Room to grow:</strong> Kitchener’s 2024 move to allow up to four units '
    'city-wide means the same lot can potentially scale beyond a single suite if you choose — with '
    'the larger federal rental-rebate programs opening up at four units.</li>\n'
    '  </ul>'
)

GRANTS_ROWS = (
    '<tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units '
    '(Bill 23)</td><td>Additional residential units are exempt from municipal development '
    'charges — covering the first two additional units on the lot. Applies to a compliant '
    'secondary suite without a separate application. Source: Ontario More Homes Built Faster Act '
    '(Bill 23). Confirmed in Phase 2.</td></tr>\n'
    '    <tr><td>Regional</td><td>Region of Waterloo — Secondary Suite Funding (Ontario '
    'Renovates)</td><td>Forgivable loan reported up to $25,000 toward creating a secondary suite '
    '(reported 15-year forgivable term; affordable-rent commitment and income criteria apply). '
    'Budget-limited and periodically open/closed. Source: Region of Waterloo Housing Services — '
    'Ontario Renovates. Current availability and exact terms confirmed in Phase 2.</td></tr>\n'
    '    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing Rebate — at 4+ units</td>'
    '<td>Does not apply to a single secondary suite. If the lot is built to four or more '
    'self-contained rental units (Kitchener’s maximum), a rebate of the 5% federal GST opens '
    'up, with Ontario mirroring the 8% provincial component on qualifying purpose-built rental. '
    'Threshold: 4+ rental units. Confirmed in Phase 2.</td></tr>\n'
    '    </table>'
)

# ---- replacement plan: ('lit'|'re', anchor, replacement) --------------------
PLAN = [
    # cover
    ('lit', '<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
            '<div class="addr">479 Connaught Street<span>Kitchener, ON</span></div>'),
    # property details barhead
    ('lit', '<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
            '<div class="barhead">479 Connaught Street, Kitchener, ON&nbsp;&nbsp;N2C 1C6</div>'),
    # imagery block (regex over the whole placeholder row)
    ('re', r'<div class="imgrow" style="margin-top:0;">.*?Imagery: source and licence inserted at generation\.</div>',
            IMG_BLOCK),
    # property table 1 (literal ASCII block)
    ('lit',
     '    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>\n'
     '    <tr><td>Name</td><td>John Arockiaraj</td></tr>\n'
     '    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>\n'
     '    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>\n'
     '    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>',
     '    <tr><td>Property Address</td><td>479 Connaught Street, Kitchener, ON&nbsp;&nbsp;N2C 1C6</td></tr>\n'
     '    <tr><td>Name</td><td>Saleem Sial</td></tr>\n'
     '    <tr><td>Phone Number</td><td>Provided at intake</td></tr>\n'
     '    <tr><td>Email</td><td>Provided at intake</td></tr>\n'
     '    <tr><td>Development Goals</td><td>Secondary suite (additional dwelling unit) for rental income</td></tr>'),
    # property table 2 (regex, ASCII anchors, spans unicode lot-size line)
    ('re', r'<tr><td>Municipality</td><td>Toronto</td></tr>.*?Multiplex \(alternative\)</td></tr>',
            PROP2),
    # neighbourhood spotlight (regex to first </ul>)
    ('re', r'<div class="ct">Neighbourhood Spotlight</div>.*?</ul>', SPOTLIGHT),
    # zoning table (regex)
    ('re', r'<tr><td>Current Zoning</td><td>RD.*?Development Goals Achievable\?</td><td><strong>YES</strong>.*?</td></tr>',
            ZONING),
    # what this means (regex)
    ('re', r'<li><strong>Townhouse &amp; Stacked Townhouse:</strong>.*?boost density</li>', MEANS),
    # time-sensitive three cards (regex)
    ('re', r'<div class="d"><div class="dt">Ontario HST Rebate.*?reduce any risk\.</div></div>', TIMESENS),
    # rezoning co-green
    ('lit', '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
            '<div class="co-green"><div class="ct2">Not Required for This Property</div>A secondary suite (additional dwelling unit) is permitted as-of-right under City of Kitchener Zoning By-law 2019-051 — no rezoning required.</div>'),
    # rezoning comparison "what governs"
    ('lit', '<td class="g">By-law 654-2025</td>', '<td class="g">Zoning By-law 2019-051</td>'),
    # rezoning twocard (regex)
    ('re', r'<div class="twocard">.*?as-of-right in residential zones\.</div>\s*</div>', TWOCARD),
    # rezoning barhead
    ('lit', '<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
            '<div class="barhead" style="text-align:left;">What this means for 479 Connaught Street</div>'),
    # rezoning paragraph (regex, ASCII anchors)
    ('re', r'<p>Because 303 Coxwell Avenue already permits the recommended build.*?technical review of site conditions\.</p>',
            REZ_PARA),
    # rezoning amber note (regex, ASCII anchors)
    ('re', r'<div class="co-amber"><b>One item to confirm.*?before financing or development can proceed\.</span></div>',
            AMBER),
    # option A oh / od
    ('re', r'<div class="oh">Option A [^<]*</div>',
            '<div class="oh">Option A — Interior Secondary Suite (your goal)</div>'),
    ('re', r'<div class="od">A detached 4-unit houseplex.*?\(Bill 185\)\.</div>', OPT_A_OD),
    # option B oh / od
    ('re', r'<div class="oh">Option B [^<]*</div>',
            '<div class="oh">Option B — Secondary Suite + a Second Additional Unit</div>'),
    ('re', r'<div class="od">A detached 6-unit houseplex.*?Development charges fully waived\.</div>', OPT_B_OD),
    # option C oh / od
    ('re', r'<div class="oh">Option C [^<]*</div>',
            '<div class="oh">Option C — The Path to Four Units (upside)</div>'),
    ('re', r'<div class="od">The existing ~750 sq ft garage.*?financing process can proceed\.</div>', OPT_C_OD),
    # development goal summary (regex)
    ('re', r'<div class="barhead" style="text-align:left;">6\+1 Configuration</div>.*?clear primary recommendation\.</strong></p>',
            GOAL_SUMMARY),
    # summary section 8 (regex)
    ('re', r'<p>303 Coxwell Avenue confirms a strong development option\..*?no Council approval required\.</li>\s*</ul>',
            SUMMARY8),
    # grants injection: replace the GATED_GRANTS_ROWS comment + closing table tag
    ('re', r'<!-- GATED_GRANTS_ROWS.*?See docs/PROGRAM_GATING_v1\.md -->\s*</table>',
            GRANTS_ROWS),
]

fails = []
for kind, old, new in PLAN:
    if kind == 'lit':
        c = s.count(old)
        if c != 1:
            fails.append((kind, old[:70], c)); continue
        s = s.replace(old, new)
    else:
        matches = re.findall(old, s, flags=re.DOTALL)
        if len(matches) != 1:
            fails.append((kind, old[:70], len(matches))); continue
        s = re.sub(old, lambda m: new, s, count=1, flags=re.DOTALL)

if fails:
    print("REPLACEMENT FAILURES:")
    for k, a, c in fails:
        print(f"  [{k} x{c}] {a!r}")
    raise SystemExit(1)

open(PATH, "w").write(s)

# ---- leftover guard ---------------------------------------------------------
LEFT = ["303 Coxwell", "Coxwell", "Arockiaraj", "johneeraj", "Toronto",
        "Ward 19", "Beaches", "654-2025", "474-2023", "569-2013", "Bill 185",
        "6+1", "4+1", "houseplex", "TTC", "Greenwood", "Danforth",
        "M4L 3B5", "Garden Suite By-law", "Woodbine"]
print("=== leftover check ===")
any_left = False
for t in LEFT:
    n = s.count(t)
    if n:
        any_left = True
        print(f"LEFTOVER '{t}': {n}")
if not any_left:
    print("clean — no source-city leftovers")
print("replacements applied:", len(PLAN))
