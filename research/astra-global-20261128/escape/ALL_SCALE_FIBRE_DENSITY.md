# Untrimmed real-fibre moments at all physical resolutions

**Source-qualified written theorem.** This proof uses the original ordinary first-landing power estimate, Weaver's certified-stage count, the consistent natural history of ordinary minima and landings, and Weaver's all-scale covers of natural first-hit rays. The collision lower for escaping macroscopic strips at moment two and its original physical coordinates are due to PR213. The conclusions here include upper bounds for the complete measures, at all original targets and all choices of grid cells. [First-landing estimates and the certified-stage interface](RAW_LANDING_MOMENTS.md) · [Earlier natural history and critical gauge](REAL_FIBRE_LOG_GAUGE.md) · [Weaver, Paper 175, §§7–8](https://rstation.ai/problems/collatz/papers/175) · [PR213, macroscopic physical unit-bin energy, pinned at 87be3aa8](https://github.com/GettysburgResearch/collatz/blob/87be3aa8837ecc64e83075d7571c6ab9e1646c2b/research/astra-global-rigidity-20261128/mass/MACROSCOPIC_REAL_ENERGY.md).

On positive ordinary integers let $m$ be the attained minimum. Let $R$ denote the limiting natural log correction in base two to the first $m$, obtained by summing $\log_2(1+1/(3x))$ over odd departures before this visit. For arbitrary real numbers $a_m$ write $\nu$ for the full law of $R-a_m$. Put $g=1-H_2(\log_3 2)+1/351$. For $B=2^k$, $k\ge1$, and any finite union $E$ of cells of a common real grid of mesh $B^{-1}$, one has, for every $0<\delta<g/(1+g)$,
\[
                   \boxed{\ \nu(E)\le C_\delta
                          \big(\sqrt{k}\,|E|\big)^\delta .\ }          \tag{1}
\]
Here $|E|$ is Lebesgue length and the constant is independent of all the translates, the grid origin and the chosen cells. The same bound with an absolute change in the constant holds **uniformly for the full lap-normalized harmonic row at every positive odd target**, in the relative product or reflected relative offset coordinate. It holds for all real $B\ge2$ on replacing $k$ by $1+\log B$.

If $I$ runs over the grid cells and $0<q<g$, the original full law has
\[
           B^q\sum_I\nu(I)^{1+q}\asymp_{\nu,q} k^{q/2}.               \tag{2}
\]
The upper constant is independent of the translations. For any positive-mass restriction the same two-sided order holds with a restriction-dependent lower constant. At every nonzero positive fixed-root first-hit law, its first-hit product-weighted version, and each canonical escaping-component product law, (2) holds in the natural relative mark coordinate. All lap-normalized harmonic rows have the upper uniformly. These bounds use all the mass in the indicated measure.

## Clock and correction localization with a variable failure budget

Write $Y_n$ for first odd landing at $2^n$ in the common limiting ordinary history, with a cemetery for a miss. At finite labels $Y_j=\operatorname{Pass}_{2^j}(Y_n)$ for $j<n$, and $m(Y_n)=m$. The log correction remaining beyond $Y_n$ tends to zero on taking $n\to\infty$ by the simple-path reciprocal packing in the cited natural history. Each marginal has the uniform event estimate, for every $\eta<1$,
\[
 \Pr(Y_n\in A)\ll_\eta (|A|/2^n+2^{-gn})^\eta,\qquad
 \Pr(Y_n=\dagger)\ll_\eta2^{-g\eta n}.                               \tag{3}
\]
Fix $0<\beta<g$. Choose $\eta<1$ sufficiently near one to have $g\eta>\beta$. For every integer $1\le l\le k$ there is a set of histories of omitted probability $O_\beta(2^{-\beta l})$ on whose complement $y=Y_k$, $z=Y_l$ are finite and
\[
 \begin{aligned}
   &2^k 2^{-C(l+1)}\le y\le 2^k,\qquad
             |R-R(y)|\le C(l+1)2^{-k},\\
   &\left|j-\frac{\log2}{D}(k-l)\right|
       \le C\sqrt{k}(l+1)^2,\qquad D=2\log2-\log3,                   \tag{4}
 \end{aligned}
\]
where $j$ is the actual odd grade from $y$ to $z$ at its first passage. All constants in this construction may depend on $\beta$. The lower bound for $y$ follows at once from (3) by choosing $C$ large, with an empty lower interval if necessary.

First, at every rank $n\ge l+1$ the passage $Y_n\to Y_{n-1}$ takes at most $C n$ odd steps, except on total probability $O_\beta(2^{-\beta l})$ across all such ranks. Labels already at or below $2^{n-1}$ require zero steps. Above that level, the ordinary count of uncertified $y$ is $O((1+n)^3 2^{(1-g)n})$ by Weaver 102, Lemmas 3–4. Apply (3), absorb the polynomial at an exponent strictly between $\beta$ and $g\eta$, include missed landings, and sum geometrically. We use these coarse simultaneous bounds only where a shorter binary-clock estimate does not fit. [Certified-clock count](RAW_LANDING_MOMENTS.md).

For the upper residual use $n=k+h$ with $h\ge1$. When $n\ge C_1(l+h+1)$ use $J=\lceil C_2(l+h+1)\rceil$ odd gaps; take $C_1$ large enough that $4J+1\le n$. For a uniformly counted odd label in $[1,2^n]$ the first $J$ gaps restricted to native total at most $4J$ have exactly their binary Haar counts. The complementary event also has the correct count since each legal word in the restriction is a residue class modulo a divisor of $2^{4J+1}$. For independent geometric gaps $\Pr(e=d)=2^{-d}$ the two events $S_J<d_0J$ and $S_J>4J$ have probability $O(e^{-cJ})$, where $\log_2 3<d_0<2$ and $S_i$ is the sum of the first $i$ gaps. The finite counting statement for the first event can be made with $S_J\le4J$ and the second added. If the path has not crossed $2^{n-1}$ by $J$, its $J$ departures exceed that level and
\[
  \log U^J y=\log y+J\log3-S_J\log2+O(J2^{-n}).
\]
For $J$ larger than an absolute constant, $S_J\ge d_0J$ forces a crossing. By increasing $C_2$ the total exceptional probability from (3) at this rank is $O(2^{-2(l+h)}+2^{-g\eta n})$. At all remaining $n$ the coarse certified clock is at most $C n\le C C_1(l+h+1)$. Summing all failures and the contributions of their complementary high segments gives
\[
           |R-R(y)|\le C 2^{-k}\sum_{h\ge1} (l+h+1)2^{-h}.
\]
Indeed the departure on each segment exceeds $2^{k+h-1}$; the compatible corrections telescope, and their infinite residual is zero by the history input. This proves the first line of (4).

For the longer inward clock, start at $n_0=k$ and take $n_{i+1}=\lfloor .97 n_i\rfloor$ as long as $n_i\ge C_3(l+i+1)$ and its successor is at least $l$. At one such stage set $n=n_i$, $n'=n_{i+1}$ and $J=\lfloor n/8\rfloor$. The ordinary fraction of labels whose first $J$ geometric sums violate
\[
              \max_{0\le u\le J}|S_u-2u|
                           \le C_4\sqrt{n(l+i+1)},\qquad S_J\le4J     \tag{5}
\]
is at most $C2^{-A(l+i+1)}$, for any fixed desired $A$ after choosing $C_4$ and then $C_3$ large. To see this without a factor $J$, use the nonnegative exponential martingale for the centered geometric sums and the centered log moment generating function bound $C\lambda^2$ near zero. The maximal inequality at each of the two signs gives $2\exp[-c\min(t^2/J,t)]$ at threshold $t$. The separate $S_J>4J$ tail is exponentially small in $J$. As above all retained words are decided by $4J+1\le n$ bits. Under (3) these bad labels, and labels with $Y_n<2^n2^{-A(l+i+1)}$, have aggregate probability $O(2^{-\beta l-ci})$ at stage $i$; choose $A,C_3$ large enough. In particular the retained $Y_n$ exceeds $2^{n'}$.

Up to and including that first crossing the true log heights satisfy $\log U^uY_n=\log Y_n-Du-(S_u-2u)\log2+O(u2^{-n'})$ for $u\le J$. If there is no crossing by $J$, this identity at $J$ contradicts the absence of a crossing because $D/8>.03\log2$ and $C_3$ can make $C_4\sqrt{n(l+i+1)}$ arbitrarily small relative to $n$. At the crossing and its preceding step the heights lie on opposite sides, so the stage clock differs from $(n-n')\log2/D$ by $O(\sqrt{n(l+i+1)})$. This absorbs both the initial height loss $A(l+i+1)$ and integer rounding. The sum of these errors is at most $C\sqrt{k}\sqrt{l+1}$, by the geometric decrease of $n_i$.

The last rank $n_*$ is bounded by $C(l+\log(k+2))$: either the proposed successor falls below $l$ or the rank fails the displayed size condition, and the total number of geometric stages is $O(\log(k+2))$. Fill the interval from this rank down to $l$ using the previously retained coarse clocks. Their total and the remaining linear main term are $O((l+\log(k+2))^2)\le C\sqrt{k}(l+1)^2$. Summing the failure probabilities proves the second line of (4), including $l=k$.

## Counting the true labels for a selected set of real cells

Let $s$ be the native total of the segment from $y$ to $z$. The global minimum is reached no earlier than that first $z$, with the immediate case allowed. Therefore
\[
 R(y)-R(z)=s-j\log_23-\log_2(y/z),\qquad
                      0\le R(y)-R(z)\le C .                           \tag{6}
\]
The uniform upper comes from reciprocal packing on this simple segment; a repeated state prior to the first passage would prevent that passage. For fixed $j,z$ the bound for $y$ in (4) restricts the possible integers $s$ to $O(l+1)$ choices. For one $j,s,z$, both the eventual minimum and $R(z)-a_{m(z)}$ are fixed. Requiring $R-a_m$ to lie in a specified $1/B$ cell confines $\log_2 y$ to an interval of length $C(l+1)/B$, by (4),(6). Since $y\le B$, this interval contains at most $C(l+1)$ actual integer labels. This remains valid at short $k$ or large $l$ by increasing $C$. There are at most $2^l$ choices of $z$ and at most $C\sqrt{k}(l+1)^2$ choices of $j$. If $E$ contains $J_E$ grid cells, the retained possibilities for $Y_k$ therefore occupy an ordinary set of size at most
\[
                     C\sqrt{k}(1+l)^4 2^l J_E .
\]
Apply (3) once to this union. For all $1\le l\le k$,
\[
 \nu(E)\le C_\beta 2^{-\beta l}+
 C_\eta\big[C\sqrt{k}(l+1)^4 2^l|E|+2^{-gk}\big]^\eta .             \tag{7}
\]
If $J_E=0$ there is nothing to prove. Otherwise $u=\sqrt{k}|E|\ge 2^{-k}$. For $u$ bounded below use the total mass. For smaller $u$ choose $2^l$ within a factor two of $u^{-\eta/(\eta+\beta)}$, allowing the minimum $l=1$; this never needs a rank larger than $k$. The logarithmic factor from $l$ is absorbed at any exponent strictly below $\eta\beta/(\eta+\beta)$. Let $\beta$ approach $g$ and $\eta$ approach one to obtain (1). The same inequality holds for a union of at most $J_E$ intervals each of length $1/B$ placed at arbitrary origins, by covering each by at most a constant number of cells in one common dyadic grid at comparable resolution. This also proves its extension to nonbinary $B$.

## All original harmonic rows, including cycles

For a fixed positive unit target $a$ the ordinary first-hit log correction is dominated as a measure by a sum of two instances of the law in (1), with total multiplicity two independent of $a$. Indeed if the hit occurs no later than the first global minimum, the correction is $R(n)-R(a)$ with $R(a)$ the ordinary correction from $a$ to its own minimum. If the minimum occurs first, the correction is $R(n)+L_a(m(n))$, where $L_a(m)$ is the deterministic forward correction to the first $a$ from that minimum. Extend $L_a$ arbitrarily at minima never leading to $a$. The alternatives imply the two-measure domination when tested against nonnegative continuous functions in the natural limit. Bounded product weighting and the constant $\kappa=\log(4/3)/2$ preserve the estimate. On simple first-hit paths the product lies uniformly in $[c_0,1]$, so the log and product coordinates are bi-Lipschitz on the relevant range with constants independent of $a$. Pulling a cell through the inverse coordinate change costs only a bounded number of cells at the same resolution. Hence (1) holds uniformly for the (unnormalized) true first-hit harmonic measure $\phi_a$ in product coordinates. [First-hit and ordinary trace identities](SPATIAL_TRACE_TAIL.md).

Write $a_y=h(y)/y$ and $\nu_y$ for the stationary law of the relative product $1-R_{\rm abs}/y$. At nonperiodic targets $\phi_y=a_y\nu_y$ and set $\tau_y=1$. At periodic targets with primitive loop product $\lambda\in(0,1)$ put $\tau_y=1-\lambda$. The exact first-hit splitting reads
\[
              \tau_y a_y\nu_y
                =(1-\lambda)\sum_{j\ge0}\lambda^j
                    (D_{\lambda^j})_*\phi_y ,
\]
where $D_v(b)=vb$. In the $j$th dilation, preimages of $J_E$ cells have width $1/(B\lambda^j)$. If $B\lambda^j\ge2$, apply (1) at this new resolution with logarithmic factor at most $C\sqrt{k}$. At smaller $B\lambda^j$, the total-mass estimate also gives the claimed bound $C(\sqrt{k}|E|/\lambda^j)^\delta$ for $J_E\ge1$. Since
\[
         (1-\lambda)\sum_{j\ge0}\lambda^{(1-\delta)j}
                         \le (1-\delta)^{-1},
\]
the whole lap-normalized row satisfies (1). The zero row at a nonunit causes no exception. Reflection $b\mapsto1-b$ preserves the interval count. The component product law $\eta_C$ is the natural distribution of $F$ conditioned on escape in $C$ and reweighted by $F$, up to its fixed normalization. Before the minimum, $-\log_2 F(n)=R(n)-\log_2 F(m(n))$ on this population. Choosing these translates in (1), restricting, and exponentiating on the compact positive simple-path range gives (1) there with a component-dependent constant. [Ordinary-to-canonical product formula](ORDINARY_PRODUCT_TRANSITION.md).

## Positive moments, quadratic upper and the physical strip

For a measure $\xi$ satisfying (1), let $M$ be the mass of the cells with $B\xi(I)>t\sqrt{k}$. Their combined length is at most $M/(t\sqrt{k})$. If needed first take finite selections and pass to their union. By (1), $M\le C_\delta(M/t)^\delta$, so $M\ll t^{-\delta/(1-\delta)}$. Integrating this tail against $q t^{q-1}$ yields the upper of (2) for every $q<g$. This also holds for any submeasure with the same constants. Ordered cell masses obey $\xi(I_j)\le C_\delta(\sqrt{k}/B)^\delta j^{\delta-1}$ by applying (1) to the first $j$. Since $\delta<1/2$,
\[
                B\sum_I \xi(I)^2
                    \le C_\delta B^{1-2\delta}k^\delta .               \tag{8}
\]
The same sorting bounds every higher moment beyond the uniform-integrability range, with the power from summing $j^{-(1-\delta)(1+q)}$.

For the lower in (2) we use the quantitative cover in the proof of Paper 175, §7, at *every* sufficiently late resolution. At fixed attained minimum $m$, all typical first-hit rays have their absolute affine limit in some $V_{N,1/i}(m)$ for every $N\ge N_0$ with $i,N_0$ depending on the ray. For fixed $i,N_0$ these sets have at most $C_m i\,2^{8N}/\sqrt N$ cells of mesh $2^{-8N}$. Paper 175, §8, identifies the conditional natural terminal law with these rays under its timed-passage inputs. Its coordinate relation is $1-R_{\rm abs}/m=2^{-R}$, bounded uniformly away from zero by simple-path packing. Thus on a fixed minimum cell the change to $R-a_m$ is Lipschitz on this range. Countable minimum cells and all their fixed cover pieces exhaust the law. Any positive restriction has positive mass on some such piece. Taking $8N$ within a constant of $k$, the corresponding image is covered by $O(2^k/\sqrt{k})$ cells of *any* mesh-$2^{-k}$ grid. The same conclusion for fixed-root first-hit laws follows from the two translated-law domination above; on components a bounded weight, conditioning, and the fixed change to the product coordinate preserve it. A normalized cyclic row is covered by countably many dilated copies via its finite first-hit decomposition. Jensen's inequality on a piece of positive fixed mass now gives the lower in (2). [Weaver, Paper 175, Theorem 1, §7 all-scale covers and §8 identification](https://rstation.ai/problems/collatz/papers/175).

Let $\mu_y$ be the stationary probability law of the actual absolute intercept at positive-trace targets. With physical unit cells $J_b=[b,b+1)$, define $\xi_{y,b}=\tau_y h(y)\mu_y(J_b)/y$. The uniform row result gives, for all $y\ge3$,
\[
 y^q\sum_b \xi_{y,b}^{1+q}\ll_q(1+\log y)^{q/2}\quad(0<q<g),
 \qquad y\sum_b \xi_{y,b}^2
        \ll_\epsilon y^{(1-g)/(1+g)+\epsilon}.                        \tag{9}
\]
It also bounds every macroscopic substrip by restriction. On an escaping ray PR213 proves that at each fixed $t$ with $\eta_C([0,1-2t])>0$, along all late sites a positive unnormalized mass on $R_{\rm abs}\ge ty$ lies in $O_{C,t}(y/\sqrt{\log y})$ unit cells. Applying Jensen to those cells gives the matching lower $\gg_{C,t,q}(\log y)^{q/2}$ at every $q>0$; thus (9)'s first estimate has the exact order there for $0<q<g$. At moment two the known lower is $\gg_{C,t}\sqrt{\log y}$, while (9) gives only a sublinear power upper. Strict improvement to $o((\log y)^{q/2})$ on a subsequence of each putative ray for any one $q$ in the positive range would exclude escape. This proof does not supply such an improvement.

## The pointwise exponent at every sufficiently fine scale

For each nonzero law or positive restriction $\xi$ just discussed, one has the full limit
\[
     \lim_{r\downarrow0}
        \frac{\log\big(\xi([x-r,x+r])/r\big)}{\log\log(1/r)}
                   =\frac12 \quad\text{for }\xi\text{-almost every }x. \tag{10}
\]
The earlier packet obtained the upper limit $1/2$ and a matching lower along some sequence of radii using the two sides of the Hausdorff gauge. Here the simultaneous all-resolution covers give the lower bound at every small radius. The following argument also gives, writing $L=\log(1/r)$, an almost-sure eventual lower of order $\sqrt L/(\log L)^{1+\epsilon}$ for every $\epsilon>0$.

Normalize $\xi$ to a probability and choose a half-open dyadic grid, with nested cell $I_n(x)$ at mesh $2^{-n}$. Given $x$ sampled from $\xi$, $D_n=2^n \xi(I_n(x))$ is positive almost surely. Its reciprocal is a nonnegative supermartingale for the dyadic partition filtration: in a cell of positive mass the conditional expectation of the two child reciprocals is its own reciprocal times the number of positive-mass children divided by two. Therefore for each grid cell $I$ of level $n$,
\[
   \xi\{x\in I:\ D_j(x)<T\text{ for some }j\ge n\}\le T\,2^{-n}.
\]
This follows from the conditional maximal inequality for the reciprocal, applied first through a finite horizon and then by monotone convergence.

Fix a piece of the countable all-scale cover from the preceding proof. At levels $n_i=8\cdot 2^i$ it meets at most $C2^{n_i}/\sqrt{n_i}$ dyadic cells for all sufficiently large $i$. Summing the last bound at threshold $T_i=\sqrt{n_i}/i^{1+\epsilon}$ over those cells costs $O(i^{-1-\epsilon})$. Borel–Cantelli shows that for almost every point of the piece, $D_j\ge T_i$ for every $j\ge n_i$ for all large $i$. Countable exhaustion and $n_{i+1}=2n_i$ give the claimed lower throughout all fine levels. For a centered interval use a dyadic cell of size between $r/2$ and $r$ containing its center.

For completeness the upper in (10) also follows immediately from the untrimmed moments, with no need for a differentiation transfer. Fix $0<q<g$ and $\varepsilon>0$. The tail bound for $D_{n_i}/\sqrt{n_i}$ from (2) at any one nested dyadic grid is at most $C n_i^{-q\varepsilon/2}$ for threshold $n_i^{\varepsilon/2}$. If $D_j\ge n_i^{1/2+\varepsilon}$ somewhere in $n_i\le j\le n_{i+1}$ but $D_{n_{i+1}}\le \sqrt{n_{i+1}}\,n_i^{\varepsilon/2}$, stop on the first such large value. Conditionally there the reciprocal supermartingale bounds the latter probability by $C n_i^{-\varepsilon/2}$. Both estimates are summable over $i$. Hence eventually $D_j\le C j^{1/2+\varepsilon}$ throughout all large levels. Centered balls are controlled by a bounded number of nested grids: take the three fixed translates of the dyadic grid by $0,1/3,2/3$. At any given scale their boundary residues are separated by one third of the mesh, so any interval of length between one twelfth and one sixth of that mesh lies inside a cell of one of them. The same upper moment bound applies at every such grid origin. Taking $\varepsilon\downarrow0$ through rational values proves (10). This identifies an all-scale almost-sure exponent while permitting isolated fluctuations in the normalized density.

[DyadicDensityStopping.lean](DyadicDensityStopping.lean) proves the finite stopping estimates for arbitrary nonnegative additive dyadic masses. At the first density below a threshold the total stopped mass is at most that threshold times the initial cell width. First crossing a high threshold and subsequently a low threshold costs at most their ratio times the initial mass. Both statements include zero-mass cylinders and every finite horizon. The source estimates, all-scale cover, limit and differentiation arguments above remain written.
