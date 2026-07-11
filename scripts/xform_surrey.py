"""
xform_surrey.py — adapt the House Lyft master into the report for
62 Surrey Avenue, Scarborough (Toronto) — Kaman Brideash.

Same city as the master (Toronto), but Ward 21 (Scarborough Centre) is NOT one
of the nine six-unit wards, so the as-of-right ceiling is 4 units city-wide
(By-law 474-2023), not 6. The intake goal is a garden suite / ADU. Every
six-unit / Ward-19 / By-law 654-2025 claim is recast to the 4-unit reality,
and the master's invented Coxwell property specifics (garage, lot size, corner
frontage) are replaced with the confirm-phrase per the accuracy contract.

House Lyft prose sections stay verbatim; only property / zoning / market /
imagery content changes. Assert-once + leftover grep mirror the other xforms.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates", "report_surrey.html")

s = open(TPL, encoding="utf-8").read()
R = []

# ---- cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">62 Surrey Avenue<span>Scarborough (Toronto), ON</span></div>'))

# ---- property details barhead ----------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">62 Surrey Avenue, Scarborough, Toronto, ON&nbsp;&nbsp;M1R 1G4</div>'))

# ---- imagery (real aerial + real licence credit) ---------------------------
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="padding:0;overflow:hidden;background:#000;"><img src="aerial_surrey.jpg" alt="Aerial view of 62 Surrey Avenue, Scarborough" style="width:100%;height:100%;object-fit:cover;display:block;"></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street-level view<br><small>provided in Phase&nbsp;2</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Aerial: City of Toronto Orthophoto 2025 (8&nbsp;cm), approx. 90&nbsp;m across. Contains information licensed under the Open Government Licence – Toronto.</div>'''))

# ---- property table 1 (contact + goals) ------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>62 Surrey Avenue, Scarborough, Toronto, ON&nbsp;&nbsp;M1R 1G4</td></tr>
    <tr><td>Name</td><td>Kaman Brideash</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Garden suite / laneway home / ADU (per intake); scope to be decided</td></tr>'''))

# ---- property table 2 (municipal / lot) ------------------------------------
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
'''    <tr><td>Municipality</td><td>City of Toronto (Scarborough)</td></tr>
    <tr><td>Neighbourhood</td><td>Wexford</td></tr>
    <tr><td>Ward</td><td>Ward 21 — Scarborough Centre</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Zone</td><td>RD (x288) — Residential Detached (exception 900.3.10(288))</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite / ADU (primary); interior secondary suite as optional add</td></tr>'''))

# ---- neighbourhood spotlight -----------------------------------------------
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
    62 Surrey Avenue is in the Wexford neighbourhood of Scarborough, within the City of Toronto — an established, primarily residential east-end community:
    <ul>
      <li>Settled residential streets of detached homes — the kind of stable stock that rents well and holds value</li>
      <li>Served by TTC surface transit with connections toward the Line&nbsp;2 subway; exact routes and schedules confirmed in Phase 2</li>
      <li>Close to schools, parks, and the retail corridors along Lawrence Avenue East and the Victoria Park / Warden avenues</li>
      <li>Steady east-end rental demand supports an added suite or multiplex units</li>
      <li>(Illustrative neighbourhood context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table ----------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD (x288) — Residential Detached (Toronto Zoning By-law 569-2013, exception 900.3.10(288))</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. This is a serviced residential lot within the City of Toronto — the setting for the city-wide multiplex and garden-suite permissions below. Site-specific standards (setbacks, height, coverage) are confirmed during the feasibility phase.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide in Toronto (By-law 474-2023). Ward 21 (Scarborough Centre) is not among the wards carrying the six-unit permission, so the as-of-right ceiling here is 4 units. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — Toronto's city-wide multiplex permissions allow up to <strong>4 residential units</strong> as-of-right in a residential zone, plus a rear garden suite under the Garden Suite By-law (2022), subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" (zoning cell) -------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite (ADU):</strong> a self-contained home in your rear yard — your primary goal, permitted as-of-right under Toronto's Garden Suite By-law</li>
      <li><strong>Detached Houseplex (up to 4 units):</strong> a standalone multi-unit home, permitted as-of-right city-wide</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> secondary suites (like a basement suite) can be paired with a garden suite to boost density</li>
      <li><strong>Townhouse forms:</strong> multi-unit attached homes, subject to the RD zone's built-form standards</li>'''))

# ---- time-sensitive: DC waiver (recast to 4-unit reality) ------------------
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). A 4-unit build with a garden suite sits well within this envelope — a saving of roughly $45,000–$50,000 per unit, with no application required. The benefit applies automatically to compliant builds.</div></div>'''))

# ---- rezoning: co-green ----------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended garden suite — and up to four units — is permitted as-of-right under Toronto\'s city-wide multiplex and Garden Suite by-laws.</div>'))

# ---- rezoning: comparison table "what governs" row -------------------------
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Toronto By-law 569-2013 (as amended)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: twocard -----------------------------------------------------
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Up to four units</div>Toronto's city-wide multiplex permissions (By-law 474-2023) allow up to four residential units in a residential zone without rezoning, subject to the built-form standards.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>'''))

# ---- rezoning: "what this means for ..." heading + para ---------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 62 Surrey Avenue</div>
  <p>Because 62 Surrey Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# ---- rezoning: co-amber (existing structure) -------------------------------
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the permit status of any existing rear or accessory structure.</b><br><span class="sub">If a structure was built or converted without a permit, a retroactive application may be needed before financing or development can proceed. Confirmed in Phase 2.</span></div>'))

# ---- development options: headers + bodies ---------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Toronto's Garden Suite By-law (2022) on a non-laneway residential lot; no rezoning. The size and siting are set by the City's garden-suite standards — setbacks, height, angular planes, and a floor-area cap — confirmed in Phase 2. No parking space is required.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Up to 4 Units + Garden Suite (4+1)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Toronto's city-wide multiplex permissions allow up to four units in the main building as-of-right (By-law 474-2023), and a rear garden suite can be added under the Garden Suite By-law — up to five income units on the lot. This is the higher-density path if you want to go beyond a single suite. The exact unit count and layout depend on the lot's confirmed dimensions and the built-form standards, established in Phase 2. No parking spaces are required; development charges are waived for multiplexes up to 6 units.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Interior Secondary Suite Pairing</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A garden suite can be paired with an interior secondary suite in the existing home (for example, a basement apartment) to add a further income unit within Toronto's as-of-right framework. Confirming the layout, egress, and permit status of any existing below-grade space is an essential early step — both for financing qualification and for counting a suite as a legal unit. Any unpermitted prior work would need a retroactive permit before development or financing can proceed. Confirmed in Phase 2.</div>'''))

# ---- development goal summary ----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>62 Surrey Avenue is a serviced residential lot in Scarborough (Ward 21 — Scarborough Centre) where a detached garden suite is permitted as-of-right under Toronto's Garden Suite By-law, and up to four units are permitted city-wide under By-law 474-2023. <strong>The detached garden suite is the clear primary recommendation</strong>, matching your intake goal, with a multiplex or an interior secondary suite as optional paths to additional income units.</p>'''))

# ---- summary: current zoning review ----------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>62 Surrey Avenue confirms a strong development option. This is a serviced residential lot in Scarborough (Ward 21 — Scarborough Centre) within the City of Toronto. Under Toronto's city-wide multiplex permissions (By-law 474-2023), up to <strong>four residential units are permitted as-of-right</strong>, and a detached garden suite is permitted under the Garden Suite By-law (2022) — the path that matches your intake goal — with no rezoning required.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> a garden suite (and up to four units) is permitted on this lot with no rezoning, no public hearing, and no Council approval required — subject only to technical review of site conditions.</li>
  </ul>'''))

# ---- grants table: Bill 185 municipal row (4-unit framing) -----------------
R.append(('<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>',
          '<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025) — roughly $45,000–$50,000 per unit; a 4-unit build with a garden suite is fully within this envelope. Parking minimums also waived city-wide since February 2022. No application required — benefit applies automatically to compliant builds.</td></tr>'))

# ---- apply -----------------------------------------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(TPL, "w", encoding="utf-8").write(s)

# ---- leftover check --------------------------------------------------------
# Terms that must be GONE. ("6 units" is intentionally allowed — Bill 185
# legitimately references an up-to-6-unit ceiling city-wide.)
banned = ["Coxwell", "Arockiaraj", "johneeraj", "223-4342", "Ward 19",
          "Beaches", "654-2025", "6+1", "nine wards", "Woodbine",
          "M4L 3B5", "six units", "six-unit", "6-unit", "Greenwood",
          "303 Coxwell"]
print("---- leftover scan ----")
any_left = False
for t in banned:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        any_left = True
if not any_left:
    print("clean — no banned source terms remain")
print("done, fails:", fails)
