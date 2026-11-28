# A four-rank sign reversal under a common binary calendar

For an ordered three-grade cycle let \(L_r\) denote the integer or rational folded labels, extended by \(L_{r+p}=2L_r\), and \(q=2^{1/p}\). The frozen three-column theorem proves the sign of \(L_r-2L_{r+b}+L_{r+c}\) agrees with \(1-2q^b+q^c\) on sufficiently short rank intervals of ordinary candidates. Consider the four-column extension
\[
              H_r=L_r-L_{r+1232}-L_{r+3828}+L_{r+5043}.
\]
At \(p=190537\) its ideal coefficient is strictly positive. The following two **different** objects use the same full binary valuation word of total clock \(A=301994\). They show which hypotheses are still needed for an ordinary four-rank sign theorem. [Three-column theorem at 100ba85](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-diagonal-20261127/arithmetic/SHORT_RANK_MIDPOINTS.md)

| Object | Actual ordinary source or cycle conditions | Four-rank result |
|---|---|---|
| One positive rational cycle | Every one of the \(190537\) cyclic affine transitions holds exactly. The primitive cycle has binary native valuations, the canonical three-grade band and the complete reduced denominator \(2^{301994}-3^{190537}\). | The same four fixed offsets give both signs along this one orbit. |
| One finite ordered integer array | Every phase is an odd positive unit modulo three in the bounded physical band. Its actual native valuation agrees at every rank with the same cyclic valuation word. Four marked six-edge paths, and \(45971\) chronological edges in all, give exactly their assigned successors. | The four marked paths have heights \(0,0,-1,-2,-1,0,0\). Somewhere else in the array the native successor differs from the assigned successor, with maximum difference 26. |

For **both** objects, every three-rank midpoint comparison for \(0<b<c\le6000\) has its prescribed strict sign at every one of the \(190537\) ranks, including octave wraps. A four-rank proof restricted to ordinary cycles could still use exact global integrality and closure together. These controls already obey the asserted three-rank inequalities themselves. A claim using an unspecified smaller short-arc constant on arbitrarily large periods requires a separate quantifier.

## One globally exact rational cycle

Use initial coordinates with \(r_j=jA\bmod p\), \(b(r)=\lfloor(r+A)/p\rfloor\). Put \(k=A-p\). Mark four starting ranks \(r_*=2050\) plus the offsets \(0,1232,3828,5043\). At their next seven chronological dates, the lowbit tags in their common octave are
\[
 2222,\ 2442,\ 1222,\ 2224,\ 2124,\ 2244,\ 2222.
\]
These dates share the six mechanical letters \(1,2,1,2,1,2\). The complete tag list starts at the constant two and includes the specified lowbit rows. The few additional edits in the exact checker give tag four to the minimum and its necessary neighbors, and preserve the four marked integer sources' actual outgoing valuations at their final date. The finite implementation gives the literal entire word, including all edits.

For \(c=c_r,\ c'=c_{(r+A)\bmod p}\), set \(2^{a_i}=2^{b(r)}c'/c\) in chronological order. All values are exactly 2 or 4 and \(\sum a_i=A\). If \(E_i=\sum_{j<i}a_j\), put
\[
 K=\sum_{i=0}^{p-1}3^{p-1-i}2^{E_i},\qquad D=2^A-3^p>0 .
\]
The exact gcd is \(\gcd(D,K)=1\), so the ordinary rational starting phase \(K/D\) has denominator \(D\) in lowest terms. That denominator has 301971 bits and is coprime to six. The checker iterates all \(p\) reduced numerators using \(N'=(3N+D)/2^a\), verifying exact divisibility, oddness, the return to the identical initial numerator, \(\max x<16\min x/3\), the true minimum at rank zero and strict folded rank order. Since \(\gcd(A,p)=1\) the period is primitive. The two opposite signs even occur on the printed six-edge window. At its starting date \(H\in[20800,20804]/65536\). Two dates later \(H\in[-42136,-42132]/65536\). The full machine output includes every interval and the hash of the complete denominator.

## All short midpoint comparisons on both objects

The table uses outward integer enclosures of \(q^j\) on mesh \(2^{-110}\). A logarithm series encloses \(\log2\), a positive exponential polynomial with a geometric remainder encloses \(\exp((\log2)/p)\), and multiplication with directed rounding encloses its powers. For all \(0<b<c\le6000\), the checker obtains
\[
 p^2 |1-2q^b+q^c|>0.48,\qquad
 c\ne2b\ \Longrightarrow\ p^2 |1-2q^b+q^c|>5.5 .
\]
The smallest comparison has \((b,c)=(1,2)\). For fixed \(b\), the expression increases strictly with \(c\). Binary search and testing the neighboring intervals and eligible endpoints cover all comparisons, including those on either side of the excluded \(c=2b\) in the second estimate. For the four offsets,
\[
      0.0031<p^2(1-q^{1232}-q^{3828}+q^{5043})<0.0032 .
\]

For every rational folded label the literal arithmetic gives
\[
  \left|\frac{L_r}{1420491705477\,q^r}-1\right|<0.1/p^2 .
\]
The bound persists across the octave by doubling. Its possible effect on a midpoint comparison, normalized by the ideal scale at the first rank, is less than \(0.1(1+3q^{6000})/p^2<0.48/p^2\). This proves the simultaneous comparison for the rational cycle.

In the integer array put \(s=545709081523\). The four initial ordinary sources are \(1099587966023,\ 1104527209193,\ 1115007650569,\ 1119946893739\). Their 24 literal odd integer transitions and the same tags give the claimed signed sequence. To complete the entire rank array, the checker first assigns the closest label to \(4sq^r\) with the specified lowbit, actual native valuation and an ordinary odd part prime to three. It retains the imposed sources and the minimum. It then repairs finite neighborhoods of adjacent convexity failures. At each permitted integer \(z\) at the next rank, it keeps the greatest prior label \(y\) with some retained predecessor \(x\) satisfying \(x+z>2y\). The greatest such \(y\) dominates smaller choices in the next comparison; the stored predecessors reconstruct a path. The two fixed labels on each side of a repaired interval preserve the outside inequalities. Finally it verifies strict cyclic convexity everywhere, all ordinary valuations, and
\[
  \left|\frac{L_r}{4s q^r}-1\right|<0.5/p^2 .
\]
Convexity gives every equal-spacing comparison by summing adjacent second differences. For unequal spacings \(0.5(1+3q^{6000})<5.5\) gives all the remaining signs. This finite array has no claim to the simultaneous affine return, or to the known lower period and minimum of a hypothetical positive integer cycle.

## Arbitrarily long ordinary finite windows

There is also a genuine mechanical sign reversal with an arbitrary number of physical predecessor and successor tests. At initial angular phase \(1/6\), take the twelve mechanical letters from \(\lfloor1/6+j\gamma\rfloor\), \(\gamma=\log_2 3\). The thirteen successive tag tuples are
\[
 2222,\ 2442,\ 1222,\ 2444,\ 2224,\ 2124,\ 4224,\ 
 2122,\ 4244,\ 2242,\ 1242,\ 2244,\ 2222 .
\]
With signs \(w=(1,-1,-1,1)\), the transported heights are
\(0,0,-1,-2,-2,-1,0,1,2,2,1,0,0\). At each step \(2^b H'=3H+\sum w_i c_i\), every induced native exponent is one or two, and tag one occurs only below the high-rank cutoff. Constant tag two pads both ends through any prescribed number of ordinary mechanical letters. All four columns then have the same total native exponent \(B\), their physical carries obey \(\sum w_iK_i=0\), and ordinary starting residues modulo \(3\cdot2^{B+1}\) may be chosen with \(\sum w_i x_i=0\). Indeed their signed residue sum is zero modulo this modulus, so correct the fourth representative by that multiple. The exact cyclic parity condition is unnecessary for the resulting four finite paths. Positive lifts may be made arbitrarily high by adding multiples of the modulus that preserve the signed sum. This is the same finite-cylinder argument as in the [higher-difference construction](HIGHER_DIFFERENCES.md).

For these finite windows, choose a large fixed integer \(B_0\) and unequal endpoint rank gaps \(B_0,B_0-1\). At a large rank period \(p\), set
\[
 c=\operatorname{round}\!\left(p\log_2\frac{q^{B_0}-1}{q^{B_0-1}-1}\right),\qquad
 d=c+B_0-1 .
\]
The offset list \(0,B_0,c,d\) has ideal tetrad \(O_{B_0}(p^{-2})\). The relative middle spacing tends to \(\log_2(B_0/(B_0-1))\), which can be made smaller than all positive seam margins in any one fixed padded window. Then all four dates really share the mechanical calendar and the grade cap on the complete window. Their two middle-separated gap scales make the midpoint signs of the four selected triples stable under small relative perturbations. At the first date choose three source representatives within a bounded distance, depending on the padding, of their ideal target values. Choose the fourth by the signed relation. Its added error is \(O_{B_0}(s/p^2)\), and after a bounded number of affine steps the homogeneous multiplier correction adds \(O_{\rm pad}(s|A/p-\gamma|)\). Taking lifts sufficiently high achieves the strict physical band with floor tending to infinity. This is a finite ordinary construction with four parallel columns. The first part of the note separately gives one complete periodic rational obstruction and an entire static integer midpoint array.

[Exact full-denominator and integer-array replay](check_tetrad_rank.py) · [Recorded controls](tetrad_rank_controls.json)
