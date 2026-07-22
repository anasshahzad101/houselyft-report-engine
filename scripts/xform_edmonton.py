import os
HTML = os.path.join(os.path.dirname(__file__), "..", "templates", "report_edmonton.html")
s = open(HTML).read()
R = []

# --- cover
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">10511 52 Avenue NW<span>Edmonton, AB</span></div>'))

# --- property details barhead
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">10511 52 Avenue NW, Edmonton, AB&nbsp;&nbsp;T6H 0N9</div>'))

# --- imagery row: Edmonton has NO verified-licence imagery source -> drop the
#     grey placeholder boxes entirely, keep one honest line (routine step 4b).
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div style="font-size:8.5pt;color:#7a818f;font-style:italic;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# --- contact table
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>10511 52 Avenue NW, Edmonton, AB&nbsp;&nbsp;T6H 0N9</td></tr>
    <tr><td>Name</td><td>Aaron Choi</td></tr>
    <tr><td>Phone Number</td><td>(403) 830-7855</td></tr>
    <tr><td>Email</td><td>aaronchoi5@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — maximize unit count under Edmonton's Small Scale Residential (RS) zone</td></tr>'''))

# --- municipality table
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
    <tr><td>Neighbourhood</td><td>Pleasantview</td></tr>
    <tr><td>Ward</td><td>papastew Ward (Councillor Michael Janz)</td></tr>
    <tr><td>Community League</td><td>Pleasantview Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Edmonton for the local collection schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count under RS is set by lot geometry and the RS site standards, confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize unit count under the RS zone (up to 6 dwellings mid-block as-of-right)</td></tr>'''))

# --- neighbourhood spotlight
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
    10511 52 Avenue NW is in Pleasantview, an established south-central Edmonton neighbourhood set on elevated ground (the source of its name), first developed from 1914 and built out substantially after WWII:
    <ul>
      <li>Close to Southgate Centre and the Southgate LRT (Capital Line) station — quick transit access to the University of Alberta and downtown</li>
      <li>Near Whitemud Drive and 111 Street for regional road access</li>
      <li>Served by the Pleasantview Community League; parks and schools throughout the neighbourhood</li>
      <li>Many original 1940s-era bungalows are being replaced with larger homes and multi-unit infill — a neighbourhood actively redeveloping under Edmonton's Small Scale Residential rules</li>
      <li>Note: illustrative neighbourhood context, not a property valuation.</li>
    </ul>'''))

# --- section 2: current zoning kv table
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone consolidated the former RF1–RF4 districts. Row and small-scale multi-unit housing are permitted by default; the unit count on a specific lot is governed by the RS site standards (setbacks, height, coverage, separation space), confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Zoning Bylaw 20001's one-year-review amendments (2025), the mid-block maximum was set at 6 dwellings as-of-right (down from 8); up to 8 dwellings are permitted on corner sites, and developments of more than 8 units are limited to corner sites. Backyard (garden) housing is permitted and counts toward the total. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing — the RS zone permits row housing and small-scale multi-unit development, up to <strong>6 dwellings mid-block as-of-right</strong> (up to 8 on a corner site), subject to the RS site standards and technical review.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- section 2: "what this means for you" list
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing &amp; Multi-Unit Housing:</strong> Attached and small-scale multi-unit buildings — the core of what the RS zone permits</li>
      <li><strong>Up to Six Dwellings (mid-block):</strong> A multiplex of up to six dwellings as-of-right, no rezoning (up to eight on a corner lot)</li>
      <li><strong>Backyard (Garden) Housing:</strong> A detached backyard house is permitted and counts toward the site's total dwelling count</li>
      <li><strong>Secondary Suites:</strong> An internal suite can be paired with the principal dwelling to add density and rental income</li>'''))

# --- Time-Sensitive: replace the three Toronto rows with Edmonton/Alberta ones
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Edmonton RS Height Cut-off — Act Now<br><small>applications from Aug 1, 2026</small></div><div class="dx">Under an amendment approved April 27, 2026, the maximum building height in the RS zone drops from 10.5 m to 9.5 m for development permit applications submitted on or after August 1, 2026. Filing before that date preserves the taller 10.5 m envelope — which can be the difference of a full storey of buildable space. (City of Edmonton, Zoning Bylaw 20001 amendments.)</div></div>
    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build before 2031</small></div><div class="dx">The federal 100% rebate of the 5% GST on new purpose-built rental housing (projects of 4+ self-contained units, 90%+ long-term rental) applies in Alberta as elsewhere. Construction must generally begin before 2031. Structuring the project as qualifying rental from Day 1 is essential to capture this. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# --- section 3: rezoning
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended multiplex configuration is permitted as-of-right under Edmonton Zoning Bylaw 20001 (RS zone) — no rezoning required.</div>'))
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS)</td><td class="n">A new site-specific bylaw</td></tr>'))
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to six dwellings</div>The RS zone permits up to six dwellings mid-block as-of-right (up to eight on a corner site) under Zoning Bylaw 20001 — no rezoning, no public hearing.</div>
    <div class="card2"><div class="ct">Backyard house</div>A detached backyard (garden) house is permitted in the RS zone and counts toward the site's total dwelling count.</div>'''))
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 10511 52 Avenue NW</div>
  <p>Because 10511 52 Avenue NW already permits the recommended build under the existing RS zone, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the bylaw in force at the date of this report and is subject to technical review of site conditions.</p>'''))
R.append(('''  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-amber"><b>One item to confirm: the lot's corner-vs-mid-block status and dimensions.</b><br><span class="sub">Mid-block lots permit up to six dwellings as-of-right; corner sites permit up to eight. The final unit count is set by the RS site standards once the lot survey is confirmed in Phase 2.</span></div>'''))

# --- section 4: development options
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 dwellings, as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A triplex or fourplex built on the lot — the reliable baseline under the RS zone, with no rezoning or public hearing. Buildable size is governed by the RS site standards (setbacks, height, lot coverage, and separation space) rather than a unit cap at this scale. This is the fastest-approving multiplex tier and a dependable fallback if the six-dwelling form is constrained by lot geometry. Confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (mid-block) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Up to six dwellings on a mid-block RS lot as-of-right — the highest-density, strongest-income direction without rezoning (a corner lot can reach eight). This matches Aaron's stated multiplex goal. A backyard (garden) house may be added and counts toward the six-dwelling total. Height is capped at 10.5 m today, dropping to 9.5 m for applications filed on or after August 1, 2026 — a reason to move early. No blanket parking minimum applies to small-scale residential. Confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Backyard House / Secondary Suite Route</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep or build the principal dwelling and add a detached backyard house and/or an internal secondary suite. Backyard housing is permitted in the RS zone and counts toward the site's dwelling total; a legal internal secondary suite may also qualify for the City's Secondary Suite Incentive (see Grants). This is often the fastest route to rental income while a larger multiplex is designed. Suite sizes and siting confirmed in Phase 2.</div>'''))

# --- section 5: development goal summary
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex under the RS zone (up to 6 dwellings)</div>
  <p>10511 52 Avenue NW is an RS (Small Scale Residential) lot in Edmonton, where up to six dwellings are permitted mid-block as-of-right (up to eight on a corner site) under Zoning Bylaw 20001 — no rezoning, no public hearing. <strong>A six-unit multiplex is the clear primary recommendation</strong>; a triplex/fourplex is the reliable fallback, and a backyard house or secondary suite is the fastest entry to rental income.</p>'''))

# --- section 7: grants table (inject gated, geography-correct rows after the header)
R.append(('    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>',
'''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Rebate</td><td>100% rebate of the 5% federal GST on new purpose-built rental housing — projects of 4+ self-contained units, 90%+ long-term rental, construction generally before 2031. Applies in Alberta. Unlocks at the 4-dwelling tier. (Government of Canada — Enhanced GST Rental Rebate.) Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Multi-unit mortgage insurance for purpose-built rental of 5+ units — favourable amortization and loan-to-value on a qualifying rental project. Unlocks at the 5-dwelling tier. (CMHC MLI Select.) Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing, minimum $1M loan (gated on the project budget established in Phase 2, not on unit count). Can bridge into MLI Select permanent financing at completion. (CMHC ACLP.)</td></tr>
    <tr><td>Provincial (Alberta)</td><td>No-PST Advantage</td><td>Alberta levies no provincial sales tax, so construction materials carry only the 5% federal GST rather than a combined HST rate. Against an HST province this is a real, automatic structural saving on the build budget — nothing to apply for. Figures scale to the project; confirmed in Phase 2.</td></tr>
    <tr><td>Municipal (Edmonton)</td><td>Secondary Suite Incentive</td><td>Up to $10,000 toward a legal internal secondary suite (one application per owner) — applies where the design includes a legal suite. Status: WAITLISTED as of June 24, 2026 — apply to hold a position. (edmonton.ca — Secondary Suite Incentive Program.)</td></tr>
    <tr><td>Municipal (Edmonton)</td><td>Infill Infrastructure Fund (IIF)</td><td>HAF-funded support for off-site public infrastructure tied to infill development. Status: fully allocated ($39M across 33 projects) — monitor for future rounds. (edmonton.ca — Infill Infrastructure Fund.)</td></tr>'''))

# --- section 8: summary
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>10511 52 Avenue NW confirms a strong development option. This property is zoned RS (Small Scale Residential) under Edmonton Zoning Bylaw 20001, where up to <strong>six dwellings are permitted mid-block as-of-right</strong> (up to eight on a corner site) — no rezoning, no public hearing, no Council approval required.</p>
  <ul>
    <li><strong>The Six-Dwelling As-of-Right Advantage:</strong> The RS zone allows a multiplex of up to six dwellings as-of-right, with backyard housing counting toward the total — a direct path to the multiplex you are considering.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)
open(HTML, "w").write(s)

print("--- leftover scan ---")
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj", "654-2025",
          "474-2023", "Ontario HST", "Bill 185", "Bill 23", "6+1 Config", "RD zone",
          "garden suite", "Garden Suite", "M4L 3B5", "johneeraj", "(647)"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
