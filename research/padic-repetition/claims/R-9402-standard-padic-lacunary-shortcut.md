# R-9402 — Standard `p`-adic lacunary theorems do not cover the stack value

Claim ID: R-9402  
Title: Exact hypothesis failure for the Bugeaud–Kekeç lacunary-value theorems  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9407, T-9410, T-9411  
Scope: the direct application of Bugeaud–Kekeç (2020), Theorems 2.1 and 2.2  
Related counterexample candidates: Q-9409; no `K-####` candidate

## Source audited

Y. Bugeaud and G. Kekeç, *On Mahler's p-adic S-, T-, and U-numbers*,
Analele Științifice ale Universității Ovidius Constanța, 28(1) (2020),
81--94, DOI `10.2478/auom-2020-0005`.

The paper proves transcendence and Mahler-classification results for two kinds
of `p`-adic lacunary power series. This file records the exact comparison with
the sparse stack series

```text
F(T)=sum_(j>=0) T^H_j,
alpha=64/81 in Q_2.                                 (1)
```

It is an applicability audit, not a criticism of the source theorem.

## Refutation 1 — Theorem 2.1 coefficient-decay route

The source Theorem 2.1 considers

```text
f(x)=sum_k c_k*x^(e_k)
```

with coefficient valuations satisfying

```text
|c_k|_p <= p^(-u_k),
u_k positive,
liminf u_(k+1)/u_k >1,
lim u_k/e_k = infinity.                             (2)
```

For (1), every nonzero coefficient is

```text
c_k=1,
|c_k|_2=1.                                          (3)
```

No positive `u_k` can satisfy `1<=2^(-u_k)`. Thus the theorem fails already at
its coefficient-decay hypothesis. The quadratic growth of `H_k` cannot replace
the missing `2`-adic decay of `c_k`.

## Refutation 2 — Theorem 2.2 zero-gap route

The source Theorem 2.2 assumes zero intervals

```text
r_n < h < s_n
```

with nonzero endpoint coefficients and, critically,

```text
theta=liminf s_n/r_n >1.                            (4)
```

For the support of (1), the maximal zero intervals have endpoints at
consecutive support positions. Therefore, up to an index shift, the only
available choice is

```text
r_n=H_n,
s_n=H_(n+1).                                       (5)
```

T-9410 gives

```text
H_(n+1)/H_n ->1.                                    (6)
```

Hence

```text
theta=1,                                            (7)
```

which violates the strict hypothesis (4). Skipping a support point cannot
increase `theta`, because the skipped nonzero coefficient would lie inside the
purported zero interval.

## Quantitative height failure

For completeness, the source Theorem 2.2 also requires

```text
lambda+sigma+log max(|a|,|b|)
 <(theta/2)*log(R/|alpha|_p),                        (8)
```

for `alpha=b/a`.

For (1):

```text
lambda=0                 (integer coefficients),
sigma=0                  (numerators are 0 or 1),
R=1                      (p-adic radius),
alpha=64/81,
|alpha|_2=1/64,
max(|a|,|b|)=81.                                    (9)
```

Thus (8) would read

```text
log 81 < (theta/2)*log 64,                           (10)
```

or

```text
theta > 2*log_64(81)=2.113283334294... .            (11)
```

The actual value is `theta=1`. So even apart from the strict multiplicative-gap
failure, the source height inequality misses by a fixed quantitative margin.

## Relation to T-9411

The source proof uses rational partial sums and a Ridout-type approximation
exponent greater than two. T-9411 computes the exact direct-truncation exponent
for (1):

```text
1/log_64(81)=0.946394630357... .                     (12)
```

This is consistent with the source-theorem failure. The issue is not a loose
constant or denominator cancellation overlooked in the audit; direct partial
sums are far below the required approximation regime.

## Formal conclusion

The following inference is **refuted**:

> "The stack series is sparse/lacunary, therefore a standard `p`-adic
> lacunary-series transcendence theorem applies."

The correct statement is:

> the nearest located primary theorem requires multiplicative support gaps
> bounded away from one and a stronger height inequality; the stack support is
> additive/quadratic with consecutive support ratio tending to one.

No conclusion about rationality, algebraicity, or transcendence of (1) follows
from this refutation.

## What remains potentially usable

The source method suggests what a successful replacement must provide:

```text
- approximants stronger than ordinary partial sums;
- an effective denominator-height saving;
- or simultaneous linear forms produced by repeated S-adic standard words.
```

L-9408 supplies an exact transfer-polynomial interface for pursuing that gain.

## Dependency audit

- L-9407 supplies the exact series.
- T-9410 supplies the support ratio limit.
- T-9411 supplies the exact direct-truncation exponent.
- The source theorem is used only for an applicability comparison; it is not a
  proof dependency for any positive native theorem.

## Gap audit

- Failure of a theorem's hypotheses is not evidence that the target value is
  algebraic.
- Other `p`-adic lacunary or Mahler theorems may use different hypotheses and
  require separate audits.
- The radius `R=1` is the `2`-adic power-series radius in the formal variable
  `T`, not a statement about real convergence.
- The coefficient-decay theorem and zero-gap theorem are distinct; both are
  audited separately.

## Suggested next attack

Use L-9408 to construct standard-word Padé or determinant approximants, then
measure whether their reduced height and `2`-adic vanishing cross the exact
barrier in T-9411.