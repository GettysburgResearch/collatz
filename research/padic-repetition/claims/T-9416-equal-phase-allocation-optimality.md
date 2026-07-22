# T-9416 — Equal phase allocation is asymptotically optimal

Claim ID: `T-9416`  
Title: Unequal phasewise Gaussian-binomial root allocation cannot improve the universal block-Padé exponent  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9411`  
Scope: the entire phasewise root-product denominator class of `L-9411`  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Statement

Fix a periodic word `W` of displayed length `r>=2`. Consider any sequence of
phase-allocation vectors

```text
n^(D)=(n_0,...,n_(r-1)),
D=sum_j n_j -> infinity,
```

and pass to a subsequence on which

```text
p_j=n_j/D -> p_j^*,
p_j^*>=0,
sum_j p_j^*=1.
```

For clarity, write the limiting vector simply as

```text
p=(p_0,...,p_(r-1)).
```

The phasewise root-product family of `L-9411` has raw denominator-height shape

```text
h(p)=(1+sum_j p_j^2)/2.                             (1)
```

For phase `j`, the first coefficient after its allocated zero window has
quadratic valuation shape

```text
e_j(p)
 =(1+p_j)^2/2
  +sum_(l=0)^(r-1)
    [a_(l,j)^2/2-p_j a_(l,j)],                      (2)

a_(l,j)=min(p_l,p_j).
```

Therefore the universal pre-reduction approximation shape obtainable from the
first surviving individual phase is

```text
sigma(p)=min_j e_j(p)/h(p).                          (3)
```

Then

```text
boxed:
sigma(p)
 <=(r^2+r+1)/(r(r+1)).                              (4)
```

Equality holds only at equal allocation

```text
p_0=...=p_(r-1)=1/r.                                (5)
```

Multiplying by the place-conversion factor gives

```text
mu_root(p)
 =[6/log_2(81)] sigma(p)
 <=[1/log_64(81)](1+1/[r(r+1)]),                    (6)
```

which is exactly the exponent `mu_r` of `L-9410`.

In particular, for `r=4`,

```text
mu_root(p)<=mu_4=0.993714361875...<1.               (7)
```

No unequal redistribution of Gaussian-binomial cancellation roots among the
four phases can recover the rationality threshold within this universal
pre-reduction root-product analysis.

## Derivation of the shapes

Let `C(n)` be the root set from `L-9411`. Equation (5) of that lemma gives

```text
Q(n)
 =(r/2)[D^2+sum_j n_j^2]+O(D).
```

Since `lambda=T^(9S(W))`, the quadratic part of the denominator-clearing
`T`-exponent is

```text
9S(W) rD^2 h(p),
```

which proves (1).

The first possible nonzero coefficient in phase `j` occurs at

```text
N_j=D+n_j.
```

Its base phase factor contributes

```text
r N_j(N_j-1)/2
```

powers of `lambda`. A root belonging to phase `l` has the form

```text
c=r(D+t)+l,
0<=t<n_l.
```

It contributes a negative power in the product of `L-9411(1)` exactly while
`t<n_j`, up to an `O(D)` endpoint correction from the phase residues. Summing
those negative exponents gives, after division by `rD^2`,

```text
sum_l [a_(l,j)^2/2-p_j a_(l,j)].
```

Adding the base quadratic term `(1+p_j)^2/2` proves (2). Fixed powers `C_j`,
`Z`, and phase residues contribute only `O(D)` and disappear from the quadratic
shape.

## Optimization proof

Let

```text
p=min_j p_j
```

and choose a phase `j_*` with `p_(j_*)=p`. Then

```text
a_(l,j_*)=p
```

for every `l`, so (2) gives

```text
e_(j_*)
 =[1+2p+(1-r)p^2]/2.                                (8)
```

Also, among the remaining `r-1` coordinates with total `1-p`, convexity gives

```text
sum_j p_j^2
 >=p^2+(1-p)^2/(r-1).                               (9)
```

Consequently

```text
sigma(p_vector)
 <= f_r(p),                                          (10)
```

where

```text
f_r(p)
 =(r-1)[1+2p-(r-1)p^2]
   /[r-2p+r p^2].                                    (11)
```

Since `p` is the smallest of `r` nonnegative numbers summing to one,

```text
0<=p<=1/r.
```

A direct derivative calculation gives

```text
f_r'(p)
 =2(r-1)[r+1-r^2 p-p^2]
   /[r-2p+r p^2]^2.                                  (12)
```

The numerator in brackets is positive throughout `[0,1/r]`; at the right
endpoint it is `1-1/r^2>0`. Hence `f_r` is strictly increasing there. Therefore

```text
f_r(p)
 <=f_r(1/r)
 =(r^2+r+1)/(r(r+1)),                                (13)
```

proving (4).

Equality in (9) requires the other `r-1` coordinates to be equal, and equality
in (13) requires `p=1/r`. Thus equality in the theorem occurs only at (5).
**QED**

## What this theorem closes

It closes the following proposed repair of the period-four deficit:

> Give more Padé cancellation conditions to the difficult phases and fewer to
> the cheap phases, while retaining one root-product denominator.

Equal allocation is already asymptotically optimal for the guaranteed
valuation-to-height ratio in that entire class.

## What remains open

The theorem does **not** exclude:

1. a quadratic-scale common factor after numerator/denominator reduction;
2. exact cancellation between first surviving coefficients of different phases;
3. an adjacent-order determinant or Hermite–Padé construction not expressible
   by one root set;
4. a theorem using PR #16's carry geometry or PR #33's completion-height state;
5. irrationality of period four or of the balanced nonperiodic directive.

These mechanisms are genuinely coupled; they are not phasewise root
redistributions.

## Dependency audit

- `L-9411` supplies the exact arbitrary-allocation denominator and product
  formula.
- The proof uses only quadratic asymptotics, convexity, and the derivative in
  (12).
- No finite computation, external irrationality theorem, or unmerged branch
  claim is a dependency.

## Gap audit

- The bound concerns the universal pre-reduction height scale. Systematic gcd
  savings remain the explicit `Q-9411` possibility.
- `sigma(p)` uses the first surviving individual phase. A new construction that
  forces cross-phase cancellation lies outside the theorem by design.
- Allocation vectors with some `p_j=0` are included; they are strictly below the
  equal-allocation optimum.
- The displayed word length should be reduced to the true minimal period before
  applying the period classification.

## Adversarial tests

`X-9410` exhausts 657,774 weak integer allocations for period lengths `2` through
`7` and total degree through `18`. Every exact functional lies below (4), and
every finite maximizer is balanced. These checks validate the formula and
boundary cases; the proof above is universal.

## Suggested next attack

Move to a genuinely coupled construction. The most concrete targets are:

```text
- a Casoratian of adjacent Padé orders whose first phase errors cancel;
- a phase-sensitive denominator using P_W rather than only the phase count;
- a completion-height numerator for the reduced rational approximant;
- or a standard-word determinant compatible with the S-adic skew transfer.
```