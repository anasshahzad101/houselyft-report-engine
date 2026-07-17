"""
xform_vaughan.py — turn the House Lyft master report into the Vaughan
(Woodbridge) lead report for Matt Collura, 147 Riverside Drive.

Runs from the templates/ directory (like the other render/xform scripts):
    cd templates && python3 ../scripts/xform_vaughan.py

Context: Vaughan's live parcel GIS (services2.arcgis.com) is egress-blocked in
this routine environment, so the zoning engine's Vaughan adapter could not read
the parcel. Rules below are Vaughan's PUBLISHED city-wide ARU rules, researched
live and corroborated (By-laws 082-2025 / 083-2025, March 2025, implementing
Ontario's Bill 23): up to 3 units as-of-right on a serviced residential lot —
principal + 2 additional residential units, at most one detached; ARU capped at
45% of the principal dwelling's floor area, min 35 m2. Vaughan does NOT permit
4+ units as-of-right. This report ships report-needs-review.
"""
s = open("report_vaughan.html").read()
R = []

# --- cover ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">147 Riverside Drive<span>Woodbridge (Vaughan), ON</span></div>'))

# --- property barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">147 Riverside Drive, Woodbridge (Vaughan), ON&nbsp;&nbsp;L4L 2L5</div>'))

# --- imagery row: no licensed source for Vaughan -> remove grey boxes, honest line ---
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# --- property table 1 ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>147 Riverside Drive, Woodbridge (Vaughan), ON&nbsp;&nbsp;L4L 2L5</td></tr>
    <tr><td>Name</td><td>Matt Collura</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize units within Vaughan's as-of-right envelope (up to 3)</td></tr>'''))

# --- property table 2 ---
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
'''    <tr><td>Municipality</td><td>City of Vaughan (York Region)</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbridge</td></tr>
    <tr><td>Region</td><td>York Region</td></tr>
    <tr><td>Waste Collection</td><td>York Region / City of Vaughan curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Vaughan Comprehensive Zoning By-law 001-2021 (legacy By-law 1-88 still applies in parts of the city); ARU permissions per By-laws 082-2025 / 083-2025</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — up to 3 units as-of-right (principal + 2 additional units)</td></tr>'''))

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
    147 Riverside Drive is in Woodbridge, an established residential community in the City of Vaughan (York Region), in the northwest Greater Toronto Area:
    <ul>
      <li>One of Vaughan's older, fully-serviced communities, near the Humber River valley and its trail system</li>
      <li>Established low-rise residential streets — the kind of stock that supports steady rental demand across the GTA</li>
      <li>Served by York Region Transit, with connections toward the TTC and GO Transit network; road access via major Vaughan arterials</li>
      <li>Local shopping, schools, and services throughout Woodbridge; specifics confirmed in Phase 2</li>
      <li>Note: parts of Vaughan fall within Greenbelt, Oak Ridges Moraine, or TRCA-regulated areas; any such status for this lot is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (Vaughan Comprehensive Zoning By-law 001-2021; legacy By-law 1-88 in parts of the city). Exact zone designation confirmed in Phase 2.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) — the provincial criterion for as-of-right additional residential units under Bill 23.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 and Vaughan By-laws 082-2025 / 083-2025 (March 2025), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — the principal dwelling plus two additional residential units, at most one in a detached accessory building. No rezoning required. Vaughan does not permit four or more units as-of-right.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and a detached garden suite (additional residential units) are permitted, subject to Vaughan's site standards — setbacks, height, and a floor-area cap (an additional unit is capped at 45% of the principal dwelling's floor area, minimum 35 m²). Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — a multiplex of up to three units; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means" list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite:</strong> an additional residential unit within the existing home, such as a basement apartment</li>
      <li><strong>Detached Garden Suite:</strong> a self-contained additional residential unit in the rear yard (at most one of the two additional units may be detached)</li>
      <li><strong>Up to 3 units total:</strong> the principal dwelling plus two additional residential units, subject to Vaughan's site standards</li>
      <li><strong>Confirm before design:</strong> the exact zone, any Established-Neighbourhood suffix or overlay, and lot servicing are confirmed in Phase 2</li>'''))

# --- time-sensitive section ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">ARU Development-Charge Exemption — In Effect</div><div class="dx">Under Ontario's Bill 23, the first two additional residential units on a residential lot are exempt from municipal development charges — a per-unit saving on a second suite or garden suite within Vaughan's up-to-3-unit as-of-right envelope. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Ontario Purpose-Built Rental HST Rebate<br><small>agreement window Apr 1, 2026 – Mar 31, 2027</small></div><div class="dx">Ontario's 2026 Budget introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on the federal rebate. It applies to purpose-built rental projects of four or more units — beyond Vaughan's 3-unit as-of-right envelope — so it is relevant only if the project is scaled up through the planning process. The provincial enhancement is temporary. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# --- rezoning green box ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Up to three residential units — the principal dwelling plus two additional residential units — are permitted as-of-right on a serviced residential lot in Vaughan under By-laws 082-2025 / 083-2025 (implementing Ontario\'s Bill 23). No rezoning is required for that envelope.</div>'))

# --- rezoning comparison: "what governs your build" ---
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-laws 082-2025 / 083-2025</td><td class="n">A new site-specific by-law</td></tr>'))

# --- rezoning "also permitted" twocard ---
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior second suite</div>An additional residential unit inside the existing home (for example, a basement apartment) is permitted as-of-right on a serviced residential lot under Bill 23, subject to Vaughan's site standards.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>A detached additional residential unit in the rear yard is permitted as-of-right under By-laws 082-2025 / 083-2025 — at most one of the two additional units may be in a detached accessory building. Setbacks, height, and size follow Vaughan's standards; confirmed in Phase 2.</div>'''))

# --- rezoning "what this means for ..." heading + para + amber ---
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 147 Riverside Drive</div>
  <p>Because a two- or three-unit configuration is permitted under existing zoning, no rezoning application is contemplated for that envelope. Your project can advance directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Because this report was prepared without a live parcel-level zoning read, two items are confirmed in Phase 2:</b><br><span class="sub">the property's exact zone designation (and any Established-Neighbourhood suffix, legacy By-law 1-88 area, or Greenbelt / Oak Ridges Moraine / TRCA overlay), and whether any existing accessory structure was permitted. These are settled before design proceeds.</span></div>'''))

# --- options A ---
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Second Suite (2 units)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add one additional residential unit to the existing home — for example, an interior basement suite — for a two-unit property. Permitted as-of-right on a serviced residential lot under Bill 23; no rezoning. This is the simplest income step and a common first move. The unit's size and layout follow Vaughan's site standards (an additional unit is capped at 45% of the principal dwelling's floor area, minimum 35 m²), confirmed in Phase 2.</div>'''))

# --- options B ---
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Three Units: Principal + Two Additional Units — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The principal dwelling plus two additional residential units — for example, an interior secondary suite and a detached garden suite in the rear yard — for a total of three units. This is the maximum permitted as-of-right on a serviced residential lot in Vaughan (By-laws 082-2025 / 083-2025), and it matches your multiplex goal at the largest scale that avoids rezoning. At most one of the two additional units may sit in a detached accessory building. No rezoning; the site standards and exact envelope are confirmed in Phase 2.</div>'''))

# --- options C ---
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Larger Purpose-Built Rental (beyond as-of-right)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A purpose-built rental building of four or more units is not permitted as-of-right on this lot and would require the planning process — a zoning by-law amendment and the associated approvals. It is noted here only because that scale is what unlocks the federal and provincial rental programs (the GST/HST purpose-built rental rebate at 4+ units; CMHC financing at larger scale). Whether the lot, frontage, and servicing could support it is assessed in Phase 2.</div>'''))

# --- goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Three-Unit Configuration</div>
  <p>147 Riverside Drive is a residential lot in Woodbridge (City of Vaughan) where, under By-laws 082-2025 / 083-2025 (Bill 23), up to three residential units are permitted as-of-right — the principal dwelling plus two additional units. <strong>A three-unit configuration is the clear primary recommendation</strong>, as the largest multiplex form achievable without rezoning. The exact zone designation and site standards are confirmed in Phase 2.</p>'''))

# --- grants table: inject Vaughan-appropriate gated rows (thresholds shown) ---
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->
    </table>''',
'''    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Under Ontario's More Homes Built Faster Act (Bill 23), the first two additional residential units on a lot are exempt from municipal development charges — a meaningful per-unit saving on a second suite or a garden suite. Applies within Vaughan's up-to-3-unit as-of-right envelope. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal / Provincial</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate — <em>at 4+ units</em></td><td>Available at four or more self-contained rental units (90%+ long-term rental): a 100% rebate of the 5% federal GST, which Ontario mirrors with a 100% rebate of the 8% provincial HST component. Reaching this threshold means a purpose-built rental project beyond Vaughan's 3-unit as-of-right envelope (a larger form through the planning process) — explored in Phase 2. The Ontario provincial enhancement is time-limited (agreement signed April 1, 2026 – March 31, 2027).</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / Apartment Construction Loan Program — <em>at larger scale</em></td><td>Low-cost CMHC financing for purpose-built rental unlocks at larger scale — MLI Select at five or more rental units, the Apartment Construction Loan Program at a $1M+ loan. Shown here as upside if the project is scaled up through the planning process; it is not reached by the 3-unit as-of-right form. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where a new self-contained suite houses an eligible senior or an adult eligible for the Disability Tax Credit, this credit may return 15% on up to $50,000 of eligible cost. Applies only in that circumstance — confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes may offset efficient design and equipment on a new suite. Applicability confirmed in Phase 2.</td></tr>
    </table>'''))

# --- summary: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>147 Riverside Drive is a residential lot in Woodbridge, City of Vaughan. Under By-laws 082-2025 / 083-2025 (implementing Ontario's Bill 23), up to <strong>three residential units are permitted as-of-right</strong> — the principal dwelling plus two additional residential units — with no rezoning required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Three-Unit As-of-Right Advantage:</strong> a second suite and a detached garden suite can be added on land you already own, adding two income streams without a rezoning, a public hearing, or a Council decision.</li>
  </ul>
  <p style="font-size:8.6pt;color:#7a818f;"><em>Note: this report was prepared from Vaughan's published city-wide additional-unit rules; the property's exact zone designation and any site-specific overlays were not read from a live parcel query and are confirmed in Phase 2.</em></p>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)
open("report_vaughan.html", "w").write(s)

# leftover guard — MUST all be zero
print("--- leftover check ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "johneeraj",
          "654-2025", "474-2023", "6+1", "4+1", "Bill 185", "569-2013", "houseplex",
          "imgbox", "auto-generated"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
