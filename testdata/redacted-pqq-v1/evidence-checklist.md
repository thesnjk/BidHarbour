# Evidence checklist — redacted-pqq-v1

**Rules:** Each row must end as `draft` (source cited), `approved`, `waived`, or `MISSING`. Never silent-fill.

| Q | Topic | Expected evidence type | Status | Notes / gap |
|---|-------|------------------------|--------|-------------|
| 1 | Legal name / CH number | Companies House extract or letterhead | MISSING | |
| 2 | Addresses | Letterhead / lease / CH filing | MISSING | |
| 3 | Group structure | Org chart or CH PSC | MISSING | |
| 4 | FTE / founded | Internal HR note or accounts | MISSING | |
| 5 | ISO 9001 | Certificate PDF (number, scope, expiry) | MISSING | |
| 6 | ISO 14001 / 45001 | Certificate PDF or “not held” | MISSING | |
| 7 | RIDDOR | HSEQ log (redacted) | MISSING | |
| 8 | HSEQ lead | CV / role description | MISSING | |
| 9 | EL insurance | Broker schedule | MISSING | |
| 10 | PL insurance | Broker schedule | MISSING | |
| 11 | PI insurance | Broker schedule or N/A rationale | MISSING | |
| 12 | Core processes | Capability statement | MISSING | |
| 13 | Capacity envelope | Shop specs / photos | MISSING | |
| 14 | Subcontractors | Approved vendor list | MISSING | |
| 15 | Case study | Redacted project note | MISSING | |
| 16 | Modern slavery | Statement URL or threshold note | MISSING | |
| 17 | Dual-use / minerals | Policy or N/A rationale | MISSING | |
| 18 | Cyber Essentials | Certificate or “not held” | MISSING | |
| 19 | Payment terms | Standard T&Cs | MISSING | |
| 20 | Quality plan / audit | Signed acknowledgement | MISSING | |
| 21 | Adverse declarations | Director declaration | MISSING | |
| 22 | Conflicts | Declaration form | MISSING | |

## Dry-run scoring (fill after attempt)

### DRY-001 — empty library

See [`../../operations/pack-dry-run-dry-001.md`](../../operations/pack-dry-run-dry-001.md).

| Metric | Value |
|--------|-------|
| Minutes to first complete draft | 1 |
| Fields MISSING at first draft | 22/22 |
| Rework loops after Approver review | 1 |
| Export blocked until Approver sign-off? (yes/no) | yes (export_approved=no; no waiver) |

### DRY-003 — partial library (`synthetic-evidence-library-v1`)

See [`../../operations/pack-dry-run-dry-003.md`](../../operations/pack-dry-run-dry-003.md). Working statuses for that run: Q1–Q2/Q4–Q21 **draft** (library cite); Q3 + Q22 **MISSING**. Template table above stays blank for new Path A copies.

| Metric | Value |
|--------|-------|
| Minutes to first complete draft | 1 |
| Fields MISSING at first draft | 2/22 |
| Rework loops after Approver review | 1 |
| Export blocked until Approver sign-off? (yes/no) | yes (export_approved=no; no waiver) |

### DRY-005 — expired library (`synthetic-evidence-library-v1-expired`)

See [`../../operations/pack-dry-run-dry-005.md`](../../operations/pack-dry-run-dry-005.md). Working statuses: Q9 **EXPIRED** (`ins_el`); Q22 **MISSING**; other matched rows **draft**. Base v1 library unchanged.

| Metric | Value |
|--------|-------|
| Minutes to first complete draft | 1 |
| Fields MISSING at first draft | 1/22 |
| EXPIRED at first draft | 1/22 (Q9) |
| Rework loops after Approver review | 1 |
| Export blocked until Approver sign-off? (yes/no) | yes (export_approved=no; no waiver) |
