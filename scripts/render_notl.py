"""render_notl.py — render the Niagara-on-the-Lake (Virgil) report to PDF.

Mirrors run.py's Playwright settings (Letter, print background, footer
disclaimer, brand margins). Niagara-on-the-Lake has no zoning-engine adapter,
so this report was researched live per THE PRIME RULE and carries the
report-needs-review confidence tag. Point Playwright at the repo template so the
vendored fonts and static images resolve by relative path.
"""
import asyncio
import os

from playwright.async_api import async_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML = os.path.join(ROOT, "templates", "report_notl.html")
OUT = os.path.join(ROOT, "Property_Report_1065_Concession3_NOTL-AI-DRAFT.pdf")


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file://" + HTML, wait_until="networkidle")
        await page.wait_for_timeout(1200)
        await page.pdf(
            path=OUT,
            format="Letter",
            print_background=True,
            display_header_footer=True,
            header_template="<div></div>",
            footer_template=(
                "<div style='width:100%; font-family:Arial,sans-serif; font-size:6.4pt;"
                " color:#aeb6c4; padding:0 16mm; text-align:center;'>"
                "Preliminary analysis only. This report is not a planning opinion, legal advice, or development permit. "
                "Verify all information before making any investment decision."
                "</div>"
            ),
            margin={"top": "15mm", "bottom": "14mm", "left": "15mm", "right": "15mm"},
        )
        await browser.close()
        print("PDF written ->", OUT)


asyncio.run(main())
