# Synthetic evidence / approved-answer library v1

**Org (fictional):** East Anglia Precision Fabrication Ltd  
**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Maps to:** [`../../operations/pilot-evidence-library-intake.csv`](../../operations/pilot-evidence-library-intake.csv) `doc_key`s  
**Evidence label:** **Synthetic fixture only** — not a real SME library. Do not treat answers as real certifications.

## Purpose

Partial-library dry-runs against [`../redacted-pqq-v1/`](../redacted-pqq-v1/) and [`../redacted-sq-v1/`](../redacted-sq-v1/): match `approved` rows; leave `not_held` → **MISSING**.

## Contents

| File | Role |
|------|------|
| [`approved-answers.csv`](approved-answers.csv) | One row per intake `doc_key` with synthetic answer + evidence label |

## How to use (Path A partial-library)

1. Open a fixture checklist.  
2. For each question, look up `doc_key` in `approved-answers.csv`.  
3. If `approval_status=approved` (or `draft`), cite `evidence_label` + `answer_summary` — still route to Approver before export.  
4. If `not_held` → mark **MISSING** (Broads-specific SQ rows are intentionally empty for multi-customer practice).  
5. Do **not** invent certificates beyond this stub.

## Rules

- Never commit live customer certificates or filled real intake CSVs here.  
- Approver gate still applies; library ≠ export approval.  
- Buyer-specific declarations (`decl_conflicts_buyer`, Broads QP ack) stay `not_held` until a buyer-named synthetic row is added.
