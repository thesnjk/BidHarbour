# FO7 Path B live scoped-answer write-back playbook (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use after:** Approver decision on a **live** pack when buyer-specific drafts were approved for that `customer_id` only  
**Lead gap:** multi-customer isolation — shared library ≠ silent buyer-specific inheritance (FO7 / G5)  
**Training (not Actuals):** [`pack-dry-run-dry-007.md`](pack-dry-run-dry-007.md) · [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md)  
**Schema reference only:** [`../testdata/synthetic-customer-scoped-answers-v1/`](../testdata/synthetic-customer-scoped-answers-v1/)  
**Companions:** [`pilot-evidence-library-intake.md`](pilot-evidence-library-intake.md) · [`path-b-first-live-pack-intake.md`](path-b-first-live-pack-intake.md) · [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) · [`pilot-dual-buyer-live-window-checklist.md`](pilot-dual-buyer-live-window-checklist.md) · [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md) · [`approver-review-training.md`](approver-review-training.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until rows are filled from **real** live packs.  
**Do not** invent promotions, doc_keys, or scoped answers in git. Prefer anonymised IDs; keep live scoped CSVs on the local encrypted path. DRY-007/008 rehearse FO7 — they are **not** live write-back proof.

## Goal

After Approver signs buyer-specific answers on a live pack, write them back to a **customer-scoped** store without polluting the shared library — so the next buyer pack cannot silently inherit another customer’s answers (I5).

## When to use

- Live pack (`mode=live`, pack_id `P01`/`P02`/`P03`) just closed Approver review  
- One or more answers were approved as **buyer-specific** for this `customer_id`  
- Next pack for a **different** buyer may run in the same pilot window  

Skip when: every approved answer is already shared-eligible and Approver explicitly marked shared promote; or pack was dry-run only.

## Sequence

1. **Classify** — For each Approver-approved draft, mark **scoped-only** vs **shared-eligible** (Approver must say so explicitly; default = scoped-only if buyer-named).  
2. **Write scoped** — Append scoped-only rows to the **local** customer-scoped CSV (outside git). Mirror columns from the synthetic fixture: `doc_key`, `customer_id`, `scope=customer`, `applies_to`, `approval_status`, `answer_summary`, `evidence_label`, `expiry_or_review_date`, `promoted_from_pack` (= this pack_id), `notes`.  
3. **Shared library** — Leave shared approved-answers **unchanged** unless Approver explicitly promotes a row **and** sets/confirm `applies_to` (second control). Never silent-merge scoped rows into shared.  
4. **FO7 pre-next-pack check** — Before matching another buyer’s pack: cite shared only for that buyer; cite this customer’s scoped store **only** when `customer_id` matches (I5). Log the control check below.  
5. **Log** — Fill a blank row in this playbook’s log (local copy OK if identifiers are sensitive).

## Log (blank until real)

| Customer (or anonymised) | CRM id | pack_id | doc_keys → scoped | Shared unchanged? (Y/N) | Other-buyer control check (Y/N/blank) | Logged by | Notes |
|--------------------------|--------|---------|-------------------|-------------------------|---------------------------------------|-----------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Founder / operator checklist

- [ ] Approver named which answers are scoped-only vs shared-eligible  
- [ ] Local scoped CSV updated (`scope=customer`, matching `customer_id`, `promoted_from_pack`)  
- [ ] Shared library untouched **or** only rows Approver explicitly promoted with `applies_to`  
- [ ] Log row filled (blank Actuals in git until real)  
- [ ] Before next different-buyer pack: FO7 control check done  
- [ ] No live scoped CSV or customer answer text staged for git  

## Stop rules

- Never invent promotions, evidence labels, or certifications.  
- Never silent-merge buyer-specific answers into the shared library.  
- Never cite another buyer’s scoped store (FO7 / I5 failure).  
- Never treat DRY-007/008 outcomes as live write-back proof or scorecard Actuals.  
- Never commit live customer-scoped CSVs or confidential answer text to git.
