import os
os.chdir(os.path.join(os.path.dirname(__file__), "..", "templates"))
s = open("report_niagara.html").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">5059 Palmer Avenue<span>Niagara Falls, ON</span></div>'))
# barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">5059 Palmer Avenue, Niagara Falls, ON&nbsp;&nbsp;L2E 3T9</div>'))
# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>5059 Palmer Avenue, Niagara Falls, ON&nbsp;&nbsp;L2E 3T9</td></tr>
    <tr><td>Name</td><td>Mark Maltman</td></tr>
    <tr><td>Phone Number</td><td>(289) 990-1959</td></tr>
    <tr><td>Email</td><td>markmaltman@hotmail.com</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (per intake)</td></tr>'''))
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
'''    <tr><td>Municipality</td><td>City of Niagara Falls (Niagara Region)</td></tr>
    <tr><td>Neighbourhood</td><td>Downtown Niagara Falls</td></tr>
    <tr><td>Region</td><td>Regional Municipality of Niagara</td></tr>
    <tr><td>Property Type</td><td>To be confirmed (intake notes a commercial–residential context)</td></tr>
    <tr><td>Waste Collection</td><td>Niagara Region curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Niagara Falls Zoning By-law — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (per intake)</td></tr>'''))
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
    5059 Palmer Avenue is in the downtown core of Niagara Falls, an established, walkable neighbourhood in the Regional Municipality of Niagara:
    <ul>
      <li>In the Queen Street / downtown district — the City's historic main-street area</li>
      <li>Close to the Niagara Falls GO / VIA rail station and regional transit connections</li>
      <li>Steady rental demand from the area's tourism, hospitality, and healthcare employers</li>
      <li>Walkable to downtown shops, cafés, and services along Queen Street</li>
      <li>Established residential and mixed-use streets typical of the downtown core (illustrative context, not a valuation)</li>
    </ul>'''))
# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Niagara Falls Zoning By-law) — exact zone confirmed in Phase 2. Intake notes a commercial–residential context; whether the site is residential or mixed-use is confirmed in Phase 2.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot province-wide — no rezoning required. Any larger multiplex depends on the site's specific zone and is confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and/or an additional residential unit are permitted on a serviced residential lot, subject to the City's site standards — setbacks, height, and floor-area limits. The multiplex scale you're after is confirmed against the site's zone in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td>Likely, subject to confirmation of the site's zone; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))
# what this means (section 2 list)
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Additional Residential Units (Bill 23):</strong> up to 3 units as-of-right on a serviced residential lot — for example a main dwelling plus an interior suite and a detached backyard unit</li>
      <li><strong>Multiplex / Small Apartment:</strong> a purpose-built multi-unit building, where the site's specific zone permits it — confirmed in Phase 2</li>
      <li><strong>Interior &amp; Backyard Suites:</strong> secondary suites (such as a basement or backyard unit) paired with the main dwelling to boost density</li>
      <li><strong>Mixed-Use (if applicable):</strong> given the downtown, commercial–residential context noted at intake, a mixed-use form may be an option — the redevelopment path is confirmed in Phase 2</li>'''))
# time-sensitive (replace the two Toronto items; keep CMHC item)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>time-limited</small></div><div class="dx">Ontario's 2026 Budget introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. This is a temporary provincial enhancement tied to when the agreement is signed. Structuring the project correctly from Day 1 is essential to capture it — eligibility for your project is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under Ontario's provincial legislation — a meaningful per-unit saving. The City of Niagara Falls / Niagara Region development-charge treatment for a larger multiplex is confirmed in Phase 2.</div></div>'''))
# rezoning: co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Likely Not Required for the As-of-Right Scale</div>Up to 3 residential units are permitted as-of-right on a serviced residential lot under Ontario\'s Bill 23 — no rezoning. A larger multiplex may need confirmation of the site\'s zone or a planning approval; this is confirmed in Phase 2.</div>'))
# rezoning: cmp table row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Provincial ARU rules (Bill 23) + City zoning</td><td class="n">A new site-specific by-law</td></tr>'))
# rezoning: twocards
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to three units</div>Under Bill 23, a serviced residential lot may hold up to three residential units as-of-right — no rezoning — subject to the City's site standards.</div>
    <div class="card2"><div class="ct">Backyard / additional suite</div>An additional residential unit (such as a backyard suite) is permitted on a serviced residential lot, subject to the City of Niagara Falls' setback, height, and floor-area standards. Confirmed in Phase 2.</div>'''))
# rezoning: barhead "what this means for..."
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 5059 Palmer Avenue</div>'))
# rezoning: paragraph
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>On a serviced residential lot, the up-to-three-unit scale is permitted as-of-right under Bill 23, so no rezoning is contemplated for that scale. The larger multiplex you\'re targeting depends on the site\'s specific zone — if the zone already permits it, the project advances directly to design and permitting; if not, a planning approval may be required. Which path applies is confirmed in Phase 2. This assessment reflects the rules in force at the date of this report and is subject to technical review of site conditions.</p>'))
# rezoning: co-amber
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the site\'s exact zone and current legal use.</b><br><span class="sub">Intake notes a commercial–residential context. Confirming the zoning designation and any existing legal use is an essential first step — it determines whether the multiplex is as-of-right or needs a planning approval, and it affects financing.</span></div>'))
# options A header + body
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Up to 3 Units As-of-Right (Bill 23)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">On a serviced residential lot, up to three residential units are permitted as-of-right under Bill 23 — for example the main dwelling plus an interior secondary suite and a detached backyard unit. No rezoning required for this scale. Unit sizes and siting are set by the City of Niagara Falls' site standards (setbacks, height, floor-area limits), confirmed in Phase 2. Additional residential units are exempt from development charges under provincial legislation.</div>'''))
# options B header + body
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Purpose-Built Multiplex (your goal)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A purpose-built multi-unit building matching your stated goal of maximizing unit count. Whether this is permitted as-of-right or needs a planning approval depends on the site's specific zone — especially given the downtown, commercial–residential context noted at intake. The buildable envelope, unit count, and any required approvals are confirmed in Phase 2. Ontario's purpose-built rental rebates and CMHC financing programs (below) are designed for exactly this kind of project.</div>'''))
# options C header + body
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Mixed-Use Path (if applicable)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Given the downtown location and the commercial–residential context noted at intake, the site may sit in — or near — a mixed-use designation. Where that applies, residential units above or behind a commercial ground floor can be an option, and downtown revitalization incentives may apply. Whether a mixed-use path is available, and which incentives apply, is confirmed in Phase 2 once the exact zone and Official Plan designation are established.</div>'''))
# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex Development</div>
  <p>5059 Palmer Avenue is a serviced lot in downtown Niagara Falls. Up to three residential units are permitted as-of-right on a serviced residential lot under Ontario's Bill 23, with a larger purpose-built multiplex depending on the site's specific zone. <strong>A purpose-built multiplex is the primary path to explore</strong>, with the up-to-three-unit ARU scale available as-of-right as a fallback — the exact zone and achievable unit count are confirmed in Phase 2.</p>'''))
# grants table
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Ontario mirrors this with a 100% rebate of the 8% provincial HST component. Eligibility and current program windows for your project are confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction loans up to 100% of residential project cost for purpose-built rental (minimum loan applies). Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A CMHC program that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under provincial legislation — a meaningful per-unit saving. The City of Niagara Falls / Niagara Region charge treatment for a larger multiplex is confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Niagara Falls / Niagara Region Housing &amp; Downtown Incentives</td><td>The City and Region periodically offer community-improvement-plan (CIP) incentives for residential and downtown development. Availability and eligibility for this property are confirmed in Phase 2 — no program amount is stated here until verified.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where a new suite houses an eligible relative. Applicability confirmed in Phase 2.</td></tr>'''))
# summary section 8 current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>5059 Palmer Avenue is a serviced lot in downtown Niagara Falls. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> on a serviced residential lot — no rezoning required, subject to the City's site standards. A larger, purpose-built multiplex — your stated goal — depends on the site's specific zone and, given the commercial–residential downtown context, may open a mixed-use path. The exact zone and achievable unit count are confirmed in Phase 2.</p>
  <ul>
    <li><strong>The As-of-Right Baseline:</strong> up to three units are available on a serviced residential lot with no rezoning — a guaranteed floor while the larger multiplex scale is confirmed against the site's zone.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)
open("report_niagara.html", "w").write(s)

print("--- leftover check ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Aroc", "654-2025",
          "474-2023", "Bill 185", "569-2013", "6+1", "4+1", "TTC", "M4L 3B5",
          "Garden Suite By-law", "Greenwood", "Gerrard", "Woodbine"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
