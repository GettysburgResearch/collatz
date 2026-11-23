# Scalar natural boundaries and the binary interpolation center

23 November 2026. Author: `source_construction`.

**Status: PROPOSED written deductions from checked primary rationality
theorems. No universal arithmetic Taylor germ, complementary rational
candidate, escape exclusion, or full Collatz proof is constructed.**

The attempted central construction was to use the actual binary value
`B_n(2)=-n` as a second arithmetic interpolation center. It gives a
nontrivial conditional consumer: at critical parity density, a suitable
arithmetic Taylor germ at that center yields a strictly positive
two-center capacity matrix and hence rationality. Its first unsupported
input is the arithmetic germ itself, not a missing estimate for the
matrix. The known value supplies only its constant coefficient.

Two accompanying deductions delimit this construction. A fixed source
with a limiting parity density has either a rational weighted parity
series or a scalar natural boundary. Deflating the known binary zero
preserves the actual integer numerators but gives an exact disc-capacity
product at most one. These are source-dependent statements; no changing
finite realizers or unrelated symbolic law enters them.

## 1. Fixed source, complete identity, and primary inputs

Use the shortcut map `T` on positive ordinary integers. Fix `n>=1` and put

\[
x_k=T^k(n),\qquad e_k=x_k\bmod2,\qquad
p_k=\sum_{j<k}e_j,\qquad
b_k=e_k3^{-p_{k+1}},\qquad B_n(z)=\sum_{k\ge0}b_kz^k.
\tag{1}
\]

Every object in (1) belongs to this single ordinary orbit. The inherited
complete affine identity is

\[
n+\sum_{j<k}b_j2^j=\frac{2^k x_k}{3^{p_k}}.
\tag{2}
\]

In particular, `B_n(2)=-n` in `Q_2`. This identity does not identify a
real boundary value. All numerators and powers of three in (2) are
retained below.

There are infinitely many odd inputs: an eventually all-even positive
ordinary orbit would be divisible by arbitrarily high powers of two.
Write

\[
\rho_- =\liminf_k p_k/k,\qquad
\rho_+ =\limsup_k p_k/k.
\]

The following exact radius calculation and the rational-series consumer
are inherited, with their elementary justifications recalled as needed:

\[
R_\infty(B_n)=3^{\rho_-},\quad
R_3(B_n)=3^{-\rho_+},\quad R_\ell(B_n)=1\quad(\ell\ne3).
\tag{3}
\]

To sample the liminf or limsup in (3), use clocks of odd inputs.
Between consecutive odd inputs the count is constant, so the extrema of
`p_k/k` occur immediately before or after those clocks. Changing the
count by one or shifting a clock by one changes the ratio by `o(1)`.
The Cauchy--Hadamard formula then gives (3). At other primes every
nonzero `b_k` is a unit.

The primary inputs actually checked are:

- Bost--Chambert-Loir, *Analytic curves in algebraic varieties over
  number fields*, arXiv:math/0702593v3, Theorem 7.9, its following
  condition `2'`, and Example 7.10. A formal germ with the stipulated
  adelic meromorphy and integral model is rational when its capacitary
  degree is strictly positive. No equality-case algebraicity hypothesis
  is substituted for that strict inequality.
- Chambert-Loir--Noûs, *Potentiel et rationalité*,
  arXiv:2305.17210v2, 31 August 2026, Sections 2.1--2.8 and 4.1--4.3.
  The multipoint criterion uses arithmetic formal germs, compatible
  meromorphic realizations at every place, and a strictly positive
  potential-game value. Local analytic domains may be disconnected.

The source ledger supplies primary URLs and exact repository hashes.
These are applications of the cited machinery, not new general
algebraicity theorems. The previous PR180 `HOLONOMICITY.md` proves and
credits the needed special consumer

\[
B_n\in\mathbb Q(z)
\quad\Longleftrightarrow\quad(e_k)\text{ eventually periodic}
\quad\Longleftrightarrow\quad(x_k)\text{ eventually periodic}.
\tag{4}
\]

The last implication retains the full block denominator: for a repeated
word of length `L`, odd count `a`, carry `C`, and
`D=2^L-3^a`, repeated integer realization makes `2^(Lt)` divide the
fixed integer `D x_0-C` for every `t`. Thus that integer is zero.
Neither (4) nor rationality alone excludes another positive cycle.

## 2. A scalar natural-boundary alternative

**Theorem 1.** Suppose the actual density `p_k/k` has a limit `rho`.
Then exactly one of the following occurs:

1. `B_n` is rational and the ordinary source is eventually periodic.
2. The circle `|z|=3^rho` is a natural boundary for this individual
   scalar `B_n`.

**Proof.** Put `R=3^rho`. Suppose `B_n` continues holomorphically
through a point of its convergence circle. It then extends to a domain
formed by the disc `D(0,R)` and a small boundary bump. Since its
coefficients are rational, include the conjugate bump when necessary.
Choose a symmetric simply connected enlargement `Omega_infinity`.
Its conformal radius `c` at zero is strictly greater than `R`.

Here is the strictness needed by the arithmetic theorem. If a Riemann
map `phi:D(0,1)->Omega_infinity` has `phi(0)=0`, `phi'(0)=c>0`,
then `phi^(-1)(R z)` maps the unit disc to itself and has derivative
`R/c` at zero. Equality in Schwarz's lemma would force the enlarged
domain to equal the original disc. Therefore `R/c<1`.

A smooth relatively compact exhaustion preserves the strict inequality
`c>R`; it may be chosen with conformal radius still above `R`. Pick

\[
1/c<r_3<3^{-\rho},\qquad r_3\in3^{\mathbb Q}.
\tag{5}
\]

At three use the disc `D(0,r_3)`. At every other finite prime use the
unit disc. The germs are analytic on these domains by (3). Their
formal coefficients lie in `Z[1/3]`, which verifies the sufficient
integral-model condition `2'` following Bost--Chambert-Loir Theorem
7.9. The formal graph is smooth because it is a graph. The capacitary
degree is

\[
\log c+\log r_3>0.
\]

The theorem makes `B_n` rational. Apply the credited consumer (4).
Conversely a rational function has no natural boundary. If a local
continuation were merely meromorphic, a neighboring point away from
its isolated poles would give the same holomorphic argument. `QED`.

For a hypothetical critical-density source,

\[
\rho=\log_3 2,
\tag{6}
\]

the scalar circle in Theorem 1 is exactly `|z|=2`. This density is
irrational, while an eventually periodic parity word has rational
density. Hence (6) forces the natural-boundary branch. This conclusion
is conditional on the existence of such an ordinary source; it does
not produce one or exclude it.

This strengthens the *type* of boundary statement available in PR180's
new global construction: that note proves a uniform-family norm
boundary even from convergent powers of two. Theorem 1 instead concerns
one scalar source, with an explicit limiting-density hypothesis. It
does not prove that every hypothetical escape has a density limit.

## 3. Exact deflation of the known binary value

The first direct attempt was to remove the known zero at the arithmetic
point. Define the formal quotient

\[
G_n(z)=\frac{B_n(z)+n}{z-2}.
\tag{7}
\]

**Theorem 2 (the deflation pays its full capacity cost).** Its coefficients
are exactly

\[
\boxed{G_n(z)=-\sum_{k\ge0}
             \frac{x_{k+1}}{3^{p_{k+1}}}z^k.}
\tag{8}
\]

In particular no new binary denominator is present. Its exact radii are

\[
\boxed{
R_\infty(G_n)=\min(2,3^{\rho_-}),\quad
R_3(G_n)=3^{-\rho_+},\quad
R_\ell(G_n)=1\ (\ell\ne3).}
\tag{9}
\]

Thus the product of its convergence-disc radii is

\[
\boxed{\min(2,3^{\rho_-})3^{-\rho_+}\le1.}
\tag{10}
\]

**Proof.** Formal division by `z-2` gives the coefficient

\[
-2^{-k-1}\left(n+\sum_{j=0}^{k}b_j2^j\right).
\]

Use (2) at `k+1` to obtain (8). This is the inherited state-series
identity in a normalization suited to the extra center; the identity
itself is not claimed as new.

At three, integrality of `x_(k+1)` gives the upper coefficient bound
`|x_(k+1)/3^p_(k+1)|_3<=3^p_(k+1)`. At every clock with `e_k=1`,
the actual next integer is a three-adic unit because
`2 x_(k+1)=3 x_k+1`. The odd-clock sampling observation after (3)
therefore gives equality for the radius at three.

At every other prime the coefficients in (8) are integral. There are
infinitely many unit numerators. For the prime two this follows from
infinitely many odd states. For an odd prime `ell!=3`, if all late
states were divisible by `ell`, an odd input would have a next state
not divisible by `ell`, a contradiction. Hence each such radius is
exactly one.

At infinity, put `R=R_infinity(B_n)`. If `R<2`, multiplication or
division by `z-2` cannot change the radius, so `R_infinity(G_n)=R`.
If `R>=2`, equation (7) gives analyticity inside radius two. On the
other hand, (2) and positivity show

\[
\frac{x_{k+1}}{3^{p_{k+1}}}
=2^{-k-1}\left(n+\sum_{j=0}^{k}b_j2^j\right)
\ge n2^{-k-1}.
\]

The radius cannot exceed two. When `R>2`, this also has the direct
interpretation that the real numerator `B_n(2)+n` is strictly positive,
so (7) has a genuine real pole at two. Equations (9)--(10) follow.
`QED`.

At critical limiting density the product in (10) is exactly one. At
a larger limiting density it is `2/3^rho<1`. Thus this particular
arithmetic deflation does not give the strict positive degree needed
by the one-center rationality theorem. The real pole and the binary
zero belong to different completions; discarding either would change
the calculation.

## 4. A genuine two-center criterion with a strict margin

The multipoint theorem does not take a single rational value as a
second formal germ. Write the **actual** binary Taylor expansion

\[
J_n(t)=B_n(2+t)\in\mathbb Q_2[[t]].
\tag{11}
\]

It converges on the binary unit disc and has constant term `-n`.
The following concrete arithmetic hypothesis is substantially stronger:

**Jet hypothesis J.** All coefficients of `J_n` are rational; for one
positive integer `M` they all belong to `Z[1/M]`; and `J_n` has positive
radius of convergence at infinity and at every prime dividing `M`.
The equality in (11) is required for the entire binary germ. It is not
enough to prescribe a new series with the same constant term.

This is a transparent sufficient integral-model hypothesis for the
multipoint theorem. No assertion that J is automatic from ordinary
integrality is made.

**Theorem 3 (critical two-center consumer).** If (6) holds and Jet
hypothesis J holds, then `B_n` is rational. Consequently no positive
ordinary source can satisfy both (6) and J.

**Proof.** Work on `P^1_Q` with centers zero and two. The formal germs
are `B_n(z)` at zero and `J_n(z-2)` at two. The latter is a germ over
`Q` by J. Both have a common formal integral model outside the finite
set of primes dividing `6M`.

Fix a sufficiently small positive real `epsilon`. At the real place
choose the disjoint union

\[
D(0,2-2\epsilon)\ \sqcup\ D(2,\epsilon).
\tag{12}
\]

On its first component use the original complex `B_n`; on its second
use the complex realization of `J_n`. No complex gluing is asserted.
Its small radius is permitted by J.

At two use the **single** unit disc. It contains both zero and two,
and the original binary `B_n` realizes both germs there, by (11).
With local coordinates `z` and `z-2`, its two diagonal Green constants
are zero and its off-diagonal Green value is

\[
L=-\log|2|_2=\log2>0.
\tag{13}
\]

At three choose a radius

\[
\tfrac12e^{-\epsilon}<r_3<\tfrac12,
\qquad r_3\in3^{\mathbb Q},
\tag{14}
\]

for the zero center. Choose a fixed sufficiently small positive radius
for the second germ, less than one. The two ternary discs are disjoint
because `|2|_3=1`.

At every remaining prime use the unit disc at zero. At the second
center use a fixed radius at most one on which J converges. For all
but finitely many primes this radius is one. These two discs are
disjoint because their centers have distance one. Thus their
off-diagonal Green values vanish. The total finite-place diagonal
cost at the second center is a finite constant, independent of
`epsilon`. This finiteness uses the explicit `Z[1/M]` condition.

The resulting global potential matrix is exactly

\[
\boxed{\mathcal G_\epsilon=
\begin{pmatrix}a_\epsilon&L\\L&b_\epsilon\end{pmatrix},
\quad
a_\epsilon=\log((2-2\epsilon)r_3),\quad
b_\epsilon=\log\epsilon+C.}
\tag{15}
\]

Here `C` is finite and fixed. For `0<epsilon<1/2`, (14) gives

\[
-3\epsilon<a_\epsilon<0.
\]

For sufficiently small `epsilon`, also `b_epsilon<0`, and

\[
0<a_\epsilon b_\epsilon
\le3\epsilon(|\log\epsilon|+|C|)\longrightarrow0.
\tag{16}
\]

Choose `epsilon` so small that `a_epsilon b_epsilon<L^2`. The
probability of choosing the first row

\[
x=\frac{L-b_\epsilon}{2L-a_\epsilon-b_\epsilon}\in(0,1)
\]

gives the same strictly positive payoff against either column:

\[
\frac{L^2-a_\epsilon b_\epsilon}
     {2L-a_\epsilon-b_\epsilon}>0.
\tag{17}
\]

Thus the potential-game value is positive. The integral model and
all local meromorphic realizations have been specified, so
Chambert-Loir--Noûs Theorem 4.3 makes the two germs expansions of one
rational function. In particular `B_n` is rational. Equation (4)
then makes the parity density rational, contradicting (6). `QED`.

The strict gain in (17) is real: the binary disc joins the two centers,
while the loss at the first diagonal is only `O(epsilon)`. The large
negative second diagonal costs `O(|log epsilon|)`, whose product with
that first loss tends to zero. This is not the zero-margin deflation
calculation of Section 3.

## 5. What the ordinary value does and does not construct

The first unknown Taylor coefficient in (11) is already

\[
J_n'(0)=B_n'(2)
=\sum_{k\ge1} k e_k\,2^{k-1}3^{-p_{k+1}}
\quad\text{in }\mathbb Q_2.
\tag{18}
\]

Its rationality has not been proved for an arbitrary positive source.
Even rationality of every coefficient would not by itself prove the
common finite denominator-prime set or analytic bounds in J. Those
are separately retained parts of the hypothesis.

Known values at the orbit's later states do not supply independent
centers. With the full prefix polynomial
`P_k(z)=sum_(j<k) b_j z^j`, the exact tail identity is

\[
B_n(z)=P_k(z)+z^k3^{-p_k}B_{x_k}(z).
\tag{19}
\]

Substituting the known binary value `B_(x_k)(2)=-x_k` and using (2)
reduces (19) to the same single equation `B_n(2)=-n` for every `k`.
It does not provide (18), a new independent evaluation of `B_n`, or
the arithmetic Taylor germ required by Theorem 3.

A separate finite interpolation diagnostic reinforces the scope.
For jets of orders `r` at zero and `s` at two, using Hasse derivatives,
the confluent evaluation determinant on polynomials of degree less
than `r+s` is exactly `2^(rs)`. Indeed, use the monic degree-ordered
basis `1,z,...,z^(r-1),z^r,z^r(z-2),...,z^r(z-2)^(s-1)`.
The first jet block is identity, its upper-right block is zero, and
the second diagonal block is triangular with diagonal `2^r`.
The basis change has determinant one. The archimedean factor
`2^(rs)` and binary factor `2^(-rs)` cancel in the product formula.
Thus this evaluation determinant alone is not a strict saving. It
does not rule out the potential gain in (17), which additionally uses
complete arithmetic germs and their local analytic domains.

## 6. Relation to the latest construction and the remaining step

PR180's new global meromorphic family and conditional Blaschke product
reach the critical interior disc. They do not provide J or a scalar
continuation through its boundary. Finite rational pole cancellation
does not change a scalar natural boundary. An infinite Blaschke product
requires its own coefficient arithmetic before it can enter an
arithmetic rationality theorem; bounded holomorphy alone does not give
that arithmetic.

The newer PR177 numerator recognizer and PR182 linear-denominator
recognizer were inspected as finite consumers. They verify a supplied
candidate, whereas the present attempt seeks an arithmetic construction
for one original source. Neither their shorter clocks nor (17)
constructs the missing complementary candidate.

**First unsupported implication:** derive Jet hypothesis J, or a
verified weaker arithmetic-germ condition sufficient for the same
multipoint theorem, from the literal positive ordinary source. This
attempt establishes the strict-capacity consumer and the exact failure
of value-only deflation; it does not establish that implication.
The two-center consumer addresses the critical-density branch only.
It has not been shown that every hypothetical escape has a density
limit or has that critical density, and other positive cycles remain
a separate issue.

All analytic and arithmetic claims in this file have written scope.
No Lean wrapper is presented as formal verification of the primary
potential theory, infinite radii, or germ construction.
