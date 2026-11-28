# Moving coefficients and the complete denominator of arbitrary arc covers

Let \(W_n\) be a sequence of primitive positive rational shortcut cycles with length \(h=h_n\to\infty\), \(p=p_n>0\) odd steps, \(D=2^h-3^p>0\), and reduced denominator \(q=q_n\). Fix an integer \(r\ge2\). For each \(n\), partition the circle into at most \(r\) nonempty **proper** arcs. Assume that each arc's own affine fixed point has absolute logarithmic Weil height \(o(h)\), uniformly over these finitely many positions. Then
\[
 \liminf \frac{\log_2 q}{h}\ge\frac1r.                                      \tag{1}
\]
Every subsequential limit is rational. Its reduced denominator divides \(\gcd(h,p)\) along a further subsequence. In particular the limit is one when \(\gcd(h,p)=1\) throughout. The result permits arbitrary interiors and very unequal lengths. The proof uses a moving-target theorem and has no effective onset.

More generally, on each arc one may prescribe a rational starting and ending reference value \(\xi_j,\eta_j\), of logarithmic heights \(o(h)\), satisfying the arc's affine law. Require \(\xi_j\ne x_j\), where \(x_j\) is the actual starting value of the full orbit at that cut. A proper arc's fixed center satisfies separation by the least period. This extension proves (1) for \(W_n=U_1^{m_1}\cdots U_r^{m_r}\) when the motifs may change with \(n\), \(\max_j|U_j|=o(h)\), and the displayed word has least period \(h\). Taking a rational additive or multiplicative factor of height \(o(h)\) changes the logarithm of a nonzero denominator by at most \(o(h)\) in the comparisons below.

## A separated signed-sum theorem

Write \(\operatorname{ht}\) for the absolute logarithmic height and fix \(s\ge1\). For each index let \(\kappa_j\ne0\) be rational numbers with \(\operatorname{ht}(\kappa_j)=o(h)\), let \(0\le i_j<h\) and \(0\le b_j=O(h)\), and put
\[
 C=\sum_{j=1}^s \kappa_j2^{i_j}3^{b_j}.
\]
Assume the circular distances between distinct \(i_j/h\) are bounded below by a positive constant independent of the index. For \(s=1\) this assumption is empty. The denominator of \(C/D\) satisfies (1) with \(r=s\), along with the rationality and clock-divisibility conclusions. The denominator is understood in lowest terms. In particular, the theorem rules out infinitely many exact zero sums under these hypotheses.

Clear the denominators of the \(\kappa_j\) simultaneously, multiplying by a positive integer of logarithm \(o(h)\). This changes the denominator's logarithm by \(o(h)\). Hence take all coefficients integral. Let \(S=\{\infty,2,3\}\), and set \(X=2^h3^{-p}\), \(Y_j=2^{i_j}3^{b_j}\). Every coordinate is a positive \(S\)-unit of height \(O(h)\), and \(\operatorname{ht}(X)=h\log 2\). The standard two-logarithm estimate gives \(\log D=h\log2+o(h)\). See [Lagarias, Lemma 2.2](https://arxiv.org/abs/math/0512006).

Start with any subsequence on which the normalized logarithm of the denominator converges. Pass to a further subsequence on which all \(v_2/h\) and \(v_3/h\) of the original coordinates have limits. Let \(L\subseteq\mathbb Z^{s+1}\) be the integer kernel of the two limiting linear forms. This is a saturated subgroup. A character in \(L\), evaluated on the tuple, has height \(o(h)\). A character outside \(L\) has height bounded below by a positive multiple of \(h\), even on any further subsequence. The quotient lattice is free. In a basis of it, \([X]=d[T]\) for a positive integer \(d\), with \(T\) primitive. Lift a basis to integral characters of the original tuple and call the remaining coordinates \(Z\). Exact evaluation gives
\[
   X=c_nT_n^d,\qquad
   Y_j=c'_{j,n}T_n^{m_j}Z_n^{u_j}.
\]
All \(c_n,c'_{j,n}\) are positive rational \(S\)-units of height \(o(h)\). The exponents are now fixed integers or fixed integer vectors. Every nontrivial fixed character of \((T_n,Z_n)\) has height \(\gg h\). Moreover \(\operatorname{ht}(T_n)=h\log2/d+o(h)\) and the heights of the remaining coordinates are \(O(h)\).

Form the moving Laurent polynomials \(F_n=c_nT^d-1\) and \(G_n=\sum_j \kappa_j c'_{j,n}T^{m_j} Z^{u_j}\). Two distinct atoms cannot have both \(u_j=u_k\) and \(m_j\equiv m_k\pmod d\). Otherwise \(Y_j/(Y_kX^{(m_j-m_k)/d})\) has height \(o(h)\), so \(i_j-i_k-(m_j-m_k)h/d=o(h)\), contrary to circular separation. Thus every occupied pair of a \(Z\)-character and a residue modulo \(d\) has exactly one nonzero coefficient. No sign assumption on the \(\kappa_j\) is needed.

Let \(R_n\) be the monic rational common divisor of \(F_n\) and all coefficients of \(G_n\) as a Laurent polynomial in \(Z\), taking the full gcd in \(\mathbb Q[T,T^{-1}]\). It divides \(F_n\) as an ordinary polynomial, and \(F_n\) has distinct nonzero roots. Pass to a further subsequence keeping \(M=\deg R_n\) fixed. Set \(J=d-M\). Every root of \(F_n\) has algebraic height \(\operatorname{ht}(c_n)/d=o(h)\). Elementary symmetric polynomials in at most \(d\) such roots show each coefficient of \(R_n\) has height \(o(h)\). Polynomial division of bounded degree by a monic polynomial makes all coefficients of \(F_n/R_n,G_n/R_n\) have height \(o(h)\) as well. Outside \(S\), the roots are units at every place above the base prime, hence \(R_n\) is integral. Monic division, after clearing fixed Laurent powers in \(G_n\), shows both residual polynomials are integral outside \(S\).

### Removing the residual gcd

Multiply the residuals by fixed Laurent monomials if needed to obtain ordinary polynomials. Only \(G_n/R_n\) needs this potentially, since \(F_n/R_n\) is already a univariate polynomial with nonzero constant. No new common factor is introduced. They are coprime by the definition of \(R_n\). Their total degrees and finite supports may be kept constant on a further subsequence. In the case of positive degrees apply Grieve and Wang, Theorem 3.1, over \(\mathbb Q\), at the \(S\)-unit tuple \((T_n,Z_n)\). Projective coefficient heights are \(o(h)\), and the maximum coordinate height is comparable to \(h\). Their theorem gives for each \(\epsilon>0\) either an infinite subset with outside-\(S\) logarithmic gcd \(<\epsilon\max\operatorname{ht}(T_n,Z_n)\), or containment in finitely many proper algebraic subgroups up to a slowly moving translation. In their proof the latter yields a fixed nonzero character of height \(o(h)\) on an infinite subset, contradicting the limiting-valuation construction. This invocation applies to **each hypothetical subsequence on which the residual gcd is \(\gg h\)**. It therefore gives an \(o(h)\) residual gcd for the retained sequence. If a residual is a nonzero constant, its outside-\(S\) positive valuations already sum to \(o(h)\). The same bound applies to a Laurent monomial of slow coefficient evaluated at units. [Grieve and Wang, arXiv version 2, Theorem 3.1 and (3.35)–(3.36)](https://arxiv.org/abs/1902.09109) · [Published version](https://doi.org/10.1090/tran/8220)

For each \(n\), let \(\lambda\) be any root of \(F_n\), and let \(\zeta\) be a primitive \(d\)-th root of unity. For an occupied \(Z\)-character look at the polynomial coefficient of that character evaluated at \(\lambda\zeta^a\), \(a\in\mathbb Z/d\mathbb Z\). It is a sum of powers \((\zeta^{m_j})^a\) with at most \(s\) distinct bases and with nonzero coefficients \(\kappa_jc'_{j,n}\lambda^{m_j}\). Consecutive values of length equal to the number of bases cannot all vanish, by the Vandermonde determinant. Counting cyclic windows shows at least \(d/s\) roots have this coefficient nonzero. These roots are absent from \(R_n\), so \(J/d\ge1/s\). [Finite exponential-sum lemma in Lean](FourierSupport.lean)

The outside-\(S\) positive valuations of \(R_n(T_n)\) and \((F_n/R_n)(T_n)\), weighted by \(\log\ell\), sum to \(\log D\), as \(F_n(T_n)=D/3^p\) and \(D\) is coprime to six. Their individual sums are at most \(M\operatorname{ht}(T_n)+o(h)\) and \(J\operatorname{ht}(T_n)+o(h)\) by the usual polynomial height bound. The upper bounds sum to \(h\log2+o(h)\), so each is attained up to \(o(h)\). Using the residual gcd estimate, \(\log\gcd(D,C)=M h\log2/d+o(h)\), and
\[
 \log_2\operatorname{den}(C/D)/h \ \longrightarrow\ J/d.
\]
For each \(n\), every root of \(F_n\) has \(v_\ell=-v_\ell(c_n)/d\), for \(\ell=2,3\), at a fixed algebraic extension of that valuation. The monic rational factor associated with \(F_n/R_n\) has nonzero rational constant, so \(d\mid Jv_\ell(c_n)\). From \(X_n=c_nT_n^d\) this implies \(d\mid Jh\) and \(d\mid Jp\). This completes the sparse theorem and its subsequence qualifications.

## Applying the sparse theorem across unequal arcs

After passing to a subsequence, the displayed number of arcs is fixed and each length fraction has a limit. Keep the arcs of positive limiting fraction, at least one, and append to each surviving arc all immediately following arcs of zero limiting fraction as a connector. Their total length is \(o(h)\). Extend each surviving reference through its connector by the prescribed affine maps. The extended terminal height remains \(o(h)\), since either shortcut affine map increases absolute logarithmic height by at most a constant. The starting reference and its separation from the true value are preserved. Write \(\xi_j,\eta_j\) for the resulting endpoint references, \(i_j\) for the time at the surviving arc start, \(b_j\) for the number of ones before it, and \(\kappa_j=\eta_{j-1}-\xi_j\) cyclically. Distinct \(i_j/h\) are now separated on the circle. The single surviving arc case needs no separation.

For the augmented arc affine law, \(x_{j+1}-\xi_{j+1}=3^{P_j}2^{-L_j}(x_j-\xi_j)+\kappa_{j+1}\). Unroll from cut zero around the entire circle. The identity with wrap is
\[
 D(x_1-\eta_r)=\sum_j\kappa_j 2^{i_j}3^{p-b_j}.
\]
If all \(\kappa_j=0\), the homogeneous recurrence and \(\rho<1\) give \(x_1=\xi_1\), contradicting separation. Keep a subsequence fixing the nonempty support of size \(s\le r\). The \(\kappa_j\) have height \(o(h)\), so the sparse theorem applies. Adding the reference \(\eta_r\) of height \(o(h)\) changes the logarithm of the denominator by \(o(h)\). Thus the computed limit also holds for the full orbit denominator.

The specialized two-motif formula in [POWERED_LANGUAGES.md](POWERED_LANGUAGES.md) gives an exact binomial calculation and distinguishes equal from unequal slopes. The [elementary estimate](ARC_HEIGHT.md) is effective and uniform as \(r\) grows. The moving-target theorem has fixed dimension and gives no such uniformity. Positive integer cycles with unbounded arc-cover complexity and large necessary reference heights remain unresolved.
