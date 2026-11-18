# Occupied states at the critical parity-entropy exponent

**PROPOSED.** This is a proof for ordinary positive shortcut orbits. The critical estimate below strengthens the range of exponents in [T-A3-402 and T-A3-403](../astra-three-routes/pass2/ORBIT_MELLIN.md). That source already supplies reciprocal summability and coefficient escape. We use neither a conjectured orbit law nor a simulated orbit.

Let \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\). Set
\[
 p=\log_3 2,\qquad h=-p\log_2 p-(1-p)\log_2(1-p)=0.949955527\ldots .
\]
Let \(S\) be a set of positive integers such that \(T(S)\subset S\) and \(T|_S\) is injective. This includes the distinct values of a periodic orbit and the complete value set of a non-eventually-periodic orbit. Alternatively, let \(S\) be the values in a finite segment of pairwise distinct states of one trajectory. Put \(N(X)=\#(S\cap[1,X])\).

## Statement

There is an absolute constant \(C\) such that, for \(X\ge16\),
\[
 N(X)\le C X^h(\log X)^{-3/2}.       \tag{1}
\]
Consequently the *critical* Mellin sum \(\sum_{x\in S}x^{-h}\) is uniformly bounded. Its contribution from \(x\ge M\) is
\[
 O\!\left((\log M)^{-1/2}\right)
 \qquad(M\ge16).                                                \tag{2}
\]

## An elementary walk estimate

Let \(Z_j\) be the sum of \(j\) independent centered increments \(B-p\) with \(B\) Bernoulli of parameter \(p\). For \(a\ge0\) the probability of staying above \(-a\) up to time \(m\) is at most \(C_p(a+1)/\sqrt m\). The same bound holds for staying below \(a\).

Indeed, stop the walk on first leaving \([-a,b)\), with \(b=\sqrt m\). For the stopped time truncated at \(m\), the mean position is zero and it is at least \(-a-1\). The probability of exit through the top by time \(m\) is therefore at most \((a+1)/(a+b+1)\). The quadratic \((z+a+1)(b+1-z)\) is nonnegative up to and including this stopped time. Its expected decrement per active step is \(p(1-p)\), so the probability of no exit by time \(m\) is at most \((a+1)(b+1)/(mp(1-p))\). Add both bounds. Reflection gives the upper-barrier version.

The same survival bound holds for the curved lower barrier \(-g(j)=-a-b\log(1+j)\), for fixed \(b>0\), with a constant depending only on \(p,b\). Let \(\tau\) be its first strict downcrossing. The constant-barrier result with \(g(m)\) first gives \(\Pr(\tau>m)\le C_{p,b}(1+a+\log(m+1))/\sqrt m\). Define
\[
 D_j'=\mathbb E[(Z_j+g(j)+1)\mathbf1_{\tau>j}].
\]
At a first crossing the discarded factor is nonnegative, because the increments have absolute value at most one and \(g\) is nondecreasing. Conditional expectation on histories alive at \(j-1\) gives
\[
 D_j'\le D_{j-1}'+(g(j)-g(j-1))\Pr(\tau>j-1).
\]
Summing the crude bound against increments at most \(b/j\) yields \(D_j'\le C_{p,b}(1+a)\). Split at \(j=\lfloor m/2\rfloor\). Conditional on survival there, staying alive for the remainder requires staying above the weaker constant boundary \(-g(m)\). Its survival probability is at most \(C_p(1+Z_j+g(m))/\sqrt{m-j}\). Integrate and use \(g(m)-g(j)\le b\log 3\) to obtain \(\Pr(\tau>m)\le C_{p,b}(1+a)/\sqrt m\). Reflection gives the curved upper-barrier bound.

Set \(u(t)=\min(t,L-t)\). For \(L\ge6\) and an attainable terminal value \(d\ge-a\),
\[
 \Pr\{Z_t\ge-g(u(t))\ (0\le t\le L),\ Z_L=d\}
 \le C_{p,b}\frac{(1+a)(1+a+d)}{L^{3/2}}.                   \tag{3}
\]
Split the increments into three consecutive groups of lengths \(\lfloor L/3\rfloor,L-2\lfloor L/3\rfloor,\lfloor L/3\rfloor\). The first walk stays above \(-g(j)\). The last group in reverse order has every partial sum at most \(d+g(j)\), since these sums are \(Z_L-Z_{L-j}\). These restrictions are independent. Given the outer groups, the middle group must attain one prescribed sum. Its largest binomial atom is \(O_p(L^{-1/2})\) by Stirling's formula at the binomial mode. Multiplication gives (3).

## Charging contractions at several time lags

Fix a sufficiently large constant \(K>1\) and set \(c_u=K(u+1)^2\). For a large real \(X\) let \(L=\lfloor\log_2 X\rfloor\) and \(q_t\) count the odd inputs in the first \(t\) steps from \(x\). Call a source captured if for some \(1\le t\le L\)
\[
 T^t(x)\le X/c_{u(t)}.
\]
For each fixed \(t\), the endpoints of captured sources at that lag are distinct members of \(S\). For a finite segment first discard its last \(L\) positions, or all positions if it has fewer. Equal-lag endpoints are then distinct and still in the segment. Each \(u(t)\) occurs at most twice. The union bound over capture times costs at most \(2\sum_{u\le L}N(X/c_u)\).

The shortcut affine identity gives
\[
 T^t(x)=3^{q_t-pt}x+E_t,\qquad 0\le E_t\le(3/2)^t-1 .
\]
The last inequality follows inductively from \(E_0=0\) and \(E_{t+1}\le3E_t/2+1/2\). For large \(X\), \((3/2)^L<X/(2K(L+1)^2)\). Hence every uncaptured source \(x\le X\) satisfies
\[
 q_t-pt > -\log_3(2c_{u(t)})\quad(1\le t\le L).
\]
Thus (3) applies with \(a=\log_3(2K)\) and \(b=2/\log 3\). Both ends have the same constant lower bound.

Each parity word of length \(L\) fixes one residue class modulo \(2^L\), and at most two integers in \([1,X]\) occupy it. For instance, two sources with the same first \(t\) bits have endpoint difference \(3^{q_t}(x-y)/2^t\). Successive parity agreement forces one additional factor of two at each step. Under the Bernoulli law of (3), a particular length-\(L\) word with endpoint \(d=q_L-pL\) has probability
\[
 2^{-hL}\exp(\lambda d),\qquad \lambda=\log(p/(1-p))>0 .
\]
Applying (3) for attainable \(d\ge-a\) and multiplying by the reciprocal of this probability converts the walk estimate to a word count. Unit spacing and geometric decay give
\[
 \sum_{d\ge-a}e^{-\lambda d}(1+a+d)=O_{p,K}(1).
\]
The number of uncaptured sources is therefore at most \(C_K X^h/L^{3/2}\).

## Closing the scale recurrence

Write \(F(X)=X^h/(\log X)^{3/2}\) for \(X\ge16\). For all sufficiently large \(X\), every \(Y=X/c_u\) in the recurrence has \(\sqrt X\le Y<X\). Thus \(F(X/c_u)\le 2^{3/2}c_u^{-h}F(X)\). Since \(2h>1\), fix \(K\) so large that \(2^{5/2}\sum_{u\ge0}c_u^{-h}<1/2\). The preceding sections imply
\[
 N(X)\le C_K' F(X)+2\sum_{u\le L}N(X/c_u).
\]
The finite-segment boundary cost \(L\) is absorbed by the first term for large \(X\). On bounded initial scales use \(N(X)\le X\). Induct on dyadic scales, enlarging the common multiplier to cover the initial range and \(2C_K'\), and taking \(K\ge2\) so all recursive arguments lie at least one dyadic scale lower. This proves (1). Integrating the count by parts, or summing over dyadic shells above \(M\), gives (2) from \(\sum_{j\ge J}j^{-3/2}=O(1/\sqrt J)\).

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

The symmetric barrier and its survival proof arose during the transport review of the one-sided barrier argument.

## Provenance

The pinned baseline is main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The comparison is PR #92 at `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, file `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-402/403. Garcia–Tal established orbit sparsity. The reciprocal-sum and surplus consequences of their work were explicitly discussed in 2026. Global priority for the critical estimate is unassessed. [Garcia and Tal, Acta Arithmetica 90 (1999), 245–250](https://repositorio.usp.br/bitstreams/a02b7ba9-c8be-42d8-bbae-4d836520ec13) · [Public discussion of summability](https://mathoverflow.net/questions/513539).
