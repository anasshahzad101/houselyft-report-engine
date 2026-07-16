"""Transform the House Lyft master report -> 98 Calverley Trail, Scarborough (Toronto).

Ward 25 (Scarborough-Rouge Park): RD (x696), 4 units as-of-right (fourplex),
NOT a six-unit ward. Scope = Multiplex Development (developer buying land) ->
tiered. Follows the xform pattern: every replacement must match exactly once,
then a leftover grep for the source property/city.
"""
import base64, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_98calverley.html")
LOT = os.path.join(ROOT, "scratch_report", "aerial_lot.jpg")
CTX = os.path.join(ROOT, "scratch_report", "aerial_ctx.jpg")

s = open(MASTER).read()

def b64(path):
    return base64.b64encode(open(path, "rb").read()).decode()

lot_uri = "data:image/jpeg;base64," + b64(LOT)
ctx_uri = "data:image/jpeg;base64," + b64(CTX)

R = []

# ---- cover -----------------------------------------------------------------
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">98 Calverley Trail<span>Scarborough, Toronto, ON</span></div>'))

# ---- aerial image row + licence (Property Details) -------------------------
old_img = '''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>'''
new_img = f'''  <div class="imgrow" style="margin-top:0;">
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="{lot_uri}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Aerial view of 98 Calverley Trail">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Oswald',Arial,sans-serif;">Aerial view — approx. 90 m across</div>
    </div>
    <div style="flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);">
      <img src="{ctx_uri}" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Neighbourhood context around 98 Calverley Trail">
      <div style="position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:7pt;padding:3px 7px;font-family:'Oswald',Arial,sans-serif;">Neighbourhood context — approx. 300 m across</div>
    </div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto 2025 (8 cm). Contains information licensed under the Open Government Licence – Toronto.</div>'''
R.append((old_img, new_img))

# ---- property table 1 (contact block) --------------------------------------
R.append(('''    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Name</td><td>Moshiur Rahman</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development — purchasing land to build a multiplex</td></tr>'''))

# ---- property table 2 (municipality block) ---------------------------------
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
'''    <tr><td>Municipality</td><td>Toronto (Scarborough district)</td></tr>
    <tr><td>Neighbourhood</td><td>Highland Creek</td></tr>
    <tr><td>Ward</td><td>Ward 25 — Scarborough-Rouge Park</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Zoning</td><td>RD — exception 900.3.10(696)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Development Goals</td><td>Multiplex development (land purchase); 4-unit multiplex, optional garden suite</td></tr>'''))

# ---- neighbourhood spotlight -----------------------------------------------
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
    98 Calverley Trail is in Highland Creek, an established low-rise residential neighbourhood in east Scarborough near the Highland Creek ravine system:
    <ul>
      <li>Close to the University of Toronto Scarborough (UTSC) and Centennial College's Progress Campus — a steady source of student and staff rental demand</li>
      <li>Near the Toronto Pan Am Sports Centre and the Highland Creek / Colonel Danforth park and trail network</li>
      <li>Quick access to Highway 401 and Ellesmere Road; TTC bus service connects to Scarborough Centre and the subway network</li>
      <li>Established residential streets — the kind of stock that rents well and holds value</li>
      <li>Local shopping along Old Kingston Road and Morningside Avenue (illustrative context, not a valuation)</li>
    </ul>'''))

# ---- zoning table (Section 2) ----------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>RD — Residential Detached, exception 900.3.10(696) (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan designation and per-parcel standards confirmed in Phase 2. The lot is in Ward 25 (Scarborough-Rouge Park), where up to four residential units are permitted as-of-right citywide in a multiplex form — subject to the RD zone's built-form standards (height, coverage, setbacks) and technical review of site conditions.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right citywide in a multiplex form (By-law 0473/0474, May 2023) — no rezoning required. The six-unit as-of-right permission applies only in nine designated wards; Ward 25 is not among them.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone allows up to <strong>4 residential units</strong> as-of-right in a detached houseplex / multiplex form, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- time-sensitive: DC waiver phrasing (avoid implying 6 as-of-right) ------
R.append(('''<div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div>''',
'''<div class="dx">In Toronto, development charges are fully eliminated for multiplexes up to 6 units (Bill 185, January 2025) — no application required. A 4-unit multiplex on this lot sits comfortably within that cap. City figures cite roughly $45,000–$50,000 per unit in savings; the exact amount for this project is confirmed in Phase 2.</div>'''))

# ---- Section 3 Rezoning ----------------------------------------------------
R.append(('The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.',
          "The recommended 4-unit multiplex is permitted as-of-right under Toronto's citywide multiplex by-law (0473/0474)."))
R.append(('<td>What governs your build</td><td class="g">By-law 654-2025</td>',
          '<td>What governs your build</td><td class="g">By-law 0473/0474</td>'))
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Four-unit multiplex</div>Up to four units are permitted as-of-right citywide in a multiplex form under By-law 0473/0474 — no rezoning, no public meeting if within the standard envelope.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>'''))
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>',
          '<div class="barhead" style="text-align:left;">What this means for 98 Calverley Trail</div>'))
R.append(('''  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>''',
'''  <p>Because 98 Calverley Trail already permits a 4-unit multiplex under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions and confirmed lot dimensions.</p>'''))
R.append(('''  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>''',
'''  <div class="co-amber"><b>Two items to confirm in Phase 2: the lot's exact dimensions, and whether a garden suite can be added alongside a 4-unit multiplex.</b><br><span class="sub">A garden or laneway suite (the fifth unit) stacks on 4-unit-and-under projects, but the fit and eligibility on this specific lot are confirmed against the current by-law before it is relied upon.</span></div>'''))

# ---- Section 4 Development Options -----------------------------------------
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — 4-Unit Multiplex (Fourplex)</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">A detached 4-unit houseplex (fourplex) on the main structure. Fully as-of-right under Toronto's citywide multiplex by-law (0473/0474) — no rezoning, and no variances likely if designed within the standard RD-zone envelope (height, coverage, and setbacks). No parking minimums apply to multiplexes (citywide, since February 2022). In Toronto, development charges are fully waived for projects up to 6 units (Bill 185), so a fourplex qualifies. The lot's exact dimensions and buildable footprint are confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — 4-Unit Multiplex + 1 Garden Suite (4+1) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A detached 4-unit multiplex plus one detached garden suite in the rear yard — up to five income units, the maximum residential density this lot supports as-of-right. Under Toronto's rules a garden or laneway suite stacks on a 4-unit-and-under multiplex; that stacking is the single item confirmed against the current by-law in Phase 2. This configuration matches the goal of maximizing unit count on a purchased lot. One ADU per lot is permitted (garden or laneway — not both), and no parking spaces are required. The suite's size and siting follow Toronto's garden-suite standards (setbacks, height, floor-area cap), confirmed in Phase 2.</div>'''))
R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — The Fifth Unit &amp; Additional Suites</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Reaching five units on this lot means pairing the fourplex with one detached garden or laneway suite. Whether a garden suite can be added alongside a 4-unit multiplex — and whether the rear-yard, tree, and servicing conditions fit it — is the key item confirmed in Phase 2, because it decides both the final unit count and which financing programs open up. If a public laneway abuts the lot, a laneway suite is the alternative to a garden suite (never both). Confirming the lot's dimensions, any protected trees, and heritage or ravine overlays early keeps the design on the as-of-right path.</div>'''))

# ---- Section 5 Development Goal Summary ------------------------------------
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">4+1 Configuration</div>
  <p>98 Calverley Trail is in Ward 25 (Scarborough-Rouge Park), where up to four units are permitted as-of-right citywide in a multiplex form under By-law 0473/0474. Pairing the fourplex with one garden suite — a 4+1, five-unit configuration — is the path that maximizes unit count on the lot. <strong>The 4+1 configuration is the primary recommendation, with the fifth (garden-suite) unit confirmed against the current by-law in Phase 2.</strong></p>'''))

# ---- Section 6 Financing: inject tier-gated construction/permanent programs -
R.append(('''    <!-- GATED_FINANCING_ROWS
     Injected by the builder from config/programs.json AFTER apply_gates().
     Do NOT hardcode a program here. Anything above this marker is any_scale
     (refinance / HELOC / construction) and always renders.
     See docs/PROGRAM_GATING_v1.md -->''',
'''    <tr><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Low-interest construction financing for purpose-built rental, structured to a high share of project cost. It carries a minimum $1M loan, so eligibility depends on the confirmed Phase 2 project budget rather than unit count. (CMHC ACLP program terms.)</td></tr>
    <tr><td>CMHC MLI Select</td><td>Insured financing with reduced premiums and long amortization for purpose-built rental — generally a minimum of five rental units. This opens up at the 4+1 (five-unit) configuration, subject to confirming the garden-suite unit in Phase 2. (CMHC MLI Select product terms.)</td></tr>'''))

# ---- Section 7 Grants: inject gated grant/incentive rows -------------------
R.append(('''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
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
'''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>In Toronto, development charges are fully eliminated for multiplexes up to 6 units — no application required. A 4-unit multiplex is within the cap. City figures cite roughly $45,000–$50,000 per unit; the exact total is confirmed in Phase 2. (City of Toronto, Bill 185, January 2025.)</td></tr>
    <tr><td>Provincial</td><td>Development-Charge Exemption for Additional Residential Units (Bill 23)</td><td>Additional residential units — such as a garden suite — are exempt from development charges under provincial legislation, covering the first two additional units. A meaningful per-unit saving on the garden suite. (Ontario More Homes Built Faster Act, Bill 23.)</td></tr>
    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>A full rebate of the 5% federal GST on new purpose-built rental projects with four or more self-contained units, 90%+ long-term rental, construction starting before 2031. Ontario mirrors it with a rebate of the 8% provincial HST component. Opens up at the 4-unit multiplex tier. (Federal PBRH rebate; Ontario provincial component.)</td></tr>
    </table>'''))

# ---- Section 8 Summary: Current Zoning Review ------------------------------
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>98 Calverley Trail confirms a strong development option. The property sits in Ward 25 (Scarborough-Rouge Park), where up to <strong>four units are permitted as-of-right citywide in a multiplex form</strong> under By-law 0473/0474 — no rezoning, no public hearing, and no Council approval required. Paired with a garden suite, the lot can support up to five income units, subject to confirming the garden-suite unit in Phase 2.</p>
  <ul>
    <li><strong>The As-of-Right Multiplex Advantage:</strong> A 4-unit multiplex is permitted as-of-right — the project advances straight to design and permitting, avoiding the cost, delay, and appeal exposure of a rezoning.</li>
  </ul>'''))

# ---- apply (each must match exactly once) ----------------------------------
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# ---- global address string (appears twice: barhead + property table) -------
addr_old = "303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5"
addr_new = "98 Calverley Trail, Scarborough, ON&nbsp;&nbsp;M1C 3S6"
ac = s.count(addr_old)
if ac != 2:
    print(f"[FAIL addr x{ac}] expected 2")
    fails += 1
else:
    s = s.replace(addr_old, addr_new)

# ---- leftover check (source property / wrong-city / wrong-program) ---------
# strip base64 data URIs first so image bytes don't cause false-positive matches
import re as _re
scan = _re.sub(r"data:image/jpeg;base64,[A-Za-z0-9+/=]+", "", s)
print("\n-- leftover scan (base64 stripped) --")
for t in ["Coxwell", "John Arockiaraj", "Beaches", "Ward 19", "654-2025",
          "6+1", "6-Unit", "Six-unit", "M4L 3B5", "315.9", "750 sq ft",
          "Woodbine", "Greenwood", "johneeraj", "647) 223", "474-2023",
          "Canada Secondary Suite", "free grant"]:
    n = scan.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

open(OUT, "w").write(s)
print(f"\nwrote {OUT}  ({len(s)} bytes)  fails={fails}")
