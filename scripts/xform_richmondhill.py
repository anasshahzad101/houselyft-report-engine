"""
xform_richmondhill.py — turn the House Lyft master into the report for
Alexander Fernandez, 282 Palmer Avenue, Richmond Hill, ON.

City #: Richmond Hill (York Region). Zoning verified live via the
property_lookup_v2 Richmond Hill adapter (CZBL 93-25 Schedule A):
  Zone N2 (Neighbourhood Two); up to 4 units as-of-right via the ARU
  pathway (By-laws 143-24/144-24, Dec 2024 — first York Region city at 4).
Scope: sentence field "triplex or 4plex" -> fourplex is the stated goal.
Imagery: no verified licensed lot-scale source for Richmond Hill ->
  placeholder boxes removed, honest pending line kept (routine step 4b).
Program gating (config/programs.json, Richmond Hill @ <=4 units):
  Toronto DC waiver DROP (Toronto only); MLI Select / Prefab Plus DROP
  (5-unit min, unreachable on a 4-max lot); Bill 23 DC exemption CLEARS;
  GST/HST PBRH conditional at the 4-unit rental configuration.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_282_palmer.html")

s = open(SRC).read()
R = []

# ---- cover ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">282 Palmer Avenue<span>Richmond Hill, ON</span></div>'))

# ---- Property Details: imagery block (no licensed source for Richmond Hill) ----
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imglicense" style="font-size:8pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>'''))

# ---- Property Details: barhead ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">282 Palmer Avenue, Richmond Hill, ON&nbsp;&nbsp;L4C 1P3</div>'))

# ---- Property Details: contact table ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>282 Palmer Avenue, Richmond Hill, ON&nbsp;&nbsp;L4C 1P3</td></tr>
    <tr><td>Name</td><td>Alexander Fernandez</td></tr>
    <tr><td>Phone Number</td><td>(226) 582-9197</td></tr>
    <tr><td>Email</td><td>acarden4@uwo.ca</td></tr>
    <tr><td>Development Goals</td><td>Triplex or fourplex multiplex on the property (per intake)</td></tr>'''))

# ---- Property Details: property table ----
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
'''    <tr><td>Municipality</td><td>Richmond Hill (York Region)</td></tr>
    <tr><td>Neighbourhood</td><td>Beverley Acres</td></tr>
    <tr><td>Region</td><td>York Region</td></tr>
    <tr><td>Property Type</td><td>Residential lot (per intake)</td></tr>
    <tr><td>Waste Collection</td><td>City of Richmond Hill curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Richmond Hill Comprehensive Zoning By-law 93-25</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Fourplex (primary); triplex (alternative)</td></tr>'''))

# ---- Neighbourhood spotlight ----
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
    282 Palmer Avenue is in Beverley Acres, an established residential neighbourhood in central Richmond Hill within York Region:
    <ul>
      <li>Close to Yonge Street — Richmond Hill's main commercial and transit spine</li>
      <li>York Region Transit (Viva) bus rapid transit runs along the Yonge corridor</li>
      <li>Established, family-oriented streets — the kind of character stock that rents well and holds value</li>
      <li>Walkable to local schools, parks, shops, and services</li>
      <li>Richmond Hill GO station provides regional rail service toward downtown Toronto (illustrative context, not a valuation)</li>
    </ul>'''))

# ---- Section 2: zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>N2 — Neighbourhood Two (Richmond Hill Comprehensive Zoning By-law 93-25)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) — the basis on which additional residential units are permitted. Site standards (setbacks, height, lot coverage, parking) confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Richmond Hill permits up to <strong>4 units as-of-right</strong> on an urban residential lot via the additional-residential-unit (ARU) pathway (By-laws 143-24/144-24 with OPA 58, in force December 2024) — the first York Region municipality to reach four. No rezoning required. Note: the new Comprehensive Zoning By-law 93-25 is under appeal at the Ontario Land Tribunal; the governing by-law text is confirmed in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>A principal dwelling plus up to three additional residential units (maximum one in a detached accessory building) — <strong>up to 4 units total</strong> — subject to Richmond Hill's site standards. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- Section 2: what this means for you ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> up to four self-contained residential units on the lot via the additional-residential-unit pathway — matching your stated goal</li>
      <li><strong>Internal Secondary Suites:</strong> additional units within the principal dwelling (for example a basement apartment)</li>
      <li><strong>Detached Additional Unit:</strong> one of the additional units may sit in a detached accessory building in the rear yard (garden-suite form)</li>
      <li><strong>Established-neighbourhood standards apply:</strong> setbacks, height, lot coverage and parking are set by By-law 93-25 and confirmed in Phase 2</li>'''))

# ---- Time-sensitive block ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">ARU Development-Charge Exemption</div><div class="dx">Under Ontario's Bill 23, additional residential units are exempt from development charges — a meaningful per-unit saving as you add units to the property. The exemption and how it applies across your unit configuration are confirmed for your project in Phase 2.</div></div>
    <div class="d"><div class="dt">Comprehensive Zoning By-law 93-25 — Under Appeal</div><div class="dx">Richmond Hill's new Comprehensive Zoning By-law 93-25 is currently under appeal at the Ontario Land Tribunal (OLT-25-000843). Until the appeal resolves, a legacy parent by-law may govern parts of the transition. This does not change the province-wide four-unit permission, but the exact governing standards for your lot are confirmed in Phase 2 — a reason to start the file early.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- Section 3: rezoning "not required" callout ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended fourplex configuration is permitted as-of-right under Richmond Hill By-laws 143-24/144-24 (Dec 2024) via the additional-residential-unit pathway.</div>'))

# ---- Section 3: as-of-right comparison table ----
R.append(('''    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
          '''    <tr><td>What governs your build</td><td class="g">By-laws 143-24/144-24</td><td class="n">A new site-specific by-law</td></tr>'''))

# ---- Section 3: also-permitted twocard ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Up to four units</div>Richmond Hill permits a principal dwelling plus up to three additional residential units on an urban residential lot as-of-right (By-laws 143-24/144-24) — no rezoning required.</div>
    <div class="card2"><div class="ct">Detached additional unit</div>One of the additional units may take a detached (garden-suite) form in the rear yard, subject to the City's site standards. Confirmed in Phase 2.</div>'''))

# ---- Section 3: "what this means for {address}" ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 282 Palmer Avenue</div>
  <p>Because 282 Palmer Avenue already permits the recommended fourplex under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2.</b><br><span class="sub">The governing standards while Comprehensive Zoning By-law 93-25 is under OLT appeal, and whether a purpose-built multiplex teardown (versus adding units via the ARU pathway) affects the approval route on this lot.</span></div>'''))

# ---- Section 4: Option A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex (3 Units)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A principal dwelling plus two additional residential units — a triplex — permitted as-of-right on this serviced residential lot via Richmond Hill's ARU pathway (By-laws 143-24/144-24). No rezoning. The additional units may be interior (for example a basement suite) or one may take a detached form in the rear yard. Site standards — setbacks, height, lot coverage and parking under By-law 93-25 — are confirmed in Phase 2. This is a solid, lower-complexity route to rental income while staying comfortably within the as-of-right envelope.</div>'''))

# ---- Section 4: Option B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Fourplex (4 Units) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A principal dwelling plus three additional residential units — a fourplex — the maximum permitted as-of-right in Richmond Hill (By-laws 143-24/144-24, the first York Region municipality to reach four). Total: 4 independent units. This matches your stated goal. Up to one of the additional units may sit in a detached accessory building in the rear yard; the rest are within or attached to the principal dwelling. A minor variance may be required depending on the final design footprint. Setbacks, height, lot coverage and parking are set by By-law 93-25 and confirmed in Phase 2.</div>'''))

# ---- Section 4: Option C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Notes on the ARU Pathway &amp; Phase 2 Confirmations</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Richmond Hill's four-unit permission is delivered through the additional-residential-unit (ARU) pathway rather than a purpose-built multiplex zone. Two items are confirmed in Phase 2 before design: (1) the governing standards while Comprehensive Zoning By-law 93-25 is under appeal at the Ontario Land Tribunal (OLT-25-000843) — a legacy parent by-law may apply to parts of the transition; and (2) whether your preferred build is delivered by adding units to the existing dwelling or by a teardown-and-rebuild, which can change the approval route. Parking treatment (tandem parking is generally permitted, with narrow-frontage exemptions) is also confirmed against the final site plan.</div>'''))

# ---- Section 5: development goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Fourplex Configuration</div>
  <p>282 Palmer Avenue is a serviced residential lot in Richmond Hill, where up to four units are permitted as-of-right via the ARU pathway (By-laws 143-24/144-24) — Richmond Hill being the first York Region municipality to reach four. This matches your stated goal of a triplex or fourplex. <strong>The fourplex is the clear primary recommendation</strong>, with a triplex as a lower-complexity alternative.</p>'''))

# ---- Section 7: grants table (gated for Richmond Hill @ <=4 units) ----
R.append(('''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->
    </table>''',
'''    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Additional residential units are exempt from development charges under Ontario's More Homes Built Faster Act (Bill 23). This applies to the additional units you add to the property. How the exemption maps across a triplex or fourplex configuration is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>At the four-unit configuration built as purpose-built rental (4+ self-contained rental units, 90%+ long-term rental, construction started before 2031), a 100% rebate of the federal GST component may apply, with Ontario mirroring the provincial portion. Eligibility for your specific build is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>Where an additional unit will house an eligible senior or a relative eligible for the Disability Tax Credit, this credit may return 15% on up to $50,000 of eligible cost. Applicability confirmed in Phase 2.</td></tr>
    </table>'''))

# ---- Section 8: summary — current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>282 Palmer Avenue confirms a strong development option. This serviced residential lot in Richmond Hill permits up to <strong>four units as-of-right</strong> via the additional-residential-unit pathway (By-laws 143-24/144-24, in force December 2024) — Richmond Hill being the first York Region municipality to reach four. That directly supports your stated goal of a triplex or fourplex, with no rezoning required.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> a principal dwelling plus up to three additional residential units — no rezoning, no public hearing, no Council approval required — subject to the City's site standards, which are confirmed in Phase 2.</li>
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

# ---- leftover check: nothing from the source city / wrong-city programs ----
BANNED = ["Coxwell", "Toronto", "John Arockiaraj", "Ward 19", "Beaches", "654-2025",
          "6+1", "Bill 185", "TTC", "Gerrard", "MLI Select", "ACLP", "Prefab",
          "Canada Secondary Suite", "free grant", "guaranteed return"]
for t in BANNED:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

print(f"done. replacements applied: {len(R) - fails}/{len(R)}, fails: {fails}")
print(f"output: {OUT}")
