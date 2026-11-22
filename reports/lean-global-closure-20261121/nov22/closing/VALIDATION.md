# Validation of the four direct closing attempts

Date: 2026-11-22. Own parent:
`08fe1388ad63c758680b3695249aca319515c47d`.

## Formal proof actually compiled

The new `CycleMinimum.lean` and its separate `CycleMinimumAudit.lean`
compiled successfully with warnings treated as errors and automatic implicit
variables disabled. Five named declarations were audited. Each uses only
`propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` or new
research axiom appears.

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib source: `d13f23b723b8a846827a245b89c10fc7d3f11612`, clean.
The installed compiled Mathlib and package dependencies were reused.
**Only the two new project sources were freshly compiled.** The 2,456
module names listed in the import manifest are not a dependency rebuild.

The exact source hashes, invocations, elapsed times, compiler output and
object hashes are in [cycle-minimum-source-build.json](cycle-minimum-source-build.json).
The source-controlled driver is
`research/lean-global-closure-20261121/closing/build_cycle_minimum.py`.
It checks the compiler and Mathlib pins and rejects an output directory
containing precompiled project objects.

The formal scope is the product-deficit inequality, the whole finite-cycle
product formula and the natural-number inequality D(3m+1)≤p2^A. The
zero-word/ordinary-point correspondence, count, algorithmic complexity,
Subspace applications and infinite analytic results are written proofs.
Matveev is an external theorem, not a Lean axiom.

## New exact finite controls

`python -X utf8 -B zero_atom.py --large-fiber-control --receipt ...`
passed in the new source folder. The [receipt](zero-atom-control.json)
contains all 99 pairs with 1≤A≤18, 1≤p≤A, and 2^A>3^p. Direct whole-
denominator enumeration covered 453,148 words and matched the ordinary
minimum census at every pair, including the known cycle's repeated
traversals. The separate (A,p)=(27,17) full residue-law control covered
8,436,285 words; its zero count is zero and its maximum fiber is 19.
The complete execution took about 2.55 seconds in this environment.

`python -X utf8 -B check_surplus_repair.py` also passed. Its output
matched the agent's frozen [control](surplus-repair-control.json) byte for
byte; [the independent replay receipt](surplus-repair-replay.json) records
the script and output hashes. This checks the specific complete source,
actual target, every cut through the source clock and every supplied safe
endpoint. It does not prove all-certificate source maximality or a
universal repair selector.

Neither finite control proves an all-period Collatz assertion. No old
bounded census or legacy Lean module was rerun for this checkpoint.

## Written mathematical review

- The potential lane independently reconstructed root's zero-atom count,
  repeated-period accounting and numeric-period complexity. It read the
  primary Matveev statement and the exact repository specialization.
  See [the scoped review](REVIEW_ZERO_ATOM_CLOSING_ATTEMPT.md).
- The arithmetic lane independently reconstructed the original-source
  shadow identity and actual-height inequality. See
  [the scoped review](REVIEW_FIXED_SOURCE_SHADOW_ENTROPY.md).
- Root reconstructed the source-edit horizon and payment control, the
  unequal-depth transport, the actual payoff concentration and required
  witness depth. Root also reconstructed the symbolic repetition control
  relative to the classical Subspace Theorem. Imported canonical
  existence/mixing inputs and recent external manuscripts retain their
  original qualifications. See [the integration reviews](INTEGRATION_REVIEWS.md).

These are independent in-session reconstructions, not external peer review.
The review bindings and file manifest retain exact hashes. No review verdict
extends to the missing universal closing inequalities.

## Exact published-checkout integrity gate

The required `python -X utf8 -B tools/validate.py --receipt ...` is run in
a clean complete checkout of the exact proposed commit before advancing
the PR branch. Its JSON receipt must be outside that checkout. The PR
description records the tested commit, tree, parent, all five command
exit codes, clean-before/after identity, and full receipt SHA256 after the
run. This file records the preceding proof and control evidence; it does
not manufacture a self-referential commit identifier.

The optional historical `--regressions` bundle is not part of this pass.
Repository integrity is distinct from mathematical or Lean verification.
