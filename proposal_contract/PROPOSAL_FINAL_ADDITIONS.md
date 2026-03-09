# Final Proposal — Add These Sections (Brief Alignment)

Use this to make the proposal **explicitly** cover every requested item from the **Dragonfruit AI Automation Enabled Pipeline & System Architecture Brief** (slides 1–8): objective, quick wins, all 8 high-priority tools, all 8 medium-priority tools, requirements A–D, and evaluation criteria.

**Canonical references (already in proposal):** Section A.4 now links to [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro) and [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/), and references the **pipeline_demo/** folder (Batch 2–6 architecture, role playbooks, tool integration map, impact analysis, roadmap) as the supporting architecture source of truth.

---

## 1. Add to Table of Contents (after "The solution in plain language")

- What we're proposing (summary)
- Quick wins (first 30–35 days)
- Complete wish list — all 16 tools

---

## 2. New section: "What we're proposing — full alignment to your brief"

**Insert after the TOC, before "The solution in plain language".**

- **Your objective:** Scale 4 → 7 clients per pod by EOY 2026 without proportional headcount (workflow automation + agentic infrastructure + AI wish list toolkit). We deliver exactly that.
- **Quick wins (first 30–35 days):** PR-3 (Slack templates), Make/Zapier (ClickUp↔Slack), PR-1 (timeline calculator). Visible value and foundation for Phase 2.
- **8 High-priority tools — we propose for all:** CD-1, CD-2, CD-3, CD-4, ED-1, ED-2, ED-3, PR-4. All in Section B, roadmap (C), and Appendix 1.
- **8 Medium-priority tools — we propose for all:** CD-5, CD-6, CD-7, CD-8, CD-9, PR-1, PR-2, PR-3. All in scope, phased, and costed in Appendix 1.
- **Brief requirements (A–D):** A = architecture + diagram; B = AI toolkit (justification, cost, adoption); C = phased roadmap, buffers, KPIs; D = labour, system costs, engagement. All in sections A–D.
- **Evaluation criteria:** Specificity 30%, Architecture 25%, Roadmap 20%, Cost 15%, Engagement 10%. All addressed in Section E.

---

## 3. New section: "Quick wins (first 30–35 days)"

**Insert after Section B (AI toolkit), before Section C (roadmap).** Give it id="quickwins".

- **PR-3 — Slack message templates & automation:** Kickoffs, status, revisions, reminders; auto-fill client/project. Delivers in Phase 1.
- **Make/Zapier — ClickUp↔Slack:** One source of truth for task create/update; fewer ad-hoc Slacks.
- **PR-1 — Timeline calculator:** Content type, deliverables, complexity, turnaround → schedule + milestones.

**KPI:** Fewer ad-hoc Slacks; one source of truth for task created/updated. These are the “quick wins” called out in your brief.

---

## 4. New section: "Complete wish list — all 16 tools"

**Insert after Quick wins, before Section C.** Give it id="wishlist".

**Table:** One row per tool. Columns: Priority | Tool ID | Tool name | Role | Phase | Where in this proposal

| Priority | Tool ID | Tool name | Role | Phase | Where in this proposal |
|----------|---------|-----------|------|-------|------------------------|
| High | CD-1 | Predictive Retention | CD | 3–4 | B.1, Appendix 1 |
| High | CD-2 | Outlier Ideation | CD | 4 | B.1, Appendix 1 |
| High | CD-3 | Packaging & Thumbnail | CD | 4 | B.1, Appendix 1 |
| High | CD-4 | A/B Test Monitor | CD | 4 | B.1, Appendix 1 |
| High | ED-1 | Frame.io Sentiment | PPM/Editor | 2–3 | B.2, Appendix 1 |
| High | ED-2 | Automated QC | PPM | 3 | B.2, Appendix 1 |
| High | ED-3 | Capacity Assignment | Producer/PC | 2, roll 4 | B.2, Appendix 1 |
| High | PR-4 | Claude-to-ClickUp Agent | Producer | 2, roll 4 | B.3, Appendix 1 |
| Medium | CD-5 | Packaging Scorer | CD | 3 | B.1, Appendix 1 |
| Medium | CD-6 | Client Knowledge Bases | CD | 3 | B.1, Appendix 1 |
| Medium | CD-7 | Script Voice Matching | CD | 4 | B.1, Appendix 1 |
| Medium | CD-8 | Slack Scoring Bot | CD | 3–4 | B.1, Appendix 1 |
| Medium | CD-9 | Outlier Aggregator | CD | 4 | B.1, Appendix 1 |
| Medium | PR-1 | Timeline Calculator | Producer | 1 | B.3, Quick wins, Appendix 1 |
| Medium | PR-2 | Client Sentiment Tracker | Producer | 4 | B.3, Appendix 1 |
| Medium | PR-3 | Slack Templates | Producer/PC | 1 | B.3, Quick wins, Appendix 1 |

**One sentence under the table:** "We propose for every tool in your wish list: approach, phase, cost range, and maintenance are in Appendix 1; role-level justification is in Section B."

---

## 5. Evaluation criteria — add one line at the top of Section E

Before the table, add:

"Your brief specifies five criteria. This proposal addresses each one: **Specificity ✓ · Architecture ✓ · Roadmap ✓ · Cost ✓ · Engagement ✓**. Detail below."

---

## 6. Brief checklist (for your own verification)

- [ ] **Objective (brief):** 4→7 clients per pod, EOY 2026 — in cover, proposing, solution, A, C, E.
- [ ] **Quick wins:** Explicit list (PR-3, Make/Zapier, PR-1) and timeline (first 30–35 days) — new Quick wins section + Phase 1 in C.
- [ ] **8 High-priority tools:** All named and in scope — proposing, B.1–B.3, C, Appendix 1, new wish list table.
- [ ] **8 Medium-priority tools:** All named and in scope — proposing, B.1–B.3, C, Appendix 1, new wish list table.
- [ ] **Requirement A:** System architecture + diagram — Section A, Figure 1.
- [ ] **Requirement B:** AI toolkit per role (justification, cost, adoption) — Section B, Appendix 1, market context.
- [ ] **Requirement C:** Phased roadmap, buffers, KPIs — Section C.
- [ ] **Requirement D:** Labour, system costs, engagement structure — Section D.
- [ ] **Evaluation (weights):** Specificity 30%, Architecture 25%, Roadmap 20%, Cost 15%, Engagement 10% — Section E table + new one-liner.

---

## 7. Where to paste in Dragonfruit_Proposal_EOY2026.html

1. **TOC:** Add the three new nav links (proposing, quickwins, wishlist) in the `<nav class="toc">` list.
2. **After `</nav>` and before `<h2 id="solution">`:** Paste the full "What we're proposing" section (heading + 4 subsections: objective, quick wins summary, 8 high, 8 medium, requirements + criteria).
3. **After Section B (after B.3 Producers), before `<h2 id="C">`:** Paste the "Quick wins (first 30–35 days)" section and the "Complete wish list — all 16 tools" section (with table).
4. **Section E:** Add the one-line criteria checklist immediately after `<h2 id="E">` and the first `<p>`.

If you prefer, you can paste the content from this file into the HTML in the order above; the existing content (architecture, B, C, D, E, appendices, next steps) stays as is.

---

## 8. Apply via script (when the proposal file is accessible)

From the `proposal_contract` folder run:

```bash
python3 apply_final_proposal_additions.py
```

This script patches `Dragonfruit_Proposal_EOY2026.html` with the TOC updates, "What we're proposing", Quick wins, Complete wish list, and the Section E criteria line. If the file is on a slow or locked volume, run the script when it is available, or apply the sections manually using the guide above.
