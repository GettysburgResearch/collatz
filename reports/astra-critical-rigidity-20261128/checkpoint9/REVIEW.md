# Ninth coordinating mathematical review

Date: 2026-11-28 UTC. Parent public checkpoint:
`e71eab1a67515694862848cc11086915b93f4b5a`.

This checkpoint advances the global integer-cycle argument from pair sums to
triple sums and gives three further reductions of the paired-clock question.
All five new mathematical manuscripts are proposed written theorems. The
coordinator reconstructed their proofs independently of the authors, including
the complete signed packet argument and the cancellation of repeated polynomial
factors. The sparse-recurrence and triple-order manuscripts were also separately
reviewed by both other research lanes; the calendar-crossing manuscript was
reviewed by both other lanes. A review is evidence about a mathematical argument,
not a claim of independent publication or Lean certification.

The Collatz conjecture and the global logarithmic paired-clock upper bound
remain open. In particular, the new clock approximation exponent at width three
does not cross the published irrationality threshold. The exact finite controls
described below check interfaces and identities, not the large-parameter onset
of a theorem imported from Diophantine approximation.

## 1. Moving sparse recurrences on the integer rank array

[SPARSE_RANK_RECURRENCES.md](../../../research/astra-critical-rigidity-20261128/cycles/SPARSE_RANK_RECURRENCES.md)
assumes integer arrays of polynomial height which, after scaling, converge
uniformly to the exponential rank profile. It excludes a bounded-term integer
recurrence on any fixed positive-length rank interval when its degree is at
most `p/(log p)^5`. The exponents and the polynomially bounded coefficients may
move with the candidate array. This is stronger than the earlier fixed-stencil
integer-grid obstruction, which is explicitly credited.

The main issue in review was preserving the coefficient bound after removing
common factors. If `D` is the reciprocal recurrence polynomial and `Y` the
finite integer series, the recurrence gives exactly

`D Y = U + T^N V`, with `deg U, deg V < deg D`.

For a root remaining after the common factor of `D,U,V` is removed, the two
boundary polynomials have the same vanishing order below that root's
multiplicity in `D`. A sparse polynomial with at most `s` terms has nonzero-root
multiplicity at most `s-1`. Differentiating the original boundary polynomials
at precisely the shared order therefore gives `lambda^N = -U^(e)/V^(e)`
without ever needing a coefficient estimate for a quotient by the common
factor. The logarithmic coefficient cost stays `O(log p)`.

The projective height inequality is `h(U(lambda)/V(lambda)) <= w h(lambda)
+ log B`, rather than a sum of two separate evaluation heights. It applies to
nonintegral algebraic roots as well as algebraic integers: at finite places
integer coefficients introduce no extra factor, and at infinite places the
coefficient sums supply `B`. Consequently the effective roots have degree
times height `O((log p)^-4)`. The Dobrowolski–Voutier bound forces them to be
roots of unity.

Mann's theorem applies to an irredundant vanishing subsum at each effective
root, even though the coefficients change with the array. A bounded family of
strides, each a fixed primorial times a difference of two support positions,
captures every such root with its multiplicity. Each stride is independently
replaced by a positive multiple asymptotic to a sufficiently small fixed
fraction of `p`. This retains divisibility and keeps the resulting annihilator
inside the tested interval. Its coefficient sum is bounded because the number
of factors is bounded. Applied to the exponential profile, the normalized
annihilator has a nonzero limit, contradicting its exact zero value on the
integer series. No large common multiple of all the original strides is used.

The coordinator checked Voutier's original author manuscript, Corollary 2,
which states the required bound for nonzero algebraic numbers that are not
roots of unity, including nonintegral numbers. The exact rational-coefficient
Mann statement was checked in Zannier's research survey, pages 487–490. The
published theorem is an external input; its entire original proof is not
formalized here.

- [Voutier, original manuscript, Corollary 2](https://arxiv.org/pdf/1211.3110)
- [Zannier, vanishing sums of roots of unity](https://seminariomatematico.polito.it/rendiconti/cartaceo/53-4/487.pdf)

## 2. Triple order, an actual binary code, and the remaining numerical gap

[THREE_SUM_RANK_ORDER.md](../../../research/astra-critical-rigidity-20261128/cycles/THREE_SUM_RANK_ORDER.md)
uses the true two-grade integer chart of a primitive ordinary cycle. For fixed
odd width `R < 27/8`, all unordered triples on a rank span of length
`p/(log p)^5` have distinct sums, at every rank origin, in their geometric order.
Repeated positions within a triple are allowed.

The difference of two triple sums obeys a scalar integer recurrence whose
tag defect has absolute value at most three. If the difference leaves zero,
the common division exponent must be one and its new value is `+1` or `-1`.
Both the departure and successor rows must have variable tags. The actual
rotation geometry then forces the following windings to be two and one, and
forces the third successor row to have tag two throughout. At such a row the
triple difference is divisible by four. The small scalar recurrence therefore
returns to zero within three edges. Every excursion born from a zero is
confined to a prescribed low part of the rank circle; a zero anywhere on the
closed transitive circuit forces zero on a common macroscopic high arc. The
sparse-recurrence theorem excludes that event. Once zeros are excluded, integer
sign propagation works, and the exact weighted sum over the complete octave
identifies the sign using the irreducibility of `T^p-2`.

The code is formed from actual unwrapped columns, with their true common
chronological windings. Only dates in the variable-tag interval need be kept.
Equality of two coordinatewise integer triple sums of the binary words implies
equality of every aggregate affine tag. The full dyadic divisor then exceeds
the possible initial integer triple difference, forcing its exact vanishing.
Triple order identifies the two original multisets. Thus this is a real binary
`B_3` code with `p^(1-o(1))` words; it is not a code assigned to an unrelated
symbolic calendar.

For any distribution on the binary cube, convexity of the sixth power of the
Fourier norm and averaging over coordinate flips give triple-sum collision
probability at least `(20/64)^k`. In a `B_3` code the opposite bound is `6/M^3`.
The coordinator read the original proof of Proposition 3.8 in Gu's manuscript,
where this symmetrization is attributed to Polyanskiy, and reconstructed the
short proof included in the new note. The source's definition includes repeated
entries and integer coordinate sums, exactly as required here.

- [Gu, Proposition 3.8 and its proof](https://arxiv.org/html/1809.07364v1#S3.SS2)

The resulting code coefficient is `log_2(16/5)/3`. At widths tending to three,
the necessary rational-approximation exponent for the true cycle clock is
greater than 4.84. The unconditional published irrationality exponent 5.116201
still permits it. This is a stronger necessary condition, not an unconditional
increase of the width-three exclusion. Splitting the cycle into short rank
pieces, and then by tags and the finitely many physical branches, gives the
hereditary triple-energy bound `O_R((log p)^15 |S|^3)` for every subset of its
full ordinary state set. The cubic loss in the number of pieces follows from
the Fourier norm triangle inequality and Cauchy, retaining the full subset.

## 3. Simple line cycles and occupation of genuine scalar shadows

[SIMPLE_LINE_CYCLES_AND_SHADOWS.md](../../../research/astra-critical-rigidity-20261128/ordinary/SIMPLE_LINE_CYCLES_AND_SHADOWS.md)
retains the signed affine relation, its true grade gap, and its nonzero integer
translation. The universal entry construction reaches any admissible line at
cost proportional to its least complexity. Repeating a vertex-simple cycle
enough times amortizes that entry cost. Conversely, deleting repeated vertices
from an adjacent closed word partitions all its edges into vertex-simple
cycles, conserving native length and common odd grade. The actual determinant
bound controls the minimum complexity of each deleted component. These two
directions prove the stated equivalence with a simple-cycle inequality; they
do not prove that inequality.

The low-band argument was checked with both signs of the boundary level and
with a final unfinished excursion. A complete excursion outside a fixed band
returns to the same boundary, so its cumulative grade controls the possible
increase in the logarithmic translation potential. A final unfinished
excursion contributes only its exit date to the band count. No bound on the
greatest level outside the selected band is required.

On a common-parity run of length `ell` at level `j>0`, the actual two states
are congruent modulo `2^ell`. Removing the exact two-adic valuation of `3^j-1`
therefore produces the scalar center `a/(3^j-1)` and its actual native letters
for the retained `ell-v` dates. Its reduced denominator is odd and it is a
ternary unit. The note pays every discarded tail, all mismatches and all
balanced dates, rather than declaring every common run to be an exact scalar
orbit through its final date.

[ARCHIMEDEAN_CLOCK_OCCUPATION.md](../../../research/astra-critical-rigidity-20261128/ordinary/ARCHIMEDEAN_CLOCK_OCCUPATION.md)
then gives a simpler global potential for the normalized separation
`lambda=|a|/3^j`. A common-even step halves it; every active date multiplies
`max(1,lambda)` by at most two. The base potential is zero and remains
nonnegative. There are therefore at most `G` common-even dates above level
two. Each intervening even run contains at most `b+1` dates in
`[2^-b,2)`, and the active dates themselves cost at most `G`. This proves the
uniform `(b+4)(G+1)` occupation bound with room at the endpoints.

The scalar size relation implies that selected retained dates with denominator
at most `Q` number `O((G+1) log(2+Q))`, regardless of denominators elsewhere.
For a family exceeding the proposed logarithmic clock bound, a proportion
tending to one of all dates must consequently lie on genuine rational phases
smaller than every fixed inverse power of `G`, with denominators larger than
every fixed power. The odd-prime lifting identity bounds the part of
`3^j-1` supported below `Y` by `j 3^(Y^2)`. At
`Y=sqrt(log_2(2+G))` that is polynomial in `G`, so the denominator part beyond
this growing cutoff must still be superpolynomial at almost all these dates.
Prime powers are counted with multiplicity. A fixed finite prime-support
restriction consequently suffices for the logarithmic bound even for
nonperiodic paired families; no such restriction is asserted in general.

## 4. Strict calendar crossings and the signed packet estimate

[ORDERED_CALENDAR_CROSSINGS.md](../../../research/astra-critical-rigidity-20261128/literature/ORDERED_CALENDAR_CROSSINGS.md)
counts unequal ordinal ranks, unequal native letters, and strict ordered
crossings separately. The exact crossing ledger charges each inward step by
its departing imbalance and each nonaligned double-odd step by that same
imbalance. Strict inequalities exclude the current leading departure at a
tied date. Telescoping the square of the imbalance controls the outward marks.
This proves the exact finite real bound, including the saving of
`log_2(9/8)` per outward/inward pair.

The stronger estimate partitions the nonzero correction dates into fixed-size
packets. In each packet the first and last low determinant give actual nonzero
integer endpoints for the earlier chronological Subspace-Theorem estimate.
The coordinator reread the full circuit proof in
[SPARSE_DISCREPANCY_BLOCKS.md](../../../research/astra-critical-rigidity-20261128/ordinary/SPARSE_DISCREPANCY_BLOCKS.md),
including the two exceptional endpoint factors, circuit stability, and the
coverage of all chronological cuts. In the new recurrence the normalized
determinant is an integer at every date and cannot vanish: unequal grades
contradict ternary units, while equal physical states contradict the two
distinct periodic starting phases. Thus every required partial sum is nonzero,
including when two pure terms share a date.

Inside a trimmed packet the proof bounds the **signed** sum of corrections.
It never replaces this telescope by a bound on the sum of its positive parts.
Outside the trim all but at most one mark have small correction; the last low
mark is paid separately. The last incomplete packet has bounded imbalance
because the entire calendar returns to grade gap zero. Packet maxima are
bounded by their average levels plus their fixed length. Letting the packet
length increase gives

`L - (log_2 3)p <= epsilon I + C_epsilon M`.

Since `M<=p`, any family with `L >= c p log p` must have
`I/(p log p) -> infinity`. The combinatorial inequalities
`I<=MJ` and `I<=M(M+1)/2` then give the stated lower requirements on both
ordinal mismatch count and maximum imbalance. The accompanying constant is
ineffective because of the Subspace-Theorem input. The crossing count is not
known to obey a uniform upper bound strong enough to settle the clock question.

## 5. Central replay and publication scope

Three exact programs were replayed centrally with ordinary and optimized
Python; every mathematical guard uses explicit exceptions rather than
optimization-sensitive assertions. Each receipt pins its source hash and
checks that the file did not change during the runs.

| Control | Observed finite coverage |
|---|---|
| Signed lines and shadows | 28,964 actual signed steps, 512 ordinary sources, 128 static adjacent loops, 4,480 occupation checks, 3,625 retained scalar dates including 512 negative ones, and 468 simple-cycle components including 249 away from the base vertex. |
| Ordered crossings | All 510 adjacent solutions found through native length 15, 4,403 crossing incidences, 5,682 low-endpoint packets and 12,545 nonzero chronological cuts. These enumerated solutions have positive determinant; the separate signed-line control includes a negative-period example. |
| Three-sum interfaces | Exact two-boundary polynomial identities and effective multiplicities, complete finite signed birth traces, and every nonempty uniform cube support in dimensions one through three. The controls include a constant-profile boundary case to show why the exponential shape assumption matters. |

During coordinating review a proposed nonintegral-root control was found to
test an integral root of the reciprocal boundary polynomial instead. The
fixture was corrected to test the root actually used in the height argument;
the revised normal and optimized runs are the recorded publication inputs.
This did not affect the written height proof.

No new Lean roots are claimed here. The unfinished `TwoGradePairOrder.lean`
prototype is excluded from publication. The central formal inventory remains
65 distinct roots, or 66 with the separately rebuilt motif specialization.
The previous checkpoint's complete clean-checkout repository validation
receipt is retained in this checkpoint. A fresh complete validation of the
exact selected tree is required before its branch reference is advanced;
repository validation certifies integrity and project gates, not these
mathematical deductions.
