# Requirement checklist extract — DRY-011 (characterisation)

**pack_id:** DRY-011  
**Source inbound pack:** [`../testdata/redacted-pqq-v1/questionnaire.md`](../testdata/redacted-pqq-v1/questionnaire.md)  
**Shape mirror:** [`../testdata/redacted-pqq-v1/evidence-checklist.md`](../testdata/redacted-pqq-v1/evidence-checklist.md)  
**Method note:** [`pack-dry-run-dry-011.md`](pack-dry-run-dry-011.md)

**Evidence label:** Synthetic Path A characterisation — **not** a live pack Actual. Status `open` = extracted, pending match (not a silent fill).

| Q | Topic | Expected evidence type | Status | Notes |
|---|-------|------------------------|--------|-------|
| 1 | Legal name / CH number | Companies House extract or letterhead | open | Extracted from inbound PQQ |
| 2 | Addresses | Letterhead / lease / CH filing | open | |
| 3 | Group structure | Org chart or CH PSC | open | |
| 4 | FTE / founded | Internal HR note or accounts | open | |
| 5 | ISO 9001 | Certificate PDF (number, scope, expiry) | open | |
| 6 | ISO 14001 / 45001 | Certificate PDF or “not held” | open | |
| 7 | RIDDOR | HSEQ log (redacted) | open | |
| 8 | HSEQ lead | CV / role description | open | |
| 9 | EL insurance | Broker schedule | open | |
| 10 | PL insurance | Broker schedule | open | |
| 11 | PI insurance | Broker schedule or N/A rationale | open | |
| 12 | Core processes | Capability statement | open | |
| 13 | Capacity envelope | Shop specs / photos | open | |
| 14 | Subcontractors | Approved vendor list | open | |
| 15 | Case study | Redacted project note | open | |
| 16 | Modern slavery | Statement URL or threshold note | open | |
| 17 | Dual-use / minerals | Policy or N/A rationale | open | |
| 18 | Cyber Essentials | Certificate or “not held” | open | |
| 19 | Payment terms | Standard T&Cs | open | |
| 20 | Quality plan / audit | Signed acknowledgement | open | |
| 21 | Adverse declarations | Director declaration | open | |
| 22 | Conflicts | Declaration form | open | |

**Tally:** **22/22** requirement rows extracted (id + topic + expected evidence type).  
**SharePoint contrast:** opening a document library alone yields **0** countable Q-rows without this extract step.
