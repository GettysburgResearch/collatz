# Full-problem proposal and research synthesis

**Collatz is not proved by this packet.** The complete formal conclusion is
an implication from two explicit estimates for finite rational sums over
ordinary trajectories. Neither estimate has been established at every
ordinary target. The accompanying written analysis proves the converse,
so the proposal imposes no extra stopping-time hypothesis.

The six-hour pass began at 22:44:49 UTC on 26 November 2026 and continued
through 27 November. Three Astra 6.2 agents attacked cycles, escape and
global arithmetic in parallel with the root's formal assembly and literature
work. This document identifies the full mathematical target, the deductions
retained from those attacks, and their exact proof boundaries. The
[packet guide](README.md) retains the earlier checkpoints.

## The final Lean statement

Let `U` be the actual accelerated odd Collatz map. Set

\[
 d(n)=\begin{cases}1/4&n<13,\\1+1/(32n^2)&n\ge13,\end{cases}
 \qquad D_k(x)=\prod_{i<k}d(U^i x),
\]

and define the finite rational energy

\[
 E_{K,H}(y)=\sum_{k=0}^K
   \sum_{\substack{1\le x\le H\\x\text{ odd}\\U^k x=y}}
                  \frac{D_k(x)}{x^3}.
\]

Every visit is counted, with the real ordinary source and actual iteration.
The two assertions constituting `EnergyCriterion` are

\[
 \begin{aligned}
 &\forall K,H,y,\quad E_{K,H}(y)\le8,\tag{A}\\
 &\forall\epsilon\in\mathbb Q_{>0}\ \exists Y\in\mathbb N\
   \forall K,H\in\mathbb N\ \forall y\ge Y,\quad
                         E_{K,H}(y)\le\epsilon.\tag{B}
 \end{aligned}
\]

The depth cutoff `K` and source cutoff `H` remain unrestricted in (B).
[RationalEnergy.lean](root/RationalEnergy.lean) proves

```lean
theorem energy_criterion_implies_collatz
    (criterion : EnergyCriterion) : Universal
```

Here `Universal` is convergence of every positive natural number under the
usual full Collatz map, through the exact odd-part interface in
[PotentialAssembly.lean](root/PotentialAssembly.lean).

The proof follows one source. If it never reaches an odd state below 13,
its own energy term is at least `1/x^3` at every depth. Assertion (B) then
bounds all its targets. On that bounded set every edge multiplier has one
fixed margin above one, making its weight unbounded and contradicting (A).
The six small odd starts are handled by checked finite paths. This argument
does not need a density statement or a presumed orbit classification.

The [written converse](root/RATIONAL_ENERGY.md) uses the telescoping bound
`product (1+1/(32*n^2)) < 14/13` on distinct high states. It bounds the
energy at every nonperiodic target by 4 and at target 1 by `16/3`, without
assuming convergence. Additional positive cycles violate (A). If all starts
converge, exclude the finitely many targets visited by sources at most `M`;
the remaining energy is at most `1/M^2`, giving (B). Thus (A) is precisely
the cycle-uniqueness part, and their conjunction is equivalent to full
convergence in the written argument. Only the joint forward implication is
formalized in the present module.

## The proposed analytic route to those estimates

The [prefix-adaptive ternary Green series](global/ADAPTIVE_GREEN.md) uses
the least positive odd representative `r` at each prefix and the boost

\[
 b(r)=1+\frac1{2\max(r,13)}+\frac1{12\max(r,13)^2}.
\]

It has an explicit finite Haar integral. Its rationally rounded version
`G^Q` dominates the energy through

\[
                    E_{K,H}(y)\le 6\,(G^Q(y))^2/y^3.
\]

The finite coefficient inequalities are checked in
[AdaptiveGreen.lean](global/AdaptiveGreen.lean). The infinite construction,
the comparison of sums, and the ordinary simple-path arguments are written
proofs. They give uniform normalized bounds at nonperiodic targets, a
polynomial source tail away from trajectories of any fixed finite set of
sources, and a summable error in the ordinary positive recursion.

The outstanding pointwise estimate concerns those fixed-source trajectories
themselves. A putative escaping source contributes a positive persistent
normalized term along its own future. Haar integrability and a small error
in a coarse residue distribution do not eliminate that contribution. No
uniform-decay conclusion is inferred from either average.

## Original-law source analysis and the normalization still to prove

The [Poisson probe](escape/POISSON_SOURCE_PROBE.md) gives an exact signed
binary Fourier expression under the original geometric gap law. It can
read the actual multiplier of one specified ordinary source at finite depth,
uniformly in the smoothing width. The
[two-width isolation](escape/FIRST_RETURN_POISSON.md) removes every terminal
other than 1 with a power-saving error. These are concrete ways to retain
the physical source in a Fourier calculation.

The [critical profile](escape/CRITICAL_POISSON_PROFILE.md) refines the
macroscopic jump. Put `D=log(4/3)` and
`sigma^2=2*(log 2)^2/D^3`. For the mean-zero Schwartz probe at depth

\[
 k=\left\lfloor(1+\beta)\log R/D+\xi\sqrt{\log R}\right\rfloor,
 \qquad t=R^{-\beta},\quad\beta>0,
\]

the source-qualified limit is

\[
           -\frac{\pi I d_1}{2}\,\Phi(\xi/\sigma),
           \qquad I=\int_0^\infty g.
\]

Its proof supplies a real-marked local limit for the two actual first-hit
clocks and averages the native lattice. The width is independent of `beta`;
replacing this correlated statistic by the scalar independent-clock cutoff
would give a different width. The amplitude still contains the ordinary
basin density `d_1`.

The associated exit law `E` has reciprocal moment
`integral u^(-1) dE = (D/2)*d_1`. Its Mellin transform has residue `d_1/2`
at zero and a genuine nonreal lattice pole. The
[closed-support neighborhood theorem](escape/CRITICAL_SUPPORT_NEIGHBORHOODS.md)
gives a positive lower limit for `sqrt(log(1/epsilon))*|K_epsilon|`, with
the exit measure retained in the local version. These conclusions retain
the named ordinary passage, mixing, trace and reciprocal-tail inputs;
they are not Lean theorems in this packet.

The [positive trace budget](escape/POSITIVE_TRACE_BUDGET.md) puts this
normalization beside an established identity. With `h(x)=lim rho_k(x)`,
`kappa=D/2`, and positive escape charges `H_C`,

\[
 \sum_{x>0\text{ odd}}\frac{h(x)}{x(3x+1)}
              +\sum_{C\text{ escaping}}H_C=\kappa.
\]

The total budget and its exact finite-depth first difference are **prior
results of Weaver 176**, Theorem 2 and equation (6). This pass adds an
actual-tree componentwise derivation, a power-decaying physical tail for
the nonperiodic summands, and exact finite controls showing both signs of
the finite-part increments. The restricted sum over the basin of 1 is
`kappa*d_1`. Proving its value equals `kappa` would settle the full problem
under the retained all-unit predecessor floor. That value is unproved.
[Stationary selection](escape/STATIONARY_SELECTION.md) constructs bounded
auxiliary harmonic perturbations preserving any prescribed finite data and
polynomial exit moments while changing the reciprocal moment. The true
individual-depth law is therefore a necessary ingredient of a uniqueness
argument; the perturbation does not alter that law or the actual basin.

The final [stopped-row test](escape/STOPPED_RATE_TEST.md) and
[endpoint-mark test](escape/ENDPOINT_RATE_TEST.md) give a second full-problem
proposal, stated entirely in terms of the original finite-depth laws. The
nonnegative statistic `Q_j^*` retains both the positive depth difference and
positive changes of the real-prefix distribution in the explicit endpoint
band of width `1/(j+1)`. Finite rational truncations approximate it with
a proved absolute error at every depth.
On any escaping component,

\[
 Q_j^*\ge c(2/3)^j\exp(c'\log j\log\log j)
\]

eventually, using the actual placed depth differences and Weaver 174's
rise-group bound. At every extra cycle it instead satisfies
`Q_j^* >= c_y*gamma^j` with `gamma >= 9/10`. Thus one unbounded subsequence
with `Q_j^* = O(j^A*(2/3)^j)` for a fixed finite `A` would settle both parts.
This **upper estimate remains open**. The endpoint crop is necessary:
unrestricted real-prefix CDF distances already have atoms of size
`(3/4)^(j+o(j))` on the known transient fibre at 5.

[Marked solenoid mixing](escape/MARKED_SOLENOID.md) extends the retained
unmarked Haar theorem to covers carrying the actual integer label. Its
quantitative bound permits a subexponential cover range, but does not
resolve a specified arithmetic fibre of mass `3^(-d)` at clocks comparable
to `d`. The full dyadic-clock cover has an exact obstruction. These scope
limits are part of the theorem, rather than an inferred pointwise estimate.

## Cycle arithmetic with the full denominator

The [Mellin rank theorem](arithmetic/MELLIN_RANK_SPACING.md) applies the
precise Lindelöf exponential-sum estimate and the Robert–Sargos fourth
derivative bound. It controls close pairs at every amplitude up to
`C*p^(11/20)`, and gives the minimum-size exponent
`1000/479+11/20=2.63768...` under the exact ordered three-band assumptions.
The RH input is supported by the November 2026
[MIT verification record](https://math.mit.edu/~drew/grh/); the external
archive was not rebuilt or imported here. The retained two-logarithm
irrationality upper exponent is three. No contradiction between these
exponents is asserted.

[Rank division](arithmetic/RANK_DIVISION.md) constructs a common short
integer linear combination of the phases of one candidate cycle. It is
positive and `O(log s)`, and retains the **complete reduced denominator**
at every rank. On an ordinary candidate some same integer relation occurs
on many disjoint chronological windows. The three finite identities are
checked in [RankDivision.lean](arithmetic/RankDivision.lean). The
[tagged construction](arithmetic/RANK_DIVISION_TAGS.md) additionally
preserves chosen finite ternary pasts and dyadic future words simultaneously
at all phases. Its induced
affine forcing takes both signs. It consequently does not supply a smaller
ordinary cycle. The 3-adic two-logarithm argument also bounds from below the
number of nonzero coefficients needed as the depth grows.

[Local chronological rank](arithmetic/HANKEL_RANK.md) proves that every
sufficiently long consecutive window of `m+1` translated phase columns has
full rational rank, uniformly over the sizes of the proposed coefficients.
The length is explicit in `min(1<=d<=m)||d*h/p||`; for polylogarithmic `m`
it is polylogarithmic under a finite two-logarithm bound. Its two-adic proof
retains the boundary doublings. It supplies no determinant-size estimate
that would contradict ordinary integrality.

The [exact binary-past cubes](arithmetic/BINARY_PAST_CUBES.md) address the
new energy theorem in PR201. Arbitrarily large Boolean cubes of genuine
fixed-total binary words attain `E=|A|^(log₂6)`, inside a physical band of
ratio below `8/3`. Every word can occur on disjoint intervals of one finite
ordinary path in that same band. A separate CRT construction realizes the
exact integer energy at physical endpoints in one prescribed dyadic class.
This prevents using a false stronger local restriction estimate to close
the cycle argument. Periodicity of one ordinary orbit would be additional
information.

## Diophantine restrictions at physical height

The [positive S-unit theorem](global/POSITIVE_SUNIT_SHADOWS.md) applies the
Evertse–Schlickewei–Schmidt finiteness theorem to positive subsums of the
corrected orbit. It rules out syndetic representations by a fixed number
of positive terms from any fixed finite-rank multiplicative group. It
allows the complementary prime powers to be unbounded.

[Physical-height shadows](global/HEIGHT_SHADOWS.md) replaces elapsed time
by `H_i=log₂(a_i+1)`. On any hypothetical escaping source, every sufficiently
late phase is followed within `O(H_i)` steps by a prescribed finite block
avoiding the specified thick and sparse ternary approximants. Its extension
excludes all positive rational anchors of polynomially bounded height at
the same dates. The constants retain the ineffective Subspace input.
The result controls one actual ray and permits arbitrarily slow escape.
It does not force that ray to admit one of the excluded approximants.

[All-height transfer](global/ALL_HEIGHT_TRANSFER.md) combines PR200's
fixed-height pointwise clock with one optimized cutoff and a height-drop
restart. Every positive odd source has, within `O(log(n+1))` steps, a target
whose entire positive rational approximation score is
`O(sqrt(log(x+1)*log(3+log(x+1))))`. This is in the returned target's own
height. The typical ordinary census has a sharper logarithmic scale, and
neither assertion evaluates the stationary reciprocal moment.

[Ordinary relations](global/ORDINARY_RELATIONS.md) gives an unconditional
integer-root bound for polynomial relations on actual consecutive states,
and a branching version for any finite family of forward and inverse paths.
At a density-one set of dates on an escaping ray, all relations within the
displayed simultaneous degree, coefficient and clock budget are identities
already forced by the affine words. The finite integer-root kernel is
checked in [OrdinaryRelations.lean](global/OrdinaryRelations.lean).
Producing an independent relation from a positive limiting trace would
close this route; the present concentration arguments do not produce it.

The [adelic clock calculation](root/ADELIC_CLOCK.md) tests a different use
of arithmetic algebraicity. The actual series `sum 2^(A_i) z^i` has the
rational 2-adic value `-3a` at `1/3`, but its disk capacities have product
`2^(liminf A_i/i-limsup A_i/i)<=1`. Bost–Chambert-Loir's strict capacity
criterion therefore still needs a continuation or interpolation estimate.
The first positive omitted real term gives an exact lower bound at the
mixed truncation scale; no strict gain is supplied by the arithmetic clean
blocks alone.

[Critical conformal atoms](global/CONFORMAL_ATOMS.md) tests a different
operator route. An escaping component would give a finite positive atomic
eigenmeasure for the squared inverse operator. The note constructs
uncountably many such eigenmeasures on ternary irrational points, each
compatible with positive real branches, odd binary branches, and ordinary
integer realizations of every finite subdiagram. These are not positive
integer counterexamples. They show that uniqueness of finite conformal
measures cannot establish the required exclusion; an extra condition
selecting one ordinary integer in the infinite diagram is necessary.

## Repository intake and verification boundary

The final intake includes PR200 at
`7af83b786636abba2f44fe8c81441153331377fc`, PR201 at
`6795369ac4e604eec342c0b6c08b9a14cd2ca4ec`, and PR192 at
`ae48a04cca29abe5fc8273bcda45e7eee0874896`, together with the earlier frozen
heads in the packet receipts. Their relevant new proofs were read; their
bulk computations were not rerun. PR200's fifth absolute moment and
third-layer extension go beyond the range of this packet's method-specific
fourth-energy width calculation. PR201's binary-past energy, forced triple
descents and explicit third-band occupation threshold were retained with
their stated hypotheses. Neither is treated as full cycle exclusion.

The last intake adds PR200's exact exclusion through odd period `10^1000`
under its width and minimum hypotheses, PR201's tightened first-clearance
ordinary-source law and canonical path construction, and PR192's
fixed-terminal signed escape functional and full-mask moment obstruction.
The period exclusion is a substantial restricted-class theorem. It has no
proved effective overlap with the asymptotic finiteness result. The new
source laws and signed functionals do not supply either open upper estimate
in this proposal. [Final intake](../../reports/astra-six-hour-20261127/FINAL_INTAKE.json).

[LEAN_FINAL.json](../../reports/astra-six-hour-20261127/LEAN_FINAL.json)
records seventeen fresh strict builds and 136 public axiom inventories.
[Final review](../../reports/astra-six-hour-20261127/FINAL_REVIEW.md) identifies
the exact finite controls and separates written from formal claims. The formal claims
are the finite kernels and the conditional implications identified above.
The analytic limits, deep external inputs, and written converse remain
outside that audit. No instance of `EnergyCriterion`, universal pointwise
decay estimate, or complete Collatz proof is supplied.
