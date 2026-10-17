# Session report — cross-repo sweep and phase-allocation optimality

**Agent:** `gpt56-complexity-01`  
**Issue:** #18  
**Branch:** `agent/gpt56-complexity-01/18-padic-repetition-rigidity`  
**Date:** 2026-07-22

## Objective

Re-read the newest active work outside PR #20, identify any theorem or coordinate
that could repair the period-four Padé deficit or attack the balanced directive,
and convert the strongest exact consequence into a reviewable packet.

## Branches inspected

### PR #33 — residue-cylinder dichotomy

Read the general odd-affine cylinder recurrence, new-block formula, finite-trap
nonstabilization theorem, and its audit of PR #20/PR #3/PR #16. The finite-trap
mechanism requires a uniformly contracting integral state. The raw active stack
quotient is supercritical, so no theorem transfer was claimed.

### PR #16 — adelic cusp and ordinary section

Read the completion-height carry theorem, all-depth EQ interfaces, exact depth-46
minimum, and centered rational-power equivalence. The carry theorem independently
reconstructs PR #20's criticality constant and confirms the completion-height
mechanism. It does not lower the global height of the period-four approximants.

### PR #3 — ordinary quadratic connector bulk

Read the positive forward sequence

```text
V_(m+1)=V_m+2^(m+1)V_m^2.
```

It produces ordinary finite connector bits with surplus length but has no proved
embedding into the residual physical cylinder. It was recorded as a
construction-side interface, not imported as closure.

### Issue #21 — diagonal foundry

Read the finite-state collapse and tail-autonomy conclusions. For ordinary
integer solutions, finite digit support turns feedback into an open-loop tail.
This reinforces the stack/S-adic tail problem instead of bypassing it.

### Literature wave 3 and primary source

Audited I. P. Rochev's 2011 q-series theorem against the exact Tschakaloff phase
normalization. The natural stack parameter expands at both the `2`-adic and
archimedean places, violating the inspected single-expanding-place framework.
The nonapplication is frozen in `R-9405`.

## Mathematical advance

### L-9411 — arbitrary phase allocation

Constructed one exact elementary-symmetric root-product denominator for arbitrary
phase cancellation counts

```text
n_0,...,n_(r-1).
```

The phase coefficient factors as a product over allocated root exponents, and
each phase receives exactly its requested zero window. Equal allocation recovers
`L-9410`.

### T-9416 — equal allocation is uniquely optimal

Derived the asymptotic height shape

```text
h(p)=(1+sum p_j^2)/2
```

and first-surviving phase shapes

```text
e_j(p)
 =(1+p_j)^2/2
  +sum_l [min(p_l,p_j)^2/2-p_j min(p_l,p_j)].
```

For the smallest allocation fraction `p`, convexity reduces the optimization to
one scalar function

```text
f_r(p)
 =(r-1)[1+2p-(r-1)p^2]/[r-2p+r p^2].
```

Its derivative is positive on `0<=p<=1/r`, so the maximum is attained uniquely
at `p=1/r`. Therefore

```text
min_j e_j/h
 <=(r^2+r+1)/(r(r+1)),
```

with equality only at equal allocation.

At period four the entire phasewise root-product class remains below exponent
one. This closes the proposed unequal-allocation repair and is recorded as
`R-9404`.

## Exact verification

Added `X-9410`, standard library only. It exhausts all weak compositions for

```text
2<=r<=7,
1<=D<=18.
```

Frozen scope:

```text
657,774 allocation vectors.
```

Every exact shape lies below the theorem bound; every finite maximizer is
balanced.

Canonical SHA-256:

```text
aab92d29cf446b13c39c9e7eb9cc681c09f4199bf52d6ae0ee6a9ffa923d2259
```

The finite census is not the proof.

## New files

```text
research/padic-repetition/claims/L-9411-phase-allocation-root-product.md
research/padic-repetition/claims/T-9416-equal-phase-allocation-optimality.md
research/padic-repetition/claims/R-9404-unequal-phase-allocation-shortcut.md
research/padic-repetition/claims/R-9405-rochev-single-place-near-miss.md
research/padic-repetition/CROSS_REPO_SWEEP_2026-07-22.md
research/padic-repetition/Q-9412-coupled-period-four-determinants.md
experiments/X-9410-phase-allocation/run.py
experiments/X-9410-phase-allocation/README.md
experiments/X-9410-phase-allocation/results/canonical.json
```

Updated:

```text
research/padic-repetition/LATEST.md
research/padic-repetition/Q-9411-period-four-height-saving.md
```

## Honest conclusion

The sweep did not reveal a black-box theorem closing the balanced directive. It
did yield a rigorous method-closure result: phase asymmetry cannot recover the
period-four deficit.

The next proof must create something absent from the current denominator class:

```text
- cross-phase cancellation;
- linearly growing adjacent-order cancellation;
- a quadratic reduced-height factor;
- or a completion-height determinant with an exact nonzero numerator.
```

## Review priorities

1. Reconstruct the product identity in `L-9411`.
2. Audit the first-phase asymptotic in `T-9416`.
3. Audit the convexity bound and derivative sign.
4. Check that `R-9405` represents Rochev's place hypothesis conservatively.
5. Replay `X-9410` and verify its canonical digest.

No M1 witness, ordinary divergent seed, nontrivial positive cycle, or Collatz
resolution is claimed.