# Full-problem refocus: centered defects and the first support-fourteen offense

**Agent:** `gpt56-cycle-01`  
**Issue:** #9  
**Branch:** `agent/gpt56-cycle-01/9-compressed-cycle-synthesis`  
**Date:** 2026-07-23

## Starting hypothesis

The previous cycle work had exhausted raw positive-cycle windows through 27 odd terms and several very large low-complexity grammars without a hit. The refocus was:

1. read the newest repository packets rather than extending the same census blindly;
2. identify the smallest structural cycle parameter not already closed;
3. turn that parameter into a proof-producing exact certificate;
4. immediately attack the first newly open layer constructively.

The live repository refresh showed independent convergence on four themes:

- single-, double-, and distributed pulses around known negative cycles;
- a deterministic one-counter refund map whose quotient doubles whenever defined;
- a critical-scale mechanical near-candidate that passes several denominator factors but is rigorously nonintegral;
- centered positive-cycle defects, with the newest cross-direction packet excluding six non-neutral valuations.

The shortest finite-certificate route therefore remained a positive cycle. The exact next support was seven defects.

## Approaches attempted

### Cross-repository synthesis

Read and compared the live heads of PRs #34, #45, #47, #48, #49, and #51. The useful synthesis was:

- finite-state or bounded-pulse schedules keep collapsing;
- arbitrary raw odd-term length is the wrong parameter;
- centering at the trivial fixed point deletes valuation `2` exactly;
- the first potentially constructive cycle parameter is the number and arrangement of non-`2` valuations;
- the refund lane already proves growth after coherent existence, so integrality/ordinary closure—not drift—is the common bottleneck.

### Exact centered-defect classifier

Re-derived

```text
E=C-D=sum_j 3^(k-1-j)2^A_j(4-2^a_j).
```

Used the centered branch

```text
g_a(y)=(3y+4-2^a)/2^a
```

and the elementary floor `y=n-1>=6` for nontrivial positive cycles. Deleting neutral `2`s and lowering high valuations increases replay. Exact contraction tests therefore classify all possible defect multisets.

### Largest-gap finite reduction

Rotated a largest neutral gap to the end. If the core omits this terminal gap, then

```text
D_R=2^B4^R-3^s3^R,
E_full=3^t E_core,
D_R|E_core,
E_core>=2D_R.
```

A positive-term rearrangement bound gives a finite neutral-count cutoff for every surviving type through support thirteen.

### Two exact search architectures

- `X-8603`: lossless maximum-height dynamic programming followed by direct enumeration for supports 7–12.
- `X-8604`: the same height DP followed by an affine meet-in-the-middle residue join for support 13.

Both contain dormant exact reconstruction and valuation replay for any divisor hit.

### First support-fourteen offense

The finite classifier stops at support fourteen. The core `(b,1^13)` satisfies

```text
E-6D=22*3^13+2^b(3^13-2^16)>0
```

for arbitrary `b`, so the high valuation alphabet is no longer bounded by contraction.

Two attacks followed:

- `L-8604` / `X-8605`: complete exclusion of the infinite concentrated-tail family `(b,1^13,2^R)` for all `b>=3`, `R>=0`;
- `X-8606`: exact arbitrary-gap eliminant search through total neutral count `R=12`.

## New results

### `T-8603` — exact support-seven-through-thirteen exclusion

No nontrivial positive accelerated cycle has exactly 7, 8, 9, 10, 11, 12, or 13 valuations different from `2`.

`X-8603`:

```text
contraction_classes=1082
enumerated_rows=2,577,878,885
explicit_cases=421
dp_pruned_cases=512
divisor_hits=0
```

`X-8604`:

```text
contraction_classes=1018
patterns=4,746
pattern_rows=136,508
dp_pruned=109,188
left_states=64,869,934
right_states=64,869,934
queries=64,674,409
hits=0
```

Together with branch-qualified proposed PR #34 `L-9913`, the current proposed chain raises the non-neutral support floor to fourteen.

### `L-8604` — exact infinite concentrated-tail exclusion

For every `b>=3` and `R>=0`, the word

```text
(b,1^13,2^R)
```

is not a nontrivial positive cycle.

An exact eliminant caps `b` for `R<=3`; the height inequality caps it for `R>=4`; a recurrence proves every row after `R=15` permanently empty. Exactly 83 powers of two survive the bounds and none divides.

### `X-8606` — arbitrary-gap eliminant scout

For one arbitrary high defect among fourteen and arbitrary neutral-gap distribution, every fixed gap row has

```text
E_core=P(gaps,position)2^b+Q(gaps,position),
D=L_R2^b-T_R.
```

The eliminant removes `b`. Frozen exact scope:

```text
0<=R<=12
gap_vectors=1,025,557
rows=14,357,798
powers=29,391,300
zero_eliminants=0
hits=0
```

This is finite evidence only, but it is targeted at the first unbounded support-fourteen family rather than at arbitrary raw cycle length.

## Candidate counterexamples

None. No divisor hit appeared, so no integer reached the valuation-replay candidate stage and no `K-####` identifier was assigned.

## Failed approaches and negative information

1. The support-fourteen classifier genuinely changes character; simply adding another finite high alphabet would be incomplete.
2. Concentrating every neutral `2` in one terminal gap produces no cycle for any parameters.
3. The first 14.3 million arbitrary-gap eliminant rows have no zero eliminant and no hit; this does not justify extrapolation.
4. The newest cross-direction work shows additive one-counter finite control produces ultimately periodic output, while the refund construction needs nonstationary arithmetic memory.

## Potential errors and adversarial targets

- Independently reconstruct every monotone defect classification, especially supports 12 and 13.
- Reimplement the 2.57-billion-row `X-8603` direct census rather than merely replaying its code.
- Audit the support-thirteen split orientation and target residue in `X-8604`.
- Verify that tied largest gaps create only duplicate coverage, never a missing rotation.
- Reconstruct the support-fourteen eliminant signs and the persistent `R>=15` bound in `L-8604`.
- Keep non-neutral valuation count distinct from odd-term count and external local-minimum count.

## Files changed

```text
research/compressed-cycle-synthesis/claims/T-8603-centered-defect-frontier.md
research/compressed-cycle-synthesis/claims/L-8604-one-high-concentrated-tail-exclusion.md
experiments/X-8603-centered-defect-frontier/
experiments/X-8604-thirteen-defect-mitm/
experiments/X-8605-one-high-concentrated-tail/
experiments/X-8606-one-high-gap-eliminant/
reports/gpt56-cycle-01/2026-07-23-9-centered-defect-refocus.md
```

## Claims affected

- new `T-8603` — `PROPOSED / EXACT FINITE CERTIFICATE`;
- new `L-8604` — `PROPOSED / EXACT FINITE CERTIFICATE`;
- new experiments `X-8603` through `X-8606`;
- no candidate or root ledger status promoted.

## Recommended next actions

1. Finish the arbitrary-gap one-high support-fourteen family for all `R` by combining the eliminant with a gap-vector meet-in-the-middle or zero-eliminant classification.
2. If that family closes, classify the two-high support-fourteen antichain rather than reverting to raw odd-term length.
3. In parallel, test whether the refund counter’s exact most-significant closure can be encoded by the same kind of eliminant; growth is already supplied by PR #49/PR #48 once existence is closed.
4. Request one independent mathematical classifier review and one independent computational join implementation before promoting `T-8603`.

## Organizational improvement idea

Maintain one shared full-objective frontier table whose rows are certificate architectures and whose columns are ordinary initialization, exact transition replay, infinite consistency, positivity, growth/nontermination, and current minimal open parameter.

For the cycle lane, the current minimal open parameter is no longer odd-term length: it is the arbitrary-gap, one-high support-fourteen eliminant family. This prevents future agents from spending large compute on regions already structurally dominated by the centered-defect result.