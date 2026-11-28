# Moving rational residues and proper physical arc cancellations

**Proposed, source-qualified written theorems.** A short two-three monomial cannot have an accidentally small rational residue modulo an exponentially large divisor of the full physical determinant, along any unbounded sequence of clocks. This uses the moving-target gcd theorem of Grieve and Wang. At the full modulus the rational representative must differ by an integral number of complete formal laps. On partial determinants the allowed sublap is specified by an exact multiplicative order. On an actual closed orbit, it follows that every proper arc containing some and missing some odd steps has subexponential common divisor with the full determinant when both of its cleared endpoints have subexponential height. There is no restriction on the common divisor of period and weight.

## A moving rational target

For a nonzero rational $r=P/Q$ in lowest terms with $Q>0$, write $h(r)=\log\max(|P|,Q)$. Take positive clocks $n\to\infty$, $0<u<n$, raw determinant $D=2^n-3^u>0$, and divisors $M\mid D$ with $\log M\ge\eta n$ for a fixed $\eta>0$. Set $g=\gcd(n,u)$, $N=n/g$, $U=u/g$, $X=2^n3^{-u}$ and $t=2^N3^{-U}$. Let $Y=2^a3^b$ with $|a|+|b|=O(n)$. Suppose $r>0$, $h(r)=o(n)$, both its numerator and denominator are units modulo $M$, and
$$                            Y\equiv r\pmod M.                      \tag{1}$$
Then, eventually along every such sequence,
$$              r\in\langle2,3\rangle,\qquad
                Y/r=t^j,\qquad \operatorname{ord}_M(t)\mid j         \tag{2}$$
for some integer $j$. At $M=D$ the order is exactly $g$, so $Y/r=X^k$ for an integer $k$. At $M<D$ the order can be smaller. For example with $g>1$ the principal factor $M=2^N-3^U$ has $t=1\bmod M$, even at parameters where $M$ is exponential in $n$.

**Proof using moving targets.** Suppose that infinitely many inputs violate (2) and restrict to them. In Grieve–Wang Theorem 1.2 use the field $\mathbb Q$, $S=\{\infty,2,3\}$, the two genuine $S$-units $X,Y$, and the moving polynomials
$$                           f(Z,W)=Z-1,\qquad g_r(Z,W)=W-r. $$
They are coprime, of degree one, and have nonzero constant terms. The moving coefficient height is $h(r)=o(n)$. The maximum height of the arguments is between $n\log 2$ and $C n$ for some fixed $C$. At primes dividing $M$, both evaluations vanish modulo the entire corresponding prime power, with invertible denominators. Thus the all-place logarithmic gcd used by the theorem is at least $\log M$. Choose $\epsilon<\eta/C$. Its small-gcd alternative cannot hold on an infinite subsequence.

The other alternative puts the two $S$-units in small-height translates of a finite union of proper algebraic subgroups. In particular after passing to an infinite subsequence there is a fixed character $(s,v)\ne(0,0)$ with
$$                              h(X^sY^v)=o(n).                      \tag{3}$$
The character corollary follows by taking any nontrivial character annihilating each fixed subgroup (taking a multiple for a disconnected subgroup). Evaluating that character on the small-height translating point has height $o(n)$. The proof of Theorem 3.1 in the same paper obtains precisely a small-height quotient of two distinct monomials. This avoids any convention about how a translate is represented. The case $v=0$ contradicts $h(X)=n\log2$. Now $X^sY^v\equiv r^v\bmod M$ by (1). Both rationals here have height $o(n)$ and are units at the primes of $M$. Clearing their two denominators produces a difference of integers of size at most $2\exp(o(n))$, divisible by $M\ge\exp(\eta n)$. Hence the two rationals are equal. Consequently $r^v$ is a two-three unit; positivity and rationality imply that $r$ itself is a two-three unit. Applying the valuations at two and three to $X^s(Y/r)^v=1$ shows that the exponent vector of $Y/r$ is an integral multiple of $(N,-U)$. Congruence (1) gives the order condition. This contradicts the selected infinite family of counterexamples and proves the assertion with its eventual quantifier. [Grieve–Wang, Theorem 1.2, author manuscript](https://arxiv.org/pdf/1902.09109) · [Published article](https://doi.org/10.1090/tran/8220)

## Proper physical arcs

Let a primitive positive rational cycle have displayed physical numerator states $A_i$ and common reduced denominator $d$, with actual updates
$$                    2A_{i+1}=3^{b_i}A_i+b_i d,\qquad b_i=A_i\bmod2. $$
Here $d$ is coprime to six since it divides $D$. In a mixed cycle all $A_i$ are coprime to three: an odd step gives $2A_{i+1}\equiv d\bmod3$, and every subsequent even step preserves nondivisibility until another odd step. For a forward arc $I$ from $i$ to $j$ of $L$ steps and $v$ odd steps, let $C_I$ be that arc's native affine numerator:
$$                    2^L A_j=3^v A_i+d C_I.                        \tag{4}$$
The determinant in the following gcd is the **full** $D$, even though $C_I$ is the numerator of a proper arc.

If $0<v<u$ and $\log\max(A_i,A_j)=o(n)$, then uniformly in this sequential sense,
$$                          \log\gcd(D,C_I)=o(n).                    \tag{5}$$
Suppose otherwise and pass to a sequence where $M=\gcd(D,C_I)\ge\exp(\eta n)$. Write $c_0=\gcd(A_i,A_j)$. Then
$$ M'=M/\gcd(M,c_0) \quad\text{divides}\quad
         2^L(A_j/c_0)-3^v(A_i/c_0). $$
This follows from (4) and integer divisibility, even with prime-power overlap. The loss $\log\gcd(M,c_0)=o(n)$ is harmless. Each prime of $M'$ is coprime to both reduced endpoints, since it divides neither two nor three and divisibility of one endpoint would imply divisibility of both. Therefore (1) applies modulo $M'$ to $Y=2^L3^{-v}$ and $r=A_i/A_j$. It forces $r$ to be a two-three unit. Since both numerators are three-units, $r$ is a pure power of two. Thus the two endpoints have one odd core, obtained by dividing out their full powers of two.

Distinct states in a least-period cycle with the same odd core belong to the same contiguous chain of even halvings. Indeed if $A_i=2^e A_j$, $e>0$, the next $e$ transitions from $i$ are forced halvings terminating at $j$. The chain cannot contain an entire mixed lap. Therefore exactly one of the two cyclic arcs between them is all even, and the complementary arc contains all $u$ odd departures. Equal numerators mean equal phases by primitivity. This contradicts $0<v<u$, proving (5). No approximation of a residue ratio with a nonunit denominator has been used.

For a proper partition of the cycle into two arcs, the native numerators of the two arcs have equal gcd with $D$ whenever the full affine numerator vanishes modulo $D$. This follows by expanding the full numerator as the sum of the two arc numerators times powers of two and three, and then using that both coefficients are units. Under (5) this common gcd is subexponential. An isolated full cancellation is consistent with all its proper subsums having tiny gcd.

**Guaranteed domain on ordinary cycles.** A hypothetical sequence of distinct ordinary cycles has minimum $m=n^{O(1)}$ by the [external two-logarithm bound](../CONTRACTING_CALENDARS.md). Within $w(n)=o(n)$ forward or backward clocks of the minimum all states have logarithmic height $o(n)$. Forward use $x_{k+\ell}+1\le(3/2)^\ell(x_k+1)$ and backward use $x_{k-\ell}\le2^\ell x_k$. Thus (5) applies to all pairs in that two-sided growing neighborhood, and to either oriented arc that has between one and $u-1$ odd steps. More generally it applies to any other subexponential-height endpoints. No uniform subexponential bound on the maximum is assumed, and the statement does not prove that some proper subsum must share an exponentially large divisor with $D$.

## Complementary affine ratios on an ordinary cycle

For the same pair of subexponential-height endpoints on a primitive ordinary cycle, write $I,J$ for the complementary arcs of lengths $L,n-L$ and odd counts $v,u-v$, both positive. Then
$$            \log\gcd(C_I,C_J)=o(n),\qquad
 h(C_I/C_J)=\max(L,n-L)\log2+o(n).                                  \tag{6}$$
Indeed $c=\gcd(C_I,C_J)$ divides both rotated full numerators $D A_i,D A_j$ by the two affine composition formulas. Hence $c\mid D\gcd(A_i,A_j)$ and $c\le\gcd(D,C_I)\gcd(A_i,A_j)=\exp(o(n))$ by (5). For the size, $C_I\le 2^L A_j$ by (4) and $C_I\ge3^{v-1}$ by its first odd summand. The telescoped ordinary logarithmic identity gives
$$ L\log2-v\log3=\log(A_i/A_j)+\sum_{k\in I,\ b_k=1}\log(1+1/(3A_k)).
$$
The sum is nonnegative and no larger than the full-lap value $n\log2-u\log3=o(n)$. For this last bound, along any sequence of distinct ordinary cycles the minimum tends to infinity since cycles are disjoint, and the full sum is at most $u/(3\min A)$. The endpoint logarithm is $o(n)$ by hypothesis. Thus $\log C_I=L\log2+o(n)$, and the same bounds hold on $J$. Reducing the ratio proves (6).

[SimpleArc.lean](SimpleArc.lean) checks that the actual numerator shortcut recursively takes every available forced halving and that simple complementary physical arcs, each containing an odd departure, exclude either orientation of a dyadic endpoint ratio. The moving-target, prime-power gcd, logarithmic, and asymptotic parts above are written mathematics.
