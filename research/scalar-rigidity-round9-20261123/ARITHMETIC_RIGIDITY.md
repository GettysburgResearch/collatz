# Redundant digits, algebraic coordinates, and actual scalar approximation

23 November 2026. Published parent:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Status: PROPOSED elementary written results, with finite arithmetic
controls. Collatz remains OPEN.**

The direct arithmetic attack did not prove rationality or periodicity
of the actual scalar. It did identify an exact reason that two tempting
literature arguments do not close: positive bounded gap digits can be
nonperiodic and automatic while their discounted sum is rational; and
the proposed algebraic coordinate adds a multiplicative identity already
present in the scalar recurrence. The positive result is an explicit
actual-source approximation theorem in every prescribed odd congruence
class, with a linear bound on source bit length.

Use the actual odd map `2^(g_i)q_(i+1)=3q_i+1`, and retain R8-G1 from
`research/repo-synthesis-round8-20261123/GERM_BRIDGE.md`, blob
`540110f09cf68e3309fd83fea9c7ae497536ded4`:

\[
h(q)=\sum_{i\ge0}g_i/3^{i+1},\qquad
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g(q).
\tag{1}
\]

No eventual convergence of q is assumed in the constructions below.

## 1. The precise rational carry freedom

**R9-A1.** Suppose an actual rational scalar has had its powers of three
cleared, so its reduced denominator d is prime to three. Let p_i be the
unique representative of its fractional phase in `(1/2,3/2]`. The p_i
are periodic under tripling of fractional parts. Define

\[
k_i=h(q_i)-p_i\in\mathbb Z_{\ge0},\qquad
b_i=3p_i-p_{i+1}\in\{1,2,3\}.
\]

Then the complete gap equation is

\[
\boxed{g_i=b_i+3k_i-k_{i+1}\ge1.}
\tag{2}
\]

Conversely, any periodic phase sequence p_i as above and any
nonnegative integer sequence k_i with `k_N/3^N -> 0` satisfying
(2) define positive integer gaps with

\[
\sum_{i\ge0}g_i/3^{i+1}=p_0+k_0.
\tag{3}
\]

The growth condition is exactly what is needed for the displayed
telescoping; no ordinary realization is asserted in this converse. For actual sources, (1) and `q_i<=2^i q_0` give
`k_i=O(i+1)`, so the condition is automatic.

Indeed the finite identity is

\[
\sum_{i<N}\frac{g_i}{3^{i+1}}
=p_0+k_0-\frac{p_N+k_N}{3^N}.
\tag{4}
\]

In generating-series notation, with `G(z)=sum g_i z^i`,
`B(z)=sum b_i z^i`, and `K(z)=sum k_i z^i`, this is the exact normal
form

\[
\boxed{z(G(z)-B(z))=(3z-1)K(z)+k_0.}
\tag{5}
\]

In the general symbolic converse, (5) is an identity of formal power
series. The condition `k_N/3^N -> 0` funds the finite telescoping limit
in (4); it need not make `K(1/3)` converge. For actual sources,
`k_N=O(N)`, so all three series converge at 1/3 and evaluation of
(5) is justified.

The rational value at z=1/3 does not remove K. It annihilates its
coefficient in (5). Periodicity of normalized ternary digits therefore
cannot be substituted for periodicity of the raw gaps or the carries.

## 2. A nonperiodic automatic gap sequence with scalar 7/8

**R9-A2.** Let `(s_j)` be any binary sequence. Define two positive gaps
per symbol by

\[
g_{2j}=2-s_j,\qquad g_{2j+1}=1+3s_j.
\tag{6}
\]

Every gap belongs to `{1,2,4}`. Each two-step contribution is exactly

\[
(2-s_j)/3+(1+3s_j)/9=7/9.
\]

Consequently the infinite discounted scalar is exactly 7/8,
independently of the entire binary sequence. The candidate scalar
states are `7/8` at every block boundary and `5/8+s_j` at the
intermediate states. This is (2) with boundary carry zero and
intermediate carry s_j.

For a completely explicit nonperiodic automatic example, let s_j be
one precisely when j is a positive power of two. A finite binary-digit
automaton recognizes that set. Its infinitely many ones have unbounded
gaps, so it is not eventually periodic. Formula (6) can be computed by
a finite automaton as well: retain the parity of the index and whether
its quotient by two is a positive power of two. Eventual periodicity
of the gap sequence would make its even subsequence, and hence s_j,
eventually periodic, a contradiction.

This is a symbolic counterexample to a rational-discounted-sum
periodicity claim, even with positive bounded automatic gaps. It is
not a positive ordinary infinite Collatz trajectory. The next section
supplies literal ordinary realizations of every finite prefix, while
retaining precisely that distinction.

## 3. Exact ordinary cylinders with a prescribed odd congruence

**R9-A3 (finite realization).** Let `g_0,...,g_(N-1)` be any positive
integer gaps, N>=1, and put

\[
A_j=\sum_{i<j}g_i,\qquad
C_N=\sum_{j<N}3^{N-1-j}2^{A_j}.
\]

They are the actual first N odd gaps of a positive odd source q if
and only if

\[
\boxed{3^Nq+C_N\equiv2^{A_N}\pmod{2^{A_N+1}}.}
\tag{7}
\]

Thus there is exactly one odd residue class for this whole word. The
final odd quotient, not merely divisibility by `2^(A_N)`, is retained.

For completeness, split the carry at an internal k<N:

\[
C_N=3^{N-k}C_k+2^{A_k}C_{\rm suffix}.
\]

The suffix carry is odd. Reducing (7) modulo `2^(A_k+1)` therefore
gives `3^kq+C_k=2^(A_k) mod 2^(A_k+1)`. All the intermediate
quotients `(3^kq+C_k)/2^(A_k)` are positive odd integers. Their
successive numerator equations certify exactly the proposed gaps.
The final quotient is odd directly from (7). Necessity follows from
the complete ordinary affine identity.

Fix any positive odd modulus M and any residue a modulo M. The Chinese
remainder theorem combines (7) with `q=a mod M`. Choose the unique
representative in

\[
\boxed{0<q<M2^{A_N+1}.}
\tag{8}
\]

It exists because the combined binary class is odd, so its representative
cannot be zero. This is one positive ordinary source for the supplied
finite word and congruence, not a coherent source for all word lengths.

There is also a useful bound on its actual endpoint v. Since every
suffix has at least its number of gaps,

\[
\frac{C_N}{2^{A_N}}
\le\sum_{j<N}\frac{3^{N-1-j}}{2^{N-j}}
=(3/2)^N-1.
\]

Using (8) in the complete physical identity yields

\[
\boxed{v<(2M+1)3^N.}
\tag{9}
\]

The endpoint bound does not grow with the sizes of the supplied gaps.
It is paid for by the source modulus in (8).

For every finite word in (6), this constructs a literal positive
ordinary realization in every odd congruence class. Its binary clock
is `3n+2 sum_(j<n)s_j` for n blocks. Thus its bit length is at most
`5n+bl(M)+1`, or `3n+2 sum s_j+bl(M)+1` with the carries retained.
The actual scalar differs from 7/8 by less than

\[
\boxed{\frac{32n+8\operatorname{bl}(M)+11}{24\cdot9^n}.}
\tag{10}
\]

To verify (10), the exact scalar remainder is
`9^(-n)(h(v)-7/8)`. Apply (1) and (9) with N=2n, using
`2M+1<2^(bl(M)+1)` and `3<4`. This bounds the actual scalar of
each finite ordinary realization, without declaring it equal to the
symbolic target.

## 4. Quantitative actual density in every odd residue class

**R9-A4.** Fix a real x>=1/2, a positive odd modulus M, and any residue
a modulo M. Put `k=floor(x-1/2)` and `B=bl(M)`. For every N>=1 there
is a positive odd source q, congruent to a modulo M, such that

\[
\boxed{\operatorname{bl}(q)\le3N+3k+B+1,\qquad
|h(q)-x|<\frac{4N+2B+5}{6\cdot3^N}.}
\tag{11}
\]

**Proof.** Write `x-1/2=k+z`, with `0<=z<1`, and choose the ternary
expansion `z=sum d_i/3^(i+1)`, digits `d_i in {0,1,2}`. Take
`g_0=1+3k+d_0` and `g_i=1+d_i` for i>=1. Their infinite discounted
sum is x. Every first-N total gap satisfies `A_N<=3N+3k`. Apply
R9-A3 to this finite word and the specified odd congruence. Equation
(8) gives the source bit-length bound.

After N digits, the chosen symbolic scalar tail x_N is in `[1/2,3/2]`.
The actual scalar tail is h(v), and (9) gives

\[
\frac12<h(v)<\frac{2N+B+4}{3}.
\]

Since the last upper bound minus one half is at least one,

\[
|h(v)-x_N|<\frac{4N+2B+5}{6}.
\]

The finite scalar identity multiplies this discrepancy by `3^(-N)`,
proving (11). For a rational supplied target, all digits and all source
congruences are computed by integer arithmetic. For an arbitrary real
target the construction uses its supplied finite digit prefix.

It follows that the closure of the actual scalar values in every
fixed odd congruence class is exactly `[1/2,infinity)`. Finite odd
congruence restrictions cannot supply an open interval excluding a
rational phase. This does not decide exact membership in the triadic
rationals: a countable dense set can obey such an arithmetic restriction.
The changing source in (11) is essential.

## 5. What the algebraic coordinate actually adds

After ternary denominators have cleared, suppose `h_i=a_i/d` in lowest
terms with `(d,3)=1`. Put `theta=2^(1/d)` and `y_i=theta^(a_i)`.
These are algebraic S-units in one fixed number field, for the places
above two and the infinite places. Their exact recurrence is

\[
y_{i+1}=y_i^3/2^{g_i}.
\tag{12}
\]

The proposed coupled relation is

\[
(3q_i+1)y_{i+1}=q_{i+1}y_i^3.
\tag{13}
\]

Substituting (12) and cancelling the nonzero y_(i+1) turns (13)
back into `3q_i+1=2^(g_i)q_(i+1)`. The two exponential terms already
have the exact ratio `2^(g_i)`. Norms and embeddings of this identity
preserve that dependence; they do not force carry periodicity.

If `h_i=p_i+k_i`, the y_i are the finitely many phase radicals
`2^(p_i)` multiplied by `2^(k_i)`. That description does not bound or
normalize the k_i. Moreover the ordinary factors q_i are not shown to
be units for any one finite prime set. Neither a nonvanishing subsum
condition nor a suitable approximation-versus-height inequality has
been supplied for a new Subspace-Theorem application.

This is a precise obstruction to that proposed application, not a
claim that all possible algebraic-coordinate methods must fail.

## 6. Primary-literature inspection

[Adamczewski--Bugeaud, *On the complexity of algebraic numbers I*,
Annals of Mathematics 165 (2007), Theorem 5 and Theorem 5A](https://annals.math.princeton.edu/wp-content/uploads/annals-v165-n2-p04.pdf)
were inspected in the primary text. Theorem 5 treats bounded integer
coefficients with a specified repeated-prefix condition, at a Pisot
or Salem base; its conclusion allows a value in the base field.
Theorem 5A removes that alternative for the genuine normalized
expansion under its stated hypotheses. Raw valuation gaps are redundant
coefficients, and R9-A2 explicitly exhibits the rational alternative.
No digit-complexity or automatic description of an arbitrary actual
ordinary orbit has been proved here.

[Corvaja--Zannier, *Some New Applications of the Subspace Theorem*,
Compositio Mathematica 131 (2002), Theorems 1, 3, and 4](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/2F6BB76838F610EB90B204764335ABCA/S0010437X02000258a.pdf/div-class-title-some-new-applications-of-the-subspace-theorem-div.pdf)
were inspected in the primary text. Theorem 4 retains fixed finite
dimension, quantitative height inequalities, and the exclusion of a
vanishing subsum involving its distinguished term. Its applications
establish those inputs for specific series or power sums. Equations
(5) and (12) exhibit exact cancellations in the proposed present
application. The supplied actual scalar does not establish the
additional hypotheses. No imported theorem is used in R9-A1--R9-A4.

These are hypothesis checks and elementary deductions inspired by the
literature, not novelty or priority claims for positional carries,
Collatz parity cylinders, or the Chinese remainder theorem.

## 7. Evidence and remaining construction

`arithmetic_controls.py` checks exact carry cancellation, the complete
ordinary cylinder, prescribed odd residues, source and endpoint bounds,
and unconditional scalar enclosures for supplied targets and binary
carry words. It never assumes a terminating ordinary tail.

`ArithmeticRigidity.lean` contains a finite arithmetic core for the
binary block charges, arbitrary finite block concatenation, scalar-tail
transport, and elimination of the coupled coordinate. It does not
formalize the real series, the full CRT existence theorem, or the
all-real-target density statement. Compilation and dependency auditing
are recorded separately by the executing parent.

**First unsupported step:** restrict the actual carries of one unchanged
positive ordinary source enough to produce its arithmetic representation
or a nondegenerate arithmetic relation. Rationality of a redundant
discounted sum does not by itself produce that restriction; neither do
algebraic renaming or ordinary realizers that change with prefix length.
