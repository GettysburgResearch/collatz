# Occupied states at the critical parity-entropy exponent

**PROPOSED.** This is a proof for ordinary positive shortcut orbits. The critical estimate below strengthens the range of exponents in [T-A3-402 and T-A3-403](../astra-three-routes/pass2/ORBIT_MELLIN.md). That source already supplies reciprocal summability and coefficient escape. We use neither a conjectured orbit law nor a simulated orbit.

Let \(T(x)=x/2\) for even \(x\) and \(T(x)=(3x+1)/2\) for odd \(x\). Set
\[
 p=\log_3 2,\qquad h=-p\log_2 p-(1-p)\log_2(1-p)=0.949955527\ldots .
\]
Let \(S\) be a set of positive integers such that \(T(S)\subset S\) and \(T|_S\) is injective. This includes the distinct values of a periodic orbit and the complete value set of a non-eventually-periodic orbit. Alternatively, let \(S\) be the values in a finite segment of pairwise distinct states of one trajectory. Put \(N(X)=\sup_{a\in\mathbb R}\#(S\cap[a,a+X))\). The interval may lie arbitrarily far from the origin.

## Statement

There is an absolute constant \(C\) such that, for \(X\ge16\),
\[
 N(X)\le C X^h(\log X)^{-3/2}.       \tag{1}
\]
Consequently the *critical* Mellin sum \(\sum_{x\in S}x^{-h}\) is uniformly bounded. More generally, uniformly for real \(z\), the sum of \(|x-z|^{-h}\) over \(x\in S\) with \(|x-z|\ge M\) is
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

Fix a sufficiently large constant \(K>1\) and set \(c_u=K(u+1)^2\). For large real \(X\) let \(L=\lfloor\log_2 X\rfloor\). Consider starts \(x\) in any interval \([a,a+X)\). For a finite segment discard its last \(L\) positions, or all positions if it has fewer. Define \(q_t\) as the number of odd inputs in the first \(t\) steps and \(D_t=q_t-pt\). Call a source captured when for some \(1\le t\le L\)
\[
 2\cdot 3^{D_t}\le 1/c_{u(t)}.
\]
At a fixed pair \((t,q)\), all starts with \(q_t=q\) have endpoints in the single interval
\[
 [\,3^{q-pt}a,\quad 3^{q-pt}a+2\cdot 3^{q-pt}X\,).
\]
Indeed \(T^t(x)=3^{q-pt}x+E_t\) with \(0\le E_t\le (3/2)^q-1\). The upper bound holds inductively: an even step halves the old remainder, and an odd step multiplies by \(3/2\) and adds \(1/2\). Since \(X\ge 2^t\), we have \(3^{q-pt}X\ge 3^q\ge E_t\). For each such pair, the endpoints are distinct states in \(S\), including in the finite-segment version. The size of the captured population is therefore bounded by
\[
 \sum_{\substack{1\le t\le L,\ 0\le q\le t\\2\cdot3^{q-pt}\le 1/c_{u(t)}}}
    N(2\cdot3^{q-pt}X).
\]
No independence is needed between capture times, weights, or interval locations. All uncaptured sources satisfy (3) with \(a\) there replaced by \(a_0=\log_3(2K)\) and \(b=2/\log 3\). Both ends of the walk have the same constant lower bound.

Each parity word of length \(L\) fixes one residue class modulo \(2^L\), and at most two integers in \([a,a+X)\) occupy it. For instance, two sources with the same first \(t\) bits have endpoint difference \(3^{q_t}(x-y)/2^t\). Successive parity agreement forces one additional factor of two at each step. Under the Bernoulli law of (3), a particular length-\(L\) word with endpoint \(d=q_L-pL\) has probability
\[
 2^{-hL}\exp(\lambda d),\qquad \lambda=\log(p/(1-p))>0 .
\]
Applying (3) for attainable \(d\ge-a_0\) and multiplying by the reciprocal of this probability converts the walk estimate to a word count. Unit spacing and geometric decay give
\[
 \sum_{d\ge-a_0}e^{-\lambda d}(1+a_0+d)=O_{p,K}(1).
\]
The number of uncaptured sources is therefore at most \(C_K X^h/L^{3/2}\).

## Closing the scale recurrence

Write \(F(X)=X^h/(\log X)^{3/2}\) for \(X\ge16\). Terms with recursive width \(Y=2\cdot3^{q-pt}X<\sqrt X\) contribute at most \(O(L^2(1+\sqrt X))=o(F(X))\) by the trivial count on an interval. For \(\sqrt X\le Y<X\), we have \(F(Y)\le2^{3/2}(Y/X)^h F(X)\). For each \(t\), summing these ratios to power \(h\) over captured \(q\) costs at most \(c_{u(t)}^{-h}/(1-3^{-h})\), since the widths decrease geometrically as \(q\) decreases. Each \(u(t)\) occurs at most twice. Since \(2h>1\), choose \(K\ge2\) so large that
\[
 \frac{2^{5/2}}{1-3^{-h}}\sum_{u\ge0} c_u^{-h}<1/2.
\]
The finite-segment boundary loss \(L\) is absorbed in \(O(F(X))\). Induct on dyadic scales with a common multiplier for \(N(X)\le C F(X)\). On bounded initial scales use \(N(X)\le X+1\), and on large scales choose \(C\) at least twice the constant for the nonrecursive terms. Every recursive width is at most \(X/2\). Taking the supremum over starting intervals proves (1). Summing over shells \(2^j\le |x-z|<2^{j+1}\), each covered by at most three intervals of length \(2^j\), gives (2) from \(\sum_{j\ge J}j^{-3/2}=O(1/\sqrt J)\).

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

The pinned baseline is main at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The comparison is PR #92 at `7bb6d36d3bc37dd09b52aa9a23c8e33973032359`, file `research/astra-three-routes/pass2/ORBIT_MELLIN.md`, T-A3-402/403. Garcia–Tal established orbit sparsity. The reciprocal-sum and surplus consequences of their work were explicitly discussed in 2026. Curry's explicit translated-window preprint gives a bound with exponent above 0.96538. Esm's subsequent endpoint estimate supplies a logarithmic saving at the Curry exponent for general equal-time collision-free sets with an explicit constant. Formula (1) uses forward invariance or a simple segment to recurse at the smaller exponent h. This comparison is based on source inspection, without a local Lean replay. Global priority for (1) is unassessed. [Garcia and Tal, Acta Arithmetica 90 (1999), 245–250](https://repositorio.usp.br/bitstreams/a02b7ba9-c8be-42d8-bbae-4d836520ec13) · [Curry (2026)](https://doi.org/10.5281/zenodo.22087163) · [Esm, pinned window statement](https://github.com/Esythium/collatz-endpoint-lean/blob/062f233c45ebde62b1f0e8a881d8ea440bf5c4ad/CollatzEndpoint/Windows.lean) · [Public discussion of summability](https://mathoverflow.net/questions/513539).
