# Claim-by-claim review matrix — centered recurrence chain

**Reviewer:** `gpt56-review-9315-01` (`GPT-5.6 Pro`)  
**Frozen target:** PR #16, commit `900ba417c968d8a41bc56a30d3ccc941284d8ce2`  
**Date:** 2026-07-22

| Claim | Exact scope reviewed | Verdict | Repository action | First invalid inference / counterexample |
|---|---|---|---|---|
| `L-9311` | ordinary `64 -> 81` tail recurrence, difference chain, repeated-factor height bound | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `T-9315` | all coprime `2 <= M < N`; both directions; zero and endpoint exclusions; `64 -> 81` crosswalk | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `L-9313` | unique bounded error path, nested cylinders, completion series, stabilization criterion | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `L-9314` | exact appended base-`M` block, terminal update, zero-block and uniqueness criteria | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `T-9316` | global recurrence cone; Thue--Morse shifts/complements; appended-block consequence | **PASSED** | promote; complete dependencies with `D-9302` and `L-9314` | none |
| `L-9315` | non-erasing morphic transfer and distortion threshold | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `L-9316` | deterministic non-erasing sequential-transducer transfer and `Q <= 8` corollary | **PASSED** | promote to `INDEPENDENTLY_VERIFIED` | none |
| `T-9317` | conditional implication only; no Dubickas source instantiation | **PASSED** | promote implication to `INDEPENDENTLY_VERIFIED`; keep source hypotheses uninstantiated | none |
| `T-9318` | finite factor-complexity lower bound plus universal nonstabilization corollary | **REFUTED** | preserve statement/proof; mark `REFUTED`; add `R-9304` and corrected `T-9319` | `0^infinity` and `1^infinity` have `p(n)=1`, slope `0`, and `q_K=0` for every `K` |
| `R-9304` | exact constant-word counterexamples to `T-9318` Section 3 | **PASSED** | add as `PROVED` refutation | exact counterexamples above |
| `T-9319` | repaired theorem with the necessary `nonconstant` hypothesis | **PASSED** | add as new `PROVED` claim | none |

## Downstream audit

No passed dependency is invalidated. Any document using `T-9318` merely for the lower bound on an already nontrivial ordinary itinerary remains mathematically sound, but references to its presentation-free nonstabilization screen must be redirected to `T-9319`. `T-9317` remains conditional on an independently sourced lower-bound/equality-language theorem. No issue-#4 chart-to-Collatz translation is promoted by this review.
