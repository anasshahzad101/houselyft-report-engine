"""
xform_hamilton.py — turn the House Lyft master into the report for
717 Mohawk Road, Ancaster (City of Hamilton). Run from templates/.

City coverage: Hamilton has NO zoning-engine adapter yet, so the zoning rules
below were researched LIVE from the City of Hamilton's official zoning
publications (report-needs-review). Verified facts used:
  - City-wide Comprehensive Zoning By-law No. 05-200.
  - By-law No. 24-051 (in force Feb 2024): triplex + fourplex dwellings are
    permitted uses AS-OF-RIGHT in Low Density Residential zones (R1 / R1a; new
    R2 Large Lot). Fourplex = a building of 4 dwelling units, >=1 unit above
    another. R1 minimums cited: lot area 360 m2, lot width 12.0 m; max height
    10.5 m; 4.0 m front setback.
  - By-law No. 24-052 (Apr 2024): Section 5 parking replaced; reduced parking.
  - Additional Dwelling Units: detached ADU (max height 6.0 m) + internal
    secondary suite on lots with a single/semi/street-townhouse dwelling; ADUs
    DC-exempt under provincial legislation (Bill 23).
  - Mid Rise Residential zones approved Oct 8, 2025 but UNDER OLT APPEAL — not
    in effect; treated as future upside only.
Hedged (confirm in Phase 2): the parcel's exact zone (Mohawk Rd is an arterial;
Ancaster carries former By-law 87-57 history), the lot area/frontage, and
Hamilton's own DC treatment of a new fourplex. No Toronto Bill 185 / 654-2025
content, no invented figures.
"""
s = open("report_hamilton.html").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">717 Mohawk Road<span>Ancaster (Hamilton), ON</span></div>'))

# imagery row -> honest "pending" line (no licensed lot-scale source for Hamilton)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div style="font-size:8.5pt;color:#7a818f;margin:2px 0 12px;font-style:italic;">Aerial and street-level photography pending a licensed imagery source for Hamilton.</div>'''))

# barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">717 Mohawk Road, Ancaster (Hamilton), ON&nbsp;&nbsp;L9G 2X1</div>'))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>717 Mohawk Road, Ancaster (Hamilton), ON&nbsp;&nbsp;L9G 2X1</td></tr>
    <tr><td>Name</td><td>Deepak Talwar</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize the permitted unit count</td></tr>'''))

# property table 2
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
'''    <tr><td>Municipality</td><td>City of Hamilton (former Town of Ancaster)</td></tr>
    <tr><td>Neighbourhood</td><td>Ancaster</td></tr>
    <tr><td>Ward</td><td>Ancaster — confirmed in Phase 2</td></tr>
    <tr><td>Waste Collection</td><td>City of Hamilton curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Hamilton Zoning By-law No. 05-200 (city-wide residential zones); former Ancaster By-law 87-57 may still govern in some areas — confirmed in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (MPAC / survey)</td></tr>
    <tr><td>Development Goals</td><td>Fourplex (up to 4 units) as-of-right where the zone permits; triplex as the conservative alternative</td></tr>'''))

# neighbourhood spotlight
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
    717 Mohawk Road is in Ancaster — an established, historic community on the west Hamilton Mountain, now part of the City of Hamilton:
    <ul>
      <li>Mature residential area with a well-regarded village core along Wilson Street</li>
      <li>Steady rental demand typical of west Hamilton / Ancaster</li>
      <li>Convenient access to Highway 403 and the Lincoln Alexander Parkway</li>
      <li>Close to McMaster University and the broader Hamilton employment base</li>
      <li>Mohawk Road is an arterial corridor — the parcel's exact zoning designation is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Hamilton Zoning By-law No. 05-200) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (municipal water &amp; sewer) in a Low Density Residential zone — the basis on which Hamilton permits triplex and fourplex dwellings as-of-right.</td></tr>
    <tr><td>Recent Changes</td><td>Under By-law No. 24-051 (amending 05-200, in force February 2024), <strong>triplex and fourplex dwellings are permitted uses as-of-right</strong> in Hamilton's Low Density Residential zones — no rezoning required. Parking standards were reduced under By-law No. 24-052 (2024).</td></tr>
    <tr><td>Permitted Uses</td><td>Low-rise multi-unit housing — a fourplex (a building of up to <strong>four dwelling units</strong>, at least one unit above another) is permitted as-of-right in a Low Density Residential zone, subject to the zone's site standards (lot area, width, height, setbacks) and technical review. Additional Dwelling Units are also permitted on eligible lots.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>LIKELY — confirm the parcel's zone in Phase 2</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# "what this means" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex &amp; Fourplex:</strong> A single building of three or four dwelling units — permitted as-of-right in Hamilton's Low Density Residential zones</li>
      <li><strong>Additional Dwelling Unit (Detached):</strong> A self-contained suite in the rear yard on an eligible lot (maximum height 6.0 m)</li>
      <li><strong>Internal Secondary Suite:</strong> A unit within the existing home (e.g. a basement apartment) on an eligible lot</li>
      <li><strong>Up to four units as-of-right:</strong> Subject to the parcel's zone and lot dimensions, confirmed in Phase 2</li>'''))

# time-sensitive: replace only the Toronto DC-waiver item
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Fourplex As-of-Right — In Effect</div><div class="dx">Hamilton permits triplex and fourplex dwellings as-of-right in its Low Density Residential zones (By-law 24-051, in force February 2024), with reduced parking standards under By-law 24-052. Additional Dwelling Units are exempt from development charges under provincial legislation. Hamilton's own development-charge treatment of a new fourplex is confirmed in Phase 2 — no dollar figure is assumed here.</div></div>'''))

# rezoning green box
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required Where the Zone Permits</div>A triplex or fourplex is permitted as-of-right in Hamilton\'s Low Density Residential zones under By-law 24-051 — no rezoning needed once the parcel\'s zone is confirmed.</div>'))

# rezoning table last row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 05-200 (as amended by 24-051)</td><td class="n">A new site-specific by-law</td></tr>'))

# rezoning twocard
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Fourplex (up to 4 units)</div>Hamilton's Low Density Residential zones permit a fourplex — a building of up to four dwelling units — as-of-right under By-law 24-051, subject to the zone's site standards.</div>
    <div class="card2"><div class="ct">Additional Dwelling Unit</div>On an eligible lot, a detached Additional Dwelling Unit (maximum height 6.0 m) or an internal secondary suite may be permitted — confirmed for this parcel in Phase 2.</div>
  </div>'''))

# "what this means for 303 Coxwell" barhead + para + amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 717 Mohawk Road</div>
  <p>Where the parcel sits in a Low Density Residential zone, a triplex or fourplex is permitted as-of-right and the project advances directly to design and permitting — no rezoning application. This assessment reflects the by-laws in force at the date of this report and is subject to confirming the parcel's exact zone and lot dimensions, and to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm early: the parcel's exact zoning designation, and its lot area and frontage.</b><br><span class="sub">Mohawk Road is an arterial corridor and Ancaster carries former-municipality zoning history; the governing zone and whether the lot meets the fourplex minimums (lot area / width) are confirmed in Phase 2 before financing or development proceeds.</span></div>'''))

# Option A header + body
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex (3 Units) — Conservative As-of-Right</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A three-unit building (triplex) — permitted as-of-right in Hamilton's Low Density Residential zones under By-law 24-051. This is the conservative path: a triplex meets the same lot and setback standards the zone applies to a single detached dwelling (in the R1 zone, minimum lot area 360 m² and minimum lot width 12.0 m; maximum building height 10.5 m; 4.0 m front setback — confirmed for the parcel's specific zone in Phase 2). Reduced parking standards apply under By-law 24-052. A good fit where the lot is on the smaller side.</div>'''))

# Option B header + body
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Fourplex (4 Units) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A fourplex — a single building of four dwelling units, at least one unit above another — permitted as-of-right in Hamilton's Low Density Residential zones under By-law 24-051. This matches Deepak's goal of maximizing the permitted unit count. The fourplex shares the zone's setback standards (front, flankage, and rear) with the triplex, to a maximum building height of 10.5 m. Reduced parking standards apply under By-law 24-052. Eligibility depends on the parcel's zone and on the lot meeting the zone's minimum lot area and width — confirmed in Phase 2.</div>'''))

# Option C header + body
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Additional Dwelling Units &amp; Future Upside</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">On a lot with a single detached, semi-detached, or street townhouse dwelling, Hamilton permits an internal secondary suite plus a detached Additional Dwelling Unit (maximum height 6.0 m) — a route to added rental income where a fourplex is not pursued. Separately, Hamilton's new Mid Rise Residential zones (approved October 2025) could unlock taller forms on some corridors, but they are under appeal at the Ontario Land Tribunal and are NOT in effect — treated here as potential future upside only, confirmed in Phase 2.</div>'''))

# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Fourplex (Up to 4 Units)</div>
  <p>Where 717 Mohawk Road sits in a Low Density Residential zone, a fourplex — up to four dwelling units — is permitted as-of-right under Hamilton By-law 24-051, matching the goal of maximizing the permitted unit count. <strong>The fourplex is the primary recommendation</strong>, with a triplex as the conservative alternative, once the parcel's zone and lot dimensions are confirmed in Phase 2.</p>'''))

# grants table body
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Can be structured to bridge into MLI Select permanent financing at project completion. Program terms confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>Additional Dwelling Unit — Development Charge Exemption</td><td>Additional residential units are exempt from municipal development charges under provincial legislation (Bill 23) — a meaningful per-unit saving on an internal or detached suite. Hamilton's DC treatment of a new fourplex is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where a new suite houses an eligible relative. Applicability confirmed in Phase 2.</td></tr>'''))

# summary current-zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>717 Mohawk Road, Ancaster is within the City of Hamilton, where By-law 24-051 (in force February 2024) permits <strong>triplex and fourplex dwellings as-of-right in Low Density Residential zones</strong> — up to four dwelling units in a single building, with no rezoning required. The exact zone for this parcel and its lot dimensions are confirmed in Phase 2, which is why this report is flagged for a rules double-check before your call.</p>
  <ul>
    <li><strong>The Fourplex As-of-Right Advantage:</strong> Where the parcel is a Low Density Residential zone, a fourplex is permitted with no rezoning, no public hearing, and no Council approval — subject to the zone's site standards and confirming the lot meets the minimum lot area and width.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)
open("report_hamilton.html", "w").write(s)

# leftover check — Toronto/master residue must be zero
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
          "654-2025", "569-2013", "474-2023", "Bill 185", "6+1", "sixplex",
          "six units", "garden suite", "garage", "Gerrard", "TTC"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
