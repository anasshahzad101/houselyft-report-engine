# House Lyft — Property Report System

Everything built in this session: the finalized master report, four lead reports,
the nine-city GTA zoning engine, and the templates and scripts behind them.

---

## 01_Reports_PDF — final deliverables

| File | Lead | Property | Type |
|---|---|---|---|
| `Property_Report_303_Coxwell_HOUSELYFT.pdf` | John Arockiaraj | 303 Coxwell Ave, Toronto | Multiplex — **this is the master** |
| `Property_Report_258_Victoria_Cambridge.pdf` | Joe Darcy | 258 Victoria Ave, Cambridge ON | ADU / garden suite |
| `Property_Report_1361_Hastings_Saanich.pdf` | Shane Restall | 1361 Hastings St, Saanich BC | Multiplex (BC SSMUH) |
| `Property_Report_638_Broadway_Vancouver.pdf` | Rachel B | 638 E Broadway, Vancouver BC | Hotel — homeowner layout |
| `Property_Report_638_Broadway_Vancouver_COMMERCIAL.pdf` | Rachel B | 638 E Broadway, Vancouver BC | Hotel — **commercial variant (recommended)** |

`_superseded/` holds the pre-rebrand Briarstone draft. Kept for reference only — do not send.

**Coxwell is the master.** Every other report is this file with property, zoning, and
market data swapped in. The House Lyft prose (Why this report matters, How to use it,
the Advantage, Financing Pathways, Roadblocks, the $5,000 CTA) stays verbatim.

---

## 02_Templates_HTML — source templates

The HTML is the real template; the PDF is just its render. Images sit in this folder
because the HTML references them by relative path — keep them together or rendering breaks.

- `report_houselyft_master.html` — the master. Start here for any new lead.
- `_head.html` / `_body.html` — the master split into CSS/head and body, for rebuilds.
- `opt_a.png`, `opt_b.png`, `opt_c.png` — static architectural renderings (Development Options).
- `static_photo1.png`, `static_photo2.png` — static company photos (Advantage page).

Static images are client-supplied and appear on **every** report. The Property Details
aerial and street-view slots are still placeholders — those are generated per property.

---

## 03_Scripts

**Zoning engine**
- `property_lookup_v2.py` — nine GTA cities, one router. Toronto · Mississauga · Brampton ·
  Vaughan · Markham · Oakville · Richmond Hill · Burlington · Oshawa. Queries each city's
  own live GIS and returns its verified rulebook.
  ```
  python3 property_lookup_v2.py "2135 Caroline Street, Burlington, Ontario"
  ```
- `property_lookup.py` — the original Toronto-only version, wrapped by v2.

**Report generation**
- `render_*.py` — HTML → PDF via Playwright/Chromium.
- `xform_*.py` — transform scripts that turn the master into a city-specific report.
  Each asserts every replacement matches exactly once, then greps for leftovers from
  the source city. That check is what keeps Toronto data out of a Cambridge report.

---

## 04_Reference_Docs

Rulebook and role definitions from earlier in the build.

---

## Open items

1. **6+1 recommendation needs verification (Coxwell).** Secondary sources indicate Toronto
   does not permit a garden suite on a lot with five or six units. If correct, the master's
   primary recommendation — a sixplex *plus* a garden suite — is not a permitted configuration.
   Confirm against By-law 654-2025 before further use. 4+1 is unaffected.

2. **Terminology inconsistency.** Amaan's fix applied to the "What this means for you" list
   only, so the report says "Detached Houseplex" there and "Multiplex" in the option headings.
   Left as-is pending client comment.

3. **Placeholders remaining.** Real House Lyft logo file (currently a text wordmark) and the
   per-property aerial / street-view images.

4. **Commercial fee.** The commercial variant reads "Scoped per project" — no number was
   invented. Set by House Lyft.

5. **Localized incentives.** Out-of-market reports (Cambridge, Saanich, Vancouver) required
   their money sections rewritten — Toronto's HST and Bill 185 facts are simply wrong outside
   Toronto. This touches "locked" template wording and should be confirmed as policy.
