# Direct attempt to force rationality of the basin series

**Status: UNSUCCESSFUL CLOSING ATTEMPT.** The target in this note is the
entire positive-integer Collatz conjecture, including nontrivial cycles.
The exact mixed dilation equations below have not been converted into
the finite Mahler system needed by the imported theorem. No new Lean
theorem or global convergence result is claimed.

## 1. The object that would close the problem

Use the shortcut map

\[
 T(n)=\begin{cases}n/2&n\text{ even},\\(3n+1)/2&n\text{ odd}.
 \end{cases}
\]

Let a(n) be the indicator that the forward orbit of the positive integer
n reaches 1, set a(0)=0, and put

\[
 F(z)=\sum_{n\ge0}a(n)z^n.
\]

Both directions of invariance hold, including at 1 and 2:

\[
 a(2n)=a(n),\qquad a(2n+1)=a(3n+2).                 \tag{M1}
\]

The same formulas hold for any finite-valued function constant on each
weak component of the positive Collatz graph. Thus rationality of this
particular F, followed by the elementary argument in Section 4, would
give a(n)=1 for every n>0. The proposed route does not discard escaping
components or remove periodic states from its domain.

The baseline for this attempt is our own commit
23456d145df23ef2b412f61f7e49e38a222bc2b1. The literature guide in
[PR186 at 1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493](https://github.com/GettysburgResearch/collatz/blob/1a57a3bf3c83ba2fa87d3b2216cfaff970f7a493/literature/deep-machinery-20261122/03_arithmetic_and_logic.md)
already proposes the two-scale finite-closure question in Section G.
This note actually carries out the first closure calculation; it does
not claim to originate that question or the generating-function method.

## 2. The deep theorem and its exact input

Adamczewski--Bell, Definition 1.1 and Theorem 1.3, proves that a
characteristic-zero power series satisfying finite linear Mahler
equations in two multiplicatively independent integer bases is
rational. For bases 2 and 3, the required input is a nonzero finite
relation in each of

\[
 1,F(z),F(z^2),\ldots,F(z^{2^r}),\qquad
 1,F(z),F(z^3),\ldots,F(z^{3^s})
\]

over the rational-function field. The integers r,s and the coefficient
functions must describe the same all-time F.

Schäfke--Singer, Theorem 1 and Proposition 3, gives a second proof through
finite-dimensional consistent difference systems. Their matrices must
be invertible over the rational-function field, and the two substitution
actions must preserve one fixed finite-dimensional space.

Primary texts inspected:

- [Adamczewski--Bell, A problem about Mahler functions, published PDF](https://journals.sns.it/index.php/annaliscienze/article/download/574/560).
- [Schäfke--Singer, Mahler equations and rationality, author PDF dated 21 March 2017](https://singer.math.ncsu.edu/papers/vshort2-5.pdf).

The newer multivariate machinery of Adamczewski--Faverjon does not
remove the finite-system input. Its independent-transformation purity
theorem, Theorem 3.8, starts with finite linear Mahler systems and also
requires regular evaluation points, admissible transformations, and
multiplicatively independent spectral radii. No such systems have been
constructed here.

- [Adamczewski--Faverjon, author text](https://faverjon.perso.math.cnrs.fr/AdamczewskiFaverjon_MahlerFiniteAutomata.pdf).
- [Published Annals record, 204 (2026), 455--533](https://annals.math.princeton.edu/2026/204-2/p01).

## 3. Executing the closure calculation

Let omega be a primitive complex cube root of unity. Coefficient
extraction from (M1) gives two exact identities:

\[
 F(z)+F(-z)=2F(z^2),                              \tag{M2}
\]

\[
 F(z^3)=F(z^6)+\frac1{3z}
       \sum_{j=0}^2\omega^jF(\omega^jz^2).        \tag{M3}
\]

There is no pole in the second term: the roots-of-unity filter retains
only indices congruent to 2 modulo 3. In fact that term is

\[
 z^3\sum_{m\ge0}a(3m+2)z^{6m}.
\]

It equals the odd-index part of F(z^3) by (M1). Formula (M3) is the
Berg--Meinardus fixed-point equation in an integral-power form; the
adjoint formulation and its appropriate function-space boundary are
also displayed in Neklyudov's preprint, Section 1. We independently
checked the coefficient filter here.

- [Neklyudov, arXiv:2106.11859v9, 1 June 2022](https://arxiv.org/pdf/2106.11859).

### 3.1. Why adding three rotations did not close the system

The first candidate vector was F(z), F(omega z), F(omega squared z).
But to obtain an equation for F(omega z cubed) from (M3), substitute
zeta z, where zeta is a primitive ninth root with zeta cubed = omega:

\[
 F(\omega z^3)=F(\omega^2z^6)
 +\frac1{3\zeta z}\sum_{j=0}^2
       \omega^jF(\omega^j\zeta^2z^2).             \tag{M4}
\]

Ninth-root rotations now occur. Repeating this particular closure
procedure introduces rotations of orders 27,81,... . There is no finite
index set of roots of unity closed under the required repeated choice
of cubic preimages and containing a primitive cube root.

This is a failure of the displayed construction. It is **not** a proof
that the functions at these rotations are linearly independent, or
that another finite rational-function basis cannot work. If Collatz
holds, F=z/(1-z), and every one of them is rational. The unresolved
question is precisely whether actual basin information supplies the
linear dependencies that the substitution calculation alone lacks.

Equation (M2) also does not by itself make F 2-Mahler: it contains
F(-z), whose odd coefficient section remains unspecified. Keeping a
sign coordinate does not repair the expanding ternary-rotation index.

### 3.2. Exact sections, without complex roots

Write

\[
 \Lambda_{b,r}F(z)=\sum_{n\ge0}a(bn+r)z^n,
 \qquad 0\le r<b.
\]

For 0 <= p < 2^k, let o(p,k) be the odd count among the first k
shortcut steps of p. Exact parity coding gives

\[
 T^k(p+2^kn)=T^k(p)+3^{o(p,k)}n.                  \tag{M5}
\]

Moreover

\[
 0\le T^k(p)<3^{o(p,k)}.                         \tag{M6}
\]

For completeness, the induction for (M6) maintains
T^j(p) < 2^(k-j) 3^(o(p,j)). At an odd step the integer input is at
most that integer upper bound minus one; applying (3x+1)/2 leaves a
strict gap. An even step simply halves both sides. Thus no unreduced
residue or unmentioned prefix shift is needed in

\[
 \Lambda_{2^k,p}F
   =\Lambda_{3^{o(p,k)},\,T^k(p)}F.              \tag{M7}
\]

Examples are

\[
 \Lambda_{2,0}F=F,\quad
 \Lambda_{2,1}F=\Lambda_{3,2}F,\quad
 \Lambda_{4,1}F=\Lambda_{3,1}F,\quad
 \Lambda_{4,3}F=\Lambda_{9,8}F.
\]

Along the all-odd branch this is

\[
 \Lambda_{2^k,2^k-1}F
       =\Lambda_{3^k,3^k-1}F.                    \tag{M8}
\]

The binary kernel is therefore contained in the ternary kernel as a
set of actual coefficient sequences. **Containment does not prove
that either kernel is finite.** Replacing one infinite family by
another is the unclosed step, even though every individual identity
holds for ordinary positive integers.

A recent author manuscript by u/fourier_wren develops the reverse
transfer on ternary-unit sections and concludes that either 2- or
3-automaticity of a saturated set already forces triviality. Its
Sections 3--4 were inspected after the calculation above. This is a
source-qualified comparison, not a newly established automaticity
theorem for the basin:

- [Automaticity of saturated sets..., v2, 30 October 2026](https://rstation.ai/problems/collatz/papers/64/v2).

### 3.3. Finite approximants do not supply the missing uniformity

Let a_t(n) record arrival at 1 within t shortcut steps. Every nonzero
coefficient has n <= 2^t, so its generating function F_t is a polynomial.
Each F_t separately satisfies finite Mahler equations, as every rational
function does. Nevertheless, their orders or coefficient degrees can
depend on t. Coefficientwise convergence F_t -> F does not preserve a
uniform finite equation without a separate bound on its description.

This prevents using finite-time rationality as an application of the
deep theorem. We did not run a large finite kernel search: without a
uniform argument, a numerical plateau would not close this obligation.

## 4. The last step would be exact, if rationality were obtained

Here is the complete elementary implication needed after Mahler
rationality, to distinguish it from the missing premise.

A rational power series with coefficients in a finite alphabet has
eventually periodic coefficients. Indeed its eventual linear recurrence
has only finitely many possible state windows; a repeated window forces
all future windows to repeat.

Let M be a positive eventual period of a, and let lambda(r) denote the
eventual value on the residue r modulo M. Doubling invariance gives

\[
 \lambda(2r)=\lambda(r).                         \tag{M9}
\]

If M is even, (M9) makes M/2 a period, since
lambda(r+M/2)=lambda(2r+M)=lambda(r). Repeating removes the powers of
2. With M odd, each residue has arbitrarily large odd representatives,
so the odd Collatz rule, followed by (M9), gives

\[
 \lambda(3r+1)=\lambda(r).                       \tag{M10}
\]

If 3 divides M, (M10) similarly makes M/3 a period. After removing
these factors, gcd(M,6)=1, and (M9)--(M10) imply

\[
 \lambda(6r+1)=\lambda(r)=\lambda(6r+2).
\]

As 6r runs through all residues, lambda is constant. Finally every
positive n has arbitrarily large dyadic multiples and
a(2^j n)=a(n); hence eventual constancy implies constancy on all positive
integers. For the basin indicator a(1)=1, so that constant is 1.

The earlier Bell--Lagarias paper already proves the rationality/Collatz
equivalence for the basin series as part of a broader inverse-orbit
classification. Its Theorems 1.1--1.2 also show why generic analytic
continuation of ancestor series cannot be assumed. The elementary
argument above is a self-contained final implication, not a claim of
priority over that work.

- [Bell--Lagarias, Acta Arithmetica 170 (2015), 101--120, primary PDF](https://www.impan.pl/shop/en/publication/transaction/download/product/82190).

## 5. Result of the attempt

The closing route was actually pursued through its proposed finite
representation, not stopped at the name of a theorem. It yields an
exact all-source section transfer and an explicit unbounded rotation
ladder in the first candidate system. It does **not** yield either of
the finite Mahler equations required for F.

The first unsupported claim is therefore:

> The actual all-time basin series admits a fixed finite-dimensional
> rational-function space invariant under both z -> z squared and
> z -> z cubed.

No repository density bound, finite-word classification, or compact
coordinate invariance inspected in this pass proves that claim. The
attempt remains open at this exact premise. All statements in this
note are written mathematics or identified literature statements;
there is no new compiler receipt associated with it.
