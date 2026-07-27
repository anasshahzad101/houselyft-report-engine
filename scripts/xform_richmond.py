"""
xform_richmond.py — master (303 Coxwell, Toronto) -> 7200 Bridge Street, Richmond BC.

Richmond BC has no zoning-engine adapter, so its rules were researched live from
official sources (THE PRIME RULE) and the report is tagged report-needs-review:
  - BC Bill 44 SSMUH (2023) -> City of Richmond Bylaw 10573 (adopted 24 Jun 2024)
    rezoned ~27,000 single-family/duplex lots to new RSM sub-zones under Zoning
    Bylaw 8500 s.8.19. RSM height raised 9m -> 10m (March 2025).
  - RSM tiers: RSM/S (lot <=280 m2) = 3 units; RSM/M & RSM/L (larger lots not
    within 400 m of a prescribed frequent-transit stop) = 4 units; RSM/XL
    (>280 m2 within 400 m of a prescribed frequent-transit stop) = up to 6 units.
  - FAR 0.6 on first 464.5 m2 + 0.3 on balance; max lot coverage 45%; height 10 m;
    zero off-street parking within 400 m of a prescribed frequent-transit stop.
  Sources: richmond.ca Provincial Housing Legislation / SSMUH pages + Zoning
  Bylaw 8500 s.8.19 (RSM). Geocode: OSM (49.1577, -123.1170, central Richmond /
  City Centre, Canada Line corridor). Exact RSM sub-zone + City Centre Area Plan
  upside are Phase-2 confirms.

Imagery: engine/aerial_imagery.get_aerial() returns nothing for Richmond (no
verified-licence BC municipal source for this city), so per the imagery doctrine
the empty aerial/street placeholders are removed and one honest line is kept.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates")
src = open(os.path.join(TPL, "report_houselyft_master.html")).read()

R = []

# --- cover address ---
R.append((
    '<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
    '<div class="addr">7200 Bridge Street<span>Richmond, BC</span></div>'))

# --- property details barhead ---
R.append((
    '<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
    '<div class="barhead">7200 Bridge Street, Richmond, BC&nbsp;&nbsp;V6Y 2S7</div>'))

# --- imagery block: aerial resolver returned nothing -> honest line (step 4b) ---
R.append((
    '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
    '''  <div style="font-size:8pt;color:#7a818f;margin:0 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# --- property details: contact table ---
R.append((
    '''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
    '''    <tr><td>Property Address</td><td>7200 Bridge Street, Richmond, BC&nbsp;&nbsp;V6Y 2S7</td></tr>
    <tr><td>Name</td><td>Nissim Samuel</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — maximize unit count under BC's SSMUH / Richmond RSM rules</td></tr>'''))

# --- property details: municipal table ---
R.append((
    '''    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 — Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m² (20 ft × 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>''',
    '''    <tr><td>Municipality</td><td>City of Richmond (Metro Vancouver Regional District)</td></tr>
    <tr><td>Region</td><td>Metro Vancouver, BC</td></tr>
    <tr><td>Neighbourhood</td><td>Central Richmond — City Centre / Canada Line corridor</td></tr>
    <tr><td>Current Zoning</td><td>Small-Scale Multi-Unit Housing (RSM) — Zoning Bylaw 8500 §8.19; exact RSM sub-zone confirmed in Phase 2</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–6 units) under RSM, subject to lot size &amp; transit proximity</td></tr>'''))

# --- Neighbourhood Spotlight ---
R.append((
    '''    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
    '''    7200 Bridge Street sits in central Richmond, within the City Centre / Canada Line corridor — one of Metro Vancouver's most transit-connected and rapidly intensifying communities:
    <ul>
      <li>Central Richmond location with quick access to the Canada Line, Richmond–Brighouse and Aberdeen stations, and downtown Vancouver via rapid transit</li>
      <li>Proximity to a prescribed frequent-transit stop is the key factor in whether up to six units are permitted under Richmond's RSM zoning — confirmed in Phase 2</li>
      <li>Chronically tight Metro Vancouver rental market — supportive of a hold-and-rent strategy</li>
      <li>Established single-family / duplex streets now opened to gentle density by provincial SSMUH rules and Richmond's RSM zones</li>
      <li>Note: the City Centre Area Plan may support additional height/density on some lots through a separate rezoning — explored in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- Section 2: zoning kv table ---
R.append((
    '''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>''',
    '''    <tr><td>Current Zoning</td><td>Small-Scale Multi-Unit Housing (RSM) — City of Richmond Zoning Bylaw 8500 §8.19, applied to formerly single-family / duplex lots. Exact RSM sub-zone confirmed in Phase 2.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>RSM sub-zones scale with lot size and transit proximity: RSM/S (lots ≤280 m²) → 3 units; RSM/M &amp; RSM/L (larger lots not within 400 m of a prescribed frequent-transit stop) → 4 units; RSM/XL (lots &gt;280 m² within 400 m of a prescribed frequent-transit stop) → up to 6 units.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023), Richmond adopted Bylaw 10573 (June 24, 2024) rezoning ~27,000 single-family / duplex lots to the new RSM zones. RSM building height was raised from 9 m to 10 m in March 2025. <strong>3 to 6 units</strong> are now permitted as-of-right — no rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex, fourplex, and (within 400 m of a prescribed frequent-transit stop) up to a six-unit multiplex — plus secondary suites. FAR 0.6 on the first 464.5 m² and 0.3 on the balance; max lot coverage 45%; max height 10 m. Confirmed in Phase 2.</td></tr>'''))

# --- Section 2: "What this means" list ---
R.append((
    '''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
    '''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under Richmond's RSM zoning, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units (RSM/XL) where the lot is &gt;280 m² and within ~400 m of a prescribed frequent-transit stop</li>
      <li><strong>Small Apartment / Townhouse forms:</strong> multi-unit attached or stacked housing within the RSM building envelope</li>
      <li><strong>Secondary Suites:</strong> a secondary suite can be paired with the principal dwelling to add density — confirmed in Phase 2</li>'''))

# --- Time-Sensitive Information ---
R.append((
    '''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
    '''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% GST rebate on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Richmond RSM Zoning<br><small>in force</small></div><div class="dx">Richmond's RSM small-scale multi-unit zoning (Zoning Bylaw 8500 §8.19, adopted June 2024; height raised to 10 m in March 2025) permits 3–6 units as-of-right depending on lot size and transit proximity. The applicable sub-zone and site standards for this lot are confirmed against Richmond's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">No minimum off-street parking is required for RSM lots within ~400 m of a prescribed frequent-transit stop. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))

# --- Section 3: Rezoning (Toronto-specific comparison -> BC/RSM) ---
R.append((
    '''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>
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
    '''  <div class="co-green"><div class="ct2">Not Required for a 3–6 Unit Multiplex</div>Under BC's SSMUH rules and Richmond's RSM zoning (Zoning Bylaw 8500 §8.19), a 3–6 unit multiplex is permitted as-of-right — no rezoning and no public hearing.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right (RSM)</th><th>If Rezoning Were Pursued</th></tr>
    <tr><td>Change to the zoning bylaw</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 8500 §8.19 (RSM)</td><td class="n">A new site-specific bylaw</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Possible additional upside on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit multiplex (RSM/XL)</div>Where the lot is &gt;280 m² and within ~400 m of a prescribed frequent-transit stop, Richmond's RSM/XL sub-zone permits up to six units without rezoning.</div>
    <div class="card2"><div class="ct">City Centre Area Plan</div>This lot sits in Richmond's City Centre / Canada Line corridor, where the Area Plan may support additional height and density through a separate rezoning — a longer path, explored in Phase 2.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 7200 Bridge Street</div>
  <p>Because Richmond's RSM zoning already permits a 3–6 unit multiplex under existing rules, no rezoning application is required for the recommended build — your project can advance directly to design and permitting. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the lot's RSM sub-zone (its area and distance to a prescribed frequent-transit stop).</b><br><span class="sub">That is what sets the unit ceiling at 3, 4, or 6 — confirmed in Phase 2.</span></div>'''))

# --- Section 4: Option A ---
R.append((
    '''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
    '''  <div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A triplex or fourplex built directly on the lot — the baseline RSM entitlement on a serviced Richmond residential lot, with no rezoning or public hearing. On lots ≤280 m² the minimum is three units (RSM/S); on larger lots not near frequent transit the minimum is four units (RSM/M or RSM/L). Buildable size is governed by the RSM standards — FAR 0.6 on the first 464.5 m² and 0.3 on the balance, 45% lot coverage, and a 10 m height limit — confirmed in Phase 2.</div>'''))

# --- Section 4: Option B ---
R.append((
    '''  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
    '''  <div class="opt"><div class="oh">Option B — Six-Unit Multiplex (RSM/XL, near frequent transit) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">Where the lot is greater than 280 m² and within roughly 400 m of a prescribed frequent-transit stop, Richmond's RSM/XL sub-zone permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. This matches Nissim's stated multiplex-development goal. Confirming the lot's area and transit distance is the first gating step, since it is what unlocks the six-unit tier. No minimum off-street parking applies within the transit radius. Confirmed in Phase 2.</div>'''))

# --- Section 4: Option C ---
R.append((
    '''  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
    '''  <div class="opt"><div class="oh">Option C — Lower-Complexity Entry (principal dwelling + secondary suite)</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">A lower-complexity path: keep or rebuild the principal dwelling and add a secondary suite for immediate rental income while a larger RSM multiplex is designed and financed. This is often the fastest route to cashflow and can be paired later with the multiplex path. Suite size and siting are confirmed in Phase 2.</div>'''))

# --- Section 5: Development Goal Summary ---
R.append((
    '''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
    '''  <div class="barhead" style="text-align:left;">Multiplex under RSM (up to 6 units)</div>
  <p>7200 Bridge Street is a Richmond RSM lot opened to gentle density by BC's SSMUH rules — 3 to 6 units as-of-right depending on lot size and transit proximity. <strong>Where the lot qualifies for the six-unit RSM/XL tier, a six-unit multiplex is the clear primary recommendation</strong>; a triplex/fourplex is the reliable fallback, and a principal-dwelling-plus-suite is the fastest entry.</p>'''))

# --- Section 6: Financing — inject CMHC MLI Select row (BC program set) ---
R.append((
    '''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>''',
    '''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <tr><td>CMHC MLI Select</td><td>Government-backed multi-unit mortgage insurance for projects of 5+ rental units. It does not act as a direct grant, but heavily subsidizes project costs — cutting insurance premiums and extending amortizations up to 50 years on a points system rewarding affordability, energy efficiency, and accessibility. Confirmed in Phase 2.</td></tr>'''))

# --- Section 7: Grants — inject BC gated rows (all sourced + hedged) ---
R.append((
    '''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>''',
    '''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental (construction generally before 2031). Applies in BC. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / ACLP</td><td>MLI Select multi-unit mortgage insurance (5+ rental units) and the Apartment Construction Loan Program (low-interest construction financing, min $1M) — national programs that heavily subsidize a qualifying rental project. Confirmed in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>Forgivable loan reported up to $40,000 toward a new secondary suite rented below market for a set term. Eligibility and current status confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by municipality. Confirmed against Richmond's current bylaw in Phase 2.</td></tr>'''))

# --- Section 8: Summary — Current Zoning Review ---
R.append((
    '''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
    '''  <p>7200 Bridge Street is a Richmond lot now covered by the province's SSMUH framework and the City's RSM zoning (Zoning Bylaw 8500 §8.19). It is eligible for <strong>3 to 6 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and distance to a prescribed frequent-transit stop.</p>
  <ul>
    <li><strong>The SSMUH / RSM Advantage:</strong> the single most valuable step is confirming lot size and transit distance, since that is what unlocks the six-unit RSM/XL tier — established in Phase 2.</li>
  </ul>'''))

# ---- apply ----
fails = 0
for old, new in R:
    c = src.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        src = src.replace(old, new)

# ---- leftover guard: no source-city / wrong-city content may survive ----
leftovers = ["Coxwell", "John Arockiaraj", "Toronto", "Ontario", "Ward 19",
             "654-2025", "474-2023", "Bill 185", "569-2013", "TTC", "Beaches",
             "Gerrard", "Danforth", "Greenwood", "OLT", "M4L", "Saanich",
             "Hastings", "garden suite", "Garden Suite"]
for t in leftovers:
    n = src.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

out = os.path.join(TPL, "report_richmond.html")
if fails == 0:
    open(out, "w").write(src)
    print(f"OK wrote {out}  (fails={fails})")
else:
    print(f"NOT WRITTEN — {fails} replacement(s) failed")
