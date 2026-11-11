# BidHarbour legal & data policy

**Not legal advice.** This document spots issues and recommended controls for the founding team and qualified professionals.

As-of: 9 November 2025.

## Principles

1. Customer confidential packs are trust-critical.  
2. AI assists; humans approve.  
3. No invented compliance facts.  
4. No training on customer documents without written agreement and product design.  
5. Hosting region alone does not establish UK GDPR compliance.

## Classification legend

| Tag | Meaning |
|-----|---------|
| Legal obligation | Likely UK law / UK GDPR |
| Contractual | Buyer or vendor contract |
| Recommended | Good practice |
| Optional certification | e.g. ISO 27001 |
| Advice required | Needs qualified professional |

## Controller / processor

- For customer company data uploaded into Supplier Desk, BidHarbour is typically a **processor**; the customer organisation is **controller**. *(Reasoned inference — confirm in DPA.)*  
- For BidHarbour’s own CRM/billing data, BidHarbour is **controller**.  
**Advice required** for final role mapping.

## Required artefacts before paid pilots with real packs

1. Pilot agreement / MSA stub → solicitor review (**Advice required**)  
2. Data processing agreement (DPA)  
3. Privacy notice — Path A issue-spotter → [`../security-and-legal/pilot-privacy-notice-issue-spotter.md`](../security-and-legal/pilot-privacy-notice-issue-spotter.md) (**Advice required**; no customer send until counsel)  
 
4. Acceptable use policy  
5. Subprocessor list (LLM, OCR, hosting, email, payments)  
6. Incident response outline  
7. Retention and deletion schedule

## AI provider terms

- Prefer contractual **no training on customer content** / zero data retention where available.  
- Record model/version used for assisted steps.  
- Do not send unnecessary personal data to models (minimise).  
**Contractual + Advice required.**

## Security controls (MVP target)

| Control | Tag |
|---------|-----|
| MFA for all users | Recommended / often Contractual |
| Encryption in transit (TLS) | Legal obligation / Recommended |
| Encryption at rest | Recommended |
| Access control by role | Recommended |
| Audit logging of access/export/approval | Recommended |
| Backup and tested restore | Recommended |
| Virus scan + file allowlist | Recommended |
| Tenant isolation | Recommended |
| Breach notification process | Legal obligation (UK GDPR) |
| Professional indemnity insurance | Recommended — Advice required |
| ISO 27001 / Cyber Essentials | Optional certification (often Contractual later) |

## International transfers

If any subprocessor stores or processes outside UK/EEA, document transfer mechanism (e.g. SCCs / UK IDTA) — **Legal obligation + Advice required**. Decision-tree annex stub → [`../security-and-legal/international-transfers-decision-tree-annex-stub.md`](../security-and-legal/international-transfers-decision-tree-annex-stub.md).

## Retention and deletion

- Default: retain Request artefacts for customer-configured period (e.g. 12–24 months) then delete. *(Working assumption.)*  
- Customer data export and deletion workflow is an MVP **Must**.  
- Offboarding deletes or returns data per DPA.

## Acceptable use

Prohibit: uploading materials the customer has no right to process; using the product to fabricate certificates; scraping third-party portals in violation of ToS; attempting cross-tenant access.

## Liability messaging

Product messaging must not claim guarantee of qualification, contract award, or legal compliance. Liability and insurance wording — **Advice required**.
