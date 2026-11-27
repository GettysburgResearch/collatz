# Independent review of the first research checkpoint

**26 November 2026.** This is a narrow mathematical review, not an assertion that Collatz is proved. The source packet starts at owned PR192 commit `0e313e2cd42cfce1275dbef6129ac13e9a49abd5`. The [intake](INTAKE.json) freezes the surrounding proposals. They remain separate sources rather than imported joint premises.

## Arithmetic lane

**VERIFIED as written mathematics, A1–A3.** Reconstructed the polynomial square-root grid, its explicit coefficient bound, the nonzero remainder polynomial, and the Cauchy root estimate. The normalized affine offsets at odd departure rows are strictly increasing, including on repeated physical cycles. The lifted-vector argument adds exactly three parity coordinates. Applying it immediately before a record maximum gives the stated height bound without assuming that the cycle period is bounded.

**VERIFIED local mechanism, A6.** At a growth edge, `x≡3 mod4`, the next odd value is a nonsquare modulo three, adjacent values are coprime, and the outer gcd divides five. These facts eliminate six of the seven possible square products. The remaining third value is an actual square. Its following valuation is two, and the three-step estimate is `32 U³(x)≤27x+23<32x` for `x≥5`. The strong induction follows the same source and its actual tails. The Lean theorem's hypothesis is the local dependence at every relevant future triple; it is not inferred for arbitrary sources.

**VERIFIED as written mathematics, A7.** Checked the integer rounding `2^A_i≤3^i`, the normalized offsets in `[0,4]`, the unique ternary-unit coordinate, the three grid numerators, and the rational separation. The real error is below `80/n`; `80·16·3^36<2^71`. The dimension-three binary kernel has total weight at most 52 across its seven nonzero words, forcing a relation of weight two, four or six. The final all-source rank-seven corollary is separately SOURCE-QUALIFIED by Barina's published verification below `2^71`. That range calculation is not rerun here.

**VERIFIED probability argument, A8–A9.** The randomness concerns characters, with one ordinary seed fixed. A codimension-three restriction costs at most a factor eight per block; Hölder retains that single factor across arbitrarily dependent blocks. The geometric-grid Borel–Cantelli argument and interpolation are valid. The specified modulo-eight characters are exceptional candidates, not samples to which the Haar-almost-every conclusion can be applied. Their compulsory bias follows from the actual valuation table and the ordinary telescoping bound.

The private-prime argument and the known-convergent controls use the cited integral-point finiteness theorem for finitely many fixed nonsingular curves. Its hypotheses and the ordinary parity decoding were reconstructed; the external theorem is not a Lean dependency in this packet.

## Constructive lane

**VERIFIED as written mathematics, elementary portal §§1–3.** Reconstructed legality of every intermediate inverse stage from the final affine congruence, including positivity and the initial doubling pad. The constructed exponent distribution has a separate full-period variable. After the prescribed number of differences every off-diagonal character has conductor between two and the full-period precision, so its expectation vanishes. Diagonal probability is at most `j/M`. The two conductor-three Fourier terms contribute positively; they are not incorrectly treated as small. The remaining character sum is bounded by the displayed geometric series and `3^m ρ^(r+1)`. Ordering disjoint exponent windows preserves all physical gap inequalities.

**VERIFIED algebraic radix construction.** The cumulative-control derivatives are the prefix remainders `wR^j`. Half-precision linearization is exact modulo the full ternary modulus. A radix of ternary valuation one supplies the required fine digits. This algorithm has the larger clock bound stated in the source; finite controls do not claim to execute the enormous analytic witnesses.

**VERIFIED paired cusp and event grammar.** The common clock and common grade of the ordinary seeds 4 and 11 lift to the displayed all-depth family. Nonzero normalized carry follows from ternary units and persistence of an actual merger. Between odd events common halvings divide this carry by two. The event recurrence therefore enumerates all clock lengths at fixed odd budgets. The finite counts are diagnostic; neither their growth rate nor all-class controllability is extrapolated.

The separately source-qualified short-power-sum improvement invokes the precise external lemma stated in the source. It is kept distinct from the elementary theorem. Prescribing one ancestor does not transport the label of three times that ancestor, and none of these constructions gives strict descent from the fixed endpoint.

## Operator lane

**VERIFIED as written mathematics, O1–O3.** The component map annihilates every transport boundary. Finite charges can be transported to a common actual vertex; a positive cycle has an invertible damped circuit. Advancing an escaping tail makes its residual distortion tend to one, proving the quotient norm and the Cesàro norm identity. Summable truncation justifies the first-hit trace in `ℓ∞/c₀`, its complete cluster set, and its ray-level description. The source at a multiple of three has only doubling predecessors, providing the zero cluster value.

Checked the primary Garcia–Tal paper, Lemma 3 and equation (6), for the uniform translated-interval statement. For an eventually periodic orbit, deleting the at most `h` transient states just before cycle entry makes the time-`h` map injective on the remaining orbit set. This is the additional argument needed to apply the same bound uniformly to finite orbit sets.

On an escaping component the unique forward-coalescence structure supplies a consistent unitary gauge. Arbitrary noncommuting edge weights therefore preserve the escaping-component residual space. This is a real obstruction to the proposed operator route, not an independent proof that this space is zero.

## Formal and computational scope

The replay driver rebuilds every new Lean module in a fresh project-object directory and requests an axiom audit for every public theorem. It rejects proof placeholders, extra axioms, native decision shortcuts, warnings, and missing audits. The pinned Mathlib source is independently checked against the cached source tree: all 9,114 Lean/configuration files matched at revision `d13f23b723b8a846827a245b89c10fc7d3f11612`. Reused dependency objects and freshly built project objects remain distinct in the receipt.

Finite scripts use explicit checks, and the replay compares normal and optimized Python output. The complete-checkout validator tests repository integrity and its declared regressions. It does not certify the infinite written arguments. The forthcoming exact replay receipt, rather than this review narrative, records which commands actually ran at the published checkpoint.
