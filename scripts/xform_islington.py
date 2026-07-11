"""
xform_islington.py — 2672 Islington Avenue, Etobicoke (Toronto), Navy Sing.

Master (303 Coxwell) is a SIXPLEX in Ward 19 (one of the nine 6-unit wards).
This property is a FOURPLEX: RD zone in Ward 1 (Etobicoke North), which is NOT
a six-unit ward. Verified packet (property_lookup_v2, live Toronto adapter):

    zone            RD (f13.5; a510; d0.45) (x1299)  [exception 900.3.10(1299)]
    ward            01 — Etobicoke North  (NOT in the 9 sixplex wards)
    main_units_max  4          sixplex_as_of_right  False
    adu_stacking    True       gate_pass            True

So the whole "6 units as-of-right in one of nine wards / By-law 654-2025" story
is removed and the report is reframed on the 4+1 path (By-law 474-2023 + the
Garden Suite By-law, Feb 2022). Per SYSTEM_OVERVIEW open item #1, 4+1 is the
configuration flagged as unaffected by the garden-suite-on-5/6-unit-lot question.
Unknown physical facts (lot size, year built, existing structures) are written as
confirm-phrases, never invented (AI_Report_Writer_Role_v1 layers).
Aerial: live City of Toronto 2025 ortho (OGL-Toronto), embedded as a data URI.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "templates", "report_islington.html")
AERIAL_URI_FILE = os.environ["AERIAL_URI_FILE"]
AERIAL_URI = open(AERIAL_URI_FILE).read().strip()

s = open(HTML).read()
R = []

# cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">2672 Islington Avenue<span>Etobicoke, Toronto, ON</span></div>'))

# property-details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">2672 Islington Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M9V 2X5</div>'))

# aerial/street image row + licence  (embed the real, validated Toronto ortho)
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall" style="padding:0;overflow:hidden;"><img src="__AERIAL__" alt="Aerial view of 2672 Islington Avenue" style="width:100%;height:100%;object-fit:cover;"></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(added in the feasibility phase)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Aerial: City of Toronto Orthophoto 2025 (8&nbsp;cm), approx. 90&nbsp;m across. Contains information licensed under the Open Government Licence &ndash; Toronto. Street-view image added in the feasibility phase.</div>'''))

# property table 1
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>2672 Islington Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M9V 2X5</td></tr>
    <tr><td>Name</td><td>Navy Sing</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development / multi-family rental; maximize unit count (as stated at intake)</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Toronto (former Etobicoke)</td></tr>
    <tr><td>Neighbourhood</td><td>Thistletown–Beaumond Heights</td></tr>
    <tr><td>Ward</td><td>Ward 1 — Etobicoke North</td></tr>
    <tr><td>Community Council</td><td>Etobicoke York District</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed in the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in the feasibility phase (RD zone minimum frontage 13.5 m)</td></tr>
    <tr><td>Development Goals</td><td>4+1 Multiplex (4-unit houseplex + garden suite) — primary as-of-right path</td></tr>'''))

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
    2672 Islington Avenue is in the Thistletown–Beaumond Heights neighbourhood of Etobicoke North, in Toronto's northwest end along Islington Avenue — an established, primarily residential area:
    <ul>
      <li>Fronts Islington Avenue, a north–south arterial served by TTC bus routes connecting to the subway network</li>
      <li>Established detached-housing streets with generous lot depths — the kind of stock that suits gentle-density multiplex conversion</li>
      <li>Close to Humber River parkland and local green space to the west</li>
      <li>Neighbourhood amenities, schools, and shopping within the surrounding Etobicoke North community</li>
      <li>Illustrative context only — not a valuation. Precise transit, amenity, and lot details are confirmed in the feasibility phase.</li>
    </ul>'''))

# zoning table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD (f13.5; a510; d0.45) (x1299) — Residential Detached, with site-specific exception 900.3.10(1299) (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 1 (Etobicoke North), Etobicoke York Community Council district. Setbacks, coverage, height, and the site-specific exception 900.3.10(1299) are reviewed against the confirmed lot dimensions in the feasibility phase.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide in residential zones (By-law 474-2023). No rezoning required. (The 6-unit as-of-right permission applies only in nine designated wards; Ward 1 is not among them.)</td></tr>
    <tr><td>Permitted Uses</td><td>Multiplex / multi-unit housing — the RD zone permits up to <strong>4 residential units</strong> as-of-right, plus one additional residential unit as a rear garden or laneway suite, subject to technical review of site conditions and the site-specific exception.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> for a 4-unit multiplex + garden suite as-of-right; proceed to Step 2 — <strong>Builder Ready Package™</strong>. A larger 4–6 storey / higher-unit building is beyond the as-of-right envelope and would require a separate rezoning — assessed in Phase 2.</td></tr>'''))

# "what this means for you" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> A standalone building of up to four residential units</li>
      <li><strong>Garden or Laneway Suite:</strong> A self-contained unit in the rear yard, permitted as-of-right in residential zones (Garden Suite By-law, February 2022)</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>'''))

# time-sensitive DC waiver line
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">DC Waiver — Already in Effect</div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). A 4-unit multiplex plus a garden suite sits comfortably within this threshold, so the waiver applies with no application required — a saving of approximately $45,000–$50,000 per unit. The benefit holds as long as the project stays within the small-multiplex threshold (up to six units).</div></div>'''))

# rezoning green box
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 4+1 configuration (four-unit multiplex plus a garden suite) is permitted as-of-right under Toronto By-law 474-2023 and the Garden Suite By-law (February 2022).</div>'))

# comparison table "what governs your build"
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023</td><td class="n">A new site-specific by-law</td></tr>'))

# also-permitted twocard
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>''',
'''    <div class="card2"><div class="ct">Four-unit houseplex</div>Toronto's multiplex permissions (By-law 474-2023) allow up to four residential units in a residential zone city-wide, without rezoning.</div>'''))

# "what this means for" barhead + paragraph + amber note
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 2672 Islington Avenue</div>
  <p>Because 2672 Islington Avenue already permits the recommended 4+1 build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm early: the exact lot dimensions and the site-specific exception 900.3.10(1299).</b><br><span class="sub">Both set the final buildable envelope and are resolved against a survey in the feasibility phase before design proceeds.</span></div>'''))

# development option A header
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1) — Primary Recommendation</div>'))

# option A body
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear yard. Total: 5 independent units — the configuration explicitly permitted as-of-right, with no rezoning and no minor variance likely if designed within the standard RD envelope. Fully as-of-right under By-law 474-2023 (four units) and the Garden Suite By-law, February 2022 (the rear suite). Exact unit sizes and the buildable footprint follow from the confirmed lot dimensions and the site-specific exception 900.3.10(1299), resolved in the feasibility phase. No parking minimums for multiplexes (city-wide, since February 2022). Development charges fully waived for ≤6 units (Bill 185).</div>'''))

# development option B header
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — 4-Unit Multiplex (no rear suite)</div>'))

# option B body
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A detached 4-unit houseplex without the rear suite — the simplest, fastest path to as-of-right density. Total: 4 independent units, fully as-of-right under By-law 474-2023. This keeps the rear yard open (for parking, amenity, or a garden suite added in a later phase) and minimises site complexity. No parking spaces required. Development charges fully waived for ≤6 units (Bill 185). A strong option where the priority is a straightforward build with room to expand later.</div>'''))

# development option C header
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Garden / Laneway Suite as a Phased First Step</div>'))

# option C body
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite is permitted as-of-right in residential zones (a laneway suite instead, where a lane abuts the lot — one ancillary suite per lot). Building the suite first is a lighter-touch way to add a single rental unit and income while planning the larger multiplex for a later phase. Whether the lot abuts a laneway, and the suite's exact size and siting, are confirmed against a survey in the feasibility phase.</div>'''))

# development goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">4+1 Configuration</div>
  <p>2672 Islington Avenue is a residential (RD) lot in Ward 1 — Etobicoke North, where a 4-unit multiplex plus a rear garden suite is permitted as-of-right under By-law 474-2023 and the Garden Suite By-law (February 2022). <strong>The 4+1 configuration (five units) is the clear primary recommendation</strong> — the fullest build available on this lot without rezoning.</p>'''))

# summary — current zoning review
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>2672 Islington Avenue confirms a solid, low-friction development option. This RD (Residential Detached) lot in Ward 1 (Etobicoke North) supports up to <strong>four residential units plus a rear garden suite — five units in total — as-of-right</strong>, with no rezoning required. This path is secured through Toronto's multiplex permissions (By-law 474-2023) and the Garden Suite By-law (February 2022).</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> a 4-unit houseplex plus a garden suite is permitted with no rezoning, no public hearing, and no Council approval required — the project advances straight to design and permitting.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# inject the aerial data URI last (kept out of the assert loop for readability)
if s.count("__AERIAL__") == 1:
    s = s.replace("__AERIAL__", AERIAL_URI)
else:
    print(f"[FAIL] aerial marker count = {s.count('__AERIAL__')}")
    fails += 1

open(HTML, "w").write(s)

# leftover check — none of these Coxwell / sixplex-recommendation tokens may remain
for t in ["Coxwell", "John", "Arockiaraj", "654-2025", "Ward 19", "Beaches",
          "6+1", "6-Unit", "Six-Unit", "M4L", "647) 223", "johneeraj",
          "315.9", "Woodbine", "Greenwood", "converted garage", "12 ft ceilings",
          "20 ft x 170", "Community League"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
