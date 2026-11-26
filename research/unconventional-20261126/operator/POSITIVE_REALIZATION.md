# A positive real height on the mixed eigenstate, and an exact diagonal test

**Status.** PROPOSED written theorem. This tests the additional physical constraint of a positive proper Archimedean coordinate with the exact affine translations.

## OP-M3. Global positivity does not impose the integer diagonal

On the full-measure family from [OP-M1](MIXED_EIGENSTATES.md), after discarding another Haar-null subset, there is a finite $K_y$ with the following property. Start the Archimedean coordinate at any real $h>K_y$ at the root $(-1,y)$ and transport it by the common forward and inverse affine maps over its whole acyclic component. The resulting values $H(v)$ satisfy
$$
             (h-K_y)P(v)\le H(v)\le(h+1)P(v).
$$
In particular the height is everywhere positive and has only finitely many preimages of each bounded interval. If the root $h$ is a positive integer, all its values are in $\mathbb Z[1/6]$. For any preassigned finite binary and ternary precisions the integer root may be chosen to agree with both adic coordinates to those precisions. Thus positivity, properness, exact $+1$ dynamics and these finite diagonal tests coexist with the nonphysical summable slope modes.

For a ternary root $z$, let $M_k(z)$ be the maximum incoming slope among legal words of exactly $k$ letters and let $A_*(z)$ be the supremum of their real normalized carries $A'$ over all words of all lengths, using [OP-B1](TERNARY_BARRIER.md). We have $A_*(z)\le\tfrac12\sum_{i\ge0}M_i(z)$. For any $1<s<2$,
$$
 \|M_i\|_{L^s(m_3)}\le\lambda_s^{i/s}
$$
by bounding the maximum's $s$th power by the sum over the level and integrating as in OP-T1. Minkowski gives $A_*\in L^s(m_3)$.

Write $C_j=(3/2)^j$ on the initial forward spine and $y_j=-1+C_j(y+1)$. Then almost surely
$$
                    \sup_{j\ge0} C_j^{-1}A_*(y_j)<\infty.          \tag{M2}
$$
Split an arbitrary inverse word at the first $j$th odd letter as in OP-M1. All terms up to that frontier agree with inverse letters at the negative integer $-1$. Its initial self-loops contribute $O(1)$ to the normalized sum of prefix slopes divided by $C_j$ by geometric summation. The subsequent simple segment contributes at most $K\sum(1+|u_i|)^{-1}$ by OP-T3's simple-path distortion, since the preceding loop count is at most $j$. This is uniformly bounded by PR210's signed reciprocal estimate. To see it for all native steps, group any run of even vertices according to its following odd vertex and sum the reciprocal geometric series; a possible terminal even run costs at most an absolute constant. The same bound covers words stopping before the frontier.

At a frontier remove the initial $\ell$ self-loops. Let $u$ be the signed endpoint on the remaining unique simple path to $-1$, let $q_u$ count its odd steps and let $e_u$ count its even steps. Then $j=\ell+q_u$, the frontier depth is $k=j+e_u$, the normalized frontier multiplier is $C_w/C_j=2^{-e_u}$, and its ternary endpoint is $u+2^{e_u}(y+1)$. All later carries normalized by $C_j$ are at most
$$
                  2^{-e_u} A_*\big(u+2^{e_u}(y+1)\big).
$$
This expression is independent of the number of removed loops. For the empty simple path use $u=-1$, $q_u=e_u=0$. Since its simple multiplier is $(3/2)^{q_u}2^{-e_u}\le K/(1+|u|)$, we have $\sum_u2^{-s e_u}<\infty$. Each displayed ternary input is Haar under Haar $y$. Integrating the sum of the $s$th powers therefore bounds their supremum almost surely. This proves (M2), also at $j=0$ by $A_*(y)<\infty$.

At the end of a reduced walk with $j$ forward steps and inverse word $w$ the actual transported real coordinate is
$$
 H(v)=\frac{C_j(h+1)-1-A'_w}{C_w}
     =P(v)\left(h+1-\frac{1+A'_w}{C_j}\right).
$$
Equation (M2) and $C_j\ge1$ prove the bounds. Ordinary CRT gives arbitrarily large integer choices satisfying the finite root tests.

## OP-M4. A relaxed but exact arithmetic diagonal condition

Take any rational real root $h$ in the same affine model with initial adic coordinates $x\in\mathbb Z_2,y\in\mathbb Z_3$. Write $h_j$ for its transported rational heights along the forward ray. If $h\ne x$ in $\mathbb Q_2$, then for all sufficiently large $j$
$$
           v_2(h_j)=v_2(h-x)-j .
$$
Indeed its difference from the integral dyadic coordinate after $j$ letters has multiplier $3^q/2^j$. Once that difference has negative valuation, its valuation is also the rational height's valuation. If $h=x$, all these heights are dyadically integral and the native forward parity agrees forever. Thus a single subsequence with $v_2(h_j)+j\to+\infty$ already forces exact dyadic agreement.

Similarly let an inverse sequence, or just a collection of legal finite inverse words, have odd depths $q\to\infty$. If $h\ne y$ in $\mathbb Q_3$, then every corresponding sufficiently deep inverse rational endpoint satisfies
$$
           v_3(h_{w})=v_3(h-y)-q,
$$
since its difference from the integral ternary endpoint is multiplied by $2^k/3^q$. Thus $v_3(h_w)+q\to+\infty$ on even one such subsequence forces exact ternary agreement. Conversely equality at the root ensures ternary integrality on every legal inverse path. The conditions make no assertion about roots with no inverse paths of unbounded odd depth. On the ordinary positive unit core such paths exist, for example by choosing the next unit odd predecessor after at most four doublings at every stage.

For a positive root $h\in\mathbb Z$ the two submaximal denominator-growth tests force exactly $(x,y)=(h,h)$. They isolate a condition strong enough to eliminate the nonphysical companions in OP-M3 without demanding an a priori uniform denominator bound on all paths. Proving that ordinary calibrated escape modes cannot satisfy this arithmetic condition remains open. In particular OP-M3's positive integral choices have $v_2(h_j)=v_2(h+1)-j$ eventually on the all-odd spine.
