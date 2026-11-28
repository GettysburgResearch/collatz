# Coprime clocks near one odd octave force almost the entire determinant

Let a positive rational shortcut cycle have \(p\) odd phases \(x_i\), total shortcut length \(h\), positive determinant \(D=2^h-3^p\), literal full-lap carry \(C\) at an odd minimum \(m=x_0\), and reduced denominator \(q=D/\gcd(D,C)\). Suppose \(\gcd(h,p)=1\). Put
\[
 R=\max_i x_i/m,\qquad \eta=\max(0,\log_2 R-1),\qquad
 \Lambda=h-p\log_2 3.
\]
For \(\eta+\Lambda<1/4\) there is an explicitly defined nonzero integer polynomial \(H\) of degree \(s\le p(\eta+2\Lambda)+3\), all of whose coefficients are \(0,\pm1\), such that
\[
 \log\gcd(D,C)\ \ll\ s+\sqrt{p s\log(2+s)}.                           \tag{1}
\]
If \(s=0\), the exact gcd is one. The implied constant is absolute. No limit assumption is needed for (1). The statement applies to every word satisfying these physical hypotheses, with arbitrary changes of its mask inside the interval specified below.

Since \(\Lambda\le p/(3m\log2)\), every sequence satisfying \(m\ge h^{2-o(1)}\) and \(R\le2+h^{-1+o(1)}\) has
\[
 q\ \ge\ D\exp(-h^{1/2+o(1)}) .
\]
More generally \(q=2^{h-o(h)}\) when \((\eta+p/m)\log(2p)\to0\) and \(h\to\infty\). This last form uses the classical fixed two-logarithm bound \(\log D=h\log2+o(h)\). [Lagarias, Lemma 2.2](https://arxiv.org/abs/math/0512006)

The [independent-clock construction](INDEPENDENT_CLOCKS.md) gives *positive primitive rational cycles* with the same \(h^{2-o(1)}\) minimum and the same near-octave ratio, with growing \(\gcd(h,p)\) and \(q=2^{o(h)}\). All their odd exponents may be one or two. Thus just dropping the clock coprimality changes the possible complete-denominator scale even under these physical controls.

## The localized mask representing the full gcd

Write \(e_i\ge1\) for the odd division counts, \(E_i=\sum_{j<i}e_j\), \(r_i=ih\bmod p\), \(f_i=r_i/p\), and \(d_i=\lfloor ih/p\rfloor-E_i\). The \(r_i\) run through all ranks. The physical odd law \(2^{e_i}x_{i+1}=3x_i+1\) gives
\[
 \log_2(x_i/m)= f_i+d_i+\theta_i,\qquad
 \theta_i=\sum_{j<i}\log_2\!\left(1+\frac1{3x_j}\right)-i\Lambda/p .
\]
The total sum of the nonnegative corrections is \(\Lambda\), so \(|\theta_i|\le\Lambda\). The left side lies between zero and \(1+\eta\). Therefore \(d_i\in\{-1,0,1\}\). If \(d_i=1\) then \(0<r_i\le p(\eta+\Lambda)\) (rank zero is the chosen minimum and \(d_0=0\)). If \(d_i=-1\) then \(r_i\ge p(1-\Lambda)\). The exceptional ranks are localized on two sides of the same circular cut. Their order within either side is unrestricted.

For \(D>1\) choose \(u,v\in\mathbb Z\) with \(up+vh=1\). In \((\mathbb Z/D)^\times\), set \(z=2^u3^v\), \(X=z^{-1}\). Then \(z^p=2\), \(z^h=3\), \(X^p=1/2\). The identity \(1-X^p=1/2\) makes \(1-X\) a unit over the **full composite modulus**. The case \(D=1\) is immediate. Since \(2^{E_i}=z^{ih-r_i}2^{-d_i}\) there,
\[
 3^{1-p} C=\sum_{r_i}2^{-d_i}X^{r_i}.
\]
Multiply by the unit \(2(1-X)\). The geometric baseline of all \(p\) ranks becomes one. The low-rank multiplier \(2^{-1}\) subtracts a term, while the high-rank multiplier \(2\) adds a term with \(2X^{r_i}=X^{r_i-p}\). Thus an exact integral Laurent representative is
\[
 H_0(T)=1+(1-T)\!
    \left(\sum_{d_i=-1}T^{r_i-p}-\sum_{d_i=1}T^{r_i}\right).            \tag{2}
\]
If the expression in parentheses has coefficients \(b_j\), then \(b_j\in\{0,1\}\) for \(j<0\), \(b_0=0\), and \(b_j\in\{0,-1\}\) for \(j>0\). The coefficient at zero of \(H_0\) is \(1-b_{-1}\), and elsewhere it is \(b_j-b_{j-1}\). These are all \(0,\pm1\). Also \(H_0(1)=1\). Shift the least occupied exponent to zero to give \(H(T)\in\mathbb Z[T]\) with constant and leading coefficient in \(\{\pm1\}\). Its width is at most \(p(\eta+2\Lambda)+3\). For any integer representative \(\widetilde X\) of \(X\), (2) gives exactly
\[
             \gcd(D,C)=\gcd(D,H(\widetilde X)).                          \tag{3}
\]
The translation in \(T\) costs only a unit. Every algebraic root of \(H\) is a unit at every finite prime, by integrality of a monic associate of \(H\) and of its reciprocal polynomial.

## A short clock relation

For \(1\le J<p\), Dirichlet's box argument on \(0,h/p,\ldots,Jh/p\) gives integers \(1\le j\le J\) and \(i\) with \(0<|k|\le p/J,\ k=ip+jh\). The lower strict inequality uses \(\gcd(h,p)=1\), and \(|i|\ll J\) since \(h/p=\log_2 3+\Lambda/p<2\). Clear powers of two and three and, if necessary, a Laurent monomial in the exact congruence \(X^k=2^{-i}3^{-j}\pmod D\). The resulting integer binomial \(P\) has degree \(|k|\), nonzero constant, logarithmic coefficient sum \(O(J)\), and \(P(\widetilde X)=0\bmod D\). Every algebraic root of \(P\) has nonzero ternary valuation \(-j/k\) at any extension normalized by \(v_3(3)=1\). It follows that the resultant \(\operatorname{Res}(H,P)\) is nonzero. Bézout's resultant identity over \(\mathbb Z[T]\) makes the gcd in (3) a divisor of this integer.

For \(s>0\), the root formula and the Mahler measure give
\[
 \log |\operatorname{Res}(H,P)|
 \le s\log\|P\|_1+|k|\log M(H)
 \ll sJ+(p/J)\log(2+s).
\]
Here \(M(H)\le\|H\|_2\le\sqrt{s+1}\) by Jensen and Parseval. Taking \(J\) within one of \(\sqrt{p\log(2+s)/s}\), truncated to \(1,\ldots,p-1\), proves (1); bounded \(p\) can be absorbed into the absolute constant, and \(p=1\) has the constant mask. This counts every power of every canceled prime together.

Previous papers use the same Bézout unit, polynomial resultants and short auxiliary clock relations for bounded-degree factors and for a single displaced rank. The additional step here is (2), which uses actual minimum and amplitude to compress the *entire* mask into a short, integral, unit-endpoint polynomial, uniformly for arbitrary arrangements in its allowed rank interval. It does not give such a compression at fixed positive distance above one octave. The ordinary cycle case with unrestricted height spread remains open. [Earlier full-divisor factor bounds](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-ordinary-boundary-20261124/arithmetic/README.md) · [Earlier single-rank resultants](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-multiple-attacks-20261125/synthesis/CYCLE_CLOSURE.md)

[Exact arithmetic replay](check_near_octave.py) checks physical minima, both-sided rank clipping and complete numerical gcds. The 268 minimum-rooted coprime controls include 21 nontrivial cancellations. None has a negative offset after minimum rooting. The separately identified 163 arbitrary-root controls exercise both signs of the Laurent correction. [Archived counts](../../../reports/astra-infinite-descent-20261127/cycles/NEAR_OCTAVE.json)
