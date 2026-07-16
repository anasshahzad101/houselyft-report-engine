"""
xform_brampton.py — turn the House Lyft master report into the 32 Medici Place,
Brampton report. Follows the established xform pattern: exact string swaps that
each must match exactly once, then a leftover grep for the source city.

Grounding (verified live 2026-07-16):
  Zoning : engine/property_lookup_v2.lookup -> City of Brampton ArcGIS (ARU_SEARCH)
           zone R2A(1); Bill 23 framework = up to 3 residential units as-of-right
           (principal + 1 attached second unit + 1 garden suite, max 3 total).
  Imagery: engine/aerial_imagery -> City of Brampton Orthophoto 2023 (Spring),
           OGL-licensed. Lot + neighbourhood-context aerials, both validated.

House Lyft prose sections (Why / How to use / Advantage / Financing Pathways /
Roadblocks / CTA / Next Steps) are kept verbatim.
"""
import base64
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "engine"))

MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_brampton.html")

# Coordinates from the live geocode (property_lookup_v2), reused so the
# imagery lands on the same lot the zoning was pulled for.
LAT, LON = 43.7309507, -79.7430877
ADDRESS = "32 Medici Place, Brampton, Ontario"


def _aerials():
    """Fetch the lot-scale and context-scale Brampton orthophotos as data URIs.
    Returns (lot_uri, ctx_uri, credit) or (None, None, None) if the licensed
    imagery source returns nothing (honest-line fallback per the doctrine)."""
    from aerial_imagery import get_aerial
    lot = get_aerial(ADDRESS, "brampton", half_m=45.0, lat=LAT, lon=LON)
    ctx = get_aerial(ADDRESS, "brampton", half_m=120.0, lat=LAT, lon=LON)
    if not (lot and ctx):
        return None, None, None
    lot_uri = "data:image/jpeg;base64," + base64.b64encode(lot.image).decode()
    ctx_uri = "data:image/jpeg;base64," + base64.b64encode(ctx.image).decode()
    return lot_uri, ctx_uri, lot.source.attribution


s = open(MASTER, encoding="utf-8").read()
R = []

# ---- COVER ----
R.append(('<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
          '<div class="addr">32 Medici Place<span>Brampton, ON</span></div>'))

# ---- IMAGE ROW + LICENCE (Property Details) ----
lot_uri, ctx_uri, credit = _aerials()
OLD_IMG = ('''  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>''')

if lot_uri:
    cap = "position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;font-size:6.6pt;padding:2px 7px;font-family:'Lato',Arial,sans-serif;"
    box = "flex:1;position:relative;height:148px;overflow:hidden;border:1px solid var(--line);"
    img = "width:100%;height:148px;object-fit:cover;display:block;"
    NEW_IMG = (f'''  <div class="imgrow" style="margin-top:0;">
    <div style="{box}"><img src="{lot_uri}" style="{img}"><div style="{cap}">Aerial view — approx. 90 m across</div></div>
    <div style="{box}"><img src="{ctx_uri}" style="{img}"><div style="{cap}">Neighbourhood context — approx. 240 m across</div></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Brampton Orthophoto 2023 (Spring). {credit}</div>''')
else:
    NEW_IMG = ('''  <div class="imglicense" style="font-size:7.4pt;color:#7a818f;margin:2px 0 10px;">Aerial and street-level photography pending a licensed imagery source.</div>''')
R.append((OLD_IMG, NEW_IMG))

# ---- BARHEAD (Property Details) ----
R.append(('<div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>',
          '<div class="barhead">32 Medici Place, Brampton, ON&nbsp;&nbsp;L6S 3C6</div>'))

# ---- PROPERTY TABLE 1 (contact + goals) ----
R.append(('''    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>''',
'''    <tr><td>Property Address</td><td>32 Medici Place, Brampton, ON&nbsp;&nbsp;L6S 3C6</td></tr>
    <tr><td>Name</td><td>T J Sang</td></tr>
    <tr><td>Phone Number</td><td>(647) 787-7887</td></tr>
    <tr><td>Email</td><td>sadqpur@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>Convert the existing duplex to a triplex (add a third unit); multiplex development</td></tr>'''))

# ---- PROPERTY TABLE 2 (municipality facts) ----
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
    <tr><td>Neighbourhood</td><td>Bramalea</td></tr>
    <tr><td>Region</td><td>Region of Peel</td></tr>
    <tr><td>Waste Collection</td><td>Region of Peel curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Brampton Zoning By-law 270-2004 (as amended); zone <strong>R2A(1)</strong></td></tr>
    <tr><td>Legal Description</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Year Built</td><td>To be confirmed in Phase 2</td></tr>
    <tr><td>Lot size</td><td>~387 m² (City-computed screening value — confirmed in Phase 2)</td></tr>
    <tr><td>Development Goals</td><td>Convert the existing duplex to a triplex; add a third residential unit</td></tr>'''))

# ---- NEIGHBOURHOOD SPOTLIGHT ----
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
    32 Medici Place is on a quiet residential court in Bramalea, an established community in northeast Brampton within the Region of Peel:
    <ul>
      <li>Settled, family-oriented residential streets — the kind of stock that rents steadily and holds value</li>
      <li>Close to Bramalea City Centre for shopping, transit, and services</li>
      <li>Served by Brampton Transit, with Züm bus rapid transit on nearby corridors and GO Transit access to the wider GTA</li>
      <li>Parks, schools, and community facilities throughout Bramalea</li>
      <li>Illustrative context only, not a valuation.</li>
    </ul>'''))

# ---- ZONING TABLE ----
R.append(('''    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>''',
'''    <tr><td>Current Zoning</td><td>R2A(1) — Residential (Brampton Zoning By-law 270-2004, as amended)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>The lot must be a serviced residential lot (municipal water &amp; sewer) within a settlement area — the provincial criteria for as-of-right additional residential units. Exact lot standards confirmed in Phase 2.</td></tr>
    <tr><td>Recent Changes</td><td>Under Ontario's Bill 23 (More Homes Built Faster Act), up to <strong>3 residential units</strong> are permitted as-of-right on a serviced residential lot — no rezoning required. Brampton administers additional residential units under its ARU framework.</td></tr>
    <tr><td>Permitted Uses</td><td>An additional residential unit — an attached second/third unit and/or a detached garden suite — is permitted on a residential lot, up to <strong>3 units total</strong>, subject to Brampton's site standards (setbacks, height, floor-area limits) and registration. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>'''))

# ---- WHAT THIS MEANS FOR YOU (list) ----
R.append(('''      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>''',
'''      <li><strong>Additional Residential Units:</strong> up to three units on the lot under Ontario's Bill 23 — your existing home plus additional units</li>
      <li><strong>Internal / Attached Suites:</strong> a second and third unit created within or attached to the existing dwelling — the direct path for a duplex-to-triplex conversion</li>
      <li><strong>Detached Garden Suite:</strong> a self-contained unit in the rear yard may count toward the three-unit total, where the lot's dimensions allow (confirmed in Phase 2)</li>
      <li><strong>Registration required:</strong> additional residential units must be registered with the City to be legal — part of the Phase 2 pathway</li>'''))

# ---- TIME-SENSITIVE ----
R.append(('''    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>''',
'''    <div class="d"><div class="dt">Residential Rental Licence<br><small>in effect Jan 1, 2026</small></div><div class="dx">Brampton requires a citywide Residential Rental Licence for rental properties of 1–4 units as of January 1, 2026, and additional residential units must be registered with the City to be legal. Building this into the plan from Day 1 keeps the project compliant and financeable. Requirements confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">ARU Development-Charge Exemption</div><div class="dx">Additional residential units are exempt from municipal development charges under provincial legislation — a meaningful per-unit saving on a new suite. Applicability to your project is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>'''))

# ---- REZONING: green callout ----
R.append(('<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>',
          '<div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended three-unit (duplex-to-triplex) configuration is permitted as-of-right under Ontario\'s Bill 23 and Brampton\'s ARU framework.</div>'))

# ---- REZONING: comparison last row ----
R.append(('<tr><td>What governs your build</td><td class="g">By-law 654-2025</td><td class="n">A new site-specific by-law</td></tr>',
          '<tr><td>What governs your build</td><td class="g">Bill 23 + Brampton By-law 270-2004</td><td class="n">A new site-specific by-law</td></tr>'))

# ---- REZONING: two cards ----
R.append(('''    <div class="card2"><div class="ct">Six-unit houseplex</div>Ward 19 sits in the Toronto &amp; East York district, one of nine wards where By-law 654-2025 permits up to six units in a residential zone without rezoning.</div>
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's Garden Suite By-law (February 2022) permits a rear ancillary suite on a non-laneway lot as-of-right in residential zones.</div>''',
'''    <div class="card2"><div class="ct">Three units as-of-right</div>Under Bill 23, a serviced residential lot may support up to three residential units — an attached second and third unit and/or a garden suite — without rezoning.</div>
    <div class="card2"><div class="ct">Registered additional units</div>Additional residential units must be registered with the City of Brampton to be legal; the Planning Division reviews garden suites before a building permit is issued.</div>'''))

# ---- REZONING: "what this means" heading + paragraph ----
R.append(('<div class="barhead" style="text-align:left;">What this means for 303 Coxwell Avenue</div>\n  <p>Because 303 Coxwell Avenue already permits the recommended build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>',
          '<div class="barhead" style="text-align:left;">What this means for 32 Medici Place</div>\n  <p>Because 32 Medici Place already permits the recommended three-unit build under existing zoning, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. The comparison below shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>'))

# ---- REZONING: amber note ----
R.append(('<div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>',
          '<div class="co-amber"><b>One item to confirm: the legal status of the existing duplex.</b><br><span class="sub">Additional residential units must be registered with the City; if any existing unit was created without a permit, a retroactive application is needed before financing or development can proceed. Confirmed in Phase 2.</span></div>'))

# ---- DEVELOPMENT OPTIONS ----
R.append(('<div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>',
          '<div class="opt"><div class="oh">Option A — Duplex to Triplex (add a third internal unit) — your goal</div>'))
R.append(('''      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>''',
'''      <div class="od">Add a third residential unit within or attached to the existing home — the direct route from your current duplex to a triplex, and your stated goal. Permitted as-of-right under Bill 23 on a serviced residential lot; no rezoning. The City's screening data indicates an internal/attached additional unit is the fit for this lot. Exact unit sizes, egress, parking, and servicing are set by Brampton's standards and confirmed in Phase 2. The unit must be registered with the City to be legal.</div>'''))

R.append(('<div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Add a Detached Garden Suite</div>'))
R.append(('''      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>''',
'''      <div class="od">A self-contained detached suite in the rear yard can serve as the third unit instead of an internal one, where the lot's dimensions allow. Garden suites are permitted under Bill 23 but their size and siting depend on rear-yard space, setbacks, and a floor-area cap; the City's screening data shows limited backyard buildable area on this lot, so this path is confirmed against the exact lot dimensions in Phase 2. Garden-suite approval starts with Brampton's Planning Division before a building permit.</div>'''))

R.append(('<div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>',
          '<div class="opt"><div class="oh">Option C — Note on the Existing Duplex</div>'))
R.append(('''      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>''',
'''      <div class="od">Confirming the legal and permit status of the existing two units is an essential first step — both for financing qualification and for counting them as legal units toward the three-unit total. Additional residential units must be registered with the City of Brampton. If any existing unit was created without a permit, a retroactive permit application will be required before any development or financing process can proceed. This is confirmed in Phase 2.</div>'''))

# ---- GOAL SUMMARY ----
R.append(('''  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>''',
'''  <div class="barhead" style="text-align:left;">Duplex-to-Triplex Configuration</div>
  <p>32 Medici Place is a serviced residential lot in Bramalea where, under Bill 23, up to three residential units are permitted as-of-right — matching your goal of converting the existing duplex to a triplex. <strong>Adding a third unit is the clear primary recommendation</strong>, with a detached garden suite as an alternative path for the third unit where the lot allows.</p>'''))

# ---- SUMMARY: Current Zoning Review ----
R.append(('''  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>''',
'''  <p>32 Medici Place is a serviced residential lot in Bramalea, Brampton. Under Ontario's Bill 23, up to <strong>three residential units are permitted as-of-right</strong> — the path to converting your existing duplex into a triplex — with no rezoning required, subject to the City's site standards and unit registration.</p>
  <ul>
    <li><strong>The Three-Unit As-of-Right Advantage:</strong> a serviced residential lot may add units under Bill 23 without a rezoning, public hearing, or Council approval — the exact unit mix and sizes are confirmed in Phase 2.</li>
  </ul>'''))

# ---- GRANTS TABLE (Toronto DC-waiver row -> Brampton/provincial incentives) ----
R.append(('''    <tr><td>Federal</td><td>GST/HST Purpose-Built Rental Housing (PBRH) Rebate</td><td>Full 100% rebate of the 5% federal GST on new purpose-built rental projects with 4+ units, 90%+ as long-term rental. Construction must start before 2031. Ontario mirrors this with a 100% rebate of the 8% provincial HST component — together up to $130,000 in tax savings per unit on projects valued up to $1.5M. Temporary enhancement active April 1, 2026 to March 31, 2027.</td></tr>
    <tr><td>Federal</td><td>CMHC Apartment Construction Loan Program (ACLP)</td><td>Provides low-interest construction loans up to 100% of residential project cost for purpose-built rental. Minimum $1M loan. Open as of June 2026. Can be structured to bridge into MLI Select permanent financing at project completion.</td></tr>
    <tr><td>Federal</td><td>CMHC Prefab Plus (modular construction)</td><td>A newly expanded CMHC program (as of May 2026) that brings modular/prefab construction into the MLI Select financing framework. Could shorten construction timelines.</td></tr>
    <tr><td>Municipal</td><td>Toronto Development Charge Waiver (Bill 185)</td><td>Development charges fully eliminated for multiplexes up to 6 units (Bill 185, January 2025). Saves $200,000–$270,000 per project (~$45,000–$50,000 per unit). Parking minimums also waived city-wide since February 2022, saving an additional $50,000–$100,000 in site costs. No application required — benefit applies automatically to compliant builds.</td></tr>''',
'''    <tr><td>Provincial</td><td>ARU Development Charge Exemption</td><td>Additional residential units are exempt from municipal development charges under provincial legislation (Bill 23) — a meaningful per-unit saving on a new suite. Confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where the new suite houses an eligible relative (senior or adult with a disability). Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as Canada Greener Homes and utility retrofit rebates may offset efficient design and equipment on a new unit. Availability and eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Property Rebate</td><td>May apply to a newly built rental unit; the enhanced purpose-built rental rebate targets larger 4+ unit projects. Applicability to a three-unit project is confirmed in Phase 2.</td></tr>'''))

# ---------------------------------------------------------------- apply
fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:70]!r}")
        fails += 1
    else:
        s = s.replace(old, new)

# leftover check — nothing from the source property/city may remain
for t in ["Coxwell", "Toronto", "Ward 19", "Beaches", "John Arockiaraj",
          "654-2025", "6+1", "Bill 185", "M4L", "569-2013", "474-2023"]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

open(OUT, "w", encoding="utf-8").write(s)
print(f"done, fails: {fails}, wrote {OUT}")
