# Full denominators at every fixed number of separated valuation mismatches

**Proposed written theorem.** Fix an integer \(s_0\) and a real \(\delta>0\). Let a primitive positive rational odd Collatz cycle have \(p\) odd edges and common complete reduced denominator \(q\). Suppose some proper rotation of its native valuation word has at most \(s_0\) mismatches, and every cyclic gap between consecutive mismatches is at least \(\delta p\) odd edges. Then constants \(c=c(s_0,\delta)>0\) and \(p_0=p_0(s_0,\delta)\) exist with
\[
                         q\ge 2^{c p}\qquad (p\ge p_0).
\]
This applies at every rotation order and without a bound on the largest valuation, physical width, minimum or total clock error. Thus on any growing family of ordinary cycles with boundedly many mismatches, the shortest mismatch gap divided by \(p\) tends to zero. The constants are ineffective here.

The six-mismatch theorem of PR212 allows arbitrary gaps. Its arithmetic compares difference quotients at consecutive mismatch dates. Here two whole positive laps yield two forms with the same exponential dyadic saving. Multiplying their equations by a finite set of monomials charges every shared carry only once in the limit of large translation sets.

## Actual roots, dates and carries

Argue against a subsequence \(p\to\infty\), \(\log_2 q=o(p)\) with the stated properties. Write \(\gamma=\log_2 3,\ \beta=\gamma-1,\ m=\min x_i,\ y_i=qx_i\). The native equations are \(2^{e_i}y_{i+1}=3y_i+q\), with all numerators positive odd. The denominator divides \(2^A-3^p\), \(A=\sum e_i\), and every numerator has an incoming odd edge, so \(q\) and the numerators are ternary units. Distinct phases have distinct numerators. A proper period of the exponent word would repeat the affine composition of its smaller block, whose slope is positive and different from one. A positive point fixed by an iterate of that affine map is already fixed by the map, contrary to least period. Hence a proper rotation has a mismatch. Replacing the rotation by its inverse preserves the cyclic gaps up to translation and gives a forward lag \(\ell\le p/2\).

The minimum satisfies \(\log_2(m+1)=O(\log p)\). If \(m\ge1\), the positive lap implies \(A/p\le 2\), and \(0<A\log 2-p\log 3\le p/(3m)\). Apply the published two-logarithm bound. If \(m<1\), the bound for \(\log_2(m+1)\) is immediate. Every odd step satisfies \(y'+q\le(3/2)(y+q)\), so \(\log_2\max_i y_i\le\beta p+o(p)\). [Bondareva, Luchin and Salikhov, Theorem 1, printed p. 18](https://www.mathnet.ru/php/getFT.phtml?jrnid=cheb&option_lang=eng&paperid=619&what=fullt)

Mark the dates *immediately after* the mismatches. Choose an additional starting date within the next \(\eta p\) odd steps **forward** from the physical minimum, with \(\eta=1/100\), at distance at least \(b p\) from every mark on the circle. Such a date exists for large \(p\) by removing at most \(s_0\) intervals of length \(2bp+O(1)\), for example \(b=\eta/[8(s_0+1)]\). This avoids backward height estimates across a large division. Call the two actual numerators at that start and its translate \(Y_0,Y_1\). Then
\[
                   \log_2(Y_0Y_1)\le\beta(1/2+2\eta)p+o(p).              \tag{1}
\]
Starting with this cut, put \(0=t_0<t_1<\cdots<t_k=p\), using the marked dates and the full-lap endpoint. Every \(L_i=t_i-t_{i-1}\) is at least \(\min(\delta,b)p\). Pass to a fixed \(k\le s_0+1\).

The actual exponents in block \(i\) agree on every edge before the last. Include only the smaller final exponent in the common division sum \(B_i\), and put the excess on its own track. The last step at the artificial cut agrees. Let \(E_{i,j}\) be the actual cumulative divisions on track \(j\) through time \(t_i\), with \(E_{0,j}=0,\ E_{k,j}=A\). The common carry is
\[
 C_i=\sum_{h=0}^{L_i-1}3^{L_i-1-h}2^{F_{i,h}},
\]
where \(F_{i,h}\) uses the first \(h\) exponents of that block, before either unequal last division. Its first term is odd and its last is a ternary unit. Every other term at the respective prime is divisible there. Since \(F_{i,h}\le h+B_i-L_i\), the geometric series gives \(C_i\le 2^{B_i-L_i}3^{L_i}\). Consequently
\[
                         \sum_i\log_2 C_i\le A+\beta p.                  \tag{2}
\]
Subtracting the two common-block equations shows \(2^{B_i}\) divides the nonzero difference of its two starting numerators, by retaining each final excess as an integer power of two on its own endpoint. Thus \(B_i=O(p)\). Every excess is \(O(p)\) since \(2^{e_i}\le3\max y_i+q\). Summing over boundedly many blocks gives \(A=O_{s_0}(p)\). Positivity of the complete lap gives \(A>\gamma p\).

Put
\[
 X=2^A/3^p,\qquad Z_i=qC_i\,2^{E_{i-1,0}}3^{-t_i},\qquad
 v_i=2^{E_{i-1,1}-E_{i-1,0}} .
\]
Telescoping the normalized native recurrences through both entire laps gives
\[
       Y_0+\sum_i Z_i=XY_0,\qquad
       Y_1+\sum_i v_i Z_i=XY_1,\qquad v_1=1.                            \tag{3}
\]
In particular \(v_3(Z_i)=-t_i\) exactly. The multipliers between these paired contributions are pure powers of two, even at exceptional final exponents.

## A field of dyadic powers at the ternary place

Write \(v_i=2^{a_i}\), with \(a_i=O(p)\). Pass to a subsequence on which every fixed integral combination of the \(a_i\) is eventually constant or diverges absolutely, by diagonal extraction over the countably many combinations. Those eventually constant form a saturated sublattice in \(\mathbb Z^k\). Extend its basis to an integral basis, and write \(T_1,\ldots,T_n\) for the powers of two obtained from the complementary linear combinations. Then
\[
                  v_i=c_i T^{h_i},\quad c_i\in2^{\mathbb Z},
                       \quad h_i\in\mathbb Z^n
\]
with fixed coefficients and vectors. Distinct Laurent monomials in \(T\) have dyadic exponents diverging apart. In any fixed nonzero Laurent polynomial the largest term dominates the others in ordinary absolute value, with their summed absolute values relative to that term tending to zero. All nonempty subsums of its distinct monomials are eventually nonzero.

Let \(K=\mathbb Q(T_1,\ldots,T_n)\), evaluated along this subsequence. Every fixed \(0\ne f\in K\) satisfies
\[
                              v_3(f)=o(p).                              \tag{4}
\]
For a Laurent polynomial multiply by a fixed integer and a power of two of exponent \(O_f(p)\) to make all terms integers. Their prime-to-six parts are bounded by constants depending on the polynomial, their ordinary heights are \(2^{O_f(p)}\), and their largest ternary norm is a fixed positive constant. Evertse's Theorem 2 with \(S=\{\infty,2,3\}\) and test place \(3\) bounds the ternary norm of their sum below by \(2^{-\epsilon O_f(p)}\) for every fixed \(\epsilon>0\), up to its fixed constant. An upper bound for that norm follows from the maximum of the terms. This proves (4) for polynomials and their quotients. The case \(n=0\) gives the constant rational field. These facts persist on every further infinite subsequence. [Evertse, *On sums of S-units and linear recurrences*, Theorem 2, p. 228](https://www.numdam.org/item/CM_1984__53_2_225_0.pdf)

The \(Z_i\) are \(K\)-linearly independent even modulo the span of \(Y_0,Y_1\). A relation involving some \(Z_i\) has a latest such index. Its ternary valuation is \(-t_i+o(p)\), strictly smaller than those of every previous active index by the linear gap. The two roots multiplied by field coefficients have valuation \(o(p)\). A unique least valuation precludes the relation, even on an infinite further subsequence. A root-only relation would give \(Y_1=R Y_0\) for a fixed \(R\in K\) on such a subsequence. Eliminate \(X\) between (3). Independence of the \(Z_i\) forces \(R=v_i\) for all \(i\), whence \(Y_1=Y_0\) by \(v_1=1\). Those are distinct actual phases. The full \(k+2\) coordinates are therefore independent in the stated subsequential sense.

## The finite translate system

For a large fixed integer \(D\), let \(\mathcal B=\{0,\ldots,D-1\}^n\), with a singleton if \(n=0\), and \(\mathcal B_i=\mathcal B\cup(\mathcal B+h_i)\). Form one rational vector with coordinates
\[
           Y_jT^u\ (j=0,1,\ u\in\mathcal B),\qquad
           Z_iT^u\ (u\in\mathcal B_i).
\]
No fixed nonzero rational linear relation can hold on an infinite subsequence, by field independence and Laurent monomial independence. The dimension is fixed before applying the Subspace Theorem.

At infinity and three take the coordinate forms. At two retain all the \(Z_i T^u\) coordinate forms. Replace each root coordinate form for \((j,u)\) by the left side of its equation in (3) multiplied by \(T^u\), using \(v_i=c_i T^{h_i}\). All translated coordinates are present. The forms have constant rational coefficients. Their matrix has identity root block, identity carry block and a rectangular off-diagonal block, so is invertible. Each changed form evaluates to \(XY_jT^u\). Writing \([a]=|a|_\infty|a|_2|a|_3\), the exact product over all forms and the three places is
\[
    2^{-2A|\mathcal B|}\,
       ([Y_0][Y_1])^{|\mathcal B|}
       \prod_i(q C_i)^{|\mathcal B_i|}.                                 \tag{5}
\]
Each monomial has three-place product one. The same coordinate basis at infinity and three and the same carry coordinates at two ensure that large boundary monomials incur no additional cost. Each ratio \(|\mathcal B_i|/|\mathcal B|\) tends to one as \(D\to\infty\), for the already fixed \(h_i\).

By (1), (2), \(\log q=o(p)\) and \(A\ge\gamma p\), the base-two logarithm of (5), divided by \(|\mathcal B|\), is at most
\[
 -2A+\beta(1/2+2\eta)p+(1+o_D(1))(A+\beta p+o(p))+o(p).
\]
At vanishing boundary fraction its margin is at least \((\gamma-\beta(3/2+2\eta))p>0\). Because \(A=O_{s_0}(p)\), choose a single sufficiently large \(D\) and then let \(p\) increase. The product in (5) is at most \(2^{-c' p}\) for some \(c'>0\).

Clear vector denominators by powers of two and three, which preserves its three-place product of forms, and divide the resulting integer coordinates by their gcd. The latter operation can only decrease the product since \([d]\ge1\) for a nonzero integer \(d\). For fixed \(D\) the primitive maximum coordinate height \(H\) is at most \(2^{O(p)}\), directly from the displayed integers, exponents and carries. Its constant may depend also on the stabilized generator basis and fixed translation supports. The rational \(S\)-adic Subspace Theorem puts these primitive vectors into a fixed finite union of proper rational subspaces, because the product of the fixed independent forms is below \(H^{-\epsilon}\) for some fixed \(\epsilon>0\). Bounded heights also give a finite union of lines. One proper subspace must recur along an infinite subsequence, contradicting the proved rational linear independence. This rules out every violating \(\log q=o(p)\) sequence, which is equivalent to the stated uniform positive rate. [Schlickewei, original \(p\)-adic Subspace Theorem](https://doi.org/10.1016/0022-314X(77)90073-7) · [Bilu, Theorem 2.3, rational integer form](https://www.numdam.org/item/AST_2008__317__1_0.pdf)

## Source handoff and exact limitation

PR212 at 505d3fe782922904e86477990cc5d41e9110edda obtains \(q>2^{p/4096}\) through six arbitrary mismatches, including collisions on the \(p\)-scale. Its common last-exponent convention, numerator height estimates and Evertse input are antecedents. The argument above uses the paired complete-lap forms and bounded translates in the dyadic-power field for every fixed number of separated mismatches. For clustered endpoints the difference of the ternary valuations of two \(Z_i\) can be \(o(p)\), so (4) does not establish their independence. Charging the two laps as independent copies of every carry would likewise invalidate (5). [PR212, ROTATION_DENOMINATORS.md](https://github.com/GettysburgResearch/collatz/blob/505d3fe782922904e86477990cc5d41e9110edda/research/astra-infinite-descent-20261127/cycles/ROTATION_DENOMINATORS.md)

[Paired-lap verifier](check_separated_rotations.py) · [Exact replay receipt](separated_rotation_controls.json). The finite controls use 176 primitive rational cycles, including 15 proper nontrivial whole-denominator cancellations, 2,379 rooted paired full laps and 10,279 shared blocks. They check 176 complete three-place products with overlapping carry boxes and negative translation exponents. The finite products test the linear-form ledger. The asymptotic field independence and Subspace Theorem conclusion are written proofs.
