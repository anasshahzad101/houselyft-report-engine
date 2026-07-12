"""xform_mississauga.py — turn the House Lyft master into the report for
3408 Monica Drive, Mississauga (Malton), zoned R4-64.

Follows the established xform pattern: every replacement must match exactly
once, then a leftover grep guarantees no source-city (Toronto/Coxwell) data
survives. Property/zoning/market/financing content is swapped; the House Lyft
prose sections (Why / How to use / Advantage / Financing / Next Steps / CTA)
are kept verbatim.

Facts grounded in engine/property_lookup_v2 (R4-64, base R4, 4 units) plus
live City of Mississauga / Ontario / CRA sources; every unpublished figure is
hedged to Phase 2 per docs/AI_Report_Writer_Role_v1.md.
"""
import os

HTML = os.path.join(os.path.dirname(__file__), "..", "templates", "report_mississauga.html")
s = open(HTML).read()
R = []

# cover address
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">3408 Monica Drive<span>Mississauga, ON</span></div>'))

# section 1 barhead
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">3408 Monica Drive, Mississauga, ON&nbsp;&nbsp;L4T 3E7</div>'))

# imagery slots + licence placeholder (no licensed source for this city -> honest, empty)
R.append(('''    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(added in Phase 2)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(added in Phase 2)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Site aerial and street-view imagery are prepared during the feasibility phase; no third-party imagery is embedded in this preliminary report.</div>'''))

# property table 1 (contact)
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>3408 Monica Drive, Mississauga, ON&nbsp;&nbsp;L4T 3E7</td></tr>
    <tr><td>Name</td><td>Jumaal Khan</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU) in the rear yard for rental income; intends to keep the property</td></tr>'''))

# property table 2 (municipality)
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
'''    <tr><td>Municipality</td><td>Mississauga (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Malton</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Current Zoning</td><td>R4-64 — Detached Dwellings</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Mississauga Zoning By-law 0225-2007 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU); optional interior additional unit</td></tr>'''))

# neighbourhood spotlight
R.append(('''    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    3408 Monica Drive is in Malton, an established residential community in northeast Mississauga within the Region of Peel:
    <ul>
      <li>Close to Toronto Pearson International Airport — a major regional employment hub</li>
      <li>Served by Malton GO Station on the Kitchener line, with MiWay local bus service</li>
      <li>Quick access to Highways 427, 409, and 401 for commuters</li>
      <li>Neighbourhood amenities around Westwood Square and the Malton Community Centre</li>
      <li>Steady rental demand from airport-area employment and established residential streets (illustrative context, not a valuation)</li>
    </ul>'''))

# section 2 zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>''',
'''    <tr><td>Current Zoning</td><td>R4-64 — Detached Dwellings (City of Mississauga Zoning By-law 0225-2007, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (municipal water &amp; sewer) within the settlement area — the provincial criteria for as-of-right additional residential units. The R4 zone permits detached dwellings; additional units follow the City's Additional Residential Unit standards (Zoning By-law 0225-2007, Section 4.1.1.9).</td></tr>
    <tr><td>Recent Changes</td><td>Mississauga permits up to <strong>4 residential units (a fourplex)</strong> as-of-right on eligible low-rise residential lots, building on the provincial floor under Ontario's Bill 23 — no rezoning required. The exact amending provisions are confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior additional unit and a detached additional dwelling unit (garden suite) are permitted, subject to Mississauga's site standards — setbacks, height, lot coverage, and a floor-area cap. One garden suite is allowed per lot. Confirmed in Phase 2.</td></tr>'''))

# section 2 "what this means for you"
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite (ADU):</strong> a self-contained home in your rear yard — your primary goal</li>
      <li><strong>Interior Additional Unit:</strong> a unit within the existing home (e.g. a basement suite), which can be paired with the garden suite</li>
      <li><strong>Up to 4 units total:</strong> the property may support the main dwelling plus additional units, subject to Mississauga's site standards</li>'''))

# time-sensitive (replace the two Toronto boxes; keep CMHC verbatim)
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Additional-Unit DC Exemption<br><small>already in effect</small></div><div class="dx">Under Ontario's Bill 23, the second and third residential units on a lot are exempt from development charges and parkland fees — so a garden suite as your second unit is already exempt from these City charges under provincial law. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Mississauga Gentle Density Incentive<br><small>permit by Dec 31, 2027</small></div><div class="dx">Mississauga's Gentle Density Incentive Program grants back the City development charges and cash-in-lieu-of-parkland tied to a fourth unit, with a building-permit application, a 25-year rental condition, and no condo conversion. The development-charges incentive has been extended to December 31, 2027, and programs like this are budget-limited. It becomes financially meaningful if your project reaches a fourth unit — confirmed in Phase 2.</div></div>'''))

# section 3 co-green
R.append(('  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended garden suite is permitted as-of-right as an additional dwelling unit under Mississauga\'s zoning — no rezoning required.</div>'))

# section 3 comparison table "what governs" row
R.append(('    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '    <tr><td>What governs your build</td><td class="g">Zoning By-law 0225-2007 (as amended)</td><td class="n">A new site-specific by-law</td></tr>'))

# section 3 twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>Mississauga permits up to four residential units as-of-right on an eligible residential lot, building on the provincial Bill 23 floor — no rezoning required. Exact provisions confirmed in Phase 2.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>A detached additional dwelling unit (garden suite) is permitted in the rear yard — one per lot, one or two storeys — subject to Mississauga's site standards for size, height, and setbacks.</div>'''))

# section 3 "what this means" heading + paragraph + amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 3408 Monica Drive</div>
  <p>Because 3408 Monica Drive already permits the recommended garden suite under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Items to confirm in Phase 2: the rear-yard fit for the garden suite, and a conservation-authority screening.</b><br><span class="sub">Setbacks, lot coverage, height, and a servicing connection are set by Mississauga's zoning standards. Malton sits within the Toronto and Region Conservation Authority's Etobicoke Creek watershed, so whether this parcel falls in a regulated or flood-prone area is confirmed before design proceeds.</span></div>'''))

# section 4 option A
R.append(('  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '  <div class="opt"><div class="oh">Option A — Detached Garden Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right as an additional dwelling unit on this serviced residential lot; no rezoning, and one garden suite is allowed per lot (one or two storeys). The City even publishes pre-approved garden-suite design plans — compact studio and one-bedroom models of roughly 40–55 m² — as examples; your suite's maximum size, height, and setbacks are set by Mississauga's zoning standards and confirmed in Phase 2. Parking, servicing, and the exact buildable envelope are confirmed in Phase 2.</div>'''))

# section 4 option B
R.append(('  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '  <div class="opt"><div class="oh">Option B — Garden Suite + Interior Additional Unit</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior additional unit in the existing home (for example, a basement apartment). Mississauga permits up to four residential units on an eligible lot, so there is room to add income units beyond the garden suite, subject to the City's standards. This maximizes cash flow while keeping the property in your hands. Eligibility and unit sizes are confirmed in Phase 2.</div>'''))

# section 4 option C
R.append(('  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '  <div class="opt"><div class="oh">Option C — Additional-Unit Incentive &amp; DC Exemption</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Two programs support the economics. First, under Ontario's Bill 23 the second and third units on a lot are already exempt from City development charges and parkland fees — a direct saving on your garden suite. Second, Mississauga's Gentle Density Incentive Program grants back the City charges tied to a fourth unit (with a building-permit application, a 25-year rental condition, and no condo conversion; extended to December 31, 2027) — most relevant if the project grows to four units. No fixed grant amount is published, and programs are budget-limited; current terms are confirmed in Phase 2.</div>'''))

# section 5 development goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>3408 Monica Drive is a serviced residential lot in Malton where a detached garden suite is permitted as-of-right as an additional dwelling unit — matching your goal of adding rental income while keeping the property. <strong>The garden suite is the clear primary recommendation</strong>, with an interior additional unit as an optional path to further income.</p>'''))

# section 7 grants table (four Toronto rows -> Mississauga / Ontario / federal)
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>Additional-Unit DC &amp; Parkland Exemption (Bill 23)</td><td>Under Ontario's More Homes Built Faster Act (Bill 23), the second and third residential units on a lot are exempt from development charges and parkland dedication or cash-in-lieu — so your garden suite (a second unit) is already exempt from these City charges under provincial law. The first (primary) unit remains subject to charges. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Mississauga Gentle Density Incentive Program (Municipal Charges Grant)</td><td>A City grant, part of Mississauga's Community Improvement Plan, that grants back the City development charges and cash-in-lieu-of-parkland attributable to a fourth unit in a fourplex. Conditions include a building-permit application, a legal agreement, and keeping one unit as a rental for 25 years with no condo conversion. The development-charges incentive has been extended to December 31, 2027. Budget-limited; no fixed per-unit amount is published (the grant equals the actual charges owed). Most relevant if the project reaches a fourth unit — confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where the suite houses an eligible relative (a senior, or an adult eligible for the disability tax credit). Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes may offset efficient design and equipment on a new suite. Availability confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Rental Rebates</td><td>The enhanced Purpose-Built Rental Housing rebate targets projects of four or more self-contained rental units, so a single garden suite does not qualify on its own; the separate New Residential Rental Property rebate may apply to one rental unit. Applicability to your project is confirmed in Phase 2.</td></tr>'''))

# section 8 summary — current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>3408 Monica Drive is a serviced residential lot in Malton, Mississauga, zoned R4-64 (Detached Dwellings). A detached garden suite is permitted as-of-right as an additional dwelling unit — including the backyard suite you're after — with no rezoning required, subject to the City's site standards. Mississauga also permits up to four residential units on an eligible lot.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds a rental income stream while you keep the property, using land you already own — the exact size and siting are confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(HTML, "w").write(s)

# leftover check — zero source-city / master references may survive
leftovers = ["Coxwell", "Toronto", "John", "Arockiaraj", "johneeraj", "Ward 19",
             "Beaches", "654-2025", "474-2023", "569-2013", "Bill 185", "Woodbine",
             "Greenwood", "TTC", "Danforth", "Gerrard", "6+1", "4+1", "houseplex",
             "M4L 3B5", "315.9"]
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
