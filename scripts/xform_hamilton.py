"""
xform_hamilton.py — turn the House Lyft master report into the Hamilton report
for 507 Upper Paradise Road (contact: Mike Taller; goal: basement / second unit).

Hamilton has no zoning-engine adapter, so this is a report-needs-review build.
Facts below come from live official City of Hamilton sources (Zoning By-law
05-200 pages + ADU/SDU by-law history) and provincial legislation; anything not
verifiable per-lot gets the hedged "confirm in Phase 2" treatment.

Discipline (per scripts/xform_*.py): every replacement must match EXACTLY once,
then grep for source-city leftovers before the file is allowed to render.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_hamilton.html")

s = open(SRC, encoding="utf-8").read()
R = []

# ---- cover ------------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">507 Upper Paradise Road<span>Hamilton, ON</span></div>'))

# ---- property barhead -------------------------------------------------------
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">507 Upper Paradise Road, Hamilton, ON&nbsp;&nbsp;L9C 2E5</div>'))

# ---- imagery slots + licence line (no licensed source for this city) --------
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
'''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(added in Phase 2)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(added in Phase 2)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: no licensed aerial or street-view source is included at this preliminary phase; site imagery is added during the feasibility phase.</div>'''))

# ---- property table 1 (name / contact / goals) ------------------------------
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>507 Upper Paradise Road, Hamilton, ON&nbsp;&nbsp;L9C 2E5</td></tr>
    <tr><td>Name</td><td>Mike Taller</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Add a basement (internal) secondary unit for rental income; option to add a detached unit</td></tr>'''))

# ---- property table 2 (municipality block) ----------------------------------
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
'''    <tr><td>Municipality</td><td>City of Hamilton</td></tr>
    <tr><td>Neighbourhood</td><td>Gilbert (Hamilton Mountain / West Mountain)</td></tr>
    <tr><td>Property Type</td><td>Single detached (per intake) — confirm in Phase 2</td></tr>
    <tr><td>Waste Collection</td><td>City of Hamilton curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Hamilton Zoning By-law No. 05-200 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Internal (basement) secondary unit; optional detached unit — up to 3 units total</td></tr>'''))

# ---- neighbourhood spotlight ------------------------------------------------
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
    507 Upper Paradise Road is on Hamilton's West Mountain, an established residential part of the city with steady, long-term rental demand:
    <ul>
      <li>Established Mountain neighbourhood of detached homes — the kind of stock that rents well and holds value</li>
      <li>Everyday shopping and services along Upper Paradise Road and nearby Mohawk Road and Rymal Road</li>
      <li>Hamilton Street Railway (HSR) transit on the Mountain's main corridors; close to Mohawk College</li>
      <li>Quick access to the Lincoln M. Alexander Parkway and the Claremont / Garth access routes off the Mountain</li>
      <li>Illustrative context only — not a valuation. Neighbourhood boundaries and any local designations are confirmed in Phase 2.</li>
    </ul>'''))

# ---- zoning table (section 2) -----------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>Residential (City of Hamilton Zoning By-law No. 05-200, as amended) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot in Hamilton's Urban Area (municipal water &amp; sewer) with a single detached, semi-detached, or street townhouse dwelling — the basis on which additional dwelling units are permitted as-of-right.</td></tr>
    <tr><td>Recent Changes</td><td>Under provincial legislation (Bill 23 / Bill 185) and Hamilton By-laws 21-071–21-077 (2021), updated by 22-132–22-138 (2022), the City permits additional dwelling units as-of-right — an internal unit plus a detached unit, up to <strong>3 residential units</strong> total. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>An internal secondary dwelling unit (such as a basement suite) and a detached additional dwelling unit are permitted, subject to Hamilton's site standards — setbacks, height, and a floor-area cap. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- "what this means" list (section 2 cell) --------------------------------
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Internal Secondary Dwelling Unit:</strong> a self-contained unit within the existing home (for example, a basement apartment) — your stated goal</li>
      <li><strong>Detached Additional Dwelling Unit:</strong> a self-contained suite in the rear yard, on the same lot as the main home</li>
      <li><strong>Up to 3 units total:</strong> under Hamilton's ADU by-laws the lot may support the principal home plus two additional units (one of which may be detached), subject to site standards</li>
      <li><strong>Confirmed per lot in Phase 2:</strong> the exact zone, unit sizes, setbacks, height, and any special provisions are confirmed against the City's zoning mapping before design begins</li>'''))

# ---- time-sensitive section (3 items) ---------------------------------------
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">ARU Development-Charge Exemption — Already in Effect</div><div class="dx">Under provincial legislation, up to two additional residential units on your lot are exempt from municipal development charges — a meaningful per-unit saving on a new suite. The exact application to your project is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Confirm the Current Zoning Text</div><div class="dx">Hamilton's residential zoning is actively being updated (the Residential Zones Project; the by-law's general provisions were reconsolidated in 2026), and the City's new Mid-Rise Residential Zones are under appeal at the Ontario Land Tribunal and not yet in effect. The additional-dwelling-unit permissions you are relying on are in force today — the exact current text for your lot is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- rezoning: green callout ------------------------------------------------
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Additional dwelling units, including an internal (basement) suite, are permitted as-of-right on this lot under Hamilton Zoning By-law No. 05-200 (as amended). No rezoning required.</div>'))

# ---- rezoning: comparison "what governs" row --------------------------------
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">By-law 05-200 (as amended)</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- rezoning: two cards ----------------------------------------------------
R.append(('''  <div class="twocard">
    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>
  </div>''',
'''  <div class="twocard">
    <div class="card2"><div class="ct">Internal secondary unit</div>On a lot with a single detached dwelling in Hamilton's Urban Area, an internal additional dwelling unit (such as a basement suite) is permitted as-of-right under By-law 05-200, as amended (By-laws 21-071–21-077 / 22-132–22-138).</div>
    <div class="card2"><div class="ct">Detached additional unit</div>A second, detached additional dwelling unit in the rear yard is also permitted on the same lot — up to two additional units in total — subject to the City's site standards. Confirmed in Phase 2.</div>
  </div>'''))

# ---- rezoning: "what this means" barhead + para + amber ---------------------
R.append(('''  <div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>
  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="barhead" style="text-align:left;">What this means for 507 Upper Paradise Road</div>
  <p>Because 507 Upper Paradise Road already permits the additional dwelling unit you are planning under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>One item to confirm: the property's exact zone and any site-specific provisions.</b><br><span class="sub">The exact zone code, lot dimensions, servicing, and any special or holding provisions are confirmed against the City's zoning mapping in Phase 2 before design begins.</span></div>'''))

# ---- development options: A -------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Internal Secondary Unit (your goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A self-contained secondary dwelling unit within the existing home — for example, a basement apartment — rented for ongoing income while you keep the property. This is your stated goal. Permitted as-of-right under Hamilton By-law 05-200 (as amended) on a lot with a single detached dwelling in the Urban Area; no rezoning. Unit size, ceiling height, egress, and life-safety requirements follow the Ontario Building Code and the City's additional-dwelling-unit standards, confirmed in Phase 2.</div>'''))

# ---- development options: B -------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Internal Suite + Detached Unit</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">Pair the internal (basement) suite with a detached additional dwelling unit in the rear yard — a route to up to three units on the lot (the principal home plus two additional units, one of which may be detached) under Hamilton's ADU by-laws, where the lot allows. This maximizes rental income while keeping the property in your hands. Siting, size, servicing, and any parking for the detached unit are confirmed in Phase 2.</div>'''))

# ---- development options: C -------------------------------------------------
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Lot &amp; Servicing Notes</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Your Hamilton Mountain lot is a typical serviced residential parcel — generally a good fit for an internal suite and, subject to rear-yard space and setbacks, a detached unit as well. Early confirmation items include the exact zone and any special provisions, servicing capacity for a second or third unit, required setbacks and parking, and whether the existing home is a single detached dwelling for ADU purposes. The exact buildable envelope for any detached unit is confirmed in Phase 2.</div>'''))

# ---- goal summary (section 5) -----------------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Internal Secondary (Basement) Unit</div>
  <p>507 Upper Paradise Road is a serviced residential lot in Hamilton where, under By-law No. 05-200 (as amended), an internal additional dwelling unit — such as the basement suite you are planning — is permitted as-of-right, with no rezoning required. <strong>The internal secondary unit is the clear primary recommendation</strong>, with a detached additional unit as an optional path to a third income unit.</p>'''))

# ---- summary (section 8) zoning review --------------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>507 Upper Paradise Road is a serviced residential lot in Hamilton. Under the City's Zoning By-law No. 05-200 (as amended) and provincial legislation, up to <strong>two additional dwelling units are permitted as-of-right</strong> — including the internal (basement) suite you are after — with no rezoning required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Additional-Dwelling-Unit Advantage:</strong> an internal secondary suite adds a rental income stream using space you already own; a detached unit can add a third — exact sizes and siting are confirmed in Phase 2.</li>
  </ul>'''))

# ---- grants table (section 7) -----------------------------------------------
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>Additional Residential Unit — Development Charge Exemption</td><td>Under the Development Charges Act (as amended by Bill 23), up to two additional residential units on an existing residential lot are exempt from municipal development charges — a per-unit saving on a new suite. Applicability to your project confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable credit of 15% on up to $50,000 of eligible cost (up to $7,500) where a self-contained secondary unit is created to house an eligible relative (a senior, or an adult eligible for the Disability Tax Credit). Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>May apply to a newly built or substantially renovated rental suite that becomes long-term rental housing. The enhanced 100% purpose-built rental rebate is aimed at projects of 4+ units; applicability to a single suite is confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as the Canada Greener Homes initiatives and utility retrofit rebates may offset efficient design and equipment in a new suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>City of Hamilton — Additional Dwelling Unit support</td><td>Hamilton provides guidance for additional dwelling units and, from time to time, funding streams to support them. Current municipal programs and any registration or application requirements are confirmed in Phase 2.</td></tr>'''))

# ---- apply, asserting each matches exactly once -----------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# ---- leftover check (source-city / master tokens that must be gone) ---------
# Note: "Bill 185" is intentionally NOT blocked — it is a legitimate Ontario
# statute referenced in the Hamilton zoning row. We instead guard the specific
# Toronto claims (DC waiver / multiplex language) that must not survive.
LEFTOVERS = ["Coxwell", "John Arockiaraj", "Toronto", "Ward 19", "Beaches",
             "654-2025", "474-2023", "6+1", "4+1", "M4L 3B5",
             "Woodbine", "TTC", "Gerrard", "Garden Suite By-law", "569-2013",
             "houseplex", "Houseplex", "Cambridge", "Waterloo", "Galt",
             "Development Charge Waiver", "fully eliminated for multiplexes",
             "Development charges fully waived"]
print("--- leftovers ---")
any_left = False
for t in LEFTOVERS:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        any_left = True
if not any_left:
    print("(none)")

if fails == 0 and not any_left:
    open(OUT, "w", encoding="utf-8").write(s)
    print(f"WROTE {OUT}  ({len(s)} bytes)")
else:
    print(f"NOT WRITTEN — fails={fails}, leftovers={any_left}")
