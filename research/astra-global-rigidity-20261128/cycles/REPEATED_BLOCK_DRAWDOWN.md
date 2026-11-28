# A macroscopic repeated valuation block forces an internal descent

Let a primitive positive rational Collatz cycle have odd period \(p\), halving count \(A\), and complete reduced denominator \(q\). Its odd numerators \(y_i\) satisfy
\[
 2^{a_i}y_{i+1}=3y_i+q,\qquad a_i\ge1,
 \qquad S_j=\sum_{i<j}a_i,\quad B_j=2^{S_j}/3^j,\quad \gamma=\log_2 3 .
\]
Choose a cut called date zero. Suppose the valuation words of length \(L\) starting at \(r-h\) and \(r\) agree. We require \(0\le r-h<r\) and \(r+L<p\), so both endpoints occur strictly before the return to the cut. Overlap between the two blocks is allowed. Define
\[
 J=\max_{e\,\in\,\{r-h+L,r+L\}}\ \max_{e\le j<p}\log_2(B_j/B_e).
\]
Along every such family with \(p\to\infty\), \(A=O(p)\), and \(L\ge\delta p\) for fixed \(\delta>0\),
\[
              J+\log_2q+2\log_2 y_0\ \ge\ \gamma L-o(p).                 \tag{1}
\]
The little-oh is uniform for fixed \(\delta\) and a fixed upper bound on \(A/p\). Its onset is ineffective. For **ordinary** cycles cut at an odd state of subexponential height, one of the two endpoints consequently drops by a factor \(3^{L-o(p)}\) at a later date **strictly before** the final return to the cut. Here and below a drop by that factor means a lower bound on the ratio of the larger state to the later one. At small cuts this strengthens the divisibility of the endpoint difference by \(3^L\), which alone only requires a large endpoint.

In particular consider an ordinary cycle cut so \(\log y_0=o(p)\), and suppose its maximum internal logarithmic drawdown satisfies
\[
                \max_{0\le i\le j<p}\log_2(y_i/y_j)=o(p).                 \tag{2}
\]
No pair of native blocks of length a fixed positive proportion of \(p\) can recur along such an unbounded family. The number of mismatches of **every proper odd-valuation rotation** tends to infinity along it, simultaneously over shifts of all orders. One terminal transition of arbitrary size is omitted in (2).

A quantitative near-circuit consequence applies to every fixed mismatch count. For any selected odd departure \(j_*\) put \(\sigma=\sum_{i\ne j_*}(a_i-1)\). If some proper odd-valuation rotation has at most \(s\) mismatches, with fixed \(s\), then along growing primitive positive rational cycles
\[
       \liminf\frac{\sigma+\log_2q}{p}\ \ge\
                           \frac{\log_2 3}{6(s+1)}.                      \tag{3}
\]
Thus a single giant division holding all but \(o(p)\) of the excess and **any fixed number** of native mismatches exclude unbounded ordinary cycles. Small fixed linear excess budgets below the right side force an exponential reduced denominator. The result does not cover arbitrary large internal drawdowns at seven or more native mismatches. PR212 already obtained unconditional exponential denominator growth through six mismatches at arbitrary width and clock profile, as well as a near-circuit exclusion through eight mismatches under its explicit small excess budget. Its proofs use the paired native difference quotient and chains of Evertse inequalities. Equation (1) instead uses an actual long repeated block, its two remaining tails, and a low common cut. It makes no assumption at all on the rest of the word in (1). [PR212, all-profile six-mismatch theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.md) · [PR212, eight-mismatch near-circuit theorem](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/MISMATCH_CHAINS.md) · [PR212, unbounded rotation orders at ordinary denominator](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ODD_ROTATION_COMPLEXITY.md)

## Full tails and the shared integer quotient

Write \(A_c=S_{r+L}-S_r=S_{r-h+L}-S_{r-h}\). Subtracting the two actual iterates through the common block shows that \(2^{A_c}\mid y_r-y_{r-h}\), since \(3^L\) is odd. Thus
\[
 G=(y_r-y_{r-h})/2^{A_c}\in\mathbb Z\setminus\{0\}.
\]
The nonzero condition uses the least period. The complete reduced denominator divides \(2^A-3^p\), so it is prime to six. Every true odd numerator is prime to three, since the previous native equation reads \(2^{a_{i-1}}y_i\equiv q\pmod3\).

Set \(H(j)=B_j y_j=y_0+(q/3)\sum_{i<j}B_i\), and define
\[
 V=B_p y_0=H(p),\qquad w=B_r/B_{r-h}=2^d3^{-h},\quad d=S_r-S_{r-h},
 \qquad W=wV,\qquad U=B_r2^{A_c}G.
\]
Then \(U=H(r)-wH(r-h)\). Throughout the common block \(B_{r+i}=wB_{r-h+i}\) for \(0\le i\le L\). On subtracting the two tails up to the same true closing cut one obtains the signed identity
\[
 E=U-V+W=\frac q3\left(w\sum_{j=r-h+L}^{p-1}B_j-
                              \sum_{j=r+L}^{p-1}B_j\right).
\]
Consequently \(|E|\le(2pq/3)2^J B_{r+L}\), even when the contributing index sets overlap.

Suppose a uniform positive linear deficit in (1) occurs infinitely often. Use the rational Subspace Theorem for the fixed places \(S=\{2,3,\infty\}\). At infinity take linear forms \(U-V+W,V,W\), and at the finite places take coordinates. The three vectors of coefficients at each place are independent. The normalized absolute values of \(B_r2^{A_c}\) away from \(S\) are units, and \(|G|_2|G|_3\le1\). Both \(V,W\) are \(S\)-units times \(y_0\). The product of all nine local forms is therefore bounded by
\[
 \frac{|E|\,y_0^2}{B_r2^{A_c}}
 \le \frac{2p q y_0^2}{3}\,2^J\frac{B_{r+L}}{B_r2^{A_c}}
 =\frac{2p q y_0^2}{3}\,2^J3^{-L}.                                    \tag{4}
\]
This cancellation does not charge the size of the arbitrary common affine carry or the integer quotient \(G\). The inputs are \(S\)-integers. In a violating family \(\log q+2\log y_0=O(p)\) since \(J\ge0\), and \(y_j+q\le(3/2)^j(y_0+q)\). Their projective logarithmic height is \(O(p)\) by these bounds, \(A=O(p)\), and the displayed coordinate formulas. Inequality (4) is exponentially small in \(p\), so finitely many fixed proper rational hyperplanes contain all sufficiently late vectors. The usual primitive-integer statement also gives this \(S\)-integer version by the product formula. [Classical fixed-place Subspace Theorem, Bilu, Theorem 2.3 and its extension](https://www.numdam.org/item/AST_2008__317__1_0.pdf) · [Exact \(S\)-integer normalization, Paper 173, §2](https://rstation.ai/problems/collatz/papers/173)

## Eliminating every exceptional relation

We use the elementary fixed-form consequence
\[
                  v_3(b+c2^d)=o(d)\quad(d\to\infty)                    \tag{5}
\]
for fixed nonzero rationals \(b,c\), omitting an exact zero. If \(v_3(b+c2^d)\ge\epsilon d\) infinitely often, apply the same theorem to the two \(S\)-unit coordinates \((1,2^d)\), with forms \(bX+cY,X\) at three and the coordinates elsewhere. The product is at most \(3^{-\epsilon d}\) because \(2^d\) is a three-adic unit. Their projective height equals \(2^d\), so finitely many rational lines must contain infinitely many pairwise distinct projective points, a contradiction. Negative fixed valuations do not affect (5).

Extract one fixed nonzero relation \(aU+bV+cW=0\) from (4). Here \(v_3(U)\ge-r\), \(v_3(V)=-p\), \(v_3(W)=-p-h\). If \(a\ne0\), then \(b+cw\ne0\), since \(U\ne0\). If \(h\to\infty\) and \(c\ne0\), the valuation of \(b+cw\) is \(-h+v_3(c)\) eventually, also when \(b=0\). If \(c=0\) it is fixed. Both contradict \(p-r\ge L\to\infty\). For bounded \(h\), retain a fixed \(h\). If \(b,c\ne0\), use (5) with \(c3^{-h}\) in place of \(c\), since \(d\le A=O(p)\). For bounded \(d\) use its finitely many nonzero values directly. If just one of \(b,c\) occurs, its valuation is fixed. In every case \(v_3(b+cw)\le o(p)\), too small to cancel the gap of at least \(L\) between \(U\) and \(V\).

If \(a=0\), one instead has \(w=-b/c\) fixed on the subsequence. It is different from one since \(h>0\) and \(v_3(w)=-h\). Apply the two-dimensional theorem to \((U,V)\) using \(U-(1-w)V,V\) at infinity and coordinate forms at two and three. The product is bounded by the right side of (4), with one factor \(y_0\) removed. A fixed line now gives \(U/V\) fixed, impossible by \(v_3(U/V)\ge p-r\ge L\). This proves (1).

## Actual descent and the quantitative exclusion

On ordinary integer cycles the native identity gives
\[
 0\le \log_2(B_j/B_e)-\log_2(y_e/y_j)
     =\sum_{i=e}^{j-1}\log_2(1+1/(3y_i))=O(\log(2+p))\quad(e\le j<p).
\]
The last inequality follows by comparing the distinct positive numerators with the first \(p\) positive integers. Also \(A\le2p\) by the complete positive lap identity. This proves the physical interpretation and the exclusion under (2). A cyclic recurrent word can be cut into at most a bounded number of pieces by the seams at the two starting coordinates. If a proper shift has at most \(s\) mismatches, replace it by its inverse if necessary so its lag \(h\) is at most \(p/2\). On the legal pairs starting at \(0,\ldots,p-h-2\) there are at least \(p-h-1-s\) equal dates in at most \(s+1\) runs. Hence some run has \(L\ge p/[2(s+1)]-O_s(1)\), with both endpoints strictly before the closing cut. The same seam-splitting observation handles any already supplied pair of cyclically repeated blocks of macroscopic length by passing to a macroscopic subblock.

For (3) rotate \(j_*\) to \(p-1\). At every proper date \(j<p\) one has \(j\le S_j\le j+\sigma\); in fact \(S_j-S_e\le j-e+\sigma\) for \(0\le e\le j<p\). Consequently \(B_j\le2^\sigma\) and \(J\le\sigma\). The exact closing formula \(B_p y_0=y_0+(q/3)\sum_{j<p}B_j\) gives \(A\le\gamma p+\sigma+\log_2 q+O(\log(2+p))\). We need only families where \(\sigma+\log_2 q=O(p)\); others cannot violate (3). There \(A=O(p)\). The positive-real minimum \(m=\min y_i/q\) satisfies \(m\ll p^{B+1}\) for a fixed logarithmic-form exponent \(B\): combine \(A-\gamma p\gg (1+p)^{-B}\) with \(A-\gamma p\le p/(3m\log 2)\). At a minimum date \(j<p\), \(y_0\le B_j y_j\le 2^\sigma q m\), giving \(\log_2 y_0\le\sigma+\log_2q+O(\log(2+p))\). Using (1) at the run just found gives \(\gamma L\le3(\sigma+\log_2 q)+o(p)\), as claimed. [Classical two-log bound, Bondareva–Luchin–Salikhov, Theorem 1](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)

The magnitude of a jump matters for the native valuation word: changing a single exponent can add an arbitrarily long run of zeros to the shortcut word and change all subsequent shortcut alignments. Fixed-Hamming-distance bounds for a **fixed shortcut displacement** do not directly imply (1) or (3). [PR212, all shortcut rotations](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ALL_SHIFT_HEIGHTS.md)
