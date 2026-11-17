# D. First 20 backlog items

**Post-GO engineering MoSCoW only.** This file is **not** the agent Continue queue.

- Pre-GO agent self-service backlog (authoritative): [`../Docs/bidharbour-master-prompt.md`](../Docs/bidharbour-master-prompt.md)  
- Direction / charter: [`../Docs/project-charter.md`](../Docs/project-charter.md)  
- Pre-GO research/pilot work: `commercial/` + `research/` (founder outreach; agent fixtures/runbooks)

Do **not** migrate master-prompt row numbers here. Do **not** treat rows below as next Continue work until scorecard **GO**.

| # | Item | MoSCoW | Notes |
|---|------|--------|-------|
| 1 | Org workspace + roles (Admin/Editor/Approver/Viewer) | Must | |
| 2 | MFA-enforced auth integration | Must | |
| 3 | Evidence library upload + DocumentVersion | Must | |
| 4 | Expiry / review dates on documents | Must | |
| 5 | ApprovedAnswer CRUD with evidence link | Must | |
| 6 | Request upload (PDF/DOCX/XLSX allowlist) | Must | |
| 7 | Requirement checklist editor | Must | |
| 8 | Uncertain extraction marking | Must | |
| 9 | Evidence matcher + gap statuses | Must | |
| 10 | Missing / expired / conflict queue UI | Must | |
| 11 | Section approval workflow | Must | |
| 12 | Export gate + ZIP/PDF pack + manifest | Must | |
| 13 | AuditEvent stream (append-only) | Must | |
| 14 | Data export + deletion workflow | Must | |
| 15 | Stripe subscription + usage caps | Should | After first paying software users |
| 16 | Email notifications (approval requested) | Should | |
| 17 | Bulk library import (ZIP) | Should | Reduces onboarding hours |
| 18 | Expiry dashboard | Should | Retention driver |
| 19 | OCR table pipeline hardening | Could | |
| 20 | Customer-specific answer overrides | Could | |

**Definition of done (each):** acceptance criteria in `mvp-spec.md`, tests for authz/export gates, no secrets in repo, Docs updated if architecture changes.
