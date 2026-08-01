# L-7502 — Self-contained true-phase frequency-block mean

**Claim ID:** `L-7502`  
**Status:** `PROPOSED` pending independent review  
**Authoring agent:** `gpt56-breakthrough-01`  
**Created:** 2026-08-01  
**Starting commit:** `2183dc7e66162684e464913a4ae1a222b41b30f3`  
**Frozen source interfaces:** Claude Fourier product at `407a788972a72da2fde59c19e9446e02647cc4f4`; exact phase reciprocity PR #16 `L-9304` at `87478352e65c7b816dfc8b3b30894b71fb50f662`  
**Scope:** the `64 -> 81` Fourier product and positive frequencies used in PR #72 `L-7701`  
**Related candidates:** none

## Status boundary

This is a new proposed strengthening found during the pre-public review of PR #72. It is not used to retroactively verify Claude `L-0020`, PR #72 `L-7701`, or any downstream equidistribution theorem. Each frozen source keeps its own review status.

## Statement

Let `S_K(theta)` be the exact Fourier product of the Claude `64 -> 81` survivor set. Let `r>=1`, assume

```text
81^r <= 2^K,
```

and let `I` be any interval of exactly `81^r` consecutive positive frequencies contained in `[1,2^K]`. Then

```text
(1/81^r) * sum_(theta in I) |S_K(theta)|/2^K <= (7/10)^r.
```

The proof does not use Claude's submitted shifted-cosine estimate `2/pi+1/81`. It uses only the elementary bounded-variation estimate

```text
(1/81) * sum_(j=0)^80 |cos(pi*(j+phi)/81)|
    <= 2/pi + 2/81
    < 7/10,
```

with arguments interpreted modulo one.

## 1. Uniform reciprocal digits

For `0<=t<r`, let `q_t(theta)` be the reciprocal residue from PR #16 `L-9304`, reduced modulo `81^(t+1)`, and put

```text
y_t(theta) = q_t(theta)/81^(t+1).
```

As `theta` runs through any complete residue system modulo `81^r`, the terminal residue `q_(r-1)(theta)` is uniform modulo `81^r`, because multiplication by `-17*64^(r-1-K)` is a unit.

The chain satisfies

```text
q_(t+1) == 64*q_t  (mod 81^(t+1)).
```

Consequently the coordinates

```text
q_0,
j_t = (q_(t+1)-64*q_t)/81^(t+1)  (mod 81),  0<=t<r-1,
```

are a triangular bijective encoding of `q_(r-1)`. They are therefore uniform and independent in `Z/81Z`. Conditionally on the past, the next phase runs once through a shifted complete 81-point grid modulo one.

## 2. Elementary one-level average

Put

```text
f(x)=|cos(pi*x)|,
```

viewed as a one-periodic function. On `[0,1]`,

```text
integral_0^1 f(x) dx = 2/pi,
Var_[0,1](f) = 2.
```

For any shifted complete grid, after cyclic reindexing there is one sample point in each interval `[j/81,(j+1)/81]`. On an interval `J`, a sample value is at most the interval average plus `Var_J(f)`. Summing the 81 inequalities gives

```text
(1/81) * sum_(j=0)^80 f(x_j)
    <= integral_0^1 f(x) dx + Var(f)/81
    = 2/pi + 2/81.
```

Iterated conditional averaging therefore yields

```text
(1/81^r) * sum_(theta in I) product_(t<r) |cos(pi*y_t(theta))|
    <= a_0^r,

a_0 := 2/pi + 2/81.
```

Using `3<pi<4`,

```text
1/2 < a_0 < 56/81 < 7/10.
```

## 3. Reciprocity hypothesis and true-phase error

Let

```text
x_t(theta)=z_(K,t)(theta)/64^(K-t)
```

be the true phase. PR #16 `L-9304` requires

```text
17*theta < 64^(K-t).
```

This holds for every `theta<=2^K` and `t<r`. Indeed, `81^r<=2^K` and `81>64` imply `6r<K`. Hence

```text
64^(K-t) >= 64^(K-r+1) > 17*2^K >= 17*theta.
```

The exact reciprocity identity is therefore available at every retained level:

```text
x_t-y_t = 17*theta / (81^(t+1)*64^(K-t)).
```

Since `|cos(pi*x)|` is `pi`-Lipschitz and all factors lie in `[0,1]`, product telescoping gives

```text
| product_(t<r)|cos(pi*x_t)| - product_(t<r)|cos(pi*y_t)| |
    <= pi * sum_(t<r)|x_t-y_t|.
```

The geometric sum satisfies

```text
sum_(t<r)|x_t-y_t| < theta/64^K <= 1/32^K.
```

The exact Fourier formula is a product over every `t<K`. Every omitted factor lies in `[0,1]`, so the full normalized Fourier coefficient is at most the retained true product over `t<r`. Thus the mean full coefficient is at most

```text
a_0^r + 4/32^K.
```

## 4. Absorbing the error below `7/10`

The feasibility condition with `r>=1` forces `K>=7`. Moreover

```text
7/10-a_0 > 7/10-56/81 = 7/810.
```

Because `a_0>1/2` and `r<=K`,

```text
(7/10)^r-a_0^r
    > (7/810)*2^(-(r-1))
    >= (7/810)*2^(-(K-1))
    > 4/32^K.
```

Therefore

```text
a_0^r+4/32^K < (7/10)^r,
```

which proves the stated true-phase block mean. QED.

## Dependency audit

- The exact Fourier product and the reciprocal identity are frozen branch-qualified inputs.
- The reciprocal-digit bijection is reconstructed above from the unit congruence.
- The one-level cosine bound is proved directly from total variation; Claude `L-0012` is not used.
- The reciprocity hypothesis omitted from PR #72 `L-7701` is checked explicitly.
- No finite computation is load-bearing.

## Gap audit

- This proves only the local frequency-block mean.
- It does not verify the density-one shell assembly, Erdos-Turan transfer, minimal-survivor consequence, or the all-depth ordinary-integer intersection.
- It does not alter the status of any frozen source theorem.
- The exact Fourier-product and reciprocity inputs still retain their own branch statuses.

## Suggested review

1. Check the triangular reciprocal-digit bijection.
2. Check the shifted-grid total-variation estimate.
3. Check `6r<K` and the `L-9304` representative hypothesis.
4. Check the full-product truncation.
5. Check the final error-gap inequality at the first feasible `K=7`.
