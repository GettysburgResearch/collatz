# Integer gaps between adjacent odd phases in sorted dyadic order

**PROPOSED theorem with a Lean-checked arithmetic proof.** Let a primitive positive accelerated cycle have odd period $p$, shortcut period $h$, minimum $s$, and reduced common denominator $d$. Suppose its odd phases lie in $[s,8s)$ and have the ordered dyadic rotation described below. The ordinary bounded alternative of PR205 meets these hypotheses. Write $B$ for the number of changes in octave among adjacent *sorted* phases, counting the doubled seam. For every integer $k\ge0$,

$$
       3^k\max(p-kB,0)\ \le\ 4ds.                                      \tag{1}
$$

The reduced denominator of such an ordered rational cycle grows exponentially with $p$ if $B$ stays bounded. Every sufficiently long ordinary cycle in the bounded alternative needs $B\gg p/\log p$. A construction below gives positive rational cycles with both rotation orders, a positive fraction of high record phases and $B$ proportional to $p$. Unrestricted ordinary cycle exclusion and the escape alternative remain **OPEN**. [Construction](RATIONAL_ORDERS.md)

## Ordered phases and the complete denominator

Use the odd map $U(x)=(3x+1)/2^a$ with its exact positive valuation $a$. For rational phases assume a denominator prime to six and use the same valuation. Around a positive lap, $D=2^h-3^p>0$. For the carry $C$ in the affine lap equation $Dx=C$, the reduced denominator is $d=D/\gcd(D,C)$. Every phase has this same denominator. Multiplication by three, addition of one and division by the exact dyadic valuation preserve it since it is prime to six.

Write each odd phase as $x=2^j t$, with $s\le t<2s$ and $j\in\{0,1,2\}$. Sort the $p$ mantissas $t_r$ and put $z_r=4dt_r$, $c_r=2^{2-j_r}$. Extend to all nonnegative ranks by $z_{r+p}=2z_r$ and $c_{r+p}=2c_r$. The required rank recurrence is

$$
                   z_{r+h}=3z_r+d c_r .
$$

For the ordinary bounded cycle this follows from cyclic order of raw images $3t+2^{-j}$. The quarter-unit spacing prevents reversals, and a tie contradicts injectivity of the successor on a cycle. At the top of the octave the raw image is strictly below twice the first raw image. The permutation is consequently a rotation. Its lifted displacement equals $h$, since the dyadic carries telescope to the sum of the valuations. At the minimum $t_0=s$ and $c_0=4$. For rational cycles the ordering is an explicit hypothesis. The finer rational lattice alone gives no quarter-unit spacing. [Frozen ordered-cycle argument, PR192](https://github.com/GettysburgResearch/collatz/blob/a0d7c6e36c378bbb6c826002039aef486bbe0383/research/astra-universal-closure-20261124/cycle/README.md)

Define $B=|\{0\le r<p:c_{r+1}\ne c_r\}|$, where $c_p=2c_0=8$ counts the seam. Set $G_r=z_{r+1}-z_r$ on this same range. All $G_r$ are positive integers and their sum is $z_0=4ds$. Subtract the two adjacent lifted equations. For $v=(r+h)\bmod p$ and $a=\lfloor(r+h)/p\rfloor$ this gives

$$
                  2^a G_v=3G_r+d(c_{r+1}-c_r).                         \tag{2}
$$

The formula includes an image crossing the seam, because $G_{p-1}=2z_0-z_{p-1}$. At a rank where the two corrections agree, a factor of three passes to the successor gap. After $k$ such departures the terminal gap is divisible by $3^k$, since every power of two is coprime to three. Among the $p$ terminal gaps, at most $kB$ have a changed correction in those last $k$ departures. The remaining gaps are positive multiples of $3^k$. Summing them gives (1). The Lean file accepts the increasing lifted list and its affine rank recurrence, derives the gap equations including the seam, proves the finite counting statement, and telescopes the gaps. [RankGaps.lean](RankGaps.lean)

Take $k=\lceil p/B\rceil-1$, so $p-kB\ge1$. Then $4ds\ge3^{\lceil p/B\rceil-1}$. The exact cycle identity

$$
 0<h\log2-p\log3=\sum_x\log(1+1/(3x))\le p/(3s)
$$

and $h\le 2p$ in the exceptional branch give $s=O_\epsilon(p^{5.1163051+\epsilon})$. This uses Wu and Wang's Theorem 1 with integer coefficient triple $(0,h,-p)$ and height $\max(h,p)$. The same proof holds for rational cycles with $s\ge1$, since every factor $3+1/x\le4$. When $s<1$, the polynomial upper bound for $s$ holds trivially. Thus bounded $B$ forces exponential growth of $d$, and $B=o(p/\log p)$ forces $d$ to grow faster than every fixed power of $p$. On an ordinary lap, $d=1$ forces $B\gg p/\log p$. [Wu and Wang, *On the irrationality measure of log 3*, Theorem 1](https://doi.org/10.1016/j.jnt.2014.03.007)

## Location of the changes on the exceptional orbit

Start at the minimum $s$ of the PR200 ordinary strip and follow at most one lap. Let $A_i$ be the total valuation of the first $i$ odd steps, $r_i=ih\bmod p$ the current sorted rank, and $j_i$ its octave. Summing the exact lifted octave carries gives $j_i=\lfloor ih/p\rfloor-A_i$. Subtracting the lap average from the accumulated logarithmic corrections gives

$$
 \left|\log(t_{r_i}/s)-(r_i/p)\log2\right|\le p/(3s).
$$

Each correction and its lap mean belong to $[0,1/(3s)]$. The period estimate $p=O(s^{479/1000})$ implies $p^2/s\to0$ as $s\to\infty$. Uniformly in sorted rank, $t_r=s2^{r/p}+O(p)$. This holds at $r=p$ by exact equality. Every adjacent gap is consequently $O(s/p+p)=O(s/p)$ for $d=1$. If $k$ consecutive rank-rotation steps see equal adjacent corrections throughout, (2) forces the terminal positive gap to be at least $3^k$. Thus every such stretch, wherever it occurs on the actual cycle, satisfies $k\le\log_3(s/p)+O(1)$. This analytic consequence is a written proof. [PR200, Theorem S](https://github.com/GettysburgResearch/collatz/blob/81ea4c1754d73c98d1451447527e6b2ba56977cc/research/regularity-rigidity-20261124/minimum-closure/MINIMUM_CLOSURE.md)

## Test against simultaneous high phases and companion records

On the 41-odd-step rational cycle from PR192 the exact results are $p=41$, $h=65$, $B=7$, and seven odd phases exceed $2s$. At physical clocks, 30 phases exceed $2s$. All nine strict record phases for the PR193 threshold $\rho=3/5$ belong to those 30. The record test is exact at all past lengths. Increments are $5e-3$, where $e$ is the physical odd indicator, and the sum over one lap is $5p-3h=10>0$. Strict positivity on every suffix of lengths 1 through 65 therefore suffices.

For this cycle the left sides of (1) for $k=0,\ldots,6$ are $41,102,243,540,1053,1458,0$, and all later values are zero. Even replacing $d$ by 1 in (1) passes every test since $1458<4s$. The exact reduced denominator is $22131145802542991$. This check shows coexistence of the observed high occupation, synchronized records and inequality (1) with failure of full divisibility. It does not model every ordinary basin condition or give an unbounded family attaining the PR200 approximation exponent. [Exact arithmetic replay](check.py) · [PR193, synchronized records](https://github.com/GettysburgResearch/collatz/blob/24cdd0e5471d4421716cfce6bd88916f858f994c/research/astra-universal-proof-20261124/critical/COMPANION_SYNCHRONIZATION.md)

The unresolved case permits many changes in the sorted octave assignments and a reduced denominator equal to one. The synchronized record theorem constrains pasts using the companion denominator. An inequality ruling out $D\mid C$ for these remaining physical words is missing. PR206's exact-clock criterion and PR207's superdiffusive estimate also allow a sparse population of literal rows at an exceptional fixed root. The argument above uses a closed lap and gives no descent from an escaping least bad source. [PR206, cycle amplification](https://github.com/GettysburgResearch/collatz/blob/b2b56b94175174a680a296478f16c619a8828972/research/clock-itineraries/CycleAmplification.md) · [PR207, near-diagonal bounds](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/NEAR_DIAGONAL.md)
