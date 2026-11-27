# Where the two-word collision energy is created

Write \(U(x)=(3x+1)/2^{e(x)}\) on the positive odd integers, \(w_x=3x/(3x+1)\), and \(\Omega\) for the set of all nonperiodic positive odd vertices. This includes transient vertices of eventually periodic trajectories. Write \(\rho_k\) for the original whole-Haar Syracuse density and \(L_k\) for the ordinary first-hit weight. On \(\Omega\), set \(u_k(y)=L_k(y)/y=\rho_k(y)/y\). Define the following explicit source on \(\Omega\), counting **ordered** pairs:
\[
 b(y)=\sum_{\substack{Ui=Uj=y\\i\ne j}}
                 w_i w_j\,\frac{h(i)}i\,\frac{h(j)}j ,
 \qquad h(i)=\lim_{k\to\infty}\rho_k(i).
\]
The fixed-integer ordinary limit is Weaver's Theorem 2. The source is summable and strictly positive at every odd ternary unit in \(\Omega\). With \(f_\infty(y)=\prod_{j\ge0}w_{U^jy}\), the normalized energy satisfies
\[
 \lim_{k\to\infty}\frac1k
   \sum_{\substack{y\in\Omega\\y<2\cdot3^k}}u_k(y)^2
 =\sum_{\substack{y\in\Omega\\ y\ {\rm escapes}}} b(y) f_\infty(y)^2 .
 \tag{1}
\]
The same identity holds with the sum on the left taken over all \(\Omega\). Thus the coefficient has a representation by actual births of pairs at specific finite positive roots. Every escaping unit contributes strictly positive mass. The [component-energy theorem](../global/COLLISION_ENERGY.md) identifies the sum as \(\sum_C H_C^2\) and covers the original first-hit sum including periodic targets. [Weaver, fixed-integer depth limit](https://rstation.ai/problems/collatz/papers/176/v1)

## The transfer with two copies

For \(p\in\ell^1(\Omega)\) define \(Ap(y)=\sum_{Ux=y}w_x^2p(x)\). This positive contraction discards mass on first entry to a periodic vertex. All ordinary ancestors of \(y\in\Omega\) lie in \(\Omega\). Since \(3\cdot2^{-e(x)}/y=w_x/x\) when \(Ux=y\), the single-copy transfer is \(u_{k+1}(y)=\sum_{Ux=y}w_xu_k(x)\). Squaring gives the exact identity
\[
 u_{k+1}^2=A(u_k^2)+b_k,\qquad
 b_k(y)=\sum_{\substack{Ui=Uj=y\\i\ne j}}
                           w_iw_j u_k(i)u_k(j).                       \tag{2}
\]
Start (2) at \(k=1\). The first ternary period has \(\rho_1\le2\), so \(u_1^2\in\ell^1(\Omega)\). This avoids using a positive predecessor-density floor at zero depth for multiples of three.

Let \(d_i\) be the relative odd natural density of positive starts visiting \(i\). For \(k\ge1\), the uniform first-hit input gives \(u_k(i)\le C d_i\) on \(\Omega\). At multiples of three both sides vanish. Across all ordered sibling pairs in (2),
\[
                    \sum_{y\in\Omega}\sum_{Ui=Uj=y,\ i\ne j}d_i d_j\le1.
                    \tag{3}
\]
Indeed, choose ordered positive odd starts independently in a common growing interval. If the first trajectory visits \(i\) and the second visits \(j\), their two forward trajectories join at \(y\) through distinct last edges. Once they meet they have the same forward path. Two such ordered pairs on the same two trajectories would require another first meeting, which is impossible on their common nonperiodic prefix. Equivalently, two distinct ancestors at the same distance on the two arms before \(y\) have disjoint predecessor sets, and their common suffix admits no further distinct entrance edges. For any finite selection of the ordered pairs, the associated product events are pairwise disjoint. Take the sampling limit for that finite selection and then the supremum. This proves (3) without countable additivity of natural density. [Weaver, first-hit layer and predecessor inputs](https://rstation.ai/problems/collatz/papers/12) · [Pinned formulas and quantifiers](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md)

The fixed-target limit and (3) give \(\|b_k-b\|_1\to0\) by dominated convergence on the countable ordered pairs. To see strict positivity at a nonperiodic unit \(y\), its odd parents \((2^e y-1)/3\) have \(e\ge1\) in the pertinent parity class. Increasing \(e\) by two sends a parent \(x\) to \(4x+1\), so infinitely many of these parents are ternary units. Their individual traces are strictly positive by the ordinary unit atom floor. This gives a positive term in \(b(y)\). [Original atom-floor input](../global/POSTERIOR.md)

The iterated positive identity, summed over \(\Omega\), now reads
\[
 \sum_\Omega u_k^2=\|A^{k-1}u_1^2\|_1+
                         \sum_{i=1}^{k-1}\|A^{k-1-i}b_i\|_1 .
\]
After division by \(k\) the initial term vanishes. Replacing all \(b_i\) by \(b\) costs at most \(k^{-1}\sum_{i<k}\|b_i-b\|_1=o(1)\). For a point mass at an escaping \(y\) its mass after \(r\) iterations is \(\prod_{j<r}w_{U^jy}^2\). For \(y\) eventually reaching a periodic site, it eventually vanishes. Dominated convergence and Cesàro averaging yield (1) over all \(\Omega\). The product is strictly positive on every injective ordinary path by the uniform simple-path reciprocal bound. [Interval compression and reciprocal bound](../../astra-multiple-attacks-20261125/synthesis/README.md)

For the passage to the finite residue period put \(q=3^k\) and \(1\le r<2q\) odd. Periodicity gives
\[
 \sum_{\substack{y\ge2q\\y\ {\rm odd}}}
       \left(\frac{\rho_k(y)}y\right)^2
 \le \sum_r \rho_k(r)^2\sum_{j\ge1}(2jq)^{-2}
 =\frac{\zeta(2)}{4q^2}\sum_r\rho_k(r)^2.
\]
Elementary probability normalization gives \(\sum_r\rho_k(r)^2\le(\sum_r\rho_k(r))^2=q^2\). The discarded energy is at most \(\zeta(2)/4\) at every depth, enough for (1). The finite whole-Haar second moment gives the stronger \(O((k+1)/q)\) by \(\sum_r\rho_k(r)^2=q\int\rho_k^2\,dm_3\ll q(k+1)\). Both estimates apply on any subset of positive sites and to first-hit weights by domination. [Weaver, finite Haar second moment, Corollary (2a)](https://rstation.ai/problems/collatz/papers/146/v1)

## Restoring the periodic targets in the first-hit sum

Formula (1) also holds with \(L_k(y)/y\) summed over **all** odd targets. Here is a direct verification independent of a global first-moment estimate. For a periodic odd orbit \(B\), let \(l=|B|\), let \(d_B\) be the relative odd density of its basin, and set \(R_B=\sum_{z\in B}1/z\). Uniformly in \(B\), \(R_B=O(1)\). Indeed its full shortcut cycle is injective at every common clock, so interval compression bounds \(\#(B\cap[1,X])\ll X^\theta\) with \(\theta<1\), and a dyadic sum gives the assertion. [Uniform cycle compression](../../astra-multiple-attacks-20261125/synthesis/README.md)

Write \(g_k(y)=L_k(y)/y\) at all odd sites. For \(k\ge1\),
\[
               \sum_{y\in B}g_k(y)\le C\min(k,l)d_B+4R_B.             \tag{6}
\]
A first-hit path starting on \(B\) makes fewer than \(l\) cyclic steps and contributes at most \(1/x\) for its initial phase \(x\), giving at most \(R_B\) across targets. Every other path arrives from a last off-cycle parent \(p\), enters at \(z=Up\), and takes \(0\le j<l\) more cyclic steps to its first visit to \(y\). Its pre-parent time is \(t=k-1-j\). For \(t\ge1\) the total from that parent is at most \(w_p g_t(p)\le C d_p\). Over all phases \(z\) and their off-cycle parents the basins of \(p\) are pairwise disjoint, since each such visit is immediately followed by the first entry to \(B\). Thus their densities sum to at most \(d_B\), for each of at most \(\min(k,l)\) choices of \(j\). When \(t=0\) only \(j=k-1\) is possible, and \(\sum_{Up=z} w_p/p=\sum_e 3\cdot2^{-e}/z\le3/z\). Summing this over phases proves (6), including nonunit off-cycle starts.

The first-hit cap \(g_k(y)\le C d_B\) on \(B\) and (6) give
\[
 \frac1k\sum_{y\in B}g_k(y)^2\le C^2d_B^2+4C d_B R_B/k .
\]
For each fixed finite cycle the left side tends to zero by the same cap. The basins of distinct cycles are disjoint, so finite additivity gives \(\sum_B d_B\le1\). The uniform bound on \(R_B\) now allows dominated convergence over every positive cycle, showing that all periodic first-hit sites together contribute \(o(k)\). This conclusion also holds after intersecting with the single-period cutoff. Together with (1) and its elementary cutoff bound, this proves the full first-hit escape detector without a harmonic first-moment or Haar second-moment estimate. The interval-compression, first-hit, fixed-target trace, and atom-floor inputs still apply.

There is a consequence computable from the raw finite ternary law without classifying any orbit. For \(\Phi(u)=u^2/(1+u)\), \(0\le g_k\le C\) gives \(g_k^2/(1+C)\le\Phi(g_k)\le g_k^2\). Write \(v_k(y)=\rho_k(y)/y\) on all positive odd sites. On a cycle of length \(l\) and lap survival \(w_B<1\), repeated visits give \(v_k(y)-g_k(y)=\sum_{j=1}^{\lfloor k/l\rfloor}w_B^j g_{k-jl}(y)\). Here the zero-depth unit cap \(1/y\le C d_B\) follows from the unit predecessor floor. The total discrepancy from \(B\), even across all its phases, is bounded by \(Ck d_B\) and by \(C l d_B w_B/(1-w_B)\). Off the cycles it vanishes. Dividing by \(k\), use \(\sum_B d_B\le1\) and dominated convergence. Because \(\Phi\) is increasing and 1-Lipschitz, replacing \(g_k\) by \(v_k\) in its clipped sum costs \(o(k)\). Consequently the finite single-period sum of \(\Phi(\rho_k(y)/y)\) is \(o(k)\) exactly when there is no ordinary escape. An escape gives a normalized liminf at least \(\sum_{\rm escape}b(y)f_\infty(y)^2/(1+C)>0\). This argument uses (1) and (6), independently of the moving-target profile and the harmonic first-moment or minimum laws. [Repeated-lap proof and full clipped limit, equations (8)–(10)](../global/COLLISION_ENERGY.md)

## The squared flux across a grade

On an escaping component use the signed grade \(g\), corrected height \(P=x/f_\infty(x)\), and \(H_C\) from the [ordinary moving-target theorem](TRACE_PROFILE.md). Put \(M_x=h(x)/P(x)\). Then \(\sum_{Ux=y}M_x=M_y\). This follows either from the stopped-location formula (6) of the [component-energy theorem](../global/COLLISION_ENERGY.md), or by passing to the fixed-depth limit in the ordinary recursion using the summable predecessor bound on the parent antichain. For \(Ui=Uj=y\) we have
\[
                   f_\infty(y)^2w_iw_j\,h(i)h(j)/(ij)=M_iM_j.
\]
Every grade has total mass \(H_C\). For fixed \(v\) and \(n\ge\max(v,0)\), put \(t=n-v\). The ordinary telescope over \(U^t x=a_n\) gives
\[
 \frac{\rho_{j+t}(a_n)}{P(a_n)}
       =\sum_{U^t x=a_n}\frac{\rho_j(x)}{P(x)} .
\]
Here \(j\ge1\) and each summand is at most \(C d_x\) by the first-hit bound. The roots on that grade form an antichain with \(\sum d_x\le1\). Send \(j\to\infty\) and then \(n\to\infty\). The increasing sets of roots exhaust grade \(v\), and \(M_{a_n}\to H_C\).

Write \(Q_v=\sum_{g(x)=v}M_x^2\). At \(v\to+\infty\), \(M_{a_v}\to H_C\) while the remaining mass tends to zero, so \(Q_v\to H_C^2\). At \(v\to-\infty\), the forward orbits of all starts through any fixed \(R\) miss the entire grade once \(v\) is small enough. Indeed those in \(C\) have grades bounded below and all other components are disjoint. The uniform first-hit estimate (5) of [the moving-target theorem](TRACE_PROFILE.md) gives \(\sup_{g(x)=v}M_x\ll R^{-\delta}\). Increasing \(R\) proves \(Q_v\to0\). Consequently
\[
 Q_{v+1}-Q_v=\sum_{g(y)=v+1}\sum_{Ui=Uj=y,\ i\ne j} M_iM_j,\qquad
 \sum_{y\in C} b(y)f_\infty(y)^2=H_C^2.                    \tag{4}
\]
Each ordered pair contributing to (4) has a unique ordinary merger. Formula (4) explains why a uniform estimate for the repeated *single* inverse word controls only the homogeneous term of (2). The sibling terms are positive, summable across their birth locations, and keep contributing at later times whenever their common positive forward trajectory survives. A cancellation bound for (2), or a claim that all finite-root births have vanishing survival, cannot be obtained from the diagonal word estimate. An independent reason forcing the right side of (1) to vanish remains open.

## The mean-zero dyadic test and a coboundary obstruction on paths reaching one

Let
\[
 W(x)=\tfrac34-\mathbf1_{e(x)\ge2}-\mathbf1_{e(x)\ge3}.
\]
This has mean zero on odd residues modulo eight. Every actual escape has \(\liminf_{s\to\infty}s^{-1}\sum_{j<s}W(U^jx)\ge\gamma\), where \(\gamma=7/4-\log_2 3>0\). Indeed \(W\ge7/4-e\) and the corrected-height telescope gives \(\sum_{j<s}e(U^jx)\le s\log_2 3+O_x(1)\). This is the [global signed test](../global/COLLISION_ENERGY.md).

For any bounded test \(V\), the transfer proof of (1) gives the signed identity
\[
 \frac1k\sum_{y\in\Omega}V(y)u_k(y)^2
 =
 \sum_{y\in\Omega} b(y)\,\frac1k\sum_{j=0}^{k-1}
        \mathbf1_{U^jy\in\Omega}
        \left(\prod_{i<j}w_{U^iy}^2\right)V(U^jy)+o(1).
 \tag{5}
\]
The error is uniform over \(\|V\|_\infty\le1\), including depth-dependent tests, by \(\|b_i-b\|_1\to0\) and contraction. Equivalently \(\|k^{-1}u_k^2-k^{-1}\sum_{j<k}A^jb\|_1\to0\). The periodic sites, once entered, cannot be left. With \(V=W\), every transient eventually killed has inner mean tending to zero. On each escaping trajectory the product in (5) can be replaced by \(f_\infty(y)^2\) with vanishing average error. Fatou after adding a fixed bound therefore gives a signed liminf at least \(\gamma\sum_{\rm escape}b(y)f_\infty(y)^2\). For a zero upper bound one needs a cancellation estimate on the source-weighted distribution of the actual ordinary forward clocks.

There is a direct finite test of a proposed upper coboundary \(W(x)\le G(x)-w_x^2G(Ux)\). Every finite choice of positive exponents \(e_1,\ldots,e_s\) has arbitrarily large genuine positive odd realizations which reach \(1\) at their very next step after this word. Indeed the inverse word imposes one terminal residue \(r\bmod3^s\). Choose
\[
        y_s=(4^t-1)/3,\qquad 4^t\equiv1+3r\pmod{3^{s+1}} .
\]
Such \(t\) are unbounded since \(4\) generates \(1+3\mathbb Z/3^{s+1}\mathbb Z\), as follows from \(v_3(4^{3^j}-1)=j+1\). The inverse word lifts \(y_s\) to odd integers at every step, positive for all sufficiently large \(t\), and \(U(y_s)=1\). All its pre-terminal vertices are then in \(\Omega\). The inverse congruence also follows inductively by writing the last inverse as \((2^{e_s}y_s-1)/3\) and lifting its required class by one further power of three.

Set \(S_j=\lfloor j\log_2 3\rfloor\), \(e_j=S_j-S_{j-1}\). These exponents lie in \(\{1,2\}\) and
\[
 \sum_{i<s}W(y_i)=7s/4-S_s\ge\gamma s,\qquad
 y_j=(3^j/2^{S_j})y_0+O_s(1),\qquad 1\le3^j/2^{S_j}<2.
\]
In fact \(y_s\ge y_0\) by positivity of the affine intercept. First make \(s\) large, then choose the realization so high that all partial survival products are arbitrarily close to one. Its survival-weighted signed sum can be made at least \(\gamma s-o(1)\), while the endpoints stay in the same factor-three interval. Its next step arrives at \(1\).

In particular the upper coboundary fails **even on trajectories known to reach one** for every bounded \(G\), and for \(G(x)=c\log x+O(1)\) with any real \(c\). The endpoint logarithms differ by \(O(1)\), and the survival discount contributes \(O_s(\log y_0/y_0)=o(1)\). More generally it fails for \(G(x)=F(x)+O(1)\) with any eventually nondecreasing \(F(x)=o(x)\). In this case \(F(y_0)-F(y_s)\le0\) and the discount contributes at most \(O_s(|F(y_s)|/y_0)=o(1)\). Telescoping the alleged coboundary along the word would bound the signed sum by a universal constant, contradicting arbitrarily large \(s\). This family tests real height, ordinary positivity, and exact convergence of the chosen starts simultaneously. Its roots can grow extremely rapidly with \(s\); the construction yields no positive asymptotic probability of these words under the summable source \(b\).

## The full operator spectrum already occurs inside the basin of one

Let \(B=\{x>1:\text{\(x\) odd and }U^n x=1\text{ for some }n\}\). Fix any complex \(t\). On \(\ell^1(B;\mathbb C)\) send \(\delta_x\) to \(w_x^2 e^{t W(x)}\delta_{Ux}\) if \(Ux\in B\), and to zero at the entrance to one. Write \(A_t\) for this operator and
\[
 R(t)=\exp\big(\max\{(3/4)\Re t,-(5/4)\Re t\}\big).
\]
Its approximate point spectrum and its spectrum both equal the entire closed disk \(\{|\lambda|\le R(t)\}\). The same conclusions hold on \(\ell^1(\Omega;\mathbb C)\) with killing at every periodic vertex. In particular every pure Fourier twist has the full closed unit disk already on the explicitly convergent basin.

The upper bound \(\|A_t\|\le R(t)\) follows from the range of \(W\). Choose \(e=1\) or \(3\) so that \(W=\omega\) at this exponent maximizes \(\Re(t)\omega\), and set \(d=e^{t\omega}\). Realize a constant-\(e\) word of length \(s\) ending at a parent \(y_s\) of \(1\) by the preceding construction. Its distinct vertices \(y_0,\ldots,y_s\) can all be made arbitrarily large for each \(s\). On their signed measures \(A_t\) is within \(R(t)\max_{j<s}|1-w_{y_j}^2|\) in operator norm of the finite shift \(D\delta_{y_j}=d\delta_{y_{j+1}}\) for \(j<s\), \(D\delta_{y_s}=0\). Choose the word realization so this difference tends to zero with \(s\). For \(|\lambda|\le|d|\) set
\[
 v_s=\sum_{j=0}^s (\lambda/d)^{s-j}\delta_{y_j}.
\]
Then \((D-\lambda)v_s=-\lambda(\lambda/d)^s\delta_{y_0}\). After division by \(\|v_s\|_1\) the residual tends to zero, geometrically in the disk interior and with order \(1/(s+1)\) on the boundary. At \(\lambda=0\) use \(v_s=\delta_{y_s}\). This proves the assertion. Thus uniform norm estimates or a spectral gap on this space cannot distinguish surviving ordinary components. An estimate for the particular source in (5) would be a different statement.

For purely imaginary \(t\), the same operators on \(\ell^1(B)\) nevertheless satisfy \(\|A_t^n p\|_1\to0\) for every fixed \(p\): each point mass is eventually killed, and finite support approximation uses \(\|A_t^n\|\le1\). The explicitly convergent basin exhibits both properties simultaneously.
