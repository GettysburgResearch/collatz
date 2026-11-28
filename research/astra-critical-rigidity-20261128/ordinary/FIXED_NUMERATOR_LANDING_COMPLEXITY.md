# A small ordinary numerator requires a complex word to clear a ternary denominator

Use the shortcut map on a positive rational with odd denominator. Start at \(m/(q3^n)\), where \(q,m,n\ge1\), \(\gcd(q,6)=1\) and \(\gcd(m,3q)=1\). Stop at the first date \(T\) whose reduced denominator is prime to three. This is the \(n\)-th odd departure and the endpoint is \(P/q\) for a positive integer \(P\). In the main case \(q=1\), this is [first integer landing](POSITIVE_DESCENDING_INTERVALS.md). Varying \(n\) at fixed ordinary numerator \(m\) varies the starting rational.

**Proposed written theorem.** Supply the entire landing word as \(w_1^{r_1}\cdots w_K^{r_K}\), where all templates and repetition counts are nonempty. Let \(B=\sum_i|w_i|\). At each boundary \(i=0,\ldots,K\) let \(D_i,G_i\) count the remaining native dates and odd departures. As \(T\to\infty\), if \(K\) is bounded, \(B=o(T)\), and \(q=1\), then
\[
  \log_2 m\ \ge\ T-\max_i(D_i-\gamma G_i)-o(T),\qquad \gamma=\log_2 3.        \tag{1}
\]
The same bound holds for \(q\) supported on a fixed finite prime set with \(\log q=O(T)\), or for arbitrary \(q\) with \(\log q=o(T)\). Each complement contains at least \(n-G_i\) native dates, so the main term in (1) is at least \(n\). For \(m\le3^n\) and \(\log q=o(T)\) we have \(T=O_K(n)\) on these families, and hence
\[
                            \log_2 m\ge n-o(n).                        \tag{2}
\]
In particular, for each fixed \(K,\eta>0\), all sufficiently large \(n\) and all \(m\le2^{(1-\eta)n}\) on the \(q=1\) grid require \(B\ge c_{K,\eta}T\) with some \(c_{K,\eta}>0\). This applies to every fixed ordinary positive numerator prime to three. If \(T=n+o(n)\), all suffix deficits are at most \(T-n=o(T)\).

There is also an effective estimate, valid with **arbitrary** \(K,q\), with an absolute computable \(C\). In this display all logarithms are natural. Write \(H=1+B+\log(2mq)\). Then
\[
                 n\ \le\ T\ \le\ H\,[C\log(2+n/H)]^K .                 \tag{3}
\]
In particular a fixed-size dictionary budget relative to \(n\) forces many powered pieces as \(n/H\to\infty\):
\[
                K\ge (1-o(1))\frac{\log(n/H)}{\log\log(n/H)}.
\]
For the number \(E=T-n\) of individual even departures, the sharper specialization is
\[
           n\le (1+\log(2mq))[C\log(2+n/(1+\log(2mq)))]^{E+1}.         \tag{4}
\]
Thus every fixed \(m,q\) has at least \((1-o(1))\log n/\log\log n\) even departures before landing. The source-height coefficient one in (2) comes from the qualitative Subspace Theorem. Formulae (3) and (4) have an effective onset via Yu's explicit two-factor estimate.

## Centering at the actual cleared endpoint

After a prefix of length \(t\), with \(n-h\) odd departures, write the state as \(d/(q3^h)\). Its odd update sends \((h,d)\) to \((h-1,(d+q3^{h-1})/2)\), its even update to \((h,d/2)\). Until \(h=0\) the numerator is prime to three. Every state has \(d\le\max(m,q3^n)\). In ordinary real coordinates the affine map of a template of length \(b\) and grade \(g\) has slope \(3^g/2^b\), carry \(C_w=\sum_{j=1}^g3^{g-j}2^{t_j}\) for odd dates \(t_j\), and fixed point \(c=C_w/(2^b-3^g)\). Its reduced numerator and denominator have absolute values at most \(2^{O(b)}\), with denominator odd and prime to three. For an all-even template take \(c=0\).

Write \(c_i\) for the center of block \(i\), and \(U_i=3^{G_i}2^{-D_i}\). The affine center identity on each powered block telescopes forward to
\[
         P-\frac m{2^T}
        =q\left[c_K+\sum_{i=1}^{K-1}(c_i-c_{i+1})U_i-c_1 U_0\right].  \tag{5}
\]
Here \(P\) is an integer at the actual terminal date. Formula (5) retains the denominator clearance in the coefficient of the original numerator. The [ordinary powered-prefix theorem](../literature/POWERED_WORD_HEIGHT.md) centers in the other direction on an integral starting state.

Suppose (1) fails by \(\eta T\) on a subsequence. We may pass to a fixed number of nonzero terms \(Z_i=q b_i U_i\) in (5), including its constant when nonzero. All the rational coefficients \(b_i\) have logarithmic height \(o(T)\), where the height of a reduced rational is the maximum of its numerator magnitude and denominator. Write \(F=\max_i(D_i-\gamma G_i)\ge0\). Then
\[
 0<\Delta=P-\sum_i Z_i=m2^{-T}\le 2^{-F-\eta T},\qquad
                |Z_i|_\infty\ge 2^{-F-o(T)}.                            \tag{6}
\]
If there are no nonzero terms, \(\Delta\) is a positive integer, an immediate contradiction. Otherwise take \(S\) to consist of infinity, two, three, and any additional fixed primes supporting \(q\) in the fixed-support case. With \(|p|_p=p^{-1}\), \(\prod_{v\in S}|Z_i|_v\le 2^{o(T)}\). Indeed the binary and ternary powers contribute one, the coefficient contributes at most its height, and \(q\) contributes one or \(2^{o(T)}\) in the two cases.

First use coordinates \((P,Z_1,\ldots,Z_s)\). At infinity replace the \(P\)-coordinate form by the fixed form \(P-\sum_i Z_i\). At each finite place keep all coordinate forms. The product of the absolute values of all forms is at most \(2^{-\eta T+o(T)}\), as \(P\) is integral. Apply the rational \(p\)-adic Subspace Theorem. To check its primitive integral normalization, clear the binary denominators by \(2^T\), whose complete \(S\)-product is one, and all coefficient denominators by an integer of height \(2^{o(T)}\). The number of coordinates is bounded. Dividing by the resulting common integral gcd only decreases the form product. The resulting primitive sup norm is at most \(2^{O(T)}\), since \(m<2^T\), \(\log q=O(T)\) and all word exponents are at most \(T\). Thus a fixed negative power of that norm bounds the form product from above for large \(T\). The theorem places an infinite subsequence in one proper rational subspace. [Schlickewei, original theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Evertse, Theorem 1.1, including the equal-number-of-forms case](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

Use the resulting fixed relations to pass to a basis drawn from the existing coordinates on a further subsequence. If a new relation involves only the pure coordinates \(Z_i\), substitute out one of them in the expression for \(\Delta\) and repeat. If it involves \(P\), substitute out \(P\), after which \(\Delta\) is a nonzero fixed linear form in the remaining pure coordinates. For any such step with only pure coordinates left, at infinity replace a coordinate with nonzero coefficient in this form by the form for \(\Delta\). Its determinant is nonzero. Relative to all the original coordinate forms, this introduces the factor \(|\Delta|/|Z_j|\le2^{-\eta T+o(T)}\) by (6). The same normalized Subspace Theorem again supplies a proper relation. Each elimination strictly decreases dimension. A final relation \(\Delta=c Z_j\) with fixed \(c\ne0\) contradicts (6); if only \(P\) remains, \(\Delta=P\) is a positive integer. This proves (1).

For (2), let \(b\) be a template length and \(c=p_0/H_0\) its reduced center. On its repeated piece of full length \(d_0\), between numerator-height states \((u,h),(v,h-g_0)\), the integral identity is
\[
           2^{d_0}(H_0v-p_0q3^{h-g_0})=H_0 u-p_0q3^h.                  \tag{7}
\]
Its right side is nonzero since \(3\nmid H_0 u\) and \(h>0\). The numerator bound thus gives \(d_0\le O(b+1)+\log_2\max(m,q3^n)\). Summation over bounded \(K\) gives \(T=O_K(B+\log(2m)+n+\log q)\), proving the stated comparison and (2).

## Effective bounds for a variable number of pieces

We use the following corollary of Kunrui Yu's Theorem 2. For nonzero integers \(a,c\), \(1\le h\le n\), \(a+3^h c\ne0\), and any \(H'\ge 1+\log\max(|a|,|c|)\),
\[
          v_2(a+3^h c)\le C H'\log(2+n/H').                           \tag{8}
\]
If the two summands have different valuations, the smaller controls the sum. Otherwise remove their common binary valuation and take \(\alpha_1=3,\alpha_2=-c/a\), exponents \(h,1\). Both are binary units. Work in fixed \(\mathbb Q(\zeta_3)\) at its prime over two to meet (1.2); the restriction of the valuation to rationals is \(v_2\) since two is unramified. The second exponent has valuation zero as required in (1.13). The height of \(\alpha_1\) is constant and that of \(\alpha_2\) is \(O(H')\). In Theorem 2 take \(B_n=1\), \(B=\max(n,3)\) and \(\delta=c_0\min(1,H'/B)\) with a positive sufficiently small fixed \(c_0\). Then \(\delta B=O(H')\) and \(\widetilde h=O(\log(2+n/H'))\). Restore the removed valuation, at most \(H'/\log2\). No multiplicative independence is required in Yu's stated bound. The case \(c=0\) uses \(v_2(a)\le\log_2|a|\). [Yu, *p-adic logarithmic forms and group varieties II*, Acta Arithmetica 89 (1999), Theorem 2 and (1.13)–(1.14)](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8944.pdf)

Let \(t\) be a block's entry date, \(t'\) its exit, and \(h>0\) its entry height. The native prefix carry \(C_{\rm pre}\) satisfies \(2^t u=m+q3^h C_{\rm pre}\) and \(0\le C_{\rm pre}\le2^{O(t)}\). Multiplying (7) by \(2^t\) gives
\[
       2^{t'}\ \bigm|\ H_0m+3^h q(H_0 C_{\rm pre}-p_0 2^t).            \tag{9}
\]
This integer is nonzero by its residue modulo three. The two coefficients in (9) have logarithmic height \(O(H+t)\). Formula (8) and monotonicity of \(x\log(2+n/x)\) give
\[
                H+t'\le C(H+t)\log(2+n/H).
\]
Iteration from \(t=0\) proves (3).

For (4), let \(v_1<\cdots<v_E\) be the dates of the even departures, indexed from date zero. Before date \(v_i\) the height is \(h_i=n-v_i+i-1>0\). The shifted numerator \(d+q3^h\) is halved at odd dates, and at even dates \(q3^h\) is added before halving. Just before date \(v_{i+1}\), or at the final date \(T\) for \(i=E\), this gives divisibility of
\[
 m+q3^{h_i} C_i,\quad
       C_i=3^{n-h_i}+\sum_{j=1}^i3^{h_j-h_i}2^{v_j}
\]
by \(2^{v_{i+1}}\), with \(v_{E+1}=T\). For the first interval use \(m+q3^n\). Positivity ensures nonvanishing. Each \(\log C_i=O(v_i+1)\) since \(n-h_i\le v_i\) and \(i\le v_i+1\). Apply (8) with initial height \(H_*=1+\log(2mq)\) and iterate over the \(E+1\) intervals, exactly as in (9). This proves (4), including an empty list of even dates.

## Sharp source price and the finite lower tail

For \(q=1\) and each fixed \(E\ge0\) let \(m_E(n)\) be the smallest ternary-unit positive numerator with \(T=n+E\). Then
\[
                      \lim_{n\to\infty}\frac{\log_2 m_E(n)}n=1.         \tag{10}
\]
The \(E\) marked dates give at most \(2E+1\) constant runs, of total template length at most \(2E+1\), so (1) applies. For the upper bound, every length-\(T\) word with \(n\) odd departures, ending odd, is exactly a native dyadic residue class of starting rationals. Multiplication by \(3^n\) gives one numerator class modulo \(2^T\), containing a positive ternary unit at most \(3\cdot2^T\). All of its positive ternary-unit members first land at the last date. This bounded representative belongs to the complete \(m<3^n\) grid for large \(n\). The same upper bound holds for any prescribed physical word, and (1) lower bounds every member of each bounded-defect cylinder. When \(E=0\), the class is \(m\equiv-3^n\pmod{2^n}\), the classical near-integer problem for \((3/2)^n\). [Corvaja and Zannier, *On the rational approximations to the powers of an algebraic number*](https://arxiv.org/abs/math/0403522)

On the uniform complete grid \(1\le m<3^n,\ 3\nmid m\), the same elementary cylinder argument yields
\[
 \mathbb P(T=t)=\binom{t-1}{n-1}2^{-t}
              \bigl(1+O(2^t/3^n)\bigr),\qquad t\ge n.                  \tag{11}
\]
Each of the \(\binom{t-1}{n-1}\) disjoint residues has two eligible ternary-unit classes per period \(3\cdot2^t\), giving its exact density up to two integers of endpoint error. Thus the relative approximation is uniform whenever \(t\le\gamma n-\omega(1)\), even when the event is exponentially rare. This finite counting statement, the effective complexity estimate, and the ineffective sharp price concern different quantifiers. They leave the worst possible long landing time and convergence of positive ordinary Collatz orbits open.
