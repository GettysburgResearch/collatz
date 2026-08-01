# Current integration pointer

## Immutable frozen snapshot

**Snapshot:** [`2026-08-01`](2026-08-01/STATE.md)  
**Cutoff UTC:** `2026-08-01T21:16:40Z`  
**Cutoff Asia/Jerusalem:** `2026-08-02T00:16:40+03:00`  
**Frozen main:** `0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84`  

The following files remain the authoritative historical ledger for the first cutoff:

- [`SNAPSHOT.md`](2026-08-01/SNAPSHOT.md)
- [`STATE.md`](2026-08-01/STATE.md)
- [`REVIEW_COVERAGE.md`](2026-08-01/REVIEW_COVERAGE.md)
- [`INTEGRATION_REPORT.md`](2026-08-01/INTEGRATION_REPORT.md)
- [`STRATEGIC_OUTLOOK.md`](2026-08-01/STRATEGIC_OUTLOOK.md)
- [`HANDOFF.md`](2026-08-01/HANDOFF.md)
- [`open-prs.json`](2026-08-01/open-prs.json)
- [`POST_CUTOFF.md`](2026-08-01/POST_CUTOFF.md)

Do not edit those records to incorporate later work.

## Current operational continuation

**Continuation:** [`2026-08-02-lifecycle`](2026-08-02-lifecycle/README.md)  
**Observation UTC:** `2026-08-01T22:18:52Z`  
**Observation Asia/Jerusalem:** `2026-08-02T01:18:52+03:00`  
**Integration branch start head:** `390969210c5c168c52ba2795b7c3400e57a6d2e8`  

The continuation adds:

- all-45-PR lifecycle and recommended-action ledger;
- candidate-versus-accepted promotion semantics;
- durable proof-import plan;
- focused promotion audit and independent-review checklist;
- proposed `RD-BRIDGE-001` for the SC*/FC* crosswalk;
- Wave A and Wave B execution criteria;
- explicit human-owner decisions.

Use these files for operational decisions:

- [`PR_LIFECYCLE.md`](2026-08-02-lifecycle/PR_LIFECYCLE.md)
- [`pr-lifecycle.json`](2026-08-02-lifecycle/pr-lifecycle.json)
- [`PROOF_IMPORT_PLAN.md`](2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md)
- [`PROMOTION_AUDIT.md`](2026-08-02-lifecycle/PROMOTION_AUDIT.md)
- [`SC_FC_BRIDGE.md`](2026-08-02-lifecycle/SC_FC_BRIDGE.md)
- [`NEXT_WAVES.md`](2026-08-02-lifecycle/NEXT_WAVES.md)
- [`OWNER_DECISIONS.md`](2026-08-02-lifecycle/OWNER_DECISIONS.md)

A later integrator should create a new dated directory for new reviews or changed heads and then update this pointer.
