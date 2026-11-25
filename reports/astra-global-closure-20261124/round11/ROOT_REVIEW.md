# Root reconstruction and evidence scope

**Verdict: verified for the finite kernels and stated written deductions,
with the listed external inputs. Universal closure is GAP/BLOCKED.** This
review concerns the source bytes in the final `SOURCE_HASHES.json`, the
unchanged dependency pins, and the selected declarations recorded in the
fresh Lean receipt. The root is independent of the authors of the three
worker packets. The root authored the bounded-template extension and final
assembly; separate reviews of those are linked below.

## Ordinary anchor arguments

I reconstructed the actual positive lift and the two-cycle iteration. In the
scale proof, `k=min(r,s)` divides both the anchor and the displacement through
`3^k`, because the difference of the two source equations has a factor prime
to three. The actual hit gives `a≤2^h`; positive displacement gives
`3^k≤t`. Thus `x>4^d·3^(2k)`. The replacement-base comparison gives
`3^r≤2^d·3^k`, even with `b=w`, and hence `3^r<w`. The strict native endpoint
bound uses phase +1, its stronger contraction `a T^h(y)≤y`, and `b<w`.
It must not be extended to other positive phases without another argument.

For a negative periodic target, positivity forces displacement to be
positive. The signed lap expands in magnitude, the replacement is larger,
and `b≤w` forces `s>r`. The same divisibility and the actual preperiod size
bound yield `3^r≤Cw`. I checked the written general-positive-phase estimate,
including negative displacements, separately from the narrower kernel
native-descent statement.

I independently inspected the complete 3645 control. At positive preperiod
length, its odd parity removes the terminal factor of two and the scale
bound contradicts `729>136·5`. At zero preperiod, positivity bounds the
actual meeting clock by 11. The finite table really covers the full cone:
the observed values are below 8192, which forces the exponents below the
enumerated limits. Its source reaches 1 at 31 and is not a Collatz
counterexample. [Independent worker review](cycle/FINAL_REVIEW.md)

The finite-phase ESS application keeps the finite set of target phases
fixed while allowing arbitrary preperiod anchors. At zero preperiod the
rank-three group and each possible cancelling subsum were reconstructed.
The same-base destination is included; zero displacement is excluded by
the written theorem and treated separately for a proper lower cone.
[Closure cross-review](diagonal/CLOSURE_REVIEW.md)

## Complete denominator and wide rational controls

I reconstructed the lap formula by multiplying `(S^h−3)Z=c` by its finite
geometric sum and using `S^p=2`. Reduced denominators are preserved around
the entire rank rotation because they divide `2^h−3^p`, which is prime to
six. For physically legal octave letters, the ordinary odd lap also proves
that dividing `Z` by its power-of-two correction loses no integrality test.

The residue decoder forgets its initial value after `L` steps modulo `3^L`.
Bounds on the decoded values make every congruence defect smaller than its
modulus, so the defects are exact zero. The unequal complete-lap multipliers
then identify the rational array. To reverse the two filters, I checked the
orientation of multiplication by `X` on the reversed coefficient encoding.
The seam yields a unit ideal over the full composite quotient, not merely
over prime factors. Taking positive powers preserves that unit ideal.

The explicit error bound includes all shifted entries used by each finite
difference. In the continued-fraction specialization I checked the preceding
and current denominator indices, their opposite signs after perturbation to
`h/p`, the lower error bound needed to preserve those signs, and the exponent
in the large-height estimate. The displayed count is for parallel windows;
their total temporal span can be much larger. No phase-injectivity claim is
needed or supplied. The ambient repeated-filter-value control correctly
blocks that extra counting inference.

For the wide rational construction I checked every rise/fall at the three
overrides, the centered partial-sum discrepancy and its uniformity over
cyclic segments, both physical order embeddings, and the bounded-difference
estimate for simultaneous shifts. The unique minimum fixes the rotation and
the word, justifying the count of distinct rational minima. The polynomial
height bound proves many are nonordinary; it does not rule out an exceptional
integer member. [Independent cycle review, including the composite-modulus
stress test](closure/CYCLE_REVIEW.md)

## Original-source trace estimate

The recurrence uses one supplied injective path. A low-odd-count site maps
to its own actual future state; distinct index shifts remain injective.
At most `k` terminal indices have no image within the supplied segment.
The complete parity grid fixes the first bit in the odd-site count and
uses the maximum possible number of 3-units in each lifted residue class.
I checked the image bound, floor and bit-length rounding, recursive order,
and layer-cake tail `200·2^(−J/40)`.

The exact calculation gives a reciprocal sum below `593690/10^6`. The
three-term logarithm inequality gives the strict `9/50` carry threshold.
The same census is applied separately to a first-hit prefix and one
unrepeated cycle lap; it is never applied to all repeated cycle visits at
once. The inherited floor F enters only the narrower-shell lower count.

The explicit zero range also uses two external computational claims:
convergence below `2^71` and the author's shortcut path-record cap below
`2^139`. The root opened the primary record table and checked its map and
scope. The local checker replays the final record-holder to 1 in 1027
shortcut steps; that replay does not verify the exhaustive interval.
Raising the floor without proving coverage of its new gates would be
circular. [Independent trace review](cycle/DIAGONAL_REVIEW.md)

## Bounded-template extension and final proposal

The root's extension fixes the finite word bank and block-count bound, but
allows arbitrary positive repetitions. Exact ordinary word maps give the
sparse telescoping equation. Selecting a minimal vanishing subset containing
the source treats every possible degeneracy; after normalization the
finite-rank equation has finitely many projective ratios. Every reference
term has valuation bounded above by its fixed coefficient, so a fixed ratio
bounds the source's exponent. The finiteness result is written mathematics
using the published ESS theorem, with its precise statement checked in the
author's preprint. No height bound is inferred from a bound on the number of
solutions. The nonempty trace condition is essential when the base is not
prime to three. [Independent template review and 4004 exact physical
two-block checks](diagonal/TEMPLATE_REVIEW.md)

The final universal consumer retains `remaining : FrontierMerger`. The
countercontrol and progression theorems have closed hypotheses and do not
prove that premise. Merely importing the independent cycle and trace
modules supplies no extra implication. The source review of PR197's new
proposal likewise retains its residual theorem as open.

## Executed checks

The root rebuilt ten project modules in an empty project cache, with
warnings as errors, and checked all 83 selected transitive axiom reports
against the standard three-axiom list. All source hashes remained unchanged.
Four modules are reused pinned dependencies; six are new in this pass.
The compiler and cached Mathlib/package binaries were not rebuilt.
[Lean receipt](lean/receipt.json)

The root ran each of the three finite control programs in normal and
optimized Python. Every pair produced byte-identical output, and its
source remained unchanged. These controls check exact finite arithmetic,
not all-depth convergence or all candidate cycle words.
[Control receipt](controls/control-replay.json)

Repository integrity is checked separately on clean complete candidate and
published checkouts. The publication receipt records the actual commit and
tree validated; it does not convert this research packet into a complete
proof.
