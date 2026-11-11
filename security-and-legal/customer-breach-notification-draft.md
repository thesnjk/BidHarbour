# Customer breach-notification draft (stub)

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Status:** Draft customer copy only. **Advice required.** Not legal advice; **not** a substitute for counsel, ICO assessment, or a full IR plan.  
**Aligns with:** [`../operations/incident-runbook.md`](../operations/incident-runbook.md) (S1/S2) · [`dpa-stub.md`](dpa-stub.md) · [`pilot-dsr-handling.md`](pilot-dsr-handling.md) · [`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md) · [`../Docs/legal-data-policy.md`](../Docs/legal-data-policy.md)  
**Product name:** Supplier Desk

**Rule:** Do not invent incidents or “breach confirmed” Actuals in git. Do **not** send without counsel. Keep secrets and customer identifiers out of the repo.

## When (founder + counsel decide)

| Sev | Example | Customer notify? |
|-----|---------|------------------|
| **S1** | Suspected cross-tenant access or personal-data breach | Often — after counsel / UK GDPR assessment |
| **S2** | Wrong evidence exported to a customer org | Usually notify that org; use S2 variant |
| S3/S4 | Pre-export AI mismatch / billing friction | Not this draft |

## Immediate internal steps (before any customer email)

1. Revoke / limit access on affected accounts and shares.  
2. Notify counsel; start UK GDPR assessment (no conclusion in this stub).  
3. Preserve logs locally (not git).  
4. Draft below with counsel; send only when cleared.  
5. If individuals assert rights → [`pilot-dsr-handling.md`](pilot-dsr-handling.md).

## Incident log (blank until real)

| INC-ID | Sev | Detected | Customer / CRM | Counsel notified (Y/N) | Customer email sent (Y/N) | Notes (no secrets) |
|--------|-----|----------|----------------|------------------------|---------------------------|--------------------|
| | | | | | | |

Tally current: **0** open / **0** closed.

---

## S1 — Suspected breach / unauthorised access (draft)

**Subject:** Supplier Desk — security incident notice ({{company}})

```text
Hi {{Name}},

We are writing about a security incident affecting Supplier Desk materials we hold for {{company}} in connection with the BidHarbour / Supplier Desk pilot.

What we know so far (subject to ongoing review with counsel):
- Detected: {{detected_at}}
- Nature: {{brief_description — no speculative blame}}
- Categories of data that may be involved: {{data_categories_or_unknown}}
- Approximate volume / systems: {{scope_or_under_investigation}}

What we have done:
- Restricted access to affected accounts and transfer paths
- Engaged counsel and are assessing notification duties under UK GDPR
- {{other_containment_steps}}

What we ask you to do:
- {{customer_actions_if_any — e.g. watch for unusual access; rotate shared credentials you control}}
- Reply to {{Founder}} if you need a named contact for your own counsel or DPO

We will not claim “no risk” while investigation continues. We will update you when material facts change.

{{Founder}}
Supplier Desk (BidHarbour) · incident contact
```

---

## S2 — Wrong evidence exported (draft)

**Subject:** Supplier Desk — incorrect export notice (pack {{pack_id}})

```text
Hi {{Name}},

We exported or delivered materials for pack {{pack_id}} that should not have been included / went to the wrong recipient context.

What happened: {{brief_description}}  
When: {{detected_at}}  
What we ask: delete or quarantine the incorrect files and confirm by {{reply_by}}. We have halted further exports pending root cause.

We are reviewing controls so this does not recur. Contact: {{Founder}}.

{{Founder}}
Supplier Desk (BidHarbour)
```

## Stop rules

- No customer breach emails without counsel clearance.  
- No inventing INC rows, ICO filings, or “breach confirmed” claims in git.  
- No secrets, passwords, or live customer packs in the repo.  
- DSR ≠ breach — route individual rights separately.
