# 15. Security, privacy and legal workstream

**Issue-spotter only — not qualified legal advice.**  
**As-of:** 9 November 2025

## Classification

| Topic | Type | Notes |
|-------|------|-------|
| UK GDPR / Data Protection Act 2018 | Legal obligation | Apply to personal data in packs/accounts |
| Controller vs processor roles | Legal + Advice required | Usually customer = controller; BidHarbour = processor for uploaded packs |
| DPA with customers | Legal / contractual | Required before paid pilots with real packs |
| Subprocessor list | Legal / contractual | Hosting, OCR, LLM, email, payments |
| International transfers | Legal + Advice required | Document mechanism if outside UK/EEA → [`international-transfers-decision-tree-annex-stub.md`](international-transfers-decision-tree-annex-stub.md) |
| Retention / deletion | Legal + contractual | MVP must-have workflow → [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md) |
| Data subject rights (DSR) | Legal + Advice required | Pilot intake/assist → [`pilot-dsr-handling.md`](pilot-dsr-handling.md) |
| Access control + MFA | Recommended (often contractual) | All users |
| Encryption in transit / at rest | Recommended / expected | TLS + storage encryption |
| Audit logging | Recommended | Approvals, exports, access |
| Backup / recovery | Recommended | Tested restore |
| Incident handling | Legal obligation (breach) | [`../operations/incident-runbook.md`](../operations/incident-runbook.md) · customer draft → [`customer-breach-notification-draft.md`](customer-breach-notification-draft.md) |
| Confidential commercial documents | Contractual + trust | Beyond personal data |
| Terms of service | Contractual + Advice required | No win guarantees |
| Privacy notice | Legal obligation | Issue-spotter → [`pilot-privacy-notice-issue-spotter.md`](pilot-privacy-notice-issue-spotter.md) |
| Acceptable use | Contractual | Ban fabricated certs |
| Liability / insurance | Advice required | PI / cyber |
| AI provider data-use terms | Contractual | Prefer no-training / ZDR |
| Cyber Essentials / ISO 27001 | Optional certification | Often later contractual |

## Pre-pilot minimum

- [x] Privacy notice draft (issue-spotter) → [`pilot-privacy-notice-issue-spotter.md`](pilot-privacy-notice-issue-spotter.md) — counsel clearance still required before customer use  
 
- [ ] DPA draft → solicitor  
- [ ] Pilot terms → solicitor  
- [ ] Subprocessor list v0  
- [ ] MFA on all accounts used for customer data  
- [ ] Deletion process written  

## Explicit non-claim

Using a UK/EU hosting region or a particular vendor **alone** does not establish compliance.
