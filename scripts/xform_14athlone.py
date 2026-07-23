"""
xform_14athlone.py — transform the House Lyft master (303 Coxwell, Toronto)
into the report for 14 Athlone Road, Cambridge, ON (Scott Burvill).

Cambridge has NO city adapter in the zoning engine, so its rules were
researched live from official/verified sources (City of Cambridge Zoning
By-law Review, CambridgeToday, Ontario Bill 23). This report is therefore
tagged report-needs-review: figures must be double-checked before the call.

Scope: the lead's project-type field is "Multiplex Development"
(config/programs.json -> class_only, class_min_units 3, render TIERED,
lead with multiplex). So the report renders across the as-of-right range,
leads with the multiplex path, and attaches every program to the smallest
tier that clears its gate with the threshold shown. Nothing is scoped to the
smallest option.

Facts held honest:
  - Up to 3 residential units as-of-right today on a serviced residential lot
    (Ontario Bill 23). Cambridge's new form-based Comprehensive Zoning By-law
    (2025) proposes duplex/triplex/fourplex/low-rise apartment in its new R
    zones — in-force status + the lot's specific zone are Phase-2 confirms.
  - Lot ~91 ft x 289 ft per public listing (MLS 40791290) — a large parcel
    with severance/redevelopment upside; stated as "per listing, confirm P2".
  - Toronto-only programs (Bill 185 DC waiver, By-law 654-2025, garden-suite
    by-law) are removed. No Toronto data may survive the leftover check.

Aerials: real, licensed Ontario imagery (OIWMS, (c) King's Printer for
Ontario, Open Government Licence - Ontario) from engine/ontario_provincial.py,
embedded as base64. Lot view ~165 m across, context ~665 m across.
"""
import base64
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRATCH = ("/tmp/claude-0/-home-user-houselyft-report-engine/"
           "f37d939e-a7b9-5c61-992d-1ccfc0d80704/scratchpad")

s = open(os.path.join(ROOT, "templates/report_houselyft_master.html")).read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">14 Athlone Road<span>Cambridge, ON</span></div>'))

# ---- barhead (Property Details) ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">14 Athlone Road, Cambridge, ON&nbsp;&nbsp;N1R 1H8</div>'))

# ---- imagery row: two real licensed aerials, height 148px, overlay captions ----
lot_b64 = base64.b64encode(open(os.path.join(SCRATCH, "lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCRATCH, "ctx.jpg"), "rb").read()).decode()
IMG_CELL = (
    '<div style="flex:1;position:relative;height:148px;border:1px solid var(--line);'
    'overflow:hidden;">'
    '<img src="data:image/jpeg;base64,{b64}" style="width:100%;height:100%;'
    'object-fit:cover;display:block;">'
    '<div style="position:absolute;left:0;right:0;bottom:0;'
    'background:rgba(27,42,74,.74);color:#fff;font-size:7pt;padding:3px 7px;">{cap}</div>'
    '</div>')
new_imgrow = (
    '<div class="imgrow" style="margin-top:0;">\n'
    + IMG_CELL.format(b64=lot_b64, cap="Aerial view — approx. 165 m across") + "\n"
    + IMG_CELL.format(b64=ctx_b64, cap="Neighbourhood context — approx. 665 m across") + "\n"
    + '  </div>')
R.append(('''<div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>''', new_imgrow))
R.append(('<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:2px 0 8px;">Imagery: Ontario Imagery Web Map Service, © King\'s Printer for Ontario. Contains information licensed under the Open Government Licence – Ontario.</div>'))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>14 Athlone Road, Cambridge, ON&nbsp;&nbsp;N1R 1H8</td></tr>
    <tr><td>Name</td><td>Scott Burvill</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development; maximize unit count (per intake)</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>Cambridge (Region of Waterloo)</td></tr>
    <tr><td>Neighbourhood</td><td>North Galt</td></tr>
    <tr><td>Region</td><td>Region of Waterloo</td></tr>
    <tr><td>Property Type</td><td>Detached, 1.5-storey (per public listing)</td></tr>
    <tr><td>Waste Collection</td><td>Region of Waterloo curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Cambridge Zoning By-law (new form-based Comprehensive Zoning By-law in progress, 2025)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>~91 ft × 289 ft (approx. 2,440 m² / ~26,300 sq ft) — per public listing; confirm in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (primary); additional-unit and severance paths as upside</td></tr>'''))

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
    14 Athlone Road sits at the end of a quiet dead-end street in North Galt — an established residential pocket of Cambridge in the Region of Waterloo, on an exceptionally deep and wide lot for the area:
    <ul>
      <li>Quiet, low-traffic street with a large rear yard — well suited to a multi-unit build</li>
      <li>Minutes to the Grand River, its trails, and downtown Galt's shops, cafés, and the Gaslight District</li>
      <li>Steady rental demand from Region of Waterloo employers and post-secondary, including the University of Waterloo School of Architecture in Galt</li>
      <li>Established residential streets — the kind of character stock that rents well and holds value</li>
      <li>Note: any heritage designation and Grand River / GRCA environmental overlays are confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Cambridge Zoning By-law) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning. Cambridge is adopting a new form-based Comprehensive Zoning By-law (2025) that proposes additional missing-middle forms (duplex, triplex, fourplex, low-rise apartment up to four storeys) in its residential zones — the in-force status is confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>A detached dwelling plus up to two additional residential units (an interior suite and/or a detached garden suite) as-of-right today; a small multiplex / low-rise form is subject to the new zoning and the City's site standards. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means" list (zoning) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Detached / Semi-detached Multiplex:</strong> Standalone multi-unit homes — a triplex or fourplex, the core of your multiplex goal</li>
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side or vertically stacked units</li>
      <li><strong>Low-Rise Apartment (up to four storeys):</strong> a small-scale apartment form proposed under Cambridge's new form-based residential zoning</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> an interior secondary suite and/or a detached garden suite can be paired with the main dwelling — the first two additional units are exempt from development charges (Bill 23)</li>'''))

# ---- time-sensitive ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">For a purpose-built rental project of four or more units, Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component, stacking on top of the existing federal GST purpose-built rental rebate. On units valued up to $1M this equates to roughly $80,000 per unit of provincial relief. It is a temporary enhancement — the agreement must be signed between April 1, 2026 and March 31, 2027. Whether your project reaches the four-unit threshold is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">ARU Development-Charge Exemption<br><small>Already in effect</small></div><div class="dx">Under Ontario's Bill 23, the first two additional residential units on a lot are exempt from municipal development charges — a meaningful per-unit saving as you add units on this property. No application is required; confirmed for your specific configuration in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: green box ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for the As-of-Right Build</div>Up to three residential units are permitted as-of-right on this serviced residential lot under Ontario\'s Bill 23 — no rezoning. A larger multiplex may also be as-of-right under Cambridge\'s new form-based residential zoning; that is confirmed in Phase 2.</div>'))

# ---- rezoning: comparison table ----
R.append(('''    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><td>Change to the zoning by-law</td><td class="g">None required (up to 3 units)</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">Bill 23 / Cambridge Zoning By-law</td><td class="n">A new site-specific by-law</td></tr>'''))

# ---- rezoning: twocard ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Three units as-of-right</div>A serviced residential lot in Ontario supports up to three residential units under Bill 23 — the main dwelling plus two additional units — without rezoning.</div>
    <div class="card2"><div class="ct">Detached garden suite</div>An additional residential unit as a detached garden suite is a permitted form under the provincial framework and Cambridge\'s site standards, confirmed in Phase 2.</div>'''))

# ---- rezoning: "what this means" barhead + paragraph + amber ----
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 14 Athlone Road</div>'))
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <p>The three-unit build advances directly to design and permitting — no rezoning is contemplated for that path. Reaching the larger multiplex you are after depends on the specific zone applied to this lot under Cambridge's new form-based Comprehensive Zoning By-law: where that zoning permits a fourplex or low-rise form as-of-right, the larger build also avoids rezoning; where it does not, a minor variance or site-specific amendment may apply. This assessment reflects the rules understood to be in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2: the lot's specific zone under the new by-law, and the status of the existing mid-construction dwelling.</b><br><span class="sub">These set the exact unit ceiling and whether any existing work needs a permit before financing or development can proceed. Because Cambridge rules were researched live for this report, verify the zone and incentive figures before the call.</span></div>'''))

# ---- development options A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Three-Unit Build (as-of-right today)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">The main dwelling plus up to two additional residential units — for example an interior secondary suite together with a detached garden suite in the deep rear yard, or a conversion to a triplex. Three units total, fully as-of-right under Ontario's Bill 23 on this serviced residential lot; no rezoning. The first two additional units are exempt from development charges, and additional parking is not required for them. This is the immediate, lowest-friction path and a solid foundation for the larger multiplex options below. The exact unit sizes and siting follow Cambridge's site standards, confirmed in Phase 2.</div>'''))

# ---- development options B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small Multiplex / Fourplex (your goal) — Lead Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A purpose-built small multiplex — a fourplex or a low-rise form of up to four storeys — the multiplex configuration you are after. Cambridge's new form-based Comprehensive Zoning By-law (2025) proposes these missing-middle forms as-of-right in its residential zones; the wide, deep lot at 14 Athlone Road is a strong physical fit. Whether it is fully as-of-right depends on the specific zone applied to the lot under the new by-law — confirmed in Phase 2, with a minor variance or site-specific amendment as the fallback. At four or more self-contained rental units the project reaches the federal GST purpose-built rental rebate (and Ontario's mirrored provincial rebate) threshold.</div>'''))

# ---- development options C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Lot Severance / Larger Redevelopment (widest upside)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">The exceptional lot depth (~289 ft per the public listing) may support a plan of severance or a larger multi-unit redevelopment of the whole parcel — the widest-upside path. This route follows the City's consent/severance and site-plan process and is scoped in Phase 2 once the lot's dimensions, servicing, and applicable zone are confirmed. At five or more rental units, CMHC's MLI Select insured financing and the Apartment Construction Loan Program become available — a materially better cost of capital for a purpose-built rental build.</div>'''))

# ---- development goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex Development</div>
  <p>14 Athlone Road is a large serviced residential lot in North Galt, Cambridge. Up to three residential units are permitted as-of-right today under Ontario's Bill 23; the lot's exceptional size and Cambridge's new form-based residential zoning open a path to a small multiplex — a fourplex or low-rise form. <strong>The multiplex path is the lead recommendation</strong>, with the three-unit build as the immediate as-of-right foundation and a lot severance as the widest-upside option. The exact unit count is set by the lot's specific zone and site conditions, confirmed in Phase 2.</p>'''))

# ---- grants table: inject Cambridge/Ontario tiered programs (replace the empty marker) ----
GRANTS_MARKER = '''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->
    </table>'''
GRANTS_ROWS = '''    <tr><td>Provincial</td><td>ARU Development-Charge Exemption (Bill 23)</td><td>The first two additional residential units on the lot are exempt from municipal development charges (Ontario, Bill 23). Applies as you add units on this property; confirmed for your configuration in Phase 2.</td></tr>
    <tr><td>Regional</td><td>Region of Waterloo — Affordable ARU Funding (Ontario Renovates)</td><td>Forgivable loans reported up to $25,000 for additional residential units rented at affordable rates (roughly a 15-year term). Budget-limited and periodically open/closed — current availability confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td><strong>At 4+ self-contained rental units</strong> (90%+ long-term rental, construction started before 2031): full rebate of the 5% federal GST, with Ontario's 8% provincial HST component mirroring it under the 2026 Budget enhancement (agreements signed April 1, 2026 – March 31, 2027).</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental. <strong>Attaches to a larger project (minimum $1M loan)</strong> — confirmed against the Phase-2 budget.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred insured financing for purpose-built rental. <strong>Threshold: 5 or more rental units.</strong> Can bridge into permanent financing at completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>Brings modular/prefab construction into the MLI Select framework (expanded May 2026); carries the same 5-unit minimum. May shorten construction timelines.</td></tr>
    </table>'''
R.append((GRANTS_MARKER, GRANTS_ROWS))

# ---- summary: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>14 Athlone Road confirms a strong development option. It is a large serviced residential lot in North Galt, Cambridge. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> today — no rezoning required, subject to the City's site standards. Cambridge's new form-based Comprehensive Zoning By-law (2025) proposes fourplex and low-rise apartment forms in its residential zones, and the lot's size supports a small multiplex or a severance — the path you're after.</p>
  <ul>
    <li><strong>The Multiplex Path:</strong> the three-unit build is the immediate as-of-right foundation; a fourplex or low-rise form is the lead recommendation, subject to the lot's specific zone under the new by-law; a lot severance is the widest-upside option. Cambridge's rules were researched live for this report — verify the zone and incentive figures in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(ROOT, "templates/report_14athlone_cambridge.html")
open(out, "w").write(s)

# leftover check — no source-city / wrong-city / master-lead references may survive
LEFTOVERS = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
             "johneeraj", "654-2025", "474-2023", "Bill 185", "569-2013",
             "6+1", "4+1", "garage", "TTC", "auto-generated"]
for t in LEFTOVERS:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done, fails: {fails}, bytes: {len(s)} -> {out}")
