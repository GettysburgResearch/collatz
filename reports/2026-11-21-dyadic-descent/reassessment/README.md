# Whole-repository reassessment: proof and review evidence

**Full Collatz remains open.** The scientific account is the
[whole-repository synthesis](../../../research/lean-dyadic-descent-20261121/WHOLE_REPO_SYNTHESIS.md).
The complete metadata inventory covers 145 pull requests at the recorded
heads. Source-level mathematical reviews are narrower and identified
explicitly in that synthesis and the individual notes.

## Fresh Lean replay

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records the actual successful fresh
build of **five modules**, followed by the combined **38-theorem audit**.
No local proof `.olean` was reused. The two unchanged inputs are the pinned
PR173 `ShellCover` source and PR182's `OffsetDescent`; the other three
modules are new in this reassessment.

| New module | Audited public theorems | Mathematical scope |
|---|---:|---|
| CoefficientCounting | 8 | Exact parity moment, finite resistant-residue bound, and ordinary interval packing |
| CoefficientPeaks | 16 | Affine-correction budgets, derived finite injectivity, explicit coefficient strip exit and polynomial clock bound |
| CertificateBoundary | 14 | Complete odd certificates, a guarded source-growing reset with strict grade decrease, and exact boundary identities |

Every command used Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with
`-j1 -DwarningAsError=true`. Mathlib was tracked-clean at
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Source SHA-256 values were checked
before and after the fresh run and matched again during archival.

The [audit source](ReassessmentAudit.lean) covers every public theorem
declared by the three new modules. The [parsed audit](AXIOM_AUDIT.json)
records only subsets of `propext`, `Classical.choice`, and `Quot.sound`.
There is no `sorry`, custom closure axiom, or `native_decide` certificate.
Informational tactic suggestions in the captured output do not alter the
successful exit codes or complete axiom coverage.

The four earlier continuation modules and all their imported sources were
also compared with the successful [53-theorem receipt](../continuation/LEAN_RECEIPT.json).
They are unchanged. That earlier compilation was not rerun or relabeled as
part of these six jobs. Together the two checkpoints audit **91 public
statements in seven added Lean modules**, with their separate actual receipts.
This is a statement count, not a claim of 91 mathematically novel results.

## Independent semantic review

[SEMANTIC_REVIEW.md](SEMANTIC_REVIEW.md) records exact source and note hashes
for the separate internal reviews. The coefficient proofs were reviewed by
an agent separate from their implementation, including the finite horizon
and the derivation of injectivity. The certificate proof was compared with
the exact PR177 definitions by another agent, with all guards and the
cross-file formalization boundary retained. Root separately inspected the
mathematical arguments and performed this fresh replay.

The written
[predecessor-population audit](../../../research/lean-dyadic-descent-20261121/PREDECESSOR_POPULATION_AUDIT.md)
is separate from these Lean claims. It reconstructs specific PR180 analytic
steps from their primary input and authenticates source bytes. No theorem
in the Lean packet imports that analytic result as an axiom.

The new
[periodic-approximation rigidity proof](../../../research/lean-dyadic-descent-20261121/PROFINITE_LABEL_RIGIDITY.md)
also received an independent adversarial review. It needs only the earlier
marginal logarithmic-population result, not the later joint-clock
natural-density claim. The review covers the compact mixing argument,
ordinary empirical measures, exact stationarity defect, total-variation
limit and uniform approximation-error bound. It remains a source-qualified
written argument, outside the 38-theorem audit. The ordinary approximation
premise required for global convergence is still open.

The separate
[guard-composition audit](../../../research/lean-dyadic-descent-20261121/GUARD_COMPOSITION_AUDIT.md)
records an unbounded family discharged by a checked eight-step identity
and a nearby finite test case that needs a longer descent. Its exact
bounded arithmetic replays are distinguished from universal Lean statements.

## Reproduction

From a complete checkout:

```sh
python -B research/lean-dyadic-descent-20261121/replay_reassessment.py \
  --mathlib /absolute/path/to/mathlib4 \
  --lean-bin /absolute/path/to/lean-4.34.1-linux/bin \
  --out /absolute/path/to/fresh-build
```

The output directory must be empty and outside the checkout. The runner
checks both imported source pins, the compiler commit, tracked Mathlib
cleanliness, all proof source hashes, and complete theorem audit coverage.

All five required repository checks passed separately in a clean complete
checkout of proof commit `7b0db97835afb4350cd5bad50a4b53b02b72d2c6`, tree
`a2ce647784fc3ae4ef7f4e7c8e8e4bc0709710e3`, with 380 tracked files and an
unchanged checkout. The actual receipt is
[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json). The command was:

```sh
python -X utf8 -B tools/validate.py --receipt /absolute/path/to/checkout-validation.json
```

The final published head and its actual clean complete-checkout receipt are
recorded in the PR description. The previous checkpoint's description and
its exact published-head receipt are retained in
[PR182_BEFORE.json](PR182_BEFORE.json).
