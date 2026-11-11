# Pilot data-subject request (DSR) handling

**Epic:** [#5](https://github.com/thesnjk/BidHarbour/issues/5)  
**Status:** Draft operational companion for founder-run Supplier Desk pilots. **Advice required.** Not legal advice; **not** a substitute for a solicitor-cleared DPA/MSA.  
**Aligns with:** [`dpa-stub.md`](dpa-stub.md) · [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md) · [`subprocessors-and-data-flow.md`](subprocessors-and-data-flow.md) · [`../operations/incident-runbook.md`](../operations/incident-runbook.md)  
**Product name:** Supplier Desk

**Rule:** Do not invent DSR Actuals or “request completed” claims in git. Cleared DPA prevails when available.

## Roles (working assumption)

| Role | Who (pilot) |
|------|-------------|
| Controller | Usually the **customer organisation** for personal data inside uploaded packs |
| Processor | BidHarbour / founder operator for concierge processing |
| Requester | Individual (or authorised agent) exercising rights |

Confirm controller/processor split in the cleared DPA before live packs.

## Scope

Personal data that may appear in: evidence folders; intake notes; MISSING / pilot emails; export manifests; local activity notes.  
Synthetic fixtures (`testdata/`) are not customer DSRs.

## Request types

Log one of: **access** · **erasure** · **rectification** · **restriction** · **objection** · **portability** (others → escalate to solicitor).

## Clock *(hypothesis — confirm with counsel)*

UK GDPR often uses **one calendar month** from valid receipt to respond (extensions possible in complex cases). Record `received_at` and `due_by` locally. **Advice required** before treating this as contractual SLA.

## Founder steps

1. **Acknowledge** receipt in writing (same channel where possible).  
2. **Verify** identity / authority (do not over-collect ID).  
3. **Classify** type; if the data is in a **customer’s** pack about *their* staff/contacts → notify the customer controller and assist per DPA.  
4. **Locate** assets using the retention asset table in [`../operations/pilot-data-retention-schedule.md`](../operations/pilot-data-retention-schedule.md).  
5. **Act:** provide copy / erase / rectify / restrict as instructed by controller + counsel; or explain lawful refusal.  
6. **Escalate** to solicitor if unclear, contested, or high-risk; use [`../operations/incident-runbook.md`](../operations/incident-runbook.md) if the matter is actually a breach.  
7. **Note** completion date + method on a **local** activity log (not git). Never train models on the content.

## Intake log (blank until real)

| DSR-ID | Received | Type | Channel | Requester verified (Y/N) | Customer / CRM | Due by | Outcome | Notes |
|--------|----------|------|---------|--------------------------|----------------|--------|---------|-------|
| | | | | | | | | |
| | | | | | | | | |

Tally current: **0** open / **0** closed.

## Stop rules

- No uncleared DPA/MSA stubs as customer contracts.  
- No inventing completed DSRs or response letters in the repo.  
- No committing live customer files or filled intake CSVs.  
- No model training on customer or requester content.  
- Breach ≠ DSR — route Sev S1/S2 via the incident runbook.
