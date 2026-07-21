# Q-9411 — Period-four reduced-height saving

Claim ID: Q-9411  
Title: Can period-four block Padé approximants recover the missing `0.6286%` logarithmic gain?  
Status: IDEA / primary next periodic target  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-21  
Dependencies: L-9410, T-9414, R-9403  
Scope: primitive positive periodic height-increment words of minimal period four

## Current exact boundary

For the block Gaussian-binomial approximants of L-9410, the universal
asymptotic exponent at displayed period length `r` is

```text
mu_r
 =[1/log_64(81)]*(1+1/[r(r+1)]).
```

At `r=4`,

```text
mu_4=0.993714361875...,
1-mu_4=0.006285638124... .                          (1)
```

Thus the written universal height estimate misses the elementary rationality
threshold by only about

```text
0.6285638124%                                       (2)
```

on the logarithmic scale.

## Primary question

For a primitive period-four word

```text
W=d_1d_2d_3d_4,
```

let

```text
A_n^clear,
B_n^clear
```

be the integer numerator and denominator obtained from the L-9410 approximant
after clearing its universal odd power-of-`81` denominator. Is there a uniform
quadratic-scale saving, from reduction or a stronger coupled construction,
large enough to replace `mu_4` by a constant greater than one?

## Concrete routes

### 1. Exact common-factor growth

Measure and prove a lower bound for

```text
g_n=gcd(A_n^clear,B_n^clear).
```

A sufficient target is

```text
log g_n
 >=(0.006286+epsilon)
   *log max(|A_n^clear|,|B_n^clear|)                 (3)
```

along an infinite sequence of orders, with one fixed `epsilon>0`.

Because the cleared denominator is not divisible by `3`, any saving must come
from other primes or from a different integral normalization.

### 2. Coupled adjacent-order determinant

Combine orders `n` and `n+1` so the first nonzero error cancels while the
common height grows by less than the gained vanishing. Every determinant must
report:

```text
- exact first surviving block;
- exact v_2 of the determinant error;
- exact common denominator;
- reduced height or a proved upper bound;
- nonvanishing.
```

### 3. Phase-sensitive denominator

L-9410 uses one universal denominator treating all four phases symmetrically.
Exploit the actual transfer polynomial `P_W`, which may make one or more phases
cheaper. A valid improvement must work uniformly for the chosen primitive word,
not only at bounded Padé orders.

### 4. Word classification

Separate period-four words by invariants such as

```text
(S(W), e(W), phase exponents, reversal class, cyclic class).
```

Some words may reduce to a shorter algebraic phase system even when their
literal word period is four.

## Verification program

A useful exact experiment should:

1. enumerate primitive words over `{17,18}` of length four up to cyclic symmetry;
2. construct L-9410 approximants for the first feasible orders;
3. record cleared and reduced heights separately;
4. factor gcds when feasible and record unfactored cofactor digests otherwise;
5. compare measured exponents with `mu_4`;
6. test adjacent-order determinants;
7. distinguish finite anomalies from a proposed asymptotic law.

## Success criteria

### Obstruction theorem

Prove an exponent greater than one for every primitive period-four word. T-9415
would then extend automatically to every eventually period-four directive.

### Construction signal

If one word exhibits systematic stabilization or an exceptional height collapse,
replay its exact active cylinders and test whether it produces an ordinary
positive context. Finite small height alone is not an M1 candidate.

## Falsification criteria

- A bounded-order gcd pattern is not an asymptotic theorem.
- A determinant with an unproved zero/nonzero condition is not an approximant.
- A height estimate before reduction cannot be advertised as a reduced-height
  gain.
- A period-four result does not decide the balanced nonperiodic directive.

## Relationship to the S-adic frontier

Period four is the first place where the universal block estimate fails, and the
failure is very small. Any mechanism that repairs it—common factors,
phase-sensitive determinants, or transfer-matrix compression—is a candidate
building block for adjacent continued-fraction standard words in the true
balanced S-adic problem.