# T-8809 — Two-color multiplicative syndeticity

Claim ID: T-8809  
Title: Both symbols in every ordinary `4/5` survivor directive occur at every multiplicative scale  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: T-8802  
Scope: every hypothetical positive ordinary infinite `4 -> 5` chart orbit  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Suppose a positive ordinary integer `A` remains forever in the exact chart of
T-8802. Put

```text
M=A+2>=3
```

and let `eps in {0,1}^N` be its phase directive, so in `Q_2`

```text
M=(1/5)*sum_(n>=0) eps_n*(4/5)^n.                    (1)
```

For `sigma in {0,1}`, enumerate the support of that symbol as

```text
0<=h_(sigma,0)<h_(sigma,1)<...,
eps_(h_(sigma,j))=sigma.
```

Then both supports are infinite. Moreover, for every `sigma` and every `j>=0`,

```text
4^(h_(sigma,j+1))
  <= 5*M*5^(h_(sigma,j)).                            (2)
```

Put

```text
alpha=log_4(5)>1,
delta=alpha-1,
C=log_4(5M),
rho=C/delta.
```

Then

```text
h_(sigma,j+1) <= alpha*h_(sigma,j)+C,                 (3)
```

and, for all `n>=0`,

```text
h_(sigma,j+n)+rho
  <= alpha^n*(h_(sigma,j)+rho).                       (4)
```

Let

```text
N_sigma(Y)=#{j:h_(sigma,j)<=Y}.
```

For all real `Y>=X>=h_(sigma,0)`,

```text
N_sigma(Y)-N_sigma(X)
  >= floor(log_alpha((Y+rho)/(X+rho))).               (5)
```

Equivalently, every interval

```text
(X, alpha*X+C]
```

contains an occurrence of `sigma`. In particular, for both symbols,

```text
liminf_(Y->infinity) N_sigma(Y)/log(Y)
  >= 1/log(alpha)
  = 6.70013449289... .                                (6)
```

Thus neither the `0` digits nor the `1` digits of an ordinary survivor may be
arbitrarily sparse on a multiplicative scale.

## Motivation

A branch-qualified corollary of PR #34's T-9819 supplied the first support-gap
bound for the `1` digits. The argument is elementary enough to reconstruct
inside this isolated packet, and the complement identity supplies a symmetric
result for the `0` digits with the same sharp elementary constant `5M`.

This is stronger than saying that both symbols occur infinitely often and is
logically independent of the factor-complexity theorem T-8803. It is still a
necessary condition, not an existence or nonexistence theorem.

## Proof

### Both supports are infinite

Multiply (1) by `5` and write

```text
Psi_1=sum_(eps_n=1)(4/5)^n=5M.                       (7)
```

If the support of `1` were finite and nonempty with largest index `h`, then
multiplication by `5^h` would give

```text
5^(h+1)M=sum_(n<=h)eps_n*4^n*5^(h-n).
```

Modulo `5`, the right side is `4^h`, while the left side is zero, a
contradiction. Empty support would give `M=0`.

The all-one geometric series equals `5`, so the complementary support satisfies

```text
Psi_0=sum_(eps_n=0)(4/5)^n=5(1-M).                   (8)
```

The same last-term argument excludes a finite nonempty zero support. Empty zero
support would force `M=1`, contradicting `M>=3`.

### Exact first-omitted valuation

Fix one symbol and abbreviate its support by `h_0<h_1<...` and its integer value
from (7) or (8) by `Psi`. Let

```text
S_j=sum_(k=0)^j (4/5)^(h_k),
E_j=Psi-S_j.
```

The first omitted term has `2`-adic valuation `2h_(j+1)`. Every later term has
valuation at least `2h_(j+1)+2`, so the ultrametric minimum is unique:

```text
v_2(E_j)=2h_(j+1).                                   (9)
```

The ordinary denominator of `E_j` divides `5^(h_j)`. Therefore its nonzero
ordinary numerator is divisible by `4^(h_(j+1))`, and

```text
|E_j| >= 4^(h_(j+1))/5^(h_j).                        (10)
```

### Uniform real upper bound

For the `1` support, `Psi=5M` and `0<=S_j<=5`, so

```text
0<E_j<=5M.
```

For the `0` support, `Psi=5(1-M)<0`; hence

```text
|E_j|=5(M-1)+S_j<=5M.
```

Combining either upper bound with (10) proves (2).

Taking logarithms gives (3). Adding `rho=C/(alpha-1)` converts (3) into

```text
h_(j+1)+rho<=alpha*(h_j+rho),
```

whose iteration is (4).

For (5), choose the last support point `h_r<=X`. Then `h_(r+1)>X`, while (4)
shows that every

```text
1<=n<=floor(log_alpha((Y+rho)/(X+rho)))
```

produces a distinct support point `h_(r+n)<=Y`. Formula (6) follows by taking a
fixed initial `X` and dividing by `log Y`. **QED**

## Dependency audit

- T-8802 supplies only the ordinary completion identity (1).
- The proof reconstructs the first-omitted-term height argument directly and
  does not depend on the review status of PR #34.
- No real value is assigned to the nonperiodic infinite series. Real estimates
  are applied only to the fixed rational `Psi` and finite rational sums `S_j`.

## Gap audit

- Logarithmically many occurrences do not imply positive digit frequency,
  normality, or positive entropy.
- The additive constant depends on the fixed integer `M`.
- The two support estimates may hold simultaneously for many nonperiodic binary
  words; they are not sufficient for rationality.
- The proof requires infinite support before referring to a next support point.
- Thinness of either symbol does not translate automatically into a stopping
  bound without an independent upper estimate for the physical word.

## Adversarial tests

- Constant directives are excluded at the first step: they correspond to the
  negative completions in T-8802, not `M>=3`.
- The proof treats the negative complementary value without changing its
  `2`-adic valuation or silently comparing infinite limits across completions.
- The constant is the same `5M` for both symbols; no absolute-value sign is lost.

## Remaining uncertainty

A contradiction would follow from an independent theorem forcing either symbol
to have fewer than `1/log(log_4 5)` support points per logarithmic scale. No
such physical grammar upper bound is presently established.

## Suggested next attack

Combine (5) with a finite-state or Diophantine description of long bottom-word
prefixes. In particular, any theorem forcing supermultiplicative gaps in one
symbol would close the ordinary survivor problem immediately.
