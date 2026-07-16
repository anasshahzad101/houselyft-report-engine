# -*- coding: utf-8 -*-
"""Transform the master report into the 201 Margaret Avenue, Winnipeg report.
Winnipeg has no city adapter -> zoning researched live (report-needs-review).
Every replacement must match exactly once; a leftover grep guards against
Toronto/Coxwell data surviving into the Winnipeg report."""
import io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "templates", "report_winnipeg.html")
s = io.open(PATH, encoding="utf-8").read()
R = []

# --- cover ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">201 Margaret Avenue<span>Winnipeg, MB</span></div>'))

# --- property details barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">201 Margaret Avenue, Winnipeg, MB&nbsp;&nbsp;R2V 1T3</div>'))

# --- imagery placeholder -> honest pending line (no licensed Winnipeg source) ---
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8.5pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source for Winnipeg.</div>'''))

# --- property table 1 ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>201 Margaret Avenue, Winnipeg, MB&nbsp;&nbsp;R2V 1T3</td></tr>
    <tr><td>Name</td><td>Mi Singh</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development (as stated at intake); unit count to be confirmed</td></tr>'''))

# --- property table 2 ---
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
'''    <tr><td>Municipality</td><td>City of Winnipeg</td></tr>
    <tr><td>Neighbourhood</td><td>West Kildonan (Margaret Park)</td></tr>
    <tr><td>Community</td><td>Old Kildonan / Mynarski area, north-central Winnipeg</td></tr>
    <tr><td>Waste Collection</td><td>City of Winnipeg curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Winnipeg Zoning By-law No. 200/2006 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (min 325 m² / 3,500 sq ft applies for a detached secondary suite)</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development — up to a fourplex as-of-right; unit count confirmed in Phase 2</td></tr>'''))

# --- neighbourhood spotlight ---
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
    201 Margaret Avenue is in West Kildonan (Margaret Park), an established residential area on the west side of the Red River in north-central Winnipeg:
    <ul>
      <li>Mature, tree-lined residential streets with character homes, parks and riverside pathways — a family-oriented, established community</li>
      <li>Served by Winnipeg Transit along the Main Street and McPhillips corridors (the network moved to a spine-and-feeder Primary Transit Network in June 2025)</li>
      <li>Steady, established rental demand typical of Winnipeg's mature north-end neighbourhoods</li>
      <li>Note: proximity to a frequent-transit route — which governs the 4-storey height allowance — is confirmed per parcel in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential — likely R1 (Single-Family) or R2 (Two-Family) under Winnipeg Zoning By-law No. 200/2006. Exact district confirmed in Phase 2 via the City's Property Map.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot within the City of Winnipeg. Under the 2025 infill-housing amendment (By-law No. 59/2025), duplex, triplex and fourplex forms are permitted on residential lots without rezoning where the built-form rules are met.</td></tr>
    <tr><td>Recent Changes</td><td>Up to <strong>4 dwelling units per residential lot are permitted as-of-right city-wide</strong> — adopted June 26, 2025 (By-law No. 59/2025) under the federal Housing Accelerator Fund and now in force. Within 800 m of a frequent-transit route, a 4-unit building may reach up to 4 storeys. No rezoning or public hearing required.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-unit residential — up to a <strong>four-unit multiplex</strong> as-of-right, subject to Winnipeg's built-form standards (setbacks, height, coverage) and technical review of site conditions. A detached or attached secondary suite is also permitted in R1/R2, subject to the City's standards.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- what this means for you (section 2 list) ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Duplex, Triplex &amp; Fourplex:</strong> Two, three or four self-contained units in a single building — permitted as-of-right under By-law No. 59/2025</li>
      <li><strong>Attached Secondary Suite:</strong> A self-contained unit within the existing home (for example a basement suite), permitted in R1/R2</li>
      <li><strong>Detached (Backyard) Secondary Suite:</strong> A separate suite in the rear yard — permitted in R1/R2 with a single-family dwelling; size, height and parking standards confirmed in Phase 2</li>
      <li><strong>Multiplex Advantage:</strong> Winnipeg levies no development/impact charge, which lowers the cost of adding units compared with most Canadian cities</li>'''))

# --- time-sensitive (first two items; keep the CMHC item) ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>construction must begin before Dec 31, 2030</small></div><div class="dx">The federal enhanced GST Purpose-Built Rental Housing rebate provides a 100% rebate of the 5% federal GST on new purpose-built rental buildings with four or more self-contained units (90%+ long-term rental). Construction must begin by December 31, 2030 and complete by December 31, 2035. Structuring the project as qualifying rental from Day 1 is essential to capture it. Eligibility confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Manitoba Rental Housing Construction Incentive<br><small>available for use before Jan 1, 2031</small></div><div class="dx">Manitoba's Rental Housing Construction Incentive offers a refundable tax credit of up to $8,500 per rental unit (to a maximum of 8% of eligible capital cost), plus $5,000 per affordable unit, for buildings with four or more rental units. The building permit must be dated on or after January 1, 2024, and the credit must be used before January 1, 2031. Confirm eligibility in Phase 2.</div></div>'''))

# --- section 3: co-green ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A multiplex of up to four units is permitted as-of-right under Winnipeg By-law No. 59/2025 — no rezoning is required for the recommended configuration.</div>'))

# --- section 3: comparison table rows ---
R.append(('<tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '<tr><td>Appeal / hearing exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law No. 59/2025</td><td class="n">A new site-specific by-law</td></tr>'))

# --- section 3: twocard ---
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Under By-law No. 59/2025, up to four dwelling units are permitted on a residential lot in Winnipeg without rezoning, subject to the built-form standards.</div>
    <div class="card2"><div class="ct">Rear secondary suite</div>A detached (backyard) secondary suite is permitted in R1/R2 with a single-family dwelling — one per property. Whether it is fully as-of-right or requires conditional-use approval after By-law No. 59/2025 is confirmed in Phase 2.</div>'''))

# --- section 3: barhead + para + amber ---
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 201 Margaret Avenue</div>'))
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <p>Because 201 Margaret Avenue already permits a multiplex of up to four units under existing zoning, no rezoning application is contemplated for the recommended build. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))
R.append(('''  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-amber"><b>One item to confirm: the exact zoning district and any established-area standards for this lot.</b><br><span class="sub">The specific R1/R2 district, the lot dimensions, and whether the parcel is within 800 m of a frequent-transit route (which governs the height allowance) are confirmed in Phase 2 via the City's Property Map.</span></div>'''))

# --- section 4: option A ---
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Four-Unit Multiplex (Fourplex) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A four-unit multiplex (fourplex) on the lot — the maximum permitted as-of-right in Winnipeg under By-law No. 59/2025. No rezoning and no public hearing required if the design meets the City's built-form standards (setbacks, height, coverage). Within 800 m of a frequent-transit route, a four-unit building may reach up to four storeys (~39 ft) — transit proximity confirmed in Phase 2. Winnipeg levies no development or impact charge, and residential parking minimums have been reduced (generally about one space per unit, lower for affordable units). This configuration leads on unit count and rental income while staying fully as-of-right. Final unit mix and sizes are set in Phase 2.</div>'''))

# --- section 4: option B ---
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Triplex or Duplex (Lower-Intensity Multiplex)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A triplex (three units) or duplex (two units) is a lower-intensity path that is also permitted as-of-right under By-law No. 59/2025 — useful if you prefer a smaller build, a phased approach, or a simpler financing structure. Fewer units means lower capital and construction complexity, while still adding rental income on a serviced lot with no development charge and reduced parking requirements. The right tier depends on your capital and cash-flow goals, which we confirm with you in Phase 2.</div>'''))

# --- section 4: option C ---
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Detached (Backyard) Secondary Suite</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A detached (backyard) secondary suite is permitted in R1/R2 with a single-family dwelling — one per property — and can add a self-contained rental unit while you keep the existing home. The City's standards include a minimum lot size of 325 m² (3,500 sq ft), placement in the rear yard, two off-street parking spaces, and a height limit of 4.57 m (15 ft) on grade or 7.62 m (25 ft) above a detached garage. Whether a detached suite is now fully as-of-right or still requires conditional-use approval after By-law No. 59/2025, and whether it can be combined with a multiplex on the same lot, are confirmed in Phase 2.</div>'''))

# --- section 5: development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Four-Unit Multiplex</div>
  <p>201 Margaret Avenue is a serviced residential lot in Winnipeg where, under By-law No. 59/2025, up to four dwelling units are permitted as-of-right — no rezoning required. <strong>A four-unit multiplex (fourplex) is the clear primary recommendation</strong>, with a triplex or duplex as lower-intensity alternatives and a detached secondary suite as an optional additional path. The exact unit count for your project is confirmed with you in Phase 2.</p>'''))

# --- section 7: inject gated grant rows after the header row ---
GRANT_HEADER = '<tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>'
GRANT_ROWS = '''
    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>100% rebate of the 5% federal GST on new purpose-built rental buildings with four or more self-contained units (90%+ long-term rental). Construction must begin by Dec 31, 2030 and complete by Dec 31, 2035. Opens up at the four-unit tier. Eligibility confirmed in Phase 2. (Government of Canada — Enhanced GST Rental Rebate.)</td></tr>
    <tr><td>Provincial</td><td>Manitoba Rental Housing Construction Incentive (RHCI)</td><td>Refundable tax credit up to $8,500 per rental unit (max 8% of eligible capital cost), plus $5,000 per affordable unit, for buildings with four or more rental units. Building permit on or after Jan 1, 2024; credit used before Jan 1, 2031. Opens up at the four-unit tier. Confirmed in Phase 2. (Province of Manitoba.)</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Multi-unit mortgage loan insurance with reduced premiums and longer amortization, scored on affordability, accessibility and energy efficiency. Minimum five rental units — available if the project scales to five or more units (for example a multi-family building via rezoning to an RMF district). Confirmed in Phase 2. (CMHC.)</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-cost construction financing for purpose-built rental, loans from $1,000,000 up to 100% of residential cost. Suited to larger multi-unit projects. Confirmed in Phase 2. (CMHC.)</td></tr>
    <tr><td>Municipal</td><td>No Development / Impact Charge</td><td>Winnipeg levies no development or impact charge — the 2017 Impact Fee was struck down by the courts in 2020 and has not been reinstated. Only standard permit and application fees apply, a meaningful cost advantage versus most Canadian cities. Confirm the current fee schedule in Phase 2.</td></tr>'''
R.append((GRANT_HEADER, GRANT_HEADER + GRANT_ROWS))

# --- section 8: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>201 Margaret Avenue confirms a strong development option. This serviced residential lot in West Kildonan permits up to <strong>four dwelling units as-of-right</strong> under Winnipeg By-law No. 59/2025 (June 2025), adopted under the federal Housing Accelerator Fund. A multiplex can be built with no rezoning, no public hearing, and no Council approval required.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> up to a fourplex without rezoning — and Winnipeg levies no development or impact charge, a cost advantage over most Canadian cities.</li>
  </ul>'''))

# ---- apply with exact-match assertions ----
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print("[FAIL x%d] %r" % (c, old[:70]))
        fails += 1
    else:
        s = s.replace(old, new)

io.open(PATH, "w", encoding="utf-8").write(s)

# ---- leftover guard ----
print("--- leftover check ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "474-2023", "Bill 185", "6+1", "4+1", "Ontario", "TTC", "Gerrard",
          "Woodbine", "garage", "OLT", "garden suite", "houseplex", "569-2013"]:
    n = s.count(t)
    if n:
        print("LEFTOVER %r: %d" % (t, n))
print("done, fails:", fails)
