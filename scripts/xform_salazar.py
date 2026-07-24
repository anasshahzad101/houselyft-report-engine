"""
xform_salazar.py — Shirley Salazar, 31 Snowy Owl Way, Scarborough (Toronto).

Master -> per-lead report. This lead's stated goal (intake field
EPzqHHy5AU2iIvHIAhKf) is "Garden Suite, Laneway Home or ADU" -> scoped,
units_added=1. So the report LEADS with the garden suite and presents the
Ward 23 sixplex permission as upside (Ward 23 / Scarborough North is the one
Scarborough pilot ward in the nine-ward sixplex set, OPA 818 / By-law 654-2025).

Zoning verified live: Toronto adapter, RD (x649), Ward 23 (Scarborough North),
6 units as-of-right + ADU stacking. Aerials: City of Toronto Orthophoto 2025.

Run from templates/:  python3 ../scripts/xform_salazar.py
"""
import base64, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TPL = os.path.join(ROOT, "templates")
SCRATCH = os.environ.get("HL_AERIAL_DIR",
    "/tmp/claude-0/-home-user-houselyft-report-engine/5807b8f4-de18-5a41-bb3a-935690cfeede/scratchpad")

s = open(os.path.join(TPL, "report_houselyft_master.html")).read()
R = []

# ---- COVER ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">31 Snowy Owl Way<span>Scarborough, Toronto, ON</span></div>'))

# ---- Property Details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">31 Snowy Owl Way, Scarborough, Toronto, ON&nbsp;&nbsp;M1X</div>'))

# ---- Aerial image row (real Toronto 2025 orthophoto, two views) ----
lot_b64 = base64.b64encode(open(os.path.join(SCRATCH, "aerial_lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCRATCH, "aerial_ctx.jpg"), "rb").read()).decode()
old_imgrow = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_imgrow = ('''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Aerial view &mdash; approx. 90&nbsp;m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Neighbourhood context &mdash; approx. 220&nbsp;m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence &ndash; Toronto.</div>''' % (lot_b64, ctx_b64))
R.append((old_imgrow, new_imgrow))

# ---- Property table 1 (contact) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>31 Snowy Owl Way, Scarborough, Toronto, ON&nbsp;&nbsp;M1X (per intake)</td></tr>
    <tr><td>Name</td><td>Shirley Salazar</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite / laneway home / ADU (per intake) &mdash; add rental income while keeping the property</td></tr>'''))

# ---- Property table 2 (municipality) ----
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
'''    <tr><td>Municipality</td><td>Toronto (former Scarborough)</td></tr>
    <tr><td>Neighbourhood</td><td>Morningside Heights (Scarborough North)</td></tr>
    <tr><td>Ward</td><td>Ward 23 — Scarborough North</td></tr>
    <tr><td>Community Council</td><td>Scarborough Community Council</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (as amended) — zone RD, exception 900.3.10(649)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite / ADU (primary); multiplex up to six units as-of-right is available upside</td></tr>'''))

# ---- Neighbourhood Spotlight ----
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
    31 Snowy Owl Way is in Morningside Heights, a residential community in Scarborough North in the city's northeast — an established, family-oriented area well suited to a rental garden suite. (Illustrative context, not a valuation; details confirmed in Phase 2.)
    <ul>
      <li>Part of the broader Malvern / Morningside Heights area of Scarborough North</li>
      <li>Close to Rouge National Urban Park and the Rouge River valley green space</li>
      <li>Convenient to Highway 401 and Morningside Avenue for regional access</li>
      <li>Served by TTC bus routes with connections toward Scarborough Centre and the rapid-transit network — confirm specific routes in Phase 2</li>
      <li>Steady rental demand in northeast Scarborough from area employers, colleges, and University of Toronto Scarborough nearby</li>
    </ul>'''))

# ---- Zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD (x649) — Residential Detached, exception 900.3.10(649) (Toronto Zoning By-law 569-2013, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. A rear garden suite is permitted as-of-right in residential zones city-wide under Toronto's Garden Suite By-law (2022), subject to setback, height, angular-plane, and floor-area standards — confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023). Ward 23 (Scarborough North) is the one Scarborough pilot ward — added alongside eight Toronto &amp; East York wards — where up to 6 units are permitted as-of-right (OPA 818 / Zoning By-law 654-2025, June 2025). A garden suite may combine with the main dwelling. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>A detached garden suite / ADU (your goal) plus interior secondary suites, and — as upside — a detached houseplex of up to <strong>6 residential units</strong> as-of-right in Ward 23, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "What this means" list (section 2) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite / ADU:</strong> a self-contained home in your rear yard — your primary goal — rented for income while you keep the property</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> an interior secondary suite (such as a basement apartment) can be paired with the garden suite to add a second income unit</li>
      <li><strong>Detached Houseplex (upside):</strong> Ward 23's sixplex permission means a standalone multi-unit home of up to six units is also available as-of-right</li>
      <li><strong>Townhouse &amp; Low-Rise Forms (upside):</strong> multi-unit attached and small apartment forms may also be possible, subject to site standards</li>'''))

# ---- Time-Sensitive ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">ARU Development-Charge Exemption<br><small>in effect now</small></div><div class="dx">A garden suite / additional residential unit is exempt from municipal development charges under Ontario's Bill 23 — a direct per-unit saving on the suite. In Toronto, development charges are also waived on the first six units on a lot (Bill 185), so a garden suite carries no DC cost. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Ontario HST Rebate — if you scale up<br><small>window closes Mar 31, 2027</small></div><div class="dx">If you pursue the multiplex upside (four or more purpose-built rental units), Ontario's 2026 Budget added a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on the federal PBRH rebate. This applies to 4+ unit rental projects — not a single garden suite — and requires the agreement be signed between April 1, 2026 and March 31, 2027.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- Section 3: green box ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Your garden suite — and, as upside, a multiplex of up to six units — are both permitted as-of-right on this Ward 23 lot. No rezoning is contemplated.</div>'))

# ---- Section 3: comparison table last row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Garden Suite By-law + 474-2023 / 654-2025</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- Section 3: twocard ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Rear garden suite (your goal)</div>Toronto's Garden Suite By-law (2022) permits a rear ancillary suite as-of-right in residential zones city-wide, subject to setback, height, and floor-area standards.</div>
    <div class="card2"><div class="ct">Six-unit houseplex (upside)</div>Ward 23 (Scarborough North) is the one Scarborough pilot ward — with eight Toronto &amp; East York wards — where By-law 654-2025 permits up to six units without rezoning.</div>'''))

# ---- Section 3: "What this means for ..." + amber ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 31 Snowy Owl Way</div>
  <p>Because your garden suite is permitted under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>A few items to confirm in Phase 2:</b><br><span class="sub">the lot's exact dimensions and rear-yard fit for a garden suite, servicing routes, and any corner or side-yard setbacks — all standard checks for garden-suite siting.</span></div>'''))

# ---- Section 4: Option A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite / ADU (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Toronto's Garden Suite By-law (2022); no rezoning required. Size and siting are set by the City's garden-suite standards — setbacks, height, angular planes, and a floor-area cap — confirmed in Phase 2. No parking is required. As an additional residential unit it is exempt from development charges (Bill 23), and it also falls within Toronto's first-six-units DC waiver (Bill 185).</div>'''))

# ---- Section 4: Option B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Garden Suite + Interior Secondary Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior secondary suite in the existing home (for example, a basement apartment) — a route to additional income units on the lot while keeping the property in your hands. Interior and detached units combine under Toronto's multiplex and suite rules. Eligibility, unit sizes, and fire/servicing requirements are confirmed in Phase 2.</div>'''))

# ---- Section 4: Option C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Scale Up: Multiplex of up to Six Units (upside)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Because 31 Snowy Owl Way is in Ward 23 (Scarborough North) — the one Scarborough pilot ward where up to six units are permitted as-of-right (By-law 654-2025) — you also have the option to build a detached houseplex of up to six units, with a garden suite on top of that, all without rezoning. Development charges are waived on the first six units (Bill 185) and no parking is required. This is a larger-scale path than your stated garden-suite goal; it is presented here as upside should you wish to maximize the lot. The buildable envelope is confirmed in Phase 2.</div>'''))

# ---- Section 5: Goal Summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>31 Snowy Owl Way is a residential lot in Ward 23 (Scarborough North) where a detached garden suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The garden suite is the clear primary recommendation</strong>, with an interior secondary suite as an optional second income unit, and a multiplex of up to six units available as upside because Ward 23 is one of only nine sixplex wards in Toronto.</p>'''))

# ---- Section 7: inject gated grant rows ----
R.append(('''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>''',
'''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>ARU Development-Charge Exemption (Bill 23)</td><td>A garden suite / additional residential unit is exempt from municipal development charges under Ontario's More Homes Built Faster Act (Bill 23) — a direct per-unit saving on the suite. Applies to the first two additional units. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>The City waives development charges on the first six units on a lot (Bill 185, January 2025), which includes a garden suite. No application required for compliant builds. Parking minimums are also waived city-wide (since February 2022).</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where the new suite houses an eligible relative (a senior 65+ or a person eligible for the Disability Tax Credit), this credit may return 15% on up to $50,000 of eligible cost. Eligibility is occupant-specific — confirmed in Phase 2.</td></tr>
    <tr><td>Upside (4+ / 5+ units)</td><td>Federal rental programs — if you scale to a multiplex</td><td>Should you pursue the multiplex upside on this Ward 23 lot, additional federal programs open at scale: the GST/HST Purpose-Built Rental Housing Rebate (4+ self-contained rental units, 90%+ long-term rental, construction before 2031) and CMHC MLI Select (5+ rental units); CMHC's Apartment Construction Loan Program requires a minimum $1M loan. These do not apply to a single garden suite — they are shown here so you can see what greater scale unlocks. Confirmed in Phase 2.</td></tr>'''))

# ---- Section 8: Summary current-zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>31 Snowy Owl Way confirms a strong development option. A detached garden suite — your stated goal — is permitted as-of-right on this residential lot under Toronto's Garden Suite By-law, letting you add a rental income stream while keeping the property. On top of that, the lot sits in Ward 23 (Scarborough North) — one of only <strong>nine wards across Toronto where up to six units are permitted as-of-right</strong>, and the single Scarborough pilot ward — a regulatory advantage most Toronto homeowners do not have.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds income using land you already own — permitted as-of-right, no rezoning, with development charges exempt/waived.</li>
    <li><strong>The Six-Unit Upside:</strong> because this is one of nine sixplex wards (By-law 654-2025), you can scale to a multiplex of up to six units as-of-right should you choose — no rezoning, no public hearing, no Council approval.</li>
  </ul>'''))

# ---- apply ----
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(TPL, "report_salazar.html")
open(out, "w").write(s)

# ---- leftover check ----
print("--- leftover scan ---")
for t in ["303 Coxwell", "Coxwell", "John Arockiaraj", "johneeraj", "647) 223",
          "Ward 19", "Beaches", "Woodbine", "Greenwood", "Cambridge", "Saanich",
          "Vancouver", "Edmonton", "Mississauga", "315.9"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done, fails: {fails}, wrote {out} ({len(s)} bytes)")
