# Exploration log: what any resolution of the conjecture has to get past

Status: **PROPOSED**. Not reviewed by anyone else. **No proof of the Collatz conjecture, and no complete
route to one, is given here.** This records one round of exploration: what was tried, what was
verified, and what each attempt reduced to. Earlier notes: Parts [I](../syracuse-poisson-identity/README.md),
[II](../syracuse-critical-cascade/README.md), [III](../syracuse-pair-chain/README.md) and
[integer points](../collatz-integer-points/README.md). Data: [`experiments/X-COL-002-excursion-law`](../../experiments/X-COL-002-excursion-law/README.md).

## 1. The filter: every argument must fail for 3x - 1

The map `(3y - 1)/2^a` on positive odd integers is the map `(3y + 1)/2^a` on negative integers. Its branches
`phi_a` on `Z_3`, its Syracuse measure and density `f`, and its 2-adic statistics are those of `3x + 1`.
Everything in Parts I to III, Tao's mixing theorem, and Proposition 15 below hold for it unchanged.
It has three known cycles, through 1, 5 and 17. Their basins among odd `N` in `[s, 2s)`:

| scale `s` | cycle of 1 | cycle of 5 | cycle of 17 |
|---|---|---|---|
| 1024 | 0.3164 | 0.3281 | 0.3555 |
| 16384 | 0.3351 | 0.3235 | 0.3414 |
| 262144 | 0.3265 | 0.3247 | 0.3488 |

and within each unit residue class mod 9 near `10^6` the shares are again 0.325 to 0.330, 0.322 to 0.329,
0.346 to 0.351. So three invariant sets of positive density coexist, each equidistributed.

**Consequence.** No argument that uses only the 2-adic and 3-adic distribution of orbits can prove the
conjecture, because its hypotheses hold for `3x - 1` and its conclusion does not. The two problems
differ only through the sign in `y_a = (2^a x -+ 1)/3`, an effect of relative size `1/x`: the real place.

## 2. Rigidity of invariant sets (why the filter bites)

**Proposition 15 (outline of proof; details not written out).** Let `E` be a set of odd positive integers
with `N in E` if and only if `Syr(N) in E`, and let `delta` be a dilation-invariant mean on subsets of the
integers (for instance an ultrafilter limit of logarithmic densities). Then there is `eta` in `[0, 1]`
such that `delta(E ∩ C) = eta . delta(C)` for every residue class `C` of odd integers prime to 3 modulo `2^j 3^i`.

*Outline.* For fixed `a`, `N -> (3N+1)/2^a` is a bijection from `{N in E : v_2(3N+1) = a, N = y mod 3^n}` onto
`{N' in E : N' = phi_a(y) mod 3^{n+1}}` multiplying sizes by `3/2^a` up to `1 + O(1/N)`. Dilation invariance and
the bound `2^-A` for the classes with `a > A` give, for the relative densities, `eps_n(y) = sum_a 2^-a eps_{n+1}(phi_a(y))`.
They also form a bounded martingale, `eps_n = E_n eps_infinity`. Passing to the limit, `eps_infinity = L* eps_infinity`
almost everywhere. The Syracuse measure `mu` is the unique stationary measure of the Markov operator `L*`,
so bounded harmonic functions are constant `mu`-almost everywhere. `mu` is absolutely continuous (Tao), and
`f > 0` almost everywhere on units: if `f(x) = 0` then `f` vanishes on the whole forward orbit of `y_0(x)` under
the ergodic rotation `A`. Hence `eps_infinity` is constant on units, and so is each `eps_n`. Classes modulo
powers of 2 follow by transporting a parity class onto a class modulo `3^k`. ∎

This is probably known in some form; I have not searched. It applies to the set of integers reaching 1,
to its complement, and to each basin of `3x - 1`, and it distinguishes none of them.

## 3. One exponent, four faces, and a verified constant

The pressure `log(3^{sigma-1}/(2^sigma - 1))` of the weights `3 . 2^-a` vanishes at `sigma = 1` and `sigma = 2`. The second zero is:

- the `L^2` criticality of the Syracuse density (Part I) and its tail `m{f > t} ~ C/t^2` (Part II);
- the exponent 1 of excursions: for a random odd `y`, `P(max_k Syr^k(y) >= r y) ~ C/r`;
- the tail of index 1 of the real series `sum 3^{i-1} 2^{-s_i}` along a backward path;
- a logarithmic term at second order in the expansion of tree densities in powers of `1/y`.

The size-biased walk has drift `m' = log 3 - (4/3) log 2`, so renewal theory predicts that the expected
number of odd iterates of `y` in `[r y, 2 r y)` is `1/(2 m' r)` for large `r`. For 100000 random `y` near `2^41`:

| `r` | 8 | 16 | 32 | 64 | 128 |
|---|---|---|---|---|---|
| observed | 0.3583 | 0.1812 | 0.0884 | 0.0442 | 0.0208 |
| `1/(2 m' r)` | 0.3583 | 0.1792 | 0.0896 | 0.0448 | 0.0224 |

and `r P(max >= r)` is between 0.78 and 0.86. For `y` uniform modulo a large power of 2 this is a theorem about
a random walk, since the first valuations are independent; it says nothing about a fixed `y` beyond about
`log_2 y` halvings. Laws of this type are in the literature (Lagarias and Weiss); I have not checked
whether this constant is stated there.

## 4. Two halves, and what each needs

*No divergent orbit* is equivalent to `min T(x) -> infinity` as `x -> infinity`, where `T(x)` is the backward tree. Since
`f_n(x) >= (x - F)/y` for every `n`-th ancestor `y` (Lemma 13), it would follow from a power saving
`sup_n f_n(x) <= C x^{1-delta}` for Syracuse atoms at integers `x`. The pole at `-1` forces at least
`x^{log_3(3/2)} = x^{0.369}` at `x = -1 mod 3^v`; the excursion law suggests `x^{1/2}`. I can prove no bound of
this kind: it concerns the atoms at specific points, the obstruction of Part III. This half may well
hold for `3x - 1` too, so it is not excluded by the filter.

*No cycle other than 1* is the half that is false for `3x - 1`. A cycle with `k` odd steps and `s` halvings
is a word `w` with `(2^s - 3^k)` dividing `K(w) = sum 3^{k-i} 2^{s_{i-1}}` and positive quotient. This is a
Diophantine statement. Nothing in these notes addresses it, and by the filter nothing in them can.

## 5. Other directions tried this round, with outcome

- Reduction through positive density of trees ([integer points](../collatz-integer-points/README.md)): equivalent to the conjecture, no gain.
- Monotone flow along orbits: gives the reformulation of §4, no bound.
- Exact weights `1/(3y+1)` (`sum over Syr(y) = x` equals `c(x)/(3x)`): exact, but only restates the tree recursion.
- Zeta functions of invariant sets: functional equations that every invariant set satisfies, as in §2.
- The chain on `Z_2 x Z_3 x R` with the same affine map in all three places and integers on the diagonal:
  organises §1 to §4, and shows a divergent orbit would produce an invariant measure with mean valuation
  at most `log_2 3`; such measures exist in abundance, so no contradiction.
- Low complexity of an integer orbit's valuation sequence: no entropy constraint follows (computable
  sequences can be normal).
