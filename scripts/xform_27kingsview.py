# Transform master -> 27 Kingsview Blvd, Etobicoke (Toronto Ward 1) report.
# Property is RD, Ward 1 (Etobicoke North) => 4 units as-of-right (NOT a sixplex ward).
# Homeowner goal: secondary suite. All facts from the zoning engine packet.
import io, os
os.chdir(os.path.join(os.path.dirname(__file__), "..", "templates"))
s = io.open("report_27kingsview.html", encoding="utf-8").read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">27 Kingsview Boulevard<span>Toronto (Etobicoke), ON</span></div>'))

# property details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">27 Kingsview Boulevard, Etobicoke, Toronto, ON&nbsp;&nbsp;M9R 1T5</div>'))

# aerial / street imagery + licence credit (real OGL-Toronto aerial embedded)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="padding:0;overflow:hidden;"><img src="aerial_27kingsview.jpg" alt="Aerial view of 27 Kingsview Boulevard" style="width:100%;height:100%;object-fit:cover;"></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(added in Phase 2)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Aerial: City of Toronto Orthophoto 2025 (8&nbsp;cm), approx. 90&nbsp;m across. Contains information licensed under the Open Government Licence – Toronto. Street-level imagery added in Phase 2.</div>'''))

# property table 1 (contact + goals)
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>27 Kingsview Boulevard, Etobicoke, Toronto, ON&nbsp;&nbsp;M9R 1T5</td></tr>
    <tr><td>Name</td><td>Afshan Haq</td></tr>
    <tr><td>Phone Number</td><td>(647) 334-1973</td></tr>
    <tr><td>Email</td><td>afshanhaq@yahoo.com</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite; understand the property's full development capacity</td></tr>'''))

# property table 2
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
    <tr><td>Ward</td><td>Ward 1 — Etobicoke North</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Zoning Designation</td><td>RD (f13.5; a510; d0.45) — Residential Detached</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite (primary); up to a 4-unit multiplex as the full as-of-right envelope</td></tr>'''))

# neighbourhood spotlight
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
    27 Kingsview Boulevard is in Kingsview Village–The Westway, an established residential neighbourhood in Etobicoke North in the city's west end:
    <ul>
      <li>A settled, low-rise residential area — the kind of stable stock that rents well and holds value</li>
      <li>Convenient access to the Highway 401 and Highway 427 corridors for commuting across the GTA</li>
      <li>TTC bus service connects the area toward the Bloor–Danforth (Line 2) subway at Kipling and Islington stations</li>
      <li>Close to local parks, schools, and everyday shopping along the surrounding arterial roads</li>
      <li>Illustrative context only, not a valuation; specific amenities are confirmed in Phase 2.</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. The property sits in Ward 1 (Etobicoke North), where up to four residential units are permitted as-of-right city-wide. Etobicoke North is <strong>not</strong> one of the nine wards with six-unit as-of-right permissions.</td></tr>
    <tr><td>Recent Changes</td><td>Toronto's multiplex by-law permits up to <strong>4 units as-of-right city-wide</strong> (By-law 474-2023, May 2023) on Neighbourhoods-designated residential land — no rezoning required. The separate six-unit permission applies only in nine designated wards and does not include Etobicoke North.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone allows up to <strong>4 residential units</strong> as-of-right in a multiplex form, and a detached garden or laneway suite may be added on a project of four units or fewer, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# what this means for you
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Internal Secondary Suite:</strong> a self-contained unit within the existing home (such as a basement apartment) — your stated goal</li>
      <li><strong>Detached Houseplex (up to 4 units):</strong> a standalone multi-unit home, permitted as-of-right city-wide</li>
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> multi-unit attached homes — side-by-side or vertically stacked units</li>
      <li><strong>Backyard / Garden Suite:</strong> a detached rear suite that may be paired with the main dwelling to add density, subject to site standards</li>'''))

# time-sensitive: DC waiver block (fix 6-unit envelope framing; keep per-unit figure)
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025) — approximately $45,000–$50,000 per unit, with no application required. Your as-of-right envelope on this lot is up to four units, so a compliant multiplex here sits comfortably within the waiver, and the total saving scales with the number of units you build.</div></div>'''))

# section 3 co-green
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended configuration — up to a 4-unit multiplex, including your secondary suite — is permitted as-of-right under Toronto’s multiplex by-law (474-2023). No rezoning is required.</div>'))

# section 3 cmp table governing row
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023</td><td class="n">A new site-specific by-law</td></tr>'))

# section 3 twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Toronto's multiplex by-law (474-2023) permits up to four residential units as-of-right in a residential zone city-wide — no rezoning, and no Committee of Adjustment when built within the standard envelope.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones — an option to confirm alongside a multiplex on this lot.</div>'''))

# section 3 "what this means" barhead + para + amber
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 27 Kingsview Boulevard</div>
  <p>Because 27 Kingsview Boulevard already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2:</b><br><span class="sub">the lot’s exact area and frontage (which set the buildable envelope), and whether the rear yard suits a detached garden or laneway suite. Both are settled with a site review before design.</span></div>'''))

# section 4 option A
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Internal Secondary Suite (your stated goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained secondary suite within the existing home — most commonly a basement apartment with its own entrance. This is your stated goal and the most direct way to add a rental income stream while keeping your home. It counts as one of the up-to-four units permitted as-of-right, so no rezoning is required. Interior suites are governed by the Ontario Building Code — minimum ceiling height, fire separation, and egress are the items to verify early, and these are confirmed in Phase 2. No parking space is required.</div>'''))

# section 4 option B
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Up to a 4-Unit Multiplex (fourplex)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Convert and/or expand the property into a multiplex of up to four self-contained units — the full as-of-right envelope for this lot under By-law 474-2023, city-wide, with no rezoning. This is the higher-density path if you want to maximize rental income rather than add a single suite. The exact unit mix and sizes depend on the confirmed lot dimensions and the RD built-form standards (height, coverage, setbacks), confirmed in Phase 2. No parking spaces are required, and development charges are waived within the multiplex envelope.</div>'''))

# section 4 option C
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Adding a Detached Garden or Laneway Suite</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Toronto's Garden Suite By-law (February 2022) permits a detached suite in the rear yard as-of-right in residential zones, and a laneway suite where the lot backs onto a public lane. On a project of four units or fewer, this can be an additional income unit alongside the main dwelling. Whether a garden or laneway suite fits — and its size — depends on the rear-yard dimensions, tree protection, and access, all confirmed with a site review in Phase 2. No car parking is required for the suite.</div>'''))

# section 5 goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Secondary Suite — with Multiplex Upside</div>
  <p>27 Kingsview Boulevard is in Ward 1 (Etobicoke North), where up to four residential units are permitted as-of-right in a residential zone under Toronto’s multiplex by-law (474-2023) — no rezoning required. <strong>Your secondary suite is the clear starting recommendation</strong>, and the same lot can support up to a four-unit multiplex, with a detached garden or laneway suite as a further option to confirm in Phase 2.</p>'''))

# section 7 municipal DC waiver grant row
R.append(('<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>',
          '<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025) — approximately $45,000–$50,000 per unit, so the total saving scales with the number of units you build. Parking minimums are also waived city-wide (since February 2022), removing a significant per-space site cost. No application required — the benefit applies automatically to compliant builds.</td></tr>'))

# section 8 summary current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>27 Kingsview Boulevard confirms a strong development option. This property is in Ward 1 (Etobicoke North) on Neighbourhoods-designated residential land, where up to <strong>four residential units are permitted as-of-right in a residential zone</strong> under Toronto’s multiplex by-law (474-2023) — no rezoning, no public hearing, and no Council approval required.</p>
  <ul>
    <li><strong>The As-of-Right Multiplex Advantage:</strong> your secondary-suite goal fits comfortably within a permission that allows up to four units city-wide, giving you room to grow the project later without changing the zoning.</li>
    <li><strong>A note on six units:</strong> the six-unit permission applies only in nine designated wards, which do not include Etobicoke North — so this report is built around the four-unit envelope that genuinely applies to your lot.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

io.open("report_27kingsview.html", "w", encoding="utf-8").write(s)

# leftover check (hard fails: property/name; soft: sixplex-ward artefacts)
print("--- leftover check ---")
for t in ["Coxwell", "John Arockiaraj", "johneeraj", "M4L 3B5", "Ward 19", "Beaches",
          "Woodbine", "Greenwood", "654-2025", "6+1", "6-Unit", "6-unit houseplex",
          "315.9", "20 ft", "170 ft", "750 sq ft", "garage", "Arockiaraj"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
