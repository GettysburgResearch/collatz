# Exact six-branch descent packet — `73xx`

**Agent:** `gpt56-cycle-01`  
**Issue:** `#58`  
**Base:** draft PR `#64`, `agent/gpt56-extraction-01/58-six-branch-least-root`  
**Status:** no ordinary infinite root or Collatz counterexample; exact descent-classification theorems

## Objective

This packet attacks only the ordinary-extraction decision for

```text
P=3^12=531441,
Q=2^19=524288,
A={229376,258048,290304,326592,367416,413343},
Q*x_(n+1)=P*x_n+a_(i_n).
```

If the nested least roots `m_n` are bounded, they stabilize at one explicit
positive integer and the branch-qualified physical seed is `6*m-5`. If they
tend to infinity, the complete fixed chart is eliminated.

The packet does not extend finite survival depth. It asks whether a smaller
ordinary legal root can be manufactured from one hypothetical legal orbit.

## Main results

- `L-7301` gives the exact two-point cocycle

  ```text
  z_n=u*x_n+v*x_(n+1),
  Q*z_(n+1)=P*z_n+u*a_(i_n)+v*a_(i_(n+1)),
  ```

  and classifies **every** integer pair with contraction factor
  `0<u+v*P/Q<1` that produces even one allowed digit.
- `T-7301` proves that none of those contracting pairs can remain legal on an
  infinite positive orbit. The only recurrent edge graphs are constant-type;
  the only non-diagonal graphs are the finite ascent `0->1->...->5`.
- `T-7302` proves that every fixed finite-order integer-affine sliding filter
  carrying the complete six-branch language is a trivial time shift.
- `L-7302` records the exact vertical type-shift conjugacy
  `a_(i+c)=(9/8)^c a_i` and proves that the least positive all-time root, if it
  exists, must use type `0` somewhere.

While this packet was being completed, the base branch added PR #64 `T-7403`,
which proves the stronger finite **rational-function** nucleus rigidity theorem.
The overlapping local polynomial draft was therefore withdrawn rather than
published under a duplicate `73xx` claim.

The two results are complementary:

```text
T-7403: finite-control rational sections of the complete rooted subtree;
T-7302: fixed finite-window affine filters of consecutive physical orbit states;
T-7301: path-specific fixed two-point contractions on one hypothetical orbit.
```

## Exact experiment

`X-7301` contains two independent standard-library implementations of the
finite Diophantine classification. They agree on:

```text
contracting integer two-point forms: 75
constant-type diagonal forms:        73
non-diagonal forms:                    2
other forms:                           0
```

The two exceptional forms are

```text
(-8,8): i -> i+1, output i,
(-9,9): i -> i+1, output i+1.
```

The semantic digest is

```text
2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f
```

## Honest boundary

These results close broad descent mechanisms but do not decide `m_n`.
A positive proof still needs one explicit finite root and an all-time nonlinear
ordinary invariant. A negative proof may now assume that no fixed two-point
linear contraction, no finite-order affine sliding filter, no finite rational
full-subtree nucleus, and no semilinear sanctuary can supply the missing
self-descent.

## Review order

1. `claims/L-7301-two-point-cocycle-classification.md`
2. `experiments/X-7301-two-point-descent/verify.py`
3. `claims/T-7301-no-two-point-linear-descent.md`
4. `claims/T-7302-sliding-linear-filter-rigidity.md`
5. `claims/L-7302-type-shift-conjugacy.md`
6. base PR #64 `T-7403` and `T-7404`
7. the append-only report under `reports/gpt56-cycle-01/`
