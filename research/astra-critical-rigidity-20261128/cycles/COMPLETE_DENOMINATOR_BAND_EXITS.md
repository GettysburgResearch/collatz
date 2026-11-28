# The complete denominator pays for missing outliers in an actual rational orbit

**Proposed written theorem.** Let a positive rational Syracuse cycle have primitive odd period \(p\), complete reduced denominator \(q\), odd minimum \(m\), and maximum \(X\). Reduced numerators on its odd phases are odd integers and \(q\) is prime to six. Count the actual phases \(k\) outside a band \([M,RM]\). In the unrestricted-width case use \(M=m\). In the bounded-width cases assume \(X/m\le R_1<\infty\) and allow any band meeting the cycle. We use \(c=2\) for unrestricted width, \(c=1\) for bounded width, and \(c=0\) if \(R_1<9\).

Put \(v=0.4333973955184\ldots,\ \theta=0.3197044778974\ldots,\ a=1-3\theta\), with exact values in the [ordinary band-exit theorem](FROBENIUS_BAND_EXITS.md). Choose either fixed \(2<R<4\), setting \(\kappa=0\), or \(R=4-p^{-\kappa}\) with \(0<\kappa<a/(3v)\). Assume the [irrationality-exponent input](../literature/CHUDNOVSKY_LOGARITHM_IMPORT.md) \(\mu(\log_2 3)\le3\). Then along every growing-period sequence,
\[
 \liminf\frac{\log(q(1+k))}{\log p}\ge
 \min\left\{\frac{a/v-3\kappa}{\max(c+2,\,1+3\theta+a/v)},\
                 \frac{a-\kappa}{1+ca}\right\}.                         \tag{1}
\]
At any fixed sub-four cutoff the three bounds are respectively \(0.02358491\ldots,\ 0.03144655\ldots,\ 0.04088656\ldots\). In particular, for \(q=p^{o(1)}\) polynomially many **distinct actual phases** must leave the band. This allows unbounded rational denominators and, for the first bound, unbounded physical excursions. For widths \(X/m=4+O(p^{-\kappa})\), the two actual endpoint layers again give a complete bipartite family of near-four pairs at polynomial precision whenever \(\log q/\log p\) is small enough. For \(k=0\) the [whole-cycle matched rational theorem](MATCHED_RATIONAL_DENOMINATORS.md) supplies a stronger denominator exponent. Here the interval can lose any number of phases, including one long excursion.

## A local source bound with the original complete denominator

Write \(T(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd rationals of fixed denominator \(q\) prime to six. The valuation applies to the rational \(3x+1\); its denominator is odd. Fix \(Y\ge2\). The proof of the [four-copy source bound, commit 5136b7f, four actual source segments and their common clock](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md) gives the following local statement. Fix \(v'>v\). For some \(b=O_{v'}(\log Y)\), the number of distinct odd rationals of reduced denominator \(q\) in \([Y,2Y]\) whose first \(b\) odd edges all stay in **one prescribed physical band of width ratio at most four** is \(O_{v'}(q Y^{v'})\). The estimate is uniform in \(q\) and the placement of that band.

Here are the hypotheses needed from the pinned proof. Since the starting point lies in the band and in \([Y,2Y]\), all states on the observed prefix are at least \(Y/4\). Its corrected cumulative clock differs from the homogeneous clock by the log of a ratio of two in-band states plus a positive drift \(O(b/Y)\). The range used for the translated defect chart is therefore at most \(2+O(b/Y)\), uniformly at the factor-four endpoint. The finitely many phase cells and the \(o(b)\) enlargement sites are exactly the ones used there at \(R=4\). The four consecutive native windows, guard grades, local energy, dyadic quantization and Subspace-Theorem separation all use this one finite word. The physical numerator relation is \(N\equiv q2^K S\bmod 2^K\), which leaves \(O(q)\) outer source arcs and at most one numerator per fixed word and arc. No stage uses a return, an unseen state beyond the word, or a width hypothesis outside this actual prefix. At \(R=4\) the overlap exponent \(\chi(4)\) in that source equals \(v\). Taking a fixed small guard loss proves the stated local bound.

Let \(\beta,\delta,\pi,\sigma\) be the subsequential limits of \(\log q,\log(1+k),\log P,\log m\) divided by \(\log p\), respectively, where \(P\) is the reduced slope denominator. It suffices to consider \(\beta+\delta<0.1\); larger limits already imply (1). At least \(p-k\) distinct rational phases lie in the band, so \(qRM\ge p-k\), and \(M\asymp m\) in both cases under consideration. In particular \(m\) grows polynomially. The positive log clock and any classical finite irrationality bound give \(m\le p^{O(1)}\). Since \(R\le4\), at most three dyadic shells \([Y,2Y]\) cover the band with \(Y\asymp M\). Apply the local count to each shell and remove starting dates whose following required word leaves the band. Each of the at most \(k\) outgoing edges from the band charges at most \(O(\log M)\) preceding starts. This gives
\[
               p-k\ll_{v'} q M^{v'}+k\log(2M),\qquad
               \sigma\ge(1-\beta)/v>2.07 .                             \tag{2}
\]
All constants in the four-copy estimate may be ineffective.

## The finite native tube at full rational denominator

The [residue-fiber inversion bound](RESIDUE_FIBER_INVERSIONS.md) is \(g/h-1\le I_q\), where \(g=p/P\) and \(h=\operatorname{ord}_q(3^P2^{-A/g})\le q\). Its inversions use actual rational states \(y=2^d x+u\) with integral odd \(0<3u<2^d-1\). In the unrestricted case their larger endpoint is exceptional. For each fixed \(y,d\), any two candidate lower endpoints lie less than \(1/3\) apart, and their difference is an integer: it belongs to both \(q^{-1}\mathbb Z\) and \(2^{-d}\mathbb Z\), with \(\gcd(q,2^d)=1\). Hence there is at most one candidate. Since \(m\ge1\) at large periods here, the last in-band state before the maximum gives \(X/m\le4\cdot2^k\) by the actual native rise bound. For bounded total width, an exceptional endpoint allows \(O_{R_1}(1)\) choices for its partner by the inversion formula, including when the lower endpoint is fixed. For \(R_1<9\) the inversion count is zero. Thus
\[
                            1-\pi\le\beta+c\delta .                     \tag{3}
\]

Use the actual reduced grid, the longest in-band run, the true-time sampling scale \(T=\lfloor p/(10(k+1))\rfloor\), and the simultaneous rank/time cell from the [ordinary tube proof](FROBENIUS_BAND_EXITS.md). The real error remains \(O(T/m)\), since the source correction on each native log edge is still \(\log_2(1+1/(3x))\). The sharp half-open chart inequalities use only the true physical band and (2). The normalized single tags on the tube are exactly one or two. The real interaction heights now lie in \(q^{-1}\mathbb Z\).

If a pair comparison \(H_{t+1}=0\), then \(3H_t=-d_t\) for the true signed forcing \(d_t\in[-2,2]\cap\mathbb Z\). As \(H_t\in q^{-1}\mathbb Z\) and \(q\) is prime to three, this equality forces \(d_t=0\) and \(H_t=0\). Thus the entire preceding tube of zeros, and the exact prime-11 dilation on the bounded integer tags, survive unchanged. When the dilated forcing vanishes for \(l\) consecutive dates, multiply the homogeneous comparison by the **whole** \(q\). Its initial integer is divisible by \(2^{F_{t+l}-F_t}\ge3^l/2\) and has magnitude \(O(qM)\). A sufficiently large multiple of \(\log(2qM)\) dates fits inside the available polynomial length. This gives the same two physical label equalities and the same integer rank rectangles of area \(O(P^2T/m)\). They are counted and thinned just as in the ordinary proof.

Finally, an equality of coordinatewise binary tag sums over \(n=\lceil\log_3(32qM)\rceil+3\) dates forces the initial difference times \(q\) to be zero by its full dyadic divisor. The source separation of the retained unordered pairs then gives the native binary Sidon code. Its size is at most \((qM)^{\theta+o(1)}\). Consequently the log-exponent inequality before the final irrationality input is
\[
 \pi-\kappa-\delta-\tfrac13(2\pi+1-\delta-\sigma)_+
                                      \le \theta(\sigma+\beta).         \tag{4}
\]
Every denominator factor is retained in both integer divisibility steps.

If the positive part in (4) has nonnegative argument, (2)–(4) imply
\[
     (1+3\theta+a/v)\beta+(c+2)\delta\ge a/v-3\kappa .
\]
In the other case use the stated logarithm input \(\sigma\le3\pi\) to obtain
\[
                    (a+\theta)\beta+(1+ca)\delta\ge a-\kappa .
\]
Since \(1+ca\ge a+\theta\), these are precisely the two lower bounds giving (1).
