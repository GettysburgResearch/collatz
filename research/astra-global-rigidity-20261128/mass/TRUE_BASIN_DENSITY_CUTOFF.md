# Diffusive cutoff of the full ordinary predecessor density

**Source-qualified written deduction.** The ordinary first-passage and finite-quotient moment estimates, and the fixed-root joint mixing assumption used by the pinned bridge, are retained as explicit premises. The density process theorem is not a Lean theorem.

Use the odd source, component and notation of [the macroscopic acquisition theorem](TRUE_BASIN_MASS_ACQUISITION.md). For positive odd $n$ uniform in $[Y,2Y]$, set $y_i=U^i n$, $N=\log Y$, $D=\log(4/3)$ and $s=\sqrt{2/D}\log2$. Every $y_i$ for $i\ge1$ is a positive ternary unit, so its full predecessor density $d(y_i)$ is positive. Conditional on any fixed ordinary component of positive density, the following joint limits hold, with the same laws also for unconditioned sources.

* For fixed $0<\epsilon<1$ and $0\le t\le1-\epsilon$, take $i(t)=\max(1,\lfloor tN/D\rfloor)$. The linearly interpolated process $[-\log d(y_{i(t)})-(1-t)N]/\sqrt N$ converges in $C[0,1-\epsilon]$ to $sW_t$, with $W$ standard Brownian motion.
* On every compact real interval of $z$, take $j(z)=\lfloor N/D+z\sqrt N\rfloor$. Then $-\log d(y_{j(z)})/\sqrt N$ converges uniformly in distribution, using linear interpolation, to $(sW_1-Dz)_+$. The same $W$ occurs in both limits. In the macroscopic density limit at finitely many $z$, the jump in $d(y_{j(z)})$ from zero to $p_C$ is at $z=sW_1/D$.
* For each $u>0$, the first date $i\ge1$ when $d(y_i)\ge e^{-u\sqrt N}$ satisfies $(i-N/D)/\sqrt N\Rightarrow(sW_1-u)/D$, jointly for any finite list of $u$. Assign infinity on missing passage. On a fixed component this cemetery probability tends to zero. Unlike the fixed positive gate in the preceding paper, the moving gate is typically reached order $\sqrt N$ dates before the central actual hit.

These are original density observations along the positive deterministic orbit. A finite-state approximation to the density is not an input or a conclusion. The bridge inputs include the stated fixed-root joint analytic mixing assumption; no independent invariance principle for ordinary source paths is presumed. The completely invariant component can contain either a bounded cycle or an escaping ray.

## Uniform logarithmic comparison up to first small landing

There are absolute finite $B,C$ (one may take $B=10^5$ and enlarge $C$) with the following property. Put $P=N^B$ and let $T$ be the first odd date with $y_T\le P$. Except on a set of source probability $O(N^{-8})$, $T$ is finite and, simultaneously for every $i\ge1$,
\[
 \left|-\log d(y_i)-1_{i<T}\log y_i\right|\le C\log N.                 \tag{1}
\]
Only the portion through the first low landing uses physical source counts; it is essential that $d(y_i)$ stays nondecreasing after that landing.

Write $g(y)=y d(y)$, set $g=0$ at odd nonunits, and fix $H=N^{100}$. The full good-site first moment on each proportional octave and the power exceptional cardinality imply at every sufficiently large $M$
\[
  \frac{|\{y\in[M,2M]\text{ odd}:g(y)>H\}|}{M}
         \ll H^{-1}+M^{-1/64}\log M .                                 \tag{2}
\]
This controls the number of all bad sites, including the complete small-seed forward hull. There is an absolute lower bound $g(y)\ge c>0$ on units. [Ordinary critical share, good-site first moment and unit floor](ORDINARY_CRITICAL_TERNARY_SHARE.md)

Define $R_0=4Y$, $R_{i+1}=R_i^{1-1/64}$. End at the first $m$ with $R_m\le P$; thus $P^{1-1/64}<R_m\le P$ and $m=O(\log N)$. At a stage write $R=R_i$, $L=R_{i+1}$, $K=\lfloor(\log R)/2\rfloor$. Mark a positive odd $z\le R$ if it misses $[1,L]$ through $K$ odd steps, or visits an odd $y$ with $g(y)>H$ before that first landing and through $K$ steps. Let $E_i$ be the whole set of these marked ordinary labels. A uniformly chosen odd $z\le R$ has probability $O(R^{-1/64})$ of missing $L$ by $K$: the first $K$ gaps couple to positive geometric gaps by binary counting through $0.9\log_2R$ digits with a power-small overflow. Missing the floor then forces a log walk with mean $D$ to have traveled only $(\log R)/64+O(K/L)$, with the required power probability by its negative half-exponential moment. This is exactly the initial-interval calculation in [the good-site transfer](POWER_SMALL_SIBLING_DENSITY.md), equation (3), or the coupling and tilt in [the power-capped estimate](POWER_CAPPED_ORDINARY_TRACE.md).

At a retained event $U^jz=y$ before the lower landing, $j\le K$, the earlier sites all exceed $L$ and $L<y\le 2^K R$, since every positive odd step multiplies its input by at most two. The word weight satisfies $3^j2^{-S}=y b_j(z)/z\ge y/(2R)$ for large $R$, since $b_j=\prod_{k<j}3y_k/(3y_k+1)\ge1-O(K/L)$. At any fixed $j,y$ one word determines at most one physical $z$. The normalized number of starts visiting bad $y$ at grade $j$ is thus at most $2\sum_{y:g(y)>H}\rho_j(y)/y$ on this range of heights. On each dyadic octave in the range, $3^j\le R^{(\log3)/2}<L/2$, so its complete-period bound and the finite-quotient Haar $L^{3/2}$ estimate give a contribution $O((H^{-1}+L^{-1/64}\log R)^{1/3})$ by (2) and Hölder. There are $O(\log R)$ octaves and $O(\log R)$ dates, hence
\[
 |E_i|/R\ll R^{-1/64}+(1+\log R)^2(H^{-1}+L^{-1/64}\log R)^{1/3}.   \tag{3}
\]
The time-zero column has $\rho_0=1$. All future tests here concern the deterministic path of an individual landing label. [Finite-quotient moment, Weaver 9/v2, B3](https://rstation.ai/problems/collatz/papers/9)

For $i\ge1$ and large $Y$, $R_i<Y$. Weaver 102/v1 (11), (19) give the upper bound on this **entire set** for first landing through $R_i$ from the actual uniform odd octave,
\[
 C(1+N)\big((1+\log R_i)|E_i|/R_i+(1+\log R_i)^2 R_i^{-g_0}\big),   \tag{4}
\]
where $g_0>1/64$. Indeed the input smooth law at scale $Y$ dominates the uniform source on $[Y,2Y]$ by (11). At $i=0$ the original source is already below $R_0$ and (3) itself bounds its marked probability up to a constant. A source first failing to reach a stage's lower floor must already have landed at a marked upper label. Therefore a union bound using (3)–(4) covers all passage failures as well as all bad visits through first landing at $R_m$. The smallest $L$ exceeds $N^{(1-1/64)10^5}$, and all $\log R_i=O(N)$; with $H=N^{100}$ the sum is $O(N^{-8})$. This use of (19) pays a polynomial in $\log Y$ and requires no setwise comparison of two source scales at high precision. [Weaver 102/v1, finite-source inequalities (11), (19)](https://rstation.ai/problems/collatz/papers/102)

Hence up to the first passage through $P$ every visited unit has $c\le g(y)\le H$. At that first passage, the unit basin floor gives $d(y_T)\ge c/P$, since $T\ge1$ for large $Y$. All later sites have $c/P\le d(y_i)\le1$, even if their physical heights rebound far above $P$. These two conclusions prove (1). For any fixed positive-density basin or component, division by its asymptotically positive ordinary source probability preserves convergence in probability.

## The stopped height and joint critical law

Fix a nonperiodic odd unit $a$, condition on $B_a$, and write $J$ for the first odd grade there, $b=(J-N/D)/\sqrt N$. Read outward gap totals $S_l$ from $a$, starting at $S_0=0$. For each $0\le l\le J$ the exact inverse affine identity and the uniform simple-path survival floor give
\[
     \log y_{J-l}=\log a+Dl+(S_l-2l)\log2+O(1),                       \tag{5}
\]
with absolute control of the last term. In the fixed proportional source crop one has $S_J-2J=-(D/\log2)b\sqrt N+O_a(1)$. Under this physical conditional source,
\[
 \left(b,\left(\frac{S_{tJ}-2tJ-t(S_J-2J)}{\sqrt J}\right)_{0\le t\le1}\right)
        \Longrightarrow (Z,\sqrt2\,W^0),                              \tag{6}
\]
where totals are interpolated, $Z\sim N(0,2(\log2)^2/D^3)$ and $W^0$ is an independent standard Brownian bridge. To see the joint statement, use the exact-total, fixed-ordinary-root path limit jointly independent of the real offset after subtracting its linear endpoint. It is uniform along compact standardized totals by subsequence compactness. Thus for any bounded continuous bridge test and continuous compact physical source weight, the expected product in a central row differs uniformly by $o(1)$ from the bridge-test mean times the expectation of the physical weight. The latter depends on the real offset $F$ as $\chi(2^uF)$, with $u$ in a fixed compact interval. Its family of tests is equicontinuous and bounded there. The row sum, irrational phase averaging, signed-kernel offcentral control and approximation to $[Y,2Y]$ then give exactly the same scalar $Z$ as the natural clock proof. Tightness follows by the same central row crop bound and compact-total tightness. This proves (6) without applying a bare fair-geometric limit to a selected ordinary source. [PR213 pinned bridge, including its analytic assumptions and real-mark independence](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/inverse/pinned_root_bridge.md) · [Physical source crop and signed renewal-strip proof](FIXED_BASIN_NATIVE_WINDOW.md)

For large $Y$, $a\le P$, so $T\le J$ on this basin. At $l=J-T$, (5) and uniform tightness of $\max_{l\le J}|S_l-2l|/\sqrt N$ first give $J-T=O_{\mathbb P}(\sqrt N)$. The tight continuous centered process at its outward origin then gives $S_{J-T}-2(J-T)=o_{\mathbb P}(\sqrt N)$, hence $J-T=o_{\mathbb P}(\sqrt N)$ by the same identity and $\log y_T\le B\log N$. More generally, uniformly for $0\le l\le A\sqrt N$ at any fixed $A$, (5) gives $\log y_{J-l}=Dl+o_{\mathbb P}(\sqrt N)$. Consequently (1) implies, simultaneously on compact intervals of $z$,
\[
 -N^{-1/2}\log d(y_{j(z)})=D(b-z)_++o_{\mathbb P}(1).               \tag{7}
\]
In the interval between $T$ and $J$ the right side is $o_{\mathbb P}(1)$ by the just-proved clock separation. At dates after $T$ the left side is bounded by $O((\log N)/\sqrt N)$ with probability tending to one. The clipped limit is continuous in $z$, so interpolation at the integer dates gives the asserted uniform convergence in law. Its monotonicity and its nonzero slope at the level $u>0$ give the threshold date by testing levels on either side of the unique crossing. A sufficiently large compact $z$ interval contains that crossing with probability arbitrarily close to one.

For the precritical process, all dates $i(t)$ for $t\le1-\epsilon$ precede $T$ with probability tending to one. Substituting $l=J-i(t)$ in (5)–(6), with $l/J=1-t+O_{\mathbb P}(N^{-1/2})$ uniformly, gives the centered log-height process
\[
                 DtZ+s W^0_{1-t},\qquad 0\le t\le1-\epsilon .
\]
The $DtZ$ term uses the full linear endpoint of $S_J-2J$ in (5); the drift $D(J-i(t))$ alone would give $DZ$ instead. The reversed bridge $W^0_{1-t}$ is itself a standard bridge independent of $Z$. Since $DZ/s$ is standard normal, $W_t=W^0_{1-t}+tDZ/s$ is a standard Brownian motion on $[0,1]$ with $W_1=DZ/s$. Equation (1) transfers this entire limit to the full predecessor density at the displayed scale. Together with the exact positive-gate statement this identifies its macroscopic jump with the same $W_1$. Finally, exhaust each component's density by fixed nonperiodic basins as in [the preceding theorem](TRUE_BASIN_MASS_ACQUISITION.md), then use tightness of the component masses. This gives the stated conditional and unconditional laws. A postcritical fixed escaping component and a cyclic component of the same density have identical acquisition laws at these scales.
