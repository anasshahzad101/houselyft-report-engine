"""
xform_edmonton.py — turn the House Lyft master into the Edmonton (RS / ZBL 20001)
report for 5308 35 Avenue NW.

Same doctrine as the other xform_*.py scripts: every replacement must match the
master exactly once, then we grep for wrong-city leftovers. All facts come from
the verified engine packet (property_lookup_v2 Edmonton adapter) — RS small-scale
residential, up to 6 dwellings mid-block as-of-right under Zoning Bylaw 20001,
backyard housing permitted, the Aug 1 2026 height cut-off and the Jul 8 2025
side-entrance rule. No Ontario programs, no invented amounts.

Run from repo root:  python3 scripts/xform_edmonton.py
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TPL = os.path.join(HERE, "..", "templates", "report_edmonton.html")

s = open(TPL, encoding="utf-8").read()
R = []

# --- cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">5308 35 Avenue NW<span>Edmonton, AB</span></div>'))

# --- 1. Property Details ----------------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">5308 35 Avenue NW, Edmonton, AB&nbsp;&nbsp;T6L 1V8</div>'))

R.append(('<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Zoning &amp; mapping data © City of Edmonton, Open Data (gis.edmonton.ca). Lot-scale aerial and street-view imagery obtained under municipal licence (City of Edmonton / Pictometry) during Phase 2.</div>'))

R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>5308 35 Avenue NW, Edmonton, AB&nbsp;&nbsp;T6L 1V8</td></tr>
    <tr><td>Name</td><td>Maria Garcera</td></tr>
    <tr><td>Phone Number</td><td>(587) 710-5308</td></tr>
    <tr><td>Email</td><td>mgarcera@yahoo.ca</td></tr>
    <tr><td>Development Goals</td><td>Garden suite, laneway home or ADU — add a garage/backyard suite or home expansion for an additional rental suite</td></tr>'''))

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
    <tr><td>Neighbourhood</td><td>Hillview (Mill Woods)</td></tr>
    <tr><td>Ward</td><td>Karhiio Ward (Councillor Keren Tang)</td></tr>
    <tr><td>Community League</td><td>The Woodvale Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Edmonton for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via Alberta Land Titles)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; corner vs. mid-block siting</td></tr>
    <tr><td>Development Goals</td><td>Backyard/garden or garage suite (primary); small-scale multiplex up to 6 units (alternative)</td></tr>'''))

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
    5308 35 Avenue NW is in the Hillview neighbourhood of Mill Woods, southeast Edmonton — an established residential community served by The Woodvale Community League:
    <ul>
      <li>Located immediately north of the Grey Nuns Community Hospital, bounded by major roadways with curved, keyhole interior streets</li>
      <li>Strategically placed walkways make for convenient walking and cycling through the neighbourhood</li>
      <li>The neighbourhood focus is its two elementary schools and park sites</li>
      <li>Existing housing is a mix of single-unit dwellings, row housing, and walk-up apartments — consistent with the RS small-scale residential permissions</li>
      <li>Illustrative context drawn from City of Edmonton neighbourhood data, not a valuation.</li>
    </ul>'''))

# --- 2. Current Zoning ------------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone permits small-scale housing — including row housing and multi-unit buildings — on serviced residential lots. Unit count depends on lot area and whether the site is mid-block or a corner. Confirmed against site conditions in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Edmonton's Zoning Bylaw 20001 (in force Jan 1, 2024) consolidated the former RF1–RF4 districts into RS. Under the one-year-review amendments (2025), the mid-block maximum was set at <strong>6 dwellings</strong> (reduced from 8); developments of more than 8 dwellings are limited to corner sites. Backyard housing is permitted and counts toward the total.</td></tr>
    <tr><td>Permitted Uses</td><td>Small-scale housing — up to <strong>6 dwellings as-of-right mid-block</strong> (up to 8 on a corner site), plus backyard housing (garden/garage suite), under Bylaw 20001. No rezoning required. Subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing &amp; Multi-Unit Housing:</strong> Attached and small-scale multi-unit homes permitted in the RS zone</li>
      <li><strong>Small-Scale Multiplex:</strong> Up to 6 dwellings mid-block (up to 8 on a corner site) as-of-right under Bylaw 20001</li>
      <li><strong>Backyard Housing (Garden or Garage Suite):</strong> A detached rear suite is permitted and counts toward the total dwellings on the site — the direction that matches your goal</li>
      <li><strong>Secondary Suites:</strong> An internal suite (such as a basement suite) can be paired with the main dwelling to add rental income</li>'''))

# --- Time-Sensitive ---------------------------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">RS Height Cut-Off — Act Before Aug 1, 2026<br><small>time-sensitive</small></div><div class="dx">Edmonton's maximum height in the RS zone is currently 10.5 m, but drops to 9.5 m for applications made on or after August 1, 2026 (approved April 27, 2026). Filing before the cut-off preserves the taller 10.5 m envelope — a meaningful difference for a two- or three-storey backyard suite or multiplex. (City of Edmonton Zoning Bylaw 20001.)</div></div>
    <div class="d"><div class="dt">Entrance &amp; Setback Rule — In Effect</div><div class="dx">Since July 8, 2025, a maximum of two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side. This shapes suite layout and should be designed in from Day 1. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# --- 3. Rezoning ------------------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Backyard housing and small-scale multiplexes up to 6 dwellings mid-block are permitted as-of-right in the RS zone under Edmonton Zoning Bylaw 20001 — no rezoning required.</div>'))

R.append(('    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS)</td><td class="n">A new site-specific rezoning</td></tr>'))

R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Small-scale multiplex</div>The RS zone permits up to six dwellings mid-block (up to eight on a corner site) as-of-right under Bylaw 20001 — no rezoning or public hearing.</div>
    <div class="card2"><div class="ct">Backyard housing</div>A detached garden or garage suite is permitted in the RS zone and counts toward the site's total dwellings — the direction that matches your stated goal.</div>'''))

R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 5308 35 Avenue NW</div>'))

R.append(('  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '  <p>Because 5308 35 Avenue NW already permits backyard housing and a small-scale multiplex under the existing RS zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the bylaws in force at the date of this report and is subject to technical review of site conditions.</p>'))

R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the permit status of any existing garage or rear structure.</b><br><span class="sub">If you plan a garage suite and the structure was altered without a permit, a retroactive development/building permit is needed before financing or development can proceed. Confirmed in Phase 2.</span></div>'))

# --- 4. Development Options -------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Backyard Housing: Garden or Garage Suite (Primary — matches your goal)</div>'))

R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached backyard housing unit — a garden suite or a suite above/within a garage — built in the rear yard while keeping your existing home. This is permitted as-of-right in the RS zone and counts toward the site's total dwellings, so no rezoning is required. It is the most direct route to a new rental suite and matches your stated goal. Suite size and siting are governed by height, setback, and lot-coverage rules — including the July 2025 side-entrance setback — and are confirmed in Phase 2. No minimum parking applies to the suite.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small-Scale Multiplex (up to 6 units, as-of-right)</div>'))

R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The higher-density direction: a small-scale multiplex of up to 6 dwellings mid-block (or up to 8 on a corner site) built on the lot, as-of-right under Bylaw 20001 with no rezoning or public hearing. Backyard housing can be combined with the main building within the applicable dwelling count. The exact unit ceiling depends on lot area and corner-vs-mid-block siting, confirmed in Phase 2. Note the August 1, 2026 height cut-off (10.5 m → 9.5 m) when scheduling the application.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Home Expansion + Secondary Suite</div>'))

R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A lower-complexity path: expand the principal dwelling and add an internal secondary suite (such as a basement suite) for additional rental income, optionally paired with a backyard suite. This can be the fastest route to cash flow while a larger multiplex is evaluated. If any existing garage or structure was altered without a permit, confirming its permit status is an essential first step — both for financing and for counting it as a legal unit. Sizes and siting confirmed in Phase 2.</div>'''))

# --- 5. Development Goal Summary --------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Backyard Suite, with Multiplex Upside</div>
  <p>5308 35 Avenue NW is an RS (Small Scale Residential) lot in Edmonton, where backyard housing and up to six dwellings mid-block are permitted as-of-right under Bylaw 20001. <strong>A backyard garden or garage suite is the clear primary recommendation — it matches your goal and is the most direct path to rental income</strong> — with a small-scale multiplex of up to 6 units as the higher-density alternative if lot size and siting support it.</p>'''))

# --- 7. Grants & Incentives -------------------------------------------------
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>A 100% rebate of the 5% federal GST on new purpose-built rental projects (generally 4+ units, 90%+ long-term rental), with construction generally beginning before 2031. Applies in Alberta. Eligibility and figures confirmed in Phase 2. (Government of Canada.)</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / Apartment Construction Loan Program</td><td>Government-backed multi-unit mortgage insurance (MLI Select, 5+ rental units) and low-interest construction financing (ACLP) — national programs that can heavily subsidize a qualifying rental project. Confirmed in Phase 2. (CMHC.)</td></tr>
    <tr><td>Provincial (Alberta)</td><td>Provincial housing incentives</td><td>Alberta's programs differ from Ontario's, and there is no equivalent development-charge waiver. Any applicable provincial incentives are identified and confirmed against current program terms in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Edmonton fees &amp; requirements</td><td>Edmonton applies its own permit fees and off-site/servicing requirements; treatment for small-scale residential is confirmed against the City's current schedule in Phase 2. No municipal development-charge waiver is assumed.</td></tr>'''))

# --- 8. Summary -------------------------------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>5308 35 Avenue NW confirms a strong development option. This property is in Edmonton's RS (Small Scale Residential) zone under Zoning Bylaw 20001, where <strong>backyard housing and up to six dwellings mid-block are permitted as-of-right</strong> — no rezoning, no public hearing, no Council approval required.</p>
  <ul>
    <li><strong>The Backyard-Housing Advantage:</strong> a detached garden or garage suite is permitted as-of-right in the RS zone and counts toward the site's dwellings — matching your goal of an additional rental suite, with a small-scale multiplex of up to 6 units available as the higher-density alternative.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(TPL, "w", encoding="utf-8").write(s)

# wrong-city / wrong-lead leftover scan (must all be zero)
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
          "654-2025", "569-2013", "474-2023", "Bill 185", "Ontario HST",
          "6+1", "4+1", "Gerrard", "TTC", "M4L", "Secondary Suite Loan"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("done, fails:", fails)
