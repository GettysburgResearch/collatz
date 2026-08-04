# T-9407 — Stationary matching isometry and the ghost-stage theorem

Claim ID: T-9407  
Title: Exact stationary supply-demand matching forms a `2`-adic tree isomorphism with no positive ordinary point  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9403, L-9405  
Scope: the same-stage unsteered supply/demand interface for contexts `x=15 mod 16`  
Related counterexample candidates: issue #4 stack frontier; no `K-####` candidate

## Statement

For `x in 15+16Z_2`, define

```text
F_x(m)=81^(9m)*(81x+1)-D(m).
```

Then for distinct ordinary integers `m,n`,

```text
v_2(F_x(n)-F_x(m)) = 4+v_2(n-m).               (1)
```

Also `F_x(m) in 16Z_2`.  Hence

```text
F_x/16 : Z_2 -> Z_2                             (2)
```

extends to a bijective isometry.  In particular, for every
`x in 15+16Z_2`, there is exactly one

```text
m_*(x) in Z_2
```

such that

```text
F_x(m_*(x))=0.                                  (3)
```

The inverse parametrization of the stationary matching locus is

```text
X(m)
 = 17*81^(-(18m+3))
   -81^(-(9m+2))
   -81^(-1).                                    (4)
```

It satisfies

```text
X(m) in 15+16Z_2,
v_2(X(n)-X(m))=4+v_2(n-m),                      (5)
```

so `X` is a scaled isometry from `Z_2` onto `15+16Z_2`, inverse to `m_*`.

### Exact finite-depth matching law

At depth `j>=1`, for every `x=15 mod 16`, the congruence

```text
81^(9m)*(81x+1) = D(m) mod 64^j                 (6)
```

has exactly one stage class

```text
m mod 2^(6j-4).                                 (7)
```

At depth `1`, this is one class out of `4`.  From depth `j` to `j+1`, exactly
one of the `64` stage lifts continues.  Thus the conditioned agreement rates
are **exactly**

```text
1/4 for the first base-64 digit,
1/64 for each additional digit.                (8)
```

No independence or random model is used.

### Positive-quadrant exclusion

For every ordinary integer `m>=0`, the real rational represented by (4)
satisfies

```text
X(m)<0.                                         (9)
```

Therefore the stationary matching locus contains no pair

```text
(m,x) in Z_(>=0) x Z_(>=0).                     (10)
```

Equivalently, for every ordinary `x>=0` with `x=15 mod 16`, the unique
`2`-adic matching stage `m_*(x)` is not an ordinary nonnegative integer.

### Ghost-stage sequence

For such an ordinary `x`, let `m_j` be the least representative in

```text
0<=m_j<2^(6j-4)
```

satisfying (6).  Then

```text
m_(j+1)=m_j+a_j*2^(6j-4),  0<=a_j<64,          (11)
```

and the sequence is compatible at all depths.  It cannot eventually
stabilize; hence it tends to infinity through infinitely many nonzero lift
digits while converging `2`-adically to `m_*(x)`.

Thus every admissible positive context has arbitrarily deep finite stationary
matches, but their compatible limit is a **ghost stage** in `Z_2`, not one
ordinary stage.

## Proof

Put

```text
q=81^9,
a=81x+1,
b=17*81^(-2).
```

Then

```text
F_x(m)=a*q^m-b*q^(-m)+81^(-1).                 (12)
```

For `m!=n`,

```text
F_x(n)-F_x(m)
 =(q^n-q^m)*(a+b*q^(-(m+n))).                  (13)
```

Because `x=15 mod 16`, `a` is divisible by `16`; the second summand in the
parenthesis is odd.  The parenthesis is therefore odd.  L-9405's valuation
calculation gives

```text
v_2(q^n-q^m)=4+v_2(n-m),
```

proving (1).  Both the supply and demand are `0 mod 16`, so `F_x` maps into
`16Z_2`.  The same finite-quotient cardinality argument as L-9405 proves (2)
and the unique root (3).

Solving `F_x(m)=0` for `x` gives (4).  Modulo `16`, all powers of `81` equal
`1`, so `X(m)=17-1-1=15 mod 16`.  Writing `z_m=q^(-m)`,

```text
X(n)-X(m)
 =(z_n-z_m)
  *(17*81^(-3)*(z_n+z_m)-81^(-2)).             (14)
```

The bracket is odd: its first term is even and its second term is odd.  Thus
(5) follows from the same valuation identity.  Finite quotient cardinality
then proves that `X` maps onto the full context coset and is inverse to `m_*`.
This also proves the unique finite-depth classes and lift rates (6)--(8).

For ordinary `m>=0`,

```text
17*81^(-(18m+3)) < 81^(-1),
```

so (4) is strictly negative even before subtracting the middle positive term.
This proves (9) and (10).

The least representatives in (11) are nondecreasing and compatible.  If they
were eventually constant at an ordinary integer `m`, then (6) would hold for
all depths and hence `F_x(m)=0` in `Z_2`, contradicting the positive-quadrant
exclusion.  Therefore infinitely many lift digits are nonzero and the least
representatives diverge. **QED**

## Relationship to issue #4

This theorem upgrades the conditioned E4 observation from measured generic
agreement to an exact all-depth count and describes the finite shadows left by
the stationary interface.  It is compatible with the branch's SML obstruction
but needs no SML input.

It does **not** close active steering.  A genuine stack chain replaces the
context after each stage and may deliberately encode the next demand in the
high quotient.  T-9407 isolates exactly why repeated fixed-context finite
matches are not such a chain.

## Dependency audit

- D-9403 supplies the exact maps.
- L-9405 supplies the valuation of powers of `81^9`.
- No empirical distribution, external transcendence theorem, or unmerged proof
  is used.

## Gap audit

- Equality is the stationary same-stage comparison frozen in D-9403, not the
  full two-height active regeneration recurrence.
- “Exactly generic” refers to finite quotient counts after the forced coset; it
  is not a claim of independence between arbitrary random variables.
- The ghost stages are positive least representatives at every finite depth,
  but compatibility alone never turns their `2`-adic limit into an ordinary
  stage.
- The real sign argument applies only to ordinary `m>=0`; negative ordinary
  integers are irrelevant as stack heights.

## Adversarial tests

`X-9403` verifies the matching permutations through depth `3`, checks unique
roots for thirty-two context values, constructs compatible ghost-stage lifts
through depth `8`, verifies the explicit inverse context formula, and checks
the real sign on 128 ordinary stages.

## Remaining uncertainty

Independent reconstruction is pending.  The active open problem is to replace
fixed `x` by the exact high-quotient update and determine whether its moving
context can follow the matching tree forever from one ordinary initial state.

## Suggested next attack

Derive the two-variable active transition on the matching coordinates

```text
(context ghost digit, stage lift digit, high quotient)
```

and test whether the transition preserves any compact ordinary-height region
or necessarily escapes to a purely `2`-adic inverse limit.
