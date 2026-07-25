"""
xform_barrie.py — build the Barrie lead report from the master.

Barrie has NO zoning-engine adapter, so per THE PRIME RULE the zoning regime
below was researched live from the City's published by-laws (Comprehensive
Zoning By-law 2009-141, amended by By-law 2024-043, April 2024 — up to four
dwelling units as-of-right) and Simcoe County housing programs. This report is
tagged report-needs-review: rules researched live, confirm figures before the
call.

Imagery: real OIWMS (Ontario Imagery Web Map Service, © King's Printer for
Ontario — Open Government Licence Ontario) lot + context aerials injected as
base64 data URIs. Run this AFTER engine/aerial_imagery has produced the crops.

Same pattern as scripts/xform_cambridge.py: every replacement must match the
master exactly once; a leftover check greps for any Toronto/Coxwell residue.
"""
import base64
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_barrie.html")

# --- imagery (produced by engine/aerial_imagery.get_ontario_aerial) ---------
LOT_JPG = sys.argv[1]
CTX_JPG = sys.argv[2]
LOT_ACROSS = sys.argv[3] if len(sys.argv) > 3 else "164"
CTX_ACROSS = sys.argv[4] if len(sys.argv) > 4 else "656"


def datauri(path):
    return "data:image/jpeg;base64," + base64.b64encode(open(path, "rb").read()).decode()


LOT_URI = datauri(LOT_JPG)
CTX_URI = datauri(CTX_JPG)

s = open(SRC).read()
R = []

# ---- cover -----------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">97 John Street<span>Barrie, ON</span></div>'))

# ---- property details barhead ----------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">97 John Street, Barrie, ON&nbsp;&nbsp;L4N 2K6</div>'))

# ---- imagery row + licence (real OIWMS aerials) ----------------------------
old_imgrow = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_imgrow = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid #e4e7ee;">
      <img src="{LOT_URI}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Aerial view of 97 John Street, Barrie">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Aerial view — approx. {LOT_ACROSS} m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid #e4e7ee;">
      <img src="{CTX_URI}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Neighbourhood context, central Barrie">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;">Neighbourhood context — approx. {CTX_ACROSS} m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:4px 0 8px;">Aerial imagery: Ontario Imagery Web Map Service, © King&#39;s Printer for Ontario (Open Government Licence – Ontario).</div>'''
R.append((old_imgrow, new_imgrow))

# ---- property table 1 ------------------------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>97 John Street, Barrie, ON&nbsp;&nbsp;L4N 2K6</td></tr>
    <tr><td>Name</td><td>Javid Ahmad</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Project type: Other — target unit count to be confirmed</td></tr>'''))

# ---- property table 2 ------------------------------------------------------
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
'''    <tr><td>Municipality</td><td>City of Barrie</td></tr>
    <tr><td>Neighbourhood</td><td>Central Barrie — Bradford Street corridor / Allandale area</td></tr>
    <tr><td>County (service area)</td><td>County of Simcoe — housing programs</td></tr>
    <tr><td>Property Type</td><td>Residential (to be confirmed in Phase 2)</td></tr>
    <tr><td>Waste Collection</td><td>City of Barrie curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Barrie Comprehensive Zoning By-law 2009-141 (amended by By-law 2024-043)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Project type "Other" — see Development Goal Summary for the scope question</td></tr>'''))

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
    97 John Street sits in central Barrie, in an established residential area just east of the Bradford Street corridor and north of the historic Allandale neighbourhood — close to both the downtown core and the Kempenfelt Bay waterfront:
    <ul>
      <li>Walking distance to downtown Barrie and the Lakeshore Drive waterfront, trails, and beaches on Kempenfelt Bay</li>
      <li>Near the Bradford Street business district and Centennial Park</li>
      <li>Allandale GO station (Barrie line to Toronto) a short drive south; Barrie Transit routes nearby</li>
      <li>A mature, mixed-age residential neighbourhood — the kind of established stock that rents well and holds value</li>
      <li>Illustrative context only, not a valuation. Local amenities and any overlays are confirmed in Phase 2.</li>
    </ul>'''))

# ---- zoning table ----------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential — City of Barrie Comprehensive Zoning By-law 2009-141 (exact zone category confirmed in Phase 2)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a residentially-zoned, municipally-serviced parcel (City water &amp; sewer). Each additional residential unit requires one on-site parking space and a minimum 1.2 m access path (By-law Section 5.2.9).</td></tr>
    <tr><td>Recent Changes</td><td>In April 2024, By-law 2024-043 amended Zoning By-law 2009-141 to permit up to <strong>four dwelling units</strong> as-of-right on residential lots — one more than the provincial three-unit minimum under Bill 23. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>An interior secondary suite and/or a detached garden suite are permitted alongside the main dwelling, up to four units total, subject to Barrie's site standards (setbacks, height, floor-area cap, parking). Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list ----------------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Interior Secondary Suite:</strong> a self-contained unit within the existing home, such as a basement apartment</li>
      <li><strong>Detached Garden Suite:</strong> a standalone unit in the rear yard on a serviced lot</li>
      <li><strong>Up to Four Units:</strong> under Barrie's By-law 2024-043 the lot may support the main dwelling plus additional units to a total of four, subject to site standards</li>
      <li><strong>Townhouse / Small Multiplex forms</strong> where the lot and zone permit — confirmed in Phase 2</li>'''))

# ---- time-sensitive --------------------------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">County of Simcoe Secondary Suites — Budget-Limited<br><small>first-come, first-served</small></div><div class="dx">The County of Simcoe offers a 15-year forgivable loan reported up to $30,000 to create or legalize a secondary or garden suite, available to property owners in Barrie. Funding is limited and allocated first-come, first-served with priority to projects ready to build — so timing matters. Current availability and the exact amount are confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Under Ontario's Bill 23, the first two additional residential units on your lot are exempt from municipal development charges — a meaningful per-unit saving. Confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: co-green ----------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Up to four units are permitted as-of-right on this residential lot under Barrie\'s Zoning By-law 2009-141, as amended by By-law 2024-043 — no rezoning required.</div>'))

# ---- rezoning: cmp table last row ------------------------------------------
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 2009-141 (amended by 2024-043)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: twocard -----------------------------------------------------
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>Barrie's By-law 2024-043 (amending Zoning By-law 2009-141) permits up to four dwelling units on a residential lot city-wide, without rezoning — one more than the provincial minimum of three.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>A detached garden suite counts among your additional residential units and is permitted as-of-right on a serviced residential lot, subject to Barrie's site standards (Section 5.2.9): setbacks, height, a floor-area cap, and one parking space per unit.</div>'''))

# ---- rezoning: barhead + para + amber --------------------------------------
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 97 John Street</div>'))

R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 97 John Street already permits up to four units under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. Barrie is not yet covered by our automated zoning engine, so the rules in this report were researched from the City\'s published by-laws and should be re-confirmed against the parcel\'s exact zone during Phase 2. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>Two items to confirm early: the parcel\'s exact zone and its servicing.</b><br><span class="sub">Barrie\'s four-unit permission applies to residentially-zoned, municipally-serviced lots; the exact zone category and any site-specific provisions are verified against the City\'s zoning map in Phase 2. Each additional unit also requires one on-site parking space and a 1.2 m access path.</span></div>'))

# ---- development options ---------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Add One Suite (Secondary or Detached Garden Suite)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A single additional residential unit — either an interior secondary suite (for example, a basement apartment) or a detached garden suite in the rear yard. Permitted as-of-right on a serviced residential lot under Barrie's Zoning By-law 2009-141; no rezoning. This is the lowest-cost entry point and the tier the County of Simcoe forgivable-loan program is aimed at. Each additional unit requires one on-site parking space and a 1.2 m access path (Section 5.2.9). The exact size and siting are set by Barrie's ARU standards and confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Up to Three Units (Main Dwelling + Two Additional Units)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The main dwelling plus two additional residential units — for example, an interior secondary suite and a detached garden suite. Permitted as-of-right, and the first two additional units are exempt from municipal development charges under Ontario's Bill 23. This is a strong cash-flow configuration while keeping the property in your hands. Two on-site parking spaces (one per additional unit) and the ARU site standards apply; the buildable envelope is confirmed in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Up to Four Units (Barrie\'s 2024 Fourplex Permission)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Barrie's By-law 2024-043 (April 2024) permits up to four dwelling units on a residential lot — one more than the provincial minimum. Built as a purpose-built rental of four self-contained units, this tier can unlock the federal GST and Ontario HST purpose-built-rental rebates (90%+ long-term rental, construction started before 2031). A four-unit build is more likely to trigger site-plan review and possibly a minor variance depending on the final footprint, and requires four on-site parking spaces. The right tier for you depends on your goals — see the note below.</div>'''))

# ---- development goal summary ----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Choosing Your Configuration</div>
  <p>97 John Street is a residential lot in Barrie where up to <strong>four dwelling units are permitted as-of-right</strong> (Zoning By-law 2009-141, amended by By-law 2024-043) — no rezoning required. Your intake listed the project type as "Other," so rather than assume a target we've laid out the full as-of-right ladder: one added suite, up to three units, or a four-unit build.</p>
  <p><strong>Tell us your target and we'll pinpoint the exact programs and design path:</strong> are you looking to add a single rental suite, maximize cash flow with two or three units, or build a full four-unit rental? Each step up the ladder opens further incentives — the County of Simcoe forgivable loan at the first suite, development-charge exemptions on the first two additional units, and the federal/provincial purpose-built-rental rebates at four rental units.</p>'''))

# ---- summary: current zoning review ----------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>97 John Street is a residential lot in Barrie. Under the City's Zoning By-law 2009-141 — amended in April 2024 by By-law 2024-043 — up to <strong>four dwelling units are permitted as-of-right</strong>, one more than the provincial minimum of three, with no rezoning required (subject to the City's site standards and confirmation of the parcel's exact zone).</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> Barrie is among the Ontario cities that went beyond the provincial three-unit floor, allowing a fourth unit on a residential lot without a rezoning, public hearing, or Council approval — expanding both your cash-flow potential and the incentives you can reach.</li>
  </ul>'''))

# ---- gated financing rows (add ACLP, threshold shown) ----------------------
fin_marker = '''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->'''
fin_new = fin_marker + '''
    <tr><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental, available where the project reaches a minimum $1M loan — for example, a full four-unit rental build. Can bridge into long-term CMHC financing. Eligibility and loan size confirmed in Phase 2.</td></tr>'''
R.append((fin_marker, fin_new))

# ---- gated grants rows (Barrie / Simcoe / federal, thresholds shown) --------
grants_marker = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->'''
grants_new = grants_marker + '''
    <tr><td>Municipal (County)</td><td>County of Simcoe Secondary Suites Program</td><td>15-year forgivable loan reported up to $30,000 to create or legalize a secondary or garden suite; available to Simcoe County property owners including Barrie. Budget-limited and first-come, first-served — current availability and amount confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>ARU Development-Charge Exemption (Bill 23)</td><td>The first two additional residential units are exempt from municipal development charges under Ontario's More Homes Built Faster Act — a meaningful per-unit saving. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal + Provincial</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Applies at the four-unit tier: a purpose-built rental of 4+ self-contained units (90%+ long-term rental, construction started before 2031) earns a 100% rebate of the 5% federal GST, which Ontario mirrors with a 100% rebate of the 8% provincial HST. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where the new unit houses an eligible senior (65+) or disability-tax-credit relative, a 15% credit on up to $50,000 of eligible cost. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes may offset efficient design and equipment on a new suite. Availability confirmed in Phase 2.</td></tr>'''
R.append((grants_marker, grants_new))

# ---- apply -----------------------------------------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# ---- leftover check --------------------------------------------------------
leftovers = 0
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "6+1", "Bill 185", "sixplex", "Six-Unit", "six units", "M4L", "474-2023",
          "Gerrard", "Woodbine", "Greenwood", "TTC", "315.9", "170 ft", "garage",
          "johneeraj", "569-2013", "auto-generated"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        leftovers += 1

print(f"done. replacements: {len(R)}  fails: {fails}  leftover-tokens: {leftovers}")
print("wrote", OUT)
