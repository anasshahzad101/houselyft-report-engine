s = open("report_cambridge.html").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">258 Victoria Avenue<span>Cambridge, ON</span></div>'))
# barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">258 Victoria Avenue, Cambridge, ON&nbsp;&nbsp;N1S 3X4</div>'))
# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>258 Victoria Avenue, Cambridge, ON&nbsp;&nbsp;N1S 3X4</td></tr>
    <tr><td>Name</td><td>Joe Darcy</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU) for rental income; intends to keep the property</td></tr>'''))
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
'''    <tr><td>Municipality</td><td>Cambridge (Region of Waterloo)</td></tr>
    <tr><td>Neighbourhood</td><td>Galt</td></tr>
    <tr><td>Region</td><td>Region of Waterloo</td></tr>
    <tr><td>Property Type</td><td>Semi-detached, corner lot (per intake)</td></tr>
    <tr><td>Waste Collection</td><td>Region of Waterloo curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Cambridge Zoning By-law</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — corner lot with a long rear yard (per intake)</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU); optional interior suite for up to 3 units</td></tr>'''))
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
    258 Victoria Avenue is in Galt — the historic downtown core of Cambridge along the Grand River, an established and characterful neighbourhood in the Region of Waterloo:
    <ul>
      <li>Walkable to downtown Galt's shops, cafés, and the Gaslight District</li>
      <li>Close to the Grand River trails, parks, and waterfront</li>
      <li>Steady rental demand from area employers and post-secondary, including the University of Waterloo School of Architecture in Galt</li>
      <li>Established residential streets — the kind of character stock that rents well and holds value</li>
      <li>Note: parts of Galt fall within heritage areas; any heritage status is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))
# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Cambridge Zoning By-law) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Cambridge has updated its zoning by-law to comply.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and a detached garden suite (ARU) are permitted, subject to Cambridge's site standards — setbacks, height, and a floor-area cap. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))
# what this means
R.append(('''      <li><strong>Row Housing &amp; Stacked Row Housing:</strong> Multi-unit attached homes sharing side walls</li>
      <li><strong>Small Apartment Buildings / Multiplexes:</strong> Standalone multi-unit buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite:</strong> a self-contained home in your rear yard — your primary goal</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (e.g. a basement suite), which can be paired with the garden suite</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional units, subject to site standards</li>'''))
# time-sensitive
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Region of Waterloo ARU Funding<br><small>budget-limited</small></div><div class="dx">The Region of Waterloo has offered forgivable loans of up to $25,000 for additional residential units rented at affordable rates (roughly a 15-year term), delivered through Ontario Renovates. These programs are budget-limited and open and close — current availability is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under provincial legislation — a meaningful per-unit saving on a garden suite. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))
# options A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. The size and siting are set by Cambridge's garden-suite standards — setbacks, height, and a floor-area cap — confirmed in Phase 2. The long rear yard on a corner lot is typically a strong fit for this.</div>'''))
# options B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Garden Suite + Interior Secondary Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior secondary suite in the existing home (for example, a basement apartment) — a route to as many as three income units on the lot under Bill 23, where the property allows. This maximizes cash flow while keeping the property in your hands. Eligibility and unit sizes confirmed in Phase 2.</div>'''))
# options C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Corner-Lot &amp; Long-Yard Advantage</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Your corner, semi-detached lot with a long rear yard is an asset for a garden suite — it can allow a separate access point for the suite and more flexible siting than a typical interior lot. It also means confirming any corner-lot exterior-side-yard setbacks and servicing routes early. The exact buildable envelope for the suite is confirmed in Phase 2.</div>'''))
# goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>258 Victoria Avenue is a serviced residential lot in Galt where, under Bill 23, a detached garden suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The garden suite is the clear primary recommendation</strong>, with an interior secondary suite as an optional path to a third income unit.</p>'''))
# summary current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>258 Victoria Avenue is a serviced residential lot in Galt, Cambridge. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — including the detached garden suite you're after — with no rezoning required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds a rental income stream while you keep the property, using land you already own — the exact size and siting are confirmed in Phase 2.</li>
  </ul>'''))
# grants table
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Regional</td><td>Region of Waterloo — Affordable ARU Funding (Ontario Renovates)</td><td>Forgivable loans reported up to $25,000 for additional residential units rented at affordable rates (roughly a 15-year term). Budget-limited and periodically open/closed — current availability confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>ARU Development Charge Exemption</td><td>Additional residential units are exempt from development charges under Bill 23 — a meaningful per-unit saving on a garden suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where the suite houses an eligible relative. Confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes may offset efficient design and equipment on a new suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Rebate</td><td>May apply to a newly built rental suite; the enhanced purpose-built rental rebate targets 4+ unit projects. Applicability confirmed in Phase 2.</td></tr>'''))

fails=0
for old,new in R:
    c=s.count(old)
    if c!=1:
        print(f"[FAIL x{c}] {old[:65]!r}"); fails+=1
    else:
        s=s.replace(old,new)
open("report_cambridge.html","w").write(s)

# leftover check
for t in ["Coxwell","Toronto","Ward 19","Beaches","John Arockiaraj","654-2025","6+1","Bill 185"]:
    n=s.count(t)
    if n: print(f"LEFTOVER '{t}': {n}")
print("done, fails:",fails)
