s = open("report_vancouver_commercial.html").read()
R = []

# --- WHY (commercial) ---
R.append(('''  <p>According to Federal Data, Canadian property owners are currently sitting on an unprecedented $5.22 Trillion in untapped real estate equity.</p>
  <p>It is the largest concentrated pile of unused wealth in our country's history!</p>
  <p>The information inside this report has been compiled to give you a data-backed opinion on the development viability of your property before you expose your hard-earned capital to risk.</p>
  <p>It is designed to help you identify opportunities, unlock trapped equity, generate cashflow, and build wealth by optimizing your property's usage and potential.</p>
  <p>This Initial Report:</p>
  <ul>
    <li><strong>Examines Your Local Zoning Bylaw:</strong> Find out what your lot bylaws legally allow you to build.</li>
    <li><strong>Identifies Government Grants and Subsidies:</strong> Map out your property against active municipal, provincial, and federal grant programs.</li>
    <li><strong>Highlights Specialized Financing Frameworks:</strong> Show you possible ways to structure your project's economics to qualify for low-interest, government-backed financing, whenever possible.</li>
  </ul>
  <p>This is the first part of a multi-step plan to help you transform your property and reach your development goals.</p>''',
'''  <p>A commercial development lives or dies on the numbers — and the numbers turn on entitlement, program, and cost certainty long before a shovel hits the ground.</p>
  <p>This report is a data-backed read on the development viability of your site, compiled so you can pressure-test the opportunity before committing capital to detailed design and construction.</p>
  <p>This Initial Report:</p>
  <ul>
    <li><strong>Confirms Your Zoning &amp; Entitlement:</strong> the use, density, and height the site supports — and where the approval currently stands.</li>
    <li><strong>Frames the Buildable Envelope:</strong> what the FSR and height translate to in floor area, and the program options that fit it.</li>
    <li><strong>Maps the Cost &amp; Financing Picture:</strong> the levies, contributions, and financing structure that decide whether the pro forma clears.</li>
  </ul>
  <p>This is the first step in a coordinated path from an approved site to a finished, operating asset.</p>'''))

# --- HOW TO USE (commercial) ---
R.append(('''  <p>Think of this report as a high-level zoning compass. It tells you what the current regulations allow you to build on your property and the possible ways you can use that to your advantage.</p>
  <p>It's the first step in a process that takes your property from its current state to maximizing its full potential.</p>''',
'''  <p>Think of this report as a high-level entitlement and feasibility compass. It confirms what the site is approved to support and frames the program options that fit the envelope.</p>
  <p>It's the first step in a process that takes an approved site through to a finished, operating asset.</p>'''))
R.append(('''      <ul><li>What you're allowed to build under current zoning</li><li>Grants &amp; incentives that may be available</li><li>Financing options available</li></ul></div>
    <div class="step"><div class="sh"><span class="n">STEP 2</span><span class="t">BUILDER READY PACKAGE™</span></div>
      <ul><li>Design Feasibility Report</li><li>Financial Feasibility Report</li><li>Grants &amp; Incentives Report</li></ul></div>
    <div class="step"><div class="sh"><span class="n">STEP 3</span><span class="t">BUILDER MATCHING™</span></div>
      <ul><li>Matched with a trusted Builder Partner suited to your project &amp; market</li><li>They lead detailed design &amp; permitting</li><li>Through construction &amp; final occupancy</li></ul></div>''',
'''      <ul><li>Zoning &amp; entitlement status</li><li>Buildable envelope (FSR, height, program)</li><li>Cost &amp; financing framework</li></ul></div>
    <div class="step"><div class="sh"><span class="n">STEP 2</span><span class="t">BUILDER READY PACKAGE™</span></div>
      <ul><li>Design Feasibility (massing, key/unit count)</li><li>Financial Feasibility (development pro forma)</li><li>Entitlement &amp; Cost Report (levies, linkage, permit path)</li></ul></div>
    <div class="step"><div class="sh"><span class="n">STEP 3</span><span class="t">BUILDER MATCHING™</span></div>
      <ul><li>Matched with a vetted commercial general contractor</li><li>For a hotel, an operator / flag partner</li><li>They lead design, permitting, construction &amp; opening</li></ul></div>'''))
R.append(('''  <p>Once your Builder Ready Package™ is complete, we will match you with one of our trusted Builder Partners who is best suited for your project and market. Your builder will then lead the project through detailed design, permitting, construction, and final occupancy.</p>''',
'''  <p>Once your Builder Ready Package™ is complete, we match you with vetted commercial partners — a general contractor, and for a hotel an operator or flag — best suited to your project and market. They lead the project through detailed design, permitting, construction, and opening.</p>'''))

# --- ADVANTAGE blurb (commercial) ---
R.append(('''  <p>House Lyft helps Canadian homeowners unlock the equity trapped in their property and turn it into lasting income — without navigating the development maze alone.</p>
  <p>We are the orchestrator of one coordinated path. We confirm what your property can become, build your <strong>Builder Ready Package™</strong> — the design, financial, and incentive feasibility that turns an idea into an executable plan — and then match you with one of our trusted, vetted <strong>Builder Partners</strong>, who leads detailed design, permitting, and construction through to completion.</p>
  <p>Instead of stitching together a dozen disconnected vendors — surveyors, designers, brokers, planners, builders — each with their own timeline and their own bill, you get a single guided route from "what can I build?" to keys in hand. One relationship, one plan, one team accountable for getting you there.</p>''',
'''  <p>House Lyft coordinates development from an approved site to a finished, operating asset — without the owner having to assemble and manage a dozen disconnected consultants.</p>
  <p>We confirm what the site supports, build your <strong>Builder Ready Package™</strong> — the design, financial, and entitlement feasibility that turns an approval into an executable plan — and then match you with vetted commercial partners (a general contractor, and for a hotel an operator or flag) who lead detailed design, permitting, and construction through to opening.</p>
  <p>Instead of stitching together surveyors, architects, cost consultants, lenders, and contractors — each with their own timeline and their own bill — you get a single coordinated path and one accountable team.</p>'''))

# --- FINANCING (commercial) ---
R.append(('''  <p>How you finance the development of your property can significantly impact your overall ROI, as well as your cashflow and stability.</p>
  <p>Many property owners destroy their project margins by trying to use expensive personal cash lines or basic retail bank loans.</p>
  <p>A successful project requires institutional underwriting before you ever pull a permit. We partner with national commercial lending desks to bypass conventional retail hurdles, allowing our qualified files to access specialized programs, rates, and terms completely unavailable to the general public.</p>
  <table class="kv">
    <tr><td>Mortgage Refinance</td><td>If a property has appreciated in value or the mortgage has been significantly paid down, owners can typically access up to 80% of the property's newly appraised value.</td></tr>
    <tr><td>Home Equity Line of Credit (HELOC)</td><td>Is a flexible, revolving line of credit secured against the equity of an existing property. Unlike a refinance that issues a lump sum, a HELOC functions more like a high-limit credit card tied to your real estate.</td></tr>
    <tr><td>Construction Financing</td><td>Also known as a progress-draw mortgage, construction financing is a short-term loan specifically designed to fund a new build from the ground up (or fund a massive structural overhaul).</td></tr>
    <tr><td>CMHC MLI-Select</td><td>Government-backed multi-unit mortgage insurance. Requires a minimum of 5 rental units. Does not act as a direct grant, but heavily subsidizes project costs. It cuts insurance premiums by up to 30% and extends amortizations to 50 years based on a point system rewarding affordability, energy efficiency, and accessibility.</td></tr>
  </table>''',
'''  <p>How a commercial project is capitalized drives its returns, its risk, and whether it can be built at all.</p>
  <p>Commercial development is financed differently from a home — through a stack of senior construction debt, mezzanine, and equity, replaced by long-term financing once the asset is operating. Lining this up early, before detailed design locks, is what de-risks the project.</p>
  <p>We work with commercial lending and capital partners to structure the stack appropriately for the program you choose.</p>
  <table class="kv">
    <tr><td>Commercial Construction Financing</td><td>A project-specific construction loan (typically a share of total loan-to-cost) released on progress draws to fund the build. Underwriting hinges on the pro forma, sponsor strength, and the entitlement being in hand.</td></tr>
    <tr><td>Take-Out / Term Financing</td><td>Long-term commercial financing that replaces the construction loan once the asset is complete and stabilized — for a hotel, once it is operating and generating revenue.</td></tr>
    <tr><td>Mezzanine &amp; Equity</td><td>Gap financing and equity partners that top up the capital stack above senior debt where construction costs exceed conventional loan-to-cost limits.</td></tr>
    <tr><td>Hotel Flag / Franchise Support</td><td>A recognized hotel brand can improve lender terms and, in some cases, contribute key money or financing support (hotel scenario only).</td></tr>
    <tr><td>Residential-Only: CMHC MLI Select</td><td>Applies <strong>only</strong> to the ~16-unit residential alternative — government-backed multi-unit insurance (5+ rental units) that heavily subsidizes cost. A hotel cannot use it; a key input to the hotel-vs-residential comparison.</td></tr>
  </table>'''))

# --- NEXT STEPS intro + step headers (commercial) ---
R.append(('''  <h3>Step 1: Zoning — Development Rights and Requirements</h3>
  <p>In order to ensure that your project plans meet local setbacks, site coverage caps, and height restrictions, you will need the following:</p>
  <ul><li>Site Plan</li><li>Massing Diagram Options</li><li>Unit Mix, Unit Count and Unit Sizes</li></ul>
  <h3>Step 2: Grants &amp; Incentives</h3>
  <p>While your project may be eligible for various government rebates and incentives, most programs require documentation that is generated throughout the development and construction process. Applications are generally completed once all required information has been collected.</p>
  <p>In order to start the application process you will need a detailed breakdown of the necessary documentation and supporting forms required for each program.</p>''',
'''  <h3>Step 1: Entitlement &amp; Design — Rights and Envelope</h3>
  <p>To confirm the program fits the approval and the site's setbacks, coverage, and height, you will need:</p>
  <ul><li>Site Plan &amp; survey</li><li>Massing / program options (hotel vs. residential)</li><li>Key or unit count, mix, and sizes</li></ul>
  <h3>Step 2: Cost &amp; Contributions</h3>
  <p>Commercial projects carry Development Cost Levies and a Broadway Plan linkage / amenity contribution. These are project costs that must be quantified and built into the pro forma, alongside servicing and demolition of the existing vacant building.</p>
  <p>You will need a detailed breakdown of the applicable levies, contributions, and permit-path requirements to complete the financial picture.</p>'''))

# --- ROADBLOCKS advantage + CTA (commercial) ---
R.append(('''  <p>We designed our Phase 2 where over the next 30 days, our lending partners, planning and grants and incentives consultants will compile everything simultaneously into a single next step option for you. This gives you everything required to accurately plan and build your roadmap.</p>
  <p>In addition, if you decide to move forward with the project and use one of our approved and vetted builder partners, they will credit you the full cost of your Phase 2 work right back to your construction balance on Day 1.</p>
  <div class="cta">
    Your total investment for the Phase 2 blueprint is a single flat fee of<br><span class="fee">$5,000.00</span>
    <div style="margin-top:10px;font-size:8.8pt;">Getting started is simple:</div>
    <ol style="margin:6px 0 0;font-size:8.8pt;padding-left:18px;">
      <li><strong>Authorize the Phase 2 Work Order:</strong> Review and sign our Builder Ready Package Agreement.</li>
      <li><strong>Submit the Phase 2 Payment:</strong> to activate our trusted team of consultants.</li>
      <li><strong>Submit the Financial Intake Forms:</strong> as provided by our lender partner.</li>
      <li><strong>Book Your Initial Planning Session:</strong> set up your initial meeting with our planner and Senior Relationship Manager to finalize your development objectives and plan next steps.</li>
    </ol>
  </div>''',
'''  <p>Our Phase 2 compiles the design, financial, and entitlement work simultaneously — architect, cost consultant, and capital partner working in parallel — into a single executable plan, rather than the piecemeal, sequential approach that stalls most projects.</p>
  <p>In addition, if you proceed with one of our vetted commercial partners, the cost of your Phase 2 work is credited back against the project on Day 1.</p>
  <div class="cta">
    Your Builder Ready Package™ for a commercial project of this scale is<br><span class="fee">Scoped per project</span>
    <div style="margin-top:10px;font-size:8.8pt;">A commercial feasibility engagement is quoted to the program — not a flat homeowner fee. Getting started:</div>
    <ol style="margin:6px 0 0;font-size:8.8pt;padding-left:18px;">
      <li><strong>Confirm Scope:</strong> we align on the hotel and residential-comparison program to be tested.</li>
      <li><strong>Authorize the Builder Ready Package™:</strong> review and sign the engagement for your project.</li>
      <li><strong>Submit Project &amp; Financial Intake:</strong> so the design, cost, and capital work can begin in parallel.</li>
      <li><strong>Book Your Kickoff Session:</strong> with our planner and Senior Relationship Manager to finalize objectives and next steps.</li>
    </ol>
  </div>'''))

fails=0
for old,new in R:
    c=s.count(old)
    if c!=1:
        print(f"[FAIL x{c}] {old[:55]!r}"); fails+=1
    else:
        s=s.replace(old,new)
open("report_vancouver_commercial.html","w").write(s)
for t in ["5.22 Trillion","homeowner","HELOC","5,000.00","Garden Suite","keys in hand"]:
    n=s.count(t)
    if n: print(f"LEFTOVER '{t}': {n}")
print("done, fails:",fails)
