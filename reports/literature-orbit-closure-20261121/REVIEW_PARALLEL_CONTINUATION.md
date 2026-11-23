# Root mathematical review of the parallel continuation

This is a source-level reconstruction, not an additional compiler receipt.
The reviewed documents and exact SHA-256 values are listed below.

The canonical-capacity proof was independently reconstructed from its stated
PDU and fixed-basin inputs. Finite stopping lines are genuine reachability
antichains, the population estimate bounds their reciprocal mass, and the
weighted interval slices are antichains with the correct orientation. The
resulting summable weight and harmonic flow are valid on nonperiodic odd
units. Periodic nodes are explicitly excluded. The harmonic flow has bounded
pointwise values and finite reciprocal-weighted total; finite unweighted mass
is neither established nor used. The review does not independently certify
the non-elementary joint renewal argument in PR180.

The fixed-affine no-cover argument was reconstructed using the unbounded
initial odd runs of the already proved marked family. Shrinking marked width
forces a dyadic slope on any cofinal marked-to-marked subsequence; parity-word
coefficient matching then contradicts strict decrease at fixed clocks. Its
scope excludes unbounded clocks and intermediate non-marked partners.

The half-selector source formula, CRT phases, meeting clocks and no-descent
inequality were independently reconstructed. The natural-density tail bound
and finite overlap formula use actual residue progressions, not extrapolation
from a finite trajectory sample. Density refers to successful smaller-source
certificates; convergence still requires its induction hypothesis.

- `CANONICAL_FINITE_SPINE_CONCENTRATION.md`: `d9ff2f15148a2d5f0571c23c48d3976c450275d6abc9affd5a1ec31ce335adc7`
- `FIXED_AFFINE_MARKED_COVER_LIMIT.md`: `b950bd5e74d0ac0f4beeac7427bbb448c6731178391730b74dea1d6ffbecba54`
- `AL27_HALF_ROUTE.md`: `f370fa28560d36cbd63abaaf15cd497923170cad4fe00ea477755ec9e4932d76`

The residual selector's two later additions were also reconstructed. Starting
at T^3(n)=2^(k+4)w-1 instead of T^7(n) gives the smaller source
x=2^(k+1)w-1, with64x+51=9n and clocks k+9/k+15. On the W=129mod256 phase,
the final endpoint segment has seven halvings and one odd step. For k>=8,
729*3^k>=16384*2^k guarantees that even its minimum stays above the original
source. These are distinct from the broad half selector, which works at every
k>=0 with its shorter two-halving endpoint segment.

Final residual-source hashes:
- `ResidualPrefixErasure.lean`: `b4d8ae889c458ee26c3ea8d3c362290c465a725f024d53e1f3978290c6661a9c`
- `ResidualPhaseSelector.lean`: `46fd0b12977611a5a39b0bd400602ca41f7b1479e01b6dee5c004f86c134b930`
- `AL27HalfSelector.lean`: `75f0ca9b1b9c2b525a78323f4edb2efa57c87e4e586e07a60049dc622ee83bde`
