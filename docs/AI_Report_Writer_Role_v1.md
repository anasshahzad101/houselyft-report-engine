# AI Report Writer — Role & Accuracy Contract (v1)
### How we let AI write the report without letting it break the accuracy moat

> **The core idea:** we don't make the AI accurate by asking nicely. We make it *structurally unable* to be wrong about facts. The AI is the **writer, not the surveyor** — it narrates a verified packet, it never measures anything.

---

## The three layers that guarantee accuracy

A prompt alone is not enough — language models are fluent and confident even when wrong. Accuracy comes from sandwiching the AI between two hard layers:

```
   1. GROUNDING (input)   →   2. ROLE (the prompt)   →   3. VALIDATION (output)
   only verified facts        narrate, never invent       every claim re-checked
   reach the AI               flag, never guess           against the packet
```

- **Layer 1 — Grounding:** the AI receives *only* the verified packet from `property_lookup.py` + the rulebook. It never sees a raw address to "figure out." It can't hallucinate a zoning code because it's handed the real one.
- **Layer 2 — Role:** the system prompt below forbids originating facts or numbers and dictates how to handle flagged fields.
- **Layer 3 — Validation:** after the AI writes, code checks every number and claim back against the packet. Anything that doesn't trace to a source field is flagged before the report can send. **This is the real guarantee** — the role reduces errors, validation catches the rest.

---

## Layer 1 — The grounding packet (what the AI receives)

Built by code from the lookup + rulebook. The AI gets this and nothing else. Every field is tagged.

```json
{
  "property": {
    "address": "303 Coxwell Avenue, Toronto",
    "ward": {"value": "Beaches-East York (19)", "tag": "VERIFIED"},
    "zone": {"value": "R (d1.0) (x7)", "tag": "VERIFIED", "source": "ZBL 569-2013 §900.2.10(7)"},
    "lot_area_sqm": {"value": null, "tag": "CONFIRM"},
    "year_built_band": {"value": "51-99 years", "tag": "CONFIRM"}
  },
  "permissions": {
    "gate_pass": {"value": true, "tag": "VERIFIED"},
    "sixplex_as_of_right": {"value": true, "tag": "VERIFIED"},
    "main_units_max": {"value": 6, "tag": "VERIFIED"},
    "parking_required": {"value": 0, "tag": "VERIFIED"}
  },
  "computed": {
    "max_footprint_sqm": {"value": null, "tag": "CONFIRM", "reason": "awaiting lot_area + coverage%"}
  },
  "programs": [
    {"name": "DC waiver (≤6 units)", "detail": "...", "tag": "VERIFIED", "source": "By-law 654-2025"}
  ],
  "education_notes": ["Rezoning not required — as-of-right.", "..."]
}
```

**The contract:** if a value is `null` or tagged `CONFIRM`, the AI must write the confirm-phrase — it may never fill it.

---

## Layer 2 — The AI role (system prompt — use verbatim)

```
You are the report-writing layer of [Company]'s property feasibility system.
You do NOT assess, measure, calculate, or decide anything. You receive a
VERIFIED FACTS packet and write clear, accurate, homeowner-facing report prose
from it — nothing more.

ABSOLUTE RULES — accuracy is non-negotiable:

1. SINGLE SOURCE OF TRUTH. Every factual statement you write must come from the
   FACTS packet. If a fact is not in the packet, you may not state it — not from
   general knowledge, not by inference, not as a "reasonable assumption."

2. NEVER ORIGINATE NUMBERS. Do not compute, estimate, round, or infer any number
   — units, dimensions, coverage, percentages, dollar figures, dates. Use packet
   numbers verbatim. If a number is not in the packet, write the confirm-phrase.

3. HONOR THE TAGS.
   - VERIFIED / COMPUTED  → state it plainly.
   - CONFIRM or null      → write "to be confirmed during the feasibility phase."
                            Never supply a value, even if you believe you know it.

4. FLAG, DON'T FILL. If a section's required facts are flagged or missing, write
   the honest short version. Never pad a gap with plausible-sounding detail.

5. COMPLIANCE LANGUAGE (mandatory):
   - Say "government-backed financing options," never "free grants" or "free money."
   - Any value, equity, or uplift figure is an "illustrative example," never a
     promise. Never state or imply a guaranteed return, approval, or outcome.
   - Never promise permits, financing eligibility, or timelines as certainties.

6. FORBIDDEN CONTENT. Never mention the federal "Canada Secondary Suite Loan
   Program" — it was not implemented. Never name any financing or grant program
   unless it appears in the packet with a source.

7. NO LEGAL OR PLANNING OPINIONS. This report is preliminary information, not
   advice. Keep the disclaimer framing where the template calls for it.

8. STAY IN YOUR LANE. Write prose for the provided section structure only. Do not
   invent sections, recommendations, or next steps beyond what the packet supplies.

STYLE: Plain language a homeowner understands. Benefit-led but honest — never
oversell. Short sentences. Warm, professional, calm.

OUTPUT: Return the report as structured sections matching the provided template
keys. For any required value tagged CONFIRM or null, use the confirm-phrase.

SELF-CHECK before returning: re-read every sentence. For each factual claim and
each number, name the packet field it came from. If you cannot, delete it or
replace it with the confirm-phrase. When in doubt, say less.
```

---

## Layer 3 — The validation pass (the real guarantee)

After the AI returns its draft, code runs this check *before* the report is allowed to render. The AI is trusted to write; it is not trusted to be the last word.

```python
def validate(draft_text, packet):
    issues = []

    # 1. Every number in the draft must exist in the packet's verified values.
    for num in extract_numbers(draft_text):
        if num not in packet_verified_numbers(packet):
            issues.append(("UNSOURCED NUMBER", num))

    # 2. No CONFIRM/null field may appear as a stated value.
    for field in packet_confirm_fields(packet):
        if value_stated_for(field, draft_text):
            issues.append(("STATED A CONFIRM FIELD", field))

    # 3. Banned content.
    for term in ["Canada Secondary Suite Loan", "free grant", "guaranteed return"]:
        if term.lower() in draft_text.lower():
            issues.append(("BANNED PHRASE", term))

    # 4. Every named program must carry a source from the packet.
    for prog in named_programs(draft_text):
        if not has_source(prog, packet):
            issues.append(("UNSOURCED PROGRAM", prog))

    return issues   # empty list = clears to render; otherwise → human review
```

**Result:** a fact the AI invents, a CONFIRM value it fills in, or a banned phrase it slips in **cannot reach the homeowner** — it's caught and routed to review. That is what makes "AI-written" and "accurate" compatible.

---

## Worked example — 303 Coxwell, packet → output

**Section 3 (Zoning), packet says** `sixplex_as_of_right: true [VERIFIED]`, `main_units_max: 6 [VERIFIED]`, `lot_area_sqm: null [CONFIRM]`:

> ✅ **Correct AI output:**
> "Your property is in Beaches-East York, one of the Toronto wards where up to six units are permitted as-of-right — no rezoning required. The exact buildable footprint depends on your lot's confirmed area, which we'll finalize during the feasibility phase."

> ❌ **What the layers prevent:**
> "Your 232 m² lot supports a six-unit build covering roughly 81 m²..." — *blocked:* `lot_area` and footprint are CONFIRM/null; the AI may not state them, and validation would catch the numbers anyway.

**Section 8 (Financing):**

> ✅ "Government-backed financing options may help fund the build, including development-charge relief for projects up to six units (City of Toronto, By-law 654-2025)."
> ❌ "You'll get free government grants and an $80,000 secondary-suite loan." — *blocked* by rules 5 and 6, and by validation.

---

## How this plugs in

```
address → property_lookup.py → build_packet(lookup + rulebook) → AI writer (this role)
        → validate(draft, packet) → [pass] render PDF  /  [fail] human review queue
```

That's the full **address-in → accurate-report-out** loop, with the AI doing the writing and the system guaranteeing the facts.
