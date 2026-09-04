# Sources, frozen state, and claim boundaries

**All new theorem-level claims are PROPOSED pending independent review.** The local packet is a research contribution, not a canonical integration or an external-priority claim.

## Frozen repository state

Repository: `GettysburgResearch/collatz`.

```text
main  9704bcf1ff33cc9e2b729e0c40137a1e55b95397
PR87  e9adc409031a61f3801c4ee1e1e6deeb34188eb7
PR88  c28922fb6d1c070bf86a76192f40bc9ea3edd67c
PR90  aeb69ce631370be36fd1f80b472ab448e7df2a73
```

The branch starts directly from the recorded `main`. It does not import, merge, or change those PRs. It adds only its own research, experiment, and report files; no canonical result or status is promoted.

## Repository antecedents and exact distinction

**Resident extraction and coefficient stopping.** The [research map](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/docs/RESEARCH_MAP.md), [coefficient packet](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/research/integrated/coefficient-stopping/README.md), and [agent entrypoint](https://github.com/GettysburgResearch/collatz/blob/9704bcf1ff33cc9e2b729e0c40137a1e55b95397/AGENTS.md) fix the ordinary/2-adic, finite/global, and source/end boundaries. The new source bound is conditional on a stated charge budget and does not promote SC*.

**PR #87: exponent race.** See [the endpoint-one attack](https://github.com/GettysburgResearch/collatz/blob/e9adc409031a61f3801c4ee1e1e6deeb34188eb7/research/external/mazur-2026/fixed-height-power-saving-attack.md) and [synthesis](https://github.com/GettysburgResearch/collatz/blob/e9adc409031a61f3801c4ee1e1e6deeb34188eb7/research/external/mazur-2026/synthesis-and-roadmap.md). An exceptional count `o(X^0.901)` is enough when combined with the imported predecessor lower bound. This pass supplies neither that count nor a new inverse exponent.

**PR #88: fixed-height obstruction.** The inspected [committed note](https://github.com/GettysburgResearch/collatz/blob/c28922fb6d1c070bf86a76192f40bc9ea3edd67c/research/external/mazur-2026/fixed-height-forward-power-saving.md) proves a one-horizon entropy barrier, refutes uniform all-subset fiber gains by mass conservation, and gives a conditional killed-transfer bootstrap. The PR description names an older file organization; this packet follows the actual committed note. Our contraction kills on resonance as well as 1, so it is not an instance of that note's fixed-floor hypothesis.

**PR #90: critical mass and failed global weights.** See [PROOF.md](https://github.com/GettysburgResearch/collatz/blob/aeb69ce631370be36fd1f80b472ab448e7df2a73/research/astra-critical-mass/PROOF.md). That packet already gives the summable inverse-supersolution criterion, critical little-o and weighted-mass bridges, the `3^v3(n+1)/(n+1)^2` trial weight, and obstructions to its even-ray repair. Those results are credited as antecedents, not renamed here. The new arithmetic object is the exact section `n==1 mod 3`, its complete fan, the form `2n+1`, the charge `Q`, and an error-controlled resonance-return elimination. The proofs of this packet's inequalities are local and do not depend on accepting every PR #90 claim.

**PR #81: source/remainder envelope.** See [T-6812](https://github.com/GettysburgResearch/collatz/blob/09d6f9086d4ead63a5102f05458441939c29f4f5/research/positive-coefficient-entropy/claims/T-6812-support-corrected-cofinal-envelope.md). Its cofinal source-height comparison is a conditional endpoint; it is not established by the qualitative SC* equivalence. The new charge-controlled `O(log^2 n)` estimate is a separate subclass theorem, with a precisely retained universal-budget gap.

**PR #6: termination frontier.** See [the pinned packet](https://github.com/GettysburgResearch/collatz/blob/4810a0771da61a1cb609ef8707dfcf7f0f6e666f/research/termination-frontier/README.md). Its standard match-height obstruction and its distinction between admitted proofs and unadmitted legacy leads are respected. Our certificate language concerns an explicit arithmetic block strategy, not termination of every mixed-radix rewrite strategy.

## Primary external context

- Emre Yolcu, Scott Aaronson, Marijn J. H. Heule, *An Automated Approach to the Collatz Conjecture*, [arXiv:2105.14697](https://arxiv.org/abs/2105.14697). The mixed-radix termination equivalence motivates Route 3; it is not used as a black box in the local proofs, which work directly with ordinary shortcut orbits.
- Lech Mazur, *Certified x^0.90 Lower Bounds for Collatz Predecessor Sets*, July 2026, [source page](https://www.proofatlas.ai/sources/collatz-predecessor-090/) and [certificate boundary](https://www.proofatlas.ai/proofs/artifact.collatz.predecessor-lower-bound-090.real.v001.html). The target-dependent lower bound has exponent 0.901. This is source-qualified context only: the external proof build and large certificate payload were not replayed in this pass, and none of the new local inequalities uses that theorem.

No PDF was redistributed. No exhaustive external novelty comparison was performed. In particular, the elementary induction principle, parity-cylinder bijection, CRT, positive-mass contradiction, geometric resolvent series, and general idea of grouping odd/even runs are not claimed as new.

## Claim map

| Claim | Exact content | Scope / dependency |
|---|---|---|
| `T-ATR-101` | Explicit first-return map and complete finite inverse fan | Every ordinary source/endpoint in the specified section; elementary |
| `T-ATR-102` | Summable `V` and `KV <= QV/2` | All section endpoints, with explicit endpoint charge |
| `T-ATR-103` | Quantitative entry into resonance or 1, all-source weighted safe survival, exact resonance density | Not entry into 1 alone |
| `T-ATR-104` | Resonance-return Schur formula and geometric truncation error | Trial function envelope `0<=f<=CV`; no global supersolution supplied |
| `T-ATR-201` | Necessary no-descent charge pressure and quantitative source-height bound | The duration bound requires every completed prefix to satisfy the stated budget |
| `L-ATR-202` | Finite-word endpoint carry jets | Only under both strict valuation tests; boundary cases remain unfrozen |
| `R-ATR-203` | Exact counterexamples to two simple charge budgets | Refutes the particular exponents/rate tested, not every budget |
| `T-ATR-301` | Rank-drop lift to infinite upward arithmetic progressions | Fixed word, exact valuations, positive affine correction |
| `T-ATR-302` | Unbounded spike repayment for the one- and two-parameter word families | Every stated height/run pair and every legal ordinary source of the exact height |
| `T-ATR-303` | Common-rank block coverage implies Collatz | Complete coverage is explicitly open |

## Review points that could change the assessment

Check the complete inverse fan, including the terminal class-0 branch; the last two source weights and their common ternary core; the direction of the charged rank inequality; the all-source/absorption-set distinction; operator row/column conventions and truncation indexing; the prefixwise budget needed for the last unfinished block; exact source/end coefficients; the nonzero positive affine correction in the tile-lift theorem; and the all-height repayment estimate.

The small `13 -> 10` counterexample, both charge-budget failures, and the missing coverage statement must remain visible after any extraction. A proposed repair must not retroactively turn those false strengthenings into verified claims.
