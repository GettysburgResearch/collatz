# The distinguished cycle fiber through Hankel determinants

Date: 2026-11-23. **Status: exact identities for unrestricted words;
the proposed minimum-height inequality remains OPEN.** This continuation
tests whether the residual recurrence degree can force a large *minimum*
in an integer cycle. It derives the full-rank and bordered determinants,
an exact control where all shifted full-rank determinants are integral
but the cycle is not, and the cost of a natural arithmetic normalization.
None of these identities excludes an unrestricted positive integer cycle.

## 1. The target and the actual integer sequence

The companion `SUPERPOLYNOMIAL_RESIDUAL_DENOMINATOR.md` establishes
\(n/\log p\to\infty\) for primitive words, where \(n\) is the
residual degree defined below. For an actual integer cycle, the inherited
two-logarithm bound gives \(\log m=O(\log p)\) for its minimum \(m\).
A uniform estimate

\[
 \boxed{\log m\ge c n\quad(c>0)}
 \tag{H1 — OPEN}
\]

would therefore exclude all sufficiently large primitive integer cycles.
Effective constants and exclusion of the remaining finite range would
still be needed for a complete cycle theorem. This note does not prove
(H1), or even a replacement growing faster than \(\log p\).

Let \(a_0,\ldots,a_{p-1}\ge1\) be an odd-gap word, and put

\[
 A=\sum_i a_i,\qquad D=2^A-3^p>0,\qquad
 s_0=0,\quad s_j=\sum_{i<j}a_i,\quad s_{j+p}=s_j+A.
\]

Its positive rational odd cycle satisfies
\(2^{a_j}x_{j+1}=3x_j+1\), with \(x_{j+p}=x_j\).
Set \(m_0=x_0\), and extend

\[
 u_j=2^{s_j},\qquad v_j=2^{s_j}x_j.
\]

Then

\[
 v_{j+1}-3v_j=u_j,\qquad
 u_{j+p}=2^A u_j,\qquad v_{j+p}=2^A v_j.                 \tag{H2}
\]

For an integer cycle rotated to its minimum, \(m_0=m\), every \(x_j\)
is an odd positive integer and \(u_j,v_j\) are integers. The recurrence
retains this actual ordinary realization; no local periodic surrogate
is substituted for it.

Define the complete polynomials

\[
 F(X)=X^p-2^A,\qquad
 Q(X)=\sum_{i=0}^{p-1}2^{s_i}X^{p-1-i},\qquad
 G=\gcd(F,Q),\quad F_0=F/G,\quad Q_0=Q/G,
\]

where \(G\) is monic, and \(n=\deg F_0\). These are integer
polynomials; \(F_0\) is monic and squarefree,
\(\deg Q_0=n-1\), and \(\gcd(F_0,Q_0)=1\). The closing value is

\[
 m_0=-\frac{Q_0(3)}{F_0(3)},\qquad
 J(X)=\frac{Q_0(X)+m_0F_0(X)}{X-3}.                    \tag{H3}
\]

Here \(F_0(3)\ne0\), and \(J\in\mathbb Q[X]\) has degree
\(n-1\). If \(m_0\) is an integer, then \(J\in\mathbb Z[X]\).
At each root \(\lambda\) of \(F_0\),
\(J(\lambda)=Q_0(\lambda)/(\lambda-3)\ne0\).

The two generating functions are consequently

\[
 \mathcal U(z)=\frac{Q_0(1/z)}{zF_0(1/z)},\qquad
 \mathcal V(z)=\frac{m_0+z\mathcal U(z)}{1-3z}
             =\frac{J(1/z)}{zF_0(1/z)}.                \tag{H4}
\]

Both sequences have recurrence degree **exactly** \(n\). Integrality
of the cycle has not made its residual complexity disappear.

## 2. Full-rank Hankel determinants recover precisely the norm

Write

\[
 \Delta_k(w;\ell)=\det(w_{\ell+i+j})_{0\le i,j<k},\quad
 \epsilon_n=(-1)^{n(n-1)/2},\quad
 \rho=(-1)^nF_0(0).
\]

The exact identities are

\[
 \boxed{\Delta_n(u;0)=\epsilon_n\operatorname{Res}(F_0,Q_0),}
                                                               \tag{H5}
\]

\[
 \boxed{\Delta_n(u;\ell)=(-1)^nF_0(3)\Delta_n(v;\ell),}
                                                               \tag{H6}
\]

\[
 \boxed{\Delta_n(v;\ell)=\rho^\ell\Delta_n(v;0)\ne0.} \tag{H7}
\]

**Proof.** For the distinct roots \(\lambda_1,\ldots,\lambda_n\)
of \(F_0\), partial fractions in (H4) give

\[
 u_j=\sum_{\nu=1}^n
       \frac{Q_0(\lambda_\nu)}{F_0'(\lambda_\nu)}\lambda_\nu^j,
 \qquad
 v_j=\sum_{\nu=1}^n
       \frac{J(\lambda_\nu)}{F_0'(\lambda_\nu)}\lambda_\nu^j.
\]

A full-rank Hankel determinant is the product of these nonzero weights,
the squared Vandermonde determinant, and
\((\prod_\nu\lambda_\nu)^\ell\). Now

\[
 \prod_\nu F_0'(\lambda_\nu)
   =\epsilon_n\prod_{\mu<\nu}(\lambda_\nu-\lambda_\mu)^2,
 \qquad
 \prod_\nu\frac{Q_0(\lambda_\nu)}{J(\lambda_\nu)}
   =\prod_\nu(\lambda_\nu-3)=(-1)^nF_0(3),
\]

which prove all three formulas. Also \(F_0(0)\) divides \(F(0)=-2^A\)
in the integers, so \(\rho\) is a signed power of two. Thus shifting
these determinants supplies no additional odd-prime information.

In an integer cycle, (H6) implies
\(|F_0(3)|\mid\Delta_n(u;0)\). By (H5), this is exactly the
previous resultant divisibility condition. It does not distinguish the
evaluation \(X=3\) from other conjugates above the same rational prime.

## 3. All shifted full-rank determinants can be integral at wrong conjugates

The control word is credited to PR185,
`39ba48e6a8af781193e28c679ea8ab64663c3aa6`,
`research/rigidity-closing-20261122/CYCLOTOMIC_ZERO_FIBER.md`, Section 9:

\[
 A=13,\quad p=8,\quad
 (s_0,\ldots,s_7)=(0,1,2,3,4,6,8,9),
\]

equivalently gaps \((1,1,1,1,2,2,1,4)\). Its full residual pair is

\[
 F_0=F=X^8-8192,
\]

\[
 Q_0=Q=X^7+2X^6+4X^5+8X^4+16X^3+64X^2+256X+512.
\]

The relevant exact values are

\[
 D=1631=7\cdot233,\quad C=7553,\quad
 m_0=\frac{7553}{1631}=\frac{1079}{233},\quad
 \operatorname{Res}(F,Q)=-2^{71}\cdot7\cdot233^2.
\]

Equations (H5)--(H7) yield the additional control

\[
 \boxed{
 \Delta_8(v;\ell)=(-8192)^\ell\,2^{71}\cdot233\in\mathbb Z
 \quad\text{for every }\ell\ge0,
 }                                                        \tag{H8}
\]

although \(v_0\notin\mathbb Z\). Modulo seven the common root is
\(X=3\); modulo 233 the common root is \(X=-3\), whereas
\(Q(3)\equiv97\pmod{233}\). Full-rank Hankel integrality has therefore
lost exactly the same distinguished-fiber information as the norm.
This does not say all smaller minors are integral: the one-by-one minor
\(v_0\) already is not.

A targeted exact rational-elimination check in this pass verified
\(D,C,\gcd(C,D)\), (H5) and (H8) at shifts zero and one, the two
modular evaluations, and the bordered identity below at
\(t=0,1,7553/1631\). No cycle enumeration was used. The written
identity (H7), rather than a finite check, proves every shift in (H8).

## 4. The first larger border is the original closing equation

For an arbitrary rational \(t\), solve the integer-affine recurrence

\[
 v_j(t)=3^j t+\sum_{i<j}3^{j-1-i}u_i
       =v_j(m_0)+(t-m_0)3^j.
\]

Every Hankel matrix depends on \(t\) through a rank-one matrix.
Consequently every square minor is affine in \(t\), regardless of its
size. In particular,

\[
 \boxed{
 \Delta_{n+1}(v(t);0)=
 (-1)^n\Delta_n(u;0)\big(F_0(3)t+Q_0(3)\big).
 }                                                        \tag{H9}
\]

Indeed the extra mode has root three and weight \(t-m_0\). Its
Vandermonde contribution is
\(\prod_\nu(3-\lambda_\nu)^2=F_0(3)^2\), so the left side is
\((t-m_0)F_0(3)^2\Delta_n(v;0)\); apply (H6).
For the control in Section 3, (H9) reads

\[
 \Delta_9(v(t);0)=
   -2^{71}\cdot7\cdot233^2\,(-1631t+7553).
\]

Thus this border vanishes precisely at the original rational closing
value. It does not produce an independent high-degree auxiliary equation
in a small integer \(m\).

There is also no positive moment matrix supplied just by positivity of
the cycle states. At an actual nontrivial integer-cycle minimum \(m>1\),
the first gap must be \(a_0=1\), since a larger gap would give a smaller
successor. Directly from (H2),

\[
 \Delta_2(v;0)=m(2^{a_0}-3)-1=-m-1<0.                    \tag{H10}
\]

Hence a positive-semidefinite Gram or Stieltjes-moment argument would
require a different construction.

For completeness, the direct size balance also has the wrong sign.
Put \(B=3+1/m\). Then \(v_j\le mB^j\) and \(u_j\le B^j\).
Descending column operations \(C_j\leftarrow C_j-3C_{j-1}\), followed
by Hadamard's inequality, give

\[
 |\Delta_n(v;0)|\le m n^{n/2}B^{(n-1)^2}.
\]

On the other hand \(2^j\mid v_j\), since \(s_j\ge j\), so
\(2^{n(n-1)}\mid\Delta_n(v;0)\). Comparing these yields only

\[
 2^{n(n-1)}\le m n^{n/2}(3+1/m)^{(n-1)^2},
\]

which supplies no lower bound of the form (H1).

## 5. The arithmetic-holonomicity interface actually tested

The primary theorem inspected was Calegari--Dimitrov--Tang,
*The unbounded denominators conjecture*, Theorem 2.0.1:
<https://math.berkeley.edu/~ytang/UDC.pdf>.
In its rational-coefficient formulation it uses a nonconstant rational
coordinate \(P(z)\), a formal coordinate \(z(t)\in t+t^2\mathbb Q[[t]]\)
making the relevant series integral, and an analytic pullback \(\phi\)
with \(\phi(0)=0\), \(|\phi'(0)|>1\), whose pulled-back functions
are holomorphic near the closed unit disk. For \(d\) functions independent
over \(\mathbb Q(P(z))\), it gives

\[
 d\le e\,
 \frac{\int_{\mathbb T}\log^+|P(\phi)|\,d\mu}
      {\log|\phi'(0)|}.                                  \tag{H11}
\]

The independence field matters here. The rational functions in (H4)
span a space of dimension one over \(\mathbb Q(z)\), even though their
Hankel recurrence degree is \(n\). Setting \(P(z)=z\) cannot replace
\(d\) by \(n\) in (H11). A different coordinate and a proved independent
family, with all integrality and analytic hypotheses checked, would be
needed. No such application yielding (H1) has been constructed.

There is an additional exact cost in the most natural normalization that
makes the orbit coefficients archimedeanly small. For an actual integer
cycle rotated to its minimum, set

\[
 r=2^{A/p},\quad
 E_j=\sum_{i<j}\log\left(1+\frac1{3x_i}\right),\quad
 \Lambda=E_p=A\log2-p\log3>0.
\]

The coefficients of \(\mathcal V(z/r)\) are

\[
 b_j=\frac{v_j}{r^j}
     =m\exp(E_j-j\Lambda/p),\qquad b_{j+p}=b_j.           \tag{H12}
\]

For \(0\le j<p\), all archimedean conjugates have absolute value
between \(me^{-\Lambda}\) and \(me^\Lambda\), since every conjugate
of \(r\) has the same modulus. But in \(K=\mathbb Q(r)\), at each
prime above two, with valuation normalized by \(v(2)=1\),

\[
 v(b_j)=s_j-Aj/p.                                        \tag{H13}
\]

This uses that every actual \(x_j\) is odd. At the other finite primes
the \(b_j\) are integral. Therefore the smallest nonnegative integer
exponent \(\kappa\) for which all \(2^\kappa b_j\) are algebraic
integers is exactly

\[
 \boxed{\kappa=
 \left\lceil\max_{0\le j<p}\left(Aj/p-s_j\right)\right\rceil.}
                                                               \tag{H14}
\]

Let \(M=\max_j x_j\). Taking logarithms in (H12) gives

\[
 (Aj/p-s_j)\log2
   =\log(x_j/m)-E_j+j\Lambda/p.
\]

Since both \(E_j\) and \(j\Lambda/p\) lie in \([0,\Lambda]\),

\[
 \boxed{M e^{-\Lambda}\le m2^\kappa<2M e^\Lambda.}       \tag{H15}
\]

Thus this coefficientwise integral normalization pays the maximum-state
height, up to the displayed factors, rather than retaining only the
minimum height. It also initially gives algebraic, not necessarily
rational, coefficients. Equations (H14)--(H15) are an obstruction to
this proposed interface; they do not assert that every possible transform
or number-field version of arithmetic holonomicity has the same cost.

## 6. Exact remaining step

The full-rank determinant is the norm condition, its first larger border
is the scalar closing equation, and positivity of the orbit is not
positivity of its Hankel form. The tested normalization introduces \(M\)
where the proposed contradiction needs \(m\).

The open task is to build a distinguished-fiber arithmetic invariant or
an independent integral analytic family whose complexity is forced by
\(n\) and whose cost is controlled by the actual minimum. Neither (H1)
nor a strict bound on \(\gcd(F_0(3),Q_0(3))\) follows from the identities
proved here. Smaller or differently bordered minors remain possible
objects of study, but no closing assertion about them is being used.
