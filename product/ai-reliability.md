# 14. AI reliability and document safety

**As-of:** 9 November 2025  
Principle: models assist; humans approve. Model self-reported confidence is **not** treated as calibrated.

## Controls by failure mode

| Failure | Control |
|---------|---------|
| Unsupported answers | Abstain; mark MISSING; block export for required fields |
| Incorrect extraction | Human-editable checklist; Uncertain flag; sample eval set |
| Missing pages / tables | Page-count check vs source; warn; manual add |
| Conflicting evidence | CONFLICT status; show both sources; require human choice |
| Expired evidence | Deterministic date compare vs Document.expiry |
| Malicious uploaded instructions | Treat file text as untrusted data; system prompt isolation; allowlist file types |
| Cross-tenant leakage | org_id isolation; no shared vector index across tenants |
| Unsupported file types | Reject with clear error |
| Sensitive-data exposure | Minimise fields sent to LLM; DPA; optional redact pass |
| Uncontrolled model costs | Per-org credit caps; hard stop; cache |

## Required behaviours

- Source-linked suggestions only  
- Clear abstention  
- Deterministic validation where practical (dates, required presence)  
- Human approval  
- Model/version (+ prompt hash) records on AI-assisted steps  
- Evaluation datasets from **permitted** redacted fixtures only  
- Accuracy monitoring by task  
- Manual fallback always available

## Quality measures (separate)

| Task | Metric | Pilot target *(Proposed experiment)* |
|------|--------|--------------------------------------|
| Extraction | Requirement recall / precision vs human gold | ≥0.85 recall on gold packs |
| Matching | Precision of suggested EvidenceLinks | ≥0.90 precision |
| Drafting | Edit distance / % sentences rewritten by approver | Track; no ship gate until stable |

## Eval process

1. Build gold set from redacted permitted documents in `testdata/` (post-GO).  
2. Score extraction/match/draft separately each release.  
3. Regression fail blocks release if match precision drops &gt;5pp.
