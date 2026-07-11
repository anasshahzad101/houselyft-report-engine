# xform_edmonton.py — build the Edmonton (RS zone) report from the master.
# Property: 6904 - 149 Avenue NW, Edmonton, AB (contact: Ty Ho)
# Zone RS (Small Scale Residential), Edmonton Zoning Bylaw 20001. Facts sourced
# from engine/property_lookup_v2.py Edmonton adapter (live, verified 2026-07-11)
# and corroborated against City of Edmonton published RS-zone guidance.
# Doctrine: assert every swap hits exactly once, keep House Lyft prose verbatim,
# grep for any wrong-city / master-property leftovers before writing.
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_edmonton.html")

s = open(SRC).read()
R = []

# --- Cover -------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">6904 &ndash; 149 Avenue NW<span>Edmonton, AB</span></div>'))

# --- 1. Property Details -----------------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">6904 &ndash; 149 Avenue NW, Edmonton, AB&nbsp;&nbsp;T5C 2V3</div>'))

# Imagery: Edmonton aerial coverage is a licensed-third-party (Pictometry) GAP —
# excluded per doctrine; state the source honestly instead of a generic placeholder.
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(prepared in feasibility phase)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(prepared in feasibility phase)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: the City of Edmonton's aerial coverage is supplied under a third-party licence (Pictometry) that does not permit reproduction here; site imagery is prepared during the feasibility phase.</div>'''))

R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>6904 &ndash; 149 Avenue NW, Edmonton, AB&nbsp;&nbsp;T5C 2V3</td></tr>
    <tr><td>Name</td><td>Ty Ho</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Secondary (basement) suite; explore small-scale multi-unit under the RS zone</td></tr>'''))

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
'''    <tr><td>Municipality</td><td>City of Edmonton</td></tr>
    <tr><td>Neighbourhood</td><td>Kilkenny</td></tr>
    <tr><td>Ward</td><td>tastawiyiniwak Ward (Councillor Karen Principe)</td></tr>
    <tr><td>Community League</td><td>Kilkenny Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Edmonton for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — as-of-right unit count depends on lot area and corner/mid-block status</td></tr>
    <tr><td>Development Goals</td><td>Secondary (basement) suite (primary interest); small-scale multi-unit under RS (alternative)</td></tr>'''))

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
    6904 &ndash; 149 Avenue NW is in Kilkenny, an established residential neighbourhood in Edmonton's north end:
    <ul>
      <li>Located in the City's far north, within the Northern Mature Area district</li>
      <li>Predominantly single-detached homes, with low-rise apartment buildings and row housing already part of the fabric</li>
      <li>Well served by local schools — the neighbourhood is home to several, along with a sports and recreation complex</li>
      <li>Served by Edmonton Transit Service (ETS); the Kilkenny Community League anchors local amenities</li>
      <li>Illustrative context only, not a valuation. Distances, services, and transit are confirmed in the feasibility phase.</li>
    </ul>'''))

# --- 2. Current Zoning -------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone permits single-detached, semi-detached, row and multi-unit housing, plus backyard housing, on serviced residential lots. The as-of-right unit ceiling scales with lot area — each dwelling requires a minimum site area — and is confirmed against your lot in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024) consolidated the former RF1–RF4 zones into RS and permits multi-unit housing by default. A 2025 one-year-review amendment set the mid-block maximum at up to 6 dwellings, with up to 8 permitted on corner sites. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-unit housing types — the RS zone permits up to <strong>6 dwellings mid-block as-of-right</strong> (up to 8 on a corner site), including backyard housing, subject to lot area and technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing &amp; Multi-Unit Housing:</strong> Attached and small-scale multi-unit homes permitted by default in the RS zone</li>
      <li><strong>Single- &amp; Semi-Detached Housing:</strong> Standard forms, which can be paired with additional dwellings on the site</li>
      <li><strong>Backyard Housing:</strong> A self-contained home in the rear yard — permitted in RS and counted toward the site's total dwelling number</li>
      <li><strong>Secondary (Basement) Suite:</strong> An internal suite within the main dwelling — the lowest-complexity way to add a legal rental unit, and the option you flagged at intake</li>'''))

# --- Time-Sensitive ----------------------------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Edmonton RS Height Cut-Off — Act Before Aug 1, 2026<br><small>time-sensitive</small></div><div class="dx">The RS zone's maximum height drops from 10.5 m to 9.5 m for development permit applications approved on or after August 1, 2026 (City of Edmonton, approved April 27, 2026). Filing a complete application before the cut-off preserves the taller 10.5 m building envelope. Confirm timing in Phase 2.</div></div>
    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% rebate of the 5% GST on new purpose-built rental housing (projects of 4+ units, 90%+ long-term rental) applies in Alberta. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this. Confirm eligibility in Phase 2.</div></div>
    <div class="d"><div class="dt">Design Rules to Note &amp; CMHC</div><div class="dx">Since July 8, 2025, at most two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side (City of Edmonton). CMHC financing policy can change at any time — applying early reduces risk.</div></div>'''))

# --- 3. Rezoning -------------------------------------------------------------
R.append(('''  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-green"><div class="ct2">Not Required for This Property</div>Both a secondary (basement) suite and small-scale multi-unit housing are permitted uses in the RS zone under Edmonton Zoning Bylaw 20001 — no rezoning is required.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the Zoning Bylaw</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing at City Council</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Neighbour appeal exposure (SDAB)</td><td class="g">Limited — permitted use</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS)</td><td class="n">A rezoning to a different zone</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Small-scale multi-unit</div>The RS zone permits up to 6 dwellings mid-block as-of-right (up to 8 on a corner site), subject to lot area — no rezoning required.</div>
    <div class="card2"><div class="ct">Backyard housing</div>Edmonton permits a self-contained home in the rear yard in the RS zone; it counts toward the site's total dwelling number.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 6904 &ndash; 149 Avenue NW</div>
  <p>Because the RS zone already permits both a secondary suite and small-scale multi-unit housing under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to development and building permits. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2.</b><br><span class="sub">First, the lot's area and whether it is a corner or mid-block site — this sets the as-of-right dwelling ceiling. Second, the RS height cut-off: applications approved on or after Aug 1, 2026 are limited to 9.5 m rather than 10.5 m.</span></div>'''))

# --- 4. Development Options --------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Secondary (Basement) Suite — Lowest Complexity</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Keep the existing house and add a self-contained secondary suite within the main dwelling — most commonly a basement suite. This is the option you flagged at intake and the fastest, lowest-cost route to a legal rental unit. Secondary suites are a permitted use in the RS zone; a Development Permit and Building Permit are required, and the suite must meet the Alberta Building Code (egress, ceiling height, fire separation, smoke/CO alarms). Suite size and layout are confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small-Scale Multi-Unit (up to 6 dwellings)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The RS zone permits multi-unit housing by default — up to 6 dwellings mid-block as-of-right (and up to 8 on a corner site), subject to a minimum site area per dwelling. This is the highest-density, strongest-income direction without rezoning. The exact ceiling for this lot depends on its area and corner/mid-block status, confirmed as the first gating step in Phase 2. Backyard housing can form part of the unit count. The building envelope is governed by height (10.5 m, dropping to 9.5 m for applications approved on or after Aug 1, 2026), setbacks and lot coverage.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Backyard Housing (garden suite)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A self-contained home in the rear yard — permitted in the RS zone and counted toward the site's total dwelling number. Backyard housing may take a single-detached, semi-detached or multi-unit form, and can be combined with a secondary suite in the main house. Note the July 8, 2025 rule: at most two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side. Siting and size are confirmed in Phase 2.</div>'''))

# --- 5. Development Goal Summary ---------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Recommended Path</div>
  <p>6904 &ndash; 149 Avenue NW is an RS (Small Scale Residential) lot under Edmonton Zoning Bylaw 20001, which permits both a secondary suite and small-scale multi-unit housing as-of-right. <strong>A secondary (basement) suite is the recommended first step</strong> — it matches your stated interest and is the fastest route to rental income — while the RS zone leaves the door open to small-scale multi-unit (up to 6 dwellings mid-block) should you choose to go further. The exact multi-unit ceiling is confirmed against your lot in Phase 2.</p>'''))

# --- 7. Available Grants & Incentives ---------------------------------------
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must generally begin before 2031. Applies in Alberta. Confirmed in Phase 2. (Government of Canada / CRA.)</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Government-backed multi-unit mortgage insurance for 5+ rental units — reduced premiums and extended amortization on a points system rewarding affordability, energy efficiency and accessibility. National program. Confirmed in Phase 2. (CMHC.)</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction loans for purpose-built rental (minimum $1M loan), able to bridge into MLI Select permanent financing at completion. National program. Confirmed in Phase 2. (CMHC.)</td></tr>
    <tr><td>Provincial / Municipal</td><td>Alberta &amp; City of Edmonton incentives</td><td>Provincial and municipal secondary-suite and infill incentive programs change frequently and are not the Ontario or Calgary programs. Any applicable Government of Alberta or City of Edmonton program is verified against its current, official terms in Phase 2 before it is relied upon. No provincial or municipal grant is assumed in this analysis.</td></tr>'''))

# --- 8. Summary (Current Zoning Review only; grants/financing prose kept) -----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>6904 &ndash; 149 Avenue NW is an RS (Small Scale Residential) lot under Edmonton Zoning Bylaw 20001. The zone permits a secondary (basement) suite and small-scale multi-unit housing — up to <strong>6 dwellings mid-block as-of-right</strong> (up to 8 on a corner site) — with no rezoning required. The exact multi-unit ceiling depends on lot area and corner/mid-block status, confirmed in Phase 2.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> both a basement suite and small-scale multi-unit are permitted uses in the RS zone — no rezoning, no public hearing, no Council approval required. Note the time-sensitive RS height cut-off: applications approved on or after Aug 1, 2026 are limited to 9.5 m rather than 10.5 m.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# Leftover guard — nothing from the master property or a wrong city may survive.
LEFT = ["Coxwell", "Toronto", "Ontario", "Ward 19", "Beaches", "John Arockiaraj",
        "johneeraj", "647", "654-2025", "474-2023", "569-2013", "Bill 185",
        "HST", "OLT", "Woodbine", "Danforth", "TTC", "Greenwood", "Calgary",
        "M4L", "6+1", "4+1", "houseplex", "Garden Suite By-law"]
for t in LEFT:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails, "->", OUT)
