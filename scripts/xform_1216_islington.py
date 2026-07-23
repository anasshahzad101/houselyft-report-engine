"""Transform the House Lyft master report into the 1216 Islington Avenue report.

Lead: Tenzing Gomphel | 1216 Islington Avenue, Etobicoke, Toronto ON M8Z 4T1
Verified packet (engine/property_lookup_v2 + Toronto adapter):
  City: Toronto (Etobicoke) | Zone: RD (f13.5; a510; d0.45) | Ward 3 Etobicoke-Lakeshore
  Max units as-of-right: 4 (NOT a sixplex ward) + 1 garden suite = 5 units.
Owner's stated goal is a 10-unit building — beyond as-of-right; framed honestly
as a rezoning / Major-Streets path (Phase 2), never promised.

Follows the scripts/xform_*.py pattern: assert each replacement matches once,
then leftover-check for source-city / wrong-ward references.
"""
import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_1216_islington.html")
IMG = os.path.join(ROOT, "scratch_imagery")

s = open(MASTER).read()

# --- real aerials (City of Toronto Orthophoto 2025, OGL-Toronto) -------------
lot_b64 = base64.b64encode(open(os.path.join(IMG, "lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(IMG, "context.jpg"), "rb").read()).decode()

IMGROW_OLD = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''

IMGROW_NEW = (
'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:100%%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:2px 7px;">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:100%%;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:2px 7px;">Neighbourhood context — approx. 190 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>''' % (lot_b64, ctx_b64))

R = []
R.append((IMGROW_OLD, IMGROW_NEW))

# --- cover ------------------------------------------------------------------
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">1216 Islington Avenue<span>Toronto (Etobicoke), ON</span></div>'))

# --- property details barhead ----------------------------------------------
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">1216 Islington Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M8Z 4T1</div>'))

# --- property table 1 -------------------------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1216 Islington Avenue, Etobicoke, Toronto, ON&nbsp;&nbsp;M8Z 4T1</td></tr>
    <tr><td>Name</td><td>Tenzing Gomphel</td></tr>
    <tr><td>Phone Number</td><td>(647) 989-7378</td></tr>
    <tr><td>Email</td><td>gomphel@hotmail.com</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — maximize unit count (owner's stated goal: a 10-unit building)</td></tr>'''))

# --- property table 2 -------------------------------------------------------
R.append(('''    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 &mdash; Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m&sup2; (20 ft &times; 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>'''.replace('&mdash;','—').replace('&sup2;','²').replace('&times;','×'),
'''    <tr><td>Municipality</td><td>Toronto (Etobicoke)</td></tr>
    <tr><td>Neighbourhood</td><td>South Etobicoke — Islington Avenue corridor (Stonegate-Queensway area)</td></tr>
    <tr><td>Ward</td><td>Ward 3 — Etobicoke-Lakeshore</td></tr>
    <tr><td>Frontage Road</td><td>Islington Avenue — a designated major arterial (Major Street)</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 — Zone RD (f13.5; a510; d0.45)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase (frontage &amp; area from MPAC or survey)</td></tr>
    <tr><td>Development Goals</td><td>4-unit multiplex + garden suite as-of-right (5 units); larger multiplex toward the 10-unit goal via rezoning — assessed in Phase 2</td></tr>'''))

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
    1216 Islington Avenue is in south Etobicoke, fronting Islington Avenue — a major north-south arterial in Toronto's west end (Ward 3, Etobicoke-Lakeshore). The following is illustrative context, confirmed during the feasibility phase:
    <ul>
      <li>Frontage on a major arterial with TTC bus service along Islington Avenue, connecting toward Islington subway station (Line 2)</li>
      <li>Established low-rise residential area — a mix of detached and semi-detached homes, as seen in the aerial imagery above</li>
      <li>Convenient regional access via The Queensway, the Gardiner Expressway, and the QEW</li>
      <li>Arterial-facing lots like this can carry additional built-form potential under Toronto's Major Streets policy — explored later in this report</li>
      <li>Local amenities, exact transit routes, and walk times are confirmed in Phase 2</li>
    </ul>'''))

# --- zoning table -----------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD &mdash; Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district &mdash; one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 &mdash; Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types &mdash; the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 &mdash; <strong>Builder Ready Package™</strong></td></tr>'''.replace('&mdash;','—'),
'''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013). Zone label RD (f13.5; a510; d0.45).</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 3 (Etobicoke-Lakeshore) is <strong>not</strong> among the nine wards carrying the six-unit as-of-right permission, so the city-wide four-unit multiplex rule governs this lot.</td></tr>
    <tr><td>Recent Changes</td><td>Up to <strong>4 units as-of-right city-wide</strong> in a multiplex form (By-law 0473/0474, May 2023). Ontario's Bill 23 sets a floor of three units on a serviced residential lot. No rezoning is required for a multiplex of up to four units.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone permits up to <strong>4 residential units</strong> as-of-right in a multiplex, plus one detached garden suite (up to 5 units total), subject to technical review of site conditions. A larger building requires rezoning.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>PARTIALLY as-of-right.</strong> A 4-unit multiplex + garden suite (5 units) is permitted as-of-right; the 10-unit goal requires a rezoning — assessed in Step 2, <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means" list --------------------------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes &mdash; side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>'''.replace('&mdash;','—'),
'''      <li><strong>Multiplex (up to 4 units):</strong> A detached or semi-detached building with up to four self-contained units, as-of-right</li>
      <li><strong>Detached Garden Suite:</strong> One additional suite in the rear yard, as-of-right (one ADU per lot)</li>
      <li><strong>Internal / Basement Suite:</strong> A secondary suite within the main dwelling, which can form one of the four multiplex units</li>
      <li><strong>Taller forms (townhouse / small apartment):</strong> Potentially available on this arterial lot under the Major Streets policy or through rezoning — explored later and in Phase 2</li>'''))

# --- time-sensitive: DC waiver ----------------------------------------------
R.append(('''    <div class="d"><div class="dt">DC Waiver &mdash; Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000&ndash;$270,000 per project &mdash; approximately $45,000&ndash;$50,000 per unit &mdash; at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>'''.replace('&mdash;','—').replace('&ndash;','–'),
'''    <div class="d"><div class="dt">DC Waiver — Already in Effect</div><div class="dx">Development charges are fully eliminated for multiplexes of up to six units in Toronto (Bill 185, January 2025). Illustrative City-wide figures put the saving at roughly $200,000–$270,000 per project (about $45,000–$50,000 per unit), with no application required. Your as-of-right 4+1 project sits comfortably within the up-to-six-unit waiver threshold. Exact figures are confirmed in Phase 2.</div></div>'''))

# --- rezoning: co-green ------------------------------------------------------
R.append(('''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>''',
'''  <div class="co-green"><div class="ct2">Not Required for the Recommended Build</div>The recommended 4-unit multiplex plus a garden suite (5 units) is permitted as-of-right — no rezoning is required for that configuration. Reaching the larger 10-unit building you are targeting would require a rezoning application (see below).</div>'''))

# --- rezoning: comparison table "what governs" ------------------------------
R.append(('''    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><td>What governs your build</td><td class="g">By-law 0473/0474 (city-wide fourplex)</td><td class="n">A new site-specific by-law</td></tr>'''))

# --- rezoning: also-permitted twocard ---------------------------------------
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Four-unit multiplex</div>Up to four self-contained units are permitted as-of-right city-wide in a residential zone under By-law 0473/0474 (May 2023) — no rezoning, and no public meeting where the design stays within the envelope.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones. One ADU per lot; it stacks on a four-unit-and-under multiplex.</div>
  </div>'''))

# --- rezoning: "what this means" barhead ------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 1216 Islington Avenue</div>'''))

# --- rezoning: paragraph ----------------------------------------------------
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <p>The recommended 4-unit multiplex plus garden suite is permitted under existing zoning, so that build advances directly to design and permitting with no rezoning. Your stated goal of a 10-unit building is beyond the as-of-right envelope on this RD lot and would require a rezoning (a Zoning By-law Amendment, and potentially an Official Plan Amendment) with public consultation and Council approval. Islington Avenue is a major arterial, which may support additional height and units under Toronto's Major Streets policy — the most credible path to greater density, assessed in Phase 2. Nothing about the larger scheme is guaranteed; this assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# --- rezoning: co-amber -----------------------------------------------------
R.append(('''  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-amber"><b>Two items to confirm in Phase 2: the lot's exact frontage and area, and whether Islington Avenue's Major Street designation applies to this parcel.</b><br><span class="sub">Both determine how far the buildable envelope can stretch toward your unit-count goal.</span></div>'''))

# --- options A header + body ------------------------------------------------
R.append(('  <div class="opt"><div class="oh">Option A &mdash; 4-Unit Multiplex + 1 Garden Suite (4+1)</div>'.replace('&mdash;','—'),
          '  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1) — Primary Recommendation (as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage &mdash; with its 12 ft ceilings, heated floors, running water, and powder room &mdash; provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m&sup2;). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for &le;6 units (Bill 185).</div>'''.replace('&mdash;','—').replace('&sup2;','²').replace('&le;','≤'),
'''      <div class="od">A four-unit multiplex in the main building, plus one detached garden suite in the rear yard. Total: five independent units — the maximum permitted as-of-right on this RD lot. Fully as-of-right under By-law 0473/0474; no rezoning, and no variances likely required if designed within the standard envelope. RD zone built-form standards apply (frontage, coverage, height, and setbacks confirmed per lot in Phase 2). No parking minimums for multiplexes. Development charges fully waived for projects of up to six units (Bill 185). This is the fastest, lowest-risk path to income on the property and the recommended starting point.</div>'''))

# --- options B header + body ------------------------------------------------
R.append(('  <div class="opt"><div class="oh">Option B &mdash; 6-Unit Multiplex + 1 Garden Suite (6+1) &mdash; Primary Recommendation</div>'.replace('&mdash;','—'),
          '  <div class="opt"><div class="oh">Option B — Larger Multiplex / Mid-Rise Toward the 10-Unit Goal (requires rezoning)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Your stated goal is a 10-unit building. That is beyond the four-unit as-of-right envelope on this RD lot, so it would require a rezoning — a Zoning By-law Amendment (and possibly an Official Plan Amendment), with public consultation and Council approval. Because 1216 Islington fronts a major arterial, Toronto's Major Streets policy (which can support townhouse and small-apartment forms up to six storeys on qualifying Residential lots) is the most credible route to added height and units, and is assessed in Phase 2. Unit yield, height, and approval odds are not guaranteed and depend on lot dimensions, servicing, and planning review. No parking minimums apply. This option is presented as upside, not as an as-of-right entitlement.</div>'''))

# --- options C header + body ------------------------------------------------
R.append(('  <div class="opt"><div class="oh">Option C &mdash; Note on the Existing Garage / Rear Suite</div>'.replace('&mdash;','—'),
          '  <div class="opt"><div class="oh">Option C — The Garden Suite &amp; Lot Considerations</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step &mdash; both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>'''.replace('&mdash;','—'),
'''      <div class="od">Under Toronto's Garden Suite By-law (February 2022, as amended), a detached rear suite on a non-laneway lot is permitted as-of-right in residential zones — one ADU per lot, stacking on a four-unit-and-under multiplex. The suite's footprint, height, and setbacks are set by the by-law and confirmed per lot in Phase 2. Key items to confirm for this property: exact lot frontage and area (from MPAC or a survey), rear-yard fit and any protected trees, laneway access (which would decide garden versus laneway), and any heritage or arterial-setback overlays along Islington Avenue.</div>'''))

# --- development goal summary -----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 &mdash; one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>'''.replace('&mdash;','—'),
'''  <div class="barhead" style="text-align:left;">4+1 Multiplex As-of-Right, with a Rezoning Path to More</div>
  <p>1216 Islington Avenue is an RD lot in Ward 3 (Etobicoke-Lakeshore), where up to four units are permitted as-of-right in a multiplex, plus one garden suite — five units in total, with no rezoning. <strong>The 4+1 multiplex is the clear, low-risk primary recommendation.</strong> Your larger 10-unit ambition is not available as-of-right and would require a rezoning; because the lot fronts a major arterial, the Major Streets policy is the most promising route to greater height and density, and we assess it in Phase 2.</p>'''))

# --- financing gated rows (MLI Select + ACLP, thresholds shown) -------------
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC MLI Select</td><td>Specialized insured financing for purpose-built rental — reduced insurance premiums, amortization up to ~50 years, and high loan-to-cost on a points system (affordability, energy, accessibility). <strong>Available at five or more rental units.</strong> Your 4-plex-plus-garden-suite reaches five, so this opens up if the garden suite is confirmed as the fifth rental unit in Phase 2. (CMHC MLI Select product terms.)</td></tr>
    <tr><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental. <strong>Requires a minimum $1M loan.</strong> Whether the project reaches that threshold is confirmed against the construction budget in Phase 2. (CMHC ACLP program terms.)</td></tr>
    <!-- GATED_FINANCING_ROWS: injected per config/programs.json after gate check (Toronto; up to 4+1 as-of-right, 10-unit goal via rezoning). -->'''))

# --- grants gated rows (DC waiver + Bill 23 ARU + GST/HST PBRH) --------------
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td><strong>At any tier up to 6 units (Toronto).</strong> Development charges fully eliminated for multiplexes of up to six units (Bill 185, January 2025). Illustrative City figures: roughly $200,000–$270,000 per project (~$45,000–$50,000 per unit). No application required — applies automatically to compliant builds. Parking minimums also waived city-wide since February 2022. (City of Toronto, Bill 185.)</td></tr>
    <tr><td>Provincial</td><td>ARU Development-Charge Exemption (Bill 23)</td><td><strong>For the additional residential units (garden / interior suite).</strong> Additional residential units are exempt from development charges under Ontario's More Homes Built Faster Act (Bill 23) — a per-unit saving on the ADU. Confirmed in Phase 2. (Ontario Bill 23.)</td></tr>
    <tr><td>Fed + Prov</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td><strong>Opens at four or more self-contained rental units.</strong> Full rebate of the 5% federal GST on new purpose-built rental (4+ units, 90%+ long-term rental, construction start before 2031); Ontario mirrors it with a rebate of the 8% provincial HST component. Applies to the recommended four-unit multiplex if built as rental. (Federal PBRH rebate; Ontario provincial component.)</td></tr>
    <!-- GATED_GRANTS_ROWS: injected per config/programs.json after gate check (Toronto, Ontario; up to 4+1 as-of-right). MHRTC omitted (occupant gate unconfirmable -> silent). -->'''))

# --- summary: current zoning review -----------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) &mdash; one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right &mdash; no rezoning, no public hearing, no Council approval required.</li>
  </ul>'''.replace('&mdash;','—'),
'''  <p>1216 Islington Avenue is an RD lot in Ward 3 (Etobicoke-Lakeshore). Under Toronto's city-wide multiplex rules, up to <strong>four units are permitted as-of-right in a residential zone</strong> (By-law 0473/0474, May 2023), plus one detached garden suite — five units in total, with no rezoning required. That as-of-right multiplex is a strong, low-risk starting point.</p>
  <ul>
    <li><strong>The As-of-Right Multiplex Advantage:</strong> up to four units plus a garden suite (five total) with no rezoning, no public hearing, and no Council approval — the fastest path to income on this lot.</li>
    <li><strong>The Major Streets Upside:</strong> because the property fronts Islington Avenue, a major arterial, additional height and units may be achievable under Toronto's Major Streets policy or through a rezoning — the route toward your 10-unit goal, assessed in Phase 2. This is upside, not a guarantee.</li>
  </ul>'''))

# ----------------------------------------------------------------- apply
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# ----------------------------------------------------------------- leftover check
print("\n--- leftover check (must all be 0) ---")
for t in ["303 Coxwell", "Coxwell", "John Arockiaraj", "johneeraj", "654-2025",
          "Ward 19", "Beaches", "6+1", "6-unit", "sixplex", "Six-unit",
          "Woodbine", "474-2023", "M4L 3B5"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("\ndone, fails:", fails, "| out:", OUT)
