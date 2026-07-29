"""
xform_edmonton.py — turn the House Lyft master into the Edmonton report for
9115 138 Avenue NW (Reggie P). Same discipline as the other xforms: every
replacement must match exactly once, then a leftover grep proves no Toronto /
Coxwell / Ontario-program text survived.

Grounding packet (verified live 2026-07-29):
  zone            RS (Small Scale Residential), Edmonton Zoning Bylaw 20001
  ward            tastawiyiniwak Ward (Councillor Karen Principe)
  neighbourhood   Northmount  |  Northmount Community League
  units           up to 6 dwellings as-of-right mid-block (8 on corner sites);
                  backyard housing permitted and COUNTS TOWARD the total
  height          10.5 m now -> 9.5 m for applications from Aug 1, 2026
  side entrances  max two facing an interior side lot line; a side-facing
                  entrance triggers a 1.9 m setback (since Jul 8, 2025)
  incentives      NO Ontario-style DC waiver. Alberta no-PST; Edmonton
                  Secondary Suite Incentive (up to $10k, waitlisted 24 Jun 2026);
                  Edmonton IIF (fully allocated); federal GST/HST PBRH (4+),
                  CMHC MLI Select (5+), CMHC ACLP ($1M+ loan).
  source          gis.edmonton.ca ZoningWebApp (live) + ZBL 20001, 2026-07-11

Scope: contact field = "Multiplex Development" -> tiered render, lead multiplex.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates", "report_edmonton.html")
s = open(TPL).read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">9115 138 Avenue NW<span>Edmonton, AB</span></div>'))

# ---- property details barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">9115 138 Avenue NW, Edmonton, AB&nbsp;&nbsp;T5E 2B1</div>'))

# ---- imagery row: Edmonton has NO verified-licence lot-scale source.
#      Remove the empty placeholder boxes; keep one honest line. ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <p style="font-size:8.5pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source for this municipality.</p>'''))

# ---- property table 1 (contact + goals) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>9115 138 Avenue NW, Edmonton, AB&nbsp;&nbsp;T5E 2B1</td></tr>
    <tr><td>Name</td><td>Reggie P</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development; maximize unit count within the as-of-right envelope</td></tr>'''))

# ---- property table 2 (municipal facts) ----
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
'''    <tr><td>Municipality</td><td>Edmonton</td></tr>
    <tr><td>Neighbourhood</td><td>Northmount</td></tr>
    <tr><td>Ward</td><td>tastawiyiniwak Ward (Councillor Karen Principe)</td></tr>
    <tr><td>Community League</td><td>Northmount Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Edmonton for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed (area developed largely late 1960s–early 1970s)</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — mid-block vs. corner status confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development — up to 6 dwellings as-of-right (RS)</td></tr>'''))

# ---- neighbourhood spotlight (uses the City's own neighbourhood profile) ----
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
    9115 138 Avenue NW is in Northmount, an established residential neighbourhood in northeast Edmonton (tastawiyiniwak Ward). The following is drawn from the City of Edmonton's neighbourhood profile (illustrative context, not a valuation):
    <ul>
      <li>Residential land accounts for almost 70% of Northmount</li>
      <li>Most homes were built during the late 1960s and early 1970s</li>
      <li>The dominant existing structure type is the single detached house — the exact stock that RS small-scale rules are designed to intensify</li>
      <li>Residents have access to three schools, community-league facilities, and an auxiliary hospital, as well as North Town Mall</li>
      <li>An above-average share of residents has lived in the neighbourhood five or more years — a stable, established rental catchment</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone consolidated the former RF1–RF4 districts under Zoning Bylaw 20001 (in force Jan 1, 2024). Row and multi-unit ("small scale") housing is permitted by default; standard site rules (height, setbacks, coverage) are confirmed against the lot in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under the one-year-review amendments (2025), the mid-block maximum was reduced from 8 to <strong>6 dwellings</strong>; developments of more than 8 dwellings are limited to corner sites. Since Jul 8, 2025, at most two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side.</td></tr>
    <tr><td>Permitted Uses</td><td>Small-scale multi-unit housing — up to <strong>6 dwellings as-of-right on a mid-block lot</strong> (up to 8 on a corner site), subject to the RS site standards. Backyard housing is permitted and counts toward that total. No rezoning required.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row &amp; Stacked Housing:</strong> Multi-unit attached homes — side-by-side or vertically stacked units on the main structure</li>
      <li><strong>Small-Scale Multi-Unit ("Multiplex"):</strong> Up to 6 dwellings as-of-right on a mid-block RS lot</li>
      <li><strong>Backyard Housing:</strong> A detached rear-yard dwelling is permitted — but note it counts toward the 6-dwelling total, it does not add to it</li>
      <li><strong>Secondary Suites:</strong> Interior suites can form part of the unit mix within the permitted dwelling count</li>'''))

# ---- TIME-SENSITIVE block (Alberta / Edmonton, no Ontario programs) ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">RS Height Cut-Off — File Before Aug 1, 2026</div><div class="dx">Council approved (Apr 27, 2026) a reduction of the RS maximum height from 10.5 m to 9.5 m for applications submitted on or after <strong>August 1, 2026</strong>. Filing a complete development permit application before that date keeps the taller 10.5 m envelope, which can be the difference between a workable third storey and a redesign. Confirm the exact submission requirements with the City in Phase 2.</div></div>
    <div class="d"><div class="dt">Edmonton Secondary Suite Incentive — Waitlisted</div><div class="dx">The City of Edmonton offers up to $10,000 toward a legal internal (secondary) suite, one application per owner. As of June 24, 2026 the program is <strong>waitlisted</strong> — applying now holds a position for a future funding round. Current status and eligibility confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- REZONING: green banner ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A small-scale multiplex of up to 6 dwellings is permitted as-of-right in the RS zone under Edmonton Zoning Bylaw 20001 — no rezoning.</div>'))

# ---- REZONING comparison table ----
R.append(('''    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><td>Change to the zoning bylaw</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing before Council</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure</td><td class="g">Limited (as-of-right permitted use)</td><td class="n">Possible (SDAB / LPRT)</td></tr>
    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS)</td><td class="n">A site-specific rezoning</td></tr>'''))

# ---- REZONING: two "also permitted" cards ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Six-dwelling multiplex</div>The RS zone permits up to six dwellings on a mid-block lot as-of-right under Zoning Bylaw 20001 — no rezoning, no public hearing.</div>
    <div class="card2"><div class="ct">Backyard housing</div>A detached rear-yard dwelling is permitted in RS. Note it counts toward the six-dwelling total on the lot rather than adding a seventh.</div>'''))

# ---- REZONING: "what this means for {addr}" paragraph ----
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <p>Because 9115 138 Avenue NW already permits a small-scale multiplex under the existing RS zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and the development-permit stage. The comparison below shows what that avoids. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# ---- REZONING amber note (was: existing garage permit status) ----
R.append(('''  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-amber"><b>Two items to confirm early: whether this is a mid-block or corner lot, and the Aug 1, 2026 height cut-off.</b><br><span class="sub">Corner status governs whether the ceiling is 6 or 8 dwellings; a complete application filed before Aug 1, 2026 preserves the 10.5 m height envelope. Both are confirmed in Phase 2.</span></div>'''))

# ---- DEVELOPMENT OPTIONS: A (tier — smaller multiplex) ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Four-Dwelling Multiplex</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A small-scale multiplex of four dwellings on the main structure — a conservative tier well inside the RS as-of-right ceiling, giving design flexibility on setbacks and height. As-of-right under Zoning Bylaw 20001; no rezoning. At four or more self-contained rental dwellings the project reaches the federal GST/HST Purpose-Built Rental rebate threshold (confirmed in Phase 2). Site standards — height, setbacks, coverage, and the side-entrance rule — are applied to the lot in Phase 2.</div>'''))

# ---- DEVELOPMENT OPTIONS: B (primary — 6 dwellings) ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Dwelling Multiplex (RS mid-block maximum) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A small-scale multiplex of six dwellings — the RS mid-block maximum and the top of the as-of-right envelope for this lot. This is the configuration that maximizes unit count without a rezoning, matching a Multiplex Development goal. Backyard housing may form part of the six, but does not add a seventh dwelling. At five or more rental dwellings the project also reaches CMHC MLI Select financing (confirmed in Phase 2). If the lot proves to be a corner site, up to eight dwellings may be possible — a question resolved in Phase 2. The side-entrance rule (max two entrances facing an interior side lot line; 1.9 m setback where one does) shapes the final layout.</div>'''))

# ---- DEVELOPMENT OPTIONS: C (backyard / secondary suite note) ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Backyard Housing &amp; Secondary Suites</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Backyard (rear-yard) housing and interior secondary suites are permitted in the RS zone and can be part of the dwelling mix — for example, a smaller main building paired with a backyard dwelling. The key point of accuracy: in Edmonton's RS zone these count toward the six-dwelling total on the lot, they do not stack on top of it as a separate "+1". A legal internal secondary suite may also qualify for the City's Secondary Suite Incentive (up to $10,000; currently waitlisted). Any existing accessory structure's permit status is confirmed in Phase 2.</div>'''))

# ---- 5. DEVELOPMENT GOAL SUMMARY ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Six-Dwelling Multiplex (RS)</div>
  <p>9115 138 Avenue NW is in the RS (Small Scale Residential) zone, where up to six dwellings are permitted as-of-right on a mid-block lot under Zoning Bylaw 20001. <strong>A six-dwelling multiplex is the clear primary recommendation</strong> for a Multiplex Development goal — it maximizes the unit count with no rezoning. A four-dwelling tier is the conservative alternative, and corner-lot status (up to eight dwellings) is confirmed in Phase 2.</p>'''))

# ---- 6. FINANCING: add one gated row (MLI Select, threshold shown) ----
R.append(('''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <!-- GATED_FINANCING_ROWS''',
'''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <tr><td>CMHC MLI Select <small>(at 5+ rental dwellings)</small></td><td>A national CMHC multi-unit mortgage-insurance product offering favourable terms for purpose-built rental. It becomes available at a minimum of five rental dwellings — reached at the six-dwelling tier. Structure and eligibility confirmed in Phase 2.</td></tr>
    <!-- GATED_FINANCING_ROWS'''))

# ---- 7. GRANTS & INCENTIVES table (Alberta/Edmonton + federal, thresholds shown) ----
R.append(('''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <!-- GATED_GRANTS_ROWS''',
'''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>No-PST Advantage (Alberta)</td><td>Alberta levies no provincial sales tax, so construction materials carry only the 5% federal GST rather than a combined rate. Against an HST province this is a real structural saving on the build budget — automatic, with nothing to apply for. The dollar impact scales with the project and is quantified in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Edmonton Secondary Suite Incentive</td><td>Up to $10,000 toward a legal internal secondary suite (one application per owner). Waitlisted as of June 24, 2026 — apply to hold a position for a future round. Edmonton only.</td></tr>
    <tr><td>Municipal</td><td>Edmonton Infill Infrastructure Fund (IIF)</td><td>A HAF-funded program that funds off-site public infrastructure for infill. Currently fully allocated ($39M across 33 projects) — monitor for future rounds. Edmonton only.</td></tr>
    <tr><td>Federal <small>(at 4+ rental dwellings)</small></td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>A 100% rebate of the 5% federal GST on new purpose-built rental projects with four or more self-contained rental units, at least 90% long-term rental, with construction starting before 2031. Applicability confirmed in Phase 2.</td></tr>
    <tr><td>Federal <small>(at 5+ rental dwellings)</small></td><td>CMHC MLI Select</td><td>Multi-unit mortgage-insurance financing with favourable terms for purpose-built rental; minimum five rental units. Reached at the six-dwelling tier. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal <small>($1M+ loan)</small></td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental, at a minimum $1M loan (gated on project budget, established in Phase 2). Can bridge into MLI Select at completion.</td></tr>
    <!-- GATED_GRANTS_ROWS'''))

# ---- 8. SUMMARY: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>9115 138 Avenue NW confirms a strong development option. The property is in the RS (Small Scale Residential) zone under Edmonton Zoning Bylaw 20001, where up to <strong>six dwellings are permitted as-of-right on a mid-block lot</strong> (up to eight on a corner site). No rezoning, no public hearing, and no Council decision are required to build within that envelope.</p>
  <ul>
    <li><strong>The Small-Scale As-of-Right Advantage:</strong> a six-dwelling multiplex is achievable without rezoning — but note two time and site factors: the Aug 1, 2026 height cut-off (10.5 m → 9.5 m for later applications) and whether the lot is mid-block (6) or corner (up to 8). Both are resolved in Phase 2.</li>
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

if fails == 0:
    open(TPL, "w").write(s)

# ================= leftover check =================
print("--- leftover check (must all be zero) ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
          "654-2025", "Bill 185", "Bill 23", "569-2013", "6+1", "4+1",
          "HST Rebate", "OLT", "Garden Suite By-law", "johneeraj", "TTC"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
