# Spatial distribution of Collatz component colors and a shrinking-interval closing criterion

**Status.** Written quantitative theorem using the frozen PR 146 finite-grid merger bound. The deduction from a one-patch collision hypothesis to global convergence additionally uses Mazur's source-qualified positive lower natural density of the ordinary predecessors of each fixed positive ternary unit. The collision hypothesis is open. The binary and mixed-progression physical lift, their normalized intercept bounds, the finite two-color obstruction, and the finite averaging inequality combining rotation and grid errors are separately formalized in `PatchPairCounting.lean`.

Use the shortcut map $T(n)=n/2$ for even $n$, $T(n)=(3n+1)/2$ otherwise. Write $x\sim y$ if their ordinary positive trajectories meet at independently chosen finite clocks. A component color is any $f:\mathbb N_{>0}\to\{0,1\}$ satisfying $f(Tn)=f(n)$. In particular one may use the indicator of reaching one. Put $R_j=81^j$ and use the whole logarithmic circle
$$
 G_j(u)=f(\lfloor R_j81^u\rfloor),\quad 0\le u<1,\qquad p_j=\int_0^1G_j(u)\,du.
$$
The head $[7R_j,8R_j)$ occupies its fixed subarc $[\log_{81}7,\log_{81}8)$.

**Interval discrepancy theorem.** Let $q$ be any continued-fraction denominator of $\theta=\log_{81}2$. There is an absolute $C$, independent of the color, interval and denominator, such that every circle interval $W$ satisfies, for all $j\ge1$,
$$
 \left|\int_W G_j(u)\,du-|W|p_j\right|
 \le C\left(\frac{q}{\sqrt j}+\frac1q\right).                                      \tag{1}
$$
Thus if $q_j$ is the largest such denominator at most $j^{1/4}$ and $e_j=q_j/\sqrt j+1/q_j$, then $e_j\to0$ on all levels. In fact $e_j=O(1/\log(2+j))$ on every level: for consecutive denominators $q,q'$ and numerator $a$, distinct integers $2^q,81^a$ and $|q\theta-a|<1$ give $|q\theta-a|\ge1/(81\cdot2^q\log81)$ by the mean-value theorem. The convergent bound $|q\theta-a|<1/q'$ then gives $q' <81(\log81)2^q$, hence $q_j\gg\log j$ eventually. At the explicit levels $j=q^4$ the error is $O(j^{-1/4})$. Every weak-star accumulation point of the $G_j$ is constant; this does not assert that $p_j$ itself converges. The proof does not require a prior density theorem for basin colors.

**One-patch collision criterion.** Let $j_s\to\infty$, and let $W_s$ be intervals in the fixed head arc with lengths $\ell_s>0$ such that $e_{j_s}=o(\ell_s)$. For each $s$ take two independent uniform ordinary integers from
$$
 B_s=\{n:\log_{81}(n/R_{j_s})\in W_s\}.
$$
If the probability that their forward orbits meet tends to one, then all positive integers reach one. Conversely, universal convergence implies meeting probability one at every level. The location may move within the head. One fixed arbitrarily short interval suffices. Along $j=q^4$ one may, for example, take lengths $j^{-1/5}$, corresponding to integer widths of order $R_j/(\log R_j)^{1/5}$. The criterion also works anywhere within one such full annulus. A finite merger checker certifying an asymptotic proportion one of all ordered pairs in these patches would establish the hypothesis. No bound on the clocks or surrounding levels is required.

Equivalently the patch contains one component of proportion tending to one: the actual merger probability is $\sum_C (|C\cap B_s|/|B_s|)^2$, which lies between the square and the first power of the largest component share. That component can depend on $s$. A collision estimate along only a deterministic pair such as $(n,\lfloor n/81\rfloor)$ has a different sampling law and does not establish this hypothesis.

## Proof of (1)

The only Collatz counting input used below is the finite-grid estimate in PR 146, already identified in `GROWING_HEAD.md`. For $a\ge0$, $c\ge0$, and on a complete residue grid for $m$ modulo $2^b$, the proportion lacking a counted physical fusion by time $b$ between $m$ and $3^am+c$ is at most
$$
 C_0(1+a+\sqrt{\log(2+c/3^a)})/\sqrt{b}
$$
for $b\ge1$. A successful class is valid on all its positive ordinary lifts. Tiling an interval by full grids leaves fewer than $2\cdot2^b$ boundary points. Take $b=\lfloor(\log_2R_j)/2\rfloor$; then $b\asymp j$ and $2^b/R_j\le R_j^{-1/2}$. Taking $a=4$ and $0\le c<81$ gives, by division into child cells and the bounded log density on the annulus,
$$
 \|G_{j+1}-G_j\|_1\ll j^{-1/2},\qquad
 \|G_{j+d}-G_j\|_1\ll d/\sqrt j\quad(d\ge1).                         \tag{2}
$$
For the first estimate, each bad parent in $[R_j,81R_j)$ contributes at most $1/(81R_j\log81)$ from a particular child. There are only 81 child offsets.

For $M=2^k$, $0\le h<M$, the ordinary affine lifting formula is
$$
 T^k(Mm+h)=3^{a_h}m+c_h,\quad a_h=\#\{0\le i<k:T^i(h)\hbox{ odd}\},\quad c_h=T^k(h).
$$
At zero use the even extension $T(0)=0$ solely for this identity. Dividing the affine intercept expansion by $3^{a_h}$ gives
$$
 0\le c_h/3^{a_h}=h/2^k+
 \sum_{i<k:\,T^i(h)\ \mathrm{odd}}2^{i-k}/3^{a_{i+1}(h)}<4/3.
$$
Indeed the sum of the $2^{i-k}$ is less than one and the denominator on each listed term is at least three. Hence the finite-grid theorem compares $f(Mm+h)$ with $f(m)$ on all but $O((k+1)R_j/\sqrt j)$ parents in $[R_j,81R_j)$, uniformly in $h$. This uses the full affine odd/even lifting, not a law on transported partners.

For $u$ on the circle put $v=\{u+k\theta\}$ and $d=\lfloor u+k\theta\rfloor$. Exactly $R_{j+d}81^v=M R_j81^u$. Within each cell $m=\lfloor R_j81^u\rfloor$, each offset $h=\lfloor M\{R_j81^u\}\rfloor$ occupies an interval of length $1/(M R_j)$ in $81^u$. Its log measure is at most $1/(MR_j\log81)$. Summing the preceding estimate over $h$ cancels $M$ and yields
$$
 \int_0^1 |G_{j+d}(v)-G_j(u)|\,du\ll (k+1)/\sqrt j.
$$
The index $d$ assumes at most two nonnegative values, both at most $k+1$. Rotation preserves log measure, so on each corresponding piece (2) permits replacement of $G_{j+d}(v)$ by $G_j(v)$ with total $L^1$ error $O((k+1)/\sqrt j)$. This proves the quantitative rotation estimate for each $k$.

Average for $0\le k<q$. If $a/q$ is the corresponding convergent, $|k\theta-ka/q|<1/q$. The translated grid $ka/q$ has interval counting error at most $2/q$. Perturbing every grid point by less than $1/q$ can affect membership only within $1/q$ of an endpoint, again costing $O(1/q)$ uniformly in the translate and interval. Thus $q^{-1}\sum_{k<q}1_W(v-k\theta)=|W|+O(1/q)$ pointwise. Integrating against $G_j(v)\in[0,1]$ and averaging the rotation error proves (1). Interval step approximation proves the weak-star assertion.

## From global abundance to both colors on every resolved patch

Suppose a particular color has at least $cX$ members below every sufficiently large $X$. Write $p_j$ for this color's log share. It counts at most $81R_j(\log81)p_j$ integers in the full $j$-th annulus, since each included integer occupies log measure at least $1/(81R_j\log81)$. Fix $s$ with $81^{-s-1}<c/2$. Counting below $81R_j$ and discarding $n<R_{j-s}$ shows
$$
 c/2\le (\log81)\sum_{d=0}^s81^{-d}p_{j-d}
 \le (81/80)(\log81)(p_j+o(1)),
$$
where (2) gives the last inequality at this fixed $s$. In particular $\liminf p_j\ge 40c/(81\log81)>0$. The same proof applies to the other color with its own constant.

If an ordinary positive counterexample exists, apply Mazur's formalized `nonconvergence_positive_lower_density_of_counterexample` to the color failing to reach one and his fixed-target positive lower density at target one to the opposite color. Reaching one agrees for ordinary and shortcut maps: an ordinary odd step to $3n+1$ is grouped with its next halving, and the omitted intermediate is even and greater than one. No claim about shortcut visits to an arbitrary skipped even target is needed. There is now a single $\kappa>0$ with $\kappa\le p_j\le1-\kappa$ eventually. Formula (1) puts at least $(\kappa-o(1))\ell_s$ of each color's log mass on any resolved patch. Converting to uniform integer counts preserves a positive fraction uniformly: each cell has mass at most $1/(R_j\log81)$, the patch contains at most $81(\log81)R_j\ell_s+2$ integers, and at most two cells are cut by endpoints. Since $R_j\ell_s\to\infty$, each color has some fixed fraction $\varepsilon>0$ in each sufficiently high patch. The probability of different colors is at least $2\varepsilon^2$. Two different colors cannot have a common future. This proves the one-patch criterion.

The classical Krasikov–Lagarias $X^{0.84}$ theorem alone does not give the positive fractional lower bounds in this last argument. With that published input the separate power-sparse criterion of `HEAD_EDGE_RIGIDITY.md` remains available. With Mazur's positive lower density, that earlier argument also gives closure from $\sum_j D_j/R_j<\infty$, since the limiting constant then forces a zero-density color. Criterion (1) and the one-patch collision result do not assume that summability.

## One prescribed residue on each side

The closing criterion still holds if each sample is uniform on one prescribed residue class in its patch, independently between the arms. The two patches, moduli and residues may differ. For a given arm write the modulus as $M=2^k3^a$ and allow $0\le r<M$. Require both $e_j=o(\ell)$ and $(1+k+a)/\sqrt j=o(\ell)$ along the chosen levels, in addition to the requirements on each patch stated above. In particular on $j=q^4$, two arbitrary residues modulo $2^{\lfloor j^{1/4}\rfloor}3^{\lfloor j^{1/4}\rfloor}$ can be used in two intervals of log width $j^{-1/5}$.

To verify this, write $r=2^k t+h$, $h<2^k$. The lift from the preceding proof gives
$$
 T^k(Mm+r)=3^{a+a_h}m+3^{a_h}t+c_h,\qquad
 (3^{a_h}t+c_h)/3^{a+a_h}<1+4/3.
$$
The finite-grid bound on the parent coordinate therefore incurs error $O((1+k+a)/\sqrt j)$ as a fraction of its full annulus. Indeed this annulus has scale comparable with $Y=R_j/M$, with $\log Y\asymp j$ since $k+a=o(\sqrt j)$. There is no modulus factor in this relative error. The admissible $m$ form an interval obtained by subtracting $r$ from the physical patch and dividing by $M$. Its logarithmic length is $\ell+O(M/R_j)$ before integer endpoint rounding, by the mean-value theorem. In particular its length is $\ell(1+o(1))$. It intersects at most two adjacent full parent annuli (the patches are within the fixed head), at levels $j-O(1+k+a)$. Apply (1) there with the original denominator $q_j$. Its error stays $O(e_j)$ on both, and both annular means have the same eventual positive lower bound for each of the two colors. Summation and conversion from log mass to ordinary counts give $\gg Y\ell$ parents of each color. The number whose lifted child color can change is $O(Y(1+k+a)/\sqrt j)=o(Y\ell)$. Since the sample contains $O(Y\ell)$ integers, both actual colors have fixed positive conditional shares on this single progression. Opposite colors across the two independent samples then force a positive meeting deficit. The two arms can even be taken from different sequences of levels if each separately satisfies these estimates. This result does not assume a new parity distribution conditional on a component.

## Sources and boundary

* Finite-grid affine-profile estimate and its normalization: [frozen PR 146](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md), as used in the PR 197 continuation `GROWING_HEAD.md` at `9ed095c3b3386d66c1dba103117e8dda0268b7aa`.
* Lech Mazur, *Positive Lower Density of Collatz Predecessors*, 6 September 2026. The [author's formalization record](https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/) names the two exact ordinary-map public roots. It reports a 388-file owning-target check at `c290ac229b379d2b51026d3e86140496870d6f39`, with pinned precompiled third-party dependencies and only the three named standard Lean principles. The source supplement SHA-256 is `55ceb4df0cca17ae728dc65b30bf5077000e1b47f2dc322454eea9f637ac75b3`. The companion [paper, Theorem 1.1 and Corollary 1.2](https://www.proofatlas.ai/papers/positive-lower-density-collatz-predecessors/paper-v1.pdf) transfers inherited weighted inverse-path estimates to a nonperiodic odd seed in a prescribed ternary class reaching the target. The absence of a return to that seed prevents double-counting distinct depths. Equation (1.3) gives the precise inclusion of ordinary predecessors of $2a$ in shortcut predecessors of $a$. This packet imports the advertised mathematical scope; it did not rebuild the compatibility baseline, reproduce that audit, or infer positive density from the earlier $X^{0.901}$ theorem.
* The [preceding log-time paper, Theorem 1.1](https://www.proofatlas.ai/papers/positive-density-log-time-collatz/Mazur_Explicit_Positive_Density_Collatz_Convergence_in_Logarithmic_Time_v2.pdf) gives an explicit positive fraction at target one. In the fixed-target paper, Proposition 3.1 sums selected inverse words over sources in $[X,32X)$ against an auxiliary ternary weight. The prescribed congruence selects the endpoint seed; it does not condition the source samples in the one-patch criterion. Estimates (4.4)–(4.6) remove the auxiliary weight and give a fixed positive fraction, without an estimate for the fraction of uncovered starts in a chosen source patch. A single word ending at one fixed seed specifies just one ordinary start.
* Remaining positive task: prove concentration in one actual common-future component on independently sampled pairs in some resolved patches. The pre-existing merger theorem compares prescribed affine pairs. A continuation method would need control of common-future probabilities for the two separately sampled starts in the displayed law, or an equivalent dominant-component certificate.
