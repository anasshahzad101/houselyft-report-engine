# House Lyft Report Engine

Automated generation of Development Feasibility & Home Evaluation Reports, wired to GoHighLevel.

## What this repo is
The permanent home for the report-generation system. A Claude routine runs against this repo:
GHL webhook (Dev Pipeline -> Intro Booked) -> routine generates the report for the lead's address -> PDF uploaded to the contact's "Feasibility Report" field in GHL, note added, stage updated.

## Planned structure
- `engine/` - zoning lookup (property_lookup_v2), aerial imagery resolver, report builder
- `templates/` - master report template + city transform scripts
- `ghl/` - GoHighLevel API client (contact lookup, file upload, notes, stage moves)
- `routine/` - routine prompt + run entrypoint

## Status
- [x] GHL side proven end to end (scopes, pipeline IDs, address capture, file upload: HTTP 201)
- [x] Port zoning engine — ALL 9 cities live-verified. `engine/property_lookup_v2.py` (router + 8 live adapters) + `engine/property_lookup.py` (Toronto v1: live ward endpoint, self-provisioning zoning ingest from Toronto Open Data). Coxwell master address verifies: R (d1.0)(x7), Ward 19 Beaches-East York, 6 units as-of-right + ADU stacking (clears the 6+1 recommendation flag at engine level)
- [x] Port imagery module (`engine/aerial_imagery.py`) — Toronto 2025 ortho verified live (97,929 colours, edge sd 44.1)
- [x] Port report templates + city transforms — `templates/` (master + 4 city variants + static assets), `scripts/` (5 render + 4 xform), `docs/` (writer role, engine rules, Toronto rulebook, system overview). Master HTML smoke-rendered from repo assets: 16 pages, matches final deliverable page-for-page, zero Briarstone leftovers. Renderer: Playwright/Chromium (routine env must provision it). Brand fonts (Oswald/Lato) vendored in templates/fonts — no Google Fonts fetch at render (cert-blocked in cloud egress). Layout locked to the client-approved 14-page map at body zoom 0.94; aerial slots sized to the deliverable's measured geometry
- [x] GHL client module (`ghl/client.py`) — every operation live-verified against the sub-account: contact lookup, address assembly, PDF upload, notes, tags, opportunity search, stage endpoint
- [x] Orchestrator (`run.py`) — full loop executed 2026-07-10: contact id in -> engine lookup -> fresh 16-page render from repo templates -> report uploaded to Feasibility Report field -> engine-summary note -> report-ready tag
- [ ] Routine + GHL webhook wiring (final two clicks — see docs/SYSTEM_OVERVIEW.md)

## Secrets
No tokens are ever committed to this repo. Credentials are supplied to the routine at run time.
