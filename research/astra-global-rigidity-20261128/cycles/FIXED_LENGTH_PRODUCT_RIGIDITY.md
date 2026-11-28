# Unrestricted fixed-length product separation through order sixteen

For each fixed length \(L\ge1\) there exists a finite height \(H_L\) such that, on every positive native odd Collatz segment of \(L\) steps with minimum above \(H_L\), all \(k\)-fold index multiset products are distinct for every \(1\le k\le16\). All individual and total division counts are unrestricted. This proof is elementary but does not give a numerical function \(H_L\). Through order five the [explicit bound](UNRESTRICTED_FIVE_PRODUCTS.md) \(2^{8(L+1)^2}\) is stronger.

More generally fix \(L,k\) and a pair of distinct \(k\)-multisets. Cancel common indices, leaving \(h\) per side, and trim to the first and last remaining indices, denoted \(0,m\). Orient the signed multiplicities \(c_i\) so that \(t=c_m>0\). If there are collisions with unbounded minimum then
\[
                             9\mid t,\qquad h-t\ge8.                   \tag{1}
\]
Both restrictions apply to the same collision pattern. They are necessary conditions; no such family is constructed. For fixed \(L,k\) there are finitely many patterns, giving the opening assertion. [Weaver, Paper 163, all orders under a total-division budget and backward coordinates](https://rstation.ai/problems/collatz/papers/163)

## Grouping powers on one scale

The positive odd vertices obey \(T_i x_{i+1}=3x_i+1\), \(T_i=2^{a_i}\), \(a_i\ge1\). Suppose a fixed pattern has collisions with minimum tending to infinity. Set \(A=\max_{0\le i<m}a_i\). Define the rational polynomials
\[
 P_m=Y,\qquad P_i=(T_iP_{i+1}-1)/3,\qquad
 F(\mathbf T,Y)=\prod_{c_i>0}P_i^{c_i}-\prod_{c_i<0}P_i^{-c_i}.
\]
For every positive numerical \(\mathbf T\) the linear factors \(P_i\) have successively increasing distinct real roots in reverse index order: at the root of \(P_{i+1}\) the preceding factor equals \(-1/3\). Thus \(F(\mathbf T,Y)\) is nonzero as a polynomial in \(Y\). After a fixed denominator clearing its coefficients at \(\mathbf T=2^{\mathbf a}\) have absolute values \(\exp(O_{L,k}(1+A))\). A polynomial root bound gives \(\log(1+x_m)=O_{L,k}(1+A)\); in particular \(A\to\infty\).

Retain a subsequence on which \(\alpha_i=\lim a_i/A\) and \(\lim\log(x_m)/A\) exist. Call \(i\) large if \(\alpha_i>0\), small otherwise. There is at least one large index. A rational numerical coefficient is called small in the proof if its numerator and denominator have logarithms \(o(A)\) in lowest terms; zero is allowed. Fixed finite sums, products and reciprocals of nonzero small coefficients remain small. The \(T_i^{\pm1}\) at small indices are absorbed into such coefficients. In every expression below the number and degrees of the remaining monomials are bounded along the subsequence. Write \(U=(2^{a_i})_{\alpha_i>0}\) for the large arguments. A monomial \(U^v\) has a fixed limiting weight \(\lambda(v)=\sum\alpha_i v_i\), so \(U^v=2^{(\lambda(v)+o(1))A}\).

We need a consequence of the integer order of growth of ordinary powers of two. Suppose
\[
                x_m=R(U)=\sum_v r_v U^v,\qquad \lambda(v)\ge0,       \tag{2}
\]
where the \(r_v\) are small rational coefficients, possibly changing at every input, and the support is fixed finite. Then the purported collisions are impossible. To prove this, substitute \(R\) in \(F\) and group the finite Laurent terms by their limiting weight. The sum of all groups is exactly zero at the input. After factoring one monomial out of any one group, its numerical value is a small rational: every remaining ratio is an integral power of two with exponent \(o(A)\). A nonzero group at weight \(\lambda\) therefore has absolute value \(2^{(\lambda+o(1))A}\). Since distinct weights have a fixed positive separation, the largest nonzero group cannot cancel the smaller ones. Taking a further subsequence if necessary to fix which groups vanish proves that each group vanishes separately at every sufficiently late input.

Choose a vector of positive integers \(D_i\) on the large indices which gives equal dot products on all equal-weight monomials in \(F(U,R(U))\), gives dot product zero on all weight-zero monomials in \(R\), and positive dot product on every positive-weight monomial there. Such a vector exists because the positive real vector \((\alpha_i)\) satisfies these finitely many rational homogeneous equalities and strict inequalities; rational points are dense in their real equality space, and denominators can be cleared. Freeze one sufficiently late actual input. On the arc \(U_i\mapsto U_i z^{D_i}\) every previously vanishing group is multiplied by one common power of \(z\). Hence \(F(U(z),R(U(z)))=0\) identically for \(z\ne0\). The actual \(R(U(z))\) is a real polynomial, since every exponent in it is nonnegative. Small input variables remain fixed positive numbers on this arc.

This polynomial identity contradicts positivity. Put \(p_i(z)=P_i(U(z),R(U(z)))\), with the fixed small coordinates understood. Every \(p_i(1)\) is an actual positive state. At the last large edge \(j\), \(p_j(0)=-1/3\). At any zero of \(p_{i+1}\) the preceding \(p_i\) is \(-1/3\). If any polynomial with index greater than \(j\) has a zero in \([0,1)\), successive preceding polynomials have strictly later zeros by their positivity at 1. If none has a zero, \(p_j\) already has one in \((0,1)\). Propagating greatest zeros back to index zero gives a zero of \(p_0\) strictly later than every zero of every other \(p_i\) in \([0,1)\). Only one side of the product identity contains \(p_0\), an impossibility. In particular \(\log x_m=o(A)\) is ruled out by using \(R=x_m\) as a small constant. Thus after extraction \(\log x_m\gg A\).

## The first large division in reverse order

Let \(S_i=\sum_{j<i}a_j\). The height alignment lemma in the [triple-product proof](UNRESTRICTED_TRIPLE_PRODUCTS.md) gives \(\sum c_i i=\sum c_i S_i=0\) eventually. Use its normalized offsets \(s_i\) and \(Z=2^{a_{m-1}}x_m\). In detail, set
\[
 d_b=\sum_{i\le m-1-b}c_i,\quad E_b=S_{m-1}-S_{m-1-b},\quad
 w_b=3^b2^{-E_b},\quad s_i=\sum_{b=0}^{m-1-i}w_b,\quad s_m=0.
\]
Write \(G_j\) for the difference of the degree-\(j\) elementary symmetric coefficients of the two lists of offsets; put \(G_j=0\) for \(j>h\). The alignment and positive product collision imply
\[
                   G_1=G_2/Z-G_3/Z^2+\cdots.                         \tag{3}
\]
The offsets and all \(G_j\) are bounded in terms of \(L,k\). In particular \(|G_1|=O(1/Z)\) is exponentially small in \(A\). At least one internal index \(i<m-1\) must be large: if the final edge alone were large, \(\sum c_i S_i=0\), divided by \(A\), would read \(c_m\alpha_{m-1}=0\).

Let \(b_*\) be the first \(b\ge1\) such that \(m-1-b\) is large. Truncate every \(s_i\) by deleting increments \(w_b\) with \(b\ge b_*\), and denote the new offsets and symmetric differences by \(s_i^*,G_j^*\). These quantities are small rationals. Since all deleted increments contain the factor \(2^{-a_{m-1-b_*}}\), there is a constant \(\eta>0\) on the extracted sequence such that \(s_i-s_i^*=O(e^{-\eta A})\) and \(G_j-G_j^*=O(e^{-\eta A})\). It follows that \(G_1^*=0\) eventually: a nonzero small rational has magnitude at least \(e^{-o(A)}\).

We prove first that **\(G_2^*\ne0\) is impossible** on an infinite subsequence. Then \(|G_2^*|\ge e^{-o(A)}\), hence the same lower bound up to a fixed factor holds for \(|G_2|\). Put \(w=1/Z\le e^{-\eta' A}\). Equation (3) gives
\[
       x_m=2^{-a_{m-1}}\big(G_2/G_1-G_3/G_2\big)+O(e^{-\eta''A})     \tag{4}
\]
for some \(\eta''>0\). Indeed \(G_1=G_2w-G_3w^2+O(w^3)\); dividing by \(G_2w\) and expanding the reciprocal through its linear term costs \(O(w e^{o(A)})\) in the expression for \(Z\). In particular \(G_1\ne0\). Also \(G_3/G_2=G_3^*/G_2^*+O(e^{-\eta'''A})\) for some \(\eta'''>0\).

To expand \(G_2/G_1\), use \(G_1=\sum_b d_bw_b\). Group successive terms according to the intervening large gaps in their cumulative exponents \(E_b\). Each group's common monomial in large coordinates has a strictly smaller limiting weight than the preceding group's common monomial. Its numerical coefficient is a small rational. Discard zero groups (passing to a fixed pattern on a subsequence). Factoring the first surviving group writes
\[
                    G_1=c\,U^v(1+V),\qquad |V|\le e^{-\theta A}
\]
for some \(\theta>0\), with \(c\ne0\) small. If there is only one surviving group take \(V=0\). The finite Laurent polynomial \(V\) has small coefficients; \(G_2\) does as well, by construction. Since \(|G_2/(cU^v)|\le e^{C A}\) for a fixed \(C\), the finite geometric expansion \(\sum_{j=0}^N(-V)^j\) approximates \(1/(1+V)\) accurately enough to give absolute error \(O(e^{-A})\) in \(G_2/G_1\), taking any fixed \(N>(C+2)/\theta\).

Consequently (4) approximates the integer \(x_m\), with an error \(O(e^{-\epsilon A})\) for some \(\epsilon>0\), by a fixed-support Laurent polynomial in \(U\) having small rational coefficients. The prefactor \(2^{-a_{m-1}}\) is a monomial or a small coefficient, and cannot increase the approximation error. Delete every monomial whose limiting weight is strictly negative; the omission is still exponentially small. Each remaining monomial value with strictly positive limiting weight is an integer power of two with eventually nonnegative exponent. For limiting weight zero its rational denominator is \(e^{o(A)}\). Thus the common denominator of the retained finite sum is \(e^{o(A)}\). Its exponentially small distance from the integer \(x_m\) forces exact equality. This is precisely the forbidden representation (2), proving the assertion.

## Two congruences at opposite ends

On any remaining infinite sequence both \(G_1^*=G_2^*=0\) eventually. Newton's identities then give \(\sum_i c_i s_i^*=\sum_i c_i(s_i^*)^2=0\). Since \(\sum_i c_i=0\), the same holds with the summand \((1-s_i^*)^2\). At \(i=m\) this summand equals 1, while at every other index \(s_i^*\equiv1\bmod3\) in \(\mathbb Z[1/2]\) because the first increment is 1 and every later increment is divisible by three. Thus \(9\mid c_m\).

For the opposite end remove trailing zero \(d_b\) from the retained prefix, leaving the last nonzero \(d_v\). Every time such a last increment is removed, the indices it had moved all shared one maximal offset, and their signed multiplicity was exactly zero. Removing it preserves *all* signed power sums. There must have been a positive \(d_b\) on this prefix: \(\sum d_bw_b=0\), all \(w_b>0\), and \(d_0=-t\). In particular \(v\ge1\). At this shortened cutoff scale multiply each offset by \(2^{E_v}\). The indices moved by the final increment all have the same odd integer offset, and their signed multiplicity is \(d_v\). All other scaled offsets are even because \(E_v>E_b\) at previous increments. For \(P(X)=X(X-2)\), \(P(X)\) is odd on odd integers and is a multiple of eight on every even integer. The two vanishing moments annihilate \(P\), so \(8\mid d_v\).

Always \(d_b\le h-t\), since none of the \(t\) terminal positive indices lies in its defining initial segment. After the first positive \(d_b\), the later coefficients are at least \(1-(h-t)\): they can decrease by at most all of the \(h-t\) preterminal positive units. This applies to \(d_v\). Thus \(8\le |d_v|\le h-t\), giving (1). When \(k\le16\), a positive multiple of nine plus at least eight exceeds the entire cardinality.

The argument uses the ordinary integrality of the terminal state in recovering (2) from an exponential approximation. Positivity is used on the resulting real polynomial arc. If both first and second clipped moments vanish, equation (3) can instead present a multiple root at \(1/Z=0\), and expansion (4) is unavailable. No claim here excludes that remaining case.
