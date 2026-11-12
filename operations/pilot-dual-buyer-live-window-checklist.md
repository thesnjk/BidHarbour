# Path B dual-buyer live in-window checklist (blank Actuals)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**Use when:** same SME; **two different buyers** / questionnaires in one paid pilot window (`P01` then `P02`/`P03`)  
**Lead gap:** multi-customer packs vs Constructionline single profile  
**Training (not Actuals):** [`pack-dry-run-dry-008.md`](pack-dry-run-dry-008.md)  
**Companions:** [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) · [`pilot-fo7-live-writeback-playbook.md`](pilot-fo7-live-writeback-playbook.md) · [`pilot-approver-attestation-log.md`](pilot-approver-attestation-log.md) · [`path-b-first-live-pack-intake.md`](path-b-first-live-pack-intake.md) · [`pilot-repeat-usage-tracker.md`](pilot-repeat-usage-tracker.md) · [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)  
**Product name:** Supplier Desk

**Evidence label:** Template only until a **real** dual-buyer live window.  
**Do not** invent second-buyer packs, FO7 passes, or scorecard Actuals in git. DRY-008 rehearses isolation — it is **not** live dual-buyer proof.

## Goal

Run two different-buyer packs in one window with shared library clean, scoped cites isolated (FO7 / I5), and Approver attestation on each pack — without treating dry-runs as GO evidence.

## Sequence

1. **Pack 1 close** — Path B export + closeout **A**; FO7 write-back for buyer-A–specific answers only ([`pilot-fo7-live-writeback-playbook.md`](pilot-fo7-live-writeback-playbook.md)); shared library untouched unless explicit shared promote.  
2. **Pack 2 intake** — New buyer questionnaire; new `pack_id` (`P02`/`P03`); follow [`pilot-repeat-pack-playbook.md`](pilot-repeat-pack-playbook.md) (no full Path B-0 re-kickoff).  
3. **Match** — Shared library first; customer-scoped store **only** when `customer_id` matches this SME **and** the row is for this buyer context (never cite the other buyer’s scoped answers).  
4. **FO7 control** — Pack 1 cites contain no Pack-2-buyer scoped labels; Pack 2 never cites another buyer’s scoped store.  
5. **Approver + metrics** — Each pack: [`pilot-approver-attestation-log.md`](pilot-approver-attestation-log.md) + metrics `mode=live`.  
6. **Repeat usage** — If ≥2 live packs in 60d, update [`pilot-repeat-usage-tracker.md`](pilot-repeat-usage-tracker.md).

## Allowed / forbidden (live mirror of DRY-008)

| Step | Allowed | Forbidden |
|------|---------|-----------|
| Pack 1 | Shared library cites; Approver attestation | Cite other-buyer scoped answers; silent shared merge |
| After Pack 1 | FO7 scoped write-back; keep shared clean | Newest-wins / invent to clear MISSING |
| Pack 2 | Shared + this-customer scoped for matching buyer | Cite Pack 1 buyer’s scoped-only answers for Pack 2 buyer |
| Either export | Named Approver Approve/Block | Portal auto-submit; DRY-008 as live proof |

## Log (blank until real)

| Customer (or CRM id) | Buyer A label | Pack 1 id | Buyer B label | Pack 2 id | FO7 control OK? (Y/N/blank) | Shared unchanged? (Y/N) | Logged by | Notes |
|----------------------|---------------|-----------|---------------|-----------|-----------------------------|-------------------------|-----------|-------|
| | | | | | | | | |
| | | | | | | | | |

## Founder checklist

- [ ] Pack 1 closed with attestation + FO7 write-back (scoped only)  
- [ ] Pack 2 intake under repeat-pack playbook (fee gate still OK)  
- [ ] FO7 control check logged (no cross-buyer scoped cites)  
- [ ] Shared library unchanged **or** only explicit shared promotes  
- [ ] Both packs: metrics `mode=live` + attestation rows  
- [ ] Repeat-usage tracker updated if applicable  
- [ ] No confidential pack text / live scoped CSVs staged for git  

## Stop rules

- Never invent a second buyer pack to “pass” multi-customer thesis.  
- Never treat DRY-008 as live dual-buyer Actuals.  
- Never cite another buyer’s scoped store (FO7 failure).  
- Never silent-merge buyer-specific answers into shared.  
- Never open pack 4 inside the pilot window (max 3).  
- Never re-run full Path B-0 kickoff solely for packs 2–3 unless legal terms changed.
