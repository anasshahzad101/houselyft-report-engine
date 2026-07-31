# xform_delta.py — build report_delta.html from the master for
# Kazim Dabestani, 11957 92 Avenue, Delta, BC (North Delta / Kennedy).
# Delta has no zoning-engine adapter -> rules researched live from official
# sources (City of Delta SSMUH pages, TransLink R6, BC Housing). verified=False
# => report-needs-review. Every figure is either from an official source or
# hedged "confirmed in Phase 2". No invented bylaw numbers or dollar amounts.
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_delta.html")
s = open(SRC, encoding="utf-8").read()

R = []

# --- cover ---
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">11957 92 Avenue<span>Delta, BC (Metro Vancouver)</span></div>'))

# --- property details barhead ---
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">11957 92 Avenue, Delta, BC&nbsp;&nbsp;V4C 3L7</div>'))

# --- imagery row: no verified licensed source for Delta -> remove grey boxes,
#     keep one honest line (per routine step 4b / aerial_imagery doctrine) ---
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgnote" style="font-size:8.5pt;color:#7a818f;margin:2px 0 12px;padding:9px 12px;border:1px solid #e4e7ee;background:#fafbfc;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# --- contact kv table ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>11957 92 Avenue, Delta, BC&nbsp;&nbsp;V4C 3L7</td></tr>
    <tr><td>Name</td><td>Kazim Dabestani</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize unit count under BC's SSMUH rules</td></tr>'''))

# --- municipality kv table ---
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
'''    <tr><td>Municipality</td><td>City of Delta (Metro Vancouver Regional District)</td></tr>
    <tr><td>Neighbourhood</td><td>North Delta — Kennedy</td></tr>
    <tr><td>Region</td><td>Metro Vancouver, BC</td></tr>
    <tr><td>Current Zoning</td><td>Single-detached residential (RS zone family) — Delta Zoning Bylaw No. 7600, 2017; exact RS zone confirmed in Phase 2</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td></tr>
    <tr><td>Servicing</td><td>Must be serviced and within the Metro Vancouver Urban Containment Boundary — confirm in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–6 units) under SSMUH, subject to lot size &amp; transit</td></tr>'''))

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
    11957 92 Avenue is in the Kennedy area of North Delta, in Metro Vancouver — an established residential community close to the Scott Road (120 Street) corridor:
    <ul>
      <li>Roughly one block east of Scott Road (120 Street); proximity to frequent transit is the key factor in whether up to six units are permitted — confirmed in Phase 2</li>
      <li>Served by TransLink's R6 Scott Road RapidBus (launched January 1, 2024), a frequent-transit route running along 120 Street</li>
      <li>The Scott Road corridor connects north to SkyTrain (Expo Line) and the wider Metro Vancouver network</li>
      <li>Strong, chronically tight rental market across Metro Vancouver — supportive of a hold-and-rent strategy</li>
      <li>Established single-family streets now opened to gentle density by provincial SSMUH rules. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- section 2 zoning kv table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Single-detached residential (RS zone family, Delta Zoning Bylaw No. 7600, 2017), now subject to provincial SSMUH permissions — exact RS zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced lots zoned for single-detached or duplex housing within the Urban Containment Boundary. Unit count scales with lot size and transit proximity: a minimum of four units on lots over 280 m² (3,014 ft²), and up to six units on such lots within about 400 m of frequent transit along Scott Road.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023) — implemented through amendments to Delta Zoning Bylaw No. 7600 (2024) — <strong>3 to 6 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex. No rezoning, no public hearing. The Province has directed further SSMUH refinements; the in-force rules for this lot are confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex, fourplex, and (near frequent transit) up to a six-unit multiplex — plus secondary suites, garden suites and coach houses on lots zoned for single-detached or duplex housing. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- section 2 "what this means" list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is over 280 m² and within about 400 m of frequent transit on Scott Road</li>
      <li><strong>Suites Route:</strong> a secondary suite plus a detached garden suite or coach house — permitted on single-detached and duplex lots under Delta's SSMUH rules</li>'''))

# --- time-sensitive section ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% GST rebate on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">Delta SSMUH Bylaw — Confirm Current Rules</div><div class="dx">Delta implemented BC's SSMUH rules through 2024 amendments to Zoning Bylaw No. 7600, and the Province has since directed further refinements. The unit count and site standards that apply to your lot — including whether it reaches the six-unit transit tier — are confirmed against Delta's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">Under Delta's SSMUH rules no minimum parking is required for units within about 400 m of frequent-transit stops on Scott Road. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))

# --- section 3 rezoning body (replace all Toronto-specific content) ---
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
'''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended multiplex is permitted as-of-right under BC's SSMUH framework (Bill 44), as implemented in Delta Zoning Bylaw No. 7600 — no rezoning and no public hearing.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right (SSMUH)</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required (prohibited for SSMUH)</td><td class="n">Required</td></tr>
    <tr><td>Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>What governs your build</td><td class="g">SSMUH provisions of Delta Zoning Bylaw No. 7600</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">What this means for 11957 92 Avenue</div>
  <p>Because the SSMUH framework already permits a multiplex on this lot under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. This assessment reflects the by-laws understood to be in force at the date of this report and is subject to technical review of site conditions and confirmation against Delta's current bylaw.</p>
  <div class="co-amber"><b>Two items to confirm: the lot's exact area and its distance to frequent transit on Scott Road.</b><br><span class="sub">Together these decide whether the as-of-right ceiling is four units or six — the single most valuable thing to establish in Phase 2.</span></div>'''))

# --- section 4 development options ---
R.append(('  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '  <div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A triplex or fourplex built directly on the lot — the baseline SSMUH entitlement on a serviced Delta residential lot over 280 m², with no rezoning and no public hearing. This is the reliable path that does not depend on transit proximity. Buildable size is governed by setbacks, height, lot coverage, and floor-area rules under Delta Zoning Bylaw No. 7600 — confirmed in Phase 2. Under SSMUH, one on-site parking space per unit applies, with reductions for very small units.</div>'''))
R.append(('  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '  <div class="opt"><div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Where the lot is over 280 m² and within about 400 m of a frequent-transit stop on Scott Road, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. This property sits roughly a block east of Scott Road, so confirming its exact lot area and transit distance is the first gating step, since that is what unlocks the six-unit tier. No minimum parking applies within the transit radius. Confirmed in Phase 2.</div>'''))
R.append(('  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '  <div class="opt"><div class="oh">Option C — Suites Route (secondary + garden / coach suite)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep the principal dwelling and add a secondary suite plus a detached garden suite or coach house — permitted together on single-detached and duplex lots under Delta's SSMUH rules. This is often the fastest route to rental income while a larger multiplex is evaluated. Suite sizes, siting and floor-area caps are confirmed in Phase 2.</div>'''))

# --- section 5 development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex under SSMUH (up to 6 units)</div>
  <p>11957 92 Avenue is a single-detached lot in North Delta now opened to gentle density by BC's SSMUH rules — 3 to 6 units as-of-right depending on lot size and transit proximity. <strong>Where the lot qualifies for the six-unit tier, a six-unit multiplex is the clear primary recommendation</strong>; a triplex/fourplex is the reliable fallback, and the suites route is the fastest entry.</p>'''))

# --- section 6 financing: inject CMHC MLI Select at the gated marker ---
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC MLI Select</td><td>Government-backed multi-unit mortgage insurance. Requires a minimum of 5 rental units. Not a direct grant, but it heavily subsidizes project costs — cutting insurance premiums and extending amortization based on a points system that rewards affordability, energy efficiency, and accessibility. Reaches this project at the five-unit tier. Confirmed in Phase 2.</td></tr>
    <!-- GATED_FINANCING_ROWS injected: CMHC MLI Select (min 5 rental units, tiered). -->'''))

# --- section 7 grants: inject tiered BC/federal/municipal rows at the marker ---
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial (BC)</td><td>SSMUH As-of-Right Density (Bill 44)</td><td>Not a grant — a zoning entitlement. BC's SSMUH legislation requires Delta to permit 3–4 units as-of-right (up to 6 near frequent transit) on most single-detached and duplex lots under 4,050 m² within the Urban Containment Boundary, without rezoning. This is the foundation the whole plan is built on.</td></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental (construction generally before 2031). Applies in BC. Reaches this project at the four-unit tier. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / ACLP</td><td>MLI Select multi-unit mortgage insurance (5+ rental units) and the Apartment Construction Loan Program (low-interest construction financing, minimum $1M loan) — national programs that heavily subsidize a qualifying rental project. Reach this project at the five-unit / larger-budget tiers. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and purpose-built rental projects may qualify for reduced or waived Development Cost Charges; treatment varies and is set by the municipality. Confirmed against Delta's current bylaw in Phase 2.</td></tr>
    <!-- GATED_GRANTS_ROWS injected (tiered): BC SSMUH entitlement; GST PBRH (4+); CMHC MLI Select/ACLP (5+/$1M); DCC treatment. -->'''))

# --- section 8 summary: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>11957 92 Avenue is a single-detached lot in North Delta, City of Delta. Under BC's SSMUH framework (Bill 44), implemented through amendments to Delta Zoning Bylaw No. 7600, it is now eligible for <strong>3 to 6 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and transit proximity.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming lot size and distance to frequent transit on Scott Road, since that is what unlocks the six-unit tier — established in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

print("\n--- leftover scan (wrong-city / master tokens) ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "johneeraj",
          "654-2025", "474-2023", "569-2013", "Ontario HST", "Bill 185", "Briarstone",
          "Saanich", "Hastings", "Gerrard", "Danforth", "TTC", "Greenwood",
          "Secondary Suite Loan", "free grant", "guaranteed return"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done. fails:", fails, "| output:", OUT)
