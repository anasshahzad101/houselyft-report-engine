"""GoHighLevel API client for the House Lyft report automation.

Every call in this module was proven against the live sub-account on
2026-07-10 (except move_stage — see its docstring). Auth comes from the
environment; nothing secret lives in the repo.
"""
from __future__ import annotations

import os
import uuid
import requests

BASE = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"


class GHLClient:
    def __init__(self, token: str | None = None, location_id: str | None = None):
        self.token = token or os.environ["GHL_TOKEN"]
        self.location = location_id or os.environ["GHL_LOCATION"]
        self.s = requests.Session()
        self.s.headers.update(
            {
                "Authorization": f"Bearer {self.token}",
                "Version": API_VERSION,
                "Accept": "application/json",
            }
        )

    # ------------------------------------------------------------------ reads

    def get_contact(self, contact_id: str) -> dict:
        r = self.s.get(f"{BASE}/contacts/{contact_id}")
        r.raise_for_status()
        return r.json()["contact"]

    def search_contacts(self, query: str) -> list[dict]:
        r = self.s.get(
            f"{BASE}/contacts/",
            params={"locationId": self.location, "query": query},
        )
        r.raise_for_status()
        return r.json().get("contacts", [])

    def get_opportunities(self, contact_id: str) -> list[dict]:
        r = self.s.get(
            f"{BASE}/opportunities/search",
            params={"location_id": self.location, "contact_id": contact_id},
        )
        r.raise_for_status()
        return r.json().get("opportunities", [])

    # ----------------------------------------------------------------- writes

    def upload_report(self, contact_id: str, field_id: str, pdf_path: str) -> dict:
        """Upload a PDF into a file-type custom field on the contact.

        Proven 2026-07-10: multipart key must be '<field_id>_<unique_id>'.
        API limit is 50 MB per file.
        """
        key = f"{field_id}_{uuid.uuid4().hex[:12]}"
        with open(pdf_path, "rb") as fh:
            r = self.s.post(
                f"{BASE}/forms/upload-custom-files",
                params={"contactId": contact_id, "locationId": self.location},
                files={key: (os.path.basename(pdf_path), fh, "application/pdf")},
            )
        r.raise_for_status()
        return r.json()

    def add_note(self, contact_id: str, body: str) -> dict:
        r = self.s.post(
            f"{BASE}/contacts/{contact_id}/notes",
            json={"body": body},
        )
        r.raise_for_status()
        return r.json()

    def move_stage(self, opportunity_id: str, stage_id: str) -> dict:
        """Move an opportunity to a new stage within its pipeline.

        NOT yet exercised against the live account — verify on first use
        during routine wiring before trusting in production.
        """
        r = self.s.put(
            f"{BASE}/opportunities/{opportunity_id}",
            json={"pipelineStageId": stage_id},
        )
        r.raise_for_status()
        return r.json()
