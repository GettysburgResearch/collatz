# An absolutely summable signed current on the physical Collatz graph

**Status.** Proposed deduction from the source-qualified ordinary density and packing inputs below. The conclusion is a spatial conservation law with an absolutely convergent defect. Its value is undetermined.

Use the positive shortcut graph, with \(T(2r)=r\), \(T(2r+1)=3r+2\). Write \(c(x)=1\) at even \(x\) and \(c(x)=3x/(3x+1)\) at odd \(x\). The unweighted and weighted forms of the result are obtained by choosing respectively \(s(x)\equiv1\) and \(s(x)=c(x)\).

For a starting integer \(q\) and target \(v\), let \(w_v(q)\) be zero if \(q\) never hits \(v\), and otherwise the product of \(s(x)\) along the path **before its first hit**. The empty product is one. Put
\[
 f_Y(v)=Y^{-1}\sum_{1\le q\le Y}w_v(q),\qquad f(v)=\lim_{Y\to\infty}f_Y(v).
\]
In the unweighted case \(f(v)=d_v\) is ordinary shortcut predecessor density. In the weighted case \(f(v)=D_v\) is Valbuena's weighted first-hit density. Both concern all positive integers, including even targets and cycle vertices. The source gives these fixed-target limits. For a merge component \(C\), write \(m_C\) for its natural density. In an escaping component put
\[
 b'_C=\lim_j f(T^j a),\qquad a\in C .
\]
In the unweighted case \(b'_C=m_C\). In the weighted case \(c_*b'_C=b_C\) in the notation of the odd-map [first-hit spectrum](FIRST_HIT_SPECTRUM.md), where \(c_*=\log(4/3)/2\).

### The current

For each real \(p>1\), define
\[
 \Delta_f(v)=f(v)^p-\sum_{Tx=v}f(x)^p .
\]
The fiber has at most two elements. With \(\Delta_{f_Y}\) defined identically,
\[
 \Delta_f\in\ell^1(\mathbb N_{>0}),\qquad
 \|\Delta_{f_Y}-\Delta_f\|_1\longrightarrow0,\qquad
 \sum_v\Delta_f(v)=\sum_{C\ {\rm escaping}}(b'_C)^p.             \tag{1}
\]
Define, for any nonnegative label \(g\),
\[
 J_p(X;g)=
 \sum_{\substack{(2X-1)/3<n\le X\\n\ {\rm odd}}}g(n)^p
 -
 \sum_{\substack{X<n\le2X\\n\ {\rm even}}}g(n)^p .
\]
These are precisely the edges exiting and entering \([1,X]\). Internal edges cancel, giving \(J_p(X;g)=\sum_{v\le X}\Delta_g(v)\) without any density assumption. Consequently, for arbitrary integer cutoffs \(X,Y\to\infty\),
\[
 J_p(X;f_Y)\longrightarrow\sum_{C\ {\rm escaping}}(b'_C)^p.    \tag{2}
\]
Either cutoff can instead be sent to infinity first. The empirical label uses complete future visits of the first \(Y\) ordinary starts. It need not be computed by a time-\(Y\) simulation. Formula (1) is stronger than pointwise convergence of its infinitely many summands.

### Inputs and the two boundaries of a tree

We use Valbuena, *Collatz basin densities and canonical traces from first-passage stabilization*, source commit [a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex), propositions labeled **ct-basin-boundary**, **ct-forward-components**, and theorem **ct-natural-density-upgrade**. Specifically:

- Fixed \(d_v,D_v\) exist. The laws of the component and global orbit minimum under the uniform start \(q\le Y\) converge in total variation. Their limiting probabilities have total mass one.
- For each fixed root \(a\), \(d_v\to0\) as \(v\to\infty\) among its predecessors. On an escaping forward ray \(a_j\), \(d_{a_j}\to m_C\) and \(D_{a_j}\) has the stated weighted limit. The source's inverse-linear floor makes this limit positive on every escaping component.
- A finite simple trajectory has a uniform bound \(\sum_{x\ {\rm odd},\,x>H}x^{-1}\le K H^{-1/40}\), where its distinct odd states are counted only once. The resident [finite packing proof](../../astra-three-routes/pass3/FINITE_RECORDS.md) proves this by integrating the uniform count of states below a variable bound, with the lower integration limit \(H\). This remains true for the complete distinct value set of an arbitrary trajectory: truncate an escaping path or use the segment before the first repetition of an eventually periodic path.

The cited density chain uses earlier work of Tao, Mazur and others. Its primary text was inspected, and its external analytic and Lean dependencies were not independently rebuilt for this result.

Write \(B(a)=\{q:q\text{ hits }a\}\). A nonperiodic root has an ordinary rooted predecessor tree. Its first-hit layer \(L_k(a)\) is finite, and its unweighted basins are disjoint within each layer. For the limiting density,
\[
 \sum_{x\in L_k(a)}d_x\le d_a,\qquad
 \max_{x\in L_k(a)}d_x\to0.
\]
The second assertion follows from the fixed-root boundary bound, since finitely many fixed integers can occur in only finitely many layers. Thus \(\sum_{L_k(a)} f(x)^p\to0\) for \(p>1\). For a fixed finite source law, sufficiently deep layers have zero empirical mass: among the finitely many starts that hit \(a\), take the largest of their finite first-hit depths.

On an escaping component define \(W(q)=\prod_{j\ge0}s(T^j q)\). Reciprocal packing makes this product positive and gives \(W(a_j)\to1\). For an empirical law let \(b'_{C,Y}=Y^{-1}\sum_{q\le Y,\,q\in C}W(q)\). Along the ray, \(f_Y(a_j)\to b'_{C,Y}\), since every one of the finitely many sources in this component eventually reaches the ray. For each fixed \(C\),
\[
 b'_{C,Y}\to b'_C.                                             \tag{3}
\]
Indeed on \(B(a_j)\), \(W(q)=w_{a_j}(q)W(a_j)\). The error of replacing \(W\mathbf1_C\) by this truncated observable is bounded by \(\mathbf1_{C\setminus B(a_j)}\). Its empirical mean converges to \(m_C-d_{a_j}\), which tends to zero. Now take first \(Y\to\infty\), then \(j\to\infty\). In particular \(0\le b'_{C,Y}\le m_{C,Y}\), where \(m_{C,Y}\) is the empirical component mass.

### Nonperiodic vertices

For a nonperiodic \(v\), the predecessor basins are disjoint, and the source \(q=v\) is the only additional first visit. This gives
\[
 f_Y(v)=Y^{-1}\mathbf1_{v\le Y}+\sum_{Tx=v}s(x)f_Y(x),
 \qquad f(v)=\sum_{Tx=v}s(x)f(x).
\]
For either label \(g=f,f_Y\), split on these vertices
\[
 E_g(v)=g(v)^p-\sum_{Tx=v}s(x)^p g(x)^p\ge0,\qquad
 Q_g(v)=\sum_{Tx=v}(1-s(x)^p)g(x)^p\ge0,\qquad
 \Delta_g=E_g-Q_g .
\]
The first inequality follows from \((\sum t_i)^p\ge\sum t_i^p\) for nonnegative terms. The total damping \(Q_g\) is uniformly summable. In the weighted case \(1-c(x)^p\le p/(3x+1)\) at odd \(x\). Also \(f_Y(x)^p\le d_{x,Y}\), with \(d_{x,Y}\) the empirical unweighted hitting frequency. Integrating the orbitwise packing estimate over the finite source law therefore bounds all damping terms with predecessor \(x>H\) by \(Kp H^{-1/40}\), uniformly in \(Y\). The limiting bound follows by finite-subset limits. For bounded \(x\), use pointwise convergence. This proves \(\|Q_{f_Y}-Q_f\|_1\to0\), also after restricting to nonperiodic endpoints. The unweighted damping is zero.

Telescoping the raw \(\Delta_g\) over depths less than \(k\) in the inverse tree of a nonperiodic root \(a\) leaves \(g(a)^p-\sum_{L_k(a)}g(x)^p\). The layer bound and finite damping thus give
\[
 \sum_{v\in B(a)}E_g(v)=g(a)^p+\sum_{v\in B(a)}Q_g(v).          \tag{4}
\]
In an escaping component the nested \(B(a_j)\) exhaust the component. Apply monotone convergence separately to \(E_g,Q_g\) in (4). Its component excess is \((b'_C)^p\) for \(f\), or \((b'_{C,Y})^p\) for \(f_Y\).

### Cycles and absolute convergence

In a component \(C\) with cycle \(Z\), let \(I_C\) consist of all **noncycle** immediate predecessors of the cycle vertices. Their basins are disjoint and cover \(C\setminus Z\). Both the cycle and \(I_C\) are finite. Apply (4) to these roots. On the cycle itself, plain summation cancels the cyclic predecessor terms exactly, leaving
\[
 \sum_{v\in Z}\Delta_g(v)=-\sum_{x\in I_C}g(x)^p.                \tag{5}
\]
There is no net contribution from a periodic component.

Absolute convergence requires control independent of period length. Let \(z\) be the cyclic predecessor of \(v\) and \(\lambda=\prod_{u\in Z}s(u)\). Under a finite empirical source law, write \(A_v\) for the weighted mass of sources whose *first entrance to the cycle* is at \(v\), weighted up to that entrance. Thus \(\sum_{v\in Z}A_v\le m_{C,Y}\). Direct first-hit factorization gives
\[
 g(v)=s(z)g(z)+(1-\lambda)A_v\quad (g=f_Y).
\]
For entrants elsewhere, concatenation from \(z\) gives their first hit of \(v\). For entrants at \(v\), that concatenation adds a whole lap of multiplier \(\lambda\); the correction gives exactly their first-hit weight. This includes a one-vertex cycle. Since \(0\le g(v)\le m_{C,Y}\), the sum of positive differences \((g(v)^p-g(z)^p)_+\) around the cycle is at most \(p m_{C,Y}^p\). Their negative differences sum to the same magnitude. Disjointness gives \(\sum_{x\in I_C}g(x)^p\le m_{C,Y}^p\). Hence \(\sum_{v\in Z}|\Delta_g(v)|\le(2p+1)m_{C,Y}^p\). Fixed-component limits give the identical bound with \(m_C\) for \(g=f\). This step uses no bound on cycle periods or on \((1-\lambda)^{-1}\).

Summing (4) over the off-cycle vertices gives the total positive branching
\[
 \sum_{v\ \mathrm{nonperiodic}}E_g(v)
 =\sum_{v\ \mathrm{nonperiodic}}Q_g(v)
 +\sum_{C\,\mathrm{escaping}} b_C(g)^p
 +\sum_{C\,\mathrm{cyclic}}\sum_{x\in I_C}g(x)^p ,
\]
where \(b_C(g)\) denotes the appropriate empirical or limiting charge. The last two sums together are at most one. The total therefore converges as \(Y\to\infty\) to the corresponding total for \(f\): use damping convergence, (3), pointwise convergence on the finite roots of each cycle, and total-variation tightness of the component masses to discard all but finitely many components. Since \(E_{f_Y}\ge0\) and converges pointwise, convergence of its sums implies convergence in \(\ell^1\) (truncate to a finite set or use the discrete Scheffé lemma). Together with damping this proves \(\ell^1\) convergence of the off-cycle divergences. For all cycle vertices use the displayed variation bound and the same finite-component truncation. Equations (4) and (5) now prove (1), with absolute convergence justifying every regrouping.

### The endpoint and the missing estimate

For **unweighted** densities at \(p=1\), \(\Delta_d(v)=0\) off cycles. On a cycle the value is minus the total density of its noncycle immediate predecessors, since the cyclic predecessor and the target both have basin \(C\). The side basins cover \(C\) apart from its finite cycle. Thus
\[
 \lim_{X\to\infty}J_1(X;d)=-\sum_{C\,\mathrm{cyclic}}m_C,
 \qquad
 \lim_{p\downarrow1}\lim_{X\to\infty}J_p(X;d)=\sum_{C\,\mathrm{escaping}}m_C .
\]
The difference is exactly one. The limit in \(p\) follows by dominated convergence of component masses. This excludes continuity at \(p=1\) as a route to an upper bound.

A sufficient remaining arithmetic inequality is \(\liminf_{X\to\infty}J_p(X;D)\le0\) for any one \(p>1\). The proof supplies its nonnegative limit and no such upper bound. The linear first-passage approximation alone cannot control the signed annular powers. The [binary model](ENTRANCE_AND_INDEX.md) has one escaping component, exceptionally accurate uniform source approximations, and positive nonlinear current for its own map. Finite cyclic components disappear from (1), including hypothetical nontrivial positive cycles.
