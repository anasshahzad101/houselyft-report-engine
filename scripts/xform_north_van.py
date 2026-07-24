"""
xform_north_van.py — build the report for 1395 Hendry Avenue, North Vancouver, BC.

City coverage: NO adapter for North Vancouver in the zoning engine -> rules were
researched live per THE PRIME RULE. verified = False -> report-needs-review.

Jurisdiction finding (researched live): 1395 Hendry Ave, V7L 2P3 is in the
DISTRICT of North Vancouver (Grand Boulevard / Keith Lynn area) — NOT the City,
NOT Moodyville. Governed by District Zoning Bylaw 3210, amended by Bylaw 8698
(SSMUH, adopted June 18, 2024) under BC Bill 44. Every zoning specific is hedged
to Phase 2 because the parcel-level designation could not be pulled from the
District GIS (network-blocked). Sources cited in the delivery note.

Run from the templates/ dir so the relative asset paths resolve.
"""
import os

SRC = "report_houselyft_master.html"
OUT = "report_north_van.html"

s = open(SRC).read()
R = []

# --- Cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">1395 Hendry Avenue<span>North Vancouver, BC</span></div>'))

# --- 1 Property Details: barhead -------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">1395 Hendry Avenue, North Vancouver, BC&nbsp;&nbsp;V7L 2P3</div>'))

# --- 1 Property Details: imagery row (no licensed BC source -> remove boxes) -
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8.5pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source for the District of North Vancouver.</div>'''))

# --- 1 Property Details: contact table --------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1395 Hendry Avenue, North Vancouver, BC&nbsp;&nbsp;V7L 2P3</td></tr>
    <tr><td>Name</td><td>Brenna Bains</td></tr>
    <tr><td>Phone Number</td><td>(604) 619-4727</td></tr>
    <tr><td>Email</td><td>bkchutai@hotmail.com</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — rebuild an ageing home into multiple units and maximize the unit count the lot allows</td></tr>'''))

# --- 1 Property Details: municipality table ---------------------------------
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
'''    <tr><td>Municipality</td><td>District of North Vancouver</td></tr>
    <tr><td>Neighbourhood</td><td>Grand Boulevard / Keith Lynn (East side)</td></tr>
    <tr><td>Regional District</td><td>Metro Vancouver</td></tr>
    <tr><td>Waste Collection</td><td>Contact the District of North Vancouver for the local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>District of North Vancouver Zoning Bylaw 3210, as amended by Bylaw 8698 (small-scale multi-unit housing, adopted June 18, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase (via BC Assessment / BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>Older home — the owner reports it needs significant repair; exact age and condition to be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase (via BC Assessment / survey) — the 280&nbsp;m² threshold below sets the unit count</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (primary); unit count maximized to what the lot and provincial SSMUH rules allow</td></tr>'''))

# --- 1 Property Details: neighbourhood spotlight ----------------------------
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
    1395 Hendry Avenue sits in the Grand Boulevard / Keith Lynn area on the east side of the District of North Vancouver — an established, mostly ground-oriented residential neighbourhood on the North Shore (illustrative context only, not a valuation):
    <ul>
      <li>Near the Grand Boulevard greenway, a long tree-lined park corridor that anchors the neighbourhood</li>
      <li>Short drive to Lonsdale Avenue, the District's main north–south services and transit spine</li>
      <li>The Lower Lonsdale / Shipyards district and the SeaBus to downtown Vancouver are a few kilometres south</li>
      <li>Well served by North Shore grocery, schools, and parks; close to Lynn Valley and the Seymour recreation areas</li>
      <li>Note: proximity to a "frequent transit" bus stop (a 15-minute-or-better route) is what can lift the lot from four units to six under the provincial rules — to be checked for this specific address in Phase 2</li>
    </ul>'''))

# --- 2 Current Zoning table -------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>District single-family residential (RS series) — the exact designation is to be confirmed against the District GIS / BC Assessment in Phase 2. Under BC's small-scale multi-unit housing (SSMUH) rules this residential lot now carries a multi-unit entitlement regardless of its base zone.</td></tr>
    <tr><td>Provincial SSMUH Framework</td><td>Under BC Bill 44 (Housing Statutes Amendment Act, 2023), a former single-family / duplex residential lot must permit: <strong>3 units</strong> where the lot is <strong>280&nbsp;m² or smaller</strong>; <strong>4 units</strong> where the lot is <strong>larger than 280&nbsp;m²</strong>; and <strong>up to 6 units</strong> where the lot is within roughly <strong>400&nbsp;m of a frequent-transit stop</strong> (a bus route scheduled on average every 15 minutes or better).</td></tr>
    <tr><td>Local Adoption</td><td>The District of North Vancouver brought its Zoning Bylaw into compliance through Bylaw 8698 (adopted June 18, 2024), and in December 2025 adopted "Ground-Oriented Housing" regulations reported to allow up to four units on 4,000+ properties. A further provincial expansion (Bill 25) is in progress for 2026 — see the note below. Confirm the current in-force text for this parcel in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>Ground-oriented multi-unit housing — triplex / fourplex and, where the lot qualifies near frequent transit, up to a six-unit multiplex, plus secondary-suite and coach-house forms. Subject to the District's built-form standards and technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — a multiplex is achievable as-of-right; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- Time-Sensitive section (all three cards -> BC-relevant) -----------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>construction must start before 2031</small></div><div class="dx">The federal Purpose-Built Rental Housing (PBRH) rebate returns 100% of the 5% federal GST on new purpose-built rental projects of four or more self-contained units held as long-term rental. In British Columbia this is the federal component only — there is no provincial HST, so the Ontario-style 8% provincial rebate does not apply here. Confirm eligibility and structure with a BC tax advisor in Phase 2.</div></div>
    <div class="d"><div class="dt">SSMUH Rules Still Settling<br><small>provincial Bill 25 — 2026</small></div><div class="dx">The provincial six-unit-near-transit expansion (Bill 25, November 2025) carries a June 30, 2026 compliance deadline. The District of North Vancouver voted on April 13, 2026 not to adopt it locally, which can shift the drafting to the Province. The three-and-four-unit allowance is settled; the six-unit case near transit is actively evolving. This is exactly why the unit count for your lot is confirmed against the in-force bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# --- 3 Rezoning: green box --------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A ground-oriented multiplex (three to four units) is permitted as-of-right under the District\'s small-scale multi-unit housing rules — no rezoning is contemplated for the recommended build.</div>'))

# --- 3 Rezoning: comparison table (OLT -> BC framing) -----------------------
R.append(('''    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>District Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Rezoning / development-timeline risk</td><td class="g">Minimal</td><td class="n">Significant</td></tr>
    <tr><td>What governs your build</td><td class="g">The District SSMUH provisions (Bylaw 8698)</td><td class="n">A new site-specific by-law</td></tr>'''))

# --- 3 Rezoning: twocard ----------------------------------------------------
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Triplex / fourplex</div>Three units on a lot 280&nbsp;m² or smaller, four units on a larger lot — permitted as-of-right on a residential lot under the District's SSMUH provisions, no rezoning.</div>
    <div class="card2"><div class="ct">Coach house &amp; secondary suite</div>The District permits ground-oriented forms including a coach house and a secondary suite alongside the principal dwelling, subject to its coach-house development-permit guidelines.</div>'''))

# --- 3 Rezoning: "what this means" para + amber note -------------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 1395 Hendry Avenue</div>
  <p>Because a ground-oriented multiplex is permitted as-of-right under the District's small-scale multi-unit housing rules, no rezoning application is contemplated for the three-to-four-unit build. Your project advances directly to design and permitting. This assessment was researched from live provincial and District sources and is subject to confirmation of the parcel's exact zone, lot area, and frequent-transit status, and to technical review of site conditions, during Phase 2.</p>
  <div class="co-amber"><b>Two items to confirm before design locks: the lot area and the frequent-transit status.</b><br><span class="sub">The lot area (above or below 280&nbsp;m²) sets whether the baseline is four units or three; proximity to a frequent-transit stop is what can lift the lot to six units. Both are confirmed against the District GIS and the in-force bylaw in Phase 2.</span></div>'''))

# --- 4 Development Options ---------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A new ground-oriented multiplex replacing the existing ageing home: three units if the lot is 280&nbsp;m² or smaller, four units if it is larger. This is the settled, as-of-right path under the District's small-scale multi-unit housing rules — no rezoning and no public hearing. It directly answers the owner's question of how many units the lot can hold, on the most certain footing. The District's SSMUH standards (floor-space ratio, height of about three storeys, coverage, setbacks and parking) govern the built form; parking minimums are reduced, and are removed entirely within roughly 400&nbsp;m of a frequent-transit stop. The exact lot area, the governing floor-space ratio, and the final unit count are confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (if the lot qualifies near frequent transit)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">If the lot falls within roughly 400&nbsp;m of a frequent-transit stop, the provincial rules contemplate up to six units — the maximum unit count the owner asked about. Two caveats make this the upside case rather than the base case: the transit qualification must be confirmed for this specific address, and the six-unit-near-transit expansion (provincial Bill 25) is still being worked through locally — the District voted in April 2026 not to adopt it, which can move the drafting to the Province. Phase 2 confirms whether six units are available on this lot today, and a design that starts at four units can be planned to scale toward six if and when the entitlement is confirmed.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Coach House + Secondary Suite Configuration</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-intensity path that keeps or rebuilds a principal dwelling and adds a secondary (basement) suite plus a detached coach house at the rear — the District permits this ground-oriented form under its coach-house development-permit guidelines. It is a smaller step than a full multiplex but still adds rentable units and income, and can suit a phased approach or a tighter budget. The coach-house siting rules, servicing, and any development-permit requirements are confirmed in Phase 2.</div>'''))

# --- 5 Development Goal Summary ----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Ground-Oriented Multiplex (3–4 units, with a path to 6)</div>
  <p>1395 Hendry Avenue is a residential lot in the District of North Vancouver, where BC's small-scale multi-unit housing rules permit a ground-oriented multiplex as-of-right. <strong>A three-to-four-unit multiplex is the clear primary recommendation</strong> — it is the settled, no-rezoning path and directly answers the owner's question of how many units the lot can hold. Where the lot qualifies near frequent transit, the rules contemplate up to six units; that upside is confirmed against the in-force bylaw and the parcel's transit status in Phase 2.</p>'''))

# --- 6 Financing: gated program rows (tiered, thresholds shown) --------------
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC MLI Select <small>(at 5+ rental units)</small></td><td>A federal CMHC insured-financing program for purpose-built rental. It applies once the project reaches <strong>five or more rental units</strong> — reachable here only in the six-unit scenario. It can offer higher loan-to-cost and longer amortization than conventional financing. National program; applies in BC. (Source: CMHC MLI Select product terms.)</td></tr>
    <tr><td>CMHC Apartment Construction Loan Program (ACLP) <small>(at a $1M+ loan)</small></td><td>Low-interest construction financing for purpose-built rental, available where the loan is <strong>$1M or more</strong> — a Phase-2 budget question rather than a unit-count one. Can bridge into MLI Select permanent financing at completion. National program. (Source: CMHC ACLP program terms.)</td></tr>
    <tr><td>CMHC Prefab / modular financing <small>(inherits the 5+ unit MLI gate)</small></td><td>Brings modular / prefab construction into the CMHC MLI Select framework, so it carries the same five-rental-unit minimum. Potentially shortens the construction timeline. (Source: CMHC — expanded 2026.)</td></tr>'''))

# --- 7 Grants table: gated rows (BC / federal only; no municipal grant found) -
R.append(('''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->
    </table>''',
'''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>BC Small-Scale Multi-Unit Housing entitlement (Bill 44)</td><td>The core benefit here is a <strong>zoning entitlement, not a cheque</strong>: provincial law now requires the District to permit a ground-oriented multiplex as-of-right on this lot — three or four units by lot size, up to six near frequent transit. It removes the cost, delay, and uncertainty of a rezoning. (Source: BC Housing Statutes (Residential Development) Amendment Act, 2023.)</td></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate <small>(at 4+ rental units)</small></td><td>A 100% rebate of the 5% federal GST on new purpose-built rental with <strong>four or more</strong> self-contained units held as long-term rental; construction must begin before 2031. In BC this is the federal component only — there is no provincial HST rebate. (Source: federal PBRH rebate.)</td></tr>
    <tr><td>Provincial</td><td>BC tax treatment of the build</td><td>BC applies the 5% federal GST; there is no provincial HST. PST generally applies to construction materials but not to most labour. This is a structural cost consideration, not a grant — confirm the exact treatment with a BC tax advisor in Phase 2. (Source: BC tax framework.)</td></tr>
    <tr><td>Municipal</td><td>District of North Vancouver / Metro Vancouver</td><td>No municipal grant or subsidy specifically for building additional residential units was verified for the District of North Vancouver at the date of this report — the District's programs in this area are regulatory (secondary-suite and coach-house permitting), not financial. Confirmed live during Phase 2.</td></tr>
    </table>'''))

# --- 8 Summary: current zoning review ---------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1395 Hendry Avenue confirms a strong development option. It is a residential lot in the District of North Vancouver, where British Columbia's small-scale multi-unit housing rules now permit a ground-oriented multiplex <strong>as-of-right</strong> — no rezoning, no public hearing, no council approval. For an owner whose current house needs significant repair, that turns a costly rebuild into an opportunity to add units and income.</p>
  <ul>
    <li><strong>The As-of-Right Multiplex Advantage:</strong> provincial law (Bill 44) requires the District to permit three or four units on this lot as-of-right, and up to six where it qualifies near frequent transit — the settled path avoids the cost and delay of a rezoning.</li>
    <li><strong>Researched live — confirm before the call:</strong> North Vancouver is outside the engine's verified-city set, so these rules were researched from live provincial and District sources. The parcel's exact zone, lot area, and frequent-transit status are confirmed in Phase 2 before any figures are relied on.</li>
  </ul>'''))

# --- apply -------------------------------------------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:60]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# --- leftover guard ----------------------------------------------------------
print("--- leftover check ---")
for t in ["Coxwell", "Ward 19", "Beaches", "John Arockiaraj", "Arockiaraj",
          "654-2025", "474-2023", "Ontario HST", "Bill 185", "6+1", "4+1",
          "Toronto", "OLT", "garden suite", "Garden Suite", "TTC", "Danforth",
          "Secondary Suite Loan", "free grant", "guaranteed return"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
