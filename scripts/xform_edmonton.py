s = open("report_edmonton.html").read()
R = []

# cover addr
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">Greenough Landing NW<span>Edmonton, AB</span></div>'))

# section-1 barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">Greenough Landing NW, Edmonton, AB&nbsp;&nbsp;T5T 7C8</div>'))

# imagery block -> honest single line (Edmonton has no verified-licence source)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:0 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>Greenough Landing NW, Edmonton, AB&nbsp;&nbsp;T5T 7C8</td></tr>
    <tr><td>Name</td><td>Ashish George</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Affordable secondary suite for rental income; intends to keep the property</td></tr>'''))

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
    <tr><td>Neighbourhood</td><td>Granville (The Grange area, west Edmonton)</td></tr>
    <tr><td>Ward</td><td>sipiwiyiniwak Ward</td></tr>
    <tr><td>Community League</td><td>Glastonbury Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Edmonton for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force January 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>Civic street number to be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite (primary); optional backyard (garden) house</td></tr>'''))

# neighbourhood spotlight
R.append(('''    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    Greenough Landing NW is in Granville, part of the master-planned Grange area in west Edmonton — a newer suburban community that has grown quickly over the past decade:
    <ul>
      <li>Quick access to Anthony Henday Drive (the ring road) and Whitemud Drive for commuting across the city</li>
      <li>Close to Lewis Farms and Webber Greens shopping, schools, and recreation in the west end</li>
      <li>Newer, family-oriented housing stock on planned streets — the kind of community that supports steady rental demand</li>
      <li>Served by Edmonton Transit, with the Valley Line West LRT extension being built toward the west end</li>
      <li>Illustrative context only, not a valuation. Local amenities and service levels are confirmed in Phase 2.</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RSF — Small Scale Flex Residential Zone (Edmonton Zoning Bylaw 20001, §2.20)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RSF zone is applied in newer neighbourhoods and larger sites and is designed to give additional subdivision and development flexibility compared with the standard Small Scale (RS) zone. Site-specific standards — lot area per dwelling, setbacks, and site coverage — are confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Edmonton's Zoning Bylaw 20001 took effect January 1, 2024, replacing the former Bylaw 12800. It consolidated the older RF zones and made a broad range of small-scale housing — including secondary suites and backyard homes — permitted in residential zones without rezoning. Small-scale rules remain under active review; current figures are confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>The RSF zone permits a range of small-scale housing up to three storeys — single detached, semi-detached, row housing, and multi-unit — together with secondary suites and backyard (garden) houses. Public reporting indicates up to <strong>8 dwellings on an interior lot</strong>; the exact figure for this lot is confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means for you
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Secondary Suite:</strong> a self-contained unit inside your home (often a basement suite) — your stated goal, permitted in the RSF zone without rezoning</li>
      <li><strong>Backyard (Garden) House:</strong> a separate unit in the rear yard, permitted alongside the main dwelling</li>
      <li><strong>Row &amp; Multi-Unit Housing:</strong> the RSF zone also allows attached and multi-unit forms up to three storeys, for owners who want to add density later</li>
      <li><strong>Up to 8 dwellings (interior lot):</strong> reported as the RSF interior-lot maximum — well beyond a single suite — confirmed for this lot in Phase 2</li>'''))

# time-sensitive: replace the two Ontario-specific items (keep the CMHC item)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Small-Scale Rules Under Review<br><small>confirm current figures</small></div><div class="dx">Edmonton's Zoning Bylaw 20001 is still in its early years, and small-scale residential rules — heights, dwelling counts, and setbacks — have been refined through the City's one-year review. The RSF figures in this report reflect current public sources and are confirmed against the in-force bylaw text in Phase 2 before any design work begins.</div></div>
    <div class="d"><div class="dt">Suite Entrance &amp; Setback Rules</div><div class="dx">Under the current bylaw the number and placement of dwelling entrances facing an interior side lot line is regulated, and a side-facing entrance can trigger an additional side setback. Because a secondary suite usually needs its own entrance, this is worth designing around from Day 1 — reviewed in Phase 2. Note: Edmonton does not offer a Toronto-style development-charge waiver; local incentives differ and are verified per project.</div></div>'''))

# rezoning co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A secondary suite is a permitted use in the RSF zone under Edmonton Zoning Bylaw 20001 — no rezoning required.</div>'))

# cmp rows: OLT -> SDAB, and governing bylaw
R.append(('<tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '<tr><td>Appeal exposure (SDAB)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001</td><td class="n">A new site-specific by-law</td></tr>'))

# twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Secondary suite</div>A self-contained suite inside the home is a permitted use in the RSF zone under Zoning Bylaw 20001 — no rezoning, no public hearing, and no neighbour notification required.</div>
    <div class="card2"><div class="ct">Backyard (garden) house</div>A detached suite in the rear yard is also permitted in the RSF zone, alongside the main dwelling — subject to the bylaw's siting and size standards.</div>'''))

# what this means for {addr} + para + co-amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for Greenough Landing NW</div>
  <p>Because a secondary suite is already permitted under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm early: the civic address and the lot's servicing.</b><br><span class="sub">The contact record lists the street (Greenough Landing NW) without a civic number, and a secondary suite needs confirmed lot dimensions plus servicing (water, sewer, and a compliant entrance). Both are settled in Phase 2.</span></div>'''))

# option A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Secondary Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained secondary suite inside your existing home — most often a basement suite — rented for ongoing income while you keep the property, which is your stated goal. Permitted as-of-right in the RSF zone under Zoning Bylaw 20001; no rezoning. Suite size, ceiling height, and a separate compliant entrance are set by the bylaw's suite standards and the building code, and are confirmed in Phase 2.</div>'''))

# option B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Secondary Suite + Backyard (Garden) House — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the interior secondary suite with a detached backyard (garden) house in the rear yard — both are permitted in the RSF zone. This is a route to additional rental income on land you already own while keeping the property in your hands. The backyard house's size and siting follow the bylaw's standards; feasibility for this specific lot is confirmed in Phase 2.</div>'''))

# option C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — The Wider RSF Envelope (future upside)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">The RSF (Small Scale Flex Residential) zone permits far more than a single suite — a range of small-scale housing up to three storeys, with public reporting indicating up to 8 dwellings on an interior lot. For an owner who may want to add density later, this is meaningful upside beyond the secondary-suite plan. The exact count and buildable envelope for this lot are confirmed in Phase 2.</div>'''))

# section 5 goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Secondary Suite</div>
  <p>Greenough Landing NW is in the RSF (Small Scale Flex Residential) zone, where a secondary suite is permitted as-of-right under Zoning Bylaw 20001 — matching your goal of adding rental income while keeping the property. <strong>The secondary suite is the clear primary recommendation</strong>, with a backyard (garden) house as an optional path to a second income unit.</p>'''))

# section 7 grants table
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>CMHC — Mortgage Refinance for a Secondary Suite</td><td>CMHC-insured refinancing lets a homeowner borrow against the improved value of the home to fund a suite — reported up to 90% of the as-improved value (to a maximum property value of $2M), amortized up to 30 years. Directly suited to a secondary-suite project. Terms confirmed with a lender in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible costs (up to $7,500) when the new suite is created to house an eligible senior or an adult relative with a disability. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST New Residential Rental Property Rebate</td><td>Federal GST rebates can apply to newly built rental housing; the enhanced 100% purpose-built rental rebate targets larger projects (generally 4+ units), so a single suite typically will not meet that threshold. Applicability to your project is confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Edmonton — Secondary Suite Support</td><td>Edmonton permits secondary suites in residential zones without a public hearing, but its earlier Cornerstones secondary-suite grant is no longer active. Any current municipal support is verified against the City's live program list in Phase 2 — we never assume a grant that is not open.</td></tr>'''))

# section 8 summary
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>Greenough Landing NW confirms a strong, low-friction development option. The property is in Edmonton's RSF (Small Scale Flex Residential) zone, where a <strong>secondary suite is permitted as-of-right</strong> under Zoning Bylaw 20001 — no rezoning, no public hearing, and no neighbour notification. The RSF zone also allows a range of additional small-scale housing, giving room to grow beyond a single suite.</p>
  <ul>
    <li><strong>The Secondary-Suite Advantage:</strong> a self-contained suite adds a rental income stream while you keep the property, using space you already own — with a backyard (garden) house as an optional second unit. Exact sizes and siting are confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)
open("report_edmonton.html", "w").write(s)

# leftover check — zero remaining references to the source city / lead / wrong-city programs
for t in ["Coxwell", "Toronto", "Arockiaraj", "John", "Ward 19", "Beaches", "654-2025",
          "474-2023", "569-2013", "Bill 185", "HST", "Ontario", "OLT", "6+1", "4+1",
          "TTC", "Gerrard", "Woodbine"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
