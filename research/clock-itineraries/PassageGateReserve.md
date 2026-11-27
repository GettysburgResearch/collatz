# The critical fractional sum and actual new mass in the five-eighths test

The binary gate and reciprocal mass from PR 212 are
\[
 G_N(x)=\{5i\le8c_i(x)\ (0\le i\le N)\},\qquad
 H_N=\sum_{0<x<2^N,\ G_N(x)}x^{-1}.
\]
Here \(c_i(x)\) is the number of odd departures in the first \(i\) shortcut steps. The Lean theorem in PR 212 identifies full positive Collatz with \(\forall B>0\ \exists N>0,\ H_N<1/B\). Its reserve \(R_M\) covers all later births \(J_{M,N}=\sum_{2^M\le x<2^N,\ G_N(x)}1/x\) by \(J_{M,N}+R_N\le R_M\). [PR 212, finite extinction and reserve](https://github.com/GettysburgResearch/collatz/blob/8cac31f51d9a5a2bd03c211495dec8f90c2aa48e/research/astra-infinite-descent-20261127/root/README.md)

Put \(r=5/8,\ d=H_2(r),\ \rho=2^{d-1}\). All conclusions here use elementary ballot counting. The separate dictionary-height theorem used in the odd-clock pressure estimate is unnecessary for this fixed binary clock.

## Sharp scale for genuinely born mass

For all \(M\ge1\),
\[
 R_M\asymp \sup_{N\ge M}J_{M,N}
       \asymp J_{M,M+1}
       \asymp \rho^M(1+M)^{-3/2}.                                  \tag{1}
\]
The bounds up to absolute constants refer to arbitrarily large \(M\). To obtain the lower bound at every small \(M\) as well, the all-odd length-\(M+1\) word gives \(J_{M,M+1}>0\).

More generally, for \(1\le M<N\le8M/5\), let \(l=\lceil5N/8\rceil\). Then
\[
 J_{M,N}\ge 2^{-M-1}\binom Ml/M .                                   \tag{2}
\]
Of all length-\(M\) binary words with \(l\) ones, at least \(\binom Ml/M\) have all their prefixes above the line of slope \(l/M\). Rotate each word after a minimum of its partial sums centered at \(l/M\). The selected physical residue \(0\le x<2^M\) passes \(G_M\). Its upper lift \(x+2^M\) has the same first \(M\) bits. For every \(M<i\le N\) that lift already has \(8c_i\ge8l\ge5N\), irrespective of its later bits. These distinct ordinary representatives in \([2^M,2^{M+1})\) each contribute at least \(2^{-M-1}\). For \(N=M+1\), \(l=rM+O(1)\), so (2) and Stirling give the lower estimate in (1). [PassageGateReserve.lean](mathlib/PassageGateReserve.lean) certifies that every paid parent gives its own actual upper representative, and bounds \(J_{M,N}\) below by the number of paid parents divided by \(2^{M+1}\). The cyclic enumeration is a written argument.

For an upper bound on \(R_M\), recall its exact weight \(2^{-M}(8c_M-5M+5)\) per passing residue. Under the mean-\(r\) Bernoulli tilt, the killed endpoint probability at \(u=c_M-rM\ge0\) is \(O((1+u)(1+M)^{-3/2})\). The elementary three-block proof appears in [the pressure argument](PassageGatePressure.md). Multiplication by the reciprocal probability of one word gives at most \(C2^{dM}(1+u)(1+M)^{-3/2}((1-r)/r)^u\) words. The extra factor \(8u+5\) is summable against the geometric tilt. The bound on \(J_{M,N}\) now follows from the cited complete-population reserve. The matching lower bound comes from the genuine upper lifts in (2). Thus this order describes the mass introduced on an actual later level as well as its reserve.

For \(P_N=2^{-N}\#\{0\le x<2^N:G_N(x)\}\), the same upper count and the central rotation lower give \(P_N\asymp \rho^N(1+N)^{-3/2}\) for \(N\ge1\). Positive-depth passing residues are nonzero and \(x^{-1}>2^{-N}\), hence \(H_N\ge P_N\). Also \(H_N\ge J_{N-1,N}\). Any finite certificate \(H_N<1/B\) therefore requires
\[
 (1-d)N+\tfrac32\log_2(1+N)\ \ge\ \log_2 B-O(1).                  \tag{3}
\]
The reciprocal scale of the single all-odd residue alone gives a weaker lower bound on the necessary native depth.

## A fixed physical clock below the first power

For real \(p\), write \(K_N(p)=\sum_{0<x<2^N,\ G_N(x)}x^{-p}\). Equivalently, \(2^{-(1-p)N}K_N(p)\) is the gated moment of order \(p\) of the payoff \(2^N/x\) for a uniform starting residue. Give the zero residue weight zero at positive depths. Then
\[
 \begin{array}{ll}
 K_N(p)\asymp_p 2^{(d-p)N}(1+N)^{-3/2}, & p<d,\\[2mm]
 \displaystyle\lim_{N\to\infty}K_N(p)=
      \sum_{x>0,\ G_j(x)\ {\rm for\ all}\ j}x^{-p}, & p\ge d .
 \end{array}                                                        \tag{4}
\]
In particular full positive Collatz is equivalent to vanishing of \(K_N(d)\), or to decay of the raw gated \(d\)-th moment as \(o(\rho^N)\). This little-oh estimate is open. For \(p<d\) the unnormalized sum diverges even if every positive orbit converges.

For the upper estimates let \(\mathcal D_B\) be the union of all positive ordinary passing representatives over all depths. In the shell \([2^k,2^{k+1})\), a witness necessarily passes \(G_k\). There is one source per \(k\)-bit residue. Its shell count is therefore \(O(2^{dk}(1+k)^{-3/2})\) by the killed-ballot bound. The matching order for the cumulative count through \(X\) follows by taking all passing words at \(\lfloor\log_2X\rfloor\) and using rotation. Consequently the tail above \(Y\ge2\) of \(\sum_{x\in\mathcal D_B}x^{-d}\) is \(O((1+\log Y)^{-1/2})\). For \(p<d\), the sum of the shell upper bounds weighted by \(O_p(2^{-pk})\) is dominated by its last scales. The accepted upper lifts from \(M=N-1\) provide the matching lower bound at depth \(N\) for every such \(p\). For \(p\ge d\), each fixed positive \(x\) is eventually below \(2^N\), and its gate indicators decrease with \(N\). Summable domination gives (4).

For all \(N\ge1,\ Y\ge2\) the finite masses satisfy
\[
 H_N\le K_N(d)\le Y^{1-d}H_N+C(1+\log Y)^{-1/2}.                  \tag{5}
\]
The first inequality holds term by term. To get the upper bound, split at \(Y\) and use the critical tail. PR 212's equivalence, or its finite certificate and (5), now gives the asserted equivalence at \(d\). A fixed permanent \(x\) contributes its full \(x^{-d}\) at all large \(N\). The varying division total \(A_n\) in the original odd-word trace introduces an extra factor \(2^{-(1-p)(A_n-n)}\) after normalization there. This accounts for the different endpoint behavior in [the odd-word pressure theorem](PassageGatePressure.md).

The weighted finite-to-infinite passage is kernel-checked for every real exponent under a displayed summability hypothesis on all passing ordinary representatives. The ballot argument above supplies this hypothesis for \(p\ge d\). [PassageGateCritical.lean](mathlib/PassageGateCritical.lean)

The same proof of (1)–(5) applies to PR 213's separate native gate \(4i\le7c_i(x)\), with \(r=4/7\) and its own linear reserve \(2(7c_N-4N)+8\). Its endpoint convention \(0<x\le2^N\) agrees with the strict upper bound at positive depths, since \(2^N\) starts even. Use \(l=\lceil4N/7\rceil\) for the paid upper lifts, and \(d=H_2(4/7)\). The generalization to that gate is written. [PR 213, native extinction and full reserve](https://github.com/GettysburgResearch/collatz/blob/de6384b4a232b996add4f5c620929d06a1982e90/research/astra-diagonal-frontier-20261127/NATIVE_GATE.md)
