"""
xform_scarborough.py — build the House Lyft report for
Abubakar "Abu" Jaffer, 32 Beran Drive, Scarborough (City of Toronto), ON.

Follows the assert-once xform pattern: every replacement must match the master
EXACTLY once, then a leftover scan proves no source-city (Coxwell/Ward 19/6-unit)
or gated-out program content survives.

KEY FACTS (engine/property_lookup_v2 + config/programs.json):
  City ............ Toronto (Scarborough)
  Ward ............ 24 — Scarborough-Guildwood  (NOT a six-unit ward)
  Zone ............ RD (x426), exception 900.3.10(426), ZBL 569-2013
  As-of-right ..... up to 4 residential units (Toronto multiplex permissions)
                    + 1 garden suite (Garden Suite By-law, Feb 2022)
  Homeowner scope . Garden Suite / ADU  -> units_added = 1  -> SCOPED mode
  Programs (gate on 1 unit):
    render : Bill 23 ARU DC exemption (ON, first 2 ARUs) ; Toronto DC waiver
             (Bill 185, <=6 units)
    move   : GST/HST PBRH (4+) and CMHC MLI Select (5+) -> conditional, inside
             the multiplex-upside option only, with the threshold shown
    drop   : ACLP ($1M+, silent), MHRTC (occupant unconfirmed, silent),
             Prefab Plus, Simcoe, Mississauga, all AB/Edmonton
"""
import os, base64

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
SCR = os.environ.get("HL_SCRATCH", "")

src_master = os.path.join(TPL, "report_houselyft_master.html")
out_html   = os.path.join(TPL, "report_scarborough.html")
s = open(src_master).read()

# ---- aerial images (base64 data URIs) --------------------------------------
lot_b64 = base64.b64encode(open(os.path.join(SCR, "aerial_lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCR, "aerial_ctx.jpg"), "rb").read()).decode()

R = []

# ---- cover -----------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">32 Beran Drive<span>Scarborough (Toronto), ON</span></div>'))

# ---- property barhead ------------------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">32 Beran Drive, Scarborough (Toronto), ON&nbsp;&nbsp;M1G 1G1</div>'))

# ---- imagery row (real Toronto 2025 aerials) -------------------------------
old_img = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_img = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{lot_b64}" style="width:100%;height:148px;object-fit:cover;display:block;" alt="Aerial view of 32 Beran Drive">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7.2pt;padding:3px 7px;">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{ctx_b64}" style="width:100%;height:148px;object-fit:cover;display:block;" alt="Neighbourhood context around 32 Beran Drive">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7.2pt;padding:3px 7px;">Neighbourhood context — approx. 240 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:2px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''
R.append((old_img, new_img))

# ---- property table 1 (owner block) ----------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>32 Beran Drive, Scarborough (Toronto), ON&nbsp;&nbsp;M1G 1G1</td></tr>
    <tr><td>Name</td><td>Abubakar &ldquo;Abu&rdquo; Jaffer</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU) — &ldquo;a lot of space around which can be utilized for an extra source&rdquo;; intends to keep the property</td></tr>'''))

# ---- property table 2 (municipal block) ------------------------------------
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
'''    <tr><td>Municipality</td><td>City of Toronto (Scarborough)</td></tr>
    <tr><td>Neighbourhood</td><td>Golfdale-Cedarbrae-Woburn</td></tr>
    <tr><td>Ward</td><td>Ward 24 — Scarborough-Guildwood</td></tr>
    <tr><td>Community League</td><td>Scarborough-Guildwood</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — detached lot with a large rear yard (per aerial &amp; intake)</td></tr>
    <tr><td>Development Goals</td><td>Detached garden suite (ADU); optional interior/multiplex path as upside</td></tr>'''))

# ---- neighbourhood spotlight -----------------------------------------------
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
    32 Beran Drive is in the Golfdale-Cedarbrae-Woburn area of Scarborough — an established, quiet residential pocket of detached homes on generous lots in Toronto's east end:
    <ul>
      <li>Settled single-family streets with mature trees and deep rear yards — the kind of lot that suits a detached garden suite</li>
      <li>Close to Cedarbrae Mall, Scarborough Golf Club, and the Highland Creek / Bellamy ravine greenspaces</li>
      <li>TTC bus service connects the area to Scarborough Centre and the subway network</li>
      <li>Quick access to Markham Road and Ellesmere Road corridors</li>
      <li>Steady east-end rental demand from families and area employers (illustrative context, not a valuation)</li>
    </ul>'''))

# ---- zoning table ----------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD (x426) — Residential Detached, exception 900.3.10(426) (Toronto Zoning By-law 569-2013, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. A detached garden suite (ancillary residential unit) is permitted as-of-right on this residential lot, subject to Toronto's garden-suite standards — setbacks, height, angular planes, and separation distances — confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Up to <strong>4 residential units</strong> are permitted as-of-right city-wide under Toronto's multiplex permissions (2023). A rear <strong>garden suite</strong> is separately permitted as-of-right under Toronto's Garden Suite By-law (February 2022). No rezoning is required for either.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone permits a detached / semi-detached dwelling, a multiplex of up to four units, and a rear garden suite, subject to technical review of site conditions. <em>Note:</em> Ward 24 (Scarborough-Guildwood) is <strong>not</strong> among the wards where six units are permitted as-of-right; the as-of-right main-building ceiling here is four units.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — a detached garden suite is permitted as-of-right; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list ----------------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached Garden Suite:</strong> a self-contained home in your rear yard — your primary goal, permitted as-of-right on this lot</li>
      <li><strong>Interior Secondary Suite:</strong> a unit within the existing home (e.g. a basement apartment), which can be paired with the garden suite</li>
      <li><strong>Detached Houseplex (up to 4 units):</strong> the main building may be developed as a multiplex of up to four units as-of-right city-wide — an optional larger path</li>
      <li><strong>No parking minimums:</strong> Toronto has required no parking spaces for these residential forms city-wide since February 2022</li>'''))

# ---- time-sensitive block --------------------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Development-Charge Exemption — In Effect</div><div class="dx">Under Ontario's Bill 23 (More Homes Built Faster Act), the first two additional residential units on a serviced residential lot are exempt from municipal development charges. A detached garden suite qualifies — a meaningful per-unit saving, applied automatically with no application. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Toronto DC Waiver — If You Scale Up</div><div class="dx">Separately, the City of Toronto waives development charges for multiplexes of up to six units (Bill 185, January 2025). This is relevant only if you later choose the larger multiplex path; a single garden suite is already covered by the Bill 23 exemption above.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit any application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: green callout ----------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A detached garden suite is permitted as-of-right on this residential lot under Toronto\'s Garden Suite By-law — no rezoning required.</div>'))

# ---- rezoning: comparison table governs-your-build row ---------------------
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Existing zoning (ZBL 569-2013) + Garden Suite By-law</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: "also permitted" two cards ----------------------------------
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Detached multiplex (up to 4 units)</div>Toronto's multiplex permissions (2023) allow the main building to be developed as up to four residential units as-of-right city-wide — an optional larger path beyond the garden suite.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones — this is your primary goal.</div>'''))

# ---- rezoning: "what this means" heading + para ----------------------------
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 32 Beran Drive</div>'))
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <p>Because 32 Beran Drive already permits a detached garden suite under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# ---- rezoning: amber note (garage -> garden-suite fit) ---------------------
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the rear-yard envelope for the garden suite.</b><br><span class="sub">Garden-suite size and siting are governed by setbacks, height, angular planes and separation from the main house. The large rear yard is a strong starting point; the exact buildable envelope is confirmed in Phase 2.</span></div>'))

# ---- development options ---------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached Garden Suite (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained detached suite in your rear yard, rented for ongoing income while you keep the property — your stated goal. Permitted as-of-right under Toronto's Garden Suite By-law (February 2022); no rezoning required. Size and siting are set by the City's garden-suite standards — setbacks, height, angular planes and separation from the main house — confirmed in Phase 2. The large rear yard visible in the aerial above is typically a strong fit for this form. As one of the first two additional units on the lot, the suite is exempt from development charges under Bill 23. No parking space is required.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Garden Suite + Interior Secondary Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the backyard garden suite with an interior secondary suite in the existing home (for example, a basement apartment) — a route to additional income units on the lot, subject to Toronto's standards. Both of the first two additional units are exempt from development charges under Bill 23. This maximizes cash flow while keeping the property in your hands. Eligibility and unit sizes are confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Multiplex Upside (optional larger path)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">If you later decide to build beyond a single suite, the main building may be developed as a multiplex of up to four units as-of-right city-wide — no rezoning required. Scale is where the larger incentive programs begin to open up: <em>if you build to four or more self-contained rental units, the federal GST/HST Purpose-Built Rental Housing rebate becomes available</em>, and <em>at five or more rental units, CMHC MLI Select financing can be considered</em> (a four-unit multiplex with a garden suite alongside can reach five — this fifth-unit stacking is confirmed in Phase 2). These are shown as upside tied to that scale; none is claimed for the single garden suite. The Toronto development-charge waiver (Bill 185) covers multiplexes up to six units. Massing, unit mix and feasibility for this path are worked up in Phase 2.</div>'''))

# ---- goal summary ----------------------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Detached Garden Suite (ADU)</div>
  <p>32 Beran Drive is a residential lot in Scarborough (Ward 24 — Scarborough-Guildwood) where a detached garden suite is permitted as-of-right under Toronto's Garden Suite By-law — matching your goal of adding rental income while keeping the property. <strong>The garden suite is the clear primary recommendation</strong>, with an interior secondary suite, and a multiplex of up to four units, as optional larger paths.</p>'''))

# ---- summary: current zoning review ----------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>32 Beran Drive confirms a strong, low-friction development option. On this Scarborough residential lot, a <strong>detached garden suite is permitted as-of-right</strong> under Toronto's Garden Suite By-law — no rezoning, no public hearing, and no Council approval required. The main building may separately be developed as a multiplex of up to four units as-of-right city-wide, should you choose the larger path.</p>
  <ul>
    <li><strong>The Garden-Suite Advantage:</strong> a detached backyard suite adds a rental income stream while you keep the property, using land you already own — the large rear yard is a natural fit, and the exact size and siting are confirmed in Phase 2.</li>
    <li><strong>Development-charge relief built in:</strong> as one of the first two additional units on the lot, the suite is exempt from municipal development charges under Bill 23.</li>
  </ul>'''))

# ---- section 6 GATED_FINANCING_ROWS marker: no scale-gated financing at 1 unit
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <!-- GATED_FINANCING_ROWS: units_added=1 (scoped). No scale-gated financing
         program clears a single garden suite. CMHC MLI Select (5+ units) is
         shown conditionally in Development Option C, not asserted here. -->'''))

# ---- section 7 GATED_GRANTS_ROWS marker: inject programs clearing 1 unit ----
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <!-- GATED_GRANTS_ROWS injected: units_added=1 (scoped), Toronto / Ontario.
         Clears at 1 unit: Bill 23 ARU DC exemption; Toronto DC waiver (<=6).
         Moved to Option C (conditional, threshold shown): GST/HST PBRH (4+),
         CMHC MLI Select (5+). Dropped/silent: ACLP ($1M+), MHRTC (occupant),
         Prefab Plus, Simcoe, Mississauga, all Alberta/Edmonton. -->
    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Ontario's More Homes Built Faster Act (Bill 23) exempts the first two additional residential units on a serviced residential lot from municipal development charges. A detached garden suite qualifies. Applied automatically — no application. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>The City of Toronto waives development charges for multiplexes of up to six units (Bill 185, January 2025). A single garden suite is already covered by the Bill 23 exemption above; this waiver becomes the relevant relief if you develop the main building as a multiplex. No application required for compliant builds.</td></tr>'''))

# ==== apply ================================================================
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# ==== leftover / gate scan =================================================
# Coxwell-master and wrong-ward leftovers must be zero.
banned = ["Coxwell", "John Arockiaraj", "Ward 19", "Beaches-East York", "654-2025",
          "6+1", "6-unit", "six units are permitted", "Woodbine", "johneeraj",
          "$80,000 per unit"]
for t in banned:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        fails += 1

# Gated-out programs must appear ONLY conditionally (Option C), never asserted.
# Bare presence check: MLI Select / PBRH may appear only inside Option C prose.
for prog in ["MLI Select", "Purpose-Built Rental", "PBRH"]:
    print(f"scan '{prog}': {s.count(prog)} (allowed: conditional in Option C only)")
for prog in ["ACLP", "Prefab Plus", "Simcoe", "Secondary Suite Loan", "free grant",
             "guaranteed return"]:
    n = s.count(prog)
    if n:
        print(f"BANNED-PROGRAM '{prog}': {n}")
        fails += 1

open(out_html, "w").write(s)
print(f"\nwrote {out_html}")
print("fails:", fails)
