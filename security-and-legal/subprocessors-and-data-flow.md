# Subprocessors and pilot data flow

**Status:** Working inventory for solicitor review — **not legal advice**.  
**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Related:** [`dpa-stub.md`](dpa-stub.md) · [`../Docs/legal-data-policy.md`](../Docs/legal-data-policy.md) · [`../Docs/architecture.md`](../Docs/architecture.md)

**Do not** treat any row as a signed DPA or approved transfer mechanism until counsel confirms.  
**Hosting region alone does not establish UK GDPR compliance.**

## Status legend

| Status | Meaning |
|--------|---------|
| `in_use_pilot` | Used (or expected) for concierge pilots once MSA/DPA cleared |
| `candidate_post_go` | Architecture shortlist after validation GO — **not contracted** |
| `not_used` | Explicitly out of scope for current path |

## Subprocessor / tool inventory

| Function | Provider (working) | Status | Customer pack content? | Notes |
|----------|-------------------|--------|------------------------|-------|
| Local evidence store | Founder encrypted disk / folder | `in_use_pilot` | Yes (at rest locally) | No multi-tenant SaaS yet; access limited to named accounts |
| Email / scheduling | Founder mailbox (Google Workspace **or** Microsoft 365 — TBC) | `in_use_pilot` | Possible in attachments/threads | Prefer links to encrypted share over emailing full packs |
| Fee collection | Bank transfer | `in_use_pilot` | No | Default for early pilots |
| Fee collection | Stripe | `candidate_post_go` | No (billing PII only) | Only if online cards needed |
| LLM draft assist | OpenAI / Azure OpenAI / Anthropic (TBC) | `candidate_post_go` until contracted | Only if used — minimise | Prefer **no-training / zero-retention** contractual terms; record model/version; abstain on unsupported facts |
| OCR / document parse | AWS Textract / Google Document AI (TBC) | `candidate_post_go` | Yes if used | Not required for founder-operated Path A/B with manual checklist |
| App hosting / DB / object storage | UK/EU cloud (S3/R2 + Postgres — TBC) | `candidate_post_go` | Yes post-GO | Blocked until scorecard GO |
| Transactional email (product) | Resend / SES (TBC) | `candidate_post_go` | Rare | Notifications only |
| Auth (product) | Clerk / Auth0 (TBC) | `candidate_post_go` | Account data | MFA required at MVP |
| Public CRM notes | Local CSV in private repo | `in_use_pilot` | No live packs | Public company contacts only; never certificates |
| Model training on customer content | — | `not_used` | — | Forbidden unless express written agreement |

Update this table when a vendor is selected or a DPA is signed; keep URL/path stable for the DPA annex.

## Concierge pilot data flow

```text
Customer (Controller)
    |  encrypted intake (named accounts only)
    v
Founder local evidence library + intake register
    |  optional: minimise + send excerpt to LLM (only if contracted no-training)
    v
Draft checklist / answers (MISSING if unsupported)
    |  human Approver gate (export blocked if required items unapproved)
    v
Export pack → Customer
    |
    +--> retention then deletion/return per DPA
         (ops schedule → [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md))
```


### Processing rules (product + legal posture)

1. Customer organisation is **controller** for uploaded packs; BidHarbour operator is **processor** *(Reasoned inference — confirm in DPA)*.  
2. AI may draft; **only** authorised humans approve statements before export.  
3. Unsupported facts → **MISSING** — never invent certifications/insurance/financials.  
4. No foundation-model training on customer content without written agreement.  
5. International transfers (if any subprocessor outside UK/EEA): document SCCs / UK IDTA — **Advice required**.  
6. Live packs blocked until solicitor-cleared MSA + DPA are signed.

## Founder actions before live packs

- [ ] Confirm email provider row (Google vs Microsoft)  
- [ ] Confirm whether any LLM will touch live pack content in pilots (if yes: contract + minimise first)  
- [ ] Attach this file when sending [`solicitor-cover-email.md`](solicitor-cover-email.md)  
- [ ] Ask solicitor to annex approved subprocessor list to the DPA  
