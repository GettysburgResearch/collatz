# Positive-density changes in the ordered dyadic bands

**PROPOSED written theorem.** Consider a primitive ordinary positive odd Collatz cycle from the bounded least-tripling-disagreement alternative. Let its least odd member be $s$, its odd period be $p$, and its shortcut period be $h$. Write the odd members as $2^{k_r}z_r$, indexed by the increasing order of their normalized values $z_r\in[s,2s)$, with $k_r\in\{0,1,2\}$. For every sufficiently large $p$, simultaneously for the integers $1\le t\le p/(\ln p)^2$,
$$
 E_t:=\#\{0\le r<p:k_{(r+t)\bmod p}\ne k_r\}>p/83.
$$
In particular a coloring with only $o(p)$ intervals in sorted order cannot occur in these ordinary cycles. Round 9 gave $E_1\gg p/\log s$. The new bound controls a positive fraction and a growing range of rank offsets. Every modulus in the proof applies to integer gaps within the same orbit. The statement has an asymptotic onset.

## Lifted gaps and the two cuts

Put $Z_r=4z_r$, $c_r=2^{2-k_r}$ on $0\le r<p$. Extend both lists to $r\ge0$ by $Z_{r+p}=2Z_r$, $c_{r+p}=2c_r$. The established quarter-grid rotation gives $Z_{r+h}=3Z_r+c_r$ on one period. Doubling extends that equation to all $r\ge0$. In particular $\gcd(h,p)=1$. For each $t\le p$ define the positive integer gap $G_r=Z_{r+t}-Z_r$ and the signed letter $J_r=c_{r+t}-c_r$ using these **lifted** indices. Then
$$
 G_{r+p}=2G_r,\qquad G_{r+h}=3G_r+J_r.
$$
On the base ranks write $r'=(r+h)\bmod p$, $b_r=\lfloor(r+h)/p\rfloor$. The exact recurrence is
$$
                  2^{b_r}G_{r'}=3G_r+J_r.                         \tag{1}
$$
At the input cut $r+t\ge p$ the letter is $2c_{r+t-p}-c_r$. The output cut in (1) takes a common factor $2^{b_r}$ out of the entire lifted gap, including when the upper endpoint crosses another boundary. Off the input cut, $J_r$ is zero unless the bands differ, and its six possible nonzero values are $\pm1,\pm2,\pm3$. [Ordered recurrence and full-denominator congruence, PR192](https://github.com/GettysburgResearch/collatz/blob/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124/cycle/README.md) · [Round 9 order, rank error and earlier change bound](../../round9/critical/README.md)

## Why a gap value cannot occur too often

The round 9 rank estimate is $|\ln(z_r/s)-(r/p)\ln2|\le p/(12s)$. Indeed, the log error along time is a partial sum of centered increments $\ln(1+1/(3x_i))$. The range of these increments is at most $1/(3s)$, and the centered sum over $j$ terms is at most $j(p-j)/p$ times that range in absolute value. Both $z_r$ and $s2^{r/p}$ are at most $2s$. The mean value theorem gives $|Z_r-4s2^{r/p}|\le 2p/3$ on one period. On the next period the error at most doubles. Thus on the base period, with $X=st$,
$$
 |G_r-H_r|\le2p,\qquad H_r=4s(2^{t/p}-1)2^{r/p}.
$$
Successive $H_r$ differ by at least $4s(t\ln2/p)(\ln2/p)\ge X/p^2$. Any fixed gap value occurs at most $1+4p^3/X$ times. The chord bound $2^{t/p}-1\le t/p$ gives $G_r\le8X/p+2p\le10X/p$ when $s\ge p^2$.

We use two pointwise height estimates. PR200's physical strip count gives $p\ll s^{479/1000}$ for this least-disagreement branch. In particular $s\gg p^{1000/479}$ and eventually $s\ge p^2$. The cycle product gives
$$
 0<h\ln2-p\ln3=\sum_i\ln(1+1/(3x_i))\le p/(3s).
$$
Wu and Wang's Theorem 1, with zero constant coefficient, bounds this nonzero form below by $(2p)^{-4.1163051-\epsilon}$ for large $p$, using $p<h\le2p$. Hence $s\ll p^{5.12}$ using $\epsilon=0.003$. Uniformly over the claimed offsets,
$$
              p^{1000/479}\ll X\ll p^{6.12}.                         \tag{2}
$$
[PR200, Theorem S at the frozen revision](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md) · [Wu and Wang, Theorem 1, J. Number Theory 142 (2014), 264–273](https://doi.org/10.1016/j.jnt.2014.03.007)

## A two-sided cylinder fixes the middle gap

Take $L=\lceil\log_3(1+20X/p)\rceil$ and $a=\lfloor L/2\rfloor$. For two length-$L$ windows along the rank rotation with the same $(b,J)$ word, subtract (1). The resulting integer differences $d_i$ satisfy $2^{b_i}d_{i+1}=3d_i$. Iterating over the first $a$ and last $L-a$ positions gives
$$
 2^{B_-}d_a=3^a d_0,\qquad 2^{B_+}d_L=3^{L-a}d_a.
$$
Coprimality gives $3^a2^{B_+}\mid d_a$. The forward wrap sum $B_+$ is at least $(L-a)h/p-1$, by telescoping the floors from its own starting rank. As $h/p>\log_2 3$, the product modulus is at least $3^L/2>10X/p$. Thus $d_a=0$. A full word fixes one ordinary middle gap. All $p$ window starting phases give all $p$ middle ranks by a permutation. This argument also works with an entirely one-sided cylinder, with the same exponential scale. The two local moduli consume their respective steps in the single common word.

## Counting sparse windows

Suppose $E_t\le p/83$. A uniform cyclic window has mean $LE_t/p$ unlifted band mismatches by double counting. Markov's inequality leaves at least $p/83$ windows with at most $L/82$ mismatches. At most $Lt$ windows hit any of the $t$ input-cut ranks. By (2), $L=O(\ln p)$ uniformly, so $Lt=o(p)$ for the specified offsets. At least $p/166$ windows therefore avoid this cut and have at most $L/82$ nonzero $J$'s for sufficiently large $p$.

The $b$-lists have at most $L+1$ possibilities. For initial normalized rank $v/p\in[0,1)$ the partial sums are $\lfloor(v+jh)/p\rfloor$ for $1\le j\le L$. Each is nondecreasing with at most one jump as $v$ varies. Their joint vector assumes at most $L+1$ values. For $H(y)=-y\ln y-(1-y)\ln(1-y)$ and $\theta=1/82$, the number of admissible signed-letter lists is at most $(L+1)\exp[L(H(\theta)+\theta\ln6)]$. This follows by choosing the support, choosing one of six signs and magnitudes at each occupied slot, and applying the binomial entropy bound, increasing on this support range. Put $\delta=(H(\theta)+\theta\ln6)/\ln3$. The strict inequality $\delta<42/521$ is equivalent to
$$
                 (6\cdot82^{82})^{521}<81^{81\cdot521}3^{82\cdot42}.
$$
It is checked by exact integers in the accompanying replay.

Every selected word fixes a gap of multiplicity at most $1+4p^3/X$. Since $3^L\ll X/p$, this yields the necessary inequality
$$
               p\ll (\ln p)^2(1+p^3/X)(X/p)^\delta.                 \tag{3}
$$
If $X\le p^3$, divide (3) by $p$ and use (2). The right side is $O((\ln p)^2p^{2-\delta+(1000/479)(\delta-1)})$, which tends to zero because $(1000/479-2)/(1000/479-1)=42/521>\delta$. If $X\ge p^3$, the right side divided by $p$ is $O((\ln p)^2p^{5.12\delta-1})$, which also tends to zero. All constants are independent of $t$ in the indicated range. This proves the theorem.

## Why the mismatch lower bound leaves legal words

Let $d=h-p$ and choose coprime slopes with $d/p\to\log_23-1$. For large $p$ let $I=\{1,\ldots,p-d-1\}$. Set $k_r$ to freely chosen bits on $I$ and zero elsewhere. Every rank in $I$ is reached by a wrapping edge ($b=2$) and leaves on a nonwrapping edge ($b=1$), since $p-d<d$. Hence the physical exponents $b_r+k_r-k_{r'}$ always belong to $\{1,2\}$, with $k_0=0$. For fair independent bits on $I$, the unwrapped pairs $r,r+t\in I$ have mismatch indicators of mean $1/2$ and are pairwise independent for a fixed $t>0$. Indeed two distinct pairs either are disjoint or share exactly one fair bit, and conditioning on that bit leaves their independent mismatches fair. There are $(1-d/p-o(1))p$ such pairs uniformly for the offsets of the theorem. Their variance is at most $p/4$. Chebyshev gives probability $O(1/p)$ that a particular offset has at most $p/83$ mismatches. The union bound over all stated offsets tends to zero. Consequently actual-edge legality as an inequality on the exponent word permits decorations passing *all* these tests. This is a symbolic construction. It imposes neither an ordinary fixed point nor the least-basin condition.

For an ordered cycle the full physical denominator still matters. In the notation of PR192, $D=2^h-3^p$, $u^p=2$ and $u^h=3$ modulo $D$; all of $D$ must divide $\sum_{r=0}^{p-1}c_r u^{p-1-r}$ when residues are represented by integers. The theorem excludes all stated low-mismatch decorations on an actual integer cycle. The first missing bounded-branch inference is an exclusion for the high-mismatch decorations with full divisibility and the least-disagreement condition. The separate first-crossing alternative can continue indefinitely or eventually enter a cycle outside this strip. No link from its exit to a smaller exceptional integer is proved here. Kevin Knight's exclusion applies to the physical Christoffel word. Arithmetic holonomy and effective two-variable $S$-unit equations do not provide a uniform exclusion for this variable-support polynomial. [Knight, Discrete Mathematics (2026)](https://doi.org/10.1016/j.disc.2025.114812) · [Calegari, Dimitrov and Tang, arithmetic holonomy and effective Diophantine approximation](https://arxiv.org/abs/2510.04156)

The lifted recurrence, common-word propagation, coprime product divisibility and small-difference inference are formalized in [RankGaps.lean](RankGaps.lean). The logarithmic rank estimate, multiplicity, Markov and entropy counts, and the joint asymptotic exclusion above are written proofs. The [finite control](check.py) checks both cuts on a denominator-cleared physical rational cycle, exact sparse-count constants and the centered decoding on synthetic data. It supplies no ordinary nontrivial cycle.

The finite control uses the five- and 41-odd-step rational cycles from the preceding packet and PR192. Both ordinary and optimized Python reproduced 1,660 rank-gap edges, 14,880 windows and 4,562 equal-word pairs with a nonzero difference. Fresh Lean 4.34.1 compilation with warnings as errors completed all six axiom queries. [Exact control output](../../../../reports/astra-global-closure-20261124/round10/arithmetic/control.json) · [Kernel output](../../../../reports/astra-global-closure-20261124/round10/arithmetic/lean.log)
