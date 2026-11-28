# Independent review of the anchor Green word-tail defect

**VERIFIED at the stated written, source-qualified scope.** The imported positive Green representation, fractional bound and orbit-packing premise remain named inputs. No no-escape theorem or cycle exclusion is certified here.

Reviewed source: `research/astra-collision-factor-bridge-20261128/arithmetic/ANCHOR_GREEN_TAIL_DEFECT.md`.

Reviewed SHA-256: `333c3350e4bf767684dd303d0776b60bef891c4e3a2225e42c60c373af23eb75`.

Review time: 2026-11-28T10:42:51.002703+00:00.

## Reconstructed estimates and limits

The source weight w(x)=ψ(x)/x is absolutely summable. For the J(x,−1) term, grouping by j=v₃(x+1) gives the majorant 2·3^(−sj)u^(−1−s); summing the u-tail up to the logarithmic j cutoff costs O(M^(−s)log M), and the remaining j-tail is geometric. For LR_s the exact edge identity turns its normalized sum into c(x)R_s(x)/x. The condition U(x)>M implies x>(2M−1)/3, giving the stated O(M^(−s)) tail. Both sums are positive, so no cancellation or unjustified rearrangement is used.

For a nonperiodic target each predecessor has a unique visit depth. Expanding the positive Green series then gives G(a)/a=Σ_(x reaches a) w(x) f_(τ_a(x))(x), with the summable majorant w independent of both the target and depth. Along an escaping ray every fixed source in that component eventually reaches all sufficiently late vertices; sources outside it never do. Dominated convergence therefore gives precisely γ_B. This limit interchange is justified, unlike the uniform anchor-word interchange being tested.

Finite truncation in the explicit source weight proves the global limsup formula: a target missed by all sources x≤M contributes at most the w-tail; finitely many eventually periodic rays contribute only finitely many nonperiodic targets; each remaining escaping ray tends to its own γ_B. Summability over disjoint components makes a positive supremum attained. These arguments require neither natural-density additivity nor a minimum distribution.

The finite-prefix estimate is algebraically correct. Every anchor remains at least−1. If b_w<a, N=2^D(a−b_w) is a positive integer with the same 3-adic valuation as a−b_w; hence 3^v≤N. Multiplying by m_w gives 3^(sn)2^(−sD)(a+1)^(1−s). Summing all positive exponents, including arbitrarily large ones, yields Q_s^n with Q_s=3^s/(2^s−1). This proves fixed-depth normalized decay but supplies no uniform summable depth majorant.

For fixed N, removing that vanishing prefix leaves the same large-target limsup Γ. Thus every normalized tail supremum is at least Γ. Conversely large targets have G(a)/a≤Γ+ε, while the finitely many remaining target tails vanish individually. This proves the exact uniform tail limitΓ. The note correctly treats this as a full no-escape obligation under the packing premise, not as a completed bound.

## Analytic boundary and source pins

Positivity of γ_B needs the stated summable-reciprocals/packing premise. Escape alone gives distinct states and divergence of height, but does not by itself justify a positive infinite product. I independently opened Paper176 v1 Section1, which explicitly restates the packing input and its lower survival-product consequence. Its original Markdown pin is `6ae88cbd18fc56a1f223c52cdd7446cf3f81cd39c3d531283f4a1c80e52d3ebb`. The earlier positive Green comment is pinned at `43a249cc086c9d22487d8850f5fa07ca1f85a824c2009fb8156c489df5146b94`. Their full analytic proofs were not rebuilt by this review.

The fallback without the packing premise is properly qualified: the same formulas retain the possibly zero component weights, and detect only escape with positive surviving product. The nonperiodic-target restriction also correctly prevents repeated cycle visits from invalidating the unique-depth formula. The final note's two display-spacing typos were fixed before the reviewed hash above.
