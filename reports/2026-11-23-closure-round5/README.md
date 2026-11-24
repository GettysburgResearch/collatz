# Round-five review and execution record

23 November 2026. Parent checkpoint:
`cb1ae1bb4af0c8d082e9ff466b9fe0c84932301c`.

The [science entry point](../../research/closure-round5-20261123/README.md)
states the results and their open boundaries. These records are
in-session source reviews and executions. They do not record outside
peer acceptance or a proof of the Collatz conjecture.

## Fresh Lean execution

`LEAN_RECEIPT.json` records five successful compilation commands in
an initially empty output directory:

1. Unchanged `CycleWordAlgebra.lean`.
2. Unchanged `CarryFibers.lean`.
3. New `FixedSourcePressure.lean`.
4. New `TriadicConstruction.lean`.
5. New `RoundFiveAudit.lean`.

The compiler was Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Builds used one thread,
warnings as errors, and the fresh output directory first in `LEAN_PATH`.
All **15 new public declarations** were audited. Only `propext`,
`Classical.choice` and `Quot.sound` appear. Input hashes were checked
before and after compilation.

The seven source-pressure declarations formalize actual finite ordinary
coding, source congruence, height injection and word cardinalities.
The eight rational-accounting declarations formalize exact local
contraction, signed charges, the binomial product and the final numerical
contradiction. The complete recognition theorem, visited-state accounting,
entropy inequalities, stationary limits, dimension theorem and all-
threshold cycle construction remain written proofs.

The receipt retains exact commands and output. To reproduce, use the
pinned compiler and Mathlib, place a fresh directory first in `LEAN_PATH`,
and compile the files in the order above. The older Lean corpus is
preserved by exact hashes; it was not all recompiled in this round.

## Exact finite execution

`EXACT_RECEIPT.json` records normal and optimized execution of the
combined `exact_replay.py`. Both exited zero, and their output files
are **byte-identical**. Each output binds ten final mathematical,
Lean and Python source files. AST inspection found no Python `assert`
statements; all verification guards use explicit failures.

### Rational candidate controls

The independent oracle follows each of 515 known convergent ordinary
sources to 1, then pulls the exact complementary terminal value 2
backward with `Fraction`. It does not reuse the recognizer's decision
events or budgets. The largest observed stopping time was 329 shortcut
steps, within the explicitly capped fixture computation.

| Control | Executed count |
|---|---:|
| All candidate decisions | 36,501 |
| Accepted / rejected | 3,144 / 33,357 |
| Exact, unreduced and perturbed known candidates | 4,635 |
| Bounded grid across all three strategies | 31,680 |
| Nontriadic pullback decisions | 180 |
| Explicit repeated-small rejection decisions | 6 |
| Literal paired trace edges | 2,115 |
| Exact denominator-three reductions checked | 360 |
| Large single-step controls | 56,432 |
| Consecutive large-step controls | 23,576 |
| Exact central-binomial product controls | 64 |
| Invalid inputs rejected | 12 |

The bounded grid uses sources 1 through 40, signed numerators -16
through 16, and odd denominators 1 through 15. The oracle sources
are 1 through 512 plus 6171, 77031 and 837799. Nontriadic controls
retain residual denominators 5 and 7 through actual proper prefixes.
Fifteen original-one controls refute the contraction claim without its
terminal guard. A nontrivial positive ordinary repeated-pair acceptance
is explicitly **not exercised**; no such cycle is asserted to exist.

### Actual source-pressure controls

For 259 known convergent sources (1 through 256 and the three larger
sources above), the checker retains original integer states and tests:

| Exact finite control | Count |
|---|---:|
| Complete ordinary affine word identities | 77,686 |
| Original source-word fibres | 44,055 |
| Uniform long-word laws | 616 |
| Literal ordinary odd edges | 4,203 |
| Reversed-gap source/endpoint identities | 12,869 |
| Unique good gap words above the actual height | 5,175 |
| Finite truncated averaging inequalities | 3,594 |

The last comparisons use `Fraction` arithmetic, the exact original
endpoint ratio, truncations 1, 2 and 5, and rational center `3/2`.
They check finite normalization and arithmetic, not ergodic convergence
or infinite entropy by numerical experiment.

### Complete carries and rational cycles

The carry replay enumerates all **6,884** positive gap compositions
with at most five gaps and total binary clock at most 16. It compares
an explicit backward sum to an independent chronological recurrence,
then checks both complete-carry injection and the retained
residue/total-clock/full-quotient injection. It checks **7,126** finite
fibre bounds and records collision witnesses when a retained coordinate
is omitted.

For circuit parameters `2<=p<=24`, `1<=h<=24`, the 22 cases with
positive denominator and least state above 1 supply 482 literal
rational edges, 482 complete rotated carries, 460 proper coefficient
checks and 22 ordinary least-residue descents with 482 literal integer
edges. Four cases have a nontrivial full gcd; the greatest is 65.

Four larger threshold fixtures retain the full numerical gcd and use
exact closed forms, modular inversion and whole-run divisibility.
Their long state trajectories and rotated carry lists are **not
enumerated**. The largest fixture has binary clock 75,235 and reduced
denominator bit length 75,219. Finite execution is not substituted for
the written all-threshold theorem.

Reproduce all controls from the repository root:

```bash
python -X utf8 -B research/closure-round5-20261123/exact_replay.py
python -O -X utf8 -B research/closure-round5-20261123/exact_replay.py
```

## Independent review and identity

- `ENTROPY_CYCLE_REVIEW.md` independently reconstructs both entropy
  theorems, the direct odd-gap strengthening, the critical symbolic
  control, the rational certificate and both finite Lean cores.
- `RATIONAL_SOURCE_REVIEW.md` independently reconstructs the root
  recognizer, the complete circuit obstruction and the ternary
  information argument. It distinguishes its author's own rational
  accounting from those independent reviews.
- `TERNARY_PRESSURE_REVIEW.md` independently reconstructs the final
  ternary theorem and its same-source consumer. A separate section
  reviews the combined checker's finite source-pressure calculations.
- `ROOT_REVIEW.md` records the principal reconstruction of the three
  attacks and source review of both lane replay modules, with authorship
  and execution boundaries retained.

Each review states whether it is mathematical/source reconstruction or
execution. Source SHA-256 bindings prevent a review from silently
extending to later edits. `PR182_BEFORE.json` preserves the preceding
PR metadata and description; the new research `SOURCES.json` records
the refreshed exact source heads, blobs, claims and literature scope.

## Complete checkout gate

`CHECKOUT_VALIDATION.json` records the clean complete local science
checkpoint before the final two receipt files were added.
`SOURCE_BINDING.json` binds that checkpoint's files and all 44 older
tracked Lean files. The default five-command gate checks repository
structure, frozen identities and selected bounded regressions. It is
separate from mathematical verification.

After publication, a fresh detached complete checkout of the exact
remote head is validated again, and its source/report, older-Lean and
compiled-input bindings are read back. The PR reports that published
head check, avoiding a self-referential commit hash in this receipt.
