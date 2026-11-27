# Signed transport on the ordinary Collatz graph

**PROPOSED written operator theorem. Escaping components and nontrivial positive cycles remain open.** A signed sum of source masses has an exact obstruction to cancellation at unbounded ordinary endpoints. A finite source whose obstruction vanishes has a finite transport witness. The component labels below are mathematical quantities with unknown values.

## O1. The operator and its ordinary boundary

Use the positive shortcut map $T(2n)=n,\ T(2n+1)=3n+2$. Put $\gamma(n)=1$ on even inputs and $\gamma(n)=3n/(3n+1)$ on odd inputs. Fix $s>0$. On $\ell^1(\mathbb N_{>0})$ use the positive contraction
\[
       P\delta_x=\gamma(x)^s\delta_{Tx},\qquad
       G_k(x)=\prod_{0\le j<k}\gamma(T^jx)^s .
\]
Write $G_\infty(x)=\lim_k G_k(x)$. A nonrepeating positive orbit tends to infinity and has a summable reciprocal series, so $G_\infty(x)>0$ there. On an eventually periodic orbit a circuit includes an odd step, so its strictly contracting product gives $G_\infty(x)=0$. Write $\mathcal E$ for the escaping components. Two escaping positive integers represent the same component if their forward trajectories meet at possibly different clocks.

For any signed or complex $\ell^1$ charge $q$, put
\[
       (\Pi q)_C=\sum_{x\in C}q(x)G_\infty(x),\qquad C\in\mathcal E .
\]
There is a Banach-space isometry
\[
  \ell^1/\overline{(I-P)\ell^1}\ \cong\ \ell^1(\mathcal E),\qquad
  \inf_z\|q-(I-P)z\|_1
     =\|\Pi q\|_1
     =\lim_{N\to\infty}\left\|N^{-1}\sum_{k<N}P^kq\right\|_1 . \tag{1}
\]
The finite version is algebraic. If $q$ has finite support and $(\Pi q)_C=0$ for all $C\in\mathcal E$, then $q=(I-P)z$ for a finitely supported $z$. Deciding those componentwise equalities is an independent issue.

**Proof.** The factorization $G_\infty(x)=\gamma(x)^sG_\infty(Tx)$ gives $\Pi P=\Pi$ and $\|\Pi\|\le1$. On a length-$k$ path the explicit chain $z=\sum_{j<k}G_j(x)\delta_{T^jx}$ has boundary $\delta_x-G_k(x)\delta_{T^kx}$. Move finitely many sources in a component along actual paths to one common vertex $v$. On a periodic component choose $v$ on its cycle. For cycle length $p$, the one-circuit chain divided by $1-G_p(v)>0$ has boundary $\delta_v$. This removes the entire finite charge on that component.

On an escaping component the charge remaining at a common $v$ is $(\Pi q)_C/G_\infty(v)$. Its denominator tends to one on the forward tail by convergence of the infinite product. This gives exact cancellation at zero. Advancing $v$ independently on the finitely many involved components gives the upper quotient-norm bound for finite charges. The contraction lower bound and density of finite charges give the norm identity for all $q$. For surjectivity, given $z\in\ell^1(\mathcal E)$, choose one $v_C$ per nonzero coordinate with $G_\infty(v_C)\ge1/2$, and put $q(v_C)=z_C/G_\infty(v_C)$. Finally the Cesàro operators $A_N=N^{-1}\sum_{k<N}P^k$ are contractions, $\Pi A_N=\Pi$, and $\|A_N(I-P)z\|_1\le2\|z\|_1/N$. Approximation by boundaries now proves the last equality in (1).

The summability input follows from Garcia and Tal's uniform translated-interval collision estimate and dyadic summation. Their map specializes to the displayed shortcut. Their Lemma 3 forces an equal-clock collision at $h=\lfloor\log_2 X\rfloor$ among more than $K X^\theta\log(2X)$ points in any translated length-$X$ interval, for absolute $K>0,\theta<1$. On an infinite orbit $T^h$ is injective. On an eventually periodic orbit remove the last at most $h$ transient vertices before cycle entry. The remaining transient vertices have distinct noncyclic images and $T^h$ permutes the cycle. Thus, increasing $K$ if necessary, $|{\rm Orb}(x)\cap I|\le K X^\theta\log(2X)$ for every starting integer and every translated interval. Dyadic summation gives $\sum_{y\in{\rm Orb}(x)}1/y<\infty$ over distinct positive states. The quantitative uniformity uses Lemma 3 and its proof, in addition to the paper's qualitative Corollary 1. [Garcia and Tal, *A note on the generalized 3n+1 problem*, Acta Arith. 90 (1999), pp. 245–250, Lemma 3 and equation (6)](https://matwbn.icm.edu.pl/ksiazki/aa/aa90/aa9033.pdf)

## O2. First hits and ordinary traces

Write $\tau(x,y)$ for the first nonnegative $T$-clock at $y$, when it exists. Define
\[
     Kq(y)=\sum_{x:\,\tau(x,y)<\infty}q(x)G_{\tau(x,y)}(x).
\]
The norm from $\ell^1$ to $\ell^\infty$ is at most one. For $q(x)=x^{-s}$ with $s>1$, this gives the normalized first-hit version of the pre-existing Green series. To include later visits to a periodic target, divide by $1-G_p(y)$. Earlier work already proves pointwise finiteness and the Haar-versus-ordinary obstruction for the full unnormalized series. [Prior Green construction](../../astra-universal-step-20261124/descent.md)

For each escaping component choose any of its forward rays $R_C$. In $\ell^\infty/c_0$, where $c_0$ means vanishing at ordinary integer infinity, there is a norm-convergent identity
\[
       [Kq]=\sum_{C\in\mathcal E}(\Pi q)_C[1_{R_C}]. \tag{2}
\]
A single source on a finite orbit has a finite column. For an escaping source the column is zero off its own ray and its successive on-ray values tend to $G_\infty(x)$. Two rays in one component agree beyond finite prefixes. Since $\sum|q(x)|<\infty$, uniform approximation by finite charges proves (2). Different components have disjoint rays, so the quotient norm of the trace is $\sup_C|(\Pi q)_C|$. Along every actual escaping forward ray $Kq(y)$ tends to its component coefficient.

Zero is also a cluster value at ordinary infinity. For $y=3n$ its only shortcut predecessors are $2^j y$, since an odd shortcut endpoint is never divisible by three. Hence $|Kq(3n)|\le\sum_{x\ge3n}|q(x)|\to0$. The complete cluster set is $\{0\}\cup\{(\Pi q)_C:C\in\mathcal E\}$. The nonzero coefficients can accumulate only at zero. Therefore for $\eta>0$ distinct from all their moduli, $\{y:|Kq(y)|>\eta\}$ differs by finitely many positive integers from the union of the finitely many chosen rays with $|(\Pi q)_C|>\eta$.

There are two unconditional bounds at the actual ordinary endpoints:
\[
  \sum_{y\in I}|Kq(y)|\le K_0\|q\|_1 X^\theta\log(2X),\qquad
  K(I-P)q(y)=(1-\lambda_y)q(y).
\]
Here $\lambda_y=0$ off cycles and $\lambda_y=G_p(y)$ on a cycle of primitive length $p$. The first inequality sums the absolute contributions by source and uses O1. In the identity, each source $x\ne y$ contributes equally to $Kq(y)$ and $KPq(y)$ by stripping its first edge. For $x=y$ the first term has coefficient one and the second has its first-return coefficient $\lambda_y$. A genuine signed boundary charge therefore has a uniformly vanishing first-hit trace, even when the separate positive terms could retain a moving atom.

## O3. Noncommuting edge weights

Let $H$ be a nonzero complex Hilbert space. Attach an arbitrary unitary $V_x$ to every actual edge $x\to Tx$. Set $P_V(\delta_x v)=\gamma(x)^s\delta_{Tx}V_xv$ on $\ell^1(\mathbb N_{>0};H)$. The Banach quotient by $\overline{(I-P_V)\ell^1}$ is still isometric to $\ell^1(\mathcal E;H)$.

On an escaping component choose an anchor $a$. If $x,a$ reach a common $z$, write $V(x,z)$ for the chronological edge product and set $J_x=V(a,z)^{-1}V(x,z)$. Advancing $z$ multiplies both products on the left by the same unitary. Thus $J_x$ is well defined, and $J_x=J_{Tx}V_x$ conjugates the transport to $P$ on this component. The one-circuit operator on a cycle is $\lambda_y U$ for some unitary $U$, and $I-\lambda_y U$ is invertible by a norm-convergent geometric series. Its inverse gives one coefficient vector at a vertex of the finite cycle. The finite transport and truncation proof of (1) now applies with $(\Pi_V q)_C=\sum_{x\in C}G_\infty(x)J_xq(x)$.

In particular, for any unit vector $v$ and any single fixed escaping source $x$,
\[
   \left\|N^{-1}\sum_{k<N}P_V^k(\delta_xv)\right\|_1
      =N^{-1}\sum_{k<N}G_k(x)\longrightarrow G_\infty(x)>0. \tag{3}
\]
Different times occupy different actual positive vertices, so their contributions cannot cancel in this norm. This holds even if summation over those vertices nearly cancels the associated scalar phases. A legal path compressed into a new edge receives the product of the original edge maps in this calculation. Independently assigned extra edges need their own relation to the actual system.

**Open step.** To exclude escape with (1) it would suffice to prove that one $\ell^1$ charge positive at every source belongs to $\overline{(I-P)\ell^1}$. The finite primitives handle verified collisions and cycles. No component-independent construction here proves that a positive charge has zero residual norm. Formula (3) explains why a unitary twist supported solely on legal edges cannot furnish that conclusion. The contraction on a cycle treats the known positive cycle and any possible additional positive cycle in the same manner.

[WeightedTransport.lean](WeightedTransport.lean) proves the finite path, simultaneous signed collision, cycle inverse, ordinary positive-cycle contraction and eventual membership of a fixed source in a merging orbit tail. It uses ordinary shortcut edges and rational weights, with the concrete distortion instantiated at $s=1$. The infinite Banach-space and vector-valued assertions above are written proofs.
