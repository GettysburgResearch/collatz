# Continued proof and execution evidence

**Full Collatz remains open.** This report concerns the continuation after
published PR182 checkpoint `45354128f890fb479f6c23b547368bcddd9cebe6`.
The [scientific synthesis](../../../research/lean-dyadic-descent-20261121/CONTINUED_SYNTHESIS.md)
separates the new positive deductions and their exact remaining obligations.

## Fresh Lean execution

The actual fresh replay started at `2026-11-22T05:17:16.534386+00:00` and finished at
`2026-11-22T05:17:31.212806+00:00`. All three invocations succeeded:

| Compilation unit | Exit code | Seconds |
|---|---:|---:|
| PolynomialLift.lean | 0 | 7.602 |
| HarmonicCapture.lean | 0 | 4.589 |
| ContinuedAudit.lean | 0 | 2.486 |

The compiler was Lean4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with tracked-clean Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The output directory was initially
empty. Both new modules are self-contained relative to focused Mathlib
imports; no prebuilt local proof module was reused. Commands ran sequentially
with `-j1 -DwarningAsError=true`.

The combined audit covers **22 public statements**: twelve in
`PolynomialLift` and ten in `HarmonicCapture`. Their complete dependency
closures contain only subsets of `propext`, `Classical.choice`, and
`Quot.sound`. No `sorryAx`, native decision axiom, custom convergence axiom,
or external analytic hypothesis supplies these statements.

The [actual receipt](LEAN_RECEIPT.json), [all-declaration inventory](AXIOM_AUDIT.json),
and [generated audit](ContinuedAudit.lean) preserve the results. The portable
runner is [replay_continued.py](../../../research/lean-dyadic-descent-20261121/replay_continued.py).
All proof-source hashes matched before and after the replay.

The earlier 117 statements and their original receipts remain unchanged.
The combined inventory is **139 statements in eleven added modules**.
This is neither a novelty count nor a claim that all eleven modules were
freshly replayed in this round.

## Mathematical and review scope

The polynomial module proves the exact substitution representation and
commutator algebra on arbitrary polynomial functionals. Compact solenoid
realization, Haar ergodicity, ordinary-limit transfer, and the approximation
gap are written mathematics. Their marginal-density/FLOOR/LOG input pins
remain explicit. Classical polynomial Weyl equidistribution is the new
external equidistribution input.

The Green module proves finite identities and real-series comparisons,
with the required limit and bounds supplied explicitly. Existence of the
actual ordinary harmonic reference, source transport, path-law comparison,
global moments, and weighted Tonelli conclusion are source-qualified written
applications. Killing on all periodic states and the spatial weight are
retained. No unweighted absorption or cycle exclusion is inferred.

[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) records the independent internal
review scopes and exact mathematical byte pins. These are collaborating-agent
reconstructions, not external peer review or Lean verification of the
written analytic applications. The root separately read the full arguments.

## Source identity and publication

[SOURCE_BINDING.json](SOURCE_BINDING.json) binds the successful replay,
reviewed notes, runner, and [clean-checkout receipt](CHECKOUT_VALIDATION.json).
The actual published-head repository receipt is embedded in the updated PR
body after the remote write, avoiding a self-referential receipt commit.
The five default repository checks are an integrity gate, separate from
mathematical proof checking. No optional regression bundle is represented
as a new execution.

[PR182_BEFORE.json](PR182_BEFORE.json) preserves the previously published
head, complete description, and its actual published-checkout receipt.
