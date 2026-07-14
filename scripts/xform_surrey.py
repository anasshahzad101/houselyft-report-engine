import os
HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "..", "templates", "report_surrey.html")
s = open(PATH).read()
R = []

# Cover address
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">15959 108 Avenue<span>Surrey, BC (Metro Vancouver)</span></div>'))

# Property details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">15959 108 Avenue, Surrey, BC&nbsp;&nbsp;V4N 1J6</div>'))

# Imagery row + licence -> honest pending line (no unverified imagery)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div style="font-size:8.6pt;color:#7a818f;font-style:italic;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# Contact table
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>15959 108 Avenue, Surrey, BC&nbsp;&nbsp;V4N 1J6</td></tr>
    <tr><td>Name</td><td>Eduardo Carlos</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>ed_m_carlos@yahoo.com</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — maximize land use under BC's SSMUH rules</td></tr>'''))

# Municipality / property table
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
'''    <tr><td>Municipality</td><td>City of Surrey (Metro Vancouver Regional District)</td></tr>
    <tr><td>Neighbourhood</td><td>Fraser Heights (Guildford area), northeast Surrey</td></tr>
    <tr><td>Current Zoning</td><td>Single-family residential lot under Surrey Zoning By-law No. 12000 — now within the SSMUH zone framework (exact R-zone code confirmed in Phase 2)</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH), implemented by Surrey July 8, 2024</td></tr>
    <tr><td>Servicing</td><td>Must be on full urban services — confirm in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–6 units) under SSMUH, subject to lot size &amp; transit</td></tr>'''))

# Neighbourhood spotlight
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
    15959 108 Avenue is in Fraser Heights, an established residential neighbourhood in northeast Surrey (Guildford area) within Metro Vancouver:
    <ul>
      <li>Quiet, predominantly single-family streets now opened to gentle density by BC's SSMUH rules</li>
      <li>Close to Highway 1 (Trans-Canada) and the Port Mann Bridge, with connections toward Guildford Town Centre and central Surrey</li>
      <li>Served by TransLink bus service; proximity to a frequent-transit stop (within ~400 m) is the key factor in whether up to six units are permitted — confirmed in Phase 2</li>
      <li>Strong, tight rental market across Surrey and Metro Vancouver — supportive of a hold-and-rent strategy</li>
      <li>Note: lot area, slope, tree, and servicing conditions can shape what is buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# Zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Single-family residential lot under Surrey Zoning By-law No. 12000, now subject to the SSMUH zone framework (exact R-zone confirmed in Phase 2)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced residential lots. Unit count scales with lot size and transit proximity: at least 3 units on lots up to 280 m², at least 4 units on lots over 280 m², and up to 6 units on lots between 281 m² and 4,050 m² that are within about 400 m of a frequent bus stop.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023) — implemented by Surrey on July 8, 2024, which amended Zoning By-law No. 12000 and replaced 20 residential zones with 9 new SSMUH zones — <strong>3 to 6 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex, fourplex, and (near frequent transit) up to a six-unit multiplex — plus secondary and garden suites, subject to the specific new SSMUH zone's regulations. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# "What this means for you" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is over 280 m² and within about 400 m of a frequent bus stop</li>
      <li><strong>Multiplex / Small Multi-Unit Building:</strong> standalone multi-unit homes under the new SSMUH zones</li>
      <li><strong>Secondary &amp; Garden Suites:</strong> a secondary suite and/or a detached garden suite can be combined with the main dwelling to reach the unit count</li>'''))

# Time-sensitive section
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>begin before 2031</small></div><div class="dx">The federal government's 100% rebate of the 5% GST on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin after September 13, 2023 and before January 1, 2031, and complete by the end of 2035. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">Parking Relief Near Transit<br><small>lot-specific</small></div><div class="dx">Surrey requires no minimum off-street parking for SSMUH on lots within a Frequent Bus Stop Area. Whether this lot qualifies — which also drives the six-unit tier — is confirmed against Surrey's mapping in Phase 2, and it can materially change the buildable design and cost.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy can change at any time and affects financing options. It is recommended to submit your application as early as possible to reduce risk.</div></div>'''))

# Rezoning section (keep the as-of-right comparison structure; swap all Toronto specifics)
R.append(('''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-green"><div class="ct2">Not Required for This Property</div>Small-Scale Multi-Unit Housing is permitted as-of-right under BC's provincial framework and Surrey's SSMUH zones. A triplex, fourplex, or — where the lot qualifies — a six-unit multiplex can proceed without a rezoning or public hearing.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Approval timeline</td><td class="g">Building-permit path only</td><td class="n">Many months added</td></tr>
    <tr><td>What governs your build</td><td class="g">Surrey SSMUH zones (By-law 12000, as amended)</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit multiplex</div>Where the lot is over 280 m² and within about 400 m of a frequent bus stop, SSMUH permits up to six units without rezoning. Transit proximity and lot area are confirmed in Phase 2.</div>
    <div class="card2"><div class="ct">Secondary &amp; garden suites</div>Surrey's SSMUH zones allow secondary and detached garden suites to help reach the permitted unit count, subject to the specific zone's regulations.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 15959 108 Avenue</div>
  <p>Because Small-Scale Multi-Unit Housing is permitted as-of-right on serviced Surrey residential lots, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions and confirmation of the parcel's exact SSMUH zone.</p>
  <div class="co-amber"><b>Two items to confirm first: the lot's exact SSMUH zone and its distance to a frequent bus stop.</b><br><span class="sub">Together these set whether the ceiling is 3, 4, or 6 units and whether parking minimums apply — both are established in Phase 2.</span></div>'''))

# Development Options
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A triplex or fourplex built directly on the lot — the baseline SSMUH entitlement on a serviced Surrey residential lot, with no rezoning or public hearing. On lots up to 280 m² at least three units are permitted; on larger lots at least four. Buildable size is governed by the SSMUH zone's setbacks, height, lot coverage, and floor-area rules — confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Where the lot is over 280 m² and within about 400 m of a frequent bus stop, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. Confirming the lot's transit proximity and area is the first gating step, since it is what unlocks the six-unit tier and removes the off-street parking minimum. Confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Suites Route (secondary + garden suite)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep the principal dwelling and add a secondary suite plus a detached garden suite, where the SSMUH zone permits, to build toward the unit count with a simpler approval. This is often the fastest route to rental income while a larger multiplex is evaluated. Suite sizes and siting are confirmed in Phase 2.</div>'''))

# Development Goal Summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex under SSMUH (up to 6 units)</div>
  <p>15959 108 Avenue is a single-family residential lot in Surrey now opened to gentle density by BC's SSMUH rules — 3 to 6 units as-of-right depending on lot size and transit proximity. <strong>Where the lot qualifies for the six-unit tier, a six-unit multiplex is the clear primary recommendation</strong>; a triplex or fourplex is the reliable fallback, and the suites route is the fastest entry.</p>'''))

# Grants table (BC-appropriate; BC Secondary Suite Incentive Program omitted - closed to new applications since Mar 2025)
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>Enhanced GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental. Construction must generally begin before January 1, 2031 and complete by the end of 2035. Applies in BC. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Multi-unit mortgage-loan insurance for rental projects of 5+ units. Points-based (affordability, energy efficiency, accessibility) and can unlock higher loan-to-value and longer amortization — materially improving a qualifying project's economics. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental (minimum $1M loan). Can be structured to bridge into MLI Select permanent financing at completion. Confirmed in Phase 2.</td></tr>
    <tr><td>Provincial / Municipal (BC)</td><td>Development Cost Charge (DCC / ACC) treatment</td><td>Under BC's development-finance framework, municipalities levy Development Cost Charges and may apply Amenity Cost Charges. SSMUH and rental projects can attract different DCC treatment; Surrey's current rates and any relief are confirmed against the City's DCC bylaw in Phase 2.</td></tr>'''))

# Summary section 8
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>15959 108 Avenue is a single-family residential lot in the City of Surrey. Under BC's SSMUH framework (Bill 44), implemented locally through Surrey's July 8, 2024 amendments to Zoning By-law No. 12000, it is now eligible for <strong>3 to 6 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and transit proximity.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming lot size and distance to a frequent bus stop, since that is what unlocks the six-unit tier and the parking relief — established in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(PATH, "w").write(s)

print("--- leftover scan ---")
leftovers = 0
for t in ["Coxwell", "Toronto", "John Arock", "johneeraj", "Ward 19", "Beaches", "654-2025",
          "474-2023", "Bill 185", "Ontario HST", "Garden Suite By-law", "nine wards", "TTC",
          "Woodbine", "Greenwood", "Danforth", "Gerrard", "M4L 3B5", "Prefab Plus",
          "6+1", "4+1", "569-2013", "OLT"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        leftovers += 1
print(f"done. replacement_fails={fails}  leftover_terms={leftovers}")
