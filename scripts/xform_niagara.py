"""
xform_niagara.py — turn the House Lyft master into the Niagara Falls report for
5059 Palmer Avenue (Mark Maltman). Niagara Falls has NO verified zoning adapter,
so every municipal fact is either grounded in a live official source
(City of Niagara Falls Zoning By-law No. 79-200; Ontario Bill 23) or hedged with
the "confirmed in Phase 2" treatment. No bylaw numbers, program amounts, or
financing figures are invented. House Lyft prose sections are kept verbatim.

Reads templates/report_houselyft_master.html, writes
templates/report_niagara_5059palmer.html. Each replacement must match exactly
once; a leftover grep guards against source-city bleed-through.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates")
SRC = os.path.join(TPL, "report_houselyft_master.html")
OUT = os.path.join(TPL, "report_niagara_5059palmer.html")

s = open(SRC, encoding="utf-8").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">5059 Palmer Avenue<span>Niagara Falls, ON</span></div>'))

# property-details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">5059 Palmer Avenue, Niagara Falls, ON&nbsp;&nbsp;L2E 3T9</div>'))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>5059 Palmer Avenue, Niagara Falls, ON&nbsp;&nbsp;L2E 3T9</td></tr>
    <tr><td>Name</td><td>Mark Maltman</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development (residential); maximize unit count</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Niagara Falls (Niagara Region)</td></tr>
    <tr><td>Neighbourhood</td><td>Downtown Niagara Falls (per intake)</td></tr>
    <tr><td>Region</td><td>Niagara Region</td></tr>
    <tr><td>Property Type</td><td>Residential (per intake) — confirmed in Phase 2</td></tr>
    <tr><td>Waste Collection</td><td>Niagara Region curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Niagara Falls Zoning By-law No. 79-200</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (subject to zoning)</td></tr>'''))

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
    5059 Palmer Avenue is in the downtown core of Niagara Falls — an established, walkable neighbourhood in the Niagara Region close to the Queen Street district and the Niagara River:
    <ul>
      <li>Walkable to the downtown Queen Street shops, cafés, and services</li>
      <li>Close to the Niagara River, downtown parks, and regional transit connections</li>
      <li>Steady rental demand supported by the regional tourism and hospitality economy</li>
      <li>Established residential streets — character stock that typically rents well</li>
      <li>Illustrative context only, not a valuation. Local specifics are confirmed in Phase 2.</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Niagara Falls Zoning By-law No. 79-200) — exact zone category confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>To qualify for additional residential units as-of-right, the lot must be a serviced residential lot (municipal water &amp; sewer) within the Urban Area Boundary — the provincial criteria under Bill 23. Confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act, 2022), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. The City of Niagara Falls implements additional residential units through Zoning By-law No. 79-200.</td></tr>
    <tr><td>Permitted Uses</td><td>A principal dwelling plus additional residential units (interior and/or detached) are permitted, subject to the City's site standards — setbacks, height, and floor-area limits. A larger multiplex beyond the 3-unit as-of-right envelope is assessed in Phase 2 and may require a zoning by-law amendment.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>Yes — with a defined path.</strong> Up to 3 units as-of-right; a larger multiplex is assessed in Phase 2. Proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means for you
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Additional Residential Units (up to 3 total):</strong> under Bill 23, the property may support the principal dwelling plus additional units — subject to the City's site standards</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (e.g. a basement suite)</li>
      <li><strong>Detached Garden Suite:</strong> a self-contained unit in the rear yard, where the lot and servicing allow</li>
      <li><strong>Larger Multiplex:</strong> a purpose-built multiplex beyond 3 units is explored in Phase 2 and may require a zoning by-law amendment</li>'''))

# time-sensitive
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Niagara Region ARU Incentives<br><small>budget-limited</small></div><div class="dx">Niagara Region has offered affordable-housing incentives for additional residential units (for example, the Niagara Renovates program). These programs are budget-limited and periodically open and close — several were paused or fully subscribed during 2025. Current availability and eligibility are confirmed in Phase 2. These are government-backed financing options, not a guaranteed grant.</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from municipal development charges under provincial legislation (Bill 23) — a meaningful per-unit saving. The exact application to your project is confirmed in Phase 2.</div></div>'''))

# rezoning — co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for up to 3 units</div>Up to three residential units are permitted as-of-right on a serviced residential lot under Ontario\'s Bill 23 — no rezoning required. A larger multiplex may require a zoning by-law amendment; this is assessed in Phase 2.</div>'))

# rezoning — cmp "what governs" row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + By-law No. 79-200</td><td class="n">A new site-specific by-law</td></tr>'))

# rezoning — twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to three units</div>Under Bill 23, a serviced residential lot may support the principal dwelling plus additional residential units — up to three units total — without rezoning, subject to the City's site standards.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>A detached additional residential unit in the rear yard may be permitted under By-law No. 79-200 where the lot and servicing allow — confirmed in Phase 2.</div>'''))

# rezoning — what this means barhead + p
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 5059 Palmer Avenue</div>
  <p>Up to three residential units are achievable as-of-right on a serviced residential lot, so that scenario advances directly to design and permitting with no rezoning. If you pursue a larger multiplex, a zoning by-law amendment may be required — that path, its likelihood, and its timeline are assessed in Phase 2. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# rezoning — co-amber
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>Items to confirm in Phase 2: the lot\'s exact zone, servicing (municipal water &amp; sewer), and whether a larger multiplex needs a zoning by-law amendment.</b><br><span class="sub">These determine how many units are achievable and which path — as-of-right or rezoning — your project follows.</span></div>'))

# options A header
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Up to 3 Residential Units (as-of-right)</div>'))
# options A body
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">The principal dwelling plus additional residential units — up to three units total — permitted as-of-right on a serviced residential lot under Ontario's Bill 23. This can combine an interior secondary suite with a detached garden suite in the rear yard, where the lot and servicing allow. No rezoning required. Unit sizes and siting are set by the City of Niagara Falls' site standards under By-law No. 79-200 (setbacks, height, floor-area limits) and are confirmed in Phase 2. Additional residential units are exempt from development charges under provincial legislation.</div>'''))

# options B header
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Larger Multiplex (assessed in Phase 2)</div>'))
# options B body
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A purpose-built multiplex beyond three units — matching your stated multiplex goal — is explored in Phase 2. Because it exceeds the current as-of-right envelope, it may require a zoning by-law amendment (rezoning) and would be subject to the City's built-form standards and technical site review. Phase 2 assesses the achievable unit count, the likely approval path, and the timeline before any capital is committed. Unit counts and figures are confirmed at that stage.</div>'''))

# options C header
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Servicing &amp; Site Conditions</div>'))
# options C body
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">The number of units a lot can support as-of-right depends on it being within the Urban Area Boundary and connected to municipal water and sewer — the provincial conditions for additional residential units. Confirming servicing, the exact zone under By-law No. 79-200, lot dimensions, and any existing structures on the property is an essential first step, both for design and for financing. These items are verified in Phase 2 before any development path is locked in.</div>'''))

# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex Development</div>
  <p>5059 Palmer Avenue is a residential property in Niagara Falls. Under Ontario's Bill 23, up to three residential units are permitted as-of-right on a serviced residential lot — the recommended first, low-risk step. <strong>A larger multiplex, matching your stated goal, is the primary objective to test in Phase 2</strong>, where the achievable unit count and approval path (as-of-right vs. rezoning) are confirmed.</p>'''))

# grants table
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>Additional Residential Unit — Development Charge Exemption</td><td>Additional residential units are exempt from municipal development charges under Ontario's Bill 23 (More Homes Built Faster Act, 2022) — a meaningful per-unit saving. The exact application to your project is confirmed in Phase 2. Source: Province of Ontario / City of Niagara Falls.</td></tr>
    <tr><td>Regional</td><td>Niagara Region — Affordable Housing Incentives (e.g. Niagara Renovates)</td><td>Niagara Region has offered incentives for additional residential units and affordable rental renovations. These programs are budget-limited and periodically open and close; several were paused or fully subscribed in 2025. Current availability and eligibility are confirmed in Phase 2. Government-backed financing options — not a guaranteed grant. Source: Niagara Region incentive programs.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing Rebate</td><td>A federal rebate on GST/HST for new purpose-built rental housing that meets the program's unit-count and long-term-rental criteria, with a corresponding Ontario provincial component. Eligibility, current rates, and deadlines are confirmed in Phase 2. Source: Government of Canada (CRA / Finance) and Province of Ontario.</td></tr>
    <tr><td>Federal</td><td>CMHC Financing Programs (e.g. MLI Select, Apartment Construction Loan)</td><td>CMHC offers government-backed multi-unit mortgage insurance and construction-financing programs for qualifying purpose-built rental projects. Minimum unit counts and terms apply. Applicability to your project is confirmed in Phase 2. Source: CMHC.</td></tr>'''))

# summary — current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>5059 Palmer Avenue is a residential property in Niagara Falls (Niagara Region). Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> on a serviced residential lot — no rezoning required, subject to the City's site standards under Zoning By-law No. 79-200. A larger multiplex, matching your stated goal, is assessed in Phase 2.</p>
  <ul>
    <li><strong>A defined development path:</strong> up to three units as-of-right is the low-risk first step; the larger multiplex goal is tested in Phase 2, where the achievable unit count and approval path (as-of-right vs. rezoning) are confirmed before any capital is committed.</li>
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

# leftover check — source-city / master bleed-through
leftovers = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
             "johneeraj", "654-2025", "474-2023", "569-2013", "Bill 185",
             "6+1", "4+1", "M4L 3B5", "Garden Suite By-law", "Woodbine"]
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails, "->", OUT)
