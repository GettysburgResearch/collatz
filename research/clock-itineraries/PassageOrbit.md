# Reduced denominators at successive times on one Collatz orbit

Start a positive integer $a$ and close each literal shortcut parity prefix into its own periodic word. In a window of length $L$ starting at time $N$, with $L^2$ sufficiently small compared with $N$, the reduced denominators at **all nonreturn times except at most one** are multiplicatively independent. This is an elementary, finite Lean theorem. A fixed-place application of Schlickewei’s Subspace Theorem removes the exceptional time for sufficiently late windows and allows deletion of any prescribed finite set of primes.

For an unbounded family of primitive positive integer cycles, start each at its minimum and let $P$ be its native period. Every proper cut $j=o(P)$ steps before return has reduced denominator $2^{P-o(P)}$ after deletion of any fixed finite prime set. At the penultimate cut the entire denominator is coprime to the raw determinant of the full lap. The full-lap reduced denominator is one.

## Exact arithmetic of a prefix

Write $x_t=T^t(a)$, $u_t$ for its odd departure count, $X=2^t$, $Y=3^{u_t}$, and $C_t$ for its nonnegative carry. The exact equation is $Xx_t=Ya+C_t$. For $t>0$ put $D_t=|X-Y|$. The periodicized affine fixed point is $C_t/(X-Y)$, of either sign. Its absolute reduced denominator is

$$
d_t=\frac{D_t}{\gcd(D_t,C_t)}
    =\frac{D_t}{\gcd(D_t,|x_t-a|)}.
$$

The equality follows from $C_t\equiv X(x_t-a)\pmod{D_t}$ and $\gcd(X,D_t)=1$. A return gives $d_t=1$. The interpretation of the fixed point for a periodic parity word is classical. [Lagarias, *The set of rational cycles for the 3x+1 problem*](https://doi.org/10.4064/aa-56-1-33-53) · [Native affine and carry identity](mathlib/PassageOrbitHeights.lean)

A common divisor of $D_t,D_{t+h}$ divides $|2^h-3^{u_{t+h}-u_t}|$, which is positive and at most $3^h$ for $h>0$. Cancel $2^t$ in the two clock congruences. Adjacent raw determinants are coprime because their gap determinant equals one on either branch. Every factor of $d_t$ exceeding $3^J$ fails to divide each other raw determinant within $J$ native steps. [Gap divisibility and private large factors](mathlib/PassageOrbitDenominator.lean)

## Two elementary window bounds

The triangle inequality and the integral gap determinant give $2^t\le D_{t+h}+3^hD_t$. Thus at most one $t\in[N,N+L)$ has $2\cdot3^L D_t<2^t$. The ordinary growth bound $2^t(x_t+1)\le3^t(a+1)$ bounds the gcd at every nonreturn. If $2(a+1)\le2^e$ and $3(1+e+2L+2L^2)\le N$, every remaining nonreturn denominator exceeds $(3^L)^L$.

For this family $f_i$, each pairwise gcd is at most $3^L$. Then $f_i$ exceeds the product of its gcds with the other terms. Some prime $p_i$ therefore satisfies $v_{p_i}(f_i)>\sum_{j\ne i}v_{p_i}(f_j)$. These primes are distinct. Given a nontrivial multiplicative relation, take its $p_i$-valuation at an index with maximal absolute exponent. Strict dominance gives a contradiction. [All nonreturns except one](mathlib/PassageOrbitAllTimes.lean) · [Prime witnesses and multiplicative independence](mathlib/PassageOrbitRank.lean)

If $a,N>0$, $16(a+1)\le2^e$ and $3(k+e+8m^2)\le N$, then
$$
\operatorname{lcm}_{N\le t<N+4m}d_t\ge2^{km}.
$$
For fixed $a$ this gives $\log\operatorname{lcm}\gg N^{3/2}$ in every such window of length $4\lfloor c\sqrt N\rfloor$ with sufficiently small fixed $c>0$. The proof finds one large nonreturn in every four steps and bounds the overlap with the accumulated LCM. [Sliding LCM theorem](mathlib/PassageOrbitLcm.lean)

## Fixed primes and exact returns

For finite $S$ let $n_{S^c}$ denote the factor of $n$ remaining after removal of all prime powers supported in $S$. For positive $t,u$, put $H=\max(2^t,3^u)$ and $D=|2^t-3^u|$. For every $\epsilon>0$,
$$
D_{S^c}>H^{1-\epsilon}
$$
apart from finitely many pairs. Use the primitive vector $(X,Y)=(2^t,3^u)$ and the places $S\cup\{2,3,\infty\}$. At $2,3$ use the coordinate forms. At every other finite place use $X-Y,Y$. At infinity use $X-Y$ and whichever of $X,Y$ is smaller, splitting into two fixed systems. All form pairs are independent. The product of their absolute values equals $D_{S^c}/H$. Schlickewei places the exceptions on finitely many proper rational lines. Each line contains at most one primitive positive vector. This argument gives no computed threshold. [Schlickewei, 1977](https://doi.org/10.1016/0022-314X(77)90073-7) · [Product formulation, Theorem 2.3](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

Every sufficiently late prefix of a fixed positive source has $u_t>0$. Taking $\epsilon=1/8$ gives the input for the following finite implication at a nonreturn,
$$
2^{7t}\le(D_t)_{S^c}^8
\quad\Longrightarrow\quad
2^t\le\bigl((a+1)(d_t)_{S^c}\bigr)^4 .
$$
Consequently, at all sufficiently late times, $d_t$ is supported on $S$ **if and only if $T^t(a)=a$**. For a periodic start of least period $P$ these times eventually coincide with the multiples of $P$. For a start which never returns there are only finitely many such times. The same equivalence holds for membership in any fixed finitely generated multiplicative subgroup of the positive rationals. Its generators involve finitely many primes and it contains one. The finite exceptional-line cover is an explicit hypothesis of the Lean bridge. [Prime removal and return equivalence](mathlib/PassageOrbitPlaces.lean)

Under the same finite-line input, all nonreturn denominators after deletion of $S$ are independent in every sufficiently late window with $4(1+e+2L^2)\le N$, where $a+1\le2^e$. Each has a distinct valuation witness outside $S$. Including every prime at most $3^J$ in $S$ ensures that all surviving primes of a nonreturn denominator occur in none of its neighboring raw determinants within $J$ steps. [All nonreturns after prime removal](mathlib/PassageOrbitOutsideRank.lean)

There is a cost even when the ordinary starting integer varies. Suppose $t\to\infty$, the literal prefix does not return, and $d_t$ is supported on fixed $S$. Then $d_t\le D_t/(D_t)_{S^c}=H^{o(1)}$. At a nonreturn $2^tg\le D_ta+C_t$, with $g=\gcd(D_t,C_t)\ge(D_t)_{S^c}$, and $C_t+2^t\le3^t$. Division by $g2^t$ gives $a d_t\ge(1-o(1))2^t$, since $C_t/(g2^t)\le(3/2)^t/2^{(1-o(1))t}\to0$. Hence $a\ge2^{t-o(t)}$. An all-even word satisfies this directly since $2^t\mid a$. Lean checks $2^t\le2a d_t$ for $t\ge4$ under the displayed eighth-power determinant estimate. [Native starting-height bound](mathlib/PassageOrbitHeightPrice.lean)

## A growing prime cutoff

There is an explicit version uniform in the initial integer. If $t\ge 2^{90}$ and $2^t>(a+1)^4$, then
$$
T^t(a)=a
\quad\Longleftrightarrow\quad
p\le\sqrt t/10000\ \text{for every prime }p\mid d_t.
$$
At a nonreturn the part of $d_t$ supported above this cutoff is at least $2^{t/4}/(a+1)$. For $t$ late relative to a fixed $a$ this forces a prime larger than $\sqrt t/10000$. Every such prime is absent from each other raw prefix determinant within $J$ steps whenever $3^J\le\sqrt t/10000$. [Native prime cutoff and neighborhood corollaries](mathlib/PassageOrbitMovingPlaces.lean)

Here are the numerical inputs for the written cutoff. Put $1\le u\le t$, $D=|2^t-3^u|$ and $y=\sqrt t/10000$. For $5\le p\le y$ prime, use the published two-logarithm valuation estimate with $\alpha_1=2,\alpha_2=3$, field degree one and $A_1=A_2=p$. The least common multiplicative-order parameter $g$ divides $p-1$. The normalized exponent is $b'=(t+u)/\log p$, so the first term in the theorem’s maximum is $\log(t+u)+0.4$. All terms are at most $10\log(2t)$. Therefore
$$
v_p(D)\log p\le2400\,\log^2(2t)\frac{p}{\log p}.
$$
Neither two nor three divides $D$. The function $p/\log p$ increases for $p\ge3$. The bound $\pi(y)<2y/\log y$ and $\log y\ge\log(2t)/3$ for $t\ge2^{90}$ give a total removed logarithm at most $43200y^2=0.000432t$. [Bennett and Bugeaud, Theorem 2.1](https://personal.math.ubc.ca/~bennett/BeBu.pdf) · [Rosser and Schoenfeld, equation (3.6)](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf)

With $H=\max(2^t,3^u)$ and $z=|t\log2-u\log3|$, Lagarias gives $z\ge(\log3)/(1200t^{13.3})$. Since $D/H=1-e^{-z}\ge\min(1,z)/2$, we have $\log D\ge\log H-13.3\log t-8$. At the stated cutoff $13.3\log t+8\le t/100$, for example by $\log t\le\sqrt t$. Subtracting the small-prime contribution leaves more than $(7/8)t\log2$. In an ordinary word the height assumption gives $u_t>0$, because an all-even prefix requires $2^t\mid a$. This proves the input to the exact return test. The logarithm theorems and prime-counting estimate are published inputs. Lean checks the valuation sum from the stated local bounds, the logarithmic conversion to the eighth-power inequality, and the ordinary return test. [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006) · [Finite analytic and ordinary bridges](mathlib/PassageOrbitMovingPlaces.lean)

For the smaller cutoff $y=\sqrt t/\log t$, the removed logarithm is $O(t/\log^2t)=o(t)$, so the rough determinant has logarithm $\log H-o(t)$. In the near-lap result below one may take the common cutoff $y=\sqrt P/\log P$ and $J=\lfloor\log_3 y\rfloor$. For all $1\le j\le J$ the surviving parts of $d_{P-j}$ each have size $2^{P-o(P)}$, uniformly in $j$. They have pairwise disjoint prime supports, all disjoint from the entire full-lap determinant. Their product has base-two logarithm $(1+o(1))PJ$. This follows because $t=P-j$ is uniformly comparable to $P$ in the valuation sum and $3^J\le y$. [Common-divisor bound](mathlib/PassageOrbitDenominator.lean)

## Cuts before a primitive cycle returns

At the minimum $m$ of a positive integer cycle of period $P$ the finite path satisfies $(3m+1)D_P\le P2^P$. Propagate $(3m+1)C_t\le t2^t x_t$ using $x_t\ge m$, then cancel $m$ at the return. The complete multiplier is less than one, so $H_P=2^P$. The fixed-place estimate with $S$ empty gives $\log m=o(P)$ uniformly along unbounded primitive periods. At a positive proper cut $t=P-j$, reversing $j$ native steps gives $x_t\le2^jm$. Hence
$$
(D_t)_{S^c}\le2^jm(d_t)_{S^c}.
$$
Uniformly for $t\ge\eta P$ and fixed $\eta>0$ this gives $\log_2((d_{P-j})_{S^c})\ge P-2j-o(P)$. For $j=o(P)$ one gets equality with $P-o(P)$ because $D_t\le2^P$. Deleting all primes of the full-lap determinant preserves this estimate at $j=1$ by adjacent coprimality. For each fixed $J$, deleting the primes at most $3^J$ leaves $2^{P-o(P)}$ in each of the last $J$ proper cuts, on pairwise disjoint prime supports also disjoint from the full-lap determinant. [Finite minimum and near-lap inequalities](mathlib/PassageOrbitCycles.lean)

The written argument extends to primitive positive rational cycles of complete denominator $b=\exp(o(P))$. The real minimum $m$ satisfies the same bound by $1-\prod_i(1-z_i)\le\sum_i z_i$, where $z_i=1/(3x_i+1)$ at odd phases. Its numerator $bm$ is subexponential. Keeping denominator $b$ in all states gives $2^t n_t=3^{u_t}n_0+bC_t$. The gcd $\gcd(D_t,C_t)$ divides $|n_t-n_0|$, and $n_t\le2^j n_0$ at the cut. These inequalities give the same conclusion. The explicitly constructed small-complete-denominator rational cycles in PR 212 thus admit exponentially large near-lap denominators. [Finite rational cancellation](mathlib/PassageOrbitCycles.lean) · [PR 212 independent clocks](https://github.com/GettysburgResearch/collatz/blob/8cac31f5/research/astra-infinite-descent-20261127/cycles/INDEPENDENT_CLOCKS.md)

## A restriction on covers by proper arcs

Suppose the maximum native state on a primitive positive integer cycle of period $P$ is polynomial in $P$. At **every phase**, every proper arc of length $L\ge2^{90}$ with $2^L>(1+\max x_i)^4$ has a prime larger than $\sqrt L/10000$ in the reduced denominator of its own periodicized word. Indeed the arc cannot return before the least period, so the moving-cutoff theorem applies at its actual starting integer.

This condition covers, in particular, every family with physical width bounded by a fixed power of $P$. Lagarias gives $D_P/2^P\ge(\log3)/(2400P^{13.3})$, so the minimum inequality above bounds $m=O(P^{14.3})$. A bound on the odd heights also controls the intervening native heights, since even steps decrease and an odd shortcut step increases the value to at most $(3\max x_{\rm odd}+1)/2$. Thus the narrow physical bands in PRs 200 and 213 satisfy the stated polynomial-height condition.

In fact, along such a family, **every proper arc of length $L$ with $L/\log P\to\infty$** satisfies $\log_2((d_{\rm arc})_{p>\sqrt L/\log L})=L+o(L)$, uniformly in its starting phase. The reduction gcd is at most the absolute difference of its endpoints, hence at most a polynomial in $P$, while the preceding valuation sum leaves $\log H-o(L)$ in the raw determinant. Finally $3^u/2^L\le x_{\rm end}/x_{\rm start}\le\operatorname{poly}(P)$ by the affine identity, so $\log_2 H=L+O(\log P)$. [Finite arc cancellation](mathlib/PassageOrbitCycles.lean) · [Valuation sum](mathlib/PassageOrbitMovingPlaces.lean)

If such a cycle is partitioned into $r\ge2$ proper arcs, and the denominator of each arc of length $L$ is supported on primes at most $\sqrt L/10000$, then $r\gg P/\log P$ along increasing periods. Each arc has length at most $\max(2^{90},4\log_2(1+\max x_i)+1)$, and their lengths sum to $P$. The same asymptotic holds for any fixed prime support, enlarging the constant cutoff on the arc lengths to absorb those finitely many primes. The centers can have either sign and arbitrary numerator height. The finite partition implication uses actual phases of a primitive native cycle. [Native proper-arc and partition bounds](mathlib/PassageOrbitMovingPlaces.lean)

Even without a width bound, a partition rooted at the minimum into proper arcs with all centers supported in the same finite prime set requires at least $(1/\log(\log_2 3)-o(1))\log P$ arcs. Here “supported” concerns the centers’ denominators. For any fixed $\epsilon>0$, the varying-source bound above gives $L\le(1+\epsilon)\log_2(x+1)+O_{S,\epsilon}(1)$ at the entrance $x$ of each such arc. After $i$ native steps from $m$ we have $x+1\le(3/2)^i(m+1)$. The next boundary index is therefore at most $[1+(1+\epsilon)\log_2(3/2)]i+O_{S,\epsilon}(\log P)$. Iterating from index zero to $P$ and then letting $\epsilon$ decrease to zero gives the claim. The rooted condition is needed in this last argument.

## Comparison with complete-cycle restrictions

PR 212 defines the same center of a proper arc. Its effective theorem bounds the maximum Weil height of centers in a full arc partition, and its moving-arc theorem bounds the complete lap denominator when every center in a bounded cover has subexponential Weil height. Here the near-lap estimate gives the prime-to-$S$ part of the reduced denominator at every specified proper cut near a minimum-rooted return. [PR 212 arc heights](https://github.com/GettysburgResearch/collatz/blob/8cac31f5/research/astra-infinite-descent-20261127/cycles/ARC_HEIGHT.md) · [PR 212 moving arcs](https://github.com/GettysburgResearch/collatz/blob/8cac31f5/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md)

PR 200’s width restriction concerns a full rational cycle. PR 201’s Pell restriction concerns adjacent state products, and PR 211 counts discrepancies between rotations of one complete lap. PR 201’s critical-pair transport concerns rational source populations, and PR 193’s ancestor law concerns weighted preimages of fixed targets. These results supply no fixed prime support or upper rank bound for the moving prefix denominators of an arbitrary ordinary source. [PR 200 width certificate](https://github.com/GettysburgResearch/collatz/blob/eb91086951b66923787f696801f0c3ca52a0077d/research/six-hour-20261127/cycles/FIFTH_POSITIVE_CERTIFICATE.md) · [PR 201 Pell packing](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/arithmetic/FULL_DENOMINATOR_PELL.md) · [PR 211 all shifts](https://github.com/GettysburgResearch/collatz/blob/5c67ddfcc9a376cb6f6dde0a0d05c74d7b9ae3ee/research/astra-reciprocal-rigidity-20261127/cycles/ALL_SHIFT.md) · [PR 201 critical pairs](https://github.com/GettysburgResearch/collatz/blob/dac732467c6ed5307d1b78eaa8534653aeeb7a4c/research/infinity-20261127/mass/CRITICAL_PAIRED_TRANSLATION.md) · [PR 193 ancestor law](https://github.com/GettysburgResearch/collatz/blob/98d56bd8/research/astra-diagonal-20261127/escape/ORDINARY_ANCESTOR_EQUILIBRIUM.md)

PR 213’s simultaneous cuts vary an interval of *state heights* for one complete ordinary cycle of width less than eight. The induced rotation is constant and its reduced clock has coprime numerator and denominator. Its polynomial-rank theorem uses a two-child ternary past for binary odd exponents. Neither bounds the arithmetic denominators of the individual temporal prefixes studied here. [PR 213 rotation cuts](https://github.com/GettysburgResearch/collatz/blob/de6384b4/research/astra-diagonal-frontier-20261127/arithmetic/ROTATION_CUTS.md) · [PR 213 polynomial rank](https://github.com/GettysburgResearch/collatz/blob/de6384b4/research/astra-diagonal-frontier-20261127/arithmetic/POLYNOMIAL_RANK.md)

At $a=1$, the exact control is $d_{2j}=1$ for $j>0$ and $d_{2j+1}=|2\cdot4^j-3^{j+1}|$. The sole accelerated adjacent product is one, with auxiliary Pell discriminant three, and all translated complete-lap balances hold. Its odd-time denominators still have unbounded local multiplicative rank. An escaping orbit can likewise introduce arbitrarily many primes. Deducing a return this way would require forcing infinitely many fixed-support prefix denominators on a putative escaping source or obtaining a separate obstruction to unbounded support. Neither implication has been established. [Native known-cycle control](mathlib/PassageOrbitHeightPrice.lean)
