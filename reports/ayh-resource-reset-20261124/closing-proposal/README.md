# Closing-proposal execution and review record

This report accompanies the [scientific proposal](../../../research/ayh-resource-reset-20261124/closing-proposal/README.md). The new mathematical result removes the complete two-odd upper-certificate layer of a least reverse defect and proves further ordinary identities in selected three-odd families. **The unrestricted higher-rank step remains open.** The final assembly exposes only that step as an argument; the numerical quantitative return is now an unconditional kernel theorem.

## Fresh kernel execution

The publishing agent ran [the build script](../../../research/ayh-resource-reset-20261124/closing-proposal/check_lean.sh) in the complete source checkout. It rebuilt **all 17 mathematical modules**, including the six earlier local dependencies, into a new temporary object directory, then compiled the separate `PublicAudit` module. This execution used Lean **4.34.1**, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`, and Mathlib **`d13f23b723b8a846827a245b89c10fc7d3f11612`**. Every invocation used one worker, disabled automatic implicit binders, and treated warnings as errors.

The final run exited **0 in 512.901 seconds**, as recorded in `lean-execution.json`. The earlier successful 16-module build (157.758 seconds) is preserved in `initial-lean-execution.json` with its original 98-declaration audit; it predates the completed quantitative-return formalization. The audit names **100 public declarations**, including **70 earlier dependency statements and 30 new statements**. All printed axioms are subsets of `propext`, `Classical.choice` and `Quot.sound`; several statements use no axioms. There is no `sorryAx` or project-specific axiom. Explicit theorem arguments such as `HigherRankProgress` remain hypotheses even when the axiom list is standard.

- [Execution receipt with source hashes](lean-execution.json)
- [Complete compiler log](lean-build.log)
- [Parsed 100-declaration audit](axiom-audit.json)

An initial draft build stopped because the restored Mathlib cache lacked `Mathlib.Tactic.Positivity`. The dependency cache was restored, and the reported successful build started again with an empty repository-local object directory. The failed draft is not counted as a successful execution. Earlier agent development logs and temporary stand-ins are likewise not the evidence for the publisher's full run.

## Exact finite executions

[finite-execution.json](finite-execution.json) retains the actual commands, stdout, exit codes, durations and script hashes. Each of five checkers passed both normally and with Python optimization, with identical stdout in each pair. The independent ordinary verifier also passed in the publisher's environment.

| Check | Executed scope |
|---|---|
| Rank-two replay | The exact pinned 26 words; prefix factor \(16384/9\); the composite height below \(2^{40}\); the three small exponents and their lower first-hit times; the large-fiber coefficient inequality. |
| Rank-three restriction | 156 rational parity prefixes of maximum length 343; all 675 admitted positive small-tail sources, maximum first-hit time 5,619. |
| Mersenne returns | Forty complete offsets and 80 forward query positions, with residue, divisibility, positivity, direction, endpoint and parent-height comparisons. Offsets 0 and 2 require the separate ordinary merger theorem; the finite path checker correctly reports them as uncovered by its own bank. |
| Opposite-arm symbolic bank | 214 disjoint progression certificates; exactly 616 power classes and 384 contraction classes modulo 59,049; 58,049 outside this bank. |
| Quantitative table reconstruction | All 75 ternary subbanks, their complete outer tree, and the 26-leaf descent reproduced from the two frozen source banks. Lean validates their semantics and bounds independently of Python. |
| Independent opposite-arm replay | 31,847 physical clocks on all 214 first family members, including an exponent of 9,355,111; pairwise residue-class disjointness; a separate 245-clock replay of the displayed \(j=29419\) example. |

The independent program is [retained here](check_opposite_arm_independent.py). It accepts the bank path as its single argument. The full 214-progression conclusion also needs the symbolic congruence-period and ordinary-height proof; a replay of the first member alone would not establish it.

## Independent reconstruction and source boundaries

Four GPT-6.2 Astra work streams contributed during this pass, with up to three delegates active together. Authors and reviewers had different tasks. These are internal mathematical reviews, not external peer-review acceptance.

- [Rank-two review](RANK_TWO_INDEPENDENT_REVIEW.md) independently reconstructed the 26-leaf directed descent, all marked source bounds, ordered exchanges, small exponent classification and ordinary large-source descent. It also built the exact final source against a fresh full vendored dependency.
- [Local-resampling review](LOCAL_RESAMPLING_REVIEW.md) checks the original-source census, modal predictability, first actual dissent, minority mass, ordinary stride and finite graph quantifiers under the named P, R and M inputs.
- [Opposite-arm review](OPPOSITE_ARM_REVIEW.md) reconstructs congruence lifting, parity preservation, height margins and least-defect logic for all 214 rows. Its manuscript hash precedes the final wording that identifies the completed Lean progression theorem; the certificate bank and checker are unchanged. The publisher checked that limited wording change against the fresh build.
- [Final-proposal review](FINAL_PROPOSAL_REVIEW.md) checks the conditional strong-induction assembly and its open hypothesis boundary at the named source hashes, including the final wrapper that consumes the proved numerical bound.
- [Latest diffusive-row comparison](LATE_DIFFUSIVE_COMPARISON.md) freezes PR207's two manuscripts and compares their exact lower and upper clock ranges. It neither imports their source-qualified analytic inputs nor claims their candidate Lean code was compiled.
- [Publisher reconstruction](ROOT_REVIEW.md) records the final wording, written-versus-kernel boundaries and the retained failure of the full proof attempt.

The [source manifest](source-hashes.json) freezes every new scientific file, report and modified navigation document except itself. The [full open-PR inventory](OPEN_PR_INTAKE.json) is a metadata snapshot of 143 pull requests, with focused mathematical reads separately named in the [source ledger](../../../research/ayh-resource-reset-20261124/closing-proposal/SOURCES.json). Metadata coverage is not proof coverage. The [previous complete PR description](PRIOR_PR_DESCRIPTION.json) preserves earlier execution identities.

## Exact published-head integrity

The repository's required validator must run in a clean complete checkout of the final published head. Its receipt is retained outside the checkout during execution, then included with that exact head and tree in [PR197's description](https://github.com/GettysburgResearch/collatz/pull/197). This avoids changing the commit authenticated by its own receipt. The validator checks structure, frozen review identities and integrity fixtures. It is separate from the Lean and finite arithmetic executions above, and is not a proof of Collatz.
