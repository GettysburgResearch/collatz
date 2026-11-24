# Round 13: marked descent, a common cycle budget, and complete denominators

**Collatz remains open.** This packet continues PR182 at
`cbec52dde5bed390a693310dd04e911033ba0cc9`, after inspecting the newer
PR187–PR191 work. Six GPT-6.2 Astra agents worked in two waves on separate
attacks and independent written reviews; the coordinating agent reconstructed
the key counting, denominator and marked-descent implications. Agent review
is distinct from human referee acceptance and from a Lean kernel check.

The project uses the shortcut map `T(n)=n/2` for even `n` and
`T(n)=(3n+1)/2` for odd `n`. The accelerated map `U` records only the positive
odd states, dividing `3q+1` by its full power of two. A shortcut clock and an
odd clock are different throughout this packet.

## 1. A smaller marked partner and a narrower exact closing obligation

The forced section from PR173 consists of odd `n` with

    (d+1)(n-2^d) <= 70*2^d,   d=floor(log_2 n).

Write a positive odd source in its unique maximal rising form
`n=2^(k+1)u-1`, with `u` odd, and set `b=3^k*u-1`. A finite grammar of
literal paired returns certifies mergers of the two ordinary tails at
`b` and `3b+2`:

| Parameter | Actual paired action |
|---|---|
| `b=4v+2` | The two arms meet after two shortcut steps. |
| `b=2v+1` | One step returns to the same pair with parameter `3v+2`. |
| `b=64v+56` | Six steps exchange the arms and return with parameter `9v+8`. |

If a finite sequence of the return rules reaches the terminal rule, the
source `n` merges with `x=(n-1)/2`. Its odd part `y` is positive, smaller
than `n`, and **is itself marked whenever `n` is marked**. Deleting a low
binary digit preserves the section's upper-offset inequality; deleting the
trailing zero digits of `x` also follows its actual Collatz orbit.

Strong induction can therefore take place inside the marked set. The
result is an exact equivalence: universal convergence holds if and only if
every marked source not covered by this finite grammar converges. The
grammar covers an asymptotic fraction `16/31` of the odd marks in a dyadic
octave. Density is a description of the certified domain, not a substitute
for the remaining universal statement. An explicit infinite family of
uncovered marks is retained.

The repeated-six-step subfamily has the particularly simple condition
`v_2(55b-8)=6L+1`, first synchronized meeting time `6L+2`, and marked
fraction `32/63`. The infinite formal return parameter is `8/55`, an odd
denominator rational rather than an ordinary integer.

See [the complete proof and boundaries](BAND_RETURN.md). The finite return,
accepted-script transport, marked-partner construction and residual
equivalence are the Lean targets in `lean/AffinePairReturn.lean`,
`lean/PairedLanguage.lean` and `lean/MarkedHalfReturn.lean`.

## 2. One explicit correction budget, even for a union of cycles

Let `S` be a forward-invariant set of positive odd integers on which `U`
is injective, and assume every element of `S` exceeds `2^68`. An exact
dyadic-cylinder count gives

    sum_(q in S) 1/(3q) < 17/50.

The domain includes an entire escaping orbit above that floor, a primitive
cycle, or the union of distinct vertices of all cycles above that floor.
It excludes a branching predecessor basin and repeated counting of cycle
laps. The finite subtotal and geometric remainder have separate
kernel-evaluated integer certificates; the orbit-counting and infinite-sum
identification are written mathematics.

For nonnegative corrections of sum below `17/50`, rational product
inequalities imply that the square of their product is below two. Applied
to a primitive high cycle with `p` odd steps and full binary clock `A`,
this forces

    0 < A-p*log_2(3) < 1/2,
    A = ceil(p*log_2(3)).

The corresponding endpoint constraint on any nonempty arc with distinct
source vertices inside such a high invariant set is the strict integer inequality

    X^2 < (2^A*Y)^2 < 2*X^2,
    X=3^m*q_start, Y=q_end.

Combining the cycle clock bound with the actual scalar's carry telescope
eliminates all integer carries on a **contracting canonical scalar
phase**. A supplied such phase then has at most one positive cycle, and
the cycle exists exactly when its full canonical denominator divides its
complete carry. This replaces a potentially enormous confined graph by
one exact divisibility test on that branch.

Extending this classification from high cycles to every nonstandard
positive cycle uses the published verification floor. Barina's 2025
paper reports verification below `2^71`; that external computation was
not replayed here. The high-set theorem and its formal finite arithmetic
do not assume the computation. See [the complete argument](CYCLE_BUDGET.md)
and [the integer subtotal certificate](DYADIC_CERTIFICATE.md).

## 3. An infinite cycle-template exclusion with its full denominator

Take the eight-letter pattern

    w = (1,1,1,2,1,2,2,2).

Let `v` be **any** finite word of positive gaps. Form the cyclic word
`(v,w_0)(v,w_1)...(v,w_7)`, put `n=1+length(v)`, and suppose its full
cycle denominator is positive. The exact reduced denominator of its
positive rational realizer is strictly greater than

    4*9^n/7.

Consequently no member of this arbitrary-prefix template family is a
positive ordinary integer cycle. The proof cancels the common polynomial
factor and then controls the remaining *numerical* gcd by an explicit
integer Bezout identity. A proper-factor sieve alone would not suffice.

The same construction exposes a sharp obstruction to a proposed route:
one can choose `v` with only gaps one and two so that the resulting
primitive rational cycles have arbitrarily large minimum state and
arbitrarily small positive clock excess, while their top norm in PR191
vanishes. Their complete reduced denominators grow, so these are
explicitly nonintegral cycles. A high floor, primitivity and two allowed
gap sizes therefore do not imply the nonvanishing needed by that shortcut.

See [the template theorem and high-floor construction](HIGH_FLOOR_NORM.md).
[The companion arithmetic note](PRIME_POWER_NORM.md) classifies top-norm
vanishing for primitive prime-power clock gcds, records the sharp
exception, and gives residual-denominator formulas for fixed affine gap
families. The general algebraic-number-theory statements are written
proofs; the exact polynomial and numerical-divisibility kernels have
separately recorded Lean scope.

## 4. A denominator bound for arbitrary intervening words

Cut a primitive positive rational shortcut cycle at `k>=2` distinct marked
positions into blocks `U V_i`, where the same nonempty word `U` occurs
without overlap. It has `N` odd bits; all the intervening words together
have `E` even and `L` odd bits. If the full cycle has `A` shortcut clocks,
`p` odd steps and reduced denominator `d`, put `eta=1-3^p/2^A`. Then

    d > ((k-1)/k) * eta * 2^N / max(2^E, (3/2)^L).

The defects may differ and individual blocks may expand. Complete
cyclic contraction bounds the affine intercept sum, while the shared
word forces congruent boundary numerators. Their span supplies the
lower bound on the complete denominator. If only `r` distinct boundary
states are known, replace `k-1` by `r-1`.

Gouillon's effective two-logarithm bound gives
`eta >= a*(p+1)^(-C)` for fixed absolute positive constants. Thus every
fixed nonconstant terminal seed, with an arbitrary common gap prefix
of sufficiently large length, is excluded from ordinary integer cycles.
This includes seeds whose top norm vanishes. The eight-letter template
in section 3 has the stronger explicit bound at **every** length.

See [the full proof and external input](DEFECT_COVER.md). The cyclic
expansion, span/congruence argument and application of the two-logarithm
theorem are written proofs. `lean/DefectCover.lean` checks the literal
shortcut intercept estimate and finite aggregation step. No theorem
here guarantees that an arbitrary cycle admits a sufficiently economical
cover; escaping orbits also remain outside this cycle argument.

## 5. A quantified obstruction to a short residual rule

For every integer `T>=6`, an explicit ordinary marked source in binary
octave `4T` immediately fails the grammar of section 1. Its trajectory
stays strictly above its start through `3T+1` shortcut clocks, and does
not meet its canonical half partner at any pair of independently chosen
clocks through `3T+1` and `3T`, respectively. This includes `T` clocks
on both arms after their initial rising segments.

[The construction and affine proof](LINEAR_HORIZON.md) rule out this
specific short-horizon completion strategy. They do not imply divergence
or rule out longer paths or other smaller partners. This is written
mathematics with exact finite controls; it is not Lean formalized.

## 6. Follow-up after the first push: PR192–194

The first packet was published as
`cf1f04db7f9f84d3a31bfccf2546431b711312d0`. A freshness review then
reconstructed the new phase, synchronization, smaller-partner and cycle
arguments in PR192–194 at the exact heads listed in the three notes below.
This also identifies the overlapping prime-power classification in those
branches; no independent priority claim is made for our parallel derivation.

**A decidable, critically summable test set.** Combining the actual marked
descent with PR193's written translated-interval synchronization gives an
explicit decidable set `S` of marked ordinary integers such that

    Collatz holds  iff  every member of S reaches 1,
    sum_(n in S) n^(-theta) < infinity,
    theta=H_2(log(2)/log(3))=0.9499555... .

In each full marked interval, synchronize all integers, including the even
ones, after `(d+2)^3` common odd clocks. A fiber containing an even integer
or an odd integer accepted by a bounded half-return script has a marked
partner below the entire octave. Discard that fiber. From every remaining
fiber keep its minimum. Strong induction gives the equivalence, and the
translated count supplies `O(2^(theta*d)/d^(theta+1/2))` retained sources
per octave. The series converges even at exponent `theta`. This complete
new reduction is a **written proof**, depending on the written analytic
count in PR193. A finite critical-power sum does not prove convergence on
the retained minima. See [the construction and proof](LATEST_BAND.md).

**A stronger guarded predecessor.** The same note identifies the literal
five-step identity

    T^5(64t+47)=162t+121,  with 0<64t+47<162t+121.

Thus every guarded visit `r=162t+121` on a least nonconverger `n_0` obeys
`32r>=81n_0+65`. The general predecessor identity, its strict saving and
this specialization are checked in `lean/GuardedPredecessor.lean`.
The stronger bound does not force a guarded visit below its threshold.
The note constructs sources having both this alternative partner and the
earlier independent-clock half-partner obstruction, keeping the two kinds
of certificate separate.

**Complete top-factor absorption arbitrarily high.** For every fixed
clock gcd `g` with at least two distinct prime divisors, there are primitive
positive rational cycles using only gaps one and two, of arbitrarily high
minimum and arbitrarily small positive clock excess, for which the
**entire** top cyclotomic polynomial and its numerical value cancel. The
complete reduced denominator still grows at least as `c_g*2^n/n`. The
proof combines a two-grid seed with common-prefix lifts and the defect
bound; it needs no external two-log estimate for this chosen family.
This is a written theorem about nonintegral rational cycles. The exact
`g=6` fixture has 17,160 odd steps, minimum floor 90,269, a completely
absorbed 9,066-bit top value and an 18,127-bit surviving denominator.
See [the proof, attribution and exact fixture](LATEST_CYCLE.md).

**Cyclic entropy without clipping.** The half-bit cycle budget makes
PR194's conditional carry-entropy estimate uniform on cyclic windows,
with an absolute additive constant. A cycle with `k` odd vertices and
canonical period `L` consequently requires maximum height at least an
absolute constant times `(k/L)^(1/d)-1`, where `d=0.2858595...`. The
corresponding modular-collision lower bound retains the actual cyclic
law. There is still no opposing height or collision bound. The same
[phase and substitution review](LATEST_PHASE.md) credits PR194's extension
to nonidentity, nonerasing binary fixed substitutions and distinguishes
PR192's changing convergent finite-word witnesses from a single infinite
ordinary realization. These deductions and the cited infinite results
retain written-proof status.

## Verification and the remaining mathematical step

The [execution report](../../reports/2026-11-24-astra-round13/EXECUTION.md)
accompanying this packet records exact source hashes,
compiler versions, declaration-level axiom output, normal/optimized
finite replays and complete-checkout validation. A successful finite
kernel does not upgrade the surrounding unformalized counting, density
or Diophantine proof. The repaired Round 11 and Round 12 finite modules
are checked separately from their broader written consumers.

The attacks meet concrete boundaries. The marked grammar leaves an
explicit residual family. The scalar classification covers contracting
phases, while low phases and arbitrary irrational phases remain. The
complete-denominator theorem covers an unbounded template family, but
does not cover every primitive gap word. None of these missing universal
steps is assumed as an axiom or relabeled as proved.
