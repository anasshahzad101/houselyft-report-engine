"""Transform the House Lyft master report into the 45 Darlingside Drive report.
Waseem Safdar | 45 Darlingside Drive, Scarborough, Toronto, ON M1E 3P2
Ward 25 (Scarborough-Rouge Park) - NOT a sixplex ward -> 4 units as-of-right
citywide (By-law 474-2023) + secondary/garden suite. Zone RS (x122).
Run from templates/ so relative asset paths resolve.
"""
import base64, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates")
SCRATCH = sys.argv[1] if len(sys.argv) > 1 else "."

s = open(os.path.join(TPL, "report_houselyft_master.html")).read()
R = []

# --- imagery: embed both validated Toronto 2025 aerials as data URIs ---------
lot_b64 = base64.b64encode(open(os.path.join(SCRATCH, "aerial_lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCRATCH, "aerial_ctx.jpg"), "rb").read()).decode()

img_old = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''

img_new = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{lot_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 6px;font-family:'Lato',Arial,sans-serif;">Aerial view – approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{ctx_b64}" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 6px;font-family:'Lato',Arial,sans-serif;">Neighbourhood context – approx. 300 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''
R.append((img_old, img_new))

# --- cover address ----------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">45 Darlingside Drive<span>Scarborough, Toronto, ON</span></div>'))

# --- property details barhead ----------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">45 Darlingside Drive, Scarborough, Toronto, ON&nbsp;&nbsp;M1E 3P2</div>'))

# --- property table 1 -------------------------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>45 Darlingside Drive, Scarborough, Toronto, ON&nbsp;&nbsp;M1E 3P2</td></tr>
    <tr><td>Name</td><td>Waseem Safdar</td></tr>
    <tr><td>Phone Number</td><td>(519) 781-4198</td></tr>
    <tr><td>Email</td><td>ch_waseemsafdar@yahoo.com</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite for rental income; explore government-backed financing options</td></tr>'''))

# --- property table 2 -------------------------------------------------------
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
    <tr><td>Neighbourhood</td><td>West Hill</td></tr>
    <tr><td>Ward</td><td>Ward 25 — Scarborough-Rouge Park</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite (primary); up to a 4-unit multiplex (alternative)</td></tr>'''))

# --- neighbourhood spotlight ------------------------------------------------
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
    45 Darlingside Drive is in the West Hill neighbourhood of southeast Scarborough — an established residential community close to Lake Ontario and the Highland Creek ravine:
    <ul>
      <li>Near Guild Park &amp; Gardens, Morningside Park, and the Lake Ontario Waterfront Trail</li>
      <li>Close to the University of Toronto Scarborough (UTSC) and Centennial College's Morningside campus</li>
      <li>Guildwood GO Station offers rail service toward downtown; several TTC bus routes serve the area</li>
      <li>Quick access to Highway 401 via Morningside Avenue and Kingston Road</li>
      <li>Established, family-oriented streets with steady rental demand (illustrative context, not a valuation)</li>
    </ul>'''))

# --- zoning table -----------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Residential Semi-Detached, Exception 900.4.10(122) (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Under Toronto's citywide multiplex permissions, up to four residential units are permitted as-of-right on a residential lot, subject to the built-form standards of the RS zone and technical review of site conditions.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023). No rezoning required. Ward 25 (Scarborough-Rouge Park) is not one of the wards carrying the six-unit as-of-right permission, so this analysis is based on the four-unit citywide envelope.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — Toronto permits up to <strong>4 residential units</strong> as-of-right on a residential lot citywide under By-law 474-2023, and a rear garden suite may be added under the Garden Suite By-law (February 2022), subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means for you" list -----------------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Multiplex (up to 4 units):</strong> A detached or semi-detached houseplex with up to four self-contained units, as-of-right citywide</li>
      <li><strong>Interior Secondary Suite:</strong> A self-contained unit within the existing home (for example, a basement apartment) — your stated goal</li>
      <li><strong>Rear Garden Suite:</strong> A detached suite in the rear yard under the Garden Suite By-law, subject to rear-yard fit</li>
      <li><strong>Internal &amp; Backyard Suites can be paired</strong> with the main dwelling to add rental income and density, within the four-unit envelope</li>'''))

# --- time-sensitive: DC waiver ----------------------------------------------
R.append(('''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). At roughly $45,000–$50,000 per unit, this is a meaningful saving on a multiplex build, with no application required. The benefit applies as long as your project stays within the as-of-right multiplex envelope. Exact figures are confirmed in Phase 2.</div></div>'''))

# --- rezoning co-green ------------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended secondary-suite and up-to-four-unit configurations are permitted as-of-right under Toronto\'s citywide multiplex and garden-suite by-laws.</div>'))

# --- rezoning comparison table: governing bylaw row -------------------------
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 474-2023 (citywide multiplex)</td><td class="n">A new site-specific by-law</td></tr>'))

# --- "also permitted" twocard -----------------------------------------------
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>Toronto's citywide multiplex permission (By-law 474-2023) allows up to four self-contained units in a residential zone without rezoning, subject to the built-form standards of the RS zone.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones, subject to rear-yard fit.</div>'''))

# --- "what this means for 303 Coxwell" + amber ------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 45 Darlingside Drive</div>
  <p>Because 45 Darlingside Drive already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm: the lot dimensions and the rear-yard fit for a garden suite.</b><br><span class="sub">A garden suite's size and siting depend on the confirmed lot dimensions and setbacks — these are finalized during the feasibility phase.</span></div>'''))

# --- Option A ---------------------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Interior Secondary Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained secondary suite within the existing home — for example, a basement apartment — rented for ongoing income while you keep the property. This is your stated goal. Interior secondary suites are permitted as-of-right on a residential lot in Toronto, subject to the Ontario Building Code and the City's site standards. The exact unit size and layout are confirmed in Phase 2. No rezoning and no minor variance are typically required for an interior suite designed within the standard envelope. Development charges do not apply to a secondary suite under provincial rules.</div>'''))

# --- Option B ---------------------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Secondary Suite + Rear Garden Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair an interior secondary suite with a detached garden suite in the rear yard — a route to as many as three income sources on the lot (the main dwelling plus two additional units) while you keep the property. The garden suite is permitted as-of-right under Toronto's Garden Suite By-law (February 2022) on a non-laneway lot, with its size and siting set by the rear-yard fit, setbacks, and height limits — confirmed in Phase 2. No parking spaces are required for these units. Development charges do not apply to additional residential units under provincial rules.</div>'''))

# --- Option C ---------------------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Up to a 4-Unit Multiplex (higher-density path)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">If you want to maximize density rather than keep the home largely as-is, Toronto's citywide multiplex permission (By-law 474-2023) allows up to four self-contained units on the lot as-of-right — no rezoning required — and a rear garden suite may be added on top under the Garden Suite By-law. A four-unit build is governed by the RS zone's built-form standards (height, setbacks, coverage); a minor variance may be required depending on the final design footprint. No parking minimums apply to multiplexes. Development charges are fully waived for multiplexes up to six units (Bill 185). The buildable envelope is confirmed in Phase 2.</div>'''))

# --- Development Goal Summary -----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Secondary Suite — with room to grow</div>
  <p>45 Darlingside Drive is a residential lot in Ward 25 (Scarborough-Rouge Park) where an interior secondary suite is permitted as-of-right — matching your goal of adding rental income while keeping the property. <strong>The secondary suite is the clear primary recommendation</strong>, with a rear garden suite, and ultimately up to a four-unit multiplex, available as higher-density paths under Toronto's citywide by-laws.</p>'''))

# --- Grants table: municipal DC waiver row ----------------------------------
R.append(('<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>',
          '<tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025) — roughly $45,000–$50,000 per unit. Parking minimums also waived city-wide since February 2022, reducing site costs. No application required — the benefit applies automatically to compliant builds. Exact figures are confirmed in Phase 2.</td></tr>'))

# --- Summary: Current Zoning Review -----------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>45 Darlingside Drive confirms a strong development option. This property is a residential lot in Ward 25 (Scarborough-Rouge Park), where Toronto's citywide multiplex permission allows up to <strong>four units as-of-right in a residential zone</strong>, and an interior secondary suite — your stated goal — is permitted with no rezoning required.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> Under By-law 474-2023, up to a four-unit multiplex is permitted on this lot as-of-right — no rezoning, no public hearing, no Council approval required — and a rear garden suite may be added under the Garden Suite By-law.</li>
  </ul>'''))

# --- apply ------------------------------------------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# --- leftover guard (strip base64 data URIs first; they contain arbitrary
#     substrings like "6+1" that would false-positive) -----------------------
import re as _re
guard = _re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', 'DATAURI', s)
leftovers = 0
for t in ["Coxwell", "John Arockiaraj", "johneeraj", "Ward 19", "654-2025", "6+1",
          "six units are permitted", "Six-Unit As-of-Right", "6-unit houseplex",
          "Beaches", "M4L 3B5", "315.9", "Woodbine", "647) 223", "RD — Residential"]:
    n = guard.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        leftovers += 1

out = os.path.join(TPL, "report_45_darlingside.html")
if fails == 0 and leftovers == 0:
    open(out, "w").write(s)
    print(f"OK -> {out}  ({len(s)} bytes)")
else:
    print(f"NOT WRITTEN. fails={fails} leftovers={leftovers}")
