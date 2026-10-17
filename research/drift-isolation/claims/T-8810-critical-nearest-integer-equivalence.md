# T-8810 — Critical nearest-integer equivalence

Claim ID: T-8810  
Title: The two-extreme-residue `p=q+1` map is exactly the critical symmetric `Z_(p/q)` problem  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: none; T-8806 is the specialization `q=4`  
Scope: every integer `q>=2`, with `p=q+1`  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Fix an integer `q>=2`, put

```text
p=q+1,
beta=p/q,
```

and define the partial approximate-multiplication map

```text
F_q(x)=ceil(p*x/q)   if x mod q is in {0,q-1},
       STOP          otherwise.                         (1)
```

The following are equivalent.

1. Some positive integer has an infinite orbit under `F_q`.
2. There exists a real number `xi>0` such that

   ```text
   || xi*beta^n || < 1/p                              (2)
   ```

   for every `n>=0`, where `||.||` denotes distance to the nearest integer.

More precisely, an infinite integer orbit `x_0,x_1,...` canonically produces
such a parameter `xi`. Conversely, any `xi` satisfying (2) produces an infinite
integer orbit after discarding at most finitely many initial indices.

For `q=4`, `p=5`, condition (2) is

```text
|| xi*(5/4)^n || < 1/5   for every n>=0.              (3)
```

Hence a positive infinite survivor of the exact `4 -> 5` chart exists if and
only if a critical symmetric `Z_(5/4)` parameter exists.

The constant `1/p` is exact: the two permissible residue classes are precisely
the two outer fractional-part intervals

```text
[0,1/p) and (1-1/p,1).                                (4)
```

## Definitions

- The term **critical symmetric `Z_(p/q)` parameter** is used here only as a
  concise name for (2). It is not the one-sided `Z_(p/q)` definition
  `{lambda*(p/q)^n}<1/q` used by Dubickas--Mossinghoff.
- An orbit of (1) is infinite when every iterate remains in one of the two
  permissible residue classes.

## Motivation

T-8806 expressed the `5x+1` control chart as a forbidden-digit bottom path in
base `5/4`. The present theorem exposes an equivalent analytic face. It places
the exact missing theorem at a sharp nearest-integer threshold rather than at a
vague distribution-modulo-one question.

This also explains why standard range estimates do not automatically close the
problem: the required contradiction must force a distance at least `1/p`, and
strictness at that precise boundary matters.

## Proof

### Infinite orbit implies the nearest-integer condition

Let `x_0,x_1,...` be a positive infinite orbit. Define `d_n in {0,1}` by

```text
d_n=0  if x_n mod q = 0,
d_n=1  if x_n mod q = q-1.
```

Then (1) is exactly

```text
q*x_(n+1)=p*x_n+d_n.                                  (5)
```

Define the convergent real number

```text
lambda
 = x_0 + sum_(j>=0) d_j*q^j/p^(j+1),
xi=lambda/q.                                           (6)
```

Iterating (5) and separating the tail of (6) gives

```text
lambda*beta^n = x_n+u_n,                              (7)
```

where

```text
u_n=(1/p)*sum_(k>=0)d_(n+k)*(q/p)^k,
0<=u_n<=1.                                             (8)
```

The value `u_n=1` would force `d_(n+k)=1` for every `k>=0`. In that case
`y_k=x_(n+k)+1` would satisfy

```text
q*y_(k+1)=p*y_k.
```

Integrality for every future `k` would force `q^k | y_0` for every `k`, hence
`y_0=0`, contradicting positivity. Therefore

```text
0<=u_n<1.                                              (9)
```

If `d_n=0`, then `x_n=q*m` and (8) gives

```text
u_n=(q/p)u_(n+1)<q/p.
```

Thus

```text
{xi*beta^n}=u_n/q < 1/p.                              (10)
```

If `d_n=1`, then `x_n=q*m+q-1` and

```text
u_n=1/p+(q/p)u_(n+1).
```

Equality `u_n=1/p` would force every later digit to be zero. Then the future
states would satisfy `q*x_(k+1)=p*x_k`, forcing the positive integer `x_(n+1)`
to be divisible by every power of `q`, again impossible. Hence `u_n>1/p`, and

```text
{xi*beta^n}
 = (q-1+u_n)/q
 > (q-1+1/p)/q
 = q/p
 = 1-1/p.                                             (11)
```

Equations (10)--(11) prove (2).

### Nearest-integer condition implies an infinite orbit

Assume `xi>0` satisfies (2), and write

```text
z_n=xi*beta^n,
f_n={z_n}.
```

Then for every `n`,

```text
f_n in [0,1/p) union (q/p,1).                         (12)
```

Define

```text
x_n=floor(q*z_n).                                     (13)
```

If `f_n<1/p`, then

```text
x_n=q*floor(z_n),
x_(n+1)=floor(p*z_n)=p*floor(z_n),
```

so `x_n mod q=0` and `x_(n+1)=ceil(p*x_n/q)`.

If `f_n>q/p`, then `floor(q*f_n)=q-1` and
`floor(p*f_n)=q`. Consequently

```text
x_n=q*floor(z_n)+q-1,
x_(n+1)=p*floor(z_n)+q
       =ceil(p*x_n/q).                                (14)
```

Thus every `x_n` lies in a permissible residue class and follows (1). If an
initial `x_n` is zero, discard finitely many terms: since `xi*beta^n` tends to
infinity, some later `x_N` is positive, and the tail remains an infinite orbit.
This proves the equivalence. **QED**

## Specialization to the PR #35 chart

At `q=4`, equations (13)--(14) yield

```text
x_n mod 4 in {0,3},
x_(n+1)=ceil(5*x_n/4).
```

With the physical variable of T-8806, `x_n=A_n+1`. Therefore (3) is equivalent
to one positive physical seed remaining in the exact two-branch `5x+1` chart
forever.

## Dependency audit

The theorem is self-contained. T-8806 is used only to translate the `q=4`
integer orbit back to the physical `5x+1` chart.

For context, Dubickas--Mossinghoff (2009) explicitly singled out the family
`p=q+1`, `S={0,q-1}` as a natural two-residue approximate-multiplication target.
Their one-residue termination theorem does not settle this symmetric case.

## Gap audit

- The inequalities are strict. Replacing `<1/p` by `<=1/p` introduces boundary
  sequences not covered by the residue calculation.
- The parameter `xi` need not be algebraic or rational.
- General distribution results that force a large limit point below `1/p` are
  insufficient.
- The theorem is an equivalence, not an existence or nonexistence proof.
- The one-sided `Z_(p/q)` condition and the symmetric condition (2) must not be
  conflated.

## Adversarial tests

- For `q=4`, the two intervals are `[0,1/5)` and `(4/5,1)`, and the two residue
  branches are exactly `0` and `3 modulo 4`.
- Constant zero or one tails are the only possible equality cases in the forward
  implication; integrality forces their corresponding states to be `0` or `-1`,
  excluding a positive orbit.
- Direct finite orbits from X-8802 and X-8803 satisfy (10)--(11) when `xi` is
  formed from their finite digit prefix plus any legal continuation.

## Remaining uncertainty

The unresolved theorem is whether (2) can hold for any `xi>0` when `p=5,q=4`.
A proof that every sequence `||xi*(5/4)^n||` reaches or exceeds `1/5` would close
the chart negatively. A construction staying strictly below `1/5` would give a
divergent positive `5x+1` chart orbit.

## Suggested next attack

Audit sharp nearest-integer range theorems specifically at the critical value
`1/5`. Any bound strictly larger than `1/5` settles the case; a bound equal to
`1/5` requires an equality-classification theorem.