# House Lyft Report Engine

Automated feasibility report generation and delivery for House Lyft leads.

## Flow
1. Lead's opportunity reaches **Dev Pipeline → Intro Booked** in GoHighLevel
2. GHL workflow webhook fires a Claude routine (API trigger) with the contact ID
3. Routine clones this repo, runs `src/run_report.py --contact-id <id>`
4. Engine builds the property feasibility PDF from the lead's address
5. PDF is uploaded to the contact's **Feasibility Report** custom field, a note is added

## Status
- [x] GHL integration proven live (2026-07-10): auth, contact/opportunity lookup, file upload
- [x] Pipeline guard: runs only for the configured pipeline (`config/ghl.json`)
- [ ] Engine port (zoning, imagery, templates) — in progress
- [ ] Claude routine creation + GHL workflow wiring — after engine port

## Secrets
`GHL_TOKEN` and `GHL_LOCATION` come from environment variables (see `.env.example`).
Nothing secret is committed to this repository. IDs in `config/ghl.json` are identifiers, not credentials.

Maintained by SpeedX Marketing. Built and operated via Claude.
