import re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_haldimand.html")

s = open(SRC).read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">238 MacCrae Drive<span>Caledonia, ON</span></div>'))
# property barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">238 MacCrae Drive, Caledonia, ON&nbsp;&nbsp;N3W 1K6</div>'))
# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>238 MacCrae Drive, Caledonia, ON&nbsp;&nbsp;N3W 1K6</td></tr>
    <tr><td>Name</td><td>Preston Cooke</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite / accessory dwelling unit (ADU) for rental income</td></tr>'''))
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
'''    <tr><td>Municipality</td><td>Haldimand County (Caledonia)</td></tr>
    <tr><td>Community</td><td>Caledonia (Grand River)</td></tr>
    <tr><td>Servicing</td><td>Municipal water &amp; wastewater (serviced urban settlement area)</td></tr>
    <tr><td>Waste Collection</td><td>Haldimand County curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Haldimand County Comprehensive Zoning By-law HC 1-2020 (updated 2025)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite / ADU (primary); optional interior suite toward up to 3 units</td></tr>'''))
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
    238 MacCrae Drive is in Caledonia — the largest community in Haldimand County, set on the Grand River in a serviced, established residential area:
    <ul>
      <li>Caledonia is Haldimand County's principal service centre (2021 population ~12,000), with shops, schools, parks and Grand River access</li>
      <li>Full municipal water and wastewater servicing — the provincial criterion for as-of-right additional residential units</li>
      <li>Established single-detached subdivision streets — the kind of stock that rents steadily and holds value</li>
      <li>Commuter access toward Hamilton and Highway 6, supporting rental demand</li>
      <li>Illustrative context only, not a valuation. Any overlays (e.g. Grand River / hazard lands) are confirmed in Phase 2.</li>
    </ul>'''))
# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Urban Residential (Haldimand County Zoning By-law HC 1-2020) — exact residential zone category confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; wastewater) within a settlement area — the provincial criteria for as-of-right additional residential units. Caledonia is a fully serviced settlement area.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Haldimand County's Zoning By-law HC 1-2020 addresses secondary suites and additional units at Section 4.55.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and a detached secondary suite (garden suite / ADU) are permitted, subject to Haldimand's Section 4.55 standards — a detached secondary suite is limited to 5 m in height, with size and parking provisions in that section. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))
# what this means
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite (ADU):</strong> a self-contained home in your rear yard — your primary goal</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (e.g. a basement suite), which can be paired with the garden suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional units, subject to Haldimand's site standards</li>'''))
# time-sensitive item 1 (HST -> DC exemption for ARUs)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>''',
'''    <div class="d"><div class="dt">DC Exemption for ARUs — Already in Effect</div><div class="dx">Under Ontario's Bill 23, the first two additional residential units on a serviced residential lot are exempt from municipal development charges — a real per-unit saving on a detached garden suite. Haldimand County's Development Charges By-law reflects this exemption. It applies automatically to a compliant additional unit; confirmed for your project in Phase 2.</div></div>'''))
# time-sensitive item 2 (Toronto DC waiver -> rental rebate hedged)
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">If Built for Rental — Tax Rebates</div><div class="dx">A newly built rental suite may qualify for the federal GST/HST New Residential Rental Property rebate. The enhanced purpose-built rental rebate targets projects of four or more units, so a single suite is assessed under the standard rebate — the amount and eligibility are confirmed in Phase 2. No figures are stated here until your structure is set.</div></div>'''))
# section 3 rezoning: co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A detached garden suite (ADU) is permitted as-of-right on a serviced residential lot under Ontario\'s Bill 23 and Haldimand County Zoning By-law HC 1-2020 — no rezoning required.</div>'))
# comparison table last row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Zoning By-law HC 1-2020</td><td class="n">A new site-specific by-law</td></tr>'))
# twocard
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Detached garden suite</div>Under Bill 23 and HC 1-2020 (Section 4.55), a detached secondary suite is permitted as-of-right on a serviced residential lot — no rezoning required.</div>
    <div class="card2"><div class="ct">Up to three units</div>The lot may also support an interior secondary suite in addition to the garden suite — up to three units in total, subject to Haldimand's site standards.</div>
  </div>'''))
# what this means for the property
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 238 MacCrae Drive</div>
  <p>Because a detached garden suite is permitted under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment was researched live against Haldimand County's current published sources for the date of this report and is subject to technical review of site conditions in Phase 2.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2: the exact residential zone category and the lot's servicing / setback fit for a detached suite.</b><br><span class="sub">Section 4.55 sets the size, height (5 m for a detached secondary suite) and parking provisions; the buildable envelope is finalized against your lot.</span></div>'''))
# option A header + body
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. Under Haldimand's Section 4.55, a detached secondary suite is limited to 5 m in height, with size and parking provisions set in that section — the exact buildable envelope is confirmed in Phase 2. As an additional residential unit, it is exempt from municipal development charges under Bill 23.</div>'''))
# option B header + body
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Garden Suite + Interior Secondary Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior secondary suite in the existing home (for example, a basement apartment) — a route to as many as three income units on the lot under Bill 23, where the property allows. This maximizes cash flow while keeping the property in your hands. Eligibility, unit sizes and parking are confirmed against Section 4.55 in Phase 2.</div>'''))
# option C header + body
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Servicing &amp; Rear-Yard Fit</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A detached suite needs a servicing connection (water, sanitary and hydro) and must meet rear- and side-yard setbacks and any overlay constraints — for example Grand River / hazard-land or floodplain limits near the river. Caledonia's full municipal servicing is an advantage here. Confirming your lot's servicing route, setbacks and any overlays is an essential first step, finalized in Phase 2 before design and financing proceed.</div>'''))
# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>238 MacCrae Drive is a serviced residential lot in Caledonia where, under Bill 23 and Haldimand County Zoning By-law HC 1-2020, a detached garden suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The garden suite is the clear primary recommendation</strong>, with an interior secondary suite as an optional path to a third income unit.</p>'''))
# grants table header -> header + gated rows
R.append(('    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>',
'''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>The first two additional residential units on a serviced residential lot are exempt from municipal development charges under Ontario's More Homes Built Faster Act (Bill 23). Haldimand County's Development Charges By-law reflects this — a meaningful per-unit saving on a detached garden suite, applied automatically to a compliant unit. Confirmed in Phase 2. (Source: Government of Ontario, Bill 23; Haldimand County Development Charges By-law.)</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>May apply to a newly constructed unit built for long-term rental. The enhanced purpose-built rental rebate targets projects of four or more units, so a single suite is assessed under the standard rebate — amount and eligibility confirmed in Phase 2. No figure is stated until your structure is set. (Source: Canada Revenue Agency.)</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where the new suite houses an eligible relative — a senior 65+ or an adult eligible for the Disability Tax Credit — a refundable credit of 15% on up to $50,000 of eligible construction costs may apply. This condition, and eligibility, are confirmed in Phase 2. (Source: Canada Revenue Agency.)</td></tr>'''))
# summary current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>238 MacCrae Drive is a serviced residential lot in Caledonia, Haldimand County. Under Ontario's Bill 23 and Haldimand County Zoning By-law HC 1-2020, up to <strong>three residential units are permitted as-of-right</strong> — including the detached garden suite you're after — with no rezoning required, subject to the County's Section 4.55 site standards.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds a rental income stream while you keep the property, using land you already own — the exact size and siting are confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# imagery block: no licensed source -> remove placeholder boxes, keep one honest line
img_pat = re.compile(r'<div class="imgrow" style="margin-top:0;">.*?Imagery: source and licence inserted at generation\.</div>', re.S)
n_img = len(img_pat.findall(s))
if n_img != 1:
    print(f"[FAIL imagery x{n_img}]")
    fails += 1
else:
    s = img_pat.sub('<div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>', s)

open(OUT, "w").write(s)

# leftover check — Toronto/master data that must NOT survive
leftovers = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "Arockiaraj",
             "654-2025", "474-2023", "569-2013", "Bill 185", "6+1", "4+1", "303 ",
             "M4L 3B5", "Gerrard", "TTC", "Danforth", "Briarstone", "houseplex",
             "Greenwood", "johneeraj", "$80,000 per unit", "garage"]
print("--- leftover scan ---")
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done. fails={fails}. bytes={len(s)}")
