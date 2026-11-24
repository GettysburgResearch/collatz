# The complete denominator at every fixed interior clock density

**PROPOSED.** Let a circular binary word have length \(A\), weight \(0<p<A\), and distinguished initial bit. Put \(D=2^A-3^p\), let \(C\) be its shortcut affine carry, and let \(d=|D|/\gcd(|D|,C)\). Write \(u=p/A\), \(M=\max(2^A,3^p)\). Along *any* sequence with \(u\) in a compact subinterval of \((0,1)\), under uniform sampling at those exact clocks,
\[
 \Pr\{d\le M^{1-\epsilon}\}\le e^{-c_\epsilon A+o(A)}
 \qquad(0<\epsilon<1).
\]
The constant also depends on the density interval. This estimates the complete reduced denominator and applies to both signs of the rational fixed point, to arbitrary clock gcd, and likewise to primitive words conditional on primitivity. The contracting fixed-clock estimate in PR195 §2 reached the entropy exponent \(Ah(u)\), below \(A\log2\) away from one half. Its stronger full exponent when *mixing* all positive weights is an antecedent. [PR195, closing cycles §2, frozen head](https://github.com/GettysburgResearch/collatz/blob/b69ec87d28f539233a32b7c07964f5605320eb71/research/astra-global-closure-20261124/closing/cycles/README.md)

## Finite bounds before taking limits

The two shortcut branches are \(x/2,(3x+1)/2\) at even and odd numerator, for rationals with odd denominator. The affine fixed point \(C/D\) realizes the word at every rotation. The numerator at each odd step has the required parity by reducing the rotated carry modulo two. The full reduced denominator is common to all phases since \(D\) is coprime to six. All phases have the sign of \(D\). This is the classical rational parity-vector formula. [Brent, §2, BSL theorem](https://citeseerx.ist.psu.edu/document?doi=8d82ff52f741af800edeb8c0c350c2da8ffdac5e&repid=rep1&type=pdf)

Choose a minimum of absolute value over a lap. It occurs at an odd phase, since an even phase is halved. Write \(m\) for its positive cleared numerator and \(g=|A\log2-p\log3|>0\). At consecutive odd phases, the magnitudes \(y>0\) obey \(2^e y'=3y+\operatorname{sgn}D\). In the negative case every such \(y>1/3\). Multiplying gives in both signs
\[
 m/d\le Q:=\tfrac13(1+p/g).
\]
For positive sign use \(g\le p/(3\min y)\). For negative sign, \(g\le -p\log(1-1/(3\min y))\) gives \(\min y\le(3(1-e^{-g/p}))^{-1}\le(1+p/g)/3\).

Fix a cutoff \(Y\ge1\). If \(0\le k\le A\) and \(2^k\ge YQ\), then the number of marked words at these clocks with \(d\le Y\) is at most
\[
 A\tau(|D|)e^{Ah(u)} \max(u,1-u)^{A-k}. \tag{1}
\]
Here \(h(u)=-u\log u-(1-u)\log(1-u)\). Fix a divisor \(d\le Y\) of \(|D|\). Two minima with the same first \(k\) bits differ in cleared signed numerator by a multiple of \(2^k\), by subtracting the common affine equations. Positive magnitudes lie in \([1,YQ]\), so the difference vanishes. A minimum with this denominator determines its necklace by forward determinism. Under iid Bernoulli-\(u\) bits every length-\(A\), weight-\(p\) word has mass \(e^{-Ah(u)}\). Every extendible prefix of length \(k\) has mass at least \(e^{-Ah(u)}\max(u,1-u)^{-(A-k)}\), since the probability of any particular compatible suffix is at most \(\max(u,1-u)^{A-k}\). Sum the disjoint prefix probabilities and allow all divisors and at most \(A\) marks.

If \(0\le r\le p\) and \(3^r\ge YQ\), there is a second bound
\[
 A\tau(|D|)e^{Ah(u)}u^{p-r}. \tag{2}
\]
Specify the last \(r\) positive odd-to-odd gaps *ending* at the minimum. If the clocks sum to \(s\), the incoming equation is \(2^s n_{\rm end}=3^r n_{\rm start}+dC'\) for signed numerators. Thus this suffix determines \(n_{\rm end}\bmod3^r\); the difference of two endpoints is divisible by \(3^r\) even when the earlier states differ. The same minimum uniqueness argument applies. Give each successive gap \(e\ge1\) probability \(u(1-u)^{e-1}\), independently. All \(p\)-gap words of total \(A\) have probability \(e^{-Ah(u)}\). Every compatible tuple of \(r\) terminal gaps has probability at least \(e^{-Ah(u)}u^{-(p-r)}\), since each missing gap has probability at most \(u\). Distinct tuples of the same number of gaps are disjoint.

Lagarias, Lemma 2.2(1), gives \(g\ge (\log3/1200)A^{-13.3}\), hence \(Q=O(A^{14.3})\). The elementary divisor estimate \(\tau(|D|)=\exp(o(A))\) follows since \(|D|\le3^A\) and \(\tau(N)\ll_\delta N^\delta\) for each \(\delta>0\). For the latter, use \(v+1\le2^v\le q^{\delta v}\) at sufficiently large primes \(q\), and the finite product of \(\sup_{v\ge0}(v+1)q^{-\delta v}\) at the others. Take \(Y=M^{1-\epsilon}\) and use (1) with \(k=\lceil\log_2(YQ)\rceil\) when \(M=2^A\), or (2) with \(r=\lceil\log_3(YQ)\rceil\) when \(M=3^p\), at large \(A\). Divide by \({A\choose p}\ge e^{Ah(u)}/(A+1)\), the binomial mode bound at parameter \(u\). Imprimitive words number at most \(A e^{Ah(u)/2}\) by summing over repetition factors dividing both clocks. Finally \(|D|=M(1-e^{-g})=M\exp(-O(\log A))\). [Lagarias, Lemma 2.2(1)](https://arxiv.org/pdf/math/0512006)

The fixed-weight gain comes from charging only extendible prefixes, and on the expanding side from reconstructing the minimum from the past. A single primitive ordinary cycle contributes at most \(A\) rotations. This falls within the exceptional budget. An adjacent \(01\leftrightarrow10\) surgery at an ordinary cycle changes its full carry by a signed monomial in two and three, so that particular neighbor has denominator \(|D|\); this surgery does not amplify the small-denominator exception. The fixed-source issue has a different arithmetic constraint in the companion note.

## The two denominators on the same marked word

Let \(E=2^{A+p}-3^A\), \(M_*=\max(2^{A+p},3^A)\), and let \(b_*\) be the full reduced denominator of the closed companion \(2^{1+e_i}w_{i+1}=3w_i+e_i\). At the same fixed interior densities, the preceding conclusion holds *simultaneously* for \(d\) relative to \(M\) and \(b_*\) relative to \(M_*\). Also, uniformly for all \(0<p<A\),
\[
 \log\gcd(|D|,|E|)=o(A).                                         \tag{3}
\]
In particular, away from an exponentially small exceptional fraction, the logarithm of the least common multiple of the two reduced denominators is at least
\((1-\epsilon)(\log M+\log M_*)-o(A)\) for each fixed \(\epsilon>0\).

To check the second counting argument directly, the positive carry formula gives every companion phase the sign of \(E\) and a reduced denominator dividing \(|E|\). The numerator recurrences, with \(E\) coprime to six, preserve that denominator. Dyadic integrality of both sides forces the two disjoint branch residues in the [companion proof](README.md), including when the state is negative. Put \(g_*=|\log(2^{A+p}/3^A)|\). At the least magnitude \(y\) among all phases, the same signed product comparison gives \(y\le Q_*=(1+p/g_*)/3\). For a negative cycle the positive terms \(-\log(1-1/(3|w_i|))\) occur only at odd bits; if \(y\le1/3\) the bound is immediate, and otherwise all terms are at most \(-\log(1-1/(3y))\). Lagarias at denominator \(A+p\le2A\) makes \(Q_*\) polynomial. Use again at most \(A\) marks per necklace and at most \(\tau(|E|)=\exp(o(A))\) possible denominators.

For \(M_*=3^A\), the last \(r=\lceil\log_3(YQ_*)\rceil\) *bits* entering the least-magnitude phase determine its signed numerator modulo \(3^r\), since every companion step has numerator multiplier three. Take \(Y=M_*^{1-\epsilon}\). For large \(A\), \(0\le r<A\) and the mass bound for disjoint extendible \(r\)-bit suffixes is \(e^{Ah(u)}\max(u,1-u)^{A-r}\), exactly as in (1). For \(M_*=2^{A+p}\), put \(k=\lceil\log_2(YQ_*)\rceil\), and read a prefix, stopping on the *first* bit at which its accumulated companion clock \(\ell=j+P_j\) reaches \(k\). For large \(A\) every eligible word stops by length \(A\); the overshoot is at most one. The prefix determines the minimum numerator modulo \(2^\ell\) by the affine recurrence with odd numerator multiplier \(3^j\). The stopping prefixes have disjoint cylinders. The remaining length in bits satisfies \(A-j\ge(A+p-k-1)/2\), as each bit costs at most two clock units. Their number is at most \(e^{Ah(u)}\max(u,1-u)^{(A+p-k-1)/2}\). On both sides this gives exponential decay in the conditional fraction with \(b_*\le Y\). A union bound combines the two coordinate estimates without any independence assumption.

For (3) use the rational \(S\)-units \(U=2^A/3^p\), \(V=2^{A+p}/3^A\) for \(S=\{2,3,\infty\}\). The exponent determinant \(p(A+p)-A^2\) is always nonzero, since \(p/A\) cannot equal the irrational positive zero of \(x^2+x-1\). Thus \(U,V\) are multiplicatively independent for *every* pair of positive clocks. Corvaja–Zannier, Proposition 2, bounds the negative of the sum of \(\log^-\max(|U-1|_v,|V-1|_v)\) by \(\epsilon\max(h(U),h(V))\) outside finitely many pairs and finitely many one-dimensional subgroups through the identity. Independence removes all the subgroups. The remaining finite exceptions concern finitely many clock pairs by unique factorization. At every finite prime outside \(S\) the contribution is exactly its contribution to \(\log\gcd(|D|,|E|)\); neither divisor contains two or three. The omitted contributions are nonnegative after negating. Both heights are \(O(A)\), proving (3). This is an application of the complete-modulus torus gcd estimate, also used with different arguments in PR193. It gives no lower bound for \(d\) on the rare individual with \(d=1\). [Corvaja–Zannier, Proposition 2, (2.8)](https://arxiv.org/pdf/math/0311030)
