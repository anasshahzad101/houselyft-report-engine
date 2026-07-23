# xform_edmonton.py — turn the House Lyft master into the Edmonton report for
# 16027 100A Avenue NW (Connie Penaflor). Run from templates/ (cwd), same as the
# other xform_*.py scripts. Every replacement must match exactly once; a leftover
# grep at the end guards against Toronto data surviving into an Edmonton report.
#
# Grounding (engine, live-verified): Edmonton Zoning Bylaw 20001, zone RS
# (Small Scale Residential), Glenwood, Nakota Isga Ward. Up to 6 dwellings
# mid-block as-of-right (8 on corner). Height 10.5 m -> 9.5 m for applications
# from Aug 1, 2026. Programs gated for Alberta/Edmonton per config/programs.json.
s = open("report_edmonton.html").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">16027 100A Avenue NW<span>Edmonton, AB</span></div>'))

# section-1 barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">16027 100A Avenue NW, Edmonton, AB&nbsp;&nbsp;T5P 0L9</div>'))

# imagery slots -> honest pending line (no licensed Edmonton source)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div style="font-size:8.5pt;color:#7a818f;margin:4px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>16027 100A Avenue NW, Edmonton, AB&nbsp;&nbsp;T5P 0L9</td></tr>
    <tr><td>Name</td><td>Connie Penaflor</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>To be confirmed — see the goal question in Section 5</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Edmonton</td></tr>
    <tr><td>Neighbourhood</td><td>Glenwood</td></tr>
    <tr><td>Ward</td><td>Nakota Isga Ward (Councillor Reed Clarke)</td></tr>
    <tr><td>Community League</td><td>Glenwood Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Edmonton for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — mid-block vs corner status affects the unit ceiling (Section 4)</td></tr>
    <tr><td>Development Goals</td><td>To be confirmed — see Section 5</td></tr>'''))

# neighbourhood spotlight (uses the City of Edmonton neighbourhood profile text)
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
    16027 100A Avenue NW is in Glenwood, an established residential neighbourhood in Edmonton's west end:
    <ul>
      <li>A large west-end community of primarily single-family dwellings, with apartment buildings near school sites (City of Edmonton neighbourhood profile)</li>
      <li>Commercial services along Stony Plain Road, plus Mayfield Common nearby</li>
      <li>West Edmonton Mall is a short drive away</li>
      <li>Served by the Glenwood Community League</li>
      <li>Continued residential development is anticipated as the area grows (City of Edmonton). (Illustrative context, not a valuation.)</li>
    </ul>'''))

# zoning table (section 2)
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone consolidates the former RF1–RF4 districts and permits small-scale multi-unit housing by default, subject to the zone's built-form standards — height, setbacks, and site coverage. Site-specific dimensions are confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Zoning Bylaw 20001 (in force Jan 1, 2024), with the 2025 one-year-review amendments, the RS mid-block maximum is <strong>up to 6 dwellings as-of-right</strong> (reduced from 8); corner sites may reach up to 8, and developments of more than 8 dwellings are limited to corner sites. Backyard (garden) housing is permitted and counts toward the total. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Small-scale multi-unit housing — row housing, multiplexes, and backyard housing — is permitted as-of-right in the RS zone, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means (section 2 list)
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing:</strong> Multi-unit attached homes — side-by-side dwellings on a single lot</li>
      <li><strong>Multiplex (up to 6 dwellings mid-block):</strong> A small-scale multi-unit building, as-of-right in the RS zone</li>
      <li><strong>Backyard (Garden) Housing:</strong> A detached suite in the rear yard — permitted, and it counts toward the total dwelling count</li>
      <li><strong>Internal Secondary Suite:</strong> A unit within the main dwelling (such as a basement suite) to add density</li>'''))

# time-sensitive block
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">RS Height Envelope — File Before Aug 1, 2026</div><div class="dx">Edmonton has approved a reduction of the RS maximum height from 10.5 m to 9.5 m for development permit applications made on or after August 1, 2026 (approved April 27, 2026). Filing before that date keeps the taller 10.5 m envelope, which can matter for a three-storey small-scale form. If a build is contemplated, plan the timing of the permit application deliberately.</div></div>
    <div class="d"><div class="dt">Edmonton Secondary Suite Incentive — Waitlisted</div><div class="dx">The City of Edmonton's Secondary Suite Incentive offers up to $10,000 toward a legal internal suite (one application per owner). As of June 24, 2026 the program is waitlisted — applying now holds a position for a future intake. Availability and terms are confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# rezoning: co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Small-scale multi-unit housing — up to six dwellings mid-block — is permitted as-of-right in the RS zone under Edmonton Zoning Bylaw 20001. No rezoning is required.</div>'))

# rezoning: comparison table rows
R.append(('<tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '<tr><td>Appeal / hearing exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS zone)</td><td class="n">A new site-specific rezoning</td></tr>'))

# rezoning: two cards
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to six dwellings (mid-block)</div>The RS zone permits up to six dwellings on a mid-block lot as-of-right under Zoning Bylaw 20001 — no rezoning required. Corner sites may reach up to eight.</div>
    <div class="card2"><div class="ct">Backyard (garden) housing</div>Backyard housing is permitted in the RS zone and counts toward the lot's total dwelling count — a flexible way to add a rental unit.</div>'''))

# rezoning: what this means + amber note
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 16027 100A Avenue NW</div>
  <p>Because the RS zone already permits small-scale multi-unit housing as-of-right, no rezoning application is contemplated in this analysis. A project would advance directly to design and permitting. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2: the lot's mid-block vs corner status and its exact dimensions.</b><br><span class="sub">Corner sites can reach up to eight dwellings; mid-block sites up to six. Lot dimensions and any applicable overlays set the final buildable envelope.</span></div>'''))

# development options A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Add a Suite (entry tier)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add a single income unit to the existing home — an internal secondary suite (for example, a basement apartment) or a detached backyard (garden) suite in the rear yard. Both are permitted in the RS zone, and backyard housing counts toward the lot's total dwelling count. This is the lowest-complexity entry point, and a legal internal suite may qualify for the City's Secondary Suite Incentive (see Section 7). Unit size and siting are set by the RS built-form standards and confirmed in Phase 2.</div>'''))

# development options B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small-Scale Multiplex, up to 6 Dwellings (as-of-right)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A small-scale multiplex of up to six dwellings on a mid-block lot, permitted as-of-right in the RS zone under Zoning Bylaw 20001 — no rezoning required. Since July 8, 2025, at most two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side; the design is planned around this. Backyard housing may be included and counts toward the six-dwelling total. The governing height envelope is 10.5 m (see the Aug 1, 2026 cut-off in the Time-Sensitive section). Final unit count and layout are confirmed in Phase 2.</div>'''))

# development options C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Corner-Site Upside (up to 8 dwellings)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">If the lot is a corner site, the RS zone allows up to eight dwellings as-of-right, and developments of more than eight dwellings are limited to corner sites under the Residential Matrix. Confirming mid-block vs corner status early is worthwhile, because it sets the unit ceiling. The exact buildable envelope — coverage, setbacks, and height — is confirmed in Phase 2.</div>'''))

# goal summary (section 5) — tiered, ask the goal question
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">What's your goal?</div>
  <p>16027 100A Avenue NW sits in the RS (Small Scale Residential) zone, which supports a wide as-of-right range — from adding a single suite, up to a six-dwelling small-scale multiplex mid-block (up to eight on a corner site). <strong>To scope Phase 2 precisely, tell us your goal:</strong> steady rental income from one added suite, or a larger multi-unit build to make the most of the lot. Either path is permitted as-of-right; the right recommendation depends on what you want to achieve, and we will tailor the Builder Ready Package™ to it.</p>'''))

# summary (section 8) current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>16027 100A Avenue NW confirms a strong development option. The property is in Edmonton's RS (Small Scale Residential) zone under Zoning Bylaw 20001, where <strong>small-scale multi-unit housing is permitted as-of-right</strong> — up to six dwellings mid-block, and up to eight on a corner site — with no rezoning, no public hearing, and no Council approval required.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> from a single added suite to a six-dwelling multiplex, the RS zone permits the build without a rezoning — the exact configuration is scoped to your goal in Phase 2.</li>
  </ul>'''))

# grants table injection (tiered; every row gated for Alberta/Edmonton per config/programs.json)
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial</td><td>No-PST Advantage (Alberta)</td><td>Alberta levies no provincial sales tax, so construction materials carry only the 5% federal GST rather than a combined rate. Against an HST province this is a real structural saving on the build budget — automatic, with nothing to apply for. The dollar amount scales with the project and is quantified in Phase 2. (Applies at any project size.)</td></tr>
    <tr><td>Municipal</td><td>Edmonton Secondary Suite Incentive</td><td>Up to $10,000 toward a legal internal suite (one application per owner). Applies when the project creates a suite. Waitlisted as of June 24, 2026 — applying now holds a position for a future intake. Availability confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>100% rebate of the 5% federal GST on new purpose-built rental projects with four or more self-contained units, 90%+ held as long-term rental, construction beginning before 2031. Applies at the 4+ unit tier. Note: Alberta has no provincial sales-tax component, so only the federal GST portion applies.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred-rate, CMHC-insured financing for purpose-built rental of five or more units. Applies at the 5+ unit tier. Terms and eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental; minimum $1M loan (assessed against the Phase 2 project budget, not unit count). Can bridge into MLI Select at completion.</td></tr>
    <tr><td>Municipal</td><td>Edmonton Infill Infrastructure Fund (IIF)</td><td>Funds off-site public infrastructure for infill. Currently fully allocated ($39M across 33 projects) — not open for new applications; monitor for future rounds.</td></tr>'''))

# remove the financing-rows marker (the three any_scale rows above it always render)
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <!-- financing rows: only any_scale programs (refinance / HELOC / construction) render here; scale-gated CMHC programs are shown in the Grants & Incentives table with their thresholds. -->'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

open("report_edmonton.html", "w").write(s)

# leftover check — Toronto/Coxwell data must not survive into the Edmonton report
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "474-2023", "Bill 185", "6+1", "4+1", "HST component", "M4L", "TTC",
          "Gerrard", "315.9", "569-2013", "OLT", "Ontario"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
