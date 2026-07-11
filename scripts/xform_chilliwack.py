#!/usr/bin/env python3
"""
xform_chilliwack.py — turn the Saanich BC/SSMUH report into the Chilliwack report
for 9039 Garden Drive (contact: Lionel Hayer).

Same pattern as xform_saanich.py: every replacement must match exactly once, then
we grep for leftovers from the source city (Saanich/Victoria) AND the master city
(Toronto/Coxwell). Zero leftovers is the accuracy gate before render.

Chilliwack facts (verified from live official / government sources, July 2026):
  - Base zoning: City of Chilliwack "Zoning Bylaw 2020, No. 5000".
  - SSMUH (BC Bill 44) adopted locally as "Zoning Bylaw Amendment Bylaw 2024,
    No. 5395" (three readings June 4, 2024): 3 units on serviced single-detached/
    duplex lots inside the Urban Growth Boundary, up to 4 units on lots > 280 m².
  - Six-unit (frequent-transit) tier is concentrated around the Downtown Spadina
    exchange / Density Benefit Areas; 9039 Garden Drive is outside it -> unlikely.
  - Chilliwack retained off-street parking requirements for these units.
  - BC Secondary Suite Incentive Program is CLOSED to new applications (after
    Mar 30, 2025) -> dropped, replaced with the federal Multigenerational Home
    Renovation Tax Credit.
Lot-specific facts (exact zone, lot area, servicing, transit) are hedged to
Phase 2 per docs/AI_Report_Writer_Role_v1.md.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = os.path.join(HERE, "..", "templates")
PATH = os.path.join(TEMPLATES, "report_chilliwack.html")

s = open(PATH, encoding="utf-8").read()
R = []

# --- Cover -------------------------------------------------------------------
R.append(('<div class="addr">1361 Hastings Street<span>Saanich, BC (Greater Victoria)</span></div>',
          '<div class="addr">9039 Garden Drive<span>Chilliwack, BC (Fraser Valley)</span></div>'))

# --- 1. Property Details header ---------------------------------------------
R.append(('<div class="barhead">1361 Hastings Street, Saanich, BC&nbsp;&nbsp;V8Z 2W5</div>',
          '<div class="barhead">9039 Garden Drive, Chilliwack, BC&nbsp;&nbsp;V2P 5M7</div>'))

# --- 1. Contact / property table --------------------------------------------
R.append(('''    <tr><td>Property Address</td><td>1361 Hastings Street, Saanich, BC&nbsp;&nbsp;V8Z 2W5</td></tr>
    <tr><td>Name</td><td>Shane Restall</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Multiplex — maximize unit count under BC's SSMUH rules</td></tr>''',
'''    <tr><td>Property Address</td><td>9039 Garden Drive, Chilliwack, BC&nbsp;&nbsp;V2P 5M7</td></tr>
    <tr><td>Name</td><td>Lionel Hayer</td></tr>
    <tr><td>Phone Number</td><td>Provided at intake</td></tr>
    <tr><td>Email</td><td>Provided at intake</td></tr>
    <tr><td>Development Goals</td><td>Add units to the existing home; multiplex development under BC's SSMUH rules</td></tr>'''))

# --- 1. Municipality block ---------------------------------------------------
R.append(('''    <tr><td>Municipality</td><td>District of Saanich (Capital Regional District)</td></tr>
    <tr><td>Region</td><td>Greater Victoria, BC</td></tr>
    <tr><td>Current Zoning</td><td>RS-6 — Single Family (District of Saanich)</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH)</td></tr>
    <tr><td>Servicing</td><td>Must be within the Urban Containment / Sewer Service Area — confirm in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — unit count depends on lot area &amp; transit proximity</td></tr>
    <tr><td>Development Goals</td><td>Multiplex (3–6 units) under SSMUH, subject to lot size &amp; transit</td></tr>''',
'''    <tr><td>Municipality</td><td>City of Chilliwack (Fraser Valley Regional District)</td></tr>
    <tr><td>Region</td><td>Fraser Valley, BC</td></tr>
    <tr><td>Current Zoning</td><td>Urban single-detached residential (Zoning Bylaw 2020, No. 5000) — exact zone confirmed in Phase 2</td></tr>
    <tr><td>Governing Framework</td><td>BC Bill 44 — Small-Scale Multi-Unit Housing (SSMUH), adopted locally as Zoning Bylaw Amendment Bylaw 2024, No. 5395</td></tr>
    <tr><td>Servicing</td><td>Must be a serviced lot within Chilliwack's Urban Growth Boundary — confirm in Phase 2</td></tr>
    <tr><td>Legal Description</td><td>To be confirmed (via BC LTSA)</td></tr>
    <tr><td>Year Built</td><td>To be confirmed</td></tr>
    <tr><td>Lot size</td><td>To be confirmed — the 4-unit tier requires a lot larger than 280 m²</td></tr>
    <tr><td>Development Goals</td><td>Add units to the existing home / multiplex (3–4 units) under SSMUH, subject to lot size &amp; servicing</td></tr>'''))

# --- 1. Neighbourhood Spotlight ---------------------------------------------
R.append(('''    1361 Hastings Street is in the District of Saanich, part of the Greater Victoria region on southern Vancouver Island — an established, high-demand residential area:
    <ul>
      <li>Central Saanich location with quick access to Uptown, Downtown Victoria, and the University of Victoria</li>
      <li>Well served by BC Transit; proximity to a frequent-transit route is the key factor in whether up to six units are permitted — confirmed in Phase 2</li>
      <li>Strong, chronically tight rental market across Greater Victoria — supportive of a hold-and-rent strategy</li>
      <li>Established single-family streets now opened to gentle density by provincial SSMUH rules</li>
      <li>Note: slopes, trees, and setback/character guidelines can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>''',
'''    9039 Garden Drive is in the City of Chilliwack, in BC's Fraser Valley about 100 km east of Vancouver — an established, fast-growing residential community:
    <ul>
      <li>Central Chilliwack location with access to Downtown Chilliwack, Highway 1, and nearby shopping and schools</li>
      <li>Served by BC Transit; Chilliwack's six-unit tier is concentrated near the Downtown Spadina transit exchange, so most lots fall in the 3–4 unit range — confirmed in Phase 2</li>
      <li>One of the fastest-growing cities in BC, with steady rental demand — supportive of a hold-and-rent strategy</li>
      <li>Established single-family streets now opened to gentle density by provincial SSMUH rules</li>
      <li>Note: floodplain, servicing, setback and design guidelines can shape what's buildable. (Illustrative context, not a valuation.)</li>
    </ul>'''))

# --- 2. Current Zoning table -------------------------------------------------
R.append(('''    <tr><td>Current Zoning</td><td>RS-6 — Single Family (District of Saanich), now subject to provincial SSMUH permissions</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced residential lots inside the Urban Containment Boundary. Unit count scales with lot size and transit proximity (a 6-unit allowance requires a lot &gt;280 m² within ~400 m of frequent transit).</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023) — implemented by Saanich in 2024 and tightened by Bill 25 (Nov 2025, compliance by June 30, 2026) — <strong>3 to 6 units</strong> are permitted as-of-right on lots formerly limited to a single house or duplex. No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex, fourplex, and (near frequent transit) up to a six-unit multiplex — plus secondary and garden suites. Saanich exempts projects of 4 units or fewer from a Form &amp; Character development permit. Confirmed in Phase 2.</td></tr>''',
'''    <tr><td>Current Zoning</td><td>Urban single-detached / duplex residential (Zoning Bylaw 2020, No. 5000), now subject to provincial SSMUH permissions</td></tr>
    <tr><td>Minimum Site Requirements</td><td>SSMUH applies to serviced single-detached / duplex lots inside Chilliwack's Urban Growth Boundary. Unit count scales with lot size: up to 4 units on lots larger than 280 m², and 3 units on smaller lots.</td></tr>
    <tr><td>Recent Changes</td><td>Under BC Bill 44 (SSMUH, 2023), adopted by Chilliwack as Zoning Bylaw Amendment Bylaw 2024, No. 5395 (June 2024) — <strong>3 to 4 units</strong> are permitted as-of-right on lots formerly limited to a single house plus a suite. A higher <strong>six-unit</strong> tier applies only near frequent transit (concentrated around the Downtown Spadina exchange). No rezoning, no public hearing.</td></tr>
    <tr><td>Permitted Uses</td><td>Triplex and fourplex on qualifying lots, plus secondary suites and coach / garden suites. Note: Chilliwack has kept off-street parking requirements for these units (reported at up to two spaces per unit) — confirmed in Phase 2.</td></tr>'''))

# --- 2. What this means for you ---------------------------------------------
R.append(('''      <li><strong>Triplex / Fourplex:</strong> 3–4 units as-of-right on the lot under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Multiplex:</strong> up to 6 units where the lot is &gt;280 m² and within ~400 m of frequent transit</li>
      <li><strong>Suites Route:</strong> a secondary suite plus a detached garden suite — Saanich allows both on the same lot inside the boundary</li>''',
'''      <li><strong>Triplex / Fourplex:</strong> 3 units on smaller lots, up to 4 units on lots larger than 280 m² — as-of-right under SSMUH, no rezoning</li>
      <li><strong>Six-Unit Tier:</strong> up to 6 units only where the lot is near frequent transit (mainly the Downtown Spadina exchange area) — confirmed in Phase 2</li>
      <li><strong>Suites Route:</strong> a secondary suite and/or a coach or garden suite added to the existing home — often the fastest path to rental income</li>'''))

# --- Time-Sensitive ----------------------------------------------------------
R.append(('''    <div class="d"><div class="dt">BC Bill 25 — SSMUH Compliance<br><small>June 30, 2026</small></div><div class="dx">Bill 25 (Nov 2025) tightened the SSMUH rules and set a June 30, 2026 deadline for municipalities, including Saanich, to finalize compliant bylaws. The applicable unit count and site standards for your lot are confirmed against Saanich's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">No minimum parking is required for SSMUH projects within ~400 m of frequent transit. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>''',
'''    <div class="d"><div class="dt">SSMUH In Effect<br><small>since June 2024</small></div><div class="dx">Chilliwack's SSMUH rules are already in force under Zoning Bylaw Amendment Bylaw 2024, No. 5395. The exact unit count, parking, and site standards for your lot are confirmed against the City's current bylaw in Phase 2.</div></div>
    <div class="d"><div class="dt">Parking &amp; CMHC</div><div class="dx">Unlike some BC municipalities, Chilliwack has kept off-street parking requirements for SSMUH units — a real design consideration for your lot. CMHC policy can change at any time and affects financing — applying early reduces risk.</div></div>'''))

# --- 4. Option A (make it the primary recommendation) ------------------------
R.append(('<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right)</div>',
          '<div class="opt"><div class="oh">Option A — Triplex / Fourplex (3–4 units, as-of-right) — Primary Recommendation</div>'))
R.append(('''      <div class="od">A triplex or fourplex built directly on the lot — the baseline SSMUH entitlement on a serviced Saanich residential lot, with no rezoning or public hearing. At four units or fewer, Saanich exempts the project from a Form &amp; Character development permit, which meaningfully shortens the approval path. Buildable size is governed by setbacks, height, lot coverage, and floor-area rules — confirmed in Phase 2.</div>''',
'''      <div class="od">A triplex or fourplex built directly on the lot — the baseline SSMUH entitlement on a serviced Chilliwack residential lot inside the Urban Growth Boundary, with no rezoning or public hearing. Up to 4 units are permitted where the lot is larger than 280 m² (3 units on smaller lots). Buildable size is governed by setbacks, height, lot coverage, floor-area and off-street parking rules — confirmed in Phase 2. <strong>This is the primary recommendation for this lot.</strong></div>'''))

# --- 4. Option B (reframe six-unit as conditional, not primary) --------------
R.append(('<div class="opt"><div class="oh">Option B — Six-Unit Multiplex (near frequent transit) — Primary Recommendation</div>',
          '<div class="opt"><div class="oh">Option B — Six-Unit Tier (only near frequent transit)</div>'))
R.append(('''      <div class="od">Where the lot is greater than 280 m² and within roughly 400 m of a frequent-transit stop, SSMUH permits up to six units as-of-right — the highest-density, strongest-income direction without rezoning. Confirming the lot's transit proximity and area is the first gating step, since it is what unlocks the 6-unit tier. No minimum parking applies within the transit radius. Confirmed in Phase 2.</div>''',
'''      <div class="od">Chilliwack's six-unit tier is limited to lots near frequent transit — in practice concentrated around the Downtown Spadina exchange and the City's designated Density Benefit Areas. 9039 Garden Drive is well outside that area, so six units is unlikely to apply here; the fourplex path above is the reliable route. Transit proximity is confirmed against the City's current bylaw in Phase 2.</div>'''))

# --- 4. Option C (matches homeowner's "add units to existing" goal) ----------
R.append(('''      <div class="od">A lower-complexity path: keep the principal dwelling and add a secondary suite plus a detached garden suite — Saanich allows both on the same lot inside the boundary, and has removed the owner-occupancy requirement. This is often the fastest route to rental income while a larger multiplex is evaluated. Suite sizes and siting confirmed in Phase 2.</div>''',
'''      <div class="od">This matches your stated goal of adding units to the existing building: keep the principal dwelling and add a secondary suite and/or a detached coach or garden suite. It is the lower-complexity, faster path to rental income, and can be a first step while a larger fourplex is evaluated. Suite sizes, parking and siting are confirmed against Chilliwack's secondary suite / coach house rules in Phase 2.</div>'''))

# --- 5. Development Goal Summary ---------------------------------------------
R.append(('<div class="barhead" style="text-align:left;">Multiplex under SSMUH (up to 6 units)</div>',
          '<div class="barhead" style="text-align:left;">Multiplex under SSMUH (3–4 units)</div>'))
R.append(('''  <p>1361 Hastings Street is an RS-6 single-family lot in Saanich now opened to gentle density by BC's SSMUH rules — 3 to 6 units as-of-right depending on lot size and transit proximity. <strong>Where the lot qualifies for the six-unit tier, a six-unit multiplex is the clear primary recommendation</strong>; a triplex/fourplex is the reliable fallback, and the suites route is the fastest entry.</p>''',
'''  <p>9039 Garden Drive is a single-detached residential lot in Chilliwack now opened to gentle density by BC's SSMUH rules — 3 to 4 units as-of-right depending on lot size, with no rezoning or public hearing. <strong>A triplex or fourplex is the clear primary recommendation</strong>; adding suites to the existing home is the fastest entry point, and the six-unit tier applies only if the lot is confirmed to be near frequent transit.</p>'''))

# --- 7. Grants table: drop the closed BC Secondary Suite Incentive Program ---
R.append(('''    <tr><td>Provincial (BC)</td><td>BC Secondary Suite Incentive Program</td><td>Forgivable loan reported up to $40,000 toward a new secondary suite rented below market for a set term. Eligibility and current status confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by municipality. Confirmed against Saanich's current bylaw in Phase 2.</td></tr>''',
'''    <tr><td>Federal</td><td>Multigenerational Home Renovation Tax Credit</td><td>A refundable federal credit of up to $7,500 (15% of up to $50,000 in eligible costs) toward creating a self-contained secondary unit for a senior or an adult eligible for the disability tax credit. Eligibility confirmed in Phase 2.</td></tr>
    <tr><td>Municipal</td><td>Development Cost Charge (DCC) treatment</td><td>SSMUH and rental projects may qualify for reduced or waived DCCs; treatment varies by project. Confirmed against Chilliwack's current bylaw in Phase 2.</td></tr>'''))

# --- 8. Summary --------------------------------------------------------------
R.append(('''  <p>1361 Hastings Street is an RS-6 single-family lot in the District of Saanich. Under BC's SSMUH framework (Bill 44, tightened by Bill 25), it is now eligible for <strong>3 to 6 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and transit proximity.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming lot size and distance to frequent transit, since that is what unlocks the six-unit tier — established in Phase 2.</li>
  </ul>''',
'''  <p>9039 Garden Drive is a single-detached residential lot in the City of Chilliwack. Under BC's SSMUH framework (Bill 44), adopted locally as Zoning Bylaw Amendment Bylaw 2024, No. 5395, it is now eligible for <strong>3 to 4 units as-of-right</strong> — no rezoning, no public hearing — with the exact ceiling set by lot area and servicing.</p>
  <ul>
    <li><strong>The SSMUH Advantage:</strong> the single most valuable step is confirming lot size (the 4-unit tier needs a lot larger than 280 m²) and the City's parking and setback standards for your lot — established in Phase 2.</li>
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

if fails:
    print(f"\nABORTED — {fails} replacement(s) did not match exactly once. File NOT written.")
    raise SystemExit(1)

open(PATH, "w", encoding="utf-8").write(s)

# Leftover gate: source city (Saanich/Victoria) + master city (Toronto/Coxwell)
leftovers = ["Coxwell", "Toronto", "John Arockiaraj", "Ward 19", "654-2025",
             "Bill 185", "Ontario HST", "Saanich", "Hastings", "Victoria",
             "RS-6", "Bill 25", "Capital Regional", "Vancouver Island",
             "Urban Containment", "Form &amp; Character", "Uptown",
             "University of Victoria", "owner-occupancy",
             "Secondary Suite Incentive"]
found = False
for t in leftovers:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")
        found = True
print("clean" if not found else "LEFTOVERS PRESENT")
print("done, fails:", fails)
