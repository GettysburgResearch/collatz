# Linear independence at a regular point of a one-variable p-adic Mahler system

**Proposed finite-place adaptation of Adamczewski and Faverjon.** Let $k\ge2$, fix a number field inside $\mathbb C_p$, and let $f=(f_1,\ldots,f_m)^t$ be convergent power series at zero with coefficients in that field. Suppose $f(z)=A(z)f(z^k)$, with $A$ invertible over the field of rational functions. Suppose the $f_i$ are linearly independent over $\overline{\mathbb Q}(z)$. If $\alpha\ne0$ is algebraic, $|\alpha|_p<1$, its iterates lie inside the common disk of convergence, and $A$ and its inverse have no poles at any $\alpha^{k^j}$, then $f_1(\alpha),\ldots,f_m(\alpha)$ are linearly independent over $\overline{\mathbb Q}$ in the chosen completion.

We use the relation ideal and auxiliary polynomial construction of Adamczewski–Faverjon for complex values. The finite-place upper bound below uses a single closed disk, multiplicativity of its Gauss norm, and the fact that the entire disk has constant absolute value. The algebraic regularity input is their univariate formal lemma, independent of the completion. [Adamczewski–Faverjon, *A new proof of Nishioka’s theorem in Mahler’s method*, Sections 2.2–2.4](https://doi.org/10.5802/crmath.458) · [Adamczewski–Faverjon, *Méthode de Mahler: relations linéaires, transcendance et applications aux nombres automatiques*, Lemma 3.2](https://doi.org/10.1112/plms.12038)

## The algebraic construction

Suppose a nonzero algebraic row $\tau$ satisfies $\tau f(\alpha)=0$. Fix a number field $K$ containing all system coefficients, $\alpha,\tau$, and the coefficient field of $f$. Put $z_j=\alpha^{k^j}$ and $B_j=A(\alpha)\cdots A(z_{j-1})$, with $B_0=I_m$. For an indeterminate $m$-square matrix $Y$, use the ideal $I\subset K(z)[Y]$ of polynomials vanishing at $(B_j,z_j)$ for every sufficiently large $j$. It is radical, contains no nonzero element of $K(z)$ and does not contain $\det Y$. Rational function evaluations are well-defined eventually because the $z_j$ are distinct. By the Nullstellensatz there is an invertible matrix $\phi(z)$ over $\overline{K(z)}$ annihilating all of $I$. For each $P\in I$ and $t\ge0$ the polynomial $P(Y A_t(z),z^{k^t})$ belongs to $I$, where $A_t(z)=A(z)\cdots A(z^{k^{t-1}})$. Indeed its $j$th evaluation equals the $(j+t)$th evaluation of $P$. Thus
$$
P(\phi(z)A_t(z),z^{k^t})=0.                                             \tag{1}
$$

Choose a fixed large $j_0$ with $\xi=z_{j_0}$ outside the finite set of branch points, poles of the entries and zeros of the determinant of $\phi$. A place over $z=\xi$ gives algebraic analytic germs there for its entries: use a primitive element in the finite separable extension they generate, avoid the discriminant and denominators, and apply the local implicit function theorem to a simple root. Enlarge $K$ once to contain the entries of $\phi(\xi)$ and put $C=B_{j_0}\phi(\xi)^{-1}$. The enlarged relation ideal is obtained by extending scalars: after clearing denominators, expand coefficients in a basis of the enlarged number field over the original one; the point coordinates lie in the original field. Consequently (1) remains valid over the enlarged field. This choice of number field precedes all auxiliary degrees.

Set $\Theta_t=C\phi(z)A_t(z)$ and $F(Y,z)=\tau Y f(z)$. As germs about $\xi$ we have
$$
 F(\Theta_t,z^{k^t})=F(C\phi(z),z)=:F_*(z),\qquad
 \Theta_t(\xi)=B_{j_0+t}.
$$
The germ $F_*$ is nonzero. Indeed, the univariate formal regularity lemma states that $\overline{\mathbb Q}(z,f)$ is regular over $\overline{\mathbb Q}(z)$. To apply it at $\xi$, identify the generated function field with its field of germs there: a polynomial combination of the convergent series with polynomial coefficients that vanishes on an entire subdisk is identically zero on the original disk, by the one-variable nonarchimedean identity theorem (or Strassmann on any smaller closed disk containing $\xi$). A regular extension is linearly disjoint from an algebraic closure of its base, also in this germ realization. Thus the $f_i$ remain linearly independent with algebraic-function coefficients. The row $\tau C\phi$ is nonzero by invertibility.

Let $V(D,H)$ be the polynomials of total $Y$-degree at most $D$ and $z$-degree at most $H$. Write $r_D$ for the rank over $K(z)$ of all monomials of total degree at most $D$ modulo $I$. Then
$$
r_D(H+1)\le \dim_K V(D,H)/(V(D,H)\cap I)\le r_D(H+c_D+1).
$$
For the lower bound take the $z$-multiples of a monomial basis. For the upper bound express all the monomials in that basis over $K(z)$ and clear their common denominator with numerator degrees at most $c_D$. Also $r_{2D}\le C_m r_D$ for a constant depending only on $m$. Indeed, for $h=m^2$ and $D\ge2h$ reduce the exponents modulo $\lfloor D/h\rfloor$. The remainder monomial has degree at most $D$, and the possible quotient vectors have at most $(4h+1)^h$ choices. This use of total degree preserves $V(D,H)$ under $Y\mapsto CY$.

Let $J$ be the pullback of $I$ under $P(Y,z)\mapsto P(CY,z)$, so the same dimension bounds apply to $J$. For large fixed $D$ take $H$ sufficiently large relative to $D,c_{2D}$, and $s=\lfloor DH/(4C_m)\rfloor$. Choose a complement of $I\cap V(D,H)$ in $V(D,H)$. There exist polynomials $P_0,\ldots,P_D$ in that complement, not all zero, for which the truncation to powers $z^n$ with $n<s$ of
$$
 \mathcal E(Y,z)=\sum_{a=0}^D P_a(Y,z)F(Y,z)^a
$$
belongs to $J$. In fact the source dimension is at least $(D+1)r_D(H+1)$ and the truncated target modulo $J$ has dimension at most $r_{2D}(s+c_{2D}+1)$. This gives a kernel over the fixed field $K$. By (1) the truncation vanishes identically upon substituting $(\Theta_t,z^{k^t})$ for $(Y,z)$.

## The local and global bounds

Fix a sufficiently small closed disk $\mathcal D$ about $\xi$ of positive radius less than $|\xi|_p$, on which $\phi$ is analytic. Every $z$ there has $|z|_p=|\xi|_p$. After shrinking the disk once, all $A(z^{k^i})$ are analytic on it. For large $i$ this follows directly from the absence of nonzero poles sufficiently near zero, and for the remaining finitely many $i$ it follows by regularity of $\xi$. If $v$ bounds the pole order of the entries of $A$ at zero, their disk norms after composition are at most $C_1|\xi|_p^{-v k^i}$ with one constant for all $i$. Thus in the disk Gauss norm, $\|\Theta_t\|\le\exp(C_2 k^t)$, for a fixed $C_2$ independent of $D,H,t$.

Fix a real radius $R>|\xi|_p$ strictly below the common radius of convergence. The finitely many coefficient series in $Y$ of $\mathcal E$ converge on $|z|_p\le R$. For each of them the tail after truncation at $s$ therefore has norm on $|z|_p\le|\xi|_p^{k^t}$ at most $C(D,H)(|\xi|_p^{k^t}/R)^s$, for $t$ large. Their total $Y$-degree is at most $2D$. Using the vanishing of the truncation on $\mathcal D$ gives
$$
 \|\mathcal E(\Theta_t,z^{k^t})\|
 \le \exp\big[-k^t(s\log(1/|\xi|_p)-2C_2D)+O_{D,H}(1)\big].
$$
Let $a_0$ be the smallest index with $P_{a_0}\ne0$ and write $E=\sum_{a\ge a_0}P_a F^{a-a_0}$. The left side equals $\|F_*\|^{a_0}\,\|E(\Theta_t,z^{k^t})\|$ by multiplicativity of the one-variable Gauss norm. Its first factor is positive and independent of $t$.

At $z=\xi$ we have $F(B_{j_0+t},z_{j_0+t})=0$. Consequently the last bound applies, up to a fixed factor, to the absolute value of $P_{a_0}(B_{j_0+t},z_{j_0+t})$. These values are nonzero infinitely often by $P_{a_0}\notin I$. They belong to the fixed number field $K$. Their absolute logarithmic heights are at most $C_3(D+H)k^t+O_{D,H}(1)$, with $C_3$ independent of $D,H$. Indeed $h(z_j)=k^jh(\alpha)$, and the affine matrix tuple $(1,B_j)$ has projective height $O(k^j)$ by multiplying the rational matrices: locally a product norm costs at most the product of the entry maxima, with the usual factor $m$ at infinite places. Summing the resulting rational-function height bounds gives $O(\sum_{i<j}k^i)=O(k^j)$. Polynomial evaluation then gives the asserted estimate. Local Liouville gives $-\log|b|_p\le[K:\mathbb Q]h(b)$ for nonzero $b\in K$.

It follows for infinitely many $t$ that $s\log(1/|\xi|_p)-2C_2D\le [K:\mathbb Q]C_3(D+H)+o(1)$. Since $s$ grows as $DH/(4C_m)$, first taking $D$ large and then $H$ sufficiently large contradicts the inequality. This proves the asserted linear independence.
