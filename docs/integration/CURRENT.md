# Legacy integration compatibility pointer

The single current repository pointer is now [`../../STATE.md`](../../STATE.md). Newcomers should read [`../../START_HERE.md`](../../START_HERE.md), [`../../CURRENT_KNOWLEDGE.md`](../../CURRENT_KNOWLEDGE.md), and [`../../FRONTIERS.md`](../../FRONTIERS.md), not the lifecycle ledger.

This file remains to preserve old links into the first integration process.

## First immutable snapshot

Location: [`2026-08-01/`](2026-08-01/STATE.md)

```text
cutoff UTC: 2026-08-01T21:16:40Z
cutoff Asia/Jerusalem: 2026-08-02T00:16:40+03:00
frozen main: 0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84
source PR population: 45
exact-SHA review coverage: 42/45
```

Authoritative historical files:

- [`SNAPSHOT.md`](2026-08-01/SNAPSHOT.md)
- [`STATE.md`](2026-08-01/STATE.md)
- [`REVIEW_COVERAGE.md`](2026-08-01/REVIEW_COVERAGE.md)
- [`INTEGRATION_REPORT.md`](2026-08-01/INTEGRATION_REPORT.md)
- [`STRATEGIC_OUTLOOK.md`](2026-08-01/STRATEGIC_OUTLOOK.md)
- [`HANDOFF.md`](2026-08-01/HANDOFF.md)
- [`open-prs.json`](2026-08-01/open-prs.json)
- [`POST_CUTOFF.md`](2026-08-01/POST_CUTOFF.md)

Do not rewrite these files to make later work appear reviewed at the earlier cutoff.

## Pre-merge lifecycle continuation

Location: [`2026-08-02-lifecycle/`](2026-08-02-lifecycle/README.md)

This directory was created while PR #84 was still a draft. It records:

- advisory dispositions for all 45 source PRs;
- recommended future actions;
- candidate-state semantics used before merge;
- the original proof-import plan and promotion audit;
- a proposed SC*/FC* crosswalk;
- planned later integration waves and owner decisions.

PR #84 subsequently merged at

```text
7ed553faea8350050ca4c7d742c049f90211a8bd.
```

Therefore phrases such as `candidate_in_draft_pr`, “draft PR #84,” or “unmerged” inside that dated directory are historical statements, not current repository semantics.

## Current post-merge layer

Use:

- [`../../research/integrated/`](../../research/integrated/README.md) for readable proof packets;
- [`../../claims/CANONICAL.md`](../../claims/CANONICAL.md) for accepted reference and roadmap records;
- [`../../archive/integration/`](../../archive/integration/README.md) for the archive index;
- [`../../STATE.md`](../../STATE.md) for the current branch and PR status.

Stable historical paths remain in place so old PR comments, reports, and citations continue to resolve.
