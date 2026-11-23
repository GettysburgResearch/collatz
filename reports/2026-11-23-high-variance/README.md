# High-variance checkpoint: execution and review scope

**23 November 2026.** Scientific claims and their unclosed steps are in
the [research packet](../../research/high-variance-20261123/README.md).
This report records evidence for those particular files, not a proof
of full Collatz.

## Lean

- Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Fresh strict compilation of `BalancedCycleUnit.lean` and the exhaustive
  `BalancedCycleAudit.lean`, with `-DwarningAsError=true`; both exit zero.
- Eight theorems and one definition audited, with only `propext`,
  `Classical.choice`, and `Quot.sound`. No admissions or extra axioms.

The [receipt](cycles-receipt.json), [compile log](cycles-lean-compile.log),
[axiom log](cycles-lean-axioms.log), and
[replay instructions](cycles-lean-replay.md) bind the exact module.
The main theorem derives the literal floor numerator, its permutation,
and the actual full-denominator unit. It does not formalize the infinite
prime selection, rational dynamics, real floor or primitivity theorem.

## Written proofs and finite executions

The cycle construction received an independent reconstruction of its
Sections 1–4, including every rotation, full-denominator cancellation,
the real floor, cyclotomic prime selection and primitivity. Two exact
construction controls replay all 97 and 3,089 odd rotations respectively;
normal and optimized Python outputs agree. These are construction
controls, not an exhaustive integer-cycle search.

The rational-dual note has an independent review of its signed product
estimates, zero and sign-change cases, first-event bound and exact finite
terminal-index rejection. Its checker exercises 2,701 cases. The
all-input termination result is a written proof; the finite cases are
implementation evidence. No Lean claim is attached to this lane.

The coordinating agent independently reconstructed the entropy note's
log-odds/entropy bounds, sibling pairing, bilateral trace profile and
finite-path bounded-corrector refutation. The retained canonical trace
inputs remain source-qualified. The review does not certify the
upstream construction or the unproved tightness criterion.

The cycle agent independently checked the exact two-place product,
fixed-tail estimate, Hölder rearrangement and joint all-ones renewal
control. The [review](cycles-review-adelic.md) records its small
`k>=2` density-range correction and verifies the final corrected hash.
It does not certify the external analytic manuscript or infer a
positive-integer escape exclusion.

`REVIEW_SCOPE.json` and `FILES.json` bind the final reviewed scientific
files and separate these evidence levels. Review reports identify their
own exact source versions.

## Repository gate and publication

The required command is `python -X utf8 -B tools/validate.py` in a clean,
complete checkout of the final commit, with its receipt outside the
checkout. The publication record in PR178 reports the exact commit/tree,
the five command results and the external receipt hash after execution.
This report does not predeclare that later gate result.

The previous PR description is preserved in
[pr-description-before.json](pr-description-before.json). The source
refresh covers the 40 most recently updated open PR metadata and targeted
reading of the new PR185 head; it is not represented as a new all-PR
mathematical verification. Historical mathematical modules were not
rebuilt merely to create this checkpoint.
