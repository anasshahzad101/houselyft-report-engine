# Automating Report Gen — Context

**Purpose:** Single orientation file so that when this repo is cloned locally, Claude Code (or any developer) understands the whole automated-report system end to end — architecture, how to run it, the pipeline used to build reports by hand, and every gotcha learned in production. Read this first, then the reference docs in `docs/`.

**Last updated:** 2026-07-30 · Maintained by Anas (SpeedX) + Claude

---

## 0. TL;DR — what this system does

House Lyft sends Canadian homeowners a free, branded **Development Feasibility & Home Evaluation Report™** (internally "property report") that tells them what they can build on their lot. The system is zero-touch:

```
GHL lead  ->  Claude cloud Routine  ->  clones this repo  ->  geocode
          ->  zoning lookup (engine adapter or live research)
          ->  program gate (province/city/unit-count)
          ->  aerial imagery  ->  fill master HTML template
          ->  render 14-15pp branded PDF  ->  per-client Drive FOLDER
          ->  write folder LINK into a GHL text field
          ->  email reviewer (Amaan) for QA
```

It runs unattended. A human (Amaan) reviews each report; Lee Yousaf is the client / final authority. Seth supplies addresses & instructions for manual runs; Ravi Behal is sales.

---

## 1. Repo map (what lives where)

| Path | What it is |
|---|---|
| `templates/report_houselyft_master.html` | **The master.** Every report is this file with property/zoning/market data swapped in. 3 injection markers for gated content. Cover now carries the real navy HouseLyft logo. |
| `engine/property_lookup.py` | Toronto internals + `geocode()` (the router imports geocode from here). |
| `engine/property_lookup_v2.py` | Adapter router. `lookup(address)` geocodes then dispatches to a city adapter. City zoning fns take `(lat, lon)`. |
| `engine/aerial_imagery.py` | Aerial resolver: municipal sources first, then Mapbox fallback + a blank-tile validator. Has the Mapbox monthly-budget counter. |
| `engine/ontario_provincial.py` | OIWMS provincial aerial fallback for Ontario gap cities. |
| `config/programs.json` | **Program gate as DATA** (ON/AB/BC program sets). Never hardcode programs in the template. |
| `assets/houselyft_logo_navy.svg` | Logo for light backgrounds (on the cover). |
| `assets/houselyft_logo_white.svg` | Logo knockout for dark backgrounds. |
| `assets/houselyft_logo_brand.svg` | Original brand colours (Ink #1E1B17 + Coral #E0573F) as supplied. |
| `ghl/client.py` | All GHL + Drive-dropbox + email helpers. See §4. |
| `src/run_report.py` | **STUB — `generate_report()` raises NotImplementedError.** The real end-to-end engine was never ported into this repo; the cloud Routine builds reports its own way, and manual reports are hand-built from the master template (see §5). |
| `docs/` | Reference docs — see §8. |

---

## 2. The two ways reports get built

1. **The cloud Routine (production, unattended).** Fires on GHL leads. It has its own env vars set and builds/renders/delivers on its own. You do NOT run this from the repo — it lives in Claude's cloud Routine config. `docs/ROUTINE_PROMPT.md` is its prompt.

2. **Manual / batch builds (this repo, by hand).** For known contacts, corrections, or backfills. Because `src/run_report.py` is a stub, these are built by filling the master template directly. The reusable batch pipeline is described in §5.

---

## 3. Environment / running locally

The sandbox (and any fresh clone) does NOT inherit the Routine's env. Set these before running anything that geocodes, images, uploads, or emails:

```bash
export MAPBOX_TOKEN="<public pk. token — does BOTH imagery AND geocoding>"
export HL_DROPBOX_URL="<Apps Script /exec URL>"
export HL_DROPBOX_KEY="<dropbox shared key>"
export GHL_TOKEN="<GHL private integration token>"
export GHL_LOCATION_ID="<GHL location id>"
```

**Credentials are NOT stored in this file** (see §4 for why and where they live). Get them from: GHL Settings > Private Integrations (GHL token), the Apps Script project (dropbox URL/key), and the `houselyft-report-env` store (Mapbox token). If a credential is lost, regenerate it rather than digging it out of history.

Install deps after a fresh clone / sandbox reset:
```bash
pip install requests pymupdf playwright shapely pillow pyproj mercantile cairosvg --break-system-packages
playwright install chromium
```

Re-clone pattern (PAT lives in GHL/GitHub settings, not here):
```bash
cd /home/claude && git clone -q https://<PAT>@github.com/anasshahzad101/houselyft-report-engine.git gh
```

Push directly with git (there is no surviving `push.py` after a reset):
```bash
git config user.email "..."; git config user.name "..."
git add <files>; git commit -q -m "..."; git push -q origin HEAD
```

---

## 4. Credentials policy (IMPORTANT)

- **Never commit live credentials to the repo, and never paste them back into chat.** Tokens have full API access; putting them in git history or a transcript is an exposure risk.
- The GHL private token, Mapbox token, GitHub PAT, and dropbox key all live in their own settings/consoles. This context file deliberately references them by NAME only.
- **Known tech-debt:** the Apps Script dropbox creds (`HL_DROPBOX_URL` / `HL_DROPBOX_KEY`) are currently hardcoded in the Apps Script and passed as env — they should be moved to environment variables the same way `MAPBOX_TOKEN` is. (Tracked in §7.)

---

## 5. The manual batch pipeline (how hand-built reports are made)

Per report, the proven sequence:

1. **Geocode with Mapbox** (NOT the engine's default Nominatim — it rate-limits and misplaces lots). Endpoint: `https://api.mapbox.com/geocoding/v5/mapbox.places/{addr}.json?country=CA&limit=1&types=address`. Returns lat/lon + `relevance` + city/province context.
2. **Confidence + city cross-check.** If `relevance < 0.8` or the resolved city != expected city, HOLD the report and flag for a human. Never ship a wrong-location aerial.
3. **Zoning.** If the city has a verified engine adapter, monkeypatch the engine's geocoder to Mapbox and call `lookup()`:
   ```python
   import property_lookup as pl, property_lookup_v2 as v2
   pl.geocode = mb_geocode; v2.geocode = mb_geocode   # v2 imported it by name
   ```
   If no adapter, do live web research for the city's current zoning/bylaw and frame honestly ("confirm in Phase 2").
4. **Aerial.** `engine/aerial_imagery.get_aerial(desc, city_key, half_m=~52, lat=, lon=)`. Municipal source if available (Toronto ortho, Brampton), else Mapbox. **The Mapbox budget counter needs `HL_DROPBOX_URL`/`HL_DROPBOX_KEY` in env or it fails closed with a RuntimeError.** Transient HTTPErrors happen — retry 2-3x with a short sleep.
5. **Fill the master template** (the batch builder does: single aerial banner, details table, zoning section, options, province gate, summaries; then scrubs any residual template tokens).
6. **Province gate** — never let ON/AB/BC programs cross-contaminate. Alberta: no-PST every scale, GST at 4+, MLI at 5+. Ontario: Bill 23 DC relief, HST/GST at 4+, Toronto DC waiver only if Toronto & <=6 units. BC: SSMUH framing, GST at 4+, MLI at 5+/6-near-transit.
7. **Render** Letter format via Playwright/Chromium (SVG logo renders as vector — PyMuPDF `get_images()` will report 0 images on the cover; that's expected, verify by pixel/colour analysis instead).
8. **Verify** pages / orphan pages / template leaks / aerial present / correct lead & zone.
9. **Deliver:** create/find the per-client Drive folder, `client.drive_upload(pdf, folder_id, "Name - Address.pdf")`. If it's a GHL contact, set the folder-link text field (readback-verified), add note + tags. **Batch-email Amaan once at the end of a wave**, not per report.
10. **ALWAYS verify delivery** via Drive search + Gmail search — don't trust return codes (they can time out and false-FAIL, or false-succeed).

---

## 6. Hard-won gotchas (read before debugging)

- **Nominatim (engine default geocoder) is unreliable** — 503s, rate-limits, misplaces lots. Use Mapbox for geocoding. It does both geocoding and imagery on the same token.
- **Mapbox budget counter fails closed.** No `HL_DROPBOX_URL`/`HL_DROPBOX_KEY` in env -> `_mapbox_budget_ok()` raises -> every aerial "fails (RuntimeError)". Set the dropbox creds.
- **`send_notice()` can false-FAIL.** The wrapper returns False on a timeout even when the email actually sent. Always confirm in Gmail Sent rather than trusting the return.
- **Drive `download_file_content` returns the PDF as base64 nested inside a JSON string** (`type:text`, with `content: "JVBER..."`). Decode it; it's the real bytes.
- **Multi-property owners:** the Routine's scope-resolution ranks the call-note address ABOVE the form `address1`, so it can build for the wrong lot when an owner has two. Confirmed misfires historically (Moshiur, Ken). Needs a Routine fix.
- **GHL link field holds ONE url** — a client's second property overwrites the first. Consider pointing the field at a parent folder that holds all of a client's properties.
- **`src/run_report.py` is a stub** — don't expect a one-call build function; use the §5 pipeline.
- **Amalgamation / municipality accuracy:** Bolton = Town of Caledon (not a city). Stoney Creek & Ancaster = City of Hamilton (amalgamated 2001, By-law 05-200). Get the municipality right or the whole report reads wrong.
- **Verify current rules, don't assume:** e.g. Markham's proposed 4-unit as-of-right was REVOKED (strong-mayor powers, early 2026) — reliable ceiling is the 3-unit provincial floor. The federal "Canada Secondary Suite Loan Program" ($80k/2%) was NOT implemented (Budget 2025) — never cite it as available.
- **Image viewer can go blank in a session** — verify visuals via pixel/colour analysis (unique-colour counts, bounding boxes), not just the viewer.

---

## 7. Standing open items / tech-debt

- Update the Routine to drop the `-AI-DRAFT.pdf` filename suffix and the "AI-draft" email wording (Seth's naming = `Name - Address.pdf`). `docs/ROUTINE_PROMPT.md` line ~162.
- Fix the multi-property-owner address-resolution bug in the Routine (call-note addr overriding form addr).
- Move hardcoded `HL_DROPBOX_URL` / `HL_DROPBOX_KEY` out of the Apps Script into env vars (mirror `MAPBOX_TOKEN`).
- Duplicate cleanup: rebuilt folders currently hold BOTH the new imaged report AND the old `-AI-DRAFT` placeholder (dropbox adds, doesn't overwrite). Delete the superseded ones only on explicit go-ahead.
- Verification backlog: Ken Dodds corner status (6 vs 8 dwellings); Tony/Kelowna transit+hazard checks; Calgary R-CG current district post-2026-repeal; Toronto 6+1 (garden suite on 5-6 unit lots) permissibility.
- GHL workflow Part C: Opportunity Stage Changed trigger -> report-fire endpoint.

---

## 8. Reference docs (the rest of `docs/`)

- `SYSTEM_OVERVIEW.md` — deliverables map, template/engine layout.
- `PROJECT_STATE.md` — the living project-state snapshot (regenerate each session).
- `ROUTINE_PROMPT.md` — the production Routine's own prompt (the unattended builder).
- `PROGRAM_GATING_v1.md` — the program gate rules (ON/AB/BC), keep in sync with `config/programs.json`.
- `Engine_Rules_v1.md` — engine behaviour and adapter rules.
- `Toronto_Rulebook_v1.md` — Toronto-specific zoning logic (wards, 4+1 / 6+1, By-laws 474-2023 & 654-2025).
- `AI_Report_Writer_Role_v1.md` — the report-writing voice/role.

---

## 9. Compliance rules (apply to every client-facing report)

- Trademarked terms verbatim with ™: Development Feasibility & Home Evaluation Report™, Property Opportunity Assessment™, Property Opportunity Blueprint™, Builder Ready Package™, Builder Match™.
- No "grants" / "free government money" language; no build-cost figures or value guarantees.
- No invented numbers. Show commercial fee as "Scoped per project" when unconfirmed.
- Programs gated strictly by province/city/unit-count; unimplemented programs are actively corrected, not silently omitted.
- Honest caveats required (rural servicing, owner-stated dims, live-research items, heritage overlays, etc.).
