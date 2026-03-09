#!/usr/bin/env python3
"""
Inserts the final proposal additions into Dragonfruit_Proposal_EOY2026.html:
- TOC entries for proposing, quickwins, wishlist
- "What we're proposing" section
- "Quick wins" section
- "Complete wish list — all 16 tools" section
- Evaluation criteria one-liner in Section E
"""
import re

INPUT_FILE = "Dragonfruit_Proposal_EOY2026.html"
OUTPUT_FILE = "Dragonfruit_Proposal_EOY2026.html"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add TOC entries
toc_old = """        <li><a href="#solution">The solution in plain language</a></li>
        <li><a href="#A">A. System architecture &amp; vision</a></li>
        <li><a href="#B">B. AI toolkit per role</a></li>
        <li><a href="#C">C. Implementation roadmap</a></li>"""

toc_new = """        <li><a href="#proposing">What we're proposing (summary)</a></li>
        <li><a href="#solution">The solution in plain language</a></li>
        <li><a href="#A">A. System architecture &amp; vision</a></li>
        <li><a href="#B">B. AI toolkit per role</a></li>
        <li><a href="#quickwins">Quick wins (first 30–35 days)</a></li>
        <li><a href="#wishlist">Complete wish list — all 16 tools</a></li>
        <li><a href="#C">C. Implementation roadmap</a></li>"""

if toc_old in html:
    html = html.replace(toc_old, toc_new)
    print("Updated TOC.")
else:
    print("TOC block not found (may already be updated).")

# 2. Insert "What we're proposing" section after </nav>, before solution
proposing_block = """
    <h2 id="proposing">What we're proposing — full alignment to your brief</h2>
    <p>We propose a single, end-to-end solution that addresses <strong>everything</strong> in your AI Automation Enabled Pipeline &amp; System Architecture Brief: objective, quick wins, all 8 high-priority tools, all 8 medium-priority tools, architecture, roadmap, costs, and evaluation criteria.</p>

    <h3>Your objective (from your brief)</h3>
    <p><strong>Scale from 4 to 7 clients per pod by EOY 2026</strong> without proportional headcount increase — via workflow automation, agentic infrastructure, and the AI wish list toolkit. We deliver exactly that.</p>

    <h3>Quick wins (first 30–35 days)</h3>
    <ul>
      <li><strong>PR-3</strong> — Slack message templates &amp; automation (kickoffs, status, revisions, reminders; auto-fill client/project).</li>
      <li><strong>Make/Zapier</strong> — Expand ClickUp↔Slack so task create/update is one source of truth; fewer ad-hoc Slacks.</li>
      <li><strong>PR-1</strong> — Timeline calculator (content type, deliverables, complexity, turnaround → schedule + milestones).</li>
    </ul>
    <p>These deliver visible value in the first 30–35 days and set the foundation for Phase 2.</p>

    <h3>8 High-priority tools (we propose for all)</h3>
    <p>Your brief identifies 8 high-priority tools. We scope, cost, and phase every one:</p>
    <ul>
      <li><strong>CD-1</strong> Predictive Retention · <strong>CD-2</strong> Outlier Ideation · <strong>CD-3</strong> Packaging &amp; Thumbnail · <strong>CD-4</strong> A/B Test Monitor</li>
      <li><strong>ED-1</strong> Frame.io Sentiment · <strong>ED-2</strong> Automated QC · <strong>ED-3</strong> Capacity-Based Assignment</li>
      <li><strong>PR-4</strong> Claude-to-ClickUp Agent</li>
    </ul>
    <p>See <a href="#B">Section B</a> (AI toolkit per role), <a href="#C">Section C</a> (roadmap), and <a href="#appendix-cost">Appendix 1</a> (cost per tool).</p>

    <h3>8 Medium-priority tools (we propose for all)</h3>
    <p>Your wish list also includes 8 medium-priority tools. We include every one in scope, phase, and cost:</p>
    <ul>
      <li><strong>CD-5</strong> Packaging Scorer · <strong>CD-6</strong> Client Knowledge Bases · <strong>CD-7</strong> Script Voice Matching · <strong>CD-8</strong> Slack Scoring Bot · <strong>CD-9</strong> Outlier Aggregator</li>
      <li><strong>PR-1</strong> Timeline Calculator · <strong>PR-2</strong> Client Sentiment Tracker · <strong>PR-3</strong> Slack Templates</li>
    </ul>
    <p>All 16 tools are in the <a href="#wishlist">Complete wish list</a> table and <a href="#appendix-cost">Appendix 1</a>.</p>

    <h3>Brief requirements (A–D) and evaluation criteria</h3>
    <p>Your brief asks for: <strong>A</strong> System architecture with diagram; <strong>B</strong> AI toolkit per role (justification, cost, adoption); <strong>C</strong> Phased roadmap with buffers and KPIs; <strong>D</strong> Labour and system costs, engagement structure. Evaluation weights: Specificity 30%, Architecture 25%, Roadmap 20%, Cost 15%, Engagement 10%. This document addresses every requirement and each criterion explicitly — see <a href="#A">A</a>, <a href="#B">B</a>, <a href="#C">C</a>, <a href="#D">D</a>, and <a href="#E">E</a>.</p>

"""

if '<h2 id="solution">The solution in plain language</h2>' in html and 'id="proposing"' not in html:
    html = html.replace(
        '    </nav>\n\n    <h2 id="solution">The solution in plain language</h2>',
        '    </nav>\n' + proposing_block + '    <h2 id="solution">The solution in plain language</h2>'
    )
    print("Inserted 'What we're proposing' section.")
else:
    if 'id="proposing"' in html:
        print("'What we're proposing' already present.")
    else:
        print("Could not find insertion point for proposing section.")

# 3. Insert Quick wins + Complete wish list after B.3 (before C)
quickwins_wishlist_block = """
    <h2 id="quickwins">Quick wins (first 30–35 days)</h2>
    <p>Deliverables that go live in <strong>Phase 1</strong> (Days 1–35), as called out in your brief:</p>
    <ul>
      <li><strong>PR-3 — Slack message templates &amp; automation</strong> — Kickoffs, status, revisions, reminders; auto-fill client/project.</li>
      <li><strong>Make/Zapier — ClickUp↔Slack</strong> — One source of truth for task create/update; fewer ad-hoc Slacks.</li>
      <li><strong>PR-1 — Timeline calculator</strong> — Content type, deliverables, complexity, turnaround → schedule + milestones.</li>
    </ul>
    <p><strong>Success:</strong> Fewer ad-hoc Slacks; one source of truth for task created/updated. These set the foundation for Phase 2 (PR-4, ED-3, ED-1).</p>

    <h2 id="wishlist">Complete wish list — all 16 tools</h2>
    <p>We propose for <strong>every tool</strong> in your wish list. Below: priority, tool, role, phase, and where in this proposal it is addressed.</p>
    <table>
      <tr><th>Priority</th><th>Tool</th><th>Role</th><th>Phase</th><th>Where in this proposal</th></tr>
      <tr><td>High</td><td>CD-1 Predictive Retention</td><td>CD</td><td>3–4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>High</td><td>CD-2 Outlier Ideation</td><td>CD</td><td>4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>High</td><td>CD-3 Packaging &amp; Thumbnail</td><td>CD</td><td>4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>High</td><td>CD-4 A/B Test Monitor</td><td>CD</td><td>4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>High</td><td>ED-1 Frame.io Sentiment</td><td>PPM/Editor</td><td>2–3</td><td>B.2, Appendix 1</td></tr>
      <tr><td>High</td><td>ED-2 Automated QC</td><td>PPM</td><td>3</td><td>B.2, Appendix 1</td></tr>
      <tr><td>High</td><td>ED-3 Capacity Assignment</td><td>Producer/PC</td><td>2, roll 4</td><td>B.2, Appendix 1</td></tr>
      <tr><td>High</td><td>PR-4 Claude-to-ClickUp Agent</td><td>Producer</td><td>2, roll 4</td><td>B.3, Appendix 1</td></tr>
      <tr><td>Medium</td><td>CD-5 Packaging Scorer</td><td>CD</td><td>3</td><td>B.1, Appendix 1</td></tr>
      <tr><td>Medium</td><td>CD-6 Client Knowledge Bases</td><td>CD</td><td>3</td><td>B.1, Appendix 1</td></tr>
      <tr><td>Medium</td><td>CD-7 Script Voice Matching</td><td>CD</td><td>4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>Medium</td><td>CD-8 Slack Scoring Bot</td><td>CD</td><td>3–4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>Medium</td><td>CD-9 Outlier Aggregator</td><td>CD</td><td>4</td><td>B.1, Appendix 1</td></tr>
      <tr><td>Medium</td><td>PR-1 Timeline Calculator</td><td>Producer</td><td>1</td><td>B.3, Quick wins, Appendix 1</td></tr>
      <tr><td>Medium</td><td>PR-2 Client Sentiment Tracker</td><td>Producer</td><td>4</td><td>B.3, Appendix 1</td></tr>
      <tr><td>Medium</td><td>PR-3 Slack Templates</td><td>Producer/PC</td><td>1</td><td>B.3, Quick wins, Appendix 1</td></tr>
    </table>
    <p class="muted">Approach, phase, cost range, and maintenance for each tool are in Appendix 1; role-level justification is in Section B.</p>

    <div class="page-break"></div>

"""

# Insert before "<h2 id="C">C. Implementation roadmap</h2>"
if '<h2 id="C">C. Implementation roadmap</h2>' in html and 'id="quickwins"' not in html:
    html = html.replace(
        '    <div class="page-break"></div>\n\n    <h2 id="C">C. Implementation roadmap</h2>',
        '    <div class="page-break"></div>\n' + quickwins_wishlist_block + '    <h2 id="C">C. Implementation roadmap</h2>'
    )
    print("Inserted Quick wins and Complete wish list sections.")
else:
    if 'id="quickwins"' in html:
        print("Quick wins / wish list already present.")
    else:
        # Try alternate pattern (no page-break before C)
        if '    <h2 id="C">C. Implementation roadmap</h2>' in html:
            html = html.replace(
                '    <h2 id="C">C. Implementation roadmap</h2>',
                quickwins_wishlist_block + '    <h2 id="C">C. Implementation roadmap</h2>'
            )
            print("Inserted Quick wins and Complete wish list (no page-break).")

# 4. Add criteria one-liner at start of Section E
e_old = '    <h2 id="E">E. Evaluation criteria alignment</h2>\n    <p>We have structured this proposal to score <strong>maximally</strong> against each of your stated criteria. Below is an explicit mapping.</p>'
e_new = '    <h2 id="E">E. Evaluation criteria alignment</h2>\n    <p>Your brief specifies five criteria. This proposal addresses each one: <strong>Specificity ✓ · Architecture ✓ · Roadmap ✓ · Cost ✓ · Engagement ✓</strong>. Detail below.</p>\n    <p>We have structured this proposal to score <strong>maximally</strong> against each of your stated criteria. Below is an explicit mapping.</p>'

if e_old in html and 'Specificity ✓' not in html:
    html = html.replace(e_old, e_new)
    print("Added criteria one-liner in Section E.")
elif 'Specificity ✓' in html:
    print("Criteria one-liner already present.")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("Done. Updated", OUTPUT_FILE)
