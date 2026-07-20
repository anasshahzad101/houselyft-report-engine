"""
xform_17_theresa.py — adapt the House Lyft master report for
17 Theresa Avenue, North York (Toronto), Ward 18 (Willowdale).

Lead: Nick S. Scope (GHL EPzqHHy5AU2iIvHIAhKf): "Garden Suite, Laneway Home
or ADU" -> units_added = 1, scoped mode. Sentence field: grants/funding ask.

Engine (verified adapter): RD (f15.0; a550) (x5), Ward 18 Willowdale,
main_units_max = 4 (NOT a sixplex ward), adu_stacking_on_multiplex = True.

Gating for a scoped 1-unit ADU in Toronto (config/programs.json):
  clears at 1 unit  -> Bill 23 DC exemption (first 2 ARUs), Toronto DC relief
  clears at 4+ only -> GST/HST PBRH rebate  -> moves INTO Option B
  clears at 5 only  -> CMHC MLI Select      -> moves INTO Option C (conditional)
  dropped (wrong geo / unconfirmable) -> Mississauga 4th-unit, Simcoe, Alberta,
                                         Edmonton, ACLP, Prefab Plus, MHRTC.

Follows the xform doctrine: every replacement asserts it matched exactly once,
then the rendered file is grepped for leftovers from the source (Coxwell /
Arockiaraj / sixplex / Ward 19).
"""
import base64
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
SRC = os.path.join(TPL, "report_houselyft_master.html")
OUT = os.path.join(TPL, "report_17_theresa.html")
SCRATCH = ("/tmp/claude-0/-home-user-houselyft-report-engine/"
           "4bd62836-62ff-5e18-acfe-df6ed24879d6/scratchpad")

html = open(SRC, encoding="utf-8").read()

reps = []  # (label, old, new)


def rep(label, old, new):
    reps.append((label, old, new))


# ---------------------------------------------------------------- aerials
def data_uri(path):
    b = base64.b64encode(open(path, "rb").read()).decode()
    return "data:image/jpeg;base64," + b


LOT = data_uri(os.path.join(SCRATCH, "aerial_lot.jpg"))
CTX = data_uri(os.path.join(SCRATCH, "aerial_ctx.jpg"))

# CSS for the real aerial tiles (overlay caption, 148px, side by side)
rep("aerial-css",
    "  .imgbox.tall{height:148px;} .imgbox .ic{font-size:20pt;line-height:1;margin-bottom:6px;color:#c2c8d4;}",
    "  .imgbox.tall{height:148px;} .imgbox .ic{font-size:20pt;line-height:1;margin-bottom:6px;color:#c2c8d4;}\n"
    "  .aerial{position:relative;flex:1;height:148px;overflow:hidden;border:1px solid var(--line);}\n"
    "  .aerial img{width:100%;height:148px;object-fit:cover;display:block;}\n"
    "  .aerial .cap{position:absolute;left:0;right:0;bottom:0;background:rgba(27,42,74,.72);color:#fff;"
    "font-family:'Lato';font-size:7pt;padding:3px 7px;}")

# ---------------------------------------------------------------- COVER
rep("cover",
    '  <div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
    '  <div class="addr">17 Theresa Avenue<span>North York (Toronto), ON</span></div>')

# ---------------------------------------------------------------- 1. PROPERTY DETAILS
old_pd = '''<!-- 1 PROPERTY DETAILS -->
<div class="section">
  <h2 class="sec">1. Property Details</h2>
  <div class="barhead">303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</div>
  <div class="imgrow" style="margin-top:0;">
    <div class="imgbox tall"><span class="ic">◎</span>Aerial view<br><small>(auto-generated)</small></div>
    <div class="imgbox tall"><span class="ic">▤</span>Street view<br><small>(auto-generated)</small></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: source and licence inserted at generation.</div>
  <table class="kv">
    <tr><td>Property Address</td><td>303 Coxwell Avenue, Toronto, ON&nbsp;&nbsp;M4L 3B5</td></tr>
    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>
    <tr><td>Development Goals</td><td>4+1 or 6+1 Multiplex; Maximize unit count; To Be Decided</td></tr>
  </table>
  <table class="kv">
    <tr><td>Municipality</td><td>Toronto</td></tr>
    <tr><td>Neighbourhood</td><td>Woodbine Corridor / Upper Beaches</td></tr>
    <tr><td>Ward</td><td>Ward 19 — Beaches-East York</td></tr>
    <tr><td>Community League</td><td>Greenwood-Coxwell / Upper Beaches</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>Pre-1980 (Att/Row/Townhouse, 1.5 storey)</td></tr>
    <tr><td>Lot size</td><td>~315.9 m² (20 ft × 170 ft / approx. 3,400 sq ft)</td></tr>
    <tr><td>Development Goals</td><td>6+1 Multiplex (primary); 4+1 Multiplex (alternative)</td></tr>
  </table>
  <div class="cell">
    <div class="ct">Neighbourhood Spotlight</div>
    303 Coxwell Avenue is located in the Woodbine Corridor / Upper Beaches neighbourhood at the intersection of Coxwell Ave and Gerrard Street East — one of Toronto's most walkable and transit-connected east-end communities:
    <ul>
      <li>Borders Greenwood-Coxwell, Danforth, and The Beaches neighbourhoods</li>
      <li>Rocca's No Frills grocery steps away; Coxwell subway station approximately 1 km north</li>
      <li>Multiple TTC routes at the intersection: Coxwell (22), Carlton (506), and more</li>
      <li>Regular bus service along 87, 92, and 95 Avenues and 156, 163, and 170 Streets</li>
      <li>Greenwood Park approximately 9-minute walk; restaurants and retail along Gerrard Street East and Danforth Avenue</li>
    </ul>
  </div>
</div>'''

new_pd = '''<!-- 1 PROPERTY DETAILS -->
<div class="section">
  <h2 class="sec">1. Property Details</h2>
  <div class="barhead">17 Theresa Avenue, North York (Toronto), ON&nbsp;&nbsp;M2M 1W4</div>
  <div class="imgrow" style="margin-top:0;">
    <div class="aerial"><img src="__LOT__" alt="Aerial view of 17 Theresa Avenue"><span class="cap">Aerial view — approx. 90 m across</span></div>
    <div class="aerial"><img src="__CTX__" alt="Neighbourhood context around 17 Theresa Avenue"><span class="cap">Neighbourhood context — approx. 240 m across</span></div>
  </div>
  <div class="imglicense" style="font-size:6pt;color:#9aa2b2;margin:-6px 0 8px;">Imagery: City of Toronto Orthophoto, 2025 (8&nbsp;cm). Contains information licensed under the Open Government Licence – Toronto.</div>
  <table class="kv">
    <tr><td>Property Address</td><td>17 Theresa Avenue, North York (Toronto), ON&nbsp;&nbsp;M2M 1W4</td></tr>
    <tr><td>Name</td><td>Nick S</td></tr>
    <tr><td>Phone Number</td><td>(647) 830-9914</td></tr>
    <tr><td>Email</td><td>nickan_sadghian@hotmail.com</td></tr>
    <tr><td>Development Goals</td><td>Garden Suite, Laneway Home or ADU; understand available grants and funding options</td></tr>
  </table>
  <table class="kv">
    <tr><td>Municipality</td><td>Toronto (North York district)</td></tr>
    <tr><td>Neighbourhood</td><td>Newtonbrook West / Willowdale</td></tr>
    <tr><td>Ward</td><td>Ward 18 — Willowdale</td></tr>
    <tr><td>Waste Collection</td><td>Contact City of Toronto for local schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Toronto Zoning By-law 569-2013 (as amended)</td></tr>
    <tr><td>Zoning</td><td>RD (f15.0; a550) (x5) — exception 900.3.10(5)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Year Built</td><td>To be confirmed during the feasibility phase</td></tr>
    <tr><td>Lot size</td><td>To be confirmed during the feasibility phase (MPAC / survey)</td></tr>
    <tr><td>Development Goals</td><td>Rear garden suite / detached ADU (primary); up to a 4-unit multiplex (as-of-right upside)</td></tr>
  </table>
  <div class="cell">
    <div class="ct">Neighbourhood Spotlight</div>
    17 Theresa Avenue sits in the Newtonbrook West / Willowdale area of North York, an established low-rise residential neighbourhood of detached homes on generous lots:
    <ul>
      <li>Typical of the Yonge Street north corridor in North York — quiet residential streets with deep rear yards well suited to a garden suite</li>
      <li>Close to the Yonge Street corridor and its transit, retail, and services (confirm specific routes and amenities locally)</li>
      <li>Full City of Toronto municipal servicing (water, sewer, waste collection)</li>
      <li>Aerial imagery above shows the lot and its surrounding block context</li>
    </ul>
  </div>
</div>'''
rep("property-details", old_pd, new_pd)

# ---------------------------------------------------------------- 2. ZONING
old_zone = '''<!-- 2 ZONING -->
<div class="section">
  <h2 class="sec">2. Current Zoning</h2>
  <table class="kv">
    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013)</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. Ward 19 (Beaches-East York) is in the Toronto &amp; East York Community Council district — one of nine wards where 6-unit houseplexes are permitted as-of-right under By-law 654-2025.</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 474-2023); up to 6 units as-of-right in Ward 19 — Toronto &amp; East York district (By-law 654-2025, June 2025). No rezoning required for either scenario.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone in Ward 19 (Toronto &amp; East York district) allows up to <strong>6 residential units</strong> as-of-right in a detached houseplex under By-law 654-2025, subject to technical review of site conditions.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you…</div>
    <ul style="margin-top:0;">
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes — side-by-side units (townhouse) or vertically stacked units (stacked townhouse)</li>
      <li><strong>Detached Houseplex / Semi-detached Houseplex:</strong> Standalone multi-unit homes</li>
      <li><strong>Low-Rise Apartment Building:</strong> Small-scale apartment buildings</li>
      <li><strong>Internal &amp; Backyard Suites:</strong> Secondary suites (like basement or garden suites) can be seamlessly paired with main dwellings to boost density</li>
    </ul>
  </div>
</div>'''

new_zone = '''<!-- 2 ZONING -->
<div class="section">
  <h2 class="sec">2. Current Zoning</h2>
  <table class="kv">
    <tr><td>Current Zoning</td><td>RD — Residential Detached (Toronto Zoning By-law 569-2013, as amended). Zone label RD (f15.0; a550) (x5), exception 900.3.10(5).</td></tr>
    <tr><td>Minimum Site Requirements</td><td>Official Plan Designation: Neighbourhoods. The zone standard cites a minimum required frontage of 15.0 m; the actual lot frontage and area are to be confirmed during the feasibility phase (MPAC / survey).</td></tr>
    <tr><td>Recent Changes</td><td>Up to 4 units as-of-right city-wide (By-law 0473/0474, May 2023). A detached garden or laneway suite is permitted as-of-right in residential zones under Toronto's ADU by-law (89-2022, as amended, aligned to O. Reg. 462/24). No rezoning required for a garden suite or a multiplex of up to four units.</td></tr>
    <tr><td>Permitted Uses</td><td>Multi-Unit Housing Types — the RD zone permits a detached <strong>garden or laneway suite</strong> as-of-right, and a multiplex of up to <strong>4 residential units</strong> as-of-right city-wide, subject to technical review of site conditions. Ward 18 (Willowdale) is <strong>not</strong> among the nine wards where six units are permitted as-of-right, so the as-of-right ceiling here is four units.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong> — a rear garden suite / detached ADU is permitted as-of-right; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you…</div>
    <ul style="margin-top:0;">
      <li><strong>Garden Suite / Laneway Suite:</strong> A detached backyard home — one detached ADU is permitted per lot (garden <em>or</em> laneway, never both). This is your stated goal.</li>
      <li><strong>Internal &amp; Basement Suites:</strong> Secondary suites paired with the main dwelling to add units within the existing house.</li>
      <li><strong>Detached Houseplex / Multiplex:</strong> A standalone multi-unit home of up to four units as-of-right — an upside path if you decide to build larger.</li>
      <li><strong>Townhouse &amp; Stacked Townhouse:</strong> Multi-unit attached homes, within the four-unit as-of-right envelope.</li>
    </ul>
  </div>
</div>'''
rep("zoning", old_zone, new_zone)

# ---------------------------------------------------------------- TIME SENSITIVE
old_ts = '''<!-- TIME SENSITIVE -->
<div class="section">
  <h2 class="sec">⚠️ Time-Sensitive Information</h2>
  <div class="ts">
    <div class="d"><div class="dt">Ontario HST Rebate — Act Now<br><small>~ 6 weeks from now</small></div><div class="dx">Ontario's 2026 Budget (March 26, 2026) introduced a 100% rebate of the 8% provincial HST component on new purpose-built rental housing, stacking on top of the existing federal PBRH rebate. For units valued up to $1M, savings can reach $80,000 per unit in provincial relief alone. This is a temporary enhancement — applications require the agreement be signed between April 1, 2026 and March 31, 2027. Structuring the project correctly from Day 1 is essential to capture this.</div></div>
    <div class="d"><div class="dt">DC Waiver — Already in Effect<br><small>~ 3 weeks from now</small></div><div class="dx">Development charges are fully eliminated for multiplexes up to 6 units in Toronto (Bill 185, January 2025). This saves $200,000–$270,000 per project — approximately $45,000–$50,000 per unit — at no application required. This benefit is locked in as long as your project stays within the 6-unit as-of-right envelope.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>
</div>'''

new_ts = '''<!-- TIME SENSITIVE -->
<div class="section">
  <h2 class="sec">⚠️ Time-Sensitive Information</h2>
  <div class="ts">
    <div class="d"><div class="dt">DC Exemption — Already in Effect</div><div class="dx">Under Ontario's More Homes Built Faster Act (Bill 23), the first two additional residential units on a serviced lot — which includes a garden or laneway suite — are exempt from municipal development charges. Toronto separately waives development charges on multiplexes of up to six units (Bill 185, January 2025). A garden suite sits comfortably within both. No application is required for the exemption; exact figures to be confirmed during the feasibility phase.</div></div>
    <div class="d"><div class="dt">HST Rental Rebates — If You Build Larger</div><div class="dx">The federal and Ontario GST/HST purpose-built rental rebates apply to projects of four or more self-contained rental units that are held as long-term rentals (construction started before 2031). A single garden suite does not reach that threshold, but if you scale to a four-unit multiplex these rebates open up. Note also that renting out a newly built garden suite can trigger HST self-supply rules — the offsetting New Residential Rental Property rebate is time-sensitive and should be reviewed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>
</div>'''
rep("time-sensitive", old_ts, new_ts)

# ---------------------------------------------------------------- 3. REZONING
old_rz = '''<!-- 3 REZONING -->
<div class="section">
  <h2 class="sec">3. Rezoning (If Applicable)</h2>
  <p>Rezoning is when the city changes the local planning rules to legally allow more housing units, taller buildings, or different types of properties to be built on a specific piece of land than what was originally allowed. Think of it as the city giving a property a "regulatory upgrade".</p>
  <div class="co-green"><div class="ct2">Not Required for This Property</div>The recommended 6+1 configuration is permitted as-of-right under Toronto By-law 654-2025.</div>
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
  <div class="co-amber"><b>One item to confirm: the permit status of the existing rear garage.</b><br><span class="sub">If it was converted without a permit, a retroactive application is needed before financing or development can proceed.</span></div>
</div>'''

new_rz = '''<!-- 3 REZONING -->
<div class="section">
  <h2 class="sec">3. Rezoning (If Applicable)</h2>
  <p>Rezoning is when the city changes the local planning rules to legally allow more housing units, taller buildings, or different types of properties to be built on a specific piece of land than what was originally allowed. Think of it as the city giving a property a "regulatory upgrade".</p>
  <div class="co-green"><div class="ct2">Not Required for This Property</div>A rear garden suite is permitted as-of-right in Toronto's residential zones, as is a multiplex of up to four units — no rezoning is required for either.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-laws 89-2022 &amp; 0473/0474</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Rear garden suite</div>Toronto's garden-suite by-law permits a detached rear suite as-of-right in residential zones on a lot without laneway access. One detached ADU per lot — garden or laneway, never both.</div>
    <div class="card2"><div class="ct">Up to a four-unit multiplex</div>Up to four residential units are permitted as-of-right city-wide (By-law 0473/0474). Ward 18 is not one of the nine six-unit wards, so four units is the as-of-right ceiling here.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 17 Theresa Avenue</div>
  <p>Because a garden suite is permitted under existing zoning, no rezoning application is contemplated for your stated goal. Your project advances directly to design and permitting. The comparison above shows what that avoids. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions.</p>
  <div class="co-amber"><b>Items to confirm in feasibility.</b><br><span class="sub">Whether the lot has public-laneway access (this decides garden vs. laneway suite — the aerial suggests a garden suite), the buildable footprint, height and setbacks for the suite, protected trees, and any heritage or ravine overlay. Toronto's garden-suite footprint, height and setback numbers currently vary between sources and must be reconciled against the by-law before design.</span></div>
</div>'''
rep("rezoning", old_rz, new_rz)

# ---------------------------------------------------------------- 4. DEVELOPMENT OPTIONS
old_opt = '''<!-- 4 DEVELOPMENT OPTIONS -->
<div class="section">
  <h2 class="sec">4. Development Options</h2>
  <div class="opt"><div class="oh">Option A — 4-Unit Multiplex + 1 Garden Suite (4+1)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">A detached 4-unit houseplex on the main structure, plus one garden suite in the rear utilizing the existing ~750 sq ft converted garage. Total: 5 independent units. Fully as-of-right under By-law 474-2023. No rezoning, no variances likely required if designed within the standard envelope. The existing garage — with its 12 ft ceilings, heated floors, running water, and powder room — provides a strong head start on the ancillary suite. Lot: 20 ft x 170 ft (~315.9 m²). Corner lot configuration with street frontage on Coxwell Ave and a flanking side street. RD zone built-form standards apply. No parking minimums for multiplexes. Development charges fully waived for ≤6 units (Bill 185).</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — 6-Unit Multiplex + 1 Garden Suite (6+1) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">A detached 6-unit houseplex (as-of-right in Ward 19 under By-law 654-2025) plus one garden suite in the rear. Total: 7 independent units. This matches John's stated goal. The 20 ft frontage on a 170 ft deep lot is narrow but workable for a stacked or back-to-back configuration. The corner lot provides an additional entrance point improving unit separation and access. A minor variance may be required depending on the final design footprint. No parking spaces required. Development charges fully waived.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Note on the Existing Garage / Rear Suite</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">The existing ~750 sq ft garage (12 ft ceilings, heated floors, running water, powder room) may have been converted or is in process. Under Toronto's Garden Suite By-law (February 2022), a rear ancillary suite on a non-laneway lot is permitted as-of-right in residential zones. Confirming the permit status of this structure is an essential first step — both for financing qualification and for counting it as a legal unit. If the conversion was done without a permit, a retroactive permit application will be required before any development or financing process can proceed.</div>
    </div></div>
</div>'''

new_opt = '''<!-- 4 DEVELOPMENT OPTIONS -->
<div class="section">
  <h2 class="sec">4. Development Options</h2>
  <div class="opt"><div class="oh">Option A — Rear Garden Suite / Detached ADU — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">One detached suite in the rear yard — your stated goal. Permitted as-of-right in the RD zone under Toronto's garden-suite by-law (89-2022, as amended, aligned to O. Reg. 462/24); no rezoning required. The aerial shows a deep rear yard typical of this North York block, which is well suited to a garden suite. No car parking is required (two bicycle spaces are); a 1.0 m unobstructed fire-access path from the street to the rear yard must be maintained and cannot be varied. Free "Made in Toronto" pre-approved garden-suite plans (launched 2025) can speed approvals and cut design cost. The suite's exact footprint, height and setbacks are to be confirmed during the feasibility phase — Toronto's current numbers vary between sources and are reconciled against the by-law at design. One detached ADU is allowed per lot (garden or laneway, never both), and it stays on the main lot — it cannot be severed or sold separately.</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — Up to a 4-Unit Multiplex (As-of-Right Upside)</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">If you decide to build larger, up to four residential units are permitted as-of-right city-wide (By-law 0473/0474) — no rezoning, no public meeting if designed within the envelope. Ward 18 is not one of the nine six-unit wards, so four units is the as-of-right ceiling on this lot. No parking spaces are required. A minor variance may be needed depending on the final footprint. <strong>At four or more self-contained rental units, the federal and Ontario GST/HST purpose-built rental rebates open up</strong> (90%+ long-term rental, construction started before 2031) — relief that a single garden suite does not reach. Buildable area, height, coverage and setbacks are to be confirmed in feasibility once lot dimensions are established.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Four-Unit Multiplex + Garden Suite (Up to 5 Units — Deep Upside)</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">A four-unit multiplex plus one rear garden suite — up to five units in total. Toronto permits a detached ADU to stack on a multiplex of four units and under; whether that stacking applies to your specific lot is an item to confirm in Phase 2, so this option is shown as an upside rather than a firm recommendation. <strong>If the project reaches five rental units, CMHC MLI Select's five-unit minimum would be met</strong>, potentially unlocking longer amortization and higher loan-to-cost on a points system — noted here conditionally, subject to confirming the five-unit configuration and current CMHC thresholds. Development charges remain within Toronto's up-to-six-unit relief envelope.</div>
    </div></div>
</div>'''
rep("options", old_opt, new_opt)

# ---------------------------------------------------------------- 5. GOAL SUMMARY
old_gs = '''<!-- 5 DEVELOPMENT GOAL SUMMARY -->
<div class="section flow">
  <h2 class="sec">5. Development Goal Summary</h2>
  <div class="barhead" style="text-align:left;">6+1 Configuration</div>
  <p>303 Coxwell Avenue is in Ward 19 — one of only nine wards in Toronto where up to six units are permitted as-of-right in a residential zone under By-law 654-2025. <strong>The 6+1 configuration is the clear primary recommendation.</strong></p>
</div>'''

new_gs = '''<!-- 5 DEVELOPMENT GOAL SUMMARY -->
<div class="section flow">
  <h2 class="sec">5. Development Goal Summary</h2>
  <div class="barhead" style="text-align:left;">Rear Garden Suite (Primary)</div>
  <p>17 Theresa Avenue supports your stated goal directly: a rear garden suite / detached ADU is permitted as-of-right in the RD zone, with no rezoning required. <strong>The garden suite is the clear primary recommendation.</strong> Should you decide to build larger, the lot also permits up to a four-unit multiplex as-of-right (Ward 18 is not a six-unit ward), and a four-unit multiplex with a garden suite could reach up to five units — both shown above as upside paths, each subject to feasibility confirmation.</p>
</div>'''
rep("goal-summary", old_gs, new_gs)

# ---------------------------------------------------------------- 7. GRANTS (fill gated table)
old_grants_table = '''  <table class="g">
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
    </table>'''

new_grants_table = '''  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>Development-Charge Exemption — Additional Residential Units (Bill 23)</td><td>The first two additional residential units on a serviced lot — including a garden or laneway suite — are exempt from municipal development charges. No application required. Source: Ontario, More Homes Built Faster Act (Bill 23).</td></tr>
    <tr><td>Municipal</td><td>Toronto Development-Charge Relief (Bill 185)</td><td>Toronto waives development charges on multiplexes of up to six units; a garden suite sits within this envelope. Exact figures to be confirmed during the feasibility phase. Source: City of Toronto, Bill 185 (January 2025).</td></tr>
    <tr><td>Financing</td><td>Refinance · HELOC · Construction financing</td><td>Available at any project scale — see Section 6. These fund the build against your existing equity and the completed value of the new suite.</td></tr>
    </table>
  <div class="co-amber" style="margin-top:12px;"><b>What scaling up would unlock.</b><br><span class="sub">The programs above apply to your garden suite today. If you later build to four or more rental units, the federal and Ontario GST/HST purpose-built rental rebates open up; at five rental units, CMHC MLI Select's five-unit minimum is met (see Options B and C). These are shown at their thresholds, not claimed as available to a single suite.</span></div>'''
rep("grants-table", old_grants_table, new_grants_table)

# ---------------------------------------------------------------- 8. SUMMARY
old_sum = '''  <h3>Current Zoning Review</h3>
  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>'''

new_sum = '''  <h3>Current Zoning Review</h3>
  <p>17 Theresa Avenue confirms a clear development path for your stated goal. The property is in the RD (Residential Detached) zone in Ward 18 (Willowdale), where a detached <strong>garden or laneway suite is permitted as-of-right</strong> — no rezoning, no public hearing, no Council approval required. A multiplex of up to four units is also permitted as-of-right city-wide, giving you room to build larger if you choose.</p>
  <ul>
    <li><strong>Your garden suite is as-of-right:</strong> Toronto's ADU by-law permits one detached rear suite in the RD zone, subject to a technical review of footprint, height and setbacks in feasibility.</li>
    <li><strong>Headroom to grow:</strong> up to four units as-of-right (Ward 18 is not a six-unit ward), and up to five with a garden suite added — each an optional upside, not a requirement.</li>
  </ul>'''
rep("summary", old_sum, new_sum)

# ---------------------------------------------------------------- apply
for label, old, new in reps:
    n = html.count(old)
    if n != 1:
        print(f"ASSERT FAIL [{label}]: expected exactly 1 match, found {n}")
        sys.exit(1)
    html = html.replace(old, new)

# ---------------------------------------------------------------- leftover guard
# Runs BEFORE the aerial data-URIs are injected: base64 blobs legitimately
# contain substrings like "6+1" ('+' is a base64 char), which would false-positive.
banned = ["303 Coxwell", "Coxwell", "Arockiaraj", "johneeraj", "Beaches-East York",
          "Ward 19", "654-2025", "six-unit as-of-right", "6+1", "6-Unit", "6-unit",
          "sixplex", "Six-unit", "Six-Unit", "Woodbine", "Greenwood",
          "223-4342", "M4L 3B5", "750 sq ft", "20 ft x 170 ft"]
found = [b for b in banned if b in html]
if found:
    print("LEFTOVER GUARD FAIL — source-city references remain:", found)
    sys.exit(1)

# inject aerials (data URIs are large; substitute after the guard has run)
for token, uri in (("__LOT__", LOT), ("__CTX__", CTX)):
    if html.count(token) != 1:
        print(f"ASSERT FAIL [aerial {token}]: found {html.count(token)}")
        sys.exit(1)
    html = html.replace(token, uri)

open(OUT, "w", encoding="utf-8").write(html)
print("OK ->", OUT)
print("bytes:", len(html))
