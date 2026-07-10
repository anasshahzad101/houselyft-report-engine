s = open("report_vancouver.html").read()
R = []
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">638 East Broadway<span>Vancouver, BC</span></div>'))
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">638 East Broadway, Vancouver, BC&nbsp;&nbsp;V5T 1X6</div>'))
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>638 East Broadway, Vancouver, BC&nbsp;&nbsp;V5T 1X6</td></tr>
    <tr><td>Name</td><td>Rachel B</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>6-storey boutique hotel (micro-suite format); feasibility vs. a 16-unit residential alternative</td></tr>'''))
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
'''    <tr><td>Municipality</td><td>City of Vancouver</td></tr>
    <tr><td>Area Plan</td><td>Broadway Plan — Mount Pleasant / Broadway Corridor</td></tr>
    <tr><td>Current Zoning</td><td>C-2 Commercial (hotel-enabled — confirm C-2 sub-district / C-2A in Phase 2)</td></tr>
    <tr><td>Approved Use</td><td>Hotel (per client — rezoning / approval in principle secured)</td></tr>
    <tr><td>Density &amp; Height</td><td>~3.5 FSR, 6 storeys (~23 m) — confirm final entitlement in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Building Status</td><td>Vacant building — unoccupied for an extended period</td></tr>
    <tr><td>Lot size</td><td>~33 ft × 122 ft (≈ 4,026 sq ft / ~374 m²) — per intake, confirm in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Boutique hotel (micro-suites); 16-unit residential as an alternative</td></tr>'''))
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
    638 East Broadway sits on the East Broadway commercial corridor in Vancouver's Mount Pleasant area — a dense, high-traffic, transit-rich part of the city and a focus of the Broadway Plan:
    <ul>
      <li>On an arterial commercial strip with strong pedestrian traffic and established retail frontage</li>
      <li>Close to the Broadway–City Hall and Mount Pleasant SkyTrain stations (Broadway Subway) — a major driver of hotel demand</li>
      <li>Minutes from Downtown, False Creek, and Main Street's dining and culture — strong boutique-hotel catchment</li>
      <li>Vancouver's hotel vacancy is chronically tight and the City is actively targeting new room supply</li>
      <li>Note: commercial linkage, development cost levies, and design review shape the pro forma. (Illustrative context, not a valuation.)</li>
    </ul>'''))
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>C-2 Commercial (Broadway Plan area). Confirm the exact sub-district / new C-2A designation in Phase 2.</td></tr>
    <tr><td>Use &amp; Policy</td><td>Hotel use is enabled on C-2 commercial sites under Vancouver's Hotel Development Policy (2025) and the Broadway Plan. Vancouver's new C-2A framework allows small hotels up to 6 storeys via a development-permit path, reducing the need for a full rezoning.</td></tr>
    <tr><td>Density &amp; Height</td><td>~3.5 FSR and 6 storeys (~23 m) for the hotel. Ground-floor commercial is typically required. Final numbers confirmed against the approval and current schedule in Phase 2.</td></tr>
    <tr><td>Approval Status</td><td>Per the client, hotel approval/rezoning is in principle secured — the file moves to detailed design and development permit.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))
R.append(('''      <li><strong>Row Housing &amp; Stacked Row Housing:</strong> Multi-unit attached homes sharing side walls</li>
      <li><strong>Small Apartment Buildings / Multiplexes:</strong> Standalone multi-unit buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Boutique Hotel (micro-suites):</strong> maximize the number of hotel keys within the ~3.5 FSR / 6-storey envelope — the primary goal</li>
      <li><strong>Ground-Floor Commercial:</strong> retail / hospitality at street level, typically required on the corridor</li>
      <li><strong>Residential Alternative:</strong> approximately 16 larger (3-bedroom) units, as a comparison scenario</li>'''))
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Vancouver C-2A / Hotel Policy<br><small>active</small></div><div class="dx">Vancouver's Hotel Development Policy and new C-2A framework are actively streamlining small-hotel approvals on commercial corridors via development permit — an advantage for moving from approval to build. Confirm the current schedule and any conditions in Phase 2.</div></div>
    <div class="d"><div class="dt">DCLs &amp; Commercial Linkage<br><small>project cost</small></div><div class="dx">Broadway Plan commercial projects carry Development Cost Levies and a Commercial Linkage / amenity contribution. These are project <strong>costs</strong> (not grants) and must be built into the pro forma from Day 1. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Financing Climate</div><div class="dx">High construction and financing costs are the central risk for hotel/commercial projects right now. Lining up commercial construction financing early — before detailed design locks — materially de-risks the project.</div></div>'''))
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Boutique Hotel, Micro-Suite Format (primary goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A 6-storey boutique hotel designed around efficient micro-suites to maximize the number of rentable keys within the ~3.5 FSR envelope on the ~33 ft × 122 ft lot, with ground-floor commercial at street level. On a ~4,026 sq ft lot, 3.5 FSR yields roughly 14,000 sq ft of buildable area (confirm in Phase 2) — micro-suite efficiency is what drives the key count and the revenue-per-square-foot. This is a commercial hospitality build: room count, brand/flag strategy, and operating pro forma are defined in Phase 2, not assumed here.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Residential Alternative (~16 three-bed units)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The comparison scenario you raised: roughly 16 larger three-bedroom residential units instead of a hotel. This changes the entire model — purpose-built rental unlocks residential financing and rebates a hotel cannot use (federal GST rental rebate, CMHC MLI Select), but forgoes hotel nightly-rate revenue and carries Broadway Plan residential requirements. Phase 2 runs the hotel and the residential pro formas side by side so the numbers decide.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Mixed-Use (hotel + ground-floor commercial)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Not a separate scheme so much as a requirement to design in: the corridor typically expects active commercial at street level. A well-designed ground-floor retail or café frontage supports the hotel's guest experience, satisfies the policy expectation, and adds a second revenue line. The existing vacant building's demolition and site servicing are early-path items to confirm in Phase 2.</div>'''))
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">6-Storey Boutique Hotel (micro-suite)</div>
  <p>638 East Broadway is a C-2 commercial site on a transit-rich Broadway Plan corridor with hotel approval in principle already secured. <strong>The boutique micro-suite hotel is the primary direction</strong>, with the ~16-unit residential build as the comparison scenario. The decision is a numbers question — nightly-rate hotel revenue versus residential financing advantages — which the Phase 2 pro formas resolve.</p>'''))
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>638 East Broadway is a C-2 commercial site in Vancouver's Broadway Plan area with hotel use enabled under the City's Hotel Development Policy, and (per the client) approval in principle secured. It sits on a transit-rich corridor the City has explicitly targeted for new hotel supply.</p>
  <ul>
    <li><strong>The Hotel Opportunity:</strong> a 6-storey, ~3.5 FSR boutique hotel with ground-floor commercial — the key variables are room count (driven by micro-suite efficiency), operating strategy, and the Broadway Plan cost contributions, all resolved in Phase 2.</li>
  </ul>'''))
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td colspan="3" style="background:#fbf1de;color:#7d5a17;font-weight:600;">Note: this is a commercial hotel project — homeowner / residential grant programs (ARU grants, purpose-built rental rebates) do not apply to the hotel scenario. The items below are the relevant commercial considerations.</td></tr>
    <tr><td>Federal</td><td>GST — Input Tax Credits</td><td>GST on commercial construction is generally recoverable as input tax credits for a GST-registered commercial (hotel) operator, rather than rebated as with residential rental. Confirm structure with a tax advisor in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Residential-Only: GST Rental Rebate + CMHC MLI Select</td><td>These apply <strong>only</strong> if the ~16-unit residential alternative is chosen — the hotel cannot use them. A key input to the hotel-vs-residential comparison.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Levies (DCLs)</td><td>A per-square-foot charge on new floor area in Vancouver — a project <strong>cost</strong>, not a grant. Rates and any waivers confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Commercial Linkage / Amenity Contribution</td><td>Broadway Plan commercial projects carry a linkage/amenity contribution. Another pro-forma cost to confirm against the current policy in Phase 2.</td></tr>'''))

fails=0
for old,new in R:
    c=s.count(old)
    if c!=1:
        print(f"[FAIL x{c}] {old[:55]!r}"); fails+=1
    else:
        s=s.replace(old,new)
open("report_vancouver.html","w").write(s)
for t in ["Coxwell","Ward 19","Beaches","John Arockiaraj","654-2025","Ontario HST","Bill 185","6+1 Config"]:
    n=s.count(t)
    if n: print(f"LEFTOVER '{t}': {n}")
print("done, fails:",fails)
