# Fourth sums at the critical odd width force geometric near coincidences

**Proposed written theorem using the cited inputs.** Let \(m,X,p\) be the odd minimum, odd maximum, and primitive odd period of an ordinary positive cycle. Let \(\xi=2^{1/p}\), \(W=\lfloor p/(\log p)^5\rfloor\), \(\gamma=\log_2 3\), and \(\nu=5.116201\). Along any sequence \(p\to\infty,\ X/m\le3+o(1)\), for every sufficiently large \(p\) there are at least
\[
                              p^{4.4676419-o(1)}                          \tag{1}
\]
ordered eight-tuples of **eight distinct** offsets \(0\le i_1,\ldots,i_4,j_1,\ldots,j_4\le W\) with
\[
       0<\left|\sum_{a=1}^4\xi^{i_a}-\sum_{a=1}^4\xi^{j_a}\right|
                      \le20/L\ll p^{-4.8439723+o(1)}.                     \tag{2}
\]
Here \(L=2^{1-v}m\) is a folded-chart scale with fixed sufficiently small \(v>0\). The number in (1) counts ordered tuples, without averaging over periods. Its exponent is strictly above the order \(p^4\) of the diagonal four-sum pairs. No upper estimate for the off-diagonal count at this scale is asserted.

A second conclusion holds at every fixed \(2<R<256/81=3.16049\ldots\) with \(X/m\le R\). If a four-versus-four polynomial \(P(T)=\sum T^{i_a}-\sum T^{j_a}\), with all offsets in \([0,W]\), satisfies \(L|P(\xi)|>20\), its actual integer comparison \(P(E)Z_r\) has the strict sign of \(P(\xi)\) at **every** spatial origin in the ordinary folded chart. Whenever a physical equality occurs at one rank, instead \(|P(E)Z_r|\le20\) at every rank. These statements allow repetitions.

## Five intervals preserve an integer bound in reverse time

Use the [ordinary two-grade rank chart](TWO_GRADE_SIDON.md). Set \(\alpha=\gamma-1\), \(\eta=\log_2(R/2)\), choose \(v>0\) small, and choose a fixed \(U\) such that
\[
                 \max(\alpha,v+\eta)<U<3-4\alpha .
\]
This is possible exactly up to the stated outer threshold \(R<256/81\). The sorted octave representatives \(Z_r\in[L,2L)\) and the tags \(c_r\) are extended by doubling at the rank seam. The native chronological successor advances rank by \(A\pmod p\), where \(A\) is the full division sum, \(\gcd(A,p)=1\), and \(a=A/p-1\to\alpha\). Set \(e=1-a\), \(f=r/p\), and \(f'=\{f+a\}\). The winding \(h\) is one if \(f<e\) and two otherwise. All tags on a short tuple are in \(\{1,2\}\) and they are all two whenever \(f>U\), including across the seam.

Write \(H_r=P(E)Z_r\) at fundamental bases, and \(d_r=P(E)c_r\). Then \(2^h H_{r'}=3H_r+d_r,\ |d_r|\le4\). At forced rows \(d_r=0\); as \(H_r\) is an integer, also \(4\mid H_r\) there. At large \(p\), \(0<2e-a<e<U<2e<1\) and \(U<3-4a\). Define a magnitude bound \(K(f)\) as follows.

| Current interval | \(K(f)\) | Upper bound on the next magnitude \(K(f')\) |
|---|---:|---:|
| \(0\le f<2e-a\) | 12 | 17 |
| \(2e-a\le f<e\) | 14 | 20 |
| \(e\le f\le U\) | 17 | 12 |
| \(U<f<2e\) | 16 | 14 |
| \(2e\le f<1\) | 20 | 17 |

The first two successor bounds use \(f'=f+a\). In the third line \(f'=f+a-1<2e-a\) by the strict bound on \(U\). In the fourth \(f'<e\); in the fifth \(e\le f'<a\), before the final interval since \(a<2e\). In the first three lines, \(|H_{r'}|\le K(f')\) implies \(|H_r|\le K(f)\) by taking the integer floor of \((2\cdot17+4)/3,\ (2\cdot20+4)/3,\ (4\cdot12+4)/3\), respectively. In the last two, \(3H_r=4H_{r'}\) forces \(3\mid H_{r'}\). The largest eligible successor magnitudes are twelve and fifteen, giving sixteen and twenty. This proves the reverse-time implication at every rank. From any zero, induction back around the full chronological circuit gives \(|H_r|\le20\) everywhere.

The doubled spatial extension gives the exact identity
\[
 \sum_{r=0}^{p-1}\xi^{-r}H_r=P(\xi)\sum_{r=0}^{p-1}\xi^{-r}Z_r.          \tag{3}
\]
For each offset, reindexing the weighted sum contributes \(\xi^{i_a}\), also across the seam since \(\xi^p=2\). Consequently a zero implies \(|P(\xi)|\le20/L\). Without zeros, a positive integer in the scalar recurrence cannot become negative in one step: its numerator is at least \(-1\), and the divisor is at least two. The same holds after negation. The primitive chronological circuit gives a single sign, which (3) identifies.

## Lower bounding the unweighted number of near coincidences

For any set of starts \(S\subset[0,W]\), take \(n=\lceil\log_3(16L)\rceil+2\) consecutive edges in the chart and record the tags of the columns for each \(i\in S\). Delete constant rows. The resulting binary vectors have dimension \(d\le(\eta+o(1))n\) by the uniform moving-rotation average in the [three-sum proof](THREE_SUM_RANK_ORDER.md). Equal coordinate sums of four vectors give \(d_r=0\) throughout this interval and make the initial integer \(H\) divisible by \(2^{\lfloor n A/p\rfloor}>8L\). Its magnitude is less than \(8L\) for large \(p\). Thus every such code collision gives genuine equal fourth sums at the initial rank; the previous section gives (2)'s bound \(20/L\) on the ideal sums. The coding implication uses only one calendar interval.

The collision probability of four iid vectors from any law on the \(d\)-cube is at least \((70/256)^d\). Apply the convex torus \(L^8\)-norm argument of [Gu, Proposition 3.8, attributed there to Polyanskiy](https://arxiv.org/abs/1809.07364), or repeat the flip average in the [three-sum proof](THREE_SUM_RANK_ORDER.md) with four summands. Hence there are at least
\[
 |S|^8 m^{-\lambda_R-o(1)},\qquad
               \lambda_R=\frac{\eta}{\gamma}\log_2(256/70),              \tag{4}
\]
ordered code collisions. At this width \(R<256/81<27/8\), genuine physical triple sums are distinct as multisets. A nondiagonal four-sum equality therefore has disjoint supports on its two sides. Further, for one fixed left quadruple, there are at most \(4!|S|\) possible right quadruples with the same physical sum: designate the first right member, and its remaining triple is unique up to order. Quadruples with a repeated entry on a designated side number \(O(|S|^3)\), so all collisions involving a side with repetitions cost \(O(|S|^4)\), also allowing permutations and the diagonal. Thus the count in (4), less \(O(|S|^4)\), has eight distinct indices and satisfies \(|P(\xi)|\le20/L\). For these \(P\ne0\) one has \(P(\xi)\ne0\) by Eisenstein irreducibility of \(T^p-2\) and \(\deg P<p\).

At \(X/m\le3+o(1)\) apply (4) first at fixed \(R>3\) and let \(R\downarrow3\); equivalently enclose the varying upper phase endpoint before shrinking its enlargement. For \(S=[0,W]\), \(|S|=p^{1-o(1)}\). The [published two-logarithm theorem](https://doi.org/10.22405/2226-8383-2018-19-1-15-25) gives \(m\ll p^\nu\). At this limiting width \(\lambda_3=0.69042597\ldots\), giving \(8-\nu\lambda_3=4.46764192\ldots\) in (1). The [ordinary three-sum rate](THREE_SUM_RANK_ORDER.md) gives \(m\ge p^{3\gamma/(\alpha\log_2(16/5))-o(1)}=p^{4.84397232\ldots-o(1)}\), yielding the scale in (2). The two exponents come from separate bounds on the same physical minimum. An upper bound \(p^{4.46}\), for example, for the number of these eight-distinct geometric coincidences at the displayed scale on all sufficiently large candidate clocks would exclude this limiting width. The coding argument itself supplies the lower bound.
