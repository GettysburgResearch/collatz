# Strict integer curvature makes each short continued-fraction return fiber Sidon

**Proposed written theorem using the cited algebraic height input.** Let \(y_0,\ldots,y_{N-1}\) be integers of absolute value at most \(N^K\), and suppose their second differences are strictly positive throughout, or strictly negative throughout. Fix \(K,K',s\). For sufficiently large \(N\), every nonzero integer polynomial \(P\) with at most \(s\) nonzero coefficients of absolute value \(\le N^{K'}\), degree at most \(N/(\log N)^6\), and
\[
                    P(S)y_\ell=0\quad(0\le\ell<N-\deg P)
\]
is divisible by \((X-1)^3\), where \(S\) is the forward shift. In particular it cannot be a nontrivial difference of two unordered pairs of powers of \(X\). This conclusion only needs the stated one-sided sign of the second differences. No macroscopic variation of the normalized values is required.

**Native application.** Fix \(2<R<4\) and work along a sequence of chronological runs of \(T\) distinct positive ordinary odd Collatz states in \([M,RM]\), with \(M\to\infty\). Let \(h/b\) be a reduced convergent of \(\gamma=\log_23\) with next denominator \(b'\), and suppose \(b\to\infty,\ b\le T M^{-\epsilon},\ T\le b'\), for some fixed \(\epsilon>0\), and \(T=o(M)\). Let \(I\) be any integer time-offset interval in \([-T/100,T/100]\) of length at most \(T/(\log M)^8\). Fix a residue \(s_0\bmod b\) and integer lifts \(k_s=k_{s_0}+(s-s_0)h/b\) for \(s\equiv s_0\bmod b\) in \(I\). At an anchor between \(T/2\) and \(2T/3\), write \(V_t=2^{E_t}x_t\), with \(E_t\) cumulative native division. The labels
\[
                         2^{-k_s}V_{t+s},\qquad s\equiv s_0\bmod b,\ s\in I,    \tag{1}
\]
have distinct unordered pair sums, including doubled labels. Common nonzero scaling of all these labels is immaterial. This is an exact statement about one true return fiber on an open segment. Different fibers can still share pair differences.

## Eliminating torsion frequencies with a positive filter

Remove any initial monomial from \(P\), shrinking the tested interval by at most \(\deg P\). A monomial alone would give a long interval of zeros. Set \(w=\deg P\), \(D(X)=X^wP(1/X)\). On an interior sequence of length \(N_0\asymp N\) write the exact finite series identity
\[
          D(X)\sum_{\ell<N_0} y_{a+\ell}X^\ell=U(X)+X^{N_0}V(X),
                     \qquad \deg U,\deg V<w .
\]
Here \(D(0)\ne0\); both boundary polynomials are nonzero when the segment is chosen to have nonzero initial and final values. A strictly convex or concave sequence has at most two zero values, so this is possible. Put \(D_0=D/\gcd(D,U,V)\). The [sparse finite-height theorem, first two sections](SPARSE_RANK_RECURRENCES.md) applies verbatim to this identity: each effective root \(\alpha\) of \(D_0\) has \(\deg(\alpha)h(\alpha)\ll w\log N/(N_0-w)\ll(\log N)^{-5}\), including nonintegral roots and repeated factors. In detail, the orders of \(U,V\) at \(\alpha\) agree below its multiplicity in \(D\), and are \(e<s\) by sparsity. Then \(\alpha^{N_0}=-U^{(e)}(\alpha)/V^{(e)}(\alpha)\). These two polynomials have degree at most \(w\) and coefficient sums bounded by a power of \(N\); the projective height inequality gives the claimed bound. Voutier's lower estimate for nontorsion algebraic numbers contradicts it. Thus all roots of \(D_0\) are roots of unity. [Voutier, Acta Arith. 74 (1996), Corollary 2](https://arxiv.org/abs/1211.3110)

Let \(J\) be the support of \(D\), \(Q_s\) the product of primes at most \(s\). For each root of \(D_0\), Mann's theorem on an irredundant subsum associates two distinct \(i,j\in J\) for which the order of that root divides \(d_{ij}=Q_s|i-j|\). Every effective multiplicity is at most \(s-1\). [Mann, Mathematika 12 (1965)](https://doi.org/10.1112/S0025579300005210) · [Primary exposition and refinement by Zannier](https://seminariomatematico.polito.it/rendiconti/cartaceo/53-4/487.pdf)

Suppose \(P\) has root order at \(1\) at most two. So does \(D_0\). The polynomial
\[
 F(X)=(1-X)^2 H(X),\qquad
 H(X)=\prod_{\{i,j\}\subset J,\ i<j}
                    (1+X+\cdots+X^{d_{ij}-1})^{s-1}
\]
is divisible by \(D_0\) over \(\mathbb Q[X]\). Indeed each geometric sum vanishes at every nonidentity root of unity whose order divides its stride, and the separate square covers \(1\). Also \(\deg F=O_s(w)=o(N_0)\); coefficient sizes of \(H\) do not enter. Divide the finite series identity by \(\gcd(D,U,V)\) and multiply by \(F/D_0\). The resulting product \(F\sum y_{a+\ell}X^\ell\) has a zero coefficient at every index between \(w+\deg F+1\) and \(N_0-1\). But that coefficient is a nonempty positive-weighted sum of second differences of the original sequence, all of one strict sign: \(H\) has nonnegative coefficients and constant term one. This contradiction proves the theorem.

For \(P=X^i+X^j-X^u-X^v\), divisibility by \((X-1)^3\) would give \(i+j=u+v\) from the first derivative and \(i^2+j^2=u^2+v^2\) from the second and the first. The products are equal as well, forcing identical unordered exponent pairs. Repetitions are included.

## Native chronology supplies the interval of recurrence

Write \(s=s_*+\ell b\) with \(s_*\) the smallest member of the fiber in \(I\); the case of zero or one member is immediate. After a common scaling, (1) is the list of \((2^{-h}\operatorname{shift}^b)^\ell V_{t+s_*}\), for \(0\le\ell\le W\le T/[b(\log M)^8]\). A nontrivial equal-pair sum at the anchor would give a nonzero genuine four-term operator \(P(2^{-h}\operatorname{shift}^b)\) vanishing there.

On an interval of native base dates going back to \(T/4\), rescale by \(2^{-F_r}\) for \(F_r=\lfloor\log_2(V_r/L)\rfloor,\ L=M(1+R/4)\). The logarithmic shape of \(2^{-h\ell}V_{r+\ell b}/V_r\) is \(O(T|\gamma-h/b|+T/M)=o(1)\) for every offset used, and even for \(\ell b\) ranging over a fixed fraction of the run. This follows from \(T\le b'\), the continued fraction estimate and the sum of the true positive native log corrections; the bound is uniform in the base date. Since \(RM/2<L<2M\) with fixed margins, all corresponding multiplier tags \(2^{-F_r-h\ell+E_{r+\ell b}}\) lie in \(\{1,2\}\). Thus the signed comparison is an integer, and its forcing under the next native edge has absolute value at most two. A zero propagates backward, since \(3H+d=0,\ |d|\le2\) forces the integer \(H=0\). The window for this argument lies inside the actual segment after translating the anchor by \(s_*\). Consequently \(P(2^{-h}\operatorname{shift}^b)V\) vanishes on a native interval of length \(\gg T\).

Choose \(r_0\) in the interior of this zero interval and take \(N\asymp T/b\) successive sheet labels
\[
                   y_j=2^{-F_{r_0}-jh}V_{r_0+jb}.
\]
They are integers of size \(O_R(M)\) by the preceding binary chart, and \(P(S)y_j=0\) throughout a suitable interval of \(N-\deg P\) positions. Since \(N\ge cM^\epsilon\), their heights are polynomial in \(N\). The degree bound \(\deg P\le T/[b(\log M)^8]\le N/(\log N)^6\) holds for all large \(M\). The [native return-curvature theorem, (2)–(3)](NATIVE_RETURN_CURVATURE.md) applies to stride \(b\), since \(b/T\to0,\ \|b\gamma\|+b/M\to0\), and \(h\) is the nearest integer for large \(b\). It gives a common nonzero sign for all second differences of these \(y_j\)'s. The positive-filter theorem rules out the putative nontrivial pair comparison, proving (1). This argument takes entire consecutive vertical windows inside the run and uses neither arbitrary continuations nor a closed-cycle ordering.
