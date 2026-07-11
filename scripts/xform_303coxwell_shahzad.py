"""
xform_303coxwell_shahzad.py — adapt the master for contact Anas Shahzad.

Special case: the lead's property (303 Coxwell Avenue, Toronto) is the SAME
property the master was built for. The zoning engine returns identical facts
(Ward 19 Beaches-East York, R (d1.0)(x7), 6 units as-of-right). So every
property / zoning / market / financing section stays verbatim — the only
adaptation is the LEAD IDENTITY (name, phone, email + the one first-name
prose reference). Same assert-once + leftover discipline as the city xforms.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "templates", "report_houselyft_master.html")
OUT = os.path.join(ROOT, "templates", "report_303coxwell_shahzad.html")

s = open(SRC).read()
R = []

# identity block — swap Name / Phone / Email only. Property Address and
# Development Goals are correct for this property, kept verbatim.
R.append(('''    <tr><td>Name</td><td>John Arockiaraj</td></tr>
    <tr><td>Phone Number</td><td>(647) 223-4342</td></tr>
    <tr><td>Email</td><td>johneeraj@gmail.com</td></tr>''',
'''    <tr><td>Name</td><td>Anas Shahzad</td></tr>
    <tr><td>Phone Number</td><td>+92 324 4004166</td></tr>
    <tr><td>Email</td><td>anasshahzad101@gmail.com</td></tr>'''))

# one first-name prose reference in the recommended-option narrative
R.append(("This matches John's stated goal.",
          "This matches Anas's stated goal."))

fails = 0
for old, new in R:
    c = s.count(old)
    if c != 1:
        print(f"[FAIL x{c}] {old[:65]!r}"); fails += 1
    else:
        s = s.replace(old, new)

open(OUT, "w").write(s)

# leftover check — the prior lead's identity must be fully gone. The property
# (Coxwell / Toronto / Ward 19) is correct here and legitimately remains.
for t in ["John Arockiaraj", "johneeraj", "John's", "(647) 223-4342",
          "John "]:
    n = s.count(t)
    if n:
        print(f"LEFTOVER '{t}': {n}")

print("wrote:", OUT)
print("done, fails:", fails)
