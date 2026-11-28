# A power upper bound at every original target with a small real intercept

**Source-qualified written theorem.** The estimate uses the original unit landing minorant of Weaver and the arbitrary-label power upper for true first passages from the preceding packet. A common future landing label bounds the entire finite collection of inverse leaves. No convergence rate from finite ternary depth to the stationary trace enters the bound. [Weaver, Paper 12, Theorem 14](https://rstation.ai/problems/collatz/papers/12) · [Ordinary raw landing moments, equation (1)](RAW_LANDING_MOMENTS.md).

Use the finite, unconditioned kernel $K_{n,[0,B]}(y)$ defined in [the compact-real divergence theorem](COMPACT_REAL_DIVERGENCE.md); here the floor variable $B$ bounds the **absolute affine intercept**. For a periodic odd site $y$ let $\tau_y=1-\lambda_y$ with $\lambda_y$ its primitive forward-lap survival. At every other site put $\tau_y=1$. Write $\mu_M$ for the natural odd law of the first odd landing through $M$, including a cemetery $\dagger$. Set $L_M(y)=\operatorname{Pass}_M(y)$, also with cemetery on a genuine miss. For every positive odd $y$, $n\ge0$, $0\le B\le y/2$, and integer $1\le M\le y/[12(1+B)]$,
\[
 \frac{\tau_y}{y}K_{n,[0,B]}(y)\le C\,\mu_M(\{L_M(y)\}).              \tag{1}
\]
At $n=0$ a nonunit $y$ is a trivial exceptional case: (1) is asserted there only for unit targets. For nonunits the positive-depth kernel vanishes. Consequently at all odd targets and all depths,
\[
 \frac{\tau_y}{y}K_{n,[0,B]}(y)\ll_\eta
            \left(\frac{1+B}{y}\right)^{g\eta},\qquad
 g=1-H_2(\log_3 2)+1/351,\quad 0<\eta<1.                             \tag{2}
\]
The same bounds hold for the stationary absolute-intercept mass $h(y)\sigma_y([0,B])$ in place of $K_{n,[0,B]}(y)$, where $\sigma_y$ denotes the stationary probability fibre at the ordinary root $y$. In particular any sublinear cap carries uniformly vanishing **normalized** mass, at an explicit power in its ratio to the target. For a target whose entire future is above $M$, the right side of (1) is the true cemetery $D(M)$. A positive limiting escape profile can place mass at offsets comparable to its root height.

## First-visit leaves of the same odd grade

A compatible inverse word of length $n$ at an odd unit $y$ has actual odd endpoint $x=(y-B_w)/A_w$ and weight $A_w$ in the kernel. Since $B_w\le B\le y/2$, every inverse prefix is positive. The forward survival of the full path is $1-B_w/y$, a product of $3z/(3z+1)$ over its departed odd sites $z$. A departure $z\le M$ would give $B_w\ge y/(3M+1)>B$ under the displayed assumption on $M$ (indeed $3M+1\le4M\le y/[3(1+B)]$). Thus every departed site is above $M$ and $y>M$. At one specified length the original endpoint $x$ determines its word since its forward valuations are deterministic. Moreover $A_w/y\le1/x$.

First restrict to words whose forward path from $x$ first visits $y$ after exactly $n$ steps, with the empty word allowed. Promote every nonunit $x$ to $x'=4x+1$ and retain $x'=x$ on units. The image is a unit, $x\le x'\le5x$, and the next true odd site agrees, by $3(4x+1)+1=4(3x+1)$. There are at most two preimages per $x'$. The promoted segment still has no departure at most $M$; if $x'=y$ it may have first hit at time zero. All other promoted vertices have first hit on $y$ at the same time $n$. Among those on the cycle of $y$ there is at most one such vertex, by deterministic cyclic order; if $y$ is nonperiodic there are none. Among the remaining vertices no one is in another's forward future. Before first reaching $y$ this follows from equality of the two first-hit times, and after reaching $y$ a further vertex which later reaches $y$ must be on its cycle. Therefore a single source orbit can visit at most three distinct promoted vertices from this collection, including the possible root and the single cyclic exception.

For any finite selection of the promoted vertices, use the uniform ordinary first-landing minorant at the own floor $x'$ of each. It produces $\gg X/x'$ odd sources in $(X/4,X]$ whose first landing at or below $x'$ is $x'$, at every common $X$ above the finite collection's onset. Before that entry all sites exceed $x'\ge x>M$. From $x'$ until reaching $y$ all sites also exceed $M$. Every attached source therefore has exactly the same first landing at $M$, namely $L_M(y)$, with a common failure when the future of $y$ avoids the floor. The multiplicity bound of three permits summation of the lower counts. Divide by the odd annular population, send $X$ to infinity at fixed selection, and then exhaust the countable leaves. This proves
\[
          \sum_{w\ \mathrm{first\ hit}} A_w/y
              \le\sum_x1/x\ll \mu_M(\{L_M(y)\}),                     \tag{3}
\]
where the remapping costs only the fixed ratio and its multiplicity. For the empty word use the own-floor minorant directly.

## Repeated visits and the limit

At a periodic root, every full inverse word separates uniquely into $j$ initial complete reverse laps and its remaining first-visit word, possibly empty. Its weight is $\lambda_y^j A_{w'}$ and its intercept is
\[
              B_w=y(1-\lambda_y^j)+\lambda_y^j B_{w'}.
\]
For $B_w\le B<y$ this implies $B_{w'}\le B$. For each allowed $j$, the first-visit length is the fixed $n-jp_y$, with $p_y$ the odd period. Apply (3) and sum the geometric series; multiplication by $\tau_y$ proves (1). Nonperiodic targets need no splitting. If $M_0=\lfloor y/[12(1+B)]\rfloor\ge1$, choose $M_0$ in (1) and apply the raw singleton or cemetery upper. For $M_0<1$ one needs only an absolute upper on $\tau_y K_{n,[0,B]}(y)/y$: run exactly the same antichain argument with no common lower-floor restriction, bounding the attached population by one, then apply the same lap sum. For $n=0$ and a nonunit, $K_{0,[0,B]}=1$ and (2) holds directly. This proves (2).

For the stationary bound take any fixed admissible $B,M$. The inequality $y/(3M+1)>B$ has strict slack. Increase $B$ slightly still below $y$, retaining that strict inequality. The preceding word proof of (1) uses positivity of the prefixes and that inequality, so it continues to hold with the same $M$ after this enlargement. A stationary series with $R$ in the slightly enlarged open interval has its finite prefix there as well, since $B_n\le R$. Apply the fixed-root Cesàro weak convergence of the stationary cylinder measures, testing on this open interval and using the same bound on every approximant. This gives (1) for the stationary mass of the original closed interval. The absolute upper without $M$ transfers by the same enlargement. [Weaver, Paper 19, canonical fibre theorem (F3)](https://rstation.ai/problems/collatz/papers/19).

## Complete target antichains and independent depth maxima

Call a set of unit targets $\mathcal A$ a forward antichain when no two distinct members lie on one forward orbit. For each $y\in\mathcal A$ choose a cap $0\le B_y\le y/2$ with $M\le y/[12(1+B_y)]$ for the same fixed $M$. If every $L_M(y)$ belongs to a set $S$ of landing labels, with the cemetery permitted, then
\[
 \sum_{y\in\mathcal A}\sup_{n\ge0}\frac{\tau_y}y K_{n,[0,B_y]}(y)
        \ll \mu_M(S).                                                  \tag{4}
\]
Indeed the normalized full row at one root is bounded by the supremum over all first-hit row contributions in (3), because the corrected geometric lap weights sum to at most one. In a finite set of roots choose arbitrary first-hit depths independently and finite subsets of the corresponding leaves. Sources witnessing attached leaves for different roots are disjoint: their single forward orbit would otherwise visit two distinct target roots. The within-root multiplicity remains at most three and all attached sources have $L_M$ in $S$. The finite lower counts therefore sum before taking the common source limit. Exhaust the leaves, approximate each individual supremum on the finite roots, and exhaust the roots to get (4). On a finite root selection one can also take the stationary weak limits using the strict cap enlargement above before exhausting the roots.

There is a second allowable stopping family. Suppose the sites $y>M$ all first reach the floor $M$ after the same finite positive number $k$ of odd steps, with their landing labels in $S$. On any attached source its distinguished $y$ is the unique site exactly $k$ odd steps before that source's first landing at $M$. Thus different $y$ cannot share this source even if they are comparable *after* the landing, and (4) still follows. In the cyclic case an initially complete reverse lap visiting a site at most $M$ is incompatible with the cap, but the geometric comparison remains valid in either case.

At a large floor $Y$, let $\mathcal E_Y$ be the complete set of odd last exits on escaping trajectories: $y\le Y$ and every strictly later odd site exceeds $Y$, with $y$ in an escaping component. Its unit members lie in $((2Y-1)/3,Y]$ and form an antichain since none can subsequently visit a second member. Nonunit positive-depth rows vanish; only units enter the stationary exit budget. For $0\le t\le1/2$, pick $M=\lfloor c/(t+1/Y)\rfloor$ for a sufficiently small fixed $c>0$ when this is at least one. The entire selected set misses this smaller floor, and (4) yields
\[
 \sum_{y\in\mathcal E_Y\ {\rm unit}}\sup_{n\ge0}\frac1y K_{n,[0,ty]}(y)
                      \ll_\eta (t+Y^{-1})^{g\eta}.                    \tag{5}
\]
When the proposed $M$ is below one, apply the floor-free antichain argument with full attached population at most one and enlarge the constant. For stationary masses on a finite selection the same argument and weak transfer work with a slight cap enlargement, retaining all strict inequalities; exhaust the roots afterwards. Thus the entire escaping last-exit charge, if positive, must occur away from the small relative-intercept edge, with a quantitative error that already permits a separate adversarial depth choice at each outgoing donor. The estimate gives no vanishing bound on the complementary macroscopic sector.

## Domination of finite real windows at their actual source resolution

For every positive ordinary unit $x$, the unnormalized stationary absolute-intercept fibre satisfies
\[
       h(x)\sigma_x([0,u])\ge c u,\qquad 0<u\le1.                     \tag{6}
\]
Indeed in the marked ordinary minorant use landing floor $Y=\lceil Lx/u\rceil$ and target $x$, for a sufficiently large absolute $L$. This supplies relative natural first-arrival submass $\gg u/x$ with log correction at most $b/Y$; on these paths the absolute intercept $x(1-2^{-R})$ is at most $u$, and survival is bounded below absolutely. The canonical full weighted occupation measure at $x$ is $(h(x)/(\kappa x))\sigma_x$ and dominates this weighted first-visit submeasure. The conclusion follows including at periodic $x$. [Marked minorant](NATIVE_MINIMUM_ENDPOINT.md) · [Full weighted occupation and normalization, equation (4)](https://github.com/GettysburgResearch/collatz/blob/87be3aa8837ecc64e83075d7571c6ab9e1646c2b/research/astra-global-rigidity-20261128/mass/REAL_OFFSET_ORDINARY_TRACE.md).

At one odd unit $y$, fix a depth $n$ and any collection $W$ of its inverse words with positive unit origins $x_w=(y-B_w)/A_w$. For arbitrary $0<u\le1$, set $I_w=[B_w,B_w+u A_w]$. Then
\[
           \sum_{w\in W} A_w
              \le \frac C u\,h(y)\sigma_y\!\left(\bigcup_{w\in W}I_w\right).  \tag{7}
\]
Indeed its exact stationary prefix from $y$ has unnormalized mass $A_wh(x_w)$, and conditional on that prefix its intercept equals $B_w+A_w R'$, $R'\sim\sigma_{x_w}$. Distinct words of a common length are disjoint events on inverse path space regardless of overlapping real intervals. Apply (6) on each endpoint and sum. There is no periodic correction in (7): the right side is the full repeated-visit stationary fibre. This proof also allows arbitrary prefix-free collections of varying lengths by disjointness of the cylinder events. One may give each word its own $0<u_w\le1$ by placing $u_w A_w$ on the left. [Canonical inverse kernel and fibre recursion, Paper 19, §9.2](https://rstation.ai/problems/collatz/papers/19).

A positive nonunit origin on a word of length $n\ge1$ can be replaced by $4x_w+1$. Only its last inverse letter changes, increasing by two. The corresponding new slope and intercept are $A_w/4$ and $B_w-A_w/4$ since $y=A_wx_w+B_w$. The promoted unit words at a common depth have multiplicity at most two after including the original units. Thus the version of (7) for all positive ordinary leaves holds, up to an absolute factor, using $[B_w-A_w/4,B_w+u A_w]$ for the nonunits and retaining the same narrower intervals for units. For arbitrary prefix-free mixed depths we only claim (7) directly for unit leaves; promotion at varying lengths can change prefix comparability.

For example, in the genuine finite row supported on unit origins, the normalized contribution at $y$ of all words with $x_w\ge M$ and normalized intercept $B_w/y$ in a set $E\subset[0,1]$ is bounded by
\[
           C\frac{h(y)}y\,\sigma_y\{r:r/y\in E+[0,1/M]\}.            \tag{8}
\]
One can include the original leaf factor $\rho_1(x_w)\le2$ by increasing $C$. This follows with $u=1$ since $A_w/y=(1-B_w/y)/x_w\le1/M$. Consequently for any interval $E$ of length $s\le1/2$, with $M\ge1/s$, the lap-corrected truncated finite mass is $\ll_\delta(s\sqrt{1+\log(1/s)})^\delta$ for every $\delta<g/(1+g)$, **uniformly in target and depth**, by the earlier all-target stationary real-fibre estimate. Arbitrary unions of equal length intervals obey the same enlarged-set estimate. This quantitative modulus excises only the explicitly named small original inverse origins. Their genuine atoms may persist along an escaping ray. [All-scale stationary fibre bounds](ALL_SCALE_FIBRE_DENSITY.md).
