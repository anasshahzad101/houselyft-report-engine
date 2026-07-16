# Program Gating — Scope & Eligibility Contract (v1)
### How we stop recommending programs the homeowner cannot get

> **The core principle:** programs are gated on **what the homeowner told us they want**
> — never on what the zoning allows.
>
> This is the same philosophy as `AI_Report_Writer_Role_v1.md`: we don't make the report
> accurate by asking nicely. Gates live as **data** (`config/programs.json`), because a rule
> written in prose gets *interpreted* — a table gets *applied*.

---

## Why this exists

A client screenshare (14 Jul 2026) on **Ryan Ramsay / 11 Lee Ave, Angus** found the report
recommending **CMHC MLI Select** — which requires 5+ rental units — on a **one-unit ADU**.
The prospect raised it on the call.

The report printed *"Requires a minimum of 5 rental units"* directly beside a one-unit
recommendation. **It contained its own disproof.**

Root cause: `templates/report_houselyft_master.html` **hardcodes** MLI Select, the GST/HST
PBRH rebate, CMHC ACLP, CMHC Prefab Plus and a **Toronto** DC Waiver row. Every report
inherits all five regardless of scope *or municipality* — a Mississauga homeowner was being
told about a Toronto program.

The reports aren't built from a grounded packet; they're built by adapting a template with
the programs pre-printed, and the writer is expected to cross off what doesn't apply.
That's a highlighter where there should be a filter.

---

## Layer 1 — Scope is READ, never inferred

Every input already exists in GHL. Nothing new needs capturing.

| Input | GHL field ID | Type | Populated |
|---|---|---|---|
| **Project type** — the primary scope signal | `EPzqHHy5AU2iIvHIAhKf` | SINGLE_OPTIONS | **10/10** |
| **Their own words** — refines / overrides | `oPfN9unZ4y37M1g1NwTq` | LARGE_TEXT | **10/10** |
| Capital being deployed — the ACLP gate | `bvJsGbtyHmEeOLQUEuBu` | SINGLE_OPTIONS | **0/10 — unusable** |
| Accredited investor | `aGMdwojrkbwaHEm4MtFG` | SINGLE_OPTIONS | partial |
| Existing investments | `UuJGDD9alPQtyUG2U7q0` | LARGE_TEXT | partial |
| Call notes | contact notes | free text | varies |

### Scope map
| Form value | `units_added` | Confidence |
|---|---|---|
| Secondary Suite | **1** | high |
| Basement Apartment | **1** | high (interior) |
| Garden Suite, Laneway Home or ADU | **1** | high (detached) |
| Multiplex Development | *unresolved* | low — read the sentences |
| Other | *unresolved* | none — read the sentences |

**Three of five values resolve deterministically to 1 unit.** Only "Multiplex Development"
and "Other" need the sentence field.

---

## Layer 2 — Resolution order (when signals disagree)

Apply in order. **Stop at the first that resolves.**

1. **A call note naming this address.** Most recent, human-verified, property-specific.
2. **The sentence field** (`oPfN9unZ4y37M1g1NwTq`) — the homeowner's own words.
3. **The project-type single-select** (`EPzqHHy5AU2iIvHIAhKf`).
4. **Unresolved → render in TIERED mode and flag `needs-scope-review`. Never halt.**

**Never** resolve scope from the zoning maximum. Zoning answers *"what's allowed?"* — the
wrong question. Programs key off *"what's being built?"*

### The per-contact / per-property problem
The form field is **per contact**. Properties are **per address**. A contact with two
properties has *one* form answer covering *one* intent.

> **Ryan Ramsay** — form says `Basement Apartment` (his primary, 34 Knicely Rd, Barrie).
> But 11 Lee Ave, Angus is a **detached ADU for his sister**, established on the call.
> The form field is right about the wrong property.

**Rule:** where a contact has multiple properties, the address-specific note or sentence
wins over the form field. Both of Ryan's happen to resolve to 1 unit — that was luck, not design.

---

## Layer 2b — Never halt. Two render modes.

**The report is the free lead magnet. Refusing to produce one is the only outcome with no
upside** — the homeowner gets nothing and the lead goes cold. Unknown scope changes *how*
the report renders, never *whether* it renders.

### `scoped` — we know what they want
Lead with the stated goal. Larger options are labelled upside. Programs render only if they
clear the stated scope; those clearing only a larger option **move into that option**; those
no option reaches are **dropped**.

### `tiered` — we know the class, or nothing
Present tiers across the as-of-right range, smallest to largest. **Attach each program to the
smallest tier that clears its gate, with the threshold shown beside it.**

> *"At one unit: development-charge exemption. At four: the GST/HST rental rebates open up.
> At five: CMHC MLI Select."*

This is the **positive form of the gate**, and it is already how the shipped Grants &
Incentives report frames Edmonton:

> *"8 units clears every program threshold: 4+ GST Rebate · 5+ MLI Select · $1M+ ACLP."*

Nothing is claimed as available — it's available **at a tier**. That's honest *and* it's a
better sales asset than a single scoped recommendation, because it shows the owner what scale
unlocks. Then ask the scope question in the report, in their own language, and tag
`needs-scope-review`.

### Why "scope to smallest" is the wrong default
It is safe for a homeowner and **actively wrong for a developer**.

> **Rick Y** — form: `Multiplex Development`. Sentence: *"4.2 acres – across the road from
> world class…"*. No unit count anywhere.
>
> Scoping him to 1 unit would strip MLI Select, the HST rebates and ACLP from a lead on
> **4.2 acres** who told us he wants a multiplex. That's the original defect wearing a
> different hat — wrong content, opposite direction.

`Multiplex Development` is not "no information." It tells us the class: **not one unit**.
Tiered mode leads with the multiplex tiers and lets the programs attach where they land.

---

## Layer 3 — Applying the gate

Every program in `config/programs.json` carries its own gate. Then:

1. **A program renders only if some option in the report clears its gate.**
2. **It sits with the smallest option that clears it.**
3. **Gated above every option in the report → it does not appear at all.**
4. **A larger option exists that clears it → it moves into that option's description**,
   stated conditionally: *"if you build to four units, the HST rebate opens up."*
5. **Gate unconfirmable from data we hold → stay silent.** Never assert.
6. **The gate covers every mention — prose as well as table rows.**

### Rule 6 is not theoretical
On Ryan's rebuild, deleting the MLI Select **table row** left this in Section 6's intro:

> *"…construction financing, and specialized programs such as **CMHC MLI Select**."*

A row-only gate would have shipped that. Programs get name-dropped in prose.

### Rule 5 kills the occupant question
MHRTC's gate is `occupant ∈ {senior 65+, DTC-eligible}`. We almost never hold that. Gate
unconfirmed → **silent**. Nobody has to ask the homeowner who's moving in.

---

## The boundary — a per-program table, not one rule

> Amaan: *"IF 5 units or less, remove Financing / Grant content related to that."*

**Directionally right, off by one, and too blanket.** At **exactly 5**, MLI Select
**applies** — 5 is its *minimum*, not its cutoff. And the thresholds differ: GST/HST needs
**4+**, MLI Select **5+**, ACLP **$1M+**. One blanket rule trades one wrong report for another.

This is not hypothetical: **Michael Bukrinsky lands on exactly 5.** Amaan's literal wording
would have stripped a program he qualifies for.

---

## Worked examples — the three approved demos

| Lead | Scope (and where it came from) | MLI Select | GST/HST | Municipal |
|---|---|---|---|---|
| **Ryan** — 11 Lee Ave, Angus | 1 ADU — *call note* (form said Basement Apartment, wrong property). Essa caps at **2** | ❌ gone | ❌ gone | ✅ Simcoe County + Bill 23 |
| **Muhammad** — 6564 Eastridge, Mississauga | 1 ADU — *form: Garden Suite*, confirmed by sentence. Lot allows **4** | ❌ gone | ➡️ **moved to Option B** | ✅ Bill 23; 4th-unit incentive Option-B-only |
| **Michael** — 441 Rimilton, Etobicoke | **5** — *sentence: "4plex plus garden suite"* (form said "Other") | ✅ **kept** | ✅ kept | ✅ Toronto DC waiver |

**Ryan** — nothing moves: Essa caps at 2 ARUs, so 4+/5+ programs are permanently
unreachable on that lot. Removal is total, not deferred.

**Muhammad** — the lot allows 4, so GST/HST doesn't die, it **moves into Option B** with the
reason attached. His actual question was financing; Option C answers it with refinance/HELOC
against five years of equity.

**Michael** — the **retention proof**. The gate is surgical, not destructive. Note his scope
came from the *sentence field* — his form value was "Other," which resolves nothing. Rule 2
in action.

---

## Known gaps

0. **`Multiplex Development` carries no unit count** (1/10 leads — Rick Y). Renders tiered
   and tags `needs-scope-review`. Either Ravi captures the unit count on multiplex leads, or
   Amaan resolves the tag. The report still ships either way.
1. **Capital field empty 0/10** — so ACLP cannot gate on stated capital and falls back to the
   Phase 2 budget. Making it required on the form would close this deterministically.
   *Lee/Ravi decision.*
2. **County-level programs are easy to miss.** The Simcoe County suite program applies to
   **Barrie, Angus/Essa, Innisfil, Springwater** — it was found by accident on one Angus
   report. Check the **county**, not just the city.
3. **Michael's 5th unit is unconfirmed.** `adu_stacking_on_multiplex: true` says a garden
   suite can sit alongside a 4-unit multiplex — the single largest open accuracy item.
   **MLI Select's eligibility rides entirely on it.** Flagged in Option C, not asserted.
4. **This is still a filter at the writing step, not the packet.** The structural fix is
   `build_packet()` filtering programs so the AI never *sees* a failing one — then rule 6 and
   validation check 4 in `AI_Report_Writer_Role_v1.md` enforce it for free.

---

## How this plugs in

```
GHL contact ─┬─ project_type  (EPzqHHy5AU2iIvHIAhKf)
             ├─ sentences     (oPfN9unZ4y37M1g1NwTq)   ─→ resolve_scope() ─→ units_added
             └─ call notes                                        │
                                                                  ▼
property_lookup_v2 ──→ municipality / county / zoning ──→ apply_gates(programs.json)
                                                                  │
                                                    │
                                        ┌───────────┴───────────┐
                                        ▼                       ▼
                                  scope RESOLVED          scope UNRESOLVED
                                   → scoped mode           → tiered mode
                                        │                       │
                            clears  ────┤              each program attaches to
                            → renders   │              the smallest tier that
                                        │              clears it, threshold shown
                            fails   ────┤                       │
                            → moves into a larger      + tag needs-scope-review
                              option, or is dropped    + ask the scope question
```

**A report is produced in every path.** There is no branch that ends in silence.
