# Occupied states at the critical parity-entropy exponent

**PROPOSED.** This is a proof for ordinary positive shortcut orbits. The critical estimate below strengthens the range of exponents in [T-A3-402 and T-A3-403](../astra-three-routes/pass2/ORBIT_MELLIN.md). That source already supplies reciprocal summability and coefficient escape. We use neither a conjectured orbit law nor a simulated orbit.

Let \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\). Set
\[
 p=\log_3 2,\qquad h=-p\log_2 p-(1-p)\log_2(1-p)=0.949955527\ldots .
\]
Let \(S\) be a set of positive integers such that \(T(S)\subset S\) and \(T|_S\) is injective. This includes the distinct values of a periodic orbit and the complete value set of a non-eventually-periodic orbit. Put \(N(X)=\#(S\cap[1,X])\).

## Statement

There is an absolute constant \(C\) such that, for \(X\ge16\),
\[
 N(X)\le C X^h\frac{(1+\log\log X)^2}{(\log X)^{3/2}}.       \tag{1}
\]
Consequently the *critical* Mellin sum \(\sum_{x\in S}x^{-h}\) is uniformly bounded. Its contribution from \(x\ge M\) is
\[
 O\!\left(\frac{(1+\log\log M)^2}{\sqrt{\log M}}\right)
 \qquad(M\ge16).                                                \tag{2}
\]

## An elementary walk estimate

Let \(Z_j\) be the sum of \(j\) independent centered increments \(B-p\) with \(B\) Bernoulli of parameter \(p\). For \(a\ge0\) the probability of staying above \(-a\) up to time \(m\) is at most \(C_p(a+1)/\sqrt m\). The same bound holds for staying below \(a\).

Indeed, stop the walk on first leaving \([-a,b)\), with \(b=\sqrt m\). For the stopped time truncated at \(m\), the mean position is zero and it is at least \(-a-1\). The probability of exit through the top by time \(m\) is therefore at most \((a+1)/(a+b+1)\). The quadratic \((z+a+1)(b+1-z)\) is nonnegative up to and including this stopped time. Its expected decrement per active step is \(p(1-p)\), so the probability of no exit by time \(m\) is at most \((a+1)(b+1)/(mp(1-p))\). Add both bounds. Reflection gives the upper-barrier version.

For \(L\ge6\), \(A\ge0\) and an attainable terminal value \(d\ge-A\), it follows that
\[
 \Pr\{\min_{t\le L} Z_t\ge-A,\ Z_L=d\}
 \le C_p\frac{(1+A)(1+A+d)}{L^{3/2}}.                        \tag{3}
\]
Split the increments into three consecutive groups of lengths \(\lfloor L/3\rfloor,L-2\lfloor L/3\rfloor,\lfloor L/3\rfloor\). The first walk stays above \(-A\). The last group in reverse order has every partial sum at most \(d+A\), since these sums are \(Z_L-Z_{L-j}\). These restrictions on the outer groups are independent. Given their values, the middle group must attain one prescribed sum. The largest binomial atom for its length is \(O_p(L^{-1/2})\) by Stirling's formula at the binomial mode. Multiplication gives (3).

## Charging contractions at several time lags

Fix a sufficiently large constant \(K>1\) and set \(c_u=K(u+1)^2\). For a large real \(X\) let \(L=\lfloor\log_2 X\rfloor\) and \(q_t\) count the odd inputs in the first \(t\) steps from \(x\). Call a source captured if for some \(1\le t\le L\)
\[
 T^t(x)\le X/c_{L-t}.
\]
For each fixed \(t\), the endpoints of captured sources at that lag are distinct members of \(S\). The union bound over capture times thus costs at most \(\sum_{u=0}^{L-1}N(X/c_u)\).

The shortcut affine identity gives
\[
 T^t(x)=3^{q_t-pt}x+E_t,\qquad 0\le E_t\le(3/2)^t-1 .
\]
The last inequality follows inductively from \(E_0=0\) and \(E_{t+1}\le3E_t/2+1/2\). For large \(X\), \((3/2)^L<X/(2K(L+1)^2)\). Hence every uncaptured source \(x\le X\) satisfies
\[
 q_t-pt > -\log_3(2c_{L-t})\quad(1\le t\le L).
\]
In particular its walk stays above \(-A\), \(A=\log_3(2K(L+1)^2)\), and ends above \(-a\), \(a=\log_3(2K)\). The terminal lower bound is independent of \(L\). This distinction makes critical summability possible.

Each parity word of length \(L\) fixes one residue class modulo \(2^L\), and at most two integers in \([1,X]\) occupy it. For instance, two sources with the same first \(t\) bits have endpoint difference \(3^{q_t}(x-y)/2^t\). Successive parity agreement forces one additional factor of two at each step. Under the Bernoulli law of (3), a particular length-\(L\) word with endpoint \(d=q_L-pL\) has probability
\[
 2^{-hL}\exp(\lambda d),\qquad \lambda=\log(p/(1-p))>0 .
\]
Applying (3) for attainable \(d\ge-a\) and multiplying by the reciprocal of this probability converts the walk estimate to a word count. Unit spacing and geometric decay give
\[
 \sum_{d\ge-a}e^{-\lambda d}(1+A+d)=O_{p,K}(1+A).
\]
The number of uncaptured sources is therefore at most \(C_K X^h(1+\log L)^2/L^{3/2}\).

## Closing the scale recurrence

Write \(F(X)=X^h(1+\log\log X)^2/(\log X)^{3/2}\) for \(X\ge16\). For all sufficiently large \(X\), every \(Y=X/c_u\) in the recurrence has \(\sqrt X\le Y<X\). Thus \(F(X/c_u)\le 2^{3/2}c_u^{-h}F(X)\). Since \(2h>1\), fix \(K\) so large that \(2^{3/2}\sum_{u\ge0}c_u^{-h}<1/2\). The preceding sections imply
\[
 N(X)\le C_K' F(X)+\sum_{u<L}N(X/c_u).
\]
On bounded initial scales use \(N(X)\le X\). Induct on dyadic scales, enlarging the common multiplier to cover the initial range and \(2C_K'\), and taking \(K\ge2\) so all recursive arguments lie at least one dyadic scale lower. This proves (1). Integrating the count by parts, or summing over dyadic shells above \(M\), gives (2) from \(\sum_{j\ge J}(1+\log j)^2j^{-3/2}=O((1+\log J)^2/\sqrt J)\).

## Consequence for actual surplus

Along an infinite distinct orbit \(x_k=T^k(n)\), put \(D_k=q_k-pk\). The exact product identity gives
\[
 x_k=n3^{D_k}P_k,\qquad
 P_k=\prod_{i<k,\ x_i\ {\rm odd}}(1+1/(3x_i)).
\]
Since \(x_i^{-1}\le x_i^{-h}\), (2) bounds \(P_k\) by an absolute constant uniformly in \(n,k\). Thus
\[
 \sum_{k\ge0}3^{-hD_k}=(n)^h\sum_{k\ge0}P_k^h x_k^{-h}<\infty.
\]
For example, for any fixed real \(B\) there must be arbitrarily large \(k\) with \(hD_k\log 3>\log k+\log\log k+B\), since \(\sum 1/(k\log k)\) diverges. This is a record constraint, with no pointwise rate asserted. For cycle values (1) and (2) count each state once.

The full stopping question still requires excluding an actual ordinary source whose surplus escapes. This estimate constrains the time it spends in low surplus ranges. It allows paths with fast-growing surplus. In an inverse basin equal-time endpoints can coincide, so the capture charge would require an additional multiplicity estimate.

## Provenance

The pinned baseline is main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The comparison is PR #92 at `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, file `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-402/403. Garcia–Tal established orbit sparsity. The reciprocal-sum and surplus consequences of their work were explicitly discussed in 2026. Global priority for the critical estimate is unassessed. [Garcia and Tal, Acta Arithmetica 90 (1999), 245–250](https://repositorio.usp.br/bitstreams/a02b7ba9-c8be-42d8-bbae-4d836520ec13) · [Public discussion of summability](https://mathoverflow.net/questions/513539).
