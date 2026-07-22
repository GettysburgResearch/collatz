# L-9417 — Exact denominator descent along every digit tail

Claim ID: `L-9417`  
Title: Rational digit-tail denominators form a descending divisor chain  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `D-9401`; elementary rational arithmetic  
Scope: every binary survivor code  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Digit tails

For

```text
epsilon=(epsilon_n) in {0,1}^N,
T=64/81,
```

define the unscaled digit tails

```text
S_n(epsilon)
 =sum_(k>=0) epsilon_(n+k) T^k
 =(81/17) Phi(sigma^n epsilon).                        (1)
```

Every tail converges in both `R` and `Z_2` and satisfies

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

Consequently, if `S_0` is rational, all digit tails are rational and

```text
B_n divides B_0                                      (5)
```

for every `n`.

## Proof

Because `S_n` belongs to `Z_2`, its reduced denominator is odd. Solving (2) for
the next tail gives

```text
S_(n+1)
 =81(A_n-B_n epsilon_n)/(64 B_n).                     (6)
```

The left side belongs to `Z_2`. Both `81` and `B_n` are odd, so

```text
64 divides A_n-B_n epsilon_n.                         (7)
```

Put

```text
C_n=(A_n-B_n epsilon_n)/64 in Z.                      (8)
```

Then

```text
S_(n+1)=81 C_n/B_n.                                  (9)
```

Reduction can only remove factors from `B_n`, proving (4). Equation (2)
propagates rationality, and induction gives (5). **QED**

## Relation to `L-9416`

`L-9416` applies the same mechanism after jumping from one nonzero digit to the
next across an arbitrary zero gap. The present lemma is stronger and simpler:
it follows every single digit and will make the complete tail-state set finite
under rationality.

## Interpretation

A rational initial code supplies one finite odd denominator. Exact `2`-adic
integrality forces every division by `64` in the tail recursion to be an
ordinary integer division in the numerator. The tail can cancel denominator
factors, but it can never create a new one.

## Dependency audit

The proof uses only:

- the exact shift identity from the definition of `Phi`;
- rational membership in `Z_2`;
- ordinary divisibility by `64`.

No periodicity, real asymptotic, Padé approximation, external theorem, or
experiment is used.

## Gap audit

- The digit alphabet `{0,1}` is used only to keep the tails uniformly real
  bounded in the next theorem; the local denominator statement works for any
  fixed integer digit alphabet.
- Descending denominators alone do not yet prove periodicity. Real boundedness
  and code injectivity are added in `T-9420`.
- Rationality of `Phi(epsilon)` is equivalent to rationality of `S_0` because
  the scaling factor `17/81` is nonzero rational.

## Adversarial tests

`X-9413` verifies (2), (4), and (5) on exhaustive eventually periodic codes and
on synthetic rational transitions with odd denominators.

## Suggested next attack

Since all real digit tails lie in one compact interval, (5) leaves only
finitely many rational tail states. A repeated tail state and the exact
first-difference valuation of `L-9402` force eventual periodicity. This is
`T-9420`.
