"""xform_calgary.py — turn the House Lyft master into the Calgary report for
6424 Elbow Drive SW (Laveena Mendonca).

Run from templates/:  python3 ../scripts/xform_calgary.py

Calgary has no working live adapter in this run (City of Calgary Open Data was
unreachable), so the zoning rulebook here was researched live from City of
Calgary / Government of Canada sources and every parcel-specific value that
could not be verified is left as a confirm-phrase. This is a report-needs-review
build by design. House Lyft prose sections are kept verbatim; only property,
zoning, timing, options and money content is swapped.
"""
import re

s = open("report_calgary.html").read()
R = []

# --- cover ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">6424 Elbow Drive SW<span>Calgary, AB</span></div>'))

# --- section 1 barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">6424 Elbow Drive SW, Calgary, AB&nbsp;&nbsp;T2V 1J5</div>'))

# --- imagery row (no licensed Calgary source) -> honest single line ---
img_re = re.compile(
    r'<div class="imgrow" style="margin-top:0;">.*?'
    r'<div class="imglicense"[^>]*>.*?</div>', re.S)
img_new = ('<div class="imglicense" style="font-size:8pt;color:#7a818f;'
           'margin:2px 0 12px;">Aerial and street-level photography pending a '
           'licensed imagery source.</div>')
assert len(img_re.findall(s)) == 1, "imagery block not matched once"
s = img_re.sub(lambda m: img_new, s, count=1)

# --- contact table ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>6424 Elbow Drive SW, Calgary, AB&nbsp;&nbsp;T2V 1J5</td></tr>
    <tr><td>Name</td><td>Laveena Mendonca</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development — maximize unit count</td></tr>'''))

# --- municipal table ---
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
'''    <tr><td>Municipality</td><td>City of Calgary</td></tr>
    <tr><td>Community</td><td>Meadowlark Park (southwest Calgary)</td></tr>
    <tr><td>Current Bylaw</td><td>City of Calgary Land Use Bylaw 1P2007</td></tr>
    <tr><td>Land-Use Designation</td><td>To be confirmed during the feasibility phase (live City parcel data was unavailable at generation)</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Calgary for the local cart schedule</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area and the confirmed designation</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development (subject to Calgary's 2026 zoning transition)</td></tr>'''))

# --- neighbourhood spotlight ---
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
    6424 Elbow Drive SW is in Meadowlark Park, an established residential community in southwest Calgary just west of Chinook Centre and north of Glenmore Trail:
    <ul>
      <li>Fronts Elbow Drive SW, a major north–south corridor with quick access to downtown and the Glenmore reservoir/park system</li>
      <li>Minutes from Chinook Centre, Macleod Trail retail and the Elbow River pathways</li>
      <li>Well served by Calgary Transit; the LRT Red Line (Chinook / Heritage stations) is nearby</li>
      <li>Mature, sought-after inner-city area — the kind of low-density street targeted by Calgary's gentle-density policies</li>
      <li>Note: mature trees, lot grading and setback rules can shape what is buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- section 2 zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>To be confirmed — City of Calgary Land Use Bylaw 1P2007. Most established residential lots carried <strong>R-CG</strong> under the 2024–2026 citywide rezoning; the exact designation for this parcel is confirmed in Phase 2.</td></tr>
    <tr><td>Governing Framework</td><td>Land Use Bylaw 1P2007. Citywide ("blanket") rezoning made R-CG the base district in most established neighbourhoods from August 2024; City Council repealed it on April 8, 2026, effective <strong>August 4, 2026</strong>.</td></tr>
    <tr><td>Recent Changes</td><td>R-CG permitted single/semi-detached, rowhouse and up to 4 units per parcel plus secondary suites (max 75 units/ha); rowhouse became a discretionary use October 9, 2025. On August 4, 2026 most parcels revert to R-C1/R-C2 and the R-CG above-grade ceiling drops from 4 to 3. Researched live — confirm before proceeding.</td></tr>
    <tr><td>Permitted Uses</td><td>Depends on the confirmed designation and the transition date: under R-CG, a rowhouse / up-to-4-unit multiplex plus suites; under R-C1/R-C2 after repeal, a single or two dwellings plus a secondary or backyard suite. A larger multiplex after repeal would need a land use redesignation. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>LIKELY — time-sensitive</strong>; the multiplex path is strongest before August 4, 2026. Proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- section 2 "what this means" list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Rowhouse / Townhouse:</strong> Multi-unit attached homes — a discretionary use in R-CG since October 9, 2025 (confirm current status)</li>
      <li><strong>Up to a 4-Unit Multiplex (under R-CG):</strong> Permitted while this parcel carries R-CG, before the August 4, 2026 repeal — confirmed in Phase 2</li>
      <li><strong>Contextual Single / Semi-Detached:</strong> The base form most lots revert to after the repeal (R-C1 / R-C2)</li>
      <li><strong>Secondary &amp; Backyard Suites:</strong> A secondary (e.g. basement) suite and/or a detached backyard suite can add rental units; Council is considering making both permitted uses citywide (July 21, 2026 hearing)</li>'''))

# --- time-sensitive section ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Blanket Rezoning Repeal — in force soon<br><small>~ 2 weeks from now (Aug 4, 2026)</small></div><div class="dx">City Council voted on April 8, 2026 to repeal the citywide rezoning; it takes effect August 4, 2026. On that date most established residential lots revert from R-CG to R-C1/R-C2, and R-CG's above-grade unit ceiling drops from 4 to 3. To keep R-CG multi-unit rights, a project generally needs an approved development permit, building permit or subdivision before the deadline. Confirming this parcel's status is the first step.</div></div>
    <div class="d"><div class="dt">Suite Bylaw Public Hearing<br><small>today — July 21, 2026</small></div><div class="dx">Council is considering amendments to make secondary suites and backyard suites permitted (rather than discretionary) uses in all low-density residential districts. The outcome shapes the fastest suite route on this lot and is confirmed against the adopted bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Secondary Suite Incentive Program — waitlisted<br><small>as of June 24, 2026</small></div><div class="dx">The City of Calgary's Secondary Suite Incentive Program has offered up to $10,000 toward a safe, registered secondary suite. As of June 24, 2026 new applications are placed on a waitlist and funding may not be available. This is a government-backed option to explore, not a guarantee — status confirmed in Phase 2.</div></div>'''))

# --- section 3 rezoning: replace the whole co-green -> co-amber body ---
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
'''  <div class="co-amber"><div class="ct2" style="font-family:'Oswald';font-weight:600;color:#a4761c;font-size:11pt;margin-bottom:4px;">A time-sensitive, two-window situation</div>Calgary is mid-transition. The citywide ("blanket") rezoning that made <strong>R-CG</strong> the base district in most established neighbourhoods was <strong>repealed by City Council on April 8, 2026</strong>, effective <strong>August 4, 2026</strong>. Whether a multi-unit build on this lot is as-of-right or needs a rezoning depends on this parcel's current designation and on which side of that date the application lands — both confirmed in Phase 2.</div>
  <div class="barhead" style="text-align:left;">Two windows — before vs. after August 4, 2026</div>
  <table class="cmp">
    <tr><th></th><th>Before Aug 4, 2026 (current)</th><th>After Aug 4, 2026 (repeal in force)</th></tr>
    <tr><td>Base district in most established areas</td><td class="g">R-CG (grade-oriented)</td><td class="n">Reverts to R-C1 / R-C2</td></tr>
    <tr><td>Multi-unit as-of-right</td><td class="g">Up to 4 units / rowhouse under R-CG*</td><td class="n">Single or two dwellings + suite pathway</td></tr>
    <tr><td>R-CG above-grade unit ceiling</td><td class="g">4 units</td><td class="n">Drops to 3 (corner context)</td></tr>
    <tr><td>Larger multiplex</td><td class="g">May be as-of-right under R-CG*</td><td class="n">Likely needs a land use redesignation</td></tr>
    <tr><td>How rights are locked in</td><td class="g">Approval before the deadline</td><td class="n">New application under reverted rules</td></tr>
  </table>
  <p style="font-size:8pt;color:#7a818f;margin-top:-8px;">*Subject to confirming that this parcel currently carries R-CG and to Calgary Land Use Bylaw 1P2007. Rowhouse became a discretionary use in R-CG as of October 9, 2025. Researched from City of Calgary sources — verify the exact designation and unit ceiling before proceeding.</p>
  <div class="barhead" style="text-align:left;">What this means for 6424 Elbow Drive SW</div>
  <p>Two independent City of Calgary sources are needed to confirm this parcel's current land-use designation, and live access to them was unavailable when this report was generated — so the exact zoning is <strong>to be confirmed during the feasibility phase</strong>. The transition itself, however, is certain: the window to secure R-CG multi-unit rights closes on August 4, 2026, after which most established lots revert to lower-density districts. Confirming the current designation and the fastest compliant path is the first Phase 2 action.</p>
  <div class="co-amber"><b>One item to confirm first: this parcel's current land-use designation and whether any application is already in progress.</b><br><span class="sub">Transition exemptions protect parcels with an approved permit or subdivision under R-CG/R-G/H-GO before Aug 4, 2026, applications submitted before April 8, 2026, or parcels rezoned after August 6, 2024 — confirmed in Phase 2.</span></div>'''))

# --- section 4 options ---
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — R-CG Multiplex: Rowhouse / up to 4 Units (time-sensitive)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">While this parcel carries R-CG under the citywide rezoning, Land Use Bylaw 1P2007 permits a rowhouse or a multiplex of up to four units, plus secondary suites, without a rezoning. This is the highest-density as-of-right path — but it is time-sensitive: the R-CG framework is repealed effective August 4, 2026, after which the ceiling drops to three units and rowhouse permissions narrow. Securing an approved permit before the deadline is what locks the four-unit envelope. Buildable size is governed by height, lot coverage, setback and floor-area rules and the parcel's confirmed designation and lot area — all confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Secondary Suite + Backyard Suite — Primary Near-Term Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The most durable path given the transition: keep the principal dwelling and add a secondary (e.g. basement) suite and/or a detached backyard suite. These suite permissions are not swept away by the August 4, 2026 repeal, and Council is moving to make them permitted uses in all low-density districts (July 21, 2026 hearing). It is typically the fastest route to rental income and can proceed under R-C1/R-C2 as well as R-CG. Suite sizes, siting and the current permitted/discretionary status are confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Land Use Redesignation (rezoning) for a Larger Multiplex</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">If the goal is a multiplex larger than the base district allows — especially after the August 4, 2026 repeal returns most lots to R-C1/R-C2 — the path is a land use redesignation (a rezoning) to a multi-residential district. This involves an application, public engagement and a Council decision, so it carries more time and cost than an as-of-right build. It remains a legitimate route to higher density on a well-located lot such as this; feasibility, likely support and timeline are assessed in Phase 2.</div>'''))

# --- section 5 goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">A time-sensitive multiplex opportunity</div>
  <p>6424 Elbow Drive SW is an established low-density lot in Meadowlark Park, caught in Calgary's zoning transition. <strong>The strongest multiplex path is the R-CG route before the August 4, 2026 repeal</strong> — conditional on confirming this parcel's current designation and securing approval in time. The secondary-plus-backyard-suite route is the reliable near-term recommendation that survives the repeal, and a land use redesignation remains the path to a larger multiplex afterward. Confirming the designation is the first Phase 2 step.</p>'''))

# --- section 7 grants: inject Calgary/federal rows after the header row ---
R.append(('    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>',
'''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Federal</td><td>Enhanced GST Rental Rebate (Purpose-Built Rental Housing)</td><td>100% rebate of the 5% federal GST on new purpose-built rental projects of 4+ units with 90%+ long-term rental. Construction must begin on or before December 31, 2030 and complete by December 31, 2035. Applies in Alberta. A four-unit rental multiplex can qualify; single, duplex and triplex builds do not. Eligibility confirmed in Phase 2. (Source: Government of Canada / CRA — Purpose-Built Rental Housing Rebate.)</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / Apartment Construction Loan Program (ACLP)</td><td>MLI Select mortgage insurance for 5+ rental units and the ACLP low-interest construction loan (minimum $1M) — national, government-backed financing options that can materially improve a qualifying rental project's economics. Alberta-eligible. These are financing programs, not grants; eligibility and terms confirmed in Phase 2. (Source: CMHC.)</td></tr>
    <tr><td>Municipal</td><td>City of Calgary Secondary Suite Incentive Program</td><td>Has offered up to $10,000 toward a safe, registered secondary suite (with additional amounts for accessibility and energy efficiency). Important: as of June 24, 2026 new applications are placed on a waitlist and funding may not be available — treat as a possibility to confirm, not a guarantee. (Source: City of Calgary — Secondary Suite Incentive Program.)</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable federal tax credit of up to $7,500 (15% of up to $50,000 in eligible costs) for creating a secondary or garden suite for a qualifying senior or adult with a disability. Applies where the conditions are met — confirmed in Phase 2. (Source: CRA.)</td></tr>'''))

# --- section 8 summary review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>6424 Elbow Drive SW sits in Meadowlark Park, an established southwest Calgary community. Its development potential is shaped by Calgary's zoning transition: the citywide rezoning that made <strong>R-CG</strong> the base district is repealed effective <strong>August 4, 2026</strong>, after which most lots revert to R-C1/R-C2. This makes the timing — not just the lot — the decisive factor. Because live access to the City's parcel data was unavailable when this report was generated, the exact current designation is confirmed in Phase 2.</p>
  <ul>
    <li><strong>The Time-Sensitive Multiplex Advantage:</strong> while this parcel carries R-CG, a rowhouse or up-to-4-unit multiplex is permitted without a rezoning — but the window closes August 4, 2026, so confirming the designation and the fastest compliant path is the highest-value first step.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

open("report_calgary.html", "w").write(s)

print("--- leftover scan ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John", "Arockiaraj",
          "654-2025", "474-2023", "Ontario", "Bill 185", "TTC", "Woodbine",
          "M4L", "647", "Saanich", "SSMUH", "Secondary Suite Loan"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
