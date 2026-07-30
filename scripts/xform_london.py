"""
xform_london.py — build templates/report_london.html for
241 Admiral Drive, London, ON  N5V 1H9.

Reads the master (templates/report_houselyft_master.html), swaps the
Coxwell/Toronto property, zoning, options and summary content for
London-verified content, injects the gated financing/grant rows, and
replaces the imagery placeholders with the two committed Mapbox aerials.

City coverage: London has no zoning-engine adapter, so its rules were
researched live from official sources (london.ca Additional Residential
Units page + Zoning By-law Z.-1; Ontario Bill 23; CRA PBRH rebate; CMHC;
2026 Ontario Budget). Report is tagged report-needs-review.

Scope: no homeowner development goal was supplied, so the report renders
in TIERED mode (needs-scope-review) across London's as-of-right range
(up to 4 units under Z.-1), with programs attached to the tier that
unlocks them.

Run:  python3 scripts/xform_london.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.normpath(os.path.join(HERE, "..", "templates"))
MASTER = os.path.join(TPL, "report_houselyft_master.html")
OUT = os.path.join(TPL, "report_london.html")

s = open(MASTER, encoding="utf-8").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">241 Admiral Drive<span>London, ON</span></div>'))

# ---- property-details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">241 Admiral Drive, London, ON&nbsp;&nbsp;N5V 1H9</div>'))

# ---- imagery: real Mapbox aerials (licensed, commercial print use OK) ----
R.append((
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="padding:0;position:relative;overflow:hidden;">
      <img src="london_aerial.png" alt="Aerial view of 241 Admiral Drive, London, ON" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:6.4pt;padding:2px 6px;">Aerial view — approx. 150 m across</div>
    </div>
    <div class="imgbox tall" style="padding:0;position:relative;overflow:hidden;">
      <img src="london_context.png" alt="Neighbourhood context around 241 Admiral Drive" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:6.4pt;padding:2px 6px;">Neighbourhood context — approx. 280 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery © Mapbox © OpenStreetMap © Maxar — Mapbox Satellite (commercial print use permitted). Lot boundaries are approximate; confirm on the City of London zoning map in Phase 2.</div>'''))

# ---- property table 1 (contact + goals) ----
R.append((
'''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>241 Admiral Drive, London, ON&nbsp;&nbsp;N5V 1H9</td></tr>
    <tr><td>Name</td><td>Provided at intake</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>To be confirmed — a specific goal was not provided with this request, so this report presents London's full as-of-right range (up to 4 units). Share your target and we tailor the plan.</td></tr>'''))

# ---- property table 2 (municipality etc.) ----
R.append((
'''    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 — Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m² (20 ft × 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>''',
'''    <tr><td>Municipality</td><td>City of London (single-tier)</td></tr>
    <tr><td>Neighbourhood</td><td>Northeast London (Huron Heights area)</td></tr>
    <tr><td>Official Plan</td><td>The London Plan — likely "Neighbourhoods" place type (confirmed in Phase 2)</td></tr>
    <tr><td>Governing body</td><td>City of London (London is a separated city; not administered by Middlesex County)</td></tr>
    <tr><td>Waste Collection</td><td>City of London curbside — garbage, Green Bin (organics) and yard waste; recycling via Circular Materials</td></tr>
    <tr><td>Current Bylaw</td><td>City of London Zoning By-law Z.-1</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2 (established detached-home lot)</td></tr>
    <tr><td>Development Goals</td><td>Scope not yet provided — see the tiered options below</td></tr>'''))

# ---- neighbourhood spotlight ----
R.append((
'''    <div class="ct">Neighbourhood Spotlight</div>
    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    <div class="ct">Neighbourhood Spotlight</div>
    241 Admiral Drive is in northeast London, in the established Huron Heights area — a settled, tree-lined detached-home community with steady rental demand (illustrative context, not a valuation):
    <ul>
      <li>Close to Fanshawe College — a large, consistent student-rental market in the northeast end</li>
      <li>Served by London Transit (LTC) routes along the nearby corridors; confirm the closest stop for Admiral Drive in Phase 2</li>
      <li>Thames Valley Parkway green space and the Kilally Meadows natural area lie in the northeast river valley nearby</li>
      <li>Everyday shopping along the Huron Street / Highbury Avenue / Oxford Street East corridors</li>
      <li>Established residential streets — the kind of character stock that rents well and holds value. Specific distances, school catchments and the exact neighbourhood boundary are confirmed in Phase 2.</li>
    </ul>'''))

# ---- zoning table (section 2) ----
R.append((
'''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential — City of London Zoning By-law Z.-1 (established detached-home area; likely a Residential R1 zone). Exact zone code confirmed in Phase 2.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (full municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act, 2022), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot province-wide. The <strong>City of London goes further</strong>, permitting up to <strong>4 total dwelling units</strong> as-of-right under By-law Z.-1 (only two of which may be in a detached building), with <strong>no additional parking required</strong> — no rezoning needed if the site standards are met.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite (e.g. a basement apartment) and/or a detached rear-yard suite, up to <strong>4 units total</strong>, subject to London's Z.-1 site standards — setbacks, height, floor area and lot coverage. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — up to 4 units achievable as-of-right. Confirm your target unit count and we tailor the plan; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list (section 2 cell) ----
R.append((
'''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Up to 4 units as-of-right:</strong> London permits up to four total dwelling units on a qualifying residential lot under By-law Z.-1 — no rezoning if the site standards are met</li>
      <li><strong>Internal Secondary Suites:</strong> a basement apartment or a suite within the existing home</li>
      <li><strong>Detached Rear-Yard Suite:</strong> a self-contained suite in an accessory building or a small detached home in the rear yard (up to two units may be in a detached building)</li>
      <li><strong>No parking minimum:</strong> London does not require additional parking for additional residential units</li>'''))

# ---- time-sensitive block ----
R.append((
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Ontario HST Relief — Newly Announced</div><div class="dx">The 2026 Ontario Budget proposes rebating the full provincial (8%) portion of HST on new purpose-built rental housing, mirroring the federal rebate so qualifying projects can be relieved of the full 13% HST. A related enhanced rental rebate is reported to recover up to $80,000 of the provincial portion per unit for construction beginning between April 1, 2026 and March 31, 2027. This measure is being legislated — confirm final enactment, regulations and eligibility with the Ontario Ministry of Finance / CRA before relying on it.</div></div>
    <div class="d"><div class="dt">City of London Incentives — Time-Limited</div><div class="dx">The City of London runs additional-unit and affordable-rental incentives funded in part by the federal Housing Accelerator Fund. Several are time-limited and tied to permit windows in 2026, and program amounts and eligibility change. Confirm the current programs and deadlines directly with the City of London before planning around them.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes and program intake windows can change at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: co-green box ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Up to 4 units are permitted as-of-right on a qualifying serviced residential lot under City of London By-law Z.-1 — no rezoning contemplated in this analysis.</div>'))

# ---- rezoning: "What governs your build" row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law Z.-1 (existing)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: twocard ----
R.append((
'''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>City of London By-law Z.-1 permits up to four total dwelling units on a qualifying residential lot without rezoning, subject to the site standards.</div>
    <div class="card2"><div class="ct">Detached rear-yard suite</div>Up to two of the four units may sit in a detached building — an accessory-building suite or a small detached home in the rear yard, as-of-right under Z.-1.</div>'''))

# ---- rezoning: "What this means for ..." barhead + paragraph ----
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 241 Admiral Drive</div>'))
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because up to four units are permitted as-of-right on a qualifying lot under existing City of London zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions and confirmation of the lot-specific zone.</p>'))

# ---- rezoning: amber box ----
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the lot-specific zone and site standards.</b><br><span class="sub">The exact Z.-1 zone code, setbacks, height and floor-area limits for this lot are confirmed against the City of London zoning map in Phase 2 before design proceeds.</span></div>'))

# ---- options A / B / C (tiered ladder, all as-of-right) ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Add One Suite (2 units total)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add a single self-contained suite — for example an interior basement apartment, or a detached suite in the rear yard — for ongoing rental income while you keep the property. Two units total. Permitted as-of-right under By-law Z.-1; no rezoning and no additional parking required. The first additional unit is exempt from municipal development charges under Ontario's Bill 23. Size and siting are set by London's Z.-1 standards, confirmed in Phase 2. This is the lowest-cost entry point into rental income.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Up to 3 Units (main + two ARUs)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Combine an interior secondary suite (e.g. a basement apartment) with a detached rear-yard suite for up to three units in total — the provincial as-of-right level under Bill 23. Both additional units (units two and three) are exempt from municipal development charges, and no additional parking is required. This is often the strongest income-to-cost balance for an established detached lot. Unit sizes and the rear-yard envelope are confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Up to 4 Units (London\'s as-of-right maximum)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">City of London permits up to four total dwelling units as-of-right — for example two units within the existing home plus two in a detached rear building (no more than two of the four units may be in a detached building). Four self-contained rental units, structured as purpose-built rental, is the threshold at which the federal (and newly announced Ontario) purpose-built-rental HST rebates open up. Note that the Bill 23 development-charge exemption covers the first two additional units only; the fourth unit's development-charge treatment is confirmed with the City. Feasibility of the full four-unit envelope on this lot is confirmed in Phase 2.</div>'''))

# ---- development goal summary (section 5) ----
R.append((
'''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Tell us your target — we tailor the plan</div>
  <p>241 Admiral Drive is a serviced residential lot in London where up to <strong>four units are permitted as-of-right</strong> under By-law Z.-1 — no rezoning required. A specific development goal was not provided with this request, so this report presents the full as-of-right range. <strong>Tell us your target — one rental suite, a three-unit build, or the four-unit maximum — and we will tailor the recommendation, the design and the incentive strategy to it.</strong></p>'''))

# ---- summary (section 8) current-zoning-review ----
R.append((
'''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>241 Admiral Drive confirms a strong development option. This is a serviced residential lot in London, where up to <strong>four dwelling units are permitted as-of-right</strong> under City of London By-law Z.-1 — a step beyond the provincial three-unit standard, with no additional parking required and no rezoning needed if the site standards are met.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> London permits up to four units on a qualifying residential lot with no rezoning, no public hearing and no Council approval — you build under existing zoning. The exact lot-specific zone and standards are confirmed in Phase 2.</li>
  </ul>'''))

# ---- gated financing rows (section 6) : tiered, thresholds shown ----
FIN_ROWS = (
'''<tr><td>CMHC MLI Select &amp; Apartment Construction Loan Program (ACLP)</td><td>Available at a larger scale, <strong>from five rental units</strong> — beyond London's four-unit as-of-right envelope, so a five-plus-unit project would move into a rezoning / land-assembly path. MLI Select offers preferred multi-unit mortgage-loan insurance (minimum five units); the ACLP offers low-cost construction financing (minimum five self-contained units and a minimum $1,000,000 loan). Confirm current CMHC intake before relying on either. Shown here so you can see what scaling up unlocks.</td></tr>''')
s2 = re.sub(r'<!-- GATED_FINANCING_ROWS.*?-->', lambda m: FIN_ROWS, s, count=1, flags=re.S)
if s2 == s:
    print("[FAIL] GATED_FINANCING_ROWS marker not found")
s = s2

# ---- gated grant rows (section 7) : tiered, thresholds shown ----
GRANT_ROWS = (
'''<tr><td>Provincial</td><td>Development-Charge Exemption for Additional Units (Bill 23)</td><td>Under Ontario's Bill 23, the first two additional residential units (units two and three) on a serviced lot are exempt from municipal development charges, parkland dedication and cash-in-lieu — a meaningful per-unit saving. Applies at 2–3 units. The fourth unit's development-charge treatment is confirmed with the City of London.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>At <strong>four or more</strong> self-contained rental units held as long-term rental (90%+), a full 100% rebate of the federal GST (5%) applies, with no cap. Construction must begin after Sept 13, 2023 and before 2031, and complete before 2036. Opens up at the four-unit option. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>Ontario PBRH / Rental HST Rebate (2026 Budget — announced)</td><td>The 2026 Ontario Budget proposes rebating the provincial (8%) portion of HST on qualifying new purpose-built rental, mirroring the federal rebate (a reported enhanced rebate recovers up to $80,000 of the provincial portion per unit for construction beginning April 1, 2026 – March 31, 2027). At four or more rental units. This measure is being legislated — confirm final enactment and eligibility before relying on it.</td></tr>
    <tr><td>Municipal</td><td>City of London Additional-Unit &amp; Affordable-Rental Incentives</td><td>The City of London runs additional-residential-unit and affordable-rental incentive programs (grants / forgivable loans) funded in part by the federal Housing Accelerator Fund, with reported per-unit amounts in roughly the $20,000–$45,000 range depending on the specific program and stream. Amounts, eligibility and application windows are time-limited and change — the exact figure for your project is confirmed directly with the City of London in Phase 2.</td></tr>''')
s2 = re.sub(r'<!-- GATED_GRANTS_ROWS.*?-->', lambda m: GRANT_ROWS, s, count=1, flags=re.S)
if s2 == s:
    print("[FAIL] GATED_GRANTS_ROWS marker not found")
s = s2

# ---- apply exact-string replacements with occurrence guard ----
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

# ---- leftover check: nothing Toronto/Coxwell/gated-out may survive ----
leftovers = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arock", "654-2025",
             "474-2023", "Bill 185", "6+1", "4+1", "M4L", "TTC", "nine wards",
             "Garden Suite By-law", "Simcoe", "Greener Homes", "Multigenerational",
             "MLI Select on", "303 Coxwell"]
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done. fails={fails}, bytes={len(s)}, out={OUT}")
