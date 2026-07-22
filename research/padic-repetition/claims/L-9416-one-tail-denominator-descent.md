# L-9416 — Exact denominator descent along binary one-tails

Claim ID: `L-9416`  
Title: Rational `2`-adic one-tail denominators can only decrease under the `64/81` shift recurrence  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: elementary rational arithmetic  
Scope: every binary `64/81` series with infinitely many nonzero digits  
Related counterexample candidates: issue #4 ordinary `64 -> 81` section; no `K-####` candidate

## Setup and completion convention

Put

```text
T=64/81
```

and let

```text
0<=h_0<h_1<h_2<...
```

be an infinite sequence. For each `j`, the rational partial sums

```text
Y_(j,N)=sum_(k=j)^N T^[h_k-h_j]
```

converge separately in `R` and in `Q_2`. These two limits need not agree, even
when one of them is rational. In this lemma

```text
Y_j := lim_(N->infinity) Y_(j,N) in Q_2.              (1)
```

Only the `2`-adic value is used. It lies in `Z_2` and satisfies

```text
Y_j=1+T^[g_j]Y_(j+1),
g_j=h_(j+1)-h_j>=1.                                   (2)
```

## Statement — denominator descent

Assume `Y_j` is rational and write it in lowest terms as

```text
Y_j=A_j/B_j,
B_j>0.                                                (3)
```

Then `B_j` is odd and `Y_(j+1)` is rational with reduced denominator
`B_(j+1)` satisfying

```text
boxed:
B_(j+1) divides B_j.                                  (4)
```

Consequently, if the initial `2`-adic series value is rational, every
normalized one-tail is rational and

```text
B_j divides B_0                                      (5)
```

for all `j`.

## Proof

Rational membership in `Z_2` means that the reduced denominator is a `2`-adic
unit, so `B_j` is odd. Solving (2) for the next tail gives

```text
Y_(j+1)
 =81^[g_j](A_j-B_j)/(64^[g_j]B_j).                   (6)
```

The left side lies in `Z_2`; the factors `81^[g_j]` and `B_j` are odd.
Therefore

```text
64^[g_j] divides A_j-B_j.                             (7)
```

Put

```text
C_j=(A_j-B_j)/64^[g_j] in Z.
```

Then

```text
Y_(j+1)=81^[g_j]C_j/B_j.                             (8)
```

After reduction, its denominator divides `B_j`, proving (4). Rationality
propagates through (2), so induction proves (5). **QED**

## General form

The same proof works for `T=M/N`, with `gcd(M,N)=1`, at any prime `p` dividing
`M` but not `N`: if the relevant tails lie in `Z_p`, inversion across a gap
cannot create new reduced-denominator factors.

## What the lemma does and does not control

The lemma controls only the ordinary denominator of the rational **`2`-adic**
tail value. It does not bound its ordinary numerator or archimedean absolute
value. In particular, it cannot be combined with the positive real limit of the
same partial sums unless equality of the two completion values has first been
proved by an independent argument.

This boundary is load-bearing. A rational sequence can converge to different
rational limits in different completions; for example

```text
x_N=2^N/(1+2^N)
```

tends to `1` in `R` and to `0` in `Q_2`.

## Dependency audit

The proof uses only the exact `2`-adic recurrence, reduced rational
denominators, and ordinary divisibility. No real limit, Padé approximation,
product formula, external theorem, or experiment is a dependency.

## Gap audit

- The result gives a descending divisor chain, not a finite state space: the
  numerators may be unbounded.
- Infinite support is not needed for the local algebra.
- No irrationality, periodicity, bounded-gap, or M1 conclusion follows from
  denominator descent alone.

## Adversarial tests

A checker may generate odd `B`, integers `A` with `64^g|(A-B)`, form (6), and
verify exact denominator divisibility after reduction. Such finite checks
validate the algebra only.

## Suggested next attack

Seek an independent completion-height estimate for the same rational `2`-adic
tails: a bound on the ordinary numerators, a trapped affine normalization, or a
nonzero cross-completion integer. Without that additional height coordinate,
the denominator chain is not a rationality obstruction.
