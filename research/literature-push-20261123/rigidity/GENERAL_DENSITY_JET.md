# The second arithmetic germ at every limiting density

23 November 2026. Authors: root, with the small-hole estimate independently
derived by source_construction.

**Status: PROPOSED written strengthening of the two-center consumer.
The arithmetic germ remains an unproved hypothesis. No full Collatz proof.**

This addendum leaves the frozen critical-density theorem in
[SCALAR_BOUNDARY_AND_SECOND_CENTER.md](SCALAR_BOUNDARY_AND_SECOND_CENTER.md)
unchanged. It proves that its explicit Jet hypothesis J forces eventual
periodicity whenever the actual parity density has a limit, including
densities above the critical value. The additional step is an elementary
bound for the loss of Green capacity after removing a small disc.

## 1. Statement and retained arithmetic input

Keep one positive ordinary source, its actual weighted parity series
\(B_n\), and the literal binary Taylor series \(J_n(t)=B_n(2+t)\).
Assume the actual density \(p_k/k\) converges to \(\rho\). Set

\[
R=3^\rho,\qquad 1\le R\le3.
\]

Its exact complex and ternary radii are \(R\) and \(1/R\).
Keep **all** of Jet hypothesis J: the coefficients of \(J_n\) are
rational, lie in one ring \(\mathbb Z[1/M]\), and have positive
convergence radius at infinity and every prime dividing \(M\).
The binary germ must be the actual translated germ, including every
coefficient, not just its known constant value \(-n\).

**Theorem.** Under these hypotheses, \(B_n\) is rational and the actual
ordinary orbit is eventually periodic. Conversely, eventual periodicity
implies J. Thus, on the class of positive ordinary sources whose parity
density has a limit, J is equivalent to eventual periodicity.

This does not prove J, the existence of a limiting density for every
source, or the exclusion of a different positive integer cycle.

## 2. The shared finite-place construction

Use centers zero and two on \(\mathbb P^1_{\mathbb Q}\). At the binary
place the single unit disc contains both centers and the original series
realizes both germs. Its diagonal Green constants are zero and its
off-diagonal constant is

\[
L=-\log|2|_2=\log2.
\]

At three choose a radius \(r_3<1/R\) at zero and a fixed small disc at
two. They are disjoint. At every other finite prime use unit discs,
except for the finitely many smaller second-center discs needed by J.
All these remaining pairs of discs are disjoint. The total
second-center finite-place diagonal cost is a finite constant \(C\),
independent of the small complex radius \(\varepsilon\).

The formal integral model outside the primes dividing \(6M\), and
the local meromorphic realizations, are exactly those required in
Chambert-Loir--Noûs, *Potentiel et rationalité*, arXiv:2305.17210v2,
Sections 4.1--4.3:
<https://arxiv.org/pdf/2305.17210>.

Only the complex domain needs a new construction. Once it is specified,
the global potential matrix is

\[
\mathcal G_\varepsilon=
\begin{pmatrix}
a_\varepsilon &L\\
L&b_\varepsilon
\end{pmatrix},
\qquad b_\varepsilon=\log\varepsilon+C.
\tag{1}
\]

For \(a_\varepsilon,b_\varepsilon<0\), the condition
\(a_\varepsilon b_\varepsilon<L^2\) gives positive game value:
the first-row weight
\((L-b_\varepsilon)/(2L-a_\varepsilon-b_\varepsilon)\)
has guaranteed payoff
\((L^2-a_\varepsilon b_\varepsilon)/
 (2L-a_\varepsilon-b_\varepsilon)>0\).
The cited Theorem 4.3 then makes both germs expansions of one rational
function.

## 3. Densities at or below the critical value

If \(R<2\), take the disjoint complex discs
\(D(0,R e^{-\varepsilon})\) and \(D(2,\varepsilon)\).
They are disjoint for sufficiently small positive \(\varepsilon\);
J realizes the second one. Choose a ternary radius in its value-group
closure satisfying

\[
R^{-1}e^{-2\varepsilon}<r_3<R^{-1}e^{-\varepsilon},
\qquad r_3\in3^{\mathbb Q}.
\]

Then \(-3\varepsilon<a_\varepsilon<-2\varepsilon\), while
\(b_\varepsilon=\log\varepsilon+C\). Their product tends to zero.
The positive-game criterion applies.

If \(R=2\), use \(D(0,2-2\varepsilon)\) and \(D(2,\varepsilon)\),
as in the frozen critical theorem. Again
\(a_\varepsilon=-O(\varepsilon)\) and
\(a_\varepsilon b_\varepsilon\to0\).
This includes the critical density \(\rho=\log_3 2\).

## 4. A hole around the second center when \(R>2\)

Here the original complex disc already contains two. Its actual complex
value there need not agree with the binary value \(-n\). To realize the
two full germs on disjoint components, put

\[
R_\varepsilon=R e^{-\varepsilon},\qquad h=2\varepsilon,
\]
\[
\Omega_{0,\varepsilon}
=D(0,R_\varepsilon)\setminus\overline{D(2,h)},\qquad
\Omega_{2,\varepsilon}=D(2,\varepsilon).
\tag{2}
\]

For sufficiently small \(\varepsilon\), the closed hole lies strictly
inside the larger disc and avoids zero. The original \(B_n\) realizes
the first component, and J realizes the second. These components are
disjoint, so the complex off-diagonal Green value is zero.

Let \(\delta_\varepsilon\) be the decrease in the Green constant at zero
caused by the hole. The unpunctured constant is
\(\log R_\varepsilon\). Domain monotonicity gives
\(\delta_\varepsilon\ge0\).

Here is a direct quantitative bound. For a disc of radius \(S>2+h\),
the Green functions are

\[
g_S(z,0)=\log\frac{S}{|z|},
\qquad
g_S(z,2)=\log\left|
\frac{S^2-2z}{S(z-2)}
\right|.
\tag{3}
\]

On the hole boundary \(|z-2|=h\),

\[
g_S(z,0)\le M_h:=\log\frac{S}{2-h},
\]
\[
g_S(z,2)\ge m_h:=
\log\frac{S^2-4-2h}{S h}.
\tag{4}
\]

Choose the parameters small enough that \(m_h>0\).
Let \(H\) be the harmonic function on the punctured domain equal to one
on the hole boundary and zero on the outer circle. The difference
between its unpunctured and punctured Green functions at zero extends
harmonically through zero. Its outer boundary value is zero and its
inner boundary value is \(g_S(z,0)\). The maximum principle therefore
bounds this difference by \(M_hH\).

The function \(g_S(z,2)/m_h\) is harmonic throughout the punctured
domain, vanishes on the outer boundary, and is at least one on the
inner boundary. A second maximum-principle comparison gives

\[
0\le\delta_\varepsilon
\le
\frac{M_h\,g_S(0,2)}{m_h}
=
\frac{\log(S/(2-h))\log(S/2)}
{\log((S^2-4-2h)/(Sh))},
\qquad S=R_\varepsilon,\ h=2\varepsilon.
\tag{5}
\]

No asymptotic capacity theorem is assumed in (5).
As \(\varepsilon\downarrow0\), both numerator factors tend to
\(\log(R/2)\), and the denominator is
\(|\log\varepsilon|+O_R(1)\). Consequently

\[
\limsup_{\varepsilon\downarrow0}
\delta_\varepsilon|\log\varepsilon|
\le\bigl(\log(R/2)\bigr)^2.
\tag{6}
\]

Choose \(r_3\) in the same interval as in Section 3. The first global
diagonal is now

\[
a_\varepsilon
=\log R_\varepsilon+\log r_3-\delta_\varepsilon
=-\delta_\varepsilon-O(\varepsilon),
\tag{7}
\]

where the nonnegative \(O(\varepsilon)\) term lies between
\(2\varepsilon\) and \(3\varepsilon\). Since the second diagonal is
\(\log\varepsilon+C\), equations (6)--(7) imply

\[
\limsup_{\varepsilon\downarrow0}
a_\varepsilon b_\varepsilon
\le\bigl(\log(R/2)\bigr)^2
\le(\log(3/2))^2
<(\log2)^2=L^2.
\tag{8}
\]

Thus some sufficiently small choice has strictly positive game value.
All the arithmetic and local-realization hypotheses remain explicit,
so Theorem 4.3 applies. This proves rationality also when \(R>2\).

## 5. Conclusion and exact remaining boundary

The credited rational-series consumer then gives eventual ordinary
periodicity, retaining the complete repeated-block denominator. This
finishes the forward implication in the theorem.

For the converse, an eventually periodic orbit has rational \(B_n\).
Its rational function is regular at two, because the actual binary
series is analytic there. Its Taylor coefficients at two are rational,
belong to one ring \(\mathbb Z[1/M]\), and converge in a sufficiently
small disc at every place. Hence they satisfy J.

The strict positive margin in (8) is a new deduction from the explicit
small-hole comparison and the primary multipoint theorem. It is a
consumer for a complete arithmetic germ. It does not construct that germ.
Even rationality of the first unknown derivative \(B_n'(2)\) has not
been established for an arbitrary positive source, and finite
interpolation values do not replace J.

This is written potential theory, not a new Lean formalization.
The Lean modules in this checkpoint address the separate complete-gcd
arithmetic, not these Green functions or the multipoint theorem.
