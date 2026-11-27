# A superpolynomial remainder for the original subunit gate moment

Fix the odd-clock gate \(1<a<2\), put \(h=H_2(1/a)\) and \(p_c=1-a(1-h)\). Use the all-height law of [PR 200, sparse even remainder](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/SPARSE_EVEN_GATE_REMAINDER.md). At odd depth \(n\), a passing geometric word of holding total \(A=n+D\) has weight \(2^{-A}\), \(D\) is its number of additional even shortcut departures, and \(m\) is its original principal odd source. For \(z\ge0\) the payoff obeys \(Z_n(z)\le2^A/m\). For every fixed \(p_c<p<1\), there are \(c=c_{a,p}>0\) and \(n_0\) such that for all \(n\ge n_0\), uniformly for \(z\ge0\),
\[
 \mathbb E[{\bf1}_{W_n} Z_n(z)^p]
 \ \le\ 2^{-(1-p)n}\exp[-c(\log n)(\log\log n)].                 \tag{1}
\]
The polynomial improvement in the pinned PR used an elementary physical length bound for odd runs. Here the stronger input is [Paper 174, Theorem 1 (1)](https://rstation.ai/problems/collatz/papers/174), the quantitative rise-group estimate for physical positive integer trajectories. This is a written result conditional on that cited theorem, with no new formalization of its Subspace Theorem argument.

**Height versus even count.** Write \(k=\lfloor\log_2 m\rfloor\) and \(D_0(n)=c_0(\log n)(\log\log n)\) for a sufficiently small absolute \(c_0>0\), using natural logs here. For all large \(n\), every such actual word obeys
\[
 D\ge D_0(n)\quad\hbox{or}\quad k> \sqrt n.                       \tag{2}
\]
Indeed if \(D<D_0(n)\), the number of holdings \(\ge2\) is at most \(D\). Therefore at least \(P\ge n-D\ge n/2\) of the holdings equal one, and they form at most \(D+1\) maximal groups. These are the actual odd-map rises and rise groups, including truncated endpoint groups, in Paper 174. If \(k\le\sqrt n\), its \(P/(\log_2(m+1)+1)\) is at least a constant times \(\sqrt n\). Its theorem gives \(D+1\ge c_1(\log n)(\log\log n)\), contradicting the choice of \(c_0\). This concerns the same positive principal \(m\); the root is not redrawn.

**Summation.** For \(p_c<p\le h\) put \(v=(p-p_c)/(a-1)>0\), \(u=p-\log_2a>0\), \(k_0=aD/(a-1)\). As in the pinned PR the cost divided by \(2^{-(1-p)n}\), at fixed \(D\) after summing all heights, is \(O((1+D)2^{-vD})\), and the individual upper tail above \(k_0\) is \(O(2^{-vD}2^{-u(k-k_0)})\). The hypotheses \(p>p_c\) imply \(u>0\) in the stated range by that shell calculation. Sum \(D\ge D_0(n)\) using the first bound. For \(D<D_0(n)\), (2) puts every term at \(k>\sqrt n\), while \(k_0=O_a(D_0(n))=o(\sqrt n)\). The second bound and its geometric \(k\)-sum give \(O(n\,2^{-u\sqrt n/2})\). This proves (1), including \(p=h\).

For \(h<p<1\) the original summand is bounded by \(2^{-(1-p)n}2^{-(1-p)D}m^{-p}\). At each depth a principal source gives at most one word, since its actual trajectory is deterministic. The sparse global principal union \(\mathcal D\) satisfies \(\#(\mathcal D\cap[1,X])\ll_a X^h\) by [PR 201](https://github.com/GettysburgResearch/collatz/blob/d21bac748e705a64b6b57a7996a8ad6282f0bcbf/research/six-hour-20261127/escape/GLOBAL_PREFIX_TRACE.md). Thus \(\sum_{\mathcal D}m^{-p}<\infty\), and the part with \(D\ge D_0(n)\) costs \(O(2^{-(1-p)D_0(n)})\) after division by the common factor. The remaining part by (2) costs \(O(2^{-(p-h)\sqrt n})\) by dyadic summation over \(m\). This proves (1).

The same calculation gives a uniform moving-power upper bound for any fixed \(p_* \in (h,1)\), all \(p\in[p_*,1]\), and all sufficiently large \(n\):
\[
 2^{(1-p)n}\mathbb E[{\bf1}_{W_n}Z_n(z)^p]
 \le C_{a,p_*}\bigl\{ 2^{-(1-p)D_0(n)}+
                           2^{-(p_*-h)\sqrt n}\bigr\}.            \tag{3}
\]
Hence after removing the universal \(n\)-factor, that remainder still vanishes whenever \((1-p_n)\log n\log\log n\to\infty\). At \(p=1\), (3) reduces to a bounded first moment. The additional exponent specifically charges all the extra even departures and disappears from the payoff if it is reversed to first power. A fixed persistent ordinary atom \(m\), if one exists, is fully compatible with (1)–(3).
