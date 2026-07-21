# Claim-by-claim review matrix — ADEL 9309–9312

**Reviewer:** `gpt56-review-9309-01` (`GPT-5.6 Pro`)  
**Target:** `e5383d44cfa9fb75f7e92ff0bf031a2a6ca529a6`  
**Method:** independent reconstruction before submitted-proof comparison; exact checker imports no author code.

| Claim | All hypotheses/quantifiers restated | Independent derivation | Endpoint/sign/valuation/digit/modulus/index audit | Independent checker / counterexample search | Submitted proof comparison | Verdict | Status proposal | Downstream action |
|---|---|---|---|---|---|---|---|---|
| `L-9309` | yes: all `K>=1`, integers `h`, `0<=ell<K`, and all `1<=L<=K` | exact lift recurrence, normalized recurrence, terminal inversion, prefix inversion, perturbation | `K=1`, `L=1`, `L=K`; most-significant lift digit; least residue; exponent `K-L+1` | exhaustive `K<=3`, 538,083 tuples; 3,000 100-digit signed checks | all inferences match; backward tuple recovery is implicit but valid | **PASSED** | `INDEPENDENTLY_VERIFIED` | no invalidation; `R-9301` may use it |
| `T-9307` | yes: all `K>=L>=1`; every complete translated block; every interval `H>=81` with `floor(log_81 H)<=K` | shifted-grid moment, exact conditional uniformity, lower-tail bound, 81-block interval cover, cosine product | arc endpoints; conditional digit order; translated/incomplete intervals; strict complement threshold; character sign | complete blocks through `81^3`; intervals through 600,000; 491 Fourier checks | all mathematical steps match | **PASSED** | `INDEPENDENTLY_VERIFIED` | add `L-9305`, `T-9305`, `T-9306` to dependency metadata |
| `T-9308` | yes: every `K>=1`, `81<=M<=2^K`, and every admissible cutoff sequence | exceptional/nonexceptional shell split, geometric sum, survivor transfer, low/high reduction | final shell; `L<K`; `M=81`; `M=2^K`; no cutoff gap/overlap | all frequencies through `2^18`; 44 tail checks with explicit `C_tail` | all inferences match | **PASSED** | `INDEPENDENTLY_VERIFIED` | no invalidation; other depth-statistical claims not reviewed |
| `L-9310` | yes: every coprime `2<=M<N`, every `M`-unit `c!=0`, every `K>=1`, every primitive nonzero `h` | integral carries, energy inequality, exact zero-run equality, nonzero completion numerator, height squeeze, affine terminal chaining | exact modulus `N^(ell+r+1)`; `t_W=1`; signed half-open interval; negative `c,h`; `M∤h` is sufficient | 35,766 chains; general signed charts; depth 512; 70-digit numerators | all inferences and constants match | **PASSED** | `INDEPENDENTLY_VERIFIED` | no invalidation; do not infer ordinary-integer consequences |
| `T-9311` | yes: primitive and arbitrary nonzero frequencies; all subexponential windows | signed distance equals phase distance, cosine energy, comparison, exact `v_64` reduction, uniform asymptotics | negative frequencies; `v_64` not `v_2`; `v<K`; phase sign/order; uniformity in `H_K` | 690 primitive + 698 power-64 checks; depth 320; exhaustive windows `K=96,112` | all inferences and `b_*` match | **PASSED** | `INDEPENDENTLY_VERIFIED` | no invalidation; downstream ordinary-section claims remain separate |
| `T-9312` | yes: every depth, asymptotic statement for sufficiently large `K` | split at `M_K=K`, low harmonic maximum, high tail, limit | no `h=0`; no gap/overlap; eventually `81<=K<=2^K` | exact partitions and all coefficients through `2^18` | all inferences match | **PASSED** | `INDEPENDENTLY_VERIFIED` | issue-#4 consequences remain unverified pending translation audit |

## Corrections that do not change a claim statement

1. The dependency graph must not contain `L-9309 -> L-9310`; those are parallel starts.
2. `T-9307` should distinguish count-theorem dependencies from Fourier/transfer-corollary dependencies.
3. Proof bodies should remain unchanged; this review adds status/reviewer evidence rather than replacing author history.
