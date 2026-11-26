# A simultaneous binary and ternary bound with two moving centers

Consider a positive ordinary odd orbit at a junction \(t\). Its preceding and following words can vary with \(t\). The following bound pays for the part of the separation of their centers supported outside 2 and 3. This gives a bound uniform in the words and an application to adjacent transpositions of entirely unrestricted background words.

## A fixed system of linear forms

For a finite set \(S\) of primes and a nonzero integer \(n\), write \([n]_S=\prod_{q\in S}q^{v_q(n)}\), \(H_S(n)=|n|/[n]_S\). If \(A,B,A-B\ne0\), then for every \(\epsilon>0\)
\[
 [\operatorname{lcm}(|A|,|B|)]_S
 \le C_{S,\epsilon}\max(|A|,|B|)^\epsilon
       \min(|A|,|B|)H_S(A-B).                              \tag{1}
\]
The constant depends only on the displayed parameters and is ineffective.

Put \(g=\gcd(|A|,|B|)\), \(a=A/g,\ b=B/g,\ j=a-b\) and \(M=\max(|a|,|b|)\). The integers \(a,b,j\) are pairwise coprime. At infinity take \(X-Y\) and the smaller of \(X,Y\) at \((a,b)\). At each finite \(q\in S\) take two distinct forms from \(X,Y,X-Y\), including the unique \(q\)-divisible value when such a value exists. These are finitely many systems of independent forms. The full product at \((a,b)\) equals
\[
  \frac{\min(|a|,|b|)|j|}{[abj]_S}.
\]
Schlickewei's finite-place Subspace Theorem bounds this below by \(c_{S,\epsilon}M^{-\epsilon}\). Indeed vectors violating the bound with constant one lie in finitely many proper rational subspaces for each of the finitely many form selections. Each line contains at most two primitive integer vectors. All values retained here are nonzero, hence the finite exceptions give a positive common constant. Rearranging and multiplying by \([g]_S\) proves (1), since \([g]_S\le g\), \(H_S(j)\le H_S(A-B)\), and \([\operatorname{lcm}(|A|,|B|)]_S=[g]_S[ab]_S\).

This is an application of the classical fixed-form theorem. For fixed distinct rational centers the related squarefree polynomial bound is already contained in Bugeaud–Evertse–Győry, Theorem 2.1(i). [H. P. Schlickewei, *The \(\mathfrak p\)-adic Thue–Siegel–Roth–Schmidt theorem*](https://doi.org/10.1007/BF01220404) · [J.-H. Evertse, finite-place theorem, §7](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf) · [Y. Bugeaud, J.-H. Evertse and K. Győry, Acta Arithmetica 184 (2018)](https://arxiv.org/abs/1708.08290)

## Moving rational centers on an actual trajectory

Use \(S=\{2,3\}\). Suppose \(u,v\) are rationals with denominators prime to six, \(Q\) is their least common denominator, and \(t\) is an integer different from both. Set \(A=Q(t-u), B=Q(t-v)\). If \(v_3(t-u)\ge k\) and \(v_2(t-v)\ge l\), then
\[
 3^k2^l\le C_{\epsilon}
   \max(|A|,|B|)^\epsilon\min(|A|,|B|) H_S(Q(v-u)) .         \tag{2}
\]
Here \(u\ne v\). If \(u=v\), both prime powers divide the same nonzero integer \(A\), so \(3^k2^l\le |A|\). If \(t\) equals either target, its corresponding zero numerator is divisible by arbitrary powers and there is no two-place bound of this form.

For \(H(u)=\max(|\operatorname{num}(u)|,\operatorname{den}(u))\), define \(H=H(u)H(v)\). Then \(Q\le H,\ |A|,|B|\le (|t|+1)H,\ |Q(v-u)|\le 2H\), so
\[
           3^k2^l\ll_\epsilon (|t|+1)^{1+\epsilon}H^{2+\epsilon}. \tag{3}
\]
For sequences with \(t\to\infty\) and \(H\le t^{\delta+o(1)}\), (3) implies
\(\limsup (k\log3+l\log2)/\log t\le 1+2\delta\). The constant in (2) works across this entire family.

A nonempty chronological odd word \(U\) has \(m_U\) odd steps, \(a_U\) total powers of two, affine map \((3^{m_U}x+C_U)/2^{a_U}\) and fixed point \(u=C_U/(2^{a_U}-3^{m_U})\). The denominator is nonzero and prime to six. Iterating the centered affine formula on an actual positive orbit shows \(v_3(t-u)\ge k_0m_U\) after \(k_0\) copies of \(U\), since the starting difference is ternary integral. Before \(l_0\) copies of a word \(V\) the same argument backwards gives \(v_2(t-v)\ge l_0a_V\). These statements use every specified step on the actual trajectory. The elementary carry sum gives \(H(u)\le m_U 3^{m_U}2^{a_U}\), and \(m_U\le a_U\). Hence (3) yields a bilateral budget of \((1+o(1))\log t\) uniformly if \(a_U+a_V=o(\log t)\), with the zero-numerator exception above. For strict-record words both centers are negative, so the exception does not occur. This generalizes the [fixed-block turn bound](../boundary/RECORD_ENTRANCE.md).

## A single adjacent swap at arbitrary background length

Let two consecutive blocks \(U,V\) of an actual orbit contain \(m\) odd steps each and total power \(a\) each. Denote the initial, junction and terminal states by \(t_-,t,t_+\). With the common raw denominator \(D=2^a-3^m\), take
\[
       A=Dt-C_U=3^m(t_{-}-t),\qquad B=Dt-C_V=2^a(t-t_+).     \tag{4}
\]
Suppose \(t\) differs from both endpoints. If \(U,V\) differ only by a transposition of adjacent unequal gaps \(e,f\), then exactly one summand of
\(C_U=\sum_{i=0}^{m-1}3^{m-1-i}2^{e_0+\cdots+e_{i-1}}\) changes. For the exchange at indices \(i,i+1\),
\[
   |A-B|=|C_U-C_V|=
   3^{m-2-i}2^{e_0+\cdots+e_{i-1}+\min(e,f)}(2^{|e-f|}-1).
\]
In particular for gaps 1 and 2, the separation is an \(S\)-unit, independently of the whole background. Equations (1) and (4) imply
\[
  3^m2^a \le C_\epsilon
   \max(3^m|t-t_-|,2^a|t-t_+|)^\epsilon
   \min(3^m|t-t_-|,2^a|t-t_+|).                            \tag{5}
\]
A gap difference of arbitrary fixed size costs at most \(2^{|e-f|}-1\). If the words coincide and the endpoints differ from \(t\), the same conclusion with exponent zero follows by divisibility of \(A=B\).

On a bounded strip cycle with minimum \(s\to\infty\) and primitive odd period \(p\), take \(m<p\). The endpoint differences are nonzero and \(O(s)\). Suppose \(2^a\asymp3^m\) uniformly. Then (5) gives
\[
            \limsup \frac{m\log3}{\log s}\le1 .
\]
Indeed \((3^m)^2\ll_\epsilon (3^m s)^{1+\epsilon}\), and \(\epsilon\) may decrease after taking the limsup. On the least-disagreement bounded branch, \(m\le p\ll s\), and \(2^a/3^m=(t_-/t)\prod_{j<m}(1+1/(3x_j))\) is bounded above and below, directly from the physical orbit. Thus long consecutive near-squares of this particular type are excluded even when their common word has no bounded-length description. The argument requires an actual occurrence of the two blocks. An arbitrary binary valuation sequence need not contain sufficiently long consecutive near-squares, and the present estimates do not show the strip dynamics forces them.
