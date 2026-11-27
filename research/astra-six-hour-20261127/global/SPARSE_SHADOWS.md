# Avoidance of thick and sparse ternary shadows on actual positive rays

**Written deduction from the Subspace Theorem.** Let \(a_i=U^i(a)\) be one escaping positive odd trajectory. For every fixed \(\delta>0\) and every positive integer \(J\), there are arbitrarily late blocks of \(J\) consecutive dates with each of the two following exclusion properties. The two properties can also be imposed together.

* For some \(\eta=\eta(\delta,J)>0\), at every date \(i\) in the block the distance from \(a_i\) to every **nonzero** multiple of \(3^{\lfloor\delta i\rfloor}\) exceeds \(\exp(\eta i)\). A subexponentially growing \(a_i\) can itself lie within this distance of zero.
* Fix \(D\ge1, K>0, 0\le\gamma<1\). At every such date \(i\), the class of \(a_i\) modulo \(3^{\lfloor\delta i\rfloor}\) has no representative of the form \(c_i=\sum_{j=1}^D\epsilon_j2^{m_j}\), where \(\epsilon_j\in\{-1,0,1\}\) and \(-\gamma i\le m_j\le Ki\). Negative binary exponents cause no ambiguity modulo a power of three. All signs, exponents and represented magnitudes may change at every date.

The exponential constant may depend on \(D,K,\gamma\) when both exclusions are imposed together. In either case, starting at any sufficiently large odd time \(n\), a block occurs by time \(C(n+1)\) for a constant depending on the fixed parameters and source. The first assertion alone has the sharper waiting bound below. This enlarges the family of rational obstructions excluded at the packet centers in [the fixed-width shadow theorem](../escape/RATIONAL_WINDOW_SHADOWS.md). It does not classify the sources of all possible short-interval passage failures.

## A valuation estimate with moving small coefficients

Fix a number of terms \(d\) and a constant \(K_0\). For sequences \(n\to\infty\), let \(X_j=h_j2^{m_j}\) with nonzero integers \(h_j\), \(\max_j\log(1+|h_j|)=o(n)\), and \(0\le m_j\le K_0n\). For every fixed rational linear form \(L\), along the indices where \(L(X)\ne0\),
\[
                     v_3(L(X))\le o(n).                                    \tag{1}
\]
Zero coefficients of the form can be removed. At infinity and 2 choose the coordinate forms, and at 3 use \(L\) in place of one coordinate with nonzero coefficient. The remaining forms there are coordinates. The product of the absolute values of the forms is at most
\[
             |L(X)|_3\prod_j |X_j|_\infty |X_j|_2
             \le |L(X)|_3\exp(o(n)).
\]
Dividing by the positive common gcd \(g\) to obtain a primitive integral vector cannot increase the product, because \(|g|_\infty|g|_2|g|_3\ge1\). The primitive height is at most \(\exp(O(n))\) and \(v_3(g)=o(n)\). If those heights stay bounded, there are only finitely many primitive vectors and (1) follows. Along an alleged subsequence with valuation \(\ge\delta_0n\) and unbounded heights, the product at the primitive vectors is bounded by a fixed negative power of their heights. The \(p\)-adic Subspace Theorem places them in finitely many proper rational subspaces. On an infinite subsequence in one subspace, substitute its fixed nonzero rational linear relation to eliminate one coordinate of \(L\). The resulting form on the other coordinates is nonzero along this subsequence and has the same values. Induct on the number of coordinates, beginning with the valuation of one small coefficient. This proves (1), including the possibility of vanishing proper subsums. A common power of two clears negative exponents of magnitude \(O(n)\) without changing valuations. [Schlickewei, real and p-adic linear forms](https://gdz.sub.uni-goettingen.de/download/pdf/PPN365956996_0018/PPN365956996_0018.pdf) · [Evertse, Theorem 1.1 with primitive integer vectors](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

A useful uniform consequence is that for each \(\delta_0,d,K_0\), and finitely many fixed forms, there exist \(\eta>0,N\) such that after \(n\ge N\), coefficients \(|h_j|\le\exp(\eta n)\) and exponents within those bounds give either exact zero or valuation less than \(\delta_0 n\). Otherwise choose a violating sequence with \(n\ge j\) and coefficient exponent \(1/j\), fix the offending form by a subsequence, and apply (1). The constants here are existential.

## Exact transport during a chain of near hits

Call a date bad if one of the chosen shadow types occurs. Choose a witness \(c_i\) at each bad date. For the first type \(c_i\) is the signed integer residual, \(|c_i|\le\exp(\eta i)\), and \(a_i-c_i\) is a nonzero multiple of \(3^{\lfloor\delta i\rfloor}\). For the second type use the displayed sparse dyadic representative. In both cases \(v_3(a_i-c_i)\ge\lfloor\delta i\rfloor\), including exact equality of the numbers. Consider two bad dates \(i<j\) with \(d=j-i\le J\). For \(0\le l\le d\) write \(S_l\) for the total physical divisions in the first \(l\) odd steps after \(i\). The word equation shows that
\[
       2^{S_d}c_j-3^d c_i-\sum_{l=0}^{d-1}3^{d-1-l}2^{S_l}
\]
is divisible by \(3^{\lfloor\delta i\rfloor}\) in \(\mathbb Z[1/2]\). Its expanded expression has a bounded number of terms with exponents of magnitude \(O(i)\), since \(2^{S_d}\le4^d a_i/a_j\) and \(a_i+1\le(3/2)^i(a+1)\). Its coefficients are bounded constants in the sparse case. The mixed and thick cases add at most two coefficients bounded by \(\exp(\eta(i+J))\) times fixed constants. Choose \(\eta\) sufficiently small in the uniform consequence of (1), also with \(\eta<\delta\log3/2\). Thus at all sufficiently late such pairs the expression is exactly zero. Subtracting it from the physical word equation gives
\[
               2^{S_d}(a_j-c_j)=3^d(a_i-c_i).                              \tag{2}
\]

On any late chain of consecutive bad dates with gaps at most \(J\), the differences are all zero or all nonzero. In the nonzero case telescope (2) from the first date \(i\) to the last date \(t\). Since the terminal difference has binary valuation at least \(-\gamma t\), this gives
\[
                 (1-\gamma)t-i\le v_2(a_i-c_i).
\]
The valuation on the right is \(O(i)\): the real absolute value of the nonzero dyadic rational is at most \(a_i+\exp(\eta i)+D2^{Ki}\), and its binary valuation is at most its real base-two logarithm. Thus such a chain cannot run past \(C(i+1)\). For the thick case alone write \(a_i-c_i=m_i3^{\lfloor\delta i\rfloor}\ne0\). Every sufficiently late such hit has \(|c_i|<3^{\lfloor\delta i\rfloor}/2\), hence \(|a_i-c_i|\le2a_i\). Integrality at \(t\) gives the sharper bound
\[
             t-i\le v_2(m_i)\le\log_2(2a_i)-\lfloor\delta i\rfloor\log_2 3.
\]
If no complete clean \(J\)-block appears after a late \(n\), its first and last marks are each within \(J\) of the ends. Bounding the first-mark height by \((3/2)^J(a_n+1)\) shows that a clean block finishes within
\[
        O_J(1)+\max\{0,\log_2(a_n+1)-\delta n\log_2 3\}
\]
steps in the thick case.

## Exact sparse simultaneous values are not syndetic

On an escaping trajectory the positive correction product \(F(a_i)=\prod_{j\ge i}3a_j/(3a_j+1)\) tends to one, by the uniform reciprocal sum over a simple positive orbit. The corrected heights \(P(x)=x/F(x)\) have \(P(a_i)=3^i2^{-S_i}P(a)\) for the elapsed binary clock \(S_i\). Thus on the circle
\[
       \log_2 a_i=\log_2 P(a)+i\log_2 3+o(1) \pmod1 .
\]
[Corrected-height transport and reciprocal input](../escape/GRADED_CORRECTION_SETS.md)

The normalized real mantissas of all positive \(D\)-sparse signed binary sums are contained in a compact countable set. Cancel equal opposite powers and carry equal like-signed powers until the remaining exponents are distinct, using at most \(D\) terms. If \(M\) is the largest exponent, it has positive sign and the entire sum is at least \(2^{M-D+1}\). Normalize into \([1,2)\) by a power of two. Each remaining exponent is at most \(D-1\); adjoining zero to the signed powers with exponents at most \(D-1\) gives a compact countable set, as does its \(D\)-fold sum. The circle of their base-two logarithmic mantissas lies in a compact null set \(K_D\).

The union of \(K_D-l\log_2 3\) for \(0\le l<J\) is still compact and null. Its complement contains an open interval with positive distance from that union. Irrational rotation by \(\log_2 3\) enters a smaller such interval with bounded gaps, uniformly in the starting point. The \(o(1)\) above shows that every sufficiently late interval of some fixed length includes \(J\) consecutive actual dates at which the state itself is not a signed \(D\)-sparse sum. A chain with differences identically zero consists solely of sparse shadows, since a thick witness has nonzero difference by definition. Such a chain therefore has bounded duration. Together with (2), this proves the simultaneous exclusion and timing claims.

The packet interpretation in the [source theorem](../escape/RATIONAL_WINDOW_SHADOWS.md) multiplies each real clearance by \((4/3)^i\). The new conclusion allows exponentially larger thick shadows and signed binary carries with boundedly many digits. It gives no upper bound on the adaptive Green function at dates whose targets have unbounded carry complexity.
