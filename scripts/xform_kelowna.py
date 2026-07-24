"""
xform_kelowna.py — transform the House Lyft master report into the
1585 Abbott Street, Kelowna BC report.

Kelowna has NO city adapter in the zoning engine, so its rules were researched
live from public sources (BC Bill 44 SSMUH + City of Kelowna Zoning Bylaw No.
12375). This report is therefore a NEEDS-REVIEW report: every zoning/incentive
figure is hedged and must be double-checked before the call.

Two facts drive the honest framing here, both surfaced during live research:
  1. 1585 Abbott Street lies in the Abbott Street Heritage Conservation Area
     (designated 1998) — HCA guidelines + a possible heritage-alteration permit.
  2. The address presents as an existing multi-unit / strata building
     (Strata Plan KAS577), not a single-family infill lot.
Both are flagged prominently rather than papered over.

Follows the xform_*.py contract: every replacement must match exactly once,
then we grep for source-city leftovers.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT  = os.path.join(ROOT, "templates", "report_kelowna.html")

s = open(SRC, encoding="utf-8").read()

# --- imagery (step 4b): no verified licensed source for Kelowna -> drop the
# grey placeholder boxes entirely, keep one honest line. Regex because the
# placeholder glyphs are non-ASCII. ---
img_pat = re.compile(
    r'<div class="imgrow" style="margin-top:0;">.*?'
    r'<div class="imglicense"[^>]*>[^<]*</div>', re.DOTALL)
img_new = ('<div class="imglicense" style="font-size:8pt;color:#7a818f;'
           'margin:2px 0 10px;">Aerial and street-level photography pending a '
           'licensed imagery source.</div>')
s, n = img_pat.subn(img_new, s)
assert n == 1, f"imagery block matched {n} times (expected 1)"

R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">1585 Abbott Street<span>Kelowna, BC</span></div>'))

# property details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">1585 Abbott Street, Kelowna, BC&nbsp;&nbsp;V1Y 1A8</div>'))

# contact info table
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1585 Abbott Street, Kelowna, BC&nbsp;&nbsp;V1Y 1A8</td></tr>
    <tr><td>Name</td><td>Tony O</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>To be confirmed at intake (intake field: &ldquo;Other&rdquo;)</td></tr>'''))

# municipality / parcel table
R.append(('''    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 — Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m² (20 ft × 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>''',
'''    <tr><td>Municipality</td><td>City of Kelowna (Regional District of Central Okanagan)</td></tr>
    <tr><td>Region</td><td>Okanagan Valley, British Columbia</td></tr>
    <tr><td>Neighbourhood</td><td>Kelowna North / Abbott Street Heritage Conservation Area</td></tr>
    <tr><td>Heritage Overlay</td><td>Abbott Street Heritage Conservation Area (designated 1998) — HCA development guidelines apply; confirm in Phase 2</td></tr>
    <tr><td>Current Zoning</td><td>RU1 — as confirmed by Council March 18, 2024 (Kelowna Zoning Bylaw No. 12375); confirm per parcel in Phase 2</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH), implemented via Zoning Bylaw No. 12375</td></tr>
    <tr><td>Legal Description</td><td>Appears to be a strata property (Strata Plan KAS577) — confirm via BC LTSA in Phase 2</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — SSMUH unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Property Type</td><td>Presents as an existing multi-unit / strata residential building — confirm ownership &amp; redevelopment path in Phase 2</td></tr>'''))

# neighbourhood spotlight
R.append(('''    <div class="ct">Neighbourhood Spotlight</div>
    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    <div class="ct">Neighbourhood Spotlight</div>
    1585 Abbott Street sits in the Abbott Street Heritage Conservation Area, one of Kelowna's oldest and most prominent residential streets — running along the lake just south of the downtown core:
    <ul>
      <li>Steps from Okanagan Lake, City Park, and the downtown waterfront</li>
      <li>Walkable to downtown Kelowna's shops, restaurants, and cultural district</li>
      <li>Served by BC Transit; proximity to a frequent-transit corridor is a key factor in the SSMUH unit ceiling — confirmed in Phase 2</li>
      <li>A designated Heritage Conservation Area (since 1998): mature trees, wide boulevards, and heritage character that shape what can be built</li>
      <li>Note: heritage guidelines, lot dimensions, and the property's strata status can each shape what is buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# zoning section 2 table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RU1 — Large Lot Housing (Kelowna Zoning Bylaw No. 12375), within the Abbott Street Heritage Conservation Area. Confirm exact parcel zoning in Phase 2.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Under BC's SSMUH framework, serviced residential lots inside the urban containment boundary are pre-zoned for multiple units. Unit count scales with lot area and transit proximity (a 6-unit allowance generally requires a larger lot near frequent transit).</td></tr>
    <tr><td>Recent Changes</td><td>BC Bill 44 (SSMUH, 2023) — implemented by Kelowna in Zoning Bylaw No. 12375 (adopted March 18, 2024) — pre-zoned RU1/RU2/RU3/RU5 and eligible MF1 parcels for 3–4 units (up to 6 near frequent transit). The Heritage Conservation Area guidelines and any Transit-Oriented Area overlay interact with this — confirm the governing rules per parcel.</td></tr>
    <tr><td>Permitted Uses</td><td>SSMUH housing forms (e.g. duplex, triplex, fourplex, and — where thresholds are met — up to six units), subject to the Heritage Conservation Area guidelines and a heritage-alteration permit where required. Figures to be confirmed against the current bylaw in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>LIKELY — NEEDS REVIEW</strong>; the heritage overlay and the property's apparent strata / multi-unit status must be confirmed first. Proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# "what this means for you" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on a qualifying SSMUH lot, no rezoning — subject to the heritage guidelines that apply here</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot area and frequent-transit thresholds are met</li>
      <li><strong>Secondary &amp; Garden Suites:</strong> a secondary suite and/or a detached garden suite can add gentle density on a qualifying lot</li>
      <li><strong>Heritage-sensitive infill:</strong> in the Abbott Street Heritage Conservation Area, form and character follow the HCA guidelines and a heritage-alteration permit may be required. Confirm in Phase 2.</li>'''))

# TIME-SENSITIVE — three cards (Ontario-specific -> BC-relevant, all hedged)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build generally before 2031</small></div><div class="dx">The federal government's 100% rebate of the 5% GST on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is what captures it — confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Heritage Conservation Area — Confirm First<br><small>before any design</small></div><div class="dx">1585 Abbott Street lies in the Abbott Street Heritage Conservation Area, and Kelowna is actively reviewing its HCA guidelines against the provincial SSMUH / Transit-Oriented Area rules. What is buildable — and whether a heritage-alteration permit is required — must be confirmed against the current guidelines before committing to a design.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">Under SSMUH the municipality cannot require off-street parking minimums on qualifying lots. CMHC policy can change at any time and affects financing — applying early reduces risk. Confirm in Phase 2.</div></div>'''))

# Section 3 — green "not required" box -> hedged amber
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-amber"><b>To be confirmed for this property.</b><br><span class="sub">SSMUH permissions are as-of-right on qualifying RU1 lots under Zoning Bylaw No. 12375, but this property sits in the Abbott Street Heritage Conservation Area and presents as an existing strata / multi-unit building — a heritage-alteration permit and confirmation of the redevelopment path may be required before any build. Confirm in Phase 2.</span></div>'))

# Section 3 — comparison table Ontario-specific rows
R.append(('<tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '<tr><td>Public hearing exposure</td><td class="g">Reduced (as-of-right SSMUH)</td><td class="n">Public hearing likely</td></tr>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Zoning Bylaw No. 12375 + HCA guidelines</td><td class="n">A new site-specific rezoning</td></tr>'))

# Section 3 — "also permitted" twocard
R.append(('''  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="barhead" style="text-align:left;">Also enabled under SSMUH (subject to confirmation)</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Multi-unit infill</div>On a qualifying RU1 lot, Kelowna's SSMUH provisions (Zoning Bylaw No. 12375) enable 3–4 units — up to six near frequent transit — without a rezoning.</div>
    <div class="card2"><div class="ct">Secondary / garden suite</div>A secondary suite and/or a detached garden suite may be added on a qualifying lot, subject to the heritage guidelines. Confirm in Phase 2.</div>
  </div>'''))

# Section 3 — "what this means for X" + amber garage note
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 1585 Abbott Street</div>
  <p>Kelowna's SSMUH provisions allow qualifying RU1 lots to add units without a rezoning. For this property, two things shape the path: it lies within the Abbott Street Heritage Conservation Area (where the HCA guidelines and a possible heritage-alteration permit apply), and it presents as an existing strata / multi-unit building (where any redevelopment is a strata and land-title question, not a simple single-lot infill). This assessment reflects the rules in force at the date of this report and is subject to confirmation of the parcel's zoning, heritage status, and ownership structure.</p>
  <div class="co-amber"><b>Two items to confirm before relying on any configuration.</b><br><span class="sub">(1) The parcel's exact zoning and whether the Heritage Conservation Area guidelines require a heritage-alteration permit; (2) the property's ownership / strata structure and the applicable redevelopment path. Both are confirmed in Phase 2.</span></div>'''))

# Section 4 — Development Options (keep massing images, swap headers + copy)
R.append(('<div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="oh">Option A — Triplex / Fourplex under SSMUH (3–4 units)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">On a qualifying RU1 lot, SSMUH enables a triplex or fourplex as the baseline entitlement — 3–4 units without a rezoning or public hearing. Buildable size is governed by the zoning bylaw's setbacks, height, site coverage, and floor-area rules, and — because this property is in the Abbott Street Heritage Conservation Area — by the HCA form-and-character guidelines, which may require a heritage-alteration permit. Confirm the parcel's zoning, lot area, and heritage requirements in Phase 2. (Illustrative massing; not a site-specific design.)</div>'''))
R.append(('<div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Highest-Density Path</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Where the lot area and frequent-transit thresholds are met, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without a rezoning. Confirming the lot's area and its distance to a frequent-transit stop is the first gating step, since that is what unlocks the six-unit tier. No off-street parking minimum applies on a qualifying SSMUH lot. In this heritage conservation area the six-unit form must still satisfy the HCA guidelines — confirm in Phase 2. (Illustrative massing; not a site-specific design.)</div>'''))
R.append(('<div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="oh">Option C — Heritage-Sensitive / Strata Redevelopment Path</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Because 1585 Abbott Street presents as an existing strata / multi-unit building in a heritage conservation area, the realistic redevelopment path is not a single-lot infill but a heritage-sensitive and strata / land-title exercise. That means confirming the ownership structure (single owner vs. strata corporation), any strata wind-up requirements, and the HCA guidelines / heritage-alteration permitting that govern alterations on this street. This is the essential first step before any of the SSMUH options above can be relied on. Confirm ownership, strata status, and heritage requirements in Phase 2.</div>'''))

# Section 5 — goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multi-Unit under SSMUH (subject to heritage &amp; strata confirmation)</div>
  <p>1585 Abbott Street is an RU1 property in Kelowna's Abbott Street Heritage Conservation Area, where BC's SSMUH rules (Zoning Bylaw No. 12375) enable 3–4 units — up to six near frequent transit — as-of-right on a qualifying lot. <strong>Because the property sits in a Heritage Conservation Area and presents as an existing strata / multi-unit building, the recommended next step is to confirm the parcel's zoning, heritage requirements, and ownership structure before committing to a configuration.</strong> These figures were researched from public sources for Kelowna and must be double-checked in Phase 2.</p>'''))

# Section 7 — inject gated grant rows at the GATED_GRANTS_ROWS marker
GRANTS_MARKER = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->'''
GRANTS_ROWS = '''    <!-- Tiered render: project scope is "Other" (unresolved), so each program
         shows the tier/threshold that unlocks it rather than claiming availability.
         Only BC-eligible + nationwide-federal programs from config/programs.json. -->
    <tr><td>Provincial (BC)</td><td>SSMUH as-of-right density (Bill 44)</td><td>Not a grant — a zoning entitlement. Kelowna's Zoning Bylaw No. 12375 pre-zones qualifying RU1 lots for 3–4 units (up to 6 near frequent transit) without rezoning. Source: BC Housing Statutes (Residential Development) Amendment Act, 2023 (Bill 44). Heritage Conservation Area guidelines apply here — confirm in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>At 4+ self-contained rental units (90%+ long-term rental; construction generally before 2031): 100% rebate of the 5% federal GST on a new purpose-built rental project. Applies in BC. Source: Federal PBRH rebate. Confirm eligibility in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>At 5+ rental units: preferred multi-unit mortgage insurance with reduced premiums and extended amortization for qualifying rental projects. Source: CMHC MLI Select product terms. Confirm in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>At a minimum $1M loan (gated on project budget in Phase 2, not unit count): low-cost construction financing for purpose-built rental. Source: CMHC ACLP program terms. Confirm in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC tax framework (GST / PST)</td><td>BC applies the 5% federal GST; the federal purpose-built rental rebate applies to 4+ unit rental in BC as elsewhere. PST applies to materials but not most labour. Source: BC tax framework. Structure with a BC tax advisor in Phase 2.</td></tr>'''
R.append((GRANTS_MARKER, GRANTS_ROWS))

# Section 8 — summary
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1585 Abbott Street is an RU1 property in Kelowna's Abbott Street Heritage Conservation Area. Under BC's SSMUH framework (Bill 44, implemented via Zoning Bylaw No. 12375, adopted March 18, 2024), qualifying RU1 lots are pre-zoned for <strong>3–4 units as-of-right — up to six near frequent transit</strong>, without a rezoning or public hearing. The zoning rules in this report were researched from public sources for Kelowna and should be double-checked before the call.</p>
  <ul>
    <li><strong>The SSMUH Opportunity:</strong> the single most valuable first step is confirming (a) the parcel's exact zoning and lot area, (b) whether the Heritage Conservation Area guidelines require a heritage-alteration permit, and (c) the property's ownership / strata structure — each of which shapes what can actually be built here.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

print("--- leftover scan ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "johneeraj",
          "654-2025", "474-2023", "569-2013", "Ontario", "Bill 185", "6+1", "4+1",
          "Gerrard", "TTC", "Greenwood", "OLT", "garage"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done. fails:", fails, "-> wrote", OUT)
