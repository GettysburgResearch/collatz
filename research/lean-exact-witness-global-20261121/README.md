# Exact witnesses and the global Lean closure attack

**Status: OPEN for Collatz and for the requested residue implication.**
The results include kernel-checked equivalences for arbitrary finite witnesses,
an all-exponent branch of a global induction, and source-witness induction.
The latest checkpoint uses the published Evertse--Schlickewei--Schmidt
S-unit theorem to prove a new written finite-core return theorem for actual
segments with sparse binary endpoints. On every escaping odd orbit, bounded
binary-run times have upper Banach density zero. Hence every exponential
run weight with base greater than one has divergent orbit averages. Under
the pinned canonical analytic inputs this also forces divergence of the
actual terminal energy for those weights, including an interval with finite
canonical forcing. Its remaining transport commutator is not bounded.
The finite floor-return arithmetic, all-clock correction bound, and exact
fixed-block valuation loss are checked in three new core-Lean modules.
The preceding checkpoint combines least-target induction, minimum source grade,
maximum source value at that grade, and the original target floor in one
canonical counterquery. Its exact remaining proposition is `FloorIntervalStep`,
equivalent to full Collatz and the original residue implication. It is unproved.
The preceding checkpoint supplies a strict-grade interval rule from every
sufficiently separated negative low block, and an unconditional canonical
source selector for every target at least 177. The selected source's whole
future orbit stays below half the original target, making its successful
return cones actual original-target descents. The remaining certificate
language has an actual prefix ending at 11 and fixed tail `[1,2,3,4]`.
A separate global attack proves binary-run compactness and
quantitative high-run occupation on every escaping ordinary orbit. The joined
signed-shadow and modular-forcing arithmetic is checked in Lean; the complete
binary combinatorics and occupation deductions have written proofs.
A complete recursive cover of the canonical prefix states is still missing.
These results do not prove the implication or Collatz.
There is no exponent bound, witness-length bound, `sorry`, or conjectural axiom
in the new Lean modules. Lean 4.34.1 is used without Mathlib or other packages.

## Latest checkpoint: S-unit return separation and subcritical run weights

This continuation starts from published checkpoint twelve at
`431d858d1ac92e88f4a58f6610c0d67733dc7242`. Five active peer branches
advanced. The exact newly inspected heads, files, and literature inputs are
recorded in
[the source snapshot](../../reports/lean-exact-witness-global-20261121/literature-closing/SOURCES.json).
The primary literature was used to attempt closing arguments on the actual
integer orbit and canonical measure; no literature theorem was installed
as a conjectural Lean axiom.

### Sparse endpoints force an actual finite-core return

[Arithmetic return](LITERATURE_ARITHMETIC_RETURN.md) proves the following.
For each binary run bound `S`, there is one finite set `H_S` of positive odd
step separations. For every fixed `h` outside that set, there is a finite
threshold `M(S,h)` such that an actual `h`-odd-step segment whose two endpoints
have at most `S` runs must have an intervening odd input below `M(S,h)`.
All actual valuation gaps remain unrestricted.

The proof expands the two endpoints into at most `4S` signed powers of two
and retains every term of the exact Collatz correction. The published
S-unit theorem makes projective ratios in nondegenerate zero relations of
each fixed length finite. An endpoint-only minimal zero relation would
force `h` into `H_S`. Otherwise a positive correction term shares a
nondegenerate relation with the largest initial endpoint term, giving a
positive lower bound for the relative correction. An actual segment above
the finite floor has a smaller relative correction, a contradiction.

The exceptional set is fixed before `h` is chosen. The correction ratio
and finite threshold may depend on `h`. Progression packing consequently
proves that on every escaping odd orbit, times with at most `S` binary runs
have **upper Banach density zero**. Every weight `rho^runs`, `rho>1`, has
divergent averages, uniformly over the starting position of a long time
window. The S-unit theorem and these density deductions have written proofs;
they are not included in the Lean declaration count.

### The finite return arithmetic is kernel checked

`Collatz/SegmentFloor.lean` proves, for the actual supplied word `W`, length
`h`, correction `C`, and initial state `n`,

    M*C + 3^h*n <= 4^h*n

whenever every odd input of that segment is at least `M>0`. Its theorem
`ratio_forces_return` then proves that

    3^h*n <= Q*C

forces an actual ordinary iterate, at a clock strictly below `total W`,
to be less than `Q*2^h`. This is the finite return threshold used in the
written S-unit argument. The Lean result is uniform in the word and all
its gaps; the deep input supplying `Q` remains explicitly outside Lean.

`Collatz/ArithmeticPrecision.lean` proves at every positive ordinary clock
of a least bad odd target that

    t*2^(k+v) <= (3*t+1)*C_k,

with the exact odd core reached at the actual later clock `k+v`. This is
the checked reason the direct whole-identity small-product attempt does
not supply the needed Diophantine estimate.

`Collatz/AffineBlockPrecision.lean` proves for every actual repeated parity
block, with multiplier `3^r`, clock `K`, and signed displacement
`Delta(n)=3^r*n+C-2^K*n`,

    2^(K*j)*|Delta(n_j)| = 3^(r*j)*|Delta(n_0)|.

Thus each repetition consumes exactly `K` dyadic valuation units. Any
expanding block cannot repeat indefinitely on a positive integer.
[The termination analysis](LITERATURE_WITNESS_TERMINATION.md) retains the
remaining changing-block obligation; it does not infer global termination
from separate countdowns.

### Canonical forcing is finite for newly admissible weights

[Canonical energy](LITERATURE_CANONICAL_ENERGY.md) proves a finite absolute
edge-variation budget, including killed exits, by summing each original
charge's exact on-path and side-branch current. It also proves that the
standard homogeneous sector condition fails on the actual predecessor tree
of five, even though the symmetrized form on an escaping component is
recurrent.

Using the new S-unit result, for every `rho>1` and fixed truncation `L`,

    sum min(rho^runs, rho^L)*e_N  ->  rho^L*b_infinity.

For `rho=4^alpha`, `0<alpha<1/40`, the same actual canonical source satisfies

    sum d(n)*rho^runs(n)
      <= 5*3^(alpha-1)*(1-alpha)*A/(1/40-alpha) < infinity.

This opens an interval of weights that both detect escape and have finite
forcing. The exact finite-Green identity leaves the multiplication/forward
transport commutator and weighted boundary drift in equations (45)--(49).
No uniform upper bound for those terms, no zero-escape conclusion, and no
exclusion of nontrivial cycles is claimed. The entire canonical analysis
retains the stated predecessor-population and envelope qualifications.

[Checkpoint-thirteen execution and scope](../../reports/lean-exact-witness-global-20261121/literature-closing/)
records the three new-module compilations, 32 new public theorems, and
the expanded axiom audit. The global proposition `FloorIntervalStep` and
the original residue implication remain unproved.

## Previous checkpoint: the joint minimum and the canonical terminal energy

This continuation starts from published checkpoint eleven at
`8ef9bf0d828fc533721dee1f90c5d78fac80ad39`. Four peer branches advanced
while the attack continued; their actual new heads and selected file hashes
are recorded in
[the delta snapshot](../../reports/lean-exact-witness-global-20261121/joint-minimum/SOURCE_DELTA.json).

### One counterquery with every legitimate induction resource

[Joint minimum](JOINT_MINIMAL_COUNTEREXAMPLE.md) proves that a hypothetical
counterexample yields one complete supplied source with all of the following
properties simultaneously:

- The target `t>1105` is least bad and satisfies `t=3 mod4`.
- The source has minimum complete grade among sources capturing `t`, and
  maximum numerical value at that grade. The source ceiling
  `S<=2^(sum Gamma)` makes this maximum legitimate.
- The original, unrestricted `Hyp Interval` holds at the selected grade.
  A failed lower-grade child target `y` would have `t<=y`, so its source
  would also capture `t`, contradicting the minimum.
- Every larger source at the same grade multiset has the analogous full
  arbitrary-target hypothesis. This incorporates PR180's source-value tie.
- The selected word itself is `P++[1,2,3,4]`, with nonempty bounded-four
  prefix `P` ending at 11, initial exponent one through three, and
  `S+1<t<=2S+1`.
- Every future ordinary source state is at most `(t-1)/2`, and every
  nonempty literal source prefix strictly contracts its linear coefficient.

No separately selected floor witness is substituted after choosing the
minimum source. `JointMinimalCounterexample.lean` proves both
`collatz_iff_floor_interval` and `original_residue_iff_floor_interval`.
The theorem supplies the combined resources; it does not prove the
remaining universal successful-return proposition `FloorIntervalStep`.

### The entire terminal energy has the same original source measure

[Terminal Dirichlet run mass](TERMINAL_DIRICHLET_RUN_MASS.md) is a new
written deduction under the latest pinned canonical harmonic and Green
inputs. Write `R` for the canonical potential, `F` for its escape label,
`d` for its finite original charge, and `e_N` for the live endpoint
pushforward of `N` times its Cesaro Dirichlet energy. It proves

    || e_N - (1/N) sum_(j<N) L^j(dF) ||_1 -> 0.

The killed-boundary remainder tends to zero by a proved overlap squeeze.
This identifies the entire measure, beyond equality of scalar total masses.
Using the binary-run occupation theorem with bounded truncations then gives

    liminf sum min(4^runs(q),4^k) e_N(q) >= (1+3k) b_infinity,

where `b_infinity=sum dF`. If an escaping component exists, the terminal
run-weighted energy diverges. The same measure has actual contact-reset
limit `F^2 eta_0` in total variation. No uniform higher-norm estimate is
inferred from this limit.

These analytic deductions are source-qualified written proofs. The complete
binary combinatorics retain the same written status as in checkpoint ten.
Neither a finite upper bound for that weighted energy nor the required
universal arithmetic return is proved. The new Lean declarations contain
no analytic axiom.

[Checkpoint-twelve execution and scope](../../reports/lean-exact-witness-global-20261121/joint-minimum/)
records the focused new-module compilation and expanded audit.

## Previous checkpoint: actual source progress and the original target floor

This continuation starts from published checkpoint ten, PR177 head
`46a76145ef21e93318eff25da8cf00c5342fd7d2`. The three new core-Lean modules
prove unbounded structural statements on the same finite supplied source
certificate. The proof and execution record is under
[reports/source-progress](../../reports/lean-exact-witness-global-20261121/source-progress/).

### A finite negative shadow that gives a strict original-grade step

[Negative-shadow return](NEGATIVE_SHADOW_RETURN.md) proves that **every**
negative odd shadow `-m`, with `m>0`, has a nonempty prefix satisfying

\[
1\le r\le3m,\qquad 2^{A_r}\le3^r,\qquad 0<A_r<2r\le6m.
\]

The proof keeps the complete affine correction. If all prefixes through
`3m` contracted, their correction would be at least `m*3^(3m)`, contradicting
the negative endpoint. This requires no eventual behavior of negative orbits.
If a positive odd source satisfies `q+m=2^D*u` with `D>=6m`, the signed
prefix lifts to an actual positive source prefix before clock `D` and ends
at an odd `q'>q`.

`SourceOrbitProgress.advance_certificate` advances the **given** complete
witness along an arbitrary actual ordinary path. A positive clock ending
outside the terminal cycle strictly lowers its original grade.
`odd_growth_interval_rule` retains the same initial exponent and uses that
strict decrease at the larger odd core. `negative_block_interval_rule`
therefore closes the **whole original interval** under its original
`Hyp Interval`, whenever the displayed negative-block guard holds.

### A global source selector with a bound on every future state

[The original target floor](ROOTED_SOURCE_FLOOR.md) proves that for every
`t>=177`, setting `L=floor((t-1)/2)`, there is a complete source

\[
S=2^e u,\quad1\le e\le3,\quad
\operatorname{Prefix}(u,P,11),\quad P\ne[],\quad a\le4\ (a\in P),
\]

such that `L<S<=t-1`, `t<=2S+1`, and **every ordinary state after `S` is
at most `L`**. It is selected as a literal cut inside a gap of a supplied
cofinal prefix to 11. The exact source clock, unused suffix, and full
certificate are returned; target convergence is not assumed.

For `t=3 mod4`, `L` is odd, and every future source state is actually below
`L`. Thus a target return `z<=3v+2` at any later odd source endpoint `v`
satisfies `z<t`, even if intermediate target carries exceeded `t`.
Padding paid by the source gap just consumed has the same property, for
arbitrary gap sizes. `target_prefix_cap_closes` consumes an actual target
prefix and closes this return under strong induction on the original target.

[The cofinal complementary domain](STRICT_PREFIX_CONTRACTION.md) supplies
all-word written extractions: strictly coefficient-contracting complete
alphabet-four sources are cofinal, as are known sources larger than every
later odd state. The latter cannot admit any source-growth selector.
The new negative-block rule is therefore an additional exact branch,
while the original target floor supports the complementary target-return
attack. Universal success of those returns is not asserted.

## Previous checkpoint: a canonical global source language and binary-run compactness

This continuation starts from published PR177 head
`9af9118a7e9af870a32a72a4efdcf77e886940ec`. The fresh inventory covers all
122 open PRs in two API pages; the mathematical reading is selective, including
the seven updated recent branches and the older binary-rank program. Exact
source pins and the inspection boundary are in
[LATEST_SOURCE_SYNTHESIS.md](LATEST_SOURCE_SYNTHESIS.md) and the
[snapshot](../../reports/lean-exact-witness-global-20261121/global-synthesis/SOURCE_REFRESH.json).

### One fixed tail for the full residual dispatcher

[Bounded-four normal form](BOUNDED_FOUR_NORMAL_FORM.md) proves that every
complete certificate over gaps one through four is either a finite terminal
motif with arbitrary terminal twos, or is literally

\[
P\;\Vert\;[1,2,3,4]\;\Vert\;2^{[k]},
\qquad \operatorname{Prefix}(q,P,11).
\]

The seven terminal source values are `1,3,5,13,17,45,69`. Nonempty terminal
padding is removed by the existing strict whole-source rank. The residual
`LowIntervalStep` is **equivalent** to `ElevenIntervalStep`: a nonempty
alphabet-four prefix to 11, no arbitrary supplied suffix, and no terminal
padding. The common fixed tail cancels exactly from the grade comparison.
This is an all-length kernel-checked normalization of the entire interval
obligation. The resulting global closing theorem retains
`ElevenIntervalStep` as its explicit, unproved premise.

### A full-word escape constraint from binary runs

[Binary-run compactness](BINARY_RUN_COMPACTNESS.md) uses the number `R(n)` of
maximal one-runs in the binary expansion. For every `S>=1`, put

\[
J_S=4^S-1,\qquad C_S=2^{(2S-1)(2\cdot4^S-1)}.
\]

Every odd `n>=C_S` has an actual iterate with more than `S` runs within
`J_S` odd events and at most `floor(log_2 n)` ordinary clocks. Thus an
eventually bounded-run orbit is eventually periodic inside an explicit
finite core. On every escaping odd orbit, each sufficiently late block
of `4^S` odd states contains a state with more than `S` runs. In particular,
the Cesaro mean of `4^R` tends to infinity.

This covers numbers with arbitrarily many set bits, such as `2^k-1`.
The core is not numerically enumerated. The proof assembles a signed binary
gap, an exact ordinary shadow, and a uniformly reachable alternating
high-block residue. `BinaryRunForcing.actual_pattern` checks the joined
physical conclusion in Lean. The conversion from literal bit patterns to
run counts, the finite-core argument, and the asymptotic consequences are
written mathematics with their formal boundary stated explicitly.

[Original-source run mass](SOURCE_PROGRESS_AND_RUN_MASS.md) retains the same
starting atom and converts the occupation estimate to the ordinary shortcut
clock. Any unchanged-source positive atomic transport containing an escaping
atom has divergent Cesaro run moment. The latest canonical-potential and
contact estimates do not supply the finite-moment upper bound needed to
exclude that alternative. Possible nontrivial cycles remain a separate
closure obligation.

The four new core-Lean modules are `BoundedFourNormalForm`, `SignedShadow`,
`DyadicCoset`, and `BinaryRunForcing`. Source hashes, fresh compiler and axiom
logs, exact structural replays, and the complete-checkout gate are recorded
under [reports/global-synthesis](../../reports/lean-exact-witness-global-20261121/global-synthesis/).

## Previous checkpoint: whole valuation branches and the remaining psi cell

The continuation after published checkpoint eight
(`2efabba9a341839b67ed011d6b878b23730ee51d`) adds three core-Lean modules.
All conclusions below retain the original `Hyp Interval` induction premise.

- [Every odd initial valuation](PSI_ODD_VALUATIONS.md): if `S=2^e*q` and
  `e` is odd, the entire psi query `Basin(2S-1)` closes for every complete
  supplied odd word. When `q=1 mod4`, there is an exact ordinary merger at
  clocks `e+3` and `e+2` between targets `2^(e+1)*q-1` and `2^e*q-1`.
  Halving the known source preserves its whole odd word and strictly lowers
  its initial grade. When `q=3 mod4`, the leading source gap is one and the
  existing source-growth rule applies. There is no bound on `e` or the word.
- [Initial valuation two, first gap two](PSI_EVEN_HEAD_TWO.md): the target
  reaches `27u-7` at the literal tail endpoint `u`. Its two odd residue
  phases either permit target quartering or an actual expanding source
  prefix. This closes every supplied tail in this branch.
- [Initial valuation two, first gap four](PSI_EVEN_HEAD_FOUR.md): the target
  merges with the smaller partner `27u-2`. Three exhaustive ternary cells
  construct actual child source certificates. Two replace the old gap four;
  the third retains it and lowers the initial even grade. The endpoint-one
  case has an exact additional target prefix and preserves its padded tail.

Combined with the existing high-gap, high-initial-valuation, empty-word,
odd-source, and first-gap-one rules, the remaining **psi step** can only
have initial exponent two and first source gap three, with the complete
odd word over one through four. This is a reduction of the psi subproblem
under the interval induction hypothesis. It is not complete coverage of
the larger interval domain: arbitrary non-psi interval queries still need
their own successful rules. The full theorem remains unproved.

The [remaining head-three note](PSI_HEAD_THREE_FRONTIER.md) records its exact
carry and an admissible ternary class where both immediate low-gap inverse
chains stop. A verified smaller merger in that class increases the
highest changed source-grade multiplicity, so numerical descent alone does
not justify its next recursive call.

Fresh combined build and axiom receipts are in
[`reports/.../psi-branches/`](../../reports/lean-exact-witness-global-20261121/psi-branches/).

## Previous checkpoint: whole-prefix repayment and uniform carry returns

Three parallel attacks and the coordinating composition add four core-Lean
modules. These are unbounded path and certificate theorems, with no larger
finite verification threshold.

- [Whole-prefix clock repayment](CLOCK_SYNCHRONIZATION.md) allows source
  and target clocks to become unsynchronized across an arbitrary nonempty
  source prefix. At a funded return, the complete child certificate is
  strictly below the original multiset rank. Proper-prefix clock inequalities
  control the affine corrections. A consumed source gap can fund a remaining
  deficit; the intermediate ranks may increase. A delayed target-word family
  works for every positive source prefix under its exact affine guard.
- [Uniform affine carry returns](LOW_GAP_GLOBAL.md) close every positive
  target `t <= 9q+3` with `t mod 4 = (q+3) mod 4`, for every complete odd
  certificate at `q`, using the original interval induction. In particular
  `9q-1` always returns. The positive-nine carry `9q+2` returns for every
  source word beginning with `[1]` or `[2,1]`, with an arbitrary literal tail.
- [Every valuation-one psi query](PSI_VALUATION_ONE.md) closes without
  inspecting the odd source word. For `S=2q`, the actual target prefix
  `[1,1]` sends `2S-1` to `9q-1`. Deleting only the initial even grade pays
  for the uniform carry return. The result also covers every positive
  `t=2S-1-16k`. Initial exponents two and three have an additional proved
  four-leading-twos handoff in the clock module.
- [Original-source Green coefficients](GLOBAL_GREEN_MERGER.md) prove an
  exact shifted identity at every ordinary clock and characterize strict
  coefficient loss exactly by the occurrence of an even input. The Lean
  module also certifies an all-parameter family used in the written proof
  of negative cubic residuals arbitrarily far out. Written deductions give
  an exact finite loss budget, component capacity, and a component-minimum
  maximum theorem. The real-series deductions are not imported as axioms.

The global obligation remains the same `LowIntervalStep`, refined by these
new successful rules. Whole-prefix repayment is not asserted to occur for
every target. A source-clock decrease is not substituted for the original
rank decrease: the carry note preserves an exact fixed-target cycle in the
unrestricted union of those rules. Likewise, the Green maximum can return
its original source rather than furnish a strictly smaller component minimum.

The refresh includes new work on PR175, PR176, PR178, PR180, PR182, PR183,
PR185, and PR186. Full pins and the precise input boundaries are recorded
in [LATEST_SOURCE_SYNTHESIS.md](LATEST_SOURCE_SYNTHESIS.md). Actual build,
axiom, source-hash, and replay receipts are in
[`reports/.../repayment/`](../../reports/lean-exact-witness-global-20261121/repayment/).

## Previous checkpoint: parallel attacks and the alphabet-four reduction

The new [bounded-gap proof packet](BOUNDED_GAP_ATTACK.md) proves that every
certified odd ternary unit has arbitrarily large certified predecessors using
only gaps one through four before its literal supplied tail. Four is the
sharp alphabet threshold: every complete certificate using only gaps at most
three represents one. These are all-length Lean theorems.

This construction removes an arbitrary gap at least five anywhere in the
complete source word, or an initial even run of length at least four, while
producing a strictly lower-ranked known source above any requested bound.
It has no congruence entrance guard and no insertion-length cutoff. In the
active domain `0 < target <= 2*source+1`, the remaining universal step is
restricted to initial even runs one, two, or three; odd gaps at most four;
and odd targets strictly above `source+1`. The word length and values are
unbounded. `LowIntervalStep` states that remaining premise explicitly.

The parallel attacks add these independent mathematical results:

- [Psi suffix attack](PSI_SUFFIX_ATTACK.md): every complete source word
  `(2 repeated j,1,2 repeated k,a,tail)` with `a>=3` transfers to a
  strictly lower-ranked certificate for `3^k*t`, with `Basin(2n-1)`
  equivalent to `Basin(t)`. Composing it with the asymmetric reset gives
  an actual smaller ordinary merger partner satisfying
  `531441*t+578545=131072*S`.
- [Denominator and merger attack](MERGER_ATTACK.md): every reverse power
  of three has a positive denominator-clearing word, with explicit
  quadratic clock and gap bounds. The complete-source rewrite leaves an
  explicit additive comparison rather than assuming it converges.
- [Retained-even reset](MERGER_RETAINED_EVEN.md): an initial run three
  can be replaced by a shorter initial even run and an odd prefix over
  gaps one through three while the known source grows. The proved cover
  includes every unit odd core except one and the two specified ternary
  cells, and preserves every target in the old interval.
- [Low-interval refinements](LOW_INTERVAL_REFINEMENT.md): a supplied nonempty odd prefix whose
  linear coefficient is at least one can be consumed at the same initial
  even run. The known source grows while the literal-prefix deletion
  strictly decreases its grade. This includes every leading gap one.
  A synchronized-step theorem also closes every case where the target
  admits at least `min(first source gap, initial even run + 1)` halvings.
  The retained-even boundary theorem closes every initial-run-one case
  with first odd gap at least four, including both exceptional interval
  endpoints through explicit ordinary paths.
- [Inverse Green function attack](SECTION_MASS_ATTACK.md): a written
  all-depth theorem proves finiteness of the inverse Jacobian Green
  function at every positive integer for every real exponent `s>1`.
  At `s=2`, the corresponding undiscounted ternary cylinder-density trace
  is summable. This analytic theorem has an exact finite replay but is
  not claimed as a Lean result or as source-mass absorption.

The complete source rewrites have executable exact-integer generators.
The new proofs and actual validation receipts are under
[`reports/.../parallel-attacks/`](../../reports/lean-exact-witness-global-20261121/parallel-attacks/).
The analytic replay is kept in
[`reports/.../section-mass/`](../../reports/lean-exact-witness-global-20261121/section-mass/).
The source refresh inspected the latest PR178 update at
`0bb13b800e4e97f9fd3091b1a3d2e98b49911b7c`; the precise dependency boundaries
are in [LATEST_SOURCE_SYNTHESIS.md](LATEST_SOURCE_SYNTHESIS.md).

## Previous checkpoint: unbounded rewrites in one common induction

The new [proof packet](UNBOUNDED_GAP_REWRITES.md) builds on the latest
PR173 forward section and PR176 source-certificate resets. Its main changes
are mathematical rewrites quantified over arbitrary lengths, rather than
a larger finite search cutoff:

- `GapMultiset.lean` proves well-foundedness of the highest-changed-exponent
  order in Lean core. One exponent can be replaced by any finite number of
  smaller exponents. A graded initial even run makes ordinary steps and
  longer resets decrease the same complete-witness rank.
- `HighGapPump.lean` proves an arbitrary-length guarded family with complete
  source and target splices. The child source and its ordinary certificate
  clock both increase; the source expansion is unbounded. It also proves
  that no single fixed exponential energy base covers all these prefixes.
- `LowGapPump.lean`, added in the continuation after that checkpoint,
  proves an additional arbitrary-length family for source words beginning
  `(1,b)` for every `b≥4`, under the same exact affine guard. It preserves
  the entire supplied tail and also admits expanding, longer children.
- `LowGapLoops.lean` consumes arbitrary initial runs of exponent two and
  exponent one before a `(3,...,4)` block, reducing the reverse comparison
  to a forward-tripling query on the untouched witness tail.
- `UnboundedGapReset.lean` proves a word-parametric paired-entrance compiler.
  It removes the former loop-depth lower bound and provides a new entrance
  that works when the source's initial even valuation is at least three.
- `GapComparison.lean` places actual `(known source, wanted target)` pairs
  in one well-founded induction. Its rule wrappers include all the new
  families without conflating reverse-tripling and psi obligations.
- `GapHandoffs.lean` handles every reverse-tripling first gap `a≥3`
  without an extra congruence guard: it decreases that gap by two and
  transfers to `Basin(p) → Basin(2p+1)`. The latter source gap-one case
  consumes its exact suffix; gap two closes through an ordinary merger.
- `LowGapToPsi.lean` transfers every odd forward-tripling query to a
  psi-forward query with a strictly smaller supplied witness, handling
  source one explicitly. It composes this with the two low-gap loops.
- `AsymmetricPsiReset.lean` supplies an arbitrary-length reset on parent
  sources congruent to two modulo three, the residue reached by that
  handoff. It consumes an initial even run of length at least three,
  preserves the entire odd tail, and permits unbounded source expansion.
  Its nested ternary guards remain an explicit restriction on coverage.

The packet states every guard. Its universal closing theorems still require
a complete dispatcher on all activated pairs. No such dispatcher, and hence
no proof of full Collatz or the original residue implication, is asserted.

The exact source refresh is in
[`LATEST_SOURCE_SYNTHESIS.md`](LATEST_SOURCE_SYNTHESIS.md). New build, axiom,
generator-replay and source-hash receipts are under
[`reports/…/unbounded-gaps/`](../../reports/lean-exact-witness-global-20261121/unbounded-gaps/).

## The target and its exact formalization

Let `T(n) = n/2` for even `n`, and `T(n) = (3n+1)/2` for odd `n`.
`Basin n` means some finite iterate of this ordinary shortcut map reaches 1.

The user's set consists of positive integers satisfying

\[
3^r x+\sum_{j=0}^{r-1}3^{r-1-j}2^{A_j}=2^{A_r},
\qquad 0=A_0<A_1<\cdots<A_r.
\]

`CollatzWitness.E` formalizes this statement with an arbitrary natural number
`r` and an arbitrary function `A : Nat → Nat`, constrained only through index
`r`. The sum is expressed by the exactly equivalent recurrence

\[
C_A(0)=0,\qquad C_A(r+1)=3C_A(r)+2^{A_r}.
\]

Every increasing tuple of integers in the question has nonnegative entries,
so this use of `Nat` loses no tuples. The arbitrary extension beyond `r` is
never inspected. The empty witness has `r=0` and gives `x=1`.

## Kernel theorems in `lean/Collatz/Witness.lean`

| ID | Theorem | Exact scope |
|---|---|---|
| W1 | `witness_iff_basin` | Inductive positive-gap witnesses are exactly the odd members of the ordinary basin. |
| W2 | `witness_certificate`, `certificate_witness` | The entire exponent-gap identity is equivalent to an ordinary finite witness, in both directions. |
| W3 | `schedule_exists`, `e_iff_certificate` | Every original increasing tuple is represented by positive gaps, and every positive-gap certificate supplies such a tuple. |
| W4 | `e_iff_odd_basin` | For every natural `n`, `E n ↔ n % 2 = 1 ∧ Basin n`. |
| W5 | `original_iff_collatz` | The exact implication on residues 129, 257, and 385 modulo 512 is equivalent to convergence of every positive integer. |

W1–W4 do not use the finite reverse cover. W5 uses the imported
`collatz_iff_deep_reverse_binary` theorem of PR146 in its implication-to-Collatz
direction. It does not assume that reverse propagation is true.

The certificate-to-orbit argument cancels the coprime factor `3^r` against
`2^a`, obtaining the legal first odd step and the remaining certificate.
The converse constructs the full gap list from a finite ordinary hitting
time. `schedule_exists` then reconstructs the original tuple by induction,
including arbitrary gaps. The positivity, parity, empty-list case, and final
power-of-two factor are all handled in Lean.

For W5, `x=128k+1` has one of the three specified residues exactly when
`k % 4 ≠ 0`, and `(x+1)/2=64k+1`. Thus the witness formulation and the existing
reverse-basin criterion have identical quantifiers. In particular the output
witness may have any finite length and any finite exponents.

## Current checkpoint: directed and source-witness induction

The latest pass treats the global closing obligation directly. It develops
three sound induction systems, with separate complete-cover requirements:

- `Collatz/DirectedInduction.lean`: directed multiplication comparisons and
  convergence claims in one induction, with powers of two removed before
  evaluating the rank. Affine proof paths have explicit query directions,
  activation obligations and strict decrease guards.
- `Collatz/WitnessEnergy.lean`: a natural-valued rank for complete supplied
  witnesses. Replacing a removed peak by fewer than `C` strictly smaller
  values decreases the sum of `C^value`, even when the new witness is longer.
- `Collatz/SourceWitness.lean`: exact ordinary-prefix removal and insertion,
  including the early-hit guard; separate global closing theorems for strict
  certificate-length descent and witness-energy descent.

The source-witness kernels accept the entire supplied finite witness. They do
not require a bound on the output witness length or its exponents. Their
global conclusions still require an actual complete family of recursive
rules. That family is not asserted by the search output.

The methods, exact scope of the finite search, source pins, and current
unresolved obligations are recorded in
[`DIRECTED_WITNESS_SEARCH.md`](DIRECTED_WITNESS_SEARCH.md).

### Follow-on checkpoint: rank the exponent word itself

The next search uses `sum (15^a)` over the accelerated exponents of the
supplied source witness. This differs from the preceding rank over ordinary
trajectory values. It admits source transformations with both larger child
integers and longer certificates.

The [high-gap construction](gap-search/high/README.md) checks 8,147 guarded
source/target rewrites, uniformly for every first exponent `a≥5` and every
admissible inherited tail. It covers only the ternary guard union
`5950/531441` in its stated grammar. The
[low-gap dispatcher](gap-search/low/LOW_GAP_DISPATCH.md) uses the same
source-gap rank, but its fixed-cell dependency closure retains only one of
16 required deep reverse-tripling cells. These are exact arithmetic search
results; the splice implementations and the unfilled global dispatcher are
not claimed as Lean-verified theorems. The general prefix-energy inequality
used by their rank argument is proved in `Collatz.WitnessEnergy`.

Both packets preserve their exact source pins, scripts and scope. Their
execution receipts and byte identities are in
[`reports/…/gap-search/`](../../reports/lean-exact-witness-global-20261121/gap-search/).

## Earlier interval-induction attempt

The new `lean/Collatz/PsiCompletion.lean` works with the entire interval below
a hypothetical least missing positive integer. Let `H(u)=2u+1`.

| ID | Theorem | Exact scope |
|---|---|---|
| P1 | `normalize_adjacent_below` | Every positive `u<n` with missing `H(u)` normalizes to an odd known source `w≤u`, still with missing `H(w)`. This covers all powers of two in `u`. |
| P2 | `adjacent_even_tail` | If `3u+1=4^(d+1)t` with odd `t`, then `Basin(H(u)) ↔ Basin(3^d t)`. |
| P3 | `adjacent_odd_tail` | If `3u+1=2·4^d t`, then `Basin(H(u)) ↔ Basin(H(3^d t))`. |
| P4 | `initial_basin_even_tail` | The entire even-exponent branch closes because `3^d t≤u<n`. |
| P5 | `least_missing_adjacent` | A least missing `n` supplies `0<u<n`, `3n=4u+1`, `Basin(u)`, and missing `H(u)`. |

P1 is needed because the source furnished by P5 may be even. After P1,
P2–P3 partition every possible positive accelerated exponent, without a
valuation cutoff or a finite residue list.

The remaining odd branch has a concrete unresolved transition. At `d=0`,
the next source is the shorter known witness tail `(3u+1)/2`, but it may
leave the initial interval. At `d>0`, the next adjacent source is `3^d t`,
while the known witness is for `t`. Minimality alone does not transfer it
through multiplication by `3^d` once the value is outside that interval.
Neither the source value nor its witness length has been proved to decrease
across all these transitions. The following quantified family tests this
specific proposed completion.

### An unbounded reset from complete two-letter witnesses

`lean/Collatz/ResetFamily.lean` proves the following for **every** natural `j`.
Set

\[
b=12j+10,\qquad
u=\frac{2^{b+3}-11}{9},\qquad
n=2u+1,\qquad
m=2^b-1,\qquad
z=3\frac{3^b-1}{8}.
\]

The kernel theorem `CollatzResetFamily.reset_family` establishes

\[
\operatorname{Certificate}(u,[3,b]),\qquad
u<m<n,\qquad
\operatorname{Basin}(n)\iff\operatorname{Basin}(z),\qquad
2^j n<z.
\]

| ID | Theorem | Exact scope |
|---|---|---|
| R1 | `source_certificate` | The source has the complete two-letter certificate `[3,12j+10]`, for every `j`. |
| R2 | `target_reset_component` | The displayed target and reset are in the same ordinary basin component. |
| R3 | `reset_amplification` | The reset exceeds `2^j` times the target. |
| R4 | `reset_family` | Bundles R1–R3 with the strict intermediate inequalities. |

The component equivalence passes through `2^(b+1)-1` and
`3^(b+1)-1=2(4z+1)`. The growth bound is proved by induction from
`8·2^(13j+10)<3^(12j+10)`. There is no target-orbit search in this proof.

At `j=0`, the exact values are `u=909`, `m=1023`, `n=1819`, and `z=22143`.
Those values illustrate the universal theorem, rather than supply its evidence.

This disproves a uniform linear size bound for **this displayed reset**.
It does not prove that a target diverges, that no other certificate conversion
works, or that no later ordinary descendant is smaller. The equivalence is a
component equivalence; it is not claimed that `z` itself is a forward iterate
of `n`.

The imported exact closing statement is

\[
\forall k\ge0,\quad 4\nmid k,\quad
\operatorname{Basin}(81k+2)\Longrightarrow
\operatorname{Basin}(27k+1).
\]

This is `CollatzClosure.OpenLemma`, not a theorem in this packet. The ongoing
attack uses a least missing positive integer and the fact that every smaller
positive integer is already in the basin. In parallel, the interval route
tries to prove a strict survivor-count decrease at every scale. No universal
closing bound has been established in this checkpoint.

The first unsupported inference remains the displayed universal implication.
The new equivalences preserve its full strength; they do not discharge it.
The parallel interval/moment attempts did not yield a universal survivor bound,
a bound preventing endpoint mass from escaping, or exclusion of nontrivial
positive cycles. None is inserted as an assumption into W1–W5, P1–P5, or R1–R4.

## Source pins and reuse boundary

The following foundation files are copied without theorem-source edits from
[PR174 at `7034109ed60a26bc49824e1ed43c239ceca81194`](https://github.com/GettysburgResearch/collatz/tree/7034109ed60a26bc49824e1ed43c239ceca81194/research/psi-closure-20261121/lean):

- `Collatz/ReverseBasin146.lean`;
- `Collatz/Closure.lean`;
- `Collatz/Shadow.lean`.

`ReverseBasin146.lean` itself documents its source:
[PR146 at `e238c63a5d57f96bb063b7472498d1977df51951`, `research/upper-bit-mergers/ReverseBasin.lean`](https://github.com/GettysburgResearch/collatz/blob/e238c63a5d57f96bb063b7472498d1977df51951/research/upper-bit-mergers/ReverseBasin.lean).
Its only adaptation is the already-published core-only shim from PR174.
These reused results are attributed rather than presented as new work.

The global interval route was read at
[PR173 `a09eb47197cd99f218b3fa013c681df65ea0f69a`](https://github.com/GettysburgResearch/collatz/tree/a09eb47197cd99f218b3fa013c681df65ea0f69a/research/lean-shell-cover).
It supplies no hidden assumption to W1–W5.

## Reproduce

From this directory, using the pinned toolchain:

```sh
cd lean
lake build
lake env lean Audit.lean
```

`Audit.lean` prints the exact top-level statements, their axiom dependencies,
and the still-open proposition. Standard Lean logical axioms are distinct
from a conjectural axiom or `sorryAx`; the latter are not used.

The repository integrity/regression gate is run separately in a complete
clean checkout. Its process receipts belong in `reports/`, not among these
mathematical claims.
