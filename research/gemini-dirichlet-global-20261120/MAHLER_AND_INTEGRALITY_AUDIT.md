# Mixed Mahler equation and global integrality: exact audit

**Status: proved repairs and counterexamples; no Collatz closure.**
This note audits v2 Blueprints 1 and 4 and the separate bundle's Route 3.
It supplies a complete all-period proof missing from Blueprint 1, identifies
exactly what its analytic identities assert, and corrects two proposed
integrality tests. The proof below is self-contained except where an
external theorem is expressly named. Its rationality conclusion is
consistent with established Bell–Lagarias theory; no novelty claim is made.

## 1. The mixed equation is exactly component invariance

Let

\[
F(z)=\sum_{n\ge1}f(n)z^n,\qquad \omega=e^{2\pi i/3},
\]

with bounded complex coefficients. The equation under audit is

\[
\frac13\sum_{j=0}^2\omega^jF(\omega^jw^2)
 =w\bigl(F(w^3)-F(w^6)\bigr).                 \tag{M}
\]

It is equivalent, coefficient by coefficient, to

\[
f(2m)=f(m)\quad(m\ge1),\qquad
f(3k+2)=f(2k+1)\quad(k\ge0).                 \tag{1}
\]

Indeed, the left side retains precisely the terms with index
\(n\equiv2\pmod3\). At exponent \(6m+1\), its coefficient is zero,
whereas the right coefficient is \(f(2m)-f(m)\). At exponent
\(6k+4\), the coefficients are \(f(3k+2)\) and \(f(2k+1)\).
All other coefficients vanish. This argument is valid for formal power
series and therefore needs no boundary regularity.

The second equality in (1), together with the first, is equivalent to
\(f(3n+1)=f(n)\) for odd positive \(n\). Thus (M) says precisely that
\(f\) is constant on every component of the ordinary shortcut Collatz
graph. The Boolean condition and \(f(1)=0\) do not change this equivalence.
Existence of a nonzero such Boolean solution is equivalent to existence
of an ordinary source outside the basin of 1.

## 2. Complete rational-solution classification

**Theorem.** Suppose \(f\) takes values in a finite subset of
\(\mathbb C\), satisfies (1), and \(F\) is rational. Then \(f\) is
constant. In the Boolean case the only rational solutions are
\(0\) and \(z/(1-z)\). If also \(f(1)=0\), only zero remains.

**Proof.** Rationality gives a fixed linear recurrence for all sufficiently
large coefficient indices. Its next coefficient is determined by a fixed
finite tuple of preceding coefficients. There are only finitely many such
tuples because the coefficient alphabet is finite. A repeated tuple
therefore gives an eventual period \(P\). A polynomial series is handled
by the same argument, taking eventual period 1.

Write \(P=2^aP'\) with \(P'\) odd. If positive \(n,m\) satisfy
\(n\equiv m\pmod{P'}\), choose \(r\ge a\) so that both
\(2^rn\) and \(2^rm\) exceed the eventual-period threshold. These
numbers are congruent modulo \(P\), so

\[
f(n)=f(2^rn)=f(2^rm)=f(m).
\]

Hence \(f\) is globally periodic with odd period \(P'\). Denote its
residue function by \(h\). Every residue modulo \(P'\) has a positive
odd lift. Consequently, on all residue classes,

\[
h(2x)=h(x),\qquad h(3x+1)=h(x).               \tag{2}
\]

Write \(P'=3^sM\), where \(\gcd(M,6)=1\), and put \(g(x)=3x+1\).
Its \(s\)-fold iterate is

\[
g^s(x)=3^sx+(3^s-1)/2.
\]

If \(x\equiv y\pmod M\), then \(g^s(x)\equiv g^s(y)\pmod{P'}\).
Applying (2) \(s\) times gives \(h(x)=h(y)\). Thus \(h\) factors
through residues modulo \(M\), where both relations (2) still hold.
On this quotient,

\[
h(6x+1)=h(g(2x))=h(x)=h(2g(x))=h(6x+2).
\]

Because 6 is invertible modulo \(M\), this is \(h(t)=h(t+1)\) for
every residue \(t\). Therefore \(h\), and hence \(f\), is constant.
This includes \(M=1\). QED.

This argument covers every eventual period, including powers of 2 and 3.
The submitted union-find calculation for odd periods at most 99 verifies
examples; it does not by itself establish the theorem.

### Natural-boundary consequence and its exact limit

If a nonzero Boolean solution has \(f(1)=0\), doubling a supported index
gives infinitely many supported indices. Its radius of convergence is
therefore exactly 1. By the Pólya–Carlson theorem and the classification
above, the entire unit circle is a natural boundary.

Equivalently, analytic continuation through even one boundary arc would
force zero. No such continuation has been established. A natural boundary
is entirely compatible with analyticity in the open unit disk.

For the actual basin indicator, this issue is already present in
Bell–Lagarias, *3x+1 inverse orbit generating functions almost always have
natural boundaries*, Theorem 1.2: the generating function for the inverse
basin of 1 is rational when Collatz holds and has the unit circle as a
natural boundary if it fails. The complement series differs from it by
\(z/(1-z)\). This is established prior theory, not a new resolution.

## 3. Boolean Parseval supplies no additional inequality here

For Boolean coefficients, Parseval gives

\[
\frac1{2\pi}\int_0^{2\pi}|F(re^{i\theta})|^2\,d\theta=F(r^2).
                                                               \tag{3}
\]

This is true for every Boolean series, with no Collatz hypothesis. Put

\[
F_2(z)=\sum_{\substack{n\ge1\\n\equiv2\ (3)}}f(n)z^n.
\]

Taking squared angular norms in (M), and using (1), yields precisely

\[
F_2(\rho^4)
 =\rho^2\bigl(F(\rho^6)-F(\rho^{12})\bigr).       \tag{4}
\]

But (4) is (M) evaluated at the positive real number \(w=\rho^2\).
Thus the proposed norm calculation gives the same coefficient identity
after Boolean squaring. Its use has not created a strict contraction,
an angular decorrelation estimate, or a continuation theorem. The
blueprint's displayed \(F^{(2\bmod3)}(\rho^{12})\) is not correct with
the ordinary multisection convention just defined.

Several proposed next steps need additional hypotheses:

* The assignment \(\phi\mapsto(3/2)\phi\pmod{2\pi}\) is not a
  well-defined map on the circle: changing a representative by \(2\pi\)
  changes its proposed image by \(3\pi\). If interpreted instead as a
  beta transformation on representatives in \([0,1)\), the rational
  point \(2/3\) goes to 0. Thus the assertion that every rational angle
  has a dense orbit is false in that interpretation as well.
* The weighted multisection on the left of (M) can cancel complex values.
  An individual large value of one summand has not been shown to force
  a comparable value of the sum. A spike-propagation lower bound cannot
  be inferred from equality of the sums alone.
* A Dirichlet abscissa or a power growth bound does not, by itself, give
  an asymptotic \(F(r)\sim C(1-r)^{-\sigma}\). Such a conclusion needs
  additional regularity. A forward no-descent counting estimate also
  cannot be applied to the full exceptional basin without a transfer
  argument; these are different sets.

### Why the known Mahler rationality theorem does not close this

Adamczewski–Bell prove rationality for a characteristic-zero series that
satisfies separate finite-order Mahler equations in two multiplicatively
independent integer bases. For bases 2 and 3, one sufficient form is

\[
\sum_{i=0}^{d}p_i(z)F(z^{2^i})=0,
\qquad
\sum_{j=0}^{e}q_j(z)F(z^{3^j})=0,
\]

with rational-function coefficients, each equation nontrivial. Equation
(M) is a mixed equation with a projection and does not provide those two
equations. The relation
\(F(z)+F(-z)=2F(z^2)\) controls the even section but leaves the odd
section as another function. Iterating section operators has not been
proved to produce a finite-dimensional family. Supplying that missing
finite closure, or genuine boundary regularity, would be substantive new
work. It is absent from the submitted blueprint and from this audit.

## 4. Positivity does not replace the ordinary all-word supremum

Use PR149's domain: positive odd integers prime to 3, with every inverse
letter \(I_a(x)=(2^ax-1)/3\), \(a\ge1\), required to be ternary-unit
legal. If \(x\) is a positive integer and the letter is legal, its
numerator is a positive integer divisible by 3. Thus its image is a
positive integer; it is odd, and unit legality keeps it prime to 3.
Induction proves that every legal inverse word from an ordinary positive
root is already positive at every intermediate state. Therefore

\[
W_{\rm pos}(n)=W(n)
\quad\text{for every positive odd }n\text{ with }3\nmid n.       \tag{5}
\]

In particular, imposing positivity at 1 is not a new repair of PR149's
all-word problem.

The bound used by Blueprint 4 is nevertheless valid for a nonempty word:
write the reversed word in forward order, let \(A\) be its total gap
cost, and let \(a_i\) be its prefix costs, with \(a_0=0\). Then

\[
2^Az=3^ky+C_w,\qquad
C_w=\sum_{i=0}^{k-1}3^{k-1-i}2^{a_i}\ge3^{k-1}.
\]

Since \(y\ge1\), one obtains exactly the stated ceiling

\[
8k-5A\le(8-5\log_2 3)k+5\log_2z-5\log_2(4/3).
\]

The coefficient of \(k\) is positive. This ceiling does not bound the
supremum as \(k\) grows. Word orientation matters when writing the
prefix costs, but not for this lower bound on \(C_w\).

PR149's `CLOSURE_BOUNDARY.md` proves that its global closing estimates
are equivalent to **Collatz together with \(W(1)<\infty\)**. It does
not prove \(W(1)<\infty\) equivalent to Collatz alone. Also \(W\) is
defined on ternary units, not on a dyadic ambient domain as Route 3 says.

## 5. The two proposed adelic tests are false as written

Use the standard normalization \(|r|_p=p^{-v_p(r)}\). Write a positive
rational \(r=u/v\) in lowest terms and suppose \(\gcd(v,6)=1\).
The correct outside-prime denominator height is

\[
H_{\rm den}(r)=\sum_{p\ge5}\max(0,\log_2|r|_p)=\log_2v.       \tag{6}
\]

Blueprint 4 puts a minus sign inside the maximum. Its formula counts
the prime factors of the numerator outside 2 and 3. For example it gives
\(\log_2 5\) at the integer 5 and zero at \(1/5\), the opposite of
the proposed denominator test. The supplied verifier calculates
`log2(r.denominator)` directly; it never evaluates the signed formula.

Route 3 instead proposes the criterion
\(\prod_{p\ge5}|r|_p\le1\). This loses the separate inequalities at
the different primes. The exact shortcut parity word `11111000` has
positive periodic root

\[
r=\frac{3^5-2^5}{2^8-3^5}=\frac{211}{13}.
\]

Its successive states have numerators
\(211,323,491,743,1121,1688,844,422\), all over 13. They return to
\(211/13\) with exactly the displayed parity word, yet

\[
\prod_{p\ge5}|r|_p=13/211<1,\qquad r\notin\mathbb Z.
\]

There is even an example with strictly positive inverse loop score.
The blueprint's gap word consisting of ten 2's followed by seven 1's
has root \(60888923/71515\), total cost \(A=27\), and \(k=17\).
It has \(8k-5A=1\) and the same false product test is passed, since
\(71515/60888923<1\). Exact replay verifies all gaps and ternary units.

The correct integrality criterion is \(|r|_p\le1\) **separately** at
every outside prime, or equivalently \(H_{\rm den}(r)=0\). For a cycle
root \(C/D\), this is precisely the full condition \(D\mid C\).
It is not supplied by the product inequality above.

Reduced-denominator conservation and the consequences for a fixed finite
denominator penalty are treated separately in `DENOMINATOR_SECTORS.md`.
No claim is made that all adelic approaches are impossible.

## 6. What is still missing from the S-unit and CUBE-4 proposals

The expansion \(2^A=3^ky+C_w\) has an unbounded number of summands as
\(k\) varies. Moreover, an arbitrary positive integer \(y\) can have
prime factors outside \(\{2,3\}\), so \(3^ky\) is not an S-unit for
that fixed set. A fixed-dimensional S-unit or Subspace theorem cannot
be applied uniformly merely by naming this expansion. A successful
application must control dimension, coefficient heights, and any
outside-prime multipliers, and then establish the required smallness.

Likewise, a lower bound for the greatest prime factor of the unreduced
\(D=2^A-3^k\) does not control the reduced denominator
\(D/\gcd(C,D)\). Repeating a word \(t\) times multiplies both \(C\)
and \(D\) by

\[
\sum_{j=0}^{t-1}(2^A)^{t-1-j}(3^k)^j,
\]

and leaves its reduced root fixed while the unreduced denominator grows.
This refutes that inference from the raw denominator alone. It does not
refute a separately proved theorem for a specified primitive family;
such a theorem would need cancellation control that is not supplied here.

The latest inspected PR148 source is
`55d8968d2ecbc23a91c9c4733929f34be9bf0d28`,
`research/independent-attack-20261120/PROOF.md` and `README.md`.
Its CUBE-4 statement concerns complete covers of one primitive tour by
four nonempty powers, each exponent at least two, with the minimum in an
exponent-three factor. It is source-qualified and ineffective. It does
not say every four-block cycle is covered, and it does not prove the
finite set empty.

Its actual Subspace comparison uses two or three coordinates and charges
the positive ordinary multipliers through an outside-prime factor
\(M^kN\). The proposed replacement by bounds for
\(v_2(3^u-1)\) and \(v_3(2^v-1)\) supplies no reduction of the
variable-multiplier comparison to either of those two expressions.
For example, a square displacement is \(M(3^q+2^w)\), where the
integer \(M\) is unrestricted apart from the established height bounds.
Removing it, or treating it as a fixed coefficient, is not justified.
Powered-word factor count is also not interchangeable with the number
of local minima in an ordinary `m`-cycle result. No effective universal
period ceiling or final finite exclusion follows from the submitted code.

## 7. Sources and verification scope

Primary external sources inspected:

* Bell and Lagarias, [arXiv:1408.6884](https://arxiv.org/abs/1408.6884),
  published *Acta Arithmetica* 170 (2015), 101–120. Theorem 1.2 gives
  the basin rationality/natural-boundary alternative; Theorem 2.2 states
  the Pólya–Carlson input.
* Adamczewski and Bell, [arXiv:1303.2019](https://arxiv.org/abs/1303.2019),
  *A problem around Mahler functions*. Its theorem requires separate
  Mahler equations in multiplicatively independent bases.
* Evertse, [The p-adic Subspace Theorem, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf),
  for the fixed forms/dimension and projective smallness framework cited
  by PR148. No independent reproof of that analytic theorem is claimed.

PR149's logical boundary was read at frozen source
`92c0129e794dde3ec55ceec470a12d51ba3f7e2f`,
`research/forward-inverse-defect/CLOSURE_BOUNDARY.md`.

Run `python -B check_mahler_and_integrality.py` or the same command with
`-O`. The checker uses exact integers and fractions, exercises the two
coefficient families of (M), checks representative moduli including large
3-powers, verifies both rational-cycle counterexamples, verifies the
height sign, and replays legal positive inverse letters. These are finite
checks of the written arguments and counterexamples; they do not verify
analytic continuation, uniform S-unit estimates, or Collatz convergence.
