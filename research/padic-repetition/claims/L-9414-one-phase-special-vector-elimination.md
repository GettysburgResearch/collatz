# L-9414 — One-phase elimination for a special vector

Claim ID: `L-9414`  
Title: A scalar Padé family plus a lower-dimensional linear-independence measure excludes one additional phase  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: elementary integer linear-form algebra; application uses `L-9413`  
Scope: quantitative reduction of period-ten special-vector irrationality to a nine-phase measure  
Related counterexample candidates: none

## Quantitative measure convention

Let

```text
alpha_0,...,alpha_(D-1) in Q_2.
```

Suppose there is a real number `omega>=0` such that, for every `epsilon>0`,
all sufficiently large nonzero integer coefficient vectors

```text
a=(a_0,...,a_D)
```

satisfy

```text
v_2(
 a_0+sum_(j=0)^(D-1) a_(j+1) alpha_j
)
 <=(omega+epsilon) log_2 H(a),                        (1)
```

where

```text
H(a)=max_i |a_i|.
```

An exact zero is forbidden by (1), so this hypothesis includes rational linear
independence of `1,alpha_0,...,alpha_(D-1)`.

Let one further value `beta in Q_2` have reduced rational approximants

```text
p_n/q_n,
q_n odd,
H_n=max(|p_n|,|q_n|)->infinity,
```

with nonzero errors and

```text
liminf
 v_2(beta-p_n/q_n)/log_2 H_n
 =tau>omega.                                          (2)
```

## Statement — one additional phase is eliminated

Under (1)--(2),

```text
1,alpha_0,...,alpha_(D-1),beta
```

are linearly independent over `Q`.

A fortiori, no fixed nonzero rational coefficient vector involving `beta` can
produce a rational special value.

## Proof

Suppose

```text
C_0+sum_(j=0)^(D-1) C_(j+1) alpha_j+C_(D+1) beta=0    (3)
```

with integers `C_i`, not all zero.

If `C_(D+1)=0`, equation (3) contradicts (1). Hence

```text
C_(D+1)!=0.
```

For every `n`, form the integer-coefficient linear form in the first `D` values

```text
Lambda_n
 =q_n[
   C_0+sum_(j=0)^(D-1) C_(j+1)alpha_j
  ]+C_(D+1)p_n.                                       (4)
```

Equation (3) gives

```text
Lambda_n
 =C_(D+1)(p_n-q_n beta).                              (5)
```

The right side is nonzero because the scalar approximation error is nonzero.
Since `q_n` is odd,

```text
v_2(Lambda_n)
 =v_2(C_(D+1))
  +v_2(beta-p_n/q_n).                                 (6)
```

The coefficient height of (4) is at most

```text
C(C_0,...,C_(D+1)) H_n.                               (7)
```

Choose `epsilon>0` with

```text
omega+2epsilon<tau.
```

For infinitely many `n`, equation (2) makes the right side of (6) exceed

```text
(omega+epsilon)log_2 H_n+O_C(1).
```

Equations (1) and (7) give the opposite upper bound

```text
v_2(Lambda_n)
 <=(omega+epsilon)log_2 H_n+O_C(1),
```

a contradiction. **QED**

## Period-ten application

For a primitive period-ten stack word, put

```text
alpha_j=f_R(Z lambda^j),  0<=j<=8,
beta   =f_R(Z lambda^9).
```

`L-9412` verifies that the first nine points occupy distinct `R^Z`-orbits.
Väänänen–Wallisser supplies a quantitative linear-independence measure for

```text
1,alpha_0,...,alpha_8.
```

`L-9413` supplies odd-denominator scalar approximants to `beta` with

```text
tau=9/log_2(81)=1.419591945535779... .                (8)
```

Therefore a direct period-ten theorem follows as soon as the source measure is
put in convention (1) with

```text
omega_9<9/log_2(81).                                  (9)
```

## Why this is cheaper than dimension ten

The source theorem's failed dimension-ten condition controls every coefficient
direction in

```text
1,alpha_0,...,alpha_9.
```

The present argument needs:

1. a nine-phase lower bound;
2. one scalar approximation family;
3. only the coefficient direction forced by a hypothetical native relation.

It precisely implements the “special coefficient vector may be cheaper than
full independence” advice from the wave-5 literature review.

## Dependency audit

- The abstract lemma is elementary.
- The period-ten application uses only the exact phase decomposition, the
  quantitative form of the source theorem in dimension nine, and the scalar
  Padé family.
- The exact source exponent `omega_9` has not yet been transcribed into the
  normalization (1); condition (9) remains an explicit test, not a claimed fact.

## Gap audit

- Qualitative independence of nine phases alone is insufficient.
- If the source exponent is at least the scalar exponent, this particular
  elimination does not close period ten.
- A failed comparison would still identify exactly how much special-vector
  improvement is needed.
- The lemma says nothing by itself about a growing S-adic period.

## Suggested next attack

Extract the quantitative exponent and constants from Väänänen–Wallisser
Theorem 1 and normalize them as in (1). If (9) fails, repeat their determinant
construction with orthogonality only against the native coefficient vector or
the two-dimensional skew `q`-difference orbit in `Q-9413`.
