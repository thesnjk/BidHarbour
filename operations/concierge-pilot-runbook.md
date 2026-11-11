# Concierge pilot runbook (Supplier Desk)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Design:** [`../research/pilot-design.md`](../research/pilot-design.md)  
**Offer:** [`../commercial/pilot-offer-sheet.md`](../commercial/pilot-offer-sheet.md)  
**Metrics:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Dry-run fixtures:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) (PQQ) · [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/) (SQ, second buyer)  
**Completed dry-runs:** [`pack-dry-run-dry-001.md`](pack-dry-run-dry-001.md) (DRY-001 PQQ) · [`pack-dry-run-dry-002.md`](pack-dry-run-dry-002.md) (DRY-002 SQ)  
**Evidence intake:** [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md) · [`pilot-evidence-library-intake.csv`](pilot-evidence-library-intake.csv)  
**Synthetic library:** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/) (partial-library dry-runs)  
**MISSING queue email:** [`missing-queue-email.md`](missing-queue-email.md)  
**Export manifest:** [`export-manifest-template.md`](export-manifest-template.md)  
**Post-export scripts:** [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md)

**Product name:** Supplier Desk  
**Delivery:** founder-operated; AI may draft only — **Approver** signs every export.

## Preconditions

| Check | Dry-run | Live pack |
|-------|---------|-----------|
| Named Approver with authority | Yes (second person OK) | Required |
| Pilot MSA + DPA solicitor-cleared and signed | No | **Required** |
| Fee received (or waiver logged) | N/A | Per offer sheet |
| Encrypted transfer path; access limited to named accounts | Local folder OK | Required |
| No model training on customer content | N/A | Required |

**Do not** start a live pack until the Live column is satisfied.

## Path A — Dry-run (ship first)

1. Open [`../testdata/redacted-pqq-v1/questionnaire.md`](../testdata/redacted-pqq-v1/questionnaire.md).  
2. Copy [`../testdata/redacted-pqq-v1/evidence-checklist.md`](../testdata/redacted-pqq-v1/evidence-checklist.md) to a working copy (do not invent evidence).  
3. Start timer. For each question: attach a fictional source **or** mark **MISSING**.  
4. Hand draft to Approver; record rework loops.  
5. Export only after Approver approval or explicit waiver.  
6. Stop timer; fill one row in [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv) (`mode=dry_run`).

**Done (2026-11-10):** empty-library DRY-001 → [`pack-dry-run-dry-001.md`](pack-dry-run-dry-001.md) (22 MISSING; export blocked).  
**Done (2026-11-10):** empty-library DRY-002 → [`pack-dry-run-dry-002.md`](pack-dry-run-dry-002.md) (18 MISSING Broads SQ; export blocked; multi-customer thesis).  
**Done (2026-11-11):** partial-library DRY-003 → [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md) (2 MISSING vs 22 empty; export still blocked; synthetic library).  
**Done (2026-11-11):** partial-library DRY-004 → [`pack-dry-run-dry-004.md`](pack-dry-run-dry-004.md) (6 MISSING vs 18 empty Broads SQ; export still blocked; multi-customer thesis).

## Path B — Live pack (after legal clearance)

1. **Intake:** receive pack + evidence folder; log pack_id, customer, received_at in metrics CSV; update a **local** copy of [`pilot-evidence-library-intake.csv`](pilot-evidence-library-intake.csv) per [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md).  
2. **Checklist:** extract requirements into a per-pack checklist (same shape as the fixture).  
3. **Match:** map each requirement to intake `doc_key`s / approved library answers; flag expired, conflicting, customer-specific gaps; anything `not_received` → **MISSING**.  
4. **MISSING queue:** send customer the MISSING list using [`missing-queue-email.md`](missing-queue-email.md); wait ≤3 business days per pilot design.  
5. **Approver gate:** Approver reviews every statement on [`export-manifest-template.md`](export-manifest-template.md); block export until approved/waived.  
6. **Export:** deliver agreed formats + completed manifest only; no portal auto-submit.  
7. **Log:** minutes, missing count at first draft, rework loops, support minutes → metrics CSV.  
8. **Close pack:** send script **A** (pack delivered) from [`pilot-closeout-scripts.md`](pilot-closeout-scripts.md); store activity note; no win-rate claims.  
9. **Continue or close pilot:** script **B** for packs 2–3 in-window; at window end use **C → D → E** (and optional **F**).

Repeat for up to **3** packs in the 4-week window.

## Metrics ritual

After each pack (dry-run or live), one CSV row:

- `minutes_to_first_draft`, `missing_fields_first_draft`, `rework_loops`, `support_minutes`, `export_approved` (yes/no)

Friday: roll metrics into [`../research/validation-scorecard.md`](../research/validation-scorecard.md) only when they are real pilot results (not dry-run alone for GO criteria).

## Stop rules

- Never invent certifications, insurance, financials, or capabilities.  
- Never claim bid-win or qualification rates.  
- Never process live packs on uncleared MSA/DPA stubs.  
- Never start production auth/database (pre-GO).  
- Never commit live customer files to git.
