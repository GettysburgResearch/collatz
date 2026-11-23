# Checkpoint 9 execution and review evidence

The scientific entrypoint is
[the whole-repository packet](../../research/lean-global-resolvent-20261121/overview/whole/README.md).
This report records execution and narrowly scoped review, rather than a
second account of the mathematical frontier.

## Fresh formal replay

[checkpoint9-lean.json](checkpoint9-lean.json) records the new portable
driver's actual execution against Lean commit
`5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

- 16 frozen project imports compiled from their bound source files.
- All three new proof modules compiled, and both separate audits compiled.
- All 21 commands exited zero with warnings treated as errors.
- All 37 new public theorem audits passed: 12 arithmetic, 13 dispatcher, and
  12 joint-induction declarations.
- Axiom union: `propext`, `Classical.choice`, `Quot.sound`.
- Every source and audit hash was unchanged by execution.
- The optional dependency mirror was checked against the pinned original
  object/IR artifacts before being placed on the import path.

The new source hashes are:

| Module | SHA256 |
| --- | --- |
| `BlockRepetitionBudget.lean` | `25acb2f01cb05101aed116b986ff6d4fafd4eba7c90f3be58bf83174c82921da` |
| `Collatz/AffineDispatcher.lean` | `d59528865a8b1111e3b3d452eb1c4034930d6eb849c5e9a1a4398c7acda7542d` |
| `Collatz/SourceTargetInduction.lean` | `fa8269cf53fc0cd8f59022242354552c93b61d0788707da6100cd7b053c16ad0` |

The formal receipt does not certify the written transcendence argument or the
source-qualified infinite analytic conclusions. It verifies the finite
theorem types and exact imports listed in the manifest.

## Exact physical examples

[checkpoint9-examples.json](checkpoint9-examples.json) records the successful
integer replay of the one-pass failure and the symbolic all-parameter affine
repair. The replay checks every source valuation, source clock, affine degree
and offset, maximal paid ceiling, and the actual target endpoint. It also
checks the credited ray at every parameter through exact affine propagation
with constant parity, rather than sampling a finite range of parameters.

The deliberately incorrect alternative slope 768 is retained as a diagnostic:
its endpoint slope is 2187, so it does not match the partner ray's slope 729.
The diagnostic is not an independent new research result.

## Mathematical reading and cross-review

Three parallel attacks produced the arithmetic, dispatch, and analytic
developments. Root independently read their actual arguments and theorem
types before integration. A second reader reconstructed the arithmetic
rotation and cutoff and checked Matveev's original constant convention. The
finite automaton description was clarified to cover every starting phase and
reject the all-zero exponent tuple. No change to its Lean arithmetic source
was required.

The analytic note received a separate mathematical cross-read of the global
antichain, Green representation, capacity identity, total-variation formula,
and physical source-tail bound. Its source-qualified inputs are unchanged.
An initially ambiguous comparison of qualitative short-contact decay with
the prior finite-front bound was corrected to retain the stronger upper
estimate available under the joint hypotheses.

A prepublication refresh found the 52-theorem continuation of PR183 at
`68345f60a4f757acb42a69a4ac95910f8ce26163`. It was read without replaying
its modules. The three lanes identified the exact overlap and developed
the sharper complete-word cutoff, the joint source-grade/target kernel,
and the `L²(eta)` source-tail extension. The final integrated replay above
includes the additional 12-theorem joint kernel. The written channel
extension received a second reconstruction of its uniform Cauchy–Schwarz
and finite-support limit arguments. Upstream theorem counts are not added
to this checkpoint's 37 audits.

[pr-snapshot.json](pr-snapshot.json) retains the complete 145-record metadata
inventory. The selected source and review ledger identifies the actual
arguments used. No full mathematical replay of all PRs was performed or
claimed.

## Publication gate

Publication runs `python -X utf8 -B tools/validate.py` on a complete clean
checkout, with its receipt outside that checkout. The five default structural
checks are separate from Lean execution and mathematical review. The actual
published commit and the final remote read-back are recorded in PR176.

The older 44- and 94-theorem packets were not optionally replayed again. Only
the dependency closure needed for these new formal statements was rebuilt.
