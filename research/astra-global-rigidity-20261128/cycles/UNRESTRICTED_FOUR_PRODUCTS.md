# Four products and a sign test on odd Collatz segments

Use the positive odd vertices, exact division counts, signed multiplicities, and normalization of [the triple-product theorem](UNRESTRICTED_TRIPLE_PRODUCTS.md). Every positive odd \(L\)-step segment of minimum
\[
                              H>2^{8(L+1)^2}
\]
has all its four-fold multiset products distinct, including powers of a single vertex. The exponent is uniform over all division counts. Paper 163/v1 separates general orders under a total-cost bound. The new step handles the terminal signed multiplicity three that evades the triple-product congruence. [Paper 163/v1, §§3, 6](https://rstation.ai/problems/collatz/papers/163)

## A sign test

After removing shared indices, there are \(h\le k\) terms per side. Reverse signs if necessary to make \(c_m>0\) at the last surviving index \(m\). As in the earlier note put \(s_m=0\), \(Z=2^{a_{m-1}}x_m\) and
\[
 w_b=3^b2^{-E_b},\quad E_b=S_{m-1}-S_{m-1-b},\quad
 d_b=\sum_{i\le m-1-b}c_i,\quad G=\sum_{b=0}^{m-1}d_bw_b .
\]
The intervals between consecutive \(s_i\), listed from zero upwards, have lengths \(w_0,\ldots,w_{m-1}\). On the interior of the \(b\)-th interval, \(\sum_{i:s_i\ge s}c_i=d_b\). The normalized affine coordinates give \(Z>s_i\) for every \(i\), by \(x_i>0\).

Suppose the sequence of nonzero \(d_b\) consists of negative entries followed by positive entries, with either block allowed to be empty. Its first entry \(d_0=-c_m\) is negative. At an aligned product collision one has
\[
  0=\sum_i c_i f(s_i)=\int_0^{s_0} D(s) f'(s)\,ds,\qquad
  f(s)=-\log(1-s/Z),\qquad D(s)=\sum_{i:s_i\ge s}c_i .
\]
The function \(f'\) is positive and strictly increasing. If \(D\) is everywhere nonpositive in the interiors, the integral is strictly negative. Otherwise choose a point \(t\) separating the negative from positive intervals. Then \(D(s)(f'(s)-f'(t))\ge0\) on every interval and is positive on part of the initial negative interval. It follows that the integral strictly exceeds \(f'(t)G\), so \(G<0\). Every initial partial sum of \(d_bw_b\) is now strictly negative. Indeed the sums first decrease, and after the transition they increase to a strictly negative final value.

The nonzero-prefix property alone suffices for the first-gap argument. The prefix through \(j\), on multiplication by \(2^{E_j}\), is a nonzero integer. This gives the bound \(2^{-E_j}\) regardless of its residue modulo three. The same tail and symmetric-function bounds as in the triple-product theorem exclude a collision when
\[
 H>\max\{8kL3^{kL},\,2^{LM+2+k(L+2)}\},\qquad
 M=2L+\lceil\log_2(2kL)\rceil .
\]
This sign test applies in every order for which the stated sign pattern holds. All uses of a product collision in its proof are implications, so zero partial sums on an arbitrary input word cause no difficulty.

## Why all quadruples qualify

Clock alignment includes \(\sum_i i c_i=0\). This excludes \(c_m=h\), as every index opposite \(m\) is smaller. When \(h\le4\) and \(3\nmid c_m\), the triple-product congruence already supplies the nonzero-prefix property. The only other possibility is \(h=4\), \(c_m=3\). In that case the positive multiset is \((i,m,m,m)\), \(i<m\). Every negative index \(j\) satisfies
\[
                   j\ge3m+i-3(m-1)=i+3
\]
by index alignment and the strict upper bound \(m-1\) on its three companions. Hence the four negative indices lie strictly between \(i\) and \(m\). Read from the terminal end, the prefix coefficients start at \(-3\), increase by the multiplicities of the four negative indices, then decrease from \(1\) to \(0\) at \(i\). Their nonzero signs are negative then positive. The sign test therefore covers the last case. Finally \(M\le3L+3\) for \(k=4\), and \(2^{8(L+1)^2}\) bounds both sufficient thresholds for all \(L\ge1\).

Equivalently, a proposed collision of the exceptional shape would have offsets \((A,0,0,0)\) versus four offsets strictly between zero and \(A=s_i\). Strict convexity gives \(f(u)<uf(A)/A\) on this interval. Equality of the products would imply \(A<\sum_{\rm right}s_j\), precisely the sign \(G<0\) above. At order five a terminal multiplicity of three leaves up to two additional positive indices. Index alignment alone no longer confines all four or five opposite indices to one side of both. The general sign test states its actual hypothesis.
