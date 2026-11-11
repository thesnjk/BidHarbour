# Pilot named-accounts access register (encrypted paths)

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Status:** Draft operational companion for founder-run Supplier Desk pilots. **Advice required.** Not legal advice; **not** a substitute for a solicitor-cleared DPA/MSA.  
**Use at:** Path B-0 kickoff — [`../operations/pilot-kickoff-checklist.md`](../operations/pilot-kickoff-checklist.md)  
**Aligns with:** [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md) · [`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md) · [`pilot-dsr-handling.md`](pilot-dsr-handling.md)  
**Product name:** Supplier Desk

**Evidence label:** Template only until filled from a **real** pilot.  
**Do not** invent account names, emails, MFA claims, or revoke Actuals in git. Prefer anonymised customer IDs; keep filled registers on the local encrypted path only — never commit secrets or live identity detail.

## Rules

1. Least privilege: only people who need customer materials for the pilot get access.  
2. MFA is **required** on every founder operator account that can open evidence folders or transfer tools.  
3. Log each grant **before** first live intake; revoke on close-out **E** / T+30 (or sooner if DSR erasure / incident).  
4. Approver contacts may receive exports via the agreed path — still name them here if they hold pilot materials.  
5. Dry-runs (DRY-00x) need **no** register rows.  
6. No production SaaS auth scaffold until validation scorecard **GO**.

## Register (blank until real)

| Pilot / customer (anonymised OK) | Role (`founder_operator` / `approver` / `other`) | Identity handle (email or account id) | MFA on? (`yes` / `no` / blank) | Path / system (local encrypted folder / transfer tool) | Access granted | Access revoked | Purpose | Notes |
|----------------------------------|--------------------------------------------------|----------------------------------------|--------------------------------|--------------------------------------------------------|----------------|----------------|---------|-------|
| | | | | | | | |
| | | | | | | | |
| | | | | | | | |

## Tally

| Metric | Current (keep zero until data) |
|--------|--------------------------------|
| Active grants (revoked blank) | 0 |
| Grants with MFA `yes` | 0 |
| Grants still MFA blank / `no` | 0 |

## Founder checklist

- [ ] At kickoff: list every founder account that will hold this customer’s materials  
- [ ] Confirm MFA on those accounts; tick kickoff “MFA on founder accounts used for the pilot”  
- [ ] Agree encrypted transfer path; tick “access limited to named accounts”  
- [ ] Add register rows (or local private copy if handles are sensitive)  
- [ ] On close-out / T+30: revoke or wipe access; fill **Access revoked**; tick retention “Wipe / revoke named founder account access”  
- [ ] Do not start pack 1 while a required founder grant is MFA `no` or missing  

## Stop rules

- No invented accounts, MFA ticks, or “access revoked” Actuals in the repo.  
- No uncleared DPA/MSA stubs as customer contracts.  
- No model training on customer content.  
- No committing filled registers, passwords, or transfer-tool secrets.  
- Dry-run fixtures alone are not scorecard GO evidence.
