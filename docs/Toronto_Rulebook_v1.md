# Toronto Rulebook — Report Engine Reference (v1)

**Purpose:** The verified planning-rules asset the report engine reads *before* the AI writes anything. The AI applies these rules; it does not re-derive them. This is the "worked cell" — Toronto × all three pillars. Replicate this template per municipality.

**Last verified:** June 2026 · **Re-verify before any client-facing use.** Zoning and grant rules here change every few months.

---

## How to read the confidence flags

Every field carries one tag. This is the heart of the accuracy moat — we never let an unverified number reach a homeowner.

- ✅ **VERIFIED** — consistent across authoritative sources, bylaw cited. Safe to narrate.
- ⚠️ **CONFLICTING** — sources disagree. Must be reconciled against the actual bylaw text before use. **Do not let the AI state these as fact.**
- 🔎 **MUST-VERIFY** — single source, or a known-volatile program/amount. Confirm per-property at report time.

**Rule baked into every AI section:** write only from fields tagged ✅. For ⚠️ or 🔎 fields, output "to be confirmed during feasibility" — never a guessed number.

---

## The stacking logic (read first)

This determines how the three pillars combine on one lot. Get this wrong and every unit count downstream is wrong.

- **Provincial floor (Bill 23):** most serviced residential lots get **3 units as-of-right** — main house + one interior secondary suite + one detached ADU (garden/laneway). ✅
- **Toronto goes further:** up to **4 units as-of-right citywide** in a multiplex form (RD/RS/RT/RM zones on Neighbourhoods-designated land), By-law 0473/0474, May 2023. ✅
- **Sixplex layer:** up to **6 units as-of-right** in 9 wards only (see Pillar 1). ✅
- **One ADU per lot:** a lot gets **either** a garden suite **or** a laneway suite — never both. ✅
- **No ADU on 5–6 unit lots:** if you build a five- or sixplex, you **cannot** also add a garden/laneway suite. The ADU stacks on 4-unit-and-under projects only. ⚠️ *(strongly reported; confirm against current bylaw)*

---

## PILLAR 1 — Multiplex / Missing Middle

| Field | Value | Flag |
|---|---|---|
| Permission basis | By-law 0473/0474 (fourplex, May 2023); OPA 818 / By-law 654-2025 (sixplex, June 2025) | ✅ |
| Where it applies | Neighbourhoods-designated land, residential zones RD, RS, RT, RM | ✅ |
| Fourplex ceiling | 4 units as-of-right **citywide** — no rezoning, no Committee of Adjustment, no public meeting if within envelope | ✅ |
| Sixplex ceiling | 6 units as-of-right in **9 wards only**: 8 wards across Toronto & East York District (roughly south of Eglinton, Roncesvalles→Beaches) **+ Ward 23 (Scarborough North)**. Elsewhere = opt-in by local councillor | ✅ |
| Exact 9-ward list | Confirm against City "Multiplex Housing" page — do not hardcode ward numbers from memory | 🔎 |
| Max height | ~10.5 m (raised from 10.0 m in the 2025 sixplex amendment) | ✅ |
| Bedroom caps | Duplex: 8 bedrooms total. 3+ units: avg 3 bedrooms/unit (→ 12 in a fourplex, 18 in a sixplex). Cap is **per building**, discourages rooming houses | ✅ |
| Parking | **None required** — citywide parking minimums eliminated Feb 2022 | ✅ |
| FSI | Does **not** apply to multiplexes (form governed by height/coverage/setbacks instead) | ⚠️ *(reported; confirm)* |
| Practical min lot | ~7.5 m (25 ft) frontage, ~30 m (100 ft) depth to fit 5–6 units comfortably. Not a hard cutoff, but below this the envelope rarely fits the max | ⚠️ |
| Setbacks | Zone-dependent; typical front ~6 m, rear ~7.5 m, sides ~0.9–1.2 m. **Varies by zone — pull per lot** | ⚠️ |
| Major Streets route | Townhouses / small apartments up to 6 storeys on qualifying Residential lots on Major Streets (OLT decision Sept 11, 2025) — separate from the multiplex envelope | 🔎 |

**Human-flag triggers (the risky 10%):** any sixplex claim (ward must be confirmed); any design near the height/coverage/setback edge (→ variance); lots under 7.5 m frontage or 30 m depth.

---

## PILLAR 2 — Garden & Laneway Suites (detached ADU)

> ⚠️ **This is the most conflicted pillar.** Sources disagree on footprint, height, and setbacks. The numbers below are the *most-cited current* version, but **every ⚠️ field must be reconciled against By-law 569-2013 (as amended by 847-2025 / 849-2025) and O. Reg. 462/24 before client use.** This is precisely where competitors publish wrong numbers.

**Garden suite** = detached backyard unit, access via side yard/street (no laneway needed).
**Laneway suite** = same idea but the lot must back onto a public laneway.

| Field | Value | Flag |
|---|---|---|
| Permission basis | By-law 89-2022 / 569-2013, amended by 847-2025 & 849-2025, aligned to O. Reg. 462/24 (in force Nov 20, 2024) | ✅ |
| Where it applies | Detached & semi-detached homes in R / RD / RS / RT / RM zones. Condos & existing townhouses excluded | ✅ |
| One per lot | Garden **or** laneway — not both | ✅ |
| Cannot sever/sell | ADU stays on the main lot; cannot be sold separately | ✅ |
| Max footprint | **CONFLICT:** sources cite (a) lesser of 10% of lot area or 60 m² (~645 sq ft), up to ~90 m² on larger lots; vs (b) flat 100 m² (~1,076 sq ft). Likely (a) for garden suites; (b) may be conflation. **Reconcile against bylaw.** | ⚠️ |
| Max height | ~6.0 m flat / ~6.3 m sloped (post-2025 update; angular-plane requirement reportedly removed, flat/shed roofs now allowed). Older proximity rule (4 m within 5 m of main house; 6 m if ≥7.5 m away) may still interact | ⚠️ |
| Rear setback | 1.5 m from rear lot line (one detailed source: rises to 3.0 m if 2nd-storey rear wall has windows) | ⚠️ |
| Side setbacks | **CONFLICT:** "greater of 0.6 m or 10% of frontage" vs "0.9 m" vs "1.5 m all property lines." **Reconcile.** | ⚠️ |
| Separation from main house | ~4 m (ties into the height-by-proximity rule) | ⚠️ |
| Soft landscaping | ≤6.0 m frontage → 25% of rear yard soft landscaping; >6.0 m frontage → 50% | 🔎 |
| Fire access | 1.0 m unobstructed path street→rear yard, kept clear. **Cannot be varied** — redesign is the only fix | ✅ |
| Parking | **No car parking required.** 2 bike spaces required | ✅ |
| Pre-approved plans | Free "Made in Toronto" garden/laneway plans launched 2025 — speed approvals, cut design cost | ✅ |
| Variance reality | ~80% of garden-suite variances approved (City May 2025 monitoring report); adds ~2–4 months | 🔎 |

**Human-flag triggers:** every footprint/height/setback number (all ⚠️); protected trees (any trunk ≥30 cm diameter → arborist report); heritage/ravine/conservation overlays; whether the lot actually has laneway access (decides garden vs laneway).

---

## PILLAR 3 — Secondary / Basement Suites (interior ADU)

More stable pillar — governed by the Ontario Building Code (province-wide) plus zoning permission.

| Field | Value | Flag |
|---|---|---|
| Permission basis | Zoning By-law 569-2013 — as-of-right in most R zones (detached, semi, townhouse). Typically the **2nd of the 4** multiplex units | ✅ |
| Min ceiling height | **1.95 m** throughout habitable rooms (1.85 m under beams/ducts). The #1 project-killer — measure before drawing | ✅ |
| Fire separation | Required between units (OBC); fire dampers if shared furnace | ✅ |
| Egress | Egress window in every bedroom; means-of-egress to exterior not through the main dwelling | ✅ |
| Alarms | Interconnected smoke alarms every storey + every bedroom; CO alarms near sleeping areas where fuel-burning appliance/garage present. Wireless interconnect now allowed (2024 OBC) | ✅ |
| Entrance placement | Usually side or rear — Toronto discourages a new front-façade door that reads as a duplex | ⚠️ |
| 2024 OBC | In force Jan 1, 2025 (largest revision in code history) | ✅ |
| Mar 31, 2026 OBC update | New work: 18°C basement design temp, full-height basement insulation, radon protection. Pre-2026 drawings no longer permittable | ✅ |
| Registration | Legal suite must be registered with the City and pass final inspection | ✅ |
| Designer | BCIN-qualified designer for standard conversions; P.Eng stamp required once structural work (underpinning, load-bearing changes) is involved | ✅ |

**Human-flag triggers:** ceiling height < 1.95 m (→ underpinning, $40–80k+); any structural work (→ P.Eng); older home on 100-amp service (→ panel upgrade).

---

## CROSS-CUTTING — Financing & Incentives layer

Pillar-agnostic. **Pulled fresh at report time, never from AI memory** — these change constantly and are where the misinformation gap is widest.

**Compliance language (mandatory):** always "government-backed financing options," never "free government grants." Value-uplift figures are **illustrative examples with disclaimers**, never guarantees.

| Program | What it is | Flag |
|---|---|---|
| DC waiver (municipal) | Development charges **fully waived up to 6 units/lot** — saves ~$45–50k/unit (~$200–270k/project). Extended from the original 4-unit cap | ✅ |
| DC deferral (ADU) | Suite DCs deferrable interest-free up to 20 years | 🔎 |
| GST/HST PBRH rebate (federal) | Full rebate of the 5% GST on new purpose-built rental, **4+ units, 90%+ long-term rental, construction start by 2031** — strongly favours hold-and-rent | ✅ |
| HST self-supply trap (garden suite) | Renting a new garden suite can make owner a "builder" under s.191 Excise Tax Act → HST on fair market value at first occupancy. Offsetting **New Residential Rental Property rebate** exists but is time-sensitive | 🔎 |
| CMHC MLI Select | Insurance-premium reductions + amortization up to ~50 yrs + high loan-to-cost (up to ~95%) on a points system (affordability/energy/accessibility). Generally **5+ units** | ⚠️ *(confirm current point thresholds — CMHC revises these)* |
| Multigenerational Home Renovation Tax Credit (federal) | 15% back on up to $50k of eligible cost, where suite is for a parent/adult relative | 🔎 *(confirm still in effect 2026)* |
| Garden Suite Servicing Grant (Toronto) | Reported up to $35k toward water/sewer lateral connection (2026 program year) | 🔎 *(single source — verify it exists)* |

### ⛔ DEAD PROGRAM — never cite

- **Federal "Canada Secondary Suite Loan Program"** (the proposed ~$80k / 2% loan) was **not implemented** — confirmed Budget 2025. Competitors still cite it. We never do. This single exclusion is a core ranking + AI-citation advantage.

---

## What's auto-fetchable vs. manual (per-property data layer)

| Field | Source | Auto? |
|---|---|---|
| Zoning designation | Toronto Open Data / zoning lookup | ✅ free |
| Lot geometry → area | Parcel open data | ✅ free |
| Ward (→ sixplex eligibility) | Ward open data | ✅ free |
| Map + street-view image | Google | ✅ free |
| Authoritative lot dimensions | MPAC / GeoWarehouse (Teranet) | ❌ paid / manual |
| Legal description | MPAC / GeoWarehouse | ❌ paid / manual |
| Year built | MPAC | ❌ paid / manual |
| Laneway access (garden vs laneway) | Map + manual eyeball | ❌ manual |
| Heritage / ravine / tree overlays | City overlays | ⚠️ semi-auto |

---

## Source list (for the verifier — confirm against primary bylaw text, not aggregators)

- City of Toronto — Multiplex Housing (ward list, bylaw docs): toronto.ca/.../multiplex-housing
- City of Toronto — Secondary Suites permit guide: toronto.ca/.../secondary-suites
- By-laws: 0473/0474 (fourplex), OPA 818 / 654-2025 (sixplex), 89-2022 / 847-2025 / 849-2025 (garden & laneway), 569-2013 (zoning)
- O. Reg. 462/24 (provincial ARU harmonization)
- Ontario Building Code 2024 (in force Jan 1 2025; update Mar 31 2026)
- CMHC — MLI Select, Housing Design Catalogue
- Federal — GST/HST PBRH rebate; Multigenerational Home Renovation Tax Credit

> **Verifier's job:** turn every ⚠️ into ✅ or a corrected number by checking the actual bylaw PDF, and confirm every 🔎 program still exists at current amounts. Only ✅ fields feed the AI writer.
