# BidHarbour — agent self-service backlog (pre-GO)

**As-of:** 2026-11-17  
**Authority:** This file is the **authoritative pre-GO Continue queue**. Mark rows **done** in this file in the same PR that ships the slice.

| Queue | Role | Path |
|-------|------|------|
| **Continue / self-service** | Pre-GO agent work (this table) | `Docs/agent-backlog.md` |
| **Post-GO engineering** | MoSCoW after scorecard **GO** only | [`../product/backlog.md`](../product/backlog.md) |
| **Operating rules** | Local-only standing orders (do **not** commit) | `Docs/bidharbour-master-prompt.md` (attach with `@`) |

Direction: [`project-charter.md`](project-charter.md) · Map: [`developer-map.md`](developer-map.md)

## Continue loop

On every bare continue / attach of the local master prompt: (1) inspect workspace, (2) read charter + developer-map, (3) pick the **first unfinished** row below, (4) implement end-to-end on a feature branch. Never ask what next. Never idle because founder email is unsent. No filler, no premature SaaS, no invented Actuals.

**Four-axis GitHub coverage (required every Continue — keep the contribution radar covered):**

| Axis | Required action |
|------|-----------------|
| **Issues** | `gh issue create` for the slice **or** link an existing epic/issue with `Refs #N` / `Fixes #N` |
| **Commits** | Feature-branch commit(s) with why-focused message (never commit local `bidharbour-master-prompt.md`) |
| **Pull requests** | `gh pr create` with Summary + Test plan + `Fixes`/`Refs` |
| **Code review** | Substantive `gh pr review` on the real diff (not empty LGTM); then print `gh pr merge <n> --squash` |

Mark the row **done** in **this file** in the **same** PR. Do not ship Continues that skip Issues or Code review.

| # | Status | Slice | Epic |
|---|--------|-------|------|
| 1 | **done** | Redacted PQQ fixture + dry-run kit → `testdata/redacted-pqq-v1/` | #2 |
| 2 | **done** | Concierge pilot runbook + metrics stub → `operations/concierge-pilot-runbook.md` linked from `research/pilot-design.md` | #2 |
| 3 | **done** | CRM A11–A20 public contact enrichment (same pattern as A01–A10) | #6 |
| 4 | **done** | Competitor matrix honesty pass — public pages only → `research/competitors.md` | #1 |
| 5 | **done** | Observation kit one-pager for NAAME/Hethel → wire to scorecard | #1 |
| 6 | **done** | Brand clearance execution checklist (IPO/domain steps, no spend) → `strategy/` | #3 |
| 7 | **done** | Re-rank from open epics + competitive gaps; append rows 8–12 | — |
| 8 | **done** | Pack dry-run: walk `testdata/redacted-pqq-v1` → checklist/MISSING/Approver; fill DRY-001 in `operations/pilot-metrics-stub.csv` + short method note | #2 |
| 9 | **done** | Second redacted fixture `testdata/redacted-sq-v1/` (different buyer / SQ-style) for multi-customer thesis | #2 |
| 10 | **done** | Pilot evidence-library intake CSV + instructions → `operations/` | #2 |
| 11 | **done** | Subprocessor inventory + data-flow one-pager for solicitor → `security-and-legal/` | #5 |
| 12 | **done** | CRM A21–A30 public contact enrichment (same pattern as A11–A20) | #6 |
| 13 | **done** | Week-1 non-responder follow-up scripts (A01–A20) → `commercial/` | #6 |
| 14 | **done** | DRY-002 empty-library dry-run on `testdata/redacted-sq-v1/` → metrics + method note | #2 |
| 15 | **done** | Interview synthesis template (blank Actuals) wired to scorecard → `research/` | #1 |
| 16 | **done** | Re-rank from open epics + gaps; append rows 17–21 | — |
| 17 | **done** | CRM A31–A40 public contact enrichment (construction-control + Norfolk blanks; same pattern as A21–A30) | #6 |
| 18 | **done** | Synthetic approved-answer / evidence-library stub mapped to intake `doc_key`s → `testdata/` or `operations/` | #2 |
| 19 | **done** | MISSING-queue customer email + Approver export-manifest templates → `operations/` | #2 |
| 20 | **done** | Week-4 gate decision checklist wired to scorecard + interview-synthesis → `research/` | #1 |
| 21 | **done** | Re-rank from open epics + gaps; append rows 22–26 | — |
| 22 | **done** | CRM A41–A50 public contact enrichment (complete first-50; same pattern as A31–A40) | #6 |
| 23 | **done** | DRY-003 partial-library dry-run: `redacted-pqq-v1` + `synthetic-evidence-library-v1` → metrics + method note | #2 |
| 24 | **done** | Pilot continuation / close-out scripts (post-export) → `operations/` or `commercial/` | #2 |
| 25 | **done** | Week-8 gate decision checklist stub wired to scorecard → `research/` | #1 |
| 26 | **done** | Re-rank from open epics + gaps; append rows 27–31 | — |
| 27 | **done** | DRY-004 partial-library dry-run: `redacted-sq-v1` + `synthetic-evidence-library-v1` → metrics + method note | #2 |
| 28 | **done** | Enrich synthetic evidence library: add `identity_group` (and intake row) so PQQ Q3 can leave MISSING intentionally only for buyer-specific gaps | #2 |
| 29 | **done** | Approver review training one-pager (checklist before sign-off) → `operations/` | #2 |
| 30 | **done** | Week-1 non-responder follow-up scripts A21–A40 (same pattern as A01–A20) → `commercial/` | #6 |
| 31 | **done** | Re-rank from open epics + gaps; append rows 32–36 | — |
| 32 | **done** | Week-1 non-responder follow-up scripts A41–A50 (same pattern as A21–A40) → `commercial/` | #6 |
| 33 | **done** | Pilot kickoff agenda + checklist (Path B pre-pack-1) → `operations/` | #2 |
| 34 | **done** | Pilot data retention / deletion schedule one-pager (align close-out E + DPA) → `operations/` or `security-and-legal/` | #5 |
| 35 | **done** | Observation session log stub (blank Actuals) wired to observation kit + scorecard → `research/` | #1 |
| 36 | **done** | Re-rank from open epics + gaps; append rows 37–41 | — |
| 37 | **done** | Week-2 outreach pack for CRM A11–A20 (same pattern as Week-1 A01–A10) → `commercial/` | #6 |
| 38 | **done** | Pilot fee / waiver log template (blank Actuals) wired to Path B-0 kickoff → `operations/` | #2 |
| 39 | **done** | Observation / screenshare consent email stub wired to observation kit → `research/` | #1 |
| 40 | **done** | Pilot data-subject request (DSR) handling one-pager (align DPA obligations) → `security-and-legal/` | #5 |
| 41 | **done** | Re-rank from open epics + gaps; append rows 42–46 | — |
| 42 | **done** | Week-3 outreach pack for CRM A21–A30 (same pattern as Week-2 A11–A20) → `commercial/` | #6 |
| 43 | **done** | Bounce / OOO / wrong-entity triage scripts wired to Week-1/2 send logs → `commercial/` | #6 |
| 44 | **done** | Pilot refund / cancellation customer email stub (align pilot-design fees) → `operations/` | #2 |
| 45 | **done** | Customer breach-notification draft stub (align incident runbook S1) → `security-and-legal/` | #5 |
| 46 | **done** | Re-rank from open epics + gaps; append rows 47–51 | — |
| 47 | **done** | Week-4 outreach pack for CRM A31–A40 (same pattern as Week-3 A21–A30) → `commercial/` | #6 |
| 48 | **done** | Referral ask script (post-interview / post-pilot) → `commercial/` | #6 |
| 49 | **done** | Baseline minutes capture worksheet for Path B-0 kickoff / metrics (minutes-saved proof) → `operations/` | #2 |
| 50 | **done** | Named-accounts access register stub for pilot encrypted paths → `security-and-legal/` or `operations/` | #5 |
| 51 | **done** | When 47–50 done: re-rank from open epics + gaps; append new rows surgically | — |
| 52 | **done** | Week-5 outreach pack for CRM A41–A50 (same pattern as Week-4 A31–A40) → `commercial/` | #6 |
| 53 | **done** | Extend bounce / OOO triage to Week-4 send log → `commercial/` | #6 |
| 54 | **done** | Pilot continuation yes/no capture log (blank Actuals) wired to close-out D + scorecard → `operations/` | #2 |
| 55 | **done** | DRY-005 dry-run: expired (or conflicting) library evidence → block export; metrics + method note → `operations/` | #2 |
| 56 | **done** | Discovery → paid pilot offer email stub (solicitor-gated; no win-rate claims) → `commercial/` | #6 |
| 57 | **done** | When 52–56 done: re-rank from open epics + gaps; append new rows surgically | — |
| 58 | **done** | Extend bounce / OOO triage to Week-5 send log → `commercial/` | #6 |
| 59 | **done** | DRY-006 dry-run: conflicting library answers → CONFLICT + block export; metrics + method note → `operations/` | #2 |
| 60 | **done** | Interview SharePoint / inbound-pack time-study capture (blank Actuals) wired to synthesis + baseline contrast → `research/` | #1 |
| 61 | **done** | CRM stage transition scripts + notes conventions (Discovery → pilot offer → Pilot; fee + continuation) → `commercial/` | #6 |
| 62 | **done** | Post–first-50 referral / rebook wave runbook (warm intros + selective non-responder recycle) → `commercial/` | #6 |
| 63 | **done** | When 58–62 done: re-rank from open epics + gaps; append new rows surgically | — |
| 64 | **done** | Project writeup Ch 1 — executive summary & decision posture → `Docs/project-writeup.md` | — |
| 65 | **done** | Project writeup Part 2 — NEA-grade Analysis (no invented clients) → `Docs/project-writeup.md` | — |
| 66 | **done** | Project writeup Part 3 — Design (goals, architecture intent, data/class design, match/MISSING algorithm, IA, data dictionary, objective traceability) → `Docs/project-writeup.md` | — |
| 67 | **done** | Project writeup Parts 4–5 — Implementation (shipped artefacts/fixtures mapping) + Testing (strategy + DRY-001–006 as formal test evidence) → `Docs/project-writeup.md` | — |
| 68 | **done** | Project writeup Parts 6–7 — Evaluation against FO/NFO (honest no live clients; dry-run + desk evidence) + Operator/user guide → `Docs/project-writeup.md` | — |
| 69 | **done** | Project writeup Parts 8–9 — Bibliography + Appendices (artefact index, dry-run evidence pointers, blank discovery templates index) → `Docs/project-writeup.md` | — |
| 70 | **done** | When 66–69 done: re-rank from open epics + gaps; append new rows surgically | — |
| 71 | **done** | Pilot minutes-saved contrast rollup (blank Actuals): wire baseline worksheet + metrics stub + SharePoint time-study → scorecard Time/value → `operations/` | #2 |
| 72 | **done** | DRY-007 dry-run: buyer-specific approved-answer promotion after Pack 1 without polluting shared library (FO7); metrics + method note → `operations/` | #2 |
| 73 | **done** | Discovery / observation → paid pilot offer bridge checklist (solicitor-gated; wires observation kit, synthesis, pilot-offer email, Path B-0 kickoff) → `research/` | #1 |
| 74 | **done** | Senior writeup upgrade — invariants, state machine, match algebra, threat model, contracts, epistemology + Apps F–J → `Docs/project-writeup.md` | — |
| 75 | **done** | Solicitor pack: pilot privacy notice issue-spotter + international transfers decision-tree annex stub (counsel-gated; no customer send) → `security-and-legal/pilot-privacy-notice-issue-spotter.md` + `international-transfers-decision-tree-annex-stub.md` | #5 |
| 76 | **done** | NAAME / Hethel / Great Yarmouth network peer-intro pack (event + LinkedIn warm intros; referral density; not a new cold-50) → `commercial/naame-hethel-gy-network-peer-intro-pack.md` | #6 |
| 77 | **done** | When 75–76 done: re-rank from open epics + gaps; append new rows surgically | — |
| 78 | **done** | DRY-008 dual-buyer pilot-window dry-run (Harbour Wind PQQ → Broads SQ; shared + FO7 scoped; export gates) → `operations/pack-dry-run-dry-008.md` | #2 |
| 79 | **done** | Pilot pack-2/3 in-window playbook (Path B repeat; wires closeout B, fee/waiver, metrics) → `operations/pilot-repeat-pack-playbook.md` | #2 |
| 80 | **done** | Pilot results review agenda + continuation decision (blank Actuals; wires minutes rollup, closeout C→D, continuation log) → `operations/pilot-results-review-agenda.md` | #2 |
| 81 | **done** | Supplier Desk competitive objection sheet (Constructionline, SharePoint, tender-AI, Complys — abstain + Approver; no win-rate) → `commercial/competitive-objection-sheet.md` | #6 |
| 82 | **done** | Pre-pilot legal readiness gate (solicitor send, cleared MSA/DPA, named access; Script A only after PASS; Script B hold OK) → `operations/pre-pilot-legal-readiness-gate.md` | #5 |
| 83 | **done** | When 78–82 done: re-rank from open epics + gaps; append new rows surgically | — |
| 84 | **done** | Concierge discovery demo runbook (15 min; redacted PQQ fixture; checklist→MISSING→Approver; no SaaS) → `commercial/concierge-discovery-demo-runbook.md` | #6 |
| 85 | **done** | DRY-009: filled export manifest + Approver discipline dry-run (partial library; gate story; no live approval Actuals) → `operations/pack-dry-run-dry-009.md` + `export-manifest-dry-009-filled.md` | #2 |
| 86 | **done** | Complys / tender-AI copycat quarterly monitor stub (public-page checklist; wires objection sheet; no full scrape) → `research/copycat-monitor-quarterly.md` | #1 |
| 87 | **done** | Solicitor return / counsel clearance intake checklist (vault, PASS/FAIL, Script A unlock; wire legal gate) → `security-and-legal/solicitor-return-intake-checklist.md` | #5 |
| 88 | **done** | Pilot referral evidence packet template (blank Actuals; anonymised minutes/gates bullets; post–results-review referral) → `commercial/pilot-referral-evidence-packet.md` | #6 |
| 89 | **done** | When 84–88 done: re-rank from open epics + gaps; append new rows surgically | — |
| 90 | **done** | Path B first live pack intake worksheet (blank; wires kickoff + runbook Path B; no confidential content in git) → `operations/path-b-first-live-pack-intake.md` | #2 |
| 91 | **done** | DRY-010 waiver discipline dry-run (recorded waiver does not unlock export without Approver; fixture-only; no live Actuals) → `operations/pack-dry-run-dry-010.md` + `export-manifest-dry-010-filled.md` | #2 |
| 92 | **done** | Pilot support-burden log (blank Actuals; wires scorecard Support effort + metrics) → `operations/pilot-support-burden-log.md` | #2 |
| 93 | **done** | Warm-intro CRM intake checklist (blank; wires referral evidence packet + CRM stages; no invented emails) → `commercial/warm-intro-crm-intake.md` | #6 |
| 94 | **done** | Scorecard Actuals update hygiene checklist (founder; synthesis→scorecard; no invent) → `research/scorecard-actuals-hygiene.md` | #1 |
| 95 | **done** | When 90–94 done: re-rank from open epics + gaps; append new rows surgically | — |
| 96 | **done** | Minutes-saved customer leave-behind (blank Actuals; post–results-review; vs SharePoint; no invent) → `commercial/minutes-saved-leave-behind.md` | #6 |
| 97 | **done** | Repeat-usage tracker log (blank Actuals; ≥2 packs/60d; wires scorecard Repeat usage) → `operations/pilot-repeat-usage-tracker.md` | #2 |
| 98 | **done** | FO7 Path B live scoped-answer write-back playbook (blank; no shared-library pollution) → `operations/pilot-fo7-live-writeback-playbook.md` | #2 |
| 99 | **done** | Discovery no-show / densification rebook checklist (blank; wires grid + reply scripts) → `commercial/discovery-noshow-rebook-checklist.md` | #6 |
| 100 | **done** | Close-out F testimonial capture template (blank quotes; no invent; wires closeout scripts) → `commercial/closeout-f-testimonial-capture.md` | #6 |
| 101 | **done** | When 96–100 done: re-rank from open epics + gaps; append new rows surgically | — |
| 102 | **done** | DRY-011 dry-run: inbound pack → structured requirement checklist (fixture-only; vs SharePoint; metrics + method note) → `operations/pack-dry-run-dry-011.md` + `requirement-checklist-dry-011.md` | #2 |
| 103 | **done** | Live pilot Approver attestation log (blank Actuals; wires export manifest + DRY-009/010; no export without named Approver) → `operations/pilot-approver-attestation-log.md` | #2 |
| 104 | **done** | Path B dual-buyer live in-window checklist (blank; wires DRY-008, repeat pack, FO7 write-back; no shared pollution) → `operations/pilot-dual-buyer-live-window-checklist.md` | #2 |
| 105 | **done** | Customer MISSING/abstention brief template (blank; post gap-queue; vs tender-AI autofill; no invented prose) → `commercial/customer-missing-abstention-brief.md` | #6 |
| 106 | **done** | Qualified discovery/week tracker (blank Actuals; held interviews only; wires scorecard Repeatable acquisition + interview grid) → `research/qualified-discovery-week-tracker.md` | #1 |
| 107 | **done** | When 102–106 done: re-rank from open epics + gaps; append new rows surgically | — |
| 108 | **done** | DRY-012 dry-run: EXPIRED library on `redacted-sq-v1` → EXPIRED flags + export block (fixture-only; Broads SQ multi-customer; metrics + method note) → `operations/pack-dry-run-dry-012.md` | #2 |
| 109 | **done** | Constructionline single-profile vs multi-buyer inbound pack matrix (blank Actuals; discovery/demo; scheme ≠ per-buyer packs) → `commercial/constructionline-vs-multi-buyer-pack-matrix.md` | #6 |
| 110 | **done** | Path A pilot per-pack clock-time log (blank Actuals; wires baseline, minutes rollup, scorecard Time/value; vs SharePoint; no invent) → `operations/path-a-pilot-pack-clock-time-log.md` | #2 |
| 111 | **done** | Held discovery → paid pilot booking commitment checklist (blank Actuals; wires qualified week tracker, CRM stages, discovery→pilot bridge; solicitor-gated) → `commercial/held-discovery-pilot-booking-commitment.md` | #6 |
| 112 | **done** | Customer CONFLICT/abstention brief template (blank; post gap-queue; vs tender-AI newest-wins; no invented resolution) → `commercial/customer-conflict-abstention-brief.md` | #6 |
| 113 | **done** | When 108–112 done: re-rank from open epics + gaps; append new rows surgically | — |
| 114 | **done** | Customer EXPIRED/abstention brief template (blank; post gap-queue; vs silent renew/autofill; no invented dates) → `commercial/customer-expired-abstention-brief.md` | #6 |
| 115 | **done** | Complys contractor vault vs inbound OEM pack matrix (blank Actuals; discovery/demo; RAMS/vault ≠ per-buyer Approver export) → `commercial/complys-vault-vs-inbound-pack-matrix.md` | #6 |
| 116 | **done** | DRY-013 dry-run: stacked export blocks on fixture (EXPIRED + CONFLICT + unsigned Approver; metrics + method note) → `operations/pack-dry-run-dry-013.md` | #2 |
| 117 | **done** | Observation inbound-pack scatter capture worksheet (blank Actuals; wires time-study, observation kit, checklist Lead) → `research/observation-inbound-pack-scatter-worksheet.md` | #1 |
| 118 | **done** | Evidash buyer-side vs Supplier Desk supplier job one-pager (dated public pricing context only; no invented proof) → `commercial/evidash-buyer-vs-supplier-desk-one-pager.md` | #6 |
| 119 | **done** | When 114–118 done: re-rank from open epics + gaps; append new rows surgically | — |
| 120 | **done** | Charter hygiene pass: refresh `Docs/project-charter.md` as-of + next-gate only if posture/scorecard moved (no invent Actuals) | — |
| 121 | **done** | Opportunity portfolio refresh ritual: dated skim of `research/competitors.md` → update scores in `strategy/opportunity-portfolio.md` only with labelled evidence | — |
| 122 | **done** | Dual-backlog doc sync check: confirm `product/backlog.md` header still points agent Continue to `Docs/agent-backlog.md`; fix drift if any | — |
| 123 | **done** | Decision-scorecard twin note: ensure `strategy/decision-scorecard.md` points to live `research/validation-scorecard.md` for Actuals (no duplicate invent) | — |
| 124 | **done** | Agent OS regression checklist (blank): gates, evidence labels, human approval, secrets, dual-backlog, charter pointer → `Docs/agent-os-regression-checklist.md` | — |
| 125 | **done** | When 120–124 done: re-rank from open epics + gaps; append new rows surgically | — |
| 126 | **done** | SharePoint folders vs inbound checklist + Approver matrix (blank Actuals; discovery/demo; checklist Lead vs folder scatter) → `commercial/sharepoint-vs-inbound-checklist-matrix.md` | #6 |
| 127 | **done** | Tender-AI wrong-fight one-pager (Velstrian/KimonBids; Gap-by-design; no win-rate claims) → `commercial/tender-ai-wrong-fight-one-pager.md` | #6 |
| 128 | **done** | RFQ backup exclusion one-pager (ManufactIQ/FabPulse; portfolio backup only if PQQ fails; no silent pivot) → `commercial/rfq-backup-exclusion-one-pager.md` | #6 |
| 129 | **done** | DRY-014 FO7 dual-buyer scoped-export dry-run (scoped answers in pack; shared library clean; metrics + method note) → `operations/pack-dry-run-dry-014.md` | #2 |
| 130 | **done** | Observation→scorecard workflow-evidence tally (blank Actuals; ≥3 businesses; wires OBS log + scorecard Workflow evidence) → `research/observation-workflow-evidence-tally.md` | #1 |
| 131 | **done** | When 126–130 done: re-rank from open epics + gaps; append new rows surgically | — |
| 132 | **done** | Charter Continues pointer refresh: update `Docs/project-charter.md` First-five band (118/119 done; next = 126+); no posture/Actuals invent | — |
| 133 | todo | Opportunity portfolio matrix-path notes: link Constructionline/Evidash/Complys scan artefacts on candidates (dated skim; scores unchanged unless labelled evidence) → `strategy/opportunity-portfolio.md` | — |
| 134 | todo | ManufactIQ/FabPulse public pricing honesty micro-pass (Fallback A Unresolved; public pages only; no invent) → update `research/competitors.md` | #1 |
| 135 | todo | FO7 customer scoped-answer brief template (blank; vs silent shared-library pollution; wires FO7 playbook) → `commercial/customer-fo7-scoped-answer-brief.md` | #6 |
| 136 | todo | Discovery demo → held booking densification checklist (blank Actuals; wires demo runbook + booking commitment) → `commercial/demo-to-held-booking-densification.md` | #6 |
| 137 | todo | When 132–136 done: re-rank from open epics + gaps; append new rows surgically | — |
| 138 | todo | Interview pain-convergence → scorecard tally (blank Actuals; ≥6/10; wires synthesis + Week-4 gate) → `research/interview-pain-convergence-tally.md` | #1 |
| 139 | todo | Customer Approver export-gate brief template (blank; vs portal auto-submit / tender-AI; wires Approver training) → `commercial/customer-approver-export-gate-brief.md` | #6 |
| 140 | todo | Path A clock-time → minutes-saved leave-behind bridge checklist (blank Actuals; vs SharePoint; no invent) → `commercial/path-a-clock-to-leavebehind-bridge.md` | #6 |
| 141 | todo | Continuation log → scorecard Continuations tally (blank Actuals; ≥2; wires continuation log + scorecard) → `operations/continuation-scorecard-tally.md` | #2 |
| 142 | todo | NAAME peer-intro → qualified discovery/week densification checklist (blank; wires peer-intro pack + week tracker) → `commercial/peer-intro-to-qualified-week-densification.md` | #6 |
| 143 | todo | When 138–142 done: re-rank from open epics + gaps; append new rows surgically | — |
