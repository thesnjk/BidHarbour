# Pack dry-run DRY-011 (inbound pack → structured requirement checklist)

**Date:** 2026-11-12  
**pack_id:** DRY-011  
**mode:** `dry_run`  
**Fixture (inbound pack):** [`../testdata/redacted-pqq-v1/questionnaire.md`](../testdata/redacted-pqq-v1/questionnaire.md) — Harbour Wind PQQ  
**Filled extract:** [`requirement-checklist-dry-011.md`](requirement-checklist-dry-011.md)  
**Shape reference:** [`../testdata/redacted-pqq-v1/evidence-checklist.md`](../testdata/redacted-pqq-v1/evidence-checklist.md)  
**Live intake companion:** [`path-b-first-live-pack-intake.md`](path-b-first-live-pack-intake.md) step 4  
**Runbook:** Path A in [`concierge-pilot-runbook.md`](concierge-pilot-runbook.md)  
**Objection (SharePoint):** [`../commercial/competitive-objection-sheet.md`](../commercial/competitive-objection-sheet.md)  
**Metrics row:** [`pilot-metrics-stub.csv`](pilot-metrics-stub.csv)

**Evidence label:** Synthetic process training — **not** a customer pilot. Do **not** increment validation scorecard Actuals from this run alone.

**Thesis (Lead vs SharePoint):** An inbound questionnaire becomes a **countable** requirement checklist (Q id + topic + expected evidence type) **before** library match. SharePoint / folder scatter stores files but does not yield structured Q-rows without this extract.

## Method

1. Opened inbound fixture questionnaire (`redacted-pqq-v1/questionnaire.md`) — treat as pack received; no SharePoint browse as substitute for extract.  
2. Timer start: `2026-11-12T12:50:00Z`.  
3. Extract Q1–Q22 into [`requirement-checklist-dry-011.md`](requirement-checklist-dry-011.md): each row gets Topic + Expected evidence type; Status `open` (pending match — not silent fill).  
4. Contrast note: SharePoint folder open alone → **0** checklist rows; Desk extract → **22** rows.  
5. Stop before library match rewrite (not this dry-run’s job — see DRY-001/003). Leave `export_approved=no`.  
6. Timer stop: `2026-11-12T12:50:40Z` → **1** minute (agent checklist confirmation of extract completeness).

## Outcome

| Check | Result |
|-------|--------|
| Requirement rows extracted | **22/22** |
| Each row has id + topic + expected evidence | **Yes** |
| Silent library fills | **None** (Status `open`) |
| SharePoint contrast | Folder open ≠ structured checklist |
| Export | **Not approved** (`export_approved=no`) |

**Unique proof:** inbound pack → structured checklist extract characterised independently of match/export gates.

## Metrics summary (matches CSV)

| Field | Value |
|-------|-------|
| pack_id | DRY-011 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1 |
| received_at | 2026-11-12T12:50:00Z |
| completed_at | 2026-11-12T12:50:40Z |
| minutes_to_first_draft | 1 |
| missing_fields_first_draft | 22 |
| rework_loops | 1 |
| support_minutes | 0 |
| export_approved | no |

`notes`: inbound → structured checklist extract 22/22 open-until-match; vs SharePoint 0 Q-rows; see pack-dry-run-dry-011.md / requirement-checklist-dry-011.md.
