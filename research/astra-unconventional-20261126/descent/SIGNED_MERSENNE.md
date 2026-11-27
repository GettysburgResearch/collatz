# Signed descent inside the rank-three Mersenne family

**Proposed new signed seed and canonical subprogressions.** Let \(m=11+162j,\ j\ge0\), and \(z=(2^{m+7}-271)/81\). The center \(-1293643/3^9\) enters the stable all-odd bridge. Each additional lower odd buys a \(2/3\) height factor. At \(k=80\), one explicit exponent progression gives an ordinary source \(W<z/2^{40}\) with both original component labels and an exact \(+85\) upper-odd cost on every supplied hit. Three more ternary digits give a strictly smaller **canonical** parent \(Y\) already for \(k\ge9\). All these deep progressions project to \(j=3533\bmod19683\). These claims specify which original indices are covered. [Physical kernels](SignedMersenne.lean) · [Ternary lifting](SignedIndex.lean) · [Cofinal broad theorem](SignedHardFamily.lean) · [Cofinal canonical theorem](SignedNarrow.lean) · [Finite checks](signed_mersenne.py) · [Replay](../../../reports/astra-unconventional-20261126/descent/signed_mersenne.json)

**Prior scope.** PR197 already proves cofinal hard parents admitting arbitrarily large height gains by a different cycle. It obtains a contraction \(2048/2187\) per seven extra lower odds and gives a \(2^{40}\)-gain criterion at 405 laps. Its narrow positive-depth progressions project to \(j=3122\bmod19683\). The rows at \(5903,1286\bmod6561\) below are exactly two of its earlier canonical reductions. The uniform row using 623 is the known \(17\leftrightarrow11\) unit exchange. We give these as controls. The different seed, its address, the faster contraction and the exact upper-certificate accounting are the advances here. [Earlier unbounded theorem and finite classes](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/unbounded-queries/README.md) · [Earlier canonical two-center rows](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/paired-reductions/MersenneTwoCenter.lean) · [Earlier unit exchange](https://github.com/GettysburgResearch/collatz/blob/f74d2144275c3e1f9148b0b2997fecc7931ae7f5/research/ayh-resource-reset-20261124/unit-exit/UnitResidueExchange.lean)

## How the signed source determines an ordinary row

For an odd-denominator signed rational \(b\), determine parity from its numerator and use the ordinary formulas \(x/2,(3x+1)/2\). Suppose \(b=-u/3^r\) reaches \(-1\) at clock \(h\) with \(r\) odds, and \(3b\) reaches zero at clock \(h+2\) with \(r-1\) odds. Set
\[
  Z=\frac{2^{m+h}-u}{3^r}.
\]
Whenever \(Z\) is a positive integer, \(m\ge2\), its lower arm reaches \(2^m-1\) at clock \(h\) with \(r\) odds, and \(3Z\) reaches \(2^{m-2}\) at clock \(h+2\) with \(r-1\) odds. Indeed \(Z-b=2^{m+h}/3^r\), so its first \(h\) binary decisions match \(b\); the upper shift has the same binary divisibility through \(h+2\). Equivalently one can calculate the least nonnegative source residue modulo \(2^{h+2}\) and apply the integer prefix-lift theorem. Lean uses this latter proof on positive ordinary lifts alone.

| \(u\) | \(r\) | \(h\) | Upper odd count | Application |
|---:|---:|---:|---:|---|
| 271 | 4 | 7 | 3 | Original canonical hard source |
| 623 | 5 | 8 | 4 | Known uniform unit exchange |
| 1,293,643 | 9 | 19 | 8 | Stable family giving arbitrary height gain |
| 2,692,031 | 12 | 18 | 11 | Known first canonical row |
| 4,970,719 | 12 | 19 | 11 | Known second canonical row |

The first two signed lower and upper basins are \(-1\) and 0, respectively. This differs from insisting that both nonnegative low representatives hit 1. The underlying hard family and its nonnegative-origin exclusion are prior results. [Hard family](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/MersenneBarrier.lean) · [Nonnegative-origin exclusion](../../astra-literature-closure-20261125/carry/README.md)

For all \(m=11+162j\), the second source
\[
 Z_4=\frac{2^{m+8}-623}{243}
\]
is integral: \(2^{162}=1\bmod243\) and \(2^{19}=623\bmod243\). The identities for the original \(z\) and \(Z_4\) give \(3Z_4=2z-1\); hence \(0<Z_4<z\). The first four departing upper odds now lead to the same \(2^{m-2}\) as the original three. Consequently every supplied upper hit transfers with one extra clock and one extra odd departure. Here \(Z_4\equiv11\bmod16\). Minimality restricted to canonical sources cannot use the size reduction alone.

For \(j\equiv5903\bmod6561\) the fourth row is integral and \(Z\equiv17\bmod48\). For \(j\equiv1286\bmod6561\) the fifth row has the same properties. To check these classes, solve
\[
  2^{11+h+162j}\equiv u+2\cdot3^{12}\pmod{3^{13}}.
\]
The seed in each row gives \(Z\equiv1\bmod16\), and the displayed congruence gives \(Z\equiv2\bmod3\). Their limiting ordinary heights relative to \(2^m\) are \(2^{18}/3^{12}\) and \(2^{19}/3^{12}\), both below 1. Direct subtraction gives \(0<Z<z\) on both progressions. The upper certificate gains eight odds, with eleven or twelve additional clocks. Either row excludes its original source as the least canonical reverse disagreement by ordinary size.

## Arbitrary height gain with a fixed ordinary certificate

Write \(Z_0=(2^{m+19}-1293643)/3^9\) from the third row and suppose \(3^k\mid Z_0+1\). The row has \(Z_0\equiv7\bmod8\). There is a positive integer \(t\) such that
\[
 Z_0+1=8\cdot3^k t,\qquad W_k=8\cdot2^k t-1.
\]
The \(k\) all-odd clocks take \(W_k\) to \(Z_0\). Also \(T^3(3W_k)=9\cdot2^k t-1\) and \(T^3(3Z_0)=9\cdot3^k t-1\), with one odd in each three-clock opening. Another \(k\) all-odd clocks takes the former upper value to the latter. This is the previously known stable all-odd bridge, used in the direction that makes an ordinary source smaller. Its entry from this rank-three hard family is furnished by the signed row above. [Prior stable bridge](../../astra-ultra-closure-20261125/bridge/README.md) · [Prior signed Mersenne selections](../../astra-minimum-source-20261124/descent/README.md)

It follows that \(W_k\) reaches \(2^m-1\) at clock \(19+k\) with \(9+k\) odds. Its upper \(3W_k\) reaches \(2^{m-2}\) at clock \(21+k\) with \(8+k\) odds. If \(T^H(3z)=1\) is **any** supplied upper hit, then \(H\ge9\) because the value at clock nine exceeds 2 and 1 stays in the two-cycle thereafter. Appending the original suffix gives
\[
  T^{H+k+12}(3W_k)=1,\qquad
  Q_{H+k+12}(3W_k)=Q_H(3z)+k+5 .
\]
The positive lower sources \(W_k,z\) already meet at \(2^m-1\). Thus \(W_k\) is bad exactly when \(z\) is bad.

For *each* \(k\ge0\) the necessary parameter condition is obtained from
\[
  2^{30+162j}\equiv 1273960 \pmod{3^{9+k}}.
\]
Both sides are \(154\bmod243\), and \((2^{162}-1)/243\equiv1\bmod3\). Cubing shows \(2^{162\cdot3^d}=1+3^{5+d}u_d\) with \(u_d\equiv1\bmod3\). Testing \(j,j+3^d,j+2\cdot3^d\) at the next digit yields exactly one lift. Hence one class of \(j\bmod3^{k+4}\) works at every \(k\). Every member gives a positive integral \(Z_0\), since \(m\ge11\); divisibility of \(Z_0+1\) by \(8\cdot3^k\) gives positive \(t\).

We have \(W_k<2^{m+19+k}/3^{9+k}\) and \(z>2^m\) for \(m\ge11\). In particular \(2^{139}<3^{89}\) gives \(2^{40}W_{80}<z\) throughout the corresponding infinite exponent progression. The least nonnegative \(j\) for this progression is \(316349119100033932501317109648148925116\) modulo \(3^{84}\). For any hypothetically bad \(z\) in the progression, the earlier quantitative return applied to the bad physical value \(W_{80}\) gives a canonical reverse disagreement strictly below \(z\). No first-hit rank comparison is needed. More generally take \(k\) with \(2^{D+19+k}<3^{9+k}\) for any desired factor \(2^D\). Selecting \(j\) in one full period between \(3^{k+4}\) and \(2\cdot3^{k+4}\) gives ordinary \(m\asymp3^k\) and \(W_k/z\ll m^{-\log_3(3/2)}\). [Earlier quantitative return](https://github.com/GettysburgResearch/collatz/blob/156652e03fe7a78f9cd4442039779cc622fdf3de/research/ayh-resource-reset-20261124/closing-proposal/QuantitativeReturn.lean)

## A shorter canonical descent with three more ternary digits

Require \(W_k\equiv10\bmod27\). The bridge also gives \(W_k\equiv7\bmod8\), hence \(W_k=199+216t'\). Put
\[
   Y=(16W_k-7)/9=353+384t'.
\]
Then \(Y\equiv17\bmod48\), \(T^4Y=W_k\) with two odds, and
\[
    T^7(3Y)=224+243t'=T^3(3W_k).
\]
The two upper prefixes use three odds and one odd respectively. These are identities on the full binary cylinder, obtained by lifting the physical words at \(353,1059,597\). Consequently \(Y\) reaches the original \(2^m-1\) after \(k+23\) clocks and \(k+11\) odds. The upper \(3Y\) reaches \(2^{m-2}\) at \(k+25\) clocks and \(k+10\) odds. Every supplied upper hit \(H\) from \(3z\) transfers to a hit \(H+k+16\) from \(3Y\) with exactly \(k+7\) added odds.

For each \(k\ge0\), choose the single residue of \(j\bmod3^{k+7}\) solving
\[
  2^{30+162j}\equiv 1273960+3^{9+k}\,11\cdot14^k
           \pmod{3^{12+k}} .
\]
Its right side is \(154\bmod243\), so the same one-digit lift gives existence and uniqueness. Now \((Z_0+1)/3^k\equiv11\cdot14^k\bmod27\). Multiplication by \(2^k\) gives \(W_k+1\equiv11\bmod27\) because \(28\equiv1\bmod27\). The valuation \(v_3(Z_0+1)=k\) makes the canonical progressions for different \(k\) disjoint. For \(k\ge9\) they all project to \(3533\bmod19683\).

Finally \(Y<(16/9)2^{m+19+k}/3^{9+k}\) and \(z=(128\cdot2^m-271)/81\). The inequality \(32\cdot2^{19+k}<27\cdot3^{9+k}\) holds at \(k=9\) and propagates upward. It gives \(Y<(3/2)2^m<z\) for \(m\ge11\). Hence a least canonical reverse disagreement cannot occur at any of these parents. This direct smaller canonical representative uses the actual supplied upper suffix and avoids the \(2^{40}\) return cost on its narrower class. At \(k=9\) it costs sixteen additional upper odds. [Strict cofinal canonical theorem](SignedNarrow.lean)

## Why the single extra odd is needed for the uniform row

Consider the signed two-center template in which \(b=-u/3^r\) is in lowest terms and \(T^h b=-1\), whereas \(3b\) reaches zero. Assume its lower ordinary trajectory meets a point in the initial all-odd phase \(3^i2^{m-i}-1\), with \(i\ge0\). If \(e\) even clocks and \(\ell\) odd clocks precede the first signed \(-1\), comparing slopes gives \(i=\ell-r\) and the ordinary source coefficient \(\alpha=2^{e+r}/3^r\). All later signed clocks at \(-1\) are odd and leave \(e\) unchanged. An odd inverse from zero introduces denominator three, and each subsequent odd inverse raises that denominator exponent by one. Thus the upper signed count is \(r-1\). Integer \(b\ne0\) cannot have \(3b\) reaching zero.

To have at most the original three upper odds requires \(r\le4\). To improve the leading height coefficient \(128/81\) then requires \(e\le2\). Enumerate backwards from \(-1\): an even inverse doubles the signed reference, an odd inverse sends it to \((2b-1)/3\). Ignore the fixed odd inverse of \(-1\), stop past two evens or denominator 81, and keep references whose triple reaches zero. The only survivors after the height test are
\[
 -35/27,\quad -70/27,\quad -97/81,\quad -149/81,\quad -194/81.
\]
None yields an ordinary source at \(m=11\bmod162\). In the integer phase preceding the first denominator, every allowed odd inverse away from \(-1\) strictly decreases absolute value; hence the described finite search is exhaustive. A denominator divisible by three never decreases in the inverse recursion. This verifies the necessity of the one extra upper odd *in this signed template*. [Exact census](signed_mersenne.py)

## What the congruence selection leaves open

The earlier uniform \(Z_4\) row buys a \(2/3\) height ratio and changes the canonical class. The large gain requires a congruence of depth \(9+k\) depending on \(k\). A least canonical defect in a different hard exponent class need not supply this congruence. The accompanying counting argument quantifies the restriction over the full signed inverse tree. [Signed-seed counting bound](SIGNED_COVERAGE.md)

The postpeak comparison gives a different density-one exclusion inside any of these ternary progressions, using the previous affine-pair absorption bound. [Postpeak density](POSTPEAK_DENSITY.md)
