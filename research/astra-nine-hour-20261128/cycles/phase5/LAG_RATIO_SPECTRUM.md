# Reduced endpoint ratios determine sparse sets of lags

Let $y_i/q$ be the odd phases of a positive rational cycle of least odd period $u>1$, in physical order $i\in\mathbb Z/u$. Write $3y_i+q=2^{a_i}y_{i+1}$, $n=\sum a_i$, $\gamma=\log_2 3$, and $\delta=n-u\gamma$. Define $Q(\delta)=\min\{t\ge1:\|t\gamma\|_{\mathbb R/\mathbb Z}<\delta\}$. For every proper odd lag $1\le h<u$ and every phase $i$ the reduced ratio $r=y_{i+h}/y_i$ satisfies
$$ h\gamma-\log_2 r\ \bmod1\ \in\ (-\delta,0)\ \bmod1 .                \tag{1}$$
To prove this, put $\epsilon_i=\log_2(1+q/(3y_i))>0$ and sum the exact transitions:
$$ \log_2 r=h\gamma-A_{i,h}+E_{i,h},\quad
 A_{i,h}=\sum_{t=0}^{h-1}a_{i+t},\qquad E_{i,h}=\sum_{t=0}^{h-1}\epsilon_{i+t}\in(0,\delta). $$
The full sum of positive errors is exactly $\delta$. The arc product and critical clock calibration occur in prior work. Here one fixed fraction is tested simultaneously at every lag and origin. The all-origin height estimates for matching budgets and sparse postmismatch event factors in PR214 concern different data. [PR214, 8f6da3ef960a8274891714689778f3a6c0ab22c2, BLOCK_SUM_DEFECTS.md](https://github.com/GettysburgResearch/collatz/blob/8f6da3ef960a8274891714689778f3a6c0ab22c2/research/astra-critical-rigidity-20261128/cycles/BLOCK_SUM_DEFECTS.md)

**All-origin height at density-one lags.** Two distinct lags giving the same $r$ must differ by at least $Q(\delta)$, by subtracting (1) with their errors in that same open interval. Thus each ratio occurs at at most $1+u/Q(\delta)$ distinct lags. At most $H^2$ positive reduced fractions have numerator and denominator at most $H$. Consequently the number of proper lags carrying even one such pair is at most
$$ H^2(1+u/Q(\delta)).                                                \tag{2}$$
For any sequence of distinct positive integer cycles, $u\to\infty$ and $\delta\to0$ by the uniform cycle sparsity estimate. Irrationality gives $Q(\delta)\to\infty$. Put $B=\min(u,Q(\delta))$. For a proportion tending to one of all lags, **all** their endpoint pairs therefore have reduced rational height greater than $\sqrt{B}/\log(2+B)$. The argument permits arbitrary rational cycles satisfying the same clock limits. [Phase three, physical conductor and the sparsity proof](../phase3/PHYSICAL_CONDUCTOR.md)

**Multiplicative relations at best clocks.** Suppose $u$ is a two-sided best clock in the precise sense $\|h\gamma\|\ge\delta$ for every $1\le h<u$ and $0<\delta<1$. Then $Q(\delta)\ge u$. Equal proper endpoint ratios have the same odd lag by (1), and the same integer shortcut time $A_{i,h}$ since their error difference has magnitude below one. If $y_i y_j=y_k y_l$, compare $y_i/y_k=y_l/y_j$. Distinct states on a least cycle have distinct values. A ratio one forces the corresponding indices equal. Otherwise equal lags and equal shortcut times give
$$ i+j=k+l\pmod u,\qquad s_i+s_j=s_k+s_l\pmod n,\qquad s_i=\sum_{t=0}^{i-1}a_t . $$
Thus the map $y_i\mapsto(i,s_i)$ preserves every two-factor multiplicative equality in the two additive clock groups. At a general clock the same argument bounds the number of candidate lag classes by (2); a one-sided record need not be two-sided.

There is a different all-order property at one-sided records. Assume $0<\lceil h\gamma\rceil-h\gamma$ is at least $\delta$ for every $1\le h<u$. For any nonempty proper subset $I$ of the $u$ physical odd edges,
$$                         \prod_{i\in I} y_{i+1}/y_i\ne1.            \tag{3} $$
Indeed unity would give $0<\sum_{i\in I}a_i-|I|\gamma=\sum_{i\in I}\epsilon_i<\delta$. In particular a nontrivial product identity with source and target indices alternating in cyclic order is impossible, regardless of the number of factors: take the union of the disjoint forward arcs from each source to its following target. These are assertions about all endpoint factors of a given cycle. They do not supply a repeated fraction or an alternating relation on an unknown integer cycle.

**A product-only closure loses the orbit.** At $(n,u)=(8,5)$ consider five distinct valid odd transitions
$$25\to19,\quad19\to29,\quad29\to11,\quad43\to65,\quad143\to215.$$
Their shortcut exponents are $2,1,3,1,1$. This is a positive best-from-above clock, and the product of targets equals the product of sources because $25\cdot43\cdot143=11\cdot65\cdot215$. No proper subset balances by the same positive-error proof as (3). Nevertheless the five transitions are disjoint paths with different source and target multisets. Thus even a minimal product relation among distinct actual ordinary transitions need not yield a closed orbit. The broad multiplicative relaxation of the Collatz graph has an extensive literature. [Applegate and Lagarias, *The 3x+1 semigroup*, 2004](https://arxiv.org/abs/math/0411140)

The exact replay compares the ratio inequalities by integer powers, tests every proper edge subset at each one-sided best clock, and verifies the five-edge control. All 3,885 positive primitive necklaces with at least two odd dates through length fifteen passed. [lag_ratio_controls.py](lag_ratio_controls.py)
