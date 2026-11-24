# Scope of the global-step review

This is a research-branch review, not a declaration that the project has
accepted a Collatz proof. The exact new sources are bound by
`source-manifest.json`. The parent read the complete three mathematical
notes and the six Lean modules. A different Astra lane independently
reconstructed AR1–AR6; both that lane and the residue lane independently
replayed the mixed-cluster cylinders. The residue lane also reconstructed
the written phase extension and the uncovered-language example.

## Persistent descent: verified in the stated languages

The normalized source equations are `8*x' = 9*x` and
`32*x' = 9*x + 83`. Their odd-source incarnations give the literal pairs
of valuations `(2,1)` and `(1,4)`. In `Renewal.lean`, coprimality supplies
the unique dyadic source class. The canonical representative is positive
enough for natural subtraction; every ordinary source in the class is a
nonnegative lift. The `cylinder` theorem follows the actual shortcut map,
not an arbitrary affine interpolation.

For the two-state graph, a boundary value is at least 13 because it has two
subsequent legal original letters. The same initial comparison source
therefore returns above 2 at unbounded target clocks. If it had hit 1, all
later shortcut states would be 1 or 2, a contradiction. The odd-core
extraction retains both positivity and nonconvergence.

For the mixed-cluster graph, every checkpoint has three subsequent L's,
even when they cross edge boundaries. Consequently `512` divides
`x=(q+7)/2`; `U=x/128` is a positive multiple of four. This derives the
integrality and parity of `157*U-5` from the original path. The canonical
cores use 17 and 25 clocks, with 10 and 14 odd target inputs. Their scaled
affine carries are 2988 and 1102572. The same initial integer survives every
concatenation and remains above 2 at the checkpoints.

The kernel theorem applies at graph boundaries. The written extension to
every odd phase uses an explicit later original state when at most four
light blocks remain before a P. For larger light remainders a suitable
graph walk starts at the cut itself. The required inequality is compared
with the floor at that cut; it does not reapply a smaller-source statement
at an unrelated later, larger floor. The two languages still have an
explicit nonempty symbolic complement. A smaller bad source outside a
language is not an unconditional exclusion of every bad orbit within it.

## Cycle constraints: finite algebra compiled, asymptotics written

The parent reconstructed the directed height loss. Correcting each rational
state by 1 makes an odd step homogeneous; only an odd partner over an even
base costs the factor 3. Equal cyclic weights give exactly half as many
charged discrepancies as total disagreements. A permutation supplies a
phase with ratio at most one. This step applies at arbitrary clock gcds.

A common word gives divisibility by its whole dyadic modulus. Primitive
determinism forbids a zero phase difference. Starting at a minimum phase
and using the cycle correction product yields the finite denominator
inequality in the note. The second proof controls suffix slopes by the
interval discrepancy obtained from each offset's Euclidean algorithm.
The short modular return and exceptional-offset count keep the period gcd
and the offset gcd separate. The power bound at the physical odd-clock
rotation also uses the elementary harmonic upper bound on the cycle's
logarithmic correction.

`CycleRotation.lean` supplies the finite permutation and noncollision
interfaces. `ActualCycleSeparation.lean` defines the actual natural shortcut
map, proves its cleared step equation and word replay, and attaches the
divisibility bound to its least-period cycles. These interfaces do not
assume that an arbitrary word has an ordinary realization.

The logarithmic asymptotics retain the pinned Matveev application in PR196.
Only the small-physical-offset corollary uses PR192's Evertse-based grouped
window theorem. The probabilistic rational examples preserve total cell
weights, giving a uniform cyclic discrepancy bound. Independent cell
variables supply simultaneous separation at all shifts; a transposition
gives two coprime carry gcds and hence a product denominator bound. These
examples are rational, not ordinary counterexamples. No universal upper
bound on an ordinary cycle's rotational disagreement has been proved.

The parent replaced the broad `import Mathlib` in the cycle module by
specific imports. The theorem bodies are unchanged. The exact integrated
source, including this import change, passed the isolated replay.

## Residue results: verified written implications, no hidden independence

AR1 includes the terminal `2^A` in the observation, so length and observation
recover the last gap as well as the earlier ones. The endpoint congruence
requires no modular division and works at every modulus. Its finite
statement is compiled.

AR2 transmits a truncated word on bad blocks and only a clock on good ones.
This avoids discarding the entropy of an unbounded exceptional alphabet.
Reusing adjacent boundary residues and taking arbitrarily many blocks at a
fixed modulus removes the otherwise spurious factor of two.

AR3 derives the conditional word-entropy lower bound from the actual finite
fiber dynamics and stationarity. It does not assume future independence.
The two words 12 and 21 have the same slope and a translation difference
of one quarter, a unit at every modulus coprime to six. Pinsker plus a
telescoping translation average gives the stated bias constant. At zero
entropy deficit, transporting a uniform residue from a past boundary
establishes independence from the full two-sided word. The strict height
penalty is conditional on a specified positive residue bias.

AR4 applies to the same original finite prefix at prescribed growing
moduli. Fixed-block convergence and bounded-letter chunking give centered
partial sums that are small in probability, which suffices for the fixed
exponent margin. All boundary entropy comparisons use the at most N+1
underlying ordinary dates, uniformly in the modulus.

AR5 is a statement about a limiting ergodic component. Recurrence to a
p-adic atom yields a rational fixed center in the field, also for p=2 or 3.
Odd rotated carries make the rational itinerary literal and deterministic.
Negative rational cycles are allowed; no positive ordinary periodicity of
the initial source follows.

AR6 keeps the original finite dates and the complete signed return
equations. Consecutive visits have disjoint edge budgets. The cheapest
return and every sufficiently short other return have cross determinant
strictly smaller than the modulus and divisible by it, hence zero, with no
cancellation of nonunits. An exceptional return spoils at most L selected
date windows. The resulting count is exactly the stated
`s - L - L*V/T`. In the limiting consequence, a bounded-cost anchor is
chosen from a finite word set and fixed on one subsequence before the
decreasing-cylinder limit is taken. Collision convergence has no asserted
power rate.

The finite modulo-return congruence and cross-determinant step are compiled.
The entropy, recurrence and limiting arguments remain written proofs.

## What the combined information still does not prove

At the critical window length the word entropy can already exhaust the
entropy of the sampled date. Unconditional auxiliary residue entropy cannot
be added to it. The stationary proof amortizes an initial residue over
arbitrarily many blocks at a fixed modulus; a finite prefix supplies only N
possible sampled dates. A closing estimate must control conditional residue
information at complementary growing precisions for the same small
ordinary integer. Neither fixed-modulus independence nor the rate-free
moving-modulus collision limit supplies that estimate.

Likewise, the persistent descent graphs have not been forced on all
remaining L/P itineraries, and the full cycle denominator has not been
excluded for arbitrary large-disagreement words. These remain mathematical
gaps, not merely missing Lean translations of complete proofs.

## Executed evidence

`isolated-lean-replay.json` records a fresh six-module build, with every
local import resolved against freshly compiled objects in an empty external
directory. All 33 printed transitive axiom audits contain only standard
axioms; all 39 public theorem declarations compiled. No compiler diagnostic
was accepted. All source bytes remained unchanged during the replay.

`finite-controls-replay.json` records both scripts in normal and optimized
Python, with identical outputs in each pair. The 70 ordinary comparison
cylinders and finite cycle/offset censuses support exactly those samples.
The independent review also constructed and replayed finite ordinary lifts
of all 120 short cluster schedules through four graph edges. That latter
review is not represented as a separate archived executable corpus.

Full-checkout structural validation is recorded separately after committing
the research tree. Its meaning is repository integrity and retained bounded
self-tests, not mathematical verification of Collatz.
