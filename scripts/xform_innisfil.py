"""
xform_innisfil.py — transform the House Lyft master report into the Innisfil
secondary-suite report for 2178 Nevils Street, Innisfil, ON (Julius Ekhator).

Innisfil has NO zoning-engine adapter, so the municipal rules below were
researched live from official Town of Innisfil sources and are tagged
report-needs-review. Verified facts (Town of Innisfil + Ontario):
  - Comprehensive Zoning By-law 080-13, amended for additional/"third"
    dwelling units under Ontario's Bill 23 (More Homes Built Faster Act).
  - Up to 3 units on eligible detached / semi-detached / street-townhouse lots
    (principal dwelling + up to 2 accessory dwelling units).
  - A "third" dwelling unit is capped at 50% of the principal dwelling's floor
    area, to a maximum of 100 m2.
  - ADUs must be legally constructed and registered with the Town.
Everything not verified for THIS lot is hedged to Phase 2, per the accuracy
contract in docs/AI_Report_Writer_Role_v1.md.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_innisfil.html")

s = open(SRC).read()
R = []

# --- cover ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">2178 Nevils Street<span>Innisfil, ON</span></div>'))

# --- property details barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">2178 Nevils Street, Innisfil, ON&nbsp;&nbsp;L9S 0E1</div>'))

# --- imagery licence placeholder (no licensed source for Innisfil) ---
R.append(('<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: no licensed aerial/street-view source is included in this preliminary report — property imagery is added in Phase 2.</div>'))

# --- property table 1 (contact block) ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>2178 Nevils Street, Innisfil, ON&nbsp;&nbsp;L9S 0E1</td></tr>
    <tr><td>Name</td><td>Julius Ekhator</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Interior secondary suite (basement apartment); optional additional accessory dwelling unit; intends to keep the property</td></tr>'''))

# --- property table 2 (municipality block) ---
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
'''    <tr><td>Municipality</td><td>Town of Innisfil (Simcoe County)</td></tr>
    <tr><td>Neighbourhood</td><td>Alcona (per geocoded location — confirm in Phase 2)</td></tr>
    <tr><td>County</td><td>Simcoe County</td></tr>
    <tr><td>Property Type</td><td>To be confirmed (ADU rules apply to detached, semi-detached and street-townhouse dwellings)</td></tr>
    <tr><td>Waste Collection</td><td>Town of Innisfil / Simcoe County curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Town of Innisfil Comprehensive Zoning By-law 080-13, as amended</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Interior secondary suite (basement) — primary; optional second accessory dwelling unit for up to 3 units total</td></tr>'''))

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
    2178 Nevils Street is in the Town of Innisfil on the west shore of Lake Simcoe in Simcoe County — a fast-growing lakeside community within commuting distance of Barrie and the Greater Toronto Area. (Illustrative context, not a valuation.)
    <ul>
      <li>Alcona is Innisfil's largest settlement area, close to Innisfil Beach Park and the Lake Simcoe waterfront</li>
      <li>Highway 400 provides road access south toward the GTA and north to Barrie</li>
      <li>GO Transit bus service and nearby GO rail connect the area toward Toronto</li>
      <li>Steady rental demand from a growing population and proximity to Barrie-area employment</li>
      <li>Local specifics — servicing, schools, and amenities near the lot — confirmed in Phase 2</li>
    </ul>'''))

# --- zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (Town of Innisfil Comprehensive Zoning By-law 080-13) — exact zone symbol confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be an eligible detached, semi-detached or street-townhouse residential property that meets the Town's accessory-dwelling-unit standards, with adequate servicing. Confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Housing Supply Action Plan (More Homes Built Faster Act / Bill 23), Innisfil amended By-law 080-13 to permit additional (including "third") dwelling units on eligible lots — up to <strong>3 units</strong> total. No rezoning required for a compliant additional residential unit.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite (such as a basement apartment) and a further accessory dwelling unit are permitted on eligible lots, subject to the Town's ADU standards — size, parking, and registration. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> (subject to Phase 2 confirmation); proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means for you" cell list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite:</strong> a self-contained unit inside the existing home, such as a basement apartment — your primary goal</li>
      <li><strong>Additional (Third) Dwelling Unit:</strong> a further unit within, attached to, or detached from the principal dwelling, where the lot qualifies</li>
      <li><strong>Up to 3 units total:</strong> the principal dwelling plus up to two accessory dwelling units on an eligible lot under By-law 080-13, as amended</li>
      <li><strong>Registration required:</strong> accessory dwelling units must be legally constructed and registered with the Town of Innisfil</li>'''))

# --- time-sensitive block ---
R.append(('''  <div class="ts">
    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>''',
'''  <div class="ts">
    <div class="d"><div class="dt">Additional Residential Units — DC Treatment</div><div class="dx">Under Ontario's More Homes Built Faster Act (Bill 23), qualifying additional residential units benefit from development-charge relief. The exact charges (or exemption) that apply to your suite under the Town of Innisfil's current development-charge by-law are confirmed in Phase 2 — no dollar figures are stated here until verified for this lot.</div></div>
    <div class="d"><div class="dt">Register the Suite</div><div class="dx">Accessory dwelling units in Innisfil must be legally constructed and registered with the Town. If any existing work was done without a permit, a retroactive permit and registration are needed before financing or occupancy — worth confirming early.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>'''))

# --- rezoning green box ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended additional residential units are permitted on an eligible lot under Innisfil By-law 080-13, as amended — no rezoning is contemplated for a compliant suite.</div>'))

# --- as-of-right comparison: governing by-law row ---
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 080-13, as amended</td><td class="n">A new site-specific by-law</td></tr>'))

# --- "also permitted" twocard ---
R.append(('''  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="barhead" style="text-align:left;">Also available on an eligible lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Interior secondary suite</div>An in-home unit such as a basement apartment is a permitted accessory dwelling unit under By-law 080-13 on an eligible detached, semi-detached or street-townhouse lot, subject to the Town's standards.</div>
    <div class="card2"><div class="ct">Additional (third) dwelling unit</div>Innisfil permits a further dwelling unit — within, attached to, or detached from the principal dwelling — for up to three units total, subject to size, parking and registration standards.</div>
  </div>'''))

# --- "what this means for <address>" + amber ---
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 2178 Nevils Street</div>
  <p>If the lot qualifies under the Town's accessory-dwelling-unit standards, the recommended secondary suite is permitted without rezoning, and the project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report, was researched from live Town of Innisfil sources, and is subject to technical review of site conditions and confirmation in Phase 2.</p>
  <div class="co-amber"><b>Two items to confirm: the lot's servicing/eligibility and the registration of any suite.</b><br><span class="sub">Eligibility depends on lot type and servicing; every accessory dwelling unit must be legally constructed and registered with the Town. If any work was done without a permit, a retroactive application is needed before financing or development can proceed.</span></div>'''))

# --- development option A ---
R.append(('''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option A — Interior Secondary Suite (your goal)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Illustrative massing"></div>
      <div class="od">A self-contained secondary suite inside the existing home — most commonly a basement apartment — rented for ongoing income while you keep the property. This is your stated goal. It is a permitted accessory dwelling unit on an eligible lot under By-law 080-13, as amended; no rezoning is contemplated. The suite must meet the Town's ADU standards (minimum ceiling heights, a separate entrance, fire/building-code separation, parking and registration) and be registered with the Town. Exact size and layout are confirmed in Phase 2. The massing image is illustrative only.</div>
    </div></div>'''))

# --- development option B ---
R.append(('''  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option B — Secondary Suite + Additional Unit (up to 3 units) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Illustrative massing"></div>
      <div class="od">Pair the interior basement secondary suite with a further accessory dwelling unit — within, attached to, or detached from the home — for up to three units total on the lot under By-law 080-13, as amended. This maximizes rental income while keeping the property in your hands, and matches Julius's interest in a basement unit plus additional space. Innisfil limits a third (accessory) dwelling unit to 50% of the principal dwelling's floor area, up to a maximum of 100 m². Eligibility, parking, and unit sizes are confirmed in Phase 2.</div>
    </div></div>'''))

# --- development option C ---
R.append(('''  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option C — Servicing, Registration &amp; Standards</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Illustrative massing"></div>
      <div class="od">Eligibility for additional residential units depends on lot type and adequate servicing (municipal water/sewer versus private services), and every accessory dwelling unit must be legally constructed and registered with the Town of Innisfil. Confirming the lot's servicing and the permit/registration status of any existing work is an essential first step — both for financing qualification and for counting a suite as a legal unit. If earlier work was done without a permit, a retroactive permit application will be required before any development or financing process can proceed. The massing image is illustrative only.</div>
    </div></div>'''))

# --- development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Secondary Suite (up to 3 units)</div>
  <p>2178 Nevils Street is in the Town of Innisfil, where By-law 080-13 (as amended under Ontario's Bill 23) permits additional residential units — up to three units on an eligible lot — matching your goal of a basement secondary suite while keeping the property. <strong>An interior secondary suite is the clear primary recommendation</strong>, with a further accessory dwelling unit as an optional path to a third income unit. Eligibility is confirmed in Phase 2.</p>'''))

# --- grants table (four Toronto rows -> Innisfil-appropriate rows) ---
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>Additional Residential Unit — Development Charge Relief</td><td>Ontario's More Homes Built Faster Act (Bill 23) provides development-charge relief for qualifying additional residential units. The charges or exemption that apply to your suite under the Town of Innisfil's development-charge by-law are confirmed in Phase 2 — no figure is stated here until verified for this lot.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit worth 15% of up to $50,000 of eligible renovation cost (to a maximum of $7,500) where a self-contained secondary unit is created to house an eligible senior or an adult with a disability. Applicability to your suite is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>May apply to a newly built or substantially renovated rental suite. The enhanced Purpose-Built Rental Housing rebate targets projects of 4+ units, so it is unlikely to apply to a single secondary suite — applicability is confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as the Canada Greener Homes Loan and utility-run incentives may offset efficient design and equipment on a new suite. Availability and eligibility confirmed in Phase 2.</td></tr>'''))

# --- summary: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>2178 Nevils Street confirms a viable development option. Under the Town of Innisfil Comprehensive Zoning By-law 080-13 (as amended under Ontario's Bill 23), up to <strong>three residential units are permitted on an eligible lot</strong> — including the interior secondary suite you're after — with no rezoning required, subject to the Town's ADU standards. Because these rules were researched from live municipal sources rather than a pre-verified engine, the zoning and incentive specifics should be double-checked in Phase 2.</p>
  <ul>
    <li><strong>The Secondary-Suite Advantage:</strong> an in-home basement suite (and, optionally, a further accessory dwelling unit) adds rental income while you keep the property — no rezoning, no public hearing, no Council approval required for a compliant suite. Size, parking, and registration are confirmed in Phase 2.</li>
  </ul>'''))

# ---- apply, asserting each pattern matches exactly once ----
fails = 0
for i, (old, new) in enumerate(R):
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] pattern #{i}: {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# ---- leftover scan: zero references to the source city/lead/programs ----
leftovers = ["Coxwell", "Arockiaraj", "johneeraj", "Toronto", "Ward 19", "Beaches",
             "Woodbine", "Greenwood", "TTC", "654-2025", "569-2013", "474-2023",
             "Bill 185", "6+1", "4+1", "houseplex", "garden suite", "Garden Suite",
             "nine wards", "Gerrard", "Danforth", "315.9", "M4L", "multiplex", "Multiplex"]
print("---- leftover scan ----")
any_left = False
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        any_left = True
if not any_left:
    print("clean — no source-city/lead/program leftovers")
print(f"done. fails={fails}  wrote={OUT}")
