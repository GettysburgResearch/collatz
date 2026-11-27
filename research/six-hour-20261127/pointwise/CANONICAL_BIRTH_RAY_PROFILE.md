# Birth age resolves the original ordinary trace into its physical ray segments

Use the positive odd map $U(x)=(3x+1)/2^{v_2(3x+1)}$, $f(x)=3x/(3x+1)$, and $f_K(x)=\prod_{i<K}f(U^ix)$. For an ordinary odd source $x=1+2l$ put
$$
 T(x)=\min\{j\ge0:l<2^{E_j(x)}\},
 \qquad E_j(x)=\sum_{i<j}v_2(3U^ix+1).
$$
In particular $T(1)=0$. This is the canonical birth date in the original depth-zero row. Let $P\delta_y=f(y)\delta_{Uy}$ on positive odd point measures, and define
$$
 B_j=\sum_{T(x)=j}\frac{f_j(x)}x\,\delta_{U^j x},\qquad
 N_{K,J}=\sum_{j=0}^J P^{K-j} B_j \quad(0\le J\le K).
$$
The full $N_{K,K}$ is the original measure $\sum_{1\le y<2\cdot3^K,\ y\ {\rm odd}}\rho_K(y)\delta_y/y$, with all actual endpoint multiplicities retained. Indeed each $K$-gap word has one least ordinary odd source whose endpoint is its least odd representative, and that source is precisely born by $K$. The exact weight is $3^K2^{-E_K(x)}/U^Kx=f_K(x)/x$. This gives the inhomogeneous recursion $N_{K+1,K+1}=PN_{K,K}+B_{K+1}$. Its retained parent follows its unique physical forward path at each subsequent clock. [Canonical births at PR 193, commit 2796977](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/global/CANONICAL_BIRTHS.md)

Set $D=\ln(4/3)$, $L=\ln2$, and $\theta=D/(2L)$. For each escaping positive ordinary component $C$, fix a representative odd ray $(a_{C,r})_{r\ge0}$ as in the original ordinary trace theorems, with positive charge $H_C=(D/2)d_C$. Here $d_C$ is the odd-relative logarithmic mean of $F_C(x)=\mathbf1_C(x) f_\infty(x)$, $f_\infty=\lim_s f_s$. The named source inputs below give $\sum_C H_C<\infty$. Write $\|\cdot\|_1$ for the sum of absolute point masses on positive odd integers.

**Old cohort profile.** Under the stated first-hit and entrance inputs, uniformly in $0\le v\le\theta$,
$$
 \left\|\frac{N_{K,\lfloor vK\rfloor}}{K}-
 \sum_C \frac{H_C}{K}\sum_{\lceil(1-v/\theta)K\rceil\le r<K}
                    \delta_{a_{C,r}}\right\|_1\longrightarrow0.        \tag{1}
$$
The profile includes the entire last segment of the *specified actual ray* in each component. Differences of two cutoffs give the corresponding interior segment. Thus the old population at $v=\theta$ carries exactly the entire escaping trace in this norm. In particular
$$
 \lim_{K\to\infty}\frac{\|N_{K,\lfloor\theta K\rfloor}\|_1}{K}
       =\sum_C H_C.                                                     \tag{2}
$$
A zero lower subsequence on the left would exclude every positive escape under the same positivity input. The conditional formula does not establish that zero subsequence.

**Young cohorts.** With the additional pre-entry inputs specified below, for $\theta\le v\le1$ and any fixed function $V$ of the odd residue modulo $2^m$,
$$
 \frac1K\left\langle N_{K,\lfloor vK\rfloor}-N_{K,\lfloor\theta K\rfloor},V\right\rangle
        \longrightarrow L(v-\theta)\,\mathbb E_{\mathrm{odd}} V .     \tag{3}
$$
The expectation is uniform on odd residues. In particular the signed next-gap mark $W(e)=7/4-\min(e,3)$ has zero limit on every such interval, since $W(e(y))$ depends only on $y\bmod8$ and averages to zero. The remaining old interval has the actual ray sum in (1), including for this signed test. At the transition the older fraction is $\theta=0.2075\ldots$ of the birth depths. The nominal age at which a birth reaches the small core is $(\theta^{-1}-1)j=(\ln3/D)j$.

**The initial all-height window ends earlier.** For each fixed $0<\alpha<1/2$,
$$
 \sum_{\substack{x\ge1\ {\rm odd}\\T(x)\le\alpha\log_2 x}}\frac1x<\infty.\tag{4}
$$
Consequently (1) remains valid after retaining only sources for which the entire initial all-height test window ends strictly before birth. For every fixed $\epsilon>0$ it also remains valid after requiring $|M_\alpha(x)-(\ln2)^{-2}|<\epsilon$ of the very same source. Thus the ordinary initial statistic, even when tested on the specific sources that make up an old escaping cohort, supplies no signed cancellation after their passage to a common physical tail.

## Uniform cutoff for every bounded test

For each $J\ge1$, put $Y_J=2^{2J+1}$. There is the finite-scale, endpoint-independent bound
$$
 \sum_{x\ {\rm odd}}\frac{|\mathbf1_{T(x)\le J}-\mathbf1_{x\le Y_J}|}x
       \le\tfrac12\mathbb E|G_J-2J|\le\sqrt{J/2},                    \tag{5}
$$
where $G_J$ is the sum of $J$ independent geometric gaps of mass $2^{-e}$. On each octave $2^m\le l<2^{m+1}$, $T(1+2l)$ has exactly the law $1+\operatorname{Bin}(m,1/2)$. Equivalently the fraction born by $J$ is $\Pr(G_J>m)$. This follows from the odd parity cylinder bijection through the first $m$ unary gap bits. The cutoff $x\le Y_J$ includes precisely $l<2^{2J}$, and $x=1$ belongs to both sets. The discrepancy within octave $m$ has mass at most $\tfrac12|\Pr(G_J>m)-\mathbf1_{m<2J}|$. The sum of these probability differences is $\mathbb E|G_J-2J|$, by counting integral layers on each side of $2J$. The variance $2J$ gives the last inequality. In particular for every $K\ge J$,
$$
 \left\|N_{K,J}-\sum_{x\le Y_J,\ x\ {\rm odd}}
             \frac{f_K(x)}x\delta_{U^Kx}\right\|_1\le\sqrt{J/2}.      \tag{6}
$$
This holds for arbitrary endpoint tests, including all-future tests of that positive integer.

For (4), in octave $m$ one has $\log_2 x\le m+2$. At all sufficiently large $m$, $\alpha(m+2)\le(1/2-\eta)m$ for fixed $\eta>0$. The lower binomial tail bounds the octave fraction in (4) by $e^{-c_\alpha m}$, which is summable in harmonic mass. This exceptional set costs $O_\alpha(1)$ before normalizing by $K$, however the remaining sources are subsequently weighed or aged. For the second deletion in (4)'s consequence, the ordinary all-height theorem gives $o(K)$ total harmonic mass of $|M_\alpha-\kappa|\ge\epsilon$ for $x\le e^{BK}$ with fixed $B$. Use convergence in probability at $\epsilon/2$ to accommodate equality. The full canonical tail for $x>e^{BK}$ is negligible as shown next.

## Replacing the old source cutoff by the physical entry clock

Let $\tau_M(x)$ be the first odd clock in the finite set of odd states at most $M$, with infinity on failure. We use two fixed-source facts from Valbuena's pinned manuscript. For each fixed odd target $z$, outside an odd set of absolute logarithmic density zero in its hitting basin, its actual first-hit time obeys $|D k_z(x)-\ln x|\le\epsilon\ln x$ for every fixed tolerance $\epsilon>0$. This is Proposition ct-time-law. The global-minimum law is tight, so the upper odd logarithmic density of sources never hitting any odd number through $M$ tends to zero with $M$. The two facts only require fixed targets before taking $M\to\infty$. The odd restriction of the minimum law also follows from the shortcut version by bounded comparison to the complete harmonic sample and the initial decreasing even chain. The source's external analytic dependencies are retained. [Valbuena, fixed source, Proposition ct-time-law and minimum law](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex)

Fix $B$ sufficiently large. For the canonical population at depth $K$, sources $x>e^{BK}$ have total mass exponentially small. Indeed $x<2^{E_K+1}$ from the birth criterion and $3^K2^{-E_K}/U^Kx\le 3^K2^{-E_K}$. Summing the single canonical source per gap word bounds the tail by $3^K\Pr(G_K>B K/L-1)$, exponentially small by $\mathbb E(3/2)^{G_K}=3^K$. For fixed $M$ and all large $K$, a source entering the core by $K$ is automatically canonical at $K$, since its endpoint is at most $(M+1)(3/2)^K<2\cdot3^K$. This justifies the same tail removal for all core-entry measures below.

At fixed $M$ take the finite union of the fixed-target exceptional sets. Every remaining source of height at most $e^{BK}$ that visits the core obeys $|D\tau_M(x)-\ln x|\le\epsilon BK$. The cost of the exceptional sources is $o_{M,\epsilon,B}(K)$ in harmonic mass. The cost of those never visiting the core is $O_B(e(M)K)+o_M(K)$ with $e(M)\to0$. For $J=\lfloor vK\rfloor$, $0<v\le\theta$, the threshold $\ln Y_J$ differs from $D(v/\theta)K$ by $O(1)$. Thus replacing $x\le Y_J$ by $\tau_M(x)\le\lfloor(v/\theta)K\rfloor$ on these sources costs at most the harmonic mass of a log-height band of width $2\epsilon BK+O(1)$. This is $O_B(\epsilon K+1)$. All comparisons allow arbitrary endpoint tests bounded by one. Equation (6), followed by $K\to\infty$, $M\to\infty$, $\epsilon\downarrow0$, therefore gives the desired replacement with vanishing normalized error. At $v=0$, the initial source $x=1$ has bounded total weight.

## Actual transport after entry

For fixed $M$ and $z\le M$ odd let $Q_{i,z}$ be the sum of $f_i(x)/x$ over ordinary odd sources first entering the core at time $i$ and site $z$. The ordinary first-entry theorem gives $Q_{i,z}\to c_{M,z}$. The post-entry contribution selected by the preceding time cutoff is exactly
$$
 \sum_{z\le M}\sum_{0\le i\le\lfloor(v/\theta)K\rfloor}
          Q_{i,z} f_{K-i}(z)\,\delta_{U^{K-i}z}.                        \tag{7}
$$
For fixed $M,z$, replacing $Q_{i,z}f_{K-i}(z)$ by $c_{M,z} f_\infty(z)$ costs $o_M(K)$ in the sum of absolute errors: remove finitely many terms with small $i$ or $K-i$, then use convergence on the rest. Periodic component entrances give $f_\infty(z)=0$. In each escaping component change to its fixed ray after the finite coalescence time. A fixed shift of a consecutive sequence of sites changes only a bounded number of endpoints in its counting measure. The lower time cutoff on the remaining ray is $(1-v/\theta)K+O_M(1)$. Finally the ordinary entrance theorem identifies the component weights $\sum_{z\le M,\,z\in C}c_{M,z} f_\infty(z)$ with $H_C$ up to total deficit tending to zero as $M\to\infty$. These are precisely the fixed-entrance and charge inputs from the proof of the original exponential dust theorem, equations (21)–(22) of its named source. This proves (1) at every fixed $v$. To get uniformity use a finite grid in $[0,\theta]$. The measures on both sides are monotone in $v$ and the limiting mass added on each grid subinterval is at most $(\sum_C H_C)$ times its length divided by $\theta$. Squeeze and refine the grid. [PR 193, original entrance and ray decomposition](https://github.com/GettysburgResearch/collatz/blob/2796977d3f02ad57daeb7510f16da29527f9afde/research/astra-six-hour-20261127/escape/EXPONENTIAL_DUST.md)

For (3) subtract the $v=\theta$ cutoff, which represents all post-entry sources up to $o(K)$ in the prescribed successive limits. On the remaining pre-entry sources the original ladder estimate (5) of that same manuscript gives $\ln U^Kx=\ln x-DK+O_B(K^{3/5})$ outside a set of normalized source mass tending to zero as $M\to\infty$. To apply this comparison keep only canonical sources at final depth, using (5) to delete noncanonical sources below $Y_J$ at $o(K)$ cost. Then $x\le Y_{\lfloor vK\rfloor}$ is equivalent, up to $o(K)$ in harmonic comparison and the ladder exceptional mass, to $K^{-1}\ln U^Kx\le 2Lv-D$. Indeed its discrepancy forces $\ln x$ into a band of width $O_B(K^{3/5}+1)$ around $\ln Y_J$. On the pre-entry population the original dust theorem gives intensity $dt/2$ on $0\le t\le\ln3$, with uniform odd dyadic label, including for differences of fixed height cutoffs. This yields $(2Lv-D)\mathbb E V/2=L(v-\theta)\mathbb E V$. At $v=1$ the upper endpoint is $2L-D=\ln3$. These statements resolve macroscopic intervals of birth depths at fixed terminal time. They do not claim single-cohort cancellation at every individually specified old age.

## A permanent test carried at arbitrary ages

For every escaping component $C$, $P^*F_C=F_C$ pointwise on the positive odd integers. Thus for *arbitrary* nonnegative integer ages $s_j$, even chosen separately at different births,
$$
 \sum_{j=0}^J\langle P^{s_j} B_j,F_C\rangle
       =\sum_{T(x)\le J}\frac{F_C(x)}x
       =L d_C J+o(J).                                                   \tag{8}
$$
The first identity follows from $f_j(x)F_C(U^j x)=F_C(x)$ and exact source retention. The second follows from (5) and the defining odd-relative logarithmic mean of $F_C$. On any macroscopic interval $aK<j\le bK$ the corresponding mass is $(b-a)Ld_C K+o(K)$. No positive age can erase this particular mass by reapplying the deterministic transition. At $b=\theta$ its coefficient is $\theta Ld_C=H_C$. Equations (1) and (8) preserve both ordinary integrality and original weights. Their remaining obstruction is an estimate forcing the explicitly specified old-cohort measure in (2) to have a zero lower subsequence. No positive integer violating Collatz has been constructed.
