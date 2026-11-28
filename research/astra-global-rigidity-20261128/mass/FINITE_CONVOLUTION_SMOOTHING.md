# Finite independent convolutions of full ordinary terminal laws have bounded densities

**Source-qualified written deduction.** The full moment bounds and the pinned concurrent native Rajchman theorem are explicit premises. The argument below proves their Fourier-analytic consequence; it is not a Lean formalization of those source theorems.

There is an absolute positive integer $k_0$ with the following property. For each $1\le j\le k_0$, choose independently a measure from the following list.

- the unnormalized ordinary first-hit log-correction law at any positive integer target.
- the sum of the full ordinary escaping-component log-correction laws after independent arbitrary translations of the components.
- the corresponding translated escaping flux, weighted before translation by $\kappa e^{-B}$.

Each component may receive an additional constant weight in $[0,1]$, and each entire chosen measure may be translated or reflected. The convolution of these $k_0$ measures has a continuous density vanishing at infinity, bounded above by an absolute constant. Equivalently, the product source measure of
\[
        \left|\sum_{j=1}^{k_0} \sigma_j B_j-t\right|\le r
\]
is at most $C r$, for arbitrary real $t$, positive $r$, and signs $\sigma_j\in\{-1,1\}$, with the same bounds on the unnormalized ordinary measures. Positive-mass laws may be normalized at the cost of the reciprocal product of their masses. Both the number of copies and the upper constant are independent of all the choices. The statement uses the actual full distributions, including all exceptional spikes allowed by existing single-copy estimates.

## The two inputs on the same physical measure

The uniform odd-unit bounds extend to every positive target without changing
the first-hit convention. Write the target as `y=2^v u`, with `u` odd.
If `3|u`, its basin is the single dyadic inverse chain and has natural mass
zero. Otherwise a visit to `y` followed by its `v` even halvings reaches
`u` with no added correction. On sources whose first `y` is no later than
their first `u`, the two first-hit marks agree. If `u` is visited first,
the route `u -> y -> u` makes `u` periodic, and the remaining mark from
that first `u` to the first `y` is one fixed cycle-arc constant. Thus the
law at `y` is dominated by the sum of the law at `u` and one translate of
that law. The arbitrary-grid bounds below and Minkowski's inequality give
the same uniform moment estimate up to an absolute factor. The one-defect
Fourier bound already holds at every positive target. Leading even
halvings add no correction, so the odd-relative and all-positive natural
source normalizations agree.

Fix once and for all $1<p<1/(1-g)$, where $g=1-H_2(\log_3 2)+1/351$. Our full small-order bin estimate gives constants $C,D<\infty$ such that each stated measure $\nu$ satisfies
\[
        T^{p-1}\sum_{I\in\mathcal G_{1/T}}\nu(I)^p
                \le C(1+\log T)^D,\qquad T\ge2.                    \tag{1}
\]
Here $\mathcal G_h$ is a regular grid of mesh $h$. The first-hit measure is in the log correction $B$, before any nonlinear change to a relative or physical offset. The component law and its weighted flux are the exact untrimmed laws in that same coordinate. A bounded nonnegative component or mark weight preserves (1) up to its bound. [Full ordinary logarithmic moment estimate](UNTRIMMED_LOG_MOMENTS_AND_CLOCKS.md) · [Normalization and existence, including arbitrary component translations](UNTRIMMED_FIRST_HIT_MARK.md)

The independent finite-source Rajchman theorem for the genuine native map gives, for example with $a=1/4$,
\[
            |\widehat\nu(\xi)|\le C_a(1+\log(2+|\xi|))^{-a}.       \tag{2}
\]
For first hit, the eigenfunction equation has just one defective edge at the chosen target, so the constant is uniform in its height. For complete escape its proof bounds the **sum of the absolute component amplitudes** by the same right hand side. Thus arbitrary translations or constant component weights of modulus at most one preserve the bound. For the weighted flux choose a smooth compactly supported real function $w$ agreeing with $\kappa e^{-B}$ on the fixed bounded possible range of complete log corrections. The weighted sum of absolute Fourier amplitudes at $\xi$ is at most $\int |\widehat w(s)|\sum_C|\widehat\Lambda_C(\xi-s)|\,ds$, up to the choice of Fourier normalization. On $|s|\le |\xi|/2$ apply the original uniform bound. On its complement rapid decay of $\widehat w$ and total component mass at most one suffice. Translate components only after weighting them. The signs in the theorem do not affect absolute Fourier values. [PR215 checkpoint 6, uniform one-defect and joint escaping amplitudes, commit 121054cf](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/escape/phase6/LOCAL_TRIT_AND_RAJCHMAN.md)

## Integrated Fourier decay

Use the standard Fourier transform with phase $e^{-2\pi i x\xi}$ and let $K_T$ be uniform probability density on $[-1/(10T),1/(10T)]$. Its Fourier transform is bounded below in absolute value by an absolute positive constant on $[-T,T]$. On each grid cell the convolution $K_T*\nu$ is bounded by $5T$ times the sum of the masses in that cell and its two neighbors. Integrating the $p$-th power and using (1) gives
\[
 \|K_T*\nu\|_p^p\ll(1+\log T)^D.
\]
Hausdorff–Young, with $p'=p/(p-1)$, yields
\[
       \int_{-T}^T |\widehat\nu(\xi)|^{p'}\,d\xi
               \ll(1+\log T)^{D/(p-1)}.                            \tag{3}
\]
For a fixed $q>p'+(D/(p-1)+2)/a$, split the remainder of the line into shells $e^j<|\xi|\le e^{j+1}$. Bound $p'$ factors by (3) on the whole ball and the extra $q-p'$ factors by (2) on the shell. The series $\sum_{j\ge1}(1+j)^{D/(p-1)-a(q-p')}$ converges. In particular
\[
                  \sup_\nu\int_{\mathbb R}|\widehat\nu(\xi)|^q\,d\xi<\infty.       \tag{4}
\]
The masses are bounded absolutely so (4) holds at every larger exponent as well. Choose $k_0=\lceil q\rceil$. For any $k_0$ independently chosen laws, Hölder with common exponent $k_0$ places the product of their Fourier transforms in $L^1(\mathbb R)$ with uniform norm. Fourier inversion for finite measures gives the asserted $C_0$ density and its uniform bound. The same proof with $2k\ge q$ gives an $L^2$ density already after $k$ copies. All constants are absolute once $p$ is fixed. Explicit numerical optimization of $k_0$ would require constants in the source moment estimates.

When all chosen laws have positive masses, their continuous nonnegative convolution density is strictly positive somewhere. Thus the closure of the corresponding signed sum of their supports contains a nondegenerate interval. For compactly supported fixed first-hit laws the support sum itself is compact and contains this interval. This conclusion can hold even when each individual correction law is singular continuous. The $k_0$ samples are independent original natural sources. A collection of consecutive observations of a single forward orbit has a different joint law.
