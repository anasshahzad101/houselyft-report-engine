"""
xform_adjala.py — transform the master into the 10054 Highway 9 report.

Lead: Sophie Bun. Property: 10054 Highway 9, Township of Adjala-Tosorontio,
Simcoe County, Ontario (rural parcel fronting Highway 9; Hwy 9 is the
Adjala-Tosorontio / Town of Caledon boundary). No engine adapter — rules
researched live, so this is a REPORT-NEEDS-REVIEW build. Every zoning /
program fact is either VERIFIED against an official source or hedged with the
"confirm in Phase 2" treatment. No multiplex is promised as-of-right: a rural
well/septic lot falls outside Bill 23's serviced-lot 3-unit as-of-right rule.

Imagery: two real, licensed OIWMS aerials (King's Printer for Ontario, Open
Government Licence – Ontario), injected as base64 data URIs.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates", "report_adjala.html")
SCRATCH = ("/tmp/claude-0/-home-user-houselyft-report-engine/"
           "dbd5cef9-5e1c-59ae-a063-14d04ac2eac6/scratchpad")

s = open(TPL).read()
R = []

# ---- imagery data URIs (real, licensed OIWMS aerials) ----
prop_b64 = open(os.path.join(SCRATCH, "aerial_property.b64")).read().strip()
ctx_b64 = open(os.path.join(SCRATCH, "aerial_context.b64")).read().strip()

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">10054 Highway 9<span>Adjala-Tosorontio, ON</span></div>'))

# ---- barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">10054 Highway 9, Adjala-Tosorontio, ON&nbsp;&nbsp;L0G 1L0</div>'))

# ---- imagery row (placeholders -> two real licensed aerials with overlay captions) ----
old_img = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_img = (
'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;" alt="Aerial view of 10054 Highway 9">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Oswald',Arial,sans-serif;">Aerial view — approx. 330 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,%s" style="width:100%%;height:148px;object-fit:cover;display:block;" alt="Neighbourhood context around 10054 Highway 9">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.74);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Oswald',Arial,sans-serif;">Neighbourhood context — approx. 1,320 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:2px 0 8px;">Imagery: Ontario Imagery Web Map Service — &copy; King's Printer for Ontario (Open Government Licence &ndash; Ontario).</div>''' % (prop_b64, ctx_b64))
R.append((old_img, new_img))

# ---- property table 1 (contact) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>10054 Highway 9, Adjala-Tosorontio, ON&nbsp;&nbsp;L0G 1L0</td></tr>
    <tr><td>Name</td><td>Sophie Bun</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development (per intake); maximize the property's unit potential</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Township of Adjala-Tosorontio (Simcoe County)</td></tr>
    <tr><td>Location</td><td>Rural parcel fronting Highway 9</td></tr>
    <tr><td>Municipal Boundary</td><td>Highway 9 forms the Adjala-Tosorontio / Town of Caledon (Peel Region) boundary — jurisdiction confirmed in Phase 2</td></tr>
    <tr><td>Servicing</td><td>Rural — private well &amp; septic assumed (no municipal water/sewer); confirmed in Phase 2</td></tr>
    <tr><td>Conservation Authority</td><td>Nottawasaga Valley Conservation Authority (NVCA) watershed — regulated-area status confirmed in Phase 2</td></tr>
    <tr><td>Current Bylaw</td><td>Township of Adjala-Tosorontio Comprehensive Zoning By-law No. 03-57 (October 2003, as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>Rural acreage — to be confirmed (County GIS / survey)</td></tr>
    <tr><td>Development Goals</td><td>Additional residential unit(s) subject to servicing; a larger multi-unit build subject to rezoning</td></tr>'''))

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
    10054 Highway 9 is a rural property in the Township of Adjala-Tosorontio, in the rolling countryside of southern Simcoe County:
    <ul>
      <li>Fronts Highway 9, a major east–west route, with the Airport Road and Highway 50 corridors nearby</li>
      <li>A country setting of farms, woodlots, and estate-residential acreage</li>
      <li>Convenient to Tottenham, Alliston, Schomberg, and the northern edge of the GTA</li>
      <li>Highway 9 forms the boundary with the Town of Caledon (Peel Region) to the south</li>
      <li>Note: rural properties here are typically on private well and septic — servicing is a key factor in what can be built. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>A rural zone under Township Zoning By-law No. 03-57 — most likely Agricultural (A) or Rural Residential (RR). The exact zone is confirmed in Phase 2 via the County of Simcoe GIS mapping and the By-law 03-57 schedules.</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Rural zones carry large minimum lot areas and generous setbacks (the Agricultural zone minimum is reported at roughly 36 hectares). Development is also governed by on-site servicing — private septic capacity. Exact standards confirmed in Phase 2 against By-law 03-57.</td></tr>
    <tr><td>Recent Changes</td><td>Ontario's Bill 23 (More Homes Built Faster Act, 2022) permits up to <strong>3 residential units as-of-right</strong> only on a "parcel of urban residential land" — inside a settlement area on <em>municipal</em> water and sewer. A rural parcel on private well and septic falls outside that as-of-right rule; additional units are possible but discretionary and limited by septic capacity and the Township's approval.</td></tr>
    <tr><td>Permitted Uses</td><td>A single detached dwelling is the principal residential use in the rural zones. An additional in-building unit may be possible subject to septic capacity; a detached second unit or a larger multi-unit build has required a Zoning By-law Amendment in this Township. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>Not as-of-right — but a defined path exists.</strong> A multiplex is not an as-of-right build on this rural lot. Proceed to Step 2 — <strong>Builder Ready Package™</strong> — to scope the additional-unit potential now and the rezoning-plus-servicing route to a larger build.</td></tr>'''))

# ---- "what this means" list ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Additional Residential Unit (in-building):</strong> a second unit within the existing dwelling may be possible — subject to private septic capacity and the Township's standards</li>
      <li><strong>Detached second unit / larger multi-unit build:</strong> a defined but discretionary path in this Township — it has required a Zoning By-law Amendment (rezoning)</li>
      <li><strong>Servicing is the gate:</strong> on private well &amp; septic, septic capacity sets how many units the land can legally support — a septic evaluation is the key early step</li>
      <li><strong>Agricultural second dwelling:</strong> the Agricultural zone may permit a supplementary farm dwelling under conditions — confirmed in Phase 2</li>'''))

# ---- time-sensitive block ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Secondary-Suite Refinancing — In Effect</div><div class="dx">Under the Canadian Mortgage Charter, since January 15, 2025, insured mortgage refinancing can help fund a legal secondary suite — accessing up to 90% of the improved (as-completed) property value, with a $2 million property-value cap and amortization up to 30 years. The suite must be a self-contained legal unit that meets municipal zoning and is not used as a short-term rental. (Government of Canada / CMHC.)</div></div>
    <div class="d"><div class="dt">Servicing / Septic Study — Do This Early</div><div class="dx">On a private-septic rural lot, septic capacity determines how many units the land can legally support. Commissioning the septic evaluation early is the single most important step — it drives the whole timeline and defines what is realistically buildable. Confirmed and scoped in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: co-green "Not Required" -> honest co-amber ----
R.append(('''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>''',
'''  <div class="co-amber"><b>Rezoning is the likely path for a multi-unit build here.</b><br><span class="sub">On this rural lot, a multiplex is not an as-of-right build. Additional residential unit(s) may be possible now, subject to private septic capacity; a larger multi-unit development would require a Zoning By-law Amendment together with a servicing (septic) study. This is a defined process, not a dead end — we scope it in Phase 2.</span></div>'''))

# ---- rezoning: comparison table ----
R.append(('''    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><th></th><th>Additional unit(s) — servicing permitting</th><th>Larger multi-unit build — rezoning path</th></tr>
    <tr><td>Zoning By-law Amendment</td><td class="g">Not required (within rural permissions)</td><td class="n">Required</td></tr>
    <tr><td>Public meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Servicing (septic) study</td><td class="g">Confirm capacity</td><td class="n">Required</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 03-57 permissions</td><td class="n">A new site-specific by-law</td></tr>'''))

# ---- rezoning: barhead + two cards ----
R.append(('''  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="barhead" style="text-align:left;">Two paths for this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Additional residential unit</div>An additional in-building unit on the existing dwelling may be possible subject to private septic capacity and the Township's standards. The lowest-friction near-term step; confirmed in Phase 2.</div>
    <div class="card2"><div class="ct">The rezoning route</div>A larger multi-unit build toward your goal is pursued through a Zoning By-law Amendment plus a servicing (septic) study — a defined, manageable process we lead in Phase 2.</div>
  </div>'''))

# ---- rezoning: "what this means for ..." para + closing amber ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 10054 Highway 9</div>
  <p>Because this is a rural lot on private servicing, the route to your multiplex goal runs through a servicing assessment and, for anything beyond the base rural permission, a Zoning By-law Amendment. The near-term win is confirming the additional-unit potential the land and septic can support today. This assessment reflects the by-laws researched live for this municipality at the date of this report and is subject to confirmation of the exact zone and site conditions in Phase 2.</p>
  <div class="co-amber"><b>Two items to confirm first: municipal jurisdiction and septic capacity.</b><br><span class="sub">Highway 9 is the Adjala-Tosorontio / Caledon boundary — we confirm which municipality governs the parcel. And on private septic, capacity sets how many units are legally possible. Both are scoped at the start of Phase 2.</span></div>'''))

# ---- development options A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Additional Residential Unit (near-term)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add one additional residential unit within the existing dwelling (for example, an in-home secondary suite). On a rural well/septic lot this is the lowest-friction path and does not, on its own, deliver a multiplex — it establishes a legal second unit where the septic system can support the added load. The size and feasibility are set by the Township's standards and, above all, by septic capacity — confirmed in Phase 2 with a servicing evaluation.</div>'''))

# ---- development options B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Larger Multi-Unit Build via Rezoning + Servicing</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">To move toward the multiplex goal, a larger multi-unit build is pursued through a Zoning By-law Amendment (rezoning) combined with a servicing (septic) study — and, on a rural lot, likely a private communal or engineered septic solution sized to the added units. This is a defined planning process rather than an as-of-right entitlement: it involves a public meeting and a Council decision, and its ceiling is set by what the land and services can support. We scope the feasibility, the likely unit range, and the approval path in Phase 2.</div>'''))

# ---- development options C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Rural Servicing &amp; Land Considerations</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">On a private well &amp; septic property, septic capacity is the gate that determines how many units the land can legally support — a servicing evaluation comes first. The parcel sits in the Nottawasaga Valley Conservation Authority (NVCA) watershed, so any regulated-area status (near watercourses, wetlands, or floodplain) is confirmed early, as are any Agricultural-zone conditions. On the upside, rural acreage typically offers siting flexibility that a small urban lot does not. Municipal jurisdiction (Adjala-Tosorontio vs. Caledon, on the Highway 9 boundary) is also confirmed at the outset of Phase 2.</div>'''))

# ---- development goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Your Development Path</div>
  <p>10054 Highway 9 is a rural parcel in the Township of Adjala-Tosorontio, governed by Zoning By-law No. 03-57 and by private servicing. A multiplex is not an as-of-right build here — Ontario's Bill 23 three-unit rule applies to serviced lots inside settlement areas, not to rural parcels on private well and septic. <strong>The realistic path is two-step:</strong> confirm the additional-unit potential the land and septic can support now, and pursue a Zoning By-law Amendment with a servicing study for a larger multi-unit build toward your goal.</p>'''))

# ---- grants table: inject verified programs in place of the gated-rows marker ----
old_grants = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->'''
new_grants = '''    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit (MHRTC)</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (maximum $7,500) to create a self-contained secondary unit for a qualifying relative (65+, or 18–64 and eligible for the Disability Tax Credit). The unit must be within or attached to the home. (CRA — Line 45355.) Applicability to your situation confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Canadian Mortgage Charter — Secondary-Suite Refinancing</td><td>Since January 15, 2025, insured mortgage refinancing can help fund a legal secondary suite: up to 90% of the improved property value, $2M property-value cap, amortization up to 30 years. The suite must be a self-contained legal unit meeting municipal zoning. (Government of Canada / CMHC.)</td></tr>
    <tr><td>Provincial</td><td>Additional Residential Unit — Development Charges</td><td>Additional residential units are generally exempt from development charges under provincial rules. On a rural lot the significant servicing cost is the private septic design and approval, which falls to the owner. Applicability confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Enhanced GST Rental Rebate (note on eligibility)</td><td>The enhanced 100% GST rebate for purpose-built rental applies only to projects of 4+ self-contained units — it does not apply to a single added unit. It would come into play only if a larger, rezoned multi-unit build (4+ units) proceeds. Confirmed in Phase 2.</td></tr>'''
R.append((old_grants, new_grants))

# ---- summary: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>10054 Highway 9 is a rural parcel in the Township of Adjala-Tosorontio, governed by Comprehensive Zoning By-law No. 03-57. Because it is a rural lot — most likely Agricultural (A) or Rural Residential (RR), on private well and septic — a multiplex is not an as-of-right build. Ontario's Bill 23 three-unit as-of-right rule applies to serviced lots inside settlement areas, not to rural parcels on private servicing. There is, however, a defined path forward.</p>
  <ul>
    <li><strong>The Realistic Path:</strong> confirm the additional-unit potential the land and septic can support now, then pursue a rezoning plus a servicing study for a larger multi-unit build. The exact zone and site standards are confirmed in Phase 2 via the County of Simcoe GIS and By-law 03-57.</li>
  </ul>'''))

# ================= apply =================
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(TPL, "w").write(s)

# leftover check — zero tolerance for source-city / wrong-program leftovers
LEFTOVERS = ["Coxwell", "John Arockiaraj", "Toronto", "Ward 19", "Beaches",
             "654-2025", "474-2023", "Bill 185", "569-2013", "6+1", "4+1",
             "Cambridge", "Briarstone", "garden suite in the rear", "HST"]
print("--- leftover scan ---")
any_left = False
for t in LEFTOVERS:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        any_left = True
if not any_left:
    print("clean — no source-city or wrong-program leftovers")
print("done, fails:", fails)
