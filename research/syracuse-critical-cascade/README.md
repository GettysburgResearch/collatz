# The Syracuse density as a critical cascade

Status: **PROPOSED**. Not reviewed by anyone else. Continues
[`../syracuse-poisson-identity`](../syracuse-poisson-identity/README.md) (Part I); notation as there.
Checks and data: [`experiments/X-SYR-002-critical-cascade`](../../experiments/X-SYR-002-critical-cascade/README.md).

## 0. Summary

Part I reduced linear growth of the Syracuse collision energy `Q_n = ||f_n||^2` to one conjecture
(C1: the increments `a_n = Q_{n+1} - Q_n` are bounded). **C1 is still open after this note.**
What is added:

1. **Cascade form (§1).** `f` is the fixed point of a smoothing transform `f(x) = sum_a T_a f(y_a(x))`
   with `E sum T_a = E sum T_a^2 = 1`: a Mandelbrot cascade at its critical exponent 2, whose
   siblings are the points `y, Ay, A^2 y, ...` of the odometer `A y = 4y + 1` instead of being independent.
2. **Singular value decomposition (§2, Theorem 4).** `L` maps characters of `1 + 3y` to explicit
   combinations of two Dirichlet characters of `x`; the change of basis back is a Jacobi sum of constant modulus.
3. **Selection rule (§3, Theorem 5).** In the singular basis the odometer shift `V^j` couples two modes
   only if their 3-adic distance equals `|j|_3`. Hence `L` is an isometry on every singular
   image up to an error `2/(4^(3^kappa) - 1)`: criticality holds mode by mode, not only on average.
4. **Pair operator (§4, Theorem 6).** `L* C_g L = sum 3 2^-(a+b) C_g'` for every affine `g(x) = 2^c x + B`.
   Part I's Theorem 1 is the case `g = id`. The identity is the only resonant point (Lemma 7).
5. **Renewal law (§5, Theorem 8, Proposition 9).** Bounded increments give
   `int min(f,S)^2 <= (sup a_n / m') log S + C` with `m' = log 3 - (4/3) log 2`, and if
   `a_* = sum_{j != 0} 4^-|j| int f . f o A^j` is finite then `int min(f,S)^2 ~ (a_*/m') log S`.
   So the open linear upper bound implies a sharp form of the open weak-L^2 bound, with the
   constant `a_* / (2 log 3 - (8/3) log 2)` for the tail `t^2 m{f > t}` whenever that limit exists.
6. **Level 18 (§6).** The cascade form gives a much faster algorithm (level 18 in a few minutes).
   Increments of `a_n` shrink by a factor 0.88 to 0.91 per level, so `a_n -> 0.475(1)`,
   inside Part I's stated range and slightly below `a_1 = 10/21`.

Prior work is as listed in Part I (Tao; El Jaouhari, Zenodo 10.5281/zenodo.23377671, which I have read
only through an automated fetch and have not verified). Proposition 9 uses `f in L^p` for some `p > 1`,
which is El Jaouhari's Theorem B; everything else here uses only Tao's absolute continuity.

## 1. Cascade form

For a unit `x` let `a_0 = 1` if `x = 2 (mod 3)` and `a_0 = 2` if `x = 1 (mod 3)`, and
`y_0 = (2^{a_0} x - 1)/3`. The admissible exponents are `a = a_0 + 2i`, with `y_a = A^i y_0`, `T_a = 3 . 2^-a`. Then

    f_{n+1}(x) = sum_{i >= 0} T_{a_0+2i} f_n(A^i y_0) = c(x) (M f_n)(y_0),    M = (3/4) sum_{i>=0} 4^-i V^i,

with `c = 2, 1, 0` on `x = 2, 1, 0 (mod 3)`. For each `a` the map `x -> y_a` carries the class
`2^-a + 3Z_3` (measure 1/3) onto `Z_3` and scales Haar measure by 3, so for every `p`

    E_x sum_a T_a^p g(y_a) = (3^{p-1}/(2^p - 1)) int g      (if g = 1: equals 1 exactly at p = 1 and p = 2).

`p = 1` is mass conservation; `p = 2` is the criticality behind Part I. The size-biased law of the
exponent is `pi_a = 3 . 4^-a`, and `log T_a` has `pi`-mean `m' = log 3 - (4/3) log 2 = 0.17442`.
Evaluating `M` by 30 gathers along the odometer gives level `n+1` from level `n` in `O(30 . 3^n)`.

## 2. Singular value decomposition

Write units as `x = +-4^h`, `h in Z_3`, and for `xi = r/3^k` with `3` not dividing `r` (`k >= 1`) put

    psi_xi(y) = e(xi log_4(1 + 3y)),     Psi_xi(4^h) = e(xi h),   Psi_xi(-4^h) = 2 e(-xi/2) e(xi h),   Psi_xi = 0 on 3Z_3.

**Theorem 4.** `L psi_xi = sigma(xi) Psi_xi` with `sigma(xi) = 3e(xi)/(4 - e(xi))`. The `psi_xi` are an
orthonormal basis of the exact level `k` of `L^2(Z_3)`; the `Psi_xi` are orthogonal with norm squared
`5/3` and lie in exact level `k+1`. So the singular values of `L` on exact level `k` are
`|sigma(xi)| sqrt(5/3) = sqrt(15/(17 - 8 cos 2 pi xi))`, and `Psi_xi = ((1 + 2e(-xi/2)) chi_+ + (1 - 2e(-xi/2)) chi_-)/2`
where `chi_+-` are the Dirichlet characters mod `3^{k+1}` with `chi(4) = e(xi)`, `chi(-1) = +-1`.

*Proof.* For `x = 4^h` the admissible `a = 2i` give `1 + 3y_a = 4^{h+i}`, so `(L psi)(4^h) = 3 sum_{i>=1} 4^-i e(xi(h+i))`.
For `x = -4^h`, `a = 2i+1` and `1 + 3y_a = -2 . 4^{i+h} = 4^{h+i+1/2}` since `4^{1/2} = -2` in `Z_3`,
which gives `(3/2) sum_{i>=0} 4^-i e(xi(h+i+1/2))`. Both sums are geometric. Orthogonality of the `psi`
is orthogonality of characters of `Z_3` in the coordinate `log_4(1+3y)`; for the `Psi` it is the same on
each of the two cosets, with weights `1` and `4` on sets of measure `1/3`. ∎

**Proposition (flat kernel; verified for k <= 3, proof not written out).** For `eta = s/3^{k+1}`:
`|<Psi_xi, psi_eta>|^2 = 3^-(k+1) c(x_0)^2`, where `x_0 = r/s (mod 3)` is the stationary point of the
phase and `c` is the cascade weight; it vanishes when `3 | s`. This is a Jacobi sum of `chi_+-` against
a character of `1 + 3x`.

## 3. Selection rule and mode-wise criticality

**Theorem 5.** Let `xi = r/3^k`, `xi' = r'/3^k`, `j != 0`, `kappa = floor((k+1)/2)`. If
`v_3(r - r') != v_3(j)` and `min(v_3(r - r'), v_3(j)) < kappa`, then `<Psi_xi o A^j, Psi_xi'> = 0`.
In particular `<Psi_xi o A^j, Psi_xi> = 0` for every `j` not divisible by `3^kappa`, and

    | ||L Psi_xi||^2 / ||Psi_xi||^2 - 1 |  <=  2/(4^(3^kappa) - 1).

*Proof.* It suffices to treat Dirichlet characters `chi, chi'` mod `3^{k+1}` restricting to `e(r log_4/3^k)`,
`e(r' log_4/3^k)` on `1 + 3Z_3`. Let `z = 4^j x + B`, `B = (4^j - 1)/3`, so `v_3(B) = v_3(j)`, and
`I = int chi(z) conj(chi'(x)) dx` over units `x` with `z` a unit. Take `m = ceil((k+1)/2)` and
`w = 1 + 3^m tau`. The substitution `x -> xw` preserves Haar measure and sends `z` to `z(1 + 3^m tau (1 - B/z))`.
Since `2m >= k+1`, `s -> chi(1 + 3^m s)` is the additive character `e(theta r s/3^{k-m+1})` with a unit
`theta` independent of `chi`. Hence, for every `tau`,

    I = int chi(z) conj(chi'(x)) e(theta tau [r(1 - B/z) - r'] / 3^{k-m+1}) dx.

Averaging over `tau` leaves only `x` with `(r - r') z = rB (mod 3^{kappa})`. As `z` and `r` are units,
this is impossible when the two valuations differ and the smaller one is below `kappa`. The norm
statement follows from Part I's Theorem 1, `||L g||^2 = sum_j 4^-|j| <g, g o A^j>`, and
`sum_{j != 0, 3^kappa | j} 4^-|j| = 2/(4^(3^kappa) - 1)`. ∎

Numerically the rule holds with "iff" and without the restriction to `kappa` for all `j <= 3^k`, `k <= 3`,
and the non-zero entries have constant modulus `2 . 3^-(k+1)/2` when `3` does not divide `j`.

**What it gives.** `||L^2 psi_xi||^2 = 15/(17 - 8 cos 2 pi xi)` up to that doubly exponentially small error,
and the mean of `15/(17 - 8 cos theta)` over the circle is exactly 1. So two steps of `L` preserve energy
on average over modes, and one step preserves it on each singular image.

**What it does not give.** For `d_n = f_{n+1} - f_n = sum_r c_r sigma_r Psi_r`,

    a_{n+1} - a_n = sum_{j != 0} 4^-|j| sum_{v_3(r - r') = v_3(j)} c_r sigma_r conj(c_r' sigma_r') <Psi_r o A^j, Psi_r'>.

The diagonal is absent and the leading terms `j = +-1, +-2` pair the two halves `r = 1` and `r = 2 (mod 3)`
of the odometer spectrum through a kernel of constant modulus. Bounding this for the specific
coefficients `c_r` of `d_{n-1}` is exactly C1; the rule removes the diagonal but not the problem.

## 4. Pair operator

For an affine bijection `g(x) = 2^c x + B` of `Z_3` (`c in Z`, `B in Z_3`) let `(C_g h)(x) = h(g(x))`.

**Theorem 6.** `L* C_g L = sum 3 . 2^-(a+b) C_{g'}`, the sum over `a, b >= 1` with
`2^{c+b-a} + 2^b B = 1 (mod 3)`, where `g'(y) = 2^{c+b-a} y + (2^{c+b-a} + 2^b B - 1)/3`.

*Proof.* `<Lu, C_g Lv> = 9 sum_{a,b} 2^-(a+b) int 1[x in Im phi_a] 1[g(x) in Im phi_b] u(phi_a^-1 x) v(phi_b^-1 g x) dx`.
Put `x = phi_a(y)`. The condition `g(phi_a(y)) in Im phi_b` depends only on `2^{c+b-a} + 2^b B (mod 3)`, not on `y`,
and `phi_b^-1 g phi_a = g'`. ∎

With `Q_n(g) = <f_n, f_n o g>` this is the recursion `Q_{n+1}(g) = sum 3 . 2^-(a+b) Q_n(g')`, and
`Q_n(c, B)` is the level-`n` density at `B` of `X~ - 2^c X` for independent Syracuse variables. In the
coordinate `L = log_4(1 + 3X)`, `gamma_n(j) = Q_n(A^j)` is the density of `L~ - L` at the integer `j`.

**Lemma 7 (no resonance off the identity).** If `phi_w~ = A^j phi_w` for two words, then `j = 0` and `w~ = w`.

*Proof.* Slopes force equal length `l` and `|w~| = |w| - 2j`. With `N(w) = 2^|w| (1 + 3 phi_w(0)) = sum_{i=0}^{l} 3^i 2^{e_i}`,
`e_i = a_{i+1} + ... + a_l`, comparing constant terms gives `N(w~) = N(w)`. The exponents `e_0 > ... > e_l = 0`
are recovered from `N` by 2-adic valuations, starting with `v_2(N - 3^l) = a_l`. ∎

So the logarithmic singularity of the difference density sits only at `0`: the points `j != 0` where C1
asks for boundedness are never reached exactly by coinciding histories.

## 5. Renewal law for truncated second moments

Let `Phi_n(S) = int min(f_n, S)^2`, `Phi(S) = int min(f, S)^2`, and `x_a = T_a f_n(y_a)`.

**Theorem 8.** There are absolute constants `C_0, C_1` such that for all `n` and `S >= 1`

    Phi_n(S) <= C_0 + (max_{m<n} a_m) (log S / m' + C_1).

Consequently, if `abar = sup a_n` is finite, then `Phi(S) <= (abar/m') log S + C` and `m{f > t} <= ((abar/m') log t + C)/t^2`.
Conversely, if `Phi(S) = O(log S)` then `Q_n = O(n)`.

*Proof.* (a) By §1, `Phi_{n+1}(S) = sum_a pi_a Phi_n(S/T_a) + rho_n(S)` with
`rho_n(S) = E[min(sum_a x_a, S)^2 - sum_a min(x_a, S)^2]`.
(b) Pointwise, `|min(sum x_a, S)^2 - sum min(x_a,S)^2| <= sum_{a != b} x_a x_b`, whose mean is `a_n` by Part I's
Theorem 1. Also `|rho_n(S)| <= 2 S^2 (1 + log(1/S))` for `S <= 1`, from `Phi_m(S') <= min(S', S'^2)`.
(c) Iterating, with `S_k` the random walk of steps `log T_a` under `pi` and `u = log S`,
`Phi_n(S) = E Phi_0(S e^{-S_n}) + sum_{k<n} E rho_{n-1-k}(S e^{-S_k})`.
(d) The walk has drift `m' > 0` and upward steps at most `log(3/2)`, so `sum_k P(S_k <= u) <= (u + log(3/2))/m' + c_0`
by Wald's identity, and its renewal measure has bounded mass on unit intervals; this bounds the terms
with `S_k > u` through (b). Letting `n -> infinity` uses `f_n -> f` almost everywhere and bounded convergence.
For the converse, `Q_n = int f_n f <= sqrt(Q_n Phi(S)) + 2^n int f 1[f > S]` with `S = n^2 2^n`. ∎

**Proposition 9.** Assume `f in L^p` for some `p > 1` and `a_* = sum_{j != 0} 4^-|j| int f . (f o A^j) < infinity`. Then

    int min(f, S)^2 = (a_*/m') log S (1 + o(1)),

and if `t^2 m{f > t}` has a limit, the limit is `a_*/(2m') = a_*/(2 log 3 - (8/3) log 2)`.
Moreover `a_* <= liminf a_n`, so `a_* < infinity` whenever `Q_n = O(n)`.

*Proof.* `f = L f` gives `Phi(S) = sum_a pi_a Phi(S/T_a) + rho(S)` with `|rho| <= a_*` and `rho(S) -> a_*` by dominated
convergence. After `K` iterations the remainder is `E Phi(S e^{-S_K}) <= ||f||_p^p S^{2-p} theta^K` with
`theta = 3^{p-1}/(2^p - 1) < 1` for `1 < p < 2`. So `Phi = rho * U` for the renewal measure `U`, and the elementary
renewal theorem gives the limit. Fatou's lemma gives `a_* <= liminf a_n`. ∎

In an independent cascade this is the Guivarc'h and Liu tail constant. Here independence is replaced by the
single number `a_*`, the same odometer correlation sum that governs the energy.

## 6. Numerics to level 18

| n | Q_n | a_{n-1} | increment ratio | gamma_n(1) | gamma_n(2) | max f_n | min on units |
|---|---|---|---|---|---|---|---|
| 8 | 4.931742 | 0.465921 | -0.634 | 0.719261 | 0.474482 | 37.3 | 0.07507 |
| 10 | 5.865789 | 0.467387 | 0.987 | 0.722762 | 0.473125 | 84.2 | 0.06088 |
| 12 | 6.802899 | 0.468941 | 0.989 | 0.725655 | 0.473245 | 189.6 | 0.05292 |
| 13 | 7.272514 | 0.469615 | 0.872 | 0.726921 | 0.473282 | 284.5 | 0.05010 |
| 14 | 7.742768 | 0.470254 | 0.949 | 0.728069 | 0.473263 | 426.8 | 0.04692 |
| 15 | 8.213596 | 0.470828 | 0.897 | 0.729099 | 0.473334 | 640.2 | 0.04411 |
| 16 | 8.684948 | 0.471352 | 0.914 | 0.730013 | 0.473408 | 960.3 | 0.04293 |
| 17 | 9.156768 | 0.471820 | 0.894 | 0.730819 | 0.473467 | 1440.6 | 0.04175 |
| 18 | 9.629001 | 0.472233 | 0.882 | 0.731525 | 0.473514 | 2160.9 | 0.04042 |

"Increment ratio" is `(a_{n-1} - a_{n-2})/(a_{n-2} - a_{n-3})`. Data: `results_levels_18.json`, double precision.

- **Energy slope.** The increments of `a_n` shrink by 0.88 to 0.91 per level from level 13 on, and those of
  `gamma_n(1)` by 0.911, 0.907, 0.897, 0.888, 0.883, 0.874 (levels 13 to 18), still decreasing. A geometric
  tail with ratio between 0.866 and 0.91 gives `a_n -> 0.4749 ... 0.4764` and `gamma_n(1) -> 0.736 ... 0.739`.
  `gamma_n(2)` has converged to 0.4735: only the lag `+-1` converges slowly, because `A phi_2 = phi_1 B`
  with `B y = 2y + 1` fixing the pole `-1`.
- **Tail.** `t^2 m{f_18 > t}` = 0.50, 0.74, 0.92, 1.01, 1.00, 0.99 at `t` = 2, 4, 8, 16, 24, 32; the values
  for `t <= 8` are stable in `n` to one percent. Proposition 9 with `a_* = 0.475` predicts the limit 1.36.
- **Truncated moments.** `Phi_18(S)` = 1.76, 2.92, 4.26, 5.65, 6.95 at `S` = 4, 8, 16, 32, 64: increments per
  doubling 1.16, 1.34, 1.39, 1.30 (the last is affected by the finite level), against the asymptotic
  `(a_*/m') log 2 = 1.89`.
- **Why the approach is slow.** The truncated correlation `int min(f,S) . min(f,S) o A` at level 18 is
  0.371, 0.478, 0.562, 0.623, 0.665, 0.692 at `S` = 4, ..., 128, against 0.7315 untruncated: each doubling
  of `S` recovers about 0.7 of the previous gain. The remainder `rho(S)` in §5 inherits this, so the
  renewal limit is approached like a small negative power of `S`. The data are consistent with the
  prediction and do not confirm it.

## 7. Limits

- C1 is not proved. Theorems 5, 6 and Lemma 7 remove the diagonal, the resonance and the
  bookkeeping, and Theorem 8 shows what C1 would buy; none of them bounds the off-diagonal pairing.
- Theorem 5 is proved only below `kappa`; the flat-kernel proposition is verified, not proved.
- Proposition 9 depends on El Jaouhari's Theorem B, which I have not verified.
- The predicted tail constant 1.36 is not confirmed by the data: at accessible heights the tail
  product is near 1.0 and still rising. The slow approach is consistent with the measured slow
  convergence of truncated correlations, but a smaller limit is not excluded by the numerics alone.
- The rate 0.88 to 0.91 is an observation. `sqrt(3/4) = 0.866` (the tower at `-1` against a bounded
  background) is a natural candidate and is not established.
