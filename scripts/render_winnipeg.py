"""Render report_winnipeg.html -> PDF with run.py's exact Playwright settings,
then apply the QUALITY GUARD (>= 1.5 MB and >= 13 pages)."""
import asyncio, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "templates", "report_winnipeg.html")
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "Property_Report_201_Margaret_Winnipeg-AI-DRAFT.pdf")

FOOTER = ("<div style='width:100%; font-family:Arial,sans-serif; font-size:6.4pt;"
          " color:#aeb6c4; padding:0 16mm; text-align:center;'>"
          "Preliminary analysis only. This report is not a planning opinion, legal advice, or development permit. "
          "Verify all information before making any investment decision.</div>")


async def _go():
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file://" + os.path.abspath(HTML), wait_until="networkidle")
        await page.wait_for_timeout(1200)
        await page.pdf(path=OUT, format="Letter", print_background=True,
                       display_header_footer=True, header_template="<div></div>",
                       footer_template=FOOTER,
                       margin={"top": "15mm", "bottom": "14mm", "left": "15mm", "right": "15mm"})
        await browser.close()


def page_count(pdf_path):
    with open(pdf_path, "rb") as fh:
        data = fh.read()
    # count /Type /Page (not /Pages) objects
    import re
    return len(re.findall(rb"/Type\s*/Page[^s]", data))


if __name__ == "__main__":
    asyncio.run(_go())
    size = os.path.getsize(OUT)
    pages = page_count(OUT)
    mb = size / (1024 * 1024)
    print(f"OUT: {OUT}")
    print(f"SIZE: {mb:.2f} MB ({size} bytes)")
    print(f"PAGES: {pages}")
    degraded = (size < 1.5 * 1024 * 1024) or (pages < 13)
    print("QUALITY_GUARD:", "DEGRADED" if degraded else "OK")
