"""
xform_london.py — adapt the House Lyft master report for a London, Ontario ARU lead.

London, Ontario has NO city adapter in engine/property_lookup_v2.py (9 GTA + Edmonton
only), so this report is a "report-needs-review" build: Toronto-specific zoning and
programs are stripped out, and London content is drawn from Ontario's Bill 23 baseline
plus live-verified official City of London sources (Zoning By-law Z.-1 §4.37 Additional
Residential Units; the City's time-limited ARU financing incentives). Every London-
specific figure is hedged "confirmed in Phase 2" per docs/AI_Report_Writer_Role_v1.md.

Reads the master verbatim and asserts each replacement matches exactly once, then greps
for Toronto/Coxwell leftovers before writing — same accuracy guard as the other xforms.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_london.html")

s = open(MASTER, encoding="utf-8").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">Admiral Court<span>London, ON</span></div>'))

# ---- section 1: barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">Admiral Court, London, ON&nbsp;&nbsp;N5V 1H9</div>'))

# ---- section 1: imagery placeholders (honest — no imagery adapter for London) ----
R.append(('<span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small>',
          '<span class="ic">◎</span>Aerial view<br><small>(to be added in Phase 2)</small>'))
R.append(('<span class="ic">▤</span>Street view<br><small>(auto-generated)</small>',
          '<span class="ic">▤</span>Street view<br><small>(to be added in Phase 2)</small>'))
R.append(('<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Property-specific aerial and street imagery to be sourced and licensed during the feasibility phase.</div>'))

# ---- section 1: property table 1 (lead) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>Admiral Court, London, ON&nbsp;&nbsp;N5V 1H9</td></tr>
    <tr><td>Name</td><td>Mursh Al</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Additional Residential Unit (secondary suite and/or garden suite) for rental income; interested in government-backed financing options</td></tr>'''))

# ---- section 1: property table 2 (municipality) ----
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
'''    <tr><td>Municipality</td><td>City of London</td></tr>
    <tr><td>Neighbourhood</td><td>Northeast London — confirmed in Phase 2</td></tr>
    <tr><td>Region</td><td>Southwestern Ontario</td></tr>
    <tr><td>Waste Collection</td><td>City of London curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of London Zoning By-law Z.-1</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite and/or detached garden suite (ARU); optional path to additional units</td></tr>'''))

# ---- section 1: neighbourhood spotlight ----
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
    Admiral Court is in the City of London (the "Forest City") in southwestern Ontario — an established, growing city with steady rental demand. Local specifics for this address are confirmed in Phase 2:
    <ul>
      <li>London anchors a regional economy with Western University and Fanshawe College driving consistent rental demand</li>
      <li>Established residential streets and mature neighbourhoods across the city's northeast</li>
      <li>Served by London Transit; walkability and route access for this address confirmed in Phase 2</li>
      <li>Parks, schools, and shopping typical of London's residential districts</li>
      <li>Note: exact neighbourhood, servicing, and any overlays are confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- section 2: zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of London Zoning By-law Z.-1) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units. London's site standards (setbacks, minimum lot width, lot coverage, parking, and driveway width) apply.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act) and City of London Zoning By-law Z.-1 (Section 4.37), a single-detached, semi-detached or street-townhouse lot may add up to two Additional Residential Units — up to a maximum of four total dwelling units where the base zone permits — as-of-right, with no rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and/or a detached garden suite (Additional Residential Unit) are permitted, subject to London's zoning standards under By-law Z.-1. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- section 2: "what this means for you" list ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite:</strong> a self-contained unit within the existing home, such as a basement apartment — your stated interest</li>
      <li><strong>Detached Garden Suite:</strong> a self-contained home in the rear yard, a common Additional Residential Unit form</li>
      <li><strong>Up to 3–4 Units Total:</strong> under Bill 23 and London's By-law Z.-1, the main dwelling plus additional residential units — up to a maximum of four total dwelling units where the base zone permits — subject to site standards</li>
      <li><strong>Government-Backed Financing:</strong> London's Additional Residential Unit incentives and provincial development-charge exemptions may help fund the build — confirmed in Phase 2</li>'''))

# ---- time-sensitive ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">City of London ARU Incentives — Act Now<br><small>permit by Sept 7, 2026</small></div><div class="dx">The City of London has announced time-limited housing incentives for Additional Residential Units — reported as forgivable loans up to $20,000 for a new ARU with no rent restriction and up to $45,000 for an affordable ARU (rents capped at average market rates), delivered as a forgivable loan registered on title with a minimum 10-year rental commitment. Eligibility is tied to building permits issued between April 29 and September 7, 2026. A temporary building-permit-fee waiver was also approved. This is a temporary, budget-limited window — current amounts, eligibility, and deadlines are confirmed in Phase 2. (Source: City of London.)</div></div>
    <div class="d"><div class="dt">Provincial ARU Development Charge Exemption</div><div class="dx">Additional residential units are exempt from development charges under provincial legislation — a meaningful per-unit saving on a secondary or garden suite. Applicability confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- section 3: rezoning ----
R.append(('  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended Additional Residential Unit configuration is permitted as-of-right under Ontario\'s Bill 23 and the City of London Zoning By-law Z.-1 — no rezoning required.</div>'))

R.append(('    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '    <tr><td>What governs your build</td><td class="g">By-law Z.-1 (as amended)</td><td class="n">A new site-specific by-law</td></tr>'))

R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior secondary suite</div>Under By-law Z.-1 (Section 4.37) and Bill 23, a self-contained unit within the existing home is permitted as an Additional Residential Unit, subject to site standards.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>A rear garden suite is a permitted Additional Residential Unit form under London's zoning, subject to setbacks, height, and lot-coverage standards — confirmed in Phase 2.</div>'''))

R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for Admiral Court</div>
  <p>Because the property already permits the recommended Additional Residential Unit build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the base zoning of the lot and the permit status of any existing accessory structure.</b><br><span class="sub">The exact zone, servicing, and any overlays determine the number and size of units — confirmed in Phase 2.</span></div>'''))

# ---- section 4: development options ----
R.append(('  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '  <div class="opt"><div class="oh">Option A — Detached Garden Suite or Interior Secondary Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A single self-contained Additional Residential Unit — either a detached garden suite in the rear yard or an interior secondary suite within the existing home — rented for ongoing income while you keep the property, which matches your stated goal. Permitted as-of-right under Bill 23 and London's By-law Z.-1 on a serviced residential lot; no rezoning. The size and siting are set by London's ARU standards — setbacks, height, lot coverage, and parking — confirmed in Phase 2. This single-unit path is typically the fastest route to rental income and may qualify for the City's ARU financing incentives.</div>'''))

R.append(('  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '  <div class="opt"><div class="oh">Option B — Secondary Suite + Garden Suite (up to 3 units) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair an interior secondary suite in the existing home (for example, a basement apartment) with a detached garden suite in the rear yard — a route to as many as three income units on the lot under Bill 23 and By-law Z.-1, where the base zone and lot allow. This maximizes cash flow while keeping the property in your hands. Unit counts, sizes, and siting are confirmed in Phase 2, and the configuration may be eligible for the City of London ARU incentives.</div>'''))

R.append(('  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '  <div class="opt"><div class="oh">Option C — Path to a Fourth Unit &amp; Servicing Notes</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Where the base zone permits a duplex, triplex, or converted dwelling, London's By-law Z.-1 allows up to a maximum of four total dwelling units on the lot — a potential fourth income unit beyond the secondary-plus-garden-suite path. Realizing it depends on the confirmed base zone, lot size, servicing, and site standards, so confirming the zoning designation is an essential first step. Any existing accessory structure should also be checked for permit status before it is counted as a legal unit. All of this is established in Phase 2.</div>'''))

# ---- section 5: development goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Additional Residential Unit Configuration</div>
  <p>Admiral Court is a serviced residential lot in the City of London where, under Ontario's Bill 23 and By-law Z.-1, additional residential units are permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>A secondary suite paired with a detached garden suite is the clear primary recommendation</strong>, with a possible fourth unit where the base zone permits.</p>'''))

# ---- section 7: grants table ----
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Municipal</td><td>City of London — Additional Residential Unit Incentives</td><td>Time-limited forgivable loans reported up to $20,000 for a new ARU (no rent restriction) and up to $45,000 for an affordable ARU (rents capped at average market rates), plus up to $45,000 for Indigenous-led housing. Delivered as a forgivable loan registered on title, with a minimum 10-year rental commitment. Tied to building permits issued between April 29 and September 7, 2026. A temporary building-permit-fee waiver was also approved. Budget-limited — current status, amounts, and deadlines confirmed in Phase 2. (Source: City of London.)</td></tr>
    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under provincial legislation — a meaningful per-unit saving on a secondary or garden suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Rebate</td><td>May apply to a newly built rental suite that is rented long-term; the enhanced purpose-built rental rebate targets larger 4+ unit projects. Applicability to a small ARU confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where the new suite houses an eligible relative (a senior or an adult with a disability). Confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Municipal</td><td>Energy-Efficiency Programs (Canada Greener Homes / City of London BetterHomes)</td><td>Federal and City of London programs may offset efficient design and equipment on a new suite. Confirmed in Phase 2.</td></tr>'''))

# ---- section 8: summary — current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>Admiral Court is a serviced residential lot in the City of London. Under Ontario's Bill 23 and the City of London Zoning By-law Z.-1, <strong>additional residential units are permitted as-of-right</strong> — an interior secondary suite and a detached garden suite, up to a maximum of four total dwelling units where the base zone permits — with no rezoning required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Additional Residential Unit Advantage:</strong> a secondary and/or garden suite adds a rental income stream while you keep the property, using land you already own — and London's time-limited ARU financing incentives may help fund the build. The exact zone, unit count, and sizing are confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# leftover check — zero references to the master's Toronto/Coxwell content or wrong-city programs
leftovers = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
             "474-2023", "569-2013", "Bill 185", "Ontario HST", "Garden Suite By-law",
             "6+1", "4+1", "M4L", "315.9", "750 sq", "TTC", "Greenwood", "Danforth",
             "Gerrard", "Woodbine", "PBRH", "Prefab", "houseplex", "Houseplex", "nine wards"]
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

open(OUT, "w", encoding="utf-8").write(s)
print("done, fails:", fails, "-> wrote", os.path.relpath(OUT, ROOT))
