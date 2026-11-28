# The collision-energy slope on actual positive targets

Use the accelerated odd map \(U\), \(w(x)=3x/(3x+1)\), \(W_n(x)=\prod_{i<n}w(U^ix)\), and \(F(x)=\lim W_n(x)\). Let \(\rho_n\) be the ordinary fair ternary quotient density. On residues \(0,1,2\bmod3\), \(\rho_1\) takes values \(0,1,2\). Put \(b(x)=\rho_1(x)/x\) on the positive odd integers. For \(n\ge0\) define the finite-clock simple-arrival row and its ordinary energy by
\[
 s_n(y)=\sum_{\substack{U^nx=y\\x,Ux,\ldots,U^nx\ {\rm distinct}}}
               W_n(x)b(x),\qquad \mathscr S_n=\sum_{y>0\ {\rm odd}} s_n(y)^2.
\]
Distinctness requires only the displayed finite path. For a deterministic trajectory this is equivalently first arrival at its terminal \(y\). The one-step base \(b\) absorbs the nonunit initial leaves while remaining bounded by a fixed multiple of predecessor density.

**Source-qualified theorem.** Let \(H_C\) be the physical reciprocal flux of an escaping ordinary component \(C\), in the normalization \(a_y=h(y)/y,\ h(y)=\lim_n\rho_n(y)\). Then
\[
               \lim_{n\to\infty}\mathscr S_n/n
                         =\sum_{C\ {\rm escaping}} H_C^2.            \tag{1}
\]
In particular the slope is zero exactly when every positive orbit is bounded. Possible additional ordinary cycles, even infinitely many of unbounded periods, give no slope in this finite first-arrival statistic. The Haar collision-energy slope in [the independent fair-word theorem](../phase9/EXACT_COLLISION_ENERGY_SLOPE.md) is instead the unconditional positive constant \(2\kappa\mu\). Formula (1) evaluates the ordinary energy; no estimate here forces its right hand side to vanish.

Let \(d_y\) be the natural relative-odd density of the predecessor basin of \(y\), zero at a multiple of three. Such a nonunit has no odd predecessor apart from its occurrence as an initial source at depth zero. We use the published uniform positive floor \(d_y\gg1/y\) for units, and the cited ordinary-depth equilibrium. In particular \(0\le b(y)\le C d_y\). The physical grade flux formula below follows directly from the fixed-root equilibrium and the qualitative predecessor-minimum bound. [Uniform predecessor lower bound, Wren 10/v3, Theorem 1](https://rstation.ai/problems/collatz/papers/10/v3) · [Ordinary-depth equilibrium at a fixed target, PR193](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md) · [Component flux and its grade marginals, pinned PR212](https://github.com/GettysburgResearch/collatz/blob/e55fb7cac646013f143b563014ae97b105bc7547/research/astra-global-20261128/escape/SPATIAL_TRACE_TAIL.md)

## A summable source of distinct-parent collisions

For a nonperiodic \(y\), all arriving paths have distinct vertices. The exact positive-word trace and \(3^n/2^{S_n}=yW_n(x)/x\) give
\[
              s_n(y)=\rho_{n+1}(y)/y\longrightarrow a_y .
\]
Indeed the extra innermost letter contributes its full \(\rho_1(x)\). Also \(s_n(y)\le C d_y\) at every \(n\). The distinct depth-\(n\) predecessors of a nonperiodic target have pairwise disjoint predecessor basins: if two were comparable, equal hitting depths would force periodicity of \(y\). Their union lies in the basin of \(y\), so finite additivity of natural density followed by supremum bounds the sum of their \(d_x\) by \(d_y\). This bound needs no countable-additivity assumption on natural density.

On the nonperiodic sites let \(P\) act on summable masses by pushing each \(x\) to \(Ux\) with multiplier \(w(x)^2\), killing a path that enters a cycle. It is a positive \(\ell^1\)-contraction. Let \(\pi_n(y)=s_n(y)^2\) on this space and define the ordered distinct-parent injection
\[
     \gamma_n(y)=\sum_{\substack{Ux=Ux'=y\\x\ne x'}}
                           w(x)w(x')s_n(x)s_n(x').
\]
For nonperiodic \(y\) its parents are nonperiodic. Squaring the exact row recursion gives \(\pi_{n+1}=P\pi_n+\gamma_n\). Here \(\pi_0\) is summable since \(b(x)\le2/x\).

On the countable space of ordered triples \(x\ne x'\), \(Ux=Ux'=y\) nonperiodic, the sum of \(d_xd_{x'}\) is at most one. To see this for any finite subcollection, use two independent uniform positive odd sources through a growing cutoff. Ordered membership in the two indicated predecessor basins has limiting probability \(d_xd_{x'}\). Such events are disjoint across the triples: if both sources visit different parents of \(y\), their paths first have a common vertex at \(y\). A previous common vertex would force the two parents to be comparable, impossible at a nonperiodic target. After joining at \(y\), the paths cannot come through different parents of another nonperiodic target. Within one \(y\), the predecessor cones of distinct parents are disjoint. Pass to the supremum of finite subcollections. Consequently dominated convergence on this countable triple space gives \(\gamma_n\to\gamma\) in \(\ell^1\), where \(\gamma\) is the same formula with \(a_x,a_{x'}\). All finite energies on the nonperiodic sites are therefore finite.

Iterate the recursion and divide total mass by \(n\). By contraction, replacing every \(\gamma_j\) in the expansion by \(\gamma\) changes the average by at most \(n^{-1}\sum_{j<n}\|\gamma_j-\gamma\|_1\to0\). The initial term contributes at most \(\|\pi_0\|_1/n\). For each fixed starting site \(y\), the remaining mass of \(P^k\delta_y\) is \(W_k(y)^2\) if its first \(k\) steps avoid a cycle and zero once a cycle is reached. This converges to \(F(y)^2\) on escape and to zero elsewhere. Thus
\[
   \frac1n\sum_{y\ {\rm nonperiodic}}\pi_n(y)
         \longrightarrow \sum_{y\ {\rm escaping}} F(y)^2\gamma(y).  \tag{2}
\]
The survival product \(F(y)\) is strictly positive on simple escaping paths by uniform orbit-set sparsity. If there is an escape, some escaping unit \(y\) has two distinct unit parents (two suitable exponents among the first six), both in the same component and of positive \(a_x\) by the fixed-target floor. Thus (2) is positive even without invoking the explicit flux formula.

## Cyclic outputs and the first-arrival restriction

Fix one cycle of odd period \(q\), and let \(d_C\) be its ordinary basin density. For a site \(z\) on it, put \(e_z=\sum_{u\ {\rm nonperiodic},\ Uu=z}d_u\). The corresponding first-entry cones are disjoint across all such \(u,z\), so \(\sum_{z\in C}e_z\le d_C\). For each fixed \(k\ge1\), the incoming weighted row from sources that first enter this cycle at \(z\) after exactly \(k\) steps is at most \(C e_z\). Group by penultimate parent \(u\) and use the nonperiodic row bound above and \(w(u)\le1\).

A noncyclic source contributing at cycle destination \(y\) thus first enters at \(z=U^{-j}_C y\) for a unique \(0\le j<\min(q,n)\); the other \(n-j\) ticks precede and include that first entry. The strict \(j<q\) here is just the finite distinctness condition. The total of these contributions at any \(y\) is at most \(Cd_C\). Summing them over \(y\) on this cycle gives at most \(C\min(q,n)d_C\), since each first-entry site is counted at most \(\min(q,n)\) times and all later weights are at most one. Their energy is at most \(C^2\min(q,n)d_C^2\). The cycle basins are disjoint, so \(\sum_C d_C^2\le1\). Dominated convergence gives \(o(n)\) for this part of the total cyclic energy even across unbounded periods. Sources initially on cycles contribute a row of squared norm at most \(\sum_x b(x)^2\): their unweighted transitions are permutations on each cycle, and all survival factors and simple-path indicators are at most one. The \(\ell^2\) triangle inequality now gives \(o(n)\) for the entire cyclic energy, with no restriction on the number of cycles.

## Identifying the square of the escape flux

In an escaping component use the integer odd grade increasing by one along each edge and the row \(m_y=F(y)a_y\). Pass to the limit in the nonperiodic row recursion using the summable parent majorant \(C d_x\); this gives \(a_y=\sum_{Ux=y}w(x)a_x\). Thus \(m_y=\sum_{Ux=y}m_x\) since \(F(x)=w(x)F(y)\). Along a supplied forward ray the \(m_y\) increase to a finite positive limit \(H_C\), since \(m_y\le a_y\le Cd_y\le C\). This is the previously named component flux in its ray-limit normalization. For any fixed grade, the sets of its vertices reaching successive later ray sites increase to the entire grade. At each ray site, iteration of the nonnegative harmonic identity down to the stipulated grade gives its mass as the sum over precisely that set. Monotone convergence therefore gives total grade mass \(H_C\) and the cofinal capture directly. In the opposite direction \(\max_y m_y\to0\). The qualitative predecessor-minimum bound gives \(d_y\to0\) uniformly if all odd predecessors exceed \(M\), as \(M\to\infty\). Every finite set of positive sources enters this component, if at all, at a fixed grade and can only reach subsequent grades. [Weaver 12, Theorem 11, qualitative predecessor-minimum bound](https://rstation.ai/problems/collatz/papers/12) · [Previously identified bilateral flux, PR193](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md)

Now \(F(y)^2\gamma(y)=m_y^2-\sum_{Ux=y}m_x^2\). The sum of \(m_y^2\) at a grade tends to zero in the negative direction by the maximum bound and fixed total \(H_C\). It tends to \(H_C^2\) in the positive direction since one site captures the full mass in the limit. Summing the nonnegative difference over a finite interval of grades telescopes. The two limits give \(\sum_{y\in C}F(y)^2\gamma(y)=H_C^2\). Substitution into (2) finishes (1). The argument also proves absolute summability of these squared fluxes without interchanging signed component sums.

At fixed \(n\), the displayed energy admits finite approximations with deterministic tail control. Dropping first arrival bounds each row by \(\rho_{n+1}(y)/y\le3^{n+1}/y\), so the squared contribution of \(y>Y\) is at most \(9^{n+1}\sum_{y>Y}y^{-2}\). For each of the finitely many retained \(y\), discard source paths with total gap sum beyond \(S\). Their row mass is at most \(3^{n+1}\Pr(e_1+\cdots+e_{n+1}>S)/y\) when the cutoff includes the extra innermost letter generating \(\rho_1\). This gives a geometric tail in \(S\) at fixed \(n\). These bounds support evaluation of the finite-depth coefficients and do not supply an effective rate for the slope in (1).

## The limit at individual increments

In fact
\[
                \mathscr S_{n+1}-\mathscr S_n\longrightarrow
                         \sum_{C\ {\rm escaping}}H_C^2.              \tag{3}
\]
For the nonperiodic part the exact increment is \(\|\gamma_n\|_1\) less the one-tick mass loss under \(P\). At sites \(x\) whose successor stays nonperiodic the latter summand is \((1-w(x)^2)s_n(x)^2\ll d_x^2/x\). We have \(\sum_{x\ {\rm nonperiodic}}d_x/x<\infty\): average a finite partial sum of indicators that a uniform ordinary source visits those sites, weighted by \(1/x\). Each visited nonperiodic site occurs at most once on the trajectory, and its total reciprocal sum is bounded by the absolute simple-orbit packing constant. Then use the existing densities and take the supremum over finite sets. The other lost sites \(x\), those immediately entering cycles, have disjoint predecessor cones across all cycles, so their \(\sum d_x^2\) is finite. Dominated convergence shows that the loss has a limit. The nonperiodic energy therefore has convergent individual increments, whose limit equals its slope from (2).

For the cyclic part, let \(c_k(z)\) be the row of first entries at \(z\) at date \(k\ge1\) from noncyclic starts, setting \(c_k=0\) for \(k\le0\). We have \(c_k(z)\le C e_z\); also \(c_k(z)\) converges as \(k\to\infty\), by summing \(w(u)s_{k-1}(u)\) over the immediate noncyclic parents of \(z\) with their summable bound \(C d_u\). On one cycle let \(S\) push a row forward with factors \(w\), and \(\lambda=\prod_{y\in C}w(y)\). The row \(v_n\) from initially noncyclic sources at cyclic outputs is exactly
\[
   v_n=\sum_{j=0}^{q-1}S^j c_{n-j},\qquad
   v_{n+1}=S v_n+c_{n+1}-\lambda c_{n+1-q}.
\]
Thus \(v_n\) converges coordinatewise on this fixed finite cycle. Its squared-norm increment is bounded in absolute value by \(C' d_C^2\) uniformly over cycles and \(n\). Indeed \(v_{n+1}\) and \(S v_n\) are pointwise at most \(Cd_C\) and their difference has \(\ell^1\) norm at most \(2Cd_C\). The remaining difference \(\|v_n\|_2^2-\|Sv_n\|_2^2\) is at most \(C^2 d_C^2\sum_{y\in C}(1-w(y)^2)\ll d_C^2\), using the uniform reciprocal bound on the distinct sites of one cycle. Dominated convergence over \(\sum_C d_C^2\le1\) now shows that the cyclic energy of these rows has increments tending to zero.

Finally the initially cyclic row \(u_n\) has squared norm at most \(\sum_{x\ {\rm cyclic}} b(x)^2 1_{q(x)>n}\to0\). Its cross term with \(v_n\) is at most \(C\sum_{C:\ q>n}d_C\sum_{x\in C}b(x)\to0\), since each inner sum is bounded by the uniform cycle reciprocal constant and \(\sum_C d_C\le1\). The initial cyclic terms vanish absolutely. This completes (3) with an entirely finite stopping test at each \(n\).

The [first-merger Lean kernel](../../phase10/FirstMerger.lean) proves the graph disjointness for nonperiodic merger targets and provides the positive accelerated-map specialization. The [exact signed finite replay](check_ordinary_energy.py) checks cycle-lap subtraction, including longer signed cycles, independently from that kernel. The infinite mass bounds and analytic flux identification above are written results.
