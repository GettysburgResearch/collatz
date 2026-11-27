# Finite atomic measures for the critical inverse operator

On \(V=\mathbb Z_3^\times\), put \(\phi_e(x)=(3x+1)/2^e\), \(\psi_e(y)=(2^e y-1)/3\), and \(\alpha_e=3/2^e\) for \(e\ge1\). Define the bounded operator on continuous functions
\[
 Lf(y)=\sum_{e:\ \psi_e(y)\in V}\alpha_e^2 f(\psi_e(y)).
\]
Haar measure restricted to \(V\) satisfies \(L^*m=m\). Indeed each \(\phi_e\) is ternary-contracting with Haar Jacobian \(1/3\), and \(\sum_e\alpha_e^2/3=1\).

An actual escaping component would provide another finite measure,
\[
       \mu_C=\sum_{x\in C,\ 3\nmid x}P(x)^{-2}\delta_x .
\]
Here \(P(Ux)=\alpha_{e(x)}P(x)\) and \(P(x)\ge x\) on the positive odd component. Its finiteness follows from \(\sum x^{-2}<\infty\). The true positive odd parents of any positive odd \(y\) are exactly its positive integral \(\psi_e(y)\). For a source \(x\), only \(e(x)\) gives an odd integral \(\phi_e(x)\). These facts prove \(L^*\mu_C=\mu_C\). The squared-source weight already occurs in [the earlier tilted component trace](../../astra-unconventional-20261126/boundary/TILTED_TRACE.md).

**Theorem.** There are uncountably many mutually singular finite, nonzero, purely atomic measures satisfying \(L^*\mu=\mu\), concentrated on countable sets of ternary irrational points. Their sets of atoms admit a compatible strictly positive real realization and an odd binary realization. Each finite subdiagram is realizable by genuine positive odd integers. The real, binary and ternary seeds in the infinite construction are selected separately.

## An integrable bound for generic inverse trees

Read a word backwards from its root and write \(A_w=\prod_{e\in w}\alpha_e\). For the estimates allow the terminal point to be any ternary integer. Each specified word of length \(k\) is legal on precisely one residue class modulo \(3^k\), including when the terminal vertex is a multiple of three. For the following expectations use probability Haar measure on all of \(\mathbb Z_3\). Fix \(t=3/2\). Then
\[
 \mathbb E_z\sum_{\lvert w\rvert=k,\ w\ {\rm legal\ at}\ z} A_w^t
       =\lambda_t^k,\qquad
 \lambda_t=\frac{3^{t-1}}{2^t-1}<1.                                     \tag{1}
\]
In particular \(G(z)=\sum_w A_w^2\), including the empty word, satisfies \(\mathbb E G^{t/2}<\infty\) by subadditivity at exponent \(t/2\). Also
\[
       R_*(z)=\sup_{w}\frac13\sum_{\ell=1}^{|w|} A_{w| \ell}
            \quad\hbox{satisfies}\quad
       \|R_*\|_{L^t}\le\frac13\sum_{k\ge1}\lambda_t^{k/t}<\infty.         \tag{2}
\]
Bound the supremum by the sum of the levelwise maximal gains and apply Minkowski and (1).

## Uniform control off the prescribed path

Set \(y_j=\phi_1^j(z)=-1+(3/2)^j(z+1)\). For \(j\ge1\) permit only words whose first inverse letter differs from one, and call these fresh. Through length \(j\) their legal words with ternary-integral terminal points are precisely the fresh words at the negative ordinary fixed point \(-1\). These are actual first-hit signed paths. If the signed terminal is \(-s\), their gain satisfies \(A_w\le C/s\), and the reciprocal sum of the different signed magnitudes along each path is uniformly bounded. This follows from the cited signed first-hit bound, which uses only compression and the affine identity. Each \(s\) occurs at most once across all fresh words and all lengths, by determinism of its first hit. Consequently their total \(t\)-power weight over **all** lengths is at most \(C^t\sum_s s^{-t}<\infty\). Their cumulative path offsets \(\sum_{\ell} A_{w|\ell}/3\) are uniformly bounded as well. [Signed first-visit bound and proof](https://github.com/GettysburgResearch/collatz/blob/1f0f496fbea37792439feada6106eaaff596bcd1/research/ayh-resource-reset-20261124/unconventional/FRESH_ASCENT_BARRIER.md)

For each such length-\(j\) prefix \(u\), its terminal ternary coordinate from \(y_j\) is a Haar-preserving affine function of \(z\). Indeed the coefficient of \(z\) equals \(2^{E_u-j}\), a ternary unit, and the constant term is ternary integral. Thus the expected sum of \(t\)-power gains of all its longer extensions, divided by \(A_u^t\), is bounded by \(\sum_{k\ge0}\lambda_t^k\). Summing over \(u\) and adjoining shorter words shows that the fresh total squared gain \(G_j\) satisfies \(\sup_{j\ge1}\mathbb E G_j^{t/2}<\infty\).

Likewise the largest fresh offset \(R_j\) satisfies \(\sup_{j\ge1}\mathbb E R_j^t<\infty\). Before depth \(j\) use the deterministic signed reciprocal bound. The residual is at most \(\sup_{u} A_u R_*(\psi_u(y_j))\); its \(t\)-th moment is bounded by the sum over all length-\(j\) fresh prefixes of \(A_u^t\|R_*\|_t^t\). A nonunit terminal can be included in the bound. At \(j=0\) use the entire tree and the estimates (1)–(2). All estimates remain finite on restricting \(z\) to units. Hence for almost every unit \(z\),
\[
 \sum_{j\ge0}(2/3)^{2j}(1+G_j)<\infty,\qquad
 \sup_{j\ge0}(2/3)^j R_j<\infty.                                      \tag{3}
\]
For the first assertion sum the expectations of \((2/3)^{tj}(1+G_j)^{t/2}\) and use that summability in exponent \(t/2<1\) implies summability. For the second, sum the \(t\)-th moments of the weighted offsets.

## The countable atom set and its three coordinates

Choose one of the ternary irrational units \(z\) satisfying (3). Use the vertices \(y_j\), the full unit-ended inverse trees at \(y_0\), and the fresh unit-ended inverse trees at \(y_j\) for \(j\ge1\). Every vertex is \(g(z)\) for a rational affine function \(g\) of positive slope. Equality of two such values implies equality of their affine functions, by irrationality. Their binary evaluations \(g(-1)\) are units: the spine evaluates to \(-1\) and inverse steps preserve binary units. If \(\phi_e(g(z))\) lies in the constructed atom set, the affine functions must agree, so \(\phi_e(g(-1))\) is a binary unit. This determines \(e\) uniquely, and the indicated forward edge already attains it. The union includes all legal unit-ended parents of every vertex. In particular the omitted first inverse edge at \(y_j\) leads to \(y_{j-1}\).

Give the vertex \(g(z)\) mass \(g'^{-2}\), using its positive rational slope in the usual real norm. On the spine this is \((2/3)^{2j}\); on attachment through \(w\) it is \((2/3)^{2j}A_w^2\). The first assertion of (3) bounds the total mass, including if one uses the sum over word descriptions as an upper bound. Every inverse child receives exactly \(\alpha_e^2\) times its parent's mass. The unique forward edge and closure under parents prove \(L^*\mu=\mu\) by summing on this countable set. Every orbit under rational affine functions is countable. Selecting \(z\)'s in distinct such orbits gives uncountably many disjoint sets of atoms. No assertion of disjoint closed topological supports is needed.

For a real seed \(b>0\), the spine has value \(-1+(3/2)^j(b+1)\) and its inverse endpoint through \(w\) has value
\[
       g(b)=\frac{-1+(3/2)^j(b+1)-R_w}{A_w},
       \qquad R_w=\frac13\sum_{\ell=1}^{|w|}A_{w|\ell}.
\]
The second assertion of (3) allows one \(b\) so large that every spine value exceeds twice the largest corresponding offset. Then every nonempty endpoint is at least \(1/3\), since \(R_w\ge A_w/3\). Finally any finite list of these affine maps has bounded powers of two and three in its denominators. Choose a positive ordinary seed \(n\) sufficiently close to \(-1\) at two and to \(z\) at three. The Chinese remainder theorem permits arbitrarily large such \(n\). All selected rational \(g(n)\) are then odd ternary-unit integers, and their positive slopes make them positive for large \(n\). The displayed edges have their full binary valuations. By increasing \(n\) one may avoid any of the finitely many accidental intersections of distinct affine maps.

These examples prevent uniqueness of finite atomic conformal measures, even with positive real branches and ordinary realizations at every finite stage. They retain a single ternary atom set but do not supply an infinite orbit of one positive ordinary integer. Exclusion of atoms supported at such ordinary integers would still be required for the escape argument.

## The ordinary Hardy series and the missing independent bases

On an actual escaping component include all its odd positive vertices, also the nonunit leaves, and set \(m_x=P(x)^{-2}\) there and zero at every other integer. The ordinary series \(M(z)=\sum_{x\ge1}m_xz^x\) has absolutely summable coefficients, so is holomorphic for \(|z|<1\) and continuous on the closed disk. Write \(M_r(z)=\sum_{x\equiv r\ (3)}m_xz^x\). The ordinary parent substitution and \(m_x=\alpha_e^2m_{Ux}\) give
\[
 zM(z^3)=9\sum_{e\ge1}4^{-e}M_{(-1)^e\bmod3}(z^{2^e}),\qquad
 16zM(z^3)-z^4M(z^{12})=36M_2(z^2)+9M_1(z^4).                       \tag{4}
\]
The second formula subtracts the tail starting at \(e=3\). Extending \(P(2^j x)=2^jP(x)\) to the even heights gives the coefficient rules \(m_{2n}=m_n/4\) and \(m_{3n+2}=4m_{2n+1}/9\) for this full-integer extension. They specify one binary section and relate one ternary section to the other binary section. Equation (4) is mixed. No pair of independent scalar Mahler equations for the ordinary series follows from these calculations.

There is a direct test of the affine rules in the countable model. Permit the nonunit ternary leaves there as well. They have no inverse children and all the summability and real-positivity estimates above already include them. Use the triples \((g(b),g(-1),g(z))\) for its atoms, with \(b\) the fixed real seed. Assign mass zero to other triples. A point outside this atom set cannot acquire a legal edge into it without being one of the included inverse children. Thus the model retains the branch rule on positive real, odd binary, ternary-integral coordinates. Every atom reached from the \(r\)-th spine point by \(k\) inverse letters of total exponent \(E\) has slope \(g'=2^{E-r}3^{r-k}\). In particular
\[
                  v_2(g')+v_3(g')=E-k\ge0.
\]
Slope one requires \(E=k=r\), so all letters are one and the affine function is the identity.

For \(b_0=2\) or \(3\), a polynomial combination \(\sum_j p_j(Z)M(Z^{b_0^j})\) has coefficient rule \(\sum_{j,t}[Z^t]p_j\,m_{(N-t)/b_0^j}\), omitting nonintegral and unsupported indices. Take the least \(j_0\) with \(p_{j_0}\ne0\) and any \(t_0\) with \([Z^{t_0}]p_{j_0}\ne0\). Test that same rule in the joint model at the affine index \(N=b_0^{j_0}X+t_0\), evaluating \(X\) at the three seeds. Every term with \(j>j_0\) has slope \(b_0^{j_0-j}\), whose two valuation sum is negative. At \(j=j_0\) only \(t=t_0\) has the identity affine function. Irrationality of the ternary seed distinguishes the functions, and the seed atom has mass one. The tested coefficient is therefore nonzero. This excludes any nontrivial pure-base coefficient rule of this form as a consequence of branch compatibilities valid also for the joint model. The probe index is an adelic triple. The test neither constructs an ordinary Hardy solution nor excludes a Mahler identity proved using additional ordinary arithmetic or complex analysis.
