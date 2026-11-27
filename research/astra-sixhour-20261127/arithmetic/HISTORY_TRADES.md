# Large-area four-phase rectangles in actual cycle histories

**Written theorem for the bounded least-disagreement branch.** With asymmetric past and future windows, all sufficiently large candidates have at least \(p-\lceil p^{199/200}\rceil\) linearly independent four-phase rectangles on actual states. Each rectangle persists through both windows and its two positive side lengths satisfy \(AB\ge c s^2/p\). Here \(c>0\) is absolute. The balanced-window variant gives a longer future window and permits six-phase relations.

Let \(s\) be its ordinary minimum, \(p\) its least odd period, \(h\) its division count, and \(\lambda=h/p\). For all sufficiently large candidates set
\[
L=\left\lceil\frac{49\log_2 p}{32\lambda}\right\rceil.
\]
Among the \(p\) actual rank phases there are at least \(p-\lceil p^{99/100}\rceil\) linearly independent signed relations over \(\mathbb Q\). Each uses four or six **distinct** ranks, with equally many coefficients \(+1\) and \(-1\). Each single relation holds for the actual normalized states at the central cut and at **every** chronological shift from \(-L\) to \(+L\), with the dyadic lifts specified below. The multisets of the local rank digits on its two sides also agree at each of those departures. The matchings on the past and future can be different.

The statement combines actual integer phases of a single cycle. Its asymptotic height input is the external logarithm-ratio estimate below. Lean checks the finite two-modulus and synchronous transport implications. The combinatorial existence and asymptotic applications are written proofs.

## A common clock on both sides of the cut

Take the lifted rank array and digits from the [physical mask theorem](https://github.com/GettysburgResearch/collatz/blob/03b26119164664d08eaa04a1ea1d159dd4eccd7a/research/astra-global-closure-20261124/round13/cycle/README.md). Thus \(4s\le U_r<8s\) on \(0\le r<p\), \(U_{r+p}=2U_r\), \(c_{r+p}=2c_r\), and \(U_{r+h}=3U_r+c_r\). Global indices used for the following values are nonnegative. For each integer \(j\) put
\[
 m_j=\lfloor jh/p\rfloor,\qquad t_j=jh-m_jp,\qquad
 u_j(r)=U_{r+t_j},\quad v_j(r)=c_{r+t_j}.
\]
The extra dyadic factor when \(r+t_j\ge p\) belongs to the value. With \(\beta_j=m_{j+1}-m_j\), direct substitution gives the common clock
\[
 2^{\beta_j}u_{j+1}(r)=3u_j(r)+v_j(r)                       \tag{1}
\]
for every rank, including negative chronological indices. A past vertex is one occurring vector \((v_{-L},\ldots,v_{-1})\); a future vertex is one occurring vector \((v_0,\ldots,v_{L-1})\). Put one bipartite edge labeled \(r\) between its actual past and future. In particular a free concatenation of unrelated past and future words does not count as an edge.

Write \(M=2^{m_L},N=3^L\). If two ranks share their future, (1) gives \(M\mid U_r-U_{r'}\), since \(3^L\) is odd. A shared past gives \(N\mid U_r-U_{r'}\), since \(2^{-m_{-L}}\) is prime to three. For an actual rational cycle with common odd denominator \(q\), the integer labels are \(qU_r\) in both statements. These divisibilities follow by multiplying (1) by \(q\) before unrolling.

The [population transfer](RANK_SPACING.md) bounds the number of vertices on either side by \(O((L+1)^2 2^{(12/25)\lambda L})\), uniformly on the sufficiently small critical slope neighborhood. To see this for the lifted digits, partition the starting ranks at the at most \(L\) changes in each window's wrap indicators \(1_{r+t_j\ge p}\), and at the mechanical schedule cuts at which one of its native layer transitions changes. There are \(O(L+1)\) cuts of either kind. On each resulting cell the indicators, schedule and possible starting layers are known. The same 256-step free-exit count bounds the number of chronological layer histories from the first to the last date, regardless of the sign of the first date. The digits are determined by these layers and the recorded wraps. The displayed polynomial factor allows either parameter partition to be counted separately.

## Integral alternating sums

Orient a simple graph cycle of length \(2\ell\) with signs alternating around it. The signed sum of the integer edge labels is divisible by \(M\) from the future vertices, and by \(N\) from the past vertices. Since the moduli are coprime, it is divisible by \(MN\). Its absolute value is at most \(\ell\) times the range of the integer edge labels. In particular a rational cycle with a nonzero signed sum of the actual \(U_r\) obeys \(q\ell(\max U-\min U)\ge MN\). Even a parallel-edge pair satisfies this test. For ordinary phases there are no parallel edges once \(MN>\max U-\min U\), since the ordinary labels are distinct.

In the bounded ordinary branch, \(s\le p^{3+o(1)}\) along any unbounded sequence. This follows by combining the cycle product with the external bound \(\mu(\log_2 3)\le3\). Also \(\lambda\to\log_2 3\), so at the specified length
\[
 M,N=p^{49/32+o(1)},\qquad MN=p^{49/16+o(1)},\qquad |V|\le p^{147/200+o(1)}.
\]
The graph is simple and every four- or six-edge alternating sum is exactly zero, since \(49/16>3\). [Chudnovsky, Theorem 11.1](https://arxiv.org/abs/2610.28079)

A simple bipartite graph with \(v\) vertices and more than \(Cv^{4/3}\) edges contains a four- or six-cycle, for an absolute constant \(C\). Indeed iteratively remove vertices of degree less than \(e/(2v)\). The nonempty resulting graph has minimum degree at least \(e/(2v)\). If there is no cycle through length six, the breadth-first tree from a vertex has distinct vertices out to distance three, and therefore at least a constant times \((e/v)^3\) vertices when \(e/v\ge 8\). This proves the claimed bound, enlarging the constant for smaller degree.

Here \(|V|^{4/3}\le p^{49/50+o(1)}\). While more than \(\lceil p^{99/100}\rceil\) edges remain, select a four- or six-cycle and remove one of its edges. Its vector of alternating signs has a nonzero coefficient on that edge; every later vector has zero there. The selected vectors are linearly independent by their successive pivot edges.

For each selected vector, paired future vertices cancel the signed sum of all \(v_j\) for \(0\le j<L\), and paired past vertices do so for \(-L\le j<0\). They actually pair the entire corresponding words. The signed sum of \(u_0\) is zero by the two-place argument. Equation (1) propagates this equality forward and backward at every intervening date. This proves the theorem. [Finite Lean implications](HistoryTrades.lean)

## Four actual phases and a forced large rectangle area

Instead choose different numbers of odd departures in the two directions,
\[
 L_F=\left\lceil\frac{25\log_2p}{24\lambda}\right\rceil,\qquad
 L_P=\left\lceil\frac{49\log_2p}{24\lambda}\right\rceil.
\]
Use the same lifted graph with future window \(0\le j<L_F\), past window \(-L_P\le j<0\), and moduli \(M=2^{m_{L_F}},N=3^{L_P}\). The numbers of its future and past vertices are respectively at most \(p^{1/2+o(1)}\) and \(p^{49/50+o(1)}\). Its product modulus is \(p^{37/12+o(1)}\), again larger than any four-term range loss. In a four-cycle-free bipartite graph with these part sizes \(f,b\) and edge count \(e\), each unordered pair of future vertices is adjacent to at most one common past vertex. Thus \(\sum_{v\in P}\binom{d_v}{2}\le\binom f2\), and Cauchy–Schwarz gives \(e\le b+f\sqrt b\). Here this upper bound is \(p^{99/100+o(1)}\). Removing one pivot edge from each four-cycle while more than \(\lceil p^{199/200}\rceil\) edges remain yields the claimed independent four-edge relations. Each relation kills every \(u_j\) on \([-L_P,L_F]\), by the same common-clock transport.

Its four central labels form a rectangle \(x,x+A,x+B,x+A+B\), where \(A,B>0\), \(M\mid A\) and \(N\mid B\), upon orienting the two graph directions separately. The physical rank estimate gives \(\lvert\log(U_r/(4s))-(r/p)\log2\rvert\le h\log2-p\log3\le p/(3s)\) uniformly: each chronological arc contributes its partial sum of positive logarithmic corrections minus its proportional share of the full sum. Since \(p^2/s=o(1)\), consecutive ranks differ in log by at least \((\log2)/p-2p/(3s)\ge(\log2)/(2p)\) eventually. Thus rank order is numerical order, and distinct ranks have true gap at least \(c_1s/p\) for an absolute \(c_1>0\). Therefore \(A\ge c_1s/p\), while \(B\ge N=p^{49/24+o(1)}\) is asymptotically larger than \(p^2\). This makes \(AB/(ps)\to\infty\) uniformly. The rank restriction below now forces **every one** of these rectangles to satisfy \(AB\ge c s^2/p\). Equivalently the larger anchor of two equal such \(B\)-gaps has a strictly smaller rank displacement than the other. Indeed the signed cross difference of their ranks is a negative integer, by the rank-log identity below and \(AB/(ps)\to\infty\).

## A longer window splits every value into a past and a future potential

Take \(L=\lceil49\log_2p/(24\lambda)\rceil\) instead. Now \(MN=p^{49/12+o(1)}>p(\max U-\min U)\) eventually and \(|V|\le p^{49/50+o(1)}\). Every simple alternating cycle, of any length, has zero signed sum. Each connected component admits integer functions \(A\) on its past vertices and \(B\) on its future vertices such that each edge has label
\[
                              U_r=A(P_r)+B(F_r).
\]
To construct them, set one vertex potential to zero, solve each edge equation along a spanning tree, and use its fundamental cycle for every remaining edge. All differences of past potentials in that component are multiples of \(M\): move along two-edge paths through a shared future vertex. All differences of future potentials are multiples of \(N\) by the reversed argument. The same graph cycle space annihilates every state column \((u_j(r))_r\) at \(|j|\le L\) by (1).

The [exact checker](check_history_trades.py) tests every fundamental cycle in four supplied genuine fixtures at four window lengths, including the ordinary fixed point. In the actual 41-phase rational control at \(L=3\), ranks \((10,7,3,9)\) give signed sum \(-6333111209664/44835377399\). Its cleared numerator is exactly \(-14659979652\) times \(2^4 3^3\). Thus a nonzero alternating sum occurs before the ordinary height argument, and the full denominator matters. [Control output](../../../reports/astra-sixhour-20261127/arithmetic/history_trades.json)

The relations hold only over the stated bilateral windows. A contradiction would follow from a theorem precluding this many independent, short, synchronously balanced relations among integral phase histories. Neither the graph argument nor single-segment moment bounds establish that additional assertion.

## The missing linear dependency in a longer digit matrix

There is an elementary quantitative version of the shift obstruction. This section uses any \(1\le L<p\) and the forward integer matrix \(C_{jr}=v_j(r)\) for \(0\le j<L\). Its entries lie in \(\{1,2,4,8\}\), including wrapped ranks. Suppose the phases are ordinary. Given an integer \(H\ge1\) with \(8spH<2^{m_L}\), let \(W_H\) be the rational span of all integer vectors \(b\in\ker C\) with \(\|b\|_\infty\le H\). Then
\[
 L+1\ \le\ \operatorname{codim}_{\mathbb Q} W_H
 \ \le\ L+\frac{L\log(C_0\sqrt p)+\log2}{\log(H+1)}                \tag{2}
\]
for an absolute constant \(C_0\). In particular if \(L/\log p\to\infty\), \(L<p\), and \(H=\lfloor 2^{m_L}/(16ps)\rfloor\), the upper bound is \(L+(1/(2\log3)+o(1))\log p\). This counts independent directions among small integer relations; it does not bound their support by six.

For the lower bound, if \(Cb=0\), (1) unrolls to \(2^{m_L}b\cdot u_L=3^L b\cdot U\). In particular any vector used to define \(W_H\) has \(2^{m_L}\mid b\cdot U\), while \(|b\cdot U|<8spH<2^{m_L}\). Thus it annihilates \(U\) and, by (1), all \(L+1\) state columns. The independence of those columns is exact. On \(\mathbb Q^p\) let \(T\) shift rank by one, multiplying by two on the wrap. It has minimal polynomial \(X^p-2\): it is annihilated by this polynomial, which is irreducible by Eisenstein. Hence \(\mathbb Q[T]\) is a field of degree \(p\). For \(S=T^h\), the physical rank assumption \(\gcd(p,h)=1\) gives \(\mathbb Q[S]=\mathbb Q[T]\) by Bezout, using \(T^p=2I\) and \(S^p=2^h I\) to handle negative powers. Every nonzero vector, in particular \(U\), is cyclic for \(S\), because it is a nonzero vector in a one-dimensional vector space over this field. Now \(u_j=2^{-m_j}S^jU\). Likewise the local digit columns are independent, as scalar multiples of \(S^j c\), and \(c=(S-3I)U\). Thus \(\ker C\) has codimension exactly \(L\). At least one direction in this kernel is absent from \(W_H\). Equivalently \(U\) cannot be a rational combination of the first \(L\) digit columns: such a combination would give a nonzero polynomial \((X-3)P(X)-1\) of degree at most \(L<p\) annihilating \(U\).

For the upper bound, any two points of \(\{0,\ldots,H\}^p\) with equal images under \(C\) differ by a vector in \(W_H\). In each affine translate of \(W_H\), some \(\dim W_H\) pivot coordinates determine the entire point. Consequently a fiber has at most \((H+1)^{\dim W_H}\) points. The crude count of all images, \((8pH+1)^L\), already leaves only \(O(\log p)\) extra directions for the indicated budgets. To obtain (2), sample the input \(b\) uniformly from that box. Independence of its coordinates and the digit bound give \(\mathbb E\|Cb-\mathbb E Cb\|_2^2\le64LpH^2\). At least half the inputs therefore have image in a ball of squared radius \(128LpH^2\). For any real center \(t\), this ball in \(\mathbb Z^L\) has at most
\[
 e^L\prod_{j<L}\sum_{n\in\mathbb Z}e^{-(n-t_j)^2/(128pH^2)}
 \le (C_0H\sqrt p)^L
\]
points, by bounding each one-dimensional Gaussian sum by its integral plus two. Multiply the fiber bound by this image count and compare with \((H+1)^p/2\). Finally \(\log(H+1)=(\log3+o(1))L\) at the stated asymptotic budgets, since \(s\le p^{3+o(1)}\). This proves (2).

The distinction between one shift and an invariant subspace is exact. For any nonzero proper rational subspace \(V\), the degree-\(p\) field action gives \(\dim(V+SV)\ge\dim V+1\). The short-trade space annihilates a finite interval of \(U\)-shifts. The elementary upper bound in (2) still permits the necessary extra direction; it does not turn that interval into a full orbit. Splitting the digit rows into \(g\) disjoint runs also requires one initial state per run. For total length \(gL\) and a common height budget controlled by the length of just one run, the same counting loss is \(O(g\log p)\).

## Rank restriction on four-phase trades

Every four-phase trade in the short-window theorem is an actual integer rectangle \(x,x+A,x+B,x+A+B\) with \(A,B>0\). Its edge differences in the two graph directions are multiples of \(M,N\), respectively, so \(MN\mid AB\). The [physical rank approximation](RANK_SPACING.md) supplies one further restriction: there are absolute \(c,C>0\) such that
\[
                                 AB\le Cps\quad\text{or}\quad AB\ge c s^2/p.
\]
Indeed write \(r(y)\) for the unique rank of a value \(y\). The integer \(r(x)+r(x+A+B)-r(x+A)-r(x+B)\) equals
\[
 \frac{p}{\log2}\log\!\left(1-\frac{AB}{(x+A)(x+B)}\right)+O(p^2/s).
\]
All four values are in \([4s,8s)\). If \(AB<c s^2/p\), a sufficiently small absolute \(c\), and then \(p^2/s=o(1)\), make this integer zero. Its logarithm is then \(O(p/s)\), giving \(AB\le Cps\). This excludes intermediate rectangle areas. The symmetric-window extraction permits six-edge cycles and four-edge rectangles in either surviving range. The asymmetric extraction above forces four-edge rectangles into the large-area range.

## A single set of earlier ranks reconstructs the other corners

Fix any \(0<\delta<1/25\). There exist \(\epsilon>0\) and \(\kappa<1\), depending only on \(\delta\), with the following stronger asymmetric consequence. Use future and past odd lengths \(\lceil (1+\epsilon)\log_2 p/\lambda\rceil\) and \(\lceil (2+\epsilon)\log_2 p/\lambda\rceil\), respectively. There is one set of at most \(p^\kappa\) retained ranks such that every other rank is the largest corner of a four-phase rectangle with its other three corners **all belonging to that retained set and earlier in rank order**. Its one signed identity persists across the entire common-clock bilateral window. Uniformly for all these rectangles,
\[
                           AB\ge c_\delta s^2 p^{-1+\delta}.
\]

Refine the past vertex of each rank by also recording that rank modulo \(D=\lfloor p^\delta\rfloor\). The two vertex exponents are at most \(f_0=(12/25)(1+\epsilon)\) and \(b_0=(12/25)(2+\epsilon)+\delta\), up to \(o(1)\). Take \(\epsilon\) small enough that \(b_0<1\) and \(f_0+b_0/2<1\), possible since \(\delta<1/25\). The four-cycle-free bound is now \(p^{\max(b_0,f_0+b_0/2)+o(1)}\), absorbed into \(p^\kappa\) with a fixed \(\kappa<1\).

Process the actual edges in increasing rank order. Retain an edge if adding it leaves the retained graph four-cycle-free. Otherwise discard it and record a four-cycle formed with three previously retained edges. The final retained graph is four-cycle-free and obeys the preceding size bound; retained edges are never removed. The product modulus has exponent \(3+2\epsilon+o(1)>3\), giving exact integral corner balances, and the past modulus has exponent \(2+\epsilon+o(1)>2\), eliminating the small-area case. The signed cross difference of the four ranks is a negative integer in the orientation of the rank-log formula. It is also divisible by \(D\) because the past vertices pair ranks equal modulo \(D\). It has absolute value at least \(D\). In this physical range the logarithm in the rank-log formula has absolute value at most a constant times \(AB/s^2\); also \(p^2/s=o(1)\). This gives the displayed area bound. The discarded-edge relations are independent, as each has its own discarded rank and three retained ranks. The argument gives neither a prescribed rectangle containing the minimum nor a physical smaller-source comparison along its sides.

The same near-critical lengths give a packing with a repeated **single exact gap** in each family. Fix also \(\tau>0\) with \(\tau+\delta<2/25\). Choose \(\epsilon>0\) and then \(\eta>0\) small enough that \(b_0<1-\eta\) and \(2(1-\eta)-b_0-2f_0>\tau\). Suppose the remaining graph has \(e>p^{1-\eta}\) edges. The sum of common-past-neighbor counts over distinct unordered pairs of future vertices is at least \((e^2/b-e)/2\). Dividing by \(\binom f2\) gives two future vertices with at least \(t=\lfloor p^\tau\rfloor\) common past vertices, for sufficiently large \(p\). Remove the corresponding \(2t\) edges and repeat. All but at most \(p^{1-\eta}\) original ranks have thus been partitioned into families with disjoint sets of source labels. A direct four-edge removal likewise gives a disjoint four-rectangle packing covering all but a sublinear number of ranks.

Within each such family order the two future classes so the corresponding central states are \((y_i,y_i+B)\) with \(B>0\). Their difference is identical for every one of the \(t\) past vertices, because each pair of past vertices gives a four-cycle with zero signed sum. All \(y_i\) are in one future class, all \(y_i+B\) in the other, and \(N\mid B\). In increasing order of \(y_i\), the positive integers \(r(y_i+B)-r(y_i)\) are strictly decreasing multiples of \(D\). For the extreme two anchors their difference is at least \((t-1)D\). The rank-log formula consequently gives
\[
               B(y_t-y_1)\gg (t-1)D\,s^2/p,\qquad B\gg (t-1)D\,s/p.
\]
Every pair of distinct anchors gives the same bilateral synchronous identity as above. Different families may have different gaps. These restrictions leave possible large gaps and do not force a smaller bad phase.
