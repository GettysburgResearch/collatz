# Dyadic residues and exponential amplitudes of the original harmonic law

Fix a dyadic modulus \(2^m\), \(m\ge1\). For \(1\le y<2\cdot3^k\) odd let
\[
 u_k(y)=\rho_k(y)/y,\quad t_k(y)=k^{-1}\log y,\quad
 L_k(y)=-k^{-1}\log u_k(y)\qquad(u_k(y)>0).
\]
The finite law is the original independent-gap law with probability \(2^{-e}\); raising \(u_k\) to a power here raises the *sum over the entire integer fibre* to that power. Put \(D=\log(4/3)\). Let \(\sigma_m\) be uniform on odd classes modulo \(2^m\). For each escaping component \(C\) choose an ordinary odd forward orbit \(a_{C,j}\), and let \(H_C\) denote its corrected trace charge.

**Source-qualified written theorem.** In bounded-Lipschitz distance on the two real coordinates and the finite residue coordinate, the following difference tends to zero:
\[
\begin{split}
 &\frac1k\sum_{y}u_k(y)\,
       \delta_{(t_k(y),L_k(y),\,y\bmod2^m)}\!
   -\frac12\int_0^{\log3}\delta_{(t,t)}\otimes\sigma_m\,dt\\
 &\hspace{1.7em}
   -\sum_{C\ {\rm escaping}} H_C\frac1k\sum_{j=0}^{k-1}
       \delta_{(k^{-1}\log a_{C,j},\,0,\,a_{C,j}\bmod2^m)}.
                                                               \tag{1}
\end{split}
\]
Zero-weight terms are omitted. In particular \(k^{-1}\sum_y u_k(y)\delta_{L_k(y)}\) converges to one-half Lebesgue measure on \([0,\log3]\) plus \((\sum_C H_C)\delta_0\). For fixed real or complex \(\xi\),
\[
 \frac1k\sum_{u_k(y)>0}u_k(y)^{1+\xi/k}
 \ \longrightarrow\ \frac{1-e^{-\xi\log3}}{2\xi}+\sum_C H_C,       \tag{2}
\]
with the continuous value at zero and real logarithms in complex powers. Weaver's tilted law raises each *individual word weight* to that power before summing through its residue fibre; its different transition involves the source log-height interval \([D,\log4]\). [Weaver, Paper 176, Theorems 1–3](https://rstation.ai/problems/collatz/papers/176) · [Prior amplitude limit and charge identification](../../astra-unconventional-20261126/global/COLLISION_ENERGY.md)

For any bounded mean-zero function \(W\) on the odd dyadic classes, (1) gives
\[
 \frac1k\sum_y W(y)u_k(y)
       -\sum_C \frac{H_C}{k}\sum_{j<k}W\(a_{C,j}\)\longrightarrow0.   \tag{3}
\]
For \(W=3/4-\mathbf1_{v_2(3y+1)\ge2}-\mathbf1_{v_2(3y+1)\ge3}\), the escape-ray lower drift \(\delta=7/4-\log_2 3>0\) proves
\[
       \liminf_k\frac1k\sum_y W(y)\frac{\rho_k(y)}y
                           \ \ge\ \delta\sum_C H_C.                 \tag{4}
\]
Thus the signed escape statistic can be made **linear in the original finite law**, with the macroscopic detector and its positive ray coefficient still retained. A zero upper subsequence excludes every positive escape under the stated reciprocal predecessor floor. The sign of this explicit linear sum is open. The original clipped proof works with (\Phi(u)=u^2/(1+u)); that nonlinear choice suppresses the entire diffuse population before testing its direction. Equation (1) proves direction cancellation on the diffuse population itself.

## Source decomposition and the two log coordinates

We use the definitions, normalizations and passage estimates of [Weaver, Paper 176, equations (5), (7), (9)–(12), (18)–(22)](https://rstation.ai/problems/collatz/papers/176), Valbuena's ladder comparison at its stated ordinary sampling windows, and the uniform \(L^p\) bounds for \(1<p<2\) on the original finite ternary density. [Valbuena, fixed source](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [Weaver, Paper 9 v2](https://rstation.ai/problems/collatz/papers/9)

Write \(F_M\) for the odd integers up to \(M\), \(\tau_M(v)\) for their first forward entry, \(f_j(v)=\prod_{i<j}3U^iv/(3U^iv+1)\). Every bounded endpoint test at depth \(k\) can be weighted equivalently by summing \(f_k(v)/v\) over all positive odd sources that produce it. If \(y\le 2\cdot3^k\) the sources above \(e^{Bk}\) cost \(o(1)\) for a sufficiently large fixed \(B\). For sources before entry, \(\tau_M(v)>k\), Weaver (19)–(20) prove one-half Lebesgue mass in scaled target log height, with normalized errors tending to zero as \(M\to\infty\) after depth. They also supply, up to exceptional normalized source mass \(O_B((\log M)^{-c})+o_M(1)\),
\[
 \max_{i\le\tau_M(v)}|\log U^iv-\log v+Di|=O_B(k^{3/5}),\quad
 D\tau_M(v)=\log(v/M)+O_B(k^{3/5}).                                  \tag{5}
\]
Here and below \(o_M(1)\) means that \(k\to\infty\) at fixed \(M\).

We show on this pre-entry mass that \(L_k-t_k\to0\) in measure, in the same two-limit sense. The density floor gives \(\log\rho_k(y)\ge\log\alpha_0\) at every positive-mass endpoint. On \([Y,2Y)\) among least representatives let \(A_Y=\{y:\rho_k(y)>e^{\epsilon k}\}\). Since \(\sum_{y<2\cdot3^k}u_k(y)=O(k)\), we have
\[
                    |A_Y|/Y\ll k e^{-\epsilon k}.                    \tag{6}
\]
Fix \(\eta>0\). It suffices first to consider targets \(\log y\ge\eta k\); the omitted pre-entry weight is \(O(\eta)+o_M(1)+O((\log M)^{-c}+T(M))\) by (20), where \(T(M)\to0\) is the uniform simple-path reciprocal tail. On a path satisfying (5), such a target before \(\tau_M\) must precede the first entry below \(b=e^{\eta k/2}\). For after that entry (5) bounds all further heights before \(\tau_M\) by \(b e^{O_B(k^{3/5})}\).

Take the ladder \(x_i=b^{\alpha^i}\), \(\alpha=1.001\), up to \(e^{Bk}\); it has bounded length at fixed \(B,\eta\). Source windows \([x_i^\alpha,x_i^{\alpha^2}]\) tile the required log source range, extending the top partial interval for an upper bound. The uncovered interval just above \(b\) cannot reach an endpoint above \(e^{\eta k}\) on (5). A local reference segment down to the next rung has at most \(R=0.1\log x\) steps with failure probability exponentially small in a positive power of \(\log x\), where \(x\) is its lower threshold. All pre-crossing states preceding a marked visit are at least \(e^{(\log x)/2}\) on the good local event, and so is the marked height. Initial segments before the first rung from a reference window satisfy the same bound. At time \(j\le R\), on this event the ordinary source reciprocal is at most twice its exact word weight \(3^j2^{-S_j}/y\). Since \(3^R<e^{(\log x)/2}/2\), in each dyadic band meeting the good range the sparse-set inequality yields
\[
                 \sum_{y\in A_Y}\rho_j(y)/y
                             \ll_p (|A_Y|/Y)^{1-1/p}.
\]
This is [the fixed-root sparse-visit bound (3)](CANONICAL_INVERSE_PATHS.md), applied to the same periodic finite density and arbitrary deterministic exceptional set. Summing over \(O_B(k)\) times and bands makes the reference probability exponentially small by (6), apart from the bad local height event. The event of a marked visit during a two-rung stage is a test of its upper landing; the ladder total-variation error is \(O_{B,\eta}(k^{-c})\) in total. Thus the normalized mass of pre-entry visits having \(\log y\ge\eta k\) and \(\rho_k(y)>e^{\epsilon k}\) vanishes in the indicated successive limits. Sending \(\eta\downarrow0\) proves the assertion for \(L_k-t_k\).

## Cancelling dyadic tests at a single specified terminal depth

Fix a mean-zero test \(W\) of the odd residue modulo \(2^m\), of norm at most one. Its value at an odd state is a bounded function of the first \(m\) chronological gaps, each truncated at \(m\). Indeed the affine reconstruction
\[
 x=(2^{S_r}U^r x-\text{integer offset numerator})/3^r
\]
determines \(x\bmod2^m\) once \(S_r\ge m\), using at most the first \(m\) letters. A term with a partial sum at least \(m\) vanishes modulo \(2^m\). Under independent geometric letters this gives a uniform odd residue, by the usual binary cylinder bijection. The resulting bounded mean-zero sequence in the sliding \(m\)-gap windows has an exponential maximal deviation estimate through \(O(s)\) steps at tolerance \(s^{3/5}\). Split starts into \(m\) classes to get independent bounded variables inside each class. The elementary local ordinary gap approximation and the upper-landing transfer in the proof of (5) apply unchanged. Truncate the last \(m\) positions of each good block, costing at most \(m\) per stage. Consequently, for a broad ordinary ladder source, with the same exceptional probability \(O_m((\log M)^{-c})\), **every** partial sum of \(W\) over an interval of its path through first entry at \(M\) has magnitude \(O_{m,\alpha}((\log v)^{3/5})\). This simultaneous estimate permits any start and end indices along the regular path.

A clock comparison is essential. A bounded window error in the upper passage duration would leave the terminal value of \(W\) uncontrolled. We now sum exact admissible upper word lengths *at a common shell state*.

Use Weaver's shell (9)–(12) with \(\kappa=\alpha^{5/4}\), \(\gamma=\alpha^{1/2}\). For a logarithmic source block \([u,\gamma u)\), put \(l=u/\kappa\), \(x=e^l\), \(\ell=\lfloor l^{4/5}\rfloor\). Let \(\mathcal M_x\) and \(\phi_x\) be the paper's ordinary preshell states and measure. Write \(z\in\mathcal M_x\) for a state \(\ell\) steps before first crossing of \(x\), reached after \(j\) canonical prefix steps. For each such state \(\log z=l+D\ell+O(l^{7/10})\). Define the interval of integer lengths
\[
  I_u=\{j\ge0:\ u\le l+D\ell+Dj<\gamma u\}.
\]
Uniformly for *any* deterministic array \(|b_j(z)|\le1\), the following signed shell comparison holds as \(u\to\infty\):
\[
 \sum_{\substack{u\le\log v<\gamma u\\v\ {\rm good}}}
       \frac{f_{j(v)}(v)}v b_{j(v)}(z(v))
       = \frac D2\sum_{z\in\mathcal M_x}\phi_x(z)
                         \sum_{j\in I_u} b_j(z)+o(u).                  \tag{7}
\]
The eligibility constants \(0<(\kappa-1)/D<(\kappa\gamma-1)/D<0.02\) put the displayed lengths in \([\ell,0.02l]\) for large \(u\), even after enlargement by \(O(l^{4/5})\). In (7) “good” means Weaver's upper local regular-prefix event only.

Here are the error details to allow signed, clock-dependent data. Enlarge and shrink both endpoints of the log interval defining \(I_u\) by \(Cl^{4/5}\). Excluding this boundary layer costs \(O(l^{4/5})\) in provisional word weight. In fact, at any fixed \(j\), summing \(3^j2^{-S_j}/z\) over all legal words and shell states costs \(O(1)\) by Weaver (10); this bounds every signed array as well. The canonical weight \(f_j(v)/v\) is exactly \(3^j2^{-S_j}/z\). At all retained \(j\), replacing \(\rho_j(z)\) by \(\rho_\ell(z)\) in the aggregate of these terms costs \(O_A(l\ell^{-A})\) by (7) and (10) of that paper. The resulting coefficient at \(z\) is precisely \((D/2)\phi_x(z)\).

For identification with the actual source interval before making that replacement, remove words with \(|S_j-2j|>l^{3/5}\). Equation (10) applied to their conditional residue distribution costs \(O(l e^{-c l^{1/5}})\) in total. On the remaining words Weaver (12) puts every reconstruction of an interior length in the source interval; a good original source has its length in the enlarged interval by (8). Bad sources with these reconstructed lengths have \(O(l)\) possible copies each. Their total provisional weight is bounded by \(O(l^2e^{-c l^{1/5}})\) using the ordinary octave estimate and \(f_j(v)\le1\). On every good reconstruction the no-earlier-crossing argument in (11) makes the prefix canonical. The disjoint realized sources and provisional words therefore agree away from the charged boundaries and bad mass, which proves (7). No independence between the suffix test and \(j\) was used.

We apply (7) with
\[
 b_j(z)= f_r(z)\,{\bf1}_{\{0\le r<\tau_M(z),\, U^r z\le e^{ak}\}}\,W(U^r z),
                 \qquad r=k-j,                                         \tag{8}
\]
using zero for negative \(r\). Take fixed \(0<a\le\log3\). By (5) pre-entry sources of interest, apart from the stated exceptional mass and \(o_M(k)\), have log heights between \((D-o(1))k\) and \((D+\log3+o(1))k\). Cover this region with whole blocks \([u,\gamma u)\) with \(u\) between fixed positive multiples of \(k\), extending slightly on either side. The number of blocks is bounded independently of \(k\), and every eligible \(j\) on those blocks is below \(k\) since \(j\le0.02l\) and \(u\le 2k\) suffices for this coverage. Good canonical upper prefixes stay above \(x>M\). Hence (8) tests precisely the actual pre-entry endpoint in each such block; exceptional upper sources contribute \(o(k)\).

Under \(\phi_x\), the simultaneous drift and dyadic partial-sum controls for the path from \(z\) through \(\tau_M(z)\) fail on mass at most \(O_m((\log M)^{-c})+o_M(1)\). For clarity, choose a reference source logarithmically over \([x^\alpha,x^{\alpha^2}]\). The same ladder estimate as (5) holds for these source windows with bottom \(M\), even if the top is between its original rungs: begin with this top rung, divide successive log heights by \(\alpha\), and stop at a bottom threshold \(M'\in[M,M^\alpha]\). For control all the way through \(M\), continue the geometric ladder downward to \(M'\in[M^{1/\alpha},M]\); the estimates then hold until first passage below \(M\), which occurs no later. The reference first-stage local estimate applies to the initial segment. Summed failure is \(O_m((\log M)^{-c})\), uniformly in the top. The law of the canonical preshell \(z\) of this broad source is within \(o(1)\) of \(\phi_x\): tile its log interval by the short windows of Weaver (11), omitting at most two endpoint pieces of relative weight \(O(l^{-1/5})\). On the good source the path remaining from \(z\) is a subsegment of the controlled path. The stated controls can be tested from \(z\) alone, at errors \(O_m(l^{3/5})\) in every partial sum and height displacement. This proves the transfer.

For each good \(z\), the allowed residual indices in (8) form an interval up to \(O_m(l^{3/5})\) exceptions: intersect \(k-I_u\) with \([0,\tau_M(z))\), then replace the height gate by \(\log z-Dr\le ak\) using the drift bound. The bounded mean-zero partial sums of \(W\) on any remaining interval are \(O_m(l^{3/5})\). The monotone factors \(0\le f_r(z)\le1\) preserve that order by summation by parts. The exceptional shell mass contributes \(O_m(k(\log M)^{-c})+o_M(k)\) across all retained lengths. Equations (7)–(8) therefore show that, at each individual \(k\), the normalized pre-entry signed mass tends to zero as \(k\to\infty\) and then \(M\to\infty\). The endpoint interval from \(3^k\) to \(2\cdot3^k\) costs \(O(1)\) by period normalization. Differences of height cutoffs now give a uniform odd dyadic coordinate independent of the pre-entry log height. Together with (6) this proves the first measure in (1).

## Ordinary entrances and escaping components

At first entry to \(F_M\) let \(Q_{i,z}\) be the incoming mass from sources at depth \(i\) landing at \(z\). These nonnegative numbers converge at each fixed \(M,z\) to \(c_{M,z}\) by the finite return subtraction (21) in Paper 176. The post-entry mass with residual clock \(j\) and entrance at \(z\) is exactly \(Q_{k-j,z}f_j(z)\) at the specified ordinary endpoint \(U^jz\); the original test uses \(u_k(U^jz)\) with the full depth \(k\). Since the tests are bounded, replacing the weights by \(c_{M,z}f_\infty(z)\) costs \(o_M(k)\). Eventually periodic \(z\) then drop out. When \(z\) is a multiple of three, \(Q_{i,z}=0\) for \(i\ge1\), so \(c_{M,z}=0\).

For an escaping unit entrance \(z\), the endpoint is nonperiodic and its harmonic amplitude is bounded above by an absolute constant at every depth, by the ordinary antichain bound. It is bounded below on this range as well:
\[
          u_k(U^jz)\ge [f_j(z)/z]\,\rho_{k-j}(z)
                       \ge f_\infty(z)\min(1,\alpha_0)/z,\quad j\le k .
\]
The first inequality retains all words passing through this specified integer \(z\), and the second uses the actual uniform finite atom floor. Thus \(L_k(U^jz)\to0\) uniformly in these residual indices for fixed \(z\). All such endpoints are least representatives for large \(k\), because \(U^jz+1\le(3/2)^j(z+1)\). Align each entrance orbit with the chosen ray of its component. Only bounded end segments change at fixed \(M\); the real height is divided by the same total depth and the dyadic mark is preserved at each shared integer. The resulting component coefficient is \(\sum_{z\in F_M\cap C}c_{M,z} f_\infty(z)\). Weaver (22) and the minimum law show that its total deficit from \(\sum_C H_C\) tends to zero as \(M\to\infty\), using \(H_C=(D/2)d_C\) in the weighted component normalization. This proves the post-entry term in (1).

The observed \(t_k,L_k\) live in a common compact interval for large \(k\), by \(y<2\cdot3^k\), the positive finite atom floor and \(\rho_k\le3^k\). The component sum in (1) is tight as well: discard components of arbitrarily small total charge, then use the growth bound for the finitely many remaining ray starts. Approximation on the resulting compact rectangles by step tests with fixed height cuts, followed by the proved pre-entry diagonal concentration, yields bounded-Lipschitz distance as asserted. Formula (2) follows by testing \(e^{-\xi L}\). The unconditional estimate (4) follows from (3), the boundedness of \(W\), summability of component charges, and the deterministic lower mean on each escaping ray. [Escape drift and component normalization](../../astra-unconventional-20261126/global/COLLISION_ENERGY.md)


## Finite arithmetic check

The [integer checker](check_linear_trace.py) evaluates the displayed signed principal-representative sum with rational outward enclosures through depth 16. It uses the exact dyadic recursion, visits the single unit orbit under doubling, and bounds accumulated integer rounding and the residual geometric tail. A separate positive full-period enumeration over every wrapped exponent verifies all density entries through depth 5. The sum at depth 16 lies between \(-0.0672309\) and \(-0.0672270\), before division by depth. These values at finite depth do not bound the asymptotic normalized trace. [Retained table](../../../reports/astra-six-hour-20261127/escape/linear_trace.tsv)
