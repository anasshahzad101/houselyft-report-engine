"""Entrypoint for the report automation. The Claude routine runs this.

Usage:
    python src/run_report.py --contact-id <GHL contact id>

Flow:
    1. Fetch the contact from GHL
    2. Guard: contact must have an opportunity in the configured pipeline
       (Lock 2 — stray webhooks pointed at this routine get rejected)
    3. Guard: contact must have a usable property address
    4. Engine: address -> feasibility PDF        (port pending, see engine/)
    5. Upload PDF to the Feasibility Report field, add a note

Guards fail loudly: a skipped lead gets a note on their GHL record
explaining why, so nothing dies silently.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from ghl_client import GHLClient

ROOT = pathlib.Path(__file__).resolve().parent.parent
CONFIG = json.loads((ROOT / "config" / "ghl.json").read_text())


def build_address(contact: dict) -> str | None:
    parts = [contact.get("address1"), contact.get("city"),
             contact.get("state"), contact.get("postalCode")]
    if not contact.get("address1") or not contact.get("city"):
        return None
    return ", ".join(p for p in parts if p)


def generate_report(address: str, contact: dict) -> str:
    """Engine hook. Returns path to the finished PDF.

    The zoning engine, imagery module and template system get ported
    into engine/ — until then this raises so the gap is unmissable.
    """
    raise NotImplementedError(
        "Report engine not ported yet — see engine/README.md"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--contact-id", required=True)
    args = ap.parse_args()

    ghl = GHLClient(location_id=CONFIG["location_id"])
    contact = ghl.get_contact(args.contact_id)
    name = f"{contact.get('firstName', '')} {contact.get('lastName', '')}".strip()

    # Lock 2 — pipeline guard
    opps = ghl.get_opportunities(args.contact_id)
    in_pipeline = [o for o in opps if o.get("pipelineId") == CONFIG["pipeline_id"]]
    if not in_pipeline:
        print(f"SKIP {name}: no opportunity in {CONFIG['pipeline_name']}")
        return 0

    # Address guard
    address = build_address(contact)
    if not address:
        ghl.add_note(
            args.contact_id,
            "Automated report skipped: no property address on this contact. "
            "Fill the built-in address fields and re-trigger.",
        )
        print(f"SKIP {name}: no address — flagged with a note")
        return 0

    print(f"RUN {name}: {address}")
    pdf_path = generate_report(address, contact)

    ghl.upload_report(args.contact_id, CONFIG["fields"]["feasibility_report"], pdf_path)
    ghl.add_note(args.contact_id, f"Feasibility report generated and attached ({address}).")
    print(f"DONE {name}: report attached")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
