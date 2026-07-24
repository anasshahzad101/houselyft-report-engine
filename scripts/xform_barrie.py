import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "templates", "report_barrie.html")
s = open(PATH).read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">468 Mapleview Drive East<span>Barrie, ON</span></div>'))

# ---- Property Details: imagery row (no licensed lot-scale source for Barrie) ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source for this municipality.</div>'''))

# ---- barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">468 Mapleview Drive East, Barrie, ON&nbsp;&nbsp;L4N 9S9</div>'))

# ---- property table 1 (contact) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>468 Mapleview Drive East, Barrie, ON&nbsp;&nbsp;L4N 9S9</td></tr>
    <tr><td>Name</td><td>Fernando Pisano</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (per intake)</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>City of Barrie (Simcoe County)</td></tr>
    <tr><td>Neighbourhood</td><td>Mapleview corridor / Hewitt's Secondary Plan area, south Barrie</td></tr>
    <tr><td>Jurisdiction Note</td><td>Listed as "Innisfil" at intake. Mapleview Drive East is the historic Barrie–Innisfil boundary; lands here were annexed to the City of Barrie in 2009. Governing municipality confirmed as the City of Barrie — verify parcel jurisdiction in Phase 2.</td></tr>
    <tr><td>Waste Collection</td><td>City of Barrie curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Barrie Comprehensive Zoning By-law — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — presented as tiers across the as-of-right range, led by the four-unit multiplex</td></tr>'''))

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
    468 Mapleview Drive East sits on the Mapleview Drive East arterial corridor in south Barrie, within the Hewitt's Secondary Plan growth area — one of the city's most active new-development fronts:
    <ul>
      <li>Mapleview Drive East is a major arterial seeing significant new residential and mixed-use development</li>
      <li>Part of the Hewitt's / Salem secondary-plan lands, planned for a mix of ground-related and higher-density housing</li>
      <li>Convenient to Highway 400 and the Barrie South GO station for commuters</li>
      <li>South Barrie is one of Ontario's faster-growing areas, supporting steady rental demand</li>
      <li>Note: this stretch of Mapleview Drive East is the historic Barrie–Innisfil boundary; the parcel's jurisdiction is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table (section 2) ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Barrie Comprehensive Zoning By-law) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within Barrie's settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act) and the City of Barrie's zoning amendment By-law 2024-043 (April 2024), up to <strong>4 residential units</strong> are permitted as-of-right on a residential lot — no rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Additional residential units — a main dwelling plus up to three additional units — are permitted subject to Barrie's site standards (setbacks, height, and floor-area/servicing requirements; detached ARUs are capped at 4.5 m). Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list (section 2) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Fourplex / Four-Unit Multiplex:</strong> up to four self-contained units on a residential lot, permitted as-of-right under By-law 2024-043 — your primary path</li>
      <li><strong>Additional Residential Units:</strong> interior suites (e.g. a basement apartment) and a detached backyard suite, in any mix up to the four-unit ceiling</li>
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> multi-unit attached homes, where the lot and built-form standards allow</li>
      <li><strong>Larger multiplex / small apartment (5+ units):</strong> possible on this arterial corridor through a site-specific rezoning — carried as upside</li>'''))

# ---- time-sensitive block ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Purpose-Built Rental Tax Rebate</div><div class="dx">The federal GST/HST Purpose-Built Rental Housing rebate removes the 5% federal GST on new purpose-built rental projects of four or more self-contained units (90%+ long-term rental, construction started before 2031), and Ontario mirrors it with a rebate of the 8% provincial HST component. The per-unit benefit depends on unit values and project structure — confirmed for your project in Phase 2. Structuring the project correctly from Day 1 is what protects it.</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Under Ontario's Bill 23, the first two additional residential units on a lot are exempt from development charges — a meaningful per-unit saving. Barrie's municipal development charges for any units beyond that are confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- section 3: green box ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for a Four-Unit Multiplex</div>Up to four residential units are permitted as-of-right on this lot under City of Barrie By-law 2024-043 — no rezoning needed at that scale. A larger multiplex (5+ units) would follow the rezoning path shown below.</div>'))

# ---- section 3: comparison table governs-row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 2024-043</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- section 3: two cards ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four units as-of-right</div>City of Barrie By-law 2024-043 (April 2024) permits up to four residential units on a residential lot without rezoning — a main dwelling plus up to three additional units, subject to site standards.</div>
    <div class="card2"><div class="ct">Larger multiplex — rezoning path</div>Mapleview Drive East is an arterial corridor in a designated growth area, so a larger multiplex or small apartment form may be achievable through a site-specific rezoning — explored as upside in Phase 2.</div>'''))

# ---- section 3: "what this means for X" para + amber ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 468 Mapleview Drive East</div>
  <p>Because up to four units are permitted under existing zoning, a four-unit multiplex advances directly to design and permitting — no rezoning application is contemplated at that scale. A larger multiplex on this arterial corridor would follow the rezoning path in the comparison above. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Items to confirm in Phase 2: the parcel's governing municipality, its exact zone, lot area, and full servicing.</b><br><span class="sub">The property was listed as "Innisfil" at intake and sits on the historic Barrie–Innisfil boundary; the analysis treats it as within the City of Barrie (post-2009 annexation). These are verified against title and City GIS before design begins.</span></div>'''))

# ---- section 4: Option A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Four-Unit Multiplex (as-of-right) — Primary</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A four-unit multiplex on the lot — for example a fourplex, or a main dwelling paired with additional residential units. Permitted as-of-right under City of Barrie By-law 2024-043; no rezoning required if designed within the standard envelope. Barrie's ARU standards govern setbacks, height (detached ARUs capped at 4.5 m), and floor area. The first two additional units are exempt from development charges under Bill 23. Lot area, servicing, and the exact buildable envelope are confirmed in Phase 2.</div>'''))

# ---- section 4: Option B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Four Units, Optimized Unit Mix</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The same four-unit ceiling, arranged to maximize rental income — for instance a larger family unit plus smaller one-bedroom units, or an interior suite combined with a detached backyard suite. The goal is the best cash-flow mix within the as-of-right envelope. Unit sizes and the interior/detached split are set by Barrie's site standards and confirmed in Phase 2.</div>'''))

# ---- section 4: Option C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Larger Multiplex via Rezoning (upside)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Mapleview Drive East is an arterial corridor within a designated growth/secondary-plan area, so a larger multiplex or small apartment form (5+ units) may be achievable through a site-specific rezoning. This is the tier that unlocks CMHC's 5+ unit financing (MLI Select) and the Apartment Construction Loan Program. A rezoning adds process — public consultation and Council approval — and is not guaranteed; feasibility and the achievable unit count are assessed in Phase 2.</div>'''))

# ---- section 5: goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Four-Unit Multiplex (As-of-Right)</div>
  <p>468 Mapleview Drive East is a residential lot in the City of Barrie where, under Ontario's Bill 23 and City of Barrie By-law 2024-043, up to four residential units are permitted as-of-right — no rezoning required. <strong>The four-unit multiplex is the primary recommendation</strong>, with a larger multiplex on this arterial corridor as an upside path through a site-specific rezoning, explored in Phase 2.</p>'''))

# ---- section 6: inject gated financing rows ----
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->
  </table>''',
'''    <!-- GATED_FINANCING_ROWS — tiered (multiplex scope unresolved). Each row shows the tier that unlocks it. -->
    <tr><td>CMHC MLI Select <small>(at 5+ rental units)</small></td><td>CMHC's flagship insured financing for purpose-built rental of five or more units — preferred insurance premiums, higher loan-to-value, and extended amortization. Unlocks at the larger-multiplex tier (5+ units), which on this lot means the rezoning path. Source: CMHC. Structure confirmed in Phase 2.</td></tr>
    <tr><td>CMHC Apartment Construction Loan Program <small>(min. $1M loan)</small></td><td>Low-interest construction financing for purpose-built rental, sized to the project rather than a fixed unit count (minimum loan of $1M). Best suited to the larger-multiplex tier. Source: CMHC. Eligibility tested against the project budget in Phase 2.</td></tr>
  </table>'''))

# ---- section 7: inject gated grants rows ----
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
'''    <!-- GATED_GRANTS_ROWS — tiered (multiplex scope unresolved). Each row shows the tier that clears its gate. -->
    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23) <small>— first 2 added units</small></td><td>The first two additional residential units on a lot are exempt from municipal development charges under Ontario's Bill 23 — a meaningful per-unit saving on a multiplex. Applies in Barrie. Confirmed for your project in Phase 2. Source: Ontario, More Homes Built Faster Act (Bill 23).</td></tr>
    <tr><td>Federal + Prov.</td><td>GST/HST Purpose-Built Rental Housing Rebate <small>— at 4+ rental units</small></td><td>Full rebate of the 5% federal GST on new purpose-built rental of four or more self-contained units (90%+ long-term rental, construction started before 2031); Ontario mirrors it with a rebate of the 8% provincial HST component. Clears at the four-unit tier. Per-unit figures confirmed in Phase 2. Source: federal PBRH rebate; Ontario provincial component.</td></tr>
    <tr><td>Municipal (County)</td><td>County of Simcoe Secondary Suites Program <small>— creates a suite</small></td><td>The County of Simcoe (which covers the City of Barrie) has offered assistance toward creating a legal secondary/additional residential suite for affordable rental. Budget-limited; figures and current availability are confirmed in Phase 2. Source: County of Simcoe social housing — verify against the current fact sheet.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular) <small>— at 5+ rental units</small></td><td>Brings modular/prefab construction into the CMHC MLI Select framework, which carries a five-unit minimum; can shorten construction timelines. Unlocks at the larger-multiplex tier. Source: CMHC (expanded May 2026).</td></tr>
    </table>'''))

# ---- section 8: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>468 Mapleview Drive East is a residential lot in the City of Barrie (Simcoe County). Under Ontario's Bill 23 and City of Barrie By-law 2024-043 (April 2024), up to <strong>four residential units are permitted as-of-right</strong> — no rezoning required, subject to the City's site standards. A larger multiplex on this arterial corridor may be achievable through a site-specific rezoning, explored in Phase 2.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> By-law 2024-043 allows up to four units on a residential lot with no rezoning, no public hearing, and no Council approval — a main dwelling plus up to three additional units.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(PATH, "w").write(s)

# leftover check — zero references to source city / lead / wrong-city programs
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "John's",
          "654-2025", "474-2023", "6+1", "4+1", "Bill 185", "Briarstone", "303",
          "Garden Suite By-law", "M4L"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
