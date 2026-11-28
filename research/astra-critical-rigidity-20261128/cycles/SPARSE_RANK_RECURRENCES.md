# A sparse spatial recurrence cannot vanish across a fixed rank interval

**Proposed written theorem using the cited inputs.** Let \(Z_{p,r}\) be integer arrays on \(0\le r<p\), and suppose that for some scales \(L_p>0\) and fixed \(K\)
\[
 \max_r|Z_{p,r}|\le p^K,\qquad
       \max_{r<p}|Z_{p,r}/L_p-2^{r/p}|\longrightarrow0.                \tag{1}
\]
Fix an interval \([a,b]\subset[0,1]\) of positive length, a number of terms \(s\), and a coefficient exponent \(K'\). Put \(W=\lfloor p/(\log p)^5\rfloor\). For all sufficiently large \(p\), no nonzero integer polynomial \(P\) of degree at most \(W\), with at most \(s\) nonzero coefficients each at most \(p^{K'}\) in absolute value, satisfies
\[
                         P(E)Z_{p,r}=0
                  \quad(ap\le r\le bp-W).                              \tag{2}
\]
Here \(E\) shifts spatial rank forward. Both the support and the integer coefficients may move with \(p\). This includes each ordinary two-grade folded array, since its true angles give (1) and the published two-logarithm bound gives polynomial height. The [two-grade rank theorem](TWO_GRADE_SIDON.md) supplies the chart and the [original cycle minimum estimate](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/arithmetic/WIDTH_THREE.md) gives the specific bound \(m\ll p^{5.116201}\).

## The finite integer series and its boundary polynomials

Suppose (2) holds along a sequence. Remove any initial power of \(T\) from \(P(T)\), shrinking the tested interval by at most \(W\). A monomial would force a zero in an interior interval, already contrary to (1). Let \(w\le W\) be the resulting degree, \(P(0)\ne0\), and put \(D(T)=T^wP(1/T)\). Choose consecutive labels \(y_t=Z_{p,r_0+t}\), \(0\le t<N\), on a fixed interior interval of length \(N\asymp p\) where all eligible equations hold. Then
\[
      D(T)\sum_{t<N}y_tT^t=U(T)+T^N V(T),\qquad \deg U,\deg V<w .     \tag{3}
\]
Indeed every coefficient of degree \(w,\ldots,N-1\) on the left is exactly a recurrence equation. The coefficients of the two boundary polynomials are bounded by \(s p^{K+K'}\). Work over \(\mathbb Q[T]\), and put \(G=\gcd(D,U,V)\) and \(D_0=D/G\).

Each root \(\lambda\ne0\) of \(D_0\) has multiplicity in \(D\) larger than its order \(e\) in each of \(U,V\). These last two orders must agree below the multiplicity in \(D\), by (3) and \(\lambda\ne0\). A nonzero root of a polynomial with at most \(s\) monomials has multiplicity at most \(s-1\), by the invertible Vandermonde matrix of its distinct exponents using \((T\,d/dT)^j,\ 0\le j<s\). In particular \(e<s\). Differentiate (3) at \(\lambda\) to order \(e\) to obtain
\[
                    \lambda^N=-U^{(e)}(\lambda)/V^{(e)}(\lambda).     \tag{4}
\]
The two evaluations are nonzero. The derivatives are taken before division by \(G\), so their integer coefficient sums are at most \(C s W^{s+1}p^{K+K'}=:B\), with \(\log B=O(\log p)\).

For the absolute logarithmic Weil height \(h\), a quotient of two degree-at-most-\(w\) integer polynomials of coefficient sums at most \(B\), evaluated where its denominator is nonzero, has height at most \(w h(\lambda)+\log B\). At an infinite place bound both coordinates by \(B\max(1,|\lambda|)^w\); at a finite place integral coefficients permit the same estimate with factor one. Summing these local projective bounds proves the assertion also for nonintegral algebraic numbers. By \(h(\lambda^N)=Nh(\lambda)\), if \(d=[\mathbb Q(\lambda):\mathbb Q]\le W\), (4) gives
\[
                      d h(\lambda)\le \frac{W\log B}{N-W}
                                      \ll(\log p)^{-4}.                 \tag{5}
\]
A nonzero algebraic number which is not a root of unity has \(d h(\lambda)\gg (1+\log(2d))^{-3}\) by the Dobrowolski–Voutier theorem. For bounded degrees the positive lower bound follows also from Northcott; degree one uses \(\log 2\). Thus (5) forces **all** the effective roots of \(D_0\) to be roots of unity. The argument controls repeated factors without an exponential coefficient loss in \(G\). [Voutier, main theorem, Acta Arith. 74 (1996), 81–95](https://arxiv.org/abs/1211.3110) · [Dobrowolski, Acta Arith. 34 (1979), 391–401](https://doi.org/10.4064/aa-34-4-391-401)

## Boundedly many strides, dilated separately

Write \(J\) for the support of \(D\), and \(Q_s=\prod_{\ell\le s,\ \ell\ {\rm prime}}\ell\). For each effective root \(\lambda\), choose an irredundant nonempty vanishing subsum of \(D(\lambda)=0\); it has at least two terms. Mann's theorem on rational linear relations between roots of unity implies that for two distinct exponents \(i,j\) in that subsum, the order of \(\lambda^{i-j}\) divides \(Q_s\). Thus \(\lambda\) is a root of \(T^{Q_s|i-j|}-1\). Since its multiplicity in \(D_0\) is at most \(s-1\), we have divisibility in \(\mathbb Q[T]\)
\[
          D_0(T)\ \bigm|\
              \prod_{\{i,j\}\subset J,\ i<j}
                        (T^{Q_s(j-i)}-1)^{s-1}.                        \tag{6}
\]
This accounts for every effective root even when distinct roots have different orders and arise from different subsums. [H. B. Mann, *On linear relations between roots of unity*, Mathematika 12 (1965), 107–117](https://doi.org/10.1112/S0025579300005210) · [Dvornicich–Zannier's stronger rational-coefficient order bound, summarized with proof by Zannier, pp. 487–490](https://seminariomatematico.polito.it/rendiconti/cartaceo/53-4/487.pdf)

All strides \(d_j=Q_s|i-j|\) in (6) are positive and \(o(p)\). Choose a fixed \(\tau>0\) so small that \((s-1)\binom{s}{2}\tau p<N/3\) eventually. Replace each stride separately by \(d'_j=d_j\lfloor\tau p/d_j\rfloor\). It is a positive multiple of its old stride and \(d'_j/p\to\tau\) uniformly. The resulting polynomial \(F=\prod_j(T^{d'_j}-1)^{s-1}\) has degree less than \(N/3\), is divisible by \(D_0\), and has a number of factors and coefficient sum bounded independently of \(p\).

Divide (3) by \(G\), then multiply by \(F/D_0\). The initial boundary polynomial has degree at most \(W+\deg F\), while the terminal one still begins at \(N\). It follows that the coefficient of \(F(T)\sum y_tT^t\) vanishes at any \(t\) between \(W+\deg F+1\) and \(N-1\). Choose \(t=\lfloor2N/3\rfloor\). Evaluating the corresponding finite linear combination of the labels with (1), and passing to a subsequence with \(|J|\) fixed, its value divided by \(L_p\) differs by \(o(1)\) from
\[
                2^{(r_0+t)/p}\prod_j(2^{-d'_j/p}-1)^{s-1}.
\]
Its absolute value is bounded away from zero, a contradiction. This argument also covers a constant \(D_0\). No common multiple of all the original strides is required.

## Relation to the earlier integer-grid argument

PR213 ruled out a zero interval for one fixed sixth-difference polynomial by a fixed stride-sixty annihilator. Here the polynomial can have moving exponents of order \(p/(\log p)^5\), changing roots, and polynomially growing coefficients. The finite-series height estimate first removes all nontorsion effective factors. Mann's bound supplies the bounded family of short strides used in the final dilation. The numerical power five in the permitted scale is convenient; the proof applies whenever \(W(\log p)^4/p\to0\).
