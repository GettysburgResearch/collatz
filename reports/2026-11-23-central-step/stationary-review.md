# Independent review: the fast equivalent ordinary flow

23 November 2026. Reviewer: `/root`.

**Verdict: VERIFIED as conditional written mathematics at the exact bytes
listed below.** Given the stated positive ordinary harmonic flow of finite
spine capacity, the construction gives a positive harmonic flow on the same
component, an exponential coalescence tail, and uniform relative collision
comparison at every finite precision. It preserves the entire inverse law
at the original root. It does not prove an original-source collision upper
bound or exclude an escaping orbit.

## Frozen material

| File | SHA-256 |
| --- | --- |
| `research/central-step-20261123/stationary/FAST_EQUIVALENT_FLOW.md` | `97b4fe781a9c6b4922f5d8b6de970056005805595f9b2886f8f6926e695c5724` |
| `research/central-step-20261123/stationary/README.md` | `79fcede53430e4cdb3118165f436f3996565c1100682d5c4b6e381d5ab273321` |
| `reports/2026-11-23-central-step/stationary-sources.json` | `a7d0a2fbacfc3082f982b2cfa2f81f81e2693589ebb895ab7b292efbdf52a5f6` |

The base is `e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`. The review
binds these local bytes, not any later revision. I read the complete new
note and independently reconstructed its graph equations, kernel
comparisons, path change, collision estimates, and source-box consumer.
I also inspected the frozen PR182 source-box injection and count domain,
and PR180's finite-Shannon-deficit versus geometric-iid distinction.
Previously supplied analytic existence and dimension results remain
qualified inputs; this review does not re-prove their dependency trees.

## 1. Harmonicity and the tail

Every parent of an off-spine vertex has the same first spine attachment
index. Consequently its complete harmonic equation is multiplied by a
common factor. At the first spine root all incoming mass has attachment
zero. At later spine root `q_j`, the incoming mass splits into the old
spine parent and an off-spine total `Delta_j=v_j-v_(j-1)`. The new incoming
sum is exactly the new partial weighted sum in equation (4).

The normalizing series is finite and satisfies
`v_0/C <= Z_rho <= 1`. Its weighted tail is bounded by
`rho^(j+1)(C-v_j)/Z_rho`. This proves the positive flow, capacity `C`,
upper comparison with the old flow, and exponential tail. Every original
edge remains present. This constructs a different law; it does not imply
that the previously fixed canonical flow had this convergence rate.

## 2. Exact original-root preservation

Every ancestor of `q_0` attaches at zero and is multiplied by `1/Z_rho`.
All transition ratios on its inverse cone therefore remain exactly the
same. For each fixed later root `q_j`, the flow ratio throughout its cone
lies between `rho^j/Z_rho` and `1/Z_rho`. A finite cylinder's likelihood
ratio telescopes to a quotient of two such values, giving the claimed
bounds `rho^j` and `rho^(-j)`. They extend to the inverse path laws.

Thus the original-root reciprocal floor is preserved with one common
factor; each fixed later root has its own comparison constant. The note
correctly declines to infer a single reciprocal floor on the entire
component. Any subsequent pressure argument needing that stronger floor
must supply it separately.

## 3. Exact total variation and all-precision collisions

For inverse depth `r_j` from `q_(j+r_j)`, the retained endpoint mass at
`q_j` is `v_j^rho/v_(j+r_j)^rho`. No other forward-spine point can be an
endpoint at that depth, because the spine is injective. Hence the missing
spine mass and off-spine mass have disjoint supports and give the exact
total-variation formula. Its upper bound sums a single geometric tail,
uniformly over all finite deterministic depth choices.

For a finite quotient, the difference of the two probability vectors has
positive and negative mass at most the total variation. Its Euclidean
norm is at most `sqrt(2)` times that variation. The reverse triangle
inequality therefore bounds the difference of square-root collisions.
The empirical law has `N` distinct ordinary atoms, so its residue
collision is at least its diagonal `1/N`. Division by that lower bound
gives equation (12), including the positive part needed when `delta_N>1`.
The same proof applies to every finite partition. No restriction relating
the precision to `N`, or the inverse depths to `N`, was used.

## 4. Whole-path law and occupation scope

Under the separately supplied aligned whole-path probability, the first
attachment distribution has mass `v_0/C` at zero and `Delta_k/C` at `k`.
Its bounded positive density `rho^tau/Z_rho` has expectation one and
gives exactly the new vertex marginals. The change is fixed once for the
source, equivalent to the original law, and bounded above. The original
root's boundary law is literally unchanged. Other dimension transfers
are expressly conditional on the pinned fixed-absolute-continuity result;
they are not consequences of an arbitrary entropy transfer principle.

The occupation identity uses the complete injective path, so each
ordinary vertex is counted once. Tonelli gives the displayed count
bound under the changed measure. PR182's count applies to the whole
forward-invariant injective path, which is the domain used here. It is
not applied to the branching basin. The source-height factor in weighted
comparison with time averages remains; the reweighting does not remove it.

## 5. Complete source boxes and the exact remaining estimate

PR182's box retains the full binary clock, the translated full carry,
and the translated original source. Within each such box, an endpoint
residue identifies the actual occurrence. Thus its empirical collision
is exactly `N_B/N^2`. Summing Euclidean norms across boxes gives the
square of the sum in equation (17), not an independent sum of energies.
The discarded initial `m` labels have mass at most `m/N`.

For the new inverse law, retained individual spine masses are at most
`1/N`. The entire off-spine remainder has mass at most `D_rho/N`.
Applying the same nonnegative decomposition proves equation (18), with
`m+D_rho` in the numerator. No additional `sqrt(2)` is needed in this
direct decomposition; that constant belongs to the separate signed
total-variation comparison.

If the effective box count were subexponential at a precision with
`N` comparable to `3^(theta m)`, the bound would have the critical
exponent with subexponential loss. The note correctly limits the proposed
contradiction to PR180's finite-deficit branch at compatible growing
precision. The geometric-iid equality branch still has its stated order
of limits. No bound on the actual effective box count has been proved.

The elementary construction and all its consumers above are written
proofs. This review ran no Lean build and no old proof-corpus rebuild.
It does not certify the unproved universal collision estimate, transfer
the higher-rank thickened law to the original orbit, or resolve Collatz.
