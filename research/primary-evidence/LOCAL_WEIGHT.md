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

## An obstruction to deducing physical cone decay from positivity alone

A deterministic comparison system separates the physical implications. On positive integers send $2^j$ to $2^{j+1}$ and every other $n$ to $\lfloor n/2\rfloor$. Every orbit joins the powers of two within $\log_2 n$ steps and then escapes. Each orbit visits each dyadic shell at most twice, so the reciprocal tail over visited states above $H$ is $O(1/H)$ uniformly. On the shell $[2^k,2^{k+1})$, the upper half has second binary digit one and first joins the spine at $1$. The proportion whose first spine point exceeds $2^h$ is at most $2^{-h}+O(2^{-k})$, by inspecting the initial zero digits after the leading one. Thus minima are tight in logarithmic density and a positive proportion of starts reach the same fixed seed in logarithmic time.

Assign the one-step positive correction $v(n)=n/(n+1)$ and put $V_Q(x)=\prod_{i<Q}v(T^ix)$. Set $J(x,Q)=T^Qx\,V_Q(x)/x$ and $F=T^Qx-Jx$. This gives positive slopes and offsets, exact multiplicative composition of slopes, and $F/T^Qx=1-V_Q(x)$. The uniform reciprocal bound implies $V_Q\ge c>0$. Among $x\le2^{Q/2}$ in the upper half of their dyadic shells, the path visits $1$ before $Q$, so $1-V_Q\ge1/2$. Consequently $Q^{-1}\sum_{x\le2^Q} V_Q(x)(1-V_Q(x))/x$ has positive lower limit. The graph also has bounded fixed-target length-$q$ weighted mass: off-spine predecessors at a fixed depth are contained in one interval $[2^qt,2^q(t+1))$; for a spine target $t=2^j$, split according to its at most $j+1$ possible initial spine-entry vertices and their fixed distances to $t$, and include starts on the spine. These bounds are uniform in depth at each fixed target.

This example omits the Syracuse inverse-word congruences and its stationary ternary measure. It shows specifically why positive physical descendant weights, uniform reciprocal summability, fixed-target boundedness and timely small minima cannot on their own imply vanishing of the distortion cone. A proof of that vanishing needs further information about the actual arithmetic map.
