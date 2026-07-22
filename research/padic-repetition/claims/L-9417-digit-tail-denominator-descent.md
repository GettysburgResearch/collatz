# L-9417 — Exact denominator descent along every digit tail

Claim ID: `L-9417`  
Title: Rational `2`-adic digit-tail denominators form a descending divisor chain  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-9401`; elementary rational arithmetic  
Scope: every binary survivor code  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Digit tails and completion convention

For

```text
epsilon=(epsilon_n) in {0,1}^N,
T=64/81,
```

define the `2`-adic digit tail

```text
S_n
 :=sum_(k>=0)epsilon_(n+k)T^k in Z_2
  =(81/17)Phi(sigma^n epsilon).                       (1)
```

The same rational partial sums also have a real limit, but that is a separate
completion value and is not denoted by `S_n` here. The `2`-adic tails satisfy

```text
boxed:
S_n=epsilon_n+T S_(n+1).                              (2)
```

## Statement — descending denominators

Assume `S_n` is rational and write

```text
S_n=A_n/B_n,
B_n>0,
gcd(A_n,B_n)=1.                                      (3)
```

Then `B_n` is odd and `S_(n+1)` is rational with reduced denominator satisfying

```text
boxed:
B_(n+1) divides B_n.                                  (4)
```

Consequently, if `S_0` is rational, all `2`-adic digit tails are rational and

```text
B_n divides B_0                                      (5)
```

for every `n`.

## Proof

Because `S_n` belongs to `Z_2`, its reduced denominator is odd. Solving (2) for
the next tail gives

```text
S_(n+1)
 =81(A_n-B_n epsilon_n)/(64B_n).                     (6)
```

The left side belongs to `Z_2`; both `81` and `B_n` are odd. Hence

```text
64 divides A_n-B_n epsilon_n.                         (7)
```

Put

```text
C_n=(A_n-B_n epsilon_n)/64 in Z.
```

Then

```text
S_(n+1)=81C_n/B_n.                                   (8)
```

Reduction can only remove factors from `B_n`, proving (4). Equation (2)
propagates rationality, and induction gives (5). **QED**

## Relation to `L-9416`

`L-9416` applies the same algebra after jumping between consecutive nonzero
digits. The present lemma follows every digit. Neither version controls the
ordinary numerator or the archimedean size of the rational `2`-adic value.

## Interpretation

A rational initial code supplies one finite odd denominator. Exact `2`-adic
integrality forces every division by `64` in the tail recurrence to be paid by
ordinary numerator divisibility. Denominator factors may disappear but no new
ones appear.

The resulting denominator set is finite, but the rational tail-state set need
not be finite because the numerators can grow without bound.

## Dependency audit

The proof uses only the exact shift identity, rational membership in `Z_2`, and
ordinary divisibility by `64`. No real convergence, periodicity, Padé theorem,
external source, or experiment is used.

## Gap audit

- The real limit of the positive digit series is generally not the same object
  as a rational `2`-adic tail value.
- Therefore the compact real interval of the positive series cannot be used to
  bound the numerators in (3).
- Descending denominators alone do not imply eventual periodicity, bounded
  gaps, irrationality, or triviality of the ordinary section.

## Adversarial tests

A checker may enumerate reduced odd-denominator transitions satisfying (7) and
verify (4). Eventually periodic codes provide rational controls, but finite
checks cannot turn the divisor chain into a global state bound.

## Suggested next attack

Couple (5) to one additional ordinary-height coordinate. Candidates are the
integer tail orbit when an ordinary point is assumed, PR #16's centered
nearest-integer blocks, or a product-formula numerator built from two tail
states. The missing theorem must bound numerators, not denominators alone.
