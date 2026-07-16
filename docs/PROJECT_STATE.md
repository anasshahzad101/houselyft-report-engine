# House Lyft — Project State
**Last updated:** 2026-07-16 · Maintained by Anas (SpeedX) + Claude

> Drop this into Project Knowledge. Any new chat in this project can read it
> instead of being re-briefed. Regenerate at the end of a working session.

---

## 1. What this system is

GHL lead → Claude cloud Routine → clones the GitHub report engine → runs the zoning
lookup → **applies the program gate** → renders a 14-page branded PDF → delivers three ways:

| Destination | What lands there |
|---|---|
| Google Drive | Per-client folder `[Name] — [Address]`, PDF inside |
| GHL contact | **Folder link only** (text field). No PDF on the contact. |
| Email | Notice to Amaan (reviewer) via the Apps Script dropbox |

**Status:** LIVE, running unattended, **now with program gating** (built 16 Jul).

---

## 2. Where things live

| Thing | Location |
|---|---|
| Report engine | GitHub `anasshahzad101/houselyft-report-engine` |
| Routine | claude.ai/code — "HouseLyft Report Generator", env `houselyft-report-env`, prompt **v3c** |
| Drive parent folder | `1_VjKsh864qsvPc1Jmv2cdIjZ_iUpWxoT` (Amaan = Editor) |
| Reviewer | Amaan Hameed — amaan@tcsyeg.com (no GHL access; Drive only) |
| Sales / calls | Ravi Behal · **Lee Yousaf = final authority** |
| Apps Script dropbox | deployment `AKfycbz8-TqOYUIjCtSyoB-UjAuLAG4If90-lXhwTbQU-1Ok3v9vm06GMvDUlmXp14hkZU4iXA` |

**Secrets** (GHL token, GitHub PAT, dropbox key) live in memory + the working chat.
Deliberately not written here.

### GHL field IDs
| Field | ID | Notes |
|---|---|---|
| Feasibility Report Link | `eUGAPkugk1U4FHNJDP9Q` | TEXT — Drive **folder** URL. The active field. |
| AI Feasibility Report | `7JFKnnjOjyrKXxGY2Pdh` | FILE_UPLOAD — unused under link-only |
| **What sort of project are you consider?** | `EPzqHHy5AU2iIvHIAhKf` | SINGLE_OPTIONS — **the scope gate input, populated 10/10** |
| **Give us 1-2 sentences…** | `oPfN9unZ4y37M1g1NwTq` | LARGE_TEXT — **populated 10/10**, refines/overrides |
| How much capital…? | `bvJsGbtyHmEeOLQUEuBu` | SINGLE_OPTIONS — **empty 0/10, unusable** |
| Accredited investor? | `aGMdwojrkbwaHEm4MtFG` | partial |
| Existing investments | `UuJGDD9alPQtyUG2U7q0` | partial |

### Key repo files
- `config/programs.json` — **the gate table as data** (12 programs)
- `docs/PROGRAM_GATING_v1.md` — **the gate spec**
- `docs/ROUTINE_PROMPT.md` — **v3c**, step 3b is the gate
- `docs/AI_Report_Writer_Role_v1.md` — 3-layer accuracy contract, now wired to the gate
- `templates/report_houselyft_master.html` — **programs removed**, three injection markers
- `engine/property_lookup_v2.py` — verified zoning router, 10 cities
- `engine/aerial_imagery.py` — `get_aerial()` → `.image` / `.source` (**not** `.credit`)
- `ghl/client.py` — `set_text_field`, `drive_upload(path,…)`, `send_notice`, `add_note`, `find_contacts`

---

## 3. Program gating — BUILT AND LIVE (16 Jul)

### The principle
> **Programs are gated on what the homeowner wants — never on what the zoning allows.**
> Zoning answers *"what's allowed?"* — the wrong question. Programs key off *"what's being built?"*

### What was wrong
The master template **hardcoded** MLI Select, GST/HST PBRH, CMHC ACLP, Prefab Plus and a
**Toronto** DC Waiver. Every report inherited all five regardless of scope *or municipality*.
Found via client screenshare (14 Jul) on Ryan Ramsay / 11 Lee Ave: the report recommended
**MLI Select (needs 5+ units) on a one-unit ADU**, and printed *"Requires a minimum of 5
rental units"* right beside it. It contained its own disproof. The prospect raised it on the call.

### Scope is READ, never inferred
Resolution order — stop at the first that answers:
1. **Call note naming this address** (most recent, human-verified, property-specific)
2. **Sentence field** `oPfN9unZ4y37M1g1NwTq` — their own words
3. **Form select** `EPzqHHy5AU2iIvHIAhKf`
4. **Unresolved → tiered mode + `needs-scope-review`. Never halt.**

| Form value | units_added |
|---|---|
| Secondary Suite / Basement Apartment / Garden Suite, Laneway Home or ADU | **1** |
| Multiplex Development | class only (*not* 1) — read sentences |
| Other | read sentences |

**Per-contact vs per-property:** the form field is per **contact**; properties are per
**address**. Ryan's says "Basement Apartment" — true of his *primary* (34 Knicely), not of
Angus. Address-specific note/sentence wins.

### Two render modes — a report is ALWAYS produced
- **scoped** — units known. Lead with the goal; larger programs move into larger options; unreachable ones dropped.
- **tiered** — units unknown. Tiers across the as-of-right range; each program attached to the **smallest tier that clears it**, threshold shown. *"At four units the HST rebates open up; at five, MLI Select."* Nothing claimed as available — available **at a tier**.

Refusing to produce a report is the only outcome with no upside. **"Scope to smallest" is
the wrong default** — safe for a homeowner, actively wrong for a developer (Rick Y, 4.2 acres).

### Gate table (in `config/programs.json`)
| Program | Gate |
|---|---|
| CMHC MLI Select | ≥ **5** rental units |
| GST/HST PBRH Rebate | ≥ **4** units, 90%+ long-term |
| CMHC ACLP | ≥ **$1M** loan (budget-set, not unit-set) |
| CMHC Prefab Plus | inherits MLI Select |
| Multigenerational credit | occupant = senior 65+ / DTC — usually unconfirmable → **silent** |
| Toronto DC Waiver | ≤6 units **AND** municipality = Toronto |
| Bill 23 DC exemption | first 1–2 ARUs |
| County suite programs | any suite — **check COUNTY, not city** |
| Refinance / HELOC / Construction | any scale |

⚠️ **Amaan's "5 units or less → remove" is off by one.** At *exactly* 5, MLI Select **applies**.
Per-program, not blanket. Michael Bukrinsky is that exact case.

### Rules that came from real failures
- **The gate covers PROSE, not just table rows.** Section 6's intro name-dropped MLI Select after the row was deleted.
- **Unconfirmable gate → stay silent.** This is why the occupant question never needs asking.
- **Gates as data, not prose.** A rule in a prompt gets interpreted; a table gets applied.

---

## 4. Reports delivered (16 Jul) — all gated, all approved

| Lead | Scope (source) | Gate result |
|---|---|---|
| **Ryan Ramsay** — 11 Lee Ave, Angus | 1 ADU — *call note* | MLI/PBRH/ACLP/Prefab/Multigen **dropped** (Essa caps at 2 — permanently unreachable). Kept Simcoe County + Bill 23. Reframed off aging-in-place → **sister** (17 refs) |
| **Muhammad Toheed** — 6564 Eastridge, Mississauga | 1 ADU — *form: Garden Suite* | MLI **gone** (lot maxes at 4). GST/HST **moved into Option B**. Toronto DC row (wrong city) removed |
| **Michael Bukrinsky** — 441 Rimilton, Etobicoke | **5** — *sentence: "4plex plus garden suite"* (form said "Other") | **MLI Select KEPT** — the retention proof |

Amaan emailed with the reasoning + the off-by-one correction. **Open question put to him:**
Michael's 5th unit depends on `adu_stacking_on_multiplex` — if it's really 4, MLI Select comes out.

---

## 5. Pending

1. **Rick Y — the tiered-mode demo isn't built.** Form: `Multiplex Development`, 4.2 acres,
   Innisfil. The only lead of 10 that resolves to tiered. Would complete the behaviour set.
2. **Structural fix:** the gate is applied at the *writing* step, not the packet. The real
   version is `build_packet()` filtering so the AI never *sees* a failing program — then role
   rule 6 + validation check 4 enforce it for free. Needs the ReportLab/template port.
3. Retro-check reports sent before 16 Jul (Karen, Larry, Leonila, Jumaal, Abdul, Matih) — all
   scope 1, all likely carrying gated-out programs.
4. **Capital field empty 0/10** — making it required on the form would gate ACLP deterministically. *Lee/Ravi decision.*
5. Archive stale Apps Script deployments (keep only `z8-TqOY`).
6. Batch-run 3×daily (8/2/8 Toronto) — scoped, not built.
7. Parked: GitHub PAT rotation, Mapbox token, PR #21.

---

## 6. Hard-won lessons

**Process**
- **Verify before asserting.** Real defects caught this way: Springwater-not-Barrie geocode;
  missing Simcoe County grant; MLI Select surviving in *prose*; doctype corruption moving
  grants to page 1; a "missing" phrase that was only a line wrap.
- **Check the form custom fields, not just contact notes.** I wrongly told Anas that Karen/
  Larry/Leonila had no stated goal — it was in the form field all along. There was no intake gap.
- **Don't "fix" what isn't broken.** Rick Y was flagged for retroactive repair; he's a
  multiplex developer on 4.2 acres whose programs may legitimately apply.

**Technical**
- **`find()` returning -1 is dangerous.** `s[:j]` with `j = -1+5 = 4` injects into `<!DOCTYPE>`.
  Always assert the anchor exists. **The grants header uses `<th>`, not `<td>`.**
- **Page-fill check is mandatory** before delivery: 14 pages, every page ≥0.35 fill. It caught
  the doctype corruption. Keep the spotlight to 3 tight bullets or a 4th orphans.
- **Normalise whitespace before probing PDF text** — phrases wrap mid-line and read as missing.
- `client.drive_upload(path, folder, name)` takes a **path**, not bytes.
- `get_aerial()` returns `.source`, **not** `.credit`.
- **Gmail connector is READ-ONLY** — sending goes through the Apps Script `sendmail` action.
- **Drive connector can't carry multi-MB PDFs** — use the dropbox endpoint (base64 in the raw
  POST body, params in the query string).
- Toronto ortho 2025 (8cm) works at lot scale. Most other cities have no licensed source →
  honest pending line. Never Google Maps.

**Content**
- **No invented numbers.** Hedge grant figures pending official fact sheets.
- County-level programs are easy to miss (Simcoe covers Barrie, Angus, Innisfil, Springwater).
- The Grants & Incentives report already used tiered framing before we built it:
  *"8 units clears every program threshold: 4+ GST Rebate · 5+ MLI Select · $1M+ ACLP."*
