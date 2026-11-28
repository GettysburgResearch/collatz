# Which shorter denominators can a thin physical cycle erase?

Let \(D_k(n)=2^{kn}-3^k\). A primitive positive rational word with one odd departure in each of \(p\) successive aligned \(n\)-date blocks has \(L=pn\) and complete denominator \(q\mid D_p(n)\). We give an exact positive construction and a complementary obstruction.

**Proposed erasure theorem.** For **every** \(n\ge4\) and \(m\ge1\) there is such a primitive word with \(p=m(n-1)\) and
\[
       q\mid \frac{D_p(n)}{D_m(n)},\qquad
             \gcd(q,D_m(n))\mid n-1,\qquad
       \log_2 q\ge pn-(2m-1)n-O(1).                                    \tag{1}
\]
The absolute constant is independent of \(m,n\). At \(m=1\) the complete denominator is exactly \(D_{n-1}(n)/D_1(n)\).

Take \(m=\operatorname{lcm}(1,\dots,R)\) with \(R\to\infty,\ R=o(n)\). Then \(\log p=o(n)\), since \(\log\operatorname{lcm}(1,\dots,R)=O(R)\), and
\[
             \gcd(q,D_k(n))\mid n-1\quad(1\le k\le R),\qquad
                                \log_2 q/L\to1 .                        \tag{2}
\]
The actual denominator thus keeps the full exponential rate while intersecting every one of these shorter raw clock factors only in a divisor of \(n-1\). Comparing multiplicative orders through their common factors can lose all exponential information. Whether the resulting \(q\) has small multiplicative order of three remains open.

## A physical word with an exact polynomial identity

Write \(X=2^n\) and \(t=n-1\). The binary one-positions of \(X-3\) are
\[
             b_0=0,\qquad b_i=i+1\quad(1\le i<t).
\]
In the blocks numbered \(mi+r\), \(0\le i<t,\,0\le r<m\), place the sole odd date at \((mi+r)n+b_i\). The last-to-first cyclic gap is one, and all other gaps are at least \(n\); the unique unit gap proves primitivity. The usual parity-word fixed point is positive since \(X>3\) and its reduced denominator is odd and prime to three.

Let
\[
 S_m=\frac{X^m-3^m}{X-3},\quad U=(X/3)^m,\quad
 P(U)=1+2\sum_{i=1}^{t-1}(2U)^i,\quad
                         B=3^{m(t-1)}P(U).
\]
The true full carry equals \(S_m B\): the \(m\) equal translates in each consecutive group give the first factor. Its raw denominator is \(D_p(n)=X^{mt}-3^{mt}\). In reduction modulo \(X-3\) the units at three give \(B\equiv3^{m(t-1)}P(1)=3^{m(t-1)}(X-3)\). Thus \(D_m(n)=(X-3)S_m\) divides the carry, proving the first divisibility in (1). Modulo \(D_m(n)\) the integer geometric quotient \(D_p(n)/D_m(n)\) reduces to \(t3^{m(t-1)}\). Both two and three are units, so its gcd with \(D_m(n)\) is \(\gcd(t,D_m(n))\). This proves the second claim of (1) and all the divisibilities in (2).

For the lower size bound set \(H=\gcd(D_p(n)/S_m,B)\). This positive integer is prime to six and the complete denominator is \(D_p(n)/(S_m H)\). In its residue ring \(U^t=1\) and \(P(U)=0\). But
\[
             (2U-1)P(U)=2(2U)^t-2U-1 .
\]
As \(2^{t+1}=X\), it follows that \(H\mid3^m(X-1)-2X^m\). The right side is \(X-3>0\) at \(m=1\); here \(X-3\mid H\) by the preceding exact cancellation, proving the asserted complete denominator. For \(m\ge2\) the right side is negative, because \((X/3)^m\ge X^2/9>X/2\) at \(X\ge16\), and has absolute value at most \(2X^m\). Also \(S_m\le X^m/(X-3)\le2X^{m-1}\). Finally \(D_p(n)\ge X^p/2\). These inequalities prove (1) with an absolute error of at most three in its logarithmic bound.

## Finitely many macroscopic groups of shifts still transfer the one-odd obstruction

Consider a sequence with one odd departure at \(in+\delta_i\) in each of \(p\) aligned \(n\)-date blocks, \(0\le\delta_i<n\), where \(n\to\infty,\ \log p=o(n)\). Suppose the residues \(\delta_i\) on the circle of circumference \(n\) are covered by a **fixed number** of arcs, each of length \(o(n)\). Then
\[
         \log\gcd\!\left(D_1(n),\sum_i2^{\delta_i}\right)=o(n).        \tag{3}
\]
In particular if \(\log(2+\operatorname{ord}_{q}3)=o(n)\) then
\(\log(2+\operatorname{ord}_{D_1(n)}3)=o(n)\) as well, by the exact order comparison in the [translated motif theorem](COMPOSITE_DENOMINATOR_SCALE.md). Conversely any exceptional one-odd sequence already meets the clustered condition using \(p=1\). Thus allowing these several macroscopic shift positions, with unbounded multiplicities, does not evade the one-odd order question.

For (3) take an arbitrary subsequence and pass to limiting positions on \(\mathbb R/\mathbb Z\) for all the covering arcs, discarding empty arcs and merging identical limits. Choose one fixed cut on the circle asymptotically separated from every retained position. A common integer rotation of the exponents moves that cut to zero. Algebraically, multiply by the appropriate power of two and reduce wrapped powers \(2^n\) to three modulo \(D_1(n)\). This introduces at most a factor three in each **positive** coefficient and preserves the gcd with \(D_1(n)\). The positions of each surviving cluster now lie in an ordinary interval of length \(o(n)\). Factor from it the binary power at its smallest position. Its remaining positive coefficient is at most \(3p\,2^{o(n)}\), so has logarithmic height \(o(n)\). Distinct cluster starts are macroscopically separated on the circle. The [PR212 separated signed-sum theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MOVING_ARCS.md) applies at raw grade one and length \(n\). It gives a strictly positive denominator exponent, rational with reduced denominator dividing \(\gcd(n,1)=1\). Since the denominator divides \(2^n-3\), this exponent is one on every convergent subsequence, exactly (3).

Even without the fixed-cluster hypothesis, if the largest cyclic gap between occupied shifts is \(E\), the same rotation puts all the shifts in an interval of length \(n-E\) and gives
\[
       \gcd\!\left(D_1(n),\sum_i2^{\delta_i}\right)\le3p\,2^{n-E}.
\]
Thus loss of all but \(2^{o(n)}\) of \(D_1(n)\) at \(\log p=o(n)\) requires \(E=o(n)\). In the construction (1) the shift set does fill the whole circle to within two native dates. The number of occupied blocks alone would not distinguish that construction from those in (3).
