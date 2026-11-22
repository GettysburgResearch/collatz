# Checkpoint 10: execution and evidence

The scientific entry point is the
[profound-step packet](../../research/lean-global-resolvent-20261121/overview/profound/README.md).
This report records new execution, rather than relabeling the previous
checkpoint's receipts. Full Collatz remains open.

## Fresh integrated Lean replay

[checkpoint10-lean.json](checkpoint10-lean.json) records a fresh output
directory, every command, exit code and source hash before and after the
run. All **25 jobs passed**, with **50 new public statements audited**.
No source changed during the replay.

| Module / audit | Audited statements | Scope |
|---|---:|---|
| `Collatz.HeadThreeTarget` | 13 | Actual head-three transports, same-source success rule, exhaustive failed phase, `[3,3]` family, and original-target height guard. |
| `FirstCrossingBound` | 21 | Actual shortcut coefficients, first-hit clocks, all-depth finite boundary, explicit native-cardinality interface, dyadic and bounded-potential interfaces. |
| `SquaredSurvivalBudget` | 8 | Reciprocal hazard identity, finite telescope with remainder, summability and complete scalar budget. |
| `BinHeight` | 8 | Actual shortcut odd count, squared-height budget, ceiling-power comparison and original-source bin-height bound. |

The eighteen reused project modules were compiled only because they are
the exact import closure of the new head-three proof. Their older theorem
audits were not counted as new results. The dependency-free head-three
closure and the separate Mathlib modules retain their respective imports.

Environment pins:

- Lean 4.34.1, commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Every new compile used `-j1 -DwarningAsError=true`.
- The optional mirror's 8,620 object/IR artifacts were authenticated
  against the pinned dependency tree before use.
- The complete audited axiom union is `propext`, `Classical.choice`,
  and `Quot.sound`. There is no `sorryAx` or custom analytic axiom.

The numerical no-descent substitution, infinite-source bookkeeping,
real-power asymptotics and moving-window limit are not advertised as
formal consequences of these modules without their written arguments.
The canonical weighted-boundary synthesis additionally retains its pinned
source-qualified analytic inputs.

## Exact supporting arithmetic

[supporting-execution.json](supporting-execution.json) records the two
exact integer inequalities used by the written native no-descent count,
the new evaluator command, and hashes of its source and output.

The [bin-four certificate](bin4-enclosure.json) encloses the complete
infinite original-source sums with endpoint exponent `1/4`. It retains
odd sources through 667, encloses the fourth-root endpoint weights using
integer inequalities at denominator `2^24`, and adds the proved omitted
source tails. Rounded outward to the shown decimal places:

| Complete statistic | Enclosure |
|---|---|
| `W_4^(1/4)` | `[0.190867651750, 0.191867155733]` |
| `B_4^(1/4)` | `[0.023172689310, 0.024671941861]` |

The exact endpoints are rational numbers in the JSON. This is one
finite-bin enclosure, not evidence that the sequence tends to zero. The
algorithm uses the proved finite bin clock even for a hypothetical
nonconvergent source; no finite-termination assumption is built into it.

## Reviews and publication gate

The [source/review ledger](../../research/lean-global-resolvent-20261121/overview/profound/SOURCES_AND_REVIEW.md)
records independent reconstructions by the other mathematical agents.
They are distinct from compilation and from external peer review.

After committing the complete packet, publication runs the required
`python -X utf8 -B tools/validate.py` gate in a clean complete checkout.
The final PR update records the actual published head and gate result.
That integrity gate is separate from the Lean receipt and is not evidence
of a full Collatz proof. No main-branch history, other contributor PR,
workflow or repository setting is changed by this checkpoint.
