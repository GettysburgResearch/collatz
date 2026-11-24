# Actual carry returns, complete denominator rigidity, and the scalar law

23 November 2026. Published parent PR182:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

**Collatz remains OPEN.** This packet pursues the actual scalar from
round eight through four parallel approaches and one connecting
corollary. The strongest new deterministic result bounds every first
denominator-eight carry excursion, including arbitrarily large
carries. The complete-denominator and statistical results identify
further constraints without turning changing sources into a proof
about one fixed orbit.

The source and literature pins are in [SOURCES.json](SOURCES.json).
The [execution and review report](../../reports/2026-11-23-scalar-rigidity-round9/README.md)
separates written proofs, Lean checks, finite controls, and publication.

## The actual scalar remains the common construction target

For a positive odd ordinary source q, let

\[
q_{i+1}=U(q_i)=(3q_i+1)/2^{g_i},\quad
g_i=v_2(3q_i+1),\qquad h(q)=\sum_{i\ge0}g_i/3^{i+1}.
\]

The parent R8-G1--G2 proves unconditionally

\[
\frac12<h(q)\le1+\frac{\log_2q}{3},\qquad
h(Uq)=3h(q)-g_0,\qquad
q\longrightarrow1\ \Longleftrightarrow\ h(q)\in\mathbb Z[1/3].
\]

The real scalar is already constructed and effectively enclosed.
Its universal triadic arithmetic is not proved. All new uses refer
to this actual scalar, except where a candidate or symbolic sequence
is explicitly identified as such.

## 1. Every denominator-eight carry excursion has one affine bound

The surviving minimum phases are `7/8,5/8`. Write
`h_i=p_i+k_i`, where k_i is a nonnegative integer. The exact gap
equation is `g_i=b_i+3k_i-k_(i+1)`, with b alternating `2,1`.
Normalize the physical state by

\[
Y_i=q_i/2^{k_i}.
\]

The complete ordinary and scalar equations combine to give

\[
Y_{i+1}=3Y_i/2^{b_i+2k_i}+1/2^{b_i+3k_i}.
\]

This expression removes the destination carry. Every positive carry
is bounded by the unit-carry affine map, uniformly in the size of
the actual carry. [CARRY_RETURN.md](CARRY_RETURN.md), R9-C2, proves
that every paid first excursion from scalar 7/8 back to 7/8 has

\[
\boxed{r\le P(x)=\frac{9x+5}{32}\le\frac x3.}
\]

If its length exceeds two odd steps, the sharper bound is
`r <= (81x+605)/1024 < P(x)`. This is an all-length written theorem,
with a Lean arithmetic and monotonicity core; it is not an
extrapolation from bounded carries.

The unpaid low block L has gaps `(2,1)` and satisfies
`L(q)+7=(9/8)(q+7)`. Before a paid excursion there are exactly
`m=(v_2(q+7)-1)/3` such blocks. R9-C3 gives a finite actual return
budget of `2 bl(q+7)+1` odd steps. R9-C4 proves descent for **every**
paid excursion whenever m<=10. For the two-step paid block P itself,
the complete source class descends for m<=10 and expands for m>=11.

If any ordinary source has h=7/8, a global least such q must satisfy

\[
\boxed{
v_2(q+7)\in\{34,37,40,\ldots\},\quad
q\not\equiv2\pmod9,\quad v_3(16q+29)\le23.}
\]

These conditions remain compatible with infinitely many positive
integers. A total supplied-candidate reduction and a total one-return
transformer are implemented; their outputs preserve equality but do
not assert it. Iterating returns after arbitrarily long low runs is
still the missing global step.

## 2. A complete rational denominator has bounded prime exponents

Write a putative actual rational scalar in lowest terms as
`a/(3^r d)`, with d coprime to three. The parent phase test applies
to a complete tripling coset modulo d.

[PHASE_RIGIDITY.md](PHASE_RIGIDITY.md), R9-P1--P2, extends the
prime-power result to mixed denominators. If

\[
d=2^a\prod_{p\in P}p^{k_p},\quad
t_p=\operatorname{ord}_p(3),\quad w_p=v_p(3^{t_p}-1),\quad
\ell_p=\max_{q\in P\setminus\{p\}}v_p(t_q),
\]

then an actual rational scalar requires

\[
\boxed{k_p\le w_p+\ell_p,\qquad
a\le3+\max_{q\in P}v_2(t_q).}
\]

Empty maxima are zero. Thus each fixed odd prime support permits
only finitely many residual denominators, with an explicit divisor
bound. This uses full projected residue fibers and the retained
verified ordinary floor, not separate tests on the prime factors.

The exact doubling identity additionally excludes every complete
odd d>1 dividing some `3^j-2`. A qualified prime-only criterion from
complete Gauss sums excludes sufficiently large tripling cosets.

There are explicit sharp surviving families. For N>=6,
`d=2(3^N-1)` has a phase of mean `3/4+1/(4N)`, with a canonical word
that meets every forward pressure-clock inequality. At N=6 this
is d=1456, mean 19/24, and starting phase 729/1456. It attains the
binary support bound for prime support `{7,13}`. Actual positive
ordinary sources approximate these scalars through arbitrarily long
literal prefixes. The periodic rational realization is negative;
none of this constructs an infinite positive counterexample.

## 3. The same pressure maximum has an additional binary gate

[MAXIMUM_GATE.md](MAXIMUM_GATE.md), R9-M1, keeps the parent's
escaping-component product explicitly source-qualified. If the
actual scalar at its **same attained maximum m** has reduced
denominator exactly eight, with no ternary factor, the parent's
scalar ceiling forces h(m)=5/8. The new all-carry clock bound then
forces at least eight low pairs before the first paid return:

\[
\boxed{v_2(m+5)\in\{26,29,32,\ldots\}.}
\]

This maximum is not identified with the global least 7/8 source.
Clearing a ternary denominator moves the source and does not retain
the maximum's prefix ceiling. The qualification is essential.

## 4. Actual source values have a singular continuous limiting law

[ACTUAL_SCALAR_LAW.md](ACTUAL_SCALAR_LAW.md), R9-L1--L5, proves
that for uniformly chosen positive odd q<=X, the distribution of the
actual h(q) converges weakly to

\[
H=\sum_{i\ge0}G_i/3^{i+1},\qquad
\mathbb P(G_i=g)=2^{-g},
\]

with independent positive geometric G_i. The attachment uses exact
ordinary parity cylinders and the unconditional actual scalar tail.
It includes an explicit bounded Lipschitz error estimate.

The limit has no atoms and is purely singular: its Fourier transform
does not decay on `2 pi 3^N`, and the affine recursion preserves its
Lebesgue decomposition. Consequently, for every fixed positive D,
the actual sources with `h(q) in D^(-1) Z` have density zero.

This is consistent with **every** actual h(q) being triadic rational.
The denominator exponent may grow with the source, and density zero
does not pass to a countable union. The result supplies a rigorous
actual source law, not a random model for one fixed orbit.

## 5. What the arithmetic literature does and does not provide

[ARITHMETIC_RIGIDITY.md](ARITHMETIC_RIGIDITY.md), R9-A1--A4,
identifies the exact carry freedom. Every binary sequence s_j gives
positive bounded gaps

\[
g_{2j}=2-s_j,\qquad g_{2j+1}=1+3s_j
\]

with discounted sum exactly 7/8. A nonperiodic automatic s_j is
allowed. This explicitly prevents deriving periodic raw gaps merely
from a rational discounted value. These are symbolic infinite words;
every finite prefix has a literal ordinary realization.

More generally, for every real target x>=1/2, every fixed odd modulus
M and residue a, and every N>=1, an actual positive odd q congruent
to a modulo M can be constructed with

\[
\operatorname{bl}(q)\le3N+3\lfloor x-1/2\rfloor+\operatorname{bl}(M)+1,
\quad
|h(q)-x|<\frac{4N+2\operatorname{bl}(M)+5}{6\cdot3^N}.
\]

Thus finite odd congruence restrictions and finite scalar precision
alone cannot exclude these target phases. The source changes with N.

Primary texts by Tao, Solomyak, Adamczewski--Bugeaud,
Corvaja--Zannier, and Kurlberg are inspected at the stated theorem
boundaries. The proposed radical/S-unit coordinate reproduces an
existing exact equation; it does not supply the missing independent
arithmetic relation. No external theorem is invoked with its height,
normalization, or noncancellation hypotheses omitted.

## Formal and computational scope

The three Lean modules contain 30 finite theorems and nine definitions.
Their scope is the scalar block algebra, arbitrary finite affine
comparisons, complete carry power identities, clock inequalities,
and candidate transport. The real series, probability law, full CRT
existence, modular group arguments, and actual all-time attachment
remain written proofs.

`run_exact_controls.py` executes the four finite lanes, binds their
scientific inputs, and rejects disabled Python assertions. The
normal and optimized executions, fresh Lean compilation and axiom
audits, sibling reviews, and complete-checkout repository gate are
recorded in the report. None is presented as a proof of Collatz.

**First global obligation:** constrain the complete later carry
sequence of one unchanged positive ordinary source strongly enough
to end its returns or construct its triadic scalar certificate.
The results above constrain that task and rule out several shortcuts;
they do not yet supply its universal construction.
