# Ordinary walls, changing arithmetic centers, and complete inverse branches

**Collatz is OPEN.** This packet records the unconventional three-hour pass
of 26 November 2026, continuing PR197 from
`f74d2144275c3e1f9148b0b2997fecc7931ae7f5`. The central formal advance is a
general exclusion of periodic ordinary walls with two finite, positive-grade
signed reference cycles. Further formal advances exclude an explicit
infinite family of original least-defect parents and impose clock delays
on every smaller ordinary source attempting to meet an ascent. The written arguments
also locate important limits of inverse counting and local arithmetic
rigidity. No universal selector or terminating interpretation of the full
Aaronson–Yolcu–Heule system is supplied.

## What the new results say

| Result | Exact scope | Evidence |
|---|---|---|
| Periodic ordinary walls | Every fixed binary word whose two signed reference orbits enter cycles with positive odd counts has a uniform cap on new runs; on each ordinary wall, all alignments eventually obey that cap. | Lean: `WallGeneral`, `WallUniform`, `WallWords` |
| A concrete cap | Eventually no run of 81 copies of `1011`, in any alignment. | Lean certificate with 854 leaves including one exempt source class; separate exact replay |
| Word depth versus physical time | Equal-density signed cycles give a word-only cap from every position. General positive cycles give a block-depth bound linear in the initial valuation. Physical merger clocks can nevertheless be unbounded, even at every pair of block depths. | Lean: `WallDensity`, `WallShifted`, `WallLinear`, `WallDelay` |
| Arbitrary affine pairs | Every prescribed dyadic class has a subcylinder on which `x` and `3^s*x+D` merge, for every integer offset and every nonnegative `s`. | Lean: `WallAffine.in_class` |
| Perfect-power parameters | Every `m=b^(2^2956)` is excluded from the original least-defect row `81z+271=128*2^(11+162m)`. | Lean: `PerfectPowerParents.excluded`, retaining the leastness hypothesis |
| Changing ternary centers | Every prescribed ternary parameter class contains a complete subprogression with an actual smaller ordinary query, with arbitrarily prescribed savings. | Lean: `AdelicSwitch`, `AdelicParent` |
| Geometric sequences | For every nonnegative integer base `b`, all but `O(N/sqrt(log(2N)))` exponents in each translated length-`N` interval have `b^n=0` or an earlier-peak merger; the constant is independent of the base and interval. | Written deduction from the pinned affine absorption estimate; separately checked arithmetic certificates |
| Inverse-query rarity | A uniform ordinary counting bound limits how often short-surplus queries can beat the original return budget, even when all physical clocks and prepeak phases are allowed. | Written proof with finite Lean kernels and exact controls |
| Every smaller source | If `x+1=2^n*b`, `b` is odd, and `x<2^j*a-1` with `3` not dividing `a`, a meeting at ascent phase `u` requires more than `n+u` physical steps from `x`. A specified negative-address progression gives stronger postpeak rectangles and margins. | Lean: `NegativeExponentAddress.prepeak_clock`, `full_clock`, `full_margin` |
| First contact | For odd positive `a` not divisible by three, first contact with the ascent prefix at phase `u>=1` requires at least `n+u+max(1,ceil(log₃(u)/6))` physical steps. A supplied exact family shows why first contact cannot be omitted. | Elementary written proof in `FIRST_ATTACHMENT_CLOCK.md`; the weaker all-meeting bound is Lean checked |
| Actual branch gains | Along any supplied injective odd ray, complete inverse generations up to `log₂(m)/512` have summable full normalized gains at some exponent below one. | Self-contained written counting proof and finite reconstruction controls |
| Fresh ascent barrier | Actual long ordinary ascents can keep all fresh inverse gains small, even with unrestricted inverse depth and simultaneously at many phases of the same ascent. | Elementary written argument; signed transfer kernels and finite controls |
| Two-sided rational closings | At large actual states, the complete denominators of past and future periodic closings cannot both be too small; coefficient records give a stronger joint restriction. | Written Subspace-Theorem argument; elementary arithmetic kernels |

The scientific notes below distinguish their full written statements from
the smaller lemmas formalized in Lean. Recent first-passage and density
inputs are confined to explicitly source-qualified deductions.

## 1. The general wall theorem

For a binary coloring constant on shortcut edges, a mixed adjacent pair
has a unique oriented mixed child. A positive failure of convergence
therefore supplies one fixed ordinary root whose wall persists through
every binary depth. Its signed difference is exactly reconstructed by
the sparse finite sum in `WallGate`.

For a word of length `L` and value `p`, set `d=2^L-1`. After `k` copies,
the index `m_k` satisfies

\[
 d m_k+p=2^{Lk}(dn+p).
\]

The two signed numerator references are `-p` and `d-p`, under the map
`a/2` on even numerators and `(3a+d)/2` on odd numerators. If both enter
positive-grade cycles, the proof balances their odd counts using different
numbers of laps. Their actual ordinary endpoints then lie on exponential
affine rows. Exact binary lifting, coverage by powers of three, and the
general affine merger force a common integer. The two wall colors would
have to agree there.

The uniform version bounds the number of word blocks needed after a
mismatch, independently of the ordinary source. A finite-alignment
argument gives an eventual cap everywhere along a wall. For `1011`, the
explicit cap is 81 copies. A signed rational wall at the exceptional source
`-11/15` still realizes that period forever: the ordinary-source condition
does real work.

If the two positive cycles have the same ratio of odd steps to physical
steps, the cap holds from the first position, with no source-dependent
onset. Different within-word reference phases are allowed. For general
positive cycles the needed block depths are at most `A*v+B`, where
`v=v₂(d*n+p)` and `A,B` depend only on the word and its supplied cycles.
These are bounds on word blocks. `WallDelay.period18_unbounded_clocks`
proves that for every physical horizon `H`, a positive ordinary source
exists for which **no** pair of block depths meets with both clocks at
most `H`. The two statements are compatible: bounded word depth does not
bound the physical time needed after that depth.

See [WALL_RESULTS.md](WALL_RESULTS.md),
[WallWords.lean](WallWords.lean), and the finite census
[wall-periods30.json](wall-periods30.json). The census tests all 4,719
primitive parity-admissible necklaces of lengths 2–30. With the general
theorem it excludes the 4,718 nonalternating cases from ordinary eventual
periodicity. The census is finite; aperiodic ordinary walls remain open.
Among the tested necklaces, 4,715 have equal positive cycle rates and
therefore obtain the stronger cap from the first position. These counts
come from exact finite computation. The general implications, the four
individual ordinary exclusions, and separation of their designated
reference orbits are Lean checked. The finite census exhibits the signed
rational models.

## 2. Real ordinary queries, rather than a completion alone

The original row is `j=11+162m`, `81z+271=128*2^j`. Its seven-step
Mersenne state is `2^j-1`; its later peak is `3^j-1`. A query below
`z/2^40` that reaches any prepeak state contradicts leastness if `z` is a
reverse defect. The new Lean assembly permits all query clocks and grades.

The moving-center construction selects a genuine positive inverse source
at each new anchor and lifts its legality to a ternary subprogression.
The logarithmic construction uses the normalized derivative of
`3^(162m)` near zero and an exact compensated merger at clock 2,957.
This proves the pointwise perfect-power exclusion for every ordinary base
`b`, including zero and one. It is not a proof that every parent on the
row converges without the leastness condition.

The steered ternary-cylinder mechanism is prior work: see Appendix B.3
of [Paper 179](https://rstation.ai/problems/collatz/papers/179).
The inverse square-gain tilt is also prior work in
[Paper 177, section 7](https://rstation.ai/problems/collatz/papers/177)
and Paper 179, section 4. Here those mechanisms are specialized to the
actual exponential parameter, the required ordinary residue, arbitrary
savings, and the original parent consumer; the ordinary gate counts and
surplus horizon have their separate proofs. The underlying mechanisms
are not claimed as discoveries of this pass.

The geometric-sequence theorem adds a negative logarithmic residue.
Its explicit ordinary trajectory profile at clock 334,711 is checked by
`NegativeProfile.ordinary`, using 164 certified blocks. The identity of
that integer with the stabilized derivative residue has independent exact
arithmetic replays and a written finite-precision proof; that identity is
not silently counted as a Lean theorem.

Read [CHANGING_CENTERS.md](CHANGING_CENTERS.md),
[LOGARITHMIC_POWER_FIBER.md](LOGARITHMIC_POWER_FIBER.md),
[GEOMETRIC_SLICES.md](GEOMETRIC_SLICES.md), and
[INVERSE_COVERAGE.md](INVERSE_COVERAGE.md). The latter's parent-budget upper
fraction is `1/(27*2^65)` in its stated growing surplus range. The selected
successful subprogressions may still be very thin in ordinary intervals.

[ALL_SOURCE_CLOCKS.md](ALL_SOURCE_CLOCKS.md) retains every smaller
ordinary source and its own odd cofactor. Writing `x+1=2^n*b` with `b`
odd, any meeting with `3^u*2^(j-u)*a-1` requires `h>n+u` when
`x<2^j*a-1` and `3` does not divide `a`. For the original exponent row
with `m>=1`, if `2^k` divides `27m+2`, the upper peak at every clock `i<=k+3`
is separated from every smaller source throughout both intervals
`h<=n+floor(j/3)` and `h+3i+11<=n+j`.
[NEGATIVE_EXPONENT_ADDRESS.md](NEGATIVE_EXPONENT_ADDRESS.md) constructs
actual positive progressions with this obstruction; at depth at least
two they contain no nontrivial perfect powers. The written inverse-count
bound applies uniformly within these progressions. Their existence is a
limitation of the bounded mechanisms, not evidence that these ordinary
integers are reverse defects or counterexamples.

[COVERAGE_CONTROL.md](COVERAGE_CONTROL.md) gives a fully explicit check on
the quantifiers: the infinite set `{2^(3^k): k>=0}` can remain exceptional
while its complement has all three coverage shapes above. This is a
logical control, not a bad Collatz family.

## 3. Gains, records and arithmetic rigidity

[ENTRY_EDGE_GAINS.md](ENTRY_EDGE_GAINS.md) counts actual marked vertices
before, across and after a chosen physical clock. It handles every
first-entry configuration and all depths of the ancestors contributing
to a branch's maximum. The elementary exponent is below one at a marked
generation radius of `log₂(m)/512`. The corrected-height construction and
its component minimizer are credited to prior work.

[FRESH_ASCENT_BARRIER.md](FRESH_ASCENT_BARRIER.md) uses the signed fixed
point `-1` to control fresh branches on actual positive ascents. The
initial ordinary source is kept fixed across the phases of each finite
experiment, but changes between experiments. The result prevents a
generic branch-count argument from supplying a large late gain without
using additional properties of the particular infinite ray.
The exact signed census identifies `3/8` as the largest fresh gain in the
specified signed tree and supports selected positive ascents with that
same all-depth maximum. The finite reduction and census are written and
computational evidence, not silently included in the Lean theorem count.

[FIRST_ATTACHMENT_CLOCK.md](FIRST_ATTACHMENT_CLOCK.md) strengthens the
all-source delay for odd positive `a` not divisible by three when the
meeting is the first contact with the target ascent prefix. With
`B=h-n-u`, its positive carry expansion gives
`u+B<=6B*3^(3B)<=3^(6B)`, hence the extra logarithmic delay in the table.
The exact source `x=(8M-5)/9`, for `M=2^j-1` and `j=5 mod 6`, first
meets `M` and then follows its ascent with only one excess post-ascent
step. It shows that the first-contact hypothesis cannot be discarded.
That source is larger than `M/2`, so it cannot supply the original
factor-`2^40` rescue query.

[FORCED_CLOSINGS.md](FORCED_CLOSINGS.md) uses the complete denominator of
each actual periodic closing. For example, with 90-percent windows at a
large strict coefficient record, one side has at most one closing with
denominator at most `q^0.26`. The joint estimate cannot be replaced by a
claim about two separate exceptional sets.

[FINITE_RECORD_POPULATION.md](FINITE_RECORD_POPULATION.md) constructs at
least `c X^0.94` actual finite record states in `[X,3X)` for
`X=3^(1536t)`, as `t` grows, whose indicated
past and future denominators all exceed the stated threshold. Their
sources grow. This demonstrates that the arithmetic constraints are
compatible with large finite populations.

[PRECISION.md](PRECISION.md) treats fixed and moving local centers.
[RENORMALIZED_REAL.md](RENORMALIZED_REAL.md) gives further consequences
conditional on algebraicity of the corrected real limit; algebraicity is
not proved. [ENTRY_THRESHOLD.md](ENTRY_THRESHOLD.md) separately explores
the much larger first-passage threshold using named recent manuscript
inputs, including an originating Gaussian preprint not independently
verified here. [ASYMPTOTIC_ROOT_CHARGE.md](ASYMPTOTIC_ROOT_CHARGE.md) explains
why averaged shift and dilation information can lose one exact ordinary
edge condition.

## 4. The final Lean proposal and the remaining step

[UnconventionalProposal.lean](UnconventionalProposal.lean) extends the
previous original-survivor structure. A survivor has no small ordinary
query, no parameter in the proved perfect-power family, and an actual
wall obeying the new periodic restrictions. It proves

```lean
theorem collatz_iff_remaining :
  FinalProofProposal.UniversalConvergence ↔ RemainingExclusion
```

`RemainingExclusion` is explicitly **OPEN**. It is a proposition to prove,
not an axiom added to the environment. The next decisive result must either
supply a successful query for every remaining original ordinary source,
rule out every surviving ordinary wall, or provide another pointwise
descent argument. Density-one statements, finite populations, and a
sequence of changing witnesses do not discharge that proposition.

## Reproduce the evidence

Use Lean 4.34.1 at commit
`5045d0056413266e57c625dcd7c365b10e377c52` and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Supply the compiler as `LEAN`
and the pinned Mathlib/package object paths as `LEAN_PATH`, with no
repository-local prebuilt objects. Then run:

```bash
bash research/ayh-resource-reset-20261124/unconventional/check_lean.sh
python -X utf8 -B research/ayh-resource-reset-20261124/unconventional/check_controls.py --output /tmp/collatz-unconventional-controls
```

The Lean driver rebuilds the entire local dependency chain into a fresh
temporary directory and treats warnings as errors. The public audit prints
the transitive axioms of every explicitly declared public theorem. The
finite driver runs normal and optimized Python and compares their output.
The exact execution records, source pins, independent review, and broad PR
intake are in the [review packet](../../../reports/ayh-resource-reset-20261124/unconventional/README.md).
