# Every nonzero rotation of a primitive cycle costs disagreements

**Proposed written results.** Use the shortcut map, one division by two at every binary bit. Take a primitive positive rational cycle of least bit period $A$, odd count $p>0$, common reduced denominator $d$, and word $w$ indexed modulo $A$. Positivity gives $D=2^A-3^p>0$. The reduced denominator $d=D/\gcd(D,C_w)$ is the least common denominator of all states and is coprime to six. Indeed the one-lap closure gives this reduced denominator at the initial phase. Each step preserves it since $2,3$ are units modulo $d$ and the new cleared numerator is integral. At $x=n/d$ the next cleared numerator satisfies $2n'=n$ on an even bit and $2n'=3n+d$ on an odd bit. Define $\Lambda=A\log 2-p\log3>0$, $\eta=1-3^p/2^A$. For each $0<r<A$, let $t=t(r)=\#\{i:w_i\ne w_{i+r}\}$. It is positive and even. No coprimality of either clock pair or of the offset is assumed in the main theorems. Plain logarithms are natural.

## 1. A full-denominator bound at every offset

Put $c=\log_2(3/2)$, $s=1+c=\log_2 3$. Then

$$
 \log_2 d >
 \frac{c A}{s^{t+1}-1}-1-\frac{t}{2}\log_2 3
             -\log_2\!\left(1+\frac p{3\Lambda}\right).                 \tag{1}
$$

Indeed write $h_i=x_i+1$. Its next value is $3h_i/2$ on an odd bit and $(h_i+1)/2$ on an even bit. Compare the original and shifted cycle. If $h_{i+r}\le Kh_i$, $K\ge1$, then the same bound holds at the next position except possibly when the partner bit is odd and the base bit even, in which case $3K$ works. These are direct inequalities using $h_i\ge1$. On a full lap precisely $t/2$ positions have this directed disagreement, because the two words have equal weights. The product of all $h_{i+r}/h_i$ is one. Starting at a phase with ratio at most one proves simultaneously

$$
                    h_{i+r}\le3^{t/2}h_i\qquad(0\le i<A).              \tag{2}
$$

The product of all actual single-step multiplicative corrections gives
$\Lambda=\sum_{w_i=1}\log(1+1/(3x_i))\le p/(3\min x_i)$.
Start now at a phase attaining the minimum. Both corrected numerators there are at most
$H=d3^{t/2}(1+p/(3\Lambda))$. At time $j$, both corrected numerators are at most $H(3/2)^j$, since each corrected-height step multiplies by at most $3/2$. A matching run of length $L$, starting at $j$, gives
$2^L\mid n_j-n_{j+r}$ by subtraction of its two affine equations and coprimality with the odd multiplier. This difference is nonzero. Equality of the two physical states would make all their future states agree by determinism, so the full periodic orbit would have the strictly shorter return $r$. Thus $L<\log_2H+cj$. Split the lap at the $t$ disagreements into $t$ matching runs followed by one disagreement and one terminal matching run, allowing empty runs. Each update satisfies $j_{\rm next}<s j+1+\log_2 H$. Starting at zero gives $A<(1+\log_2H)(s^{t+1}-1)/c$, proving (1).

The fixed two-logarithm estimate supplies $\log(1+p/(3\Lambda))=O(\log(A+1))$ uniformly. One can use the precise pinned application in PR196 below: for $A\ge10^{13}$ it gives $\log\Lambda>-5\cdot10^9(1+\log A)$. This is the only external analytic input to this asymptotic use of (1). For increasing primitive ordinary periods,

$$
 \liminf_{A\to\infty}\ \frac{\min_{0<r<A}t(r)}{\log A}
                    \ \ge\ \frac1{\log(\log_2 3)} .                    \tag{3}
$$

For if $t\le(1/\log s-\epsilon)\log A$, the first term of (1) grows as a positive power of $A$, and its negative terms cost only $O(\log A)$. The same argument gives $\log d\gg_\epsilon A^{\epsilon\log s}$ in this range for rational cycles.

## 2. Euclidean restriction at every offset

Put $g=\gcd(A,r)$, $N=A/g\ge2$, and let $u$ be the inverse of $r/g$ modulo $N$ in $[1,N-1]$. Let $S$ be the sum of the partial quotients of the finite continued fraction of $u/N=[0;a_1,\ldots,a_h]$ with $a_h\ge2$. For every such rotation,

$$
 \log_2 d >
 \frac At-1 - \log_2\!\frac p{2\eta}
                 -(8tS+g)\log_2 3 .                                    \tag{4}
$$

Here (4) compares the complete denominator to the Euclidean data of the offset, rather than to the cycle clock gcd. To prove it, first take a cyclic interval in the circle $\mathbb R/\mathbb Z$, a starting point on that circle, and a block of $q_j$ successive steps of size $u/N$, where $q_j$ is a convergent denominator. Match the points to the equally spaced grid of step $p_j/q_j$ with the same starting point. Each point moves by at most $1/q_j$, since $k|u/N-p_j/q_j|<1/q_j$ for $0\le k<q_j$ at proper convergents, and at the last it is zero. The grid interval count differs from its length times $q_j$ by at most two. At most three grid points per boundary can lie within circle distance $1/q_j$ of that boundary, also for $q_j=1,2$. Thus the discrepancy is at most eight per interval. For any prefix of length $n<N$, greedily subtract convergent denominators starting from the largest usable one. By $q_{j+1}=a_{j+1}q_j+q_{j-1}$, at most $a_{j+1}$ copies of $q_j$ are used; at the lowest denominator the same conclusion holds, discarding any duplicate 1. Thus one needs at most $S$ blocks. At $n=N$ the entire discrete orbit is one equally spaced grid. These estimates hold at every starting phase. For an interval with endpoints on the discrete grid its mean is exactly its number of residues divided by $N$.

In the column of indices $i\equiv b\pmod g$, moving by $r$ forms a single cycle of order $N$. If that column has $t_b>0$ disagreements with its next step in this order, its ones form $t_b/2$ disjoint cyclic discrete intervals in this coordinate. In physical column order $i\mapsto i+g$, the coordinate step is $u/N$. Constant columns have zero discrepancy from their individual means. Consequently each consecutive column prefix has discrepancy at most $8 S\,t_b/2$ from its column mean. For a physical interval of $L\le A$ bits, the number sampled from each column differs from $L/g$ by less than one. Since column means are between zero and one, the discrepancy of its entire odd count from $Lp/A$ is at most $8tS+g$, summing the column discrepancies and the endpoint error.

Every suffix of any full lap consequently has slope $3^q/2^L\le 3^{8tS+g}$, because $p\log 3/A<\log 2$. The full affine translation is a sum of $p$ odd-step intercepts $1/2$ times the corresponding suffix slopes. At every phase,
$x_i\le p3^{8tS+g}/(2\eta)$. The longest cyclic stretch of agreement with this rotation has length at least $(A-t)/t=A/t-1$. Apply the nonzero difference divisibility there and the all-phase upper bound on $x_i$. In particular, writing $B=\max_I(\#_1(I)-|I|p/A)$ over all cyclic intervals, the argument proves the intrinsic bound
$$
 \log_2 d>A/t-1-\log_2(p/(2\eta))-B\log_2 3.
$$
This proves (4) without a minimum-state assumption or an external analytic input.

For integer cycles the same two-log estimate gives $\log(p/(2\eta))=O(\log A)$. If $g$ is bounded and $S=O(\log A)$, every such shift has $t\gg\sqrt{A/\log A}$. More generally $A\ll t\log A+t^2 S+tg$, with absolute constants.

### Near-rational offsets are necessary for logarithmic Hamming distance

Fix $K$. In any sequence of primitive ordinary cycles and offsets with $t\le K\log A$, there are positive integers $m=O_K((\log A)^3)$ and integers $v$ with $|v|=O_K((\log A)^3)$ such that

$$
                            mr\equiv v\pmod A.                           \tag{5}
$$

Choose an absolute constant $C$ with $A\le C(t\log(A+1)+t^2 S+tg)$. For large $A$ the first term on the right is at most $A/3$. If $Ctg\ge A/3$, take $m=N=O(t),v=0$. Otherwise $S\gg_K A/(\log A)^2$ for large $A$. There are $O(\log A)$ digits, because every two convergent denominator steps at least double. Some $a_j\gg_K A/(\log A)^3$. For its preceding convergent $p'/q'$, including $0/1$ when $j=1$, put $e=q'u-Np'$. Then $0<|e|\le N/(a_jq')$ and $q'\le N/a_j$. Since $u(r/g)\equiv1\pmod N$, one has $er\equiv gq'\pmod A$. Take $m=|e|$, $v=\operatorname{sgn}(e)gq'$. Here $0<|v|<A$, $m|v|\le A/a_j$. This proves (5) in all clock and offset gcds.

In particular, for any fixed real irrational $\xi\in(0,1)$ with $\|m\xi\|\ge c m^{-\kappa}$ for all $m\ge1$, bounded-distance roundings $r=A\xi+O(1)$ cannot have $t=O(\log A)$. Indeed (5) would give $\|m\xi\|\le O((|v|+m)/A)$. An equivalent direct quantitative use gives the power bound $t\gg (A^{1/(\kappa+1)}/\log A)^{1/2}$. To see it, if $t\log A\gg A$ there is nothing to prove. In the other two cases of (4) the same proof supplies $m,|v|\ll 1+t^2\log A$, allowing zero $v$. Therefore $A\ll(1+t^2\log A)^{\kappa+1}$. For example, at offsets nearest $A(\sqrt5-1)/2$ this is $t\gg A^{1/4}/\sqrt{\log A}$. This particular irrational has $\kappa=1$ by evaluating $X^2+X-1$ at a rational and bounding its other linear factor near the positive root.

### How many offsets can nearly agree?

Uniformly for every primitive ordinary cycle and $T\ge1$ with $T\log(A+1)\le cA$ for a sufficiently small absolute $c$, the number of nonzero offsets satisfying $t(r)\le T$ is
$$
O\!\left(T^2+X\log(2X)\right),\qquad X=C(1+T^2\log(A+1)).
$$
For $T=K\log A$ this is $O_K((\log A)^3\log\log A)$. Indeed, in the large-$g$ case of the proof of (5) the order $N$ of the shift is $O(T)$, so there are at most $\sum_{n\le C'T}\varphi(n)=O(T^2)$ such offsets. In the other case $S\gg A/T^2$, some digit $a_j\gg A/(T^2\log(A+1))$, and the constructed congruence has $m|v|\le A/a_j\le X$ with $v\ne0$. For each $1\le m\le X$, write $h=\gcd(m,A)$. Among $0<|v|\le X/m$, at most $2\lfloor X/(mh)\rfloor$ signed integers are divisible by $h$, and each has exactly $h$ inverse images modulo $A$. Summing $2X/m$ proves the result. By the triangle inequality the same bound with $2T$ also bounds, up to one additional rotation, how many rotations can lie within Hamming distance $T$ of *any* one length-$A$ target word, provided $2T\log(A+1)\le cA$.

### A power law at the cycle's own clocks

Let $\beta=\log_3 2$. Fix any effective $\kappa\ge1$ and $c_0>0$ such that $\|m\beta\|\ge c_0m^{-\kappa}$ for integers $m\ge1$, where $\|\cdot\|$ denotes nearest-integer distance. Such constants follow from the same two-logarithm theorem applied to arbitrary exponents $m$ and the nearest integer to $m\beta$. For primitive ordinary cycles the logarithmic correction has the **elementary** upper bound
$$
0<\Lambda=\sum_{\mathrm{odd}\ x_i}\log(1+1/(3x_i))
              \le(1+\log p)/3.
$$
In fact the $p$ odd integers are distinct, and their sorted $j$th member is at least $j$. Thus $|A\beta-p|\ll\log(A+1)$. Write $L=\log(A+1)$ and $E=(\kappa+2)/(2\kappa+2)$.

* At the physical offset $r=p$, **every** primitive ordinary cycle satisfies $t(p)\gg A^{1/(2\kappa+2)}L^{-E}$.
* Put $g_0=\gcd(A,p)$, $a=A/g_0$, $b=p/g_0$. At **every** physical offset $0<r<A$ with $br\equiv1\pmod a$, one has $t(r)\gg a^{1/(2\kappa+2)}L^{-E}$. This is a positive power of $A$ up to logarithms, since $a\gg(A/L)^{1/(\kappa+1)}$. In particular it applies to the inverse of the odd clock modulo the total clock when they are coprime.

In both cases, if $tL$ is larger than a sufficiently small constant times $A$, the inequalities follow immediately. Otherwise the proof of (5), now retaining $t$, supplies $0<m\le X$ and $|v|\le X$ with $mr\equiv v\pmod A$, where $X=C(1+t^2L)$. In the first case, $c_0m^{-\kappa}\le\|m\beta\|\le(|v|+O(mL))/A$; thus $A\ll X^{\kappa+1}L$. In the second case $m\equiv bv\pmod a$. If $v=0$ then $a\le m$; otherwise $c_0|v|^{-\kappa}\le\|v\beta\|\le(m+O(|v|L/g_0))/a$. Both give $a\ll X^{\kappa+1}L$. Finally $c_0a^{-\kappa}\le\|a\beta\|\le |a\beta-b|\ll L/g_0$, proving the asserted comparison between $a$ and $A$. The physical offset, the cycle clock gcd $g_0$ and the offset gcd $g$ from (4) are kept independent throughout.

## 3. Small physical offsets and powers of a rotation

For any $0<r<A$ replace it by $R=\min(r,A-r)$, since the Hamming distance is unchanged. Split a linearized word into its matching stretches relative to shift $R$ and its single disagreeing bits. A matching stretch of length $L\ge R$ is $R$-periodic within that stretch, by applying $w_i=w_{i+R}$ whenever both indices are internal. It is a power of an $R$-bit word followed by a remainder shorter than $R$. A shorter stretch is a single window. Thus the whole cycle admits at most $3t+2$ nonempty proper windows. Their rational centers have logarithmic height $O(1+R)$: a power has the same center as its base affine map, whose numerator and denominator are bounded by $3^R$, and short remainders satisfy the same estimate. An all-even word has center zero, covered by the same height bound. Each nonempty word has slope different from one because $2^L\ne3^q$ whenever $L>0$.

Apply PR192's fixed-group theorem (1) in CYCLE_EXTENSION.md to this actual partition. For every fixed $\delta>0$, on any sequence with $R\le A^{1-\delta}$ and $t=O(\log A)$, it follows that $\log d=A^{1-o(1)}$. In particular, on increasing primitive ordinary periods, **every** such shift satisfies $t/\log A\to\infty$, uniformly. Since Hamming distance is subadditive on shift composition, the same exclusion of $t=O(\log A)$ holds if some bounded positive multiple of this shift has nonzero circular representative $\le A^{1-\delta}$. The fixed-group estimate and its Evertse input remain source-qualified. They are unnecessary for (1)–(5).

## 4. Bounded-gap, high-floor rational words separated at all shifts

On infinitely many coprime upper convergents $A/p$ to $\log_2 3$, there are primitive positive rational cycles with bounded gaps, minimum $\gg p^2$, complete denominator $d\ge\sqrt D$, and $t(r)\gg A$ **simultaneously** for every $0<r<A$. Thus demanding every distance test at once leaves candidates of the correct slope and arbitrarily high floor.

Use the length-$A$ lower mechanical word of weight $p$, whose count in each full consecutive eight-bit cell is five or six for large such convergents. Write $n=\lfloor A/8\rfloor$. In each full cell put one independently fair pair $01$ or $10$ at its start and use any fixed tail having the remaining required count. Leave the terminal incomplete cell unchanged. This preserves all complete-cell prefix counts. Any prefix changes by at most eight bits in odd count; prefixes reaching the final incomplete cell have unchanged count. A cyclic interval is a difference of two prefixes, with a whole lap added when it wraps. The whole count is unchanged, so comparison with the original mechanical discrepancy gives at most 18 for every interval. This bounds the zero runs uniformly. At any rotated odd position $d_i$ (indexing odds from zero at that rotation), $|d_i p/A-i|\le18$, so $2^{d_i}\ge c\,3^i$ for some fixed positive $c$, since $A/p>\log_2 3$ and $A/p<2$. The full carry is consequently at least $cp3^{p-1}$ at every odd rotation. As $D=3^p(e^\Lambda-1)$ and $\Lambda=O(1/p)$ for convergents, every odd state is $\gg p^2$. Every even state lies on a dividing-by-two chain ending at an odd state and is at least that large. All words are primitive since $\gcd(A,p)=1$; the positive state $C/D$ and its rotations give their literal rational cycles.

For a fixed nonzero rotation $r$ compare just the first bit of every cell to the bit $r$ sites ahead. Each disagreement indicator has probability at least $1/2$: the target is a constant, a bit of an independent pair, or the opposite bit of the same pair. Each indicator depends on at most two cell variables, and each variable enters at most three indicators (one as source, at most two as target). Its dependency graph therefore has maximum degree at most four. Greedy selection gives $k\ge n/5$ mutually independent indicators. For their sum $Z$, $\mathbb E[2^{-Z}]\le(3/4)^k$, so $\mathbb P(Z\le k/4)\le(2^{1/4}3/4)^k$. A union bound over all $r$ implies that the fraction of words failing $t(r)\ge n/20$ somewhere tends to zero.

In the entire family, partition into pairs obtained by flipping the first cell's transposition. The two full carries differ by a signed monomial in 2 and 3, which is coprime to $D$. The two gcds with $D$ are coprime divisors of $D$, so the **product** of the two reduced denominators is at least $D$. At least half the words have $d\ge\sqrt D$. For all sufficiently large convergents some word meets both requirements. The external two-log estimate also gives $\log D=A\log2-O(\log A)$. None of these rational cycles supplies an ordinary exception.

## Scope and antecedents

PR196, 27d03cfe902660e06604eb55bb28ca3d2754ff48, research/astra-orbit-cycle-20261124/cycles/ROTATIONAL_EXCLUSION.md R1–2 and its uniform period-gap paragraph, proves Hamming at least four and gives the pinned two-log application. Its R1 compares complementary carries when one matching interval is long. PR192, d2081d1cd2410e6004eaee9f9b13c5553afaf3f4, research/astra-closure-attack-20261124/CYCLE_EXTENSION.md, theorem (1), supplies the analytic grouped-window implication in §3, and §3 there supplies the bounded-discrepancy construction adapted in §4. PR182, 9b02334f27ff59694a91fe7f018e0aaabad7620b, research/astra-round13-20261124/DEFECT_COVER.md, estimates an arbitrary supplied cover by disjoint copies of one fixed word with intervening defects. The present paired argument instead follows all sites of one shift, even if its separate matching intervals spell different words. The project checkout is PR188, f98262be4ea40068dc88c779a767a9400a8bcaa3. The elementary discrepancy proof above does not require an external discrepancy theorem. Lyapunov Weaver, *Finite approximation bounds for mechanical Collatz itineraries* (2 November 2026), §4 uses interval-count discrepancy to bound suffix slopes and physical height. Its §7 Hamming bound compares an ordinary prefix with a critical Sturmian factor. Here the comparator is an arbitrary nonidentity rotation of the same least period, and §2 obtains its discrepancy from the arithmetic of the rotation. [Primary manuscript, §§4 and 7](https://rstation.ai/problems/collatz/papers/84). The two-logarithm dependency behind (3) and the asymptotic applications of (4) is E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in logarithms of algebraic numbers II*, Corollary 2.3, as instantiated in the pinned PR196. [Publisher DOI](https://doi.org/10.1070/IM2000v064n06ABEH000314).

The resulting restrictions leave positive primitive words with large disagreement at every offset. A proof of universal full-denominator nonintegrality would still have to exclude ordinary realization on those words. An arbitrary primitive ordinary period is not known to have a logarithmic-distance self-rotation. Escaping trajectories also remain unresolved.

## Finite controls and formal boundary

Run `python -B shift_distance_control.py` or `python -O -B shift_distance_control.py`. Every guard uses an explicit exception. The replay covers 1,131 primitive contracting necklaces through length 13, 12,282 rotations, 148,558 phase comparisons and 1,818,380 interval discrepancies. A separate complete loop checks every convergent's modular relation at all 124,251 nonzero offsets through period 499. These tests use integer arithmetic. They do not check an unknown ordinary cycle or establish asymptotic constants.

`RotationalDistance.lean` isolates paired literal walks, the directed-loss estimate, complete dyadic divisibility on a common word and the finite geometric recurrence. Its additional declarations connect exact closed literal walks to a height bound from suffix slopes, and prove the modular identity used to localize offsets. `CycleRotation.lean` supplies the finite permutation seed, balance of directed discrepancies, and noncollision of a nonidentity rotation of a least-period deterministic cycle. `ActualCycleSeparation.lean` defines the ordinary natural shortcut map, proves its literal word replay, and specializes common-word divisibility to its primitive cycles. The continued-fraction discrepancy proof, the two-logarithm application, the earlier grouped-window theorem and the probabilistic family are written mathematics.
