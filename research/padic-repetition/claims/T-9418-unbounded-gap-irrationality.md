# T-9418 — Unbounded-gap binary `64/81` series are irrational

Claim ID: `T-9418`  
Title: A rational binary `64/81` series with infinite support must have bounded gaps between its ones  
Status: `PROPOSED`  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9416`  
Scope: every infinite binary code and the ordinary `64 -> 81` section  
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Setup

Let

```text
T=64/81
```

and let a binary word have infinitely many ones at positions

```text
0<=h_0<h_1<h_2<... .
```

Put

```text
Psi
 =sum_(j>=0) T^h_j
 in Z_2 intersect R,                                   (1)
```

and let

```text
g_j=h_(j+1)-h_j.                                      (2)
```

## Theorem

If `Psi` is rational, then the set of gaps

```text
{g_j:j>=0}
```

is bounded.

Equivalently,

```text
boxed:
sup_j g_j=infinity
 -> Psi notin Q.                                      (3)
```

For the standard code map

```text
Phi(epsilon)=(17/81)Psi,                              (4)
```

the same conclusion holds. Hence every nontrivial ordinary rational or integer `64 -> 81` code with infinitely many ones has a uniform bound on the lengths of its zero runs.

## Proof

Normalize at each one:

```text
Y_j
 =sum_(k>=j)T^[h_k-h_j].                              (5)
```

Then

```text
Y_j=1+T^[g_j]Y_(j+1).                                 (6)
```

If `Psi` is rational, then `Y_0=T^(-h_0)Psi` is rational, and (6) makes every `Y_j` rational. By `L-9416`, the reduced denominator of every `Y_j` divides one fixed positive odd integer `B`.

Every gap after the leading one is at least one, so the positive real series satisfies the uniform bound

```text
1<Y_j<=sum_(n>=0)T^n=1/(1-T).                         (7)
```

Equation (6) therefore gives

```text
0<Y_j-1
 =T^[g_j]Y_(j+1)
 <=T^[g_j]/(1-T).                                     (8)
```

If the gaps are unbounded, choose a subsequence with `g_(j_k)->infinity`. Then

```text
Y_(j_k)->1                                             (9)
```

in the real embedding.

On the other hand, `Y_j` is a rational with reduced denominator dividing `B`, and `Y_j!=1` by positivity of the infinite tail. Therefore

```text
|Y_j-1|>=1/B                                          (10)
```

for every `j`, contradicting (9). This proves (3). Multiplication by the nonzero rational `17/81` proves the statement for `Phi`. **QED**

## Sharpness of the hypothesis

The theorem is one-sided.

- Bounded gaps do occur for rational values: the all-one word gives `1/(1-T)`, and every eventually periodic binary word gives a rational value.
- Finite support gives a rational value and has no infinite gap sequence.
- Unbounded gaps, rather than low factor complexity or periodicity, are the decisive input.

Thus the theorem does not classify all rational binary `64/81` series. It excludes precisely the sparse regime containing the active stack construction.

## Relationship to earlier rigidity

`T-9401` used one repeated factor to create an eventually periodic rational approximant of small height. The present theorem uses exact rationality of every one-tail and a descending denominator chain. It is therefore insensitive to raw factor complexity and survives the unbounded-padding phenomenon of `R-9401`.

The conclusion supplies a new necessary condition for any ordinary M1 witness:

```text
infinite support + ordinary rationality
 -> bounded zero runs.                                (11)
```

It does not by itself exclude a dense, high-complexity ordinary survivor code.

## Dependency audit

- `L-9416` supplies fixed denominator divisibility.
- The only real estimate is the geometric bound (7).
- No external theorem, finite computation, density assumption, or automaticity hypothesis is used.

## Gap audit

- The code must have infinitely many ones. A finite-support code is outside the theorem.
- The proof relies on the positive digit alphabet `{0,1}`. Signed cancellation could destroy (8).
- Bounded gaps are necessary, not sufficient, for rationality.
- The theorem constrains M1 but does not settle the full survivor attractor.

## Adversarial tests

`X-9413` checks the exact recurrence, denominator descent, geometric upper bound on finite tails, and bounded-gap rational controls.

## Suggested next attack

Apply (3) to the sparse stack normal form of `L-9407`. Its successive gaps are `9m_t+1` and diverge under every positive height-increment directive. This gives a source-independent all-directive obstruction in `T-9419`.
