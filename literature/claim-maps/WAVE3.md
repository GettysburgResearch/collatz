# Claim map — literature audit wave 3

All references are branch-qualified. Verdicts do not promote native statuses.

## Diagonal Foundry (`FOUNDRY/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9601` flip lemma | KNOWN — COROLLARY / self-contained refinement | Bernstein--Lagarias parity conjugacy and finite two-lift bijection | Check exact digit orientation against the chosen `Q/Phi` convention |
| `T-9601` unique causal closure | KNOWN — COROLLARY | `LIT-KTHM-0028`: `Phi o E` is a `1/2`-Lipschitz contraction | None for existence/uniqueness; integrality remains open |
| finite-state operator taxonomy | PARTIAL OVERLAP | `LIT-KTHM-0029`, Anashin van der Put criterion | Normalize coefficients; implement exact conversion |
| `T-9602` supercritical integer criterion | FOLKLORE / NATIVE COROLLARY | finite affine iterate and positive parity-density growth | Audit limsup/tail-density hypotheses and positivity |
| positive-integral fixed point search | OPEN NATIVE FRONTIER | no located theorem turns causal fixed points into ordinary integers | Design operator classes with provable eventual-zero digits |

## PR #3 (`PR3/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `T-0018` critical particle completion | PARTIAL OVERLAP, strong native realization | `LIT-KTHM-0032` size-biased spine / many-to-one | Verify exact child/rank formulas; exploit martingale toolkit |
| `T-0019` ordinary-spine likelihood | KNOWN STRUCTURE + NATIVE IDENTITY | Doob transform and spine Radon--Nikodym product | Use the identity to constrain connector/Hensel grammar |
| `L-0016` binary-to-ternary tail replacement | POSSIBLY NOVEL FORMULATION | affine word calculus; rational-base conversion neighbors | Independent proof reconstruction |
| `L-0017` universal connector | POSSIBLY NOVEL FORMULATION | CRT and coprime affine coordinates | Ordinary initialization and positivity remain separate |
| `T-0021` finite-library transition obstruction | KNOWN — COROLLARY, reduction pending audit | Skolem--Mahler--Lech / power-sum finiteness | Expose exact recurrence, coefficients, degeneracies, effectivity boundary |
| `L-0023` quadratic stage defect | KNOWN — EXACT REINTERPRETATION | `LIT-KTHM-0030`: divided exponential converging to `-(7/4)log_2 3` | Replace opaque recurrence by explicit log target |
| `L-0024` odometer law | FOLKLORE / STANDARD | `2`-adic isometry and LTE | Independent index/modulus audit |
| `T-0024` information surplus | INTERNAL PROPOSED THEOREM + EXTERNAL ROUTER CRITERION | `LIT-KTHM-0033`: Krieger/MacDonald turn entropy surplus into finite-memory embedding after an SFT reduction | Build stationary normalized legal-transition SFT; prove mixing, entropy, periodic-point, and visible-output conditions |
| 256-transition macro | OPEN NATIVE FRONTIER | symbolic embedding or Hall-type routing plus `p`-adic digit generation | Exact arithmetic legality and one ordinary marked initialization remain after symbolic routing |

## PR #16 (`ADEL/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9309` lift-digit bijection | FOLKLORE / STANDARD MODULAR LIFTING | complete residue systems; `81`-adic digit coordinates | Check terminal inversion and digit order |
| `T-9307` low-energy prefix entropy | NATIVE ERDŐS--KAHANE ANALOGUE | Mosquera--Shmerkin sparse-exception methodology | Conditional-expectation and arbitrary-interval audit |
| `L-9310` completion-height carries | POSSIBLY NOVEL FORMULATION | product formula, rational approximation, linear forms in logarithms | Reconstruct zero-run modulus, nonzero numerator, terminal chaining |
| `T-9311` subexponential cusp decay | NATIVE COROLLARY | deterministic carry form of Erdős--Kahane | Check mirror transfer and powers-of-`64` reduction |
| `T-9308` harmonic tail | NATIVE COROLLARY | dyadic shell summation from sparse exceptions | Check uniform prefix-length range on final shell |
| `T-9312` all-depth weighted EQ | NATIVE COROLLARY | low/high cutoff assembly | Independent full-chain review; downstream issue-#4 translation |
| ordinary integer section | OPEN NATIVE FRONTIER | no measure/Fourier theorem excludes one exceptional point | Combine completion height with code complexity/congruences |

## PR #19 (`H/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9502` exact finite cylinders | NATIVE EXACT / `p`-ADIC IFS COORDINATES | Abram--Lagarias path sets; `LIT-KTHM-0031` | Independent check of direct/recursive orientation |
| `L-9503` ghost stabilization | FOLKLORE / STANDARD COMPLETION CRITERION | nested `2`-adic cylinders | Positivity and actual H legality already retained explicitly |
| `T-9501` survivor count | SUPERSEDED IF `LIT-KTHM-0031` CHECKS | countable separated IFS pressure | Replace `X exp(-c sqrt(log X))` by `O(X^(log_2 rho))` |
| `T-9502` nonperiodic real escape | NATIVE PROPOSED | renewal/toll products | Independent uniformity and sign audit |
| bounded representative tree | NATIVE FINITE REFORMULATION | König-type compactness with explicit height bounds | Exclude all positive-reward infinite rays |

## PR #20 (`PADIC/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `T-9401` repetition rigidity | NATIVE SPECIALIZED PRODUCT-FORMULA ARGUMENT | Ridout; Adamczewski--Bugeaud stammering/symmetric expansions | Independent proof; then derive approximate-pattern versions |
| `T-9402` factor-complexity slope | NATIVE COROLLARY | combinatorics on words and Diophantine complexity | Confirm pigeonhole constants and trivial case |
| `T-9405` chart criticality | POSSIBLY NOVEL GENERAL FORMULATION | rational-base height/approximation | Audit zero numerator and real embedding assumptions |
| `T-9407` stationary ghost stage | NATIVE ISOMETRY + SIGN THEOREM | `p`-adic isometries; product-formula boundary | Independent inverse-context and real-sign reconstruction |
| `T-9408` residue novelty | NATIVE COROLLARY | odometers / isometric demand tree | Distinguish novelty from computational incompressibility |
| `T-9409` finite tower cylinder | FOLKLORE / STANDARD NESTED-CYLINDER THEOREM with native exact modulus | completion in `Z_2` | Prove nonstabilization or construct eventual-zero block digits |

## Cross-program verdict

The common native statement is now:

```text
infinite directive
 -> one exact Z_2 point
 -> ordinary integer iff least representatives / new blocks stabilize.
```

This is not a literature solution; it is the correct completion boundary. The most promising common external toolkit is a product-formula/completion-height theory for adaptive rational approximants, combining:

- `p`-adic linear forms and Subspace Theorem methods;
- combinatorics of stammering words;
- exact carry/height inequalities;
- spine changes of measure;
- `p`-adic automata classification;
- symbolic embedding/zero-error coding after stationary finite-state reduction.

No existing theorem currently verifies the adaptive hypotheses needed for the final ordinary-integer step.