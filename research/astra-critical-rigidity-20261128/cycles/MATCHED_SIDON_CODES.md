# The matched tag pairs force an approximation exponent above three throughout the two-grade band

**Proposed written theorem.** Let \(p,m,X,A\) be the primitive odd period, least odd state, greatest odd state and total native division exponent of a positive ordinary cycle. Fix \(2<R<4\), set \(\gamma=\log_2 3,\ \alpha=\gamma-1,\ \eta=\log_2(R/2)\), and put
\[
 f=(\eta-\alpha)_+,\qquad s=\eta-2f,\qquad
 D(s,f)=\max\left\{\frac35(s+\gamma f),\
                         \frac9{16}s+\frac58\gamma f\right\}.
\]
Along any sequence of such cycles with \(p\to\infty,\ X/m\le R\),
\[
 \limsup \frac{\log p}{\log m}\le
 \frac{\min(0.5753\,\eta,D(s,f))}{\gamma}.                         \tag{1}
\]
The binary \(0.5753\) branch is the [previous two-grade code theorem](TWO_GRADE_SIDON.md). The new mixed-alphabet branch retains the native matching between consecutive tag rows. As \(R\uparrow4\), its numerator tends to \(0.50671960\ldots\). Throughout the fixed-width band the candidate clocks therefore satisfy
\[
              0<A/p-\gamma\le p^{-3.12788862+o(1)}.                 \tag{2}
\]
In particular, **if** the irrationality exponent of \(\log_2 3\) is strictly less than \(3.12788862\), then only finitely many ordinary cycles have width at most each fixed \(R<4\), and every growing sequence satisfies \(\liminf X/m\ge4\). The assumption \(\mu(\log_2 3)\le3\) is sufficient. The clock restriction (1) uses no such additional assumption. A sequence whose widths tend to four is permitted by this conditional conclusion.

## A mixed-alphabet difference bound

Suppose a code of \(M\) words in \(s_n\) binary and \(f_n\) ternary coordinates identifies every unordered pair, with repetitions, from the coordinatewise unordered symbol pairs. Normalize by a scale \(n\to\infty\), and suppose \(s_n/n\to s,\ f_n/n\to f\). Then
\[
                      \limsup n^{-1}\log_2 M \le D(s,f).             \tag{3}
\]
Here the ternary symbols will stand for the three allowed two-bit configurations. Coordinatewise unordered pairs of ternary symbols determine the two constituent integer bit sums, so the physical binary Sidon property gives the required identification. This direction needs no independence of physical sites.

The proof adapts the homogeneous-alphabet entropy argument of Della Fiore and Dalai with ternary coordinates placed first in the prefix. [Original paper, Theorem 2.1](https://doi.org/10.1016/j.disc.2021.112751) · [Author's full proof, Chapter 3, Theorem 3.2.1](https://stefano-dellafiore.unibs.it/contents/PhD_Thesis_.pdf)

Work on a subsequence with \((\log_2M)/n\to x>0\). Take all coordinates in ternary-first order. Choose the longest initial segment whose number \(N\) of possible prefixes is at most \(M/n^2\). Then \(\log_2 N=\log_2 M-O(\log n)\) since the next alphabet has size at most three and the whole product contains the code. Divide the code into prefix fibers of sizes \(M_h\). There are \(T=\sum_h M_h^2\ge M^2/N\) ordered pairs with a common prefix, counted with the diagonal. Choose one of the \(T\) pairs uniformly.

At each suffix coordinate write down zero if the two symbols agree, and their ordered pair otherwise. A nonzero suffix output identifies the entire ordered codeword pair. In fact, if outputs for \((u,v)\) and \((u',v')\) agree, then the cross pairs \((u,v')\) and \((v,u')\) have the same unordered symbol pair in every suffix coordinate. The common-prefix condition separately in the two ordered pairs gives this equality in the prefix coordinates as well. Separation and \(u\ne v\) give \(u=u', v=v'\). All zero suffix output identifies one of the \(M\) diagonal pairs. Its probability is \(M/T\le1/n^2\). Thus the entropy of the full suffix output is at least \(\log_2 T-(M/T)\log_2 M\ge \log_2M-o(n)\).

For an alphabet of size \(d\), the zero probability in each fiber is a sum of squared marginal probabilities, hence at least \(1/d\). The same holds after mixing fibers with weights \(M_h^2/T\). There are \(d(d-1)\) nonzero outcomes, so coordinate entropy is at most \((2-1/d)\log_2d\): entropy decreases as the mass of zero moves above \(1/d\), and at fixed zero mass it is maximized with uniform nonzero outputs. Subadditivity therefore charges \(3/2\) bits per remaining binary coordinate and \(5\gamma/3\) bits per remaining ternary coordinate.

If \(x\le\gamma f\), all but \(o(n)\) used prefix bits are ternary, including equality at the endpoint. Hence \(x\le 3s/2+(5/3)(\gamma f-x)\), giving \(x\le9s/16+5\gamma f/8\). If \(x>\gamma f\), all ternary coordinates are in the prefix, and \(x\le(3/2)(s+\gamma f-x)\). This gives \(x\le3(s+\gamma f)/5\). The case \(x=0\) is immediate. This proves (3).

## The matching occurs in the actual rank chart

Use the folded chart and the physical binary Sidon code of the two-grade theorem, now with starts \(0\le j\le W=\lfloor p/(\log p)^5\rfloor\). Their count is \(p^{1-o(1)}\). Write \(v=(1-\eta)/2\), \(L=2^{1-v}m,\ n=\lceil\log_3(8L)\rceil+2\). At chronological date \(t\) the base rank fraction is \(z_t=\{tA/p\}\). All the actual unwrapped tags lie in \(\{1,2\}\). Outside a common interval \(I=[v-\epsilon_p,v+\eta+\epsilon_p]\) their values are constant over the columns, where \(\epsilon_p\to0\) absorbs the spatial length and the uniform angular discrepancy. Retain every row in this interval, including a row that happens to be constant. The ratio of retained rows to \(n\) tends to \(\eta\) by moving irrational-rotation averaging as proved in the binary code theorem.

Pair a retained departure \(t<n-1\) with \(t+1\) whenever the winding at \(t\) is one and \(t+1\) is retained. Writing \(\alpha_p=A/p-1\to\alpha\), its precise condition is \(z_t\in I,\ z_t+\alpha_p\in I,\ z_t+\alpha_p<1\). The last condition follows from the second at all large \(p\). The length of this interval tends to \(f\). Moving-rotation averaging gives \(f_n/n\to f\). Such pairs are disjoint because a winding one is followed by a winding two when \(\alpha_p>1/2\). The remaining singleton count therefore satisfies \(s_n/n\to s\). The true native exponent on a column is \(b_t+\log_2 c_{t+1}-\log_2 c_t\ge1\). Thus the two bits \((c_t-1,c_{t+1}-1)\) at each matched pair admit only \(00,01,11\). Their three configurations serve as the ternary alphabet of (3). The physical coding proof already shows that coordinatewise equal binary sums determine the original unordered pair, via the full dyadic cylinder and strict ordinary pair-sum order. This proves (1).

For \(0\le\eta\le\alpha\) both affine terms in \(D\) increase with \(\eta\). For \(\alpha\le\eta\le1\) their derivatives equal \(3(\gamma-1)/5\) and \(5\gamma/8-9/16\), both positive. At \(\eta=1\), \(s=2\alpha-1,\ f=1-\alpha\), and the larger term is \(9s/16+5\gamma f/8\). Its reciprocal ratio \(\gamma/D=3.127888625\ldots\), together with the ordinary positive angular identity \(0<A/p-\gamma\le1/(3m\ln2)\), gives (2). The clocks are reduced in the two-grade chart. The definition of irrationality exponent now gives the finite and limiting conditional statements above. For fixed bounded \(p\), there are finitely many ordinary cycles: summing the angular increments for \(m\ge1\) bounds \(A\le2p\), and each positive exponent word has at most one positive fixed point.

The two-grade matching itself and its local energy were previously proved in Weaver 145/181 and in the four-copy packet. The mixed-prefix estimate here uses matching on actual binary Sidon columns of one integral cycle. [Previous matching and complete-denominator source count](https://github.com/GettysburgResearch/collatz/blob/5136b7fe70176172405a0de168a2de2ed26429b8/research/astra-global-rigidity-20261128/cycles/FOUR_COPY_WIDTH.md)
