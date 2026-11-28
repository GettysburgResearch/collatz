# A quantitative cost for growth near the largest odd-step multiplier

Let \(a_0=m\) be a fixed positive odd integer and let \(2^{e_j}a_{j+1}=3a_j+1\) be its actual odd Collatz orbit. Suppose \(g=\liminf_{j\to\infty}j^{-1}\log a_j>0\). Use natural logarithms. Put
\[
 A_N=\sum_{j<N}e_j,\quad S_N=A_N-N,\quad
 K_N=\#\{j<N:e_j>1\},\quad P=\lim_{j\to\infty}2^{A_j}3^{-j} a_j.
\]
The limit is positive and finite. If **\(P\) is algebraic**, of degree \(d\), set \(D=\log(6d)\). There is an absolute constant \(C\) and a fixed constant \(C_m\), depending on the specified orbit and its positive lower growth, such that for all sufficiently large \(N\),
\[
 \log\frac{N}{1+S_N}\le C_m+
 C(1+K_N)^{2/3}\{D\log[(2+K_N)D]\}^{1/3}.                  \tag{1}
\]
In particular there is an absolute \(c>0\) such that at every sufficiently large \(N\),
\[
 S_N\ \ge\ c\frac{(\log N)^{3/2}}{\sqrt{D\log\log N}},\qquad
 a_N\ \le\ P(3/2)^N 2^{-c(\log N)^{3/2}/\sqrt{D\log\log N}}. \tag{2}
\]
At any dates with \(S_N\le N^{1-\delta}\), fixed \(0<\delta<1\), the first inequality of (2) holds with \(K_N\) on its left and an additional factor \(\delta^{3/2}\) in the absolute lower constant. Thus it counts genuinely distinct exceptional dates under this observed-prefix condition. All statements include rational \(P\). The growth hypothesis by itself provides no algebraicity, and the proof does not give an onset computable from the starting integer.

## Two limits of the same finite sums

Write \(H_j=2^{A_j}/3^j\) and \(B=\log(3/2)\). The physical identity
\[
 H_j a_j=m\prod_{i<j}\left(1+\frac1{3a_i}\right)
\]
gives \(P\) by convergence of the reciprocal sum. For each fixed \(0<h<g\), \(H_j\ll_m e^{-hj}\). The rational partial sums \(R_j=H_j(a_j+1)\) tend to \(P\) in the reals and to zero in the dyadic field. Their exact positive increments are
\[
 R_{j+1}-R_j=(2/3)^{j+1}(2^{S_{j+1}}-2^{S_j})\le H_{j+1}.       \tag{3}
\]
They increase strictly at precisely the dates \(j+1\) with \(e_j>1\). There are infinitely many such dates, since an all-ones tail of length \(l\) from positive \(a\) would require \(2^l\mid a+1\). Equation (3) also bounds the real tail after date \(N\) by \(C_m'e^{-hN}\). The two completion limits serve as different approximation targets.

Fix one large \(N\) and truncate at \(T=\lfloor\min(1/2,h/(2B))N\rfloor\). Take the ordered distinct dates from 0 through \(T\) consisting of 0, \(T\), and all intervening strict increases. For neighboring dates \(u<v\) with \(u<T\), use the integer coordinates
\[
     x_u=3^u R_u=2^{A_u}(a_u+1),\qquad y_u=3^u.
\]
The error on this *single tested prefix* and the exact dyadic divisibility satisfy
\[
 0<P-x_u/y_u\le C_m''2^{S_N}(2/3)^v,\qquad 2^v\mid x_u.        \tag{4}
\]
Indeed the first possible positive increment after \(u\) has label at least \(v\). Up to \(N\), bound each geometric factor in (3) by \((2/3)^v\) and sum the differences of powers of two. Beyond \(N\), use the preceding exponential tail bound and \(v\le T\). For the second assertion \(R_{v-1}=R_u\), while \(A_{v-1}\ge v-1\) and \(a_{v-1}+1\) is even. This argument includes a final artificial endpoint at \(T\). Also \(2^v\le x_u<P3^u\), so
\[
                        v\le (\log_2 3)u+\log_2 P.              \tag{5}
\]
The partial sums indexed by the distinct left endpoints are strictly increasing, including the initial value if there is an increase before \(T\).

## Quantitative simultaneous approximation

We use Bugeaud and Evertse, Corollary 5.2 of *On two notions of complexity of algebraic numbers*. In their system (5.11), an algebraic real \(\xi\), positive integer \(y\), integer \(x\), and nonnegative local exponents with total \(2+\epsilon\) are permitted. Our finite-place exponents are at most one. For \(y>\max(2H(\xi),2^{4/\epsilon})\), the solutions lie on at most \(2^{32}(1+\epsilon^{-1})^3\log(6d)\log[(1+\epsilon^{-1})\log(6d)]\) rational lines. Their Theorem 3.1 and its proof in §8 give the corresponding three-halves exponent for the digit changes of an algebraic real in a fixed integer base. Here the approximation has both real and dyadic gains, mixed powers, and weights from actual extra halvings. [Bugeaud and Evertse, Acta Arithmetica 133 (2008), §§5 and 8](https://arxiv.org/pdf/0709.1560)

Let \(\theta=\log_3 2\). For \(0<\eta\le1/4\), any gap with \(v\ge(1+2\eta)u\) and \(u\ge C_{m,P}(1+S_N)/\eta\), with the fixed constant chosen large enough, supplies the theorem's system for \(\xi=P,\ \epsilon=\eta\) and
\[
 f_\infty=(1-\theta)(1+\eta),\qquad f_2=\theta(1+\eta),\qquad f_3=1.
\]
Namely \(|P-x_u/y_u|\le y_u^{-f_\infty}\) by (4), \(|x_u|_2\le y_u^{-f_2}\) by its divisibility, and \(|y_u|_3=y_u^{-1}\). The real error prefactor is absorbed since \(B\eta u\ge \log C_m''+S_N\log2\). The same lower cutoff on \(u\) makes \(y_u\) strictly exceed both height cutoffs. We use \(S_1=\{2\},S_2=\{3\}\) in (5.11), and \(f_2<1\). The coordinates need not be primitive. Each rational line holds at most one of these pairs, because their real slopes \(R_u\) are strictly increasing. Thus the number of such gaps is at most
\[
                          C D\eta^{-3}\log(2D/\eta).                 \tag{6}
\]

For \(0<\epsilon\le1/4\) start counting above \(U=C_{m,P}(1+S_N)/\epsilon\), increased to exceed \(1+\log_2 P\). The portion of the ordered sequence through the first crossing of \(U\) contributes at most \(\log(C_{m,P}'(1+S_N)/\epsilon)\) to \(\log T\), by (5). The statement also holds if the whole sequence is below the cutoff. For the remaining gaps \(v/u-1\) is at most two by (5). The number above \(2\eta\) for every \(\epsilon\le\eta\le1/4\) satisfies (6), since \(U\ge C_{m,P}(1+S_N)/\eta\). Integrate the counting function of the gaps, using \(\log(v/u)\le v/u-1\), the trivial bound \(K_N+1\) below \(2\epsilon\), and (6) at \(\eta=1/4\) above \(1/2\). This yields
\[
 \log T\le\log\frac{C'_{m,P}(1+S_N)}{\epsilon}
       +2\epsilon(K_N+1)+C D\epsilon^{-2}\log(2D/\epsilon).         \tag{7}
\]
Choose \(\epsilon=[D\log((2+K_N)D)/(1+K_N)]^{1/3}\). For the fixed source and degree this lies in \((0,1/4]\) at all sufficiently large \(N\), since \(K_N\to\infty\). Substitution into (7), absorbing \(\log(1/\epsilon)\) into the main term and using \(T\asymp_m N\), proves (1). For (2) it is enough to consider \(S_N\le(\log N)^2\), since larger values already satisfy it. Now \(K_N\le S_N\), the left of (1) is \((1-o(1))\log N\), and \(\log[(2+S_N)D]\le 3\log\log N\) for large \(N\). The growth bound follows from \(H_Na_N\le P\). The distinct-date consequence has the same proof using \(\log[N/(1+S_N)]\ge (\delta-o(1))\log N\) and first disposing of \(K_N>(\log N)^2\).

The corrected-height cocycle and one-date algebraic smooth-part obstruction are prior in [PR215, matched real intercepts and smooth parts](https://github.com/GettysburgResearch/collatz/blob/78fb05edaaf76acf0d336e37c0321b91f3db96b7/research/astra-nine-hour-20261128/machinery/phase2/MATCHED_INTERCEPT_AND_SMOOTH_PARTS.md). The quantitative gap-count method and its exponent belong to Bugeaud–Evertse. The fixed-source input here is (3)–(5), including the future tail control after a single tested prefix, and their joint application to actual exception counts.
