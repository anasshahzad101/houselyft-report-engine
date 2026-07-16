"""
xform_medford.py — master (303 Coxwell, Ward 19 sixplex) -> 65 Medford Avenue.

65 Medford Avenue is in Ward 20 (Scarborough Southwest) — NOT one of the nine
sixplex wards. So the recommendation is a 4+1 (fourplex + garden suite = 5
units), permitted as-of-right city-wide under By-law 474-2023. By-law 654-2025
(six units) does NOT apply here. Toronto financing/HST/Bill 185 content is
correct and kept. Real 2025 Toronto orthophotos are injected. No property facts
are invented — lot size, year built, accessory structures are "to be confirmed".
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_65_medford.html")

s = open(SRC, encoding="utf-8").read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">65 Medford Avenue<span>Toronto, ON</span></div>'))

# ---- property details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">65 Medford Avenue, Toronto, ON&nbsp;&nbsp;M1L 4G5</div>'))

# ---- imagery row: placeholders -> real Toronto 2025 aerials ----
R.append((
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="aerial_medford_lot.jpg" style="width:100%;height:100%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Aerial view &mdash; approx. 90&nbsp;m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="aerial_medford_context.jpg" style="width:100%;height:100%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Neighbourhood context &mdash; approx. 240&nbsp;m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''))

# ---- property table 1 (contact) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>65 Medford Avenue, Toronto, ON&nbsp;&nbsp;M1L 4G5</td></tr>
    <tr><td>Name</td><td>Vil C</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (up to 4 units as-of-right)</td></tr>'''))

# ---- property table 2 (location / lot) ----
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
'''    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Oakridge (Scarborough Southwest)</td></tr>
    <tr><td>Ward</td><td>Ward 20 — Scarborough Southwest</td></tr>
    <tr><td>Community Council</td><td>Scarborough Community Council district</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (Zone: RD, exception 900.3.10(350))</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (RD minimum frontage standard: 9.0 m)</td></tr>
    <tr><td>Development Goals</td><td>4+1 Multiplex (fourplex + rear garden suite); up to 5 units</td></tr>'''))

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
    65 Medford Avenue is in Oakridge, an established residential neighbourhood in the Scarborough Southwest area of Toronto's east end:
    <ul>
      <li>Established east-end Toronto neighbourhood of low-rise residential streets — the kind of character stock that rents well and holds value</li>
      <li>Close to the Danforth Avenue and Victoria Park Avenue corridors for retail, groceries, and services</li>
      <li>TTC bus and streetcar service in the area, with rapid-transit access on the Bloor–Danforth subway line nearby</li>
      <li>Parks, schools, and community amenities within the surrounding neighbourhood</li>
      <li>(Illustrative context, not a valuation. Specific distances and amenities are confirmed in Phase 2.)</li>
    </ul>'''))

# ---- SECTION 2 — CURRENT ZONING (the accuracy-critical rewrite) ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013); exception 900.3.10(350), frontage standard f9.0</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 20 (Scarborough Southwest) is in the Scarborough Community Council district. This ward is <strong>not</strong> one of the nine wards with six-unit as-of-right permission; up to <strong>4 units</strong> are permitted as-of-right city-wide.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023). The six-unit as-of-right permission (By-law 654-2025, June 2025) applies only in the Toronto &amp; East York district wards and does <strong>not</strong> apply to this property. No rezoning is required for a 4-unit build.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone allows up to <strong>4 residential units</strong> as-of-right in a detached houseplex under By-law 474-2023, subject to technical review of site conditions. A rear garden suite may be added as a fifth unit.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- TIME SENSITIVE — fix DC waiver per-project figure (Coxwell assumed 6 units) ----
R.append(('''<div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''<div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves approximately $45,000–$50,000 per unit, with no application required. On a four-unit build the total scales accordingly (illustrative; confirmed in Phase 2). This benefit applies as long as your project stays within the 6-unit as-of-right envelope.</div></div>'''))

# ---- SECTION 3 — REZONING ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 4+1 configuration is permitted as-of-right under Toronto By-law 474-2023.</div>'))

R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023</td><td class="n">A new site-specific by-law</td></tr>'))

R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Four-unit houseplex</div>Up to four units are permitted as-of-right in a residential zone city-wide under By-law 474-2023 — no rezoning, public hearing, or Council approval required.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>'''))

R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 65 Medford Avenue</div>
  <p>Because 65 Medford Avenue already permits the recommended four-unit build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Items to confirm in Phase 2: the exact lot dimensions and the permit status of any existing accessory structures.</b><br><span class="sub">These set the final buildable envelope and the garden-suite fit, and any un-permitted structure needs a retroactive application before financing or development can proceed.</span></div>'''))

# ---- SECTION 4 — DEVELOPMENT OPTIONS ----
R.append(('''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>
    </div></div>''',
'''  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one rear garden suite. Total: 5 independent units. Fully as-of-right under By-law 474-2023 — no rezoning required, and no variances if designed within the standard envelope. RD zone built-form standards (height, coverage, setbacks) apply and are resolved during design. No parking minimums for multiplexes. Development charges fully waived for builds up to 6 units (Bill 185). Final lot dimensions, the buildable envelope, and the garden-suite fit are confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — Detached Fourplex (4 Units)</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex without the rear suite — a simpler build that still captures the full four-unit as-of-right permission under By-law 474-2023. This is the fallback if the rear yard cannot accommodate a garden suite within the required setbacks. No parking spaces required. Development charges fully waived. The rear garden suite can also be added in a later phase once the main build is complete.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Rear Garden Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Paired with the fourplex, it forms the fifth unit in the recommended 4+1 configuration. Whether a garden suite fits depends on the rear-yard depth, angular-plane, and setback rules — confirmed in Phase 2 against the surveyed lot. Any existing accessory structure on the lot should have its permit status confirmed before it is counted as a legal unit.</div>
    </div></div>'''))

# ---- SECTION 5 — DEVELOPMENT GOAL SUMMARY ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">4+1 Configuration</div>
  <p>65 Medford Avenue permits up to four units as-of-right in a residential zone city-wide under By-law 474-2023. Combined with a rear garden suite under the Garden Suite By-law (February 2022), the <strong>4+1 configuration — five units in total — is the primary recommendation</strong> for this lot. (Ward 20 is not one of the nine wards with six-unit as-of-right permission, so a fourplex is the ceiling on the main building without rezoning.)</p>'''))

# ---- SECTION 7 — GRANTS: fix DC waiver per-project figure ----
R.append(('<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>',
          '<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves approximately $45,000–$50,000 per unit; on a four-unit build the total scales accordingly (illustrative — confirmed in Phase 2). Parking minimums also waived city-wide since February 2022, reducing site costs. No application required — benefit applies automatically to compliant builds.</td></tr>'))

# ---- SECTION 8 — SUMMARY ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>65 Medford Avenue confirms a strong development option. This property is located in Ward 20 (Scarborough Southwest), where up to <strong>four units are permitted as-of-right in a residential zone</strong> city-wide under By-law 474-2023 — with a rear garden suite available as a fifth unit. No rezoning is required to reach the recommended 4+1 configuration.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> Up to four units are permitted on this lot under By-law 474-2023 — no rezoning, no public hearing, no Council approval required — plus a rear garden suite under the February 2022 Garden Suite By-law for a fifth unit.</li>
  </ul>'''))

# ---- apply ----
missing = []
for old, new in R:
    n = s.count(old)
    if n != 1:
        missing.append((n, old[:70]))
        continue
    s = s.replace(old, new)

if missing:
    print("FAILED replacements (count, snippet):")
    for n, snip in missing:
        print(f"  [{n}x] {snip!r}")
    raise SystemExit(1)

open(OUT, "w", encoding="utf-8").write(s)

# ---- leftover guard ----
leftovers = []
for term in ["303 Coxwell", "Coxwell", "John Arockiaraj", "John's", "johneeraj",
             "223-4342", "Ward 19", "Beaches-East York",
             "Six-Unit", "six units are permitted", "6+1", "6-Unit Multiplex",
             "Woodbine", "Upper Beaches", "315.9", "M4L 3B5"]:
    if term in s:
        leftovers.append((term, s.count(term)))
# By-law 654-2025 must appear EXACTLY once — in the sentence stating it does
# NOT apply to Ward 20. Any other count means a stray sixplex claim survived.
if s.count("654-2025") != 1 or "does <strong>not</strong> apply" not in s:
    leftovers.append(("654-2025 context guard", s.count("654-2025")))
if leftovers:
    print("LEFTOVER city/lead references still present:")
    for t, c in leftovers:
        print(f"  {c}x  {t!r}")
    raise SystemExit(2)

print("OK ->", OUT)
print("bytes:", len(s))
