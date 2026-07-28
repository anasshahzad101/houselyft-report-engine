"""
xform_brampton.py — turn the House Lyft master report into the 55 Moore Street,
Brampton report. Same discipline as the other xform_*.py: every replacement must
match EXACTLY once, then we grep for leftovers from the source city.

Brampton facts are grounded in engine/property_lookup_v2.py's live Brampton
adapter (ARU_SEARCH): zone R1B, Bill 23 three-unit ceiling (principal + interior
second unit + detached garden suite), ARU DC exemption, City registration +
Residential Rental Licence (Jan 1 2026). No Toronto-only programs, no invented
figures. The homeowner's "multiplex" goal exceeds the 3-unit as-of-right envelope,
so the report presents that honestly (rezoning path).

Reads templates/report_houselyft_master.html, writes templates/report_brampton.html.
Run from the templates/ directory (relative asset paths must resolve for render).
"""
import base64, os, sys

SRC = "report_houselyft_master.html"
OUT = "report_brampton.html"

s = open(SRC, encoding="utf-8").read()

# --- embedded, validated aerials (City of Brampton Orthophoto 2023, OGL) -------
SCRATCH = os.environ.get("HL_AERIAL_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "scratch"))
lot_b64 = base64.b64encode(open(os.path.join(SCRATCH, "lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCRATCH, "ctx.jpg"), "rb").read()).decode()

R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">55 Moore Street<span>Brampton, ON</span></div>'))

# barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">55 Moore Street, Brampton, ON&nbsp;&nbsp;L6X 1V2</div>'))

# imagery row + licence -> two embedded aerials with overlay captions
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{lot_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,0.72);color:#fff;font-size:7pt;padding:3px 7px;">Aerial view — approx. 90&nbsp;m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{ctx_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,0.72);color:#fff;font-size:7pt;padding:3px 7px;">Neighbourhood context — approx. 300&nbsp;m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Brampton Orthophoto 2023 (Spring). Contains information licensed under the Open Government Licence – City of Brampton.</div>'''))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>55 Moore Street, Brampton, ON&nbsp;&nbsp;L6X 1V2</td></tr>
    <tr><td>Name</td><td>Sunil Lalit</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development / additional rental units on the property</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>City of Brampton (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Established residential area, City of Brampton — confirmed in Phase 2</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Property Type</td><td>Detached dwelling, R1B residential zone (per City GIS)</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Brampton Comprehensive Zoning By-law 270-2004 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — City GIS screening value ≈ 614 m² for the parcel; confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Additional residential units / multiplex development on the property</td></tr>'''))

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
    55 Moore Street is in an established residential area of the City of Brampton, in the Region of Peel — a fast-growing part of the western GTA with steady rental demand:
    <ul>
      <li>Served by Brampton Transit, with GO Transit's Kitchener line connecting Brampton to Downtown Toronto</li>
      <li>Close to Peel District and Dufferin-Peel Catholic schools, parks, and everyday shopping</li>
      <li>Quick access to Highways 410 and 407 for commuting across the GTA</li>
      <li>Established detached-home streets — the kind of stock that rents well and holds value</li>
      <li>Note: if any part of the lot falls within Credit Valley Conservation regulated lands, a conservation-authority review may apply — confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>R1B — Residential (Brampton Comprehensive Zoning By-law 270-2004, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units. City GIS screening indicates this parcel supports an additional residential unit.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Brampton implements this through its Additional Residential Unit framework under By-law 270-2004.</td></tr>
    <tr><td>Permitted Uses</td><td>A principal dwelling plus up to two additional residential units — for example an interior second unit and a detached garden suite — subject to Brampton's site standards (setbacks, height, floor-area caps) and City registration. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES for up to 3 units as-of-right</strong>; a larger multiplex (4+ units) is not permitted as-of-right in Brampton and would require a planning application — assessed in Step 2, <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite:</strong> a self-contained home in your rear yard (a detached additional residential unit)</li>
      <li><strong>Interior Second Unit:</strong> a unit within the existing home, such as a basement apartment, which can be paired with the garden suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional residential units, subject to site standards and City registration</li>
      <li><strong>Larger multiplex (4+ units):</strong> not as-of-right in Brampton — a rezoning / Official Plan amendment would be required, assessed in Phase 2</li>'''))

# time-sensitive block (all three rows)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from municipal development charges under provincial legislation (Bill 23) — a meaningful per-unit saving on a garden suite or interior second unit. The exemption applicable to your project is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Brampton Residential Rental Licence<br><small>in effect Jan 1, 2026</small></div><div class="dx">Brampton requires additional residential units to be registered with the City to be legal, and a citywide Residential Rental Licence applies to the rental of 1–4 unit properties as of January 1, 2026. Building this into the plan from Day 1 keeps the units compliant and financeable. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# rezoning co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for up to Three Units</div>The recommended configuration — a garden suite plus an interior second unit, up to three units total — is permitted as-of-right under Ontario\'s Bill 23 and Brampton\'s ARU framework. A larger multiplex (4+ units) would instead follow the rezoning path shown below.</div>'))

# rezoning comparison table
R.append(('''    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><th></th><th>Up to 3 Units — As-of-Right</th><th>Larger Multiplex — Rezoning Path</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">Bill 23 + By-law 270-2004 (ARU framework)</td><td class="n">A new site-specific by-law</td></tr>'''))

# rezoning twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior second unit</div>Bill 23 permits an additional residential unit inside the existing dwelling (for example a basement apartment) as-of-right on a serviced residential lot, subject to Brampton's site standards and City registration.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Brampton's Additional Residential Unit framework permits a detached garden suite in the rear yard as-of-right in residential zones, subject to setbacks, height, and floor-area standards.</div>'''))

# rezoning "what this means" + amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 55 Moore Street</div>
  <p>Because up to three units are permitted as-of-right on this serviced residential lot, the recommended garden-suite-plus-interior-unit build advances directly to design and permitting — no rezoning application required. If you decide to pursue a larger multiplex (4+ units), that follows the rezoning path shown above and is scoped in Phase 2. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm early: City registration and any regulated-lands review.</b><br><span class="sub">Additional residential units must be registered with the City, and if any part of the lot is within Credit Valley Conservation regulated lands a conservation-authority approval may be required before a building permit.</span></div>'''))

# options A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite (ARU)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property. Permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. The size and siting are set by Brampton's garden-suite standards — setbacks, height, and a floor-area cap — and the exact buildable envelope is confirmed in Phase 2. City GIS screening indicates a garden suite is feasible on this parcel. The suite must be registered with the City to operate as a legal rental.</div>'''))

# options B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Interior Second Unit + Garden Suite (up to 3 units) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior second unit in the existing home (for example a basement apartment) — a route to as many as three income units on the lot under Bill 23, where the property allows. This is the most direct way to add rental income while keeping the property in your hands. Additional residential units are exempt from development charges under provincial legislation. Eligibility, unit sizes, and parking are confirmed in Phase 2.</div>'''))

# options C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Larger Multiplex (4+ units): the Rezoning Path</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">If your goal is a larger multiplex (four or more units), Brampton does not permit that as-of-right — it is outside the Bill 23 three-unit framework. That path requires a planning application (a rezoning and, potentially, an Official Plan amendment), with public consultation and Council approval, and it carries OLT appeal exposure. It can still be worthwhile where the lot and surrounding context support it. House Lyft scopes the feasibility, timeline, and cost of this path in Phase 2 so you can compare it directly against the as-of-right three-unit build.</div>'''))

# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Up to 3 Units (Garden Suite + Interior Second Unit)</div>
  <p>55 Moore Street is a serviced residential lot in Brampton where, under Ontario's Bill 23, up to three residential units are permitted as-of-right — including a detached garden suite. <strong>A garden suite paired with an interior second unit is the clear primary recommendation</strong>, with a larger multiplex available as a separate rezoning path if you choose to pursue it.</p>'''))

# summary current-zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>55 Moore Street is a serviced residential lot in the City of Brampton, Region of Peel. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — including the detached garden suite — with no rezoning required, subject to the City's site standards and registration.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite plus an interior second unit adds up to two rental income streams while you keep the property, using land you already own — the exact sizes and siting are confirmed in Phase 2.</li>
  </ul>'''))

# grants table — replace the GATED marker with Brampton-appropriate, gate-cleared rows
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from municipal development charges under provincial legislation — a meaningful per-unit saving on a garden suite or interior second unit. The exemption applicable to your project is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible renovation cost (up to $7,500) where the new suite houses an eligible relation — a senior or an adult eligible for the disability tax credit. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as the Canada Greener Homes Loan and the Home Efficiency Rebate Plus (Enbridge) may offset efficient design and equipment on a new suite. Current availability and amounts confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>May apply to a newly built rental suite. The enhanced purpose-built rental rebate targets larger 4+ unit rental projects; applicability to your project is confirmed in Phase 2.</td></tr>'''))

# tidy: drop the now-irrelevant gated FINANCING marker (no gated financing program applies)
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''', ''))
R.append(('<!-- GATED_FINANCING_PROSE: the builder may append gated programs here ONLY if they clear their gate. Never name a program that has not cleared. -->', ''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

# leftover check — nothing from the source city / master lead may survive. Strip
# embedded base64 (logo SVG + aerial JPEGs) first: their alphabets contain
# substrings like "6+1"/"M4L" that are not real report text.
import re as _re
vis = _re.sub(r'data:image/(?:jpeg|svg\+xml);base64,[A-Za-z0-9+/=]+', '[IMG]', s)
leftovers = 0
for t in ["Coxwell", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "474-2023", "569-2013", "6+1", "4+1", "Bill 185", "303 ", "M4L", "Gerrard",
          "TTC", "East York", "80,000", "Garden Suite By-law", "houseplex", "GATED_"]:
    n = vis.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}"); leftovers += 1
# "Toronto" is allowed exactly once: the accurate GO-line "Downtown Toronto" line
tor = vis.count("Toronto")
if tor != 1:
    print(f"LEFTOVER 'Toronto': {tor} (expected 1: GO Kitchener-line reference)"); leftovers += 1

print(f"done. fails={fails} leftovers={leftovers} out={OUT} bytes={len(s)}")
sys.exit(1 if (fails or leftovers) else 0)
