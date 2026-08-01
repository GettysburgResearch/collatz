# State at the first major integration cutoff

## Public mathematical status

The Collatz conjecture remains **unsolved**. This snapshot contains no accepted divergent positive integer, no accepted nontrivial positive cycle, and no proof that every positive integer reaches `1`.

## Integrated canonical layer

This pass creates claim-level canonical records for:

- `IC-EXTRACT-001` — ordinary extraction by canonical stabilization;
- `IC-GHOST-001` — explicit 2-adic completion ghost;
- `IC-PERIODIC-001` — periodic tails and the complete denominator;
- `IC-SC-001` — coefficient-stopping/source-escape equivalence;
- `IC-AUT-001` — finite-safety cofinite-tail obstruction;
- `IC-RIG-001` — six-branch finite tame-section rigidity;
- `IC-REF-001` — the refuted universal factor-complexity claim;
- `IC-REP-001` — its distinct nonconstant repair.

These are integration records, not rewritten source histories. Exact source commits and reviews are in [`claims/registry.json`](../../../claims/registry.json).

## Review coverage

The pre-public wave reviewed 42 of the 45 open PRs at frozen commits. PRs #67, #68, and #69 remain unreviewed and receive no verified classification here.

Branch-level blocked or rejected packets remain blocked even when they contain useful claim subsets:

- PR #11: rejected as a monolithic theorem packet; a narrower salvage packet is still needed.
- PR #19: blocked at branch level; exact H-cylinder/ghost/decoder claims passed, while source- and computation-dependent headlines remain qualified.
- PR #34: blocked as a monolith; a reviewed cycle/method-boundary subset should be extracted separately.
- PR #42: blocked by unreplayed or missing headline artifacts, despite verified reductions.
- PR #47: blocked by identifier/file mismatch and an unreplayed billion-pair dependency, despite verified subchains.

## Strategic architecture

The repository-wide roadmap is organized around two open obligations:

```text
SC* + FC* => no least positive counterexample
```

`SC*` requires one fixed ordinary source to stop being coefficient-supercritical. `FC*` requires complete first-crossing/full-denominator exclusion, including positive cycles. Their verified interfaces are integrated; the obligations themselves remain open.

## Computation boundary

No expensive computation was rerun in this integration pass. Review reports distinguish:

- symbolic reconstruction;
- small targeted exact checks;
- artifact inspection;
- independent checker structure;
- full large-run replay.

Unreplayed large computations retain neutral qualifiers and are not promoted to all-depth claims.

## Organizational status

PR #74 is **extracted and revised**, not adopted wholesale. Its exact-SHA semantics, status separation, contributor freedom, bounded-CI principle, and private-baseline cautions are retained. Its proposed public-launch structure, license/readiness assertions, security channel, visibility actions, settings checks, and owner actions remain deferred.
