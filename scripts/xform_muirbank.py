# -*- coding: utf-8 -*-
"""
xform_muirbank.py — build templates/report_muirbank.html for
21 Muirbank Boulevard, Scarborough, Toronto, ON  M1C 4T7  (Deep Bhatt).

Reads the master (templates/report_houselyft_master.html), swaps the
Coxwell / Ward-19 / 6+1 content for this property's VERIFIED Toronto
packet, injects the two real City-of-Toronto 2025 orthophoto aerials, and
injects the gated financing / grant rows.

Grounding packet (engine + official Open Data, verified live):
  City ...... Toronto  (adapter answered -> report-ready)
  Ward ...... 25 - Scarborough-Rouge Park  (City Wards Open Data PIP;
              NOT one of the nine sixplex wards -> 4 units, not 6)
  Zone ...... RD (x714) - Residential Detached; exc. 900.3.10(714);
              Toronto ZBL 569-2013
  As-of-right up to 4 units city-wide (By-law 474-2023) + one garden
  suite (Feb 2022). Parking: 0 required (Feb 2022). Lot area / year
  built not in packet -> confirm-phrase.

Homeowner goal (GHL custom fields EPzqHHy5AU2iIvHIAhKf /
oPfN9unZ4y37M1g1NwTq): "Secondary Suite" / "Potential for second unit".
Report is scoped to that goal while showing the full as-of-right range.

Run:  python3 scripts/xform_muirbank.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.normpath(os.path.join(HERE, "..", "templates"))
MASTER = os.path.join(TPL, "report_houselyft_master.html")
OUT = os.path.join(TPL, "report_muirbank.html")

s = open(MASTER, encoding="utf-8").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">21 Muirbank Boulevard<span>Scarborough, Toronto, ON</span></div>'))

# ---- property-details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">21 Muirbank Boulevard, Scarborough, Toronto, ON&nbsp;&nbsp;M1C 4T7</div>'))

# ---- imagery: real Toronto 2025 orthophoto aerials (lot + context) ----
IMG_OLD = ('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''')
IMG_NEW = ('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="padding:0;position:relative;overflow:hidden;">
      <img src="aerial_lot.jpg" alt="Aerial view of 21 Muirbank Boulevard, Scarborough, Toronto, ON" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:6.4pt;padding:2px 6px;">Aerial view — approx. 90 m across</div>
    </div>
    <div class="imgbox tall" style="padding:0;position:relative;overflow:hidden;">
      <img src="aerial_ctx.jpg" alt="Neighbourhood context around 21 Muirbank Boulevard, Scarborough" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:6.4pt;padding:2px 6px;">Neighbourhood context — approx. 300 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Contains information licensed under the Open Government Licence – Toronto. City of Toronto Orthophoto 2025 (8&nbsp;cm). Lot boundaries are approximate; confirm on the City of Toronto zoning map in Phase 2.</div>''')
R.append((IMG_OLD, IMG_NEW))

# ---- property KV table 1 (address / contact / goals) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>21 Muirbank Boulevard, Scarborough, Toronto, ON&nbsp;&nbsp;M1C 4T7</td></tr>
    <tr><td>Name</td><td>Deep Bhatt</td></tr>
    <tr><td>Phone Number</td><td>(226) 344-8392</td></tr>
    <tr><td>Email</td><td>dvbhatt13@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>Secondary Suite; potential for a second unit</td></tr>'''))

# ---- property KV table 2 (municipality / ward / bylaw / lot) ----
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
'''    <tr><td>Municipality</td><td>Toronto (Scarborough)</td></tr>
    <tr><td>Neighbourhood</td><td>Highland Creek</td></tr>
    <tr><td>Ward</td><td>Ward 25 — Scarborough-Rouge Park</td></tr>
    <tr><td>Community</td><td>Highland Creek, northeast Scarborough</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (as amended)</td></tr>
    <tr><td>Zoning Designation</td><td>RD — Residential Detached (exception 900.3.10(714))</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase (MPAC / survey)</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite / second unit (primary); full four-unit multiplex envelope shown as upside</td></tr>'''))

# ---- neighbourhood spotlight ----
R.append(('''    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>''',
'''    21 Muirbank Boulevard is in Highland Creek, an established detached-home community in northeast Scarborough (illustrative context, not a valuation):
    <ul>
      <li>Settled, tree-lined residential area within the Highland Creek / Port Union part of Ward 25 (Scarborough-Rouge Park)</li>
      <li>Close to the University of Toronto Scarborough (UTSC) and Centennial College — a steady source of rental demand</li>
      <li>Bordered by the Highland Creek ravine and the Colonel Danforth Park trail system</li>
      <li>Neighbourhood shops and services along Old Kingston Road and Morningside Avenue; TTC bus service connecting to the subway and to Scarborough Centre</li>
      <li>Quick access to Highway 401 for regional connectivity</li>
    </ul>'''))

# ---- zoning section (RD, Ward 25, four units city-wide) ----
R.append(('<tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>',
          '<tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. The lot is in Ward 25 (Scarborough-Rouge Park). Up to four dwelling units are permitted as-of-right on residential lots city-wide; the exact site standards (setbacks, coverage, height) are set by the RD zone and confirmed in Phase 2.</td></tr>'))
R.append(('<tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>',
          '<tr><td>Recent Changes</td><td>Toronto now permits up to <strong>four units as-of-right</strong> on residential lots city-wide (Multiplex By-law 474-2023, in force May 2023). A rear garden suite is separately permitted as-of-right (Garden Suite By-law, February 2022). No rezoning is required for either. Note: the six-unit as-of-right permission (By-law 654-2025) applies only in nine designated wards and does <strong>not</strong> apply to Ward 25.</td></tr>'))
R.append(('<tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>',
          '<tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — a residential lot in Toronto allows up to <strong>4 residential units</strong> as-of-right in a multiplex under By-law 474-2023, plus one rear garden suite, subject to technical review of site conditions.</td></tr>'))

# "what this means" list stays generic (townhouse / houseplex / suites) — unchanged.

# ---- time-sensitive section ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">Ontario Purpose-Built Rental HST Rebate<br><small>application window is time-limited</small></div><div class="dx">Ontario's 2026 Budget proposes a rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal rebate. Reported illustrative relief reaches up to $80,000 of the provincial portion per unit for units valued up to $1M, for agreements signed between April 1, 2026 and March 31, 2027. This measure is being legislated and generally applies at four or more purpose-built rental units — confirm final enactment, eligibility and figures in Phase 2 before relying on it.</div></div>
    <div class="d"><div class="dt">Development-Charge Relief for Additional Units</div><div class="dx">Under Ontario's Bill 23, additional residential units created on a serviced lot are exempt from municipal development charges — a meaningful per-unit saving on a secondary suite or a small multiplex. The exact number of exempt units and the per-unit and per-project figures for this property are confirmed with the City of Toronto in Phase 2; we do not quote a fixed dollar amount here.</div></div>''')
    )

# ---- rezoning section ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A secondary suite, and up to a four-unit multiplex with a rear garden suite, are permitted as-of-right under Toronto By-law 474-2023 and the Garden Suite By-law — no rezoning required.</div>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023</td><td class="n">A new site-specific by-law</td></tr>'))
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Toronto's Multiplex By-law (474-2023) permits up to four dwelling units as-of-right on a residential lot city-wide, with no additional parking required.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>'''))
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 21 Muirbank Boulevard</div>'))
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 21 Muirbank Boulevard already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the lot’s exact area and frontage.</b><br><span class="sub">The buildable envelope and the number of units that physically fit are set by the confirmed lot dimensions (MPAC / survey), finalized in Phase 2.</span></div>'))

# ---- development options ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Add One Suite (2 units total) — matches your stated goal</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add a single self-contained secondary suite — for example an interior basement apartment, or a detached garden suite in the rear yard — for ongoing rental income while you keep the home. Two units total. This matches your stated goal of a secondary suite / second unit. Permitted as-of-right under Toronto By-law 474-2023 (and the Garden Suite By-law for a rear suite); no rezoning and no additional parking required. The additional unit is exempt from municipal development charges under Ontario's Bill 23. Suite size and siting are set by the RD zone standards and confirmed in Phase 2. This is the lowest-cost entry point into rental income.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Three or Four Units (multiplex)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Convert or build to three or four self-contained units within the home — the city-wide as-of-right maximum for a multiplex under By-law 474-2023. No rezoning and no additional parking are required. This is a natural step up from a single secondary suite when the goal shifts toward maximizing rental income, and it is the threshold at which the purpose-built-rental HST rebates (federal, and the announced Ontario rebate) begin to open up. Unit mix and the buildable envelope on this lot are confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Four Units + Rear Garden Suite (full as-of-right envelope)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">The fullest as-of-right position combines a four-unit multiplex in the main building with one rear garden suite — up to five independent units on the lot, no rezoning required. A garden suite on a non-laneway lot is permitted as-of-right under Toronto's Garden Suite By-law (February 2022). Whether the full four-plus-one envelope physically fits is governed by the confirmed lot area, frontage and the RD built-form standards, finalized in Phase 2. No parking spaces are required for the multiplex units.</div>'''))

# ---- development goal summary (section 5) ----
R.append((
'''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Secondary Suite — with room to scale</div>
  <p>21 Muirbank Boulevard is a residential lot in Toronto where up to <strong>four units are permitted as-of-right</strong> under By-law 474-2023, plus a rear garden suite — no rezoning required. Your stated goal is a secondary suite / second unit, which is comfortably within this envelope. <strong>Adding one suite is the recommended starting point; the same lot supports scaling to a three- or four-unit multiplex later if your goals change.</strong></p>'''))

# ---- summary (section 8) current-zoning-review ----
R.append((
'''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>21 Muirbank Boulevard confirms a strong development option. This is a residential lot in Toronto (Ward 25 — Scarborough-Rouge Park) where up to <strong>four dwelling units are permitted as-of-right</strong> under the city-wide Multiplex By-law (474-2023), plus a rear garden suite — no rezoning, no additional parking, and no public hearing required.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> Toronto permits up to four units on a residential lot city-wide with no rezoning, no public hearing and no Council approval — you build under existing zoning. Your secondary-suite goal sits well inside this envelope, with clear room to scale. The exact lot-specific standards are confirmed in Phase 2.</li>
  </ul>'''))

# ---- gated financing rows (section 6): CMHC unlocks above 4 units ----
FIN_ROWS = (
'''<tr><td>CMHC MLI Select &amp; Apartment Construction Loan Program (ACLP)</td><td>Available at a larger scale, <strong>from five rental units</strong> — beyond Toronto's four-unit as-of-right multiplex envelope, so a five-plus-unit project would move into a rezoning / larger-build path. MLI Select offers preferred multi-unit mortgage-loan insurance (minimum five units); the ACLP offers low-cost construction financing (minimum five self-contained units and a minimum $1,000,000 loan). Confirm current CMHC intake before relying on either. Shown here so you can see what scaling up unlocks.</td></tr>''')
s2 = re.sub(r'<!-- GATED_FINANCING_ROWS.*?-->', lambda m: FIN_ROWS, s, count=1, flags=re.S)
if s2 == s:
    print("[FAIL] GATED_FINANCING_ROWS marker not found")
s = s2

# ---- gated grant rows (section 7): scoped to goal, thresholds shown ----
GRANT_ROWS = (
'''<tr><td>Provincial</td><td>Development-Charge Exemption for Additional Units (Bill 23)</td><td>Under Ontario's Bill 23, additional residential units created on a serviced lot are exempt from municipal development charges, parkland dedication and cash-in-lieu — a meaningful per-unit saving that applies directly to your secondary-suite / second-unit goal. The exact number of exempt units and the figures for this property are confirmed with the City of Toronto in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>At <strong>four or more</strong> self-contained rental units held as long-term rental (90%+), a full 100% rebate of the federal GST (5%) applies, with no cap. Construction must begin after Sept 13, 2023 and before 2031, and complete before 2036. Opens up if you scale to the four-unit option; eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>Ontario PBRH / Rental HST Rebate (2026 Budget — announced)</td><td>The 2026 Ontario Budget proposes rebating the provincial (8%) portion of HST on qualifying new purpose-built rental, mirroring the federal rebate (a reported enhanced rebate recovers up to $80,000 of the provincial portion per unit for construction beginning April 1, 2026 – March 31, 2027). Generally applies at four or more rental units. This measure is being legislated — confirm final enactment and eligibility before relying on it.</td></tr>''')
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

# ---- leftover check: nothing Coxwell / Ward-19 / sixplex may survive ----
leftovers = ["Coxwell", "Arockiaraj", "John", "Ward 19", "Beaches", "654-2025",
             "6+1", "6-Unit", "6 units", "six units", "Six-Unit", "sixplex",
             "nine wards", "Bill 185", "M4L 3B5", "647) 223", "johneeraj",
             "20 ft", "170 ft", "315.9", "heated floors", "Greenwood",
             "Woodbine", "Upper Beaches"]
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done. fails={fails}, bytes={len(s)}, out={OUT}")
