# A local weighted shift sees escape in point spectrum

**Status.** PROPOSED, with proofs. This is an actual attempt to distinguish escaping components from periodic ones by a single bounded operator. The distinction survives at the level of exact eigenvectors. An explicit family in the known basin refutes its proposed spectral-gap closure.

For $s>1$ on ordinary counting-measure $\ell^2(\mathbb N_{>0})$ put
$$
 (C_sg)(n)=c(n)^{s/2}g(Tn),\qquad c(n)=
 \begin{cases}1/2,&n\text{ even},\\ 3/2,&n\text{ odd}.\end{cases}
$$
Each row has one entry and each fiber at most two, so this is bounded. The weights are the parity-dependent affine slopes. They can also be obtained by transforming the physical composition operator on $\ell^2(n^{-s})$ to counting measure and dropping the compact correction between $(Tn/n)^{s/2}$ and $c(n)^{s/2}$. The following exact-mode argument requires a separate treatment of this correction.

## OP-S1. The entire circle, or no point on it

For every $|\lambda|=1$, $\ker(C_s-\lambda I)$ has one dimension per nonperiodic component and zero dimensions on each periodic component. Its full dimension is the Hilbert sum of these one-dimensional spaces. Independently of the Collatz conjecture,
$$
 \ker(C_s^*-\overline{\lambda}I)=\{0\}.
$$
Thus an ordinary escaping component exists if and only if one, or equivalently every, point of the unit circle is an eigenvalue of this particular local operator. Nontrivial positive cycles would contribute no such eigenvalue.

Write $e(n)=1$ for odd $n$ and zero otherwise, and
$$
 d(n)=\big(1+e(n)/(3n)\big)^{-s/2},\qquad
 Tn=n\,c(n)\big(1+e(n)/(3n)\big).
$$
On an acyclic component every forward trajectory is a simple ordinary path. The uniform reciprocal-sum bound on simple paths gives
$$
 a_s\le v(n)=\prod_{j\ge0}d(T^jn)\le1
$$
for a constant $a_s>0$. The same lower bound applies to any finite simple prefix. For example, use O2 at 2 to bound the sum of reciprocal odd departures since $\theta<1$, adding the possible one visit to 1. The earlier finite reciprocal theorem T-A3-651 also suffices. Choose a base vertex of the component and assign integer levels $t$ by $t(Tn)=t(n)+1$. This is consistent on the underlying tree. The function
$$
 g_\lambda(n)=\lambda^{t(n)}n^{-s/2}v(n)
$$
on this component, extended by zero elsewhere, is square summable and nonzero. The identity $v(n)=d(n)v(Tn)$ gives $C_sg_\lambda=\lambda g_\lambda$. On a connected component an eigenfunction for nonzero $\lambda$ is determined by any one value, by the nonzero edge relation. On a periodic orbit of length $k$ and odd weight $p$, a nonzero eigenvalue would have $\lambda^k=(3^p/2^k)^{s/2}$. For positive ordinary cycles the affine carry is positive, so $3^p/2^k<1$ (a positive cycle cannot be all even). This excludes unit-circle eigenvectors throughout that component.

For the adjoint, if $C_s^*u=\overline{\lambda}u$, the signed or complex sequence $\nu(n)=n^{-s/2}u(n)$ is in $\ell^1$ by Cauchy–Schwarz. Its coordinate equation is
$$
 \overline\lambda\,\nu(y)=\sum_{Tn=y} d(n)\nu(n).
$$
Therefore $\sum|\nu|\le\sum d(n)|\nu(n)|\le\sum|\nu|$. Equality forces $\nu$ to vanish at every odd integer. The triangle bound also has equality at every fiber, as its nonnegative losses sum to zero. If $|\nu(n)|>0$, it propagates with positive absolute mass to $Tn$, then to every subsequent point. Every positive integer eventually has an odd departure, which gives a contradiction. This proves the adjoint assertion for all components together and for each component restriction.

## OP-S2. Unit-circle continuous spectrum inside the known basin

Fix any $|\lambda|=1$. The restriction of $C_s-\lambda I$ to the known basin is injective with dense range by OP-S1. Its range is not closed. In particular zero belongs to the essential spectrum of the bounded self-adjoint local operator $(C_s-\lambda I)^*(C_s-\lambda I)$ on the known basin.

Use the explicit growing odd-prefix pairs $n_k,y_k$ in OP-H2 for odd $k\ge3$: $T^kn_k=y_k=2^{3^{k-1}}$, with $y_k/n_k\ge(3/2)^k$. The root $y_k$ lies off the cycle. On its full ordinary descendant subtree write $\ell(x)$ for the unique forward hitting time of $y_k$. Define
$$
 u_k(x)=\lambda^{-\ell(x)} x^{-s/2}
            \prod_{j<\ell(x)}d(T^jx),
$$
and zero elsewhere. It is in $\ell^2$, agrees with the eigenvector equation at every vertex except the root, and has residual of norm $y_k^{-s/2}$. Indeed every predecessor of a subtree vertex already belongs to that subtree, while the parent of $y_k$ lies outside. The source $n_k$ gives $\|u_k\|\ge a_s n_k^{-s/2}$. Thus the relative residual is at most $a_s^{-1}(2/3)^{sk/2}$. These normalized vectors converge weakly to zero: each fixed good integer has only finitely many distinct points in its forward orbit, and therefore is in only finitely many of the indicated subtrees. Weak convergence follows by testing finite-support vectors and using the uniform norm. Applying the adjoint shows the normalized sequence is singular Weyl for the squared operator. In particular actual unimodular eigenfunctions and arbitrarily accurate good-basin pseudoeigenfunctions cannot be distinguished by a uniform lower norm bound.

A second obstruction rules out a simple trace or normality inference from the adjoint calculation. The positive diagonal $C_s^*C_s$ has entry $2^{-s}+(3/2)^s1_{\{y\equiv2\bmod3\}}$, bounded below. Thus $C_s(C_s^*C_s)^{-1/2}$ is an isometry in the generated unital $C^*$-algebra. It is proper: for every branching fiber the vector with the two inverse-edge weights swapped and one sign reversed is orthogonal to the range. This happens at infinitely many powers of two in the known basin. A faithful finite trace on this algebra would equate the trace of the isometry's range projection with the identity, which is impossible. In particular the vanishing adjoint kernel cannot be converted to vanishing forward kernel by assuming a finite operator algebra.

The first unsupported inference remains exclusion of **exact** unit-circle point spectrum on the full ordinary space. The known component realizes the continuous alternative without any escaping behavior. Composition-operator antecedents include Leventides–Poulios' analysis of the ordinary Koopman operator; their state weights and operator normalizations differ from the principal affine slope weights above. [Primary paper](https://arxiv.org/abs/2010.12987)
