# All congruence classes at one actual inverse depth

**PROPOSED, written proof using the pinned binary–ternary routing and target-mass theorems.** Let \(U(x)=(3x+1)/2^{e(x)}\), \(e(x)=v_2(3x+1)\), on positive odd integers, and \(S_n(x)=\sum_{j<n}e(U^jx)\). For every fixed positive odd target \(a\), positive integer \(d\), and residue \(r\bmod d\),
\[
 \sum_{\substack{U^n x=a\\ x\equiv r\bmod d}}3^n2^{-S_n(x)}
       \longrightarrow h(a)\,\mathbf P_{\rm odd}(r\bmod d).                 \tag{1}
\]
At odd \(d\) each class has mass \(1/d\). At even \(d\) each odd class has mass \(2/d\), and each even class has mass zero. The mass trace \(h(a)>0\) at ordinary ternary units is inherited from Weaver's individual-depth theorem. At \(3\mid a\), all positive-depth sums are zero. Every source is a positive integer with exactly the displayed odd clock, including terminal multiples of three.

The Haar limit holds on the entire profinite completion of the odd integers, jointly with the real mark of the pinned fixed-root theorem. In one escaping component it holds for the original normalized ancestor law at \(a_j=U^j a_0\) and depth \(j+k\) as \(j,k\to\infty\) independently. At each fixed modulus convergence is in total variation on its finite quotient. The conclusion on the entire completion is weak convergence.

## Inputs and the new factor

At [PR193, full SHA 100ba857239a180840930765047d65ede92abeec, original transfer](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/escape/FIRST_POWER_HAAR.md), take \(B=(1+2\mathbb Z_2)\times\mathbb Z_3\) with \(m=m_2\otimes m_3\), normalized odd binary Haar times full ternary Haar. Its transfer on tests is
\[
 Lf(x,z)=\sum_{e\ge1:\ 2^ez\equiv1\ (3)}3\,2^{-e} f(I_ex,I_ez),
 \qquad I_e(t)=(2^e t-1)/3 .
\]
The inherited estimate (6) supplies an **absolute** \(c>0\). For each fixed finite-precision base cylinder \(E\), all sufficiently large \(n\), and every \(z\in\mathbb Z_3^\times\), it gives \(L^n1_E(x,z)\ge c\,m(E)\). This uses the joint Syracuse fixed-total routing floor with the true last letters retained. A second inherited conclusion says every positive entrance family \(L^*\nu_{j+1}=\nu_j\), over all \(j\in\mathbb Z\), of common finite mass \(H\), is identically \(Hm\) on this base. The [ordinary depth and mark theorem at the same SHA](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md) supplies \(\rho_n(a)\to h(a)\) and the actual grade approximation. [Weaver 176, Theorem 2](https://rstation.ai/problems/collatz/papers/176/v1) · [Weaver 202, §2, Input 2](https://rstation.ai/problems/collatz/papers/202/v1)

Fix \(q\) coprime to six and write \(D=\mathbb Z/q\mathbb Z\), with uniform law \(u_D\). Each inverse branch also acts on \(D\), with division by three interpreted as inversion of a unit. Denote the lifted transfer by \(L_D\) and the reference by \(m_D=m\otimes u_D\). The new theorem is uniqueness of positive entrance families of common finite mass on \(B\times D\). A Haar marginal on \(B\) allows arbitrary conditional distributions on \(D\).

## The forward map and the two reference measures

For \(t=(x,z)\in B\), set \(e=v_2(3x+1)\) and define
\[
 S(t)=\big((3x+1)2^{-e},(3z+1)2^{-e}\big),\qquad
 S_D(t,u)=(S(t),F_e(u)),\quad F_e(u)=(3u+1)2^{-e}\pmod q .
\]
Define the map arbitrarily on \(x=-1/3\), a null set. \(F_e\) is a permutation. Changing variables on each valuation branch gives
\[
 \int g\,L_Df\,dm_D=\int(g\circ S_D)f\,dm_D.                          \tag{2}
\]
The inverse binary output is the valuation cylinder of mass \(2^{-e}\). The ternary eligibility has mass \(1/3\) and its image has full Haar. Together they give the branch weight \(3\,2^{-e}\). The permutation preserves \(u_D\). In particular \(S_*m=(L1)m\), where \(L1\) takes the values 0, 1, 2 by ternary class.

Let \(H_3(z)\) be the Haar density of
\[
 Z=\sum_{i\ge1}3^{i-1}2^{-(E_1+\cdots+E_i)}\in\mathbb Z_3,\qquad
 \Pr(E_i=e)=2^{-e}\quad(E_i\text{ independent}).
\]
Its distribution has mass one, is supported on ternary units and is absolutely continuous. Its reduction modulo \(3^n\) has density \(L^n1\). The uniform unit floor above with \(E=B\) and martingale convergence therefore give \(H_3\ge c\) almost everywhere on units. Write \(\pi=H_3m,\ \pi_D=\pi\otimes u_D\). The distributional recurrence for the series, and the independent odd binary Haar coordinate giving the future geometric letters, give \(S_*\pi=\pi\) and \((S_D)_*\pi_D=\pi_D\). In particular \(S_*m\ll\pi\), including when initial points have a ternary nonunit coordinate. This argument uses an almost-everywhere density. Its value at a particular ordinary integer is immaterial. [Tao, §§1, 6](https://doi.org/10.1017/fmp.2022.8) · [Weaver 146/v1, §1, the series and its conditional densities](https://rstation.ai/problems/collatz/papers/146/v1)

## The base tail is trivial

A tail event belongs, modulo null sets, to every \(S^{-n}\mathcal B\). For a tail event \(A\) under \(\pi\), choose indicators \(f_j\), \(j\ge0\), with \(f_0=1_A=f_j\circ S^j\) \(\pi\)-almost everywhere. Invariance gives \(f_j=f_{j+1}\circ S\) under \(\pi\), and all their \(\pi\)-means equal \(p=\pi(A)\). Extend each from the ternary units to their complement by \(f_j=f_{j+1}\circ S\) there. This is well-defined almost everywhere because \(S_*m\ll\pi\), and the recursion now holds \(m\)-almost everywhere.

If \(p>0\), choose \(K\) so that \(\int_{H_3>K}H_3\,dm<p/2\). For every \(j\), the mass of the unit part of \(f_j m\) is at least \(p/(2K)\), since \(H_3\) vanishes off the units. Combining (2) on the base with the cylinder minorization gives
\[
 \int_E f_0\,dm=\int f_n L^n1_E\,dm
                 \ \ge\ c\,m(E)\,p/(2K).
\]
Use sufficiently large \(n\) for each \(E\). The same constant works on all cylinders, hence on all Borel sets by finite partitions and measure uniqueness. An indicator with this bound is one \(m\)-almost everywhere, so \(p=1\). The argument permits different \(m\)-masses for the successive \(f_j\).

## The finite extension is mixing and has trivial tail

Take two-sided iid letters \((E_j)_{j\in\mathbb Z}\). At time \(j\) the future letters determine an odd binary integer \(X_j\). The inverse compositions \(I_{E_j}\cdots I_{E_{j+l-1}}\) shrink binary differences by at least \(2^{-l}\) and prescribe the actual \(l\) successive valuations. The cylinder of a specified tuple has odd Haar mass \(2^{-\sum E_i}\), so \(X_j\) has law \(m_2\). The past letters determine \(Z_j\) by the displayed convergent ternary series read backwards from \(j-1\), with law \(H_3m_3\), independently of \(X_j\). Moving one step shifts the two-sided sequence and applies \(S\).

Choose \(u_0\) uniformly and independently of all letters. Define \(u_{j+1}=F_{E_j}(u_j)\) in both directions using the inverse permutations as needed. At each time \(u_j\) is uniform independently of all letters. The process of letters and states is mixing. Indeed its state transition matrix \(P(u,v)=\sum_{e:F_e(u)=v}2^{-e}\) is doubly stochastic. The two compositions \(F_1F_2,F_2F_1\) are \((9u+7)/8,(9u+5)/8\). Their quotient in the permutation group is translation by \(1/4\), which generates the additive group \(D\). A finite semigroup of permutations contains their inverses. Thus \(P\) is irreducible. The self-loop \(F_2(1)=1\) gives aperiodicity and \(P^n(u,v)\to1/q\). For two bounded cylinder observables of the joint letter/state sequence separated by a gap, sum over the two boundary states of the unobserved gap and apply this convergence. Approximation by cylinder functions proves mixing for all bounded observables. As a factor, \((S_D,\pi_D)\) is mixing.

For a tail event \(A\) of \(S_D\), choose coherent indicators \(f_j(t,u)\) with \(f_j=f_{j+1}\circ S_D\) under \(\pi_D\). Put \(b_j(t)=q^{-1}\sum_u f_j(t,u)\). Because \(F_e\) permutes \(D\), \(b_j=b_{j+1}\circ S\). Every level set of \(b_0\) is a base tail event. Thus \(b_0\) is constant and \(\pi_D(A)\) belongs to \(\{0,1/q,\ldots,1\}\). The tail probability algebra has at most \(q\) atoms since each positive event has mass at least \(1/q\). Pullback by \(S_D\) is injective on this finite algebra and permutes its atoms. If an atom of mass \(p\) returns after \(l\) applications, mixing along multiples of \(l\) gives \(p=p^2\). Hence there is only one atom. The finite-fibre argument together with base exactness converts mixing into triviality of the tail.

## Entrance families and ordinary consequences

Suppose \(L_D^*\nu_{j+1}=\nu_j\) for all integer \(j\), with common finite mass \(H\). The base projection has the same recursion and mass, hence is \(Hm\) by the pinned result. Each \(\nu_j\le qH m_D\) has a bounded density \(v_j\). By (2), \(v_j=v_{j+1}\circ S_D\) under \(m_D\), hence also under \(\pi_D\). Each \(v_j\) is measurable in the trivial \(\pi_D\)-tail and is constant there. The constants agree under the probability-preserving recursion. Finally \((S_D)_*m_D\ll\pi_D\), so the recursion gives the same constant on the whole \(m_D\) space. Its mass fixes that constant to \(H\).

The depth measures on \(B\times D\) start at \((a,a,a\bmod q)\) and propagate by \(L_D^*\) exactly. An integral inverse step at a positive odd target gives a positive odd source and its true outgoing exponent. All three coordinates are images of one integer. The masses \(\rho_n(a)\) converge and are bounded. From any increasing subsequence of depths, take simultaneous weak limits at all fixed translated depths by compactness. The transfer preserves continuous tests by uniform convergence of its clopen branch sum; reversing the index of the translated depths gives an entrance family of common mass \(h(a)\). Uniqueness identifies it. Every subsequence gives the same limit, proving (1) by CRT. Every cylinder of the odd profinite completion depends on a single finite modulus.

For one escaping component the pinned physical grade measures satisfy the same transfer identity on \(B\times D\). Their negative-grade masses tend to the same positive flux as in the two-coordinate theorem, so the entrance argument gives product Haar for each individual remote past grade. The difference from the included depth-\((j+k)\) ancestors of \(a_j\), in true weights \(1/P(x)\), tends to zero by the pinned uniform physical trace estimate. Projection to congruences cannot increase this loss. For the real mark, in the fixed-root proof condition on a fixed genuine inverse prefix terminating at \(b\), apply (1) at \(b\), then use the cited mark-tail tightness. In the moving-root proof use the same argument at the finitely many unit anchors retained at a fixed negative grade, followed by the pinned uniform reciprocal tail estimate. The real mark retains its prior law \(\sigma_a\) or \(\lambda_C\), respectively, independent of all fixed profinite projections.

## Quantitative scope

The auxiliary **unconditioned** finite walk has an explicit spectral estimate. If \(\bar f=0\) in \(L^2(u_D)\) and \(q>1\), Jensen's variance identity for \(P^2\) and the two tuples \((1,2),(2,1)\), each of probability \(1/8\), give
\[
 \|f\|_2^2-\|P^2 f\|_2^2
 \ \ge\ \tfrac1{64}\|f(\cdot+1/4)-f(\cdot)\|_2^2
 \ \ge\ \tfrac1{16}\sin^2(\pi/q)\|f\|_2^2 .
\]
The last inequality diagonalizes a generator of the cyclic group. The \(O(q^2\log q)\) unconditioned mixing clock does not quantify fixed-target ancestor measures conditioned on exact ternary legality.

At zero overshoot in an actual escaping component, the pinned source posterior has a positive atom at the ordinary seed. If its normalized mass is \(w>0\), any modulus \(q\) coprime to six with \(1/q<w\) gives a total-variation discrepancy of at least \(w-1/q\) in the limiting zero-grade posterior. Positive-overshoot convergence uses \(k\to\infty\). An effective estimate of conditional finite-fibre mixing at genuinely growing moduli, or a relative lower bound for a specified sibling of a supplied high-mass target, requires further information.
