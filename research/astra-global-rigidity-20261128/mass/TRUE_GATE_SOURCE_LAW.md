# Ordinary sampling of the strict future parity gate

Use the shortcut map $T$ and the odd map $U$. Put $b_t(n)=2Q_t(n)-t$, where $Q_t$ counts odd shortcut departures, and define
\[
 g(n)=-\min_{t\ge0}b_t(n),\qquad \mathcal P=\{n:b_t(n)>0\text{ at every }t>0\}.
\]
The finite record theorem computes $g$ and membership of this gate in $O(1+\log n)$ shortcuts. Every gate member is odd. The elementary ballot test on the first $\lfloor\log_2 X\rfloor$ letters already gives $\#(\mathcal P\cap[X,2X])\ll X/\sqrt{\log X}$. The estimates below give the matching order in every individual octave even after requiring a visit to a specified target. [Exact record identity and decidability](../cycles/RARE_ODD_ASCENTS.md)

Let $A$ be an arbitrary union of true components, or the predecessor set of one fixed positive odd unit. Write $d$ for its ordinary natural density. For every $1<p<2$ there are absolute positive $c,C$ and a positive $C_p$ independent of $A$ such that
\[
 c d^C\ \le\ \liminf_{X\to\infty}\frac{\sqrt{\log X}}X
     \#(\mathcal P\cap A\cap[X,2X])
 \ \le\ \limsup_{X\to\infty}\frac{\sqrt{\log X}}X
     \#(\mathcal P\cap A\cap[X,2X])\ \le\ C_p d^{1-1/p}.               \tag{1}
\]
These are source-qualified ordinary estimates. The constants for the lower bound may use the fixed inputs below but do not depend on the outcome, its target, or its natural density. The asymptotic onset may depend on all of them. In particular every fixed component has positive lower relative frequency among the genuine gate members in each large octave. This includes the terminating basin of $1$ and every possible different component. The inequalities do not assert existence of a normalized gate density.

## Incoming locations of the genuine gate

Put $D=\log(4/3)$, $L=\log X$. Conditional on any fixed positive odd unit's first-hit basin, sample ordinary $n\in[X,2X]$ and write $\tau$ for its first shortcut visit to that unit $a$. In time $0\le t\le1$ the linearly interpolated path $b_{t\tau}(n)/\sqrt{2L/D}$ converges in distribution to standard Brownian motion $B_t$. To verify the normalization, for odd inputs of first odd grade $J$ use outward actual gap totals $S_i$. The true central row gives $(J-L/D)/\sqrt L$ a centered Gaussian limit of variance $2(\log2)^2/D^3$. The terminal centered total satisfies $S_J-2J=-(D/\log2)(J-L/D)+O_a(1)$ on the physical octave. After removing its linear endpoint, the outward bridge divided by $\sqrt J$ tends to an independent variance-two Brownian bridge, including after sampling the physical real mark. Thus $(S_{tJ}-2tJ)/\sqrt{2L/D}$ tends to standard Brownian motion. At forward odd grade $i$, the centered shortcut surplus is the outward deviation at $J-i$ minus that at $J$. Reversing the Brownian increments with this sign again gives standard Brownian motion. The shortcut clock fractions of these grades tend uniformly to their odd-grade fractions. The maximum individual gap is $o_{\mathbb P}(\sqrt L)$ by continuous-path tightness. This fills in all intermediate shortcuts. Fixed initial halvings do not change the limit, and their count on the basin is tight by natural counting. [Physical first-hit clock and tail](FIXED_BASIN_NATIVE_WINDOW.md) · [Joint physical bridge including its analytic premises](TRUE_BASIN_DENSITY_CUTOFF.md) · [Frozen bridge with real mark and cycle first-hit restriction](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/inverse/pinned_root_bridge.md)

For $0\le i\le\tau$ the actual future minimum level is exactly
\[
 R_i=\min\left(\min_{i\le t\le\tau}b_t(n),\ b_\tau(n)-g(a)\right).
\]
It is nondecreasing, $g(n)=-R_0$, and $R_{i+1}-R_i=1_{\mathcal P}(T^in)$. Indeed an increase occurs exactly at a strict future minimum and must equal one since the next shortcut has increment at most one. The future-minimum map on a continuous path is Lipschitz in the uniform norm. The term $g(a)$ is finite and fixed. With $M_t=\min_{t\le u\le1}B_u$, joint convergence therefore gives
\[
 \left(\frac{g(n)}{\sqrt{2L/D}},\quad
        \frac1{\sqrt{2L/D}}\sum_{i<\tau}1_{\mathcal P}(T^i n)\delta_{i/\tau}\right)
 \quad\Longrightarrow\quad (-M_0,\ dM_t) .                            \tag{2}
\]
The second entry has the weak topology of finite measures on $[0,1]$. Uniform convergence of their cumulative mass functions to the continuous $M_t-M_0$ implies this assertion. Its total mass $B_1-M_0$ and the first entry $-M_0$ each have the standard half-normal law. The theorem states no independence between them. On the event that this count is positive, the first strict gate date before the hit is the last attainment of $R_0$. The probability of that event tends to one, since $B_1-M_0>0$ almost surely. Brownian motion has a unique minimizing time $V$ in $[0,1]$, with the arcsine distribution. Thus the first gate date divided by $\tau$ tends to $V$. The exact height formula before the first hit is $\log T^i n=\log n-Di/2+(\log3)b_i(n)/2+O(1)$, by uniform survival on a simple path. The first gate height consequently has logarithm divided by $L$ tending to $1-V$, jointly with (2).

These statements hold unconditionally and conditional on each true component if the endpoint is the first attained orbit minimum. On a fixed basin its date differs from $\tau$ by a constant bounded in terms of its target. A prior minimum must be at some $z\le a$ on a finite first-hit path from that $z$ to $a$, and a subsequent one is bounded by the first minimum date on $a$'s own future. Counts and clock changes over those fixed paths cost $O_a(1)$. Exhaust each component from within by fixed-unit basins up to arbitrarily small natural mass and then truncate the countable family of components. On a bounded component one odd cycle target suffices. In particular $g(n)/\sqrt{2\log X/D}$ has the standard half-normal limit on unconditional ordinary octaves. The estimate below only needs this marginal. [Component exhaustion and positive natural masses](FINITE_COMPONENT_PARTITION.md)

## A full-column estimate for an arbitrary source-side event

Take $b$ and $k$ positive integers and $j=b+k$. Under independent fair positive geometric gaps, let $E$ be any condition on the first $k$ **forward** gaps, write $l$ for their total, and $p_l=\Pr(E,S_k=l)$. The independent next $b$ gaps have total $h$. On reversing the whole word to outward order from the physical target, those $b$ unrestricted letters come first. Put $\rho_{m,s}(y)=3^m\Pr(F_m=y\bmod 3^m,S_m=s)$ for the outward affine offset $F_m=\sum_{i\le m}3^{i-1}2^{-S_i}$ and $\rho_m=\sum_s\rho_{m,s}$. Let $C_{h,l}(y)$ be the density $3^j$ times the mass of the full compatible words satisfying $E$ and these two clocks. It has period $3^j$ on the odd roots. Complete compatibility gives genuine positive odd inverse parents at every positive odd representative. All the words at this $(h,l)$ have the same weight $3^j2^{-(h+l)}$.

Fix exponent 4 in the extra-precision theorem and choose $k\le\delta b$ for its constant $\delta>0$. With $m=\lfloor b^{1/4}\rfloor$, let
\[
     D_h(y)=\sum_s\rho_{m,s}(y)\,\pi_{b-m}(h-s),\qquad
     \pi_t(v)=2^{-v}\binom{v-1}{t-1} .
\]
Here $\pi_t$ vanishes outside its support and is the true fair total-gap probability. The counting Haar mean on one full period obeys
\[
   \sum_{h,l}\operatorname{Ave}_{3^j}|C_{h,l}-p_lD_h|
                  \ll \Pr(E)m^{-4}.                                    \tag{3}
\]
Indeed the full offset is $F_b+3^b2^{-h}F'_k$. Condition on $h$ and on the entire independently sampled tail restricted to $E,S_k=l$, in its reversed order. Shifting by $3^b2^{-h}F'_k$ leaves each coarse residue modulo $3^m$ intact. Replacing the joint mass of $(F_b\bmod3^j,h)$ by its uniform lift from $3^m$ has sum-norm error $O(m^{-4})$ after summing $h$. Convolution and the restricted tail cost the factor $\Pr(E)$, since that error applies independently of the tail. The coarse law of $F_b$ sees only its first $m$ letters. Splitting their total $s$ leaves independent total probability $\pi_{b-m}(h-s)$, giving exactly $D_h$. This estimate is averaged on the full period and retains both actual totals. [Weaver–Wren, Theorem 6, equations (65)–(66)](https://rstation.ai/problems/collatz/papers/48)

Write $\rho_m^{\rm good}=\sum_{s\le4m}\rho_{m,s}$, and define $D_h^{\rm bad}$ by restricting $s>4m$ in $D_h$. Then $\sum_h\operatorname{Ave}D_h^{\rm bad}\ll e^{-c m}$. There is a nonnegative sequence $J_h$ with $\sum_hJ_h\ll1$ and
\[
 D_h\le J_h\rho_m+D_h^{\rm bad},\qquad
 |h-2b|\le\sqrt b\quad\Longrightarrow\quad
                   D_h\ge c b^{-1/2}\rho_m^{\rm good}.                 \tag{4}
\]
Take $J_h=\max_{0\le s\le4m}\pi_{b-m}(h-s)$. Unimodality and the $O(b^{-1/2})$ maximal atom give a bounded sum because $m=o(\sqrt b)$. The lower follows from the elementary geometric local Gaussian bound across that compact central window, uniformly for $s\le4m$. The imported finite-quotient estimates are $\operatorname{Ave}\rho_m^p\ll_p1$ at fixed $1<p<2$ and $\rho_m(y)\ge c>0$ on all ternary units at large $m$. The latter follows also by summing the pointwise central total-atom floors over $|s-2m|\le\sqrt m$. [Weaver 9, B3](https://rstation.ai/problems/collatz/papers/9) · [Weaver 211, Appendix A, uniform restricted central atom](https://rstation.ai/problems/collatz/papers/211)

## Transfer to the physical octave

Choose $b=\lfloor L/100\rfloor$ and $k=\lfloor\delta' b\rfloor$ for a fixed $0<\delta'<\min(\delta,1/2)$. For $l+h\le 3j$ every physical band at scale $Y=X3^j2^{-l-h}$ contains many periods $3^j$ even on restricting to odd integers. All such $Y$ satisfy $X^{9/10}\le Y\le X^{11/10}$ for sufficiently large $X$. Every compatible word gives $y=3^j2^{-h-l} n+F_j$, where $0\le F_j\le(3/2)^j-1=o(Y)$. Therefore starts in $[X,2X]$ can give only $y\in[Y,3Y]$, and every legal odd $y\in[5Y/4,7Y/4]$ lifts to a start in $[X,2X]$. The normalized number of starts for a specified output subset at fixed $(h,l)$ is the sum of $C_{h,l}(y)/Y$ on that subset, with the actual source restriction where needed. Summing the absolute errors in this correspondence with $C$ replaced by $p_lD_h$ costs $O(\Pr(E)m^{-4})$. Indeed an interval of length $O(Y)$ is covered by $O(Y/3^j)$ full periods of odd representatives, so the positive sum-norm error divided by $Y$ is at most a constant times its full-period average, even for an interval chosen separately for each $(h,l)$.

On these finite paths there is no exception to transporting $1_A$ between the start and output once $X$ is sufficiently large. For a fixed basin every intermediate height is at least $X2^{-3j}$ by the clock bound, hence exceeds the fixed target. For a completely invariant set transport is exact at every date. The natural masses in all fixed arithmetic classes are their ordinary proportions, by counted coalescence under fixed translation. In particular the odd ternary units in $A$ have density $d/3$ among all positive integers. Natural density here gives estimates uniform over the present proportional test intervals as their smallest endpoint goes to infinity. [Actual component and first-hit colors under fixed translations](ORDINARY_BASIN_WINDOWS.md)

For the upper bound in (1) retain $E=\{2i-S_i>0,\ 1\le i\le k\}$ in the **forward** order. Genuine gate membership implies this condition and $h+l<2j$. The fair event has probability $O(k^{-1/2})$ by the elementary ballot estimate: the odd-source shortcut sequence begins with an odd departure and its other parity bits are fair until the $k$th full gap. Using (3)–(4) and covering periods, the total bad-clock cost is $O(\Pr(E)e^{-cm})$. On each output band, Hölder and the Haar moment give
\[
   Y^{-1}\sum_{y\in A\cap[Y,3Y],\ y\text{ odd}}\rho_m(y)
                          \ll_p(d+o_A(1))^{1-1/p} .
\]
Sum the bounds $p_lJ_h$ over both clocks. This gives the stated upper, including zero natural mass.

For the lower assume $d>0$. Choose a fixed $B\ge2$ and strengthen the same source-side ballot event by
\[
          B\sqrt L\le 2k-l\le (B+1)\sqrt L .
\]
Call its probability $p_E$. There are absolute constants, allowing dependence on the fixed choice of $\delta'$, such that for every fixed $B$ and sufficiently large $X$,
\[
    p_E\ge c e^{-C(B+1)^2}/\sqrt L.                                  \tag{5}
\]
At $d'=2k-l>0$ the exact mass of the strict ballot words is $2^{-l}(d'/l)\binom{l}{k}$. Each such word starts odd and corresponds to exactly one composition of $l$ into $k$ positive gaps. Apply the binomial local Gaussian lower on this fixed, possibly large standardized window and sum its order $\sqrt L$ integers. The absolute Gaussian exponential constants in (5) follow directly from Stirling with $B$ fixed before $X$ increases.

Keep $|h-2b|\le\sqrt b$ and restrict the physical inner output interval to units $y\in A$ with $g(y)\le B\sqrt L/2$. From (2) the fraction failing this last inequality has upper limit $O(e^{-cB^2})$, uniformly over all those bands. This follows by fixed proportional-interval comparison and $9L/10\le\log Y\le11L/10$, using the ordinary half-normal tail with a fixed $B$ before taking the limit. For $O(e^{-cB^2})\le c_1d$ with sufficiently small $c_1$, the retained units have at least $c_2dY$ members. The pointwise unit floor and the full-period bound on $\rho_m-\rho_m^{\rm good}$ imply that their sum of $\rho_m^{\rm good}/Y$ is at least $c_3d-o(1)$ uniformly in the two totals. Apply (3)–(4), sum the order $\sqrt b$ central $h$ and all eligible $l$, and obtain at least $(c_4d-o(1))p_EX$ actual starts with these two outer conditions.

Remove paths whose middle $b$ gaps ever change their centered total from its starting value by more than $B\sqrt L/4$ in absolute value. In the eligible $(h,l)$ one has $h+l\le3j$. The complete actual prefix through those gaps is read modulo $2^{3j+1}$. After splitting into whole binary periods its removed fraction of the original octave is at most
\[
       C p_E e^{-c B^2}+O(2^{3j+1}/X).
\]
Indeed the fair geometric middle gaps are independent of the first block. Their centered maximum has the displayed Gaussian tail by the exponential maximal inequality since $b\asymp L$ and $B$ is fixed. It suffices to drop the endpoint and other constraints when giving this upper bound. On each retained path the forward surplus stays strictly positive throughout the initial $k$ gaps. Its buffer of at least $B\sqrt L$ at their end pays for all the middle fluctuations, including intermediate shortcuts because the minimum within each complete gap occurs at one of its ends. The final surplus exceeds $g(y)$; hence the entire infinite continuation stays positive as well. This proves that the retained starts belong to the genuine gate. Choose $B=C_0\sqrt{\log(2/d)}$ with a sufficiently large absolute $C_0$ so both removed terms cost at most half the lower count in the large-$X$ limit. Equation (5) now gives the polynomial lower in (1).

The upper in (1) bounds sampling a true outcome at a starting gate. The forward orbit of one supplied gate uses one actual future. A post-minimum escaping path would have a positive frequency of gate visits despite the spatial law (1). No upper for that conditional time occupation follows from these source estimates.
