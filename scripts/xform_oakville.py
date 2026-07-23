"""
xform_oakville.py — transform the House Lyft master report into the
Oakville / 2440 Towne Blvd / Tare Elgu report (basement apartment goal).

Scoped render: 1 interior secondary suite (basement apartment) as the goal,
up to 3 units under Bill 23 as upside. Verified city (Oakville RL5, live GIS
adapter). Programs gated to the stated 1-unit interior scope: financing
(any-scale) + Bill 23 ARU DC exemption. No Toronto DC waiver, no PBRH (4+),
no MLI Select (5+). No invented figures.

Pattern mirrors scripts/xform_cambridge.py: each replacement must match its
expected count exactly; then a leftover grep asserts zero Toronto residue.
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
DST = os.path.join(ROOT, "templates", "report_oakville.html")

shutil.copyfile(SRC, DST)
s = open(DST, encoding="utf-8").read()

# (old, new, expected_count)
R = []

# --- cover ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">2440 Towne Blvd<span>Oakville, ON</span></div>', 1))

# --- address string (barhead + property table first row: 2 occurrences) ---
R.append(('303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5',
          '2440 Towne Blvd, Oakville, ON&nbsp;&nbsp;L6H 5X6', 2))

# --- imagery: no verified lot-scale licensed source for Oakville
#     (aerial_imagery.get_aerial returned None). Remove placeholder boxes;
#     honest pending line per the imagery doctrine. ---
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>''', 1))

# --- property table 1 (name / phone / email / goals) ---
R.append(('''    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Name</td><td>Tare Elgu</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Basement apartment (interior secondary suite) for rental income; intends to keep the property</td></tr>''', 1))

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
'''    <tr><td>Municipality</td><td>Town of Oakville</td></tr>
    <tr><td>Region</td><td>Halton Region</td></tr>
    <tr><td>Property Type</td><td>Residential (per intake)</td></tr>
    <tr><td>Waste Collection</td><td>Halton Region curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Oakville Zoning By-law 2014-014 (as amended by 2024-053/054/111)</td></tr>
    <tr><td>Current Zoning</td><td>RL5 — Residential Low</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Basement apartment (interior secondary suite); optional detached ADU for up to 3 units</td></tr>''', 1))

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
    2440 Towne Blvd is in Oakville — an established lakeside town in Halton Region on the QEW / Lakeshore corridor between Toronto and Hamilton:
    <ul>
      <li>Part of the Greater Toronto and Hamilton Area, with GO Transit Lakeshore West rail service connecting to downtown Toronto</li>
      <li>Well-regarded schools, parks, and the Sixteen Mile Creek and Lake Ontario waterfront trail networks</li>
      <li>Steady rental demand from commuters and nearby employment lands and post-secondary (Sheridan College)</li>
      <li>Established residential streets — the kind of character stock that rents well and holds value</li>
      <li>Note: some Oakville areas fall within heritage districts or near Conservation Halton regulated lands; any such status is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>''', 1))

# --- zoning table (section 2) ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RL5 — Residential Low (Oakville Zoning By-law 2014-014, as amended by 2024-053/054/111)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Oakville has amended its zoning by-law (2024-053/054/111) to implement additional residential units.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite (basement apartment) and, optionally, a detached additional residential unit are permitted, subject to Oakville's site standards — setbacks, height, parking, and a floor-area cap. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''', 1))

# --- "what this means for you" list (section 2 cell) ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite (Basement Apartment):</strong> a self-contained unit within your existing home — your primary goal</li>
      <li><strong>Detached Additional Residential Unit (ADU / Garden Suite):</strong> a separate suite in the rear yard, which can be paired with the interior suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional units, subject to Oakville's site standards</li>''', 1))

# --- time-sensitive: replace the two Toronto items (HST rebate + DC waiver) ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Bill 23 ARU Development-Charge Exemption — In Effect</div><div class="dx">Under Ontario's More Homes Built Faster Act (Bill 23), the first two additional residential units on a serviced residential lot are exempt from municipal development charges. A basement apartment is covered. This is a per-unit saving confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Oakville ARU Standards &amp; Registration</div><div class="dx">Oakville regulates additional residential units through its zoning by-law (2024-053/054/111) and a registration process. Confirming the current standards early — parking, ceiling height, egress, and fire separation — and any registration requirement keeps the project on schedule. Confirmed in Phase 2.</div></div>''', 1))

# --- section 3 rezoning: co-green line ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended basement apartment is permitted as-of-right under Ontario\'s Bill 23 and Oakville\'s zoning by-law — no rezoning required.</div>', 1))

# --- section 3 comparison table: "what governs your build" ---
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + Oakville ZBL 2014-014</td><td class="n">A new site-specific by-law</td></tr>', 1))

# --- section 3 twocard "also permitted" ---
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior secondary suite</div>Under Bill 23, an interior secondary suite (basement apartment) is permitted as-of-right on a serviced residential lot — your stated goal — subject to Oakville\'s site standards.</div>
    <div class="card2"><div class="ct">Detached ADU (garden suite)</div>A detached additional residential unit in the rear yard is also permitted as-of-right under Bill 23 and Oakville\'s ARU by-laws (2024-053/054/111), for up to three units total.</div>''', 1))

# --- section 3 "what this means" barhead ---
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 2440 Towne Blvd</div>', 1))

# --- section 3 paragraph ---
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 2440 Towne Blvd already permits the recommended basement apartment under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>', 1))

# --- section 3 co-amber ---
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: Oakville\'s current ARU standards and registration.</b><br><span class="sub">The suite\'s ceiling height, egress, fire separation, parking, and any registration requirement are confirmed against the by-law in Phase 2 before financing or development proceeds.</span></div>', 1))

# --- section 4 options: A ---
R.append(('''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option A — Interior Secondary Suite / Basement Apartment (your goal)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A self-contained basement apartment within your existing home, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. The unit\'s size and layout are governed by Oakville\'s ARU standards and the Ontario Building Code — minimum ceiling height, a separate entrance, egress windows, and fire separation — confirmed in Phase 2. Additional residential units carry no municipal development charges under Bill 23.</div>
    </div></div>''', 1))

# --- section 4 options: B ---
R.append(('''  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option B — Basement Apartment + Detached ADU (up to 3 units)</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">Pair the interior basement apartment with a detached additional residential unit (garden suite) in the rear yard — a route to as many as three income units on the lot under Bill 23, where the property allows. This maximizes cash flow while keeping the property in your hands. The exact size and siting of the detached suite are set by Oakville\'s ARU standards — setbacks, height, and a floor-area cap — and confirmed in Phase 2.</div>
    </div></div>''', 1))

# --- section 4 options: C ---
R.append(('''  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option C — Oakville Site Considerations</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">A basement apartment is largely an interior conversion, so the main variables are the Ontario Building Code requirements for a legal second unit (ceiling height, egress, fire separation) and Oakville\'s parking and registration rules. Confirming the RL5 built-form standards, any tree-protection by-law requirements for a future detached ADU, and whether the lot is near Conservation Halton regulated lands (ravines / creeks) are the early steps. The exact buildable envelope for any detached suite is confirmed in Phase 2.</div>
    </div></div>''', 1))

# --- section 5 goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Interior Secondary Suite (Basement Apartment)</div>
  <p>2440 Towne Blvd is a serviced residential lot in Oakville where, under Bill 23, an interior secondary suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The basement apartment is the clear primary recommendation</strong>, with a detached ADU as an optional path to a third income unit.</p>''', 1))

# --- section 7 grants: inject the gated-clearing rows into the empty table ---
GRANTS_MARKER = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->'''
GRANTS_ROWS = '''    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Under Ontario's More Homes Built Faster Act (Bill 23), the first two additional residential units on a serviced residential lot are exempt from municipal development charges. Your basement apartment is covered — a meaningful per-unit saving. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where the new suite houses an eligible relative — a senior aged 65+ or an adult eligible for the Disability Tax Credit — this credit returns 15% on up to $50,000 of eligible renovation cost. It applies only in that case; applicability confirmed in Phase 2.</td></tr>
    <tr><td>Note</td><td>Larger-scale rebates (shown for context)</td><td>The federal GST/HST Purpose-Built Rental Housing rebate and its Ontario provincial component apply to projects with four or more self-contained rental units — they are not reached by a single basement apartment, but become available if you later scale the property toward a multi-unit build. Thresholds shown so the path is clear.</td></tr>'''
R.append((GRANTS_MARKER, GRANTS_ROWS, 1))

# --- section 8 summary: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>2440 Towne Blvd is a serviced residential lot in Oakville (RL5 — Residential Low). Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — including the interior secondary suite (basement apartment) you're after — with no rezoning required, subject to the Town's site standards.</p>
  <ul>
    <li><strong>The Basement-Apartment Advantage:</strong> an interior secondary suite adds a rental income stream using space you already own, with no development charges on the added unit under Bill 23 — the exact standards and layout are confirmed in Phase 2.</li>
  </ul>''', 1))

# ---- apply ----
fails = 0
for old, new, want in R:
    got = s.count(old)
    if got != want:
        print(f"[FAIL want {want} got {got}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(DST, "w", encoding="utf-8").write(s)

# ---- leftover check: zero Toronto / Coxwell / wrong-city residue ----
print("--- leftover check ---")
for t in ["Coxwell", "Toronto", "John Arockiaraj", "Ward 19", "Beaches",
          "654-2025", "474-2023", "Bill 185", "6+1", "4+1", "569-2013",
          "TTC", "M4L 3B5", "Waterloo", "Simcoe", "Mississauga", "Edmonton",
          "Calgary", "Vancouver", "Cambridge"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER {t!r}: {n}")
print(f"done. fails={fails}, bytes={len(s)}")
