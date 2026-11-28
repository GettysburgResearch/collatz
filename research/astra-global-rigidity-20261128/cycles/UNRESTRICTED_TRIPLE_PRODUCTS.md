# Triple products on odd Collatz segments with unrestricted division counts

An odd segment has positive odd vertices \(x_0,\ldots,x_L\) and exact transitions
\[
  2^{a_j}x_{j+1}=3x_j+1,\qquad a_j\ge1,\qquad S_j=\sum_{b<j}a_b .
\]
Suppose \(L\ge1\) and put \(H=\min_{0\le j\le L}x_j\). If
\[
                         H>2^{8(L+1)^2},
\]
then the \(\binom{L+3}{3}\) products \(x_ix_jx_k\), \(0\le i\le j\le k\le L\), are pairwise distinct. Repetitions within a triple are allowed. The threshold is independent of every division count and of \(S_L\).

Weaver's Paper 160 gives unrestricted pair-product separation at \(H>8L9^L\). Paper 163 gives arbitrary fixed product order under a total-division budget, supplies the backward affine coordinates used below, and exhibits an aligned five-fold pair with vanishing first correction. Here the conclusion at order three holds without a budget. The exponent quadratic in \(L\) leaves open a linear exponent at this order. [Paper 160/v1](https://rstation.ai/problems/collatz/papers/160) · [Paper 163/v1, §§3, 6](https://rstation.ai/problems/collatz/papers/163)

## Alignment at high height

Suppose two different multisets of cardinality \(k\ge1\) yield the same product. Cancel common indices and let \(h\le k\) be either remaining cardinality. Write \(c_i\) for the signed multiplicity, so \(\sum c_i=0\) and \(\sum |c_i|=2h\). Put \(I=\sum i c_i\), \(J=\sum S_i c_i\). Taking logs of the exact transitions gives
\[
 |I\log3-J\log2|\le\frac{2kL}{3H},\qquad |I|\le kL .
\]
Indeed the error in each \(\log x_i-\log x_0-i\log3+S_i\log2\) lies in \([0,L/(3H)]\). If \((I,J)\ne(0,0)\), invert the clock ratio to arrange \(I\ge0\). Outside \([1/2,2]\) its absolute logarithm is at least \(\log2\). Inside this interval, \(J<0\) can only give the ratio 2. Otherwise \(3^I,2^J\) are distinct positive integers bounded by \(2\cdot3^{kL}\), and the mean value theorem gives an absolute logarithm at least \((2\cdot3^{kL})^{-1}\). In particular \(H>8kL3^{kL}\) forces \(I=J=0\).

Let \(m\) be the largest surviving index. It exists and \(m\ge1\). If \(|c_m|=h\), one side consists solely of index \(m\) while every index on the other side is strictly smaller, contradicting \(I=0\). Thus \(1\le |c_m|\le h-1\). At order three this ensures \(3\nmid c_m\).

## A lower bound for the first coefficient

In the following argument suppose \(3\nmid c_m\), also allowing arbitrary fixed \(k\). With \(r=2^{-a_{m-1}}\) and \(Z=x_m/r\), backward iteration gives
\[
 x_i=\frac{2^{S_m-S_i}}{3^{m-i}}r(Z-s_i),\qquad
 s_i=\sum_{j=i}^{m-1}3^{m-1-j}2^{-(S_{m-1}-S_j)},\qquad s_m=0.
\]
The normalization cancels even an arbitrarily large final division count. Since each \(a_j\ge1\), \(0\le s_i\le \sum_{b=0}^{m-1}(3/2)^b<2^{L+1}\). Equal cardinalities and \(I=J=0\) cancel all factors outside \((Z-s_i)\) in the product equality.

The difference of the two sums of offsets is
\[
 G=\sum_i c_i s_i=\sum_{b=0}^{m-1}d_b3^b2^{-E_b},\qquad
 d_b=\sum_{i\le m-1-b}c_i,\qquad E_b=S_{m-1}-S_{m-1-b}.
\]
Here \(|d_b|\le k\), \(E_0=0\), the \(E_b\) strictly increase, and \(d_0=-c_m\). For every \(j\), multiply the prefix through \(b=j\) by \(2^{E_j}\). The result is an integer congruent to \(d_02^{E_j}\pmod3\), hence the prefix has absolute value at least \(2^{-E_j}\).

Set \(M=2L+\lceil\log_2(2kL)\rceil\). If every gap is at most \(M\), the full sum has absolute value at least \(2^{-LM}\). Otherwise let \(b\ge1\) be the first index with \(E_b-E_{b-1}>M\). The preceding prefix has magnitude at least \(2^{-E_{b-1}}\), with \(E_{b-1}\le LM\). The entire remaining tail has absolute value at most
\[
 kL3^L2^{-E_b}\le \tfrac12\,2^{-E_{b-1}}.
\]
Consequently \(|G|\ge2^{-LM-1}\), uniformly over the valuation word.

## Root bound and scope

Let \(\Delta_j\) be the difference of the two degree-\(j\) elementary symmetric functions in the respective multisets of offsets, so \(\Delta_1=G\). Each polynomial evaluated at \(Z\) is monic of degree \(h\). Nonnegative offsets give
\[
 \sum_{j=2}^h|\Delta_j|\le2(1+2^{L+1})^k\le2^{1+k(L+2)} .
\]
At their common value, subtract the monic products and divide by \(Z^{h-1}\). Since \(Z>1\), this gives \(|G|\le2^{1+k(L+2)}/Z\). Hence a collision with \(3\nmid c_m\) is impossible when
\[
 H>\max\{8kL3^{kL},\,2^{LM+2+k(L+2)}\}.
\]
For \(k=3\), \(M\le3L+3\) since \(6L\le2^{L+3}\). Both thresholds are bounded by \(2^{8(L+1)^2}\) for \(L\ge1\). This proves the stated triple-product theorem. More generally it also proves separation of all distinct squarefree \(k\)-fold index products at the displayed \(k\)-dependent threshold, because then \(|c_m|=1\).

The first correction alone does not settle arbitrary repeated-index multisets of higher order. In Paper 163's valuation word \((1,2,2,2,1,1,2)\), the order-five index multisets \((0,0,7,7,7)\) and \((1,4,4,6,6)\) have equal index and clock sums and \(G=0\). A nonzero higher coefficient distinguishes those particular monic polynomials. The companion exact checker includes that example, actual prescribed high segments, widely separated division counts, and a low-height collision.
