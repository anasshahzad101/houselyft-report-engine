s = open("report_saanich.html").read()
R = []
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">1361 Hastings Street<span>Saanich, BC (Greater Victoria)</span></div>'))
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">1361 Hastings Street, Saanich, BC&nbsp;&nbsp;V8Z 2W5</div>'))
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1361 Hastings Street, Saanich, BC&nbsp;&nbsp;V8Z 2W5</td></tr>
    <tr><td>Name</td><td>Shane Restall</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize unit count under BC's SSMUH rules</td></tr>'''))
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
'''    <tr><td>Municipality</td><td>District of Saanich (Capital Regional District)</td></tr>
    <tr><td>Region</td><td>Greater Victoria, BC</td></tr>
    <tr><td>Current Zoning</td><td>RS-6 — Single Family (District of Saanich)</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td></tr>
    <tr><td>Servicing</td><td>Must be within the Urban Containment / Sewer Service Area — confirm in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–6 units) under SSMUH, subject to lot size &amp; transit</td></tr>'''))
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
    1361 Hastings Street is in the District of Saanich, part of the Greater Victoria region on southern Vancouver Island — an established, high-demand residential area:
    <ul>
      <li>Central Saanich location with quick access to Uptown, Downtown Victoria, and the University of Victoria</li>
      <li>Well served by BC Transit; proximity to a frequent-transit route is the key factor in whether up to six units are permitted — confirmed in Phase 2</li>
      <li>Strong, chronically tight rental market across Greater Victoria — supportive of a hold-and-rent strategy</li>
      <li>Established single-family streets now opened to gentle density by provincial SSMUH rules</li>
      <li>Note: slopes, trees, and setback/character guidelines can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS-6 — Single Family (District of Saanich), now subject to provincial SSMUH permissions</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced residential lots inside the Urban Containment Boundary. Unit count scales with lot size and transit proximity (a 6-unit allowance requires a lot &gt;280 m² within ~400 m of frequent transit).</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023) — implemented by Saanich in 2024 and tightened by Bill 25 (Nov 2025, compliance by June 30, 2026) — <strong>3 to 6 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex, fourplex, and (near frequent transit) up to a six-unit multiplex — plus secondary and garden suites. Saanich exempts projects of 4 units or fewer from a Form &amp; Character development permit. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))
R.append(('''      <li><strong>Row Housing &amp; Stacked Row Housing:</strong> Multi-unit attached homes sharing side walls</li>
      <li><strong>Small Apartment Buildings / Multiplexes:</strong> Standalone multi-unit buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is &gt;280 m² and within ~400 m of frequent transit</li>
      <li><strong>Suites Route:</strong> a secondary suite plus a detached garden suite — Saanich allows both on the same lot inside the boundary</li>'''))
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% GST rebate on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">BC Bill 25 — SSMUH Compliance<br><small>June 30, 2026</small></div><div class="dx">Bill 25 (Nov 2025) tightened the SSMUH rules and set a June 30, 2026 deadline for municipalities, including Saanich, to finalize compliant bylaws. The applicable unit count and site standards for your lot are confirmed against Saanich's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">No minimum parking is required for SSMUH projects within ~400 m of frequent transit. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A triplex or fourplex built directly on the lot — the baseline SSMUH entitlement on a serviced Saanich residential lot, with no rezoning or public hearing. At four units or fewer, Saanich exempts the project from a Form &amp; Character development permit, which meaningfully shortens the approval path. Buildable size is governed by setbacks, height, lot coverage, and floor-area rules — confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Where the lot is greater than 280 m² and within roughly 400 m of a frequent-transit stop, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. Confirming the lot's transit proximity and area is the first gating step, since it is what unlocks the 6-unit tier. No minimum parking applies within the transit radius. Confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Suites Route (secondary + garden suite)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep the principal dwelling and add a secondary suite plus a detached garden suite — Saanich allows both on the same lot inside the boundary, and has removed the owner-occupancy requirement. This is often the fastest route to rental income while a larger multiplex is evaluated. Suite sizes and siting confirmed in Phase 2.</div>'''))
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex under SSMUH (up to 6 units)</div>
  <p>1361 Hastings Street is an RS-6 single-family lot in Saanich now opened to gentle density by BC's SSMUH rules — 3 to 6 units as-of-right depending on lot size and transit proximity. <strong>Where the lot qualifies for the six-unit tier, a six-unit multiplex is the clear primary recommendation</strong>; a triplex/fourplex is the reliable fallback, and the suites route is the fastest entry.</p>'''))
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1361 Hastings Street is an RS-6 single-family lot in the District of Saanich. Under BC's SSMUH framework (Bill 44, tightened by Bill 25), it is now eligible for <strong>3 to 6 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and transit proximity.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming lot size and distance to frequent transit, since that is what unlocks the six-unit tier — established in Phase 2.</li>
  </ul>'''))
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental (construction generally before 2031). Applies in BC. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / ACLP</td><td>MLI Select multi-unit mortgage insurance (5+ rental units) and the Apartment Construction Loan Program (low-interest construction financing, min $1M) — national programs that heavily subsidize a qualifying rental project. Confirmed in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>Forgivable loan reported up to $40,000 toward a new secondary suite rented below market for a set term. Eligibility and current status confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by municipality. Confirmed against Saanich's current bylaw in Phase 2.</td></tr>'''))

fails=0
for old,new in R:
    c=s.count(old)
    if c!=1:
        print(f"[FAIL x{c}] {old[:60]!r}"); fails+=1
    else:
        s=s.replace(old,new)
open("report_saanich.html","w").write(s)
for t in ["Coxwell","Toronto","Ward 19","Beaches","John Arockiaraj","654-2025","Ontario HST","Bill 185","6+1 Config"]:
    n=s.count(t)
    if n: print(f"LEFTOVER '{t}': {n}")
print("done, fails:",fails)
