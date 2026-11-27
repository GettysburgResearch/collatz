# Polynomial relations on consecutive ordinary states

Write \(U(x)=(3x+1)/2^{v_2(3x+1)}\) on positive odd integers. For the actual orbit \(a_i=U^i(a)\), let \(e_i=v_2(3a_i+1)\), \(E_{i,d}=\sum_{i\le j<i+d}e_j\), and \(r=\log_2(3/2)\). The following result allows the window, coefficients, polynomial and degree to vary with the starting date. A *formal identity on the word* means that replacing the starting state by an indeterminate and applying the specified affine maps gives the zero polynomial. Such an identity holds on every positive integer realization of that same word.

## A finite source bound

Let \(P\in\mathbb Z[X_0,\ldots,X_d]\) have total degree \(D\), with \(P\ne0\). Write \(M=\|P\|_1\) for the sum of the absolute coefficients. If \(P(a_i,\ldots,a_{i+d})=0\) and this relation is not a formal identity on the observed word, then
\[
  \boxed{\quad \log_2 a_i\ \le\ \log_2 M+D\big(E_{i,d}+1+rd\big). \quad}       \tag{1}
\]
No condition on the later trajectory is needed.

In fact the successive ordinary states are \(L_j(a_i)\), where \(L_j(X)=3^j2^{-E_{i,j}}X+B_j\), starting with \(L_0=X\). The recursion \(L_{j+1}=(3L_j+1)/2^{e_{i+j}}\) gives \(0\le B_j\le(3/2)^j-1\). In the univariate coefficient norm, \(\|L_j\|_1\le 2(3/2)^d\). Every coefficient of every \(L_j\) has denominator dividing \(2^{E_{i,d}}\). Consequently
\[
      Q(X)=2^{D E_{i,d}}P(L_0(X),\ldots,L_d(X))
               \in\mathbb Z[X],\qquad
      \|Q\|_1\le M[2^{E_{i,d}+1}(3/2)^d]^D .                            \tag{2}
\]
The norm bound follows term by term, by submultiplicativity and \(2(3/2)^d\ge1\). If \(Q\ne0\), remove its initial zero coefficients so its new constant coefficient \(b\ne0\). Since \(a_i\ne0\), the remaining polynomial still vanishes at \(a_i\). Reducing its value modulo \(a_i\) gives \(a_i\mid b\), and \(a_i\le |b|\le\|Q\|_1\) proves (1).

More generally the normalized difference takes integer-spaced values:
\[
 \frac{2^{D E_{i,d}}}{a_i}
 \left(P(a_i,\ldots,a_{i+d})-P(B_0,\ldots,B_d)\right)\in\mathbb Z.       \tag{2a}
\]
This follows by reducing \(Q(a_i)\) modulo \(a_i\). Thus the two values coincide or their distance is at least \(a_i2^{-D E_{i,d}}\). To bound a small observed integer value \(b=P(a_i,\ldots,a_{i+d})\), equation (1) can alternatively be applied to \(P-b\) with coefficient norm at most \(M+|b|\).

[Finite Lean kernel](OrdinaryRelations.lean) proves divisibility by an integer root of the first nonzero coefficient, the resulting coefficient-size bound and the zero-polynomial conclusion at a root larger than every coefficient. The affine substitution and density-one statements have written proofs here.

## A common bound for branching families of actual relatives

There is a pointwise version for a whole finite collection of paths from an ordinary root \(y\), traversing true edges in either direction. Charge a step with division exponent \(e\) the integer cost \(e+1\), and suppose that each path has cost at most \(B\). Different paths and their endpoints can be chosen after \(y\) is given. Write \(z_j=L_j(y)\) for their endpoints, using the indicated forward or inverse affine formulas. For every integer polynomial \(P\) in all those endpoints with coefficient norm \(M\) and degree \(D\),
\[
 P((z_j)_j)=0,\qquad M\,12^{BD}<y
       \quad\Longrightarrow\quad P((L_j(X))_j)\equiv0.                 \tag{2b}
\]
The number of paths enters only through the polynomial norm and degree.

Indeed the integer matrices for the two directions are respectively
\(\left(\begin{smallmatrix}3&1\\0&2^e\end{smallmatrix}\right)\) and
\(\left(\begin{smallmatrix}2^e&-1\\0&3\end{smallmatrix}\right)\).
Their maximum absolute row sums are at most \(2^{e+1}\) for \(e\ge1\). A path product has maximum row sum at most \(2^B\). Its positive denominator divides \(6^B\), since its powers of two and three have exponents individually at most \(B\). Hence \(6^B L_j(X)\) has integer coefficients, of absolute sum at most \(12^B\), uniformly for the entire family. Clearing \(P((L_j)_j)\) by \((6^B)^D\) bounds the resulting integer coefficient norm by \(M12^{BD}\) term by term, including monomials of degree less than \(D\). Applying the integer-root argument proves (2b). In particular even branching positive stencils of logarithmically bounded cost can exhibit only relations forced by their specified affine templates within this budget. Deep equal-clock central packets can cost much more than \(\log y\) on an escaping ray.

## A density-one assertion simultaneous in all window lengths

On any positive escaping orbit and for every function \(\omega(L)\to\infty\), there is a set of dates of ordinary asymptotic density one such that, with \(L_i=\log_2(a_i+1)\), the implication
\[
 \log_2 M+D[1+d(\omega(L_i)+r)]<\log_2 a_i,\qquad
 P(a_i,\ldots,a_{i+d})=0
 \quad\Longrightarrow\quad P(L_0,\ldots,L_d)\equiv0                    \tag{3}
\]
holds for **every** \(d,D,M,P\) at each date in the set. For example, this allows coefficient norm at most \(a_i^\eta\) for fixed \(0<\eta<1\), and degree times window length \(o(\log a_i/\omega(L_i))\).

Only a counting bound on the genuine division exponents is needed. Since \(2^{e_j}a_{j+1}=3a_j+1\le4a_j\), telescoping gives \(E_{0,n}\le2n+\log_2 a\). Set \(m_i=\sup_{d\ge1} E_{i,d}/d\). The upper ordinary density of \(m_i>R\) is at most \(4/R\) for \(R>5\). To see this on \(0\le i<N\), a witnessing \(d\ge N\) cannot occur once \(N>\log_2 a\), since \(E_{i,d}/d\le[2(i+d)+\log_2 a]/d\le5\). For each remaining bad starting index choose one witnessing half-open interval of length \(d<N\). Choose the leftmost bad index, retain its interval and discard all starting indices it covers. Repeat at the leftmost remaining bad index. The retained intervals are disjoint in \([0,2N)\) and cover all bad starting indices. The number of those indices is therefore at most the sum of retained lengths, at most \(E_{0,2N}/R\). Taking the upper limit proves the density bound. As \(a_i\to\infty\), the set where \(m_i>\omega(L_i)\) has upper density at most \(4/R\) for each fixed \(R>5\), hence density zero. Equation (1) applies at all other dates simultaneously in \(d\).

A large local valuation can produce an independent quadratic relation. For every \(e\ge1\), take \(y=2^e+3\) and \(x=(2^e y-1)/3\). Then \(x\) is a positive odd integer, \(U(x)=y\), and \(3x+1=y(y-3)\). The polynomial \(3X+1-Y(Y-3)\) is nonzero after the single affine substitution \(Y=(3X+1)/2^e\), so it is an independent relation at these unbounded pairs. The size of \(e\) is comparable to \(\log x\), as (1) requires.

The result makes the arithmetic requirement on an inverse concentration theorem explicit. If a positive limiting trace forced such independent relations on a positive proportion of times of its actual orbit, (3) would rule that out. The present transfer and the [positive stationary trace budget](../escape/POSITIVE_TRACE_BUDGET.md) have not produced that implication.
