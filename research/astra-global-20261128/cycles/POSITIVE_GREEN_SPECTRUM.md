# A spectral gap for the positive Green operator of all ordinary parents

Let $X$ be the positive odd integers coprime to three, and $U$ the ordinary odd-to-odd Collatz map. It sends $X$ to $X$. Let $w_x=3x/(3x+1)$ and $t_x=1-w_x=1/(3x+1)$. The all-visit harmonic function supplies $0<a_x=h(x)/x<\infty$ and

\[
                 \sum_{Ux=y}a_xw_x=a_y.                                 \tag{1}
\]

The sum includes all positive unit parents. Nonunit odd sources have zero harmonic mass and cannot be periodic. We use the ordinary uniform reciprocal packing of simple orbit segments, $\sum_{x\ge b}t_x\le K b^{-\sigma}$ for some $K<\infty,\sigma>0$. Both inputs and their source pins are stated in [the raw-cycle trace](CYCLE_TRACE_LAW.md). The numerical bound $\lambda_C=e^{-g_C}>e^{-.024}$ on every extra primitive lap uses [the two inputs for the diagonal moment](DIAGONAL_CYCLE_MOMENT.md). The fixed lap has $\lambda=3/4$. The spectral gap below also has a nonnumerical version using merely the packing bound $\inf_C\lambda_C>0$.

On $\mathcal H=\ell^2(X,a)$ set $Pf(x)=w_x f(Ux)$, and write $M_v$ for multiplication by $v$. The true Green kernel counts every forward visit, weighted by survival to that visit. Its two-sided weighted version is

\[
 L=\lim_{r\uparrow1}M_{\sqrt t}(I-rP)^{-1}M_{\sqrt t}.                   \tag{2}
\]

The limit exists strongly. It is a bounded positive operator, meaning that nonnegative functions have nonnegative images. Its spectrum satisfies

\[
      \sigma(L)\subseteq\{1\}\cup\{|z|\le1/4\}.                         \tag{3}
\]

Its eigenspace at one has one dimension for every genuine positive cycle and none for an escaping component. Its powers converge in operator norm to that spectral projection, with $\|L^n-\Pi\|\ll_\epsilon(1/4+\epsilon)^n$ for $0<\epsilon<3/4$. In contrast, the Fredholm essential spectrum of the original $P$ is the whole closed unit disk on this same Hilbert space, regardless of the cycle count. **The multiplicity in (3) remains undetermined.**

## The unsandwiched survival operator

By (1), $Vf(x)=\sqrt{w_x}f(Ux)$ is an isometry on $\mathcal H$. For every $y$ the unit parents contain at least two distinct sites (in fact infinitely many). On the parent set choose a unit vector perpendicular to the restricted vector $(\sqrt{w_x})_{Ux=y}$ in the weighted inner product. This gives mutually orthogonal vectors in $\ker V^*$ as $y$ varies. For such a vector $u$, the vectors $V^n u$ are orthonormal. Vectors arising from different orthogonal $u$ are orthogonal at all grades by the isometry identity and $V^*u=0$. For $|z|<1$, the normalized sum $(1-|z|^2)^{1/2}\sum_{n\ge0}z^nV^n u$ is therefore a unit $z$-eigenvector of $V^*$, with infinitely many orthogonal choices.

Now $P=M_{\sqrt w}V$, and $M_{\sqrt w}-I$ is Hilbert–Schmidt since $\sum_{x\in X}(1-\sqrt{w_x})^2\le\sum_x t_x^2<\infty$. Compact perturbations send an orthonormal sequence to a norm-null sequence. The preceding vectors give an orthonormal approximate eigensequence of $P^*$ at every $|z|<1$, incompatible with Fredholmness there. Taking adjoints, using closure of the Fredholm essential spectrum and $\|P\|\le1$ proves the disk claim. On a cycle the normalized point masses span an invariant subspace of $P^*$, and the cyclic permutation has product weight $\lambda_C$. Its eigenvalues $\lambda_C^{1/p_C}e^{2\pi i j/p_C}$ lie inside this essential disk.

## A positive upper for the full Green kernel

Write $G(x,y)=\sum_{n:U^nx=y}\prod_{j<n}w(U^jx)$. The forward telescoping identity gives $G t\le1$, with equality on each cyclic basin and $G t(x)=1-F(x)<1$ on an escaping path. Here $F$ is the infinite survival product, strictly positive on every simple path by reciprocal packing. On function values $P^*$ is the reverse Markov kernel $Q(y,x)=a_xw_x/a_y$ for $Ux=y$. The adjoint Green potential is

\[
             G^*t(y)=\mathbb E_y^Q\sum_{n\ge0}t(X_{-n}).                 \tag{4}
\]

A nonperiodic root has a simple reverse path. At a periodic root $y\in C$, the number of complete initial laps before the path leaves the cycle has the geometric law on $k\ge0$ with weights $(1-\lambda_C)\lambda_C^k$: the product of $Q$ along a lap telescopes to $\lambda_C$. After removing the complete laps the remaining reverse sequence visits each state at most once. Equation (4) is bounded uniformly by $K+\sup_C g_C\lambda_C/(1-\lambda_C)<\infty$, since each complete lap has $\sum_{C}t_x\le g_C$. This argument counts every ordinary off-cycle parent under its actual probability.

The Schur test with comparison function $\sqrt t$ gives a uniform bound for the operators in (2), since the two Schur quotients are bounded by $Gt$ and $G^*t$. The entrywise limiting positive kernel is $L(x,y)=\sqrt{t_x}\,G(x,y)\sqrt{t_y}$ in function coordinates. For nonnegative inputs monotone convergence and dominated convergence in $\ell^2(a)$ give the strong limit; positive and negative real and imaginary parts cover general inputs.

Let $G^0(x,y)$ retain only the first visit from $x$ to $y$. Then $L^0=M_{\sqrt t}G^0M_{\sqrt t}$ is compact. In fact, with $Q_N$ projecting on $x>N$, both Schur quotients for $Q_NL^0Q_N$ are at most $KN^{-\sigma}$. In the forward field one sums $t$ only over distinct large sites. In the reverse field one counts up to, and excluding, the first positive return to the root. Until that return the reverse path is simple, also when it leaves a periodic root for good. Visits to smaller sites need not be excluded from the intervening path. Since $L^0-Q_NL^0Q_N$ has rank at most $2N$, its singular numbers satisfy $s_n(L^0)\ll n^{-\sigma}$.

The first-visit operator is in fact Hilbert–Schmidt. Its squared normalized-basis coefficient on a first-hit pair $x\to y$ equals $(a_x/a_y)t_xt_y A_{xy}^2$, where $A_{xy}$ is survival on that path. If $y\ge x$, (1) implies $a_x A_{xy}\le a_y$. Summing these terms at fixed $x$ costs at most $K t_x x^{-\sigma}$ by forward simple-path packing. If $x>y$, the factor $a_x A_{xy}/a_y$ is the probability of this reversed prefix under $Q$, and $A_{xy}\le1$. Summing first-hit terms at this fixed $y$ costs at most $K t_y y^{-\sigma}$ by reverse simple-path packing up to the first return to the root. Thus

\[
       \|L^0\|_{\mathcal S_2}^2\le 2K\sum_{x\in X}t_x x^{-\sigma}<\infty.     \tag{4a}
\]

## Principal contribution and compact remainder

The ordered rows and columns of a fixed basin $B_C$ form an orthogonal component block. For $x\in B_C$ let $e(x)$ be its first cycle entry and $A_x$ the survival from $x$ to $e(x)$, including $A_x=1$ on the cycle. Write $w_{e,y}$ for survival on the simple cyclic segment from $e$ to $y$; $\lambda_C\le w_{e,y}\le1$. The only repeated-target columns are $y\in C$, on which

\[
 (L-L^0)(x,y)=\frac{\lambda_C}{1-\lambda_C}
        \sqrt{t_x} A_x w_{e(x),y}\sqrt{t_y}.                             \tag{5}
\]

Replacing $w_{e(x),y}$ by one defines a nonnegative rank-one operator $J_C$ on that basin. Entrywise $\lambda_C J_C\le (L-L^0)|_{B_C}\le J_C$. Thus $J_C$ is bounded uniformly by $\|L\|/\inf\lambda_C$, by domination on this weighted lattice. Its error in (5) has norm at most $(1-\lambda_C)\|J_C\|$. Put $S_C=\sum_{y\in C}t_y$ and replace the prefactor $\lambda_C/(1-\lambda_C)$ in $J_C$ by $1/S_C$, obtaining an idempotent $E_C$. Indeed $A_y=1$ on $C$. Since $1-\lambda_C\le S_C\le g_C$ and $g_C\to0$ along distinct cycles by packing and their increasing cycle minima, $\lambda_C S_C/(1-\lambda_C)\to1$. The idempotents are uniformly bounded. Their orthogonal component sum $E=\bigoplus_C E_C$, zero on the escaping components, obeys

\[
                      L-E\text{ is compact}.                             \tag{6}
\]

The errors for finitely many basins have finite rank in (5), and the remaining block norms tend to zero. This proves (6) after adding $L^0$. In particular the Fredholm essential spectrum of $L$ is $\{0\}$ if there are finitely many cycles and $\{0,1\}$ if there are infinitely many. The complementary space to the range of $E$ is infinite-dimensional: even the fixed cycle has infinitely many ordinary off-cycle parents.

There is also a Hilbert–Schmidt refinement of (6). The pointwise absolute error in (5) after the first replacement is dominated by $(1-\lambda_C)J_C$. An entrywise majorant bounds the Hilbert–Schmidt norm in the normalized point-mass basis. The rank-one norm of $J_C$ is uniformly bounded, so this error is $O(g_C)$ in that ideal. The normalization changing $J_C$ into $E_C$ costs $O(g_C)$ there as well, by $1-\lambda_C\le S_C\le g_C$. The simple-path packing already bounds $\sum_C g_C^2$: $S_C^2\le2\sum_{x\in C}t_x\sum_{y\in C,\,y\ge x}t_y\le2K\sum_{x\in C}t_xx^{-\sigma}$, $g_C\le(4/3)S_C$ since $t_x\le1/4$, and the cycles are disjoint. Squaring and summing over disjoint components and using (4a) proves $L-E\in\mathcal S_2$.

## The gap and the actual projection

Separate nonperiodic sites $T$ from the union of cyclic sites $Z$. On $\mathcal H_T\oplus\mathcal H_Z$, the operator is upper block triangular. The compression to $T$ is compact, since it is the compression of $L^0$. Each finite-height compression there is triangular in any linear extension of proper forward reachability and has exactly the diagonal values $t_x$. These finite compressions converge in norm by compactness. If the compact limiting operator had a different nonzero spectral value, its isolated nonzero Riesz projection would persist for all sufficiently large finite compressions, a contradiction. Thus its spectrum is contained in $\{0\}\cup\{t_x:x\in T\}$.

The $Z$ compression is the direct sum of the finite cycle matrices, each similar by $M_{\sqrt t}$ to the stochastic matrix $K_C=(I-P_C)^{-1}M_t$. Its row at $x$ has entries $w_{x,y}t_y/(1-\lambda_C)$. It dominates $\lambda_C$ times the common probability vector $t_y/S_C$. Subtracting this row kernel and dividing by $1-\lambda_C$ gives a stochastic matrix. On zero-mass signed row vectors the resulting total-variation contraction is at most $1-\lambda_C$ (also for complex vectors). Consequently the principal eigenvalue is simple and every other eigenvalue has modulus at most $1-\lambda_C$. The characteristic polynomial can equivalently be obtained as $[\prod_{x\in C}(z-t_x)-\lambda_C z^{p_C}]/(1-\lambda_C)$.

There is no extra direct-sum spectrum away from zero and one beyond the closure of these finite eigenvalues. On a sequence of distinct cycles, the compression of $L^0$ to cyclic sites tends to zero in norm because their minima tend to infinity. The other compression approaches its uniformly bounded rank-one idempotent by (5)–(6). For each fixed $z\notin\{0,1\}$ the inverses of $z-E_C|_C$ are uniformly bounded by the elementary idempotent resolvent formula. A Neumann argument controls all sufficiently large cycles. This proves (3) with the triangular resolvent formula. The numerical specialization uses $\sup_x t_x\le1/4$ and $\inf_C\lambda_C\ge3/4$.

The isolated eigenvalue $1$ is semisimple even if it has infinite multiplicity. For the cyclic-site direct sum its Riesz projection is blockwise the finite principal projection, and the operator equals the identity on that range. For the whole triangular matrix let $A$ be the transient block, $B$ its off-diagonal block, and $D$ its cyclic-site block. Its principal projection has lower block the projection $\Pi_D$ of $D$, upper right $(I-A)^{-1}B\Pi_D$, and remaining blocks zero. This follows either from the contour resolvent or by expanding $(z-D)^{-1}=\Pi_D/(z-1)$ plus a holomorphic term near one. The uniform bounds above justify the direct-sum expansion; equivalently the restriction to the complementary finite-block subspaces has spectrum in $|z|\le1/4$ by the same idempotent approximation. The spectral-radius formula gives the claimed power rate.

More explicitly write $f(x)=\sqrt{t_x}\,u(x)$. If $Lf=f$, the identity $u=G(tu)$ and splitting the first step give $u(x)=t_xu(x)+w_xu(Ux)$, hence $u(x)=u(Ux)$. The positive bounded kernel gives absolute convergence for each coordinate of the split. On an escaping component the constant must vanish, since $Gt<1$ there. On a cyclic basin it is arbitrary, since $Gt=1$. The vector $\sqrt t\,\mathbf1_{B_C}$ belongs to $\mathcal H$: the bounded rank-one kernel in (5) after replacing $w_{e,y}$ by one has output proportional to $\sqrt t A$ on the basin, and simple-path packing gives $A_x\ge c>0$. Distinct cyclic basins give orthogonal eigenvectors.

The stationary row of $K_C$ is $\mu_C(y)\propto t_y/w_y=1/(3y)$ on $C$. Indeed if $\mu K_C=\mu$ then $\mu M_t^{-1}M_w$ is invariant for the deterministic cycle permutation, hence constant on $C$. The unique extension of its principal mode to the rest of the basin yields

\[
 (\Pi f)(x)=\sqrt{t_x}\sum_{y\in C}\mu_C(y)\frac{f(y)}{\sqrt{t_y}}
           \quad(x\in B_C),\qquad (\Pi f)(x)=0\quad(x\text{ escaping}).   \tag{7}
\]

The common contour separating one from both complementary spectra yields $\Pi-E\in\mathcal S_2$ from $L-E\in\mathcal S_2$ and the resolvent identity. In particular the entire nonprincipal operator $L-\Pi$ is Hilbert–Schmidt, even if the unknown principal multiplicity is infinite. For $n\ge1$ the exponential convergence holds in Hilbert–Schmidt norm by multiplying $L-\Pi$ by $(L-\Pi)^{n-1}$; for $n\ge2$ the difference is trace class. These are unconditional estimates on full off-diagonal as well as diagonal entries.

This gives exponential convergence in the number of successive potential killing events. An event count can cover arbitrarily many physical odd steps, so the operator norm bound does not bound the physical-time diagonal moment $\mathcal J$. Norm convergence in the single physical-time cutoff (2) would force compactness, since each $r<1$ operator there is compact. The source-independent norm bound and strong convergence in (2) alone permit infinitely many principal modes.

The [finite Lean kernels](GreenSpectralKernels.lean) check signed zero-mass contraction for arbitrary finite stochastic matrices with a common lower row, principal-edge constancy, the cleared resonant imaginary numerator, and the physical reciprocal-height stationary weight. The [exact finite arithmetic controls](check_green_spectrum.py) check the ordinary integer Green matrix and determinant sections, rational-cycle stochastic laws and characteristic polynomials, and the signed resonance numerator. [Recorded counts](../../../reports/astra-global-20261128/cycles/GREEN_SPECTRUM.json)
