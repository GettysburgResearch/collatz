# Coordinator reconstruction of the final joint argument

Scope: the eight new formal modules and the final written manuscripts listed in `source-hashes.json`, built on PR197 head `578e43911f49d41ef610b368a89b5a1ec269e134`. I reconstructed the arguments separately from their authors' derivations and inspected the relevant frozen PR146 proofs and the primary short-block clock estimate. This is a narrow internal review, not a proof of universal convergence.

## Strongest result: every fixed-triple moment below three halves

The three profiles on an exposed source cylinder all have odd coefficients of the remaining quotient. Their next parity vector is therefore one fixed vector or its complement, with equal probabilities. Every labeled grade difference is a bounded-increment martingale; the pair marginals remain the actual canonical pair chains even after the full three-arm past is fixed. No independent pair or fresh landing distribution is introduced.

I checked the physical occupation input directly against frozen PR146 `THREE_RAY_UPPER.md`. A positive-level excursion contributes `2 min(s,l)` expected visits to level `l`; the expected wait is bounded by `v₂(3^l−1)+2`. Subsequent excursions and boundary phases cost a constant times `1+sqrt(|D|/3^s)`. This gives the uniform low-band Green bound. Killing at the first merger of any of the three pairs only reduces nonnegative offset contributions. Its contracting convolution bounds the killed offset moment by the earlier triple-survival probability plus an exponential remainder.

For the basic ordered-gap product, the strict-order drift is exactly minus the middle-isolation indicator. Resolving a tie injects at most one times the new spread. The dyadic occupation estimate and Azuma control the sum of these injections. Averaging a shell is converted to a pointwise bound only for the monotone first-merger survival probability. Repeating the argument gives `P(t)=O(1/t)` and finite total middle-isolation occupation.

For the stronger potential `uv(u+v)^γ`, `0<γ<1`, the exact Hessian contraction is

\[
\tfrac14(f_{uu}+f_{vv}-f_{uv})
=\tfrac{\gamma-1}{4}\big(U^\gamma+\gamma uvU^{\gamma-2}\big).
\]

The separate Lean module verifies the actual second derivatives along all directions before specializing to this expression. Its domain includes `u=0` or `v=0` when `u+v>0`; the negative estimate requires both gaps nonnegative and the stated strict exponent range. The stochastic block use restricts to positive, well-separated gaps.

The external step is **equation (21) in the proof of Theorem 6 of rStation paper 13, version 1**. I read the primary displayed estimate and its surrounding derivation at the unversioned page, whose header identifies v1. It is unconditioned, uniform over arbitrary integer offsets and gaps up to `K`, and applies to a prescribed mixed-step quota or earlier level-one hit. The versioned URL and the Leen deposit were inaccessible to this browsing tool; this is not claimed as an independent rebuild of external Lean sources.

At a deep block the gap cannot reach one within either requested quota, so the completion event in that estimate is certain. The physical block has length comparable with `H^(1/4)`, while its maximum initial gap is `O(H)`; hence the estimate's logarithmic parameter is small enough for its error to tend to zero uniformly after the exact shared prefix. The contribution of bad clock outcomes is bounded by their probability times the block length. This establishes the conditional expected covariance, not an independent Brownian approximation.

I recomputed the Taylor error. Freezing the Hessian across a block costs `O_γ(B² U_*^(γ−1))`; the fixed depth multiplier can absorb this into the negative `B U_*^γ` term. A block classified as near a tie at its start retains one specified close labeled pair at every later live clock. Its positive drift is therefore paid by actual low-gap occupation. Ties cost `U^(1+γ)` times true triple-live tie occupation. With the reciprocal tail and the Azuma envelope, both dyadic costs have exponent `(γ−1)/2` up to logarithms and are summable.

The deterministic power-of-two blocks tile each dyadic shell. At every finite terminal endpoint the potential is integrable and nonnegative, so finite telescoping bounds the negative drift without assuming an unknown terminal moment. This gives finite total `U^γ` occupation. For the final time moment, the small-spread part is charged to the earlier quarter-shell with coefficient `O(ε)`. It is absorbed **before** taking the finite cutoff to infinity. Tail summation then gives every `p=1+γ/2` in `(1,3/2)` and all smaller positive moments. Monotonicity yields the little-o estimate. Complete binary blocks transfer the actual finite event uniformly in ordinary interval location.

Verdict: **VERIFIED written deduction with the stated source-qualified clock input**. The full probability theorem is not a Lean theorem in this packet. The endpoint `p=3/2`, uniformity in growing families and the two-class case are not included.

## Landing-weight and joint-clock interfaces

The first-passage sliding tests make the sum of pre-entry reciprocals at most `O(log d/M)` by a reverse geometric series, with all original sources retained. Stagewise maximal binomial deviations imply a deterministic entrance-clock window with `O(sqrt(d log d))` possible clocks. For one fixed clock and endpoint, the narrow source annulus admits only one odd count. The fiber is contained in an ordinary parent-coordinate interval of length `O(R log d/M)`. Applying the original uniform-location head merger bound inside that interval, before summing the possible clocks, gives the announced per-endpoint cap. I checked that the exceptional set is independent of the tested endpoint sets and that fractional covers do not pay it repeatedly.

The formal endpoint theorem has the strict condition `3YU < 3(3Y−t)L`. Multiplication by the reciprocal Bernoulli bound and cancellation of positive powers of three give odd-count uniqueness. Its simpler annular assumptions `2t≤3Y` and `2U<3L` imply that condition. This removes the odd-count index from the existing finite cardinality bound. No asymptotic time law is hidden in its hypotheses.

For the joint clock theorem, doubling shifts both physical clocks by one and preserves both odd counts; tripling preserves physical clocks and lowers both odd counts by one. The extra step in the doubling comparison is essential. All prefixes stay above the prescribed entrance sets by `2^hY<X`, including the added step on the doubled arms. First-hit values, missing status and signed gaps are retained even when the respective fusion clocks differ. Near-equal **full intervals**, followed by averaging all modular translations, give the total-variation estimate without a factor equal to the number of bins. A selected population of mass `δ` only inherits the absolute estimate divided by `δ`.

The typical strip exponents are `O(sqrt(d log d))` because both passage clocks lie in the displayed window; the exact logarithmic relation then gives the same range for the odd-count difference. The two-logarithm separation is applied at this smaller coefficient range. It does not assert mixing within any strip.

## The unresolved two-class contribution

The suffix-73 cylinder was independently checked from its ordinary formulas. On `n=32q+23`, both dilated arms can join the original upper arm, leaving only `z=27q+20` and `9z+2`. A positive finite-certificate discrepancy of order `1/sqrt(log R)` survives on the actual head rows. It is outside the event controlled by a theorem about three surviving classes.

The exact identities are Lean-checked for every `q≥0`. The square-root lower tail is a written fair-walk transfer. Neither implies different eventual colors. Likewise, a positive amount of joint diagonal mass, marginal entrance control, or uniform common modular grades does not bound the full weighted off-diagonal color mass. The final closing series remains explicitly open.
