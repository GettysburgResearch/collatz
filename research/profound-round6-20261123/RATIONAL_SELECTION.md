# Rational selection through the actual arithmetic germ

23 November 2026. Round six, parent checkpoint
`afe6f4d1a661b377c9daa4623bdd732ba478386b`.

**Status: PROPOSED written arithmetic theorem with a Lean-checked finite
ordered-word core. The convergence corollary is SOURCE-QUALIFIED by the
frozen PR178 arithmetic-germ consumer. No universal rational complementary
candidate or universal arithmetic germ is constructed. Full Collatz remains
open.**

The new result concerns the **prime divisors of the actual Taylor
coefficients at the binary interpolation point**. Every nonstandard
positive integer cycle would force an odd prime other than three to occur
with exponentially growing powers in those denominators. Consequently the
natural strengthening of the upstream Jet hypothesis from an arbitrary
ring `Z[1/M]` to `Z[1/3]` excludes every other positive cycle as well as
giving eventual periodicity through the upstream consumer. This removes a
separate cycle-exclusion obligation from that conditional route.

The all-time arithmetic-germ construction remains the first unsupported
step. Even rationality of its first derivative is not established for an
arbitrary positive source.

## 1. The one fixed ordinary source and the exact germ

Use the shortcut map

\[
T(x)=
\begin{cases}
x/2,&x\equiv0\pmod2,\\
(3x+1)/2,&x\equiv1\pmod2.
\end{cases}
\]

Fix **one positive ordinary integer** \(n\). Define its actual orbit,
parity count, and weighted parity series by

\[
x_k=T^k(n),\qquad e_k=x_k\bmod2,\qquad
p_k=\sum_{j<k}e_j,
\]
\[
B_n(z)=\sum_{k\ge0}e_k\,3^{-p_{k+1}}z^k.
\tag{1}
\]

The full affine identity is

\[
n+\sum_{j<k}e_j3^{-p_{j+1}}2^j
   =\frac{2^kx_k}{3^{p_k}}.
\tag{2}
\]

It gives \(B_n(2)=-n\) in \(\mathbb Q_2\). Because the coefficients in
(1) are binary integral, the actual binary function is analytic on
\(|z|_2<1\), which contains both zero and two. Its literal translated germ is

\[
J_n(t)=B_n(2+t)=\sum_{j\ge0}c_jt^j\in\mathbb Q_2[[t]].
\tag{3}
\]

In particular \(c_0=-n\). Neither a freely chosen rational germ with this
constant term nor a sequence of changing finite parity realizers is (3).

## 2. Precise source dependencies

The following PR178 files were read at the fixed full head
`398b3a04da071e96362005792417bd5cf8cc6497`. Path prefixes in this table are
`research/literature-push-20261123/rigidity/`.

| Exact path | Git blob | Imported claim and scope |
| --- | --- | --- |
| [GENERAL_DENSITY_JET.md](https://github.com/GettysburgResearch/collatz/blob/398b3a04da071e96362005792417bd5cf8cc6497/research/literature-push-20261123/rigidity/GENERAL_DENSITY_JET.md) | `5a4250dfc3b976dd5eb552d4a4b008ec19a120ee` | Section 1 theorem and Sections 2–5 proof: a limiting actual parity density plus the full Jet hypothesis J gives rational \(B_n\), hence eventual ordinary periodicity. |
| [SCALAR_BOUNDARY_AND_SECOND_CENTER.md](https://github.com/GettysburgResearch/collatz/blob/398b3a04da071e96362005792417bd5cf8cc6497/research/literature-push-20261123/rigidity/SCALAR_BOUNDARY_AND_SECOND_CENTER.md) | `951a88535220cf0673dd7a9186b0751368c76ce6` | Section 1 definitions and complete identity; Section 4 definition of J; equation (4) credits the inherited rational-series consumer. |
| [FINITE_FILTER_TEST.md](https://github.com/GettysburgResearch/collatz/blob/398b3a04da071e96362005792417bd5cf8cc6497/research/literature-push-20261123/rigidity/FINITE_FILTER_TEST.md) | `c31b142a0b56c0ffe1c682581c2bc196ba35bdc0` | A finite rational filter does not freely remove the exponential ternary denominators from the actual coefficients. It supplies no construction of J. |

The external consumer retains all these hypotheses:

1. \(p_k/k\) has a limit;
2. every coefficient of the actual germ (3) is rational;
3. they lie in one fixed ring \(\mathbb Z[1/M]\);
4. that germ has positive convergence radius at infinity and every prime
   dividing \(M\).

It concludes eventual ordinary periodicity, not convergence to the standard
cycle. The extension from the critical density to all limiting densities
is a written application of the multipoint theorem, not a Lean theorem.
The present cycle obstruction does **not** need that application once
eventual periodicity is assumed.

For the requested current-repository comparison, PR177 was refreshed at
`92e7aaf602a0d4f0442556a133ae8e882e1fe93f` and PR176 at
`81095581a1dccb8b5d89ee2ea3e9ba4a7b447e0a`. Their PR metadata and full
descriptions were read; their new exact files were not mathematical
dependencies of this note. These observations are not reviews of those
heads.

## 3. An uncancellable positive pole

Assume for this section that the actual orbit is eventually periodic.
Let its chronological preperiod word be \(a\), of length \(h\) and odd
count \(s\), and its repeated word be \(w\), of length \(A>0\) and odd
count \(p>0\). Neither word is replaced by an unordered multiset.

For any finite word \(v\) of length \(L\), write
\(p_j(v)=\sum_{i<j}v_i\), \(p(v)=p_L(v)\), and define the full carry
polynomial

\[
C_v(z)=\sum_{j=0}^{L-1}v_j\,3^{p(v)-p_{j+1}(v)}z^j.
\tag{4}
\]

Every nonzero coefficient is positive. Its recursion and concatenation
identity are

\[
C_{b::v}(z)=b\,3^{p(v)}+zC_v(z),
\]
\[
C_{a v}(z)=3^{p(v)}C_a(z)+z^{|a|}C_v(z).
\tag{5}
\]

Summing the entire repeated tail, rather than one denominator factor,
gives

\[
B_n(z)=
\frac{C_a(z)}{3^s}
+\frac{z^h}{3^s}\frac{C_w(z)}{3^p-z^A}
=\frac{N_{a,w}(z)}{3^s(3^p-z^A)},
\tag{6}
\]
\[
N_{a,w}(z)=C_a(z)(3^p-z^A)+z^hC_w(z).
\]

Put \(r=3^{p/A}>0\). Since \(p>0\), \(C_w(r)>0\), and therefore

\[
N_{a,w}(r)=r^hC_w(r)>0.
\tag{7}
\]

**R6-SEL-1.** The positive real zero \(r\) of the complete repeated-block
denominator is a genuine pole of \(B_n\). No preperiod and no common
polynomial factor can cancel this pole.

This uses positivity of the ordered coefficients, not an assumed gcd
bound. It remains valid even when evaluation at \(z=2\) cancels large
parts of the full integer denominator.

Now set

\[
g=\gcd(A,p),\qquad u=A/g,\qquad v=p/g,\qquad
F(z)=z^u-3^v.
\tag{8}
\]

The polynomial \(F\) is irreducible over \(\mathbb Q\). Here is an
elementary proof. A monic rational factor is integral by Gauss's lemma.
If its degree is \(d\), each of its complex roots has absolute value
\(3^{v/u}\), so its nonzero integer constant term \(q\) satisfies

\[
|q|^u=3^{vd}.
\]

Unique prime factorization gives \(u\mid vd\). Because \(\gcd(u,v)=1\),
we have \(u\mid d\); thus no factor has \(0<d<u\).
Since \(r\) has minimal polynomial \(F\), (7) shows that \(F\) divides the
**reduced rational-function denominator** of \(B_n\).
Every conjugate root of \(F\), at every completion, remains a pole:
coprimality of the reduced numerator and denominator persists after
extending the coefficient field.

The passage to \(F\) is not a replacement of the original ordinary
integrality condition by a proper-factor divisibility test. Equation (6)
first retains the complete denominator, and (7) then proves that this
particular irreducible factor cannot cancel as a polynomial.

## 4. Every reduced-denominator prime appears in the actual jet

For a rational number \(q\), let \(\operatorname{den}(q)>0\) be its
reduced positive denominator, with \(\operatorname{den}(0)=1\).
Normalize \(v_\ell(\ell)=1\).

For an actual positive cycle, the complete cycle product gives

\[
3^p<2^A,
\]

so the positive integer

\[
D_{\mathrm{red}}=F(2)=2^u-3^v
\tag{9}
\]

is well defined. It is odd and prime to three.

**R6-SEL-2 (quantitative denominator theorem).** Suppose the fixed
positive ordinary source \(n\) is eventually periodic, with \(u,v\) as
in (8). Its actual Taylor coefficients \(c_j\) in (3) are rational.
For every prime \(\ell\mid D_{\mathrm{red}}\),

\[
\boxed{\displaystyle
\limsup_{j\to\infty}
\frac{v_\ell(\operatorname{den}(c_j))}{j}
\ \ge\
\frac{v_\ell(D_{\mathrm{red}})}{u}>0.}
\tag{10}
\]

**Proof.** Work in a complete algebraic closure of \(\mathbb Q_\ell\).
Let \(\alpha_1,\ldots,\alpha_u\) be the roots of \(F\).
Because \(\ell\ne3\), each \(\alpha_i\) is an \(\ell\)-adic unit.
As \(\ell\ne2\), each difference \(2-\alpha_i\) is integral. The full
product gives

\[
\sum_{i=1}^u v_\ell(2-\alpha_i)
=v_\ell\!\left(\prod_{i=1}^u(2-\alpha_i)\right)
=v_\ell(F(2)).
\tag{11}
\]

Consequently at least one root \(\alpha\) satisfies

\[
v_\ell(2-\alpha)\ge v_\ell(D_{\mathrm{red}})/u>0.
\tag{12}
\]

Section 3 proves that \(\alpha\) is an actual pole. Thus the radius of
the Taylor expansion at two is at most

\[
|2-\alpha|_\ell\le
\ell^{-v_\ell(D_{\mathrm{red}})/u}<1.
\tag{13}
\]

For completeness this upper bound does not assume a vague
analytic-continuation principle. Write \(B_n=P/Q\) in reduced form.
The formal identity
\(Q(2+t)J_n(t)=P(2+t)\) holds. If the series converged on a disc containing
\(t=\alpha-2\), multiplication by the polynomial and evaluation there
would give \(0=P(\alpha)\), contradicting coprimality.
The nonarchimedean Cauchy–Hadamard formula applied to (13) gives (10).
The usual convention \(v_\ell(0)=+\infty\) causes no difficulty, because
the stated expression uses reduced positive denominators. \(\square\)

The radius formula used here is Theorem 3.7 of Keith Conrad,
[*Infinite series in p-adic fields*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf).
The local pole calculation and its application to this particular orbit
are proved above.

**R6-SEL-3 (prime support).** If an eventually periodic positive
ordinary source has all its actual \(c_j\) in \(\mathbb Z[1/M]\), then

\[
\boxed{\operatorname{rad}(D_{\mathrm{red}})
       \mid\operatorname{rad}(M).}
\tag{14}
\]

Indeed, for any \(\ell\nmid M\) all the coefficients are
\(\ell\)-integral, giving radius at least one and contradicting (13).
No archimedean growth bound, ternary growth bound, or limiting-density
assumption is needed for this obstruction after eventual periodicity is
known.

## 5. A ternary arithmetic germ excludes all other positive cycles

For the \(p\) odd states \(q_i\) on a positive ordinary cycle, multiplication
of the accelerated odd-step relations gives

\[
2^A=\prod_{i=1}^{p}\left(3+\frac1{q_i}\right)\le4^p,
\tag{15}
\]

with equality only when every \(q_i=1\).
Also every factor exceeds three, so \(2^A>3^p\).

If \(D_{\mathrm{red}}=1\), then \(2^u=3^v+1\).
For \(u,v\ge1\), the only solution is \(u=2,v=1\): \(u=1\) is impossible,
and if \(u\ge3\), reduction modulo eight would require
\(3^v\equiv7\pmod8\), whereas its residues are only one and three.
For \(u=2\), necessarily \(v=1\).
It follows that \(A=2p\), so (15) is an equality and the cycle is the
standard \(1\leftrightarrow2\) cycle.

Thus a nonstandard positive ordinary cycle has
\(D_{\mathrm{red}}>1\), and some prime \(\ell\ne2,3\) divides it.
Equations (10)–(14) exclude this possibility when all actual jet
coefficients lie in \(\mathbb Z[1/3]\).

**R6-SEL-4.** For a positive ordinary source already known to be
eventually periodic,

\[
J_n(t)\in\mathbb Z[1/3][[t]]
\quad\Longleftrightarrow\quad
T^k(n)=1\text{ for some }k.
\tag{16}
\]

The reverse implication, including a stronger common-denominator
statement, is proved in Section 6.

The independently developed finite arithmetic attachment is
[CYCLE_ARITHMETIC.md](CYCLE_ARITHMETIC.md) and
[CycleArithmetic.lean](CycleArithmetic.lean).
Its statements retain actual positive state equations and a successor
permutation rather than assuming the cycle-product inequality as a
black box.

Define **J3** to mean:

- (3) is the actual binary germ and every coefficient is in
  \(\mathbb Z[1/3]\);
- this rational-coefficient series has positive radius of convergence
  at infinity and at three.

**R6-SEL-5 (source-qualified full convergence criterion).**
On the class of fixed positive ordinary sources for which \(p_k/k\)
has a limit,

\[
\boxed{J3(n)\quad\Longleftrightarrow\quad
       T^k(n)=1\text{ for some }k.}
\tag{17}
\]

For the forward implication use the frozen PR178
`GENERAL_DENSITY_JET.md` theorem with \(M=3\) to obtain eventual
ordinary periodicity, then apply (16). The reverse implication follows
from Section 6. This is stronger than the arbitrary-\(M\) Jet consumer,
which allows any eventual cycle. It remains conditional on constructing
J3 for the source and on the existence of the limiting density.

The external potential-theoretic input is Chambert-Loir–Noûs,
[*Potentiel et rationalité*](https://arxiv.org/pdf/2305.17210),
arXiv:2305.17210v2, 31 August 2026, Sections 4.1–4.3.
Its hypotheses concern full arithmetic formal germs, compatible local
meromorphic realizations, an integral model outside a finite prime set,
and a strictly positive potential-game value.
Its preceding one-center framework is Bost–Chambert-Loir,
[*Analytic curves in algebraic varieties over number fields*](https://webusers.imj-prg.fr/~marco.maculan/java/2016/files/BostChambertLoir.pdf),
arXiv:math/0702593v3, Theorem 7.9, the following condition \(2'\), and
Example 7.10.
Neither paper asserts that the required second germ arises automatically
from a rational value at that point.

## 6. The exact common denominator supplied by actual convergence

Suppose the first hit of one occurs after \(\tau\) steps, of which \(s\)
are odd. Since \(B_1(z)=1/(3-z^2)\), the exact prefix identity gives

\[
B_n(z)=\frac{C_a(z)}{3^s}
       +\frac{z^\tau}{3^s(3-z^2)}.
\tag{18}
\]

After translating,

\[
3^sJ_n(t)=C_a(2+t)
-\frac{(2+t)^\tau}{1+4t+t^2}.
\tag{19}
\]

The denominator on the right has constant coefficient one, so its
formal inverse has integer coefficients. Hence

\[
\boxed{3^sJ_n(t)\in\mathbb Z[[t]].}
\tag{20}
\]

This uses one common denominator for the **entire** germ, which is
stronger than the varying powers of three allowed by J3.
The germ has a positive complex convergence radius, at least
\(2-\sqrt3\), and ternary radius at least one; its actual parity density
is \(1/2\). Thus convergence supplies all hypotheses in (17).

Equation (20) is a target for a new construction, not a derivation of
that construction from ordinary integrality alone. The parameter \(s\)
here comes from an already known successful orbit.

## 7. A cancellation control and the first unconstructed coefficient

The exact positive rational cycle with chronological word
\(110000\) is

\[
\frac1{11}\longmapsto\frac7{11}\longmapsto\frac{16}{11}
\longmapsto\frac8{11}\longmapsto\frac4{11}
\longmapsto\frac2{11}\longmapsto\frac1{11}.
\]

It is a cycle on rationals with odd denominator, **not** an ordinary
positive integer cycle. Its full word has \(A=6,p=2\), and

\[
B(z)=\frac{3+z}{9-z^6},\qquad
D=2^6-3^2=55,\qquad C(2)=5.
\]

The factor five disappears from the reduced constant value:

\[
B(2)=-\frac1{11}.
\]

However \(u=3,v=1\), so \(D_{\mathrm{red}}=5\), and the very next Taylor
coefficient is

\[
B'(2)=\frac{181}{605}
      =\frac{181}{5\cdot11^2}.
\tag{21}
\]

Thus cancellation from the known value at two does not imply
cancellation from the actual germ. The positive pole of \(z^3-3\)
remains. This fixture supports the necessity of considering all
coefficients and is not evidence for an ordinary counterexample.

For an arbitrary positive ordinary source, the first unknown
coefficient is already

\[
d(n):=c_1=B_n'(2)
=\sum_{k\ge1} k e_k\,2^{k-1}3^{-p_{k+1}}
\quad\text{in }\mathbb Q_2.
\tag{22}
\]

The actual tail identity yields the exact cocycle

\[
\boxed{2d(Tx)=3^{x\bmod2}d(x)+Tx.}
\tag{23}
\]

This follows by differentiating
\(B_x(z)=3^{-e}(e+zB_{Tx}(z))\) and using
\(B_{Tx}(2)=-Tx\). A rational choice for \(d(n)\) must satisfy this
identity and all-time binary legality, not merely fit finitely many
Taylor digits.

For example, \(d(1)=4\), and on the known power-of-two orbit,

\[
d(2^k)=2^k(4-k/2).
\tag{24}
\]

In particular \(d(128)=64\); because \(T(85)=128\), equation (23)
gives \(d(85)=0\). Positivity or nonvanishing of this derivative is
therefore not a valid general invariant. Equations (22)–(23) have not
given its rationality, a denominator bound, or a universal complementary
candidate.

The round-five finite rational verifier still decides each **supplied**
candidate with its complete denominator retained. This note neither
changes that verifier nor turns its total guard into a universally
successful selector. The attempted literature route has produced the
prime-support obstruction above; the missing source construction is
still substantive.

## 8. Formalization and evidence boundary

[RationalSelection.lean](RationalSelection.lean) formalizes seven finite
theorems for all chronological Boolean words:

- exact odd-count concatenation;
- full carry-polynomial concatenation;
- nonnegative evaluation for nonnegative real arguments;
- positive evaluation for positive arguments when an odd input occurs;
- the exact prefix-period numerator evaluation at a denominator root;
- positivity at its positive real root;
- nondivisibility by any polynomial factor vanishing at that root.

These prove the finite noncancellation mechanism (7). The module does
not formalize Gauss's lemma application here, binomial irreducibility,
nonarchimedean analytic radii, or the multipoint rationality theorem.
Those parts are the written proof and source-qualified deduction above.
The companion cycle module checks the separate finite arithmetic
attachment.

The Lean target is 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`, using
`-j1 -DwarningAsError=true -DautoImplicit=false`.
Exact execution and publication receipts belong to the round-six
checkpoint report; they are not a proof of the unformalized analytic
claims.
