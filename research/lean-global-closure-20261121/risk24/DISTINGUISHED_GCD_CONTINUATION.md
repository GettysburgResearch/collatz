# Continuing from the superpolynomial denominator to the integer fiber

Date: 2026-11-23. **Status: a direct unrestricted-cycle attack with an
unclosed arithmetic step.** The proved outcome of this pass is the
companion all-word degree theorem; this note records the precise
Diophantine continuation attempted, its valid identities, and its first
unproved estimate. It does not turn a large residual polynomial
denominator into a lower bound for the reduced rational denominator.

## 1. The stronger target supplied by the degree theorem

Keep the full notation of `SUPERPOLYNOMIAL_RESIDUAL_DENOMINATOR.md`:

\[
 D=2^A-3^p>0,\quad C=Q(3),\quad
 F=X^p-2^A,\quad G=\gcd(F,Q),\quad F_0=F/G,\quad Q_0=Q/G.
\]

The complete integral-cycle condition is

\[
 D\mid C
 \quad\Longleftrightarrow\quad
 D_{\rm pol}:=|F_0(3)|\mid Q_0(3).
 \tag{1}
\]

The new degree bound and the explicitly source-qualified PR185 factor
gap give

\[
 \log D_{\rm pol}>
 \log(3/2)\left(
 \frac{(\log p)^2}{72\log(2\log p)}-1\right)
 \qquad(p\ge10).
 \tag{2}
\]

Consequently an integer cycle needs a gcd larger than every fixed power
of \(p\), even after all common polynomial factors are removed. When
the word is rotated to its minimum, its integer quotient \(m=C/D\)
satisfies \(\log m=O(\log p)\) by the inherited two-logarithm
estimate. This puts the quotient height and required gcd on genuinely
different scales. It was the reason to attempt a height/gcd theorem at
the distinguished fiber again.

The needed assertion remains

\[
 \sum_{\ell\mid D_{\rm pol}}
 \min\{v_\ell(F_0(3)),v_\ell(Q_0(3))\}\log\ell
 <\log D_{\rm pol}.
 \tag{3}
\]

Every valuation here is at the same ordinary evaluation \(X=3\). A
resultant estimate that collects roots at different conjugates would
not imply (3).

## 2. The heavy theorem and three exact representations

The primary statement checked was Grieve--Wang, *Greatest common divisors
with moving targets and consequences for linear recurrence sequences*,
arXiv:1902.09109v2, Theorem 1.2:
<https://arxiv.org/pdf/1902.09109>.
Its moving-polynomial gcd theorem keeps the torus dimension and the
polynomial degrees fixed, assumes coprime moving polynomials, and
requires slow coefficient-height growth relative to the moving
S-unit arguments. Its alternatives also include algebraic-subgroup
degeneracy; it is not a blanket bound on every moving point.

Three ways of representing the actual cycle equation were tried.

**Retain the actual residual polynomials.** The pair \(F_0,Q_0\) is
coprime in \(\mathbb Q[X]\), and its evaluations preserve (1) exactly.
But the evaluation point is the fixed integer three, of constant height,
whereas \(\deg F_0=n\to\infty\) by the new degree theorem. This is
not the moving-point, fixed-degree setting of that result.

**Make every word monomial a separate S-unit argument.** One can write

\[
 C=\sum_{i<p}2^{d_i}3^{p-1-i},\qquad D=2^A-3^p
\]

as evaluations of linear forms with small fixed coefficients. This
removes the changing polynomial degree, but now the number of arguments
grows with \(p\). The fact that each scalar monomial uses only the
primes two and three does not make the dimension of this coordinate
space fixed. The cited theorem has no conclusion uniform in that
changing dimension.

**Exploit the small integer quotient.** Under the very integrality
assumption to be contradicted, set

\[
 u=2^A3^{-p},\qquad
 f(X)=X-1,\qquad k(X)=m(X-1).
\]

Then

\[
 f(u)=D/3^p,\qquad k(u)=C/3^p.
 \tag{4}
\]

The ordinary coefficient size of \(m\) is only polynomial in \(p\),
while \(h_{\mathrm W}(u)=\max(A\log2,p\log3)=A\log2\) for the usual
logarithmic Weil height of the S-unit \(u\). Thus the scale comparison
looks favorable.
However, the two *polynomials* in (4) share the entire factor \(X-1\).
The required coprimality has disappeared. Dividing that common factor
out leaves the constants one and \(m\), and removes exactly the
denominator whose divisibility had to be tested.

The last representation is particularly important to keep explicit:
an integer quotient with small height is compatible with arbitrarily
large gcd. It cannot be fed into a coprime-polynomial theorem after
replacing the actual parity numerator by \(mD\). Polynomial coprimality
of the original \(F_0,Q_0\) does not transfer through this change of
representation.

No valid interpolation between these three representations was obtained.
In particular, this pass did **not** derive
\(\log\gcd(D_{\rm pol},Q_0(3))=O(\log p)\) or any fixed fraction
of \(\log D_{\rm pol}\).

## 3. A precise limit on universal bounded-size compression

There is also an elementary counting obstruction to one especially
tempting repair. It concerns a specified class of literal arithmetic
encodings, not every possible use of the Subspace Theorem.

Fix positive constants \(c\) and integers \(r,d\). Suppose that every
canonical numerator \(C\), at each length \(A\), could be represented
by a rational expression in at most \(r\) arguments

\[
 u_j=2^{s_j}3^{t_j},\qquad |s_j|,|t_j|\le cA,
\]

whose numerator and denominator have total degree at most \(d\), and
whose rational coefficients all have numerator and denominator bounded
by \(\exp(H_A)\), where \(H_A=o(A)\). All scalar prefactors must be
charged to this same coefficient-size budget. Then the number of
possible evaluated expressions is \(\exp(o(A))\): the argument choices
are only \(O(A)^{2r}\), there are a fixed number
\(\binom{r+d}{d}\) of coefficient slots per polynomial, and each slot
has \(\exp(O(H_A))\) choices.

In contrast, even primitive words in the positive cone supply
exponentially many distinct canonical numerators. Here is a direct
proof avoiding a genericity assumption.

First, for fixed \(A,p\), the map

\[
 w\longmapsto C_w\pmod{2^A}
 \tag{5}
\]

is injective. The denominator \(D\) is fixed and odd. The rational
fixed point \(C_w/D\in\mathbb Z_2\) has precisely the parity word
\(w\): its first parity is the parity of \(C_w\), and one-letter
rotation gives

\[
 2C_{\rm rot}=C_w\quad(w_0=0),\qquad
 2C_{\rm rot}=3C_w+D\quad(w_0=1).
\]

If two numerators agree modulo \(2^A\), their first parities agree;
the rotated numerators then agree modulo \(2^{A-1}\). Repeating this
argument recovers all \(A\) letters and proves (5).

Take prime lengths \(A\) and \(p=\lfloor3A/5\rfloor\). For all
sufficiently large such lengths the words are nonconstant, hence
primitive, and

\[
 3^p\le3^{3A/5}<2^A
\]

because \(3^3<2^5\). There are \(\binom Ap\) distinct values in
(5). With \(k=\min(p,A-p)\), choose one element from each of \(k\)
disjoint pairs to see

\[
 \binom Ap=\binom Ak\ge\binom{2k}{k}\ge2^k=\exp(\Omega(A)).
\]

This contradicts the proposed \(\exp(o(A))\) universal encoding count.
Thus one cannot compress **every** such primitive positive word into
this bounded-dimension, bounded-degree, small-coefficient class at
argument height \(O(A)\).

The limitation is exact. It does not exclude a future theorem proving
that the much smaller set of *integral* words admits an additional
structural compression. The attempted small-quotient compression in
(4) does describe those words, but loses polynomial coprimality. A new
argument would have to retain both the ordinary word and the relevant
coprimality at once.

## 4. The carry clock also preserves one arithmetic class

PR177 at `6de3e304bb49a93a6c5ef0e5563137e75c7defb4`,
`research/lean-exact-witness-global-20261121/HIGH_VARIANCE_ARITHMETIC.md`,
Section 5, supplies the exact carry dynamics for the odd-gap word:

\[
 (L_av)_i=2^{a_i}v_{i+1}-3v_i,\qquad
 2c^{(t+1)}=c^{(t)}-L_ab^{(t)},\qquad c^{(0)}=\mathbf1.
 \tag{6}
\]

In the full finite group \(\Gamma=\mathbb Z^p/L_a\mathbb Z^p\),
whose order is \(D\), multiplication by two is an automorphism because
\(D\) is odd. Therefore

\[
 \boxed{[c^{(t)}]=2^{-t}[\mathbf1]\quad\text{in }\Gamma.}
 \tag{7}
\]

This identity retains every prime power of the original denominator.
It also identifies what repeated carry steps alone cannot add: their
classes are unit multiples of the same initial class. An invariant box
for the actual integer representatives can still contain useful
additional information, but a sequence of group congruences from (7)
is not a collection of independent vanishing conditions. This is the
carry-clock counterpart of the exact unit relation among cyclic
rotations in PR185's polynomial algebra.

## 5. Frontier retained

The new all-word result forces a superpolynomial residual denominator.
The direct gcd continuation checked moving-target Diophantine estimates,
proved the explicit encoding obstruction above, and retained the full
carry-group relation. None proves the strict distinguished-fiber
inequality (3). That inequality, or an actual ordinary-orbit argument
that forces a coprime low-height representation without discarding the
word, is still needed for unrestricted positive-cycle exclusion.

The primary older gcd source checked for comparison was Corvaja--Zannier,
*A lower bound for the height of a rational function at S-unit points*,
Theorem 1 and the Main Theorem,
<https://arxiv.org/pdf/math/0311030>. Those results also retain fixed
rational functions and exceptional subtori; they do not justify a
degree-uniform conclusion for the growing residual polynomials here.
The primary statements were inspected. No inaccessible theorem or
unproved variable-dimension strengthening is used in this note.
