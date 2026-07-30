"""
render_london.py — render templates/report_london.html to PDF using the
exact run.py Playwright settings (Letter, print background, footer
disclaimer). The two aerials are committed PNGs in templates/, so this
render needs no network access.

Run:  python3 scripts/render_london.py [out.pdf]
Default output: outputs/Report_241_Admiral_Drive_London.pdf (gitignored).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, ROOT)

from run import render_pdf  # canonical Playwright settings

HTML = os.path.join(ROOT, "templates", "report_london.html")
DEFAULT_OUT = os.path.join(ROOT, "outputs", "Report_241_Admiral_Drive_London.pdf")


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT
    os.makedirs(os.path.dirname(out), exist_ok=True)
    render_pdf(HTML, out)
    size_mb = os.path.getsize(out) / 1_048_576
    print(f"Rendered {out} ({size_mb:.2f} MB)")


if __name__ == "__main__":
    main()
