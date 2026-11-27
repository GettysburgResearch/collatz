# How many hard exponents the complete signed lower tree can cover

**PROPOSED written bound.** Consider every odd-denominator signed reference \(b<0\) that reaches \(-1\), including references whose triple has no known hit at zero. Put \(r=v_3(\operatorname{den}(b))\) for a denominator that is a power of three, and let \(e\) count the even clocks before the first signed hit of \(-1\). When a family \(Y=\alpha 2^m+b\) reaches the initial all-odd ascent of \(2^m-1\) uniformly in \(m\), integer compatibility forces the coefficient
\[
  \alpha=2^{e+r}/3^r.
\]
Indeed, if the signed prefix has \(\ell\) odds and the physical meeting is at \(3^i2^{m-i}-1\), comparison gives \(\alpha=2^{e+\ell-i}/3^{\ell-i}\). For nonintegral \(b\) in lowest terms the denominator of \(\alpha 2^m\) must match that of \(b\) at any integral source. This gives \(\ell-i=r\). A signed integer \(b\) cannot have its nonzero triple reach zero. The full tree used for the bound includes it harmlessly at \(r=0\).

For \(m=11+162j\), let \(\mathcal U_D\) be the union, over all such templates of coefficient \(\alpha\le2^{-D}\), of their integer-compatibility cylinders in \(j\in\mathbb Z_3\). Here a cylinder consists of the residues of ordinary \(j\) for which its source is integral, extended to their ternary congruence class. It disregards all later requirements on the upper component and on positivity. With
\[
 \theta=\tfrac32,\quad B=2^{-\theta},\quad A=(3/2)^\theta/3,
\]
the normalized ternary Haar mass is at most
\[
 \mu(\mathcal U_D)\ \le\
 \frac{243\,2^{-\theta D}}{(1-2B)(1-A-B)}.
 \tag{1}
\]
Both denominators are positive, since \(B=1/(2\sqrt2)\) and \(A=\sqrt{3/8}\). At \(D=40\) the upper bound is less than \(2.2\cdot10^{-14}\). Thus a finite union cannot handle every ordinary hard index with this leading coefficient. A countable union with small ternary Haar mass can contain every nonnegative integer, so (1) alone cannot settle unbounded-rank ordinary coverage.

## Counting all denominators and all even lengths

For fixed \(r,e\), the number \(N_{r,e}\) of distinct first-hit references is at most
\[
 N_{r,e}\le \sum_{i=0}^e2^i {r+e-i\choose r}.
\]
Read a signed inverse from \(-1\). On integer values \(b\le-1\) an odd inverse stays between \(b\) and \(-1\); an even inverse doubles the magnitude. After \(i\) even inverses there are at most \(2^i\) possible negative integers before the first denominator. Once a factor three appears, every odd inverse adds exactly one power of three to the reduced denominator and every even inverse preserves it. Hence the remaining word has \(r\) odd and \(e-i\) even symbols, including the first nonintegral odd inverse. Ignoring its required first position gives the binomial bound. The integer stage can be reconstructed from its last integer by the deterministic forward orbit ending at its first \(-1\).

Each template of rank \(r\) is compatible on at most one class of \(j\bmod 3^{\max(r-5,0)}\), by \(v_3(2^{162}-1)=5\) and the one-digit lift. Its contribution to the union is at most \(243/3^r\). When \(\alpha\le2^{-D}\), use \(1\le 2^{-\theta D}(3/2)^{\theta r}2^{-\theta e}\). Therefore the unrestricted sum is bounded by
\[
  243\,2^{-\theta D}\sum_{r,e\ge0}A^rB^e
              \sum_{i=0}^e2^i{r+e-i\choose r}
   =\frac{243\,2^{-\theta D}}{(1-2B)(1-A-B)}.
\]
This proves (1). The signed paired rows form a subset of this count, including all their paid all-odd extensions.

## A consequence on ordinary indices up to a rank cutoff

Put \(K=(3/2)^\theta/(1-B)<2.85\). The same enumeration, with the grade held at \(r\), bounds the number of small-coefficient templates at that grade by
\[
  \frac{2^{-\theta D}}{(1-2B)(1-B)}K^r.
\]
For \(0\le j<J\), counting one residue class of ordinary integers contributes at most one rounding error per template. Summing to \(r\le(1-\delta)\log_K J\) for fixed \(0<\delta<1\) adds \(O_D(J^{1-\delta})\) to \(J\) times (1). Thus, apart from the fraction in (1) and a term tending to zero, actual ordinary indices have no template of the stated coefficient at these ranks.

The leading coefficient and individual physical height must be distinguished when the template can depend on \(m\). Its signed origin has \(|b|\le2^e\), so
\[
   |b|/(\alpha 2^m)\le (3/2)^r\,2^{-m}.
\]
In the logarithmic-rank regime this goes to zero for growing \(m\). For much higher ranks the negative offset may instead cancel part of the leading term at the actual \(m\). The positive, arbitrarily strong subprogressions in the companion proof therefore coexist with (1); the residue and the template vary with the requested gain. [Signed Mersenne rows](SIGNED_MERSENNE.md)
