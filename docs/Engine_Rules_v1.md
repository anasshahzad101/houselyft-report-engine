# Engine Rules & Form Logic — v1
### Built from Amaan's review of the Toronto prototype report

> **What this is:** Amaan ran the report's logic by hand in his comments. This document turns each comment into a **rule the engine executes automatically** — input → source → logic → output. It's the first real slice of the form-and-rulebook layer.
>
> **Two things to hold separate:**
> - His **method** (which map to open, which value decides what) → reusable now.
> - His **data values** (ward, zoning, area) → only plug in once we confirm the address they belong to.
>
> Where his note had a planning error, I corrected it against the verified Rulebook and **marked it** so the error doesn't get baked into every future report. See Part C.

---

## Part A — Data inputs (what the form + data layer must supply)

Every rule below pulls from one of these. This is the field list the form/fetch layer is responsible for.

| Field | Source | Auto-fetchable? | Amaan ref |
|---|---|---|---|
| Ward | Toronto Maps (`map.toronto.ca/torontomaps`) | Open data — likely yes | p2 |
| Zoning code + density + exception | Zoning By-law map (`map.toronto.ca/maps/map.jsp?app=ZBL_CONSULT`) | Open data — likely yes | p2 |
| Property age band | City property data | Yes (band only) | p2 |
| Lot area + frontage × depth | MPAC / GeoWarehouse / survey | **Paid or manual** | p4 |
| Major Street status | City Official Plan — Major Streets overlay | Semi-auto | p3 |
| Laneway abutment | Map + manual check | Manual | — |
| Property type | Zoning + form input | Yes | (gate) |

---

## Part B — The engine rules

Format for each: **Input → Source → Logic → Output → Flag.**

### R0 · Eligibility Gate *(runs first — before anything else)*
This is the rule 303 Coxwell taught us. The gate keys off **zoning**, not the photo.

```
INPUT:   zoning_code, property_type
SOURCE:  ZBL map + form
LOGIC:   IF zoning_code starts with R / RD / RS / RT / RM  (residential)
            AND property_type ∈ {detached, semi, townhouse}
         THEN pass → continue to R1
         ELSE fail → do NOT generate a homeowner report;
                     route to "commercial / mixed-use — needs manual review"
OUTPUT:  pass/fail (silent gate)
FLAG:    if zoning is residential but the building is commercial-use,
         flag "residential zone, non-residential current use — confirm redevelopment path"
```
> **This reopens the 303 Coxwell question:** Amaan's lookup returned `R (d1.0)(x7)` — residential. If that's 303 Coxwell, it **passes** the gate (zoning beats the storefront look). Confirm the address before trusting the pass.

### R1 · Ward → Sixplex eligibility
Amaan's headline comment, as a rule.

```
INPUT:   ward
SOURCE:  Toronto Maps
LOGIC:   sixplex_wards = {4, 9, 10, 11, 12, 13, 14, 19, 23}
         IF ward ∈ sixplex_wards  THEN sixplex_as_of_right = TRUE  (6 units)
         ELSE                          sixplex_as_of_right = FALSE (4 units; note opt-in path)
OUTPUT:  "Your ward ({ward}) {permits / does not permit} six units as-of-right."
FLAG:    ✓ VERIFIED once ward is confirmed
```
✓ For this lot: ward 19 (Beaches-East York) ∈ set → **6 units as-of-right.**

### R2 · Unit ceiling (main building)
```
INPUT:   sixplex_as_of_right (from R1)
LOGIC:   IF sixplex_as_of_right  THEN main_units_max = 6
         ELSE                          main_units_max = 4
OUTPUT:  feeds the Options section (fourplex / sixplex)
FLAG:    ✓ VERIFIED
```

### R3 · ADU stacking *(corrected — see Part C)*
```
INPUT:   main_units_max, laneway_abutment, rear_yard_available
LOGIC:   one ADU per lot (garden OR laneway, never both)
         IF laneway_abutment THEN adu_type = laneway
         ELSE IF rear_yard_available THEN adu_type = garden
         ELSE adu_type = none
         total_units_max = main_units_max + (adu_type ≠ none ? 1 : 0)   // up to 6 + 1 = 7
         DC: waived for first 6 units (incl. ADU if total ≤ 6);
             if total ≥ 7, ADU gets DC deferral (waived if rental 20+ yrs)
OUTPUT:  "Up to {total_units_max} units: {main_units_max} in the main building + 1 {adu_type} suite."
FLAG:    ⚠ confirm rear-yard fit + laneway status per lot
```

### R4 · Major Street → height upside *(corrected — not a gate)*
```
INPUT:   major_street_status
SOURCE:  Official Plan Major Streets overlay
LOGIC:   IF major_street_status = TRUE
         THEN unlock "small apartment / townhouse up to 6 storeys" envelope
              (ADDITIONAL upside — does NOT change the unit count from R1/R2)
         ELSE standard multiplex envelope (~4 storeys)
OUTPUT:  if TRUE: "This lot may also qualify for a taller small-apartment form
                   under the Major Streets rules — explored in the paid phase."
FLAG:    ⚠ confirm in paid assessment
```

### R5 · Buildable area / footprint
Now computable because the zoning returned a density (`d1.0`).
```
INPUT:   lot_area, density (d-value)
LOGIC:   buildable_gfa = density × lot_area      // 1.0 × 346.98 = ~347 m²
         CONFIRM which control binds the form:
            the FSI (d-value) OR the multiplex envelope (height/coverage/setbacks)
OUTPUT:  "Indicative buildable floor area ≈ {buildable_gfa} m² (control to confirm)."
FLAG:    ⚠ confirm governing control before stating as fact
```

### R6 · Bedroom cap
```
INPUT:   total main-building units
LOGIC:   IF units ≥ 3 THEN per-building bedroom cap applies (avg 3/unit)
            → fourplex 12 ; sixplex 18
OUTPUT:  "Bedroom cap for this building: {cap} total."
FLAG:    ✓ VERIFIED
```

### R7 · Parking
```
LOGIC:   parking_required = 0   // citywide, since Feb 2022
OUTPUT:  "No parking spaces required."
FLAG:    ✓ VERIFIED
```

### R8 · Financing & grants — citation requirement *(Amaan's "provide the link" notes)*
Not a math rule — a **content rule**. Every financing/grant line must print its primary source, or it doesn't render.

```
LOGIC:   FOR each program in {DC waiver, GST/HST rebate, DC deferral, Multigen credit, MLI Select}:
            IF no primary_source_url attached → do NOT print the line
OUTPUT:  each line shows its citation inline
```
Authoritative sources to attach:
- **DC waiver (≤6 units):** City of Toronto — By-law 654-2025 / development charges page
- **GST/HST purpose-built rental rebate:** Government of Canada — Enhanced GST Rental Rebate (CRA / Finance)
- **DC deferral (ADU):** City of Toronto — ADU development-charge deferral
- **Multigenerational Home Renovation Tax Credit:** CRA (federal)
- **CMHC MLI Select:** CMHC

---

## Part C — Corrections to Amaan's notes (transparency)

| His note | Issue | Verified rule |
|---|---|---|
| "Major Street decides 6 units (yes→6, no→fourplex)" | Treats upside as the gate | Ward 19 already grants 6 as-of-right (R1). Major Street is a **height** upgrade (R4), not the unit gate |
| "4 main + 1 ADU = 5" | Conservative | In the 9 wards: up to **6 main + 1 ADU = 7**, with the DC waiver/deferral nuance (R3) |
| Treated property as commercial earlier (photos) | Photo ≠ zoning | Gate keys off **zoning** (R0); his `R (d1.0)(x7)` lookup means it may be residential after all |

Everything else in his markup was correct and is used as-is.

---

## Part D — The one open decision

Rules R1, R5, R6, R7 are pure logic — they run fully automatically the moment the inputs exist. The bottleneck is **where two of those inputs come from**:

- **Ward + zoning** (R1, R0): Amaan read these off the City maps by hand. The question is whether those maps expose an **API / open-data feed** the engine can hit automatically, or whether a person has to click them per property.
- **Lot area** (R5): MPAC/GeoWarehouse — paid or manual, as before.

That's the "fully automated vs. analyst-assisted" fork, now pinned to exactly two fields instead of the whole report. **Want me to check whether Toronto's ward and zoning maps have an automatable open-data endpoint?** That answer decides how much of this runs with zero human touch.
