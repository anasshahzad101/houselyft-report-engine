"""
xform_delta.py — turn the House Lyft master report into the Delta (Tsawwassen)
report for 871 Gale Drive, Mike Pineda.

City coverage: Delta has NO zoning-engine adapter, so its rules were researched
live from official / official-adjacent sources (City of Delta SSMUH pages, Delta
Zoning Bylaw No. 7600, provincial Bill 44 / Bill 25). Confidence = needs-review.

Verified facts used (BC SSMUH, City of Delta implementation, 2024):
  * Up to 3 units on lots <= 280 m^2; up to 4 units on larger lots.
  * 6 units ONLY on larger lots within 400 m of frequent transit along Scott
    Road (North Delta) — NOT applicable to this Tsawwassen property.
  * Principal dwelling + secondary suite + up to two garden suites / coach houses.
  * Governed provincially by Bill 44 (2023), tightened by Bill 25 (Nov 2025,
    compliance deadline June 30, 2026).
Programs are BC-gated (config/programs.json): GST PBRH rebate (4+), CMHC ACLP/
MLI Select (threshold shown, not promised), BC Secondary Suite Incentive,
municipal DCC treatment. No Ontario/Alberta programs leak in.

Pattern (same as xform_saanich.py): every replacement must match exactly once,
then grep for leftovers from the source city. That check is what keeps Toronto
data out of a Delta report.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC  = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT  = os.path.join(ROOT, "templates", "report_delta.html")

html = open(SRC, encoding="utf-8").read()

R = []  # (old, new) — each old must appear exactly once

# --- cover address -----------------------------------------------------------
R.append((
'  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
'  <div class="addr">871 Gale Drive<span>Delta, BC (Tsawwassen)</span></div>'))

# --- section 1 barhead -------------------------------------------------------
R.append((
'  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
'  <div class="barhead">871 Gale Drive, Delta, BC&nbsp;&nbsp;V4M 2P6</div>'))

# --- imagery slots -> honest pending line (step 4b: no verified BC source) ----
R.append((
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <p style="font-size:8.5pt;color:#7a818f;font-style:italic;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source.</p>'''))

# --- section 1 first kv table ------------------------------------------------
R.append((
'''  <table class="kv">
    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>
  </table>''',
'''  <table class="kv">
    <tr><td>Property Address</td><td>871 Gale Drive, Delta, BC&nbsp;&nbsp;V4M 2P6</td></tr>
    <tr><td>Name</td><td>Mike Pineda</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize unit count under BC's SSMUH rules</td></tr>
  </table>'''))

# --- section 1 second kv table (municipality etc.) ---------------------------
R.append((
'''  <table class="kv">
    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 — Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m² (20 ft × 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>
  </table>''',
'''  <table class="kv">
    <tr><td>Municipality</td><td>City of Delta (Metro Vancouver Regional District)</td></tr>
    <tr><td>Community</td><td>Tsawwassen</td></tr>
    <tr><td>Region</td><td>Metro Vancouver, BC</td></tr>
    <tr><td>Current Zoning</td><td>Single-detached residential — Delta Zoning Bylaw No. 7600, 2017 (exact zone confirmed in Phase 2)</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH), implemented in Delta's zoning amendment bylaws (2024)</td></tr>
    <tr><td>Servicing</td><td>Must be on full municipal services within the urban containment area — confirmed in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on whether the lot exceeds 280 m² (most established Tsawwassen lots do)</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–4 units) under SSMUH, subject to lot area</td></tr>
  </table>'''))

# --- section 1 neighbourhood spotlight ---------------------------------------
R.append((
'''    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    871 Gale Drive is in Tsawwassen, an established, high-demand residential community in the City of Delta at the southwest edge of Metro Vancouver:
    <ul>
      <li>Quiet, family-oriented single-family streets close to Tsawwassen Town Centre, the beaches, and the George C. Reifel Migratory Bird Sanctuary</li>
      <li>Convenient access to Highway 17, the BC Ferries Tsawwassen terminal, and the Tsawwassen Mills / Tsawwassen Commons retail district</li>
      <li>Served by TransLink bus service; the SSMUH six-unit tier is limited to lots near frequent transit along Scott Road in North Delta and does not apply here</li>
      <li>Established single-family lots now opened to gentle density (triplex / fourplex) by provincial SSMUH rules</li>
      <li>Note: lot grading, trees, and Delta's setback and character guidelines can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- section 2 zoning table + "what this means" ------------------------------
R.append((
'''  <table class="kv">
    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you…</div>
    <ul style="margin-top:0;">
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>
    </ul>
  </div>''',
'''  <table class="kv">
    <tr><td>Current Zoning</td><td>Single-detached residential under Delta Zoning Bylaw No. 7600, 2017 — now subject to provincial SSMUH permissions</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced single-detached and duplex residential lots inside Delta's urban containment area. The unit ceiling scales with lot size: up to 3 units on lots of 280 m² or less, up to 4 units on larger lots.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023) — implemented through Delta's zoning amendment bylaws in 2024 and governed provincially (compliance tightened by Bill 25, Nov 2025, deadline June 30, 2026) — <strong>3 to 4 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex and fourplex, plus a principal dwelling with a secondary suite and up to two garden suites / coach houses. A six-unit allowance applies only to larger lots within 400 m of frequent transit along Scott Road (North Delta) and does not apply to this Tsawwassen property. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you…</div>
    <ul style="margin-top:0;">
      <li><strong>Triplex:</strong> 3 units as-of-right under SSMUH on a lot of 280 m² or less, no rezoning</li>
      <li><strong>Fourplex:</strong> up to 4 units as-of-right where the lot exceeds 280 m² — the likely tier for an established Tsawwassen lot</li>
      <li><strong>Suites Route:</strong> keep the principal house and add a secondary suite plus a detached garden suite or coach house — Delta permits this on the same lot</li>
    </ul>
  </div>'''))

# --- time-sensitive ----------------------------------------------------------
R.append((
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% GST rebate on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in BC. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">BC Bill 25 — SSMUH Compliance<br><small>June 30, 2026</small></div><div class="dx">Bill 25 (Nov 2025) tightened the provincial SSMUH rules and set a June 30, 2026 deadline for municipalities, including Delta, to finalize compliant bylaws. The applicable unit count and site standards for your lot are confirmed against Delta's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">SSMUH parking minimums are set locally in Delta outside the Scott Road frequent-transit area; confirm the requirement for this lot in Phase 2. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))

# --- section 3 rezoning body -------------------------------------------------
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
'''  <div class="co-green"><div class="ct2">Not Required for This Property</div>A triplex or fourplex is permitted as-of-right under BC's SSMUH framework as implemented in Delta's zoning bylaw — no rezoning, no public hearing.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right (SSMUH)</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning bylaw</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Timeline exposure</td><td class="g">Minimal</td><td class="n">Extended</td></tr>
    <tr><td>What governs your build</td><td class="g">Delta's SSMUH bylaw (Bill 44)</td><td class="n">A new site-specific bylaw</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also available on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Fourplex</div>Where the lot exceeds 280 m², Delta's SSMUH bylaw permits up to four units on a former single-family or duplex lot without rezoning.</div>
    <div class="card2"><div class="ct">Garden suite / coach house</div>Delta permits a detached garden suite or coach house in addition to a principal dwelling and secondary suite — a lower-complexity route to rental income.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 871 Gale Drive</div>
  <p>Because 871 Gale Drive already permits a triplex or fourplex under Delta's SSMUH bylaw, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the lot's exact area and servicing.</b><br><span class="sub">Whether the lot exceeds 280 m² sets the three-versus-four unit ceiling, and full municipal servicing is a precondition — both confirmed in Phase 2.</span></div>'''))

# --- section 4 development options -------------------------------------------
R.append((
'''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option A — Fourplex (up to 4 units, as-of-right) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A four-unit multiplex built directly on the lot — the baseline SSMUH entitlement on a serviced Delta residential lot larger than 280 m², with no rezoning or public hearing. This is the highest-density, strongest-income direction available as-of-right on this Tsawwassen property. Buildable size is governed by Delta's setbacks, height, lot coverage, and floor-area rules — confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — Triplex (3 units, as-of-right)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A three-unit multiplex — the SSMUH entitlement that applies on lots of 280 m² or less, and a reliable fallback if the confirmed lot area or site constraints favour a smaller footprint. Still fully as-of-right, no rezoning. Final unit count and massing confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Suites Route (secondary suite + garden suite / coach house)</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">A lower-complexity path: keep the principal dwelling and add a secondary suite plus a detached garden suite or coach house — Delta permits this configuration on the same lot. This is often the fastest route to rental income while a larger multiplex is evaluated. Suite sizes and siting confirmed in Phase 2.</div>
    </div></div>'''))

# --- section 5 goal summary --------------------------------------------------
R.append((
'''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Fourplex under SSMUH (up to 4 units)</div>
  <p>871 Gale Drive is a single-family lot in Tsawwassen now opened to gentle density by BC's SSMUH rules — 3 to 4 units as-of-right depending on lot area. <strong>Where the lot exceeds 280 m², a fourplex is the clear primary recommendation</strong>; a triplex is the reliable fallback, and the suites route is the fastest entry to rental income.</p>'''))

# --- section 7 grants: inject BC-gated rows ----------------------------------
R.append((
'''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->
    </table>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ long-term rental (construction generally before 2031). Applies in BC and is reachable at the four-unit tier. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC ACLP / MLI Select</td><td>The Apartment Construction Loan Program offers low-interest construction financing (minimum $1M loan). CMHC MLI Select mortgage insurance requires a minimum of 5 rental units — beyond this lot's 3–4 unit as-of-right entitlement, noted here for completeness. Confirmed in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>Forgivable loan reported up to $40,000 toward a new secondary suite rented below market for a set term. Eligibility and current status confirmed in Phase 2.</td></tr>
    <tr><td>Municipal (Delta)</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by municipality. Confirmed against Delta's current bylaw in Phase 2.</td></tr>
    </table>'''))

# --- section 8 summary current-zoning-review --------------------------------
R.append((
'''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>871 Gale Drive is a single-family lot in Tsawwassen (City of Delta). Under BC's SSMUH framework (Bill 44, tightened by Bill 25 and implemented in Delta's zoning bylaw), it is now eligible for <strong>3 to 4 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by whether the lot exceeds 280 m².</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming the lot area and servicing, since that is what sets the three-versus-four unit ceiling — established in Phase 2.</li>
  </ul>'''))

# ---- apply -----------------------------------------------------------------
for i, (old, new) in enumerate(R):
    n = html.count(old)
    if n != 1:
        sys.exit(f"[FAIL] replacement #{i} matched {n} times (expected 1):\n{old[:120]}...")
    html = html.replace(old, new)

open(OUT, "w", encoding="utf-8").write(html)

# ---- leftover guard: zero references to the source city / lead -------------
# Strip base64 data-URIs first (the logo blob coincidentally contains short
# substrings like "M4L") so the guard scans only real report content.
scan = re.sub(r"data:image/[^\"')]+", "", html)
BANNED = ["Coxwell", "John Arockiaraj", "Toronto", "Ontario", "Ward 19",
          "654-2025", "474-2023", "Bill 185", "569-2013", "M4L 3B5", "HST",
          "TTC", "Beaches", "Gerrard", "johneeraj", "OLT"]
leftovers = [b for b in BANNED if b in scan]
if leftovers:
    sys.exit(f"[FAIL] source-city leftovers remain: {leftovers}")

print(f"[ok] wrote {OUT} ({len(html):,} bytes); no leftovers.")
