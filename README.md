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
- [x] Port zoning engine (`engine/property_lookup_v2.py`) — 8 live-query cities verified from container; Toronto adapter pending v1 rebuild (ward + zoning ingest)
- [x] Port imagery module (`engine/aerial_imagery.py`) — Toronto 2025 ortho verified live (97,929 colours, edge sd 44.1)
- [ ] Port report templates + city transforms
- [ ] Routine + GHL webhook wiring

## Secrets
No tokens are ever committed to this repo. Credentials are supplied to the routine at run time.
