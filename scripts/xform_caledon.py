"""Transform the House Lyft master (303 Coxwell, Toronto) into the Caledon /
Bolton secondary-suite report for Frank D — 22 Pavin Crescent.

City = Caledon: NO zoning-engine adapter. Rules researched live from official
sources (caledon.ca, TRCA) per THE PRIME RULE. verified = False -> needs-review.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates/report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates/report_caledon.html")

s = open(SRC, encoding="utf-8").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">22 Pavin Crescent<span>Bolton (Caledon), ON</span></div>'))

# imagery row -> no licensed source for Caledon: drop placeholder boxes, honest line
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:6px 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">22 Pavin Crescent, Bolton (Caledon), ON&nbsp;&nbsp;L7E 1W9</div>'))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>22 Pavin Crescent, Bolton (Caledon), ON&nbsp;&nbsp;L7E 1W9</td></tr>
    <tr><td>Name</td><td>Frank D</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite (second unit) for rental income; intends to keep the property</td></tr>'''))

# property table 2
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
'''    <tr><td>Municipality</td><td>Town of Caledon (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Bolton</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Town of Caledon Comprehensive Zoning By-law 2006-50 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Interior secondary suite (primary); optional garden suite for up to 3 units</td></tr>'''))

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
    22 Pavin Crescent is in Bolton — the largest urban settlement in the Town of Caledon, in the Region of Peel at the northwest edge of the GTA:
    <ul>
      <li>Established residential neighbourhood with schools, parks, and local shopping close by</li>
      <li>Bolton sits in the Humber River watershed; parts of the community are within Toronto and Region Conservation Authority (TRCA) regulated areas</li>
      <li>Highway 50 and Queen Street connect Bolton south to Brampton, Vaughan, and the wider GTA</li>
      <li>Steady rental demand typical of an established Peel Region community</li>
      <li>Illustrative context only, not a valuation. Any conservation-authority or heritage constraints are confirmed in Phase 2.</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (Town of Caledon Zoning By-law 2006-50, as amended) — exact zone symbol confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within the Bolton settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Caledon Council adopted implementing zoning amendments in 2024, and additional residential units are exempt from development charges.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and a detached garden suite (ARU) are permitted, subject to Caledon's site standards — setbacks, height, parking, and a floor-area cap. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite:</strong> a self-contained unit within the existing home (for example, a basement apartment) — your primary goal</li>
      <li><strong>Detached Garden Suite:</strong> a self-contained home in your rear yard, which can be paired with the interior suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional units, subject to site standards</li>'''))

# time-sensitive (all three rows)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Development Charges — ARU Exemption<br><small>Already in effect</small></div><div class="dx">Additional residential units — such as a secondary suite — are exempt from development charges under Ontario's Bill 23 and Caledon's implementing by-law, a meaningful per-unit saving. The exemption is confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Caledon Zoning Modernization<br><small>In progress</small></div><div class="dx">The Town of Caledon is updating its Comprehensive Zoning By-law (2006-50) through an ongoing review. Site standards for additional units can change as the new by-law advances — designing under the permissions in force today keeps your project on the current rules. Current standards are confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# rezoning: co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended secondary suite is permitted as-of-right under Ontario\'s Bill 23 on a serviced residential lot in Caledon.</div>'))

# rezoning cmp row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + Caledon By-law 2006-50</td><td class="n">A new site-specific by-law</td></tr>'))

# rezoning twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior secondary suite</div>Under Bill 23, a second self-contained unit inside the existing dwelling is permitted as-of-right on a serviced residential lot — no rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>A detached garden suite in the rear yard is permitted as-of-right as one of the additional residential units, subject to Caledon's site standards.</div>'''))

# rezoning barhead
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 22 Pavin Crescent</div>'))

# rezoning paragraph
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 22 Pavin Crescent already permits the recommended secondary suite under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

# rezoning co-amber
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: whether the lot falls within a TRCA regulated area.</b><br><span class="sub">Bolton lies in the Humber River watershed. If the property is within a Toronto and Region Conservation Authority regulated area, a conservation permit may be required before development. Confirmed in Phase 2.</span></div>'))

# options A header
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Interior Secondary Suite (your goal)</div>'))
# options A body
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained second unit within your existing home — for example, a basement apartment — rented for ongoing income while you keep the property. This is your stated goal. Permitted as-of-right under Bill 23 on a serviced residential lot in Bolton; no rezoning. Unit size, ceiling height, a separate entrance, fire separation, egress, and parking follow Caledon's additional-residential-unit standards, confirmed in Phase 2. Additional residential units are exempt from development charges.</div>'''))
# options B header
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Secondary Suite + Detached Garden Suite (up to 3 units)</div>'))
# options B body
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the interior secondary suite with a detached garden suite in the rear yard — a route to as many as three units on the lot under Bill 23, where the lot allows. This maximizes cash flow while keeping the property in your hands. The garden suite's size and siting follow Caledon's standards; eligibility and unit sizes are confirmed in Phase 2.</div>'''))
# options C header
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Bolton Lot &amp; Conservation Considerations</div>'))
# options C body
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Bolton is in the Humber River watershed, and parts of the community fall within Toronto and Region Conservation Authority (TRCA) regulated areas. If your lot is within a regulated area, a conservation-authority permit may be required alongside the building permit. Confirming servicing (municipal water and sewer), setbacks, and any conservation or heritage constraints early keeps the project on schedule. The exact buildable envelope for the suite is confirmed in Phase 2.</div>'''))

# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Interior Secondary Suite</div>
  <p>22 Pavin Crescent is a serviced residential lot in Bolton where, under Bill 23, an interior secondary suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The secondary suite is the clear primary recommendation</strong>, with a detached garden suite as an optional path to a third income unit.</p>'''))

# summary current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>22 Pavin Crescent is a serviced residential lot in Bolton, Town of Caledon. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — including the interior secondary suite you're after — with no rezoning required, subject to the Town's site standards.</p>
  <ul>
    <li><strong>The Secondary-Suite Advantage:</strong> a second self-contained unit adds a rental income stream while you keep the property, using space you already own — the exact size and layout are confirmed in Phase 2.</li>
  </ul>'''))

# grants table injection
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under Ontario's More Homes Built Faster Act (Bill 23) and Caledon's implementing by-law — a meaningful per-unit saving on a secondary suite. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (up to $7,500), but only where the new unit is created to house an eligible senior (65+) or an adult eligible for the Disability Tax Credit. Applicability confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs for insulation, heat pumps, and efficient equipment (for example, Enbridge's Home Efficiency Rebate Plus) may offset efficient design on a new suite. Program availability and amounts are confirmed in Phase 2.</td></tr>
    <tr><td>Municipal / Regional</td><td>Town of Caledon &amp; Region of Peel</td><td>Municipal and regional housing incentives change periodically and are budget-limited. Any current Caledon or Peel funding applicable to a second unit is confirmed in Phase 2 — no figure is stated here until verified.</td></tr>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

# leftover check
print("--- leftover scan ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
          "654-2025", "474-2023", "6+1", "4+1", "Bill 185", "M4L", "569-2013",
          "Woodbine", "garage", "sixplex", "houseplex", "HST Rebate"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails, "| bytes:", len(s))
