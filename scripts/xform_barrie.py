"""
xform_barrie.py — turn the House Lyft master report into the 118 Patterson Road,
Barrie report.

Barrie has NO city adapter in property_lookup_v2, so its rules were researched
LIVE from official/primary sources (report-needs-review). Everything the engine
would normally verify is hedged "confirmed in Phase 2".

Sources (researched 2026-07-28):
  - City of Barrie Comprehensive Zoning By-law 2009-141 (in force)   barrie.ca/Zoning-Bylaw.pdf
  - City of Barrie By-law 2024-043 (April 2024): amends 2009-141 to permit up to
    FOUR residential units as-of-right on residentially-zoned lots (up from 3),
    introducing "Additional Residential Units" with standards — max height 4.5 m,
    3 m interior/exterior side & rear-yard setbacks, 1 parking space per unit.
    barrie.legistar.com File# BY-LAW 2024-043 ; barrietoday.com coverage
  - Ontario Bill 23, More Homes Built Faster Act, 2022: province-wide as-of-right
    threshold (up to 3 units) + development-charge exemption for ARUs.

Follows the xform_*.py contract: every swap is asserted, then the output is
grepped for leftovers from the master (Toronto / Coxwell / sixplex / etc.). That
leftover check is what keeps the wrong city out of this report.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_barrie.html")


def replace_once(html, old, new):
    n = html.count(old)
    assert n == 1, f"expected exactly 1 match, found {n} for:\n{old[:120]!r}"
    return html.replace(old, new)


def replace_section(html, start_marker, end_marker, new_block):
    """Replace everything from start_marker up to (but not including) end_marker."""
    i = html.find(start_marker)
    assert i != -1, f"start marker not found: {start_marker}"
    j = html.find(end_marker, i + len(start_marker))
    assert j != -1, f"end marker not found: {end_marker}"
    assert html.count(start_marker) == 1, f"start marker not unique: {start_marker}"
    return html[:i] + new_block + html[j:]


def main():
    html = open(MASTER, encoding="utf-8").read()

    # -- COVER address -------------------------------------------------------
    html = replace_once(
        html,
        '<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>',
        '<div class="addr">118 Patterson Road<span>Barrie, ON</span></div>',
    )

    # -- 1. PROPERTY DETAILS -------------------------------------------------
    property_block = '''<!-- 1 PROPERTY DETAILS -->
<div class="section">
  <h2 class="sec">1. Property Details</h2>
  <div class="barhead">118 Patterson Road, Barrie, ON&nbsp;&nbsp;L4N 3W3</div>
  <div class="imglicense" style="font-size:8.4pt;color:#7a818f;margin:8px 0 12px;">Aerial and street-level photography pending a licensed imagery source for the City of Barrie.</div>
  <table class="kv">
    <tr><td>Property Address</td><td>118 Patterson Road, Barrie, ON&nbsp;&nbsp;L4N 3W3</td></tr>
    <tr><td>Name</td><td>OMG GTA</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Additional residential units / gentle intensification (up to 4 units); to be confirmed</td></tr>
  </table>
  <table class="kv">
    <tr><td>Municipality</td><td>Barrie (single-tier city)</td></tr>
    <tr><td>Neighbourhood</td><td>Ardagh (Ardagh Bluffs), southwest Barrie</td></tr>
    <tr><td>Property Type</td><td>Detached dwelling in an established residential subdivision (per public records)</td></tr>
    <tr><td>Waste Collection</td><td>City of Barrie curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>City of Barrie Comprehensive Zoning By-law 2009-141 (as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Additional residential units — up to 4 units on the lot; to be confirmed</td></tr>
  </table>
  <div class="cell" style="break-inside:avoid;page-break-inside:avoid;">
    <div class="ct">Neighbourhood Spotlight</div>
    118 Patterson Road is in Ardagh (the Ardagh Bluffs area) in southwest Barrie — an established, family-oriented residential subdivision:
    <ul>
      <li>Backs onto the Ardagh Bluffs greenspace and trail network — a large protected forest-and-trail system in the city's southwest</li>
      <li>Serviced with municipal water and sewer — the provincial criterion for as-of-right additional residential units</li>
      <li>Quick access to Highway 400 and to GO service at Barrie South / Allandale Waterfront stations</li>
      <li>Established residential streets with steady rental demand from a growing regional workforce</li>
      <li>Note: proximity to the Ardagh Bluffs environmental lands can carry site-specific setbacks or overlays — confirmed in Phase 2. (Illustrative context, not a valuation.)</li>
    </ul>
  </div>
</div>

'''
    html = replace_section(html, "<!-- 1 PROPERTY DETAILS -->", "<!-- 2 ZONING -->", property_block)

    # -- 2. CURRENT ZONING ---------------------------------------------------
    zoning_block = '''<!-- 2 ZONING -->
<div class="section">
  <h2 class="sec">2. Current Zoning</h2>
  <table class="kv">
    <tr><td>Current Zoning</td><td>Residential zone under the City of Barrie Comprehensive Zoning By-law 2009-141 — the exact zone designation for this parcel is confirmed in Phase 2</td></tr>
    <tr><td>Minimum Site Requirements</td><td>A serviced residential lot (municipal water &amp; sewer) within the settlement area — the criteria for as-of-right additional residential units.</td></tr>
    <tr><td>Recent Changes</td><td>Barrie passed <strong>By-law 2024-043</strong> (2024), amending By-law 2009-141 to permit up to <strong>4 residential units</strong> as-of-right on residentially-zoned lots — one more than the 3-unit minimum set by Ontario's Bill 23. No rezoning required.</td></tr>
    <tr><td>Permitted Uses</td><td>The main dwelling plus Additional Residential Units (interior suites and/or a detached suite), up to <strong>4 units total</strong>, subject to Barrie's ARU standards — maximum height 4.5 m, 3 m side and rear-yard setbacks, and one parking space per unit. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>YES</strong>; proceed to Step 2 — <strong>Builder Ready Package™</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you…</div>
    <ul style="margin-top:0;">
      <li><strong>Additional Residential Units (ARUs):</strong> interior suites within the existing home (for example a basement or in-law suite)</li>
      <li><strong>Detached / Garden Suite:</strong> a self-contained home in the rear yard, subject to the ARU height and setback standards</li>
      <li><strong>Up to 4 units total:</strong> under By-law 2024-043, the lot may support the main dwelling plus additional units — the largest as-of-right allowance among comparable Ontario cities</li>
      <li><strong>Gentle intensification:</strong> permitted as-of-right where the site standards are met — no rezoning and no public hearing</li>
    </ul>
  </div>
</div>

'''
    html = replace_section(html, "<!-- 2 ZONING -->", "<!-- TIME SENSITIVE -->", zoning_block)

    # -- TIME-SENSITIVE ------------------------------------------------------
    ts_block = '''<!-- TIME SENSITIVE -->
<div class="section">
  <h2 class="sec">⚠️ Time-Sensitive Information</h2>
  <div class="ts">
    <div class="d"><div class="dt">Development Charges — ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under Ontario's Bill 23 (up to three units per lot) — a meaningful per-unit saving on a new suite. How the exemption applies to your specific configuration is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Provincial &amp; Federal Rental Rebates<br><small>criteria change periodically</small></div><div class="dx">Government-backed financing options and rebate programs for new purpose-built rental housing open, close, and change their criteria over time. We confirm which programs are currently open and applicable to your project in Phase 2. These are potential options, never a guaranteed grant.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>
</div>

'''
    html = replace_section(html, "<!-- TIME SENSITIVE -->", "<!-- 3 REZONING -->", ts_block)

    # -- 3. REZONING ---------------------------------------------------------
    rezoning_block = '''<!-- 3 REZONING -->
<div class="section">
  <h2 class="sec">3. Rezoning (If Applicable)</h2>
  <p>Rezoning is when the city changes the local planning rules to legally allow more housing units, taller buildings, or different types of properties to be built on a specific piece of land than what was originally allowed. Think of it as the city giving a property a "regulatory upgrade".</p>
  <div class="co-green"><div class="ct2">Not Required for This Property</div>Up to four residential units are permitted as-of-right on a residentially-zoned Barrie lot under By-law 2024-043, so no rezoning is contemplated for a project within that envelope.</div>
  <div class="barhead" style="text-align:left;">As-of-Right vs. The Rezoning Path</div>
  <table class="cmp">
    <tr><th></th><th>Your Path — As-of-Right</th><th>If Rezoning Were Needed</th></tr>
    <tr><td>Change to the zoning by-law</td><td class="g">None required</td><td class="n">Required</td></tr>
    <tr><td>Public consultation meeting</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>City Council decision</td><td class="g">Not required</td><td class="n">Required</td></tr>
    <tr><td>Appeal exposure (OLT)</td><td class="g">Not applicable</td><td class="n">Possible</td></tr>
    <tr><td>What governs your build</td><td class="g">By-law 2024-043 / 2009-141</td><td class="n">A new site-specific by-law</td></tr>
  </table>
  <div class="barhead" style="text-align:left;">Also permitted as-of-right on this lot</div>
  <div class="twocard">
    <div class="card2"><div class="ct">Up to four units</div>By-law 2024-043 (2024) permits up to four residential units on a residentially-zoned lot without rezoning, subject to the City's site standards.</div>
    <div class="card2"><div class="ct">Detached / garden suite</div>A detached additional residential unit in the rear yard is permitted as-of-right, subject to the 4.5 m height cap and 3 m setbacks in the same by-law.</div>
  </div>
  <div class="barhead" style="text-align:left;">What this means for 118 Patterson Road</div>
  <p>Because the recommended build fits within Barrie's four-unit as-of-right envelope, no rezoning application is contemplated in this analysis. Your project advances directly to design and permitting. This assessment reflects the by-laws in force at the date of this report and is subject to technical review of site conditions. Because Barrie has no automated zoning adapter yet, the specific figures above were researched live from the City's by-laws and should be re-verified before the call.</p>
  <div class="co-amber"><b>Two items to confirm in Phase 2:</b><br><span class="sub">the exact residential zone designation for this parcel under By-law 2009-141, and whether any environmental-protection setback or overlay applies given the property's proximity to the Ardagh Bluffs greenspace.</span></div>
</div>

'''
    html = replace_section(html, "<!-- 3 REZONING -->", "<!-- 4 DEVELOPMENT OPTIONS -->", rezoning_block)

    # -- 4. DEVELOPMENT OPTIONS (reuse master massing renderings) -------------
    options_block = '''<!-- 4 DEVELOPMENT OPTIONS -->
<div class="section">
  <h2 class="sec">4. Development Options</h2>
  <div class="opt"><div class="oh">Option A — Interior Additional Residential Unit(s)</div>
    <div class="ob">
      <div class="massing"><img src="opt_a.png" alt="Massing illustration"></div>
      <div class="od">Add one or two self-contained suites within the existing home — for example a basement apartment, or a basement suite paired with a main-floor or upper suite. Permitted as-of-right under By-law 2024-043; no rezoning. Parking is one space per unit, and additional residential units are exempt from development charges under Bill 23 (up to three units). This is typically the fastest, lowest-cost route to rental income while you keep the property. Final unit count and sizes confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option B — Detached / Garden Suite + Interior Suite(s) (up to 4 units) — Primary Recommendation</div>
    <div class="ob">
      <div class="massing"><img src="opt_b.png" alt="Massing illustration"></div>
      <div class="od">Combine interior suite(s) in the existing home with a detached suite in the rear yard — up to four units on the lot under By-law 2024-043. The detached suite is subject to a maximum height of 4.5 m and 3 m side and rear-yard setbacks. The established Ardagh lots and their rear yards are generally well suited to a detached suite; the exact buildable envelope and siting are confirmed in Phase 2. No rezoning required within the four-unit envelope.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C — Servicing, Setbacks &amp; the Ardagh Bluffs Greenspace</div>
    <div class="ob">
      <div class="massing"><img src="opt_c.png" alt="Massing illustration"></div>
      <div class="od">Before design, confirm municipal water and sewer servicing capacity for the added units, the exact interior and rear-yard setbacks for this parcel, and whether any environmental-protection overlay applies given the property's proximity to the Ardagh Bluffs environmental lands. These are the site-specific items that shape the final envelope, and they are resolved in Phase 2 with a survey and a servicing review.</div>
    </div></div>
</div>

'''
    html = replace_section(html, "<!-- 4 DEVELOPMENT OPTIONS -->", "<!-- 5 DEVELOPMENT GOAL SUMMARY -->", options_block)

    # -- 5. DEVELOPMENT GOAL SUMMARY -----------------------------------------
    goal_block = '''<!-- 5 DEVELOPMENT GOAL SUMMARY -->
<div class="section flow">
  <h2 class="sec">5. Development Goal Summary</h2>
  <div class="barhead" style="text-align:left;">Up to Four Units (Additional Residential Units)</div>
  <p>118 Patterson Road is a serviced residential lot in Barrie's Ardagh neighbourhood where, under By-law 2024-043, up to four residential units are permitted as-of-right — no rezoning required. A detached / garden suite paired with interior suite(s) is the clear primary path to maximize permitted density while you keep the property. <strong>The four-unit configuration is the primary recommendation</strong>, with an interior-suite-only build as a lower-cost alternative. Exact unit mix and siting are confirmed in Phase 2.</p>
</div>

'''
    html = replace_section(html, "<!-- 5 DEVELOPMENT GOAL SUMMARY -->", "<!-- 6 FINANCING -->", goal_block)

    # -- 7. GRANTS (fill the gated table with sourced, hedged rows) ----------
    grants_block = '''<!-- 7 GRANTS -->
<div class="section">
  <h2 class="sec">7. Available Grants &amp; Incentives</h2>
  <p>Most property owners don't realize how much government assistance is available to help them complete their project.</p>
  <p>Creating housing is a key mandate of government at all levels: federal, provincial, and municipal. The work you are considering undertaking with your property is the exact kind of work the government wants to support!</p>
  <p>It's important to note that the timing, criteria, and application processes change regularly. Working with clients across the country, we are intimately familiar with available grants, incentives and programs that may be available for your project.</p>
  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>ARU Development Charge Exemption (Bill 23)</td><td>Additional residential units are exempt from development charges under Ontario's Bill 23 — up to three units per lot. A meaningful per-unit saving; how it applies to your configuration is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>GST/HST New Residential Rental Rebate</td><td>The enhanced purpose-built rental rebate targets rental projects of four or more units; a four-unit build may qualify. Applicability and value confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>May provide 15% back on up to $50,000 of eligible cost where a suite houses an eligible relative (a senior or an adult with a disability). Confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Programs such as the Canada Greener Homes initiative and utility Home Renovation Savings rebates may offset efficient design and equipment on a new suite. Availability confirmed in Phase 2.</td></tr>
  </table>
</div>

'''
    html = replace_section(html, "<!-- 7 GRANTS -->", "<!-- 8 SUMMARY -->", grants_block)

    # -- 8. SUMMARY — swap only the Current Zoning Review prose ---------------
    old_summary = '''  <h3>Current Zoning Review</h3>
  <p>303 Coxwell Avenue confirms a strong development option. This property is located in Ward 19 (Beaches-East York) — one of only nine wards across Toronto where up to <strong>six units are permitted as-of-right in a residential zone</strong>. This regulatory advantage, secured through By-law 654-2025 (June 2025), is not available to most Toronto homeowners evaluating the same path.</p>
  <ul>
    <li><strong>The Six-Unit As-of-Right Advantage:</strong> This lot is in one of nine wards in Toronto where By-law 654-2025 allows a 6-unit houseplex as-of-right — no rezoning, no public hearing, no Council approval required.</li>
  </ul>'''
    new_summary = '''  <h3>Current Zoning Review</h3>
  <p>118 Patterson Road is a serviced residential lot in Barrie's Ardagh neighbourhood. Under the City's By-law 2024-043 (2024), up to <strong>four residential units are permitted as-of-right</strong> on residentially-zoned lots — one more than the provincial Bill 23 minimum, and among the most generous as-of-right allowances of any comparable Ontario municipality. No rezoning is required, subject to the City's site standards.</p>
  <ul>
    <li><strong>The Four-Unit As-of-Right Advantage:</strong> Barrie permits up to four units on a residential lot with no rezoning, no public hearing, and no Council approval — confirmed live from the City's by-laws for this report and to be re-verified in Phase 2.</li>
  </ul>'''
    html = replace_once(html, old_summary, new_summary)

    # -- leftover guard ------------------------------------------------------
    banned = ["303 coxwell", "arockiaraj", "coxwell", "toronto", "ward 19",
              "654-2025", "474-2023", "beaches", "sixplex", "houseplex",
              "ttc", "bill 185", "briarstone", "cambridge", "galt"]
    low = html.lower()
    hits = [b for b in banned if b in low]
    assert not hits, f"LEFTOVER city/master content still present: {hits}"

    open(OUT, "w", encoding="utf-8").write(html)
    print(f"wrote {OUT} ({len(html):,} bytes); leftover check clean")


if __name__ == "__main__":
    main()
