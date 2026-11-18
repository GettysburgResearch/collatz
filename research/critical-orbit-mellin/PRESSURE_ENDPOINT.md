# The exact critical inverse-pressure tail

The random variable here is the all-word Green sum. Paper 146 proves an exact quadratic tail for the distinct stationary geometric density and develops related offset and overlap techniques. [Prior-work comparison](PRIOR_WORK.md)

**PROPOSED.** At a Haar ternary target, let $H=\mathcal H_2$ be the sum of $J^2$ over all integral inverse valuation words, including the empty word, where $J=3^q/2^A$. Then
$$
 \lim_{u\to\infty}u\Pr(H>u)=\frac1{2\mu},\qquad
 \mu=\log 3-\tfrac43\log2 .
$$
By [the ordinary first-hit distribution theorem](../fixed-floor-shells/PRESSURE_LAW.md), this specifies the tail of the ordinary limiting law. All target-population limits precede the large-pressure limit. The proof uses the [cross-depth terminal-digit bound and weak first moment](MINIMUM_SHARP.md) and the [supercritical tail constants](MINIMUM_CONSTANT.md).

## Counts in an annulus have controlled clumping

Fix $1<p<2$, and for $R>0$ let $N_R$ count all legal words with $R\le J<2R$. We claim $\mathbb E N_R^p\ll_p R^{-2}$. The empty word poses only a bounded additional term when $1/2<R\le1$.

Use iid tilted letters of law $3\cdot4^{-a}$ and write $S_q=\log J=\sum_{i\le q}\log(3/2^{a_i})$. Their drift is $\mu>0$. For every interval $I$ of width $\log2$, $\sum_{k\ge0}\Pr(S_k\in I)\le C$ uniformly over its location: stop on first entry and bound returns by the summable probabilities $\Pr(S_k\le\log2)$ at subsequent times. For each word denote its scaled numerator $C/3^q$ by $B_0$. Let $K_0$ be one plus the largest suffix length $l\ge1$ with final valuation sum greater than $8l/5$, taking $K_0=1$ when there is none. For every $0<d<1$,
$$
 \sum_{q\ge1}\mathbb E[B_0^d\,{\bf1}_{S_q\in I}]\ll_d1,
 \qquad
 \sum_{q\ge1}\Pr(S_q\in I,\ K_0>k)\ll e^{-ck}\quad(k\ge1).
$$
For the first assertion use $B_0=(1/3)\sum_{l<q}\exp[-(S_q-S_{q-l})]$ and subadditivity of the $d$-power. Condition on the final $l$ letters: summing over the independent complementary prefix length costs at most $C$ by the uniform interval occupation bound. The remaining sum is geometric because $\mathbb E e^{-dS_1}<1$ for $0<d<1$, by strict concavity and $\mathbb E e^{-S_1}=1$. For the second assertion union over bad suffix lengths $l\ge k$, condition on the suffix in the same way, and use the exponential Chernoff upper tail for its valuation sum since the tilted mean is $4/3$.

Group words into bins $B=2^i$, $i\ge0$, for which $\max(1,B_0)\in(B/2,B]$, and $K=K_0\ge1$. Write $N_{R,B,K}$ for the marked count. Each word has legality probability $3^{-q}$ equal to its tilted word probability times $J^{-2}$. With any $p-1<d'<d<1$, the two summation estimates above and the bound by the geometric interpolation of their minimum give
$$
 \mathbb E N_{R,B,K}\ll_{d,d'}R^{-2} B^{-d'} e^{-c'K}.
$$
The small bins $B=1$, $K=1$ use the interval occupation bound without a restriction.

For this one bin we also have
$$
 \mathbb E N_{R,B,K}^2\ll B(1+K)\mathbb E N_{R,B,K}.
$$
Indeed at a fixed depth $q$ the half-open annulus fixes at most one total $A$ and the bound $C\le B3^q$ allows at most $B+1$ words per residue. For $r<q$ write $l=q-r$. On a prescribed depth-$r$ cylinder the eligible longer numerators form a subset of a single progression modulo $3^r$ of at most $B3^l+1$ terms. This bounds the conditional expected longer count by $O(B)$ for all gaps. For $k=\lfloor l/2\rfloor\ge K$, the last $k$ letters must have total at most $8k/5$. As in the [cross-depth proof](MINIMUM_SHARP.md), among residues modulo $2^{1+\lfloor8k/5\rfloor}$ this decoding event has frequency $O(e^{-c''k})$, because low bits of an odd uniform numerator decode independent geometric letters of mean 2. Every residue occurs in the progression at most $O(B3^l/2^{1+\lfloor8k/5\rfloor})$ times. Each numerator determines at most one word and one longer cylinder, so the conditional expected count is $O(Be^{-c'''l})$ at these gaps. Multiply by the shorter count, measurable at level $r$, and sum the bounded and geometric ranges of gaps. All the second-moment bounds hold first for finite depth cutoffs and then by monotone convergence.

Interpolating the first and second moments gives $\mathbb E N_{R,B,K}^p\le[O(B(1+K))]^{p-1}\mathbb E N_{R,B,K}$. Taking the $p$th root and summing by Minkowski over the dyadic $B$ and integer $K$ is convergent since $d'>p-1$. This proves the annular claim, and it holds uniformly even for $R<1$.

## The critical tail has a limit

Let $H_{\le M}$ be the contribution of words with $J\le M$. Partition $(0,M]$ into geometric annuli (a boundary can be included by enlarging the top annulus). Minkowski and the annular estimate yield
$$
 \|H_{\le M}\|_p\ll_p M^{2-2/p}.
$$
In particular $u\Pr(H_{\le\varepsilon\sqrt u}>\delta u)\ll_p\delta^{-p}\varepsilon^{2p-2}$ uniformly in $u$. For $s>2$ put $V_s=\mathcal H_s^{2/s}$. Its established tail satisfies $u\Pr(V_s>u)\to c_s$. Monotonicity of sequence norms gives $V_s\le H$ and $V_s$ increases as $s\downarrow2$, so $c_s$ increases to some $c\in(0,\infty)$ by the weak first-moment bound on $H$.

On $H>u$ with $H_{\le\varepsilon\sqrt u}\le\delta u$, the remaining words have total squared weight greater than $(1-\delta)u$ and each contributes to $\mathcal H_s$ at least $(\varepsilon\sqrt u)^{s-2}$ times its squared weight. Hence $V_s>[\varepsilon^{s-2}(1-\delta)]^{2/s}u$. The upper limit of $u\Pr(H>u)$ is at most $c_s[\varepsilon^{s-2}(1-\delta)]^{-2/s}+O_p(\delta^{-p}\varepsilon^{2p-2})$. Send $s\downarrow2$, then $\varepsilon\downarrow0$, then $\delta\downarrow0$. The lower limit is at least each $c_s$, so $u\Pr(H>u)\to c$.

## Identification by a tilted word

Let $Q_q$ denote the total squared pressure of words at depth $q$. Then $\int Q_q=1$: sampling a tilted $q$-word and then a Haar target conditional on legality gives exactly target density $Q_q$. For each fixed $\eta>0$ restrict to words with $|S_q-\mu q|\le\eta q$ and $B_0\le e^{\eta q}$. The discarded tilted mass is $O_\eta(e^{-c_\eta q})$, by Chernoff and the uniform unconditional fractional moment of $B_0$ proved by the same suffix-product sum. The restricted target density is bounded pointwise by $O((1+q)e^{(2\mu+3\eta)q})$: there are $O_\eta(1+q)$ possible totals, each contributes at most $e^{\eta q}+1$ legal words on a residue by numerator injectivity, and every squared weight is at most $e^{(2\mu+2\eta)q}$. Thus the weak tail $\Pr(H>u)\ll1/u$ implies
$$
 \int_{H>u} Q_q\ll_\eta e^{-c_\eta q}
     +(1+q)e^{(2\mu+3\eta)q}/u .
$$
Summing for $q\le\log(u)/(2\mu+4\eta)$ gives $O_\eta(1)$ for sufficiently large $u$. Therefore $\mathbb E\min(H,u)\ge\int_{H\le u}\sum_{q\le\log(u)/(2\mu+4\eta)} Q_q\ge\log(u)/(2\mu+4\eta)-O_\eta(1)$.

For the reverse bound, words with $J^2>u$ contribute to the clipped pressure at most $u$ times the probability one exists, which is $O(1)$ by FS-010. The remaining expected squared pressure is exactly $\sum_{q\ge0}\Pr(2S_q\le\log u)$ under the tilted law. For $q>\log(u)/(2\mu-\eta)$ its tail probabilities are exponentially small in $q$ by Chernoff, while earlier terms are at most one. Letting $\eta\downarrow0$ gives $\mathbb E\min(H,u)\sim(\log u)/(2\mu)$. Integrating the already established pointwise tail asymptotic yields $c=1/(2\mu)$.

## Subcritical pressures

For $1<s<2$ put $a=2/s\in(1,2)$. Then $\Pr(\mathcal H_s>u)\sim c_su^{-a}$ with $0<c_s<\infty$, so the positive-moment threshold is $a$. Together with the supercritical and critical cases this yields an exact power-law equivalent for every $s>1$.

Choose $a<p<2$. The annular bound and Minkowski give $\|\sum_{J\le M}J^s\|_p\ll_{s,p} M^{s-2/p}$. Take $M=u^{1/s}$, use Markov for this sum and the quadratic maximum-word tail for the rest. This proves the upper bound $O_s(u^{-a})$; the lower bound follows from a single word of weight $J^s>u$.

Write $H_s=\mathcal H_s=1+\sum_i B_i$, where the legal branch terms are as in the [supercritical constant proof](MINIMUM_CONSTANT.md). For $1<r<a$, the tail upper bound gives $\mathbb E H_s^r\ll_s1/(a-r)$ as $r\uparrow a$. Each branch integrated on its legality class gives
$$
 \mathbb E\left[H_s^r-\sum_i B_i^r\right]
  =\left(1-\frac{3^{sr-1}}{2^{sr}-1}\right)\mathbb E H_s^r=O_s(1).
$$
The parenthesis is $O_s(a-r)$ by differentiability at $sa=2$. Convexity makes the random difference nonnegative. Since $\sum B_i<\infty$ almost surely, the sums of powers converge pointwise as $r\uparrow a$ by domination using $B_i+B_i^a$. Fatou gives $\mathbb E[H_s^a-\sum_i B_i^a]<\infty$.

Let $B=\max_i B_i$, or zero if there is no legal branch. Since $(x+b)^a-x^a\ge(2^a-1)b^a$ for $x\ge b\ge0$, adding the nonmaximal branches in any order gives
$$
 H_s^a-\sum_i B_i^a\ \ge\ (2^a-2)\left(\sum_i B_i^a-B^a\right).
$$
Thus both $\sum_i B_i^a-B^a$ and $H_s^a-B^a$ have finite expectation. Splitting the renewal defect about the maximum exactly as in the supercritical case proves absolute integrability. The same nonarithmetic ladder smoothing and monotone unsmoothing give the claimed equivalent, with
$$
 c_s=\frac{\mathbb E[H_s^a-\sum_i B_i^a]}{2\mu}.
$$
The critical case $s=2$ admits the same numerical expression, since its additive toll is 1, but needs the separate endpoint argument above. For $s>2$ the analogous integrable difference is the one established using strict concavity.
