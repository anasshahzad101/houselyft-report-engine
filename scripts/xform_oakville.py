"""
xform_oakville.py — turn the House Lyft master into the report for
1251 Brillinger Street, Oakville, ON (Atif Kausar).

Property is an ADU / detached-suite lead: the owner wants a rentable suite on
an existing detached double garage with rear-lane access. Oakville verified
facts come from the live Town of Oakville GIS (ZBL 2014-014) + the zoning
engine: zone RM1 (Residential Medium); as-of-right up to 3 units under Bill 23
(principal + up to 2 additional residential units, at most one detached),
implemented via Oakville By-laws 2024-053/054/111. No sixplex; Toronto DC
waiver / Bill 185 / Ward-19 rules do NOT apply here. Everything site-specific
is hedged to Phase 2 per the accuracy contract.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_oakville.html")

s = open(SRC).read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">1251 Brillinger Street<span>Oakville, ON</span></div>'))

# ---- property barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">1251 Brillinger Street, Oakville, ON&nbsp;&nbsp;L6M 3T2</div>'))

# ---- imagery placeholders + licence ----
R.append(('<div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>',
          '<div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(added in the feasibility phase)</small></div>'))
R.append(('<div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>',
          '<div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(added in the feasibility phase)</small></div>'))
R.append(('Imagery: source and licence inserted at generation.',
          'Imagery: to be added from a licensed source during the feasibility phase.'))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1251 Brillinger Street, Oakville, ON&nbsp;&nbsp;L6M 3T2</td></tr>
    <tr><td>Name</td><td>Atif Kausar</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>A rentable suite on the existing detached rear garage (ADU); intends to keep the property</td></tr>'''))

# ---- property table 2 ----
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
'''    <tr><td>Municipality</td><td>Oakville (Halton Region)</td></tr>
    <tr><td>Neighbourhood</td><td>Northwest Oakville (confirmed in Phase 2)</td></tr>
    <tr><td>Region</td><td>Halton Region</td></tr>
    <tr><td>Property Type</td><td>Detached dwelling with a detached rear garage on a back lane (per intake)</td></tr>
    <tr><td>Waste Collection</td><td>Halton Region curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Town of Oakville Zoning By-law 2014-014</td></tr>
    <tr><td>Legal Description</td><td>PIN 256470000 (Town parcel record) — full legal description confirmed in Phase 2</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (survey) — per intake, a lot with a detached double garage and rear-lane access</td></tr>
    <tr><td>Development Goals</td><td>Detached suite on the existing garage (primary); optional interior secondary suite for up to 3 units</td></tr>'''))

# ---- neighbourhood spotlight ----
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
    1251 Brillinger Street is in northwest Oakville, within the Town of Oakville in Halton Region — an established, family-oriented community, and notably a rear-lane street, which is an asset for a garage-based suite:
    <ul>
      <li>Part of Oakville's newer northwest neighbourhoods, well connected to Dundas Street and the area's major arterials</li>
      <li>Close to the schools, parks, and trails typical of northwest Oakville</li>
      <li>Steady rental demand across the Halton market</li>
      <li>Rear-lane access on this street lends itself naturally to a garage-based or laneway-style suite</li>
      <li>Note: parts of Oakville fall within Conservation Halton regulated lands, heritage areas, or tree-protection provisions; any such status is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RM1 — Residential Medium (Town of Oakville Zoning By-law 2014-014)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within the settlement area — the provincial criteria for as-of-right additional residential units. Site-specific standards (setbacks, height, lot coverage, floor-area cap) are confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Oakville implements additional residential units through By-laws 2024-053/054/111. (Some 2026 sources report movement toward four units under Livable Oakville updates; this is confirmed against the governing by-law text in Phase 2.)</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and a detached additional residential unit (for example, a suite on the existing rear garage) are permitted, subject to Oakville's site standards. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- what this means (list) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Additional Residential Unit (ARU):</strong> a self-contained suite on or in place of your rear garage with lane access — your primary goal</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (for example, a basement suite), which can be paired with the detached suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23 the property may support the main dwelling plus two additional units — at most one detached — subject to Oakville's site standards</li>'''))

# ---- time-sensitive (replace the two Toronto items; keep CMHC) ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Development Charges — ARU Exemption<br><small>in effect now</small></div><div class="dx">Additional residential units are exempt from development charges under provincial legislation (Bill 23) — a meaningful per-unit saving on a new suite, with no application required. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Purpose-Built Rental Rebates — Time-Limited<br><small>2026–2027 window</small></div><div class="dx">Enhanced federal and provincial GST/HST rebates on new purpose-built rental housing are time-limited (agreements generally 2026–2027) but target projects of four or more rental units. Their applicability to a smaller ARU project is assessed in Phase 2 — no figure is assumed here.</div></div>'''))

# ---- Section 3 (Rezoning) — Toronto-specific content out ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The additional residential units you\'re considering are permitted as-of-right under Ontario\'s Bill 23 and Oakville\'s implementing by-laws — no rezoning is contemplated.</div>'))

R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + Oakville ZBL 2014-014</td><td class="n">A new site-specific by-law</td></tr>'))

R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to three units</div>Under Ontario's Bill 23, a serviced residential lot may support the principal dwelling plus up to two additional residential units — at most one in a detached accessory building — without rezoning, subject to the Town's site standards.</div>
    <div class="card2"><div class="ct">Detached suite on the garage</div>A detached additional residential unit — such as a suite on your rear garage with lane access — is permitted as-of-right under Oakville's ARU framework (By-laws 2024-053/054/111), subject to setbacks, height, and floor-area standards confirmed in Phase 2.</div>'''))

R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 1251 Brillinger Street</div>
  <p>Because 1251 Brillinger Street already permits the additional residential units under existing zoning and Ontario's Bill 23, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# ---- Development Options ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Suite on the Rear Garage (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite built on or in place of your existing rear garage, using the back-lane access, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Ontario's Bill 23 as an additional residential unit on a serviced residential lot; no rezoning. The size and siting are set by Oakville's ARU standards — setbacks, height, and a floor-area cap — confirmed in Phase 2. Rear-lane access is typically a strong fit for a garage-based or laneway-style suite. The existing garage's structure, servicing, and permit history are reviewed early to confirm how much can be reused.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Detached Suite + Interior Secondary Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the detached garage suite with an interior secondary suite in the existing home (for example, a basement apartment) — a route to as many as three units on the lot under Bill 23, at most one of them detached. This maximizes cash flow while keeping the property in your hands. Eligibility, unit sizes, and any parking or servicing considerations are confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — RM1 Context &amp; Rear-Lane Advantage</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Your property is in an RM1 (Residential Medium) zone with rear-lane access — both are advantages. The lane allows a separate access point for a garage-based suite and more flexible siting than a typical interior lot. RM1 is a medium-density residential zone; whether it also supports a larger residential built form beyond the as-of-right additional-unit pathway is a separate question confirmed against the governing by-law in Phase 2. Confirming the permit status of the existing garage is an essential first step — both for financing qualification and for counting the suite as a legal unit. If any prior conversion was done without a permit, a retroactive permit application will be required before development or financing can proceed.</div>'''))

# ---- goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Additional Residential Unit (ADU)</div>
  <p>1251 Brillinger Street is a serviced residential lot in Oakville, zoned RM1 (Residential Medium), where under Ontario's Bill 23 up to three residential units are permitted as-of-right — including a detached suite on your rear garage, matching your goal of adding rental income while keeping the property. <strong>The detached garage suite is the clear primary recommendation</strong>, with an interior secondary suite as an optional path to a third income unit.</p>'''))

# ---- summary: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1251 Brillinger Street is a serviced residential lot in Oakville, zoned <strong>RM1 (Residential Medium)</strong> under Town of Oakville Zoning By-law 2014-014. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — including the detached garage suite you're after — with no rezoning required, subject to the Town's site standards.</p>
  <ul>
    <li><strong>The Detached-Suite Advantage:</strong> a suite on your rear garage with lane access adds a rental income stream while you keep the property, using land and a structure you already own — the exact size and siting are confirmed in Phase 2.</li>
  </ul>'''))

# ---- grants table (Section 7) ----
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under provincial legislation — a meaningful per-unit saving on a new suite, with no application required. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (up to $7,500) where the new self-contained unit houses an eligible senior or an adult eligible for the disability tax credit. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs for efficient building envelopes, heat pumps, and equipment may offset efficient design on a new suite. Current program availability confirmed in Phase 2.</td></tr>
    <tr><td>Regional / Municipal</td><td>Halton / Oakville ARU Incentives</td><td>Any regional or municipal grants, forgivable loans, or fee relief for additional residential units are budget-limited and periodically open and close — current availability is confirmed for your project in Phase 2. No amount is assumed here.</td></tr>
    <tr><td>Federal / Provincial</td><td>GST/HST New Residential Rental Rebate</td><td>May apply to a newly built rental suite; the enhanced purpose-built rental rebate targets projects of four or more units. Applicability confirmed in Phase 2.</td></tr>'''))

# ---- apply with exact-once assertions ----
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# ---- leftover check: nothing from the source city may survive ----
BANNED = ["Coxwell", "John Arockiaraj", "Toronto", "Ward 19", "Beaches", "654-2025",
          "474-2023", "569-2013", "Bill 185", "6+1", "sixplex", "houseplex", "M4L 3B5",
          "Gerrard", "Danforth", "Greenwood", "TTC", "Woodbine",
          "Canada Secondary Suite Loan", "free grant", "guaranteed return"]
leftovers = 0
for t in BANNED:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        leftovers += 1
print(f"done. fails={fails} leftovers={leftovers} -> {OUT}")
