# A logarithmically growing odd cost along entire ordinary ascents

Write $T$ for the shortcut map, $Q_t$ for its odd-departure count, and $a=3/2$. For an odd supplied $N>1$, its initial all-odd ascent has sites $Y_i=a^i(N+1)-1$ for $0\le i\le v_2(N+1)$. The input restriction below is $N\equiv1\pmod{3^K}$. Different targets may have arbitrarily different ascent lengths.

**Uniform depth theorem.** In every interval of $R$ positive integer depths $K$, all but $O(R^{0.96})$ have the following property. Set $M=\lfloor0.25\log R\rfloor$. For **every** such ordinary $N$ with $N+1\ge6^{K+M}$, **every** upper ascent site $Y_i$, and **every** ordinary visitor $x<N$ with $T^h x=Y_i$ at **any** incoming clock $h$,

$$Q_h(x)>i+K+M. \tag{1}$$

All logarithms without a base are natural. The constant in the exceptional count is absolute and independent of the interval's location. The depth count is over $K$, not over the individual sources, upper sites or incoming clocks. The proof accepts repeating or unbounded hypothetical positive orbits. In the selected depth classes the estimate applies to all of them. For the two supplies in the preceding packet with depths $41$ and $141$, the smallest costs at every site are exactly $i+50$ and $i+171$, respectively. Those finite statements do not use the asymptotic bound.

## Extracting a small ordinary forward orbit

Suppose $Q_h(x)=i+K+m$ with $1\le m\le M$ and $N+1\ge6^{K+M}$. The range $Q_h(x)\le i+K$ is already excluded by the PR146 unit barrier. Let $e=h-Q_h(x)$ count all reverse even steps. On shifted heights $v+1$, a reverse odd multiplies by $2/3$ and a reverse even sends $V$ to $2V-1\ge(3/2)V$ for physical $v\ge1$. Since $Y_i+1=a^i(N+1)$, $x<N$ implies $e<K+m$. More exactly, unrolling the inverse word gives

$$x+1=D(N+1)-E,\qquad D=2^e(2/3)^{K+m},\qquad 0\le E\le2^e-1. \tag{2}$$

Each inverse even contributes one times the later factors, bounded by two for each later even and one for each later odd. The resulting geometric sum proves the bound on $E$. If $D>1$, its positive excess is at least $3^{-(K+m)}$, contradicting the stated size threshold because $e<K+m$. Equality is impossible. Hence $D<1$.

In the reverse word from $Y_i$, stop just after odd number $i+K$; let $r$ be the number of even steps up to this cut. For these letters run the same affine reverse updates from the positive rational $y_i=2a^i-1$. The two initial targets differ by $3^{K+i}u/2^i$ where $N=1+3^Ku$. Induction or the affine formula shows that after $j$ reverse letters, $q$ of them odd, the difference equals $2^{j-i}3^{K+i-q}u$. The only possible denominator of the reference values is the remaining power of two: reduction modulo three makes every prescribed inverse odd divisible in $\mathbb Z[1/2]$ while $q<i+K$. For the first $j\le i$ letters the reference value stays at least $2a^{i-j}-1\ge1$: the odd inverse attains that minimum and the even inverse is strictly larger at positive input. At $j=i$ it is an integer, also directly from the difference formula; from then on it follows ordinary positive integer inverse moves. The endpoint $w$ at the cut is a positive odd integer. In shifted coordinates the reference gives

$$w+1\le2\,2^r(2/3)^K<2a^m. \tag{3}$$

The last inequality follows from $D<1$ since $r\le e$. Thus a cheap visitor produces a **small ordinary** $w$, independently of $N$, $i$, and the incoming clock.

Let $z$ be the reference after the first $i$ reverse dates. The actual forward orbit of $w$ reaches $z$ at $t=K+r$ shortcut steps. Let $d$ count evens among those first $i$ virtual reverse letters. Then $Q_t(w)=K+d$. Forward along their affine formulas from $z$ in shifted coordinates yields

$$3^{i-d}(z+1)+B=2\,3^i,\qquad 0\le B/3^{i-d}\le 2^d-1.$$

Indeed each forward even contributes $2^b(2/3)^q$ to the normalized carry when $b$ earlier evens and $q$ earlier odds have been read. This computation only uses affine identities on the final rational part. It follows that

$$2\,3^d-2^d\le z\le2\,3^d-1. \tag{4}$$

The case $i=0$ gives $d=0$, $z=1$ as required. [PR146 unit barrier](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/ADJACENT_DESCENT.md) · [Earlier positive-root direct price](DIRECT_ANCESTORS.md).

## Counting all possible cheap depths, including hypothetical cycles

For each $w$ from (3), define its monotone real correction

$$P_t(w)=\prod_{0\le j<t,\ T^jw\text{ odd}}\left(1+\frac1{3T^jw}\right).$$

The exact identity $2^t z=3^{K+d}w P_t(w)$, (3) before its final comparison, (4), and $D<1$ imply

$$\frac12\le\frac{2^t}{3^K}<a^M,\qquad 0\le\log P_t(w)\le\log(2a^M),\qquad |t-K\log_2 3|\ll M+1. \tag{5}$$

For $z\ge Y$ equation (4) also gives

$$t-K\log_23=\log_2(w/2)+\log_2 P_t(w)+O(Y^{-\eta}),\qquad \eta=1-\log_32. \tag{6}$$

No bound on the product after the last eligible clock is needed.

Fix $w$ and a translated depth interval of length $R$. The clocks $t$ eligible under (5) lie in an interval of length $O(R+M)$. At the last eligible clock $t_*$, $\log P_{t_*}\ll M+1$. Every odd visit to height at most $Y$ before $t_*$ increases $\log P$ by at least $c/Y$. Every even visit below $Y$ reaches such an odd in at most $\log_2Y$ halvings, aside from a possible final incomplete run. Thus there are $O((M+1)Y\log(2Y))$ eligible dates with $z\le Y$, including repetitions. Each date has $O(M+1)$ eligible $K$ by (5).

Set $Y=R^{0.42}$ and $\delta=R^{-0.15}$, so $Y^{-\eta}=O(\delta)$. Partition $\log_2 P_t$ through $t_*$ into consecutive bins of width $\delta$. Monotonicity gives at most $B=O((M+1)/\delta)$ contiguous clock intervals. Intersect each with the allowed clock range from (5). Expanding its range by $O(M+1)$ and dividing by $\log_23$ gives one integer $K$-interval of length $L_j$, with $\sum_j L_j\ll R+(M+1)B$. In each such interval (6) places the fractional part of $K\log_23$ in one fixed circle arc of length $O(\delta)$.

Bondareva–Luchin–Salikhov, Theorem 1, with constant coefficient zero, gives $\|j\log_23\|\gg j^{-4.117}$ for $j\ge1$. Indeed take the nearest integer multiple of $\log2$ and absorb finitely many small nonzero forms in the constant. The Erdős–Turán inequality and the finite geometric sum yield, for any consecutive interval of $L\ge1$ integers and arc $I$,

$$\#\{K:\{K\log_23\}\in I\}\le L|I|+C L^{1-1/(4.117+1)}.$$

To see the exponent, truncate Erdős–Turán at $H=\lfloor L^{1/(4.117+1)}\rfloor$: the error is $O(L/H+\sum_{j\le H} j^{4.117-1})$. Hölder's inequality sums the discrepancy terms to $O(B^{1/5.117}(\sum L_j)^{1-1/5.117})$. As $M\ll\log R$, the small-height term is $R^{0.42+o(1)}$, the arc main term is $R^{0.85+o(1)}$, and the discrepancy sum is at most $R^{1-0.85/5.117+o(1)}$. Hence each $w$ accounts for $O(R^{0.85+o(1)})$ possible depths. Equation (3) allows $O(R^{0.25\log(3/2)})$ roots. Since $0.85+0.25\log(3/2)<0.952$, this proves (1). The rotation estimate uses homogeneous two-logarithm approximation; it does not assume a Diophantine inequality for the moving correction $P_t$. [Bondareva–Luchin–Salikhov, primary theorem](https://doi.org/10.22405/2226-8383-2018-19-1-15-25).

## Exact all-clock prices on three supplied entire ramps

For a finite screen at $i\ge1$, make the virtual-to-ordinary cut one date earlier, after $i-1$ reverse steps. The reference there is an integer because $y_i=2(3/2)^i-1$ has denominator dividing $2^{i-1}$, and at that date the translated difference is $3^{K+i-q}u/2$, an integer since $u$ is even. Let $z$ be this integer, $d$ the number of evens in those first $i-1$ virtual reverse steps, and $r$ the number of evens up to odd number $K+i$ as before. The identical carry computation gives

$$t=K+1+r,\qquad Q_t(w)=K+1+d,\qquad 3^{d+1}-2^d\le z=T^t(w)\le3^{d+1}-1. \tag{7}$$

If $w$ first reaches one with at most $K$ odd departures, its physical prefix to $z$ has already reached the known cycle. Then $z=2$ and $d=0$ from (7), so those first $i-1$ reverse letters are all odd. The next reverse letter must also be odd, since the preceding physical state was one on this cycle and its forward image was two. Thus the true inverse word has first backtracked to $N$ itself. Its remaining cost is at least $K+m_K$ by the direct theorem for the three supplies. This gives a general consequence: infinitely many unbounded depths admitting an all-ascent excess bounded by a fixed $M$ would require a nonterminating odd $w<2(3/2)^M$ (use the divergence of $m_K$). The primary verified range $w<2^{71}$ therefore already excludes such exceptions for each $M\le119$ at sufficiently large $K$, with an unspecified finite threshold. Formula (1) additionally controls larger $M$ and does not require prior computational convergence. [Bařina, 2025, verified range](https://doi.org/10.1007/s11227-025-07337-0).

More precisely, (2) forces $2^{r+K+m}<3^{K+m}$, and the unrounded first inequality of (3) forces $(w+1)3^K\le2^{r+K+1}$. Those give finite ranges for $r,w$. For a proposed upper budget $m\le m_0$, use the bounds at $m_0$. On each remaining odd $w$ it suffices to follow its actual orbit until one or the largest possible $K+1+r$, testing (7) and the last size bound. If it reaches one, subsequent feasible cycle positions force backtracking as just proved. A failure of this necessary test excludes every remote ascent date and every incoming clock at once; passing it alone does not construct a visitor.

| $K$ | Excess tested $m_0$ | Possible odd $w$ bounded by | $w$ requiring more than $K$ odds | Survivors of (7) and size test | Exact minimum at every $Y_i$ on the supplied prime ramp |
|---:|---:|---:|---:|---:|---:|
| 41 | 8 | 50 | 0 | 0 | $i+50$ |
| 141 | 29 | 255,667 | 2 | 0 | $i+171$ |
| 357 | 44 | 111,955,488 | 0 | 0 | $i+402$ |

In the third row the single-thread checker also determines the unique length-592 minimizing $K=357$ benchmark among every odd $w\le75,417,042$. It uses a fixed cache of $2^{20}$ pairs of unsigned shorts, checks every orbit multiplication for overflow, and stops at $K+1$ odd steps when the first hit can no longer qualify. The Python driver supplies the exact power cutoffs. The small checker additionally reports deliberately relaxed cutoff tests; those may leave unclassified candidates. For each prime source in the direct-ancestor packet its explicit ordinary visitor at cost $K+m_K$ follows the real upper ascent forward, attaining the stated price at every $i$. The all-clock lower prices hold for every odd $N$ of the stated depth and sufficient size; the constructive equality additionally requires the source residual specified there. [Depth-41/141 checker](check_ramp_ancestors.py) · [Small controls](ramp_ancestor_controls.json) · [Depth-357 checked C++ scan](check_large_ramp.cpp) · [Exact cutoff driver](run_large_ramp.py) · [Large controls](large_ramp_controls.json) · [The three supplied prime exponents](direct_ancestor_controls.json).

PR195 already calculates the sharp incoming cost at the **other edge** of a single apex using the negative integer tree rooted at $-2$, including a complete criterion at a supplied cofactor. The cost over the entire near-one ramp permits intersections through earlier sites at arbitrary upper dates, and its comparison after the dyadic denominator disappears takes place in the positive integer graph. Neither that earlier theorem nor the sufficient upper examples here establish unrestricted smaller coalescence for every integer. [PR195, exact other-edge optimum](https://github.com/GettysburgResearch/collatz/blob/51d97cbe17054415acaf95e422801a3532545033/research/astra-unconventional-20261126/renormalization/FIRST_MEETING.md).

A further antecedent is Weaver's Paper 65, Theorems 1, 2 and 5. Its terminating-seed construction already inserts a first-arrival word to improve a loop at one, and its full compiler has vanishing coverage near multiples of $3^k$ for its seven-symbol rational cycle. It does not classify all physical competitors at the positive-one target. Likewise Paper 229 §2 upgrades the window transfer behind the direct-ancestor upper estimate to a worst-root asymptotic; its uniformity is stronger than needed at the benchmark root one. [Paper 65 v1](https://rstation.ai/problems/collatz/papers/65) · [Paper 229 v1](https://rstation.ai/problems/collatz/papers/229).
