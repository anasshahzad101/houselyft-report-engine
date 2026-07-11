"""
xform_edmonton.py — turn the House Lyft master into the Edmonton (RS) report.

Property : 8411 42A Avenue NW, Edmonton, AB  T6K 1C7  (David Simonic)
Zoning   : RS — Small Scale Residential, Edmonton Zoning Bylaw 20001
           (verified live via gis.edmonton.ca ZoningWebApp, 2026-07-11)

Same contract as the other xform_*.py: every (old -> new) must match EXACTLY
once, then a leftover grep proves no Toronto / Coxwell / Ontario-program text
survives. House Lyft prose sections (Why / How to use / Advantage / Financing
intro / Grants intro / Next Steps / Roadblocks / CTA) are kept verbatim.

Grounding rules honoured:
  - Only engine output + live official gov/municipal facts are stated.
  - No Ontario-only programs (HST 8% rebate, Bill 185 DC waiver) — Alberta has
    no PST and no DC-waiver equivalent.
  - No invented program dollar figures. The Edmonton Secondary Suite grant is
    named but its amount is left to Phase 2 (not verifiable from an official
    source at render time).
  - Canada Secondary Suite Loan Program is never cited (never implemented).
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(HERE, "..", "templates", "report_edmonton.html")
s = open(PATH).read()
R = []

# --- cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">8411 42A Avenue NW<span>Edmonton, AB</span></div>'))

# --- property details: barhead ----------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">8411 42A Avenue NW, Edmonton, AB&nbsp;&nbsp;T6K 1C7</div>'))

# --- property details: imagery licence credit -------------------------------
R.append(('<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>',
          '<div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: property, zoning and ward context from City of Edmonton Open Data (gis.edmonton.ca), retrieved 2026-07-11. Aerial and street-level photography pending a licensed imagery source.</div>'))

# --- property details: contact table ----------------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>8411 42A Avenue NW, Edmonton, AB&nbsp;&nbsp;T6K 1C7</td></tr>
    <tr><td>Name</td><td>David Simonic</td></tr>
    <tr><td>Phone Number</td><td>(780) 903-4425</td></tr>
    <tr><td>Email</td><td>dsimonic@hotmail.com</td></tr>
    <tr><td>Development Goals</td><td>Garden / garage suite in the rear alley (backyard housing); open to a broader small-scale multi-unit build</td></tr>'''))

# --- property details: municipality table -----------------------------------
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
    <tr><td>Neighbourhood</td><td>Tweddle Place (Mill Woods)</td></tr>
    <tr><td>Ward</td><td>Karhiio Ward (Councillor Keren Tang)</td></tr>
    <tr><td>Community League</td><td>North Millbourne Community League</td></tr>
    <tr><td>Waste Collection</td><td>Contact the City of Edmonton (311) for the local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Edmonton Zoning Bylaw 20001 (in force Jan 1, 2024)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — mid-block vs. corner status sets the unit ceiling</td></tr>
    <tr><td>Development Goals</td><td>Backyard (garden/garage) suite (primary); up to a 6-dwelling small-scale build (upside)</td></tr>'''))

# --- property details: neighbourhood spotlight ------------------------------
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
    8411 42A Avenue NW is in Tweddle Place, an established residential neighbourhood in Edmonton's Mill Woods area (Karhiio Ward). Per the City's neighbourhood profile, Tweddle Place reflects the "compact development" philosophy of early Mill Woods, with a genuine mix of housing types:
    <ul>
      <li>The City records the housing mix as roughly 50% single detached, 21% row housing, and 26% low-rise apartments — an area already accustomed to gentle density</li>
      <li>Focused on a multi-purpose school and recreation site at the heart of the neighbourhood</li>
      <li>Well connected to the wider Mill Woods area by Edmonton Transit Service; Mill Woods Town Centre and the Valley Line LRT are nearby (illustrative context, not a valuation)</li>
      <li>Served by the North Millbourne Community League</li>
      <li>Note: exact lot dimensions, servicing, and any easements or accessory-structure permits shape what is buildable — confirmed during the feasibility phase</li>
    </ul>'''))

# --- section 2: current zoning table ----------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RS — Small Scale Residential (Edmonton Zoning Bylaw 20001)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The RS zone permits small-scale residential development up to 3 storeys — including detached, semi-detached/attached, row, and multi-unit housing — plus backyard housing (garden and garage suites). Applicable setbacks, height, lot coverage, and site standards are confirmed against the lot during the feasibility phase.</td></tr>
    <tr><td>Recent Changes</td><td>Under Zoning Bylaw 20001 (in force Jan 1, 2024), and following the 2025 one-year-review amendments, the RS zone permits up to <strong>6 dwellings on a mid-block lot as-of-right</strong> (reduced from 8), with up to 8 on corner sites; developments of more than 8 dwellings are limited to corner sites. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>Small-scale residential housing types — detached, semi-detached, row and multi-unit — plus backyard (garden/garage) suites, which are permitted and count toward the lot's total dwelling count.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- section 2: "what this means for you" list ------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Row Housing:</strong> Multi-unit attached homes sharing side walls, up to 3 storeys</li>
      <li><strong>Detached &amp; Semi-detached Multi-unit:</strong> Standalone or paired small-scale multi-unit homes</li>
      <li><strong>Small Multi-unit / Low-Rise:</strong> Up to 6 dwellings mid-block (8 on a corner site) as-of-right in the RS zone</li>
      <li><strong>Backyard Housing (Garden / Garage Suite):</strong> A rear suite off the alley — your stated goal — is permitted and counts toward the lot's total dwelling count</li>'''))

# --- time-sensitive section -------------------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">RS Height Cut-Off — Act Before Aug 1, 2026<br><small>time-sensitive</small></div><div class="dx">Edmonton Council approved a reduction in the RS maximum building height from 10.5 m to 9.5 m (approved April 27, 2026). The 9.5 m limit applies to development permit applications submitted on or after <strong>August 1, 2026</strong>. Filing before that date can preserve the taller 10.5 m envelope for your project. Confirm the current standard for your application in the feasibility phase.</div></div>
    <div class="d"><div class="dt">Federal GST Rental Rebate<br><small>build before 2031</small></div><div class="dx">The federal government's 100% rebate of the 5% GST on new purpose-built rental housing applies in Alberta. It requires a project of <strong>4 or more self-contained rental units</strong> with at least 90% long-term rental, construction begun after Sept 13, 2023 and before 2031. A single backyard suite does not qualify on its own; a 4-to-6-dwelling build does. Structuring the project as qualifying rental from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">Side-Entrance Setback Rule<br><small>in effect since Jul 8, 2025</small></div><div class="dx">In the RS zone, a maximum of two dwelling entrances may face an interior side lot line, and a side-facing entrance triggers a 1.9 m setback on that side. This can shape unit layout and access — factored into design during the feasibility phase. CMHC policy can also change at any time; applying early reduces financing risk.</div></div>'''))

# --- section 3: rezoning not-required callout -------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Both a backyard (garden/garage) suite and a small-scale multi-unit build up to the RS ceiling are permitted as-of-right under Edmonton Zoning Bylaw 20001 — no rezoning is contemplated in this analysis.</div>'))

# --- section 3: as-of-right vs rezoning comparison table --------------------
R.append(('''    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>''',
'''    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public hearing at Council</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal / hearing exposure</td><td class="g">Limited (permit-level review)</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">Zoning Bylaw 20001 (RS zone)</td><td class="n">A new site-specific rezoning</td></tr>'''))

# --- section 3: also-permitted twocard --------------------------------------
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Small-scale multi-unit</div>The RS zone permits up to 6 dwellings on a mid-block lot as-of-right (up to 8 on a corner site) under Zoning Bylaw 20001 — no rezoning.</div>
    <div class="card2"><div class="ct">Backyard (garden/garage) suite</div>A rear suite off the alley is permitted in the RS zone and counts toward the lot's total dwelling count — a direct fit for your stated goal.</div>
  </div>'''))

# --- section 3: "what this means for ..." heading + paragraph ----------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <div class="barhead" style="text-align:left;">What this means for 8411 42A Avenue NW</div>
  <p>Because the RS zone already permits both a backyard suite and a small-scale multi-unit build on this lot, no rezoning application is contemplated in this analysis. Your project advances directly to design and development permit. Whether the lot is mid-block or a corner site sets the exact dwelling ceiling (6 vs. 8) and is confirmed in the feasibility phase. This assessment reflects the by-law in force at the date of this report and is subject to technical review of site conditions.</p>'''))

# --- section 3: amber note --------------------------------------------------
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the status of any existing rear/accessory structure and the lot\'s corner vs. mid-block designation.</b><br><span class="sub">If an existing garage or structure would become a suite, its permit status must be confirmed; if it was altered without a permit, a retroactive application may be needed before financing or development can proceed.</span></div>'))

# --- section 4: development options ------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Backyard (Garden / Garage) Suite — Your Stated Goal</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Keep the principal home and add one backyard suite off the rear alley — a garden suite or a garage suite (a suite above or attached to a garage). This is your stated goal and the lowest-complexity path to rental income. In the RS zone the suite is permitted as-of-right and counts toward the lot's total dwelling count. Suite size, siting, and the interior side-entrance rules (max two entrances facing an interior side lot line; a side entrance triggers a 1.9 m setback) are worked out at design. Existing accessory-structure and servicing details are confirmed in the feasibility phase.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Small-Scale Multi-Unit (up to 6 dwellings) — Upside</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Redevelop toward the RS ceiling: up to 6 dwellings on a mid-block lot as-of-right (up to 8 on a corner site), which can include a backyard suite in the count. This is the higher-density, stronger-income direction and — at 4 or more self-contained rental units — is the path that can qualify for the federal GST purpose-built rental rebate. Height envelope is currently 10.5 m (9.5 m for applications from Aug 1, 2026). Final dwelling count depends on lot size and corner vs. mid-block status, confirmed in the feasibility phase.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Phased Path (suite now, redevelop later)</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">A staged approach: add the backyard suite now to start generating rental income, then evaluate a fuller small-scale multi-unit build later while the RS permissions remain in force. If any redevelopment is likely before Aug 1, 2026, filing that application ahead of the height cut-off preserves the 10.5 m envelope. Confirming any existing accessory structure's permit status is an essential first step for both financing qualification and counting it as a legal unit.</div>'''))

# --- section 5: development goal summary -------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Backyard suite now, with multi-unit upside</div>
  <p>8411 42A Avenue NW is an RS (Small Scale Residential) lot under Edmonton Zoning Bylaw 20001. A backyard (garden/garage) suite — your stated goal — is permitted as-of-right and is the recommended first move. <strong>The lot also carries genuine upside: up to 6 dwellings mid-block (8 on a corner site) as-of-right</strong>, which, at 4+ rental units, opens the door to the federal GST rental rebate. Confirming lot size and corner status is the single most valuable next step.</p>'''))

# --- section 7: grants & incentives table -----------------------------------
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Federal</td><td>GST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects of <strong>4 or more self-contained units</strong>, with at least 90% long-term rental. Construction must have begun after Sept 13, 2023 and before 2031. Applies in Alberta; there is no provincial-sales-tax component (Alberta has no PST). A single backyard suite does not qualify on its own. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select / Apartment Construction Loan Program</td><td>MLI Select multi-unit mortgage insurance (minimum 5 rental units) and the Apartment Construction Loan Program (low-interest construction financing, minimum $1M loan) — national programs that can materially reduce the cost of a qualifying rental project. Fit and current terms confirmed in Phase 2.</td></tr>
    <tr><td>Provincial / Federal</td><td>Accessory suite (ARU) treatment</td><td>Additional/accessory residential units (garden and garage suites) are supported by provincial and federal housing measures; the specific tax and financing treatment for this project is confirmed against current program rules in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Edmonton Secondary Suite (Cornerstones) Grant</td><td>The City of Edmonton offers a grant supporting new and upgraded secondary, garage, and garden suites. Edmonton has no Ontario-style development-charge waiver; Alberta municipalities use off-site levies instead. Current intake, the exact grant amount, and eligibility for this property are confirmed with the City in Phase 2.</td></tr>'''))

# --- section 8: summary — current zoning review -----------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>8411 42A Avenue NW confirms a strong development option. This property is zoned <strong>RS — Small Scale Residential</strong> under Edmonton Zoning Bylaw 20001, which permits a backyard (garden/garage) suite — the owner's stated goal — as-of-right, and allows up to <strong>6 dwellings on a mid-block lot (8 on a corner site) as-of-right</strong>. No rezoning, public hearing, or Council approval is required for either path.</p>
  <ul>
    <li><strong>The As-of-Right Advantage:</strong> a rear alley suite and a small-scale multi-unit build are both permitted outright in the RS zone — and a 4-or-more-unit build can qualify for the federal GST rental rebate. The key time-sensitive item is the RS height cut-off on Aug 1, 2026.</li>
  </ul>'''))

# ---------------------------------------------------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

open(PATH, "w").write(s)

# leftover check — no source-city / wrong-program text may survive
LEFTOVERS = ["Coxwell", "Toronto", "Ontario", "Ward 19", "Beaches", "John Arockiaraj",
             "654-2025", "474-2023", "569-2013", "Bill 185", "HST", "6+1", "4+1",
             "Gerrard", "TTC", "Garden Suite By-law", "OLT", "Danforth", "houseplex",
             "Canada Secondary Suite Loan", "Provided at intake"]
print("--- leftover scan ---")
any_left = False
for t in LEFTOVERS:
    n = s.count(t)
    if n:
        # "Canada Secondary Suite Loan" is allowed ONLY inside the explicit
        # not-relied-on disclaimer; flag everything else.
        print(f"LEFTOVER {t!r}: {n}")
        any_left = True
if not any_left:
    print("clean — no leftovers")
print("done, fails:", fails)
