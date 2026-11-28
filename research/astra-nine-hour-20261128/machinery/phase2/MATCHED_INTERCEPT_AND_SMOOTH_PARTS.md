# Matched real intercepts, bounded shadow dates, and arithmetic separation on one orbit

**Written theorems.** On a positive odd escaping orbit with lower exponential growth rate \(g>0\), a positive lower density of ordinary dates has uniformly bounded *absolute* correction \(P(a_j)-a_j\). Two distinct dates of comparable size have exponentially large product of their prime-to-\(S\) cofactors, for every fixed finite prime pool \(S\). The shifted assertion has exactly one possible additional case: the actual intervening word follows a closed signed Collatz orbit based at the specified negative shift. A separate one-date theorem gives a restriction on algebraic corrected height, without assuming such algebraicity holds.

Let \(a_j=U^j m\) be the actual odd orbit of one positive odd \(m\), \(e_j=v_2(3a_j+1)\), \(A_j=\sum_{i<j}e_i\), and \(P_j=P(a_j)=3^j2^{-A_j}P(m)\) on escape. Put \(C_j=P_j-a_j\) and \(B=\log(3/2)\). The positive and finite height product, its cocycle and \(P_j/a_j\to1\) are the pinned ordinary results. Their exact compatible series gives
\[
 C_j=\frac13\sum_{r\ge0}\frac{P_j}{P_{j+r}},\qquad
 \frac{C_j}{P_j}-\frac{C_{j+1}}{P_{j+1}}=\frac1{3P_j}.             \tag{1}
\]
Indeed the affine recurrences give the difference identity. Telescope to infinity using \(C_i/P_i\to0\). Each ratio \(P_{j+r}/P_j\le(3/2)^r\), so \(C_j\ge1\). Equality would force every future exponent to be one. That would make \(a_j+1\) divisible by arbitrarily high powers of two, since \(U(a)+1=3(a+1)/2\) on an exponent-one step. Thus \(C_j>1\) for positive integer sources. [Ordinary corrected height and path posterior](https://github.com/GettysburgResearch/collatz/blob/100ba857239a180840930765047d65ede92abeec/research/astra-unconventional-20261126/global/POSTERIOR.md) · [Real mirror and subtraction of the all-ones tail, paper 168, Theorem 1](https://rstation.ai/problems/collatz/papers/168/v1)

## A positive lower density of bounded actual tails

Suppose \(g=\liminf_{j\to\infty}(\log a_j)/j>0\), equivalently the same lower limit with \(P_j\). For \(0<h<g\), define
\[
 J_h=\{j:P_{j+r}\ge P_j e^{hr}\ \text{for every integer }r\ge0\}.
\]
Then
\[
 \underline d(J_h)\ge\frac{g-h}{B-h},\qquad
       1<C_j\le\frac1{3(1-e^{-h})}\quad(j\in J_h).                 \tag{2}
\]
To prove this set \(b_j=\log P_j-hj\) and \(v_j=\min_{i\ge j}b_i\). The minimum exists since \(b_i\to\infty\). The sequence \(v_j\) is nondecreasing and \(\liminf v_j/j\ge g-h\), by taking any slightly smaller slope in the defining lower limit. If \(v_{j+1}>v_j\), the minimum was attained at \(j\), hence \(j\in J_h\), and \(v_{j+1}-v_j\le b_{j+1}-b_j\le B-h\). Telescoping proves the density bound. A geometric sum in (1) proves the other bound.

For \(g>\log(6/5)\), one can take \(h>\log(6/5)\). A positive lower density of dates then has \(1<C_j<2\), \(\lfloor P_j\rfloor=a_j+1\), and \(e_j\le2\) by \(C_j=(1+2^{e_j}C_{j+1})/3\). At maximal \(g=B\), every \(J_h\), \(h<B\), has density one. Letting \(h\uparrow B\) gives \(C_j\to1\) in density. These are statements about matched dates on the specified orbit; the all-dates tame survivor classification of Paper 168 requires the stronger condition \(C_j<2\) at every future date.

## An elementary input from the two-dimensional Subspace Theorem

For a fixed finite prime set \(S\) containing two and three, set \(R_S(x)=|x|\prod_{p\in S}|x|_p\) for any nonzero integer \(x\). Thus \(R_S\) is the positive factor with all primes from \(S\) removed, counting multiplicity. For any \(\eta>0\), uniformly over positive distinct integers \(X,Y\) of height \(H=\max(X,Y)\),
\[
 \frac{|Y-X|}{X}\,R_S(X)R_S(Y)\ \gg_{S,\eta}\ H^{-\eta}.           \tag{3}
\]
At the real place take the two independent forms \(Y-X,Y\). At each \(p\in S\) take \(X,Y\). The product of all their absolute values is precisely the left side of (3). Schlickewei's rational-point theorem puts the vectors with product at most \(H^{-\eta}\) on finitely many rational lines. On a fixed exceptional line \(X/Y\ne1\), the factor \(|Y-X|/X\) is a positive constant and both cofactors are integers at least one. The diagonal was excluded. Lower the implied constant finitely many times. This uses the standard integral-vector formulation; equivalently divide by the common gcd first. Its \(S\)-part contributes overall scale one, its prime-to-\(S\) part can only decrease the form product upon division, and the primitive height is at most the given height. The onset and constants are ineffective. [Schlickewei's original theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Bilu's precise integral formulation, Theorem 2.3](https://www.numdam.org/book-part/AST_2008__317__1_0/)

## Pairwise cofactor growth and signed periodic exceptions

Fix \(K_0>1\), a fixed integral shift \(b\), and \(\epsilon>0\). For all sufficiently large \(j<k\le K_0 j\), at least one of the following holds.
\[
 \begin{split}
 &R_S(a_j+b)R_S(a_k+b)\ \ge\ \exp((g-\epsilon)j);                 \tag{4}\\
 &\text{the actual word }(e_j,\ldots,e_{k-1})\text{ is a closed
              signed odd Collatz word at }-b.                       \tag{5}
 \end{split}
\]
For \(b=0\) the second possibility cannot occur. For \(b=1\) it says explicitly that every intervening exponent is one. For \(b=-1\) they are all two.

Set \(r=k-j,\ D=A_k-A_j,\ X=3^r(a_j+b)\), \(Y=2^D(a_k+b)\), both positive eventually. Formula (1) and \(P_i\gg_\zeta e^{(g-\zeta)i}\) imply \(C_i/P_i\ll_\zeta e^{-(g-\zeta)i}\) for each \(0<\zeta<g\). Therefore \((a_i+b)/P_i=1+O_{b,\zeta}(e^{-(g-\zeta)i})\). Corrected scaling cancels exactly in \(Y/X\), leaving
\[
             |Y/X-1|\ll_{b,\zeta}e^{-(g-\zeta)j}.
\]
The bound \(a_i+1\le (m+1)(3/2)^i\), or the equality \(Y/X=1+o(1)\) and the definition of \(X\), gives \(\log H=O_{m,K_0}(j)\). For \(Y\ne X\), choose \(\zeta,\eta\) sufficiently small in (3) to deduce (4). Both monomials factored from the endpoints have all their primes in \(S\).

If \(Y=X\), then \(2^D\mid a_j+b\) and the integral starting point \(-b\) realizes exactly the same \(D\) shortcut bits as \(a_j\). Equivalently its difference from \(a_j\) is a multiple of \(2^D\), so the finite parity bijection applies also to signed starts. The image difference after these steps is \(3^r(a_j+b)/2^D=a_k+b\); hence the signed endpoint is \(-b\). If \(b\) is even the equality already contradicts oddness of \(a_j\) and \(D\ge1\). In particular \(b=0\) is excluded. The signed odd maps fix \(-1\) with valuation one and \(1\) with valuation two, yielding the two asserted descriptions. Conversely a closed signed word based at \(-b\) that agrees with the actual word gives this equality.

If \(j_i\uparrow\infty\) and \(R_S(a_{j_i})=\exp(o(j_i))\), then \(j_{i+1}/j_i\to\infty\); otherwise one bounded-ratio subsequence violates (4) with \(b=0\). Thus there are \(o(\log N)\) such dates up to \(N\) on any such sequence. Paper 138's Theorem 7 already gives the strong relative-height conclusion $\log R_S(a_j)/\log a_j\to1$ in time density on every nonperiodic positive orbit, alongside polynomial-threshold bounds and finite-prefix valuation budgets. The new fast-growth implication controls *every pair* of comparable dates and forces multiplicative lacunarity even inside the exceptional density-zero set. It also treats all fixed additive shifts with explicitly classified signed exceptions. [Weaver, paper 138, Theorem 7](https://rstation.ai/problems/collatz/papers/138)

There is a local version without an escaping-orbit assumption. For any fixed \(H_0>0,\epsilon>0,S,b\), take a sufficiently large positive odd \(a_0\), and an actual segment \(1\le r\le H_0\log a_0\) on which every odd \(a_i\ge a_0\). Then (5) holds, or \(R_S(a_0+b)R_S(a_r+b)\ge a_0^{1-\epsilon}\). The ratio without shifts is the product of \(1+1/(3a_i)\) for \(i<r\), so its distance from one is \(O_{H_0}((\log a_0)/a_0)\); the two bounded shifts change the ratio by \(O_b(1/a_0)\). The same \(X,Y\) have \(\log H=O_{H_0}(\log a_0)\). Apply (3). This holds in particular at each sufficiently large future minimum of any positive escaping orbit.

## A one-date condition on algebraic corrected height

Keep an escaping positive \(m\). Write
\[
 q_j=3^j,\quad B_j=\sum_{i<j}3^{j-i-1}2^{A_i},\quad
 u_j=B_j+b2^{A_j},\quad L=P(m)-m.
\]
For any fixed integer \(b\), \(q_jm+B_j=2^{A_j}a_j\). Consequently
\[
 L-u_j/q_j=2^{A_j}q_j^{-1}(C_j-b),\qquad
         u_j+mq_j=2^{A_j}(a_j+b).                                \tag{6}
\]
In particular \(u_j/q_j\to L>0\) in the reals, by \(2^{A_j}/q_j=P(m)/P_j\), \(C_j/P_j\to0\) and \(P_j\to\infty\). The same quotient tends to \(-m\) in the dyadic field, since \(A_j\ge j\) and \(a_j+b\) is integral.

Suppose \(P(m)\) is algebraic. Take real forms \(Lq-u,q\), dyadic forms \(u+mq,q\), ternary forms \(u,q\), and at every additional \(p\in S\) use \(u+mq,q\). They are independent at each place. For large \(j\), \(0<a_j+b<3^j\); therefore \(|u_j|_3=|a_j+b|_3\) by (6). Multiplication now gives *exactly*
\[
     \prod_{v\in S\cup\{\infty\}}\prod_{i=1}^2|L_{v,i}(u_j,q_j)|_v
        = |C_j-b|\prod_{p\in S}|a_j+b|_p.                          \tag{7}
\]
The archimedean factors contribute \(2^{A_j}q_j|C_j-b|\), canceled by \(2^{-A_j}\) and \(q_j^{-1}\) at two and three. The vector height is \(O_{m,b}(3^j)\) since \(u_j/q_j\to L\). If (7) were \(\le e^{-\epsilon j}\) infinitely often, the same Subspace Theorem would put an infinite subsequence on one rational line. Its slope \(u_j/q_j\) would be a fixed rational, forced both to equal the positive real \(L\) and the strictly negative rational \(-m\) by its two limits. This is impossible. Hence for every \(\epsilon>0\), at all large dates,
\[
       |C_j-b|\prod_{p\in S}|a_j+b|_p>e^{-\epsilon j}.              \tag{8}
\]
At the positive-density dates (2), the \(S\)-smooth part of \(a_j+b\) must therefore be \(\exp(o(j))\), equivalently \(a_j^{o(1)}\) when \(g>0\), for each fixed shift \(b\). For \(b=0,S=\{2,3\}\) on a unit orbit the product (7) equals \(C_j>1\) identically. Thus the unshifted real/dyadic truncation alone cannot give any strict product saving. The shifted forms identify exactly the additional physical arithmetic that can force transcendence.

The alternatives here constrain the original macroscopic-intercept branch of a single specified source. There is no independent proof that \(P(m)\) would be algebraic, that two comparably placed small cofactor dates must occur, or that the bounded-shadow dates in (2) eventually occupy all times. These are the first missing hypotheses for those respective applications.
