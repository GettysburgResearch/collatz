# The matched-pair bound charges the full rational denominator throughout the two-grade band

**Proposed written theorem using an explicit approximation input.** Let \(\mu\ge2\) be an upper bound for the irrationality exponent of \(\gamma=\log_2 3\). Fix an odd-width bound \(2<R<4\). Use the physical minimum \(m\), maximum \(X\le Rm\), primitive odd period \(p\), and complete reduced denominator \(q\) of a positive rational Syracuse cycle. Define
\[
 \eta=\log_2(R/2),\quad f=(\eta-\gamma+1)_+,\quad s=\eta-2f,\quad
 \theta=\gamma^{-1}\min\{0.5753\eta,D(s,f)\},\quad
 \chi=\frac{s\log_2 6+f\log_2 15}{3\gamma},
\]
where \(D(s,f)=\max\{3(s+\gamma f)/5,\ 9s/16+5\gamma f/8\}\).
If \(\mu\theta<1\), put \(b=1/(\mu\theta)-1\). Then
\[
 \liminf_{m\to\infty}\frac{\log q}{\log m}\ge b,\qquad
 \liminf_{p\to\infty}\frac{\log q}{\log p}\ge
 \max\left\{\frac{b}{b+\chi},\
 \min\left(1-\chi,\frac{1-\mu\theta}{1-(\mu-1)\theta}\right)\right\}.  \tag{1}
\]
On the branch \(m/p\to\infty\), the last quotient alone is always a lower bound in (1). These exact-cycle estimates allow all positive native exponents and do not impose coprimality of the odd and halving clocks.

With the approximation input \(\mu=3\), (1) applies for **every fixed \(R<4\)**. Its limiting minimum and period bounds as \(R\uparrow4\) are respectively \(0.04262954\ldots\) and \(0.11338763\ldots\). In particular every fixed complete denominator then supports only finitely many such cycles in each fixed band. This is a substitution of the specified irrationality input; the written proof below also applies with the [published BLS exponent \(5.116201\)](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) wherever \(\mu\theta<1\). The [source statement of the newer exponent](https://arxiv.org/html/2610.28079v1#S11) has the usual quantifier over every strictly larger approximation exponent.

## A single pair collision propagates through the complete denominator

Use either of the two true chronological grids in the [rational six-sum construction](RATIONAL_SIX_SUM_DENOMINATORS.md) or its [reduced-clock version](REDUCED_CLOCK_SIX_SUMS.md). Here only pairs are required. The first grid uses arbitrary \(m\to\infty\). In its continued-fraction construction, for every \(\epsilon>0\), \(Q_{i+1}\ll_\epsilon Q_i^{\mu-1+\epsilon}\) by the definition of irrationality exponent, so \(N\ge m^{1/\mu-o(1)}\) in that construction. The second grid is available when \(m/p\to\infty\), with \(N=P=p/\gcd(A,p)\), where \(A\) is the nonreduced total division exponent. The full de-meaned angle error is \(O(p/m)\), uniformly across arbitrary numbers of traversals of the original lap. The two sampling clocks can be used independently on the same cycle.

In both cases take \(v=(1-\eta)/2\) and \(L=2^{1-v}m\). Then \(L>X/2,\ 2L<4m\) are strict, as required in the grid proofs. The synchronized columns \(Z_{t,j}\), \(0\le j\le W=\lfloor N/(\log N)^5\rfloor\), are actual dyadic lifts of phases of this cycle, with fixed common chronological base, winding \(h_t\), source tags \(c_{t,j}\in\{1,2\}\), and equations
\[
        2^{h_t} Z_{t+1,j}=3Z_{t,j}+c_{t,j},\qquad qZ_{t,j}\in\mathbb Z .
\]
They are \(p\)-periodic in \(t\). At true angles below \(v-o(1)\) or above \(v+\eta+o(1)\) all the column tags agree. There is also a length-\(N\) integer array \(qY_r=qL(2^{r/N}+o(1))\), with uniform relative error. On any compact interior interval of \(r/N\), each original column comparison is literally its spatial translation on that array, by the exact floor identity in the corresponding grid proof.

For two distinct unordered pairs of offsets, let \(T\) be the difference of their monomial sums, \(H_t=\sum_j T_j Z_{t,j}\), and \(d_t=\sum_jT_j c_{t,j}\). If \(H_t\) vanishes anywhere, it is integral everywhere: divisibility of \(qH_t\) by the odd \(q\) propagates forward around the whole physical \(p\)-cycle. Since \(|d_t|\le2\), the recurrence \(2^{h_t}H_{t+1}=3H_t+d_t\) then preserves every nonzero integer sign strictly. A zero on this cycle therefore forces **all** \(H_t=0\). In particular \(T(E)(qY)_r=0\) on every compact interior spatial interval. When \(qm\le N^K\) for a fixed \(K\), the [sparse integer recurrence theorem](SPARSE_RANK_RECURRENCES.md) excludes this, since \(T\ne0\) has at most four terms, bounded coefficients and degree at most \(W\). Hence all pair sums of the sampled columns at any base are distinct on such a polynomial-height sequence. This argument concerns the full reduced denominator, even on a grid of fewer ranks than the native period.

## Passing the actual matching to the sampled columns

Set \(n=\lceil\log_3(16qL)\rceil+2\). A coordinatewise pair sum of the tags over these \(n\) successive native dates determines its unordered pair of starts: equal tag sums give \(2^{\sum h_t}\mid qH_0\), with the divisor exceeding \(8qL\) and \(|qH_0|<8qL\) for large \(m\). Apply the preceding injection. In the polynomial-height case \(n=O(\log m)\). For the first grid \(N\ll m\) by construction. For the second \(N\le p=o(m)\). The true angle differs from the corresponding irrational rotation over these dates by \(O(n/m)=o(1)\), so all fixed arc and pair-intersection counts have their limiting lengths, uniformly in the starting angle.

Retain the rows in the availability interval \([v-o(1),v+\eta+o(1)]\), even if accidentally constant. Join two adjacent retained dates whenever the departure winding is one. Their limiting density is \(f\): the true positive angular increment is \(\gamma+O(1/m)\), and inside this interval a winding one followed by another retained date requires precisely that the angle and its unwrapped translate by \(\gamma-1+O(1/m)\) lie in the interval. The pairs are disjoint. The native exponent \(h_t+\log_2c_{t+1,j}-\log_2c_{t,j}\) is positive for every column. This gives just the three symbols \(00,01,11\) per matched site. There are \(sn+o(n)\) remaining singleton bits. Thus the ordinary [mixed-alphabet difference bound and independent binary bound](MATCHED_SIDON_CODES.md) apply to these actual rational-cycle words, giving
\[
                      \log N\le(\theta+o(1))\log(qm).                 \tag{2}
\]
If \(\log(qm)/\log N\) tends to infinity, the limsup-ratio form of (2) is immediate. Passing to bounded-ratio or divergent-ratio subsequences covers the full claim.

On the first grid \(N\ge m^{1/\mu-o(1)}\), giving the minimum bound. The [complete-denominator four-copy estimate](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md) is \(p\ll_{R,\epsilon}q(1+m)^{\chi+\epsilon}\). It gives the period bound \(b/(b+\chi)\), including bounded minima. For the reduced grid let \(g=\gcd(A,p)\). By the [zero-inversion residue-order theorem](RESIDUE_FIBER_INVERSIONS.md), \(g=\operatorname{ord}_q(3^P2^{-A/g})\le q\) throughout this band (with order one at \(q=1\)). Thus \(p\le qP\). Also \(A/p-\gamma\ll1/m\) by the actual positive clock drift, while \(A/p\) has reduced denominator \(P\), giving \(m\le P^{\mu+o(1)}\) on the large-minimum branch. From (2), \((1-\mu\theta-o(1))\log P\le(\theta+o(1))\log q\). This and \(p\le qP\) yield the last quotient in (1). To combine the branches, pass to convergent subsequences of \(\log(1+m)/\log p\), which are bounded by the clock inequality when \(m\to\infty\). A limit exceeding one gives \(m/p\to\infty\); a limit at most one gives the independent lower bound \(1-\chi\) by the four-copy estimate.

At \(R\uparrow4,\ \mu=3\), one has \(\theta\to0.3197044778\ldots,\ \chi\to0.4333973955\ldots\). The three period entries \(b/(b+\chi),\ 1-\chi,\ (1-3\theta)/(1-2\theta)\) tend to \(0.08955279\ldots,\ 0.56660260\ldots,\ 0.11338763\ldots\), respectively. Finiteness for bounded \(p\) and fixed \(q\) follows because \(m\ge1/q\) in that case, so \(A/p\le\log_2(3+q)\), and each of the finitely many words supplies at most one rational fixed point.
