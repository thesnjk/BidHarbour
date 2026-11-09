# 12. UX and information architecture

**As-of:** 9 November 2025  
Optimise for users who do **not** want a complex procurement platform.

## Primary user journeys

1. Onboard evidence library  
2. Create / upload new request  
3. Resolve missing / expired / conflicts  
4. Approver review  
5. Export pack  
6. Offboard / export-delete data  

## Navigation structure

```
Home (Requests)
Library (Documents | Approved answers)
Customers
Approvals (inbox)
Settings (Users | Billing | Security | Data export)
```

## Screen map

| Screen | Purpose |
|--------|---------|
| Request list | Status, due dates, gaps count |
| Request detail | Checklist + match + evidence + approval |
| Library document | Versions, expiry, owner |
| Answer bank | Approved text + links |
| Approval inbox | Items awaiting named approver |
| Export viewer | Manifest + download |
| Empty states | CTA to upload first library / first request |

## States

| State | Behaviour |
|-------|-----------|
| Empty | Plain CTA; no fake dashboards |
| Loading | Skeleton on checklist rows |
| Error | Recoverable message; retain draft |
| Permission | Explain missing role; link to admin |

## Review and approval flow

Editor marks Ready for review → Approver sees per-requirement Approve / Reject / Request change → Export enabled only when gates pass → AuditEvent written.

## Mobile vs desktop

- **Desktop:** primary authoring  
- **Mobile:** approver notifications + approve/reject only  

## Accessibility

WCAG 2.2 AA target: keyboard focus order; status not by colour alone; labels on inputs; sufficient contrast; don’t rely on drag-only actions.

## Onboarding flow

1. Create org  
2. Invite Approver  
3. Upload 5–20 core documents  
4. Mark 10 approved answers  
5. Process first sample/real request with concierge help  

## Evidence provenance display

Every suggestion shows: document title, version, page/section if known, retrieved date, expiry. Uncertain extraction banner: “Model suggestion — verify against source.”

## Uncertain extraction and conflicts

```
[Request: ACME PQQ 2025]  Status: Awaiting approval
┌──────────────────────────────────────────────────┐
│ Req │ Question (short) │ Match │ Evidence │ Status │
│ 4.2 │ ISO 9001         │ Yes   │ cert.pdf │ OK     │
│ 7.1 │ PL £5m           │ —     │ —        │ MISSING│
│ 8.3 │ H&S policy date  │ 2 docs│ A, B     │ CONFLICT│
└──────────────────────────────────────────────────┘
[Approver: Jane]  [Export blocked: 2 open items]
```
