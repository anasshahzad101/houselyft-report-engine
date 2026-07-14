"""Transform the House Lyft master report into the Coquitlam (Roger Challis) report.
Live-researched municipality (no city adapter) -> report-needs-review.
Mirrors the assert-once + leftover-scan discipline of the other xform_*.py scripts."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_coquitlam.html")

s = open(SRC).read()
R = []

# 1. Cover address
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">729 Accacia Avenue<span>Coquitlam, BC</span></div>'))

# 2. Property Details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">729 Accacia Avenue, Coquitlam, BC&nbsp;&nbsp;V3J 2E6</div>'))

# 3. Imagery row -> honest pending line (no verified BC lot-scale source; remove grey boxes)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div style="font-size:8pt;color:#7a818f;margin:2px 0 12px;font-style:italic;">Aerial and street-level photography pending a licensed imagery source for Coquitlam.</div>'''))

# 4. Contact table
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>729 Accacia Avenue, Coquitlam, BC&nbsp;&nbsp;V3J 2E6</td></tr>
    <tr><td>Name</td><td>Roger Challis</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>challisrw@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>Four detached units (~2,200 sq ft each) under BC's SSMUH rules</td></tr>'''))

# 5. Municipality table
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
'''    <tr><td>Municipality</td><td>City of Coquitlam (Metro Vancouver Regional District)</td></tr>
    <tr><td>Region</td><td>Tri-Cities, Metro Vancouver, BC</td></tr>
    <tr><td>Neighbourhood</td><td>Cariboo</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH); City of Coquitlam Zoning Bylaw No. 5449 (adopted June 9, 2025)</td></tr>
    <tr><td>Current Zoning</td><td>Small-Scale Residential — Coquitlam's SSMUH zones replaced the former RS single-family series; exact zone confirmed in Phase 2</td></tr>
    <tr><td>Servicing</td><td>Municipal water/sewer connection required — confirm capacity in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>~1,133 m² (owner-stated ~12,200 sq ft) — to be confirmed; unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Four detached units under SSMUH (up to 6 where a frequent-transit tier applies)</td></tr>'''))

# 6. Neighbourhood Spotlight
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
    729 Accacia Avenue is in the Cariboo neighbourhood of southwest Coquitlam, in the Tri-Cities area of Metro Vancouver — an established residential area close to the Coquitlam–Burnaby border:
    <ul>
      <li>Near the Lougheed Town Centre area and its SkyTrain station (Millennium and Expo lines) — the owner reports the lot is approximately 950 m from the station (to be confirmed)</li>
      <li>Proximity to a frequent-transit stop is the key factor in whether up to six units are permitted under SSMUH — confirmed in Phase 2</li>
      <li>Well served by TransLink bus and SkyTrain across the Tri-Cities and into Burnaby and Vancouver</li>
      <li>Strong, chronically tight Metro Vancouver rental market — supportive of a hold-and-rent strategy</li>
      <li>Note: lot grade, trees, and setback rules can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# 7. Zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Small-Scale Residential (City of Coquitlam) — the SSMUH zones that replaced the former RS single-family series under Zoning Bylaw No. 5449; exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced single-family / duplex residential lots. Unit count scales with lot size and transit proximity: lots between 280 m² and 4,050 m² permit up to 4 units; a 6-unit allowance requires the lot be within ~400 m of a frequent-transit (≤15 min) stop.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023), implemented by Coquitlam through Zoning Bylaw No. 5449 (adopted June 9, 2025), <strong>3 to 4 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex — up to <strong>6</strong> near frequent transit. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex and fourplex (plus secondary and garden/carriage suites); and, where a lot is within ~400 m of frequent transit, up to a six-unit multiplex. Small-Scale Residential form: max 3 storeys / ~11 m. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# 8. "What this means for you" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Detached Units / Multiplex:</strong> multiple ground-oriented homes — matching the owner's four-unit goal</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is 280–4,050 m² and within ~400 m of frequent transit</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> secondary suites and garden/carriage suites can be paired with the main dwellings to add density</li>'''))

# 9. Time-Sensitive box (drop Ontario HST + Bill 185)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% GST rebate on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">Coquitlam SSMUH Bylaw — In Effect<br><small>adopted June 9, 2025</small></div><div class="dx">Coquitlam has adopted its SSMUH-compliant Zoning Bylaw No. 5449, so the small-scale multi-unit permissions are already in force. The applicable unit count and site standards for your lot are confirmed against the City's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">No minimum parking is required for SSMUH projects within ~400 m of frequent transit. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))

# 10. Rezoning section
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended multiplex (up to 4 units, or 6 near frequent transit) is permitted as-of-right under BC\'s SSMUH rules and Coquitlam Zoning Bylaw No. 5449 — no rezoning needed.</div>'))
R.append(('<tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '<tr><td>Appeal exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">SSMUH (Bylaw 5449)</td><td class="n">A new site-specific by-law</td></tr>'))
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Fourplex, as-of-right</div>On a serviced lot between 280 m² and 4,050 m², SSMUH permits up to four units without rezoning — the tier that matches the owner's four-unit goal.</div>
    <div class="card2"><div class="ct">Garden / carriage suite</div>Coquitlam's Small-Scale Residential rules allow ground-oriented suites (secondary and garden/carriage) to be paired with the principal dwellings, subject to lot standards — confirmed in Phase 2.</div>
  </div>'''))
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 729 Accacia Avenue</div>
  <p>Because 729 Accacia Avenue already permits the recommended build under existing SSMUH zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the rules in force at the date of this report, was researched live for Coquitlam, and is subject to technical review of site conditions.</p>'''))
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>Two items to confirm in Phase 2: the lot\'s exact area and its distance to a frequent-transit stop.</b><br><span class="sub">Together these set whether the lot qualifies for the 4-unit tier or the 6-unit near-transit tier under SSMUH.</span></div>'))

# 11. Development Options
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Four Detached Units / Fourplex (as-of-right) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Up to four ground-oriented units built directly on the lot — the baseline SSMUH entitlement on a serviced Coquitlam residential lot between 280 m² and 4,050 m², with no rezoning or public hearing. This matches Roger's stated goal of four detached units (~2,200 sq ft each). Small-Scale Residential form governs the envelope: max 3 storeys / ~11 m, with lot coverage, setback, and floor-area rules confirmed against Coquitlam's current bylaw in Phase 2. The owner-reported ~12,200 sq ft lot, if confirmed, comfortably supports the four-unit tier.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Upside to Confirm</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Where the lot is between 280 m² and 4,050 m² and within roughly 400 m of a frequent-transit (≤15 min) stop, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. The owner reports the lot is about 950 m from Lougheed Town Centre SkyTrain; because that is beyond the ~400 m frequent-transit radius, the six-unit tier is not assumed here — it hinges on confirming a qualifying frequent-transit stop closer to the lot. Confirming lot area and transit proximity is the first gating step. No minimum parking applies within the transit radius. Confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Suites Route (secondary + garden/carriage suite)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep or rebuild a principal dwelling and add a secondary suite plus a detached garden or carriage suite, where the lot standards allow. This is often the fastest route to rental income while a larger multiplex is designed and permitted. Suite sizes and siting are governed by Coquitlam's Small-Scale Residential rules and confirmed in Phase 2.</div>'''))

# 12. Section 5 — Development Goal Summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Four-Unit Multiplex under SSMUH</div>
  <p>729 Accacia Avenue is a single-family lot in Coquitlam now opened to gentle density by BC's SSMUH rules and Zoning Bylaw No. 5449 — 3 to 4 units as-of-right, and up to 6 near frequent transit. <strong>A four-unit build is the clear primary recommendation</strong>, matching the owner's stated goal; the six-unit tier is an upside to confirm against the lot's distance to a qualifying frequent-transit stop.</p>'''))

# 13. Section 7 — Grants table (BC set)
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental (construction generally before 2031). Applies in BC. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / Apartment Construction Loan Program</td><td>MLI Select multi-unit mortgage insurance (5+ rental units) and the Apartment Construction Loan Program (low-interest construction financing, min $1M) — national programs that heavily subsidize a qualifying rental project. Confirmed in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>Forgivable loan reported up to $40,000 toward a new secondary suite rented below market for a set term. Eligibility and current status confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by municipality. Confirmed against Coquitlam's current bylaw in Phase 2.</td></tr>'''))

# 14. Section 8 — Summary
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>729 Accacia Avenue is a single-family lot in the City of Coquitlam. Under BC's SSMUH framework (Bill 44) and Coquitlam Zoning Bylaw No. 5449 (adopted June 2025), it is now eligible for <strong>3 to 4 units as-of-right</strong> — no rezoning, no public hearing — with up to 6 units where the lot is within ~400 m of frequent transit.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> a four-unit multiplex is achievable as-of-right and matches the owner's goal; the most valuable next step is confirming lot area and distance to frequent transit, since that is what could unlock the six-unit tier — established in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

print("--- leftover scan ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John", "Arockiaraj",
          "654-2025", "474-2023", "569-2013", "Ontario HST", "Bill 185",
          "OLT", "6+1", "Garden Suite By-law", "johneeraj", "M4L"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails, "-> wrote", OUT)
