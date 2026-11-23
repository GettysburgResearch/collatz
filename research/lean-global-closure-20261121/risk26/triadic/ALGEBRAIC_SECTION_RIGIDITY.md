# The autoconjugacy has no algebraic ordinary generating function

23 November 2026. **PROPOSED written theorem, with a complete proof below;
not Lean formalized.** This is a restriction on representations of the
whole sequence. It neither disproves nor proves that each individual
ordinary value of the autoconjugacy is triadic. Universal successful
triadic-witness construction remains **OPEN**.

The attempted construction was to close the finite Newton coefficients
using simultaneous dilation equations and arithmetic rationality. The
exact section equation instead gives an unconditional obstruction to a
large part of that strategy: both the ordinary generating function of
the values and the ordinary generating function of their Newton
coefficients are transcendental over the rational-function field.

## 1. Objects and exact statement

Use the shortcut map

\[
T(x)=x/2\quad(x\text{ even}),\qquad
T(x)=(3x+1)/2\quad(x\text{ odd}).
\]

Let `f=Omega` be its parity-complement autoconjugacy on `Z_2`. Its
defining finite equations are

\[
3f(2n)=2f(n)-1,\qquad f(2n+1)=2f(3n+2),
\quad f(0)=-1,\quad f(1)=2.                       \tag{AS1}
\]

The autoconjugacy and its normalization are from Monks--Yazinski,
*The autoconjugacy of the 3x+1 function*, Sections 1--2:
<https://monks.scranton.edu/files/pubs/AutoConjV13.pdf>.
No all-source convergence statement is used in (AS1).

Define formal power series over `Q_2`, without assuming complex
convergence,

\[
F(z)=\sum_{n\ge0}f(n)z^n,\qquad
G(z)=F(z)+\frac1{1-z}=\sum_{n\ge0}(f(n)+1)z^n.
\]

For `H(z)=sum h_n z^n`, write

\[
U_2H(z)=\sum_{n\ge0}h_{2n}z^n.
\]

Then (AS1) says exactly

\[
\boxed{U_2G=\frac23G,\qquad G(0)=0,\quad [z]G=3.}    \tag{AS2}
\]

**Theorem AS-A.** `F` and `G` are transcendental over `Q_2(z)`.

If

\[
a_j=\sum_{i=0}^j(-1)^{j-i}\binom ji f(i),\qquad
A(w)=\sum_{j\ge0}a_jw^j,
\]

then `A` is also transcendental over `Q_2(w)`.

The proof uses only the first functional equation and the nonzero value
`f(1)+1=3`. The odd equation is needed for the definition of the actual
autoconjugacy, but not for this obstruction.

## 2. Algebraic section-eigenvalue lemma

**Lemma AS-B.** Let `H` be a nonzero complex algebraic power series,
analytic at zero, with `H(0)=0`. If

\[
U_2H=cH\quad\text{for some real }c>0,                 \tag{AS3}
\]

then there is a rational number
`rho` outside the set of nonnegative integers such that

\[
\boxed{c=2^{-\rho-1}.}                              \tag{AS4}
\]

In particular `c=2/3` is impossible.

Here and below, algebraic branches at a point include all branches
reachable by analytic continuation of the germ at zero. Finite
singularity sets and convergent Puiseux expansions are the standard
Newton--Puiseux inputs. A primary exposition read for this proof is
Flajolet--Sedgewick, INRIA Research Report 4103 (2001), Section 5.1,
Lemma 8.3 and Theorem 8.11, printed pages 59--62:
<https://algo.inria.fr/flajolet/Publications/FlSe01.pdf>.
The proof below uses the local expansions themselves, not an assertion
that leading coefficient asymptotics cannot cancel.

### 2.1 There must be a nonzero finite singularity

A polynomial satisfying (AS3) cannot have a positive-degree coefficient:
if `h_m!=0` at its largest positive index, then
`h_(2m)=c h_m!=0`, a contradiction. The remaining constant polynomial
is zero because `H(0)=0`. Thus `H` is not a polynomial.

Let `S` be the set of nonzero finite points at which at least one
analytic continuation of `H` has a pole or a genuinely ramified
Puiseux branch. It is finite by algebraicity.

If `S` were empty, the only possible finite obstruction would be at
zero. The original germ is holomorphic there, so continuation around
a small loop about zero fixes that germ. Such a loop generates the
fundamental group of `C*`; the germ therefore has a single-valued
continuation on `C*`, extends across zero, and is entire. An entire
algebraic function is a polynomial: the polynomial equation gives a
polynomial bound on its growth at infinity, and Cauchy's estimates
then kill all sufficiently high Taylor coefficients. This contradicts
the preceding paragraph. Hence `S` is nonempty.

### 2.2 The whole singularity set is permuted by squaring

The root-of-unity filter gives the germ identities

\[
U_2H(z)=\frac{H(\sqrt z)+H(-\sqrt z)}2,
\qquad H(z)+H(-z)=2cH(z^2).                         \tag{AS5}
\]

Away from zero, every continuation of the first expression can be
singular only at the square of a point in `S`. Each square root is a
local analytic coordinate, and both continued branches are holomorphic
if neither square root belongs to `S`. Since `U_2H=cH`, it follows that

\[
S\subseteq S^2:=\{s^2:s\in S\}.
\]

But `S` is finite and `|S^2|<=|S|`. Thus `S=S^2`, and squaring is a
permutation of `S`. In particular:

* every point of `S` is a root of unity of odd order;
* if `alpha in S`, then `-alpha` is not in `S`.

The second conclusion is the exact cancellation control needed below.
It was not assumed from a chosen dominant singularity.

### 2.3 Local singular coefficients cannot have the required scaling

Choose `alpha in S` and a singular continued branch at `alpha`.
Use the normalized coordinate `u=1-z/alpha`. Its convergent Puiseux
expansion has a first term

\[
B u^\rho\quad(B\ne0)
\]

whose exponent is outside `Z_{>=0}`. This means the first pole term,
if a pole is present, or the first fractional-power term otherwise.
Every earlier term is holomorphic and has an integer nonnegative
exponent. The exponent `rho` is rational.

Continue the second identity (AS5) along a path yielding this branch.
All branches of `H(-z)` are holomorphic at `alpha`, because
`-alpha` is not in `S`. Hence the continued branch of `H` at `alpha^2`
on the right is also singular, and its first nonholomorphic exponent
is the same `rho`. In the normalized coordinate there,

\[
1-z^2/\alpha^2=2u-u^2.
\]

If its coefficient is `B'`, comparison of the first nonholomorphic
term gives

\[
|B|=2c\,2^\rho |B'|.                              \tag{AS6}
\]

A possible change of determination of a Puiseux root multiplies the
coefficient by a root of unity, so it does not change (AS6).
Holomorphic terms never contribute to this comparison. Lower pole
terms are absent by the choice of the first nonholomorphic exponent.

Repeat this continuation step, following `alpha -> alpha^2 -> ...`.
The exponent `rho` remains fixed. There are only finitely many points
in `S` and finitely many algebraic Puiseux branches at each point, so
the possible positive magnitudes of the coefficient of `u^rho` form
a finite set. Equation (AS6) produces an infinite sequence in this
finite set with one fixed positive ratio. Two magnitudes repeat,
which forces

\[
2c\,2^\rho=1.
\]

This is (AS4). If `c=2/3`, it would say
`3=2^(rho+2)`. Writing `rho+2=p/q` with `q>0` and raising to the
`q`th power gives `3^q=2^p`. For `p<0`, clearing denominators makes
the impossibility immediate; for `p>=0`, unique prime factorization
does so. This proves Lemma AS-B.

## 3. Descent from a hypothetical algebraic series over Q_2

The complex lemma cannot simply be applied by claiming that the actual
`Q_2` coefficient sequence has a real embedding. The following finite
field-of-definition argument supplies precisely the needed bridge.

Suppose `G` were algebraic over `Q_2(z)`, and choose a nonzero
separable polynomial `P(z,Y)` with `P(z,G)=0`. Separability in
characteristic zero gives

\[
s=\operatorname{ord}_z P_Y(z,G)<\infty.
\]

Choose `N>=s` and truncate `G` through degree `N`, obtaining `T`.
Write `G=T+z^(N+1)J`. Let `K_0` be the field generated over `Q`
by the finitely many coefficients of `P` and `T`.

Expansion in the `Y` variable shows that

\[
Q(z,J):=z^{-(N+1+s)}P(z,T+z^{N+1}J)
\]

is a polynomial in `J` with coefficients in `K_0[z]`. Indeed,
`P(z,T)` has order at least `N+1+s`, the linear term has exactly
that order, and the terms of degree at least two have larger order.
Moreover

\[
Q(0,J)=b+dJ,\qquad d\ne0,
\]

so `J(0)=-b/d in K_0`. The formal implicit-function recursion now
places every coefficient of `J`, and hence of `G`, in `K_0`.

The finitely generated characteristic-zero field `K_0` embeds in `C`.
Apply such an embedding to all coefficients. It fixes the rational
constants in (AS2), preserves `G(0)=0` and `[z]G=3`, and produces an
algebraic complex formal power series. The same implicit-function
equation, or Newton--Puiseux, makes this series convergent near zero.
It would therefore violate Lemma AS-B with `c=2/3`.

Thus `G` is transcendental over `Q_2(z)`. Since
`F=G-1/(1-z)`, the same holds for `F`.

Finally, finite binomial inversion gives the formal identities

\[
F(z)=\frac1{1-z}A\!\left(\frac z{1-z}\right),\qquad
A(w)=\frac1{1+w}F\!\left(\frac w{1+w}\right).
\]

An algebraic `A` would make `F` algebraic by the first identity.
Therefore `A` is transcendental as asserted.

## 4. Rational and hypergeometric checks against primary literature

The rational special case has an elementary independent proof. An
eventually linearly recurrent sequence is eventually a finite sum
`sum P_lambda(n) lambda^n`. The identity `g_(2n)=(2/3)g_n` implies
that the nonzero characteristic roots are permuted by squaring: the
root set on the right must be contained in the image of the root set
on the left, and the finite cardinalities make squaring bijective.
Thus, for a suitable positive `L`, every root satisfies
`lambda^(2^L)=lambda`. Comparing a nonzero leading polynomial
coefficient of degree `d>=0` in
`g_(2^L n)=(2/3)^L g_n` gives

\[
2^{Ld}=(2/3)^L,
\]

which is impossible. An eventually zero sequence is excluded by
`g_(2^k)=3(2/3)^k!=0`.

This rational mechanism is consistent with the existing Hecke-operator
spectrum work of Gil--Robins, *Hecke operators on rational functions I*,
Forum Mathematicum 17(4) (2005), 519--554; author manuscript:
<https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/RobinsSinai.pdf>.
No novelty is claimed for that rational-spectrum mechanism.

There is a separate published exclusion of a hypergeometric ansatz.
Moll--Robins--Soodhalter, *The action of Hecke operators on
hypergeometric functions*, J. Aust. Math. Soc. 89 (2010), 51--74,
Theorems 6.13--6.16, compute the nonzero spectrum on their specified
hypergeometric class as integer powers of the section base:
<https://www.math.tulane.edu/~vhm/papers_html/official.pdf>.
Since `[z]G=3`, the normalized series `G/3` would be in their
order-one-at-zero case; its eigenvalue `2/3` is not an integer power
of two. This excludes a single hypergeometric coefficient formula in
that class. It is not a theorem about every holonomic series or every
sum of hypergeometric sequences.

## 5. Why simultaneous Mahler rigidity points in the wrong direction here

For `S_(b,r)F=sum f(bn+r)z^n`, (AS1) gives only

\[
S_{2,0}F=\frac23F-\frac1{3(1-z)},\qquad
S_{2,1}F=2S_{3,2}F,
\]

or equivalently

\[
F(z)=\frac23F(z^2)-\frac1{3(1-z^2)}
       +2z(S_{3,2}F)(z^2).                           \tag{AS7}
\]

This is one mixed section identity with an uncontrolled third-section
function. It does not give finite independent 2- and 3-Mahler systems.

Adamczewski--Bell, *A problem about Mahler functions*, Ann. Sc. Norm.
Super. Pisa Cl. Sci. (5) 17 (2017), 1301--1355, Definition 1.1 and
Theorem 1.3, apply over every characteristic-zero field:
<https://journals.sns.it/index.php/annaliscienze/article/download/574/560>.
Their conclusion would make a series satisfying both systems rational.
Theorem AS-A therefore proves that `F`, `G`, and `A` cannot satisfy
both a 2- and a 3-Mahler equation of their stated kind. No hidden
finite system of that kind can close this exact whole-sequence ansatz.

The 2026 Adamczewski--Faverjon extension was also checked at its primary
manuscript, Theorems 1.1, 3.3 and 3.8:
<https://faverjon.perso.math.cnrs.fr/AdamczewskiFaverjon_MahlerFiniteAutomata.pdf>.
It studies values of already supplied finite linear Mahler systems with
the stated algebraic-coefficient, regularity and admissibility inputs.
It does not generate such a system from (AS7), and it does not assert
that arbitrary `Q_2` coefficients are algebraic numbers.

The finite Newton expansion of a continuous 2-adic function is called a
Mahler expansion in a different sense. The name does not supply a
Mahler functional equation for the ordinary generating series.

## 6. Exact remaining construction boundary

This theorem is compatible with **every** value `f(n)` being in
`Z[1/3]`: a series with rational or triadic coefficients can be
transcendental as a function. It does not supply even one previously
unproved successful candidate.

The useful conclusion is methodological and exact. A global algebraic
generating-function construction, a simultaneous 2/3 Mahler
rationalization of this series, or a single hypergeometric formula in
the quoted class is impossible already on the known even branch.
An all-source construction must preserve enough nonalgebraic
sequence-level complexity to coexist with (AS2), while proving
pointwise triadic arithmetic by another argument.

The first open arithmetic step remains to construct, for each fixed
positive ordinary `n`, a finite triadic value which is exactly
`Omega(n)`. This document does not replace that existence theorem by
finite prefix compatibility, a growing coefficient cutoff, a rational
generating-function claim, or a complex value theorem lacking its
required system.
