# Original first-power transfer and the past of each ordinary escaping component

Let \(G=\mathbb Z_3\), \(V=G^\times\), and \(m\) be probability Haar measure on all of \(G\). For continuous functions define the exact geometric-word transfer
\[
 (Lf)(y)=\sum_{e\ge1:\,2^ey\equiv1\ (3)}3\,2^{-e}f((2^ey-1)/3).
\]
The series converges uniformly, maps continuous functions to continuous functions, and \(L1\) takes the values \(0,1,2\) on residues \(0,1,2\). Haar is fixed by \(L^*\): on each single inverse branch its domain has Haar mass \(1/3\), and its affine expansion maps that restriction to \(m/3\).

## A lower bound on every inverse terminal cylinder

There are absolute \(c,\delta>0\) such that, for all sufficiently large \(n\), any union \(E\) of depth-\(k\) ternary cylinders with \(0\le k\le\delta n\), and every \(y\in V\),
\[
                       L^n\mathbf1_E(y)\ge c\,m(E).                  \tag{1}
\]
Use the published fixed-total joint routing statement, Weaver 202 §2, Input 2. At each integer \(S\) with \(|S-2n|\le\sqrt n\) and each unit residue \(v\bmod3^{n+k}\), at least \(a2^S/(3^{n+k}\sqrt n)\) length-\(n\) words of total \(S\) have \(\beta_w=\sum_{i=1}^n3^{i-1}2^{-(e_1+\cdots+e_i)}\equiv v\bmod3^{n+k}\), with an additional bounded-real-intercept restriction. For any requested terminal class \(r\bmod3^k\) prescribe \(v=y-3^n2^{-S}r\), which is a unit. Each word is compatible and its actual inverse endpoint \(2^S(y-\beta_w)/3^n\) lies in class \(r\). Integrality at the last site implies integrality at every preceding site by applying the forward affine maps. The weight is precisely \(3^n2^{-S}\). Summing the disjoint central totals gives \(c3^{-k}\). Disjoint terminal classes add. The bound is on the unrestricted unnormalized transfer even though the selected evidence has bounded intercept. [Weaver, *How little a Collatz predecessor set can gain at its first odd doubling*, §2 Input 2](https://rstation.ai/problems/collatz/papers/202) · [Weaver and Wren, *Hierarchical Syracuse renewal and linear valuation budgets for modular routing*, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48/v2).

## Uniqueness for finite positive measures, including an entire entrance family

Suppose \((\nu_t)_{t\in\mathbb Z}\) are finite positive Borel measures of common mass \(H\), satisfying \(L^*\nu_{t+1}=\nu_t\) at every \(t\). Then \(\nu_t=H m\) for every \(t\). In particular Haar is the unique probability fixed by \(L^*\).

Indeed \(H=\int L1\,d\nu_{t+1}\le2\nu_{t+1}(V)\). For each fixed clopen \(E\), choose \(n\) large enough in (1). At each \(t\), \(\nu_t(E)=\int L^n\mathbf1_E\,d\nu_{t+n}\ge cH m(E)/2\). Compact regularity extends the comparison to all Borel sets. Decrease \(c\) if necessary so \(\epsilon=c/2\in(0,1)\). Subtract \(\epsilon H m\) from every grade simultaneously. The remaining measures still form a positive entrance family, of common mass \((1-\epsilon)H\). Iterating increases the Haar coefficient to \(H\). This proof uses the cone of positive measures, without any invariance of Jordan factors. The [Lean positive-cone uniqueness theorem](../operator/InvariantCone.lean) checks the abstract maximal-subtraction argument for a single positive fixed functional.

## Every individual past grade becomes equidistributed

In a hypothetical ordinary escaping odd component use its integer grade \(g(Ux)=g(x)+1\) and corrected height \(P(Ux)=3\,2^{-e(x)}P(x)\). Define the finite actual grade measure
\[
           \mu_v=\sum_{g(x)=v}\frac{\delta_x}{P(x)},\qquad Z_v=\|\mu_v\|.
\]
All actual inverse endpoints of an ordinary odd positive target are odd and positive. Their corrected weights then show \(L^*\mu_{v+1}=\mu_v\) exactly, including the ternary-nonunit terminal leaves. The earlier source-qualified [integer trace profile](../../astra-unconventional-20261126/boundary/TRACE_PROFILE.md), using Weaver 176, Theorem 2, proves \(\sup_v Z_v<\infty\), \(Z_v\to H_C>0\) at minus infinity and \(Z_v\to0\) at plus infinity. It follows that
\[
                             \mu_v\ \Rightarrow\ H_Cm\qquad(v\to-\infty).  \tag{2}
\]
For any sequence \(v_i\to-\infty\), compactness of the space of bounded positive measures on the compact metrizable group gives a subsequence with weak limits of \(\mu_{v_i+t}\) simultaneously at every integer \(t\). The limits have common mass \(H_C\); continuity of \(L\) passes their entrance recursion to the limit. The just-proved theorem identifies every limit with \(H_Cm\). This proves full individual convergence. In particular (2) controls each fixed ternary cylinder on the actual integer grade without depth averaging. At the original grade zero, the limiting own-word posterior remains a probability on countably many physical integers. Its total variation limit was proved in the [ordinary source posterior theorem](../../astra-unconventional-20261126/global/POSTERIOR.md).

## The boundary surviving transverse smoothing

For \(k\ge0\) let \(S_k\mu\) average \(\mu\) by translations in \(3^kG\), normalized to probability on that ball. Then \(S_0\mu=\|\mu\|m\) for positive \(\mu\) and, for \(k\ge1\),
\[
                           L^* S_k\mu=S_{k-1}L^*\mu .                 \tag{3}
\]
For each branch its eligibility is constant on depth-\(k\) source cylinders and its affine image of a uniform such cylinder is uniform at depth \(k-1\). Summation proves (3). Hence for \(N\ge-K+1\) the finite sum \(\Gamma_{K,N}=\sum_{v=-K+1}^N S_{v+K}\mu_v\) satisfies
\[
                   L^*\Gamma_{K,N}-\Gamma_{K,N}=Z_{-K}m-S_{N+K}\mu_N.   \tag{4}
\]
The last term tends to zero in total mass as \(N\to\infty\). The past boundary has positive mass. If \(\rho\) denotes the Haar density of the original stationary ternary Syracuse measure, its depth-\(k\) conditional expectation is the finite density \(\rho_k=L^k1\). Then
\[
       \int \rho\,dS_{v+K}\mu_v=\int\rho_{v+K}\,d\mu_v=Z_{-K}.           \tag{5}
\]
Both equalities use actual graded source weights. Thus the positive smoothed sum has infinite stationary-density moment in the limit even if its unweighted total were finite. Equations (4)–(5) specify the flux a finite-current construction must cancel. The earlier [two-coordinate transverse measure](../../astra-unconventional-20261126/global/TRANSVERSE.md) used a different tilt.

At a true escaping ray \(a_j\), the normalized terminal law at depth \(j\) weights \(x\in\{U^jx=a_j\}\) by \(1/P(x)\) and converges in total variation to its purely atomic grade-zero law. A lower estimate \(L^j1_E(a_j)\ge c'\rho_j(a_j)m(E)\) for every fixed clopen \(E\) along one common subsequence would contradict that limit: it would dominate a positive copy of the nonatomic Haar measure. Formula (1) supplies only \(c/\rho_j(a_j)\) after this normalization, and \(\rho_j(a_j)\asymp P(a_j)\to\infty\). In particular the absolute minorization does not yet bound the relative side mass on this same ordinary ray.

## Both local coordinates of the same ordinary source

Let \(G_2=1+2\mathbb Z_2\) with its normalized odd Haar law \(m_2\). On \(G_2\times G\), lift \(L\) by applying \(I_e(z)=(2^e z-1)/3\) in both coordinates, with eligibility in the ternary coordinate alone. Denote the lift by \(\widehat L\). Its product-Haar fixed measure is \(m_2\otimes m\). Indeed \(I_e\) sends odd binary Haar to its conditional uniform restriction to the valuation class \(v_2(3x+1)=e\), whose original mass is \(2^{-e}\). On the ternary coordinate the eligible Haar class contributes the factor \(1/3\) as before. Summing the weighted restrictions recovers the full product, since the single missing binary point \(-1/3\) has Haar mass zero.

For any binary class \(A\) of odd residues modulo \(2^{b+1}\) and any ternary class \(E\) of depth \(k\), the uniform product floor is
\[
 \widehat L^n\mathbf1_{A\times E}(z,y)\ge c\,m_2(A)m(E)
 \quad (y\in V,\ n-b\text{ sufficiently large},\ b+k\le\delta(n-b)).        \tag{6}
\]
Prescribe the last \(b\) letters of the outward inverse word. For one such suffix \(w\), its binary output modulo \(2^{b+1}\) is independent of the incoming odd coordinate, since all incoming differences are even and its slope is \(2^{S_w}/3^b\) with \(S_w\ge b\). Its valid ternary incoming cylinder for terminal class \(E\) has depth \(b+k\), obtained by applying the unique forward affine inverse of the suffix. Every point in that cylinder passes all suffix integrality tests. Route the first \(n-b\) letters into the cylinder using (1). Multiplying the lower bound \(c3^{-b-k}\) by the exact suffix weight \(3^b2^{-S_w}\) gives \(c2^{-S_w}3^{-k}\). Sum over the disjoint suffixes giving \(A\). Their weights \(2^{-S_w}\) sum exactly to \(m_2(A)\), since independent inverse binary letters of law \(2^{-e}\) preserve odd Haar and erase the incoming class at this precision. The case \(b=0\) is (1). General clopen sets are disjoint finite unions of rectangles at common precisions. The constant is independent of both precisions. [Tao, *Almost all orbits of the Collatz map attain almost bounded values*, odd Haar and geometric valuations in §1](https://doi.org/10.1017/fmp.2022.8).

The simultaneous Haar-subtraction argument applies verbatim, since \(\widehat L1=L1\) on the ternary coordinate. Its unique finite positive probability fixed measure is \(m_2\otimes m\), and every bi-infinite positive entrance family of constant finite mass has this same product law after normalization. In particular with the actual diagonal embedding \(x\mapsto(x,x)\),
\[
       \sum_{g(x)=v}P(x)^{-1}\delta_{(x,x)}\ \Rightarrow\ H_C\,m_2\otimes m
                           \qquad(v\to-\infty).                             \tag{7}
\]
This is individual-grade joint equidistribution of actual positive odd integers, in the ordinary binary valuation space together with the original ternary one. The proof again passes the exact recursion to translated subsequential weak limits. The terminal coordinates are never randomized in the original grade measures. Equation (7) retains finite congruences in both places; it does not turn a cylinder of precision comparable to the whole horizon into a fixed positive atom.

## Strong convergence on integrable product densities

With \(M=m_2\otimes m\), the same \(\widehat L\) extends to a positive mass-preserving contraction on \(L^1(M)\). It satisfies the norm convergence
\[
 \lim_{n\to\infty}\left\|\widehat L^n f-\rho(x_3)\int f\,dM\right\|_{L^1(M)}=0
                        \qquad(f\in L^1(M)),                                \tag{8}
\]
where \(\rho\) is the original stationary ternary density. The contraction follows from product-Haar invariance of the adjoint, using \(|\widehat Lf|\le\widehat L|f|\). Set \(W=G_2\times V\). For a nonnegative function constant on finitely many rectangles, (6) gives \(\widehat L^nf\ge c\mathbf1_W\int f\,dM\) for all sufficiently large \(n\). Approximate any nonnegative \(f\in L^1\) in norm by such functions to obtain
\[
 \left\|\big[c\mathbf1_W\!\int f\,dM-\widehat L^nf\big]_+\right\|_1\longrightarrow0. \tag{9}
\]
For real mean-zero \(u\) apply (9) to its two nonnegative parts of equal mass. Their images overlap in mass at least \(cM(W)\|u\|_1/2-o(1)\). It follows that \(\limsup_n\|\widehat L^nu\|_1\le(1-cM(W))\|u\|_1\). The norms decrease. Replacing \(u\) by \(\widehat L^ju\) and letting \(j\to\infty\) forces their limit to zero. Use real and imaginary parts for complex tests. Finally \(\widehat L^n1=\rho_n\), the depth-\(n\) conditional expectations of \(\rho\), converge to \(\rho\) in \(L^1\). Applying the mean-zero result to \(f-\int f\,dM\) proves (8). This conclusion concerns integrable densities for product Haar. An individual ordinary integer has zero product Haar mass.
