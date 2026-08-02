# Integration evidence archive

The first major integration pass was merged by PR #84 at commit

```text
7ed553faea8350050ca4c7d742c049f90211a8bd
```

Its bookkeeping remains valuable as provenance, but it is backstage material. The current scientific front door is [`../../CURRENT_KNOWLEDGE.md`](../../CURRENT_KNOWLEDGE.md).

## Immutable first cutoff

Location: [`../../docs/integration/2026-08-01/`](../../docs/integration/2026-08-01/)

Frozen facts:

- cutoff UTC: `2026-08-01T21:16:40Z`;
- frozen main: `0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84`;
- 45 source PRs at cutoff;
- 42 exact-SHA review verdicts;
- #67, #68, and #69 unreviewed in that wave.

Important files:

- `STATE.md` — frozen status;
- `SNAPSHOT.md` — cutoff construction;
- `REVIEW_COVERAGE.md` — exact-SHA verdict matrix;
- `INTEGRATION_REPORT.md` — first-pass synthesis;
- `STRATEGIC_OUTLOOK.md` — then-current roadmap;
- `HANDOFF.md` — historical next-integrator instructions;
- `open-prs.json` — machine inventory;
- `POST_CUTOFF.md` — later-activity boundary.

These files are intentionally not rewritten.

## Lifecycle continuation before merge

Location: [`../../docs/integration/2026-08-02-lifecycle/`](../../docs/integration/2026-08-02-lifecycle/)

This continuation recorded:

- an advisory disposition for all 45 source PRs;
- recommended future repository actions;
- candidate-versus-accepted status semantics used while PR #84 was still a draft;
- a proof-import plan;
- an integration-boundary audit;
- the proposed SC*/FC* crosswalk;
- planned later integration waves;
- owner decisions.

Statements such as “draft PR #84” or `candidate_in_draft_pr` in this dated directory describe the historical state at that observation. They are not current semantics.

## Current post-merge semantics

After PR #84 merged:

- the eight `IC-*` records became **accepted reference records** on `main`;
- the three `RD-*` records became **accepted roadmap records**, while remaining mathematically open or proposed;
- proof residency is tracked separately;
- Round 1 adds local proof packets without claiming new mathematical review;
- `IC-PERIODIC-001` remains pending narrow review of the integrated synthesis.

The active registry is under [`../../claims/registry/`](../../claims/registry/). The readable proof layer is [`../../research/integrated/`](../../research/integrated/README.md).

## Legacy current pointer

[`../../docs/integration/CURRENT.md`](../../docs/integration/CURRENT.md) is retained as a compatibility pointer for old links. The single current front-stage pointer is [`../../STATE.md`](../../STATE.md).

## Why files remain at their original paths

The dated files and machine records are left in place to preserve exact links from PRs, reports, review comments, and external citations. This archive index changes their **navigation role**, not their historical bytes or provenance.
