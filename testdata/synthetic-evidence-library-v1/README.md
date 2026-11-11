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

**Identity keys:** `identity_ch`, `identity_address`, `identity_fte`, `identity_group` (`SYNTH-GROUP-ORG-v1` — standalone / no parent group). Maps to PQQ Q3 group structure for **future** partial-library runs. DRY-003 recorded Q3 MISSING before this key existed — leave that historical metric as-of; do not rewrite.

## How to use (Path A partial-library)

1. Open a fixture checklist.  
2. For each question, look up `doc_key` in `approved-answers.csv`.  
3. If `approval_status=approved` (or `draft`), cite `evidence_label` + `answer_summary` — still route to Approver before export.  
4. If `not_held` → mark **MISSING** (Broads-specific SQ rows are intentionally empty for multi-customer practice).  
5. Do **not** invent certificates beyond this stub.

## Expired variant (DRY-005)

For Path A **EXPIRED** rehearsal (backdated `ins_el` only), use sibling [`../synthetic-evidence-library-v1-expired/`](../synthetic-evidence-library-v1-expired/). Leave this v1 folder unchanged so DRY-003/004 metrics stay valid.

## Rules

- Never commit live customer certificates or filled real intake CSVs here.  
- Approver gate still applies; library ≠ export approval.  
- Intentional MISSING after this enrichment: buyer-specific declarations (`decl_conflicts_buyer`, Broads `sq_*` / QP ack) — not identity/group gaps.
