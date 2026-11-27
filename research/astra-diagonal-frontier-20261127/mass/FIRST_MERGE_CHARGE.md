# The first common ordinary vertex of a collision at a late clock

**Source-qualified written result.** On positive odd starts, write \(a_y=h(y)/y\) for the original stationary trace, \(w_x=3x/(3x+1)\), and \(F_j(y)=\prod_{i<j}w_{U^iy}\), with \(F_\infty(y)=\lim_jF_j(y)\). Put \(D=\log(4/3)\). For every nonperiodic odd target and real \(q>1\), define the nonnegative quantity
\[
     J_{q,y}=a_y^q-\sum_{Ux=y}(w_xa_x)^q,\qquad
                   a_y=\sum_{Ux=y}w_xa_x.                              \tag{1}
\]
Here an odd nonunit has zero trace. The sources used below are the earlier ordinary first-arrival and slow-source laws, the predecessor-minimum limit, and the original stationary trace transfer. [Stationary component budget](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md) · [First-arrival row spectrum](FIRST_ARRIVAL_ROW_SPECTRUM.md) · [Slow-source square and cubic limits](SLOW_SOURCE_CHARGE_SPECTRUM.md).

Writing \(C\) for an escaping component and \(H_C\) for its actual charge, one has
\[
 \sum_{y\ \mathrm{nonperiodic}}J_{q,y}\le\kappa^q,\qquad
 \sum_C H_C^q=\sum_{y\ \mathrm{nonperiodic}}J_{q,y}F_\infty(y)^q
             =\lim_{N\to\infty}\sum_{y\ \mathrm{nonperiodic}}J_{q,y}F_N(y)^q .
                                                                         \tag{2}
\]
The last finite-clock sums decrease. Each nonperiodic unit \(y\) has \(J_{q,y}>0\) because it has at least two unit parents and each has positive trace. The weight in (2) is on a fixed original positive vertex at every clock \(N\).

There is a more specific interpretation in the actual common-depth statistic. For \(q=2,3\), take the ordered \(q\)-tuples of distinct odd \(x_i\le X\) that first reach a common endpoint at the same positive odd depth \(n\) and same native clock \(s\). Give each tuple weight \(p^{-q}\), where \(p=y_{\rm end}2^s/3^n\). Mark its earliest common vertex \(y\), the odd depth \(k\) of this meeting and the native total \(t\) there. These dates agree across all members: after a shared site the path to the specified endpoint's first visit has uniquely determined odd and native lengths. Equivalently at the last incoming step to \(y\) the \(q\) parents are not all the same. For three paths this is the earliest vertex common to *all three*; two can have met sooner.

As \(X,n\to\infty\) with \(n\ge300\log X\), normalize by \(\sqrt{\log X}\) for \(q=2\) and by \(\log\log X\) for \(q=3\). The resulting measures on \(y\) converge in total variation to
\[
       c_q\sum_{y\ \mathrm{nonperiodic}} J_{q,y}F_\infty(y)^q\,\delta_y,
 \qquad c_2=(2\pi D)^{-1/2},\qquad c_3=(4\pi\sqrt3)^{-1}.             \tag{3}
\]
For \(q=3\) one may take independent cofinal \(X,n\) using normalization \(\log\min(n,\log X)\). In particular every sufficiently large finite set of possible merge vertices captures all but an arbitrarily small fraction of the limiting coefficient, including when the eventual observed endpoints lie far above that set.

The joint distributions of the two original clocks are determined as well. For pairs put \(u=Dk/\log X\). For triples put \(u=\log k/\log\min(n,\log X)\). In either case put \(z=(t-2k)/\sqrt k\). In the sense of weak convergence of finite measures, the limit on \((y,u,z)\) is the measure in (3) times independent factors. For pairs their densities are \(1_{0<u<1}/(2\sqrt u)\) and the standard normal density. For triples they are \(1_{0<u<1}\) and the centered normal density of variance \(2/3\). No division by a possibly zero total escape charge is required.

## Conservation on the ordinary inverse graph

The natural precursor density at a nonperiodic site obeys \(\sum_{Ux=y}d_x=d_y\), and \(a_x\le\kappa d_x\) there. For a nonnegative vector \((v_i)\), the difference \((\sum v_i)^q-\sum v_i^q\) is coordinatewise increasing for every \(q>1\); use finite partial sums and then a limit. Thus \(J_{q,y}\le\kappa^q(d_y^q-\sum_{Ux=y}d_x^q)\). On a nonperiodic inverse tree, summation by levels telescopes this latter difference. The deep level remainder tends to zero because all its vertices have least ancestor tending uniformly to infinity, their maximum density tends to zero, and their level sum is \(d_y\). In a cyclic component, apply the inequality to each disjoint tree rooted at an off-cycle immediate parent of the cycle, then sum the roots' \(q\)th powers, bounded by \(d_C^q\) by disjointness. On an escaping component increase the root along an ordinary ray. This proves the first bound in (2) since the component densities sum to at most one by finite disjointness. [Ordinary density-coordinate proof of the level tail](DENSITY_COORDINATE_AND_TRACE.md).

On an escaping component, \(j_y=F_\infty(y)a_y\) is an exactly conserved flow: \(F_\infty(x)=w_x F_\infty(Ux)\), so \(j_y=\sum_{Ux=y}j_x\). Moreover \(j_y\le\kappa d_y\), and it tends to \(H_C\) along any escaping ray. Apply the same level telescoping to \(j_y^q-\sum_{Ux=y} j_x^q=F_\infty(y)^qJ_{q,y}\) and increase the root. Every eventually periodic source has \(F_\infty=0\) because its repeated primitive lap has multiplier strictly below one. This proves the middle identity in (2), and the first bound supplies domination for the last. Thus sequences of true early merges and their subsequent ordinary survival are separate factors in the exact formula.

## Marking the first merge in the common-depth spectrum

Fix one escaping target \(y\). For each fixed parent \(x\) let \(e_x=v_2(3x+1)\). The contribution at a first arrival to \(y\) at odd clock \(k\) and native total \(t\), restricted to paths entering through \(x\), is
\[
               w_x m_{k-1,t-e_x}(x)
          =w_xa_x g_k(t)+o_y(k^{-1/2})
           \quad\bigl(|t-2k|\le B\sqrt k\bigr).                      \tag{4}
\]
This is the fixed-root local estimate for each fixed selected parent (the error may depend on that parent). The last gap changes a fixed translate of \(g_{k-1}\) by \(O_x(k^{-1})\). The coefficient \(w_x\) is the actual ratio between the two normalizations \(3^k2^{-t}/y\) and \(3^{k-1}2^{-(t-e_x)}/x\). These are full positive ordinary first-arrival rows. Every represented input is at most \(p_y=y2^t/3^k\).

Take a finite selection of parents and all its ordered \(q\)-tuples of parent choices which are not constant. Their distinct underlying branch groups have first common vertex \(y\). At common depth \(n\) these paths have moved together for \(n-k\) odd steps after \(y\). Their observed row weight per tuple has gained the common factor \(F_{n-k}(y)^q\) because its physical height is \(p_y/F_{n-k}(y)\). The observed endpoint is a true first visit on these escaping paths. Counts for two different merge dates of this fixed \(y\) specify different eventual endpoints, since the tail is nonperiodic. A tuple has only one earliest common vertex.

For pairs retain \(k\) with \(Dk/\log X\) in a closed subinterval of \((0,1)\). For triples retain \(k\) with \(\log k/\log\min(n,\log X)\) in such a subinterval. In both cases \(n-k\to\infty\) uniformly and \(p_y\le X\) on every bounded central native window. For pairs use \(n\ge300\log X\) and \(\log p_y=Dk+O_B(\sqrt k)+\log y\); for the cubic range \(k\) is a fixed subpower of \(\min(n,\log X)\). Thus the original physical source cutoff is respected without any resampling.

With \(\phi(z)=(4\pi)^{-1/2}e^{-z^2/4}\), the local Gaussian clock kernel is \(g_k(t)\sim k^{-1/2}\phi((t-2k)/\sqrt k)\) uniformly on a fixed bounded central window. Sum the product of (4) over these \(t\). For pairs this gives the \(k^{-1/2}\) weight times the integral of \(\phi^2\) on the chosen window. For triples it gives the \(k^{-1}\) weight times the integral of \(\phi^3\). Their normalized sums over \(k\) give exactly the indicated clock densities and constants, including \(F_\infty(y)^q\). For three paths with repeated choices of a parent, the same product initially counts repeated *starts*. Removing each individual-source diagonal costs \(O(1)\) globally: if any two coordinates agree, its summed cube weight on a row is at most \(m_{n,s}(y_{\rm end})\sum_{x\text{ in row}}p^{-2}\), with \(m\) uniformly bounded and \(\sum_x x^{-2}<\infty\). Pairs pose the same bounded self-diagonal.

Increase the finite parent list. By positivity, the sum of the nonconstant parent products increases to \(J_{q,y}\). Increase the finite list of escaping roots and exhaust \((0,1)\times\mathbb R\) by interior clock rectangles. The preceding lower bounds then have total mass \(c_q\sum_C H_C^q\) by (2), which is the entire known slow-source limit. This proves the asserted joint convergence, for instance first on a finite partition into interior rectangles with null boundaries. It proves total variation in the discrete root mark by finite approximation. Positive mass on unmarked eventual cycles or exceptional clocks cannot persist after this exhaustion. No exchange of the infinite root sum with a nonuniform single-site estimate is needed.

## A fixed terminating control for the arithmetic prefix

For the known transient unit \(y=5\), \(U(5)=1\), and two distinct unit parents are \(13\) and \(53\) (their ordinary gaps are three and five). At each central clock \(k\), the ordered cross-parent pairs arriving for the first time at 5 therefore have a positive leading coefficient from (4), with \(w_{13}a_{13}w_{53}a_{53}>0\). Integrating through \(k\asymp\log X\) gives order \(\sqrt{\log X}\) in the cumulative *arrival-to-5* pair statistic. The analogous cubic order is \(\log\log X\). Both are genuine simultaneous first meetings of ordinary paths with matching native and odd clocks. The later common tail loses its weight because \(F_\infty(5)=0\). Thus an upper saving for all first-meeting prefixes, including the terminating component and omitting the subsequent ordinary trajectory, would already fail at this explicit site. A bound that includes the physical survival factors in (2) remains open.
