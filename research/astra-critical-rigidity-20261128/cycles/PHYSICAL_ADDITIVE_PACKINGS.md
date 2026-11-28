# Almost every physical phase belongs to a disjoint, locally transported additive quadruple

**Proposed written theorem.** Let a sequence of primitive positive rational odd cycles have odd period \(p\to\infty\), complete reduced denominator \(q\) prime to six, minimum \(m\), and maximum \(X\le Rm\). Ordinary cycles have \(q=1\). Write \(\gamma=\log_2 3,\ e=2-\gamma,\ s=1-2e,\ \omega=\log_2(R/4)\). Work with fixed \(4\le R<4\cdot2^e\), and define
\[
 D_R=\max\left\{\omega\log_25,\
 \tfrac35\big(s+(e-\omega)\gamma+\omega\log_25\big),\
 \tfrac9{16}s+\tfrac58\big((e-\omega)\gamma+\omega\log_25\big)\right\},
 \qquad \theta_R=D_R/\gamma .
\]
Along a subsequence suppose \(\log m/\log p\to\sigma>0,\ \log q/\log p\to\beta\ge0\) are finite. Give the actual phases any prescribed coloring with at most \(p^{\lambda+o(1)}\) colors. Fix \(0\le\kappa<\sigma+\beta\). Consider four distinct phases of one color, sorted by their **true unscaled heights** \(x_1<x_2<x_3<x_4\), for which
\[
       x_1+x_4=x_2+x_3,\qquad
             \log_2(x_4/x_1)\le p^{-\kappa}/\log p .                 \tag{1}
\]
Take any maximal collection of vertex-disjoint quadruples (1). The number \(J\) of uncovered phases satisfies
\[
 \limsup\frac{\log(1+J)}{\log p}
 \ \le\ \kappa+\lambda+\theta_R(\sigma+\beta-\kappa).                 \tag{2}
\]
The same conclusion holds with \(R=4\) on the right if \(\limsup X/m\le4\), by applying (2) first with a fixed larger \(R\).

If \(\mu(\log_23)\le3\) and \(q=p^{o(1)}\), then \(\sigma\le3\) in every limiting subsequence. With \(\kappa=\lambda=0\), (2) covers all but \(p^{3\theta_R+o(1)}\) phases; at limiting width four \(3\theta_4=0.95911343\ldots\). The upper exponent is strictly below one up to the fixed threshold \(R_* =4.1321644\ldots\) characterized by \(D_{R_*}=\gamma/3\). The cited irrationality-measure input is used only in this numerical corollary. [Original claimed measure theorem, Theorem 11.1](https://arxiv.org/abs/2610.28079) · [Formalization paper, Theorem 1.1](https://arxiv.org/abs/2611.30820)

There is a coherent two-sided version. With \(\ell=\lfloor c\log_2 p\rfloor\) the quadruples can be required to have the same true native valuation itinerary across all dates from \(-\ell\) to \(\ell\) within each quadruple. For \(R<R_*\) this costs at most \(2c\gamma\) in the exponent in (2). Thus if
\[
       \kappa+2c\gamma+\theta_R(3-\kappa)<1,                          \tag{3}
\]
almost every phase of an ordinary or subpolynomial-denominator cycle is covered, assuming the cited measure bound. Every one of these quadruples gives an exact additive relation at *every* date in this two-sided interval. At a fixed translated date the resulting quadruples are vertex-disjoint. At limiting width four, for example, one may take \(\kappa=0,\ c=0.012\), or \(\kappa=0.02,\ c=0.008\). The relation concerns ordinary rational addition among actual odd states of the given cycle. It does not assert the existence of any new ordinary cycle.

## Short physical intervals have a common native calendar

Partition \([m,Rm]\) into \(O_R(p^\kappa(\log p)^5)\) multiplicative bins of ratio at most \(1+p^{-\kappa}/(\log p)^5\). Fix one bin with left endpoint \(Y\), and use the same calendar for every phase with initial height in this bin. Fix a small \(u>0\) with \(\omega+u<e\), set \(L=4m2^{-u}\), and write
\[
 \begin{split}
 F_t&=\lfloor\log_2(Y/L)+t\gamma\rfloor,\qquad
 z_t=\{\log_2(Y/L)+t\gamma\},\\
 U_{t,i}&=2^{E_{t,i}},\qquad V_{t,i}=U_{t,i} x_{t,i},\qquad
 Z_{t,i}=2^{-F_t}V_{t,i},\qquad c_{t,i}=2^{-F_t}U_{t,i},
 \end{split}
\]
where \(E_{0,i}=0\) and \(E_{t,i}\) counts the actual divisions forward from the initial phase \(i\). The exact lift obeys \(V_{t+1,i}=3V_{t,i}+U_{t,i}\). Take
\[
             n=\lceil\log_3(32R(1+qm p^{-\kappa}))\rceil+4 .
\]
This tends to infinity, is \(O(\log p)\), and satisfies \(n/\log_2p\to(\sigma+\beta-\kappa)/\gamma\). The logarithm of \(Z_{t,i}/L\) equals \(z_t+\log_2(x_{0,i}/Y)\) plus the sum of \(t\) corrections \(\log_2(1+1/(3x_{j,i}))\). The latter is nonnegative and \(O(n/m)=o(1)\). Hence \(L\le Z_{t,i}\le2L(1+o(1))\) uniformly for \(0\le t\le n\). The bounds \(L>Rm/2,\ 2L<8m\) have fixed positive margins. Since \(Z_{t,i}=c_{t,i}x_{t,i}\), the dyadic powers \(c_{t,i}\) are exactly confined to the alphabet \(\{1,2,4\}\). Any tag one satisfies \(Z_{t,i}=x_{t,i}\le Rm\), so its row has \(z_t\le\omega+u\). This test is independent of the starting column.

Write \(b_t=F_{t+1}-F_t\). A winding one occurs precisely when \(0\le z_t<e\). It is followed by a winding two and its successor angle is at least \(\gamma-1>e\). Match each winding-one row with its successor within the \(n\) recorded rows, discarding only a possible final unpaired row to a separate coordinate of alphabet size at most three. The actual positive valuation equals \(b_t+\log_2c_{t+1,i}-\log_2c_{t,i}\), so along the matched edge the tag cannot decrease. For \(z_t>\omega+u\) the joint alphabet lies in \((2,2),(2,4),(4,4)\). For \(z_t\le\omega+u\) it lies in these three and \((1,2),(1,4)\). All unmatched rows, up to the stated endpoint, have binary alphabet \(\{2,4\}\). Uniform irrational-rotation averaging over the moving initial angle (for instance by trigonometric polynomial approximation to intervals) gives the counts divided by \(n\) as
\[
             s+o(1),\qquad e-\omega-u+o(1),\qquad
                    \omega+u+o(1)                                     \tag{4}
\]
for the binary, ternary and five-symbol coordinates, respectively. The calendar, horizon, matching, and \(o(1)\) estimates are common to every subset of the bin.

## Maximality gives a genuine Sidon subpopulation

Fix one color among the uncovered phases in the bin, with population \(M\). The bin diameter is small enough for (1), so there is no four-distinct equal-sum relation on this population. For each \(b\) in it, there is at most one unordered pair of distinct elements \(a,c\) with \(a+c=2b\); two different such pairs are disjoint and would give four distinct elements with equal pair sums. Hence there are at most \(M\) nonconstant three-term progressions. Randomly keep each point with probability \(1/2\), and delete one point for each remaining progression. The expected lower bound is \(M/2-M/8=3M/8\). Thus a subset of size at least \(3M/8\) has distinct unordered pair sums, with repetitions allowed. Indeed, pairs with a shared member cancel, two doubled members agree only when equal, and a doubled member versus a distinct pair would give a removed progression. Distinct phases have distinct heights because the cycle is primitive and the accelerated odd map is deterministic.

Encode each selected point by its matched word (4). Equal coordinatewise unordered symbol pairs determine equal sums of individual tags on every recorded row. If the two source pairs are \(i,j\) and \(k,l\), let \(H_t=Z_{t,i}+Z_{t,j}-Z_{t,k}-Z_{t,l}\). All \(qH_t\) are integers. Under equal pair outputs the genuine recurrence gives \(2^{F_n-F_0}H_n=3^nH_0\), hence \(2^{F_n-F_0}\mid qH_0\). Here \(F_n-F_0\ge n\gamma-1\), while \(qH_0=q2^{-F_0}(x_{0,i}+x_{0,j}-x_{0,k}-x_{0,l})\) has absolute value at most \(8Rqm p^{-\kappa}/(\log p)^5\), since \(Y\ge m,\ L\le4m\) give \(2^{-F_0}\le8\), and a pair-sum difference is at most twice the bin width (equivalently \(2^{-F_0}Y\le2L\le8m\)). The chosen horizon makes this strictly less than the divisor for large \(p\). Thus the actual source sums agree. The selected points are Sidon, so the source pairs coincide. This also implies injectivity of individual words by using doubled pairs.

## The mixed-alphabet upper bound

For clarity, the prefix calculation is the one in the [two-grade matched code proof](MATCHED_SIDON_CODES.md), using the original difference-code argument. [Della Fiore–Dalai, Theorem 2.1](https://doi.org/10.1016/j.disc.2021.112751) · [Author's complete proof, Theorem 3.2.1](https://stefano-dellafiore.unibs.it/contents/PhD_Thesis_.pdf)

Write \(f=e-\omega-u,\ g=\omega+u,\ K=f\gamma+g\log_25\). On any nontrivial limiting subsequence let \(x=\lim n^{-1}\log_2|\mathcal C|>0\). Order quintary coordinates first, then ternary, then binary, and choose the largest prefix capacity \(N\le|\mathcal C|/n^2\). Since successive capacity ratios are at most five, \(\log_2N=nx-O(\log n)-o(n)\). For uniformly chosen ordered pairs with equal prefix, the entropy of their suffix difference (zero when symbols agree, ordered pair otherwise) is at least \(nx-o(n)\). In fact there are \(T\ge|\mathcal C|^2/N\) ordered pairs. Each nondiagonal difference identifies the whole ordered pair by crossing the two putative pairs and applying unordered separation. The diagonal has probability at most \(n^{-2}\). In a suffix alphabet of size \(d\) the probability of zero is at least \(1/d\) by averaging squared marginal probabilities within each fiber. Its \(d(d-1)\) nonzero outputs therefore give entropy at most \((2-1/d)\log_2d\).

When \(x\le g\log_25\) keep this as an upper bound. For \(g\log_25\le x\le K\), all five-symbol coordinates have been used up to \(o(n)\) and the suffix entropy gives \(x\le 3s/2+(5/3)(K-x)\). For \(x\ge K\) it gives \(x\le(3/2)(s+K-x)\). Boundary effects are \(o(n)\). These three branches give \(x\le D_{4\cdot2^{\omega+u}}\). Applying the bound to the largest leftover color-bin cell, summing over the number of cells, and letting \(u\downarrow0\) proves (2).

## Coherence and numerical threshold

The positive cycle product gives \(0<A/p-\gamma\le1/(3m\ln2)\). On reducing \(A/p\), the reduced denominator tends to infinity whenever \(m\to\infty\). The assumption \(\mu(\gamma)\le3\) bounds \(m\le p^{3+o(1)}\); using an unreduced odd period only weakens this inequality. When \(q=p^{o(1)}\), distinct odd numerators in \([qm,qRm]\) give \(m\ge p^{1-o(1)}\), so every subsequence has further limiting exponents of the required type. At the numerical root the third affine branch of \(D_R\) equals \(\gamma/3\); the other two are strictly smaller. This gives
\[
 R_*=4\cdot2^{\left[(\gamma/3-9s/16)8/5-e\gamma\right]/(\log_25-\gamma)} .
\]

Since \(3R_*<16\), every true valuation on these cycles is at most three for all sufficiently large \(m\), from \(2^{a_t}m\le3Rm+1\). Color each center by the \(2\ell\) actual valuations from \(-\ell\) through \(\ell-1\); there are at most \(3^{2\ell}\) colors. The four centers in a packed quadruple undergo the same increasing affine map from the center to any future date in the window, or the same inverse affine map to a past date. This preserves exact pair-sum equality and strict order. The multiplicative slope over any forward subinterval is \(3^j2^{-\Delta E}\), equal to the ratio of the true endpoint heights times the reciprocal of \(\prod(1+1/(3x_t))\). Both slopes and their inverses are bounded by constants depending only on \(R\) for \(j=O(\log p)\). Hence the transported quadruple has log width \(O_R(p^{-\kappa}/\log p)\) at every date. Native translation permutes the phases, preserving disjointness.

The earlier [mixed-code width bound](MATCHED_SIDON_CODES.md) enforces global separation on two-grade, ordered rank lifts. The result here extracts actual additive configurations on physical heights with a three-grade calendar. It uses the hereditary upper bound only on the uncovered phases in each color-bin cell. Four-copy physical-source energy and its earlier matching constraint appear in the [prior complete-denominator packet](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md).
