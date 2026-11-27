# The physical clock in every nonzero rational normalization

**PROPOSED written theorem.** Fix a positive odd rational $q_0=x_0/d$, where $x_0,d$ are positive odd integers. For its actual odd Collatz orbit put $a_j=v_2(3q_j+1)$, $q_{j+1}=(3q_j+1)/2^{a_j}$, $A_0=0$ and $A_j=\sum_{i<j}a_i$. For every $c\in\mathbb Q^\times$ and every integer $k\ge2$,

$$H_c(z)=\sum_{j\ge0}2^{A_j}c^jz^j\text{ is }k\text{-Mahler}\quad\Longleftrightarrow\quad(q_j)\text{ is eventually periodic}.\tag{1}$$

The quantifiers include each fixed base and each negative or positive rational normalization. Proving the Mahler assumption for a single pair $(c,k)$ for each ordinary starting integer would exclude escape. A separate cycle argument would still be needed.

**Prior inputs.** PR195's GS1 had already proved the rationality and D-finiteness equivalences for ordinary positive integral sources by applying Bell–Smertnig to the cumulative-clock coefficients. Rationality and D-finiteness transport under $z\mapsto cz$. The latest PR195 A2 applies Bost–Chambert-Loir to a physical orbit, proving the bound $2^{-s}$ on the archimedean conformal radius of any regular meromorphic continuation domain for its undilated series on an escape, where $s=\liminf A_j/j$. Its whole-circle natural-boundary conclusion assumes the mean clock exists. The argument below applies adelic continuation at *all* places to a hypothetical Mahler equation and uses the physical two-place argument at the two exceptional rational dilations. It allows the mean to oscillate. [PR195, GS1 at `a24ef018147a1e16bf314d14085e2d0d6c620d32`](https://github.com/GettysburgResearch/collatz/blob/a24ef018147a1e16bf314d14085e2d0d6c620d32/research/astra-global-closure-20261124/analytic/README.md) · [PR195, A1–A2 at `07aa5124f7ca482b6665d61355fac0af5f6e55b2`](https://github.com/GettysburgResearch/collatz/blob/07aa5124f7ca482b6665d61355fac0af5f6e55b2/research/astra-global-closure-20261124/closing/adelic/README.md) · [Companion physical two-place proof, §§1–2](proof.md)

## Local radii and the adelic criterion

Write $x_j=dq_j$. Exact normalization gives $2^{a_j}x_{j+1}=3x_j+d$, so the $x_j$ remain odd positive integers, whether or not the denominator divides out on the tail. On a nonperiodic source the sequence is injective by determinism, whence $x_j\to\infty$. Put $L_j=2^{A_j}x_j/3^j$. Then

$$L_j=x_0\prod_{i<j}\left(1+\frac d{3x_i}\right)\ge x_0,\qquad \log L_j=o(j).\tag{2}$$

The second assertion follows by Cesàro averaging since the logarithmic increments tend to zero. It follows from $x_j\ge1$ and $a_i\ge1$ that $1\le s=\liminf A_j/j\le t=\limsup A_j/j\le\log_2 3$. In the normalization $|p|_p=p^{-1}$ the local Taylor radii are

$$R_\infty(H_c)=2^{-t}/|c|,\qquad R_2(H_c)=2^s/|c|_2,\qquad R_p(H_c)=1/|c|_p\ (p\ne2).\tag{3}$$

These are direct Cauchy–Hadamard equalities, with no need for convergence of $L_j$. On escape $H_{1/2}$ is nonrational by the companion physical two-place proof; rational functions are Mahler in every base, and that proof excludes every base at $c=1/2$. Hence $H_c$ is nonrational for every nonzero rational $c$, since a rational change of variable preserves rationality in both directions.

**Adelic implication.** Suppose $H\in\mathbb Z[1/N][[z]]$ has strictly positive radii at all places and satisfies a $k$-Mahler equation. It extends meromorphically to the open unit disk at every place. Indeed isolate $H(z)$ using a nonzero polynomial leading coefficient and the finitely many higher iterates $H(z^{k^i})$. Starting on any smaller convergence disk of radius $r<1$, the quotient extends meromorphically to radius $r^{1/k}$. Repeating covers the open unit disk; the functions agree on overlaps by their common formal germ. This reasoning is valid on complex and on nonarchimedean analytic disks. For rational coefficients of $H$, a polynomial Mahler relation over $\overline{\mathbb Q}$ can be defined over $\mathbb Q$ by projecting its coefficients from their finite number field onto a rational component on which the leading coefficient survives.

If even one of the Taylor radii exceeds one, choose at that place an open centered disk of radius strictly between one and the Taylor radius (at $p$, choose the radius in $p^{\mathbb Q}$). At all other places take the open unit disk. This is an adelic tube adapted to $P=0$ on the geometrically connected smooth projective curve $\mathbb P^1_{\mathbb Q}$. It is the standard reduction tube at almost all finite places. The germ extends meromorphically on each disk by the preceding paragraph and analytically on the enlarged one. Its graph is A-analytic by condition $2'$ after Theorem 7.9 of Bost–Chambert-Loir: the formal coefficients are integral on $\operatorname{Spec}\mathbb Z[1/N]$ and the origin extends on the standard smooth model. The disk capacitary degree is the sum of the logarithms of the radii; equivalently their product is strictly greater than one. Theorem 7.9 therefore makes $H$ **rational**. Example 7.10 identifies this all-disk case directly with the Borel–Dwork rationality criterion. [Primary paper, Theorem 7.9, condition $2'$, and Example 7.10, printed pp. 48–49](https://arxiv.org/pdf/math/0702593)

## The two remaining rational dilations

Suppose $H_c$ were $k$-Mahler along a nonperiodic source. Its coefficients belong to $\mathbb Z[1/N]$ for a fixed $N$. The adelic implication and nonrationality force all three types of radii in (3) to be at most one. No odd prime may divide the reduced numerator of $c$, since that would give $R_p>1$. Since $|c|_2\ge2^s\ge2$, its reduced denominator is even. Thus $|c|=1/(2^a d')$ with $a\ge1$ and $d'$ odd positive. The real bound gives $|c|\ge2^{-t}\ge1/3$. The only surviving absolute value is $1/2$.

For both signs let $G_c(z)=\sum_{j\ge0}c^j2^{A_j}x_jz^j$. Then

$$(1-3cz)G_c=x_0+cdzH_c.\tag{4}$$

Mahler series in a fixed base are closed under rational-function affine combinations, by the finite-span criterion. Thus the assumed $H_c$ makes $G_c$ Mahler. Write $\lambda=1/(3c)=\pm2/3$. At the complex place (2) gives $G_c(\lambda u)=\sum L_j u^j\to+\infty$ as $u\uparrow1$ and its Taylor radius is $|\lambda|$. In every Mahler relation for $G_c$ the higher iterates are analytic near $\lambda$ because $|\lambda|<1$. Every possible leading polynomial vanishes at $\lambda$, so the genuine Mahler denominator does too. But $|\lambda|_2=1/2$, and Adamczewski–Bell–Smertnig, Proposition 6.4, forces the dyadic Taylor radius below one. The coefficients of $G_c$ are integers since $A_j\ge j$ and $c=\pm1/2$. This contradiction covers both signs directly. [Primary paper, Definition 3.9 and Proposition 6.4](https://adamczewski.perso.math.cnrs.fr/HeightMahler.pdf)

Finally an eventually periodic orbit has $A_{j+p}-A_j$ constant on its tail for a suitable period $p$, making $H_c$ rational by geometric summation. This proves (1). In general rational variable dilation does **not** preserve the Mahler property: $L(z)=\sum_{j\ge0}z^{2^j}$ satisfies $L(z)=z+L(z^2)$ and is nonrational, as its isolated nonzero coefficients have arbitrarily long intervening zero runs. The rational dilation $L(2z)$ stays nonrational but has dyadic radius two. The preceding adelic implication shows it is not Mahler in any base.
