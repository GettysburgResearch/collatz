# The critical signed defect law at individual depths

The Mellin exponent one has an exact undamped transport on ordinary sites and a real coordinate. This gives a distribution of the contraction rates of positive cycles under their ordinary basin densities. Positive preimage compensation gives an equivalent test on a positive scalar. The [previous Poisson clock spectrum](../../astra-six-hour-20261127/escape/POISSON_CLOCK_SPECTRUM.md) already detects the same cycle rates and densities using source-window Poisson probes at two large external scales. The present statistic is the signed difference of consecutive original geometric prefix rows at a single clock, with a summable transport error.

Use the notation and true row measures in [the dissipation theorem](STOPPED_MELLIN_DISSIPATION.md). Define on positive odd sites and \(s>0\) the signed integrable density
\[
 G_j(y,s)=e^s\,[L_{j+1,y}(e^{-s})-L_{j,y}(e^{-s})]/y.
\]
Write \(a_B=|B|^{-1}\sum_{y\in B}\log(1+1/(3y))\) for a cycle's mean loss in log defect. For an escaping component \(C\), write \(H_C\) for its original trace charge and \(d_C\) for its ordinary component density. For a cyclic component \(d_B\) denotes its full basin density. Then for every bounded continuous \(g\) on \([0,\infty)\),
\[
 \lim_{j\to\infty}\sum_y\int_0^\infty
          g(s/j) G_j(y,s)\,ds
   = g(0)\sum_{C\ {\rm escaping}}(\kappa d_C-H_C)
       +\kappa\sum_{B\ {\rm cyclic}}d_B g(a_B).                     \tag{1}
\]
More sharply,
\[
 \lim_{j\to\infty}\sum_{y>1}\int_{\log(j+1)}^\infty
                         G_j(y,s)\,ds
       =\kappa\sum_{B\ne\{1\}\ {\rm cyclic}}d_B .                  \tag{2}
\]
There is no positive part inside these signed sums. The limiting coefficients are nonnegative. In particular the potentially signed left side in (2) has a nonnegative limit.

Let \(K\) transport a density by \((x,s)\mapsto(Ux,s+\ell_x)\) with **no** amplitude discount, where \(\ell_x=-\log w_x\). On signed \(\ell^1(L^1)\) this is a contraction. The factor \(e^s\) cancels the original amplitude multiplication exactly. The same tail translation used in the proof of (4) of the dissipation theorem gives, up to null endpoints,
\[
 G_{j+1}=KG_j+E_j,\quad
 E_j(y,s)=\sum_{Ux=y}w_xd_{j+1}(x)e^s\,
                      {\bf1}_{0<s<\ell_x}.
\]
In particular \(\|E_j\|_1\le b_{j+1}\), whose sum is finite. The contribution of any fixed site and bounded initial mark after many steps has \(s/j\to a_B\) in a cyclic component, since the path eventually repeats its true lap. In an escaping component its marks stay bounded, by the uniform sum of reciprocals on a distinct positive path. Applying dominated convergence in the finite measure \(|G_i|\), or \(|E_i|\), proves the corresponding limit for each fixed injected density. The tail after injection date \(J\) costs at most \(\sum_{i\ge J}\|E_i\|_1\), uniformly in the final date. The same argument works with the cutoff \(s\ge\log(j+1)\); it eventually admits every cyclic packet and rejects every escaping packet. The extra spatial condition \(y>1\) rejects the packet if it eventually reaches the cycle at 1.

To evaluate the total coefficient on each actual component, observe that \(\int_0^{\ell_x} w_xe^s ds=1-w_x\). At \(j=0\), integration of the signed residual gives exactly \(\sum_{x\in C}\phi(x)\rho_1(x)/x=\lambda_0(C)\); the component is invariant under \(U\). Each subsequent signed injection on \(C\) has integral \(\sum_{x\in C}(1-w_x)d_{j+1}(x)=\lambda_{j+1}(C)-\lambda_j(C)\). Thus \(\sum_{y\in C}\int G_j(y,s)ds=\lambda_j(C)\) exactly, and its limit is \(\lambda_\infty(C)\) by total variation. The existing component budget identifies this mass as \(\kappa d_B\) on cycles, and \(\kappa d_C-H_C\) on escapes. The summable absolute injection bounds justify summing over all components. This proves (1) and (2). Adding the unmarked one-period signed increment from PR195 times \(g(0)\) to (1) restores \(\kappa d_C\) at zero on escape. It gives total mass \(\kappa\). [PR195, (4)–(6)](https://github.com/GettysburgResearch/collatz/blob/3fa7ef4a0011b35447a70f587b400878d5ea8ebe/research/astra-six-hour-20261127/collision/DEPTH_DIFFERENCE.md) · [Ordinary component budget](../../astra-six-hour-20261127/escape/POSITIVE_TRACE_BUDGET.md)

The unique known cycle has \(a_{\{1\}}=D\) and every other positive cycle has \(a_B\le\log(10/9)<D\). No all-cycle exclusion is implicit in this separation. PR200 obtains a different distribution in the first-power boundary layer of a selected drift gate: its masses use the actual permanent principal source weights \(1/m\); (1) uses the unconditioned original law and ordinary basin weights. [PR200, boundary-layer formula (1)](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/pointwise/FIRST_POWER_BOUNDARY_LAYER.md)
