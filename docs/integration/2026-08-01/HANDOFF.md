# Handoff to the next integrator

## Authoritative state

Start with:

1. [`../CURRENT.md`](../CURRENT.md)
2. [`STATE.md`](STATE.md)
3. [`open-prs.json`](open-prs.json)
4. [`REVIEW_COVERAGE.md`](REVIEW_COVERAGE.md)
5. [`../../../claims/registry.json`](../../../claims/registry.json)
6. [`INTEGRATION_REPORT.md`](INTEGRATION_REPORT.md)
7. [`POST_CUTOFF.md`](POST_CUTOFF.md)

The previous cutoff is `2026-08-01T21:16:40Z` / `2026-08-02T00:16:40+03:00`. The frozen main commit is `0ae0c67bb058f9a7c56cc7744fe5bf2650a7cb84`.

## Reconstructing the cutoff

- Check out the frozen main SHA for the base tree.
- For each open PR, use `head_sha_at_cutoff` from `open-prs.json`.
- For a review verdict, use `reviewed_sha`, not the current head.
- The report path and report commit are recorded in `REVIEW_COVERAGE.md`.
- Do not edit this snapshot to incorporate later work. Create a new dated directory and update `docs/integration/CURRENT.md`.

## First post-cutoff observation

At `2026-08-01T21:57:47Z`, `main` was still at the frozen SHA and every source PR head from #3 through #83 was unchanged. The only new open PR was draft integration PR #84. See `POST_CUTOFF.md`. This observation does not alter or extend the earlier review cutoff.

## Deltas already present at this cutoff

The following current heads were ahead of their reviewed commits:

- report-only or review-artifact deltas: #3, #19, #38, #72, #81;
- report plus proposed/strategic delta: #13, #57, #61, #65, #77, #80;
- theorem-bearing unreviewed delta: #83 `L-6916`.

The exact file-level treatment is in `REVIEW_COVERAGE.md`. An older verdict must not be extended to these additions.

## Pending reviews

First examine:

1. PRs #67, #68, and #69, which received no review-wave verdict.
2. Material post-review additions: #13 proposed PR19 repair, #57 `L-7610`, #61 `O-7401`, #65 `L-7502`, #77 `M-6712`, and #83 `L-6916`.
3. Any PR head that changed after the cutoff.
4. Clean extraction packets for #11, #19, #34, #42, and #47.

## Settled organizational decisions

Treat these as the default unless a later integrator records a reasoned migration:

- exact-SHA verdicts;
- branch-qualified source IDs and separate canonical IDs;
- repairs/refutations never overwrite originals;
- mathematical, integration, and artifact statuses are orthogonal;
- stable README, volatile timestamped state;
- exploratory freedom with a lightweight contract only for canonicalization;
- no automatic public-readiness inference from organizational files.

## Provisional decisions

These may be improved with an explicit migration:

- schema version `1.0`;
- the exact set of eight first canonical records;
- claim-level frozen-reference integration rather than immediate proof-file import;
- `SC* + FC*` as the principal roadmap spine;
- the exact canonical ID naming convention.

## What the next pass should examine first

1. Requery `main` and all open PR heads.
2. Diff every changed head against this cutoff and classify each delta as editorial, review-only, proposed, computation-only, or theorem-bearing.
3. Review #67/#68/#69 or keep them explicitly unreviewed.
4. Decide whether the canonical proof bodies for `IC-EXTRACT-001`, `IC-PERIODIC-001`, `IC-SC-001`, and `IC-RIG-001` should be imported into dedicated clean packets.
5. Resolve active dependency debt: PR #81's closed-#82 dependencies, PR #34 pins, source normalizations, and claim-ID collisions.
6. Extract the passing subsets of mixed packets without inheriting blocked headlines.
7. Create a new immutable snapshot and advance `CURRENT.md`.

## Normal checks

Run:

```bash
python3 tools/check_integration_state.py
```

Then run only small source-specific exact checkers needed by changed canonical packets. Do not rerun expensive searches by default. For a large computation, preserve the distinction among code inspection, checker execution, artifact regeneration, and independent full replay.

## Updating without erasing provenance

- Never rewrite an old verdict to match a repaired theorem.
- Add a new source SHA, new claim, or explicit migration.
- Keep the original refutation and its counterexample.
- Preserve source PR, commit, paths, reviewer, review report, dependency pins, and replay state.
- Broad research PRs remain welcome; only canonical integration requires the registry contract.
