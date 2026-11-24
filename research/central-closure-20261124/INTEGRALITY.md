# A fixed-source Subspace Theorem attempt with moving cuts

**Status: the displayed closing argument fails.** All calculations here
are written mathematics, not Lean formalizations. They do not rule out
other Diophantine forms or all uses of the Subspace Theorem.

## 1. The exact same ordinary source at every cut

Let \(q_i\) be one escaping positive odd orbit, let
\(2^{a_i}q_{i+1}=3q_i+1\), and put

\[
A_j=\sum_{i<j}a_i,\qquad V_j=2^{A_j}q_j,
\qquad\lambda_j=V_j/3^j.
\]

Then

\[
V_j=3^jq_0+\sum_{i<j}3^{j-1-i}2^{A_i},
\qquad\lambda_{j+1}/\lambda_j=1+1/(3q_j).
\]

Use the fixed-source reciprocal-summability input cited in PR192's
`FIXED_SOURCE.md`, at the exact head in `SOURCES.json`, to obtain
\(q_0\le\lambda_j\le\Lambda<\infty\). The boundedness of this
sequence is an explicit input, not a new theorem of this note.
For \(j\ge1\), \(3\nmid q_j\), whether or not \(3\mid q_0\).

At terminal clock \(m\), set \(X_i=3^{m-i}V_i\). For \(a<b\),

\[
X_b-X_a=3^{m-b}2^{A_a}C_{a,b},\qquad
C_{a,b}=\sum_{a\le j<b}3^{b-1-j}2^{A_j-A_a}>0.
\tag{1}
\]

## 2. Every fixed number of cuts leaves an endpoint factor

Choose \(1\le t_1<\cdots<t_s=m\), and use the vector
\((3^m,X_{t_1},\ldots,X_{t_s})\). At the finite places 2 and 3 take
coordinate forms. At the real place take the triangular forms

\[
3^m,\quad X_{t_1},\quad X_{t_2}-X_{t_1},\ldots,
X_{t_s}-X_{t_{s-1}}.
\]

All local systems have determinant one. Since each \(q_{t_i}\) is odd
and prime to three, cancellation using (1) gives the exact raw product

\[
\mathcal P=
q_{t_1}\prod_{i=2}^s
\frac{C_{t_{i-1},t_i}}{2^{A_{t_i}-A_{t_{i-1}}}}.
\tag{2}
\]

Keep only the first positive summand of every \(C\). Then

\[
\mathcal P\ge
3^{1-s}q_m\frac{\lambda_{t_1}}{\lambda_m}
\ge3^{1-s}\frac{q_0}{\Lambda}q_m.
\tag{3}
\]

For fixed \(s\), this diverges uniformly over all placements of the
cuts. These specific forms cannot give the required small local product.
Large separation between the cuts does not remove the first positive
forcing term in each block.

## 3. Taking every cut makes the product small, but changes the problem

Take \(t_i=i\), \(1\le i\le m\). Each block carry is one, so

\[
\mathcal P=q_1\,2^{-(A_m-A_1)}=O_{q_0}(2^{-m}).
\tag{4}
\]

The dimension is now \(d=m+1\), and one fixed orbit provides one vector
at each dimension. The vector is primitive: its first coordinate is
\(3^m\) and its last coordinate is prime to three. Consequently its
projective height is its real maximum and

\[
3^m\le H\le\Lambda3^m.
\]

Finite local sup norms are one. Thus the normalized product in the
Subspace Theorem is precisely \(\mathcal P/H^d\), with determinant
product one. The large-height threshold in Evertse--Ferretti Theorem 3.1
includes \(d^{d/\epsilon}\), with \(0<\epsilon\le1\); their
Corollary 3.2 treats the product inequality. Already \(d^d\) eventually
exceeds \(\Lambda3^m\). That particular large-height estimate therefore
does not cover these vectors. This comparison is not a theorem about all
possible quantitative versions or their small-height ranges.

There is also a more direct arithmetic issue, independent of constants.
Put \(D_i=X_{i+1}-X_i=3^{m-i-1}2^{A_i}\). Then

\[
3D_{i+1}=2^{a_i}D_i.
\]

Every unit gap \(a_i=1\), for \(1\le i\le m-2\), supplies the exact
height-five relation

\[
3X_{i+2}-5X_{i+1}+2X_i=0.
\tag{5}
\]

The corresponding shifted coefficient vectors are linearly independent
by their distinct first nonzero indices. If \(u_m\) is the number of
unit gaps in the full prefix, then \(A_m\ge2m-u_m\). On the other
hand, \(q_m\ge1\) and the bound for \(\lambda_m\) give
\(A_m\le m\log_2 3+\log_2\Lambda\). After omitting the two boundary
indices, there remain at least

\[
(2-\log_2 3)m-O_{q_0}(1)
\]

independent relations (5). Thus the genuine vector already lies in many
explicit exceptional hyperplanes. Producing a containing rational subspace
does not contradict its ordinary realization. The proof would have to
exclude these subspaces or derive incompatible constraints after reducing
them. No dimension bound after that reduction is established here.

For comparison, any integer vector of \(m+1\) coordinates between zero
and \(\Lambda3^m\) has a nonzero relation with coefficients of absolute
value at most three for all sufficiently large \(m\). There are
\(4^{m+1}\) coefficient choices in \(\{0,1,2,3\}^{m+1}\), and only
\(O_\Lambda(m3^m)\) possible integer sums. Pigeonhole gives two equal
sums. Even small relation coefficients are therefore insufficient in
this dimension range.

## 4. Remaining inference

The fixed-dimensional attempt loses smallness; the growing-dimensional
attempt gains smallness but has no exceptional-subspace exclusion. Neither
calculation proves an escaping orbit exists. Neither eliminates one. The
fixed-source hypotheses and full additive forcing have been retained in
both calculations.

Primary reference: J.-H. Evertse and R. G. Ferretti, *A further improvement
of the quantitative Subspace Theorem*, Annals of Mathematics 177 (2013),
513--590, Theorem 3.1 and Corollary 3.2;
[authors' full text](https://arxiv.org/pdf/1008.2340), printed pp. 13--14.
