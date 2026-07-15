import base64, os, sys

TPL = "templates"
SCR = "/tmp/claude-0/-home-user-houselyft-report-engine/084a7f9c-c557-5106-b391-ba9d78118be8/scratchpad"

s = open(os.path.join(TPL, "report_houselyft_master.html")).read()
R = []

# ---------------- COVER ----------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">441 Rimilton Avenue<span>Etobicoke, Toronto, ON</span></div>'))

# ---------------- PROPERTY DETAILS barhead ----------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">441 Rimilton Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M8W 2G7</div>'))

# ---------------- IMAGE ROW + licence (real aerials injected) ----------------
lot_b64 = base64.b64encode(open(os.path.join(SCR, "aerial_lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCR, "aerial_ctx.jpg"), "rb").read()).decode()
img_old = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
img_new = ('''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Neighbourhood context — approx. 220 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>''' % (lot_b64, ctx_b64))
R.append((img_old, img_new))

# ---------------- PROPERTY TABLE 1 ----------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>441 Rimilton Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M8W 2G7</td></tr>
    <tr><td>Name</td><td>Michael Bukrinsky</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>4-unit multiplex plus a rear garden suite (4+1); siting mindful of a mature City tree on the lot</td></tr>'''))

# ---------------- PROPERTY TABLE 2 ----------------
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
'''    <tr><td>Municipality</td><td>Toronto (former Etobicoke)</td></tr>
    <tr><td>Neighbourhood</td><td>Alderwood</td></tr>
    <tr><td>Ward</td><td>Ward 3 — Etobicoke-Lakeshore</td></tr>
    <tr><td>Community Council</td><td>Etobicoke York Community Council</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>4+1 Multiplex (4 units + rear garden suite)</td></tr>'''))

# ---------------- NEIGHBOURHOOD SPOTLIGHT ----------------
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
    441 Rimilton Avenue is in Alderwood — an established, quiet residential neighbourhood in south Etobicoke near Lake Ontario, framed by the Etobicoke Creek and the Long Branch area:
    <ul>
      <li>Close to Marie Curtis Park, the Etobicoke Creek trail, and the Lake Ontario waterfront</li>
      <li>Long Branch GO station and the Long Branch streetcar (501) offer transit to downtown; TTC bus routes serve the area</li>
      <li>Quick access to the QEW and Highway 427 for regional connectivity</li>
      <li>Alderwood Pool, Library, and community centre serve the neighbourhood; local schools nearby</li>
      <li>Mature tree-lined streets — the kind of established stock that holds value and rents steadily (illustrative context, not a valuation)</li>
    </ul>'''))

# ---------------- ZONING TABLE ----------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RM (u4) (x18) — Residential Multiple, exception 900.6.10(18) (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. The property is in Ward 3 (Etobicoke-Lakeshore), Etobicoke York Community Council district. Up to 4 residential units are permitted as-of-right on residential lots city-wide, subject to the built-form standards of the applicable zone.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023). A rear garden suite is permitted as-of-right on a non-laneway residential lot (Garden Suite By-law, 2022). No rezoning required for the 4+1 configuration.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — this is an RM (Residential Multiple) zone. Up to <strong>4 residential units</strong> are confirmed as-of-right city-wide; the RM zone's site-specific multiple-dwelling permissions and exception 900.6.10(18) are confirmed in Phase 2 and may allow additional density. Subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---------------- TIME-SENSITIVE (fix DC-waiver envelope wording) ----------------
R.append(('This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.',
          'This benefit applies to multiplex projects of up to 6 units.'))

# ---------------- REZONING §3 ----------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 4+1 configuration is permitted as-of-right under Toronto By-law 474-2023 (four units city-wide) and the Garden Suite By-law.</div>'))

R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023 + Garden Suite By-law</td><td class="n">A new site-specific by-law</td></tr>'))

R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Four-unit multiplex</div>Up to four residential units are permitted as-of-right on residential lots across Toronto under By-law 474-2023 — no rezoning, no public hearing, no Council approval required.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>'''))

R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>\n  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<div class="barhead" style="text-align:left;">What this means for 441 Rimilton Avenue</div>\n  <p>Because 441 Rimilton Avenue already permits the recommended 4+1 build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the mature City tree on or near the lot.</b><br><span class="sub">Its protected status under Toronto\'s tree-protection by-laws, and any required tree-protection zone, must be confirmed before the garden-suite or multiplex footprint is sited. This is a design input, not a barrier — it is resolved during the feasibility phase.</span></div>'))

# ---------------- DEVELOPMENT OPTIONS §4 ----------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1) — Primary Recommendation</div>'))

R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A 4-unit multiplex in the main structure, plus one garden suite in the rear yard. Total: 5 independent units — matching your stated goal. The four main units are permitted as-of-right under By-law 474-2023, and the rear garden suite under Toronto's Garden Suite By-law (2022); no rezoning is required. Lot dimensions and the exact buildable envelope are confirmed in Phase 2. The garden suite's siting will be planned around the mature City tree on the lot and any required tree-protection zone. RM (Residential Multiple) built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for multiplex projects up to 6 units (Bill 185).</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Phased Start: Rear Garden Suite First</div>'))

R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">If you prefer to phase the investment, the rear garden suite can be built first as a standalone income unit — permitted as-of-right under the Garden Suite By-law (2022) on a non-laneway residential lot — while the four-unit multiplex is planned for a later stage. This spreads capital and construction over time while still using land you already own. The suite's size and siting are set by Toronto's garden-suite standards (setbacks, height, floor-area cap) and by the mature-tree considerations on the lot, confirmed in Phase 2. No parking spaces required.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Site Consideration: The Mature City Tree</div>'))

R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">You've flagged a mature City tree growing into the lot, and the aerial confirms a substantial canopy. Toronto protects trees through its tree-protection by-laws (private-tree and City-owned/street-tree rules), which can require permits and a tree-protection zone around the trunk and root area. In practice this shapes where the garden suite and any new footprint can sit and may influence setbacks and access, rather than preventing the build. The exact protected status, ownership (private vs. City/street tree), and any tree-protection zone are confirmed early in Phase 2 so the design works with the tree from Day 1.</div>'''))

# ---------------- DEVELOPMENT GOAL SUMMARY §5 ----------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">4+1 Configuration</div>
  <p>441 Rimilton Avenue permits up to four residential units as-of-right city-wide (By-law 474-2023), plus a rear garden suite under the Garden Suite By-law — a 4+1 configuration totalling five units, matching your stated goal. <strong>The 4+1 configuration is the clear primary recommendation</strong>, designed around the mature City tree on the lot.</p>'''))

# ---------------- SUMMARY §8 ----------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>441 Rimilton Avenue confirms a strong development option. This property sits in Ward 3 (Etobicoke-Lakeshore) in an RM (Residential Multiple) zone, where up to <strong>four residential units are permitted as-of-right city-wide</strong> under By-law 474-2023, plus a rear garden suite under the Garden Suite By-law — a 4+1 (five-unit) build with no rezoning required.</p>
  <ul>
    <li><strong>The Four-Plus-Garden-Suite Advantage:</strong> this lot supports up to four units as-of-right plus a rear garden suite — no rezoning, no public hearing, no Council approval required. The RM zone may permit additional density, confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(TPL, "report_rimilton.html")
open(out, "w").write(s)

print("--- leftover check ---")
for t in ["Coxwell", "John Arockiaraj", "654-2025", "Ward 19", "Beaches", "6+1",
          "6-Unit", "6-unit", "Six-Unit", "Six-unit", "six units", "M4L 3B5",
          "johneeraj", "converted garage", "12 ft ceilings"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails, "| bytes:", len(s))
