# Trace sampling on the actual head edges

**PROPOSED written bounds.** The measure in this file counts each original head child once. First-passage and finite-profile inputs are fixed at PR197 `9ab91d964b38fc870d1034bac628d62f59488467`. The full convergence coloring remains open. The reach of the estimates is specified by three different tests: weights at the landing, arbitrary sparse marks before the landing, and paths after the landing.

## A summable weighted sampling inequality

Let $x$ be uniform on $[7R_j,8R_j)$, $R_j=81^j$, and $m=\lfloor x/81\rfloor$. Write $d_j=\log_2R_j$, $M_j=d_j^D$ and $v_j$ for the first shortcut iterate below $M_j$ of one labeled arm. Set $v_j=\partial$ if it misses, and put $g(\partial)=0$. For each fixed $A>1$ and every sufficiently large fixed $D$, [PR197, LANDING_WEIGHT_TRANSFER, (1)](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/LANDING_WEIGHT_TRANSFER.md) selects a deterministic pair-merger clock $h_{*,j}$. Let $E_j$ mean that the two original arms fail its finite merger certificate. In particular any true component discordance is contained in $E_j$. On a common regular set with exception $O_A(d_j^{-A})$, each individual point has weight

$$ \mathbb P(E_j,\ v_j=z,\ \text{regular})\ll_A (\log d_j)^{3/2}/M_j,
 \qquad M_j/2\le z<M_j. \tag{1} $$

For every bounded $g:\mathbb N_{>0}\to[0,\infty)$ this gives

$$ \sum_{j\ge2}\mathbb E[\mathbf1_{E_j}g(v_j)]
 \ll_{A,D} \|g\|_\infty+\sum_{z\ge1} g(z)\, z^{-1+1/D}(\log(2+z))^{3/2}. \tag{2} $$

Indeed $M_j$ is a fixed constant times $j^D$; each positive $z$ lies in at most $O_D(z^{1/D})$ of the bands $M_j/2\le z<M_j$, in which $M_j\asymp z$. Sum the exceptions against $\|g\|_\infty$ and interchange the remaining nonnegative sums. Finitely many small rows cost a bounded multiple of $\|g\|_\infty$. Equivalently, for every $\eta>0$ we can select $D$ so that $z^{-1+\eta}$ dominates the weight on the right. The cutoff and measured landing law vary with this choice of $D$; there is no conclusion at the critical weight $1/z$ with $D$ fixed.

For example, let $S_j$ be any forward-invariant union of at most $d_j^B$ whole prescribed ordinary forward trajectories, where $B$ is fixed. Leen's uniform orbit sparsity $\#(O\cap[M/2,M))\ll M^\theta$, $\theta<1$, bounds its landing-band size by $O(d_j^BM_j^\theta)$. By (3) of [MEETING_CLOCKS.md](MEETING_CLOCKS.md), reaching $S_j$ at **any** clock through first passage is equivalent to a landing in $S_j$ when passage is finite. In addition to the exceptional mass, (1) thus costs

$$ O_A\big((\log d_j)^{3/2}d_j^B M_j^{\theta-1}\big). \tag{3} $$

This estimate is on the actual missed head pair and can be added over the two labels or intersected with any later source selection. Arbitrary tests at unbounded future times can be used to *select* a subset of this counted event. The assertion does not let the future selection pick a different trace dictionary for each original source. One prescribed dictionary per row, or conditioning on an independent dictionary, is allowed. The corresponding unfiltered estimate has an extra factor $\sqrt{d_j}$ in the second term. Enlarging the fixed $D$ still gives any prescribed negative power of $d_j$.

## Occupation of arbitrary sparse sets throughout first passage

Forward invariance need not hold for a set of marks. There is a direct bound on all actual visits. Work on either arm with original $n$ in a fixed-ratio positive annulus of scale $R$ (the fixed parent multiplicity in a head row is harmless). Put $d=\log_2R$. Fix $A>0$. Use the [PR197 simultaneous sliding-window first-passage theorem](https://github.com/GettysburgResearch/collatz/blob/578e43911f49d41ef610b368a89b5a1ec269e134/research/ayh-resource-reset-20261124/literature-step/FIRST_PASSAGE_MARKS.md). Outside $O_A(Rd^{-A})$ sources, $h=\tau_M(n)\le H\ll_A d$ at $M=d^D$, and every full $b$-block before $h$ has at most $.525b$ odds, with $b=\lceil K_A\log_2 d\rceil$. We may enlarge $D$ after fixing $K_A$. Put $y_i=T^i n$.

For $i<t\le h$, each full $b$-block beginning at $i$ and ending by $t$ contracts the height by at least the factor $2^{-c b}$ (in the sense $y_{s+b}\le 2^{-cb}y_s$), from the exact multiplier and $y_u\ge M$ for $u<h$. The at most $b-1$ remaining steps grow by at most $2^b$. Consequently with $z=y_t$,

$$ \sum_{i<t}\frac1{y_i}\le \frac{b2^b}{z(1-2^{-cb})},
 \qquad z\le C R2^b. \tag{4} $$

For the sum, group $i$ by $\lfloor(t-i)/b\rfloor$. There are at most $b$ indices in each group. Equation (4) holds at a realized non-record height as well as at a first crossing. The accumulated logarithmic odd-branch correction at $t$ is therefore $O(b2^b/z)$. For fixed $t,z,p$ the possible original inputs in this annulus lie in a single interval of length $O(R b2^b/z)$ by the exact multiplier. Choose $D>K_A+2$, so the correction is uniformly $o(1)$ since $z\ge M/2$. For a fixed $t,z$, only $O(1)$ values of $p$ occur, because centers for consecutive $p$ have ratio three. The integer rounding term is absorbed by $O(R b2^b/z)$ using the upper bound on $z$ in (4). Thus for every function $0\le g_j\le1$ chosen independently of the original source, the original-source regular occupation satisfies

$$ \frac1R\sum_{n\text{ regular}}\sum_{t=0}^{\tau_M(n)}g_j(T^t n)
 \ll_A d b 2^b \sum_{M/2\le z\le C R2^b}\frac{g_j(z)}{z}. \tag{5} $$

A visit probability for an indicator is at most the right side plus the exceptional $O_A(d^{-A})$. The bound counts atypical starts once in this probability statement; no bound on their uncapped occupation is needed. In particular, suppose a moving mark set $S_j$ obeys $\#(S_j\cap[L,2L))\le C d^B L^\theta$ for all dyadic bands meeting the range of (5), with $\theta<1$ fixed. Enlarging bands by bounded factors handles the first and last partial bands (equivalently assume the bound on all integer $L\ge1$). Summing the weighted tail gives $O(d^B M^{\theta-1})$. Increasing $D$ again bounds the entire visit probability by $O_A(d^{-A})$. The marks can be unrelated to trajectories and need not persist even one additional step. The result includes any adaptive choice of the hitting time within the prefix. In the forward-invariant case (3) removes the larger occupation factor and allows finite-error weighted summation as in (2).

### A delay measured from a higher landing

Fix $A,B,\theta$ as above and $\epsilon>0$. Choose $0<\delta<1/40$, then $b=\lceil K\log_2 d\rceil$ large enough to enforce the sharper lower odds bound $(1/2-\delta)b$ on every full block through the lower passage. In the quoted first-passage proof this replaces the constant Hoeffding exponent by $2\delta^2$ and is achieved by increasing $K$; the dyadic-grid and $O(d^3)$ first-entrance costs are unchanged. First choose a fixed lower exponent $D_0$ meeting all preceding error requirements. Then choose a much larger fixed $D$. Let $h_0,h_1$ be the first passages to $M_0=d^{D_0}$ and $M_1=d^D$ respectively (so $h_1\le h_0$). At $h_1$ the height is at least $M_1/2$. Every whole $b$-block before $h_0$ decreases by a factor no worse than $2^{-(a+\delta\log_2 3)b}$, by its lower odd count and the nonnegative additive correction. The last partial block decreases by at most a factor $2^b$. As $T^{h_0} n<M_0$,

$$ h_0-h_1\ \ge\frac{\log_2(M_1/M_0)-1-b}{a+\delta\log_2 3}
 \ \ge (1/a-\epsilon)\log_2 M_1. \tag{6} $$

Choose $\delta$ sufficiently small in terms of $\epsilon$, then $D$ sufficiently large compared to $D_0,K$. By (5), off $O_A(Rd^{-A})$ original sources, neither arm visits its prescribed sparse mark set before or at $h_0$. Thus a subsequent hit must take at least the additional time (6) *after the higher first passage*. The entire marked event up to $h_0$ was counted from the original source. No fresh randomness at $M_1$ or $M_0$ was used.

## Two classes at the native deadline, even with additional affine arms

For any fixed $r$ consider $m,81m+r$ and any fixed finite menu of additional positive affine arms $3^{a_i}m+c_i$ on the head parameter interval $[7R_j/81,8R_j/81)$. Set $h_j=\lfloor\log_2(R_j/81)\rfloor$. On a complete $2^{h_j}$-bit block the signed grade difference of the head pair starts at four. Until its first zero its mixed-step walk uses independent fair signs: at a mixed step the next free binary digit decides the sign, with all previous bits fixed. A fair walk kept positive for its first $h_j$ moves remains positive for every physical clock through $h_j$, since at most that many mixed moves can occur. Reflection gives probability $\gg h_j^{-1/2}$. A full consecutive block occupies at least half the parameter interval. Thus $\gg R_j/\sqrt j$ original children for this one suffix still have distinct head profiles. On the other hand, [PR197, TRIPLE_SUBCRITICAL_MOMENTS](https://github.com/GettysburgResearch/collatz/blob/9ab91d964b38fc870d1034bac628d62f59488467/research/ayh-resource-reset-20261124/joint-renewal/TRIPLE_SUBCRITICAL_MOMENTS.md) bounds the fraction with three or more complete surviving profiles by $o(j^{-4/3})$ for any fixed menu. After subtraction the same order lower bound survives with *exactly two* classes and the original head pair in different classes; the standard pair upper bound gives $O(R_j/\sqrt j)$. The lower constant may be chosen independent of the menu once the row is large enough for that menu.

For any sequence of increasing fixed finite menus exhausting a countable family (each eventually positive), a diagonal choice of an increasing row threshold for each menu gives the same lower bound with a menu size tending arbitrarily slowly to infinity. One may choose these thresholds so the absolute normalized three-class errors are summable over all selected rows: for menu $k$ choose its tail sum at most $2^{-k}$ before moving to the next menu. This gives no prescribed rate of menu growth. The surviving classes need not have different eventual colors. In particular even exhaustive finite menus with this slow growth cannot rule out the two-class profiles based solely on the number of classes present.

At all times, the predecessor set of even one fixed odd ternary unit can have positive lower density. Replacing a forward trace by its entire ancestor set destroys the sparsity in (3) and (5); for the known basin of one this occurs irrespective of the conjecture. Full head closure requires a mark that distinguishes the two actual eventual colors with its true original-source multiplicity. Equations (2)–(6) cover weighted landings, sparse prefix visits and a post-landing clock window. The unrestricted two-class discordance has no proved bound here.
