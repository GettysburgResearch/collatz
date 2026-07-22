# Claim map — literature audit wave 4

All references are branch-qualified. Verdicts do not promote native statuses.

## PR #20 (`PADIC/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9408` S-adic transfer | NATIVE EXACT | finite q-functional transfer | independent algebra/index audit |
| `L-9410` block Gaussian Padé | NATIVE PADÉ CONSTRUCTION | Tschakaloff/q-functional determinant theory | reduced-height and nonvanishing audit |
| `T-9412` constant irrationality | NATIVE COROLLARY | `LIT-KTHM-0035` rational-target threshold | independent reconstruction |
| `T-9414` periods `r<=3` | NATIVE COROLLARY | finite Tschakaloff vector, `LIT-KTHM-0034` | audit simultaneous denominator/height estimates |
| `T-9415` finite prefix + short period | NATIVE TRANSFER COROLLARY | rational affine transfer | none beyond dependencies |
| fixed arbitrary period | POSSIBLY KNOWN — HYPOTHESES UNVERIFIED | Väänänen--Wallisser 1991 p-adic Tschakaloff values | obtain full theorem and normalize phase points |
| period four | OPEN NATIVE FRONTIER | Matala-aho determinant; cyclotomic/minor gcd methods | save more than the exact exponent deficit |
| balanced `17/18` directive | OPEN NATIVE FRONTIER | uniform periodic linear-independence measure + S-adic transfer | control constants as standard-word length grows |

## PR #16 (`ADEL/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `T-9312` all-depth weighted EQ | INDEPENDENTLY RECONSTRUCTED / INTEGRATION PENDING | deterministic nonarchimedean Erdős--Kahane | native status update and downstream translation audit |
| `T-9313` fixed-room equivalence | NATIVE EXACT REFORMULATION | completion-height and survivor-order statistics | independent reconstruction |
| `T-9314` depth-46 finite bound | INTERNAL EXACT COMPUTATION | meet-in-the-middle/certificate replay | no asymptotic conclusion |
| `T-9315` centered rational-power equivalence | NATIVE EXACT REFORMULATION | `LIT-KTHM-0041`; FLP and Dubickas | specialize explicit constants to `(81,64)` |
| ordinary section | OPEN NATIVE FRONTIER | nearest-integer/two-interval rational-power theory | prove centered radius `1/81` impossible or construct it |

## PR #3 (`PR3/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `T-0025` finite prefix compiler | NATIVE EXACT ENGINEERING | finite transducers / circuit synthesis | independent replay and complexity audit |
| `T-0026` Montgomery zipper | NATIVE EXACT COORDINATE CHANGE | Montgomery arithmetic | ordinary invariant cylinder |
| `T-0027` stage renormalization | NATIVE NONAUTONOMOUS AFFINE SYSTEM | q/Mahler cocycle methods | exact normalized offset recurrence |
| `T-0028` padding-counter isometry | KNOWN ABSTRACT STRUCTURE + NATIVE MAP | `LIT-KTHM-0038`, Anashin | finite or infinite section verdict for actual map |
| `T-0029` adaptive finite-scale chart | NATIVE FINITE-SCALE CONSTRUCTION | symbolic embeddings only after stationarization | one coherent all-scale finite initialization |
| `T-0030` ordinary quadratic bulk | KNOWN FORMAL-GROUP NORMALIZATION + NATIVE ROLE | `LIT-KTHM-0039` | causal precision growth and stage integration |
| final router | OPEN NATIVE FRONTIER | Krieger/MacDonald after SFT normalization | stationarity, mixing, periodic points, arithmetic initialization |

## Foundry (`FOUNDRY/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| finite-state zero-tail collapse | NATIVE COROLLARY / STANDARD | automatic eventual periodicity | exact model statement |
| standard deterministic one-counter class | KNOWN BY SHORT ARGUMENT | `LIT-KTHM-0036` | incorporate model and scope boundaries |
| counter with digit/residue access | OPEN NATIVE FRONTIER | p-adic automata / finite sections | exact operator taxonomy and integrality theorem |

## PR #33 (`CYL/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `T-9701` finite trap | NATIVE AFFINE LYAPUNOV THEOREM | `LIT-KTHM-0040` generalization | independent audit |
| `T-9702` frozen direct class | NATIVE MODEL-FAMILY CLOSURE | completion-height + finite trap | preserve exact class boundary |
| expansion-positive finite control | OPEN NATIVE FRONTIER | path-complete Lyapunov and occupation-measure duals | normalized graph and proof-producing certificates |

## PR #34 (`SYN/...`)

| Native claim | Verdict | Literature / suite connection | Required native remainder |
|---|---|---|---|
| `L-9862/L-9864` dyadic q-Padé states | NATIVE EXACT BOOLEAN q-ALGEBRA | q-Lucas/Frobenius/Cartier methods | all-`2^a` endpoint invariant |
| `L-9863/L-9867` isometry sections | KNOWN ABSTRACT THEOREM + NATIVE NORMALIZATION | `LIT-KTHM-0038`, Anashin | actual section-orbit computation |
| `L-9865` bucket minima | NATIVE ORDER-STATISTIC RECURRENCE | min-plus weighted automata | closed finite section state or obstruction |
| `L-9866` fractional Hall | KNOWN FINITE FLOW THEOREM + NATIVE DATA | `LIT-KTHM-0037` purification | prove atomlessness; dynamic coherence remains |

## Cross-program verdict

The most valuable external shortcuts are now sharply testable:

```text
Väänänen--Wallisser full hypotheses
Dubickas (81,64) constant
symbolic maximal-minor factors
actual rooted-tree section finiteness
DWW atomlessness
q-Lucas endpoint invariant.
```

Each can either close a large native class or return an exact hypothesis failure. No literature theorem presently supplies one positive ordinary counterexample.