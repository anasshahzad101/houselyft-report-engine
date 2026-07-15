"""
xform_orillia.py — turn the House Lyft master into the Orillia report for
230 Murphy Road (Kevin Wood).

Run from templates/:  python3 ../scripts/xform_orillia.py

Orillia has NO city adapter in the zoning engine, so its rules were researched
live from official sources (City of Orillia Zoning By-law 2014-44, consolidated
June 2, 2025; Ontario Bill 23) — this report is a report-needs-review deliverable.

Honest framing for this lead:
  * Up to 3 residential units are permitted AS-OF-RIGHT on a serviced residential
    lot under Bill 23 (primary dwelling + up to 2 additional residential units).
  * The lead's goal — a multiplex / stacked-townhouse form BEYOND three units —
    is NOT as-of-right in Orillia today; it requires a Zoning By-law Amendment
    (rezoning), scoped in Phase 2. (Evidenced by the R2 "Three-Unit Dwelling"
    rezoning applications on file with the City, e.g. 325 Peter St N.)
Every city-specific figure that could not be verified live is left as a
"confirm in Phase 2" per the AI Report Writer accuracy contract.
"""
s = open("report_orillia.html").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">230 Murphy Road<span>Orillia, ON</span></div>'))

# ---- property-details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">230 Murphy Road, Orillia, ON&nbsp;&nbsp;L3V 6Y4</div>'))

# ---- imagery row: no verified licensed source for Orillia -> honest line ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source for this municipality.</div>'''))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>230 Murphy Road, Orillia, ON&nbsp;&nbsp;L3V 6Y4</td></tr>
    <tr><td>Name</td><td>Kevin Wood</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development / stacked townhouses (per intake)</td></tr>'''))

# ---- property table 2 ----
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
'''    <tr><td>Municipality</td><td>City of Orillia (single-tier)</td></tr>
    <tr><td>Neighbourhood</td><td>To be confirmed</td></tr>
    <tr><td>County (for context)</td><td>Simcoe (Orillia is a separated single-tier city)</td></tr>
    <tr><td>Waste Collection</td><td>City of Orillia curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Orillia Zoning By-law 2014-44 (consolidated June 2, 2025)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Multiplex / stacked townhouses (primary); up to 3 units as-of-right (ARU path) as the immediate baseline</td></tr>'''))

# ---- neighbourhood spotlight ----
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
    230 Murphy Road is in Orillia — a lakeside single-tier city between Lake Couchiching and Lake Simcoe, at the junction of Highways 11 and 12 in Central Ontario. (Illustrative context, not a valuation.)
    <ul>
      <li>Established residential city with steady rental demand from local employers, Georgian College's Orillia campus, and Lakehead University's Orillia campus</li>
      <li>Waterfront, trails, and the historic Mississaga Street downtown are local draws</li>
      <li>Highway 11/12 corridor gives commuter access toward Barrie and the GTA</li>
      <li>Full municipal services (water and sewer) across the urban area — the servicing baseline for as-of-right additional residential units</li>
      <li>Exact neighbourhood, school, and servicing details for this lot are confirmed in Phase 2</li>
    </ul>'''))

# ---- zoning table (Section 2) ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Orillia Zoning By-law 2014-44) — exact zone (e.g. R1 / R2) confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within the settlement area — the provincial criteria for as-of-right additional residential units. Confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act, 2022), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — including lots with detached, semi-detached, and townhouse dwellings — with no rezoning. Orillia has updated Zoning By-law 2014-44 to comply.</td></tr>
    <tr><td>Permitted Uses</td><td>A primary dwelling plus up to two additional residential units (an interior suite and/or a detached suite), subject to Orillia's site standards — setbacks, height, and a floor-area cap. A larger multiplex or stacked-townhouse form beyond three units is <strong>not</strong> as-of-right and would require a Zoning By-law Amendment. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>Up to 3 units — YES, as-of-right.</strong> Multiplex / stacked townhouse — achievable via rezoning; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "What this means for you" list (Section 2 cell) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Up to 3 Units As-of-Right:</strong> a primary dwelling plus up to two additional residential units under Bill 23 — no rezoning</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (for example, a basement apartment)</li>
      <li><strong>Detached / Backyard Suite:</strong> a self-contained suite in the rear yard, subject to Orillia's site standards</li>
      <li><strong>Multiplex / Stacked Townhouse (your goal):</strong> a larger built form beyond three units — not as-of-right in Orillia today; achievable through a Zoning By-law Amendment, explored in Phase 2</li>'''))

# ---- time-sensitive: swap the Toronto Bill 185 DC waiver for the ARU DC exemption ----
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under provincial legislation (Bill 23) — a meaningful per-unit saving on the interior and detached suites in the as-of-right 3-unit path. The City of Orillia applies this exemption. Development-charge treatment of a larger multiplex (beyond the ARU exemption) is confirmed for your project in Phase 2.</div></div>'''))

# ---- Section 3 Rezoning: green "not required" box -> honest two-track box ----
R.append(('''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>''',
'''  <div class="co-green"><div class="ct2">Not Required for the As-of-Right Path</div>Up to three residential units (the primary dwelling plus two additional units) are permitted as-of-right under Bill 23 — no rezoning.</div>
  <div class="co-amber"><b>Required for the multiplex / stacked-townhouse goal.</b><br><span class="sub">A built form beyond three units is not as-of-right in Orillia today. It would proceed through a Zoning By-law Amendment (and, if needed, an Official Plan review) — the approval path, timeline, and unit count are scoped in Phase 2.</span></div>'''))

# ---- Section 3 comparison table: "what governs your build" row ----
R.append(('''    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><td>What governs your build</td><td class="g">Bill 23 + Zoning By-law 2014-44</td><td class="n">A new site-specific by-law</td></tr>'''))

# ---- Section 3 two-card "also permitted as-of-right" ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to three units</div>Under Bill 23, a serviced residential lot may hold the primary dwelling plus up to two additional residential units without rezoning — subject to Orillia's site standards.</div>
    <div class="card2"><div class="ct">Detached backyard suite</div>A self-contained suite in the rear yard is one of the two permitted additional units — its size and siting follow Orillia's setback, height, and floor-area standards, confirmed in Phase 2.</div>'''))

# ---- Section 3 "what this means" barhead + paragraph ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 230 Murphy Road</div>
  <p>The as-of-right 3-unit path advances directly to design and permitting with no rezoning. Your stated goal — a multiplex or stacked-townhouse form beyond three units — is pursued in parallel through a Zoning By-law Amendment, which Phase 2 scopes: the exact zone, the buildable envelope, and the approval route. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Items to confirm in Phase 2:</b><br><span class="sub">the exact zoning of the lot (e.g. R1 / R2) and its permitted uses, full municipal servicing, lot dimensions, and whether the target multiplex form needs an Official Plan amendment in addition to rezoning.</span></div>'''))

# ---- Section 4 Options A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Up to 3 Units (As-of-Right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">The primary dwelling plus up to two additional residential units — an interior secondary suite (for example, a basement apartment) and/or a detached suite in the rear yard. Up to three units total, permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. Unit sizes and siting follow Orillia's setback, height, and floor-area standards (confirmed in Phase 2). Additional residential units are exempt from development charges, and no additional parking may be required for them under provincial rules. This is the fastest route to income on the lot.</div>'''))

# ---- Section 4 Options B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Multiplex / Stacked Townhouse (Your Goal) — via Rezoning</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A multiplex or stacked-townhouse building beyond three units — the configuration you are after. This built form is not as-of-right in Orillia today; it is achievable through a Zoning By-law Amendment (rezoning), and potentially an Official Plan review, rather than a simple permit. The achievable unit count depends on the lot's area, frontage, and servicing, and on Council's decision — all scoped in Phase 2. We do not state a unit count here because it is not yet verified; Phase 2 establishes the realistic envelope and the approval path before any commitment.</div>'''))

# ---- Section 4 Options C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Phased Approach (Build Now, Rezone in Parallel)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A practical route for this lead: put the as-of-right 3-unit path into design now for near-term income, while the Zoning By-law Amendment for the larger multiplex goal runs in parallel. This keeps the property productive during the rezoning timeline and de-risks the larger build. The first steps are confirming the exact zone and permitted uses, lot dimensions, and full municipal servicing — the inputs that determine what the rezoning can realistically ask for. All confirmed in Phase 2.</div>'''))

# ---- Section 5 Goal Summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex / Stacked-Townhouse Path</div>
  <p>230 Murphy Road can support up to three residential units as-of-right under Bill 23 today — the fastest route to income. Your primary goal, a multiplex or stacked-townhouse form beyond three units, is <strong>achievable through a Zoning By-law Amendment</strong> rather than as-of-right. <strong>Phase 2 scopes that rezoning path</strong> — the exact zone, the buildable envelope, and the realistic unit count — so the target is grounded in verified numbers before any commitment.</p>'''))

# ---- Section 7 Grants table: swap Toronto DC Waiver row for ARU DC exemption ----
R.append(('''    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under provincial legislation — a per-unit saving on the interior and detached suites in the as-of-right 3-unit path. The City of Orillia applies this exemption. Any City of Orillia municipal incentives, and the development-charge treatment of a larger multiplex, are confirmed in Phase 2.</td></tr>'''))

# ---- Section 8 Summary: Current Zoning Review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>230 Murphy Road is a residential lot in the City of Orillia. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> on a serviced residential lot — the primary dwelling plus two additional units — with no rezoning, subject to the City's site standards. The multiplex / stacked-townhouse form you are targeting sits beyond that as-of-right envelope and is pursued through a Zoning By-law Amendment.</p>
  <ul>
    <li><strong>The As-of-Right Baseline:</strong> up to three income units without rezoning — the near-term path — with additional units and detached suites exempt from development charges under Bill 23.</li>
    <li><strong>The Rezoning Upside:</strong> the larger multiplex goal is achievable via a Zoning By-law Amendment; Phase 2 establishes the realistic unit count and approval path before any commitment. Because Orillia has no city adapter in our engine, these rules were researched live and should be re-verified against the City before the call.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open("report_orillia.html", "w").write(s)

# leftover check — anything from the source city means a bad transform
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "Arockiaraj", "654-2025",
          "474-2023", "569-2013", "Bill 185", "6+1", "4+1", "303 ", "John",
          "TTC", "garden suite in the rear utilizing"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
