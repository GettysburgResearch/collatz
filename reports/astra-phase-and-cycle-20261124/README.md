# Execution and review record

**Collatz remains open.** This report distinguishes executed arithmetic controls, written mathematical review and actual Lean compilation.

## Written work and independent review

The phase and cycle arguments were developed by separate GPT-6.2 Astra workers. The cycle worker independently reconstructed PS1–PS6, including the actual scalar identities, dyadic and ternary endpoint estimates, two-step terminal permutation, convergence witness and exact fiber classification. The phase worker independently reconstructed the new cyclotomic degree count and exceptional component splitting. The integrating reviewer checked those mathematical interfaces and their inherited assumptions. The exact review boundary appears in the packet's review files.

The complete cycle-size corollary retains the specific PR185 linear-forms/certificate input. The full analytic proof of that input was not rebuilt or newly formalized. No whole-project theorem acceptance is claimed.

## Exact arithmetic controls executed by the integrating agent

[EXACT_CONTROLS.json](EXACT_CONTROLS.json) pins the tested scripts and their output hashes. Normal and optimized Python returned identical output in each case.

- [Phase controls](phase_controls.json): 2,385 distinct literal ordinary states, 209 positive-carry lowest-digit transitions including 143 resets, 23,850 shifted-grid checks, all 3,279 canonical words through length seven with both kinds of witnesses, 29,523 terminal permutation cases through level nine, and 654 complete scalar-fiber/modulus comparisons. The largest certified convergent witness has 39,362 binary digits.
- [Cycle controls](cycle_controls.txt): 8,031 primitive words, 14,317 homogeneous components, 1,649 positive prime-power instances, four literal rational cycles and six simultaneously saturated nonzero component norms.
- Independent phase review: a separately derived terminal-congruence formula verified all 1,092 words through length six. The separate fiber review grouped 16,290 legal two-step gap pairs and checked six ternary precisions. These are review checks, not counted as additional author controls.

Finite controls do not establish the unbounded mathematical assertions.

## Lean execution status at this checkpoint

The pinned Lean 4.34.1 compiler was installed and actually executed. The exact Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612` and its cache were obtained. Earlier environment absence is therefore not the status of this session.

Successfully compiled in the worker's recorded checks: the byte-exact upstream actual-scalar file, the `Std` lower-run kernel, the `Std` infinite ordinary-shadow theorem, and the immutable PR191 `TwoSidedPacking.lean`. The latter printed 13 axiom reports containing only standard Lean axioms. This checkpoint does not yet assert a complete new dependency replay: the actual-scalar bridge modules and aggregate audit are awaiting the final sequential execution receipt.

An initial sequential attempt to replay the other newly uncompiled upstream candidates was interrupted during its first file under severe shared storage pressure. No file completed in that attempt, and no kernel status is assigned from it. The new contribution uses a separately documented fresh-source replay. Header/visibility ports, if needed, are recorded explicitly and do not change statements or proof bodies.

The final head-bound receipt will replace this pending paragraph only after successful execution. No pending Lean file is claimed checked on the basis of written review.
