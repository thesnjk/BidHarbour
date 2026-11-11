# Solicitor return / counsel clearance intake checklist

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Use when:** Counsel replies to the solicitor pack (MSA/DPA / guidance)  
**Outbound first:** [`solicitor-send-checklist.md`](solicitor-send-checklist.md) · [`solicitor-cover-email.md`](solicitor-cover-email.md)  
**Gate exit:** [`../operations/pre-pilot-legal-readiness-gate.md`](../operations/pre-pilot-legal-readiness-gate.md)  
**Also:** [`pilot-privacy-notice-issue-spotter.md`](pilot-privacy-notice-issue-spotter.md) · [`international-transfers-decision-tree-annex-stub.md`](international-transfers-decision-tree-annex-stub.md) · [`pilot-named-access-register.md`](pilot-named-access-register.md)  
**Product name:** Supplier Desk

**Evidence label:** Blank until a **real** counsel return. Do **not** invent PASS dates, MFA ticks, or clearance Actuals in git. Cleared drafts stay in a **private vault** — never commit counsel content.

## Goal

Turn a solicitor reply into vault filing + honest **PASS / FAIL / pending** inputs for the legal readiness gate, so Script **A** unlocks only when counsel-cleared MSA/DPA exist and pack-processing blockers are closed.

## Intake steps

1. **Receive** — Log return date + firm in **private** notes (not git if sensitive).  
2. **Classify reply** — Cleared drafts / open blockers / questions only (pick one primary; note mixed cases).  
3. **Vault MSA** — Store cleared **pilot MSA** outside git (encrypted vault / private drive).  
4. **Vault DPA** — Store cleared **DPA** outside git the same way.  
5. **Privacy / transfers** — Note counsel guidance; stubs remain counsel-gated for customer send — do **not** treat issue-spotters as approved notices.  
6. **Blockers** — Confirm nothing still **blocks** processing real packs (or list open items → pending).  
7. **Subprocessors** — Spot-check Path A inventory still matches what counsel reviewed ([`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md)).  
8. **Feed gate** — Complete legal gate §2–3, then §4 exit (PASS only if §1–3 complete).  
9. **CRM / offer** — PASS → Script **A** unlock; FAIL/pending → Script **B** hold (`pilot_offer_held_legal`).

## PASS / FAIL (aligned with legal gate)

| Result | Required | Allows | Forbids |
|--------|----------|--------|---------|
| **PASS** | Vault MSA + vault DPA + no open pack blockers + founder named-access procedure ready (gate §3) | Script **A**; proceed toward kickoff after acceptance | Treating stubs as signed contracts; inventing Actuals |
| **FAIL / pending** | Any missing vault draft, open counsel blocker, or incomplete §3 | Script **B**; discovery without third-party packs | Script **A**; live packs; customer MSA/DPA stubs as contracts |

Re-run this intake when counsel returns a later cleared set; then re-evaluate the gate.

## Intake checklist

- [ ] Return date logged privately  
- [ ] Cleared MSA in vault (outside git)  
- [ ] Cleared DPA in vault (outside git)  
- [ ] Privacy / transfers guidance noted (stubs still not customer-ready without counsel say-so)  
- [ ] No open counsel blockers on real packs (or blockers listed → pending)  
- [ ] Subprocessor / data-flow spot-check done  
- [ ] Legal gate §2–4 updated; PASS or FAIL decided honestly  
- [ ] CRM / Script A–B tags match gate exit ([`../commercial/crm-stage-scripts.md`](../commercial/crm-stage-scripts.md))

## Tracking (blank until real)

| return_date | vault_msa (Y/blank) | vault_dpa (Y/blank) | blockers (Y/blank) | gate_result (PASS/FAIL/pending/blank) | notes (no secrets) |
|-------------|---------------------|---------------------|--------------------|---------------------------------------|--------------------|
| | | | | | |

Tally: **0** PASS · **0** pending (keep zero until founder fills privately or anonymised).

## Stop rules

- No Script **A** while gate FAIL/pending.  
- No uncleared stubs sent as customer contracts.  
- No cleared counsel drafts committed to git.  
- No invented PASS dates or clearance Actuals in this table.  
- Live packs still require gate PASS **and** Path B-0 kickoff complete.
