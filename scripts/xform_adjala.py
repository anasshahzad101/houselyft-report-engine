"""
xform_adjala.py — build the House Lyft report for
Manjit Singh, 3364 County Road 50, Loretto, Township of Adjala-Tosorontio (Simcoe County).

Adjala-Tosorontio is OUTSIDE the verified-city engine, so zoning was researched
live from official sources (Township Zoning By-law 03-57 + Ontario's provincial
ARU framework). Confidence = researched live -> report-needs-review.

Mirrors the scripts/xform_*.py pattern: start from the master, swap only the
per-property sections, keep every House Lyft prose section (Why / How to use /
Advantage / Financing intro / Next Steps / CTA) verbatim, then assert there are
zero leftovers from the master's source property/city.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_adjala.html")

html = open(SRC, encoding="utf-8").read()

# ---- cover address (ASCII-only source line) --------------------------------
old_addr = '<div class="addr">303 Coxwell Avenue<span>Toronto, ON</span></div>'
new_addr = '<div class="addr">3364 County Road 50<span>Loretto, Adjala&ndash;Tosorontio, ON</span></div>'
assert html.count(old_addr) == 1, "cover addr anchor not unique"
html = html.replace(old_addr, new_addr)


def replace_between(text, start, end, block):
    i = text.index(start)
    j = text.index(end, i)
    assert i < j, f"marker order wrong: {start} .. {end}"
    return text[:i] + start + "\n" + block.strip("\n") + "\n\n" + text[j:]


PROPERTY = """\
<div class="section">
  <h2 class="sec">1. Property Details</h2>
  <div class="barhead">3364 County Road 50, Loretto (Adjala&ndash;Tosorontio), ON&nbsp;&nbsp;L0G 1L0</div>
  <div style="font-size:8.5pt;color:#7a818f;margin:6px 0 12px;">Aerial and street-level photography pending a licensed imagery source for this municipality.</div>
  <table class="kv">
    <tr><td>Property Address</td><td>3364 County Road 50, Loretto (Adjala&ndash;Tosorontio), ON&nbsp;&nbsp;L0G 1L0</td></tr>
    <tr><td>Name</td><td>Manjit Singh</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Add a secondary suite (additional residential unit) for rental income</td></tr>
  </table>
  <table class="kv">
    <tr><td>Municipality</td><td>Township of Adjala&ndash;Tosorontio</td></tr>
    <tr><td>Community</td><td>Loretto (rural hamlet)</td></tr>
    <tr><td>County</td><td>County of Simcoe</td></tr>
    <tr><td>Conservation Authority</td><td>Nottawasaga Valley Conservation Authority (NVCA)</td></tr>
    <tr><td>Servicing</td><td>Private well &amp; septic assumed (rural lot) &mdash; to be confirmed</td></tr>
    <tr><td>Waste Collection</td><td>County of Simcoe / Township curbside schedule</td></tr>
    <tr><td>Current Bylaw</td><td>Township of Adjala&ndash;Tosorontio Comprehensive Zoning By-law No. 03-57 (2003, as amended)</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed</td></tr>
    <tr><td>Development Goals</td><td>Secondary suite / additional residential unit (primary)</td></tr>
  </table>
  <div class="cell" style="break-inside:avoid;page-break-inside:avoid;">
    <div class="ct">Neighbourhood Spotlight</div>
    3364 County Road 50 is in Loretto, a small rural hamlet in the Township of Adjala&ndash;Tosorontio in the County of Simcoe &mdash; the rolling countryside of the region's south, well north of the GTA:
    <ul>
      <li>Quiet rural setting with the generous lot sizes typical of Adjala&ndash;Tosorontio's countryside</li>
      <li>Within the County of Simcoe, a short drive to Alliston and the Highway 9 / Highway 50 corridor</li>
      <li>Located in the Nottawasaga Valley watershed &mdash; parts of the township fall within conservation-authority regulated areas</li>
      <li>Rural properties here are typically on private well and septic services rather than municipal water and sewer</li>
      <li>Illustrative context only, not a valuation; site-specific details are confirmed in Phase 2.</li>
    </ul>
  </div>
</div>"""

ZONING = """\
<div class="section">
  <h2 class="sec">2. Current Zoning</h2>
  <div class="co-amber" style="margin:0 0 14px;"><b>Researched live for this municipality.</b><br><span class="sub">Adjala&ndash;Tosorontio is outside our verified-city engine, so the rules below were researched from the Township's published by-law and Ontario's provincial framework. Treat the exact zone, unit count, and any incentive figures as items to confirm before the call.</span></div>
  <table class="kv">
    <tr><td>Current Zoning</td><td>Rural / Agricultural&ndash;residential zone under Township of Adjala&ndash;Tosorontio Zoning By-law No. 03-57 (2003, as amended). The Loretto area is covered by the by-law's rural schedules; the exact zone for this parcel (e.g. Agricultural, Rural, or Rural Residential) is confirmed in Phase 2.</td></tr>
    <tr><td>Servicing Basis</td><td>Rural lots in the township are generally on private well and septic. On private services, the size and number of dwelling units is governed by the local zoning by-law and by the septic system's rated capacity &mdash; not by the urban as-of-right rules.</td></tr>
    <tr><td>Provincial Framework</td><td>Ontario's <em>More Homes Built Faster Act, 2022</em> (Bill 23) requires up to <strong>3 residential units as-of-right</strong> only on a &ldquo;parcel of urban residential land&rdquo; &mdash; a lot in a settlement area on full municipal water and sewer. A rural lot on private well and septic falls outside that mandatory framework; a secondary suite / additional residential unit is instead permitted through the Township's zoning by-law, subject to servicing.</td></tr>
    <tr><td>Permitted Uses</td><td>A secondary suite (an additional residential unit &mdash; interior or a detached unit) is the modest, most likely path on a rural lot, subject to the by-law's standards (setbacks, height, floor area) and to confirmed septic capacity. Confirmed in Phase 2.</td></tr>
    <tr><td>Development Goals Achievable?</td><td><strong>Likely &mdash; subject to Phase 2 confirmation</strong> of the exact zone and septic capacity. Proceed to Step 2 &mdash; <strong>Builder Ready Package&trade;</strong></td></tr>
  </table>
  <div class="cell">
    <div class="ct">What this means for you&hellip;</div>
    <ul style="margin-top:0;">
      <li><strong>Interior Secondary Suite:</strong> a self-contained unit within the existing home (e.g. a basement or in-law suite) &mdash; typically the simplest additional unit to add</li>
      <li><strong>Detached Additional Residential Unit:</strong> a separate suite on the lot (garden / coach-house style), where the by-law and your septic capacity allow it</li>
      <li><strong>Servicing is the key variable:</strong> on a rural well-and-septic lot, confirming septic capacity early is what determines how many units are feasible</li>
    </ul>
  </div>
</div>"""

TIMESENS = """\
<div class="section">
  <h2 class="sec">&#9888;&#65039; Time-Sensitive Information</h2>
  <div class="ts">
    <div class="d"><div class="dt">Development Charges &mdash; ARU Exemption</div><div class="dx">Additional residential units are exempt from development charges under Ontario's provincial legislation (Bill 23). For a secondary suite this can be a meaningful per-unit saving. Its application to your project &mdash; under the County of Simcoe and Township development-charge by-laws &mdash; is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Septic Capacity &mdash; Confirm Early<br><small>governs feasibility</small></div><div class="dx">On a rural well-and-septic lot, the septic system's rated capacity often decides whether a second unit is feasible and how large it can be. A septic evaluation early in the process avoids late surprises and, where needed, lets you budget for an upgrade. Confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">Conservation Authority (NVCA)</div><div class="dx">The township lies in the Nottawasaga Valley watershed. If any part of the lot is within an NVCA regulated area (near a watercourse, wetland, or valleyland), a permit under Ontario Regulation 41/24 may be required before building. Whether your lot is regulated is confirmed in Phase 2.</div></div>
    <div class="d"><div class="dt">CMHC</div><div class="dx">Canada Mortgage Housing Corporation (CMHC) policy changes can occur at any time, potentially affecting financing options. It is recommended to submit your application as early as possible to reduce any risk.</div></div>
  </div>
</div>"""

REZONING = """\
<div class="section">
  <h2 class="sec">3. Rezoning (If Applicable)</h2>
  <p>Rezoning is when the city changes the local planning rules to legally allow more housing units, taller buildings, or different types of properties to be built on a specific piece of land than what was originally allowed. Think of it as the city giving a property a &ldquo;regulatory upgrade&rdquo;.</p>
  <div class="co-amber"><b>Whether rezoning is needed here depends on the exact zone.</b><br><span class="sub">If Zoning By-law 03-57 already permits a secondary suite / additional residential unit in your zone, the project proceeds as-of-right &mdash; no rezoning. If it does not, a minor variance or a zoning amendment may be required. Either way, the added unit remains subject to the by-law's site standards and to confirmed septic capacity. This is confirmed in Phase 2.</span></div>
</div>"""

OPTIONS = """\
<div class="section">
  <h2 class="sec">4. Development Options</h2>
  <div class="opt"><div class="oh">Option A &mdash; Interior Secondary Suite (your goal)</div>
    <div class="ob">
      <div class="massing"><svg viewBox="0 0 140 100" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
        <ellipse cx="70" cy="94" rx="60" ry="9" fill="#e9ecf2"/>
        <polygon points="18,20 70,4 122,20" fill="#26365c"/>
        <rect x="22" y="20" width="96" height="70" fill="#eef0f4" stroke="#26365c" stroke-width="1.5"/>
        <line x1="22" y1="58" x2="118" y2="58" stroke="#26365c" stroke-width="1.5"/>
        <g fill="#fff" stroke="#26365c" stroke-width="1"><rect x="32" y="30" width="18" height="13"/><rect x="90" y="30" width="18" height="13"/></g>
        <rect x="62" y="70" width="16" height="20" fill="#26365c"/>
        <rect x="34" y="66" width="16" height="12" fill="#3f7d33"/></svg></div>
      <div class="od">A self-contained secondary suite inside the existing home &mdash; for example a basement or in-law suite with its own entrance, kitchen and bathroom. This is typically the simplest and lowest-cost way to add a rental unit while you keep the property. Permitting is through the Township's zoning by-law; on a rural lot the main variables are the by-law's standards and your septic system's capacity to serve an added unit. Size, layout and servicing are confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option B &mdash; Detached Additional Residential Unit</div>
    <div class="ob">
      <div class="massing"><svg viewBox="0 0 140 100" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
        <ellipse cx="70" cy="92" rx="58" ry="9" fill="#e9ecf2"/>
        <polygon points="26,44 70,28 114,44" fill="#26365c"/>
        <rect x="34" y="44" width="72" height="46" fill="#eef0f4" stroke="#26365c" stroke-width="1.5"/>
        <g fill="#fff" stroke="#26365c" stroke-width="1"><rect x="44" y="52" width="16" height="12"/><rect x="80" y="52" width="16" height="12"/></g>
        <rect x="62" y="72" width="16" height="18" fill="#26365c"/></svg></div>
      <div class="od">A separate suite elsewhere on the lot &mdash; a garden- or coach-house-style unit. Rural lots often have the space for this, but a detached unit places more demand on septic and can bring setback, well-separation and (if near a watercourse or wetland) conservation-authority considerations into play. Feasibility depends on the exact zone, lot servicing and NVCA regulation status &mdash; all confirmed in Phase 2.</div>
    </div></div>
  <div class="opt"><div class="oh">Option C &mdash; Servicing &amp; Siting Considerations</div>
    <div class="ob">
      <div class="massing"><svg viewBox="0 0 140 100" xmlns="http://www.w3.org/2000/svg" style="width:100%;height:auto;">
        <ellipse cx="70" cy="90" rx="52" ry="8" fill="#e9ecf2"/>
        <circle cx="45" cy="52" r="16" fill="#dbe1eb" stroke="#26365c" stroke-width="1.5"/>
        <rect x="78" y="40" width="34" height="26" fill="#ccd4e1" stroke="#26365c" stroke-width="1.5"/>
        <line x1="45" y1="52" x2="78" y2="53" stroke="#26365c" stroke-width="1.2" stroke-dasharray="3,3"/></svg></div>
      <div class="od">On a rural property, the biggest determinants of what you can add are the septic system's capacity and the placement of the well, septic bed and any regulated natural features. A modest interior suite usually places the least new load on these systems, which is why it is the most reliable first step. Where a larger or detached unit is the goal, an early septic assessment tells you whether the existing system can carry it or whether an upgrade should be budgeted. All of this is scoped in Phase 2.</div>
    </div></div>
</div>"""

GOAL = """\
<div class="section flow">
  <h2 class="sec">5. Development Goal Summary</h2>
  <div class="barhead" style="text-align:left;">Secondary Suite (Additional Residential Unit)</div>
  <p>3364 County Road 50 is a rural property in Loretto, Adjala&ndash;Tosorontio, where a secondary suite &mdash; an additional residential unit &mdash; is the natural fit for your goal of adding rental income while keeping the property. <strong>An interior secondary suite is the clear primary recommendation</strong>, with a detached additional unit as an optional path where the exact zone and septic capacity allow. Because this municipality is outside our verified-city engine, the exact zone, permitted unit count and any incentive figures are confirmed in Phase 2 before you commit.</p>
</div>"""

GRANTS = """\
<div class="section">
  <h2 class="sec">7. Available Grants &amp; Incentives</h2>
  <p>Most property owners don't realize how much government assistance is available to help them complete their project.</p>
  <p>Creating housing is a key mandate of government at all levels: federal, provincial, and municipal. The work you are considering undertaking with your property is the exact kind of work the government wants to support!</p>
  <p>It's important to note that the timing, criteria, and application processes change regularly. Working with clients across the country, we are intimately familiar with available grants, incentives and programs that may be available for your project.</p>
  <table class="g">
    <tr><th style="width:70px">Level</th><th style="width:190px">Program</th><th>Notes</th></tr>
    <tr><td>Provincial</td><td>Additional Residential Unit &mdash; Development Charge Exemption</td><td>Additional residential units are exempt from development charges under Ontario's <em>More Homes Built Faster Act, 2022</em> (Bill 23) &mdash; a meaningful per-unit saving on a secondary suite. Application to your project under the County of Simcoe and Township by-laws is confirmed in Phase 2.</td></tr>
    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit (CRA)</td><td>A refundable credit of 15% on up to $50,000 of eligible renovation cost (to a maximum of $7,500) where the secondary suite houses an eligible relative &mdash; a senior, or an adult eligible for the disability tax credit. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Fed / Utility</td><td>Energy-Efficiency Rebates</td><td>Federal and utility efficiency programs may offset the cost of efficient design and equipment in a new suite. Current availability and amounts are confirmed in Phase 2.</td></tr>
  </table>
  <p style="font-size:8.4pt;color:#7a818f;margin-top:10px;">These are government-backed financing options and incentives that <em>may</em> apply &mdash; not guaranteed grants. Because this municipality was researched live, each program's current terms and any dollar figures are verified in Phase 2 before you rely on them.</p>
</div>"""

SUMMARY = """\
<div class="section">
  <h2 class="sec">8. Summary</h2>
  <h3>Current Zoning Review</h3>
  <p>3364 County Road 50 is a rural property in Loretto, in the Township of Adjala&ndash;Tosorontio (County of Simcoe). It is governed by the Township's Comprehensive Zoning By-law No. 03-57. On a rural well-and-septic lot, a <strong>secondary suite / additional residential unit</strong> &mdash; matching your goal &mdash; is permitted through the local by-law rather than the urban three-unit as-of-right rule, and is subject to the by-law's site standards and to confirmed septic capacity.</p>
  <ul>
    <li><strong>The Secondary-Suite Advantage:</strong> an added unit creates a rental income stream using property you already own &mdash; an interior suite is the most reliable first step, with the exact size and servicing confirmed in Phase 2.</li>
    <li><strong>Researched live:</strong> this municipality is outside our verified-city engine, so the exact zone, permitted unit count and any incentive figures should be double-checked in Phase 2 before you commit.</li>
  </ul>
  <h3>Grants &amp; Incentives Review</h3>
  <p>Governments at the federal, provincial, and municipal levels continue to prioritize housing development by offering grants, rebates, and other incentives to help reduce project costs. Because these programs and their eligibility criteria change frequently, we help identify and navigate the opportunities that may apply to your project, maximizing available funding and improving overall project feasibility.</p>
  <h3>Financing Options Review</h3>
  <p>Choosing the right financing strategy is essential to maximizing project returns, maintaining healthy cash flow, and reducing financial risk. We work with trusted lending partners to identify financing solutions that align with your development goals, including mortgage refinancing, home equity lines of credit (HELOCs), and construction financing. By securing the right financing early in the process, we help position your project for long-term success.</p>
</div>"""

html = replace_between(html, "<!-- 1 PROPERTY DETAILS -->", "<!-- 2 ZONING -->", PROPERTY)
html = replace_between(html, "<!-- 2 ZONING -->", "<!-- TIME SENSITIVE -->", ZONING)
html = replace_between(html, "<!-- TIME SENSITIVE -->", "<!-- 3 REZONING -->", TIMESENS)
html = replace_between(html, "<!-- 3 REZONING -->", "<!-- 4 DEVELOPMENT OPTIONS -->", REZONING)
html = replace_between(html, "<!-- 4 DEVELOPMENT OPTIONS -->", "<!-- 5 DEVELOPMENT GOAL SUMMARY -->", OPTIONS)
html = replace_between(html, "<!-- 5 DEVELOPMENT GOAL SUMMARY -->", "<!-- 6 FINANCING -->", GOAL)
html = replace_between(html, "<!-- 7 GRANTS -->", "<!-- 8 SUMMARY -->", GRANTS)
html = replace_between(html, "<!-- 8 SUMMARY -->", "<!-- NEXT STEPS / ROADBLOCKS / CTA -->", SUMMARY)

# ---- leftover guard: nothing from the master's source property/city ---------
BANNED = ["Coxwell", "Arockiaraj", "johneeraj", "Toronto", "654-2025", "474-2023",
          "569-2013", "Bill 185", "Ward 19", "Beaches", "Woodbine", "Greenwood",
          "303 ", "Cambridge", "Waterloo", "Secondary Suite Loan", "free grant",
          "guaranteed return"]
hits = [b for b in BANNED if b in html]
if hits:
    sys.exit(f"LEFTOVER CHECK FAILED — found: {hits}")

open(OUT, "w", encoding="utf-8").write(html)
print("wrote", OUT, "bytes", len(html))
print("leftover check: clean")
