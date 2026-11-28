# Fixed-target loss quantiles and the terminal-product law

**Status.** The bounded-clock comparison in (1) is a deterministic consequence of elementary packing on simple positive orbits. The population results additionally use the natural-density fixed-target clock law of Leen, the ordinary minimum tightness bound, and the known component budgets for the identified limiting measure. PR145 already proved the Gaussian product-process limit, its stronger Skorokhod formulation, the half-mean criterion, the outer depth limits, and finite numerical enclosures. Equations (4) and (7) below recover those prior results. The additions here are the deterministic bounded comparison at each target for every fixed loss fraction, the proof from unmarked fixed-target clock inputs via finite first-low partitions, and the identification (5)–(6) of the marked component law. [PR145, distortion cutoff](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/unsafe-return-weights/DISTORTION_CUTOFF.md).

For a positive integer \(n\) ignore its initial even coast and write \(x\) for its odd part. Put \(b_d(n)=\prod_{i<d}3U^ix/(3U^ix+1)\), \(F(n)=\lim_d b_d(n)\). These are the actual ordinary Collatz corrections. They are positive at finite depth, and \(F(n)<1\) at every source. For \(0<\delta<1\) define
\[
 T_\delta(n)=\min\{d\ge0: b_d(n)\le1-\delta(1-F(n))\}.
\]
The time is finite on every positive orbit, including a hypothetical escaping one. It is a mathematical statistic using the infinite future \(F(n)\); every finite value \(b_d(n)\) itself is computable from the first \(d\) ordinary odd steps.

## Deterministic comparison at every specified root

Let \(y\) be a fixed positive odd target, \(B_y\) its ordinary predecessor basin among positive integers, and \(J_y(n)\) the odd grade at its first visit for \(n\in B_y\). For each \(0<\delta<1\) there is a finite constant \(L_{y,\delta}\) such that
\[
          |T_\delta(n)-J_y(n)|\le L_{y,\delta}
                 \quad\hbox{for every }n\in B_y .                       \tag{1}
\]
All ordinary odd departures before first hitting \(y\) are distinct. On any such simple segment the sum of reciprocal departed odd heights greater than \(A\) is at most \(R(A)\to0\), uniformly in the path. One may use the elementary explicit \(R(A)\ll A^{-1/50}\). [Elementary simple-path packing, PR212](../../astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

Every \(n\in B_y\) has \(F(n)\le w_y=3y/(3y+1)<1\), since its full forward product includes that departure. Choose \(A\ge y\) so \(1-\exp[-R(A)/3]<\delta(1-w_y)\). Through the first entrance to an odd \(m\le A\), all departed odd heights exceed \(A\); their logarithmic inverse product is at most \(R(A)/3\). Thus the \(\delta\)-threshold has not crossed earlier. The remaining time from that first low \(m\) to \(y\) is bounded by the maximum of the first-hit times of the finitely many \(m\le A\) which actually reach \(y\). This proves the lower inequality in (1). Choose \(L\) so \(b_L(y)-F(y)<(1-\delta)(1-w_y)\). At \(J_y(n)+L\) the difference from \(F(n)\) is \(b_{J_y(n)}(n)[b_L(y)-F(y)]<(1-\delta)(1-F(n))\), proving the upper inequality. The finite constants need not be effectively known.

In particular, for every \(0<\varepsilon<1/2\), the entire transition from a fraction \(\varepsilon\) to \(1-\varepsilon\) of the eventual loss has bounded odd-step width on each \(B_y\). It has tight width under ordinary natural density:
\[
 \lim_{L\to\infty}\overline{\operatorname{dens}}\{
       n:T_{1-\varepsilon}(n)-T_\varepsilon(n)>L\}=0.                  \tag{2}
\]
Indeed every source whose path hits a positive odd root through \(M\) lies in a finite union of these basins. Their remaining complement has upper density \(O(M^{-\sigma})\) on odd starts by [the minimum law](SPATIAL_TRACE_TAIL.md). On all positive starts a finite initial number of possible even coast lengths gives the same upper bound by dilation, then a geometric tail exhausts the other coasts. No central limit theorem is required for (2).

## A natural-density transition on the whole population

Put \(D=\log(4/3)\), \(\sigma_o^2=2(\log2)^2/D^3\). On \(B_y\), let \(m_y(n)\) be the full shortcut time to the first visit to \(y\). The exact clock relation is
\[
 m_y(n)\log2=J_y(n)\log3+\log n-\log y-\log b_{J_y(n)}(n).
\]
The last product is bounded below by an absolute constant, by the same packing on distinct paths. The natural-density timed first-arrival theorem for each fixed target gives its centered shortcut time mean parameter \(2/D\) and variance parameter \(2(\log3)^2/D^3\), both per unit of \(\log n\). The relation therefore turns its normalized Gaussian limit into that for the odd grade with mean parameter \(1/D\) and variance parameter \(\sigma_o^2\). Equation (1) transfers the result to \(T_\delta\). Dependence on \(y,\delta\) in a bounded shift disappears after division by \(\sqrt{\log n}\). This includes every fixed odd unit. A nonunit odd \(y\) can be reached only from its own initial even coasts and has a density-zero basin. [Leen, *Brownian motion in Collatz orbits*, §1.3, “Every target”, version 1 TeX lines 122–130](https://zenodo.org/api/records/23252395/files/collatz-brownian-motion.tex/content) · [Weaver 179, Appendix A.5, exact input (A.8)](https://rstation.ai/problems/collatz/papers/179/v1).

The exact source assumption is the version-one corollary `cor:target`. With $T$ the shortcut map, for every positive integer $a$ and every real $t$ it asserts
\[
 \operatorname{dens}\{n\in\operatorname{Pred}_T(a):
 \tau_a^T(n)\le(2/D)\log n+t\sqrt{2(\log3)^2/D^3}\sqrt{\log n}\}
 =h_T(a)\Phi(t),
\]
where $h_T(a)=\operatorname{dens}(\operatorname{Pred}_T(a))$. This includes zero-density targets and assumes no convergence of $a$ to one. The cited deposited TeX has SHA-256 `43635af89c6727e4a7d5065d2621477913f58fb8d6570de16396168bbe49a5f1`. The corollary is an external preprint input in this manuscript.

The full population has the same Gaussian limit, jointly independent of the terminal product \(F(n)\) and its component label. More precisely, in the limit from uniform positive integers in any fixed proportional interval \((aX,bX]\), \(0<a<b\), let \((C,B)\) have the limiting natural law of the component and the product \(B=F(n)\). Then
\[
 \left(C(n),F(n),
   \frac{T_\delta(n)-(\log X)/D}{\sigma_o\sqrt{\log X}}\right)
          \ \Longrightarrow\ (C,B,Z),\qquad
  Z\sim N(0,1)\text{ independent of }(C,B).                            \tag{3}
\]
This statement also proves existence of the indicated natural terminal law. The component set is countable and carries the discrete topology.

To see this without assuming marked first-hit independence, the finite union of basins through a fixed height \(A\) can be analyzed as follows. Two such basins which intersect are nested or equal, since the two targets occur on the same forward path in one order or the other. The bounded-orbit roots through \(A\) have a disjoint list of maximal basins after removal of duplicates. On these basins \(F=0\) and the component is fixed. On the escaping part, take the first low point \(m\le A\) ever visited. The corresponding set is
\[
   B_m\ \setminus\!
    \bigcup_{\substack{m'\le A,\ m'\,\mathrm{odd}\\
                       U^j m'=m\,\text{ for some }j\ge1}} B_{m'}.
\]
Every displayed \(m'\) belongs to the same escaping component and is strictly upstream. Removing the finitely many disjoint maximal upstream basins gives this set and shows its natural density exists. On it, \(|F(n)-F(m)|\le 1-\exp[-R(A)/3]\) by the high, simple first segment. The component is again fixed. Each finite combination of these basin indicators has a Gaussian clock factor \(\Phi(z)\) multiplying its ordinary density, by the single-target conclusion already obtained for the *same* variable \(T_\delta\). The complement of all chosen basins has upper density \(O(A^{-\sigma})\).

Approximate any bounded continuous test of \(F\) on these finite cells and pass to the limit. The same argument holds with an indicator of any prescribed component. The countable component family is tight since the finite collection meeting the low set covers all but \(O(A^{-\sigma})\) of sources. For joint tests depending on the component, first truncate to finitely many components; their finitely many mark tests share a modulus of continuity. These observations prove the joint cumulative limits with natural source cutoffs. Subtract the counts through \(aX,bX\), using \(\log n=\log X+O_{a,b}(1)\) between these endpoints, to obtain (3). The same results hold for uniform odd sources, since deleting even \(n=2m\) gives an exact copy with unchanged component, \(F\), and odd grade and a bounded shift of log height.

At each Gaussian clock \(d_X(z)=\lfloor(\log X)/D+z\sigma_o\sqrt{\log X}\rfloor\), the actual finite product law is
\[
  (C(n),F(n), b_{d_X(z)}(n))
      \Longrightarrow
   \big(C,B,\ 1_{\{z<Z\}}+B\,1_{\{z>Z\}}\big).                       \tag{4}
\]
The assertion holds jointly at any finite collection of real \(z\)'s using one common \(Z\). Before \(T_\varepsilon\) the product differs from one by at most \(\varepsilon\). After \(T_{1-\varepsilon}\) it differs from \(F\) by at most \(\varepsilon\). By (2) the rescaled width between these quantiles tends to zero in probability, and the limiting standard Gaussian has no atom at any threshold. Applying (3) and then taking \(\varepsilon\downarrow0\) proves (4). Monotonicity also gives convergence in distribution in local \(L^1\) of the whole function \(z\mapsto b_{d_X(z)}(n)\) to this single step: on a bounded interval approximate off a finite grid by its monotone upper and lower step envelopes, whose integral difference is at most the grid mesh. Set the finitely negative indices to the empty product if needed.

## The actual terminal law and the finite mean criterion

On every escaping component the real source outcome has the following natural finite measure, in the variable \(s=F(n)\):
\[
   \mathcal L(C,B\in ds)=\frac{H_C}{\kappa s}\,\eta_C(ds),
          \qquad \kappa=D/2 .                                         \tag{5}
\]
The bounded components have \(B=0\) with their ordinary component densities. PR145 previously identified the source law weighted by its terminal product, in the translated coordinate \(1-s\). Formula (5) divides that law by its positive coordinate. The following also obtains it from the full killing-clock construction. [PR145, component-local ordinary distribution and nested predecessor exhaustion](https://github.com/GettysburgResearch/collatz/blob/dd245a712f985909f541590e3f6c179b7ba011e4/research/critical-orbit-mellin/COMPONENT_STIELTJES.md). The critical source-clock theorem identifies the limiting joint law of the *surviving* sources in \(C\) under the selector \(\rho_1\) with measure \(H_C\eta_C/\kappa\). On a start with terminal product \(F\), its survival probability is \(F^{1+u}\). Initial unselected odd weights \(x^{-1-u}\) have the same normalized limit after one odd step: at target \(y\) the new surviving unselected masses have multiplier
\[
     L_p1(y)=\sum_{e\ge1:\,2^e y\equiv1\,({\rm mod}\ 3)}
                   (3\,2^{-e})^p \quad (p=1+u)
\]
on \(y^{-p}\). This finite list of geometric-series formulas (one per terminal trit) converges uniformly to \(\rho_1(y)\), as does \(\rho_1(y)^p\). Their normalized mass discrepancy after one step is \(o(1)\). A kill on the first step has normalized mass \(O(u)\), by \(1-w_x^p\ll1/x\). The mark correction for that step is \(w_x\to1\) in probability since fixed bounded sources have normalized mass tending to zero. The component is preserved. Hence the plain odd Dirichlet source law has the same survivor limit. Its survivor selection multiplies the plain source law by \(F^{1+u}\), uniformly close to \(F\) on \([0,1]\). Existence of the ordinary natural distribution in (3) gives its same normalized Dirichlet mean by partial summation. Restriction to odd starts has the same limit, as already shown. This proves (5) by testing against continuous functions and dividing by \(s\) on escapes, where \(s\ge c_0>0\). [Critical source-clock identity](CRITICAL_SOURCE_CLOCK.md).

There is an exact marked refinement of the scalar component budget:
\[
  \sum_{y\in C}(1-w_y)a_y(D_{F(y)})_*\nu_y
       = H_C(s^{-1}-1)\,\eta_C(ds)
                  \quad(C\text{ escaping}).                             \tag{6}
\]
Using the bilateral ordinary path with one native grade per site, the left side equals \(H_C\mathbb E_C[\delta_J\sum_{v\in\mathbb Z}(1-w_{Z_v})/F(Z_v)]\). The sum telescopes via \((1-w_{Z_v})/F(Z_v)=F(Z_v)^{-1}-F(Z_{v+1})^{-1}\). The two endpoint products are \(J\) and one. This proves (6). In particular \(\kappa d_C^{\rm ord}=H_C\int s^{-1}\,d\eta_C\), consistent with (5) and the prior scalar stationary budget. A separate prior description records the natural pre-minimum log correction in each minimum cell; multiplying its corresponding product by the minimum's full forward product gives the same actual terminal outcome. [Weaver 175, Theorem 1 and the minimum-cell terminal inputs](https://rstation.ai/problems/collatz/papers/175).

Let \(H=\sum_C H_C\) over escaping components. From (5), \(\mathbb E B=H/\kappa\). Alternatively the same equality follows from the known ordinary logarithmic mean of \(F\) once natural convergence is established. The following criterion uses only finite ordinary positive-integer products:
\[
  \boxed{\quad
   \lim_{X\to\infty}\frac1X\sum_{X<n\le2X} b_{d_X(z)}(n)
       =1-\Phi(z)+\Phi(z)\,H/\kappa\quad(z\in\mathbb R).\quad}         \tag{7}
\]
In particular a liminf upper bound of \(1/2\) at \(z=0\) is equivalent to absence of positive escaping orbits. At any fixed \(c>1/D\), the same harmonic-free count with \(d=\lfloor c\log X\rfloor\) tends to \(H/\kappa\); at \(0<c<1/D\) it tends to one. These follow by monotonicity, the extreme limits of the Gaussian CDF, and the pointwise lower bound \(b_d(n)\ge F(n)\). The finite statistic has positive summands in \([0,1]\). The estimate establishing the required half bound, or the zero bound past the transition, remains open. Its validity would still allow additional finite cycles.
