# From the Syracuse measure to individual integers: what a full proof would need

Status: **PROPOSED**. Not reviewed by anyone else. **This is not a proof of the Collatz conjecture and does
not contain one.** It records an attempt to pass from the distributional results of Parts I to III
([I](../syracuse-poisson-identity/README.md), [II](../syracuse-critical-cascade/README.md),
[III](../syracuse-pair-chain/README.md)) to statements about every integer, the exact place where
that fails, and an elementary reduction. Data: [`experiments/X-COL-001-integer-points`](../../experiments/X-COL-001-integer-points/README.md).

`Syr(y) = (3y+1)/2^a` with `a = v_2(3y+1)` on odd `y`; `T(x)` is the backward tree of `x` (all odd `y` whose orbit
reaches `x`); `Gen_n(x)` is its `n`-th generation; `f_n` is the level-`n` Syracuse density.

## 1. The Syracuse density at an integer is a sum over its Collatz ancestors

**Lemma 13.** Let `x >= 1` be an odd integer not divisible by 3. Then

    f_n(x) = 3^n mu_n(x mod 3^n) = sum_{y in Gen_n(x)} 3^n / 2^{s(y)},        3^n/2^{s(y)} = (x - F(y))/y,   0 < F(y) < x,

where `s(y)` is the number of halvings between `y` and `x`. In particular `f_n(x) <= h_n(x) := x sum_{y in Gen_n(x)} 1/y`,
and `h_{n+1}(x) = sum_a (3x/(2^a x - 1)) h_n((2^a x - 1)/3)` over the admissible `a`.

*Proof.* A word `w` of length `n` contributes to `mu_n(x)` exactly when `y = phi_w^-1(x)` is a 3-adic integer.
Since `2^{|w|}(x - phi_w(0))` is an integer, `y` is then an integer, every intermediate value is an integer,
and each is positive because `(2^a z - 1)/3 > 0` for `z >= 1`. So `w` is a path of length `n` in the
predecessor tree, and conversely. The weight is `3^n 2^-|w|`, and `x = 3^n 2^-|w| y + phi_w(0)`. ∎

This is essentially Tao's observation relating Syracuse atoms to preimage counts. What matters below is
the correction `F`: the 3-adic value of the series `sum 3^{i-1} 2^{-s_i}` along a backward path is `x`, while its
real partial sums stay below `x`. Both places enter.

## 2. Flow and an elementary reduction

Write `d_(S)` and `d^(S)` for lower and upper natural density within the odd integers.
Since `T(y)` is contained in `T(Syr(y))`, the tree density is non-decreasing along every orbit.

**Proposition 14.** Assume (A): `d_(T(x)) > 0` for every odd `x` not divisible by 3.
(i) The Collatz conjecture holds if and only if `T(1)` has density 1.
(ii) If `z` has a divergent orbit `x_k -> infinity`, then `d_(T(x_k)) >= d_(T(z)) > 0` for all `k`. Hence if
`d^(T(x)) -> 0` as `x -> infinity`, there is no divergent orbit.

*Proof.* (i) If an odd `N_0` does not reach 1, then `T(Syr(N_0))` is disjoint from `T(1)` and has positive lower
density. (ii) is the monotonicity. ∎

(A) is the linear lower bound for predecessor counts that El Jaouhari's preprint attributes to Mazur.
**I have not verified it.** Given (A), the conjecture is equivalent to an "almost all integers reach 1"
statement. That is not easier: a counterexample class above the verified range would have density of
order `1/m` for its least element `m`, so no estimate with an error term can exclude it.

## 3. Where distributional methods stop: the path of 27

Renewal heuristic: if the generation sums `h_n(x)` converge to `h(x)`, the fraction of odd integers whose
orbit passes through `x` is `2 h(x)/(x log(4/3))`. The table compares the true fraction among odd `N <= 2 . 10^6`
with this formula evaluated at level 15, where `f_15(x)` stands in for `h(x)`.

| x | true fraction | `f_15(x)` | `2 f_15/(x log 4/3)` | true / predicted |
|---|---|---|---|---|
| 7 | 0.1906 | 0.1969 | 0.1956 | 0.97 |
| 11 | 0.4448 | 0.7185 | 0.4541 | 0.98 |
| 17 | 0.4604 | 1.1435 | 0.4676 | 0.98 |
| 19 | 0.1796 | 0.4952 | 0.1812 | 0.99 |
| 29 | 0.2386 | 1.0118 | 0.2426 | 0.98 |
| 341 | 0.0377 | 1.9878 | 0.0405 | 0.93 |
| 23 | 0.4338 | 0.3576 | 0.1081 | 4.01 |
| 35 | 0.4507 | 0.7920 | 0.1573 | 2.86 |
| 53 | 0.4563 | 1.0165 | 0.1333 | 3.42 |
| 5 | 0.9380 | 0.4330 | 0.6021 | 1.56 |
| 3077 | 0.3939 | 70.09 | 0.1584 | 2.49 |

For integers off the trajectory of 27 the formula is right to a few percent. On it (`27 -> ... -> 3077 -> ... -> 23 -> 35 -> 53 -> 5`)
it is wrong by factors up to 4. The reason is visible in the tree of 23: `23 h_n`-type sums (truncated at `2 . 10^6`) are
0.33, 0.27, 0.25, 0.30, 0.36 at generations 3, 5, 8, 12, 16, then 1.39, 1.89, 1.72, 2.36 at generations 34 to 37,
where the tree contains 47, 31, 41 and 27 themselves. One ancestor `y = 27` contributes `23/27` to a single
generation sum, with 3-adic weight `3^37/2^59 = 0.78`: an extremely unlikely low-halving word carrying an
extremely large weight.

So the level densities `f_n(x)` at an integer `x` do not approach their limit until `n` passes the generation
of the smallest ancestors, and the limit is decided by those individual ancestors, that is, by the
Collatz dynamics of small numbers. A theorem about the distribution of `f` (Parts I to III, or Tao's
mixing) says nothing about them. This is the same "specific point" obstruction as in Part III, in the
form relevant to the conjecture itself.

## 4. What is missing

- A verified proof of (A).
- Either density 1 for `T(1)` with no error term at all, or decay of tree densities at infinity (which
  excludes divergence but not cycles) together with a separate exclusion of cycles.
- I have no argument for any of these, and I do not see how the tools of Parts I to III could give one:
  they control averages over 3-adic residue classes, and every statement above is about single integers.
