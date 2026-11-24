# Rational trials of the genuine dyadic scalar on one fixed escape

**PROPOSED written theorem.** Suppose that a fixed positive ordinary `n` has an injective shortcut orbit. For rational approximants `d_j=a_j/b_j` in reduced form, write the odd denominator as `b_j=3^(h_j)q_j`, `3∤q_j`, and put

\[
 N_j=\lfloor v_2(D(n)-d_j)/2\rfloor,\qquad J_j=\lfloor N_j/2\rfloor.
\]

Assume `N_j→∞`, `log(2+|a_j|+b_j)=o(N_j)` and `log q_j≤(K+o(1))log N_j` for some finite `K>0`. An even reduced denominator cannot have positive agreement. Let `μ` be **any** weak limit of the uniform shifts of the periodically repeated first `J_j` physical bits of this same source. For each `β<ρ<τ₀<α`, using the definitions in [the closed-word proof](README.md), `μ` dominates `cν` for some stationary probability `ν` satisfying

\[
 c=(\tau_0-\rho)/(1-\rho),\qquad \nu([1])\ge\rho,\qquad h(\nu)\ge (\log3)/K.
\]

In particular a zero-entropy limit at these clocks precludes this family of approximants. For an ergodic limit the lower entropy bound holds for `μ` itself. This conclusion uses the approximation of the actual `D(n)` and does not first replace `n` by a periodic rational source.

**Legality and signs.** Suppress `j`. Put `A_i=2^(i+p_i)/3^i`, `B_i=Σ_{t<i}e_tA_t`. The actual and trial companions at clock `i` are `−D(x_i)/3` and `w_i=(B_i−d)/(3A_i)`. They differ by dyadic valuation at least `2N−i−p_i`. Thus all trial phases through time `N` are dyadically integral, and before each of the `N` steps they agree with the actual companion modulo four. Physical bits are therefore uniquely determined by the trial states at those steps, via the two disjoint legal residues. The denominator of `w_0` divides `3^(h+1)q`, and a factor of 3 in its reduced denominator is consumed by each subsequent step where one remains. Thus `qw_i` is integral for `i≥h+1` up to `N`. This finite argument occurs already in the frozen PR193 rational-trial theorem. [PR193, arithmetic §§1–2](https://github.com/GettysburgResearch/collatz/blob/67f58e8eec87a4f1fb5f5e6da164ce0b9df44e1e/research/astra-global-resolution-20261124/arithmetic/README.md)

The fixed escaping orbit has `liminf p_i/i≥α>β`, as proved in the companion note. Hence `log A_i≥η i` eventually, for some `η>0` depending on a fixed slope between `β` and `α`. The exact telescoping identity `2B_i=3A_i−3+Σ_{t<i}A_t` shows that `w_i` is positive once `i≥I`, with `I=o(N)` chosen larger than `h+1` and a sufficiently large constant multiple of `1+log(2+|a|+b)`. We may also require `r^I|w_0|≤1`. Constants can depend on `n,ρ` and are independent of the approximant.

**Selection.** On the ordinary prefix of length `J`, record maxima of `Σ(e−ρ)` from time zero give at least `c'J` endpoints with every partial past down to time zero having odd count at least its length times `ρ`, for any fixed `c'` strictly between `c` and `(α−ρ)/(1−ρ)` once `J` is large. At each of these endpoints `i≥I` unrolling the real recurrence gives `0<w_i≤1+B`. Let `k` be the least nonnegative integer with `3^k>(1+B)q`. It is `O(log N)`. Discard the first `I+k=o(J)` indices and the last endpoint `J` if it occurs. At least `cJ` remain. Their `k`-pasts use physical steps of this same source, and the positive numerator at the start of each past is on the `1/q` grid.

The trial phases at the remaining endpoints are distinct. If `w_i=w_j` for `0≤i<j≤J`, the deterministic trial gives identical physical parities over the next `N−j` steps. Therefore `2^(N−j)` divides the nonzero integer `x_i−x_j`. The usual positive orbit bound gives `|x_i−x_j|≤(n+1)(3/2)^J`, whereas `N−j≥N−J≥J`. This is impossible for all sufficiently large `N` because `n` is fixed. At the marked positive phases the ternary congruence in (1) of the closed-word note now gives pairwise different `k`-pasts. In particular `k→∞`.

**Entropy transfer.** Periodizing the length-`J` prefix only defines the ambient empirical measure. The selected pasts lie entirely inside that actual prefix. Choose their starting phases uniformly, average their `k` forward shifts, and apply exactly the finite block proof of (2). The empirical measure dominates this averaged measure times `c`, and `log(cJ)/k` has liminf at least `log(3)/K`. All limiting statements concern this fixed `n` and the displayed clocks. No zero-entropy law or approximants with the required prime-to-six cost have been produced on every hypothetical escape. Ordinary dyadic truncation alone generally spends coefficient height of order `N` and does not meet the height assumption.
