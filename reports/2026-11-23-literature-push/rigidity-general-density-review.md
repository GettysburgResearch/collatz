# Reconstruction review: the second germ at every limiting density

23 November 2026. Reviewer: `/root/source_construction`.

**Verdict: VERIFIED in written conditional scope.** The source is
`research/literature-push-20261123/rigidity/GENERAL_DENSITY_JET.md`,
SHA-256 `400e3c6cdccea71b71224fc2ee5cfb1379b334e5422cd64b81a87bd239403890`.
The verdict binds only those bytes.

The reviewer contributed the initial maximum-principle estimate before
the root author wrote this addendum. This report reconstructs the final
assembly and its hypotheses; it is not a claim of independence from
authorship of that preliminary estimate or of external referee acceptance.

## 1. Arithmetic and local-realization hypotheses

The theorem retains one fixed positive ordinary source and assumes the
existence of its limiting odd-input density. No new source or stationary
law is substituted. Jet hypothesis J includes the full actual binary
Taylor germ, rationality of every coefficient, a common ring
`Z[1/M]`, and positive radii at infinity and all its exceptional primes.
The value `-n` alone is never treated as that germ.

The primary multipoint source was read directly:
Chambert-Loir--Noûs, *Potentiel et rationalité*,
arXiv:2305.17210v2, Sections 2.1--2.8 and 4.1--4.3,
<https://arxiv.org/pdf/2305.17210>.
Section 4.1 requires compatible full formal expansions and an adelic
integral model; Section 4.3 uses strictly positive game value.
The analytic domains need not be connected. The paper separately
discusses the consequences of connectedness at one place.

Here the first coefficients belong to `Z[1/3]`, the second belong to
`Z[1/M]`, and the centers are rational. Outside the finite set dividing
`6M`, the stated unit-disc union is exactly the union of their residue
classes. At two, the single unit disc contains both centers and the
same actual binary function realizes the complete two germs there.
At the other places the chosen separate realizations are legitimate;
no unproved complex identification of their values at two is used.

For the first finite-place diagonal, only the radius at three changes
with `epsilon`. The second-center bad-prime radii are fixed before
that limit, so their total logarithmic cost `C` is finite and independent
of `epsilon`. The good-prime radii are one. These observations verify
the exact arithmetic hypotheses needed by the application.

## 2. Shared potential matrix and the cases R<=2

In the binary unit disc, the centers have distance `|2|_2=1/2`.
Both diagonal Green constants are zero, while the off-diagonal value
is `L=log 2`. The remaining finite-prime components are disjoint and
contribute zero off-diagonal entries. The complex components are also
kept disjoint. Thus the global matrix in equation (1) has exactly the
claimed entries, with no additional omitted cross term.

For `R<2`, the two complex discs are disjoint once `epsilon` is
sufficiently small, and the first diagonal lies strictly between
`-3 epsilon` and `-2 epsilon`. The second is `log epsilon+C`.
Their product tends to zero. The `R=2` case is the already frozen
critical construction; its first loss is again `O(epsilon)`.

For two negative diagonal entries `a,b`, the stated probability
`(L-b)/(2L-a-b)` lies strictly between zero and one. Direct substitution
into each column payoff gives
`(L^2-ab)/(2L-a-b)`. Hence `ab<L^2` really supplies a strictly positive
guaranteed payoff, not merely a positive entry of the matrix.

## 3. The removed-disc comparison for R>2

Fix `R>2` throughout the limit. For sufficiently small `epsilon`,
`S=R exp(-epsilon)` and `h=2 epsilon` satisfy `S>2+h` and `h<2`.
The closed inner disc therefore lies strictly inside the outer disc
and does not contain zero. The punctured domain and the second germ's
disc of radius `epsilon` are disjoint smooth analytic components.

The two disc Green functions in equation (3) have the correct signs,
normalizations, poles, and zero boundary values. On the inner circle,
`|z|>=2-h` and
`|S^2-2z|>=S^2-4-2h`. These give the stated bounds `M_h` and `m_h`.
For sufficiently small `epsilon`, the latter is positive.

Let `u` be the difference between the unpunctured and punctured Green
functions with pole at zero. Their logarithmic singularities cancel,
so `u` is harmonic through zero. Its inner boundary values equal the
unpunctured Green function, and its outer values vanish. Thus
`u<=M_h H`, where `H` is harmonic measure of the inner circle.

The second Green function has its pole inside the removed disc and is
therefore harmonic throughout the punctured domain. Dividing by
`m_h` makes its inner boundary values at least one and its outer
values zero. The maximum principle gives
`H<=g_S(z,2)/m_h`. At zero, `u(0)` is precisely the nonnegative Robin
loss `delta_epsilon`. This reconstructs equation (5) without importing
an unstated small-hole capacity theorem.

The denominator in (5) equals

\[
|\log\epsilon|+\log\frac{R^2-4}{2R}+o(1),
\]

while both numerator factors tend to `log(R/2)`. Therefore
`limsup delta_epsilon |log epsilon| <= log(R/2)^2`, and also
`delta_epsilon -> 0`. The first global diagonal is
`-delta_epsilon-t_epsilon`, where
`2 epsilon<t_epsilon<3 epsilon`. Multiplying by the second negative
diagonal shows that all the terms involving `C` or `t_epsilon`
vanish in the limit. This proves equation (8).

The bound `R<=3` is essential to the uniform strict conclusion:
`log(R/2)^2<=log(3/2)^2<log(2)^2`. The estimate need not be uniform
as `R` approaches two; the theorem fixes its source and density, and
then chooses a sufficiently small radius. That order is respected.

The positive-game criterion now applies at every possible limiting
density. The primary theorem makes the two germs expansions of a
single rational function, despite their initially separate complex
realizations. This is a consequence of the fully checked arithmetic
and all-place hypotheses, not a prior gluing assumption.

## 4. Ordinary consumer and converse

The addendum correctly credits rational weighted parity series to the
earlier finite-window recurrence consumer. For an ordinary source,
eventual parity periodicity gives eventual state periodicity using the
entire repeated-block denominator and unbounded binary divisibility.
No other positive cycle is excluded by this step.

Conversely, an eventually periodic source has a rational `B_n`. Its
original binary power series is analytic on the unit disc, including
two, so the corresponding rational function has no pole at two.
The Taylor coefficients there are rational. A fixed rational function
regular at a rational center has Taylor coefficients in `Z[1/M]`
for some `M`, obtained by clearing its polynomial coefficients and
inverting its nonzero denominator value at that center. It has positive
radius at every place. This proves all of J, including the actual
binary-germ identity.

Thus the claimed equivalence on the class of sources with a limiting
density is correct. It remains an equivalence with an unproved
arithmetic-germ condition. Neither the existence of that density for
all escaping sources nor J has been established. The first unknown
Taylor coefficient remains `B_n'(2)`, followed by the independent
finite-denominator-prime and local analytic requirements.

No Lean formalization of Green functions or the multipoint theorem
is claimed. The newly compiled gcd modules have a separate algebraic
scope and do not formally certify this analytic addendum.

Release normalization refresh: hashing the current source bytes plus one
newline reproduces the previously reviewed source hash. Only that final
redundant newline was removed. The binding above is refreshed; the
mathematical verdict and review scope are unchanged.
