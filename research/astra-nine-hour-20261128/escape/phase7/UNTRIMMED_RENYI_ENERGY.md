# Untrimmed Rényi energy of the ordinary real correction

Let \(\lambda_y\) be the unnormalized ordinary limiting measure of the positive log correction \(B_y\) before the first visit to an odd target \(y\), with total mass its true predecessor density. Put \(g=1-H_2(\log_3 2)+1/351\), as in the [timed floor theorem](TIMED_FLOOR_AND_CLOCK_CENTRES.md), and \(a_T=\sqrt{\log T}/T\) for \(T\ge3\). Use any translate of the half-open real grid of mesh \(1/T\). Uniformly in every odd \(y\), grid translation, and \(T\ge3\), for each \(0<c<g\) and \(K\ge1\),
\[
       \sum_{J:\lambda_y(J)>K a_T}\lambda_y(J)\ \ll_c K^{-c},
       \qquad
       \sum_J\lambda_y(J)^q\ \ll_q a_T^{q-1}\quad(1<q<1+g).            \tag{1}
\]
The same upper estimates hold on any restriction of \(\lambda_y\). Constants do not depend on a predecessor-density floor. The positive-mass first-minimum cell at \(y=1\) gives a genuine instance. On each fixed positive-mass first-minimum cell the corresponding **untrimmed** \(q\)-sum has order \(a_T^{q-1}\), with component-dependent lower constants.

On a hypothetical escaping odd ray with canonical inverse probabilities \(\mu_y\) in the true physical offset, the resulting unit-grid theorem is
\[
      y^{q-1}\sum_{k\ge0}\mu_y([k,k+1))^q\asymp_{C,q}
                   (\log y)^{(q-1)/2}\qquad(1<q<1+g).                 \tag{2}
\]
This bound includes every physical bin and every source. The critical logarithmic growth agrees with the earlier lower bound and comes with an upper bound near order one. At \(q=2\) only the fixed-discard upper estimate has been established here. [Previous critical mass covers, information tightness, and trimmed quadratic energy](../phase6/CRITICAL_QUANTILE_COVER.md)

Concurrent PR212 checkpoint six proves the same untrimmed range \(1<q<1+g\) and critical logarithmic order by counting the labels of a limiting joint landing history. Its theorem also covers the full minimum law under arbitrary translations depending on the minimum, every lap-normalized periodic row, and almost-everywhere local-density exponents. The argument below gives an independent finite smooth ordinary-source proof using the quantitative native floor clock and the two orders of the actual target and first-floor visits. [PR212, all-scale fibre density, equations (1)–(2)](https://github.com/GettysburgResearch/collatz/blob/e55fb7cac646013f143b563014ae97b105bc7547/research/astra-global-20261128/escape/ALL_SCALE_FIBRE_DENSITY.md)

## Rapid smooth sampling at varying resolution

Fix a nonnegative \(\Phi\in C_c^\infty((1,2))\) of integral one. For every \(|f|\le1\) of Lipschitz constant at most \(T\), \(X\ge2T\), uniformly in \(y,T,X,f\),
\[
  \left|\frac1X\sum_{n\to y}\Phi(n/X)f(B_y(n))-\int f\,d\lambda_y\right|
        \ll_{A,\Phi}(1+\log(X/T))^{-A}.                               \tag{3}
\]
Here \(n\to y\) means a first visit exists. For fixed \(T\) the limiting ordinary sharp-prefix measure exists. The residual \(r=(I-P)U\) of its actual sharp prefix \(U(x)=e^{-x}\sum_{n\le e^x,\ n\to y}f(B_y(n))\) obeys (5) of the preceding critical-cover note. For the rate, truncate and recenter to \(\widetilde U(v)=\mathbf1_{v\ge0}U(\log T+v)\). The real size operator \(P\) has bounded shifts. The new residual vanishes below a fixed negative constant, is bounded on a fixed finite slab, and decays to every power in \(v\ge2\) with constants independent of \(y,T,f\). Convolve with \(h(s)=-e^{-2s}\Phi'(e^{-s})\). For large \(v=\log(X/T)\) this gives exactly the smooth source average; bounded \(v\) costs only a fixed constant. The smoothed residual is uniformly Schwartz, with derivatives falling on \(h\). The [trivial-phase Fourier estimate](../phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md) subtracts a smooth step times the limiting mean. Its residual has integral \(\kappa\) times the mean by integration of the two bounded shifts or the earlier renewal formula. Division of the remaining zero-integral Schwartz transform by the size symbol is uniformly Schwartz, using the fixed two-logarithm lower bound and the simple zero at the origin. Bounded homogeneous solutions vanishing at minus infinity vanish by iteration of the negative-drift walk. This gives (3) for the recentered profile; its mean is still the original one. This argument uses only a fixed smooth source weight even as \(K\) and \(T\) increase.

## Counting heavy cells with the actual late-arrival times

For fixed \(c<g\) choose \(c<b<g\) and \(c/b<\eta<1\). Fix sufficiently small \(\gamma,\zeta>0\) so
\[
          \eta+\zeta+\gamma/2<1,\qquad \zeta<\gamma/2 .
\]
Let \(R=2^{\lfloor\eta\log_2 K\rfloor}\asymp K^\eta,\ B=K^\zeta,\ X=T^{\,2+K^\gamma}\). Increase the \(K\)-onset by an absolute constant depending on these parameters. For the source prefix through \(2X\) one has \(L=\log(2X)\asymp K^\gamma\log T,\ \log(2R)\le L^{1/3}/2\) and \(1\le B\le\sqrt L\). These conditions hold uniformly for \(T\ge3\). The smooth source in (3) is bounded termwise by a constant multiple of this prefix law.

Let \(m\) be the left hand heavy-cell mass in (1). The number of its cells is at most \(m/(K a_T)\). Majorize their union by a function \(0\le f\le1\) equal to one in the union and vanishing outside its \(1/T\)-neighborhood, with Lipschitz constant at most \(T\). Its support is covered by at most three intervals of length \(1/T\) per selected cell, allowing closed endpoints. The cells lie on a bounded mark support by simple first-path packing. Use this single test in (3).

By (3)–(4) of the timed floor theorem, outside prefix mass \(O_{b,A}(R^{-b}+L^{-A/3}+e^{-c_2 B^2})\), every finite first time \(s=\tau_y(n)\) lies in one of at most \(R+1\) integer windows of width \(O(B\sqrt L)\). This includes sources hitting \(y\) before their first odd landing under \(R\). For \(X<n<2X\) and \(p\) actual odd departures before \(y\),
\[
       B_y(n)=\log y+s\log2-p\log3-\log n,\qquad 0\le B_y(n)\le C_0 .
\]
The uniform upper bound is the [simple-path correction bound](../phase4/HARMONIC_SOURCE_PHASE.md). Thus each \(s\), even when its center is arbitrarily large, permits only \(O(1)\) integers \(p\) on this source octave. For a specified pair \((s,p)\) and mark interval of length \(1/T\), the possible \(n\) occupy an interval with \(O(X/T+1)\) integers. Counting every physical integer meeting these necessary conditions bounds the smooth mass from the permitted windows by
\[
     C\,\frac{m}{K a_T}\,(R+1)B\sqrt L\,(1/T+1/X)
                    \ll m K^{\eta+\zeta+\gamma/2-1}.                  \tag{4}
\]
The bad probability is counted once for the whole union. Combining (3) and (4),
\[
 m\le C mK^{\eta+\zeta+\gamma/2-1}
    +O_{b,A}\!\left(R^{-b}+L^{-A/3}
        +e^{-c_2K^{2\zeta}}+(1+\log(X/T))^{-A}\right).
\]
Absorb the first term when \(K\) is sufficiently large and take \(A\) so large that \(\gamma A/3>c\). Since \(\eta b>c\), this proves the first half of (1) for every \(K,T\). Bounded \(K\) uses the total mass at most one. Sampling with the subprobability \(\lambda_y\), the variable \(W=\lambda_y(J)/a_T\) now has an integrable \(q-1\) power for \(q-1<c<g\), uniformly in \(T,y\). Its integral is \(a_T^{1-q}\sum_J\lambda_y(J)^q\), proving the second half of (1). The fixed-minimum upper follows by domination. For the matching lower retain any fixed positive mass quantile from the preceding critical cover and apply Hölder to its \(O(T/\sqrt{\log T})\) cells.

## Physical rays and ordinary entropy

At a late nonperiodic root \(y\) on an escaping odd-unit ray, the exact canonical-to-ordinary identity maps \(B\) to \(y(1-e^{-B})\), and weights \(d\lambda_y(B)\) by \((\kappa y/h(y))e^{-B}\). On this ray \(h(y)/y\) tends to a positive constant, and \(0\le B\le C_0\). Every physical unit bin pulls back into at most a bounded number of \(1/y\)-intervals on the natural grid; each natural interval intersects at most a bounded number of these preimages. The elementary inequality \((x_1+\cdots+x_d)^q\le d^{q-1}\sum x_i^q\), positivity and (1) thus give the upper in (2). The positive quantile physical upper-cover theorem and Hölder give its lower. [PR213, exact marked ordinary trace (4)](https://github.com/GettysburgResearch/collatz/blob/ca48af42546268771e34297872783631f61e8f02/research/astra-global-rigidity-20261128/mass/REAL_OFFSET_ORDINARY_TRACE.md)

For a normalized fixed minimum cell, or for the physical unit grid along an actual escaping ray with \(T=y\), let \(p_J\) be the cell probabilities. Their Shannon entropy satisfies
\[
     \mathsf H_T=\log T-\tfrac12\log\log T+o(\log\log T).             \tag{5}
\]
Indeed (1)–(2) and Jensen give the lower \(-\sum p_J\log p_J\ge-\log a_T-O(1)\). For the upper, fix \(\delta>0\) and cover mass at least \(1-\delta\) using \(O_\delta(1/a_T)\) cells. The whole measure has \(O(T)\) possible cells. Conditioning the entropy on cover membership thus gives \(\mathsf H_T\le-\log a_T+(\delta/2)\log\log T+O_\delta(1)\). Send \(\delta\) to zero after the fine-scale limit. The \(O_{\Pr}(1)\) information centering proved previously used fixed quantiles alone. Formula (5) also controls Shannon expectation through the logarithmic correction. Neither conclusion asserts convergence of the centered expectation to a constant.
