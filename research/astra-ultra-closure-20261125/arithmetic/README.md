# Dyadic phase counts and the width of an ordinary cycle

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers. In a primitive cycle of $U$, write $p$ for the number of odd phases, $m$ for the smallest odd value, and $M$ for the largest odd value.

**Proposed written cycle theorem.** For each fixed $2<K<4$ and each $\epsilon>0$, every sufficiently large $m$ in a cycle with $M\le Km$ satisfies
$$
                         p\le m^{\log_3(K/2)+\epsilon}.
$$
Consequently, along any sequence of distinct positive cycles, Wu and Wang's published logarithmic-form estimate gives $\liminf M/m\ge 2\cdot3^{1/5.1163051}=2.47904859\ldots$. With the two-logarithm estimate reported in Chudnovsky's October and November 2026 preprints, the same argument gives $\liminf M/m\ge2\sqrt[3]{3}=2.88449914\ldots$. Equivalently, for any fixed number strictly below the applicable threshold, only finitely many cycles could have odd width ratio below that number. No numerical cutoff on $m$ is supplied. For a nontrivial cycle the maximum under the shortcut map is $(3M+1)/2$, since this is the largest image of any odd member and even steps only decrease. Thus the second bound corresponds to an asymptotic shortcut width of at least $3\sqrt[3]{3}$.

**Kernel-checked results.** *PolynomialStrips.lean* proves that one ordinary odd orbit, sampled at explicit shortcut clocks, either falls below a prescribed floor or visits a whole nearly uniform grid of dyadic logarithmic phases with different time indices. It also proves the ordinary terminal uniqueness used in the cycle count below. The entropy count, its asymptotic arithmetic consequences, and the externally supplied logarithmic-form estimates are written mathematics. The width bound permits arbitrarily wide positive cycles. Its argument for a full lap does not apply to escape.

## Counting clocks inside a fixed band

Set $\alpha=\log_2 3$, $\beta=\log_2 K$, and $k=\lceil\log_3(Km)\rceil$. From every phase take the next $k$ odd steps, wrapping around the cycle if needed. Write $x_i=U^i(x_0)$ and $S_i=\sum_{j<i}v_2(3x_j+1)$. Telescoping gives
$$
 \log_2(x_i/m)=\log_2(x_0/m)+i\alpha-S_i+e_i,\qquad
 0\le e_i\le k/m\quad(0\le i\le k).
$$
Indeed each summand of $e_i$ is $\log_2(1+1/(3x_j))\le1/m$. All endpoints lie in the same closed band $[m,Km]$.

Fix $\eta>0$ with $\beta+2\eta<2$. Partition $[0,\beta]$ into a fixed finite number of bins of width at most $\eta$, and let $b$ be the left endpoint of one bin. For large $m$, $k/m\le\eta$. Every starting value in this bin has
$$
               S_i\in[b+i\alpha-\beta,\ b+i\alpha+2\eta].
$$
The interval length $w=\beta+2\eta$ is strictly between one and two. For each $i$, the bin allows at most two integers. Two occur precisely when the fractional part of its left endpoint lies in the closed circular arc from $2-w$ to $1$, with residue $0$ included. This arc has length $w-1$.

For clarity, the required uniform estimate is elementary. Take a reduced rational $a/q$ approximating the irrational $\alpha$ with $|\alpha-a/q|<1/q^2$, with $q$ arbitrarily large. In every block of $q$ consecutive indices, the phases of $i\alpha$ are within $1/q$ on the circle of a translated complete rational grid. Each closed arc of length $L$ consequently receives at most $qL+4$ observations in that block, regardless of its starting phase. Divide $1,\ldots,k$ into complete blocks and a remainder, let $k\to\infty$ with $q$ fixed, then let $q\to\infty$. The upper frequency is at most $L$, uniformly in the translate. Irrationality here follows from the distinct prime powers $2^a,3^q$.

Thus the number of possible tuples $(S_1,\ldots,S_k)$ per initial bin is at most $2^{(w-1+o(1))k}$. The locations permitting two integers are common to the bin. Counting all these independent choices is an upper bound, even though some choices fail to produce a legal path.

Each tuple determines every gap by successive differences since $S_0=0$. Two paths with the same gaps have equal carry $C$ and satisfy
$$
                 2^{S_k}x_k=3^k x_0+C.
$$
Their terminal values agree modulo $3^k$ by coprimality. The band length $(K-1)m$ is smaller than $3^k$, giving at most one terminal per word. Lean proves this assertion in **band_terminal_unique**. Advancing $k$ steps permutes the $p$ phases of a primitive cycle, including when $k>p$. Its $p$ distinct ends are covered by all the initial bins. Therefore
$$
 \limsup\frac{\log p}{\log m}
 \le\frac{(\beta+2\eta-1)\log 2}{\log 3}.
$$
Letting $\eta$ decrease to zero proves the upper exponent. The same argument bounds the number of distinct endpoints of length-$k$ windows along any ordinary path in the band, even without a cycle assumption.

## Applying logarithmic-form estimates to the full lap

If $A$ is the sum of the gaps around one lap, its exact product gives
$$
       0<A\log 2-p\log3
       =\sum_{j<p}\log(1+1/(3x_j))\le p/(3m),\qquad A\le2p.
$$
For any $\kappa$ with a bound $|q\log3-a\log2|\gg q^{-\kappa}$ when $q\le a\le2q$, this implies $m\ll p^{\kappa+1}$. If $\log_3(K/2)<1/(\kappa+1)$, combining this lower exponent for $p$ with the upper exponent just proved bounds $m$. A given minimum specifies at most one cycle by determinism.

Wu and Wang, Theorem 1, give exponent $4.1163051+\varepsilon$ for a three-coefficient form, with an effectively computable onset depending on $\varepsilon>0$. Take their constant coefficient zero, the others $A,-p$, and use $A\le2p$. Taking $\varepsilon$ arbitrarily small gives the first width threshold. [Wu and Wang, Journal of Number Theory 142 (2014), 264–273](https://doi.org/10.1016/j.jnt.2014.03.007)

Chudnovsky reports exponent $2+\varepsilon$ for this homogeneous two-logarithm form, with an ineffective constant. The positive rationals 2 and 3 satisfy the multiplicative-independence hypothesis by unique factorization. The November preprint explicitly credits its earlier two-logarithm case to the October paper. The November appendix gives the Lean endpoint and the author's axiom audit. We checked the stated theorem in the primary paper and did not rebuild the external proof. [October preprint](https://arxiv.org/abs/2610.28079) · [November preprint, Corollary 1.2 and Appendix A](https://arxiv.org/html/2611.30820v1)

For comparison, PR 206 uses separated branch indices in a specific strip to obtain $M/m>2.08$ for every hypothetical nontrivial cycle, with published computational and period bounds. Our thresholds have an asymptotic quantifier and use uniform frequencies of branch indices. PR 205 restricts certain bounded cycles to a period $O(m^{0.49})$. The lower exponent $1/3-\varepsilon$ allowed by the newer logarithmic form is compatible with that bound. The remaining gap is to force a contradiction also for cycles outside every band excluded above. [PR 206 at b2b56b9, OrbitAttack](https://github.com/GettysburgResearch/collatz/blob/b2b56b94175174a680a296478f16c619a8828972/research/clock-itineraries/OrbitAttack.md) · [PR 205 at 32d722c, Height Strip](https://github.com/GettysburgResearch/collatz/blob/32d722c5d5597846da5dad842c8ea15742abc176/research/astra-fixed-target-closure-20261124/ordinary/HEIGHT_STRIP.md)

## A forward exit for every sufficiently large ordinary start

Fix $2<K$ strictly below either width threshold above, using the corresponding logarithmic-form input. For every $\epsilon>0$, every sufficiently large odd integer $n$ has an actual odd iterate below $n$ or above $Kn$ within $O_{K,\epsilon}(n^{\log_3(K/2)+\epsilon})$ odd steps. The same order bounds the elapsed shortcut clock.

To see this, start at $n$ and follow the odd trajectory while it stays in $[n,Kn]$. Any repeat among those states would supply a positive cycle with minimum at least $n$ and largest-to-smallest ratio at most $K$. Such a cycle is excluded once $n$ exceeds the threshold for this fixed $K$. Thus all the states observed before the first exit are distinct. Ignore the first $k=\lceil\log_3(Kn)\rceil$ of them. Every remaining state is a distinct endpoint of a preceding $k$-window contained in the band. The count above, including its fixed collection of starting bins, bounds the number of those endpoints by $O_{K,\epsilon}(n^{\log_3(K/2)+\epsilon})$. Since the exponent is positive, this bound also absorbs $k$ and the final exit step. At the first exit after $j$ odd steps, the product formula and positivity of the terminal give $2^{S_j}\le n(3+1/n)^j\le n4^j$. This bounds its shortcut clock by $2j+\log_2 n$, even if the last odd gap drops far below the band.

An upward exit is compatible with escape. The result forces the supplied trajectory to leave a fixed band but does not select the exit direction.

## A polynomial phase grid on one supplied orbit

For integers $N,m\ge1$, reduced Dirichlet approximation gives $0<q\le N$ and $a$ with $|q\alpha-a|\le1/(N+1)$. If the first $q$ odd states of a supplied positive odd start are at least $m$, every rotation of the grid $r/q$, $0\le r<q$, can be matched to distinct time indices $j<q$. After an integer phase shift the actual log-height is above the corresponding target by between zero and
$$
                             E=3/q+q/m .
$$
For each prescribed target, multiplication by $a$ permutes residues modulo $q$. Choose $j$ so the ideal grid phase is one to two grid spacings above that target. The Dirichlet error is at most $1/q$, and the accumulated positive physical error is at most $q/m$. This gives a common injection for all $r$. For example an arc of length $L\ge E$ contains at least $\lfloor q(L-E)\rfloor$ matched times, by selecting ideal targets in the arc after trimming $E$ at its upper end. If the block wraps around a cycle multiple times these are distinct observation times. The number of distinct physical values can be smaller.

The finite theorem **polynomial_grid_physical** takes integers $t\ge1,s,h,C$ with $t^{s+h}\le m$, uses $N=t^s$, and consumes the explicit condition that every eligible reduced approximant has $t^h\le Cq$. It proves a fall below $m$ or the grid match with $E\le(3C+1)/t^h$, on the given ordinary shortcut orbit. It computes physical observation clocks by adding the actual $2$-adic valuations. Its bound $q\le t^s$ is on odd steps.

To derive the stated rates in written mathematics, take a form bound with $\kappa=s/h>0$. For the Dirichlet witness, $q\le a\le2q$ (or handle bounded denominators directly), and the lower bound for the form gives $q\gg N^{1/\kappa}$. Here the exponent refers to $|q\alpha-a|$. The normalized quotient $|\alpha-a/q|$ has the extra denominator. Taking $t=\lfloor m^{1/(s+h)}\rfloor$ supplies $E\ll m^{-h/(s+h)}$ within $m^{s/(s+h)}$ odd steps. With $s=33,h=8$, Wu–Wang yields a radius $O(m^{-8/41})$ within $m^{33/41}$ odd steps. With the recent homogeneous preprint and a fixed rational $\kappa>2$ arbitrarily close to 2, the radius exponent approaches $1/3$ from below and the time exponent approaches $2/3$ from above.

If the observed values stay in $[m,Km]$, these widths are polynomial in the actual hit height as well. For an unrestricted escaping orbit a hit may be much larger than the originating floor. PR 173 already proves a shrinking section at a rate reciprocal in the logarithm of the actual hit height. The present theorem adds a full permutation of visits and a polynomial floor-sensitive radius. It does not certify downward movement at a hit. [PR 173 at fa0c9e2, ForwardSection](https://github.com/GettysburgResearch/collatz/blob/fa0c9e2a2851e6324391e39c17afcb5913185aec/research/lean-shell-cover/ForwardSection.lean)
