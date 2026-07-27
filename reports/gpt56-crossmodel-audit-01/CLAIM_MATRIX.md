# Claude / Opus / Fable cross-model audit matrix

**Reviewer:** `gpt56-crossmodel-audit-01` (`GPT-5.6 Pro`)  
**Date:** 2026-07-27

## Frozen heads

```text
Claude symbolic rewrite: 407a788972a72da2fde59c19e9446e02647cc4f4
Fable foundry/cone:      0888a211f2703f5d3082e60fcbd0e8002b4b4650
Fable/Opus foundations:  2cb80b4629ebfde5c8aaa3433c38e1382ea956b7
```

`PENDING SEPARATE REVIEW/REPLAY` is neutral: it means this pass did not execute or reconstruct the full named object.

## Claude symbolic-rewrite packet

| Claim/group | Verdict | Finding |
|---|---|---|
| Status/provenance discipline | **PASSED** | Claims enter as `PROPOSED`; author reproduction is not called independent review. |
| `L-0001`–`L-0010` elementary affine/rigidity interfaces | **PENDING SEPARATE FULL REVIEW** | Spot checks found no new defect; several overlap independently developed repository claims. |
| `L-0011` Markov digit decomposition | **PASSED** | Reconstructed from one unit state modulo `81^r` and successive base-81 digits. |
| `L-0012` shifted cosine Riemann sum | **PASSED** | Standard bounded-variation estimate; distinct from the already conceded `T-0012` valuation gap. |
| Historical `T-0012` depth contraction | **GAP, ALREADY CONCEDED** | Source correctly demotes it to `PARTIAL`; phases can vanish for `81`-divisible frequencies. |
| `L-0020` position-free frequency-block mean | **GAP AS SUBMITTED; REPAIRED** | True reciprocal phases carry an explicit nonzero error omitted from the proof. `L-7701` proves the exact replacement `mean <= (7/10)^r`. |
| `T-0030` density-one full EQ assembly | **GAP / PENDING ASSEMBLY REVIEW** | Depends on submitted `L-0020`, references a superseded historical PR16 assembly, and compresses fair-window/minimal-survivor consequences needing separate review. The repaired block input is now available. |
| Bounded numerical EQ evidence | **EMPIRICAL WITH DECLARED SCOPE** | No extrapolation accepted. |

## Fable diagonal-foundry packet

| Claim/group | Verdict | Finding |
|---|---|---|
| `L-9601` parity digit-flip/locality | **PASSED** | Independent induction reconstructs the one-bit flip and finite-prefix locality. |
| `T-9601` unique strictly-causal 2-adic closure | **PASSED** | Strong induction forces exactly one digit at every stage. |
| `T-9602` supercritical integral closure is unbounded | **PASSED AFTER MINOR REPAIR** | The proof's displayed strict lower bound fails on an all-even prefix; replace it by `>=`, with strictness on the supercritical subsequence. Conclusion unchanged. |
| `L-9603/T-9603` finite-state tail collapse | **PASSED** | Eventually constant binary input gives eventually periodic output; parity bijection then yields an integer cycle. |
| `T-9604` unpaired open-loop family equivalence | **SCOPE NARROWING REQUIRED** | The projection loses the equality of the input prefix with the decoded integer prefix; unconditional countability is false. `R-7701/L-7702` give the correction. |
| `X-9601/X-9602` empirical packets | **PENDING SEPARATE FULL-ARTIFACT REPLAY** | The theorem-level findings above do not rely on accepting the complete census. |

## Fable solution-cone packet

| Claim/group | Verdict | Finding |
|---|---|---|
| `T-9701` fixed signals = component constants | **PASSED** | Direct graph argument. |
| `T-9702` extreme rays = component indicators | **PASSED** | Correct in the nonnegative bounded fixed cone. |
| `T-9703` unit-circle point spectrum | **PASSED** | Cyclic components give roots of unity; cycle-free components admit all unit eigenvalues. Exact equivalence, not yet an analytic separator. |
| Actual `T-9704` pushforward/count theorem | **PASSED** | Canonical cycle-to-component injection and finite-cardinality caveat reconstruct. |
| `CONE.md` `T-9704` slogan | **SCOPE NARROWING REQUIRED** | Drops the finite-cardinality caveat; infinite cardinal equality does not imply no divergence. |
| `L-9705` weighted Hilbert setting | **PASSED** | Exact norm and fixed-space dimension reconstruct. It repackages component counting rather than deciding it. |
| Actual `L-9708` space-selection theorem | **PASSED** | Correctly retains the one-dimensional `e_0` summand on `N_0`. |
| `CONE.md` `L-9708` slogan | **REFUTED AS WRITTEN** | Says unweighted fixed space is zero on `N_0`; actual file correctly says `C e_0`. |
| `L-9706/L-9707` analytic functional-equation lane | **PENDING SEPARATE REVIEW** | `Q-9707` remains the real non-tautological separator target. |

## Fable / Claude Opus foundations packet

| Claim/group | Verdict | Finding |
|---|---|---|
| Status semantics | **PASSED** | `PROVED` means initial detailed review under README; packet explicitly says none is cross-model `INDEPENDENTLY_VERIFIED`. |
| `L-9905` cycle equation/product formula | **PASSED** | Exact telescoping and product formulas reconstruct; general-`a` scope correction is preserved. |
| `L-9913` floor-to-cycle-length theorem | **PASSED WITH SOURCE BOUNDARY** | The theorem reduction and `F=10^6` floor replay pass; `m*=2966,K=4701` and `m*(10^9)=47468,K=75235` arithmetic pass. Independent verification of the entire `10^9` finite floor is pending. |
| `L-9915` no cycles through 21 odd states | **PARTIAL CROSS-MODEL REPLAY** | Exact windows and all 648,635 cases through `m=14` replay with zero hits. The `m=15..21` billion-case layer is neutrally pending separate full replay. |
| `L-9918.1`–`.7`, `.9` extraction/method barriers | **PASSED IN THIS PASS** | Least-root dichotomy, adic asymmetry, periodic sign, cusp lower bound, ET constant region, and halting reduction reconstruct. |
| `L-9918.8` exact Parseval identities | **PASSED** | Mean-square identities are correct. |
| `L-9918.8` typical-size/density corollary | **REFUTED / SCOPE NARROWING REQUIRED** | Full-group digit set has mean square `d` but is zero on density `1-1/d`. See `R-7703`. |
| `L-9923` affine-alphabet collapse | **PASSED BY RECONSTRUCTION OF CORE ARGUMENT** | Convex-combination and span threshold `W<P+Q` are coherent; not every packet specialization was replayed. |
| `T-9925` rows through `a=448` | **PENDING INDEPENDENT CERTIFICATE REPLAY** | No concrete defect found; main classification depends on memory-bound phase-floor certificates not executed here. |
| `L-9926` descent-sieve ceiling | **PENDING SEPARATE REVIEW** | Not used in this audit's corrections. |
| `L-9927` S-closure sieve | **PASSED** | Independent exact arithmetic reproduces 166 eliminations, maximum 1024, threshold 1039, and the universal fixed-allowed-set ceiling. |
| `X-9903` larger finite floors | **PENDING INDEPENDENT FULL-ARTIFACT REPLAY** | Neutral execution status. |

## Cross-branch findings

| Finding | Action |
|---|---|
| Fable `L-9918.1` predates the later global `T-7801` least-root dichotomy | Add branch-qualified prior-art note to PR #56; retain distinct signed-chain and expanding-affine contributions. |
| Claude repaired block mean and Fable Parseval result are compatible | Do not use global second-moment losslessness to reject low-frequency first-moment/Markov estimates. |
| Foundry must retain input/output pairing | Search a diagonal graph intersection, not an output language projection. |
| Solution-cone is a faithful reformulation but not a finite witness | Concentrate on `Q-9707`-type analytic separation rather than more equivalent kernel dimensions. |
