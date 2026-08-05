# PR #51 claim review matrix

**Reviewer:** `gpt56-refund-01` (`GPT-5.6 Pro`)  
**Core-review source:** `9c0753db8543a99247ed55beefbce75ca8f2b507`  
**Second-pass source:** `c7f1c75d0a71a63b32ef3e23306c23f1d0a60bfa`

| Claim/artifact | Verdict | Finding |
|---|---|---|
| `O-8001` negative-three-cycle physical chart | **PASSED** | Both integer branches and their three-/four-step shortcut-Collatz conjugacies reconstruct directly. |
| `L-8002` maximal-run and quotient-refund normal form | **PASSED** | The maximal run, exact core equation, full modulus `2^(8+3s)`, three-run residue, and deterministic changing-modulus quotient law reconstruct. |
| `L-8004` divisible-seven `+1` normalization | **PASSED** | `7|z` is invariant; division changes the core toll from `+7` to `+1`; the CRT residue classes reconstruct. |
| `T-8002` run-five counterexample implication | **PASSED** | The exact macro difference changes sign at run length five; a forever-defined all-high-run ordinary path is positive and unbounded. |
| `L-8003` reset highways | **PASSED** | The closed reset seed, exact `B A^(m/3)` prefix, LTE tail length, and re-entry condition reconstruct. |
| `T-8003` block-average highway | **PASSED / ELEMENTARY PROOF READ** | Multiplying the exact macro lower bounds gives `z_N>z_0 2^((9S_N-44N)/53)`; `9^53>2^168` proves the nine-run total-44 criterion. |
| `L-8005` base-nine logarithmic renormalization | **PASSED / ELEMENTARY PROOF READ** | `9^alpha` is an isomorphism `Z_2 -> 1+8Z_2`; LTE gives `v2(alpha+r+1)=1+3s`; the normalized-unit update reconstructs. |
| Explicit affine schedule `r_n=64+n` | **CLOSED NEGATIVELY** | `R-8202` expresses its selected core as one scalar Tschakaloff value and applies Amou--Matala-aho--Väänänen Theorem 5.1 to prove irrationality. |
| Every eventually affine positive-slope schedule | **PROPOSED SOURCE-QUALIFIED EXCLUSION** | The source parameter is `lambda=-(2/3)log_2(3)`, independent of slope; exact source-window inequalities hold. See `R-8202/X-8203`. |
| `Q-8203` nonlinear block-average highway | **PRIMARY POSITIVE TARGET** | A viable schedule must be genuinely nonlinear/adaptive, meet the nine-run resource total `44`, and prove ordinary transported-cylinder closure. |
| `X-8005` named formulas and interfaces | **INDEPENDENTLY CORROBORATED** | `X-8202` checks 10,001 physical edges, 208 maximal macros, 13,056 quotient identities, 256 divisible-seven cases, and 200 reset seeds. |
| Full canonical `X-8005` payload | **PENDING INDEPENDENT FULL-ARTIFACT REPLAY** | The complete byte-for-byte source payload is a separate neutral replay task. |
| Earlier `L-8001/T-8001/X-8001...X-8004` finite-cycle packet | **PENDING SEPARATE REVIEW** | Outside the critical path selected for this pass. |