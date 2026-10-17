# Issue-#4 symbolic-rewrite claim-to-literature map

**Snapshot:** `claude/collatz-migration-math-osr370@41617a5`
**Namespace:** `CLAUDE/...`

## Lemmas

| Claim | Verdict | Source / correction |
|---|---|---|
| `CLAUDE/L-0001` `c_w≥0` | **KNOWN — COROLLARY** | Terras affine formula; immediate from the explicit positive sum. |
| `CLAUDE/L-0002` affine-constant upper bound | **UNVERIFIED AS ATTRIBUTION** | Likely elementary in the branch notation; no printed exact bound located. Keep native proof. |
| `CLAUDE/L-0003` suffix multiplier bound | **UNVERIFIED AS ATTRIBUTION** | No exact source located. Keep native proof and definitions. |
| `CLAUDE/L-0004` valuation “fuel conservation” | **KNOWN — COROLLARY** | Terras 1.2 plus one-step difference calculation; full proof in `LIT-KTHM-0002`. |
| `CLAUDE/L-0005` `A log3=S log2` | **FOLKLORE / STANDARD** | Unique factorization alone; Gelfond–Schneider is unnecessary here. |
| `CLAUDE/L-0006` sign-criticality | **PARTIAL OVERLAP** | Rational-cycle literature (Lagarias) supplies context; fixed-point sign calculation is elementary and native. |
| `CLAUDE/L-0007`–`L-0010`, `L-0014` | **POSSIBLY NOVEL FORMULATION / INTERNAL** | Exact phase, bridge, and carry gadgets; no external antecedent located. |
| `CLAUDE/L-0011` Markov decomposition | **POSSIBLY NOVEL FORMULATION** | Riesz/self-similar products are nearby, not this exact finite-group bijection. |
| `CLAUDE/L-0012` shifted cosine average | **FOLKLORE / STANDARD** | Elementary analysis; retain full native proof rather than seek attribution. |
| `CLAUDE/L-0013` `⟨64⟩ mod 81^j` | **KNOWN — COROLLARY** | Odd-prime LTE; completed in `LIT-KTHM-0003`. |
| `CLAUDE/L-0015` periodic skeleton fixed point | **FOLKLORE / STANDARD** | Composition of affine maps; native integrality search remains computational. |

## Theorems

| Claim | Verdict | Source / correction |
|---|---|---|
| `CLAUDE/T-0001` H-rigidity | **POSSIBLY NOVEL FORMULATION** | Uses elementary affine bounds and unique factorization; no exact printed theorem located. |
| `CLAUDE/T-0002` `V∞` coding and rational periodic codes | **PARTIAL OVERLAP** | Bernstein–Lagarias gives standard-map 2-adic conjugacy. The exact `H` attractor and interval bound are native. |
| `CLAUDE/T-0003` automaticity package | **KNOWN — COROLLARY, wording correction required** | Use `LIT-KTHM-0004` and `LIT-KTHM-0005`, not the two-base Cobham theorem. “Exactly Sturmian/Ostrowski” is not implied. |
| `CLAUDE/T-0004` schedule locking | **POSSIBLY NOVEL FORMULATION** | Periodicity calculation is native. Exact Ostrowski-computability source not matched. |
| `CLAUDE/T-0005` supply isometry | **KNOWN — COROLLARY + NATIVE CONSEQUENCE** | LTE gives the isometry valuation; class-count/density conclusion follows from the native bijection. |
| `CLAUDE/T-0006` SML finiteness | **KNOWN — COROLLARY, reduction pending** | `LIT-KTHM-0008`; display coefficients and zero cases before calling it closed. |
| `CLAUDE/T-0007` product formula | **FOLKLORE / STANDARD** | Fourier transform of independent finite digit choices factors; exact coefficients are native. |
| `CLAUDE/T-0008` cascade lemma | **POSSIBLY NOVEL FORMULATION** | No exact source located. |
| `CLAUDE/T-0009` self-similarity and sharp maximum | **POSSIBLY NOVEL FORMULATION** | No exact source located; stationary self-similar papers do not imply it. |
| `CLAUDE/T-0010` exact-run rigidity | **POSSIBLY NOVEL FORMULATION** | No exact source located. |
| `CLAUDE/T-0011` block-mean decay | **POSSIBLY NOVEL FORMULATION** | Li–Sahlsten/Solomyak are methodologically nearby but outside the current object class. |
| `CLAUDE/T-0012` fixed-frequency density-one depth decay | **POSSIBLY NOVEL FORMULATION** | Same caveat; native proof must stand alone. |
| `CLAUDE/T-0013` schema rigidity | **PARTIAL OVERLAP** | Exponential-polynomial and SML literature supplies tools, not this dichotomy. |
| `CLAUDE/T-0014` entropy cost floor | **KNOWN — COROLLARY + NATIVE COUNTING STEP** | Binomial entropy bound in `LIT-KTHM-0009`; inequality linking fibers to the supercritical tail is native. |
| `CLAUDE/T-0015`–`T-0017` chart/conjugacy/injectivity | **POSSIBLY NOVEL FORMULATION / INTERNAL EXACT** | No external chart antecedent located. |
| `CLAUDE/T-0018` explicit 2-adic boundary point | **PARTIAL OVERLAP** | Classical 2-adic parity coding; explicit aperiodic construction is native. |
| `CLAUDE/T-0019` order lifting | **KNOWN — COROLLARY** | Fully proved for all levels in `LIT-KTHM-0003`; the branch's current `PARTIAL` gap can be closed. |
| `CLAUDE/T-0020` skeleton rigidity | **KNOWN DEPENDENCY, NATIVE THEOREM** | Replace “Kronecker criterion” with `LIT-KTHM-0007`; ensure minimal noncancelling base representation. |
| `CLAUDE/T-0021` free bridge nullity | **KNOWN — COROLLARY + NATIVE ECONOMICS** | Terras parity bijection and odd affine permutation; full core proof follows `LIT-KTHM-0001`. Relay-cost corollary is native bookkeeping. |

## Open questions and analogies

| Claim | Literature assessment |
|---|---|
| `CLAUDE/Q-0001` M1 | Native existence problem. Classical 2-adic conjugacy supplies language, not an answer. |
| `CLAUDE/Q-0002` M2 | **Analogue only** of Mahler Z-numbers. No equivalence or FLP transfer located. |
| `CLAUDE/Q-0003` EQ interchange | Modern Fourier-decay papers suggest renewal/product methods, but direct hypotheses fail. |
| `CLAUDE/Q-0004` capacity | Applegate–Lagarias/Krasikov–Lagarias are plausible methodological inputs; exact object mismatch remains. |
| `CLAUDE/Q-0005` orbit normality/rigidity | Furstenberg/Rudolph/Shmerkin/Wu concern invariant measures/sets, not one integer point. |
| `CLAUDE/C-0003` width exponent | No external theorem located. Compare carefully with `PR3/T-0005`, whose constructed family may use a different depth/geometry regime. |

## Required wording changes before literature-backed status

1. `T-0003`: say “Cobham's rational-frequency theorem for uniform tag/automatic sequences,” not merely “Cobham's theorem.”
2. `T-0006`: expose the exact power sum and coefficient audit.
3. `Q-0002`: consistently say “2-adic analogue,” never equivalence to Mahler's original real problem.
4. `MINIMAL.md` EQ paragraph: describe Li–Sahlsten/Solomyak as nearby fixed-real models, not theorems applying to the current triangular array.
5. `T-0020`: cite the integral-denominator theorem and remove the ambiguous “Kronecker criterion” attribution.
