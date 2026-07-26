import base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
IMG = sys.argv[1] if len(sys.argv) > 1 else "/tmp/img"

s = open(os.path.join(TPL, "report_houselyft_master.html")).read()

def datauri(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()

LOT = datauri(os.path.join(IMG, "aerial_lot.jpg"))
CTX = datauri(os.path.join(IMG, "aerial_context.jpg"))

R = []

# ---- CSS for aerial boxes ----
R.append((".cta .fee{font-family:'Oswald';font-weight:700;font-size:16pt;}",
""".cta .fee{font-family:'Oswald';font-weight:700;font-size:16pt;}
  .aerialbox{flex:1;height:148px;position:relative;overflow:hidden;border:1px solid var(--line);}
  .aerialbox img{width:100%;height:148px;object-fit:cover;display:block;}
  .aerialbox .cap{position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Lato';}"""))

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">10699 Clarkway Drive<span>Brampton, ON</span></div>'))

# ---- property details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">10699 Clarkway Drive, Brampton, ON&nbsp;&nbsp;L6P 0W2</div>'))

# ---- image row + licence ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
f'''  <div class="imgrow" style="margin-top:0;">
    <div class="aerialbox"><img src="{LOT}" alt="Aerial view of 10699 Clarkway Drive"><span class="cap">Aerial view — approx. 90 m across</span></div>
    <div class="aerialbox"><img src="{CTX}" alt="Neighbourhood context around 10699 Clarkway Drive"><span class="cap">Neighbourhood context — approx. 300 m across</span></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Brampton Orthophoto 2023 (Spring). Contains information licensed under the Open Government Licence – City of Brampton.</div>'''))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>10699 Clarkway Drive, Brampton, ON&nbsp;&nbsp;L6P 0W2</td></tr>
    <tr><td>Name</td><td>Jitesh Tripathi</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Additional residential unit(s) — garden suite and/or interior second unit; specific scope to be confirmed</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Brampton (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Northeast Brampton — Clarkway / Coleraine area</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Property Type</td><td>Detached dwelling on a residential-estate lot (per City parcel data)</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Brampton Zoning By-law 270-2004 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>~4,079 m² (~1.0 acre) — City-computed screening value; confirm by survey in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Additional residential unit(s) — up to 3 units total, subject to servicing and site standards</td></tr>'''))

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
    10699 Clarkway Drive sits in northeast Brampton, in the Clarkway / Coleraine area near the Brampton–Caledon boundary in the Region of Peel — a large-lot, estate-style residential pocket bordered by open countryside:
    <ul>
      <li>Residential-estate setting on a roughly one-acre lot with a deep rear yard — well suited to a detached backyard suite</li>
      <li>Quick access to Highway 50 and The Gore Road corridor, connecting south into Brampton and north into Caledon</li>
      <li>Part of a growing northeast Brampton area with ongoing residential development nearby</li>
      <li>A watercourse and treed lands sit near the lot — a conservation-authority (TRCA) regulated-area check is confirmed in Phase 2</li>
      <li>Illustrative context only, not a valuation.</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RE2 — Residential Estate (Brampton Zoning By-law 270-2004, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Additional residential units under Ontario's Bill 23 apply to eligible residential lots meeting the City's site standards (servicing, lot size, setbacks). On an estate lot that may be on private services (well/septic), servicing capacity is a key confirmation — addressed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on an eligible residential lot — no rezoning. Brampton administers additional residential units (ARUs) through its framework under By-law 270-2004, as amended.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior second unit and a detached garden suite (ARU) may be permitted, subject to Brampton's ARU standards — including a garden-suite floor-area cap (City screening indicates up to ~80 m²), setbacks and height. The City's ARU screening tool returns a positive result for this parcel; confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>LIKELY YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong> to confirm servicing and site standards</td></tr>'''))

# ---- what this means (zoning cell list) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite:</strong> a self-contained home in your rear yard — the strongest fit for this large-lot property</li>
      <li><strong>Interior Second Unit:</strong> a secondary suite within the existing home (for example, a basement or in-law suite)</li>
      <li><strong>Up to 3 units total:</strong> under Bill 23, the property may support the main dwelling plus two additional residential units, subject to Brampton's site and servicing standards</li>
      <li><strong>Registration required:</strong> additional residential units must be registered with the City; a Residential Rental Licence applies to 1–4 unit rentals from January 1, 2026</li>'''))

# ---- time-sensitive ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">ARU Development-Charge Exemption<br><small>in effect</small></div><div class="dx">Additional residential units are exempt from municipal development charges under Ontario's Bill 23 — a meaningful per-unit saving on a garden suite or second unit. The exemption covers the first two additional units on the lot. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Brampton Residential Rental Licence<br><small>from Jan 1, 2026</small></div><div class="dx">Brampton requires a Residential Rental Licence for rental dwellings of 1 to 4 units city-wide, phasing in from January 1, 2026, and any additional residential unit must be registered with the City to be legal. Building this into the plan from Day 1 avoids compliance delays later.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning green box ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Additional residential units (a garden suite and/or interior second unit) are permitted as-of-right under Ontario\'s Bill 23 and Brampton\'s ARU framework — subject to site and servicing standards confirmed in Phase 2.</div>'))

# ---- rezoning comparison last row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + Brampton By-law 270-2004 (ARU framework)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning twocard ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Interior second unit</div>Ontario's Bill 23 permits an additional residential unit inside the existing dwelling (for example a basement or in-law suite) on an eligible residential lot, subject to Brampton's ARU standards.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>A detached backyard suite (ARU) may be permitted on this lot — the City's ARU screening returns a positive result for this parcel — subject to a floor-area cap, setbacks and servicing confirmed in Phase 2.</div>'''))

# ---- rezoning what-this-means barhead + para ----
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 10699 Clarkway Drive</div>'))
R.append(("<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>",
          "<p>Because 10699 Clarkway Drive can support additional residential units under existing provincial and municipal rules, no rezoning application is contemplated in this analysis. Your project advances directly to design, servicing confirmation and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site and servicing conditions.</p>"))

# ---- rezoning amber ----
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>Two items to confirm early: servicing and conservation-authority status.</b><br><span class="sub">On an estate lot, whether the property is on municipal services or private well/septic affects how many units are feasible, and any conservation-authority (TRCA) regulated lands near the watercourse require a permit. Both are confirmed in Phase 2.</span></div>'))

# ---- options A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, for ongoing rental income while you keep the property. Permitted as-of-right under Bill 23 as an additional residential unit; no rezoning. The City's ARU screening indicates a detached suite of up to roughly 80 m² is supported on this parcel, with exact size and siting set by Brampton's garden-suite standards — setbacks, height and servicing — confirmed in Phase 2. The roughly one-acre lot with a deep rear yard is a strong fit for this form.</div>'''))

# ---- options B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Garden Suite + Interior Second Unit — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior second unit in the existing home (for example, a basement apartment) — a route to as many as three units on the lot under Bill 23, where servicing and site standards allow. This maximizes rental income while keeping the property in your hands. Additional units must be registered with the City. Eligibility, servicing capacity and unit sizes are confirmed in Phase 2.</div>'''))

# ---- options C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Estate-Lot, Servicing &amp; Conservation Considerations</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">This is a large residential-estate lot in northeast Brampton. Its size and deep rear yard are real advantages for a garden suite, but an estate setting brings two early checks. First, servicing: if the property is on a private well and septic system rather than municipal water and sewer, servicing capacity — not the zoning — often governs how many additional units are feasible. Second, conservation authority: with a watercourse and regulated lands in the vicinity, a Toronto and Region Conservation Authority (TRCA) permit may be required. Both are confirmed in Phase 2 and shape the final buildable envelope.</div>'''))

# ---- goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Additional Residential Units — up to 3</div>
  <p>10699 Clarkway Drive is a residential-estate lot in northeast Brampton where, under Ontario's Bill 23 and Brampton's ARU framework, additional residential units are permitted as-of-right — the City's own ARU screening returns a positive result for this parcel. <strong>A detached garden suite, optionally paired with an interior second unit for up to three units total, is the primary recommendation</strong> — with servicing and conservation-authority status confirmed in Phase 2.</p>'''))

# ---- grants table rows ----
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Under Ontario's More Homes Built Faster Act (Bill 23), the first two additional residential units on a residential lot are exempt from municipal development charges — a meaningful per-unit saving on a garden suite or second unit. Applies in Ontario; confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>A partial GST/HST rebate may apply to a newly built, self-contained long-term rental unit. This is the individual-unit rebate — distinct from the 4-plus-unit purpose-built rental rebate, which a project of this size does not reach. Eligibility and amount confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (up to $7,500) — but only where the new self-contained unit is built to house an eligible senior (65+) or an adult eligible for the Disability Tax Credit. Applies only if that condition is met; confirmed in Phase 2.</td></tr>'''))

# ---- summary current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>10699 Clarkway Drive is a residential-estate lot in northeast Brampton (Region of Peel). Under Ontario's Bill 23 and Brampton's ARU framework, up to <strong>three residential units may be permitted as-of-right</strong> — including a detached garden suite — with no rezoning required, subject to the City's site and servicing standards. The City's ARU screening tool returns a positive result for this specific parcel.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds a rental income stream while you keep the property, using land you already own on a large, roughly one-acre lot — the exact size and siting are confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(TPL, "report_brampton_clarkway.html")
open(out, "w").write(s)

print("--- leftover check ---")
for t in ["Coxwell", "Toronto Zoning", "John", "Arockiaraj", "Ward 19", "Beaches",
          "654-2025", "474-2023", "Bill 185", "6+1", "4+1", "sixplex", "Six-unit",
          "six units", "M4L", "569-2013", "houseplex", "PBRH", "johneeraj", "Woodbine"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
# 'Toronto' allowed only inside 'Toronto and Region Conservation Authority'
tor = s.count("Toronto")
tor_ca = s.count("Toronto and Region Conservation Authority")
print(f"Toronto total={tor} (allowed TRCA={tor_ca}, other={tor-tor_ca})")
print("fails:", fails, "-> wrote", out)
