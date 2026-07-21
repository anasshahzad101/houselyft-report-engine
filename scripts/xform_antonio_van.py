"""
xform_antonio_van.py — build the Antonio Rigor / 580 East 30th Avenue, Vancouver
report from the House Lyft master. Follows the scripts/xform_*.py pattern:
every replacement must match exactly once, then grep for leftovers.

City: Vancouver (no engine adapter) -> rules researched live from official
City of Vancouver + Province of BC sources -> report-needs-review.
Scope: "Garden Suite, Laneway Home or ADU" -> scoped render, lead with the
laneway/garden suite; R1-1 multiplex presented as the density upside.
"""
import base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_antonio_van.html")
IMGDIR = "/tmp/claude-0/-home-user-houselyft-report-engine/4e02187f-f973-5a05-a93c-84499c21531c/scratchpad/imgs"

def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()

LOT = b64(os.path.join(IMGDIR, "lot_opt.jpg"))
CTX = b64(os.path.join(IMGDIR, "ctx_opt.jpg"))

s = open(MASTER).read()
R = []

# --- cover address ---
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">580 East 30th Avenue<span>Vancouver, BC</span></div>'))

# --- property details barhead ---
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">580 East 30th Avenue, Vancouver, BC&nbsp;&nbsp;V5V 2V6</div>'))

# --- imagery row: inject the two validated aerials + real licence line ---
IMG_CAP = "position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Lato',Arial,sans-serif;"
IMG_WRAP = "flex:1;position:relative;height:148px;border:1px solid var(--line);overflow:hidden;"
R.append(('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''',
f'''  <div class="imgrow" style="margin-top:0;">
    <div style="{IMG_WRAP}"><img src="data:image/jpeg;base64,{LOT}" style="width:100%;height:148px;object-fit:cover;display:block;"><div style="{IMG_CAP}">Aerial view - approx. 90 m across</div></div>
    <div style="{IMG_WRAP}"><img src="data:image/jpeg;base64,{CTX}" style="width:100%;height:148px;object-fit:cover;display:block;"><div style="{IMG_CAP}">Neighbourhood context - approx. 300 m across</div></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Aerial imagery: City of Vancouver Aerial Basemap (2018). Contains information licensed under the Open Government Licence &ndash; Vancouver. Street-level photography pending a licensed source.</div>'''))

# --- property details table 1 (contact + goals) ---
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>580 East 30th Avenue, Vancouver, BC&nbsp;&nbsp;V5V 2V6</td></tr>
    <tr><td>Name</td><td>Antonio Rigor</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Garden suite / laneway home / ADU (primary); R1-1 multiplex as upside</td></tr>'''))

# --- property details table 2 (municipality block) ---
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
'''    <tr><td>Municipality</td><td>City of Vancouver</td></tr>
    <tr><td>Neighbourhood</td><td>Riley Park / Kensington-Cedar Cottage</td></tr>
    <tr><td>Current Zoning</td><td>R1-1 — Residential Inclusive (confirm this address via VanMap in Phase 2)</td></tr>
    <tr><td>Current Bylaw</td><td>Vancouver Zoning &amp; Development By-law No. 3575 — District Schedule R1-1</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed (via BC Assessment)</td></tr>
    <tr><td>Lot size</td><td>To be confirmed (via VanMap / BC Assessment in Phase 2)</td></tr>
    <tr><td>Development Goals</td><td>Laneway home / garden suite (primary); R1-1 multiplex as upside</td></tr>'''))

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
    580 East 30th Avenue sits in the Riley Park / Kensington-Cedar Cottage area of East Vancouver — an established, family-oriented residential neighbourhood well served by transit and close to the Main Street and Fraser Street shopping districts:
    <ul>
      <li>Walking distance to Main Street's shops, cafés, and restaurants — one of East Vancouver's most active retail streets</li>
      <li>Close to Queen Elizabeth Park, Hillcrest Community Centre, and Nat Bailey Stadium</li>
      <li>Frequent bus service on Main Street, Fraser Street, and the Broadway / King Edward corridors connects to the Canada Line and the Broadway Subway</li>
      <li>Proximity to a frequent-transit stop can raise the provincial minimum density to six units — to be confirmed against the transit map in Phase 2</li>
      <li>Illustrative neighbourhood context only — not a valuation</li>
    </ul>'''))

# --- zoning table ---
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>R1-1 — Residential Inclusive (Vancouver Zoning &amp; Development By-law No. 3575, District Schedule R1-1). Applies to lots formerly zoned RS; confirm the designation for this address via VanMap in Phase 2.</td></tr>
    <tr><td>What R1-1 Allows</td><td>A "multiplex" of up to <strong>6 units (strata / ownership)</strong>, or up to <strong>8 units if all secured rental</strong>, to a maximum 1.0 FSR — as-of-right, no rezoning. A house with a secondary suite plus a laneway / garden suite is a separate permitted path (see Development Options).</td></tr>
    <tr><td>Recent Changes</td><td>R1-1 took effect October 17, 2023, consolidating the former RS single-family zones and permitting small-scale multi-unit housing city-wide. It meets or exceeds the Province's Small-Scale Multi-Unit Housing requirements (Bill 44). Exact figures to be confirmed against the current R1-1 district schedule in Phase 2.</td></tr>
    <tr><td>Permitted Uses</td><td>Multiplex, rowhouse / townhouse forms, a single detached house with a secondary suite, and a laneway / garden suite — the maximum configuration for this lot depends on lot area and frontage and is confirmed at design in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# --- "what this means for you" list ---
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Laneway House / Garden Suite:</strong> a detached rental suite in the rear yard under Section 11 of the Zoning &amp; Development By-law — your stated goal</li>
      <li><strong>House + Secondary Suite:</strong> a single detached house may also include an internal secondary suite, alongside a laneway house (up to three units in total)</li>
      <li><strong>Multiplex (up to 6 strata / 8 secured-rental units):</strong> a small-scale multi-unit building to a maximum 1.0 FSR — the density upside on this lot</li>
      <li><strong>Rowhouse / Townhouse forms:</strong> attached ground-oriented units within the R1-1 envelope</li>'''))

# --- time-sensitive section ---
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Faster Multiplex Permitting<br><small>active now</small></div><div class="dx">Vancouver introduced a combined Development + Building Permit process for multiplexes of up to four units in 2025, cutting typical processing time by roughly half. Designing within that envelope can materially shorten your timeline. Confirm the current process and any conditions in Phase 2.</div></div>
    <div class="d"><div class="dt">Enhanced GST Rental Rebate — Time-Limited<br><small>federal window</small></div><div class="dx">The federal Enhanced GST Rental Rebate refunds 100% of the 5% federal GST on qualifying new purpose-built rental with four or more units. Construction must begin by December 31, 2030 and complete by December 31, 2035. This applies only if the project is built as four or more rental units (the multiplex path) — a single laneway suite does not qualify. Structuring early preserves eligibility.</div></div>
    <div class="d"><div class="dt">Suite Subsidies Have Closed</div><div class="dx">Two secondary-suite subsidy programs are no longer available to new applicants: the federal secondary-suite loan program was cancelled in Budget 2025 (it was never operational), and BC's Secondary Suite Incentive Program stopped accepting applications in March 2025. Do not budget for either. The live path for a single suite is CMHC-insured refinancing — confirm current terms in Phase 2.</div></div>'''))

# --- rezoning: green box ---
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>Both a laneway / garden suite and an R1-1 multiplex are permitted as-of-right under Vancouver\'s R1-1 zone — no rezoning required.</div>'))

# --- rezoning: comparison table "what governs" row ---
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">R1-1 District Schedule (By-law 3575)</td><td class="n">A new site-specific by-law</td></tr>'))

# --- rezoning: two cards ---
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">R1-1 multiplex</div>Vancouver's R1-1 zone permits a multiplex of up to six strata units — or up to eight if all secured rental — as-of-right, to a maximum 1.0 FSR, without rezoning.</div>
    <div class="card2"><div class="ct">Laneway house / garden suite</div>A detached rental suite in the rear yard is permitted under Section 11 of the Zoning &amp; Development By-law, alongside a house that may also contain a secondary suite.</div>'''))

# --- rezoning: barhead + para ---
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 580 East 30th Avenue</div>'))
R.append(('<p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<p>Because 580 East 30th Avenue already permits both the laneway / garden suite and a multiplex under existing R1-1 zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. This assessment reflects the by-laws in force at the date of this report, was researched from current City of Vancouver and Province of BC sources, and is subject to technical review of site conditions in Phase 2.</p>'))

# --- rezoning: amber box ---
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>Two items to confirm in Phase 2:</b><br><span class="sub">the exact R1-1 unit-tier figures and this lot\'s zoning and area against VanMap and the current district schedule; and the permit status of any existing rear structure before it can count as a legal unit or support financing.</span></div>'))

# --- development options A ---
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Laneway House / Garden Suite (your stated goal)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached laneway house (garden suite) in the rear yard, alongside your existing house — which may also carry an internal secondary suite — for a configuration of up to three units in total. Under Section 11 of the Zoning &amp; Development By-law, a laneway house is built to a maximum 0.25 FSR and 186 m² (about 2,000 sq ft), up to 8.5 m and two storeys, as rental tenure (it cannot be strata-titled and sold separately). No minimum parking is required in R1-1. This is the most direct route to new rental income while keeping your existing home. Final size and siting depend on lot width and rear-yard fit, confirmed at design in Phase 2.</div>'''))

# --- development options B ---
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — R1-1 Multiplex (the density upside)</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">The larger opportunity on this lot: a multiplex of up to six strata (ownership) units, or up to eight units if the building is all secured rental, to a maximum 1.0 FSR — all as-of-right under R1-1, no rezoning and no minimum parking. A multiplex is a different project from a laneway suite: it typically replaces the existing house, and its unit count is the total on site (it does not also carry separate secondary or laneway suites). Building at four or more rental units unlocks the federal Enhanced GST Rental Rebate, and five or more units brings CMHC MLI Select financing into reach — neither of which a single suite can access. Whether the numbers favour keeping the house with a laneway suite or redeveloping to a multiplex is exactly what the Phase 2 pro forma resolves.</div>'''))

# --- development options C ---
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Note on the Combined-Permit Path &amp; Existing Structures</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Two practical notes. First, Vancouver's combined Development + Building Permit stream for multiplexes of up to four units (introduced in 2025) can cut permitting time by roughly half — a real advantage if the design stays within that envelope. Second, the permit status of any existing rear structure (garage or accessory building) must be confirmed before it can count toward a legal unit or support financing; if it was altered without a permit, a retroactive permit is required first. Both are early Phase 2 items.</div>'''))

# --- development goal summary ---
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Laneway Suite First, Multiplex Upside</div>
  <p>580 East 30th Avenue is a Vancouver R1-1 lot. Your stated goal — a laneway house or garden suite — is permitted as-of-right, alongside a house that may also carry an internal secondary suite (up to three units). <strong>The laneway / garden suite is the recommended first step</strong>, with an R1-1 multiplex of up to six strata (or eight secured-rental) units as the larger upside the Phase 2 numbers can weigh.</p>'''))

# --- financing: insert a CMHC refinance row before the gated marker ---
R.append(('''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <!-- GATED_FINANCING_ROWS''',
'''    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <tr><td>CMHC-Insured Refinance (for a suite)</td><td>CMHC-insured refinancing can let owners draw on a portion of their property's post-renovation value to fund a new secondary or laneway suite. This is the live federal path for a single-suite project — the former federal secondary-suite loan program was cancelled. Current limits and terms are confirmed with CMHC in Phase 2.</td></tr>
    <!-- GATED_FINANCING_ROWS'''))

# --- grants table: inject gated rows (threshold shown for every gated program) ---
R.append(('''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <!-- GATED_GRANTS_ROWS''',
'''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>BC Small-Scale Multi-Unit Housing (Bill 44)</td><td>Provincial legislation requires Vancouver to permit small-scale multi-unit housing as-of-right (3–6 units, depending on lot size and frequent-transit proximity). This is a zoning entitlement, not a cash grant — it is what makes your build possible without rezoning. Vancouver's R1-1 meets or exceeds it.</td></tr>
    <tr><td>Federal</td><td>Enhanced GST Rental Rebate (Purpose-Built Rental)</td><td>100% rebate of the 5% federal GST on qualifying new purpose-built rental. <strong>Threshold: four or more rental units</strong> — reached at the multiplex scale, not with a single laneway suite. Construction must start by Dec 31, 2030 and complete by Dec 31, 2035. Source: Canada Revenue Agency.</td></tr>
    <tr><td>Federal</td><td>CMHC MLI Select</td><td>Preferred mortgage-insurance terms (higher leverage, longer amortization) for rental projects scored on affordability, energy efficiency, and accessibility. <strong>Threshold: five or more rental units</strong> — a multiplex-scale program, not available for a single suite. Source: CMHC.</td></tr>
    <tr><td>Federal</td><td>CMHC-Insured Refinance for a Suite</td><td>Refinancing insured by CMHC can fund a new secondary or laneway suite from a portion of the home's post-renovation value. This is the live path at the single-suite scale you are considering. Terms confirmed with CMHC in Phase 2.</td></tr>
    <tr><td>Provincial</td><td>BC / GST tax treatment</td><td>BC applies the 5% federal GST; the federal purpose-built rental rebate above applies in BC as elsewhere. BC's own sales-tax treatment (PST on some materials, not most labour) affects the build budget. Confirm the structure with a BC tax advisor in Phase 2. (Illustrative — no figure is stated.)</td></tr>
    <!-- GATED_GRANTS_ROWS'''))

# --- summary section ---
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>580 East 30th Avenue is a City of Vancouver R1-1 (Residential Inclusive) lot. Under R1-1, a laneway house or garden suite — the stated goal — is permitted as-of-right, and the lot also carries multiplex density of up to <strong>six strata or eight secured-rental units</strong> to a maximum 1.0 FSR, all without rezoning. The figures here were researched from current City of Vancouver and Province of BC sources; the exact unit-tier table and this lot's zoning and area should be confirmed against the R1-1 district schedule and VanMap in Phase 2.</p>
  <ul>
    <li><strong>As-of-Right Flexibility:</strong> both a laneway / garden suite and a multiplex are permitted on this lot with no rezoning, no public hearing, and no Council approval — the choice is a numbers question, not a zoning one.</li>
  </ul>'''))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# strip the build-time gated-rows marker comments (they carry Toronto/HST example
# text and are not needed in the delivered report; rows are already injected above)
import re as _re0
s = _re0.sub(r'\s*<!-- GATED_FINANCING_ROWS.*?-->', '', s, flags=_re0.DOTALL)
s = _re0.sub(r'\s*<!-- GATED_GRANTS_ROWS.*?-->', '', s, flags=_re0.DOTALL)
s = _re0.sub(r'<!-- GATED_FINANCING_PROSE.*?-->', '', s, flags=_re0.DOTALL)

open(OUT, "w").write(s)

print("--- leftover check ---")
# strip base64 image data so coincidental substrings inside it aren't false positives
import re as _re
scan = _re.sub(r'data:image/jpeg;base64,[A-Za-z0-9+/=]+', 'data:image/jpeg;base64,', s)
LEFTOVERS = ["Coxwell", "Arockiaraj", "Ward 19", "Beaches", "654-2025", "474-2023",
             "569-2013", "Bill 185", "Ontario", "HST", "Toronto", "TTC", "houseplex",
             "Greenwood", "Danforth", "johneeraj", "647) 223"]
any_left = False
for t in LEFTOVERS:
    n = scan.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        any_left = True
if not any_left:
    print("clean — no leftovers")
print("done, fails:", fails, "-> wrote", OUT)
sys.exit(1 if fails else 0)
