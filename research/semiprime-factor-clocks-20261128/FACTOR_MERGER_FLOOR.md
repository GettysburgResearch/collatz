# A merger with the larger prime must reach a low value

Let \(T\) be the positive shortcut map. Fix a prime \(p>3\) and a positive integer \(q\). Write \(n=pq\), and let \(\tau_*(u)\) be the first time the global minimum of the orbit of \(u\) occurs. A common vertex can have different dates on the two arms. Define its first horizon by
\[
 J(n,q)=\inf\{\max(i,j):T^in=T^jq\}.
\]
For the same-date version define \(J_{=}(n,q)=\inf\{i:T^in=T^iq\}\). Both can be infinite.

**PROPOSED deterministic theorem.** If a connection of at most \(H\) actual shortcut edges joins \(q\) to \(pq\), in either orientation at each edge, then some input of a traversed odd edge is at most
\[
 H\exp\!\big(C(1+\log p)\log(2+H)\big)                         \tag{1}
\]
for an absolute effectively computable \(C\). A common forward vertex with both clocks at most \(h\) supplies such a connection with \(H\le2h\). The proof uses the true additive correction at each odd step and the integer prime factor \(p\).

For a forward even edge the logarithm of the output/input ratio is \(-\log2\). For a forward odd edge at \(x\) it is \(\log3-\log2+\log(1+1/(3x))\). Reverse traversal negates the corresponding expression and retains the odd departure of the underlying forward edge. Summing gives
\[
 |\Lambda|=|\log p+a\log 2+b\log3|
       \le\sum_{\text{odd edges}}\log(1+1/(3x))
       \le H/(3M),
\]
if their departures are at least \(M\), where \(|a|,|b|\le H\). The form is nonzero by unique factorization. The rational three-logarithm case of Matveev's theorem gives \(\log|\Lambda|\ge-C(1+\log p)\log(2+H)\). Place the nonzero coefficient of \(\log p\) last. The three logarithms are linearly independent over the integers, the heights of 2 and 3 are fixed, \(p\) has height \(\log p\), and the largest integer coefficient is at most \(H\) for \(H\ge1\). If using the multiplicative version, \(|e^\Lambda-1|\le e|\Lambda|\) when \(|\Lambda|\le1\), and larger forms already satisfy the needed bound. There is at least one odd edge, as a path consisting only of halvings and inverse halvings changes a value by a power of two. Rearrangement proves (1). [Matveev, original rational linear-form estimate, Theorem 2.1](https://doi.org/10.1070/IM2000v064n06ABEH000314) · [PR #217, earlier signed logarithmic edge identity](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/arithmetic/HIGH_STATE_AND_PROFILE_OBSTRUCTIONS.md)

## An elementary bound for a forward meeting with a prescribed time lag

Suppose \(T^i(pq)=T^jq\). Write \(\ell=|i-j|\), \(h=\max(i,j)\), and let \(s_i,s_j\) count the odd departures on the respective prefixes. For their exact additive corrections \(E_i,E_j\), as defined in the [first-passage proof](README.md),
\[
 \Lambda=\log p+(s_i-s_j)\log3-(i-j)\log2=E_j-E_i.
\]
If both prefixes have all their odd departures at least \(M\), each correction lies in \([0,h/(3M)]\), so \(|\Lambda|\le h/(3M)\). The rational \(e^\Lambda\ne1\) is a ratio of distinct positive integers. Before any cancellation, either its numerator or its denominator is at most \(p2^\ell\), by splitting on the sign of \(s_i-s_j\). Consequently \(|\Lambda|\ge\log(1+1/(p2^\ell))\ge1/(p2^\ell+1)\). At least one arm has an odd departure at most \(h(p2^\ell+1)/3\). In particular the result for a same-date meeting needs no theorem about linear forms in logarithms.

**A smaller-factor crossing is usually necessary at short time lags.** Fix \(C>0\), put \(L=\log X\), and sample uniformly from the actual semiprime family in \((X,2X]\). Uniformly for \(0\le\eta\le1\), except on a proportion \(O_C(\eta+1/\log L)\), every meeting at dates \(i,j\) satisfying
\[
    \max(i,j)\le CL,\qquad |i-j|\le\eta\,p/L
\]
has an earlier odd departure below \(p\) on at least one of the two arms. Taking \(\eta=0\) gives the same-date statement with \(O_C(1/\log\log X)\) exceptional proportion. One may let \(\eta\) tend to zero arbitrarily slowly, allowing growing time lags. The assertion includes products for which no such meeting occurs.

Indeed, if no odd departure is below \(p\), then with \(a=i-j\) some integer \(r\) satisfies
\[
  |\log(p/(2^a3^r))|\le CL/(3p),\qquad |p-2^a3^r|\le KL,
  \quad K=\max(2,Ce^{C/3}/3).
\]
Here \(p>L\) and \(e^u-1\le ue^u\) for \(u\ge0\). The primes \(p\in(L,4KL]\) have reciprocal sum \(O_C(1/\log L)\) by the ordinary prime-counting upper bound. For all other primes use dyadic bands \([P,2P]\) with \(P\ge 2KL\). There are \(O(\log L)\) such bands through \((\log(2X))^2\). Each admits \(O(1+\eta P/L)\) integers \(a\). For each \(a\), only \(O(1)\) geometric centers \(2^a3^r\) lie within \(KL\) of the band, since \((2P+KL)/(P-KL)\le5\). Brun–Titchmarsh bounds the number of primes within \(KL\) of each center by \(O_C(L/\log L)\). After weighting by \(1/P\), the reciprocal mass per band is \(O_C((L/P+\eta)/\log L)\). The \(L/P\) terms have bounded geometric sum. Hence the total exceptional reciprocal mass is \(O_C(\eta+1/\log L)\). Each \(p\) contributes \(O(X/(p\log X))\) possible products. Divide by the family count \((\log 2+o(1))X/\log X\) from the [first-passage note](README.md). [Montgomery and Vaughan, Brun–Titchmarsh](https://doi.org/10.1112/S0025579300004708)

## An integer clock bound

There is also an elementary pointwise bound. If \(T^i(pq)=T^j q\) and \(h\ge\max(i,j)\), then \(q+2^h\le3^h\). Indeed the affine numerator \(A_w\) of any realized word of length \(i\) satisfies \(A_w+2^i\le3^i\) by induction. Padding to common denominator \(2^h\) bounds each padded numerator by \(3^h-2^h\). Equality of the two actual endpoints forces an integer multiple of \(q\) to equal the difference of the two padded numerators. The coefficient is nonzero since only one slope contains the prime \(p>3\). This excludes every common vertex in the specified time window, even when the two clocks differ. The proof is formalized as \(\texttt{factor_merger_height}\). [Finite kernel](FactorClock.lean) · [PR #217, earlier two-source affine argument](https://github.com/GettysburgResearch/collatz/blob/85b48ef9de755fe016166592cb048167c83fb7e8/research/astra-collision-factor-bridge-20261128/factoring/MULTIPLIER_CERTIFICATE_RIGIDITY.md)

## Localization at the actual minimum clocks

**SOURCE-QUALIFIED.** Use the prime sampling in (1) of the [factor-clock note](README.md), with \(pq\in(X,2X]\) and \(\log X\le p\le(\log(2X))^2\). Under Leen's ordinary timing and fusion inputs, for every fixed \(\epsilon>0\) and for \(J'=J\) or \(J'=J_=\),
\[
 \sup_p\Pr\!\left(J'(pq,q)<\infty,\
   \left|J'(pq,q)-\max(\tau_*(pq),\tau_*(q))\right|>
                      \epsilon\sqrt{\log X}\right)\longrightarrow0.       \tag{2}
\]
The probability here measures the indicated intersection of events. A bound on the probability of eventual meetings would be a separate result.

**The two marginal bounds.** For either source, uniformly in \(p\), its minimum is tight as an integer mark and \(\tau_*=\mu\log X+O_P(\sqrt{\log X})\). With \(B_X=\exp((\log X)^{1/4})\), the probability of missing \(B_X\) tends to zero, and \(\tau_*-\tau_{B_X}=o_P(\sqrt{\log X})\) on visits, where the crossing uses a strict inequality. The larger-factor source is sampled as primes at scale \(X/p\), while the product uses odd multiplier \(p\) at scale \(X\). Apply the upper sampling estimate (3) in the factor-clock note on these two fibres. For the ordinary input the centered capped passage to \(B_X\) and the centered minimum clock differ by \(o_P(1)\) in units of \(\sqrt{\log X}\), by the uniform-topology Brownian limit and continuity at its endpoint. One may use \(B_X/2\) and \(2B_X\) to bracket a strict crossing. The center shift is \(O((\log X)^{1/4})\). Events concerning the minimum clock can first be restricted to a visit below any fixed sufficiently large \(R\). The discarded mass vanishes as \(R\to\infty\). All starting parameters in these octaves stay above \(B_X\) through the early fusion cutoff, so the relevant events are unchanged by an early fusion. The two marginal estimates require no independence. [Leen, fate–clock invariance principle](https://doi.org/10.5281/zenodo.23269488) · [Leen, uniform pair-fusion cylinders](https://doi.org/10.5281/zenodo.23268751)

**Lower bound in (2).** Truncate to both minima at most \(R\), then take \(R\to\infty\) after the limit in \(X\). On events of probability arbitrarily close to one it suffices to consider horizons \(O(\log X)\) for the lower bound, since the two minimum dates are \(O_P(\log X)\). If both arms meet before either minimum has been reached, their remaining times to their respective minima are identical, because the remaining trajectories are identical and both first minima lie in that common future. Bound (1) implies that one arm has already passed below \(B_X\), since \((1+\log p)\log(2+\log X)=O((\log\log X)^2)=o(\log B_X)\). That arm, and hence both arms, is within \(o_P(\sqrt{\log X})\) dates of its minimum. If both arms are past their minima, the lower bound holds directly. In the mixed case, the meeting vertex lies on the forward orbit of the already attained bounded minimum \(r\) and has the other bounded minimum \(s\) in its future. Its remaining time to the next \(s\) has a finite bound depending only on \(R\). For each of the finitely many pairs \(r,s\le R\), either the orbit of \(r\) visits \(s\) once and the eligible positions form a finite initial segment, or it repeats \(s\) and its eventual cycle bounds every later wait. Thus every such meeting also satisfies the lower bound.

**Upper bound in (2).** Fix bounded minimum labels \(r,s\le R\) with a common future. They have a common vertex reached at two finite offsets, bounded in terms of \(R\) by the finite choice of pairs. Adding the source minimum dates therefore bounds \(J\) by their maximum plus a constant depending on \(R\). For \(J_=\), if the shared future is aperiodic then two different positions on that forward ray can never meet at equal later times. If a same-date meeting exists, the two entrance offsets to the common ray therefore give the same absolute date. If the shared future is periodic, both arms reach the same fixed cycle within bounded offsets from their minima, and eventual same-date meeting forces equality as soon as both are on the cycle, by injectivity of its rotation. This proves the upper bound uniformly after truncation.

In particular, for each fixed \(\delta>0\), the probability of any common vertex of \(pq\) and \(q\) with both dates at most \((\mu-\delta)\log X\) tends to zero. This includes nonsynchronous meetings. In the same sampling the product typically drops below the numerical value \(q\) after only \(\mu\log p+O_P(\sqrt{\log p})\) steps. Reaching below a factor and meeting that factor's actual orbit take substantially different amounts of time. The estimates leave open whether the product and factor ever meet for every member of the semiprime family.
