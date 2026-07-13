"""
run.py — House Lyft report loop orchestrator.

    contact (id or search query)
      -> pull contact + property address from GHL      (ghl/client.py)
      -> zoning lookup                                  (engine/)
      -> render the report PDF                          (templates/ via Playwright)
      -> upload to the contact's Feasibility Report field
      -> note + confidence tag (+ optional stage move)

The deterministic rails live here. Per-lead report CONTENT adaptation is the
routine's job, guided by docs/AI_Report_Writer_Role_v1.md and the xform
pattern in scripts/ — this module renders whichever HTML it is pointed at.
"""
import asyncio
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ROOT, "engine"))
sys.path.insert(0, ROOT)

from ghl import client
from property_lookup_v2 import lookup

VERIFIED_NOTE = "Report ready. Zoning rules verified for this municipality — present with confidence."
REVIEW_NOTE = ("Report ready. Rules for this municipality were researched live — "
               "double-check zoning and incentive figures before the call.")


def render_pdf(html_path, out_pdf):
    from playwright.async_api import async_playwright

    async def _go():
        async with async_playwright() as p:
            browser = await p.chromium.launch()
            page = await browser.new_page()
            await page.goto("file://" + os.path.abspath(html_path), wait_until="networkidle")
            await page.wait_for_timeout(1200)
            await page.pdf(path=out_pdf, format="Letter", print_background=True,
                           display_header_footer=True, header_template="<div></div>",
                           footer_template=("<div style='width:100%; font-family:Arial,sans-serif; "
                                            "font-size:6.4pt; color:#aeb6c4; padding:0 16mm; text-align:center;'>"
                                            "Preliminary analysis only. This report is not a planning opinion, "
                                            "legal advice, or development permit. Verify all information before "
                                            "making any investment decision.</div>"),
                           margin={"top": "15mm", "bottom": "14mm", "left": "15mm", "right": "15mm"})
            await browser.close()

    asyncio.run(_go())
    return out_pdf


def process_contact(contact_id, html_path, pdf_name, move_to_stage=None):
    contact = client.get_contact(contact_id)
    addr = client.contact_address(contact)
    if not addr:
        client.add_note(contact_id, "Report automation: no property address on this contact — skipped.")
        return {"status": "skipped", "reason": "no address"}

    z = lookup(addr)
    eng = z.get("engine", {}) or {}
    zone_found = bool((z.get("zoning") or {}).get("zone"))
    verified = zone_found and "No adapter" not in str(eng.get("note", ""))

    out_pdf = os.path.join(ROOT, pdf_name)
    render_pdf(html_path, out_pdf)
    up = client.upload_report(contact_id, out_pdf)

    summary = (f"{VERIFIED_NOTE if verified else REVIEW_NOTE}\n"
               f"Address: {addr}\nCity: {z.get('city')}  |  "
               f"Zone: {(z.get('zoning') or {}).get('zone')}  |  "
               f"Max units (as-of-right): {eng.get('main_units_max')}\n"
               f"Source: {z.get('source', 'n/a')}")
    client.add_note(contact_id, summary)
    client.add_tags(contact_id, [client.TAG_READY if verified else client.TAG_REVIEW])

    if move_to_stage:
        for opp in client.opportunities_for(contact_id):
            if client.in_trigger_stage(opp):
                client.move_stage(opp["id"], move_to_stage)

    return {"status": "done", "verified": verified, "city": z.get("city"),
            "uploaded": bool(up.get("succeeded") or up.get("succeded"))}


if __name__ == "__main__":
    cid = sys.argv[1] if len(sys.argv) > 1 else None
    html = sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, "templates/report_houselyft_master.html")
    name = sys.argv[3] if len(sys.argv) > 3 else "Property_Report.pdf"
    print(process_contact(cid, html, name))
