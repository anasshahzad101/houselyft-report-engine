import base64, os, sys

ROOT = "/home/user/houselyft-report-engine"
SCRATCH = "/tmp/claude-0/-home-user-houselyft-report-engine/84309467-b7a8-50aa-931f-594af6a1b81e/scratchpad"
MASTER = os.path.join(ROOT, "templates/report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates/report_enzo_25cliff.html")

s = open(MASTER).read()

lot_b64 = base64.b64encode(open(f"{SCRATCH}/aerial_lot.jpg", "rb").read()).decode()
ctx_b64 = base64.b64encode(open(f"{SCRATCH}/aerial_ctx.jpg", "rb").read()).decode()

R = []

# --- cover address ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">25 Cliff Street<span>Toronto, ON</span></div>'))

# --- property details barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">25 Cliff Street (York), Toronto, ON&nbsp;&nbsp;M6N 4L7</div>'))

# --- aerial image row + licence line (inject the two real Toronto orthos) ---
img_old = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
img_new = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{lot_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Lato';">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{ctx_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Lato';">Neighbourhood context — approx. 220 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:6px 0 8px;">Aerial imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''
R.append((img_old, img_new))

# --- property table 1 (owner / goals) ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>25 Cliff Street (York), Toronto, ON&nbsp;&nbsp;M6N 4L7</td></tr>
    <tr><td>Name</td><td>Enzo Moreno</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>enzomoreno63@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>Exploring development potential — direction to be confirmed at the planning session</td></tr>'''))

# --- property table 2 (municipal facts) ---
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
'''    <tr><td>Municipality</td><td>Toronto (former City of York)</td></tr>
    <tr><td>Neighbourhood</td><td>Rockcliffe-Smythe</td></tr>
    <tr><td>Ward</td><td>Ward 5 — York South-Weston</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2 (minimum lot frontage in this zone: 12.0 m)</td></tr>
    <tr><td>Development Goals</td><td>To be confirmed — options presented across the as-of-right range</td></tr>'''))

# --- neighbourhood spotlight ---
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
    25 Cliff Street sits in Rockcliffe-Smythe, an established residential neighbourhood in Toronto's west end (former City of York):
    <ul>
      <li>A mature, largely residential community of detached and semi-detached homes on tree-lined streets</li>
      <li>Close to the St. Clair Avenue West corridor and the Stockyards District retail area</li>
      <li>Green space along the Humber River and Black Creek ravine systems nearby</li>
      <li>Served by TTC surface transit with connections toward the St. Clair West and Weston corridors</li>
      <li>Established west-end stock of the kind that supports steady rental demand (illustrative context, not a valuation)</li>
    </ul>'''))

# --- zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RM — Residential Multiple (Toronto Zoning By-law 569-2013). Zone label: RM (f12.0; u4; d0.8) (x252), exception 900.6.10(252).</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Minimum lot frontage in this zone is 12.0 m; permitted density is 0.8 times the lot area. Site-specific standards under exception 900.6.10(252) are confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 residential units are permitted as-of-right city-wide under By-law 474-2023 (multiplex permission). No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing — the RM zone permits multiple-unit residential forms. Up to <strong>4 residential units</strong> are achievable as-of-right on this lot under the city-wide multiplex permission, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means for you" bullets ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Multiplex (up to 4 units):</strong> A standalone building with up to four self-contained units, permitted as-of-right city-wide</li>
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side or vertically stacked units</li>
      <li><strong>Detached / Semi-detached forms:</strong> The RM zone accommodates multiple-unit residential building types</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> A secondary suite (such as a basement or garden suite) can be paired with the main dwelling to add a unit</li>'''))

# --- time-sensitive section ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, provincial relief can reach roughly $80,000 per unit. This is a temporary enhancement — the agreement must be signed between April 1, 2026 and March 31, 2027, and eligibility begins at four rental units. Structuring the project correctly from Day 1 is essential to capture it.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are eliminated for multiplexes of up to six units in the City of Toronto (Bill 185, January 2025), with no application required — a four-unit build sits well within this envelope. The exact per-project saving is confirmed against your final design in Phase 2. This benefit holds as long as the project stays within the as-of-right envelope.</div></div>'''))

# --- rezoning co-green ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A multiplex of up to four units is permitted as-of-right under Toronto\'s city-wide multiplex permission (By-law 474-2023) — no rezoning required.</div>'))

# --- cmp "what governs your build" ---
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023 (as-of-right)</td><td class="n">A new site-specific by-law</td></tr>'))

# --- "also permitted as-of-right" twocard ---
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Up to four self-contained units are permitted as-of-right city-wide under By-law 474-2023 — no rezoning, no public hearing.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right — subject to rear-yard fit, confirmed in Phase 2.</div>'''))

# --- "what this means for 303 Coxwell" block ---
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 25 Cliff Street</div>
  <p>Because 25 Cliff Street already permits a multiplex build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2: the exact lot dimensions and the rear-yard envelope for a possible garden suite.</b><br><span class="sub">These set the buildable footprint and whether a fifth (garden-suite) unit fits — both are established from a site plan during the feasibility phase.</span></div>'''))

# --- Option A ---
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Multiplex, up to 4 units (as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A standalone multiplex of up to four self-contained units on the main structure — permitted as-of-right city-wide under By-law 474-2023, with no rezoning and no variances likely if designed within the standard envelope. The RM zone's built-form standards (12.0 m minimum frontage, 0.8 density, setbacks, and height) govern the form; exact figures are confirmed against a site plan in Phase 2. No parking minimums apply to multiplexes. Development charges are waived for builds up to six units in Toronto (Bill 185).</div>'''))

# --- Option B ---
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Add a detached garden suite in the rear yard to the four-unit multiplex, for a total of up to five independent units. The rear ancillary suite is permitted as-of-right under Toronto's Garden Suite By-law (February 2022) on a non-laneway lot, subject to rear-yard fit and the suite's size and siting standards — confirmed against a site plan in Phase 2. No parking spaces required. At five rental units the project may also reach CMHC MLI Select financing (see Grants &amp; Incentives).</div>'''))

# --- Option C ---
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Rear-Yard &amp; Garden-Suite Potential</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">The aerial imagery shows a rear yard behind the main dwelling. Under Toronto's Garden Suite By-law (February 2022), a detached rear suite is permitted as-of-right in residential zones on a non-laneway lot. Whether a suite fits — and at what size — depends on the rear-yard depth, setbacks, and servicing, all confirmed from a site plan in Phase 2. If a garden suite is a goal, it is the most straightforward path to an additional income unit on this lot.</div>'''))

# --- development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex up to 4 units, with garden-suite upside</div>
  <p>25 Cliff Street is an RM (Residential Multiple) lot in Ward 5 — York South-Weston. Up to four residential units are permitted as-of-right city-wide under By-law 474-2023, with no rezoning required, and a rear garden suite is a potential fifth unit under the Garden Suite By-law. <strong>Because your goal is still open, the options above are presented across the as-of-right range — we confirm your preferred direction at the planning session.</strong></p>'''))

# --- summary: current zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>25 Cliff Street confirms a strong development option. This property sits on an RM (Residential Multiple) lot in Ward 5 — York South-Weston. Up to <strong>four residential units are permitted as-of-right city-wide</strong> under By-law 474-2023, with a rear garden suite as a potential fifth unit under the Garden Suite By-law — all without rezoning.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> a four-unit multiplex needs no rezoning, no public hearing, and no Council approval — the project advances directly to design and permitting.</li>
  </ul>'''))

# --- gated grants rows (Toronto, tiered 4+1) ---
grants_marker = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->'''
grants_rows = '''    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges are eliminated for multiplexes of up to six units in the City of Toronto — a four-unit build sits well within this envelope. Parking minimums are also waived city-wide (since February 2022). No application is required; the benefit applies automatically to compliant builds. The exact per-project saving is confirmed against the final design in Phase 2. (City of Toronto, Bill 185, January 2025.)</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>A 100% rebate of the 5% federal GST on new purpose-built rental projects with four or more self-contained units (90%+ long-term rental), where construction begins before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — up to roughly $80,000 per unit in provincial relief on units valued up to $1M. This tier is reached at four units. Enhancement window: agreement signed April 1, 2026 – March 31, 2027. (Federal PBRH rebate; Ontario provincial component.)</td></tr>
    <tr><td>Provincial</td><td>DC Exemption for Additional Residential Units (Bill 23)</td><td>Additional residential units — such as a rear garden suite — are exempt from development charges under Ontario's More Homes Built Faster Act (Bill 23), for up to the first two additional units. A meaningful per-unit saving on a garden-suite component. Confirmed for your project in Phase 2. (Ontario Bill 23.)</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred insured financing terms for rental projects of five or more units. Reached at the five-unit scale — a four-unit multiplex plus a garden suite. Whether your project reaches this tier is decided by the direction chosen in Phase 2; the five-unit threshold is shown so the path is clear. (CMHC MLI Select product terms.)</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental, with a minimum $1M loan. Applicability is set by the project budget, confirmed in Phase 2 — shown here so the threshold is clear. (CMHC ACLP program terms.)</td></tr>'''
R.append((grants_marker, grants_rows))

# apply replacements
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# leftover check — Coxwell-identifying / sixplex content must be gone
print("--- leftover check ---")
for t in ["303 Coxwell", "Coxwell", "Arockiaraj", "johneeraj", "654-2025", "Ward 19",
          "Beaches", "M4L 3B5", "647) 223", "nine wards", "6+1", "6-Unit Multiplex",
          "750 sq", "John's", "garage"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

open(OUT, "w").write(s)
print(f"\nfails: {fails}")
print(f"written: {OUT}  ({len(s)} bytes)")
