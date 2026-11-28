# New factoring evaluators against the actual Collatz trace

Date: 2026-11-28. This follow-up inspected the complete source of three
additional evaluator manuscripts, including the new factoring PR 365 opened
during this Collatz pass. The immutable source pins are recorded in
[LATEST_FACTORING_SOURCE_INTAKE.json](LATEST_FACTORING_SOURCE_INTAKE.json).
None of the cited PRs claims general polynomial-time factoring.

The consumer is now concrete: the full-conductor joint Cauchy trace, or the
stationary two-copy rare-event probability in
[STATIONARY_COLLISION_CONSUMER.md](STATIONARY_COLLISION_CONSUMER.md). The
latter must be estimated relative to a probability of order
\(X^2/4^{h_X}\), approximately \(X^{-7.6377}\) at the native critical clock.

## 1. PR 361 really does compress enormous coefficient modules

Pinned head: `a376fed33a238b4eb61fe222007851a9b4e85d76`.

The complete
[circuit-content manuscript](https://github.com/gfreund123/factoring-in-p/blob/a376fed33a238b4eb61fe222007851a9b4e85d76/research/factoring-nine-hour-2026-11-28/constructive/circuit-content.md)
gives a randomized polynomial-bit algorithm for the coefficient **row module**
of a list of univariate arithmetic-circuit polynomials modulo an arbitrary
integer. The formal degree enters through its binary length. Random monic
quotients preserve the relevant coefficient subspace; local Smith arguments
retain repeated-prime information. The manuscript also gives clipped
bivariate rank tests and bounded-degree rational-relation recovery.

This is stronger than requiring a dense coefficient array or a fixed low
formal degree. It is not a prescribed-coefficient evaluator. The distinction
can be tested on the actual Collatz aggregate, not only on an unrelated
example.

Fix a length and grade with at least two words, and put

\[
F(z)=\sum_w z^{A(w)}.
\]

Carry injectivity makes every nonzero coefficient exactly 1. Attempt to read
\([z^B]F\) by adjoining the marker column \(z^B\) to the coefficient
matrix. Over **every** coefficient ring \(\mathbb Z/N\mathbb Z\), its row
module is the full module \((\mathbb Z/N\mathbb Z)^2\), regardless of
whether \(B\) occurs as a carry:

- if it does not occur, one carry row is \((1,0)\) and the marker row is
  \((0,1)\);
- if it does occur, another carry gives \((1,0)\), while its row is
  \((1,1)\), whose difference gives \((0,1)\).

Thus even exact recovery of this natural augmented coefficient module loses
the requested positional information completely. The formal coefficient
algorithm in the earlier PR 234 remains useful precisely because it follows
the **prescribed Cartier digits**, rather than only a row module.

The new
[prime-power Newton manuscript](https://github.com/gfreund123/factoring-in-p/blob/a376fed33a238b4eb61fe222007851a9b4e85d76/research/factoring-nine-hour-2026-11-28/quantum/prime-power-newton-shifts.md)
recovers entire formal translation cosets for public-order matrix products
whose univariate entries are succinct circuits. It uses random extension
centres to retain formal identities, a factorial-divisibility bound on
Newton indices modulo \(p^e\), and graded linear congruence solving. Its
cost is polynomial in numerical \(p,e\), the supplied program width, and
binary formal degree. It does not claim a general prescribed-coefficient
algorithm for an unrestricted circuit. Supplying the full Collatz residue
matrix still supplies width \(3^a\); a new representation is needed to
remove that cost.

## 2. PR 365 gives a genuine strong nonlinear Fourier evaluator

Pinned head: `10a5d69497a931061a14b21860f1ebcd45fe0161`.

The complete
[isotropic Fourier manuscript](https://github.com/gfreund123/factoring-in-p/blob/10a5d69497a931061a14b21860f1ebcd45fe0161/research/astra-load-bearing-2026-11-28/transforms/notes/isotropic-fourier.md)
evaluates, for an odd modulus \(M\),

\[
\sum_{x\in(\mathbb Z/M\mathbb Z)^n}
e_M\left(\tfrac12x^TAx+H(BAx)-y^Tx\right)
\tag{1}
\]

when \(A\) is symmetric and every entry of the public Gram matrix
\(BAB^T\) is nilpotent. The nonlinear \(H\) may be an arbitrary supplied
arithmetic circuit with enormous formal degree. The output is an exact
Gaussian amplitude descriptor, not only a weak Fourier sample. The
nilpotent Gram condition forces a unique auxiliary critical point and an
explicit phase. The associated Fourier-sampling law is uniform on the image
of \(A\).

This directly answers the question whether the factoring work contains any
actual strong pointwise Fourier evaluator: it does. The remaining issue is
whether the **constrained Collatz observable** has that representation and
nilpotence property.

## 3. The natural Boolean path encoding fails the unique-critical-point test

An arbitrary Collatz carry circuit can be built using the chronological
updates

\[
A_{j+1}=3^{b_j}A_j+b_j2^j
=(1+2b_j)A_j+b_j2^j,\qquad b_j\in\{0,1\}.
\tag{2}
\]

Modulo an odd prime power, this gives a polynomial circuit in the bit
variables. It retains exactly the ordered carries; an additional grade
marker is needed to select their sum.

The most direct way to impose the Boolean domain inside a complete Fourier
sum introduces multiplier variables \(\lambda_i\) and the phase

\[
P(b,\lambda)=H(b)+\sum_{i=1}^h\lambda_i b_i(b_i-1).
\tag{3}
\]

For \(M=3^e\), summing the multipliers gives exactly
\(M^h\sum_{b\in\{0,1\}^h}e_M(H(b))\), because the only roots of
\(b(b-1)=0\) modulo this prime power are 0 and 1. Thus this lift retains
the Boolean sum rather than replacing its domain by an unconstrained field.

Already over \(\mathbb F_3\), its critical equations are

\[
b_i(b_i-1)=0,\qquad
\partial_iH(b)+\lambda_i(2b_i-1)=0.
\tag{4}
\]

For every Boolean vector \(b\), each \(2b_i-1\) is a unit, so the second
equation fixes a unique multiplier vector. Thus (3) has **exactly \(2^h\)
critical points**, independently of \(H\). Each is nondegenerate: the
Hessian has block form

\[
\begin{pmatrix}
H''(b)+2\operatorname{diag}(\lambda)&D\\
D&0
\end{pmatrix},\qquad D=\operatorname{diag}(2b_i-1),
\tag{5}
\]

with determinant \((-1)^h\det(D)^2\ne0\). These critical points lift
uniquely to higher powers of three; a stationary-phase calculation retains
their separate phase contributions instead of selecting one of them.

There is a distinction between the theorem's **auxiliary** critical point
and the full phase in (1). The latter can have multiple full critical points
when \(A\) is singular, but that does not repair this encoding. Modulo 3 its
Hessian is

\[
A+AB^TH''(BAx)BA.
\]

If \(A\) is singular, every vector in \(\ker A\) lies in the Hessian
kernel, so all its critical points are degenerate. Our Boolean lift has
only nondegenerate critical points. If \(A\) is invertible, the full
critical equation, with \(u=BAx\), gives

\[
u+BAB^T\nabla H(u)=By.
\]

Nilpotent Gram entries vanish modulo 3, so \(u=By\) and
\(x=A^{-1}y-B^T\nabla H(By)\) is the **unique full critical point**.
These two cases explicitly rule out the natural lift's pattern of
\(2^h\) nondegenerate critical points in this theorem class, for \(h\ge1\).
An invertible change of variables preserves both the number of critical
points and their Hessian degeneracy. This does not exclude a different
structured encoding or a useful sum over critical points; it identifies the
concrete missing construction.

When \(H=0\), all contributions align and the sum is easy. For the coupled
carry, real-window, and two-copy collision conditions, their controlled sum
has not been supplied. A sampler that cheaply chooses a critical branch is
also not an estimate of the resulting small probability or complex sum to
the required relative accuracy.

## 4. What can be imported now

The earlier normalized matrix plus prescribed Cartier coefficient engine
remains a valid positive algorithm for the specified low-conductor moments.
The new PRs add real circuit-module and nonlinear Fourier machinery, but
their exact hypotheses expose different missing data:

| Imported evaluator | Input already available | Missing Collatz input |
|---|---|---|
| Circuit coefficient module | A succinct carry polynomial circuit | A positional coefficient consumer beyond module/content information |
| Prime-power formal shift recovery | Succinct ordered polynomial layers | A compact full-conductor program for the requested trace |
| Nilpotent-Gram strong Fourier evaluation | A polynomial carry circuit | A valid complete-sum encoding whose Gram matrix is nilpotent and which retains Boolean selection, grade, and real window |

These are source-specific applicability tests. No impossibility theorem for
general conductor compression, approximate resolvents, or Collatz proofs is
asserted. The written proofs and immutable source blobs were inspected;
these external implementations and full analytic arguments were not rebuilt
or formally certified in this lane.
