# An all-scale ternary correction to a height barrier

**23 November 2026. Status: attempted escape-exclusion mechanism;
the required barrier was not constructed.** The ordinary one-pole and
finite-pole candidates below fail on exact positive integer inputs. The
Haar calculation concerns a stronger, explicitly stated ternary
superharmonicity condition. It does **not** rule out an ordinary-only
barrier or a genuinely nonlocal bound for the canonical envelope.

The purpose of this attempt was to compensate for every long contracting
inverse branch, rather than fix a finite residue resolution or shorten
an already bounded word. It was pursued alongside the full-basin Fourier
attack, the unrestricted cycle attack, and the same-source entropy attack.
No new Lean theorem is claimed in this note.

## 1. The intended closing mechanism

For positive odd integers use

\[
U(n)=(3n+1)/2^{v_2(3n+1)},\qquad
I_e(q)=(2^e q-1)/3.
\]

Retain only positive odd ternary units as vertices. A nonunit odd vertex
has no odd predecessor, so assign the candidate function value zero there.
The actual inverse operator is

\[
(PF)(q)=\sum_{\substack{e\ge1\\ I_e(q)\text{ an odd ternary unit}}}
                 \frac3{2^e}F(I_e(q)).                         \tag{1}
\]

A finite nonnegative function with

\[
F\ge1\text{ on positive odd units},\qquad PF\le F,
\qquad F(q)=o(q)                                               \tag{2}
\]

would exclude an escaping ordinary orbit. This is a sufficient condition,
not an established estimate. Here is the consumer with its dependency
visible. Along distinct successive odd unit states
`q_0,...,q_k`, write `A_k=sum_{i<k} v_2(3q_i+1)` and

\[
\Lambda_k=\prod_{i<k}\frac{3q_i}{3q_i+1},\qquad
\frac{3^k}{2^{A_k}}=\frac{q_k}{q_0}\Lambda_k.                  \tag{3}
\]

Iteration of the single retained branch of (1) gives

\[
F(q_k)\ge \frac{q_k}{q_0}\Lambda_k F(q_0).                     \tag{4}
\]

The resident ordinary-orbit counting estimate gives
`sum_i 1/q_i < infinity` on such an injective ray. Hence
`Lambda_k` has a strictly positive limit, and (4) contradicts (2)
as `q_k` tends to infinity. The counting input and the resulting uniform
positive product bound were already recorded in
[LITERATURE_CLOSURE_ATTEMPT.md](../LITERATURE_CLOSURE_ATTEMPT.md), Section 2,
at own baseline `8a8b1eea6c9fdfbce7b0bbf0af4eb771791e3a73`.
This consumer addresses escape; it does not by itself classify positive
cycles.

The proposed construction was

\[
F(q)=q^pH(q),\qquad 0<p<1,\qquad
H(q)\le Cq^\kappa,\quad p+\kappa<1,                           \tag{5}
\]

where `H` reads arbitrarily many ternary digits and compensates for
exceptionally contracting inverse branches. In contrast with a fixed
finite residue profile, a ternary pole can grow along deeper and deeper
approximations to a negative rational point.

## 2. Why the first pole looks promising, and why it fails

The inverse branch `I_1(q)=(2q-1)/3` fixes `-1`. If
`a=v_3(q+1)>=1`, then

\[
v_3(I_1(q)+1)=a-1.                                           \tag{6}
\]

Thus the trial function

\[
F_{p,\kappa}(q)=q^p3^{\kappa v_3(q+1)}                       \tag{7}
\]

reduces the dangerous asymptotic weight of the `e=1` branch from
`(3/2)^(1-p)` to `(3/2)^(1-p)3^(-kappa)`. A choice

\[
\kappa>(1-p)\log_3(3/2)
\]

would make that one branch contract while still allowing `p+kappa<1`.
This was the initial high-upside hypothesis: the negative fixed point
could be the principal source of exceptional inverse growth.

The `e=2` branch defeats it on an explicit infinite positive family.
For every integer `j>=1`, put

\[
q_j=\frac{3^{2j+1}-1}{2},\qquad x_j=2\cdot3^{2j}-1.
\]

Both values are positive odd ternary units, and

\[
3x_j+1=4q_j,\quad U(x_j)=q_j,\quad
v_3(q_j+1)=0,\quad v_3(x_j+1)=2j.                            \tag{8}
\]

Consequently, for every `p>=0` and every `kappa>0`,

\[
\frac{(PF_{p,\kappa})(q_j)}{F_{p,\kappa}(q_j)}
\ge\frac34\left(\frac{x_j}{q_j}\right)^p3^{2j\kappa}
\ge\frac34\,3^{2j\kappa}\longrightarrow\infty.               \tag{9}
\]

Here `x_j/q_j=4/3-1/(3q_j)>1`. All inputs in this countertest
are ordinary positive integers; `-1` was only the location of a
ternary singularity. Thus (7) is not an excessive function.

## 3. Adding any finite collection of poles still fails

Consider the more general candidate

\[
H(z)=c+\sum_{a\in A}c_a|z-a|_3^{-\kappa_a},
\quad c\ge0,\quad c_a>0,\quad \kappa_a>0,                    \tag{10}
\]

where `A` is a nonempty finite set of distinct ternary units. If a
pole is a positive odd ordinary unit, the candidate is already infinite
at an input and cannot satisfy (2). Otherwise choose any `a in A`.
The points

\[
b_e=(3a+1)/2^e,\qquad e\ge1,
\]

are distinct units, since `3a+1` is nonzero. Choose an `e` with
`b_e` outside `A`. Take positive odd integers `q_j` tending to `b_e`
ternarily and to infinity in the ordinary real absolute value. Such a
sequence is obtained by choosing the appropriate residue modulo `3^j`
with its representative chosen odd, and then adding a sufficiently large even
multiple of `3^j`.

For all sufficiently large `j`, `I_e(q_j)` is a positive odd ternary
unit and tends ternarily to `a`. Hence `H(I_e(q_j))` tends to infinity.
But `H(q_j)` tends to the finite value `H(b_e)`, because the finite
sum (10) is continuous away from its poles. Also

\[
\frac3{2^e}\left(\frac{I_e(q_j)}{q_j}\right)^p
\longrightarrow\left(\frac3{2^e}\right)^{1-p}>0.             \tag{11}
\]

The one legal summand in (1) therefore exceeds the target for large
`j`. This proves that no nonempty finite positive sum (10), multiplied
by any fixed real power of the ordinary height, is excessive at every
positive odd unit.

The failure is propagation of singularities under **all** forward
affine maps `a -> (3a+1)/2^e`, not just the repeated `e=1` point.
A countably infinite, accumulating pole set is not excluded by this
finite-pole proof.

## 4. The all-scale Haar construction has the wrong mean multiplier

An attractive way to organize infinitely many poles is to construct a
superharmonic function on `U_3=Z_3^times` first, then restrict it to
ordinary integers. Set `delta=1-p` and define the positive operator

\[
(R_\delta H)(z)
=\sum_{\substack{e\ge1\\ I_e(z)\in U_3}}
       (3/2^e)^\delta H(I_e(z)).                             \tag{12}
\]

For ordinary legal positive inputs, the exact, rather than asymptotic,
comparison is

\[
\frac{(PF)(q)}{q^p}
=\sum_e(3/2^e)^\delta
  \left(1-\frac1{2^e q}\right)^p H(I_e(q))
\le (R_\delta H)(q).                                        \tag{13}
\]

Thus **pointwise** `R_delta H<=H` at the ordinary inputs would suffice
for excessivity of the candidate (5). A construction imposing this
inequality everywhere on `U_3` is stronger still.

Let `mu` be Haar measure normalized to give `U_3` mass one. The map
`f_e(x)=(3x+1)/2^e` sends `U_3` bijectively onto the legal branch
domain with measure `1/3`. Its ternary Jacobian is `1/3`.
Tonelli therefore gives, for every nonnegative measurable `H`,

\[
\int R_\delta H\,d\mu
=m(\delta)\int H\,d\mu,
\qquad m(\delta)=\frac{3^{\delta-1}}{2^\delta-1}.             \tag{14}
\]

For `0<delta<1`, this multiplier is strictly greater than one.
One proof uses weights `2^(-e)`, whose sum is one and whose mean
exponent is two. Jensen gives

\[
m(\delta)
=\sum_{e\ge1}2^{-e}
       \exp((\delta-1)\log(3/2^e))
\ge (4/3)^{1-\delta}>1.                                     \tag{15}
\]

It follows that no nonzero nonnegative **integrable** `H` satisfies
`R_delta H<=H` Haar almost everywhere for this exponent range.
The geometric multiplier is the same elementary normalization used in
the capped inverse-transfer literature, for example
[rStation paper 37, Section 2](https://rstation.ai/problems/collatz/papers/37/v2).
Here (14)--(15) are proved directly; no claimed spectral theorem is
imported.

For example, a positive countable sum of poles with summable coefficients
and a common order `0<kappa<1` is integrable. For a unit pole `a`,

\[
\int_{U_3}|z-a|_3^{-\kappa}\,d\mu(z)
=\frac12+\sum_{j\ge1}3^{(\kappa-1)j}<\infty.                \tag{16}
\]

The integral is independent of the pole. The same conclusion holds for
orders bounded above by a fixed number less than one. Such a potential
cannot supply the proposed **Haar-a.e. superharmonic construction**.

## 5. The distinction that prevents an invalid no-go theorem

Equation (14) is not an objection to a function satisfying an inequality
only at positive ordinary integers. That set has Haar measure zero.
Nor does density of the ordinary integers extend an inequality between
two arbitrary lower semicontinuous, singular potentials to Haar almost
everywhere. The finite-pole argument used actual continuity off a finite
set; that step is unavailable for a dense accumulating set of poles.

In particular, a future construction could deliberately encode the
ordinary zero-digit tail in an infinite pole pattern. It would then need
to prove the exact ordinary inequality (13), the finiteness and obstacle
condition in (2), and the sublinear height bound in (5). The Haar
calculation does not settle any of those ordinary-only questions.

The actual outcome is narrower and precise:

* The single negative fixed-point correction (7) fails by the infinite
  ordinary family (8).
* Every finite positive pole correction (10) fails by ordinary
  approximations to a missing image pole.
* The attempted integrable, everywhere-superharmonic infinite-pole
  construction fails because its mean multiplier exceeds one.
* No all-scale ordinary-only correction meeting (2) or (5) was found.

An arbitrary pointwise upper bound for the canonical envelope need not
itself be excessive and is also outside these exclusions. The full
Collatz theorem has not been proved by this attempt.
