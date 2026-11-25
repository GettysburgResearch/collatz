# Second live source review before publication

The user's renewed request to step back over the repository prompted a second live GitHub refresh. Of the forty most recently updated open PRs, three heads changed after the initial source intake. Each changed head received a separate exact-source review. These are source and mathematical comparisons; their upstream Lean projects were not rebuilt or imported into PR197's proof path.

| PR | Earlier head | Newly reviewed head | Review |
|---|---|---|---|
| 192 | `570476be82f706122cdd23ebd7a00f3d4ff90cd8` | `07d494324c7ea440d45845d725f5cebad8a67124` | [LIVE_192_REVIEW.md](LIVE_192_REVIEW.md) |
| 195 | `5b2bdcb6e4e60da15c29eadff8bd08b3991c5b57` | `4fd8af31c1ea525252b4d8f7411b5921dd447048` | [LIVE_195_REVIEW.md](LIVE_195_REVIEW.md) |
| 206 | `b2b56b94175174a680a296478f16c619a8828972` | `45a6a111321f947a8482c9e96e898435b57cee09` | [LIVE_206_REVIEW.md](LIVE_206_REVIEW.md) |

## The stronger fixed-tower theorem

PR206 supplies a genuine statement on the **prescribed odd base** w. For every starting rank s there is d<=2^1379 and a common positive endpoint y below 3^(s+d)w such that all 513 values 3^(s+d+r)w, 0<=r<=512, meet y after 1381 clocks. This is stronger than choosing a favorable new base. The ordinary base remains fixed, but the offset on its tower is selected.

Its conditional consumer requires a rank-zero disagreement in basin labels to recur in every 512-edge window. A PR197 reverse defect gives the initial disagreement C(w)=false, C(3w)=true. Neither the new merger nor our smaller-query results prove the needed recurrence. A constant tail after one initial change is an abstract label sequence compatible with arbitrarily long constant blocks; it is not asserted to be a realizable Collatz orbit. The endpoint inequality is relative to a potentially enormous shifted vertex, not to the original least defect or its 2^40 return floor.

The root independently fetched the exact `TowerFrontierMergers.lean` and `TowerRecurrence.lean` blobs and checked these quantifiers and the explicit recurrence premise. The accompanying source review retains both Git blob IDs and SHA-256 hashes.

## Actual certificate transport and the two difficult rows

PR192's `canonical_height` requires an odd factorization 27z+5=2^(7+2k)u and k>=91. The root independently read this theorem and `canonical_suffix` at the new head. On our e=7 row, 81z+527=1024*2^j gives

    3(27z+5)=512(2^(j+1)-1),

so k=1. The suffix gives the familiar good u=(2^(j+1)-1)/3 and bad 3u, but does not meet the height threshold. On the e=6 row, 81z+271=128*2^j gives

    3(27z+5)=256(2^(j-1)-1),

whose exact valuation is even and does not fit the slice. The more general signed-prefix theorem requires supplied compatible charts; it does not construct a legal smaller chart for every surviving source. The global rational-model and parity-series statements also require structures not constructed for every actual orbit.

## Full cycle denominators

PR195's new criterion reconstructs the entire denominator condition for a supplied near-critical bounded-cycle word. A failed word has a bounded window witness under the stated assumptions. It does not prove that every nontrivial admissible word fails, and it does not exclude an unbounded trajectory. Its new positive descent families vary the base; its final Lean theorem still takes `FrontierMerger` as an explicit argument. The root independently fetched that final file and checked the argument is passed directly to the preceding equivalence.

## Effect on the proposed proof

These new sources sharpen both the available certificates and their limitations. They do not discharge `ClosingProposal.RemainingExclusion`, so no unproved upstream result was added to the local theorem. The final packet preserves the stronger PR206 quantifier and the exact remaining recurrence problem rather than describing it as selected-base coverage.
