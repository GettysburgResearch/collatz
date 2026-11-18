# Scale-uniform local estimates for the Syracuse density

**PROPOSED.** Let $\lambda$ be Haar probability on $\mathbb Z_3$ and let $g=d\mu/d\lambda$ be the stationary geometric-word Syracuse density, supported on $U=\mathbb Z_3^\times$. Denote by $B=t_0+3^q\mathbb Z_3$ a unit cylinder, $q\ge1$, and put $g_B=\lambda(B)^{-1}\int_Bg=g_q(t_0)>0$. For any convex nonnegative Borel function $\Phi$ on $[0,\infty)$,
$$
 \frac1{\lambda(B)}\int_B\Phi(g/g_B)\,d\lambda\le\int_{\mathbb Z_3}\Phi(g)\,d\lambda. \tag{1}
$$
There is an absolute $c>0$ such that
$$
 \operatorname*{ess\,inf}_B g\ge c g_B. \tag{2}
$$
Thus on the unit space the density is a Muckenhoupt $A_1$ weight with uniform reverse Hölder estimates of all orders $1<p<2$. The threshold $p=2$ fails on every unit cylinder. El Jaouhari proves the global $L^p$ threshold and essential unboundedness on each unit cylinder. Here the point is the uniform local normalization by $g_B$. [El Jaouhari](https://doi.org/10.5281/zenodo.23377671)

Indeed let $w$ range over all inverse-order words of length $q$ compatible with $t_0$. For $S_w=\sum a_i$ and $J_w=3^q2^{-S_w}$ write $r_w=(t_0-\beta_w)/J_w\in\mathbb Z_3$. Stationarity and change of variables give
$$
 g(t_0+3^q u)=\sum_w J_w g(r_w+2^{S_w}u)\quad\text{for Haar-a.e. }u.
$$
Each affine argument preserves Haar probability in $u$. The coefficients $J_w/g_B$ sum to one. Jensen and integration give (1), including the case of an infinite right side. Taking $\Phi(v)=v^p$ gives the stated reverse Hölder inequalities. Conversely a single compatible word with positive coefficient makes the $L^2$ integral infinite since its Haar-isometric copy of $g$ already has divergent second moment. There is a compatible word on every unit cylinder by the natural atom floor. The same representation gives
$$
 \frac{\mu(E)}{\mu(B)}\le \sup_{\lambda(A)=\lambda(E)/\lambda(B)}\int_A g\,d\lambda
$$
for every measurable $E\subset B$. In particular the entire small-set modulus of the global density transfers uniformly inside every ball.

For (2), the [unconditioned selected floor](FIXED_PRECISION.md) gives $g_j(z)\ge c_0$ on every unit for all sufficiently large $j$. For each word of length $q$ compatible at $t$, its source $r=(t-\beta_w)/J_w$ is either a unit or else $4r+1$ is. In the second case increasing the innermost valuation by two gives exactly the new source, with the same image after one step and a factor-four smaller slope. There are at most two original words for each resulting word. Prefixing all possible $j$-step histories gives $g_{q+j}(t)\ge(c_0/8)g_q(t)$ pointwise. On $B$, $g_q=g_B$ is constant. Martingale convergence of $g_{q+j}$ yields (2) with $c=c_0/8$. On the whole unit space, the positive uniform lower floor controls the one remaining root ball. The weight vanishes on the nonunit ball, so the $A_1$ statement is made on $U$.

The local estimates control masses of measurable subsets of a ball, including ratios of finite-depth masses. They still allow exceptional arithmetic centers: at $s_a=-2^{1-a}$ the published negative-start construction gives $\mu(B_{n+1}(s_a))\ge2^{-a-n}$. No upper bound on the limiting ordinary ratio $g(t)/t$ along a moving positive orbit follows from (1) or (2).
