# How the complete rational denominator enters Pell return packing

**PROPOSED, elementary apart from the stated square-gap lemma for the complete-list bound.** Let a primitive positive rational Syracuse cycle have \(P\) odd phases and common reduced denominator \(d\). In an increasing-period family, if a fixed positive fraction of its adjacent-product squareclasses lies in affine spaces of dimensions \(r=o(\log P)\), then \(d\) exceeds every fixed power of \(P\) eventually. This applies to arbitrary valuations and real height. If the whole product list has bounded affine rank and \(\omega(d)\), the number of different prime factors of \(d\), remains bounded, then \(d\ge \exp(cP)\) for sufficiently large \(P\), with \(c>0\) depending only on the two bounds.

In the ordinary case \(d=1\). The [ordinary packing theorem](PELL_RETURN_PACKING.md) gives stronger constants there. For rational cycles, dropping the denominator-dependent residue below gives a false spacing assertion even on the primitive cycle \(5/7\leftrightarrow11/7\).

## One residue modulo the square of the whole denominator

Write the odd phases as \(x_i=n_i/d\), with positive odd numerators, \((n_i,d)=1\), and \(2^{a_i}n_{i+1}=3n_i+d\). Any positive rational realization of a nonempty cycle with odd steps has \(d\) coprime to six from the complete affine closing denominator \(2^{\sum a_i}-3^P\). Its reduced denominator persists at every phase. Put
\[
  D_i=\operatorname{sf}(3n_i(3n_i+d)),\qquad
  X_i=6n_i+d,\qquad V_i=2\sqrt{3n_i(3n_i+d)/D_i}.
\]
Then \(X_i^2-D_iV_i^2=d^2\), with \(V_i\) even. The squarefree \(D_i\) is at least one. In a cycle the predecessor relation makes \(3\nmid n_i\) (because \(3\nmid d\)), so \(3\) occurs exactly once in \(3n_i(3n_i+d)\). Thus \(3\mid D_i\) and \(D_i>1\).

For every \(p\mid d\), \(X_i\) is a unit at \(p\), hence both \(V_i\) and \(D_i\) are units there. Define \(R_i=X_i/V_i\bmod d^2\); for \(d=1\) use the unique residue. Then \(R_i^2=D_i\bmod d^2\). For each fixed \(D\) there are at most \(2^{\omega(d)}\) possibilities. Indeed two square roots at an odd prime power differ only by sign: the product of their sum and difference is zero modulo that power, and at most one factor can be divisible by the prime. Apply the Chinese remainder theorem at all exact prime powers in \(d^2\).

For phases with equal \(D,R\), the quantities
\[
 U=(XX'-DVV')/d^2,\qquad W=(XV'-X'V)/d^2
\]
are integers, by substitution of the common residue. If \(x<x'\), their unit \(q=U+W\sqrt D=(X'+V'\sqrt D)/(X+V\sqrt D)>1\) has norm one. Both \(X,X'\) are \(d+6\bmod12\), so \(XX'\equiv1\bmod12\). Also \(12\mid DVV'\), since both second coordinates are even and \(3\mid D\). As \(d^2\equiv1\bmod12\), \(U\equiv1\bmod12\) and \(U=(q+q^{-1})/2\ge13\). Therefore \(q\ge13+\sqrt{168}>16\). In particular the increasing values
\[
        L(x)=\log_2\big((X+V\sqrt D)/d\big)>0
\]
for one joint class have successive gaps greater than four. The normalized operand is \(1+6x+\sqrt{(1+6x)^2-1}\), so \(L(x)\) depends only on the positive real phase, including phases below one.

## Exact return norm

For any complete intervening word of \(h\) shortcut steps and \(b\ge1\) odd steps, set \(A=3^b,\ B=2^h,\ By=Ax+C,\ K=6C+B-A\). For equal joint classes use normalized coordinates \(\bar X=X/d,\ \bar V=V/d,\ \bar Y=X'/d,\ \bar W=V'/d\). They satisfy norm-one Pell equations and \(B\bar Y-A\bar X=K\). The return norm
\[
      K^2-D(B\bar W-A\bar V)^2
             =A^2+B^2-2ABU
\]
is an odd integer even when the normalized coordinates are rational. This is where the joint modulus matters. The reciprocal argument in [the ordinary proof](PELL_RETURN_PACKING.md) now applies verbatim to positive \(x,y\). It gives \(x<3\cdot12^h\) for the earlier phase. Consequently
\[
          L(x)<\log_2(2(1+6x))<4h+6.                                     \tag{1}
\]
This bound has no dependence on the height or factorization of \(d\).

A primitive lap has distinct physical sources and shortcut clock \(H=\sum a_i\le P\log_2(3+d)\), by multiplying the positive edge ratios and using \(n_i\ge1\). If a nonempty joint class occurs \(m\) times, summing (1) around its own cyclic returns and sorting the \(L\)'s gives
\[
             2m(m-1)<4H+6m,\qquad m< 5+2\sqrt H.                           \tag{2}
\]
In particular an affine \(r\)-space of adjacent-product squareclasses can contribute at most
\[
          2^{r+1+\omega(d)}\big(5+2\sqrt{P\log_2(3+d)}\big)                \tag{3}
\]
edges, with no assumptions on the omitted phases. Here \([D_i]=[3]+(a_i\bmod2)[2]+[x_i x_{i+1}]\) since the numerical product \(n_in_{i+1}\) differs by \(d^2\).

If \(d\le P^B\) along a subsequence with fixed \(B\), elementary factorial growth gives \(\omega(d)=O_B(\log P/\log\log(P+2))\): an integer with \(k\) prime factors is at least \(k!\). If in addition \(r=o(\log P)\), (3) is \(P^{1/2+o(1)}\), contradicting fixed positive occupancy. This proves the first complete-denominator assertion. More generally for \(d\le P^B\), any subset of \(P^{\beta+o(1)}\) physical edges with \(\beta>1/2\) has affine product squareclass rank at least \((\beta-1/2-o(1))\log_2P\).

## A whole-lap estimate

Suppose now the entire adjacent-product list has affine rank \(r\). The numerator products have the same classes and all numerator states lie in an affine space of dimension at most \(r+1\). Put \(m=r+4\) and cut \(m\) odd steps before the maximum numerator \(M\), wrapping if needed. If \(M\le 2^{m+2}d\), its logarithm is already \(O(m+\log(2d))\). Otherwise every one of the preceding \(m\) numerators exceeds \(d\): iteration of \(n_{i+1}+d\le(3/2)(n_i+d)\) gives \(n_i+d\ge(2/3)^m(M+d)>2d\). All edge numerators on this window then grow by factors at most two. Telescoping as in [the record proof](RANK_CERTIFICATE.md) bounds the total dyadic clock by \(2m\).

The normalized translates of the initial numerator now have integer offsets \(d b_j\) after multiplication by \(3^m\). The old strictly increasing \(b_j\) obey \(b_m<6^m\) by the clock bound. The same augmented \(m+1\) vectors give an even square relation, and [PR192 A1](https://github.com/GettysburgResearch/collatz/blob/ae48a04cca29abe5fc8273bcda45e7eee0874896/research/astra-unconventional-20261126/adelic/README.md) yields \(3^m n_0\le(64(d6^m+1))^{m+3}\). Since \(M\le2^m n_0\), in both cases
\[
                \log_2 M=O((r+1)(r+1+\log(2d))).
\]
For any one \((D,R)\), \(0<L(x)<\log_2(2(1+6M))\). The height gap therefore allows \(O(1+\log(2M))\) occurrences, independent of the arc clock. Combining counts gives
\[
         P=O\!\left(2^{r+\omega(d)}(r+1)(r+1+\log(2d))\right).             \tag{4}
\]
This proves the second assertion and, for all rational cycles with \(d\le P^B\), the whole-list bound \(r\ge(1-o(1))\log_2P\) when \(P\to\infty\). For the latter conclusion one may first assume \(r\le\log_2P\), as larger \(r\) already suffices.

## The two root residues can both occur

The actual positive rational cycle \(5/7\to11/7\to5/7\) has valuations \(1,3\) and complete reduced denominator \(2^4-3^2=7\). Both discriminants are 330. The pairs \((X,V)\) are \((37,2)\) and \((73,4)\), and the residues modulo 49 are \(43,6\), opposite roots. The height ratio \(11/5\) is below the joint-class gap. Thus local integrality at primes away from seven, or the discriminant alone, does not recover the unit quotient.

The first unsupported step toward excluding all ordinary cycles would be to force insufficient squareclass diversity on such a cycle. A rational word can instead evade these bounds by increasing the rank, its denominator, or both.
