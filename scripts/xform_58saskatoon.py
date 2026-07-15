import os, shutil

TPL = os.path.join(os.path.dirname(__file__), "..", "templates")
SRC = os.path.join(TPL, "report_houselyft_master.html")
OUT = os.path.join(TPL, "report_58saskatoon.html")
shutil.copyfile(SRC, OUT)
s = open(OUT, encoding="utf-8").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">58 Saskatoon Drive<span>Etobicoke (Toronto), ON</span></div>'))

# ---- property details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">58 Saskatoon Drive, Etobicoke, Toronto, ON&nbsp;&nbsp;M9P 2G2</div>'))

# ---- image row: inject real aerials ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="position:relative;padding:0;overflow:hidden;">
      <img src="aerial_58saskatoon_lot.jpg" style="width:100%;height:100%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;font-family:'Lato',Arial,sans-serif;padding:3px 7px;text-align:left;">Aerial view — approx. 90 m across</div>
    </div>
    <div class="imgbox tall" style="position:relative;padding:0;overflow:hidden;">
      <img src="aerial_58saskatoon_ctx.jpg" style="width:100%;height:100%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;font-family:'Lato',Arial,sans-serif;padding:3px 7px;text-align:left;">Neighbourhood context — approx. 220 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>58 Saskatoon Drive, Etobicoke, Toronto, ON&nbsp;&nbsp;M9P 2G2</td></tr>
    <tr><td>Name</td><td>H K</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — 4-plex + ADU (per intake)</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Toronto (Etobicoke)</td></tr>
    <tr><td>Neighbourhood</td><td>Kingsview Village–The Westway</td></tr>
    <tr><td>Ward</td><td>Ward 2 — Etobicoke Centre</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Zoning</td><td>RD (f13.5; a510; d0.45) — Residential Detached</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>4-plex + garden suite (4+1); maximize as-of-right units</td></tr>'''))

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
    58 Saskatoon Drive is located in Kingsview Village–The Westway, an established residential neighbourhood in central Etobicoke:
    <ul>
      <li>Quiet, low-rise residential streets of the kind that rent well and hold value</li>
      <li>Close to the Humber River valley and its trail system to the east</li>
      <li>Well connected by road to Highways 401 and 427 and the Pearson Airport employment lands</li>
      <li>TTC bus service along nearby arterials such as The Westway, Kipling Avenue, and Royal York Road</li>
      <li>Illustrative context only, not a valuation — local amenities and transit confirmed in Phase 2</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD (f13.5; a510; d0.45) — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. The RD zone permits detached house-form buildings; a multiplex of up to four units is permitted as-of-right in residential zones city-wide, subject to the built-form standards of the zone.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide under Toronto's multiplex by-law (By-law 474-2023). Ward 2 (Etobicoke Centre) is not among the nine wards where a sixth unit is permitted as-of-right, so this analysis is built on the 4-unit envelope. No rezoning is required for a fourplex.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone allows a detached multiplex of up to <strong>4 residential units</strong> as-of-right, plus a rear garden suite, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- rezoning: co-green ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 4+1 configuration is permitted as-of-right — the four-unit multiplex under Toronto\'s city-wide multiplex by-law (474-2023) and the rear garden suite under the Garden Suite By-law (February 2022).</div>'))

# ---- rezoning: comparison table governing row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">The city-wide multiplex by-law (474-2023)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: also-permitted twocard ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Toronto's city-wide multiplex by-law (474-2023) permits up to four units in a residential zone without rezoning — the basis for this analysis.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>'''))

# ---- rezoning: "what this means" barhead + para ----
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 58 Saskatoon Drive</div>'))
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 58 Saskatoon Drive already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

# ---- rezoning: co-amber ----
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the lot\'s exact area, frontage, and depth.</b><br><span class="sub">The buildable envelope for the multiplex and any garden suite depends on the confirmed lot dimensions (MPAC / survey) and the RD setback and coverage standards — finalized in Phase 2.</span></div>'))

# ---- development options ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Four-Unit Multiplex + Garden Suite (4+1) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached four-unit multiplex on the main building, plus one garden suite in the rear yard — five independent units in total. Both are permitted as-of-right in the RD zone: the multiplex under Toronto's city-wide multiplex by-law (474-2023) and the rear suite under the Garden Suite By-law (February 2022). No rezoning is required. The RD zone's built-form standards — height, setbacks, coverage — together with the lot's confirmed area and frontage set the final envelope, finalized in Phase 2. No parking minimums apply to multiplexes in Toronto. Development charges are fully waived for multiplexes up to six units (Bill 185), which covers this configuration.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Four-Unit Multiplex</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A detached four-unit multiplex on the main building, without a rear suite — four independent units, fully as-of-right under Toronto's city-wide multiplex by-law (474-2023). A simpler build that still captures the multiplex development-charge waiver and the no-parking-minimum advantage, and leaves the option to add a garden suite in a later phase. Unit mix and sizes are set within the RD built-form envelope and confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Garden Suite as a First Phase</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A single detached garden suite in the rear yard as a standalone first phase — one additional rental unit, permitted as-of-right under Toronto's Garden Suite By-law (February 2022) on a non-laneway lot. A lower-cost entry point that adds income while you keep the existing home, and can precede the full multiplex build. The suite's size and siting depend on the rear-yard dimensions, setbacks, and servicing, confirmed in Phase 2.</div>'''))

# ---- development goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">4+1 Configuration</div>
  <p>58 Saskatoon Drive is in Ward 2 (Etobicoke Centre), where up to four units are permitted as-of-right in a residential zone under Toronto's city-wide multiplex by-law, and a rear garden suite is permitted under the Garden Suite By-law. <strong>The 4+1 configuration — a four-unit multiplex plus one garden suite — is the clear primary recommendation.</strong></p>'''))

# ---- time-sensitive: DC waiver envelope phrasing ----
R.append(('This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.',
          'This benefit is locked in as long as your project stays within the six-unit multiplex envelope the waiver covers.'))

# ---- summary ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>58 Saskatoon Drive confirms a strong development option. This RD-zoned lot in Ward 2 (Etobicoke Centre) supports up to <strong>four residential units as-of-right in a detached multiplex</strong>, plus a rear garden suite — five income units in total, with no rezoning, no public hearing, and no Council approval required.</p>
  <ul>
    <li><strong>The As-of-Right Multiplex Advantage:</strong> Toronto's city-wide multiplex by-law lets this lot add up to four units in the main building, and the Garden Suite By-law adds a rear suite — all under existing zoning, avoiding the cost and uncertainty of a rezoning.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w", encoding="utf-8").write(s)

print("\n--- leftover check ---")
for t in ["303 Coxwell", "Coxwell", "John Arockiaraj", "Arockiaraj", "johneeraj",
          "Ward 19", "654-2025", "Beaches", "6+1", "6-unit houseplex", "nine wards",
          "Woodbine", "Greenwood", "converted garage", "750 sq ft"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("\nfails:", fails, "| out:", OUT)
