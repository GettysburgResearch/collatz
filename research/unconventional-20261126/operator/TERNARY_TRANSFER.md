# Ternary incoming slopes and the ordinary escape end

**Status.** PROPOSED, with proofs. The positive transfer calculation arose jointly in the operator lane and root review. Its ordinary diagonal distinguishes escape, and its averaged law does not impose diagonal control. A separate first-passage result quantifies the Haar exceptional targets.

For $y\in\mathbb Z_3$ use inverse letters $E(y)=2y$ everywhere, $O(y)=(2y-1)/3$ at $y=2\bmod3$. Write $c_E=1/2$, $c_O=3/2$ for the multipliers in the **forward** direction. A legal inverse script $w$ with $k$ letters and $q$ copies of $O$ has incoming slope $C_w=3^q/2^k$. Include the empty script. Put
$$
 B(y)=\sup_{w\text{ legal at }y}C_w,\qquad
 W_s(y)=\sum_{w\text{ legal at }y}C_w^s.
$$

## OP-T1. Haar resolvent and the ordinary return factor

For the positive transfer
$$
 (\mathcal L_s f)(y)=2^{-s}f(2y)+(3/2)^s1_{y\equiv2(3)}f((2y-1)/3)
$$
normalized Haar integration gives $\int\mathcal L_s f=\lambda_s\int f$ for nonnegative measurable $f$, with $\lambda_s=2^{-s}(1+3^{s-1})$. The two maps act respectively by a Haar-preserving bijection and a bijection from the admitted cylinder with Haar mass $1/3$ onto the whole ring. Strict convexity of $\lambda_s$ and $\lambda_1=\lambda_2=1$ give $\lambda_s<1$ for $1<s<2$. Thus $W_s=\sum_{k\ge0}\mathcal L_s^k1$ has Haar integral $1/(1-\lambda_s)$ and satisfies $W_s-\mathcal L_sW_s=1$ almost everywhere.

At any ordinary $y>0$ all legal inverse letters preserve positive integrality. For a script reaching source $x$, positivity of the affine carry yields $C_w\le y/x$. If $y$ is off-cycle, each source occurs at most once, and $W_s(y)\le y^s\zeta(s)$ for every $s>1$. For a cyclic $y$, let $r<1$ be its forward lap slope. Every hitting source contributes its first-arrival term times $(1-r^s)^{-1}$, since subsequent arrival slopes acquire successive factors of $r$. In every case $W_s(y)<\infty$, and $B(y)$ is a maximum. Indeed its candidates of slope at least one have $x\le y$; one need only take the earliest arrival of each such source.

## OP-T2. Ordinary diagonal limits and positive escape

The following limit over the ordinary integers is equivalent to absence of escaping components:
$$
                          B(y)/y\longrightarrow0.
$$
For fixed $\epsilon>0$, if $B(y)\ge\epsilon y$, then a maximizing source lies in the finite range $x\le1/\epsilon$. If every forward trajectory is finite, only finitely many such targets occur.

For the converse take an escaping component $D$ and its $L$ from [OP-D1](HYBRID_DESCENT.md). Every nonempty finite forward prefix there is simple. Write $A(y)$ for the full ancestor set of $y$, including $y$. The cocycle identity gives the exact formulas
$$
 B(y)=\frac{L(y)}{\min_{x\in A(y)} L(x)},\qquad
 W_s(y)=L(y)^s\sum_{x\in A(y)}L(x)^{-s}\quad(s>1).
$$
Choose any $y_j=T^j a$ on that component. These nested ancestor sets exhaust $D$, because every pair of vertices has intersecting forward trajectories. A globally minimizing source for $L$ enters at finite $j$ and henceforth supplies the denominator of $B$. The convergent tail of the reciprocal correction gives $L(y_j)/y_j\to1$. Monotone summation of $L(x)^{-s}\le x^{-s}$ now yields
$$
 \lim_j B(y_j)/y_j=1/\min_D L>0,\qquad
 \lim_j W_s(y_j)/y_j^s=\sum_{x\in D}L(x)^{-s}>0.
$$
Both limits are independent of which source in $D$ was chosen.

For a formulation insensitive to a collection of undetected cycles, replace $W_s$ by $W_s^{\rm first}$, keeping only the first arrival from each source. The limit $W_s^{\rm first}(y)/y^s\to0$ is also equivalent to absence of escape. In one direction use $C_w^s/y^s\le x^{-s}$ and dominated convergence over sources: a source with finite orbit contributes at only finitely many distinct targets. In the other direction the two transfers coincide on any escaping component. On the entire known basin the two limits to zero hold unconditionally, even when one restricts neither the size nor the depth of its off-cycle targets. Indeed each contributing source lies in that basin and its forward trajectory is finite; the only cyclic targets there are 1 and 2. This gives no power rate.

Finally, a proposed bound $W_s(y)\ll y^\gamma$ with $\gamma<s$ would force the uniform peak bound
$$
                    T^k x\ll x^{s/(s-\gamma)}
$$
on every finite simple forward path. Its incoming slope is at least a constant times $T^kx/x$ by the uniform reciprocal estimate. In particular $\gamma<s-1$ would prove a uniform excursion exponent strictly below $s$ for $1<s<2$. Independently $T^k(2^k-1)=3^k-1$ already forces $\gamma\ge s\log_3(3/2)$ by taking this one term of $W_s$. Thus for $s\le\log_2 3$ the proposed strict bound is impossible. For larger $s$ that example leaves room, and the uniform diagonal estimate remains open. The weaker little-oh criterion already suffices, but its equivalence identifies the ordinary quantifier that Haar integrability misses. For the classical excursion statistic, see [Lagarias and Weiss, *The 3x+1 Problem: Two Stochastic Models*](https://doi.org/10.1214/aoap/1177005779).
