"""
xform_edmonton.py — turn the House Lyft master into the Edmonton report for
11909 83 Street NW (contact Sunny R).

Edmonton is not one of the engine's nine GTA adapter cities, so zoning is NOT
machine-verified — the specific parcel zone is treated as CONFIRM (expected RS)
and every unverified figure carries the "confirmed in Phase 2" hedge. All
stated rules trace to official City of Edmonton / Government of Canada sources:

  - Zoning Bylaw 20001 (in effect Jan 1, 2024) — RS (Small Scale Residential)
    zone permits up to 8 dwelling units per lot as-of-right on qualifying sites,
    up to 3 storeys; max height 10.5 m dropping to 9.5 m effective Aug 1, 2026
    (Council Apr 27, 2026).
  - Open Option Parking (2020) — no minimum parking requirements citywide.
  - Federal GST Purpose-Built Rental Housing rebate — 100% of the 5% GST,
    4+ units, construction before 2031 / substantially complete before 2036;
    applies in Alberta.
  - CMHC MLI Select / Apartment Construction Loan Program — national.

Run from the templates/ directory:  python3 ../scripts/xform_edmonton.py
"""
s = open("report_edmonton.html").read()
R = []

# --- cover ---
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">11909 83 Street NW<span>Edmonton, AB</span></div>'))

# --- section 1 barhead ---
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">11909 83 Street NW, Edmonton, AB&nbsp;&nbsp;T5B 4E7</div>'))

# --- imagery licence placeholder -> real source credit ---
R.append(('  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Aerial and street-level imagery to be sourced from the City of Edmonton open imagery during the feasibility phase.</div>'))

# --- property table 1 ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>11909 83 Street NW, Edmonton, AB&nbsp;&nbsp;T5B 4E7</td></tr>
    <tr><td>Name</td><td>Sunny R</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — 8-plex; maximize unit count under Edmonton's Small Scale Residential rules</td></tr>'''))

# --- property table 2 ---
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
    <tr><td>Neighbourhood</td><td>Eastwood (Avenue District)</td></tr>
    <tr><td>Current Zoning</td><td>To be confirmed against the City Zoning Map — expected RS (Small Scale Residential)</td></tr>
    <tr><td>Governing Framework</td><td>City of Edmonton Zoning Bylaw 20001 (in effect Jan 1, 2024)</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Edmonton for the local schedule</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via Alberta Land Titles)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count (4 to 8) depends on lot width &amp; area</td></tr>
    <tr><td>Development Goals</td><td>Small-scale multiplex — up to 8 units (primary); smaller multiplex fallback on a narrow lot</td></tr>'''))

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
    11909 83 Street NW is in Eastwood, an established residential neighbourhood in north-central Edmonton — the kind of mature, fully serviced area the City's new zoning rules were designed to gently intensify:
    <ul>
      <li>Close to Edmonton's central core, with quick access to downtown, NAIT, and the Kingsway corridor</li>
      <li>Well served by Edmonton Transit Service; the mature street grid supports small-scale infill</li>
      <li>A tight, in-demand rental market across central Edmonton — supportive of a hold-and-rent strategy</li>
      <li>Established residential streets now opened to up to eight units per lot under Zoning Bylaw 20001</li>
      <li>Note: lot width, mature trees, and setback rules shape what is buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- section 2 zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>To be confirmed against the City of Edmonton Zoning Map — expected RS (Small Scale Residential) under Zoning Bylaw 20001</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Under Bylaw 20001, the RS zone permits small-scale housing on serviced residential lots citywide. The number of units a lot can carry (up to 8) scales with lot width and area — confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Zoning Bylaw 20001 (in effect Jan 1, 2024) consolidated the former RF1–RF4 zones into a single RS zone, permitting up to <strong>8 dwelling units</strong> per lot as-of-right on qualifying sites. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Small-scale residential — row housing, small apartments/multiplexes, and backyard/secondary suites. On a qualifying RS lot, up to <strong>8 units</strong> are permitted as-of-right, subject to lot dimensions and technical site review.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — subject to confirming the parcel's zone (expected RS) and lot dimensions; then proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means for you" list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing &amp; Stacked Row Housing:</strong> Multi-unit attached homes — side-by-side or vertically stacked units</li>
      <li><strong>Small-Scale Multiplex:</strong> Standalone buildings of up to 8 dwelling units on a qualifying lot</li>
      <li><strong>Small Apartment / Low-Rise:</strong> Small-scale apartment forms up to 3 storeys</li>
      <li><strong>Backyard &amp; Secondary Suites:</strong> Backyard housing and secondary suites can be combined with the main dwelling, counting within the lot's unit total</li>'''))

# --- time-sensitive ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build by 2031</small></div><div class="dx">The federal government's 100% rebate of the 5% GST on new purpose-built rental housing (projects of 4+ self-contained units, 90%+ long-term rental) applies in Alberta. Construction must begin before 2031 and be substantially complete before 2036. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">Edmonton RS Height Change<br><small>effective Aug 1, 2026</small></div><div class="dx">On April 27, 2026 Council approved reducing the maximum building height in the RS zone from 10.5 m to 9.5 m, effective August 1, 2026. For a three-storey small-scale multiplex, finalizing the design envelope early can matter — the applicable height is confirmed against the current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# --- section 3 rezoning: strip Toronto-specific tail, keep as-of-right story ---
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
'''  <div class="co-green"><div class="ct2">Not Required for This Property</div>A small-scale multiplex is permitted as-of-right in Edmonton's RS zone under Zoning Bylaw 20001 — no rezoning is contemplated in this analysis, subject to confirming the parcel's zone.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS zone)</td><td class="n">A new site-specific rezoning</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">What this means for 11909 83 Street NW</div>
  <p>Provided the parcel carries the expected RS zone, the small-scale multiplex you are considering is already permitted under existing zoning, so the project can advance directly to design and permitting. This assessment reflects the bylaw in force at the date of this report and is subject to confirming the zone and a technical review of site conditions.</p>'''))

# --- development options A/B/C ---
R.append(('  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '  <div class="opt"><div class="oh">Option A — Small-Scale Multiplex (up to 4 units, as-of-right)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A small-scale multiplex of up to four units built directly on the lot — the reliable baseline on a narrower RS site, with no rezoning or public hearing. Buildable size is governed by the RS zone's height, lot-coverage, setback and floor-area rules — confirmed in Phase 2. Edmonton removed minimum parking requirements citywide under Open Option Parking (2020), so on-site parking is a design choice rather than a mandate.</div>'''))
R.append(('  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '  <div class="opt"><div class="oh">Option B — Eight-Unit Small-Scale Multiplex — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">On a qualifying RS lot, Zoning Bylaw 20001 permits up to eight dwelling units as-of-right — the highest-density, strongest-income direction without rezoning, and a direct match to your stated 8-plex goal. Whether the lot reaches the eight-unit tier depends on its width and area, so confirming lot dimensions is the first gating step. No minimum parking applies under Open Option Parking. Confirmed in Phase 2.</div>'''))
R.append(('  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '  <div class="opt"><div class="oh">Option C — Backyard &amp; Secondary Suite Route</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: keep the principal dwelling and add backyard housing plus a secondary suite. The RS zone permits these forms, and they count within the lot's overall unit total. This is often the fastest route to rental income while a larger multiplex is designed and evaluated. Suite sizes and siting confirmed in Phase 2.</div>'''))

# --- section 5 development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Small-Scale Multiplex (up to 8 units)</div>
  <p>11909 83 Street NW sits in an established Edmonton neighbourhood opened to gentle density by Zoning Bylaw 20001 — up to 8 dwelling units as-of-right on a qualifying RS lot, with the exact ceiling (4 to 8) set by lot width and area. <strong>Where the lot qualifies for the eight-unit tier, an eight-unit small-scale multiplex is the clear primary recommendation</strong>; a smaller multiplex is the reliable fallback, and the backyard/secondary-suite route is the fastest entry.</p>'''))

# --- section 7 grants table ---
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects of 4+ self-contained units, 90%+ long-term rental. Construction must begin before 2031 and be substantially complete before 2036. Applies in Alberta (no provincial sales tax applies). Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction loans for purpose-built rental, minimum $1M loan. Can be structured to bridge into MLI Select permanent financing at project completion. National program. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Government-backed multi-unit mortgage insurance (minimum 5 rental units) that reduces premiums and can extend amortization on a points system for affordability, energy efficiency, and accessibility. National program. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Edmonton permit &amp; levy treatment</td><td>Edmonton removed minimum parking requirements citywide (Open Option Parking, 2020). Permit fees and any applicable off-site levies for a small-scale residential build are confirmed against the City's current schedule in Phase 2 — no figures are stated here until verified.</td></tr>'''))

# --- section 8 zoning review ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>11909 83 Street NW presents a strong development option. Under the City of Edmonton's Zoning Bylaw 20001 (in effect January 1, 2024), the RS (Small Scale Residential) zone permits up to <strong>eight dwelling units per lot as-of-right</strong> on a qualifying site — one of the most permissive small-scale frameworks of any major Canadian city, and a direct match to your 8-plex goal.</p>
  <ul>
    <li><strong>The Eight-Unit As-of-Right Potential:</strong> On a qualifying RS lot, up to eight units are permitted with no rezoning, no public hearing, and no Council approval — the exact ceiling is set by lot width and area, confirmed in Phase 2.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}"); fails += 1
    else:
        s = s.replace(old, new)

open("report_edmonton.html", "w").write(s)

print("replacements:", len(R), "| fails:", fails)
LEFTOVER_TERMS = ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
                  "654-2025", "474-2023", "569-2013", "Bill 185", "Ontario HST",
                  "6+1", "4+1", "Garden Suite By-law", "OLT", "Woodbine",
                  "Danforth", "TTC", "Greenwood", "RD zone", "RD —"]
any_left = False
for t in LEFTOVER_TERMS:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}"); any_left = True
if not any_left:
    print("LEFTOVER CHECK: clean — zero wrong-city / wrong-lead references")
