# Approver export manifest — DRY-009 filled (synthetic)

**Epic:** [#2](https://github.com/thesnjk/BidHarbour/issues/2)  
**pack_id:** DRY-009  
**Method note:** [`pack-dry-run-dry-009.md`](pack-dry-run-dry-009.md)  
**Template:** [`export-manifest-template.md`](export-manifest-template.md)  
**Match prior:** [`pack-dry-run-dry-003.md`](pack-dry-run-dry-003.md)

**Evidence label:** Synthetic process training — **not** a live Approver Actual. Do **not** increment validation scorecard from this alone. `export_approved=no`.

## Pack header

| Field | Value |
|-------|-------|
| pack_id | DRY-009 |
| mode | dry_run |
| customer_or_fixture | testdata/redacted-pqq-v1 + synthetic-evidence-library-v1 |
| buyer / pack label | Harbour Wind (fixture PQQ) |
| Named Approver | DR (synthetic dry-run role) |
| Draft prepared by | Path A operator (dry-run) |
| Date | 2026-11-11 |

## Manifest

Status ∈ {approved, waived, MISSING, EXPIRED, CONFLICT}. Export blocked while required rows are MISSING / EXPIRED / CONFLICT without waiver, or while draft-only library cites are withheld.

| Req # | Topic / doc_key | evidence_label / version | Status | Approver initials | Date | Notes |
|-------|-----------------|--------------------------|--------|-------------------|------|-------|
| 1 | Legal name / `identity_ch` | SYNTH-CH-LETTERHEAD-v1 | approved | DR | 2026-11-11 | |
| 2 | Addresses / `identity_address` | SYNTH-ADDRESS-LETTERHEAD-v1 | approved | DR | 2026-11-11 | |
| 3 | Group structure | — | MISSING | — | 2026-11-11 | **BLOCK** — no doc_key in stub |
| 4 | FTE / founded / `identity_fte` | SYNTH-HR-FTE-v1 | approved | DR | 2026-11-11 | |
| 5 | ISO 9001 / `hseq_iso9001` | SYNTH-ISO9001-v1 | approved | DR | 2026-11-11 | |
| 6 | ISO 14001 / 45001 / `hseq_iso14001_45001` | SYNTH-ISO-NOTHELD-v1 | approved | DR | 2026-11-11 | not_held cite |
| 7 | RIDDOR / `hseq_riddor` | SYNTH-RIDDOR-LOG-v1 | approved | DR | 2026-11-11 | |
| 8 | HSEQ lead / `hseq_lead` | SYNTH-HSEQ-CV-v1 | approved | DR | 2026-11-11 | |
| 9 | EL insurance / `ins_el` | SYNTH-EL-SCHED-v1 | approved | DR | 2026-11-11 | |
| 10 | PL insurance / `ins_pl` | SYNTH-PL-SCHED-v1 | approved | DR | 2026-11-11 | |
| 11 | PI insurance / `ins_pi` | SYNTH-PI-NA-v1 | approved | DR | 2026-11-11 | |
| 12 | Core processes / `cap_processes` | SYNTH-CAPABILITY-v1 | approved | DR | 2026-11-11 | |
| 13 | Capacity envelope / `cap_envelope` | SYNTH-SHOP-SPEC-v1 | approved | DR | 2026-11-11 | |
| 14 | Subcontractors / `cap_subcontractors` | SYNTH-AVL-v1 | approved | DR | 2026-11-11 | |
| 15 | Case study / `cap_case_study` | SYNTH-CASE-DRAFT-v1 | approved | — | 2026-11-11 | **BLOCK** — library `approval_status=draft`; Approver withheld initials |
| 16 | Modern slavery / `ethics_msa` | SYNTH-MSA-THRESHOLD-v1 | approved | DR | 2026-11-11 | |
| 17 | Dual-use / minerals / `ethics_dual_use` | SYNTH-DUALUSE-NA-v1 | approved | DR | 2026-11-11 | |
| 18 | Cyber Essentials / `cyber_ce` | SYNTH-CE-NOTHELD-v1 | approved | DR | 2026-11-11 | |
| 19 | Payment terms / `commercial_terms` | SYNTH-TERMS-v1 | approved | DR | 2026-11-11 | |
| 20 | Quality plan / audit / `commercial_quality_ack_generic` | SYNTH-QP-ACK-GENERIC-v1 | approved | DR | 2026-11-11 | |
| 21 | Adverse declarations / `decl_adverse` | SYNTH-ADVERSE-DECL-v1 | approved | DR | 2026-11-11 | |
| 22 | Conflicts / `decl_conflicts_buyer` | — | MISSING | — | 2026-11-11 | **BLOCK** — shared `not_held` |

## Approver declaration

I confirm I am authorised to approve statements in this pack for the organisation. I have reviewed each required row. I understand Supplier Desk / BidHarbour does **not** invent missing evidence and does **not** guarantee qualification or contract award.

- [ ] **Approve export** of the attached pack + this manifest  
- [x] **Block export** — list blocking rows in Notes  

**Blocking rows:** Q3 (MISSING), Q15 (draft-only library — initials withheld), Q22 (MISSING). No waiver.

Approver name: DR (synthetic) Signature / mark: dry-run Date: 2026-11-11

## Export log

| Field | Value |
|-------|-------|
| export_approved | **no** |
| formats delivered | none (blocked) |
| portal auto-submit | **no** |
| metrics CSV updated | yes |

## Stop rules

- Full manifest ≠ export approval.  
- Never invent evidence for MISSING rows.  
- Never commit live customer manifests to git.  
- Dry-run ≠ scorecard GO / live Approver Actual.
