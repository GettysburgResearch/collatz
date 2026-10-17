# R-9407 — Scalar adjacent-order Casoratians cannot close period ten

Claim ID: `R-9407`  
Title: Even a zero-height-cost adjacent-order benchmark stays below one at the first source-uncovered period  
Status: `PROPOSED cross-branch method audit`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: branch-qualified PR #34 `L-9891`; native place conversion  
Scope: scalar combinations of aligned equal-allocation adjacent-order Padé errors  
Related counterexample candidates: none

## Exact adjacent-order interface

PR #34 `L-9891` proposes an exact rank theorem for aligned adjacent-order
errors. If the highest constituent order is `t` and `q` neighboring orders are
combined, put

```text
theta=(q-1)/t,
0<=theta<1.
```

The exact additional valuation is linear in `q-1`. Grant the construction the
deliberately optimistic assumptions that:

1. its cofactors have zero quadratic height cost;
2. no extra denominator cost is charged;
3. the raw height is only that of the highest constituent.

Under those assumptions, its normalized exponent is

```text
mu_r^adj(theta)
 =[6/log_2(81)]
  [r^2+r+1+2theta]/[r(r+1)].                          (1)
```

This is an optimistic upper benchmark, not the actual reduced exponent.

## Statement 1 — absolute ceiling

Since `theta<1`,

```text
mu_r^adj(theta)
 <log_81(64)
  [r^2+r+3]/[r(r+1)]
 =:mu_r^adj,max.                                      (2)
```

The factor in (2) is strictly decreasing in `r`.

At `r=7`,

```text
mu_7^adj,max<1
```

because this is exactly

```text
64^59<81^56.                                         (3)
```

Therefore

```text
mu_r^adj(theta)<1
```

for every `r>=7`, even under the zero-height-cost assumptions.

## Statement 2 — period ten

At the first fixed period not covered by the Väänänen–Wallisser source theorem,

```text
mu_10^adj,max
 =log_81(64)*113/110
 =0.972205393003291...<1.                             (4)
```

The strict inequality is certified exactly by

```text
64^113<81^110.                                       (5)
```

Thus the scalar aligned adjacent-order construction cannot close period ten,
even if every cofactor were free.

## Interpretation

This result sharply redirects the wave-5 Casoratian advice.

The following remain possible:

- phase-sensitive Hermite–Padé cancellation of the **combined** native vector;
- a determinant built from a low-dimensional `q`-difference orbit rather than
  scalar adjacent orders;
- a quadratic common-factor height saving;
- the one-phase elimination route of `L-9414`.

What is closed is only the scalar aligned adjacent-order family represented by
(1).

## Dependency and status audit

- The rank, exact cancellation count, and formula (1) are read from PR #34
  `L-9891`, which remains `PROPOSED`.
- Equations (2)--(5) are independently elementary.
- This file does not promote the PR #34 theorem.
- Even if `L-9891` passes review, the result is a method boundary, not a
  period-ten irrationality theorem.

## Adversarial tests

`X-9411` evaluates (2) for periods through fifteen and freezes the exact
boundary comparisons at periods six, seven, and ten.
