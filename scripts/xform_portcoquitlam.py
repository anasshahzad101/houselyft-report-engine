import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
s = open(os.path.join(TPL, "report_houselyft_master.html")).read()

lot_b64 = open(os.path.join(ROOT, "scratch_poco/lot.b64")).read().strip()
ctx_b64 = open(os.path.join(ROOT, "scratch_poco/context.b64")).read().strip()

R = []

# 1. Cover address
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">1157 Ellis Drive<span>Port Coquitlam, BC</span></div>'))

# 2. Property Details barhead
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">1157 Ellis Drive, Port Coquitlam, BC&nbsp;&nbsp;V3B 1G9</div>'))

# 3. Imagery row + licence
old_img = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_img = ('  <div class="imgrow" style="margin-top:0;">\n'
    '    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">\n'
    '      <img src="data:image/jpeg;base64,' + lot_b64 + '" style="width:100%;height:148px;object-fit:cover;display:block;" alt="Aerial view of 1157 Ellis Drive">\n'
    '      <div style="position:absolute;left:0;bottom:0;right:0;background:rgba(27,42,74,0.72);color:#fff;font-size:7pt;padding:3px 6px;">Aerial view — approx. 90 m across</div>\n'
    '    </div>\n'
    '    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">\n'
    '      <img src="data:image/jpeg;base64,' + ctx_b64 + '" style="width:100%;height:148px;object-fit:cover;display:block;" alt="Neighbourhood context around 1157 Ellis Drive">\n'
    '      <div style="position:absolute;left:0;bottom:0;right:0;background:rgba(27,42,74,0.72);color:#fff;font-size:7pt;padding:3px 6px;">Neighbourhood context — approx. 320 m across</div>\n'
    '    </div>\n'
    '  </div>\n'
    '  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery © Mapbox © OpenStreetMap © Maxar. Satellite basemap, used under the Mapbox Terms of Service (static print use permitted with attribution).</div>')
R.append((old_img, new_img))

# 4. Contact / goals kv
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>1157 Ellis Drive, Port Coquitlam, BC&nbsp;&nbsp;V3B 1G9</td></tr>
    <tr><td>Name</td><td>Paula Rubio</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Add one detached ADU (coach house / garden suite) to the rear of the property</td></tr>'''))

# 5. Property details municipality kv
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
'''    <tr><td>Municipality</td><td>City of Port Coquitlam (Metro Vancouver)</td></tr>
    <tr><td>Neighbourhood</td><td>Birchland Manor</td></tr>
    <tr><td>Region</td><td>Metro Vancouver Regional District, BC</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td></tr>
    <tr><td>Current Bylaw</td><td>Port Coquitlam Zoning Bylaw No. 3630 (as amended for SSMUH, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit ceiling depends on lot area (280 m² threshold) &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>One detached ADU (coach house) at the rear — primary; larger SSMUH build (up to 4 units, 6 near transit) as upside</td></tr>'''))

# 6. Neighbourhood Spotlight
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
    1157 Ellis Drive is in the Birchland Manor neighbourhood of Port Coquitlam, an established, family-oriented residential area in Metro Vancouver's northeast:
    <ul>
      <li>Quiet single-family streets now opened to gentle density by BC's province-wide SSMUH rules</li>
      <li>Served by TransLink bus routes; proximity to a frequent-transit stop is the single factor that decides whether up to six units are permitted — confirmed in Phase 2</li>
      <li>Close to the Coquitlam River, local parks and schools; everyday shopping along the Coast Meridian and Prairie Avenue corridors</li>
      <li>Strong, chronically tight Metro Vancouver rental market — supportive of a hold-and-rent strategy</li>
      <li>Note: slopes, trees, watercourse setbacks and firefighting-access rules can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# 7. Section 2 zoning kv
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential Small-Scale (RS1–RS4), now subject to provincial SSMUH permissions — exact district confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced RS1–RS4 lots not already holding a duplex or triplex. The unit ceiling scales with lot area and transit proximity (the six-unit tier needs a lot &gt;280 m² within ~400 m of frequent transit).</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023), Port Coquitlam amended Zoning Bylaw No. 3630 (2024) to permit <strong>up to 4 units as-of-right</strong> on RS1–RS4 lots (3 on lots ≤280 m²; 6 on larger lots near frequent transit) — plus a detached accessory dwelling unit. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>A detached ADU (coach house / garden suite), secondary suite, duplex, triplex or fourplex — and, near frequent transit, up to a six-unit multiplex. A detached ADU is capped at <strong>90 m² (968 ft²)</strong> and cannot be strata-subdivided or be the lot's principal dwelling. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# 8. "What this means for you" list
R.append(('''    <ul style="margin-top:0;">
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>
    </ul>''',
'''    <ul style="margin-top:0;">
      <li><strong>Detached ADU (Coach House / Garden Suite):</strong> a self-contained home at the rear of the lot, up to 90 m² — your stated goal, permitted as-of-right on an RS lot under SSMUH</li>
      <li><strong>Secondary Suite:</strong> a suite within the principal house, which can pair with a detached ADU on the same lot</li>
      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is &gt;280 m² and within ~400 m of frequent transit</li>
    </ul>'''))

# 9. Time-sensitive .d blocks
R.append(('''<div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>''',
'''<div class="d"><div class="dt">SSMUH Development Permit<br><small>required before building permit</small></div><div class="dx">In Port Coquitlam, a new duplex, any development of three or more dwellings, and an accessory dwelling unit each require a Small-Scale Multi-Unit Housing (SSMUH) Development Permit before a building permit can be issued. Building this into the timeline from Day 1 avoids a mid-project stall. Requirements are confirmed with the City in Phase 2.</div></div>'''))
R.append(('''<div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>''',
'''<div class="d"><div class="dt">BC Secondary Suite Incentive — Paused<br><small>closed Mar 30, 2025</small></div><div class="dx">The Province's Secondary Suite Incentive Program (a forgivable loan of up to $40,000 toward a new suite) stopped accepting applications on March 30, 2025 and is not currently open. Do not count on provincial suite-incentive money unless and until a renewed program is confirmed — this is verified before your Phase 2 financing plan is built.</div></div>'''))
R.append(('''<div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''<div class="d"><div class="dt">Federal GST Rental Rebate &amp; CMHC<br><small>build by 2031 / policy can change</small></div><div class="dx">The federal 100% GST rebate on new purpose-built rental (projects of 4+ units, 90%+ long-term rental) applies in BC, with construction generally required before 2031 — relevant only if you scale beyond a single ADU. CMHC program terms and intake windows can change at any time; applying early reduces risk. Confirmed in Phase 2.</div></div>'''))

# 10. Section 3 rezoning
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A detached ADU — and up to a fourplex — is permitted as-of-right on an RS lot under BC\'s SSMUH rules. No rezoning is contemplated.</div>'))
R.append(('    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>',
          '    <tr><td>Public-hearing exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'))
R.append(('    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '    <tr><td>What governs your build</td><td class="g">SSMUH rules in Zoning Bylaw No. 3630</td><td class="n">A new site-specific by-law</td></tr>'))
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Triplex / Fourplex</div>SSMUH permits 3–4 units on a serviced RS lot without rezoning; the six-unit tier opens where the lot is &gt;280 m² and within ~400 m of frequent transit.</div>
    <div class="card2"><div class="ct">Detached ADU (coach house)</div>An RS lot may add a detached ADU at the rear — up to 90 m², at grade or above a garage — as-of-right under SSMUH, which is exactly the stated goal.</div>'''))
R.append(('  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '  <div class="barhead" style="text-align:left;">What this means for 1157 Ellis Drive</div>'))
R.append(('  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '  <p>Because a detached ADU is permitted as-of-right on an RS lot under SSMUH, no rezoning application is contemplated. Your project advances directly to the SSMUH development-permit and building-permit stage. The comparison above shows what that avoids. This assessment reflects the rules in force at the date of this report and is subject to technical review of site conditions — and, because Port Coquitlam is a newly researched municipality for us, the zone and figures are double-checked with the City before the call.</p>'))
R.append(('  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '  <div class="co-amber"><b>Two items to confirm early: the exact RS district and the lot\'s distance to frequent transit.</b><br><span class="sub">The RS district (RS1–RS4) and whether the lot is within ~400 m of a frequent-transit stop together set the unit ceiling. Neither changes the as-of-right ADU, but both shape any larger build — confirmed in Phase 2.</span></div>'))

# 11. Development options
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Detached ADU / Coach House (1 unit, as-of-right) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A single detached accessory dwelling unit (coach house / garden suite) at the rear of the lot — Paula's stated goal. On an RS lot this is permitted as-of-right under SSMUH: no rezoning and no public hearing. The ADU is capped at 90 m² (968 ft²), may sit at grade or above a garage/carport, cannot be strata-subdivided, and needs a 1 m paved firefighting-access path from its entrance to the street. Because it adds a unit, an SSMUH development permit is required before the building permit. This is the lowest-complexity, fastest route to new rental income; buildable size and siting are confirmed against Zoning Bylaw No. 3630 in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Triplex / Fourplex (3–4 units, as-of-right) — Upside</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">If Paula later wants more than a single suite, SSMUH allows a triplex or fourplex on the same lot with no rezoning — 3 units on a lot ≤280 m², 4 units on a larger lot. At four or more self-contained rental units, the federal GST purpose-built rental rebate comes into reach. This is a larger commitment than the stated ADU goal and is shown as upside; the exact unit ceiling is set by lot area and confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Six-Unit Multiplex (near frequent transit) — Upside</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Where the lot is greater than 280 m² and within roughly 400 m of a frequent-transit stop, SSMUH permits up to six units as-of-right — the highest-density direction without rezoning, and the point at which CMHC's MLI Select and Apartment Construction Loan Program (5+ rental units) come into play. Confirming the lot's transit distance is the gating step. This is well beyond the single-ADU goal; shown so the full ceiling is visible.</div>'''))

# 12. Section 5 summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">One Detached ADU (Coach House)</div>
  <p>1157 Ellis Drive is an RS-zoned lot in Port Coquitlam, now opened to gentle density by BC's SSMUH rules. Paula's goal — one detached ADU at the rear — is permitted as-of-right, making it the clear primary recommendation and the fastest route to rental income. A triplex/fourplex, and (near frequent transit) a six-unit multiplex, remain available as upside if she later wants more scale. <strong>The single detached ADU is the recommended first move.</strong></p>'''))

# 13. Section 6 financing gated row
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC MLI Select &amp; ACLP</td><td>Available at a larger scale — <strong>from five rental units</strong>, beyond a single-ADU project. MLI Select offers preferred multi-unit mortgage-loan insurance (minimum five units); the Apartment Construction Loan Program offers low-cost construction financing (minimum five self-contained units and a minimum $1,000,000 loan). Both apply nationwide, including BC. Confirm current CMHC intake before relying on either. Shown so you can see what scaling up unlocks.</td></tr>'''))

# 14. Section 7 grants gated rows
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial (BC)</td><td>BC SSMUH (Bill 44) as-of-right density</td><td>Not a grant but the core entitlement: up to 4 units (6 near frequent transit) — and a detached ADU — permitted on your RS lot without rezoning or a public hearing. This is what makes the ADU project as-of-right. Applies to your lot; scope confirmed in Phase 2.</td></tr>
    <tr><td>Provincial (BC)</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and additional-unit projects may qualify for reduced or waived DCCs; treatment varies and is set by the City. Confirmed against Port Coquitlam's current bylaw in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>At <strong>four or more</strong> self-contained rental units held long-term (90%+), a full 100% rebate of the 5% federal GST applies, with construction generally before 2031. Beyond a single ADU — opens up at the four-unit option. Applies in BC; eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select &amp; ACLP</td><td>At <strong>five or more</strong> rental units — preferred mortgage-loan insurance (MLI Select) and low-cost construction financing (ACLP, minimum $1,000,000 loan). Beyond the single-ADU scope; shown so you can see what scaling up unlocks.</td></tr>
    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>A provincial forgivable loan (up to $40,000 / 50% of costs) that supported new suites rented below market — the pilot <strong>stopped accepting applications March 30, 2025</strong> and is not currently open. Do not rely on it unless a renewed program is confirmed. Status checked in Phase 2.</td></tr>'''))

# 15. Section 8 summary
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>1157 Ellis Drive confirms a strong, low-complexity development option. It is an RS-zoned lot in Port Coquitlam, and under BC's SSMUH framework (Bill 44) a <strong>detached ADU is permitted as-of-right</strong> — no rezoning, no public hearing. A triplex/fourplex, and up to six units near frequent transit, remain available as upside.</p>
  <ul>
    <li><strong>The As-of-Right ADU Advantage:</strong> Paula's stated goal — one detached coach house — can proceed directly to the SSMUH development-permit stage, with the exact RS district, lot area and transit distance confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(TPL, "report_portcoquitlam.html")
open(out, "w").write(s)

print("\n--- LEFTOVER CHECK ---")
for t in ["Coxwell", "Toronto", "John Arockiaraj", "Ward 19", "654-2025", "474-2023",
          "Ontario HST", "Bill 185", "TTC", "OLT", "Beaches", "303", "M4L", "569-2013",
          "GATED_", "Briarstone", "Garden Suite By-law"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("fails:", fails, "| bytes:", len(s), "| wrote:", out)
