# Ordinary early windows avoid every future state of power-sized sources

Let $U$ be the accelerated positive odd map. Write $\mathcal R(v)=\{U^h v:h\ge0\}$ for the set of distinct odd states visited from the positive odd source $v$. Fix $0<\alpha<1/2$ and set
$$
 b_\alpha=1-(2-\log_2 3)\alpha .
$$
For each fixed $0<\epsilon<b_\alpha/40$ there is $c=c(\alpha,\epsilon)>0$ such that a uniformly sampled odd $n\in[2^k,2^{k+1})$ satisfies
$$
 \Pr\bigl(\exists 0\le j\le\alpha\log_2 n,\quad
        \exists\,v\le n^\epsilon\ \mathrm{odd},\quad\exists h\ge0:
                       U^j n=U^h v\bigr)=O_{\alpha,\epsilon}(e^{-ck}).  \tag{1}
$$
The visitor horizon is unrestricted. The tested dates and every competing visitor are actual ordinary integer paths. The same bound holds for any predetermined family of $O(2^{\epsilon k})$ positive odd starting integers per octave, with no size restriction on its members. The implied constant may depend on that family-size bound.

The sum of $1/n$ over all sources admitting the small visitor in (1) is therefore finite. Under any macroscopic source law $F_X(x)\le1/x$ of total weight at least $\delta\ln X$ with odd core $n$, the chance that this occurs is $O_{\alpha,\epsilon,\delta}(1/\ln X)$. The all-height statistic on this same protected early window still converges in probability to $(\ln2)^{-2}$ under ordinary octaves and under those gate laws, by the all-height theorem. For any prescribed ordinary ray, the chance that an early window visits even one of its states has the same summable estimate, regardless of the ray's future. An almost-sure statement for all starts is not asserted.

## Source-qualified inputs

The elementary ordinary path packing estimate gives an absolute $C$ such that
$$
 \sum_{y\in\mathcal R(v),\ y>H}\frac1y\le C H^{-1/40}
\quad (H\ge1)
$$
uniformly in every positive odd $v$. Truncate an injective path or retain the segment before a first repetition in the periodic case. The positive full trajectory may revisit a cycle, but its set of states needs only one traversal. The other input is the original geometric ternary density $\rho_j=3^j p_j$, with uniform normalized $L^p$ bound for a fixed $1<p<2$ on $\mathbb Z/3^j\mathbb Z$. Both inputs refer to the genuine ordinary map and its original finite geometric word law. The density estimate is an external theorem and was not reproved here. [Resident simple-path packing and its hypotheses](https://github.com/GettysburgResearch/collatz/blob/bf7d52e78631954a9fd35e4ce973acd27738fc80/research/unconventional-20261126/trace/ANNULAR_ESCAPE_CURRENT.md) · [Weaver, Paper 9, original finite density regularity](https://rstation.ai/problems/collatz/papers/9)

## Physical height and period

Put $J=\lfloor\alpha(k+1)\rfloor$, and choose $\eta>0$ sufficiently small that $2\alpha+2\eta<1$ and $40\epsilon<b_\alpha-2\eta$. Except on probability $O(e^{-c_\eta k})$, for all $j\le J$ one has
$$
 E_j\le2j+\eta k,\qquad E_J\le(1-\eta)k
$$
for all sufficiently large $k$. To see this, the test $E_J\le\lfloor(1-\eta)k\rfloor$ is available in the initial finite parity bits and has a geometric negative-binomial exponential tail. On that event the complete retained word masses are exactly $2^{-E_J}$. Under the independent geometric law one obtains the first assertion by a Chernoff estimate and a union bound over $j$. At every actual date on this event, $y_j=U^jn$ has the bounds
$$
 y_j\ge3^j2^{k-E_j}\ge 3^j2^{\eta k},\qquad
 y_j\ge 2^{(b_\alpha-2\eta)k},\qquad
 y_j+1\le(3/2)^j(n+1).
$$
The second follows from $k+j\log_2 3-2j-\eta k$, absorbing the $O(1)$ from $J$. In particular there are $O_\alpha(k)$ possible dyadic terminal height bands. Every band $[Y,2Y)$ meeting the good range has $Y\ge3^j$ for large $k$ and $Y\ge2^{(b_\alpha-2\eta)k}/2$. The entire corrected survival $f_j(n)=\prod_{i<j}3y_i/(3y_i+1)$ is at least $1/2$ for all these dates and large $k$, since every factor has loss at most $2^{-(b_\alpha-2\eta)k}$.

Fix the competing source family $\mathcal V_k$ of size $O(2^{\epsilon k})$ and its union of forward states $A$. The packing estimate implies
$$
 \frac{|A\cap[Y,2Y)|}{Y}\ll 2^{\epsilon k}Y^{-1/40}.
$$
One can apply the tail estimate at $H=Y/2$ to include a possible endpoint. On any such band, physical harmonic transport and Hölder give
$$
 \sum_{\substack{n\in[2^k,2^{k+1}),\ n\ {\rm odd},\ n\ {\rm good}\\
             U^jn\in A\cap[Y,2Y)}}\frac1n
 \le 2\sum_{y\in A\cap[Y,2Y)}\frac{\rho_j(y)}y
 \ll_p \left(\frac{|A\cap[Y,2Y)|}{Y}\right)^{1-1/p}.               \tag{2}
$$
For the first inequality sum the exact word weights $f_j(n)/n=3^j2^{-E_j(n)}/y$ over the positive ancestors of each fixed endpoint $y$. Each compatible word contributes at most once. For the second inequality, periodicity and the normalized $L^p$ bound give $\sum_{Y\le y<2Y}\rho_j(y)^p\ll_p Y$ since $Y\ge3^j$. The physical height being above its current ternary period is essential for this step.

The right side of (2) is exponentially small in $k$ by the choice of $\eta$. Summing over $O(k)$ dates and $O(k)$ bands preserves that conclusion. Harmonic mass on an odd octave and its uniform probability differ by at most absolute factors. To cover all $v\le n^\epsilon$ one may choose every odd $v< 2^{\epsilon(k+1)}$. For the macroscopic extension the cumulative weight on a bad odd core is at most $2/n$, so finite reciprocal mass suffices.

This also protects the intermediate native shortcut states through the last tested odd endpoint, provided the competing starts are below $n$. A meeting at an intermediate state persists to the immediately following odd endpoint, and an initial even chain from a start at most $n^\epsilon$ only decreases to its odd core. The starting odd state itself is already tested. Protection against visitors in the remaining interval $n^\epsilon<v<n$ does not follow.
