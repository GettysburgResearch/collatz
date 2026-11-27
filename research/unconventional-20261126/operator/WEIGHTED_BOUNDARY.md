# Which boundary does an arithmetic resistance see?

**Status.** PROPOSED written deductions. The occupation input is [Theorem O2](../renewal/OCCUPATION.md) on finite simple ordinary shortcut paths, and the local counting input is [OP-H1](HEIGHT.md). The only additional external arithmetic input, explicitly identified below, extends one mass range. No computation of an unknown merging class is assumed.

Put $\theta=H_2(\log_3 2)$, where $H_2$ denotes binary entropy. Give the edge from $n$ to $Tn$ resistance $r_n=n^{-\theta}$ and conductance $1/r_n$. Keep both edges at $1\leftrightarrows2$. For $s>0$ give vertex $n$ mass $\mu_s(n)=n^{-s}$. On the full ordinary graph or its indicated unit subgraph define
$$
 E(f)=\sum_{n\to Tn}n^\theta |f(n)-f(Tn)|^2 .
$$
The maximal Neumann form domain $\mathcal D_N$ consists of all $f\in\ell^2(\mu_s)$ of finite energy. The minimal Dirichlet domain $\mathcal D_D$ is the closure of finitely supported functions in the norm $(\|f\|^2+E(f))^{1/2}$. The maximal domain is complete by coordinate convergence of the vertex values and completeness of the edge difference norm. Both domains are dense and define nonnegative self-adjoint operators. Components are separate in the maximal form.

## OP-W1. Arithmetic completion of each ordinary component

In each component, give a path the sum of its edge resistances as length, and take shortest-path distance $d_r$. If a simple undirected path is written in traversal order, its edge orientations are a forward segment followed by a backward segment, either possibly empty. A backward edge followed by a forward one would give a vertex two different outgoing edges. Each segment is therefore an actual finite simple shortcut trajectory when read in the appropriate direction. O2 gives a uniform function
$$
 \eta(M)\ll (\log\log(3M))^2/\sqrt{\log(2M)}\ \longrightarrow 0
$$
such that each connected component after deleting the vertices below $M$ has intrinsic $d_r$-diameter at most $2\eta(M)$. The same argument at $M=2$, allowing the finitely many visits to 1, gives a finite uniform diameter $D_*$ on all components. This reasoning applies unchanged on the unit subgraph.

The completion of each component is its ordinary space of vertices and ends. An end is an equivalence class of infinite simple rays whose tails lie in the same connected component outside every finite vertex set. To check compactness, delete the vertices below $M$ after $M$ exceeds the component's minimum. There are finitely many resulting pieces, each adjacent to a deleted vertex; their diameters tend uniformly to zero. Each ray is Cauchy. Distinct ends remain separated, since a path between their tails meets a fixed finite cut and its incident edges have positive minimum resistance. Conversely a Cauchy sequence which does not converge to an isolated vertex eventually belongs to one fixed piece outside each finite cut. The resulting nested choices give an end: for example, take simple paths from a fixed root to a subsequence escaping the successive cuts, and choose a diagonal ray using finite branching. In a one-cycle component one may delete one cycle edge when constructing the ray. This changes none of the ends. Equivalently use exhausting finite balls in a rooted spanning tree with the single redundant edge removed.

Every finite-energy $f$ satisfies
$$
 |f(x)-f(y)|^2\le d_r(x,y)E_C(f)\qquad(x,y\in C)
$$
by weighted Cauchy–Schwarz on paths, so it extends continuously to the completion of each component. Write $\mathrm{Tr}\,f$ for its end values. Then
$$
 \mathcal D_D=\{f\in\mathcal D_N:\mathrm{Tr}\,f=0\text{ at every end}\}.
$$
Evaluation at a fixed end is form-norm continuous: compare with the value at any fixed vertex using $D_*$. This proves one inclusion. On a single component a real finite-energy function with zero end values has only finitely many vertices with $|f|\ge\epsilon$, by compactness and isolation of its vertices. The cutoffs $\operatorname{sgn}(f)(|f|-\epsilon)_+$ are finitely supported and converge in form norm. Their residual is a 1-Lipschitz clipping, so dominated convergence applies to both vertex squares and edge differences. Apply this to real and imaginary parts, then exhaust the countable collection of components using the summable norm and energy contributions.

There is a stronger global observation specific to ordinary doubling. The ray $n,2n,4n,\ldots$ has resistance $r_\infty(n)=n^{-\theta}/(2^\theta-1)$ from $n$ onward. Hence a common end value $b$ gives $|f(n)-b|^2\le r_\infty(n) E(f)$ at *every* ordinary vertex. Conversely an ordinary limit as $n\to\infty$ gives that limit at every end. In particular $\mathcal D_D=\mathcal D_N\cap c_0$. For $s>1$ the domain that wires all ends to one common potential is exactly $\mathcal D_D+\mathbb C1$. Its zero energy space is one-dimensional by construction, whatever the number of physical components.

The discrepancy is visible inside the known basin. Let $a_k=3\cdot2^k$ and $b_k=2^k$, $k\ge4$. Free resistance here means the supremum of $|f(a_k)-f(b_k)|^2/E(f)$ on the maximal form; take $s>1$. All edges on the simple geodesic are bridges. Equality with the sum of those path resistances follows by putting a voltage with constant current on the geodesic and extending constantly on each side branch, which is allowed in $\ell^2(\mu_s)$. Consequently the free resistance tends to
$$
 \frac{3^{-\theta}+16^{-\theta}}{1-2^{-\theta}}+5^{-\theta}>0.
$$
The path runs through $3,5,8,16$. In contrast the common-boundary domain yields resistance at most $r_\infty(a_k)+r_\infty(b_k)=O(2^{-k\theta})$, by sending the unit current out on one doubling ray and back on the other. Those two ray tails are disjoint. More generally finite-energy currents with divergence $\delta_n-\delta_m$ obtained by joining two such rays at infinity can exist even for different components. They do not certify an ordinary path. The indicator of the open $3,6,12,\ldots$ half-line gives an explicit finite-energy function with different end values in the known component.

## OP-W2. The positive Neumann spectrum for finite total mass

For $s>1$, let $A_N$ be the generator of the physical maximal form. Its kernel consists of the $\ell^2(\mu_s)$ functions that are constant on each component, and **every component contributes** because the total mass is finite. On the orthogonal complement the operator has a uniform gap, compact inverse, and in fact
$$
 \operatorname{Tr}\big((A_N|_{\ker^\perp})^{-1}\big)\le D_*\,\zeta(s)/2 .
$$
For each component put $m_C=\sum_{x\in C}\mu_s(x)$. The variance identity and the path bound give
$$
 \|f-\bar f_C\|^2_{\ell^2(\mu_s|_C)}
 =\frac1{2m_C}\sum_{x,y\in C}\mu_s(x)\mu_s(y)|f(x)-f(y)|^2
 \le \tfrac12 m_C D_* E_C(f).
$$
This gives the global gap. To see the trace bound without assuming compactness, take any finite energy-orthonormal family of mean-zero form vectors in $C$. Bessel's inequality for the evaluation difference functional gives $\sum_i|f_i(x)-f_i(y)|^2\le d_r(x,y)\le D_*$. The variance identity then bounds $\sum_i\|f_i\|^2$ by $m_C D_*/2$. Thus the inclusion of the mean-zero energy Hilbert space in $\ell^2(\mu_s|_C)$ is Hilbert–Schmidt with that squared norm bound. Its product with its adjoint is precisely the positive inverse, by the variational identity for the closed form. Sum over components. The zero eigenspace can still have arbitrary multiplicity; trace class here concerns the positive inverse only.

There is a quantitative finite-dimensional approximation. Separate vertices below $M$ and the at most $3M$ complementary pieces incident to them. Retain their individual values and piece means, and put zero on entire components disjoint from the low set. On $\ker^\perp$ these last pieces already have mean zero. Applying the variance estimate on every high piece gives squared approximation error
$$
 O_s\!\left(M^{1-s}\eta(M)\right) E(f)
$$
for an approximation of rank at most $4M$, since each piece has mass at most $\sum_{n\ge M}n^{-s}$ and diameter at most $2\eta(M)$. This is an existence statement for the partition into *actual* pieces. Deciding whether two cut edges connect far above the cutoff is itself an arithmetic problem.

In particular the actual orthogonal zero projection is
$$
 (\Pi f)(n)=\frac{\sum_{m\in C(n)}\mu_s(m)f(m)}{\mu_s(C(n))}.
$$
For $f=1_{\{1\}}$ its values are either zero or the single number $1/\mu_s(C(1))\ge1/\zeta(s)$. For a fixed computable real $s>1$ (for instance $s=2$), a uniformly computable approximation of this physical marked row at individual inputs would decide membership in the basin of 1 by a fixed separation threshold. Conversely a membership algorithm computes this row, since the omitted tail of $\sum n^{-s}$ is effective. This equivalence is about deciding membership, which is weaker than proving it holds for every input. The positive trace and gap estimates alone give no procedure for evaluating the unknown global Neumann boundary data.

## OP-W3. An arithmetic mass range leaves only the half-line traces

Let $s_0=9691/25000$. For **every** $0<s\le s_0$ the maximal and minimal forms on the ordinary unit subgraph coincide. In the full graph the exact remaining boundary data are the traces at the pendant half-lines:
$$
 \mathcal D_N/\mathcal D_D
 \ \simeq\
 \ell^2\big(\{m>0:\ m\text{ odd},\ 3\mid m\},\ m^\theta\big).
$$
The trace map is bounded in the form norm and has a bounded linear right inverse. Both domains have zero kernel in this mass range. Moreover for $s+\theta>1$ the maximal generator has a positive gap and trace-class inverse on the full graph. The statements include the known component and any hypothetical additional component.

For the arithmetic step, OP-H1 gives $\gg_a X^{s_0}$ **unit** descendants below $X$ of every off-cycle unit $a$. Partial summation gives infinite $s$-mass in each such descendant subtree for $s\le s_0$, including logarithmic divergence at $s=s_0$. Every neighborhood of a unit-graph end contains a full off-cycle unit descendant subtree. Indeed a simple ray eventually points consistently along or against $T$. Apart from the finite cycle, it meets branching vertices at bounded gaps: backwards the unary steps are doublings with at most three before a branch; a forward run through successive unary destinations must be the same doubling chain read in reverse. At each sufficiently far branch there is an unused inverse child off the ray. Its descendant subtree is disjoint from the ray and the other such side subtrees. A fixed finite cut intersects only finitely many of them. Thus every end neighborhood has infinite vertex mass. Continuity at that end and square integrability force the trace there to be zero. OP-W1 gives equality of the two core domains. Each component has infinite total mass, so a component constant can belong to $\ell^2$ only with value zero.

On the full graph restrict $f\in\mathcal D_N$ to the core first, so the same conclusion holds there. The ends of the full graph either stay in the core or follow one pendant half-line. If $t_m=\lim_j f(2^jm)$ is its end value and $h_m=(3m+1)/2$ its attachment, Cauchy–Schwarz on that line gives
$$
 m^\theta|t_m-f(h_m)|^2
 \le (1-2^{-\theta})^{-1}E_{\rm line}(f).
$$
The core attachment values are controlled by a dyadic Hardy inequality. For any family of full doubling chains along which $f$ has zero limiting value, telescoping from infinity gives
$$
 \sum_n n^\theta|f(n)|^2
 \le (2^{\theta/2}-1)^{-2}
     \sum_n (2n)^\theta|f(2n)-f(n)|^2 ,
$$
where the sums are over the chosen chains. To check the constant, on one chain $n=2^j u$ write $f(2^ju)$ as the sum of successive differences at levels $\ell>j$. After multiplying by $2^{j\theta/2}$ the convolution kernel has weights $2^{-k\theta/2}$ for $k\ge1$. Its $\ell^1$ norm is $(2^{\theta/2}-1)^{-1}$, and Young's inequality proves the display. Apply to all core chains. Since $h_m\asymp m$, summing the half-line estimates gives $\sum_m m^\theta|t_m|^2\ll E(f)$. Conversely extend an arbitrary sequence in this weighted $\ell^2$ by its constant $t_m$ on the open half-line at $m$ and by zero on the core. Its energy is exactly $\sum_m m^\theta|t_m|^2$; its $\ell^2(\mu_s)$ norm squared is $(1-2^{-s})^{-1}\sum_m m^{-s}|t_m|^2$. The kernel of this trace map is $\mathcal D_D$ by OP-W1, proving the boundary isomorphism.

Finally subtract this constant-on-lines extension from $f$. The residual has zero trace on every doubling chain. Its energy is $O(E(f))$ by the bounded trace result, and the Hardy bound gives $\sum_n n^\theta |f_{\rm residual}(n)|^2\ll E(f)$. The extension has $\ell^2(\mu_s)$ norm bounded by a constant times $\sqrt{E(f)}$, so the maximal form has a positive gap. If $s+\theta>1$, the inclusion from the residual's weighted vertex space $\ell^2(n^\theta)$ to $\ell^2(n^{-s})$ is Hilbert–Schmidt, since its squared singular values are $n^{-(s+\theta)}$. The constant-on-lines extension similarly has squared singular values proportional to $m^{-(s+\theta)}$. The energy-space inclusion is their sum after bounded maps, and is therefore Hilbert–Schmidt. The inverse generator is trace class as in OP-W2.

The same domain conclusions extend to $s\le0.84$ if one invokes Krasikov–Lagarias, Theorem 6.1, for each fixed unit target. Its count of all positive predecessors implies divergence of their $s$-mass throughout this range. Removing the nonunit half-lines preserves divergence: at a core attachment $h_m$, the mass of its whole open half-line is $m^{-s}/(1-2^{-s})\ll_s h_m^{-s}$. Thus the unit subtree still has infinite mass. This extension uses their published computer-assisted bound; no replay of their linear program is claimed. [Krasikov–Lagarias, author PDF](https://websites.umich.edu/lagarias/doc/krasikov.pdf)

## OP-W4. A sufficient arithmetic estimate, without wiring

Fix $s>1$ in the *vertex measure*, and write $p=\Pi1_{\{1\}}$ for the actual maximal-form projection in OP-W2. For any single fixed arithmetic cylinder $P=\{n:n\equiv r\bmod 2^a3^b\}$, the following is sufficient for full convergence:
$$
 \sum_{n\in P} n^{-s_0}\,|p(n)-p(1)|^2<\infty .
$$
Indeed, the existence of a bad component would make the difference exactly $p(1)$ there. It has infinite $s_0$-mass in its unit vertices by OP-H1. The cylinder transfer in OP-L1, with an arbitrary varying unit $w$ in that component and exponent choice in a fixed finite range, carries these inputs into $P$ inside the same component, with bounded multiplicity and new heights $O_P(1+w)$ (the constants may also depend on the fixed seed used to specify $P$). Thus it has infinite $s_0$-mass in $P$ as well. The same criterion accepts exponent $0.84$ with the external predecessor theorem just described. This is an arithmetic estimate for a specified physical projection; no boundary values have been imposed. The estimate is open. In particular O2 controls individual simple paths at exponent $\theta$, while the proposed series can sum across infinitely many branches.
