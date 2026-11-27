# Which factors and which words can absorb the cycle determinant?

**PROPOSED written results.** For a sufficiently large bounded least-tripling-disagreement cycle, canceling every factor matched by reversal leaves a nonreciprocal irreducible factor of degree at least a constant times the logarithm of the period. A root-angle inequality strengthens the bound to order $p/\ln p$ if all the remaining roots stay in a fixed sector away from the positive ray. On the larger, exactly identifiable population of positive rational cycles with the same period pair, ordered bands and physical height ceiling, the mean logarithm of the full cancellation agrees with that of a uniform residue to stretched-exponential error. This second result also treats rank polynomials that are themselves irreducible. A single exceptional integer cycle would suffice to defeat universal exclusion.

An exact 41-phase positive rational control combines an irreducible degree-40 rank polynomial absorbing 9,378,571 with all 1,681 one-lap inverse-window saving bounds on its fixed numerator lattice. All applicable central clock optima are attained. The reduced denominator is 44,835,377,399.

## Physical data and scope

Use the odd map $2^{a_j}x_{j+1}=3x_j+1$ on positive rationals of odd denominator, with the numerator odd in reduced form. Time is $j$; sorted dyadic rank is $r_j=jh\bmod p$. Take $\gcd(p,h)=1$, $D=2^h-3^p>1$, $B_j=\lfloor jh/p\rfloor$, $b_j=B_{j+1}-B_j$, and $\delta=h\ln2-p\ln3>0$. Assign $k_r\in\{0,1,2\}$ with $k_0=0$. Require $a_j=b_j+k_{r_j}-k_{r_{j+1}}\in\{1,2\}$ on every cyclic edge. The rank letter is $c_r=2^{2-k_r}$. The two orientations are $C(X)=\sum c_r X^r$ and $F=C^*=X^{p-1}C(1/X)$. For the unit $u^p=2,u^h=3\pmod D$ the least common denominator of the rational cycle is $D/\gcd(D,F(u))$. This uses the complete determinant, including multiplicities. [Round 9, rotation and denominator](../../round9/critical/README.md) · [Round 12, high-degree factor reduction](../../round12/cycle/README.md)

For all sufficiently large pairs in the bounded branch, $3/2\le h/p\le5/3$ and $0<\delta< (\ln2)/(2p)$ by the cited bounded-branch estimate. At such pairs the following additional restriction selects **exactly** the ordered, minimum-anchored rational cycles with these bands, valuations and upper bound $x_j\le(16s+7)/3$, $s=x_0$:

$$k_r\le1\quad\text{for }r\ge R=2p-h. \tag{1}$$

Here and below the exact-mask assertion is for sufficiently large $p$. Indeed the contracting affine lap has a unique positive rational fixed point, equal to its positive integer carry divided by $D$. Rotations of the formula give all sites the same odd denominator after reduction; their numerators are odd since their own rotated carry starts with $3^{p-1}$ and all remaining terms are even. Consequently $a_j$ is the actual valuation. Put $z_{r_j}=2^{-k_{r_j}}x_j$. Around any cyclic arc of $l\le p$ edges the difference

$$\ln(z_{r_{j+l}}/z_{r_j})-(r_{j+l}-r_j)(\ln2)/p$$

is the sum of $\ln(1+1/(3x_i))$ on the arc minus $l\delta/p$. The full sum is $\delta$, so the absolute difference is at most $\delta$. This proves strict rank ordering, $z_0=s$, $z_{p-1}<2s$, and hence true minimum and true dyadic bands. Odd sites are distinct: equal sites would repeat their forward valuations, giving a proper repetition of the length-$p$ word, contrary to $\gcd(p,h)=1$. Conversely the bounded ordinary branch supplies such an assignment by its rotation theorem. Since $x_j<8s$, $\delta\ge p/(24s+1)$ by $\ln(1+t)\ge t/(1+t)$. Consecutive sorted $z$ differ by at least $s((\ln2)/p-\delta)$, tending to infinity. At $R$, the edge to rank zero wraps and $a\le2$ forces $k_R=0$. Thus $z_R=(4s-1)/3$. Below $R$ even band two obeys the ceiling; above $R$, band two violates it once the rank gap exceeds $11/12$. Both lower bands always obey the ceiling. This proves (1).

The population in the distribution theorem gives equal weight to those finite decorations. Membership of the ordinary basin of 1, least-disagreement and optimal inverse-clock conditions impose further restrictions. No probability statement below conditions on these restrictions.

## A pointwise constraint on nonreciprocal factors

Let $E$ count the temporal edges on which $k$ changes. The actual ordinary bounded branch has $E>p/20$ for all sufficiently large $p$. The proof at the frozen prerequisite uses ternary decoding, the physical height bounds, and the entropy of the change mask. [Round 10, temporal shift](../../round10/arithmetic/EXTENDED_SHIFTS.md)

Write $d=h-p$ and $b(r)=1+\mathbf1_{r\ge p-d}$. The reflection $\tau r=p-1-r$ sends $r\to r+d$ to the **reversed** edge starting at $\tau(r+d)$. The latter has the same $b$, as is seen separately for $r<p-d$ and $r\ge p-d$. At $b=1$ the forward $c$ is nondecreasing and at $b=2$ it is nonincreasing. Hence $c_{\tau r}$ has the opposite monotonicity on the same edges. A changing edge must touch a mismatch between $c_r$ and $c_{\tau r}$, giving more than $p/40$ mismatched coefficients.

More generally, suppose $A C=B C^*$ for two nonzero polynomials with nonnegative real coefficients, degrees at most $m$, and $A(0)>0$. Reduce modulo $X^p-1$ to make the two coefficient convolutions cyclic. Subtract their values at $r$ from those at $r+d$. When $b(r-i)$ is constant for $0\le i\le m$, all terms on the left have the same weak sign, and all terms on the right have the opposite weak sign. Equality forces every left term to vanish, including $A(0)(c_{r+d}-c_r)$. There are at most $2m$ exceptional ranks, since the interval of length $m+1$ must cross one of two cut edges. For $m\ge p$ the bound is immediate. Thus

$$ E\le 2m. \tag{2}$$

For any reciprocal divisor $H$ with $H^*=H$ write $C=HQ$. If $Q$ has nonnegative coefficients (up to a scalar) take $A=Q^*, B=Q$; (2) gives $\deg Q>p/40$ at large ordinary candidates. A reciprocal divisor up to sign here has plus sign since no divisor vanishes at 1.

For a general $Q$ choose positive leading sign, so $Q$ has no positive real root and $Q(0)>0$. Write its real factorization into negative linear roots and conjugate pairs $\rho e^{\pm i\theta}$, $0<\theta<\pi$. Linear factors and pairs with $\theta\ge\pi/2$ already have nonnegative coefficients. For a smaller angle set $n=\lceil\pi/\theta\rceil$, $z=X/\rho$, and multiply $1-2z\cos\theta+z^2$ by

$$ V_\theta(z)=\sum_{i=0}^{n-2}\frac{\sin((i+1)\theta)}{\sin\theta}z^i.$$

The sine addition formula makes the product $1-z^{n-1}\sin(n\theta)/\sin\theta+z^n\sin((n-1)\theta)/\sin\theta$. Every coefficient of the multiplier and the product is nonnegative. Multiplying these multipliers gives $V\ge0$ coefficientwise and $QV\ge0$. The reciprocal multiplier $VV^*$ makes $A=Q^*VV^*$ and $B=QVV^*$ coefficientwise nonnegative and $AC=BC^*$. Their degree gives the explicit pointwise cost

$$\deg Q+2\!\sum_{\text{conjugate pairs of }Q,\,\theta<\pi/2}(\lceil\pi/\theta\rceil-2)>p/40. \tag{3}$$

Factor occurrences and root pairs count with multiplicity. Take $H$ to be the primitive gcd of $C,C^*$, up to scalar. Reversal preserves its multiset of roots, and it has no root at 1, so it is reciprocal. This removes both individually reciprocal irreducibles and all matched occurrences of a nonreciprocal irreducible and its reverse. If all roots of the remaining $Q$ have angle bounded away from the positive ray, their total degree is $\gg p$ with a constant depending only on the angle bound.

Even without a sector assumption **one unmatched nonreciprocal irreducible has degree $\gg\ln p$**. For a root $\alpha=r e^{i\theta}$ of $C$ with $r<1$ and $0<\theta<\pi$, subtract $C(\alpha)=0$ from $C(r)$ to get

$$1\le\theta\frac{\sum_j j c_j r^j}{C(r)}\le4\theta\frac{\sum_{j<p}j r^j}{\sum_{j<p} r^j}\le\frac{4\theta}{1-r}.$$

The last ratio is bounded by the infinite geometric mean $r/(1-r)$, since truncation drops only larger indices. For $r>1$, apply the same argument to the reciprocal root of $C^*$ using the absolute angle. All roots of $C,C^*$ have magnitude at most 5 by the elementary Cauchy bound. It follows, also at $r=1$, that $|1-\alpha|\le |1-r|+r\theta\le25\theta$. For an irreducible factor $G$ of degree $n$ containing that root, $1\le|G(1)|\le4\,|1-\alpha|\,6^{n-1}$ by the integer leading coefficient bound and the other roots' moduli. Thus $1/\theta\ll6^n$. Smyth's theorem gives a constant $M>1$ as a uniform lower bound on the Mahler measure of a monic irreducible nonreciprocal polynomial with nonzero constant term. Nonmonic primitive factors have measure at least two. Since $M(C)\le4\sqrt p$, at most $O(\ln p)$ unmatched irreducible occurrences exist. If $n_*$ is their largest degree then (3) gives $p\ll(\ln p)n_*6^{n_*}$, proving the claim. In the fixed-sector case $n_*\gg p/\ln p$. This argument does not identify the unmatched factor as the factor carrying the large determinant divisor. [Smyth, *On the product of the conjugates outside the unit circle of an algebraic integer* (1971)](https://doi.org/10.1112/blms/3.2.169)

## Full determinant and inverse-clock comparison

The [residue distribution proof](DISTRIBUTION.md) gives exponential scarcity of words with $\gcd(D,F(u))\ge D^\gamma$ for each fixed $\gamma>0$ and computes the expected logarithmic cancellation over the physical rational strip population. Its single-window test can erase $p-O(\ln p)$ exponents at full divisibility. The earlier polynomial height bound on the ordinary minimum already permitted a polynomial list of candidates. The new test instead separates **every residue fiber** modulo every divisor in arbitrary local contexts.

At $(p,h)=(41,65)$, an exact transfer count finds 233,702,141 masked words; split at time 20, matching the two partial sums modulo $9,378,571$ finds exactly 34 words divisible by this target. One has chronological physical word `12112121212211222212212121221122212211222`. The primitive part of $F$ is irreducible of degree 40, the full gcd is $19\cdot29\cdot17021$, and its minimum is $29340952507853/44835377399$. The replay verifies actual closure, the sorted ranks, the prescribed ceiling and absence of the forbidden reverse word. This finite instance is tested directly, independently of the asymptotic onset in (1).

PR192 compares ordinary inverse paths at every native window. For the control keep the denominator $d=44835377399$ fixed, so the reverse move from an odd numerator $y$ is $(2^e y-d)/3$ when positive and integral. For every one of the $41^2$ windows $(i,k)$ of lengths $1\le k\le41$, the native cost is $A$. At $i\ne0$ enumerate every inverse word through cost $A-2$: no word costs less than $A-2$, and none starting at a multiple of three costs at most $A-2$. At $i=0$ enumerate through $A+1$: the minimum is $A$, no multiple costs at most $A$, and for every $3\le k\le41$ the specific source $2S+d$, $S=29340952507853$, is a multiple attaining $A+1$. The recursion tries every exponent in the unique legal parity up to the remaining budget minus the number of still required edges. Multiples of three have no further predecessor; odd positive sources with unreduced numerator are allowed. This visits 5,735,790 recursion nodes. It establishes these window comparisons on the stated lattice. It neither gives complete lower-basin separation nor transfers the witness to $d=1$. [PR192, inverse clock theorem at 1f1d3d69](https://github.com/GettysburgResearch/collatz/blob/1f1d3d690d7517e1b2a44b5f2f4930bd45b63302/research/astra-diagonal-closure-20261125/cycle/README.md)

The first missing inference is a pointwise obstruction to full cancellation for the surviving ordinary, least-disagreement candidates, especially a high-degree nonreciprocal polynomial satisfying (3). An exceptional word can survive a small ensemble frequency. The separate first-crossing branch remains open.

[Arithmetic Lean kernels](RankCharacter.lean) · [Exact transfer and inverse-clock replay](check.py) · [Arithmetic output](../../../../reports/astra-global-closure-20261124/round13/cycle/control.json) · [Lean output](../../../../reports/astra-global-closure-20261124/round13/cycle/lean.log)
