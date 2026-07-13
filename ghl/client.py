"""
ghl/client.py — GoHighLevel API client for the House Lyft report loop.

Every call pattern here was proven live against the production sub-account
on 2026-07-10 (token scopes, contact lookup, file upload to the Feasibility
Report field, notes, opportunity search). Auth comes from the environment:

    GHL_TOKEN         Private Integration token (pit-...)
    GHL_LOCATION_ID   Sub-account location id

Locked pipeline configuration (IDs pulled via API, 2026-07-10):
    Dev Pipeline -> Intro Booked is the trigger stage for report generation.
"""
import os
import uuid

import requests

BASE = "https://services.leadconnectorhq.com"
API_VERSION = "2021-07-28"

# ---- locked configuration (identifiers, not secrets) ------------------------
PIPELINE_ID      = "4YhS7zSRYXpYIxScGW3J"                    # Dev Pipeline
TRIGGER_STAGE_ID = "0a4dcc80-4997-4265-993c-c2ec2310c566"    # Intro Booked
REPORT_FIELD_ID  = "7JFKnnjOjyrKXxGY2Pdh"                    # Feasibility Report (FILE_UPLOAD)

# Confidence tags — GHL workflows key off these, no extra fields needed.
TAG_READY  = "report-ready"           # verified-city rules
TAG_REVIEW = "report-needs-review"    # new city, rules researched live


def _auth():
    return os.environ["GHL_TOKEN"], os.environ["GHL_LOCATION_ID"]


def _headers():
    tok, _ = _auth()
    return {"Authorization": f"Bearer {tok}",
            "Version": API_VERSION, "Accept": "application/json"}


def _get(path, **params):
    r = requests.get(BASE + path, headers=_headers(), params=params, timeout=45)
    r.raise_for_status()
    return r.json()


def _send(method, path, payload):
    r = requests.request(method, BASE + path,
                         headers={**_headers(), "Content-Type": "application/json"},
                         json=payload, timeout=45)
    r.raise_for_status()
    return r.json() if r.text else {}


# ---- contacts ----------------------------------------------------------------

def find_contacts(query, limit=5):
    _, loc = _auth()
    return _get("/contacts/", locationId=loc, query=query, limit=limit).get("contacts", [])


def get_contact(contact_id):
    return _get(f"/contacts/{contact_id}").get("contact", {})


def contact_address(contact):
    """Assemble the property address from the built-in fields the funnel fills.
    Returns None when there isn't enough to geocode — caller must handle."""
    if not (contact.get("address1") and contact.get("city")):
        return None
    parts = [contact.get("address1"), contact.get("city"),
             contact.get("state"), contact.get("postalCode")]
    return ", ".join(p for p in parts if p)


def add_note(contact_id, body):
    return _send("POST", f"/contacts/{contact_id}/notes", {"body": body})


def add_tags(contact_id, tags):
    return _send("POST", f"/contacts/{contact_id}/tags", {"tags": list(tags)})


def remove_tags(contact_id, tags):
    r = requests.delete(f"{BASE}/contacts/{contact_id}/tags",
                        headers={**_headers(), "Content-Type": "application/json"},
                        json={"tags": list(tags)}, timeout=45)
    r.raise_for_status()
    return r.json() if r.text else {}


# ---- opportunities -------------------------------------------------------------

def opportunities_for(contact_id):
    _, loc = _auth()
    return _get("/opportunities/search",
                location_id=loc, contact_id=contact_id).get("opportunities", [])


def in_trigger_stage(opp):
    return (opp.get("pipelineId") == PIPELINE_ID
            and opp.get("pipelineStageId") == TRIGGER_STAGE_ID)


def update_opportunity(opportunity_id, payload):
    return _send("PUT", f"/opportunities/{opportunity_id}", payload)


def move_stage(opportunity_id, stage_id):
    return update_opportunity(opportunity_id, {"pipelineStageId": stage_id})


# ---- the proven file upload -----------------------------------------------------

def upload_report(contact_id, pdf_path, field_id=REPORT_FIELD_ID):
    """Attach a PDF to the contact's Feasibility Report custom field.
    Multipart key format {fieldId}_{uid} — proven live (HTTP 201)."""
    _, loc = _auth()
    key = f"{field_id}_{uuid.uuid4().hex[:10]}"
    with open(pdf_path, "rb") as fh:
        r = requests.post(f"{BASE}/forms/upload-custom-files",
                          headers=_headers(),
                          params={"contactId": contact_id, "locationId": loc},
                          files={key: (os.path.basename(pdf_path), fh, "application/pdf")},
                          timeout=120)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    # Read-only smoke: token works, test contact reachable, opportunity visible.
    cs = find_contacts("Shahzad")
    print("contacts:", [(c["id"], c.get("email")) for c in cs])
    if cs:
        c = get_contact(cs[0]["id"])
        print("address:", contact_address(c))
        for o in opportunities_for(cs[0]["id"]):
            print("opp:", o["id"], "trigger-stage:", in_trigger_stage(o))


# ---- text custom field writer (for the Feasibility Report Link) ----------------

FOLDER_LINK_FIELD_ID = "eUGAPkugk1U4FHNJDP9Q"

def set_text_field(contact_id, value, field_id=FOLDER_LINK_FIELD_ID):
    """Write a plain text/URL value into a contact custom field.
    Used to store the Drive folder link (link-only model - no PDF in GHL)."""
    return _send("PUT", f"/contacts/{contact_id}",
                 {"customFields": [{"id": field_id, "value": value}]})
