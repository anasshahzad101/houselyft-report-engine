"""
xform_burnaby.py — turn the House Lyft master into the Burnaby R1 SSMUH report.

Lead: Hank Bhaloo — 6685 Broadway, Burnaby, BC V5B 2Y6.
City has NO engine adapter -> rules researched live from official City of Burnaby
sources (R1 Small-Scale Multi-Unit Housing District; adopted Jun 10 2024, in
effect Jul 1 2024, amended Oct 14 2025) + BC Bill 44 (SSMUH). Report is tagged
report-needs-review; every dimensional / incentive figure is hedged to Phase 2.

Run from templates/ (operates in place on report_burnaby.html).
"""
import os

os.chdir(os.path.join(os.path.dirname(__file__), "..", "templates"))
s = open("report_burnaby.html").read()
R = []

# ---- cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">6685 Broadway<span>Burnaby, BC</span></div>'))

# ---- 1. property details: barhead ------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">6685 Broadway, Burnaby, BC&nbsp;&nbsp;V5B 2Y6</div>'))

# ---- 1. imagery row: no licensed source for Burnaby -> honest line, no boxes -
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 12px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# ---- 1. property contact table ---------------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>6685 Broadway, Burnaby, BC&nbsp;&nbsp;V5B 2Y6</td></tr>
    <tr><td>Name</td><td>Hank Bhaloo</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Garden suite, laneway home or ADU; build additional space for rental</td></tr>'''))

# ---- 1. property municipality table ----------------------------------------
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
'''    <tr><td>Municipality</td><td>City of Burnaby</td></tr>
    <tr><td>Region</td><td>Metro Vancouver — North Burnaby (Broadway corridor)</td></tr>
    <tr><td>Current Zoning</td><td>R1 — Small-Scale Multi-Unit Housing (SSMUH) District (confirm exact designation on the City of Burnaby zoning map in Phase 2)</td></tr>
    <tr><td>Governing Bylaw</td><td>Burnaby Zoning Bylaw — R1 SSMUH District (adopted Jun 10 2024, in effect Jul 1 2024; amended Oct 14 2025)</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Burnaby for the local schedule</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA / BC Assessment)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (via BC Assessment) — the unit ceiling under R1 depends on lot area and transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Garden suite / laneway home / ADU for rental (primary); small-scale multiplex as an upside scenario</td></tr>'''))

# ---- 1. neighbourhood spotlight --------------------------------------------
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
    6685 Broadway sits in a residential part of North Burnaby, in the Broadway corridor within Metro Vancouver — an established, transit-served part of the city now opened up to gentle density under the new R1 rules:
    <ul>
      <li>Established single-family residential fabric now zoned R1 Small-Scale Multi-Unit Housing, permitting multiplex, laneway and secondary-suite forms</li>
      <li>Served by TransLink bus routes; SkyTrain (Millennium Line) stations are within the broader North Burnaby area — proximity to <em>frequent</em> transit is what can lift the unit ceiling to six (confirm the 400 m frequent-transit test in Phase 2)</li>
      <li>Walkable access to local shopping, schools and parks typical of the North Burnaby neighbourhoods</li>
      <li>Close to major routes connecting to Vancouver, the SFU/Burnaby Mountain area, and the Brentwood and Lougheed town centres</li>
      <li>Illustrative context only — not a valuation. Exact transit distances and amenities are confirmed in Phase 2.</li>
    </ul>'''))

# ---- 2. current zoning table -----------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>R1 — Small-Scale Multi-Unit Housing (SSMUH) District. In 2024 Burnaby consolidated its twelve former Residential (R) districts into this single R1 district (confirm the exact parcel designation on the City zoning map in Phase 2).</td></tr>
    <tr><td>Units Permitted (as-of-right)</td><td>Under BC's Bill 44 and Burnaby's R1 district, a former single-family lot may accommodate <strong>3 to 6 dwelling units</strong> depending on lot area and transit proximity: roughly 3 units on smaller lots, 4 units on larger lots, and up to 6 units where the lot is within about 400 m of frequent-transit service. Secondary suites count toward the total. The exact ceiling for this lot is confirmed against lot area and the frequent-transit test in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>SSMUH permissions came into effect Jul 1 2024. On Oct 14 2025 Council <strong>tightened the R1 envelope</strong> — reducing maximum height from four storeys to three, capping rear principal buildings at two storeys, cutting lot coverage, and raising parking minimums (with provincial limits on enforcing parking minimums on frequent-transit lots). Design to the current in-force schedule — confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Forms</td><td>Single-family dwelling plus secondary suite and/or laneway/garden home; cottage court (multiple detached dwellings on one lot); multiplex (3–6 units in one building); rowhouse; and duplex — all within the R1 district, subject to the built-form rules.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — a laneway/garden suite plus a secondary suite is squarely within the R1 permissions; proceed to Step 2 — <strong>Builder Ready Package™</strong> to confirm the exact unit ceiling and envelope.</td></tr>'''))

# ---- 2. "what this means for you" list -------------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Multiplex (3–6 units):</strong> A single small-scale building with three to six dwelling units — the higher-density path under R1</li>
      <li><strong>Rowhouse &amp; Duplex:</strong> Ground-oriented attached homes permitted within the R1 district</li>
      <li><strong>Laneway / Garden Home:</strong> A detached rear dwelling — the form that most directly matches your rental goal</li>
      <li><strong>Secondary Suite:</strong> A self-contained suite within the principal dwelling; it counts toward the lot's unit total and pairs well with a laneway home</li>'''))

# ---- Time-Sensitive section (whole inner block) ----------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Burnaby R1 Envelope Tightened<br><small>in force since Oct 14, 2025</small></div><div class="dx">On October 14, 2025 Burnaby Council reduced the R1 small-scale envelope — from four storeys to three, a two-storey cap on rear principal buildings, reduced lot coverage, and higher parking minimums (subject to provincial limits on frequent-transit lots). Designing to the current rules from Day 1 avoids a costly redesign. The exact schedule in force for this lot is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>time-limited</small></div><div class="dx">The federal Enhanced GST Rental Rebate provides a 100% rebate of the 5% GST on new purpose-built rental housing (4+ units, 90%+ long-term rental), with construction-start timing conditions. If your build is structured as purpose-built rental, this is a government-backed saving worth capturing — eligibility and timing confirmed in Phase 2. (British Columbia levies GST/PST, not HST, so there is no Ontario-style provincial HST rebate here.)</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy and program terms can change at any time, potentially affecting financing options. It is recommended to begin your application as early as possible to reduce that risk.</div></div>'''))

# ---- 3. rezoning: co-green -------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>A laneway/garden suite plus secondary suite — and a small-scale multiplex — are permitted as-of-right within Burnaby\'s R1 SSMUH District. No rezoning is contemplated in this analysis.</div>'))

# ---- 3. rezoning: comparison table -----------------------------------------
R.append(('''    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
          '''    <tr><td>What governs your build</td><td class="g">Burnaby R1 SSMUH District</td><td class="n">A new site-specific by-law</td></tr>'''))
# swap the OLT row (BC uses no OLT)
R.append(('''    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>''',
          '''    <tr><td>Appeal / public-hearing exposure</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>'''))

# ---- 3. rezoning: two cards ------------------------------------------------
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Small-scale multiplex</div>Burnaby's R1 district permits a 3–6 unit multiplex on a former single-family lot without rezoning, with the exact ceiling set by lot area and frequent-transit proximity (confirmed in Phase 2).</div>
    <div class="card2"><div class="ct">Laneway / garden home + suite</div>A detached rear (laneway/garden) home and a secondary suite are permitted forms within R1 — the combination that most directly matches your rental goal.</div>'''))

# ---- 3. rezoning: "what this means for X" + amber --------------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 6685 Broadway</div>
  <p>Because the R1 district already permits the laneway/garden-suite and multiplex forms, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the rules understood to be in force at the date of this report, was researched from public City of Burnaby sources, and is subject to confirmation of the exact parcel designation and technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2:</b><br><span class="sub">(1) the exact unit ceiling for this lot — set by confirmed lot area and the 400 m frequent-transit test; and (2) the current R1 built-form schedule (height, lot coverage, setbacks, parking) following the October 2025 amendments.</span></div>'''))

# ---- 4. development options -------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Laneway / Garden Home + Secondary Suite (your stated goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">The path that most directly matches your goal: keep (or rebuild) the principal dwelling, add a detached laneway/garden home at the rear for rental, and add a secondary suite within the principal dwelling. Under Burnaby's R1 district these are permitted forms, and the secondary suite counts toward the lot's unit total. This is the lowest-complexity way to create rental income on the lot. Final unit sizes, siting and rear-yard fit are set against the current R1 built-form schedule and the confirmed lot area in Phase 2.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small-Scale Multiplex (3–6 units) — density upside</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The higher-density scenario: a single small-scale multiplex of three to six dwelling units. The exact ceiling depends on confirmed lot area and whether the lot falls within about 400 m of frequent-transit service (which can lift the maximum to six). This path yields more rental units than Option A but is more design- and cost-intensive, and must be shaped to the tighter post-October-2025 R1 envelope (three storeys, reduced lot coverage, updated parking). Phase 2 confirms the achievable unit count and massing.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Confirming What This Lot Can Carry</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Before locking a design, two determinants decide how far this lot can go under R1: the confirmed lot area (which sets the 3-vs-4 unit tier) and the 400 m frequent-transit test (which can unlock six). Any existing rear structure should have its permit status confirmed so it can count as a legal unit rather than trigger a retroactive application. These are the first checks in the Builder Ready Package™, and they turn the ranges in this report into firm numbers.</div>'''))

# ---- 5. development goal summary -------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Laneway / Garden Suite for Rental</div>
  <p>6685 Broadway is in Burnaby's R1 Small-Scale Multi-Unit Housing District, which permits a laneway/garden home plus a secondary suite as-of-right on a former single-family lot. <strong>That laneway-plus-suite path is the primary recommendation — it matches your rental goal directly</strong> — with a small-scale multiplex (up to six units, subject to lot area and transit proximity) as the density-upside scenario. The exact unit ceiling and built-form limits are confirmed in Phase 2.</p>'''))

# ---- 7. grants table (replace the 4 Toronto rows) --------------------------
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td colspan="3" style="background:#fbf1de;color:#7d5a17;font-weight:600;">These items were researched live from public federal, provincial and City of Burnaby sources for a municipality not yet in the engine. Treat every figure below as government-backed financing options to be confirmed in Phase 2 — none is a promised grant.</td></tr>
    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>A 100% rebate of the 5% federal GST on new purpose-built rental projects (generally 4+ units, 90%+ long-term rental), with construction-start timing conditions. British Columbia levies GST/PST rather than HST, so there is no Ontario-style provincial HST component here. Applies to the purpose-built rental scenario — eligibility and amounts confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction loans for purpose-built rental (typical minimum loan and eligibility thresholds apply). Can be structured to bridge into MLI Select permanent financing at completion. Applicability to a small-scale project confirmed in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td><td>The provincial legislation that requires Burnaby to permit 3–6 small-scale units on former single-family lots. This is what unlocks the density on your lot as-of-right — it is an enabling framework, not a cash grant.</td></tr>
    <tr><td>Municipal</td><td>City of Burnaby — R1 SSMUH permissions &amp; fees</td><td>The R1 district permits the laneway/suite and multiplex forms without rezoning. Applicable City charges (e.g. development cost charges / community amenity contributions) and any fee reductions differ from Ontario's development-charge model — the exact charges and any waivers for this project are confirmed in Phase 2.</td></tr>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:60]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open("report_burnaby.html", "w").write(s)

print("\n--- leftover check (should all be zero) ---")
for t in ["Coxwell", "Ward 19", "Beaches", "John Arockiaraj", "654-2025", "474-2023",
          "Ontario HST", "Bill 185", "6+1 Config", "Toronto", "TTC", "Garden Suite By-law",
          "johneeraj", "569-2013"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print("\ndone, fails:", fails)
