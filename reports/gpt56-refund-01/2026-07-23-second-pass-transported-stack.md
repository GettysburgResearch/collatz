# Second pass — affine-run exclusion and the transported future-cylinder stack

```text
Agent: gpt56-refund-01
Issues: #43 and #46
Branch: agent/gpt56-refund-01/43-linear-refund-invariant
Date: 2026-07-23
```

## Objective

Re-read the newest post-review advances rather than extending the earlier growth argument. The pass concentrated on two questions:

1. does the explicit linear run schedule from the first pass actually have an ordinary core?
2. does PR #49's claimed generated mixed-radix stack really contain the future legality digits?

## Finding 1 — the explicit affine run schedule is a completion ghost

The first pass proposed

```text
r_n=64+n
```

because it satisfies both the physical run-five cone and the moving-boundary refund cone. That growth design is correct, but its ordinary realization fails.

For every eventually affine positive-slope schedule

```text
r_n=R+d*n,
d>=1,
```

the selected divisible-seven core is

```text
v_0=-9^(-(R+1))*F_q(z),
q=(8/9)^d,
z=2^(3R+3d+4)/9^(R+d+1),
F_q(z)=sum_(n>=0) q^(n(n-1)/2) z^n.
```

The primary q-difference theorem of Amou--Matala-aho--Väänänen applies at the 2-adic place. The exact source parameter is

```text
lambda=-(2/3)log_2(3),
```

independent of `d`, and lies strictly inside the source window for `m=s=1`, `delta=1/2`. Hence `1,F_q(z)` are Q-linearly independent and the initial core is irrational.

This is `R-8202`. It kills `Q-8202` as a positive target and replaces it by `Q-8203`: a successful run schedule must be genuinely non-eventually-affine while still meeting the exact nine-run resource total `44`.

## Finding 2 — the plain Euclidean stack crosswalk is false

PR #49 `T-8512` expands the current top quotient in the future radix sequence and identifies those digits with the residues consumed by later connectors. The size comparison is correct, but that digit interpretation is not.

One transition is

```text
m_n     = rho_n + H_n*ell_n,
m_(n+1)= sigma_n + A_n*ell_n.
```

The second plain digit is `ell_n mod H_(n+1)`, whereas the actual next legality residue is imposed on

```text
sigma_n+A_n*ell_n mod H_(n+1).
```

A frozen intrinsic-core instance gives

```text
plain pulled quotient digit mod64: 45
actual next cylinder residue mod64: 16.
```

Thus the plain digit/future-residue crosswalk is refuted. This is recorded in `R-8203`. The numerical `1/288` and `1/233` size bounds survive as radix-capacity estimates.

## Repair — inverse-affine transported cylinders

The false crosswalk has a canonical exact repair.

For

```text
H_(h+1)*ell_(h+1)=A_h*ell_h+delta_h,
```

define the accumulated future radix `K_s`, odd multiplier `P_s`, and affine carry `B_s` by

```text
K_(s+1)=K_s*H_(s+1),
P_(s+1)=A_s*P_s,
B_(s+1)=A_s*B_s+K_s*delta_s.
```

Then

```text
K_s*ell_s=P_s*ell_0+B_s.
```

Hence the complete first-`s` future legality condition is one unique pulled-back residue

```text
ell_0=Theta_s mod K_s,
Theta_s=[-P_s^(-1)B_s]_(K_s).
```

The residues are nested. Their mixed-radix digits are generated one at a time only after pulling the next condition backward through the accumulated odd multiplier and carry.

This is the true future-cylinder stack. It is formalized as `L-8210`.

## Corrected generated-stack consequence

If the current top quotient has ordinary radix capacity `d` in the sense retained from `T-8512`, then its current lift contains at least `d-1` complete **transported** future-cylinder levels. Therefore the permanent-refund tail still dynamically creates an unbounded finite stack, but the stack digits are the inverse-affine residues `Theta_s`, not the raw Euclidean digits.

The corrected quantitative bounds are

```text
transported depth >= floor(r/288)-1       uniformly,
transported depth >= floor(r/233)-1       for r>=100909,
liminf transported_depth/r >= 1/233.
```

This salvages the strategic point while removing the false direct-read interpretation.

## Diagonal-foundry boundary

The transported recursion also clarifies any causal feedback/foundry proposal. Once a finite-state branch path is fixed causally, the inverse-affine recurrence determines one unique nested `2`-adic stack. Existence and uniqueness of that completion are automatic. The load-bearing condition is still

```text
transported digits eventually zero
+ all physical lifts nonnegative
+ every finite-state gate legal.
```

A controller that proves only a unique `2`-adic fixed point has not advanced ordinary existence.

## Updated constructive target

The strongest small-chart target is now:

```text
one explicit positive ordinary run core
+ genuinely nonlinear/adaptive schedule
+ nine-run total at least 44
+ changing-modulus refund absorption
+ transported-cylinder eventual-zero closure.
```

For PR #49, the target is the analogous four-cell transported-stack invariant after permanent refund entry.

## Repository actions

- added `R-8202` and `Q-8203` in the preceding pass;
- added `R-8203` narrowing PR #49 `T-8512`;
- added `L-8210` in this pass to repair the future-stack theorem;
- source-branch comments should be posted to PR #49 and PR #51;
- no counterexample or `K-82xx` identifier is claimed.