# Moving height intervals and dyadic–triadic order on an ordinary cycle

**Status.** Proposed elementary proofs. The confined-trajectory estimate in §1 applies to a single ordinary source, and §3 applies to primitive cycles of arbitrary amplitude. The single-octave cycle calculation in §2 recovers a known balanced-cycle exclusion. No universal ordinary-orbit contradiction was obtained. The exact obstruction to completing the two arguments is in §4.

## 1. A sharp word-count bound for any prescribed sequence of moving octaves

Let $U(q)=(3q+1)/2^{a(q)}$, with $a(q)=v_2(3q+1)$, on positive odd integers. Fix arbitrary positive real numbers $H_0,\dots,H_k$, $k\ge1$. Consider all actual paths $q_0,\dots,q_k$ with $H_j\le q_j<2H_j$ at each clock. The intervals may move up or down by different factors at every step.

**M1.** Across those paths there are at most $k+1$ complete valuation words $(a_0,\dots,a_{k-1})$. The total number of distinct ordinary starting values is at most

$$ (k+1)\left\lceil H_k/3^k\right\rceil. \tag{1} $$

For a proof, put $s_0=\log_2(q_0/H_0)\in[0,1)$, and define the real lifts

$$F_j(t)=\lfloor t\rfloor+\log_2\big((3H_j2^{\{t\}}+1)/H_{j+1}\big).$$

Each map is strictly increasing on each integer interval, satisfies $F_j(t+1)=F_j(t)+1$, and jumps upwards at every integer. Indeed the jump is $\log_2((6H_j+2)/(6H_j+1))>0$. Write $G_j=F_{j-1}\circ\cdots\circ F_0$. The path constraints and the literal odd map give

$$G_j(s_0)=A_j+\log_2(q_j/H_j),\qquad A_j=\sum_{i<j}a_i.$$

In particular $A_j=\lfloor G_j(s_0)\rfloor$. For $s_0\in[0,1)$ the function $\lfloor G_j(s_0)\rfloor$ is nondecreasing and takes at most two consecutive values, since $G_j$ is increasing of degree one. As $s_0$ increases, the vector of $k$ prefix clocks can make at most $k$ strict changes: each change increases its coordinate sum by at least one, and the total increase is at most $k$. A prefix-clock vector determines its complete valuation word by successive differences.

For a fixed word write $2^{A_k}q_k=3^kq_0+C$. Subtract the equations for any two starting values. The difference of their odd endpoints is even, and $3^k$ is odd, so the sources agree modulo $2^{A_k+1}$. Also $2^{A_k}q_k>3^kq_0$, because the carry is positive. From the initial and terminal intervals we obtain $2^{A_k+1}>3^kH_0/H_k$. An interval of length $H_0$ contains at most $\lceil H_0/2^{A_k+1}\rceil\le\lceil H_k/3^k\rceil$ members of one such residue class. This proves (1). The $k+1$ valuation-word bound is sharp at every fixed $k$, already for one stationary interval $[H,2H)$. Put $\alpha=\log_2 3$. The $k$ interior cuts $\{-j\alpha\}$, $1\le j\le k$, are distinct by irrationality. In each of the $k+1$ complementary open intervals pick a point $t$. Its clock vector $A_j=\lfloor t+j\alpha\rfloor$ differs at successive cuts, so these give $k+1$ words of gaps one or two. Any prescribed positive gap word with total $A_k$ is realized by one odd residue modulo $2^{A_k+1}$: a parity bit word of length $A_k+1$ specifies a unique such residue, including the terminal odd bit. The parity bijection follows inductively since two source lifts differing by $2^l$ share their first $l$ bits and their images there differ by the odd integer $3^{\#\mathrm{odd}}$. Choose a source in the residue within $2^{A_k+1}$ of $2^t H$. Its successive heights divided by $H$ tend to $2^{\{t+j\alpha\}}$ as $H\to\infty$ by the affine equations with fixed clocks and fixed carries. All these limits lie strictly between one and two, including $j=0$. For a common sufficiently large $H$ all $k+1$ chosen ordinary paths stay in the band. This proves word-count sharpness and makes no joint sharpness claim for the two factors in (1).

**M2.** Suppose $q_0,\dots,q_L$ are distinct and all lie in $[H,2H)$. For $k=\max(1,\lceil\log_3 H\rceil)$ one has $L\le2k$. If $L\ge k$, the $L-k+1$ initial states of its length-$k$ windows are distinct. They all fit the same stationary interval schedule, whose (1) bound is $k+1$. The claim follows; $L<k$ is immediate. Thus an actual nonperiodic orbit, from any of its suffix minima $m$, attains an odd value **strictly greater** than $2m$ within $2\max(1,\lceil\log_3 m\rceil)+1$ odd steps. There is no lower exit at a suffix minimum, no repetition on the nonperiodic orbit, and an odd value cannot equal $2m$. It may subsequently fall below this new value.

For a two-octave band $[H,4H)$ every length-$k$ window follows one of $2^{k+1}$ schedules on the intervals $[H,2H)$ and $[2H,4H)$. With $k=\max(1,\lceil\log_3(2H)\rceil)$, (1) gives $L-k+1\le 2^{k+1}(k+1)$ whenever $L\ge k$. More generally, (1) applies separately to each distinct prescribed profile, regardless of its amplitude. The profile count, not the set of values of an unconstrained orbit, is the input to this summation.

## 2. A single-octave periodic trajectory and the complete reduced denominator

Consider a primitive positive rational odd cycle of $p$ phases $x_i$, common reduced odd denominator $d$, valuations $a_i\ge1$, total $A=\sum a_i$ and $D=2^A-3^p>0$. The complete return equation gives $d\mid D$. Every phase has the same denominator because $D$ is prime to 6 and both multipliers are units at its primes. Put $z_i=dx_i$. These are distinct positive odd integers.

If the odd phases lie in $[m,2m)$ for the cycle minimum $m$, then **$d=D$**. Sort the numerators as $z_0<\cdots<z_{p-1}$ and extend their ordered list as $Z_{j+p}=2Z_j$ for all integer $j$. For $0\le j<p$ the raw images $W_j=3Z_j+d$ are strictly increasing, and $W_{p-1}<2W_0$. They are distinct dyadic representatives of all orbit rays by the cycle equation. Hence there is an integer $R$ with $W_j=Z_{j+R}$ on the base period: the $p$ images are in increasing order, all within $[W_0,2W_0)$, which contains exactly $p$ members of the ordered list. Let $\sigma(j)$ give the forward index, $a(j)$ its physical valuation, and $\Delta_j=Z_{j+1}-Z_j$ on the base period. For $j<p-1$, $W_{j+1}-W_j=3\Delta_j$. At the seam $2W_0-W_{p-1}=3\Delta_{p-1}+d$. In both cases the output gap is $2^{a(j)}\Delta_{\sigma(j)}$. Thus

$$2^{a(j)}\Delta_{\sigma(j)}=3\Delta_j+d\,\mathbf 1_{j=p-1}.$$

The permutation is a single $p$-cycle. Iterating once from any gap gives $D\Delta=d\,2^b3^c$ for some nonnegative $b,c$, since exactly one additive term occurs on the whole lap. Because $D$ is prime to 6, $D\mid d$. For an ordinary cycle $d=1$, thus $2^A-3^p=1$. For $A\ge3$ this is impossible modulo 8, as $3^p\bmod 8\in\{1,3\}$. The remaining positive solution is $A=2,p=1$ with $x=1$.

**Prior work.** The balanced high-cycle gcd result is due to Kevin Knight, [*Collatz high cycles do not exist*, Discrete Mathematics 349(3), 114812 (2026)](https://doi.org/10.1016/j.disc.2025.114812). The selection of balanced words by small amplitude in the two-letter setting and an ordered-state obstruction are explicit in [Lyapunov Weaver, Cassian Mahler and Fourier Wren, *Sparse block-sum and ordered-state complexity in positive Collatz cycles*, v3, especially §§“Definitions and the sparse numerator” and “Ordered-state complexity”](https://rstation.ai/problems/collatz/papers/22/v3). For $m\ge1$ and width less than two the possible valuations are $1,2$ (with the trivial point included). We give the adjacent-gap proof as a self-contained connection to the moving-interval argument and claim no priority for balanced-cycle exclusion. The rank calculation below orders all dyadic or triadic lifts, so it compares numbers in different ordinary height ranges.

## 3. Two order obstructions for the same primitive cycle, without an amplitude bound

**O1.** Let $g=\gcd(A,p)$. The odd values of a primitive positive **ordinary** cycle contain at least $g-1$ distinct triples $(u,v,s)$ such that

$$ s\ge3,\qquad 0<3(v-2^s u)<2^s-1. \tag{2} $$

No two counted triples use the same unordered pair: $v>u$, and the allowed intervals for $v$ at different $s$ are disjoint because $u\ge1$. In particular, if the largest odd value is at most eight times the smallest, the clocks of the cycle are coprime. For a primitive positive rational cycle the exact condition on its **reduced numerator** phases $U,V$ is $s\ge1$, $0<3(V-2^sU)<d(2^s-1)$, with the same count of triples. Thus the exclusion at small spread uses ordinary integrality genuinely.

**O2.** Consider the full primitive shortcut cycle, of length $A$, with the odd branch $(3x+1)/2$ and even branch $x/2$. Let $e(x)\in\{0,1\}$ be the parity of the *physical predecessor* of the state $x$ on this cycle. On the very same ordinary cycle there are at least $g-1$ triples of shortcut states $(u,v,s)$ with

$$ s\ge1,\qquad e(v)=1,\qquad 0<2(3^s v-u)<3^s-e(u). \tag{3} $$

These are a second list of witnesses. The arguments impose no equality of the pairs in the two lists. Both counts, taken with triples as written, have parity $g-1$.

### Order argument

Suppose $J$ is a permutation of $\mathbb Z$ satisfying $J(j+n)=J(j)+n$ and inducing a single cycle on the $n$ residue positions. The integer $R=n^{-1}\sum_{j=0}^{n-1}(J(j)-j)$ is its mean displacement; it is integral since the target residues are a permutation. Count inversions modulo simultaneous translation of both indices by $n$:

$$ I=\sum_{j=0}^{n-1}\#\{l>j:J(l)<J(j)\}.$$

This is finite since $J(j)-j$ is bounded. Bubble-sort any adjacent descent by swapping its two entries and all their translates by $n$ simultaneously. For $n\ge2$ the swapped pairs are disjoint. The inversion count drops by exactly one: for any other position the comparisons with the two swapped entries cancel in aggregate, and the sole internal comparison in one period changes from inverted to ordered. Equivalently, count on $N$ consecutive periods and divide by $N$; bounded displacement confines boundary effects to $O_J(1)$ pairs. The mean displacement is unchanged, including for a swap across the periodic seam. After $I$ swaps there are no descents. An increasing permutation of $\mathbb Z$ is $j\mapsto j+R$. Its residue projection has $\gcd(R,n)$ cycles. Each swap composes the residue permutation with one transposition, changing its cycle count by exactly one. Hence $I\ge\gcd(R,n)-1$ and $I\equiv\gcd(R,n)-1\pmod 2$. For $n=1$, $I=0$ directly.

For (2), sort **all** real numbers $2^t x$ for odd phases $x$ and integers $t$. Distinct odd numerator phases of a rational cycle with common denominator lie on distinct dyadic rays. Index the ordered set by $Z_j$, where $Z_{j+p}=2Z_j$. Send $2^t x$ to $2^t(3x+1)=2^{t+a(x)}U(x)$. This is a bijection on the lifted set and determines $J$. Its projection is the physical forward $p$-cycle. To see the mean displacement, choose one simultaneous period of the sorted starts, give its $p$ representatives scaling exponents $t_x$, and write $J(j)=\sigma(j)+p(t_x+a(x)-t_{U(x)})$ for the rank permutation $\sigma$. The terms $t_x-t_{U(x)}$ sum to zero, giving $R=A$.

A lifted inversion has $\lambda u<\mu v$ and $\lambda(3u+1)>\mu(3v+1)$, so $\lambda>\mu$ and $\lambda/\mu=2^s$ for an integer $s\ge1$. This is precisely $0<3(v-2^s u)<2^s-1$. Conversely each such triple gives one inversion up to simultaneous scaling. For integer $u,v$ the positive difference is at least one and so $2^s-1>3$, forcing $s\ge3$. Substitution $u=U/d$, $v=V/d$ gives the rational version. With no inversions, the dyadic rank map on the infinite ordered cover is exactly $j\mapsto j+A$.

For (3), every shortcut phase is prime to 3. At an odd step the output is a unit modulo 3, division by two preserves this property, and a complete period has an odd step. Thus distinct shortcut phases lie on distinct triadic rays. For the true predecessor $y$ of $x$ we have $3^{e(x)}y=2x-e(x)$. Sort all $3^t x$ and send them to $3^t(2x-e(x))$. The same rank calculation gives $n=A$, $R=\sum_x e(x)=p$, and a single residue cycle in the backward direction. An inversion has $\lambda u<\mu v$ but $\lambda(2u-e(u))>\mu(2v-e(v))$. Hence $0<2(\mu v-\lambda u)<\mu e(v)-\lambda e(u)$ and $e(v)=1$. If $\mu\le\lambda$, divide by $\mu$: the positive integer $v-(\lambda/\mu)u$ would have twice its value less than or equal to one. Thus $\mu/\lambda=3^s$, $s\ge1$, giving exactly (3), with the converse obtained by using these lifts. This proves both count and parity assertions.

## 4. Where the proposed global contradiction stops

The harmonic correction on an ordinary injective orbit can be small, yet an order inversion depends on an arbitrarily close pair of *scaled* states. Even on one actual injective segment, the odd path from $27$ contains $47$ and $377=8\cdot47+1$ before dropping below $27$; these are a crossing in (2). This is a control for the proposed inference from ordinary legality to order preservation, not an example of an ordinary nontrivial cycle. Likewise, the primitive positive rational cycle with gaps $(1,1,1,2,1,4)$ has $D=295$, $d=59$, showing partial numerical cancellation is possible outside the one-octave proof. Neither small reciprocal correction alone nor divisibility at selected primes proves that (2) and (3) are incompatible. In the entire coprime-clock case both lower bounds are zero. For escape, no estimate here bounds the number of different height profiles a single source may traverse or prevents return after a fast doubling. Global convergence, all nontrivial ordinary cycle exclusion, and fixed-source escape exclusion remain open.

**Repository context and verification.** The checks here are independent of the analytic estimates in PR182 (`9b02334f27ff59694a91fe7f018e0aaabad7620b`, complete reciprocal budget), PR192 (`d2081d1cd2410e6004eaee9f9b13c5553afaf3f4`, fixed-source unit equations), and PR196 (`27d03cfe902660e06604eb55bb28ca3d2754ff48`, chronological rotation exclusions). PR193 (`c6cb5e66516a86c33a757154983bbddc822510de`, `research/astra-universal-descent-20261124/cycles.md`, C3–C5) supplies the earlier common-denominator and parity-cylinder context. The independent written proofs above need no lower bound for a linear form in logarithms and no computational verification of convergence up to any threshold.

`OctaveProfiles.lean` proves the ordered-vector count, actual affine endpoint congruence including the terminal odd bit, final unit-denominator cancellation, and the integer crossing-interval criterion. The monotone real lifts, sharpness construction, circular gap derivation and affine-permutation sorting are written mathematics. `check.py` tests the ranks and inversions, finite paths, and rational denominators with exact arithmetic. Both normal and optimized Python runs returned 9,774 moving profile groups (16,368 source occurrences), 941 primitive rational cycles with 5,627 dyadic and 32,459 triadic inversions, and 49,999 ordinary single-octave starts. The rational census includes 506 cycles with noncoprime clocks and 30 one-octave cycles. No unbounded assertion is inferred from the replay.
