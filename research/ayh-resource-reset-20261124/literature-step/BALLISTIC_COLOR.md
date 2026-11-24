# Linear parity separation on color-discordant head edges

Let `T` be the ordinary positive shortcut and let `p_x(t)` count its odd inputs up to but excluding clock `t`. For the four-trit edge take `x=81m+r` with `0≤r<81`. Give an integer color one if its orbit reaches one, and zero otherwise. Suppose the colors differ, write `u` for the good arm, `n` for the bad arm and fix an actual clock `q` at which `T^q(u)=1`. The estimates below apply to every such pair of positive integers. They use no statistical hypothesis.

## Finite physical clocks

Every iterate of the bad arm is at least 600 by the checked finite table. For any real `B≥64` that bounds all its iterates below, the product formula gives

\[
 2^t T^t(n)\le n(3+1/B)^{p_n(t)}.
\]

The extra factor on an odd input `y` is exactly `1+1/(3y)`. The good arm alternates between one and two after clock `q`. Consequently `p_u(t)=t/2+O_u(1)` and

\[
 \liminf_{t\to\infty}\frac{p_n(t)-p_u(t)}{t}
 \ge \frac{\log2}{\log(3+1/B)}-\frac12 .
\]

At `B=600` this exceeds `0.1306`. If the bad orbit has no repeated vertex, it eventually lies above every fixed `B` and the lower limit is at least `log(2)/log(3)−1/2`. With `G=q−2p_u(q)` and `e=(t−q) mod 2`, one has exactly `2p_u(t)=t−G+e` for `t≥q`. Thus the finite lower bound can retain the signed terminal grade rather than paying for the entire hitting time.

The integer inequality `(3y+1)^5≤2^8y^5` for `y≥64` gives the following statements without logarithms. For `n≤2^L`, at every `t≥0`,

\[
 8(p_n(t)-p_u(t))\ge t-C,\qquad C=5L+4q+4. \tag{1}
\]

For `t≥q` the right side can be replaced by `t−5L+4G−4`. More precisely, over any window beginning on the bad arm at `y` and ending after `b` steps at `y'`, the hypothesis `y≤2^L y'` gives `5b≤8p_y(b)+5L`. This follows by cancelling `(y')^5` from the iterated one-step bound. If the good arm is already on its terminal cycle, its odd count in the same window is at most `(b+1)/2`.

For the original ray, the canonical slope-difference level at clock `t` is `|4+p_x(t)−p_m(t)|` by the two affine slope formulas. Its distance from `|p_n(t)−p_u(t)|` is at most four. In particular, any sublinear level subsequence rules out different basin-of-one colors. This implication does not require the two orbits to merge.

## Two families of uniform future windows

After any prescribed clock `a`, there is a clock `s≥max(a,q)` at which the bad trajectory takes its smallest value on that tail. For every `b≥0` this gives `T^s(n)≤T^{s+b}(n)`. The height-ratio bound with `L=0` implies

\[
 8\big(p_{T^s(n)}(b)-p_{T^s(u)}(b)\big)\ge b-4 \qquad(b\ge0). \tag{2}
\]

A second choice of clocks has a uniform lower time density. Put `d(t)=p_n(t)−p_u(t)`, `W(t)=16d(t)−t` and `M(s)=min_{t≥s}W(t)`. The minimum exists by (1), since `W(t)≥t−2C`. Moreover `W(t+1)−W(t)≤15` and `M(0)≤0`. An increase from `M(s)` to `M(s+1)` forces `M(s)=W(s)` and is at most `15`. Telescoping from `0` to `N` therefore gives at least `(N−2C)/15` such increases among `0≤s<N`. At each of them, `W(s+b)≥W(s)` for every `b`. Thus

\[
\#\{s<N:16(p_{T^s(n)}(b)-p_{T^s(u)}(b))\ge b\text{ for every }b\ge0\}
  \ge (N-2C)/15. \tag{3}
\]

The actual-height minima in (2) and excess minima in (3) are different clocks. Only the latter have the lower density `1/15` here. Both choices can depend on future digits. For a finite version through a specified horizon `N`, put `M_N(s)=min_{s≤t≤N}W(t)`. Its strict increases give at least `max(0,W(N))/15` indices `s<N` for which the same inequality holds for all `b≤N−s`. This count uses no information after clock `N`.

The finite counting argument is the forward-window form of the Pliss selection principle. Reversing a finite increment list converts its backward sums at selected endpoints into forward sums at selected starts. The coercive lower bound in (1) permits taking genuine minima on infinite tails here. [Pliss, 1972](https://www.mathnet.ru/eng/de1484) · [Alves, Bonatti and Viana, Lemma 3.1](https://cmup.fc.up.pt/cmup/jfalves/artigos/abv.pdf)

## The marks detectable before the critical descent time

Fix `0<ε<1`, put `d=log₂R`, `a=log₂(2/√3)` and `H=floor((1−ε/2)d/a)`. Except for `O_ε(R^{1−δ_ε})` actual head sources for some `δ_ε>0`, neither orientation of their odd-count difference has **any** mark satisfying the all-future slope `1/16` of (3) by clock `floor((1−ε)d/a)`. This assertion is about marked starts even if one has not yet classified either arm's basin.

Take the simultaneous single-arm envelope (4) in [the finite-stage transport theorem](POST_DESCENT_TRANSFER.md) with its altitude parameter `α=ε/2` and a sufficiently small fixed tolerance `η`. Its power-exception estimate applies to original head children. Uniformly through `H` each participating arm `v` has `T^i(v)` between constant multiples of `R·2^(−ai)·R^{±η}`. Every preceding input exceeds a constant multiple of `R^{ε/2−η}`. Its product correction between `T^i(v)` and `v·3^{p_v(i)}2^(−i)` consequently has logarithm `o(1)`. As `v` is comparable to `R`,

\[
 |p_v(i)-i/2|\le (\eta/\log_2 3)d+O_{\epsilon,\eta}(1)\quad(0\le i\le H).
\]

A mark at `s≤(1−ε)d/a` would require a signed difference of the two count increments from `s` to `H` of at least `(H−s)/16≥ε d/(32a)−1`. The four endpoint deviations bound its magnitude by `4ηd/log₂3+O(1)`. Taking `η<min(ε/8, ε log₂3/(256a))` rules this out for all sufficiently large `R`. No grid is selected at a random mark. This use of simultaneous single-arm counts is also available from [Inselmann, §3, Theorem 3.3](https://arxiv.org/pdf/2402.03276v3).

A precise diagonal consequence uses `ε=1/m` for `m≥2`. Choose increasing integers `J_m` with the sum of the exceptional fractions over `j≥J_m` for this fixed `m` at most `2^{−m}`. This is possible by its power bound and `R=81^j`. On `J_m≤j<J_{m+1}` use `ε_j=1/m`. Then `ε_j→0`, and all original heads exhibiting even one such mark before `(1−ε_j)log₂R/a` have a summable total of level fractions. This supplies no rate for `ε_j` and gives no upper bound on marks after that horizon.

## Consequence for the one-head counting argument

Let `E_j` count edges in `[7·81^j,8·81^j)` for which, in at least one fixed orientation, the excess-window property in (3) holds with lower time density at least `1/15`. Every color-discordant edge is counted by `E_j`. Since the actual color controls the digit-limit argument, `E_j` may replace the count of all nonmerging edges there. In particular `E_j=o(81^{.84j})` suffices using the published Krasikov–Lagarias exponent. Assuming the separately sourced positive lower natural density of each fixed target basin, `Σ_j E_j/81^j<∞` suffices. At a specified level, a criterion stated directly in terms of the smaller set of discordant edges is also valid.

For a finite test with horizon `N_j` and block length `b_j≤N_j`, every discordant source of height `L`, good hit time `q`, and `C≤N_j/4` has at least `N_j/30−b_j` candidate starts `s≤N_j−b_j` satisfying the signed block inequality in one fixed direction. Therefore bounds for the *sum over actual sources and clocks* of these tests, together with bounds for exceptions to `C≤N_j/4`, control the corresponding source count by division by `N_j/30−b_j` when this is positive. This is a deterministic double count; no law on the selected clocks is assumed. The finite-horizon version permits using `W(N_j)` instead of the coarser `C` threshold, and the grade bound above can be used after a known hit.

Neither a summable bound for these witness-rich edges nor control of the original-source mass at delayed onset is proved. A fair residue grid at a separately fixed early clock cannot be assigned to an anticipatively selected late mark. Forward control through the ordinary critical descent time does not by itself bound post-hit pairs over the needed blocks. Universal Collatz remains open.

The formal source uses the existing `CollatzShell` shortcut and `OffsetDescent.oddCount`. The sharp real-log expression, asymptotic-source counting combination, and cited distribution inputs are written arguments.
