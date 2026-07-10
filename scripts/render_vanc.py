import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("file:///home/claude/report_vancouver_commercial.html", wait_until="networkidle")
        await page.wait_for_timeout(1200)  # let Google Fonts settle
        await page.pdf(
            path="/mnt/user-data/outputs/Property_Report_638_Broadway_Vancouver_COMMERCIAL.pdf",
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
        print("PDF written.")

asyncio.run(main())
