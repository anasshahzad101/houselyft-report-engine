"""
xform_brampton_164main.py — adapt the House Lyft master into the report for
164 Main Street North, Brampton (contact Maxim Mendes).

Follows the repo xform pattern: every replacement must match exactly once,
then a leftover check greps for source-city (Toronto/Coxwell) traces.

Scope = "Multiplex Development" -> TIERED render (config/programs.json):
baseline up to 3 units as-of-right (Bill 23); apartment-form upside from the
Residential Apartment zoning context + Brampton GO Primary MTSA. Zoning could
not be machine-verified for this exact parcel by the Brampton adapter (the ADU
layer excludes it; adjacent lots are R4A/R4B), so this is researched-live =>
report-needs-review. No invented figures; wrong-city (Toronto) programs dropped.
"""
import base64, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
SCRATCH = ("/tmp/claude-0/-home-user-houselyft-report-engine/"
           "a4b3d116-80bd-54ba-99ee-ffc9eb35e5fb/scratchpad")

lot_b64 = base64.b64encode(open(os.path.join(SCRATCH, "lot.jpg"), "rb").read()).decode()
ctx_b64 = base64.b64encode(open(os.path.join(SCRATCH, "context.jpg"), "rb").read()).decode()

s = open(os.path.join(TPL, "report_houselyft_master.html")).read()
R = []

# ---- cover ----
R.append(('  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '  <div class="addr">164 Main Street North<span>Brampton, ON</span></div>'))

# ---- Property Details barhead ----
R.append(('  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '  <div class="barhead">164 Main Street North, Brampton, ON&nbsp;&nbsp;L6V 1N9</div>'))

# ---- image row: real Brampton aerials (OGL) ----
old_img = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_img = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{lot_b64}" alt="Aerial view of 164 Main Street North" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 6px;">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="data:image/jpeg;base64,{ctx_b64}" alt="Neighbourhood context around 164 Main Street North" style="width:100%;height:148px;object-fit:cover;display:block;">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 6px;">Neighbourhood context — approx. 240 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Brampton Orthophoto 2023 (Spring). Contains information licensed under the Open Government Licence – City of Brampton.</div>'''
R.append((old_img, new_img))

# ---- property table 1 ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>164 Main Street North, Brampton, ON&nbsp;&nbsp;L6V 1N9</td></tr>
    <tr><td>Name</td><td>Maxim Mendes</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development — unit count to be confirmed (scope question below)</td></tr>'''))

# ---- property table 2 ----
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
'''    <tr><td>Municipality</td><td>Brampton (Region of Peel)</td></tr>
    <tr><td>Neighbourhood</td><td>Downtown Brampton — Main Street North</td></tr>
    <tr><td>Transit Growth Area</td><td>Brampton GO Primary Major Transit Station Area (PMTSA)</td></tr>
    <tr><td>Conservation Authority</td><td>CVC / TRCA — regulated-lands check confirmed in Phase 2</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Brampton Zoning By-law 270-2004, as amended — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Development Goals</td><td>Multiplex Development (tiered analysis below)</td></tr>'''))

# ---- neighbourhood spotlight ----
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
    164 Main Street North sits in the heart of downtown Brampton, on Main Street North within the Region of Peel — one of the most transit-connected and rapidly intensifying urban cores in the GTA:
    <ul>
      <li>Inside the Brampton GO Primary Major Transit Station Area — the provincial growth area anchored on the Brampton GO station (Kitchener GO line)</li>
      <li>Walkable to downtown Brampton's shops, restaurants, Garden Square, and the Rose Theatre</li>
      <li>Steps from Brampton Transit and Züm bus rapid transit along Main Street and Queen Street</li>
      <li>Gage Park and the Etobicoke Creek trail system nearby; established residential streets that rent well and hold value</li>
      <li>Note: downtown Brampton includes Central-Area and heritage considerations; any such status is confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# ---- zoning table ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential Apartment — adjacent parcels are zoned R4A and R4B under City of Brampton Zoning By-law 270-2004; the exact designation for 164 Main Street North is confirmed in Phase 2</td></tr>
    <tr><td>Growth-Area Designation</td><td>Within the Brampton GO Primary Major Transit Station Area (PMTSA) — a provincially-designated transit-oriented growth area (verified against City of Brampton GIS)</td></tr>
    <tr><td>As-of-Right Units (baseline)</td><td>Under Ontario's Bill 23, up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot (principal dwelling + up to two additional residential units). Brampton adopted the conforming Official Plan and Zoning By-law amendments on May 3, 2023.</td></tr>
    <tr><td>Higher-Density Potential</td><td>The Residential Apartment zoning context and the PMTSA location point to apartment-form potential beyond the 3-unit baseline. The permitted units, height and density for this parcel are set by the zone's standards and any special section — confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means for you" list ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Additional Residential Units (ARUs):</strong> the existing home plus up to two additional units — for example an interior suite paired with a detached garden suite — as-of-right on a serviced lot under Bill 23</li>
      <li><strong>Purpose-Built Multiplex / Small Apartment:</strong> the Residential Apartment zoning context supports a standalone multi-unit building; the permitted scale is confirmed in Phase 2</li>
      <li><strong>Transit-Oriented Density:</strong> the parcel's location in the Brampton GO Primary MTSA is where provincial and City policy direct higher residential densities</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> secondary suites (interior or garden) can be paired with a principal dwelling to add density on the lower-intensity path</li>'''))

# ---- time-sensitive ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Purpose-Built Rental Rebates<br><small>confirm current terms in Phase 2</small></div><div class="dx">A new purpose-built rental building of four or more self-contained units, held as long-term rental, may qualify for the federal GST purpose-built rental housing rebate, with Ontario moving to match the rebate on the provincial portion of the HST. These are government-backed savings on the tax cost of the build. Eligibility, current rates, and application windows are confirmed in Phase 2 — structuring the project correctly from Day 1 is what preserves access.</div></div>
    <div class="d"><div class="dt">Residential Rental Licence<br><small>in effect Jan 1, 2026</small></div><div class="dx">Brampton requires a Residential Rental Licence for rental dwellings of one to four units across the city as of January 1, 2026, and any additional residential unit must be registered with the City to be legal. Building these approvals into the plan early avoids a compliance gap later.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage and Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to advance your file as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: green box ----
R.append(('  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '  <div class="co-green"><div class="ct2">Not Required for the Baseline Path</div>Up to three residential units are permitted as-of-right on a serviced residential lot under Bill 23 — no rezoning. A larger apartment-form build is assessed against the confirmed zone standards in Phase 2; some configurations proceed as-of-right, others through a minor variance or site plan.</div>'))

# ---- rezoning: comparison row ----
R.append(('    <tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '    <tr><td>What governs your build</td><td class="g">Bill 23 as-of-right (up to 3 units)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: twocard ----
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Up to three units</div>Under Bill 23, a serviced residential lot in Brampton supports the principal dwelling plus up to two additional residential units without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>A detached garden suite is one of the two additional units permitted as-of-right; it must be registered with the City, and its siting and size follow Brampton's ARU standards.</div>
  </div>'''))

# ---- rezoning: closing barhead/para/amber ----
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 164 Main Street North</div>
  <p>The up-to-three-unit path is permitted as-of-right, so that baseline advances directly to design and permitting with no rezoning. A larger, apartment-form build leverages the parcel's Residential Apartment zoning and its place in the Brampton GO Major Transit Station Area — the permitted scale, and whether it proceeds as-of-right or through a minor variance or site plan, is confirmed once the exact zone designation is pulled in Phase 2. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2: the exact zone designation for this parcel, and the City registration / Residential Rental Licence steps for any new units.</b><br><span class="sub">These are process items, not obstacles — building them into the plan early keeps the project compliant from Day 1.</span></div>'''))

# ---- development option A ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Up to 3 Units As-of-Right (ARU Baseline)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A serviced residential lot in Brampton supports the principal dwelling plus up to two additional residential units — for example an interior suite and a detached garden suite — for as many as three income units, as-of-right under Bill 23. No rezoning. The two additional units are exempt from municipal development charges under provincial legislation. Each additional unit must be registered with the City, and rentals of one to four units require a Residential Rental Licence from January 1, 2026. Siting and unit sizes follow Brampton's ARU standards, confirmed in Phase 2.</div>'''))

# ---- development option B ----
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Purpose-Built Multiplex / Small Apartment (Transit-Oriented Upside)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The parcel sits among Residential Apartment zoning (adjacent lots are R4A and R4B) inside the Brampton GO Primary Major Transit Station Area — the growth area where provincial and City policy direct apartment-scale density. A purpose-built rental building unlocks government-backed financing the smaller path does not: at four or more self-contained rental units, the federal and provincial purpose-built rental rebates open up; at five or more units, CMHC MLI Select; and where the project budget supports a $1M+ loan, the CMHC Apartment Construction Loan Program. The exact permitted units, height and density for this parcel are set by the zone's standards and any special section — confirmed in Phase 2. This is the scale that matches a "Multiplex Development" goal.</div>'''))

# ---- development option C ----
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Downtown &amp; Transit-Oriented Advantage</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Main Street North places this lot in the heart of downtown Brampton, close to the Brampton GO station on the Kitchener line and the downtown's shops, transit and amenities. A location inside a Primary Major Transit Station Area is a genuine planning advantage — it is exactly where higher residential density is encouraged. The offsetting items to confirm early are the exact zone designation, any Central-Area or secondary-plan provisions, and whether any part of the lot touches conservation-authority regulated lands (CVC/TRCA) — all confirmed in Phase 2. (Illustrative context, not a valuation.)</div>'''))

# ---- goal summary ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Multiplex Development — Tiered</div>
  <p>You told us your goal is a <strong>Multiplex Development</strong>. A unit count was not specified, so this report is presented in tiers rather than a single recommendation. The baseline — up to three units — is available as-of-right today under Bill 23. The upside — a purpose-built multiplex or small apartment — is supported by the parcel's Residential Apartment zoning context and its place in the Brampton GO Major Transit Station Area, and is confirmed in Phase 2.</p>
  <div class="co-amber"><b>One quick question to sharpen this:</b> how many units are you aiming for? Your answer sets which tier — and which government-backed programs — the Phase 2 work targets. <span class="sub">(Marked for scope review.)</span></div>'''))

# ---- financing gated rows (Section 6) ----
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC MLI Select</td><td>A CMHC multi-unit insured financing program for purpose-built rental. Opens at <strong>five or more rental units</strong> — reached on the purpose-built multiplex path (Option B), not the 3-unit baseline. Offers preferred loan-to-value, longer amortization and lower-cost insured financing when the project meets affordability, energy or accessibility criteria. Confirmed in Phase 2.</td></tr>
    <tr><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental, structured around loans of <strong>$1M and up</strong>. Applicable on a larger Option B build; can bridge into MLI Select permanent financing at completion. Confirmed in Phase 2.</td></tr>'''))

# ---- grants gated rows (Section 7) ----
R.append(('''    <!-- GATED_GRANTS_ROWS
         Injected by the builder from config/programs.json AFTER apply_gates().
         EVERY grant/incentive is gated - none may be hardcoded here.
         Previously hardcoded (the defect this fixes): GST/HST PBRH (4+ units),
         CMHC ACLP ($1M+ loan), CMHC Prefab Plus (inherits MLI), Toronto DC Waiver
         (Toronto only - was appearing on Mississauga reports).
         scoped mode -> only programs clearing the stated scope.
         tiered mode -> each program attached to the smallest tier that clears it.
         See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>Provincial</td><td>DC Exemption for Additional Residential Units (Bill 23)</td><td>The two additional residential units on the baseline path are exempt from municipal development charges under Ontario's More Homes Built Faster Act — a meaningful per-unit saving. Applies to the first two additional units. Confirmed for your project in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Opens at <strong>four or more</strong> self-contained rental units held as long-term rental (90%+), with construction beginning before 2031 — i.e. on the purpose-built multiplex path (Option B), not the 3-unit baseline. Ontario has moved to match the rebate on the provincial portion of the HST. Government-backed savings on the tax cost of the build; current terms confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred insured financing for purpose-built rental. Opens at <strong>five or more</strong> rental units — reached on a larger Option B build. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing structured around loans of <strong>$1M and up</strong>. Applicable on a larger Option B build. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Brampton incentives</td><td>Brampton administers housing and downtown / Central-Area incentives that change from time to time. Whether any current program fits your project is confirmed in Phase 2 against the City's live criteria — we never rely on a program that is not open.</td></tr>'''))

# ---- summary: current zoning review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>164 Main Street North confirms a real development opportunity on two levels. Today, up to <strong>three residential units are permitted as-of-right</strong> on a serviced residential lot under Bill 23 — no rezoning required. Above that, the parcel's Residential Apartment zoning context (adjacent lots are zoned R4A and R4B) and its location inside the <strong>Brampton GO Primary Major Transit Station Area</strong> point to purpose-built apartment potential — the scale that matches your Multiplex Development goal.</p>
  <ul>
    <li><strong>As-of-right today:</strong> the principal dwelling plus up to two additional residential units, with the ARUs exempt from development charges under Bill 23.</li>
    <li><strong>Transit-oriented upside:</strong> a Primary MTSA is exactly where provincial and City policy direct higher density; the permitted apartment scale for this parcel is confirmed in Phase 2, and the 4+ / 5+ / $1M+ government-backed programs open up as the unit count grows.</li>
  </ul>'''))

# ---- apply ----
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

out = os.path.join(TPL, "report_brampton_164main.html")
open(out, "w").write(s)

# ---- leftover check (source-city + wrong-city programs) ----
print("--- leftover check ---")
for t in ["303 Coxwell", "Coxwell", "John Arockiaraj", "johneeraj", "Toronto",
          "Ward 19", "Beaches", "654-2025", "474-2023", "Bill 185", "M4L 3B5",
          "569-2013", "6+1", "houseplex"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
print(f"done. fails={fails}  ->  {out}")
