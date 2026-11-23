# Attempt to force Mahler rigidity from an actual basin indicator

**Outcome: no finite-rank deduction, rationality theorem, or Collatz
closure was obtained.** This is a separate direct attack using generating
functions and multiplicatively independent substitutions. The mixed
functional equation below is historical Berg–Meinardus material, not a
new reformulation claimed as progress.

## 1. Exact coefficient and functional equations

Let \(a_n\) be a bounded function constant on ordinary Collatz components;
the main case is the \(0/1\) indicator of the basin of 1. Set \(a_0=0\)
and

\[
F(z)=\sum_{n\ge1}a_nz^n,\qquad |z|<1.
\]

The shortcut map gives the exact relations

\[
a_{2n}=a_n,\qquad a_{2n+1}=a_{3n+2}.
\tag{1}
\]

Write \(C_{b,r}F(z)=\sum_{n\ge0}a_{bn+r}z^n\) for residue extraction.
Then

\[
C_{2,0}F=F,\qquad C_{2,1}F=C_{3,2}F,
\]

and consequently

\[
F(z)=F(z^2)+z\,C_{3,2}F(z^2).
\tag{2}
\]

For \(\omega=e^{2\pi i/3}\), the root-of-unity filter converts (2) to

\[
\boxed{3t\,[F(t^3)-F(t^6)]
 =F(t^2)+\omega F(\omega t^2)+\omega^2F(\omega^2t^2).}
\tag{3}
\]

These calculations are identities of convergent series and of formal
series. No branch of a fractional power is needed. Equation (3) is the
homogeneous Berg–Meinardus equation. Efrem's 2025 primary manuscript,
Section 1.1, equations (3)–(6), explicitly gives its history and the
corresponding analytic reformulation.

## 2. Attempt to close the extraction system

The natural states are the sequences

\[
A_{k,r}(n)=a_{3^k n+r},\qquad k\ge0,\quad0\le r<3^k.
\]

Apply one binary extraction \(D_\epsilon s(n)=s(2n+\epsilon)\),
\(\epsilon\in\{0,1\}\). Since \(3^k\) is odd, (1) gives

\[
D_\epsilon A_{k,r}=
\begin{cases}
A_{k,(3^k\epsilon+r)/2},&\epsilon+r\text{ even},\\[2mm]
A_{k+1,(3^{k+1}\epsilon+3r+1)/2},&\epsilon+r\text{ odd}.
\end{cases}
\tag{4}
\]

Both indices are integers in their displayed residue ranges. Starting
from \(A_{0,0}=a\), this describes a countable exact system containing
every binary-kernel state. In particular

\[
D_1^k a(n)=a_{2^k(n+1)-1}=a_{3^k(n+1)-1}=A_{k,3^k-1}(n).
\tag{5}
\]

I tried to eliminate the growing modulus by using root-of-unity
rotations and the even equation

\[
F(z)+F(-z)=2F(z^2).
\tag{6}
\]

The rotations of (3) by cube roots of unity only reproduce the same
filtered relation. Replacing \(t\) by \(-t\) recovers (6) at
\(z=t^3\); it does not supply a second independent equation. Attempting
to close a vector of finitely many rotated copies under substitutions
introduces additional half-angle or third-angle rotations, while (4)
continues to create larger ordinary residue moduli.

This establishes neither finite rank nor infinite rank. Unbounded
*labels* in (4) do not prove that the resulting sequences are distinct
or linearly independent: if all positive integers reach 1, the basin
indicator is constant on positive indices. What is missing from this
attack is a proof that the actual states satisfy finitely many sufficient
linear dependences. Boundedness, a finite coefficient alphabet, and the
finite description of the two arithmetic rules do not themselves supply
such dependences.

## 3. The precise classical rigidity theorem that was tested

Adamczewski–Bell, *A problem about Mahler functions*, Theorem 1.3, and
Schäfke–Singer, *Mahler equations and rationality*, Theorem 1, prove
rationality in characteristic zero when one series satisfies two separate
finite Mahler equations with multiplicatively independent bases. In the
present application the needed inputs would be, for finite \(m,\ell\),

\[
\sum_{i=0}^{m}p_i(z)F(z^{2^i})=0,
\qquad
\sum_{j=0}^{\ell}q_j(z)F(z^{3^j})=0,
\tag{7}
\]

with rational-function coefficients and nonzero endpoint coefficients
after the usual normalization. Equation (3), which mixes bases and a
residue projection, is not a pair of equations of the form (7).

In the Schäfke–Singer proof the separate equations produce a finite
\(\mathbb C(z)\)-space invariant under both substitutions. A basis then
gives invertible matrices \(A,B\) satisfying

\[
Y(z^2)=A(z)Y(z),\qquad Y(z^3)=B(z)Y(z),
\qquad A(z^3)B(z)=B(z^2)A(z).
\]

The consistency and regular-singular machinery applies to this finite
system. This attempt did not construct that finite space or those
matrices for the actual basin series. The theorem was therefore not
applied to claim rationality.

## 4. Pólya–Carlson does not select the required alternative

For the nonempty basin indicator, infinitely many coefficients are one
(doubling any basin member stays in the basin), and all coefficients are
zero or one. Its radius of convergence is therefore exactly one.
Pólya–Carlson gives the rational/natural-boundary dichotomy. It does not
eliminate the natural-boundary case. The mixed equation has not supplied
analytic continuation across an arc of the circle.

This target is already explicit in Bell–Lagarias, *3x+1 inverse orbit
generating functions almost always have natural boundaries*, Theorem
1.2: rationality for the basin-of-1 generating function is equivalent
to the Collatz assertion; if that assertion is false, this generating
function has a natural boundary. Their theorem also proves natural
boundaries for many actual ancestor-set series, so no generic smoothing
claim for the Collatz operator is available merely from the functional
equation's form. An ancestor set at a nonperiodic target is not itself
the fully saturated basin used in (1); these objects must not be equated.

## 5. Result and source access

The direct algebra produced the exact hierarchy (4), but no closing
dependence. The pass therefore obtained no rationality result for the
actual basin, no separate finite Mahler equations, and no theorem about
all ordinary trajectories. No Lean declaration was added for these
routine identities. This note is an unsuccessful attempt record.

Primary sources inspected:

- Boris Adamczewski and Jason P. Bell, *A problem about Mahler functions*,
  Ann. Sc. Norm. Super. Pisa XVII (2017), Theorem 1.3;
  [author PDF](https://adamczewski.perso.math.cnrs.fr/Cobham.pdf).
- Reinhard Schäfke and Michael F. Singer, *Mahler equations and
  rationality*, March 21, 2017 author manuscript, Theorem 1 and its
  finite-space construction on pages 1–3;
  [author PDF](https://singer.math.ncsu.edu/papers/vshort2-5.pdf).
- Jason P. Bell and Jeffrey C. Lagarias, *3x+1 inverse orbit generating
  functions almost always have natural boundaries*, Acta Arithmetica
  170 (2015), 101–120, DOI 10.4064/aa170-2-1. The inspected
  [author preprint](https://arxiv.org/pdf/1408.6884) is arXiv v1,
  August 28, 2014; Theorems 1.2 and 2.2 are the relevant statements.
- Christos N. Efrem, *Functional Equations for Generalized Collatz
  Dynamics Using Integral Representations and Residue Calculus*,
  [arXiv:2510.06736v1](https://arxiv.org/html/2510.06736v1),
  Section 1.1, equations (3)–(6), for the historical equation and
  attribution to Berg–Meinardus. No analytic closure theorem is imported
  from that manuscript.
- Berg–Meinardus's 1995 Rostock publication metadata was accessed at
  [the institutional page](https://www.math.uni-rostock.de/math/pub/romako/heft48/berg2.html).
  Its linked PostScript was not readable through the search tool. The
  historical full paper was therefore not independently audited here.
