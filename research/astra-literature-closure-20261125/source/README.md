# First-entrance gates for all sites of an ordinary query window

**PROPOSED written theorem with finite Lean components. Universal convergence is OPEN.** Fix the original PR197 row and its good physical envelope. Given $A$, one can choose a fixed exponent $B$ as large as desired. Write $M=\lceil d^B\rceil$ and $W=\lceil\sqrt{d\log d}\rceil$. For any prescribed gate bank $G\subset[M/2,M)$, the fraction of all parents that are on the good envelope and have **some site of some eligible physical query window** whose first entrance below $M$ lies in $G$ is at most
\[
 O_A(d^{-A})+O_A\!\left(\frac{|G|\,W\log d}{M}\right).                    \tag{1}
\]
Constants can also depend on the fixed schedule and $B$. All sites first cross the common floor outside the first error term. The estimate applies to a gate bank defined by the actual orbit colors. The second term has no multiplicity factor for the number of query windows, reply paths, sites or opening seeds. It gives a saving for sparse gate banks. For positive-density banks it is trivial.

## Physical sites on the original row

Use $T(2m)=m,\ T(2m+1)=3m+2$. Fix a suffix $0\le u<81$, $R=81^j$, $d=\log_2 R$, and $N=R/81$. The $N$ original parents satisfy $7R\le81n+u<8R$. Fix PR197's zero-ternary-advice logarithmic microblock schedule. Count original parents as a fraction of $N$, without any averaging over unrestricted positive lifts.

For every eligible actual query center of a good parent at $3d\le t\le3.1d$, each positive site $z$ in its full aligned window satisfies
\[
 z=F n+i3^e+\epsilon,\qquad F=3^k2^{-t},\quad k=t/2+O(W),\quad
 0\le e=O(W),\quad |i|\le d^C,\quad |\epsilon|\le d^C .                 \tag{2}
\]
The integral displacement $i$ is measured in lattice sites from the actual query. A shifted site need not have a source lift with the same seeds. To verify (2), the center is $\lfloor3^e m/2^\Delta\rfloor+b$ with bounded correction, $m=\lfloor3^{k_0}2^{-t_0}n\rfloor$, $\Delta=t-t_0$ and $k=k_0+e$. The rebase slope $3^e2^{-\Delta}\le1$ and the two floors cost at most two in the ordinate. A bottom endpoint arises by a last division by 81 with its corresponding reduced exponent and bounded correction. Reindexing adds exactly $i3^e$. This uses the physical seeds and retained correction checks; arbitrary synthetic intercepts need not satisfy (2).

With $a=1-\frac12\log_2 3$, the scale $Z=FN=2^{d-at+O(W)}$ has $.34d<\log_2 Z<.40d$ eventually. Also $|i3^e|\le2^{O(W)}$. Thus all sites for fixed $t,k,e,i$ lie in $[5Z,10Z]$. At each exact bad ordinate $z$ there are $O((d^C+1)/F+1)$ possible parents by the real interval (2). Keeping the large translation $i3^e$ fixed is important. The integers $t,k,e,i$ run through $d^{O(1)}$ tuples. If each site scale $[5Z,10Z]$ contains $O(Zd^{-L})$ scalar exceptions, the fraction of original parents having **even one exceptional site** is $O(d^{C_1-L})$. The schedule and envelope determine $C_1$ before the scalar accuracy is chosen. This also covers formal reply choices subject to (2). Intersecting with a source selection does not increase this absolute count.

## Scalar first passage at the required precision

For every fixed $L$ there are $b=\lceil K\log_2 d\rceil$ and a sufficiently large $B$, freely increasable thereafter, such that outside $O(Zd^{-L})$ sites in $[5Z,10Z]$ the **first** $h$ with $y=T^h z<M$ satisfies
\[
 h=O(d),\quad |p_h(z)-h/2|=O_L(W),\qquad
 0\le y-3^{p_h(z)}2^{-h}z=O_L(b),\qquad M/2\le y<M.                   \tag{3}
\]
Here $p_h$ counts odd departures. A typical height estimate at one later successful clock alone would not establish (3).

We extend the stopped-source argument of PR197, FIRST_PASSAGE_MARKS, equations (2)–(5). Choose fixed $0<\eta<a$, $\lambda=1-(a-\eta)/2$, thresholds $Y_0=11Z$, $Y_{j+1}=Y_j^\lambda$ and $k_j=\lfloor(\log_2Y_j)/2\rfloor$. Stop at the first $J$ with $Y_J\le M$. Use $z$ at the initial stage and the first entrance below each $Y_j$ thereafter. For large $d$, $Y_1$ is below the entire initial interval. The block budgets sum to at most $H=\lceil\log_2(11Z)/(a-\eta)\rceil=O(d)$.

On the complete binary grid of length $k_j+3b$ discard a word in any of these cases.

1. Its first $k_j$ odd count exceeds $(1/2+\eta/(2\log_2 3))k_j$.
2. Some length-$b$ subword starting at $0\le i\le k_j+b$ has odd count differing from $b/2$ by at least $b/40$.
3. Some prefix of length $v\le k_j$ differs from $v/2$ in odd count by more than $C_L\sqrt{k_j\log d}$.

Parity coding is bijective. Hoeffding and the union bound over $O(d)$ lengths give failure $O(d^{-L-6})$ for the third test. For the second increase $K$. For the first increase $B$ since $\log_2Y_j>\log_2M$ for every tested stage. Also take $B$ large enough that $k_j+3b\le\log_2Y_j$ and $M>H$.

The transfer to original scalar sources costs $O((H+1)^3)$ per stage in relative count. At first entrance through $Y_j$ by time $s\le H$ the landing $v$ is in $[Y_j/2,Y_j)$. With odd count $p$ the ratio $v/(3^p2^{-s}z)$ lies between 1 and $(1+1/(3Y_j))^H$ by multiplying the physical steps. For fixed $s,p,v$ this puts the possible $z\in[5Z,10Z]$ in an interval of length $O(HZ/Y_j)$. Its cardinal is $O((H+1)Z/Y_j)$. A bad residue set of proportion $\rho$ includes $O(\rho Y_j)$ possible $v$ by complete-period covering. Sum over the $O((H+1)^2)$ pairs $s,p$. At the initial stage direct residue covering costs $O(Z\rho)$. The $O(\log d)$ stages together give the claimed exceptional count, without any uniformity assumption for a stopped distribution.

The first test takes a start below $Y_j$ below $Y_{j+1}$ within $k_j$ steps: the elementary estimate $T^k v\le3^{p_k}(2^{-k}v+1/3)$ gives a strict exponent margin from $\eta$. Induction proves timely first crossing. Partition the path up to first crossing of $M$ at the actual stage starts, shortening its last segment at this crossing. Each segment is a prefix of length at most $k_j$. The third test and $\sum_{j<J}\sqrt{k_j}\ll\sqrt d$ give the odd-count estimate in (3). The second test gives odd-count control on every length-$b$ window ending no later than $h$, including windows that cross a stage boundary.

The short windows improve the *additive* uncertainty at the gate. Write $v_j=T^jz$. Any full $b$-step block ending no later than first crossing satisfies
\[
 \frac{v_{j+b}}{v_j}
 \le 2^{-b}3^{(1/2+1/40)b}(1+1/(3M))^b\le\theta^b
\]
for fixed $\theta<1$ and large $d$. Group $j<h$ by their residue modulo $b$. The last pre-entry value of each nonempty progression is at least $M$. Going backwards along that progression and summing gives
\[
 \sum_{j<h}1/v_j \le \frac{b}{M(1-\theta^b)}.
\]
The exact correction product gives $\log(y/(3^{p_h}2^{-h}z))\le\sum_{j<h}1/(3v_j)$. Since $y<M$ and $1-\exp(-x)\le x$ for $x\ge0$, the additive error at the gate is $O(b)$. This is an estimate *at first passage*, not an $O(b)$ bound on all prefix offsets. A shortcut reduces by at most two, so $y\ge M/2$.

## One landing interval at each absolute clock

Apply (3) simultaneously via (2), choosing $L>A+C_1+2$. Fix any retained parent and query-window site. Set $r=t+h$, $m'=k+p_h(z)$. Since $3^{p_h}2^{-h}\le y/z\le M/z$, the initial perturbation $i3^e+\epsilon$ contributes $o(1)$ at the gate. Uniformly,
\[
 |y-3^{m'}2^{-r}n|\le C_A\log d,\qquad
 m'=r/2+O_A(W),\qquad
 r=(d-\log_2M)/a+O_A(W).                                                 \tag{4}
\]
The last equality uses $\log_2 n=d+O(1)$ and $M/2\le y<M$. Across the *entire row* only $O_A(W)$ integer absolute clocks occur.

For fixed $y,r$, at most one integer $m'$ meets (4) across this row. The ratio of the largest parent to the smallest is $8/7+o(1)$, relative gate error is $O_A(\log d/M)$, and successive grades differ by a factor three. Hence the possible parents lie in one interval of length $O_A(N\log d/M)$. Sum over the $O_A(W)$ clocks and $y\in G$. The additive one per interval is absorbed since $M\ll N$. This proves (1) independently of any source-population lower bound.

There is also a simultaneous description per actual **exterior cell**. Choose one representative parent $n_0$ of an occupied coarse quotient. The coordinate $m=\lfloor c_0n\rfloor$ gives relative spread $O((2^{H_0}+1)/(c_0N))=2^{-\Omega(d)}$ for its parents, where $H_0$ is the exterior bit cutoff of the pinned schedule. Thus replacing $n$ by $n_0$ in (4) costs $o(1)$. At fixed $r$ the centers $3^{m'}2^{-r}n_0$ lie in $[M/2-C\log d,M+C\log d]$, an interval of ratio less than three. Only one grade fits. Over the entire cell all retained gates belong to $O(W)$ intervals of length $O(\log d)$. This describes joint support and does not assert that the exceptional probability inside each cell is small.

Distinct realized absolute clocks even have **separated** gate intervals for sufficiently large $B$. Their center logs differ by $(m'_1-m'_2)\log3-(r_1-r_2)\log2$, with both coefficients $O(W)$ since the centers are comparable. Multiplicative independence and the fixed two-logarithm lower bound give absolute value $\gg(2+W)^{-\nu}$ for an absolute $\nu$. The ordinary center separation $\gg M(2+W)^{-\nu}$ exceeds $10C_A\log d$ after enlarging $B$. A realized gate and its exterior therefore determine its absolute clock. The fixed-logarithm estimate is needed only for this decoding refinement. [Simons and de Weger, §5, Lemma 12 and the referenced Rhin bound](https://doi.org/10.4064/aa117-1-3)

## All earlier first passages on one sample

Fix $0<\beta<0.34$. The retained original parents and all their sites work **simultaneously for every real floor** $M\le Y\le 2^{\beta d}$. Write $h_Y$ for the first entrance below $Y$. The site starts above $Y$ and $h_Y\le h$. The stopped-prefix decomposition and the third binary test give $|p_{h_Y}-h_Y/2|=O_A(W)$ for every such prefix; the same argument shortens the stage containing $h_Y$. Every full $b$-block before that first crossing already passed the second test. The reverse reciprocal sum, now relative to $Y$, bounds the additive uncertainty by $O_A(b)$ again. Finally, the initial window displacement at the new gate is $O((Y/z)2^{O(W)})=o(1)$ uniformly. No union over floors is involved.

For a specified ordinary integer $g$ reached as any one of these gates, the allowable absolute clocks satisfy
\[
 r=(d-\log_2 g)/a+O_A(W).
\]
This interval is centered using $g$ itself. Hence a prescribed set $\mathcal G$ across all these heights has original incidence at most
\[
 O_A(d^{-A})+O_A\!\left(W\log d\sum_{g\in\mathcal G}1/g\right).          \tag{7}
\]
Indeed a fixed $g,r$ again permits at most one effective grade, and costs $O_A(N\log d/g+1)$ parents. Every reachable $g$ is at most $2^{\beta d}\ll N$, so the endpoint term is absorbed. A direct union over separately proved exceptional bounds for all integer floors would lose this simultaneous statement.

## Opposite replies after the change of scale

Assume the source-qualified PR197 genuine-disagreement and resampling hypotheses at rows with fraction $w\gg d^{-3}$. Each resampling witness has both true colors at sites in the same query window. Choose $A>3$, discard the absolute exceptional parents above, and keep these windows. The two ordinary site paths retain their colors at first gates $g,g'$. They give **actual** opposite-color gates satisfying
\[
 g,g'\in[M/2,M),\qquad |g'-3^s2^{-l}g|\le C_A\log d,\qquad
 l=r'-r=O_A(W),\qquad 3^s2^{-l}\in[1/2-o(1),2+o(1)].                   \tag{5}
\]
Divide the two leading terms of (4) for the same parent. For given $l$ there are at most two possible integers $s$; both $l$ and $s$ may be signed. If $l=0$, the grades coincide and $|g'-g|=O_A(\log d)$. The source hypotheses do not require both colors at the same absolute clock.

Let $G$ be the bad gates appearing in actual witness pairs in (5). Applying (1) to this set and interchanging the colors gives on the supplied rows
\[
 |G|\gg \frac{M}{d^3W\log d}
 \gg_\varepsilon M^{\,1-(3.5+\varepsilon)/B}                             \tag{6}
\]
for either color and every fixed $\varepsilon>0$. Increasing $B$ changes the gate shell. The stronger exponent for truly discordant parents appears below in the head-regeneration proof. The extra restriction relative to the two-arm landing statistic is the near-dilation certificate from the same queried window. The conditional lower uses PR197's separately source-qualified fixed-target positive-density and merger/regeneration inputs. The classical Krasikov–Lagarias $X^{0.84}$ inverse count alone does not yield this lower for actual opposite-query pairs.

The *same* two actual query sites have opposite-color first gates at every floor from the preceding section. In particular take disjoint half-open gate shells $[Y/2,Y)$ for $Y=2^jM\le 2^{\beta d}$. There are $\asymp_\beta d$ shells. At each floor let $G_Y$ be the first gates of one specified color actually occurring in (5) there. The proof of (6) gives $|G_Y|/Y\gg w/(W\log d)$ uniformly, since the exceptional set and constants were shared. Thus the retained near-dilation witnesses of that color across the union have harmonic mass
\[
 \sum_Y\sum_{g\in G_Y}\frac1g \gg_\beta \frac{w\,d}{W\log d}.             \tag{8}
\]
This gains a factor $d/(W\log d)$ relative to the original fraction when summing across the whole logarithmic height range. Its output is a family of near-dilation pairs at varying lags. The next section constructs an actual four-trit head using the intervening clocks and the exact base-81 boundary.

For any fixed $\delta>0$, a bank with $|G|\ll M^{1-\delta}$ has incidence $O(d^{-A}+d^{-B\delta}W\log d)$. Choose $B\delta>4$ to make it $o(d^{-3})$. In particular the PR201 logarithmic-depth thin bands with row index $b_0=O(\log M)$, depth $k=O(\log b_0)$, a gate menu polynomial in $b_0$, and $0\le S\le2b_0$ cover only $(\log M)^{O(1)}$ integers in the gate shell. There are polynomially many centers, each of width at most $2^{8k}$. This includes its large-row construction at each fixed gate $a_0$ when its band meets the shell, since $S\gg_{a_0}b_0$ there. Such a bank cannot account for the selected mass. This conclusion concerns incidence at the polynomial first-entrance floor; the PR201 amplification in its own bands stands.

## Regeneration of a literal four-trit head in the smaller shell

The near-dilation in (5) can in fact be converted back to **actual** head edges. Fix an open mantissa interval $J\subset(7,8)$. Write $\mathcal H_J$ for ordinary children $z$ with $z/81^m\in J$ for some $m\ge0$ and $f(z)\ne f(\lfloor z/81\rfloor)$. Here $f$ is a fixed shortcut-invariant binary color. On the source-qualified genuinely discordant population, the original-row estimate sharpens. For each $A>3$ there are fixed $D,C>0$, with the floor exponent $B$ taken large enough after $D$, such that at **each** $M\le Y\le 2^{\beta d}$,
\[
 w \ \ll_A\ d^{-A}+
 \frac{(\log d)^{3/2}}{Y}\,
 \#\{z\in\mathcal H_J:cY/d^D\le z\le CY\}.                               \tag{9}
\]
Here $w$ is the relative mass of the true-disagreement parents with a witnessed opposite-color query window, up to PR197's stated source losses. The constants may depend on $J$. For $Y=M=d^{B}+O(1)$ this regenerates a true head at **logarithmic heights of order $\log d$**, below the $\sqrt{d\log d}$ lower range of PR197's HEAD_INCIDENCE recurrence. On the cofinal rows with the assumed $w\gg d^{-3}$ it forces some such smaller head row to have disagreement fraction $\gg w/(\log d)^{3/2}$ (over all suffixes). Indeed the total sizes of the smaller base-81 head rows through $CY$ sum to $O(Y)$.

**Saving on truly discordant parents.** The finite native pair-merger bound at PR146, GROWING_ADDITIVE_GAPS.md, controls failure of fusion for $(n,81n+u)$ on complete native binary grids of depth $m$, by $O(m^{-1/2})$ uniformly in the bounded suffix. Every genuinely discordant parent fails this physical fusion. The parent interval in (4) at a fixed gate and absolute clock can be enlarged to length comparable to $N\log d/Y$, which is exponential in $d$ uniformly up to $Y\le 2^{\beta d}$. Tile with complete binary grids of depth $\lfloor(1-\beta)d/2\rfloor$. The boundary term is exponentially smaller than the interval length. Applying the failure bound *on this deterministic interval*, before selecting its parents, saves a factor $\sqrt d$. Union over clocks gives the cost $O_A((\log d)^{3/2}/Y)$ per specified ordinate at height comparable to $Y$. This also sharpens (6) to $|G|\gg M/[d^3(\log d)^{3/2}]$ and thus $|G|\gg_\varepsilon M^{1-(3+\varepsilon)/B}$ for the selected, paired gates of each color. The extra saving requires true original discordance and the pinned PR146 estimate; (1) includes ordinary parents without it.

**From a long clock difference to adjacent ordinary integers.** Fix the two actual opposite-color sites and their gates at this chosen $Y$. For every integer absolute clock $r$ between their gate clocks take the unique integer $p_r$ with
\[
                   V_r=3^{p_r}2^{-r}n\in[2Y/5,6Y/5).
\]
At the two ends these are the actual leading gate terms of (4), because $[Y/2-C\log d,Y+C\log d]$ lies strictly inside this normalization. Let $x_r=\lfloor V_r\rfloor$. If a gate color differs from its own $x_r$ color, there is an adjacent split within $C\log d+1$ of $V_r$. Otherwise the endpoints of the sequence $x_r$ have opposite colors, and there is a split between two successive terms. This argument also handles identical absolute clocks: in that case the true gates themselves yield a nearby adjacent split.

The normalization gives $V_{r+1}/V_r\in\{1/2,3/2\}$. In the first case $2x_{r+1}\in\{x_r-1,x_r\}$, so doubling invariance gives an adjacent split. In the second case $2x_{r+1}$ is within two of $3x_r$. If all adjacent comparisons in the fixed neighborhoods of $x_r$ and $3x_r$ agree, then $f(x_r)=f(3x_r)$. To verify this, replace $x_r$ by the odd member $v$ of $\{x_r,x_r+1\}$, use $f(v)=f(3v+1)$, and note that $3v+1$ is within four of $3x_r$. Doubling now implies $f(x_{r+1})=f(x_r)$, a contradiction. Thus some adjacent split lies within $C\log d+5$ of either $V_r$ or $3V_r$. Every possible such witness has the same phase form (4). The absolute-clock census already includes *all* the intervening $r$; telescoping incurs no additional $|r_1-r_2|$ loss.

**Putting a genuine adjacent split inside $J$.** The irrational rotation by $\log_{81}2$ has dense forward orbit. Compactness of the circle gives a fixed finite $v_0=v_0(J)$ such that one of $2^v$, $0\le v\le v_0$, takes the lower integer of the split to the interior of $81^mJ$ with a fixed mantissa margin. For example choose an open subarc whose closure lies inside $\log_{81}J$; its backward translates cover the circle, so finitely many suffice. Doubling preserves the two colors. The interval between the two multiplied integers has bounded length and contains an adjacent opposite pair $X-1,X$ with the same interior margin for all large $Y$. In particular, for some effective grade $p$ and clock $r'=r-v$,
\[
 X\asymp_J Y,\qquad |X-3^p2^{-r'}n|\le C_{A,J}\log d,\qquad
 r'=(d-\log_2Y)/a+O_{A,J}(W).                                           \tag{10}
\]

**Taking base-81 parents.** If neither endpoint supplies a true head edge, its two parents must still have opposite colors. For neighbors they are equal unless $81\mid X$, in which case the parents are $X/81-1,X/81$. Iterate. Persistence for $q$ generations requires $81^q\mid X$, with split exactly $X/81^q-1,X/81^q$. At the first successful generation the true child is $z=X/81^q-\delta$ for $\delta\in\{0,1\}$. So $81^q(z+\delta)=X$ **exactly**, also for $q=0$.

To keep the child in a large, resolved mantissa cell, discard the event that *any* such $X$ is divisible by $81^{q_0}$ with $q_0=\lceil D\log_{81}d\rceil$. There are $O_J(Y/81^{q_0}+1)$ multiples at the height in (10). For each, (10) and the same ordinary-interval native failure estimate cost at most $O_{A,J}((\log d)^{3/2}/Y)$ of the original parents, already summed over clocks. The total is $O_A(d^{-A-2})$ by taking $D>A+4$ and $B>D+3$. This also permits simultaneous exclusion at the $O(d)$ dyadic floors below. The successful child is then at least $c_JY/d^D$. Dividing $X$ by $81^q$ preserves its mantissa, and moving by at most one retains the fixed $J$ margin at these heights.

For a fixed candidate true child $z$ and floor $Y$, only $O_J(1)$ exponents $q$ satisfy $81^q(z+\delta)\asymp_J Y$, however many generations the individual parent descended. Apply (10) to these **exact integers $X$**. At a fixed $X,r'$ there is at most one grade $p$ on the original narrow row, and its parent interval has cost $O_A(\log d/(Y\sqrt d))$ using true native nonfusion. Summing over the $O_A(W)$ absolute clocks proves (9). This counts an original parent even if the same deeper head serves many paths; its upper bound has denominator $Y$, not the smaller height $z$.

Taking $Y=2^jM\le 2^{\beta d}$ gives $\asymp_\beta d$ shells on the same scalar good set. When summing (9), a fixed child contributes at most $C\sum_{Y\ge c z}1/Y\ll_J1/z$ over dyadic $Y$, even if it serves multiple floors. Thus its harmonic contribution is counted with bounded total weight and
\[
 \sum_{\substack{z\in\mathcal H_J\\ cM/d^D\le z\le C2^{\beta d}}}
 \frac1z\ \gg_{A,J,\beta}\ \frac{w d}{(\log d)^{3/2}}                   \tag{11}
\]
when $w\gg d^{-3}$. At macroscopic logarithmic heights the older HEAD_INCIDENCE estimate has a better logarithmic factor. The new feature here is the same-parent regeneration down to **every polynomial floor** with the exact ancestor carry retained.

**What fails in the iteration.** Inequality (9) is an actual smaller-head recurrence, but the cost $(\log d)^{3/2}$ grows. It has an additive exceptional term and its output row can depend on the input. At a polynomial floor the returned logarithmic height is $d'=\Theta(\log d)$. From input mass only $w\asymp d^{-3}$, the guaranteed smaller-row mass can be exponentially small in $d'$. It falls below the polynomial-in-$d'$ population required to invoke the same PR197 many-site resampling estimate again. For example a model sequence $a_l=(1+l)^{-1/2}$ is consistent with this scale loss: moving from $d$ to $\asymp\log d$ allows a *larger* discrepancy. This is a comparison profile, not an invariant-color construction. A contraction sufficient to control the full harmonic sum of true disagreements, or another way to prove that the regenerated true edges are absent, remains open.

## Literature, frozen inputs and formal scope

* PR197 at 10d87fee615d1095990d6b7ea329126b4cf7aa5a, under research/ayh-resource-reset-20261124: directed-return/SELECTED_TRIT_CELLS.md (blob daae5a5ae1146ef51c20e539a32b7e2cf0ff6b02), closing-proposal/LOCAL_RESAMPLING.md (e75869e2591a0f287307c5b6a1e0546fdef0f066), source-progress/GRID_TRANSFER.md (4bd4457da84728314719e99adcc3a6fedf98bcff), unit-exit/LOCAL_COLOR_INFORMATION.md (8184c096d63c6b41e462abb91a713be61de6cab4), and literature-step/FIRST_PASSAGE_MARKS.md (682273eaae27190bab78603c0dee9449e1a6f3e4). The first four provide coordinates, physical eligibility and separately qualified source lower bounds. The last supplies the stopped-source architecture extended above.
* PR146 at f431078244e868dc699fad011044f0d5e7f76437, research/upper-bit-mergers/GROWING_ADDITIVE_GAPS.md, supplies the source-qualified complete-grid merger estimate for the true-parent refinement (9). PR197 at the above head, two-class-descent/HEAD_INCIDENCE.md, gives the earlier logarithmic-height comparison.
* PR201 at 02fb390a76fb2ffb00fee612649ca23a82d99d31, research/killed-green-head-closure-20261124/thin-band/README.md, §§2–3 for the polynomial band comparison. PR193 at aa0b01234735683b413098b81afdf764de503730, research/astra-closure-20261125/global/README.md, gives a Fourier–Stieltjes test for the full ordinary coloring. A scalar gate census does not bound the total variation in that test.
* Tao's Proposition 1.17 estimates a primitive Fourier character of the Syracuse offset modulo $3^n$ under its specified random valuation law. Its $O_A(n^{-A})$ bound cannot simply be conditioned on two actual colors or on an original interval of short native precision. [Tao, Forum of Mathematics, Pi 10 (2022), e12](https://doi.org/10.1017/fmp.2022.8)
* Inselmann's Theorems 3.1 and 3.3 give scalar height and parity-count estimates for a whole interval of times with a power-small set of ordinary exceptions and a fixed tolerance proportional to $\log n$. Shaik's Corollary 1.2 gives a specified polylogarithmic hitting height, two-sided clock and orbit bounds, with a logarithmic-power exceptional rate. Neither statement was substituted for the sliding first-passage estimate (3). [Inselmann, arXiv:2402.03276v3](https://arxiv.org/html/2402.03276v3) · [Shaik, manuscript v4.0.2, Corollary 1.2](https://shaikidris.github.io/polylog/paper/)
* [OriginalWindow.lean](OriginalWindow.lean) formalizes the affine source-fibre diameter and cardinality, finite union bound, one-grade rigidity, and both directions of finite meeting transport between sites and their actual gates with an additive horizon allowance. The module also proves the physical inequality $2^h T^h(x)\le 3^{p_h}x+b2^h$ at a positive record landing, assuming $2\cdot3^{p_b}\le2^b$ on each contained block. For the checked exponent envelope this holds for all sufficiently large $b$. The local tripling-to-adjacency implication and one-generation exact base-81 boundary dichotomy are also kernel-checked. Equations (1)–(11), the exterior separation and the source-qualified lower are written mathematics. [Execution record](../../../reports/astra-literature-closure-20261125/source/README.md)
