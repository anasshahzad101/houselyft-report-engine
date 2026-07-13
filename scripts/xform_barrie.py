"""
xform_barrie.py — turn the House Lyft master report into the Barrie lead report
for 331 Leacock Drive, Barrie ON (Deepak K Sood).

Same contract as the other xform_*.py: every replacement must match exactly once,
then a leftover grep guarantees no source-city (Toronto / Coxwell) data survives.
Run from the templates/ directory against a fresh copy of the master:
    cp report_houselyft_master.html report_barrie.html && python3 ../scripts/xform_barrie.py

Barrie facts are researched-live (no engine adapter) -> report-needs-review:
  - Up to 4 residential units as-of-right on a residential lot; By-law 2009-141
    amended April 17, 2024 (up from 3). ARU standards: 4.5 m height, 3 m setbacks.
  - City of Barrie 2026 ARU Incentives Program (50% permit/zoning/water fee cut,
    full rebate on interior conversions passing final inspection <=12 months).
  - Housing CIP Per Door Grant (budget-limited). Provincial ARU DC exemption (Bill 23).
  - Federal Multigenerational Home Renovation Tax Credit (in-law suite fit).
Imagery: no licensed lot-scale source for Barrie -> placeholders removed, honest
pending line kept.
"""
s = open("report_barrie.html").read()
R = []

# ---- cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">331 Leacock Drive<span>Barrie, ON</span></div>'))

# ---- property-details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">331 Leacock Drive, Barrie, ON&nbsp;&nbsp;L4N 6J8</div>'))

# ---- imagery block: no licensed source for Barrie -> drop placeholders, honest line
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source for this municipality.</div>'''))

# ---- property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>331 Leacock Drive, Barrie, ON&nbsp;&nbsp;L4N 6J8</td></tr>
    <tr><td>Name</td><td>Deepak K Sood</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Basement in-law suite (interior second unit) for rental income — architectural drawings approved by the City of Barrie; owner intends to keep the property and is seeking project funding to begin</td></tr>'''))

# ---- property table 2
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
'''    <tr><td>Municipality</td><td>Barrie (single-tier city)</td></tr>
    <tr><td>Neighbourhood</td><td>Letitia Heights (northwest Barrie)</td></tr>
    <tr><td>Property Type</td><td>Single detached (per intake)</td></tr>
    <tr><td>Waste Collection</td><td>City of Barrie curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Barrie Comprehensive Zoning By-law 2009-141 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Letitia Heights subdivision era (1980s) — to be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Basement second suite (in-law suite) — approved; optional detached unit toward up to 4 units total</td></tr>'''))

# ---- neighbourhood spotlight
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
    331 Leacock Drive is in Letitia Heights, an established residential neighbourhood in northwest Barrie built in the 1980s and known for its quiet, author-named streets (Leacock, Shakespeare, Browning, Burns):
    <ul>
      <li>Family-oriented community and a recognized affordable entry point in Barrie's housing market</li>
      <li>Lampman Lane Park (splash pad, tennis and basketball courts) and the large Sunnidale Park with its walking and cycling trails are nearby — the area has several parks and recreational facilities</li>
      <li>Well served by local schools, including Andrew Hunter Elementary and Portage View Public School, with Catholic options and French Immersion available</li>
      <li>Barrie Transit serves the neighbourhood; Georgian College, downtown Barrie, and Highway 400 are accessible across the city</li>
      <li>Steady local rental demand supports a second-suite strategy. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Barrie Comprehensive Zoning By-law 2009-141) — exact zone (e.g. R2) confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) — the standard for as-of-right additional residential units. Additional units carry site standards including a maximum height of 4.5 m and minimum 3 m rear and side-yard setbacks.</td></tr>
    <tr><td>Recent Changes</td><td>In April 2024, Barrie amended By-law 2009-141 to permit up to <strong>4 residential units</strong> as-of-right on a residential lot (up from 3) — no rezoning required. Additional residential units are permitted in the R1–R5 and RM residential zones.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior second suite (such as a basement in-law suite) plus further additional residential units — up to 4 units total on the lot — subject to the City's site standards. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Second Suite:</strong> a self-contained unit within the existing home — such as the basement in-law suite you have approved</li>
      <li><strong>Detached Additional Residential Unit (ARU):</strong> a separate suite in the rear yard (coach house / garden suite), subject to the 4.5 m height and 3 m setback standards</li>
      <li><strong>Up to 4 units on the lot:</strong> under the April 2024 by-law amendment, the property may support up to four residential units as-of-right, subject to site standards</li>
      <li><strong>Additional income potential:</strong> pairing an interior suite with a detached unit is a route to more rental income on land you already own</li>'''))

# ---- time-sensitive block (all three rows)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Barrie 2026 ARU Incentives Program — Act in 2026<br><small>application window open through Dec 31, 2026</small></div><div class="dx">The City of Barrie is reducing building-permit, zoning, and water fees for new additional-residential-unit permits by 50% for applications submitted between January 1 and December 31, 2026 — and rebating those fees in full when an interior conversion passes its final interior inspection within 12 months of permit issuance. Interior conversions that add a second unit, such as your basement in-law suite, are expressly eligible. Applications must be received by December 31, 2026 and projects completed by December 31, 2027. (Source: City of Barrie.)</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under Ontario's provincial legislation (Bill 23) — a meaningful per-unit saving on a new suite. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- section 3: co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended interior second suite — and up to four units on the lot — is permitted as-of-right under Barrie\'s Comprehensive Zoning By-law 2009-141 (as amended April 2024).</div>'))

# ---- section 3: comparison table "what governs your build"
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 2009-141 (as amended)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- section 3: "also permitted as-of-right" twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>Barrie permits up to four residential units on a residential lot as-of-right (By-law 2009-141, amended April 2024) — no rezoning required.</div>
    <div class="card2"><div class="ct">Detached rear unit</div>A detached additional residential unit (coach house / garden suite) is permitted in the rear yard as-of-right, subject to the 4.5 m height and 3 m setback standards.</div>'''))

# ---- section 3: barhead + paragraph
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 331 Leacock Drive</div>'))
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 331 Leacock Drive already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting — and your basement-suite drawings are already approved. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

# ---- section 3: amber note
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: that the City-approved basement-suite drawings and building permit remain current.</b><br><span class="sub">Approvals can lapse if a permit is not issued, or work not commenced, within the City\'s timelines — confirm the permit is active before arranging financing draws.</span></div>'))

# ---- section 4: option A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Interior Basement Second Suite (your approved project)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained interior second suite in the basement of the existing home — an in-law suite rented for ongoing income while you keep the property, which is your stated goal. This is permitted as-of-right under Barrie's By-law 2009-141 on a serviced residential lot; no rezoning is required. Your architectural drawings for this suite are already approved by the City of Barrie, so the project can move straight to construction once financing is arranged. Additional residential units are exempt from development charges, and the City's 2026 ARU Incentives Program can reduce or fully rebate the building-permit fees. Final unit size and any Building Code items are confirmed in Phase 2.</div>'''))

# ---- section 4: option B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Basement Suite + Detached ARU (toward up to 4 units)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the approved basement suite with a detached additional residential unit (a coach house or garden suite) in the rear yard — a route toward as many as four income-generating units on the lot under Barrie's By-law 2009-141, where the property allows. The detached unit follows the City's ARU standards: a maximum height of 4.5 m and minimum 3 m rear and side-yard setbacks. This maximizes cash flow while keeping the property in your hands. Eligibility, siting, and unit sizes are confirmed in Phase 2.</div>'''))

# ---- section 4: option C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Scaling to a Four-Unit Property</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Barrie's April 2024 amendment allows up to four residential units on a residential lot as-of-right — for example, the main dwelling, the basement in-law suite, and a detached rear unit, with room to configure a fourth where the site standards are met. Reaching the full four-unit envelope depends on lot area, servicing capacity, parking, and the 4.5 m height and 3 m setback rules for the additional units. The exact buildable configuration is confirmed in Phase 2. Starting with the approved basement suite keeps the first income unit moving now while these options are scoped.</div>'''))

# ---- section 5: goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Basement Second Suite</div>
  <p>331 Leacock Drive is a serviced residential lot in Letitia Heights where, under Barrie's By-law 2009-141 (amended April 2024), an interior second suite is permitted as-of-right — matching the basement in-law suite you already have approved. <strong>Completing the approved basement suite is the clear primary recommendation</strong>, with a detached additional unit as an optional path toward up to four units on the lot.</p>'''))

# ---- section 7: grants table
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Municipal</td><td>City of Barrie — 2026 ARU Incentives Program</td><td>A 50% reduction on building-permit, zoning, and water fees for new additional-residential-unit permits applied for between Jan 1 and Dec 31, 2026, with a full fee rebate when an interior conversion passes final interior inspection within 12 months of permit issuance. Covers interior second suites, detached ARUs, and new builds of two to four units. Apply by Dec 31, 2026; complete by Dec 31, 2027. (City of Barrie.)</td></tr>
    <tr><td>Municipal</td><td>City of Barrie — Housing Community Improvement Plan (Per Door Grant)</td><td>A city-wide capital grant provided in place of certain fees and charges to encourage new rental housing, with an emphasis on affordable units. Budget-limited and delivered through periodic intakes — current availability and project fit confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under Ontario's provincial legislation — a meaningful per-unit saving on a new suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (up to $7,500) for creating a self-contained secondary unit for an eligible senior or adult relative — a strong fit for an in-law suite. Eligibility confirmed in Phase 2 (CRA).</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes / Home Renovation Savings may offset efficient design and equipment on a new suite. Applicability confirmed in Phase 2.</td></tr>'''))

# ---- section 8: current zoning review paragraph + li
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>331 Leacock Drive is a serviced residential lot in Letitia Heights, Barrie. Under the City's Comprehensive Zoning By-law 2009-141 (amended April 2024), up to <strong>four residential units are permitted as-of-right</strong> — including the interior second suite you have approved — with no rezoning required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Second-Suite &amp; Four-Unit Advantage:</strong> the basement in-law suite is already approved by the City, and the lot can support up to four units as-of-right — added income on land you already own, with the exact envelope confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)
open("report_barrie.html", "w").write(s)

# ---- leftover check: no source-city / wrong-program data may survive
print("\n--- leftover check ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "johneeraj",
          "654-2025", "474-2023", "569-2013", "Bill 185", "6+1", "4+1", "TTC",
          "Danforth", "Gerrard", "Greenwood", "Woodbine", "M4L", "garden suite in the rear",
          "houseplex", "Garden Suite By-law"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
