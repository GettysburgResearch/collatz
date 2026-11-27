# The archimedean spectrum of a single escaping ordinary component

**PROPOSED written implication for one hypothetical escaping source.** Let \(a\) be a fixed positive odd ternary unit with an injective forward odd trajectory \(q_i=U^i(a)\); positive injectivity implies escape to infinity. The following arithmetic sets use only positive ordinary trajectories coalescing with this one path. The component is held fixed throughout the limit.

* The nonnegative odd-time levels have a compact countable real spectrum. Its Cantor–Bendixson derivative removes exactly the first remaining level. All finite derivatives are nonempty and have exactly one common point, the corrected real height \(L=\Lambda(a)\). The next derivative is empty. For every finite-rank rational in the spectrum its rank equals the negative of its ternary valuation.
* At every integer shortcut delay \(\Delta\), the same-odd-time meeting fiber is finite and eventually stabilizes along the actual forward ray. Its normalized real locations \(2^{-\Delta}x\) have **two exact Hausdorff limits**, according to the parity of \(\Delta\). The limits differ precisely at the one-step stratum, as specified below. Every sufficiently late normalized source lies arbitrarily near a single countable compact set. In particular the number of these true sources is \(o(2^\Delta)\).
* For every escaping component, \(|F_\Delta|\ge2^{\lfloor\Delta/17\rfloor}\) at every large integer delay, while only polynomially many sources of that delay can stay outside any fixed neighborhood of \(L\) after rescaling. The equally weighted measures of these finite ordinary fibers converge to the point mass at \(L\), with exponentially small off-neighborhood mass. This conclusion is elementary.
* Under the [source-qualified fixed-total floor](EXACT_INTERVALS.md), a critical escape, meaning \(A_n/n\to\log_2 3\) on this same ray, would nevertheless force \(2^{\Delta-o(\Delta)}\) sources of **each** sufficiently large delay, already with a prescribed unit residue modulo three. Every finite derivative of the countable spectrum then has Hausdorff dimension zero and lower and upper box dimension one. No tilt to the critical mean is assumed.

## Exact grades and a corrected coordinate

Write \(A_i=\sum_{s<i}v_2(3q_s+1)\), \(M_i=3^i2^{-A_i}\). The odd component consists of positive odd \(z\) for which \(U^r(z)=q_n\) for some \(r,n\ge0\). Assign to \(z\) integer grades
\[
    l(z)=n-r,\qquad h(z)=A_n-E,\qquad
    E=\sum_{t<r}v_2(3U^t(z)+1).
\]
Another meeting can only be a continuation of the earlier one at equal additional odd times, since the target ray has no repeated states. Thus the grades are independent of the meeting, \(l(a)=h(a)=0\), and an edge with cost \(e\) increments the grades by \(1,e\). Every path in this component is simple.

We use a uniform elementary input for ordinary positive simple paths. The sum of the reciprocals of their odd states of height at least \(B\ge1\) is at most \(C B^{-\delta}\) for absolute \(C,\delta>0\); one can take \(200,1/40\) from the pinned positive-path estimate. The infinite-path case follows by increasing finite truncations. [Finite simple-path estimate and proof, PR201 commit 2978d84f8a1fda9083593b26c6bf724d5976d859](https://github.com/GettysburgResearch/collatz/blob/2978d84f8a1fda9083593b26c6bf724d5976d859/research/killed-green-head-closure-20261124/escape-analysis/README.md) · [Prior shared-source distortion and balanced-row shells](../../astra-global-closure-20261124/round12/trace/README.md)

Let \(D(z)=\prod_{i\ge0}(1+1/(3U^i(z)))\), \(\Lambda(z)=zD(z)\), \(L=\Lambda(a)\). These products converge by the uniform input. The exact edge identity gives \(\Lambda(Uz)=3\cdot2^{-e}\Lambda(z)\). Define
\[
   \eta(z)=2^{h(z)}3^{-l(z)}z= L/D(z),\qquad 0<\eta(z)<L.           \tag{1}
\]
For an edge into \(Uz\), \(\eta(Uz)-\eta(z)=2^{h(z)}3^{-l(z)-1}>0\). In particular \(\eta(q_n)=q_n/M_n\uparrow L\) by the tail product. At any two odd ternary units, (1) gives distinct values unless the two integers coincide. Indeed \(v_3(\eta(z))=-l(z)\), \(v_2(\eta(z))=h(z)\), and (1) then recovers \(z\) itself.

## Exact derived sets

For integers \(j\ge0\) put
\[
   K_j=\{L\}\cup\{\eta(z):z\text{ is a ternary unit in the supplied component},
                              \ l(z)\ge j\}.
\]
Then \(K_j\) is compact and its set of accumulation points is exactly \(K_{j+1}\).

To see the upper inclusion take distinct points \(\eta(z_i)\) tending to \(t<L\) with \(l(z_i)\ge j\). By (1), \(D(z_i)\) stays above \(1+\epsilon\) eventually. Choose \(B\) so large that an orbit all of whose inputs exceed \(B\) has \(D\le\exp(C B^{-\delta}/3)<1+\epsilon\). Every sufficiently late \(z_i\) has a future value among the finite set of component sites at most \(B\). Pick a subsequence with the same such value \(b\). Its first hitting time here is necessarily \(l(b)-l(z_i)\), between zero and the fixed bound \(l(b)-j\). We can therefore make that time constant on a further subsequence. At each of the finitely many indices through this hit, pass again to make the ordinary states constant or divergent to infinity. Let \(z\) be the first constant one. Its index is positive, since the initial unit points are distinct. The prior finite product tends to one, so \(D(z_i)\to D(z)\) and \(t=\eta(z)\). The site \(z\) is a unit as it was reached by an odd edge, with \(l(z)\ge j+1\). This proves the upper claim, and also closedness since bounded sequence limits are either of this type or \(L\).

For the reverse inclusion, \(L\) is approached by \(\eta(q_n)\) from every \(K_j\). For a given unit \(z\) with \(l(z)\ge j+1\), take the infinitely many one-edge inverse exponents \(e\) with \(2^e z\equiv4\text{ or }7\bmod9\). Their unit sources \(w_e=(2^e z-1)/3\) tend to infinity and have level \(l(z)-1\ge j\). Formula (1), or \(D(w_e)=(1+1/(3w_e))D(z)\), gives \(\eta(w_e)\to\eta(z)\). This proves the claimed derivative equality. Unique factorization excludes a finite-level point from the intersection of all \(K_j\). Therefore the \(\omega\)-th derived set is \(\{L\}\), the \((\omega+1)\)-st is empty, and a point \(\eta(z)\) has exact finite rank \(l(z)=-v_3(\eta(z))\). These are properties of sets of ordinary positive coalescing vertices.

## Stabilization and the two Hausdorff limits

The exact same-odd-time fiber of delay \(\Delta\in\mathbb Z\) is
\[
 F_\Delta=\{x:l(x)=0,\ h(x)=-\Delta\}
           =\bigcup_{n\ge0} S_{q_n,n,A_n+\Delta}.
\]
Allow the empty word in the usual way and a negative time to give an empty set. The sets in the union increase in \(n\), by appending the actual next edge. For all \(x\in F_\Delta\), (1) gives \(x<2^\Delta L\), hence this increasing union stabilizes at a finite stage for every fixed delay. In fact every sufficiently late path to \(q_n\) at these grades has its normalized real offset \(\beta=q_n-M_n2^{-\Delta}x\) bounded below by \(c_{a,\Delta}q_n>0\): the finite source set lies strictly below \(2^\Delta L\) and \(q_n/M_n\to L\). This also rules out a bounded-offset construction at the actual grades \(\Delta=0\).

Let \(P_\Delta=2^{-\Delta}F_\Delta\), allowing in this section all positive odd sources, including multiples of three. For parity \(b\in\{0,1\}\) define
\[
   E_b=K_2\ \cup\ \{\eta(z): 3\nmid z,\ l(z)=1,\quad
                      2^{h(z)+b}z\equiv1\pmod3\},                  \tag{2}
\]
where negative exponents use the inverse modulo three. The sets \(P_\Delta\) converge in Hausdorff distance to \(E_b\) as \(\Delta\to\infty\) through \(\Delta\equiv b\bmod2\). Both \(E_b\) are compact by the derived-set theorem. They are distinct, since the unit \(q_1\) has level one and its uniquely represented \(\eta(q_1)\) lies in just one of them.

For the upper limit, take a convergent sequence of normalized sources along delays of the prescribed parity. If the limit is below \(L\), the same bounded-hit argument with all initial levels zero finds a first bounded site \(z\) at some fixed positive time \(j=l(z)\). The initial ordinary integers cannot repeat along distinct delays by the grade definition. The limit equals \(\eta(z)\). When \(j=1\), its inverse exponent is exactly \(h(z)+\Delta\); division imposes the congruence in (2). When \(j\ge2\), the limit already belongs to \(K_2\).

For the lower limit fix such a unit \(z\) at level \(j\ge1\), and write \(E=h(z)+\Delta\) for the required total of a \(j\)-edge inverse path. At \(j=1\) the specified parity makes the unique inverse \((2^Ez-1)/3\) integral and positive odd at every sufficiently large \(\Delta\). Its normalized value tends to \(\eta(z)\). At \(j\ge2\), set the inverse exponents in terminal-first order to \(e_1,\ldots,e_j\). Prescribe \(e_3=\cdots=e_j=2\). The complete integer carry for the forward path is
\[
 C=3^{j-1}+3^{j-2}2^{e_j}+\cdots+3\cdot2^{e_j+\cdots+e_3}
                     +2^{e_j+\cdots+e_2},
\]
with the first part interpreted as \(3\) when \(j=2\). That first part is divisible by three and fixed. Choose \(e_2\) in a bounded positive range depending only on \(j\) to make \(C\equiv2^Ez\bmod3^j\); this is possible because the required residue for the last power of two is a unit and two generates every ternary unit group. Set \(e_1=E-e_2-\cdots-e_j\), which grows to infinity. The source \(x=(2^Ez-C)/3^j\) is integral. Each intermediate reverse division is then integral by reducing the full affine equation modulo successive powers of three; from a positive odd terminal every integral reverse step is positive odd. Thus \(l(x)=0,h(x)=-\Delta\), and
\[
                    2^{-\Delta}x=\eta(z)-2^{-\Delta}C/3^j
                          \longrightarrow\eta(z)
\]
at **every** sufficiently large delay, with \(C\) bounded independently of that delay. The common limit point \(L\) follows by taking \(z=q_j\) with \(j\to\infty\). Finite nets of the compact \(E_b\) give the stated Hausdorff lower inclusion, while compactness of \([0,L]\) and the sequential upper inclusion give the other direction.

Both possible limit sets in (2) are countable, hence have Lebesgue measure zero. Cover their union by finitely many intervals of total length below any given \(\epsilon>0\), using compactness. Every sufficiently large \(P_\Delta\) lies in this open cover, and its distinct points are spaced by at least \(2^{-\Delta}\). Thus \(\limsup 2^{-\Delta}|F_\Delta|\le\epsilon\), proving \(|F_\Delta|=o(2^\Delta)\).

For the variant requiring all sources to be ternary units, use delays modulo six. At level one the condition becomes \(2^{h(z)+\Delta}z\equiv4\text{ or }7\bmod9\). At every \(j\ge2\) select \(e_2\) by the same proof one digit deeper, imposing \(C\equiv2^Ez-3^j u\bmod3^{j+1}\) for the desired \(u\in\{1,2\}\). The quantity to be matched by the last power of two remains a unit. This proves the corresponding six residue-class limits, without asserting that all six closed sets are distinct.

## Most normalized integer sources converge to one point

At any positive odd ternary-unit root \(y\) and every two-edge total \(H\ge19\) there are at least two distinct positive ternary-unit inverse sources. In the formula \(x=(2^Hy-3-2^e)/9\) for the two terminal-first inverse exponents \(H-e,e\), the condition on \(e\bmod6\) is \(2^e\equiv2^Hy-3\bmod9\). Among \(e=1,\ldots,18\) there are three choices in that class. Their sources occupy all three residues modulo three because \(2^6=64\equiv1+9\pmod{27}\); multiplying the last power by 64 changes the quotient by a fixed nonzero residue modulo three. The other exponent is at least one and integrality implies positive odd endpoints, so two distinct choices are units.

For \(J=\lfloor\Delta/17\rfloor\ge1\), choose the one true terminal \(q_{2J}\). Since \(A_{2J}+\Delta\ge 2J+17J=19J\), split its desired total into \(J\) integers each at least 19. Repeated two-edge branching gives at least \(2^J\) different unit sources at odd depth \(2J\) and the exact required total. Distinct paths from one terminal have distinct sources since all edges are actual deterministic forward steps. These sources all belong to \(F_\Delta\).

Fix any \(\epsilon>0\). A point \(x\in F_\Delta\) with \(2^{-\Delta}x\le L-\epsilon\) has a future gate \(z\) in the finite ordinary set \(z\le B_{a,\epsilon}\) by the same distortion bound used for compactness. Its odd distance to that gate is necessarily \(j=l(z)\ge0\), and its total is precisely \(h(z)+\Delta\). For \(j\ge1\), at most \(\binom{h(z)+\Delta-1}{j-1}\) positive compositions have those two exact grades, each specifying at most one inverse source. A zero-length hit accounts for finitely many fixed inputs. Summing over the bounded gates, for some finite \(J_{a,\epsilon}\) we obtain
\[
 \#\{x\in F_\Delta:2^{-\Delta}x\le L-\epsilon\}
             =O_{a,\epsilon}((1+\Delta)^{J_{a,\epsilon}}).            \tag{3}
\]
Thus the proportion off any fixed open neighborhood of \(L\) is at most \(2^{-\Delta/17+o_{a,\epsilon}(\Delta)}\). This proves convergence of the equally weighted normalized-fiber measures to the point mass at \(L\) for every true escape.

The entire spectrum away from \(L\) also has a quantitative covering bound. A point of \(K_0\cap(-\infty,L-\epsilon]\) is within at most \(J_{a,\epsilon}\) inverse steps of one of the same finitely many ordinary gates. If these steps have terminal-first exponents \(e_1,\ldots,e_m\), repeated use of (1) gives
\[
 \eta(z)-\eta(x)
       =2^{h(z)}3^{-l(z)}
           \sum_{s=1}^m3^{s-1}2^{-(e_1+\cdots+e_s)} .
\]
At metric scale \(2^{-R}\), drop each term whose cumulative exponent exceeds \(R+C_{a,\epsilon}\). Its whole omitted tail is shorter than \(2^{-R}\) for a sufficiently large constant, since there are at most \(J_{a,\epsilon}\) terms. The retained exponent lists have only \(O_{a,\epsilon}((1+R)^{J_{a,\epsilon}})\) possibilities. This covers the entire displayed region with that many intervals of length \(2^{-R}\). Every compact subregion away from the single point \(L\) therefore has upper box dimension zero.

## Exponential rate in the critical case

The following count uses the [pinned source-qualified floor (76)](https://rstation.ai/problems/collatz/papers/48). Its central-total consequence at any positive unit terminal \(y\), length \(n\) large and total \(2n\), gives \(\gg(4/3)^n/\sqrt n\) distinct ordinary sources, already in either prescribed unit class modulo three. Each word has mass \(2^{-2n}\), and the first-letter spread at extra depth one costs only an absolute factor. Distinct words yield distinct positive sources by deterministic forward decoding. The source qualification of the analytic estimate is the same as in the [exact-clock statement](EXACT_INTERVALS.md).

Set \(B_n=2n-A_n\). Its increments are integers at most one. Since \(q_n=M_n\eta(q_n)\ge1\) and \(\eta(q_n)<L\), we have \(B_n\ge(2-\log_2 3)n-\log_2 L\). Consequently each integer \(\Delta\ge0\) is attained, and the first such \(n=n(\Delta)\) satisfies \(\Delta\le n\ll_a\Delta+1\). At this actual moving terminal \(q_n\), the central total \(2n=A_n+\Delta\) lies in the one supplied delay fiber. Hence for every sufficiently large \(\Delta\),
\[
              |F_\Delta|\gg (4/3)^{n(\Delta)}/\sqrt{n(\Delta)}.    \tag{4}
\]
If \(A_n/n\to\log_2 3\), we have \((2-\log_2 3)n(\Delta)=\Delta+o(\Delta)\). Equations (1) and (4) give \(\log_2 |F_\Delta|/\Delta\to1\), simultaneously for the count restricted to either unit class. At scale \(2^{-\Delta}\), the corresponding normalized unit sources are distinct points of \(K_0\) on the dyadic grid. This gives lower box dimension at least one on all dyadic scales, hence on all scales by monotonicity. The upper bound is one since the set lies on a bounded real interval. The same argument applied with root \(q_j\) gives full lower box dimension for every \(K_j\), since the new level-zero spectrum is the homothetic set \(M_j K_j\). Countability gives Hausdorff dimension zero for every \(K_j\).

The two conclusions measure different properties. The fixed-component rational spectrum and its two parity limits have zero real measure. Its finite-scale discretizations may still grow at full exponential rate. Obtaining a power saving in (4)'s opposite direction for this one actual component would rule out a critical escape. The exact topology alone gives the little-o bound above, which is compatible with (4).
