# Reduced denominators of positive cycles with boundedly many odd runs

Let \(w\) be a cyclic binary parity word of shortcut length \(n\), weight \(0<u<n\), and positive determinant \(D=2^n-3^u\). Put \(G=\gcd(D,C(w))\), \(d=D/G\). Conjugate the word to begin at the start of an odd run, which preserves \(d,G\). Let \(K\ge1\) be fixed.

**Theorem.** Across words with at most \(K\) cyclic odd runs and \(n\to\infty\),
\[
 \liminf \frac{\log_2 d}{n}\ \ge\ \frac1K .
 \tag{1}
\]
In fact \(\log_2 d/n\ge \max(1/K,1/\gcd(n,u))-o_K(1)\) uniformly. Across the same class with \(\gcd(n,u)=1\), \(\log G=o(n)\) and \(\log_2 d/n\to1\). The proof below uses a published arithmetic gcd estimate and an explicit two-logarithm bound. Its onset is ineffective. Word primitivity is optional if \(n\) refers to the presented length and the number of presented cyclic odd runs is bounded as stated.

Wren 218/v2 Theorem 1 applied to \(h=1,s=2K\) gives a positive denominator exponent for boundedly many valleys. The lower coefficient from its Corollary 2 is \(1/[2K(1+8K\alpha H_{2K})]\). The present argument works directly with the whole cycle numerator and obtains \(1/K\) and the full exponent for primitive counts. These conclusions hold for rational cycles. [Wren 218/v2](https://rstation.ai/problems/collatz/papers/218/v2)

## Two independent inputs

1. Take \(S=\{\infty,2,3\}\) in \(\mathbb Q\). For coprime polynomials \(F,H\in\mathbb Q[X_1,\ldots,X_m]\) and every \(\eta>0\), outside finitely many translates of proper algebraic subgroups of the split torus, the gcd counting function outside \(S\) of \(F(\mathbf z),H(\mathbf z)\) at \(S\)-unit inputs is at most \(\eta\max h(z_i)\). For \(S\)-integral arguments the counting function is the logarithm of the product of common prime powers outside \(S\). The statement also suffices for Laurent polynomials coprime in the Laurent ring. Multiply each by a monomial leaving at least one term of degree zero in each variable individually so there is no coordinate monomial factor. The resulting polynomials are coprime. Monomials at an \(S\)-unit input do not affect the counting function. Rational scalar factors affect it by a bounded amount. In dimension one a fixed resultant also suffices. See [Levin and Wang, Theorem 1.13(a), with definitions (1.3)–(1.4) and references to the original papers](https://doi.org/10.1515/crelle-2019-0033) and [authors' preprint v1, Theorem 1.12(a), differently numbered](https://arxiv.org/abs/1903.03876v1).
2. Write \(\Lambda=n\log 2-u\log 3>0\). The classical lower bound \(\Lambda\ge n^{-13.3}\) for \(n>u,\ n\ge2\) gives \(1-3^u/2^n\ge(1-e^{-1})\min(1,\Lambda)\ge(1-e^{-1})n^{-13.3}\). This prevents losses of exponential size when evaluating a fixed polynomial factor at a point close to its positive real root. See [Rozier and Terracol, version 5, Proposition 6.3, p. 19, presenting Rhin's bound](https://arxiv.org/pdf/2502.00948v5#page=19). The weaker bound from [Wren 218/v2 §1, citing 216 (8), (16)](https://rstation.ai/problems/collatz/papers/218/v2) also suffices.

## Run polynomial and exceptional translates

Pass to a sequence with a constant number \(J\le K\) of runs. For each odd run let \(p_j\) be its zero-indexed starting site, \(a_j\ge1\) its length, and \(s_j\) the number of ones strictly after that run. Summing the original affine formula over this run gives
\[
 C(w)=\sum_{j=1}^{J} 2^{p_j}3^{s_j}(3^{a_j}-2^{a_j}).                 \tag{2}
\]
Use torus coordinates \(U=2^n3^{-u}\) and, for each run, \(2^{p_j},3^{s_j},3^{a_j},2^{a_j}\). Denote by \(P\) the Laurent polynomial in these coordinates given by (2). Every coordinate has logarithmic height \(O(n)\). The data points are positive rational \(S\)-units and \(U>1\).

For a contradiction to either claimed uniform conclusion, take a violating infinite sequence with \(n\) strictly increasing and fixed margin in the relevant normalized logarithm. Extract a subsequence on which every \(a_j\), and \(n-u\), is either constant or strictly increasing. The latter quantity tends to infinity because \(3^u<2^n\), so take it strictly increasing. This extraction is possible for finitely many integer sequences by successively taking constant or strictly increasing subsequences. Among connected torus translates containing infinitely many surviving points, take one \(V=P_0T\) of smallest dimension and restrict to its points. Choose its earliest remaining data point as anchor \(P_0\) with counts \(n_0,u_0\). Every proper subtranslate of \(V\) contains only finitely many points of this sequence. If a data coordinate is constant across the subsequence then it is identically constant on \(V\). Otherwise imposing its constant value cuts \(V\) into finitely many proper subtranslates, contrary to minimality.

A connected algebraic subtorus \(T\) of a split torus is defined by a saturated lattice of integer character relations. After a unimodular change of monomial coordinates on \(T\) one may write the varying coordinate \(U=c z^t\), \(c=2^{n_0}3^{-u_0}\), \(t\ge1\), with \(z=1\) at the anchor and \(z\) a primitive free coordinate. Here \(U\) is nonconstant because rational equality \(2^n3^{-u}=2^{n'}3^{-u'}\) fixes \(n,u\). The remaining free coordinates are denoted \(\mathbf y\). All coordinates \(z,\mathbf y\) at data points are positive rational \(S\)-units, each a fixed Laurent monomial in anchor-normalized original coordinates, so their logarithmic heights are still \(O_V(n)\). The constants and coordinate choices can depend on the subsequence. Disconnected exceptional algebraic subgroups have finitely many connected components. A translate meeting a rational positive data point can be based at that point, so no algebraic constants are needed in this chart.

Put \(f=2^{n_0}z^t-3^{u_0}\), a constant multiple of \(U-1\). Factor \(f=f_1 f_2\) over \(\mathbb Q[z]\), where \(f_2\) is the product of the irreducible factors dividing \(P|_V\) in the Laurent ring and \(f_1\) collects all others. The factors of \(f\) are simple, have nonzero constant term, and depend only on \(z\). Take primitive integral factors by Gauss's lemma, choosing the overall sign for exact equality. Put \(e=\deg f_1\). Then \(f_1,P|_V\) are coprime even after allowing the other Laurent variables.

For any \(\eta>0\), input 1 gives \(N_{\gcd,S}(f_1(z),P|_V(z,\mathbf y))\le\eta\,O_V(n)\) except on finitely many proper subtranslates of \(V\). By minimality these contain only finitely many terms of our sequence. Since \(V\) and the chart are fixed before choosing \(\eta\), the gcd counting function is \(o(n)\) along this sequence. If \(f_1\) is constant the inequality is immediate. The estimates below give \(e>0\).

## A surviving fraction of the determinant

For two data points \(P_0,P_1\), define \(\Delta v_\ell\) as the vector of coordinatewise \(\ell\)-adic valuation differences \(v_\ell(P_1)-v_\ell(P_0)\). Any character constant on \(V\) pairs to zero with this integral vector, so adding a real multiple of \(\Delta v_\ell\) to log-magnitudes moves along \(V\) in the positive real torus. Choose \(P_1\) later than \(P_0\). Write \(\Delta n=n_1-n_0>0,\ \Delta u=u_1-u_0,\ \Delta a_j=a_j(P_1)-a_j(P_0)\). We have \(\Delta(n-u)>0\). Each growing \(a_j\) has \(\Delta a_j>0\), and all fixed run lengths are constant on \(V\).

Choose any positive real point of \(V\) with \(U=1\), which exists by \(U=c z^t\). In this fiber vary the positive real coordinates by adding a multiple of
\[
 \mathbf v=\Delta u\,\Delta v_2+\Delta n\,\Delta v_3
\]
to their log-magnitudes. The \(U\)-coordinate has weight \(\Delta u\,\Delta n-\Delta n\,\Delta u=0\), so the motion preserves the fiber. Assign to each monomial in (2) its weight under this motion. In a growing run the weight of \(2^{p_j}3^{s_j+a_j}\) exceeds the weight of \(2^{p_j+a_j}3^{s_j}\) by exactly \(\Delta(n-u)\Delta a_j>0\). In a fixed-length run combine the two terms into one positive constant \(3^{a_j}-2^{a_j}\) times \(2^{p_j}3^{s_j}\). Consequently the terms of maximal weight form a nonempty collection of at most \(J\) positive monomials at the positive base point.

At the \(t\) complex components \(z=\rho\zeta^i\), with \(\rho=c^{-1/t}\) and \(\zeta=\exp(2\pi i/t)\), use the same initial values for \(\mathbf y\) and the same magnitude motion. Each highest-weight monomial acquires the phase \(\zeta^{i m}\) for its integer exponent \(m\) of \(z\). Combining equal residue exponents gives Fourier data \(c_m\ge0\) of support size \(b\le J\), not all zero. Its discrete Fourier transform is nonzero on at least \(t/b\) indices. Indeed
\[
 \sum_i|\widehat c(i)|^2=t\sum_m c_m^2
 \ \ge\ (t/b)\Big(\sum_m c_m\Big)^2,\qquad
 |\widehat c(i)|\le\sum_m c_m .
\]
On every such index the top weight has nonzero coefficient, so \(P|_V\) is not identically zero on that component. One can see this by sending the magnitude parameter to \(+\infty\) after dividing by the top exponential. Every such root of \(f\) is a root of \(f_1\). Thus \(e/t\ge1/J\ge1/K\). This argument also shows \(P|_V\) is nonzero on the positive real component \(z=\rho\).

For primitive counts \(\gcd(n,u)=1\), already \(\gcd(n_0,u_0)=1\). The polynomial \(f(z)\) is irreducible over \(\mathbb Q\). If \(d_0=[\mathbb Q(\rho):\mathbb Q]\), then \(N(\rho)^t=(3^{u_0}/2^{n_0})^{d_0}\), giving \(t\mid n_0d_0\) and \(t\mid u_0d_0\). Hence \(t\mid d_0\), and \(d_0=t\) since \(f(\rho)=0\) has degree \(t\). As \(P\) is nonzero on the positive component, it has no common factor with \(f\). Thus \(f_1=f\), which gives the stronger assertion about \(G\).

More generally, if \(g=\gcd(n,u)\) is fixed on the subsequence, the same positive-root norm gives \(t\mid g d_0\). Its full rational minimal polynomial divides \(f_1\), so \(e/t\ge1/g\). To obtain the uniform maximum in the theorem it suffices to consider \(g<K\), which has finitely many possible values. All other subsequences are covered by \(1/K\).

## From the surviving polynomial to the integer denominator

The actual positive rational \(z\) satisfies \(z^t=2^{n-n_0}3^{-(u-u_0)}\). Uniqueness of prime factorization implies the two exponent differences are divisible by \(t\). Thus \(z=A/B\) with \(A=2^{(n-n_0)/t}\), \(B=3^{(u-u_0)/t}\) coprime integers. Both exponents are nonnegative by the subsequence choice, since \(u=\sum_j a_j\). Homogenizing the integral factorization of \(f\) at \(A,B\) gives integer factors
\[
 F_1=B^e f_1(A/B),\qquad F_2=B^{t-e}f_2(A/B),\qquad
 F_1F_2=2^{n_0}A^t-3^{u_0}B^t=D.
\]
In particular \(F_1\) is prime to 6, and its whole gcd with \(C(w)\) is bounded by the outside-\(S\) estimate since \(B\) is an \(S\)-unit. Hence \(\log\gcd(|F_1|,C(w))=o(n)\).

For any fixed root \(\rho\zeta^i\) of \(f_1\),
\[
 \frac{|A-B\rho\zeta^i|}{A}
 \ \ge\ 1-\rho B/A
 \ =\ 1-(3^u/2^n)^{1/t}
 \ \ge\ (1-3^u/2^n)/t .
\]
The last estimate follows from the geometric sum. Input 2 bounds this below by a fixed reciprocal polynomial in \(n\). The nonzero leading coefficient of \(f_1\) is fixed. Taking its product over \(e\) roots yields \(\log_2|F_1|\ge e(n-n_0)/t-O_V(\log n)\). Since \(|F_1|\mid D\), prime valuations give \(|F_1|/\gcd(|F_1|,C(w))\mid d\). This proves (1) and contradicts the chosen violating margin. In the primitive-count case \(F_1=\pm D\) and the gcd estimate itself gives \(\log G=o(n)\), independently of input 2; that input converts it to \(\log_2d/n\to1\).

## A primitive three-run example with exponent \(3/4\)

Dilate every bit of the eight-bit base word \(10110100\) into \(l\) copies of itself. Its length is \(8l\) and its weight is \(4l\). Every boundary site is a multiple of \(l\). A translation preserving the word must preserve this boundary set and hence be a multiple of \(l\). The induced base rotation is trivial, so the dilated words are primitive. They have three odd runs.

With \(X=2^l,\ Y=3^l\), (2) and direct factorization give
\[
 C=(Y-X)(X^2+Y)(X^3+Y^2),\qquad
 D=(X^2-Y)(X^2+Y)(X^4+Y^2).
\]
The common \(X^2+Y\) removes asymptotically one quarter of \(\log_2D\). The displayed cofactors are coprime Laurent polynomials. For example their irreducible factors over \(\mathbb Q[X,Y]\) are the distinct primitive binomials shown, apart from \(X^4+Y^2\), irreducible over \(\mathbb Q\) as a quadratic in \(Y\). The other nonlinear numerator binomial \(X^3+Y^2\) is irreducible by the same construction or the coprime exponent test. Apply input 1 to the two cofactors at \((2^l,3^l)\). Every proper subtorus translate imposes a nontrivial relation \((2^a3^b)^l=c'\) and meets this sequence at most once. The additional cancellation has logarithm \(o(l)\) and the points have positive \(D\). Therefore \(\log_2d/(8l)\to3/4\). The coprime-count hypothesis in the full-exponent conclusion has substantive content.

If arbitrary presented periods are allowed, the \(1/K\) coefficient is sharp. Take \(K\) exact repeats of the one-odd-run word \(10^{l-1}\) with \(l\to\infty\). The base word has determinant, and reduced denominator, \(2^l-3\), and the repeats describe the same rational states at presented length \(Kl\). This example has primitive period \(l\). Sharpness of \(1/K\) for every fixed \(K\) under the additional least-period requirement is a separate question.
