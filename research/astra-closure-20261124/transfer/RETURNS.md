# A uniform actual-orbit bound for returns after descent

**Status.** Written theorem conditional on the relative first-passage estimate (15) of [*First-landing bounds and canonical inverse laws*, §6](https://rstation.ai/problems/collatz/papers/12) and the uniform fixed-barrier estimate N in [PR199, frozen head](https://github.com/GettysburgResearch/collatz/blob/d868f8e8405c08b8c501236853bea495ca593824/research/optimal-critical-ancestors-20261124/README.md). The former is credited there to David Leen's zero-frequency relative passage theorem and its telescoped corollary. Those external proofs were not compiled here. Our local Lean file checks five deterministic arithmetic, counting and orbit lemmas. The return probability estimates are written mathematics.

Use the positive shortcut map $T(n)=n/2$ on even $n$ and $(3n+1)/2$ otherwise. Write $h_L(n)$ for its first **clock** at a value at most $L$, with value infinity on failure. The maximum below includes every shortcut state, including even states between successive odd values. All counts concern original ordinary integers.

**Uniform return theorem.** Fix $0<c<C$ and $A>0$. Let $R$ be a source scale, $K_0(A)\le K\le Y\le R^{.98}$. Except for at most
$$
 O_{A,c,C}\left(R\left[(\log K)^{-A}+Y^{1.001}/R+Y^{-\gamma}\right]\right)                 \tag{1}
$$
original $n\in[cR,CR]$, the two first clocks $h_Y,h_K$ are finite and
$$
 \max_{h_Y(n)\le t\le h_K(n)}T^t(n)\le Y^{1.004}.                       \tag{2}
$$
Here $\gamma>0$ is the exponent in N. For $R=81^j$ this holds on **both actual arms** $x$ and $\lfloor x/81\rfloor$ of the head $7R\le x<8R$, outside a set of the order in (1). Each offending parent accounts for at most 81 original children. The conclusion remains valid as an absolute error after arbitrary source selection.

In particular, if $Y=R^\theta$ with $0<\theta\le.98$ and $K=\exp((\log R)^\delta)$ with $0<\delta<1$, the two-arm exceptional level fractions are summable. Any fixed power of $\log R$ may multiply these fractions and leave them summable, by choosing $A$ large enough. The starts and their returned distributions can remain dependent at every threshold.

## The post-landing test, including failure on its next segment

Let $y$ be large, $m=y^{.99}$, $H=y^{1.004}$, and $Q=y^{1.001}$. For an odd landing $v\le y$, put $g_y(v)=1$ if its shortcut future either fails to hit $[1,m]$, or exceeds $H$ by that first clock. Include its starting point and endpoint. Define the test to be zero on failure to land at $y$ in the first place. If the first shortcut landing at $y$ is even, the subsequent steps through its odd part only decrease. That odd part is exactly the first odd landing at $y$. Any intermediate earlier shortcut hit of $m$ also precedes a decreasing segment. Thus, **conditional on passage to $y$**, failure of the claimed $y$-to-$m$ segment is detected by this function of the actual first odd landing. This applies as well if a single run of halvings crosses both thresholds.

Sample an odd integer $n$ uniformly in $[Q,2Q)$. Set $J=\lfloor(\log_2 y)/2\rfloor$. The first $J$ shortcut parities are within $O(2^J/Q)$ in total variation of a forced first one followed by independent fair bits. Indeed each full period modulo $2^J$ contains each parity word exactly once. This follows inductively since increasing the start by $2^i$ preserves its first $i$ parities and flips the next one. Incomplete periods give the stated error after restriction to odd inputs.

Write $p_i$ for the first $i$ odd-count and $Z_i=3^{p_i}2^{-i}$. Before the first hit on $m$, and also at its arrival, the exact affine update gives
$$
 T^in=n Z_i\prod_{0\le l<i,\, T^ln\ {\rm odd}}(1+1/(3T^ln))
     \le 2Q Z_i\exp(J/(3m)),\qquad i\le J.
$$
Under the fair law, $(Z_i)_{1\le i\le J}$ is a nonnegative martingale with $Z_1=3/2$, since the two possible next factors are $1/2,3/2$. Stopping at a first exceedance gives $\Pr(\max_{i\le J}Z_i>H/(3Q))\le 9Q/(2H)$. Once $y$ is large enough that $2\exp(J/(3m))<3$, this bounds the probability of any pre-$m$ exceedance up to clock $J$, with the grid error above.

If the orbit has still not hit $m$ at clock $J$ and $p_J\le.6J$, the same inequality gives
$$
 T^Jn\ll y^{1.001+(0.6\log_2 3-1)/2}<y^{.99}.
$$
This contradicts that failure. The binomial upper tail for $p_J>.6J$ under the forced-first-bit law is $O(y^{-c_0})$ for some absolute $c_0>0$. Together these estimates give a power-small local probability, including the possibility that the $m$ passage never occurs. In particular
$$
 \Lambda_{Q,y}(g_y)\ll y^{-c_2}                                      \tag{3}
$$
for an absolute $c_2>0$. Here $\Lambda$ is the probability of the marked successful first odd landing at $y$. Both stops and every tested state refer to one physical source. None of the arguments requires the distribution of its landing to be flat.

The external relative landing input, in its specified odd-octave normalization, gives simultaneously for $L\ge y^{1.001}$ and every $0\le g\le1$, zero on failure,
$$
 \Lambda_{L,y}(g)=\mathcal H_y(g)\,[1+O((\log y)^{-c_1})]+O_A((\log y)^{-A}),
 \qquad 0<c_1<5/143.                                                   \tag{4}
$$
Use (4) first at $Q$, absorb the relative coefficient once its absolute error is below $1/2$, and then apply it at $L$. Nonnegativity and (3) give $\Lambda_{L,y}(g_y)\ll_A(\log y)^{-A}$. An absolute total-variation comparison with error $O((\log y)^{-c_1})$ alone would not give this conclusion for arbitrary $A$.

For ordinary $n\in[cR,CR]$, split $n=2^d u$ with $u$ odd. When $cR/2^d\ge y^{1.001}$, cover its $u$-interval by a bounded number of full octaves of comparable size. The costs sum to $O_{A,c,C}(R(\log y)^{-A})$. All remaining $n$ are divisible by one power of two of size $\gg_c R/y^{1.001}$, so they cost $O_{c,C}(y^{1.001}+1)$. Initial halvings cannot cause an upward return after their first $y$ passage.

Now put $y_0=Y$ and $y_{i+1}=y_i^{.99}$. Use the displayed original-source estimate at each $y_i>K$, down to the first $y_{i+1}\le K$. The logarithms form a geometric progression, so the sum of $(\log y_i)^{-A}$ is $O_A((\log K)^{-A})$. Also $\sum_i(y_i^{1.001}+1)\ll Y^{1.001}$ for large $K$, since $y_{i+1}^{1.001}/y_i^{1.001}\le K^{-.01001}$ at every used step. N bounds the number failing ever to pass $Y$ by $O_{c,C}(RY^{-\gamma})$. Outside this union of original-source events, each successive actual passage is finite and all intervening states stay below $y_i^{1.004}\le Y^{1.004}$. The final segment already includes the first hit of $K$. For $K=Y$ only the initial non-passage term is needed. This proves (1) and (2).

## Which all-time returns survive

Let $e(n)=1$ for an unbounded shortcut orbit and zero otherwise. A bounded deterministic positive orbit is eventually periodic. Define $b_Y(n)=1$ if it first reaches $[1,Y]$ and **later** exceeds $Y^{1.004}$ (zero on failure). For each fixed $K$, let $B(K)$ be the largest future value of any bounded orbit started at an integer at most $K$, or zero for an empty family. This finite cap has no supplied numerical growth bound. For $Y^{1.004}>B(K)$ the discrepancy between $b_Y$ and $e$ is confined to (1). Indeed every unbounded orbit that passes $Y$ later crosses the high threshold. A bounded orbit obeying (2) cannot return before the $K$ passage, and its $K$ landing rules out any later return by the definition of $B(K)$.

Consequently, as $R,Y\to\infty$ with $Y\le R^{.98}$, the empirical mass of bounded original starts with such a late rebound is $o(1)$, uniformly over these source scales. First bound the limsup by $O_A((\log K)^{-A})$ at fixed $K$, then send $K$ to infinity. The same holds for the probability that the **ordered two-arm rebound indicators** differ from their actual ordered escape indicators in either coordinate. No assertion about a rate in this last limit, or independence of the indicators, is needed. This discards the entire bounded-orbit contribution to any fixed-height clipping of normalized late-return weight supported on these events.

In Sultanow's [Appendix D, Corollary A1](https://www.preprints.org/manuscript/202610.2552/v3), take the first lower floor $Y=X^{.99}$. Then $Y^{1.004}=X^{.99396}<X^{.995}$, the bottom of the upper target band. Up to first passage of $K=\exp((\log X)^\delta)$, $0<\delta<1$, the contribution of any such return weight clipped at $X(\log X)^B$ is $o(X)$ in the remote-source logarithmic mean for every fixed $B$. To see this, apply (1) on all original octaves $[R,2R)$ sufficiently far out at fixed $X$ and take the logarithmic mean (harmonic weights vary by at most two on each octave). Then let $X$ grow, choosing $A\delta>B$. This calculation bounds weights carried by visits into $(X^{.995},X]$ after the $Y$ passage and before the $K$ passage. It does not estimate the untruncated return weight, contributions from lower target bands, or an unbounded trajectory's excursions after $K$. For those source and target regimes the full potential remains open.

## Why the last barrier still matters

For a fixed escaping unit $v$ and every $K\ge v$, **every** actual ancestor of $v$ passes $K$ and subsequently makes arbitrarily high excursions. Fixed-target positivity would give this set positive lower density. The correct use of (4) charges the post-landing test according to its actual probability at $y^{1.001}$. In particular, if a test includes the later unbounded trajectories from small roots, its near-scale probability need not be small. The barrier union stops at first passage to $K$, not at last exit from $K$. Inserting the same positive minorization at every successive floor conditioned on earlier failures would disregard this point. Nontrivial bounded cycles also require a separate exclusion.
