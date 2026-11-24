# Divisor certificates for short prefixes of actual odd orbits

Let \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. For \(t\ge2\), write \(q_i=U^i(x)\), \(0\le i<t\). Call position \(j\) **covered** when
\[
 v_p(q_j)\le \sum_{i\ne j}v_p(q_i)\qquad\text{for every prime }p .
\]
For example, a position holding 1 is covered. Let \(E_t(X)\) count positive odd \(x\le X\) with at least one covered position in this prefix.

**Theorem 1 (unconditional).** If \(2\le t=t(X)=o(\log\log X)\), then \(E_t(X)\le X^{o(1)}\). Outside this set each position has a prime whose valuation there exceeds the sum of its valuations at all other positions. The \(t\) witnessing primes are distinct, and the \(t\) states are multiplicatively independent. The variable in this count is the original source \(x\).

### A finite count

Put \(a_i=v_2(3q_i+1)\ge1\), and \(A_{ij}=\sum_{i\le u<j}a_u\). For a possible word \(w=(a_0,\ldots,a_{t-2})\) define
\[
 C_{ij}=\sum_{u=i}^{j-1}3^{j-1-u}2^{A_{iu}},\qquad
 P_j(w)=\prod_{i\ne j} C_{\min(i,j),\max(i,j)} .
\]
Each factor is positive, and each adjacent-pair factor is 1. Write \(\tau(n)\) for the positive divisor count and \(B=\lfloor\log_2X\rfloor+2(t-1)\). Then
\[
 E_t(X)\ \le\
 \sum_{\substack{w\in\mathbb Z_{\ge1}^{\,t-1}\\ \sum a_i\le B}}
 \ \sum_{j=0}^{t-1}\tau(P_j(w))
 \ \le\ t {B\choose t-1}
 \max_{1\le n\le (12^tX)^{t-2}}\tau(n).                    \tag{1}
\]

Iterating the actual equations gives
\[
 2^{A_{ij}}q_j=3^{j-i}q_i+C_{ij},\qquad \gcd(q_i,q_j)\mid C_{ij}.
                                                               \tag{2}
\]
If \(j\) is covered, truncate each competing \(p\)-valuation at \(v_p(q_j)\). If a competitor reaches this threshold its term suffices. Otherwise truncation leaves the sum unchanged. Consequently
\[
 q_j\mid \prod_{i\ne j}\gcd(q_i,q_j)\mid P_j(w).             \tag{3}
\]
For fixed \(w,j\), (2) with \(i=0\) recovers at most one source for each candidate divisor \(q_j\). For \(j=0\) the source is the divisor itself. This is where divisibility gives more information than a height inequality for \(q_j\).

Multiplying the edge equations gives \(2^{A_{0,t-1}}q_{t-1}\le4^{t-1}x\), since \(3q+1\le4q\) at each positive \(q\). The cumulative exponents select \(t-1\) distinct positive positions at most \(B\), giving the binomial count. Each \(C_{ij}\le 2^{A_{0,t-1}}(3^{j-i}-1)/2\le12^t X\), and at least one factor of \(P_j\) is 1. This proves (1), including \(t=2\).

Uniformly for \(1\le n\le Y\), \(\log\tau(n)=O(\log Y/\log\log Y)\) as \(Y\to\infty\). Primes up to \(\sqrt{\log Y}\) contribute at most \(\sqrt{\log Y}\log(1+\log_2 Y)\) to \(\log\tau(n)\). At larger primes use \(\log(e+1)\le e\log2\) and \(\sum e\log p\le\log Y\). For \(t\ge3\) set \(Y=(12^t X)^{t-2}\). The last factor in (1) has log \(O(t\log X/\log\log X)\). The other factors have log \(O(t\log(\log X+t))\). Both are \(o(\log X)\) in the stated range. At \(t=2\) bound (1) is already polylogarithmic.

A nonzero integer multiplicative relation has an index \(j\) of largest nonzero coefficient magnitude. Taking the \(p\)-valuation and the triangle inequality shows that \(j\) is covered. Two different positions cannot both have strictly dominating valuation at the same prime. This proves the independence and distinctness assertions.

### An original-floor bound

**Theorem 2.** For any positive odd source \(x\) with a covered position in its first \(t\ge3\) states, \(m=\min_{0\le i<t}q_i\) satisfies
\[
 m^{t-1}\le (4^{t-1}x)^{t-2}.                                \tag{4}
\]
In particular there is an actual iterate strictly below the original \(x\) when \(x>4^{(t-1)(t-2)}\). At every future minimum above this threshold all first \(t\) heights have distinct strictly dominating coordinates.

Indeed \(m2^{A_{iu}}\le q_u2^{A_{iu}}\le4^{u-i}q_i\). Summing the positive carry terms gives
\[
 mC_{ij}\le(4^{j-i}-3^{j-i})q_i\le 4^{t-1}x .
\]
For the last step \(q_i\le2^i x\) follows from \(a_i\ge1\). Remove one adjacent factor from (3), multiply the remaining \(t-2\) bounds, and use \(q_j\ge m\) at the covered position. This proves (4) without any restriction on individual division exponents.

For \(t=3\), write the states \(x,y,z\). A covered position exists **if and only if \(z\mid x\)**. The adjacent gcds are 1, so the three alternatives are \(x\mid z,\ y=1,\ z\mid x\). If \(y=1\), then \(z=1\). Write \(2^a y=3x+1,\ 2^b z=3y+1\). For any common divisor \(g\) of \(x,z\), (2) gives \(g\mid 2^a+3\). As \(2z-1\le3y\),
\[
 (g-3)(2z-1)\le 2^a(3y)=9x+3 .
\]
If \(x\mid z\) and \(x\ge9\), setting \(g=x\) and using \(z\ge x\) yields \(2x^2-7x\le9x\), a contradiction. For \(x=3,5,7\), the corresponding \(z\) is \(1,1,17\); only \(x=1\) is left in the alternative \(x\mid z\). Therefore whenever \(x>1\) has a covered triple, \(z<x\) and \(2z^2-7z\le9x\), by setting \(g=z\) above. No multiplicative dependence follows from \(z\mid x\) alone.

### Retaining every fixed target in a sparse section (conditional)

Let \(B(k,\sigma)\) be the exact dyadic head and valuation section of [PR 199, Theorem A](https://github.com/GettysburgResearch/collatz/blob/d868f8e8405c08b8c501236853bea495ca593824/research/optimal-critical-ancestors-20261124/README.md). Write \(\mathcal A(b)\) for the ordinary ancestor set of a fixed positive odd \(b\) coprime to 3. Under the same external inputs M (target-dependent positive lower density) and R (the stated Rhin phase bound), for every \(k\ge2\), \(0<\sigma<10/133\), and \(2\le t(X)=o(\log\log X)\), the set
\[
 \{x\le X:x\in B(k,\sigma)\cap\mathcal A(b),\
          \text{each of its first }t(X)\text{ positions has a dominating prime}\}
\]
has count \(X^{1-1/k+o(1)}\). Section members are odd. Subtract (1) from the lower bound in Theorem A at the same cutoff \(X\). Its upper bound remains valid. For \(10/133\le\sigma<1\), the corresponding limsup exponent follows under M alone. The external inputs are used as stated in that checkpoint. Estimate (1) itself applies unconditionally to any source population of positive count exponent.

In particular, one nonconvergent trajectory would force \(X^{1-1/k+o(1)}\) nonconvergent critical sources with these growing independent prefixes, for each fixed \(k\) in the all-cutoff range. Choose any positive odd 3-unit on that trajectory as \(b\); such a unit occurs after at most one odd step. Every ancestor of \(b\) inherits its nonconvergence. An upper count exponent strictly below \(1-1/k\) for the nonconvergent sources with the stated prime witnesses would close the problem under M and R. The lower count shows exactly why merely proving the presence of those prime witnesses in each component cannot furnish that upper bound.

### Testing the reverse implication on ordinary orbits

For any fixed finite positive gap word and any fixed positive odd \(b\) coprime to 3 there are arbitrarily large sources with exactly that word whose *next* accelerated step lands on \(b\). In particular, they may all be chosen in the basin of 1, with no covered position in the prescribed word. Put \(s=t-1,\ A=A_{0s},\ C=C_{0s}\). Pick arbitrarily large \(E\) with
\[
 2^E b\equiv 1+3C\,2^{-A}\pmod {3^{s+1}} .
\]
The right side is a unit, and 2 generates the units modulo \(3^{s+1}\). Indeed \(v_3(4^{3^j}-1)=j+1\) follows by induction by cubing \(1+3^{j+1}u\) with \(3\nmid u\), and the order modulo 3 is 2. Set \(q_s=(2^E b-1)/3\) and \(x=(2^A q_s-C)/3^s\). The congruence makes \(x\) integral. Inverting the word successively gives positive odd integers for large \(E\). For every suffix starting at \(i\), its numerator \(2^{A_{is}}q_s-C_{is}\) is divisible by \(3^{s-i}\), since \(C=3^{s-i}C_{0i}+2^{A_{0i}}C_{is}\) (set \(C_{ii}=0\)). Each nonempty suffix numerator is odd, because its first carry term is odd and later ones even. These exact steps have the prescribed valuations, and every \(q_i\) tends to infinity. Equation (3) then fails for every fixed \(P_j(w)\).

A growing interval may therefore have a different strictly dominating prime for each position, even on a terminating trajectory. The same primes have no obligation to recur after that interval. The ancestor counts estimate how many *sources* have a covered position. They supply no upper bound on the time one must wait for a named escaping trajectory to reach such a position, nor on its height at that time. To force descent below its original source, one needs the covered position in a window whose current height is still small enough for (4) to cross that source. Prescribing a preceding inverse word at the target changes the orientation of this obligation.

### Relation to existing rank results

The valuation criterion and affine gcd divisibility in (2)–(3) are exactly [Paper 137, Lemma 4 and equation (12)](https://rstation.ai/problems/collatz/papers/137/v1). Its equations (18)–(24) also give independence on high windows with bounded total exponent and aggregate window estimates. [Paper 138, Theorems 1 and 2](https://rstation.ai/problems/collatz/papers/138/v1) gives substantially stronger whole-prefix rank and coset visit results than elementary window estimates. [Paper 144, Theorem 14](https://rstation.ai/problems/collatz/papers/144/v1) proves Sidonicity for sufficiently high distinct segments from their minimum alone. It treats relations between two products of two states. Our (4) concerns arbitrary integral relations and retains the original source height. [Paper 159](https://rstation.ai/problems/collatz/papers/159) also charges expensive returns to decreases of running minima. Yang's earlier rank and return manuscript is cited in those comparisons. The additional use here is counting original sources by divisors of an entire fixed word before summing over physical words, and applying that bound within each named critical ancestor population. We make no general literature priority claim.


### Finite verification

[FixedWord.lean](FixedWord.lean) proves the physical affine identity, gcd divisibility, adjacent carry, total height budget, floor-weighted carry bound, covered-row divisibility, and multiplication of floor bounds. [DivisorCount.lean](../controller/DivisorCount.lean) proves the divisor count for one fixed affine row and a finite union of source-selected rows. Both modules compiled with Lean 4.34.1 and warnings as errors. The assembly over all subintervals, enumeration of division words, asymptotic count, triple classification, and fixed-target corollary are written proofs. [controls.py](controls.py) separately checks 8,000 positive odd starts at each of five prefix lengths and 360 ordinary finite-word/target lifts.
