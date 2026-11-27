# Analytic continuation forces exceptional ordinary clocks

**Proposed mathematical theorem.** Fix one hypothetical ordinary component `C` disjoint from 1. Retain its positive squared-slope weights from [the ordinary spectrum note](ORDINARY_SPECTRUM.md) and put zero everywhere else. Denote its generating function by `M₂`. If `M₂` continues holomorphically through any open arc of its unit circle, then both conclusions below hold.

1. There exist `c,δ>0` and arbitrarily large `N` for which at least `δN/log N` distinct positive starts `n≤N` in `C` have absolute signed relative clock at least `c n`.
2. For each fixed real `A>0` there are infinitely many distinct positive `u` in that component with absolute signed relative clock greater than `u^A`. In particular, a polynomial bound on the component clock at every ordinary vertex suffices for a full natural boundary at the physical exponent.

The signed clock is defined on the ordinary graph. In an acyclic component fix its calibration vertex `r`; if `T^i(n)=T^j(r)`, put `τ(n)=j-i`. All mergers give the same difference, since disagreement would give a repeated state on the forward spine. In a cyclic component use the negative of the time to first hit the chosen cut vertex `r`. Then `τ(Tn)=τ(n)+1` on every retained edge in either case. A large value is a large difference of clocks to an actual common ordinary state. It need not be the duration of a single forward segment from the small vertex.

[The actual ordinary block theorem](BASIN_BLOCK_BOUNDARY.md) independently rules out the antecedent. The denominator/clock argument below supplies an alternative obstruction that does not use ordinary interval routing and may be applied in settings in which that routing is unavailable. It does not assert extreme clocks exist in any ordinary component.

## Denominator density

Let `d(n)` denote the reduced positive denominator of `a(n)`, with denominator 1 for zero. Suppose, for a contradiction, that for every fixed `ε>0` the set `E_ε={n : log d(n)≥ε n}` has count `o(N/log N)`. Choose strictly increasing `N_k→∞` so its count for `ε=1/k` is at most `N/(k log N)` whenever `N≥N_k`. Use threshold `1/k` on `[N_k,N_{k+1})` and let `E` contain the inputs crossing their local threshold. For `N_k≤N<N_{k+1}`, elements of `E` up to `N` also cross threshold `1/k`, apart from finitely many initial values. Thus `|E∩[1,N]|=o(N/log N)`, and `log d(n)=o(n)` off `E`.

The denominators use only primes 2 and 3. Their least common multiple outside `E` through `N` has logarithm at most twice the maximum of those logarithmic denominators, hence `o(N)`. Bell, Gunn, Nguyen and Saunders, Theorem 1.2, now applies over the rational field; `M₂` converges throughout the unit disk. Under analytic continuation on an arc, it gives a rational series with poles at roots of unity whose coefficients agree exactly with the component weights off `E`. Its coefficients have a common denominator (also stated in Remark 1.3), while `a(n)=O(n^-2)`. Consequently all sufficiently late coefficients off `E` are zero. [Original theorem and remark](https://arxiv.org/pdf/2206.00862)

The component support is infinite by doubling, so a support contained in a zero-density set up to finitely many indices has arbitrarily long runs of zeros ending immediately before a nonzero coefficient. At the first positive index after such runs take a bounded two-sided right limit of `b(n)=n²a(n)`. Every negative entry is zero and its value at zero is positive by the uniform gap. Its Fourier distribution cannot vanish on any open arc, by the one-sided Cauchy-transform uniqueness argument in [the spectrum proof](ORDINARY_SPECTRUM.md). Continuation of `M₂` would instead force it to vanish there. This contradiction proves that for some `ε,δ>0`, at least `δN/log N` starts satisfy `log d(n)≥ε n` for arbitrarily large `N`.

## From rational height to an ordinary clock

Write `a(r)=4^-h`. In the acyclic case take the first common merger and use the counts of odd source sites, `s_n,s_r`, on the two directed paths of lengths `i,j`. In the cyclic case take the first visit to the cut root, with `j=s_r=0`. The exact weight formula reads

\[
 a(n)=4^{\tau(n)-h}9^{s_n-s_r}.
\]

Since `b(n)=n²a(n)` is bounded from above and away from zero throughout the component, uniformly in `n`,

\[
 (s_n-s_r)\log 9 = -2\log n- (\tau(n)-h)\log 4+O(1).
\]

It follows directly that `log d(n)≤2(log 4)|τ(n)|+2 log n+O_C(1)`. Removal of the fixed initial interval where the logarithmic term is large relative to `εn` proves conclusion 1, with a smaller positive density constant if needed.

## Moving to much smaller vertices

Inselmann's Corollary 3.2 and Definition 2.6 give, for every fixed `η>0`, a constant `D_η>0` such that all but `O_η(N^(1-D_η))` starts `n≤N` satisfy

\[
 T^{k(n)}n\le n^\eta,\qquad
 k(n)=\left\lfloor\frac{\log_2 n}{1-\log_2\sqrt3}\right\rfloor.
\]

This power-saving input is used before choosing a start. Its exceptional count is `o(N/log N)`, so infinitely many distinct sources in conclusion 1 satisfy the stated descent. Put `u=T^k(n)`. In the cyclic case the large negative clock means that first arrival at the cut vertex is at least `c n` steps away, longer than `k=O(log n)` for large inputs. Thus in both cases `u` is in the component and `|τ(u)|≥c n-O(log n)≥c n/2`. The values of `u` must be unbounded, since finitely many fixed vertices have bounded clocks. Choosing `η<1/A` now proves conclusion 2. [Inselmann, Corollary 3.2 and Definition 2.6](https://arxiv.org/html/2402.03276v3)

The proof supplies no common lower bound for the number of distinct endpoints reached *at the same clock date* from the many starts in conclusion 1. Many sources can merge immediately, and the descent dates vary. A bound counting different terminal states of parity-constrained starts needs an additional clock-dispersion statement. Neither the measured clocks nor the existence of a regular arc has been established on a bad ordinary component.
