# L-9416 — Exact denominator descent along binary one-tails

Claim ID: `L-9416`  
Title: Rational one-tail denominators can only decrease under the `64/81` shift recurrence  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: elementary rational arithmetic  
Scope: every binary `64/81` series with infinitely many nonzero digits  
Related counterexample candidates: issue #4 ordinary `64 -> 81` section; no `K-####` candidate

## Setup

Put

```text
T=64/81.
```

Let

```text
0<=h_0<h_1<h_2<...
```

be an infinite sequence of integers and define its normalized one-tails

```text
Y_j
 =sum_(k>=j) T^[h_k-h_j]
 =1+T^[g_j]Y_(j+1),

g_j=h_(j+1)-h_j>=1.                                  (1)
```

Every `Y_j` converges both in `R` and in `Z_2`. In particular,

```text
Y_j in Z_2.                                           (2)
```

## Statement — denominator descent

Assume `Y_j` is rational and write it in lowest terms as

```text
Y_j=A_j/B_j,
B_j>0.                                                (3)
```

Then `B_j` is odd and `Y_(j+1)` is rational with reduced denominator `B_(j+1)` satisfying

```text
boxed:
B_(j+1) divides B_j.                                  (4)
```

Consequently, if the initial series is rational, every normalized one-tail is rational and

```text
B_j divides B_0                                      (5)
```

for all `j`.

## Proof

Rational membership in `Z_2` means that the reduced denominator is a `2`-adic unit. Thus

```text
2 does not divide B_j.                                (6)
```

Solving (1) for the next tail gives

```text
Y_(j+1)
 =81^[g_j](A_j-B_j)/(64^[g_j] B_j).                   (7)
```

The left side lies in `Z_2`. The factors `81^[g_j]` and `B_j` are odd. Therefore

```text
2^[6g_j] divides A_j-B_j.                             (8)
```

Put

```text
C_j=(A_j-B_j)/64^[g_j] in Z.                          (9)
```

Then (7) becomes

```text
Y_(j+1)=81^[g_j] C_j/B_j.                            (10)
```

After reduction, its denominator divides `B_j`, proving (4). Rationality propagates through (1), so induction proves (5). **QED**

## General form

The same proof works for

```text
T=M/N,
0<M<N,
gcd(M,N)=1,
```

at any prime `p` satisfying `p|M` and `p` not dividing `N`. If every one-tail lies in `Z_p`, then a rational tail denominator loses no new prime factors when the recurrence is inverted across a zero gap.

The present `64/81` case is especially sharp because all rational series tails automatically lie in `Z_2`.

## Interpretation

Rationality would preload only finitely many odd denominator states. Passing through an arbitrarily long zero gap consumes a very large power of `64`, but exact `2`-adic integrality forces that power to divide the ordinary numerator. No new denominator is created after the division.

This is different from a rational-approximation argument. It uses the exact rationality of every shifted tail, not the height of a finite truncation.

## Dependency audit

The proof uses only:

- the exact one-tail recurrence (1);
- reduced rational denominators;
- the characterization `Q intersect Z_2 = {a/b: b odd}`;
- ordinary divisibility.

No Padé approximation, product formula, external irrationality theorem, or experiment is used.

## Gap audit

- Infinite support is needed only in the later irrationality theorem, not in the local descent.
- The digit at each chosen support position is exactly `1`; a varying rational leading digit would need a fixed-denominator audit.
- Positivity and real convergence are not used here.
- The result does not claim that bounded gaps are sufficient for rationality.

## Adversarial tests

`X-9413` exhausts synthetic reduced rationals with odd denominator and exact `64^g` divisibility, then verifies that every resulting next denominator divides the current one. It also checks the recurrence on finite stack words.

## Suggested next attack

Combine (5) with a real limit point of the normalized tails. If long zero gaps force `Y_j -> 1`, bounded denominators make eventual equality unavoidable; positivity then excludes equality. This is `T-9418`.
