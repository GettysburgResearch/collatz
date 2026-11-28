# Arbitrarily sparse marked windows with full numerator cofactors on actual denominator-clearing paths

The [uniform cofactor theorem](DESCENDING_NUMERATOR_COFACTORS.md) gives almost-full cofactor height at almost every denominator level. The following exact construction tests whether even imposing this conclusion at **every** observed level would bound elapsed native time in terms of the number of odd departures in that window. It works within the positive, bounded-real-size, residual-denominator-one test \(J(N)\) of [Positive descending intervals](../ordinary/POSITIVE_DESCENDING_INTERVALS.md).

Fix a finite prime set \(P\supset\{2,3\}\). Let \(q=1\) or a power of five, let \(N\ge1\), and put \(Q=q3^N\). Take **any** binary word \(W\) of length \(D\ge1\) with \(k\le N\) odd departures. If \(k=N\), let its last letter be the last odd departure, so the prescribed segment stops at the landing. Let \(R\) be the longest run of zero letters. There is an explicit constant \(C_P\) depending only on \(P\) such that if
\[
                       Q\ge C_P\,2^D(k+1)^{|P|},                      \tag{1}
\]
then some integer \(Q/2\le b\le Q\) coprime to \(Q\) gives an actual rational shortcut orbit from \(b/Q\) with precisely this prefix. At **each** of its \(k\) odd departures the signed reduced numerator (positive in this construction) satisfies
\[
 \log_2 b_P(u_h)\ge \log_2(q3^h)-R-1-
                              \sum_{\ell\in P\setminus\{2,3\}}\log_2[2\ell(k+1)],
                                                                        \tag{2}
\]
where \(q3^h\) is the current complete reduced denominator. No prime-density or random-independence premise enters the construction.

For the proof, let \(g_j\) be the number of odds before relative date \(j\), and let \(C_j\) be the usual integer carry for the first \(j\) letters. Modulo \(2^D\), the word specifies exactly one residue of \(b/Q\) since \(Q\) is odd. Let \(b_*\) be an integer in the corresponding residue of \(b\). At any observed odd date \(t<D\), the reduced-numerator candidate is
\[
                   u_{N-g_t}=\frac{b+q3^{N-g_t}C_t}{2^t}.
\]
This follows by multiplying the physical affine equation by \(q3^{N-g_t}\). As \(b=b_*+2^Dz\) varies, this integer changes by \(2^{D-t}z\). Choose a residue of \(z\) modulo three making \(3\nmid b\), and, when \(5\mid q\), choose one modulo five making \(5\nmid b\). Then the reduced denominator really is \(q3^{N-g_t}\). For each other \(\ell\in P\setminus\{2,3\}\), except five if it divides \(q\), take \(a_\ell=\lceil\log_\ell[2(k+1)]\rceil\). Each odd date forbids just one class of \(z\bmod\ell^{a_\ell}\) if we ask that \(\ell^{a_\ell}\nmid u_{N-g_t}\). There are at most \(k\) forbidden classes, strictly fewer than the modulus, since \(2^{D-t}\) is invertible there. Choose an allowed class for each prime and use the Chinese remainder theorem. The joint modulus for \(b\) is at most
\[
                    15\cdot2^D\prod_{\ell\in P\setminus\{2,3\}}2\ell(k+1).
\]
For example \(C_P=30\prod_{\ell\in P\setminus\{2,3\}}2\ell\) suffices to find a representative in \([Q/2,Q]\). Every marked numerator is odd and prime to three and \(q\), and the logarithms of the powers removed at the other primes are bounded by the sum in (2). The real input is at least \(1/2\). Every positive odd departure also produces a real value of at least \(1/2\), and the intervening consecutive even steps halve it. Thus the real value at any marked input is at least \(2^{-R-1}\). Multiplying by its reduced denominator proves (2).

Two consequences isolate different global costs.

* For a genuine \(q=1\) bounded initial test one may prescribe \(k=\lfloor\sqrt N\rfloor\) odd departures spread across \(D=\lfloor(\log_2 3)N-(|P|+3)\log_2(N+2)\rfloor\) positive dates with maximum even run \(O(\sqrt N)\). For example split \(D\) into \(k\) blocks of sizes differing by at most one, each ending in one odd letter. For all large \(N\), (1) holds. Throughout this moving window \(h\ge N-k+1\), and (2) gives \(\log b_P(u_h)/\log(3^h)\ge1-o(1)\) on **every** marked date. Yet \(D/[k\log(2+k)]\to\infty\). The same construction accommodates any ordered rearrangement with the same maximal-run bound and many distinct waits. The full landing expends all \(N\) odd departures. This particular segment has time \(O(N)\), so it does not violate a bound for \(J(N)\) in terms of \(N\).
* If the remaining denominator \(q=5^s\) can grow, prescribe the entire \(k=N\)-odd path ending at its \(N\)-th odd, with **any** requested duration \(D\ge N\). Take \(\log_2 q\ge (D+N+\log C_P)^2\) by increasing \(s\) if needed for (1). Even the trivial \(R\le D\) in (2) then gives \(\log b_P(u_h)/\log(q3^h)\ge1-o(1)\) at every level as \(D+N\to\infty\), while the positive initial value lies in \([1/2,1]\). This is a complete descent with an unbounded arbitrary native clock, fixed prime support of \(q\), and large cofactors at every level. Its precision cost is carried by the growing \(q\). The master ordinary worst-source clock and the \(q=1\) complete landing still require a separate global argument.

These are varying true rational sources. The local \(q=1\) case already rules out a window bound using only the number of its odd levels, positivity, bounded initial real size and almost-full numerator cofactors. The exact word-cylinder input requires the whole available initial precision in (1); a proposed global proof has to use how precision is shared across the full descent.
