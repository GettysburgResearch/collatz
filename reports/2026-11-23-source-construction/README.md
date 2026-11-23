# Checkpoint 17: execution and review record

23 November 2026. Scientific entry point:
[finite candidate exactness](../../research/lean-global-resolvent-20261121/overview/source-construction/README.md).
Full Collatz remains open. This report records scoped checks and
reconstruction; repository integrity is not mathematical verification.

## Formal evidence

The new `TriadicCertificateRigidity.lean` has 15 theorem declarations and
two definitions, all listed in the packet's `RIGIDITY_THEOREMS.json` and
covered by its audit. It proves exact paired-cycle entry by 8E, all-time
compatibility of the unchanged supplied candidate, and finite/all-time
equivalence with the literal candidate-dependent horizon.

The executable is Lean 4.34.1, compiler
`5045d0056413266e57c625dcd7c365b10e377c52`. Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Its existing package objects
were reused; the two unchanged project dependencies and new module were
freshly compiled with warnings treated as errors. All three replays
(author, separate reviewer, integration) report only the axiom union
`propext`, `Classical.choice`, `Quot.sound`.

- [Author execution receipt](rigidity-author-receipt.json).
- [Independent mathematical and formal reconstruction](REVIEW_EXACT_CANDIDATE_RIGIDITY.md).
- [Independent fresh Lean replay](independent-lean-replay.json).
- [Integration execution receipt](integration-execution.json).

The original combined author receipt predates a one-sentence n>2 scope
clarification in the construction note. The sealed rigidity proof and Lean
module are unchanged; the final construction receipt and integration replay
bind the clarified note.

The independent reviewer suggested the n=1 simplification during
development; that contribution is disclosed. These are internal agent
reviews, not external peer review.

## Exact controls and their scope

Every new checker passed both normal Python and `python -O`, with
identical output. The controls are exact arithmetic examples, distinct
from the uniform proofs.

| Control | Coverage |
|---|---|
| [Finite candidate rigidity](rigidity-controls.json) | 21 accepted representations, including unreduced denominators; 36 signed terminal defects rejected at their exact two-adic clocks; four zero rejections; one stale-horizon mutation. |
| [Construction attempt](construction-controls.json) | 54 all-target lifts, 12 true-dual identities, 30 complete positive reset chains. |
| [Infinite optimizer](optimizer-controls.json) | 840 exact finite-tail product identities and 371 rational-anchor congruences, on selected actual finite trajectories. |
| [Rational cycle/product control](cycle-controls.json) | 62 small cycles and 12,185 unordered products; 17,065 literal shortcut steps overall. Separate high-floor witnesses have odd periods 11, 17, 253 and 8,286. The large cases check each valuation and legal step, not all quadratic products. Three damaged inputs are rejected. |
| [Independent carry reconstruction](carry-written-review-controls.json) | 168 lifts, 35 selected continuations, 12 true-dual examples, 320 complete reset sequences, and 40 unit-reset valuation levels. |

The general rational-cycle Sidon and arbitrary-floor theorems have
written proofs. No finite enumeration is offered as their proof. None
of these controls proves a universal successful candidate construction.

## Written mathematical review

- [Coordinating reconstruction](ROOT_REVIEW.md) covers the new Lean
  argument's mathematical semantics, the infinite-optimizer attempt,
  the universal rational controls, and literature access scope.
- [Cycle/product reconstruction](REVIEW_CYCLE_PRODUCT_CONTROL.md) checks
  the universal shifted-valuation argument, rational legality,
  primitivity, energy count, and arbitrary-floor construction.
- [Boundary reconstruction](REVIEW_HAAR_AND_ORDINARY_LABELS.md) checks
  the finite clock comparison, conditional joint limit, and exact
  mixed-phase endpoint formula.
- [Carry construction reconstruction](CARRY_CONSTRUCTION_WRITTEN_REVIEW.md)
  checks the all-target lift, denominator law, negative-sector estimate,
  and reset telescope, retaining the n>2 domain of the clock corollary.

The packet's `SOURCES.json` records frozen commits, paths, blobs, hashes,
and inspected scope. `source-refresh.json` records the start-of-turn PR
snapshot. Five peer branches had advanced relative to the preceding
checkpoint. `previous-pr-description.json` preserves our earlier PR body.
No review verdict extends to later peer heads.

## Reproduce the scoped check

From a complete checkout, provide the Lean executable and the prepared
Mathlib tree explicitly:

```sh
python -X utf8 -B research/lean-global-resolvent-20261121/overview/source-construction/verify_checkpoint17.py \
  --lean /path/to/lean-4.34.1/bin/lean \
  --mathlib /path/to/mathlib \
  --receipt /tmp/checkpoint17-scoped.json
```

The runner uses a new temporary build directory, checks the complete
declaration audit, compares normal and optimized checker outputs to the
frozen records, and checks available pinned upstream objects. A missing
upstream object is reported as unavailable, never as verified. All 23
source entries were available and checked during integration.

`manifest.json` binds the packet, reviews, author receipts, frozen
controls, source refresh, and this report. It excludes itself and
`integration-execution.json` to avoid a receipt/manifest hash cycle.
The latter records the manifest hash and exact execution status. Git's
published tree binds both files.

The repository gate is run separately in a clean complete checkout:

```sh
python -X utf8 -B tools/validate.py --receipt /tmp/checkpoint17-integrity.json
```

Its receipt stays outside the checkout and is reproduced in the PR body
for the exact published head. No expensive previous census or historical
Lean suite is replayed by this checkpoint.
