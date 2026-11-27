# Arithmetic deflation and record-phase separation for ordinary gate mass

**Status.** Proposed arithmetic consequences of [the finite-gate theorem](EXIT_GATES.md) and [the finite-alphabet rigidity of record phases](../renewal/RATIONAL_DIAGONAL.md). The physical flux is power-small outside an explicit thin set at every cutoff. In any escaping component, some heavy gates avoid the entire rational diagonal in the joint local limit. These are restrictions on the remaining possible mass.

## OP-G3. Universal thin sieve at every numerical threshold

Let $\alpha=\log_2 3$, $b=1/\alpha$, $\theta=H_2(b)$ with binary entropy in base 2, and $\delta=1-\log_2(3/2)=2-\alpha>0$. Given integer $X\ge2$, put $k=\lfloor\log_2 X\rfloor$. Construct a finite set $E_X$ in the actual gate shell $[X,(3X-2)/2]$ as follows. Read a possible native binary word of length $k$ **backwards from the gate**, and let $q_j$ count its odd letters through the first $j$ reversed positions. Retain only words satisfying $3^{q_j}/2^j\ge1/2$ at every $0\le j\le k$. For each such word let $q=q_k$ and $A=A(w)$ be the integer carry of its **forward** reading, so the rank-$k$ identity is $2^k y=3^q u+A$. Insert every shell integer in $2^ky\equiv A\bmod 3^q$ into $E_X$. Restrictions $y\equiv2\bmod3$ and actual inverse legality can also be imposed, but are unnecessary for the estimates.

There are constants independent of $X$ such that
$$
 |E_X|\ll \frac{X^\theta}{(\log (2X))^{3/2}},
 \qquad
 \sum_{y\notin E_X}J_{s,X}(y)\ll_s X^{-\delta(s-1)}\quad(s>1).
$$
In particular every gate of mass above any prescribed positive $\varepsilon$ belongs to the explicit sieve for all sufficiently large $X$. The excluded sites number a proportion tending to one of all actual charged gates.

Indeed the real affine carry over any $j$ steps is at most $(3/2)^j-1$, by domination by all odd operations. Suppose an exit from below occurs at $y$ after at least $k$ steps. For its last $j\le k$ steps from $u<y$ the slope satisfies
$$
 3^{q_j}/2^j\ge (y-(3/2)^j+1)/y\ge 1-X^{-\delta}.
$$
For $X$ large this exceeds $1/2$. The integer identity then enforces its terminal residue, so $y\in E_X$. A source $x$ exiting in fewer than $k$ steps satisfies $y+1\le(3/2)^k(x+1)$, hence $x+1\ge X^\delta$. The combined mass of these sources is at most $\sum_{x+1\ge X^\delta}x^{-s}\ll_s X^{-\delta(s-1)}$. Small cutoffs are absorbed in the constants.

For the counting estimate, write $Z_j=\alpha q_j-j$ and use independent Bernoulli-$b$ bits only to count the possible words. The sieve floor is $Z_j\ge-1$. A specific rank-$k$ word has probability
$$
 2^{-\theta k}\exp(a Z_k),\qquad
 a=\alpha^{-1}\log\!\left(\frac b{1-b}\right)>0.
$$
The centered bounded walk estimate O4 gives
$\mathbb E[\exp(-aZ_k)\mathbf1_{\min_{j\le k} Z_j\ge-1}]\ll k^{-3/2}$.
Equivalently there are $O(2^{\theta k}k^{-3/2})$ retained words. To recall its elementary proof, first-third survival above $-1$ costs $O(k^{-1/2})$ by the bounded-overshoot stopping estimate. In a terminal unit bin $v\le Z_k<v+1$ the reversed last third stays below $v+2$, costing $O((v+3)k^{-1/2})$. Conditional on those two independent pieces, the middle binomial block costs $O(k^{-1/2})$ by Stirling. Sum the bins with the exponential terminal weight. Finally $3^q\ge2^{k-1}\ge X/4$, so each retained residue has $O(1)$ representatives in the shell. This proves the cardinality estimate. The centered-walk counting input also occurs in Weaver's Paper 28/v3; the arithmetic conclusion here concerns the union of possible target labels of **all** long exits and the discarded physical mass. [Independent elementary estimate O3–O4](../renewal/OCCUPATION.md) · [Weaver, Paper 28/v3](https://rstation.ai/problems/collatz/papers/28)

For dyadic $X=2^j$ the union of these explicit candidates has finite critical Mellin mass $\sum_{j\ge1}\sum_{y\in E_{2^j}}y^{-\theta}<\infty$. Despite this summability every escaping component would deposit its full limiting charge on a candidate at all sufficiently large dyadic cutoffs.

## OP-G4. Each escaping atom has an off-diagonal pre-gate limit

On a single ordinary escaping component $D$, choose any forward ray. Let $p_i$ be its successive strict maxima among **odd** vertices, after the initial possible even run. Beyond a fixed initial height the strict native numerical maxima on this ray are precisely $y_i=(3p_i+1)/2$. Indeed the first native successor of each odd $p$ is the largest value before its ensuing even divisions, and $p\mapsto (3p+1)/2$ strictly preserves numerical order. An odd input itself is below its immediate successor. There are cofinally many such maxima. At the specific integer cutoff $X=y_i$, the ray has first exit exactly $y_i$. OP-G2 gives
$$
                             J_{s,y_i}(y_i)\longrightarrow Z_D(s)>0 .
$$
Using a different representative of $D$ changes only finitely many record gates. This assertion uses $\ell^1$ comparison with the moving distinct atoms in OP-G2 and coalescence beyond the finitely many pre-meeting heights.

For the cluster sets of the pre-gates $p_i$ in $\mathbb Z_2^\times$, $\mathbb Z_3$ and their joint product, the three conclusions D1–D3 of the [coefficient-record theorem](../renewal/RATIONAL_DIAGONAL.md) persist:
    
* The dyadic cluster set is not contained in periodic phases that each admit a finite coefficient upcrossing. In particular it is not entirely negative periodic.
* If odd gaps between successive strict odd-height records stay bounded, the ternary cluster set contains a point outside $\mathbb Q\cap\mathbb Z_2^\times\cap\mathbb Z_3$.
* At least one joint cluster pair is outside $\{(r,r):r\in\mathbb Q\cap\mathbb Z_2^\times\cap\mathbb Z_3\}$ without any gap assumption.

Here are the changes needed for numerical records. In an odd segment of length $j$ with native clock $S$ ending at a record $p$, all its earlier odds $x_h$ are smaller than $p$. If $u$ is its first odd, the exact relation is
$$
 \frac{2^S}{3^j}=\frac{u}{p}\prod_{h<j}\left(1+\frac1{3x_h}\right)
                 \le (4/3)^j .
$$
Thus $S\le 2j$. For each fixed $j$ along an escaping ray the finitely many last $x_h$ tend to infinity, so the right side before the final inequality is at most $1+o(1)$. The finitely many possible integer clocks and $2^S\ne3^j$ for $j>0$ imply the eventual strict critical inequality $2^S/3^j<1$. Every ternary cluster point of record $p$ therefore carries an infinite backwards critical odd code, by finite-branch diagonal extraction and the exact inverse congruences.

Next, if odd record gaps are unbounded, take starting records of gaps tending to infinity and pass to a dyadic cluster phase. A fixed finite coefficient upcrossing there persists on a finite cylinder including the terminal odd bit. From any positive ordinary starting record in this cylinder the strictly superunit coefficient and nonnegative carry produce a strictly larger odd height, contradicting the growing gap. If odd gaps are bounded by $J$, the preceding inequality applied to each whole inter-record segment gives a bound $2J$ on its native clock.

These facts are exactly the two substitutes needed in the finite-alphabet argument. Under the proposed dyadic confinement, every two-sided native omega center has a preceding record within a bounded offset, hence its right tail is purely periodic. The compact one-sided tail subshift then has a continuous unique predecessor, finite memory, and a factor graph consisting of cycles. The original parity word is eventually periodic, impossible on a simple ordinary ray. For the second claim a bounded offset to a later record gives a purely periodic **left** tail under the proposed ternary rational confinement, because every backwards critical code of an odd-numerator, odd-denominator rational is purely periodic on a negative signed cycle by PR210 R1. The same subshift argument in reverse applies. Finally, projection of the joint cluster set onto the dyadic coordinate is onto. If it contained only the rational diagonal, R1 would put every dyadic phase on a negative periodic cycle, contradicting the first claim. [Rational classification and purity, PR210 §4](https://github.com/GettysburgResearch/collatz/blob/592328fecf8ea2cf41736294856d95f890a1ba98/research/critical-record-rational-rigidity-20261125/README.md)

Consequently, to exclude escape it would suffice to prove that for each $\varepsilon>0$ every joint subsequential limit of $(p,p)$ from physical gates $y=(3p+1)/2$ with $X\to\infty$ and $J_{s,X}(y)\ge\varepsilon$ lies on the rational diagonal. Necessity in the zero-escape case is vacuous by OP-G2. The arithmetic sieve proves neither rational confinement nor a common uniform decay on its surviving labels. Coordinatewise rationality alone would still allow unequal local values.

## Exact one-height bookkeeping

For an optional scalar replay define $R(n)$ to be the first state above $n$ on its own orbit, or $\bot$ if it never exits. Both alternatives are decidable after at most $n$ steps. Put $H_s(n)=n^{-s}+J_{s,n}(n)$, interpreting $J_{s,1}=0$, and let $r_s(n)=0$ at a sink, otherwise the retention along the path from $n$ to $R(n)$. In the step from cutoff $n$ to $n+1$ every previously charged gate other than $n$ is already at or above the new cutoff. Therefore the entire loss of augmented mass is exactly
$$
 A_s(n)-A_s(n+1)=(1-r_s(n))H_s(n)\quad(n\ge1),\qquad A_s(1)=\zeta(s).
$$
Summing this positive series gives $\sum_{n\ge1}(1-r_s(n))H_s(n)=\zeta(s)-\sum_D Z_D(s)$. All strict increase arrows have $n<R(n)\le(3n+1)/2$ and $R(n)=2\bmod3$. Along a genuine escaping record chain the product of retentions is strictly positive by the reciprocal estimate, so summability of small local losses alone is compatible with survival of the atom.
