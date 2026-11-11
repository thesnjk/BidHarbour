# Pilot evidence-library intake

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Register:** [`pilot-evidence-library-intake.csv`](pilot-evidence-library-intake.csv)  
**Runbook:** [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Fixtures:** [`../testdata/redacted-pqq-v1/`](../testdata/redacted-pqq-v1/) · [`../testdata/redacted-sq-v1/`](../testdata/redacted-sq-v1/)  
**Synthetic library (partial-library dry-runs):** [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/)  
**Customer-scoped answers (FO7 promotion):** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/) — Broads-only; do **not** merge into shared library without Approver + `applies_to` change (see DRY-007). Dual-buyer in-window sequence → [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md).

**Purpose:** Track which evidence documents a pilot SME has provided before matching a PQQ/SQ checklist. Concierge Path B intake — not a SaaS library.

**Example org name (synthetic only):** East Anglia Precision Fabrication Ltd. Do not put live customer files in git.

## When to use

| Mode | Use intake CSV? |
|------|-----------------|
| Path A empty-library dry-run | No (everything stays MISSING) |
| Path A partial-library dry-run | Yes — use [`../testdata/synthetic-evidence-library-v1/`](../testdata/synthetic-evidence-library-v1/); mark matching intake rows `received` locally; do not commit secrets |
| Path B live pack | **Yes** — fill before / during intake via [`path-b-first-live-pack-intake.md`](path-b-first-live-pack-intake.md); keep CSV + files in local encrypted folder |

## How to fill

1. Copy the CSV to the pilot’s local working folder (outside git).  
2. For each `doc_key` the customer can supply: set `status` to `received` (or `expired` / `waived`), fill `received_at`, `expiry_or_review_date` if `expiry_required=yes`, and a non-secret `version_label`.  
3. Put `storage_path_local` only in the **local** copy — never push real paths that embed customer names/secrets to GitHub.  
4. Match checklist rows in the pack to `doc_key`s; any requirement without a usable received doc → **MISSING**.  
5. Approver still signs every export; intake ≠ approval.

`applies_to`: `pqq` = Harbour Wind–style fixture, `sq` = Broads OEM–style fixture, `both` = reusable across buyers (still verify buyer-specific declarations).

Identity band includes `identity_group` (group structure / org chart or CH PSC) — see synthetic library `SYNTH-GROUP-ORG-v1`.

## Status values

| status | Meaning |
|--------|---------|
| `not_received` | Default — treat as MISSING for matching |
| `received` | File in local library; check expiry |
| `expired` | Present but past review/expiry — flag conflict |
| `waived` | Approver recorded explicit waiver |

## Rules

- Never invent certifications, insurance, financials, or capabilities.  
- Never commit live certificates, packs, or filled customer intake CSVs to git.  
- Live packs require solicitor-cleared MSA/DPA (runbook Path B).  
- Buyer-specific rows (`sq_broads_qp_ack`, conflicts) are **not** interchangeable across customers.
