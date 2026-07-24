"""xform_mississauga.py — turn the House Lyft master into the 1968 Balsam Avenue,
Mississauga report. Same discipline as the other xform_*.py scripts: every
replacement must match exactly once, then grep for leftovers from the source city.

Grounding (verified, report-ready):
  Zone R3-2 (base R3, Detached Dwellings), Mississauga ZBL 0225-2007.
  Up to 4 units (fourplex) as-of-right city-wide — City Council, Dec 2023.
  Fourth-Unit Incentive: DC + cash-in-lieu-of-parkland grant + permit-fee grant
  for the 4th unit; 25-yr rental, no condo conversion (City of Mississauga).
  No ADU stacking on a fourplex lot; no sixplex. Imagery: licence GAP (no source).
"""
s = open("report_mississauga.html").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">1968 Balsam Avenue<span>Mississauga, ON</span></div>'))

# barhead (property details)
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">1968 Balsam Avenue, Mississauga, ON&nbsp;&nbsp;L5J 1L2</div>'))

# imagery row — no licensed lot-scale source for Mississauga: drop the grey
# placeholder boxes, keep one honest line (per the routine's imagery doctrine).
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:0 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1968 Balsam Avenue, Mississauga, ON&nbsp;&nbsp;L5J 1L2</td></tr>
    <tr><td>Name</td><td>Harry Mangaroo</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count within the as-of-right envelope</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Mississauga (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Clarkson</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Property Type</td><td>Detached dwelling (zoning: R3-2 — Detached Dwellings)</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Mississauga Zoning By-law 0225-2007</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Fourplex (4 units) primary; triplex (3 units) alternative</td></tr>'''))

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
    1968 Balsam Avenue is in Clarkson, an established residential community in southwest Mississauga near Lake Ontario, within the Region of Peel:
    <ul>
      <li>Served by Clarkson GO station on the Lakeshore West line — a direct rail connection toward downtown Toronto</li>
      <li>Close to Clarkson Village shops and services along Lakeshore Road West</li>
      <li>Near the Rattray Marsh Conservation Area and the Lake Ontario waterfront trails</li>
      <li>MiWay transit service along the neighbourhood's arterial routes</li>
      <li>Established low-rise residential streets with steady rental demand (illustrative context, not a valuation)</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>R3-2 — Residential, Detached Dwellings (Mississauga Zoning By-law 0225-2007)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer). Mississauga permits up to four residential units as-of-right in its low-rise residential zones, subject to the by-law's site standards — setbacks, height, lot coverage, landscaping and parking.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23, up to 3 residential units are permitted as-of-right on a serviced residential lot. Mississauga went further, permitting up to <strong>4 units (fourplexes) as-of-right</strong> across most low-rise residential neighbourhoods (City Council, December 2023). No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>A multiplex of up to <strong>4 residential units</strong> is permitted as-of-right on this lot under Mississauga's fourplex framework, subject to technical review of site conditions — confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means (section 2 list)
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Fourplex (up to 4 units):</strong> A detached building divided into as many as four self-contained residential units — the as-of-right maximum on this lot</li>
      <li><strong>Triplex (3 units):</strong> A more conservative three-unit configuration, also permitted as-of-right</li>
      <li><strong>Duplex / Additional Residential Units:</strong> Two-unit or added-unit forms permitted under the provincial and municipal framework</li>
      <li><strong>Rental-focused build:</strong> Structuring the units as long-term rental may unlock the City's fourth-unit incentive and federal/provincial rental rebates (see Grants &amp; Incentives)</li>'''))

# time-sensitive rows
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>time-limited enhancement</small></div><div class="dx">Ontario's 2026 Budget introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal GST rental rebate. This applies province-wide, including Mississauga, to qualifying purpose-built rental projects of four or more units. The provincial enhancement is temporary — the agreement generally must be signed within the announced 2026–2027 window. Structuring the project as purpose-built rental from Day 1 is essential to capture it. Exact eligibility and figures are confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Mississauga Fourth-Unit Incentive — Apply With the Building Permit<br><small>application-gated</small></div><div class="dx">If you build or legalize a fourplex, the City of Mississauga offers a grant covering development charges and cash-in-lieu-of-parkland fees for the fourth unit, plus a grant toward building-permit fees. Eligibility requires the fourth unit to remain a rental for at least 25 years with no condominium conversion, and the grant must be applied for in connection with the building permit. This is not a blanket waiver — it attaches to the fourth unit specifically. Confirm current terms and amounts in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# section 3 — co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended fourplex (up to 4 units) is permitted as-of-right under Mississauga\'s fourplex framework — no rezoning required.</div>'))

# section 3 — comparison table "what governs your build"
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Mississauga ZBL 0225-2007</td><td class="n">A new site-specific by-law</td></tr>'))

# section 3 — twocard
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Four-unit multiplex</div>Mississauga permits up to four residential units as-of-right in its low-rise residential zones — no rezoning, no committee approval — subject to the by-law's site standards.</div>
    <div class="card2"><div class="ct">Additional residential units</div>Ontario's provincial framework permits additional residential units on a serviced residential lot; how they combine on this lot is confirmed against Mississauga's standards in Phase 2.</div>
  </div>'''))

# section 3 — "what this means for X" barhead + para + amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 1968 Balsam Avenue</div>
  <p>Because 1968 Balsam Avenue already permits the recommended fourplex under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the lot's exact frontage, area and servicing.</b><br><span class="sub">Fourplex eligibility depends on meeting Mississauga's site standards (setbacks, coverage, servicing); these are confirmed against a survey in Phase 2.</span></div>'''))

# options A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — 4-Unit Multiplex (Fourplex) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached building divided into up to four self-contained units — the as-of-right maximum for this lot under Mississauga's fourplex framework. No rezoning and no committee approval are required where the design meets the by-law's site standards (setbacks, height, lot coverage, landscaping and parking). Structuring the fourth unit as a long-term rental (a 25-year commitment, no condominium conversion) can unlock the City's fourth-unit grant covering development charges and cash-in-lieu-of-parkland fees. Exact unit sizes and the buildable envelope are confirmed in Phase 2.</div>'''))

# options B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — 3-Unit Multiplex (Triplex)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A three-unit configuration — a more conservative path that is also permitted as-of-right (Ontario's Bill 23 sets a three-unit floor province-wide, and Mississauga permits up to four). This can mean larger individual units or a simpler build while still adding meaningful rental income. The additional residential units are exempt from development charges under the provincial framework. Unit mix and sizing are confirmed in Phase 2.</div>'''))

# options C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Rental Structuring &amp; the Fourth-Unit Incentive</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">How you structure the units affects which incentives you can capture. Committing the fourth unit to long-term rental (at least 25 years, no condominium conversion) is what makes the lot eligible for Mississauga's fourth-unit grant on development charges and parkland fees, and a purpose-built rental structure of four or more units is what unlocks the federal GST and Ontario provincial HST rental rebates. These structuring decisions are best made before design is finalized — they are confirmed and quantified in Phase 2.</div>'''))

# section 5 — goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Fourplex (4 units)</div>
  <p>1968 Balsam Avenue is a serviced residential lot in Clarkson where Mississauga permits up to four residential units as-of-right — no rezoning required. <strong>The fourplex is the clear primary recommendation</strong>, with a triplex as a more conservative alternative, and rental structuring to capture the City's fourth-unit incentive.</p>'''))

# financing — inject the one gated financing program (CMHC ACLP, $1M loan threshold)
R.append(('''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>''',
'''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <tr><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>A federal program offering low-interest construction financing for purpose-built rental. It requires a minimum loan of roughly $1M, so it becomes relevant only if the project budget reaches that threshold — confirmed against your Phase 2 project budget. It can be structured to bridge into CMHC's MLI Select permanent financing, which itself requires five or more rental units.</td></tr>'''))

# grants — replace the empty GATED_GRANTS_ROWS marker with the programs that
# clear (or show their threshold) for a Mississauga fourplex rental at 3-4 units.
# Toronto DC Waiver is deliberately absent (municipality gate = Toronto only).
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Municipal</td><td>Mississauga Fourth-Unit Incentive</td><td>Grant covering development charges and cash-in-lieu-of-parkland fees for the <strong>fourth unit</strong> of a fourplex, plus a grant toward building-permit fees. The fourth unit must remain a rental for at least 25 years with no condominium conversion, and the grant must be applied for in connection with the building permit. Attaches to the fourth unit specifically — not a blanket waiver. (City of Mississauga — Fourplex / Fourth-Unit incentive.) Terms and amounts confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Under Ontario's More Homes Built Faster Act (Bill 23), additional residential units on a lot are exempt from development charges — a meaningful per-unit saving on the added units within the as-of-right envelope. Confirmed for your configuration in Phase 2.</td></tr>
    <tr><td>Federal + Provincial</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Applies to purpose-built rental projects of <strong>4 or more</strong> self-contained units (90%+ long-term rental) where construction starts before 2031: a full rebate of the 5% federal GST, with Ontario mirroring it via a 100% rebate of the 8% provincial HST component. Reaches this property at the four-unit (fourplex) tier when structured as rental. (Government of Canada; Ontario 2026 Budget.) Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred CMHC insurance terms for purpose-built rental — but it requires a minimum of <strong>five rental units</strong>, one beyond Mississauga's four-unit as-of-right envelope. Shown so the threshold is clear: it becomes reachable only on a larger-scale path (which would require rezoning), explored separately if desired. (CMHC.)</td></tr>'''))

# section 8 — current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1968 Balsam Avenue confirms a strong development option. This is a serviced residential lot in Clarkson, Mississauga, zoned R3-2. Mississauga permits up to <strong>four residential units as-of-right</strong> across most low-rise residential neighbourhoods (City Council, December 2023) — no rezoning, no public hearing, and no committee approval required for a compliant fourplex.</p>
  <ul>
    <li><strong>The Fourplex As-of-Right Advantage:</strong> up to four units can be built on this lot without a rezoning, and structuring the fourth unit as long-term rental unlocks the City's fourth-unit incentive on development charges and parkland fees.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)
open("report_mississauga.html", "w").write(s)

# leftover check — Toronto / source-city / master-lead tokens must be gone
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "474-2023", "569-2013", "Bill 185", "6+1", "4+1", "garden suite", "garage",
          "houseplex", "TTC", "Danforth"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
