# Incident ownership (draft)

**Not a substitute for a full IR plan.** Expand before holding sensitive packs at scale.

## Severity

| Sev | Example | Response |
|-----|---------|----------|
| S1 | Suspected cross-tenant access or data breach | Founder owns; revoke access; notify counsel; UK GDPR assessment; customer draft → [`../security-and-legal/customer-breach-notification-draft.md`](../security-and-legal/customer-breach-notification-draft.md) |
| S2 | Wrong evidence exported to customer | Halt exports; notify customer org; root cause; draft → [`../security-and-legal/customer-breach-notification-draft.md`](../security-and-legal/customer-breach-notification-draft.md) (S2) |
| S3 | AI mismatch caught before export | Log; improve matcher; no customer notify required |
| S4 | Billing/login friction | Support queue |

## Owner

Founder is incident commander until a hire exists.

## After-action

Write note in `operations/` (no secrets); update controls; score trust impact on retention risk.
