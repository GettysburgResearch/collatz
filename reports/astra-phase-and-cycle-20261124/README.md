# Execution and review record

**Collatz remains open.** This report distinguishes executed arithmetic controls, written mathematical review and actual Lean compilation.

## Written work and independent review

The phase and cycle arguments were developed by separate GPT-6.2 Astra workers. The cycle worker independently reconstructed PS1–PS6, including the actual scalar identities, dyadic and ternary endpoint estimates, two-step terminal permutation, convergence witness and exact fiber classification. The phase worker independently reconstructed the new cyclotomic degree count and exceptional component splitting. The integrating reviewer checked those mathematical interfaces and their inherited assumptions. The exact review boundary appears in the packet's review files.

The complete cycle-size corollary retains the specific PR185 linear-forms/certificate input. The full analytic proof of that input was not rebuilt or newly formalized. No whole-project theorem acceptance is claimed.

## Exact arithmetic controls executed by the integrating agent

[EXACT_CONTROLS.json](EXACT_CONTROLS.json) pins the tested scripts and their output hashes. Normal and optimized Python returned identical output in each case.

- [Phase controls](phase_controls.json): 2,385 distinct literal ordinary states, 209 positive-carry lowest-digit transitions including 143 resets, 23,850 shifted-grid checks, all 3,279 canonical words through length seven with both kinds of witnesses, 29,523 terminal permutation cases through level nine, and 654 complete scalar-fiber/modulus comparisons. The largest certified convergent witness has 39,362 binary digits.
- [Cycle controls](cycle_controls.txt): 8,031 primitive words, 14,317 homogeneous components, 1,649 positive prime-power instances, four literal rational cycles and six simultaneously saturated nonzero component norms.
- Independent phase review: a separately derived terminal-congruence formula verified all 1,092 words through length six. The separate fiber review grouped 16,290 legal two-step gap pairs and checked six ternary precisions. These are review checks, not counted as additional author controls.

Finite controls do not establish the unbounded mathematical assertions.

## Completed fresh-source Lean replay

**PASS.** The integrating agent executed the entire seven-module replay at published source commit `e3c33885e5d1530c4ad4595e324f9dbeb2761482`, tree `06fba51f3518271d8c31fffd96a2e19b1ad48ca7`. The source checkout was clean. Every source matched that Git head, and the source bytes and head remained unchanged through completion.

- [Complete machine-readable receipt](fresh_replay/receipt.json): actual commands, exit codes, timestamps, source hashes, generated-source hashes, fresh object hashes and all axiom inventories.
- [Combined axiom output](fresh_replay/12-AllAxioms.stdout.log): ten new public theorem declarations, including intermediate bridge lemmas, and five selected upstream theorem declarations.
- [Exact visibility patch](fresh_replay/visibility-port.patch), [original sources](fresh_replay/src-original) and [generated sources](fresh_replay/src): the complete source transformation used in the successful build.

The environment was Lean 4.34.1, release commit `5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`. The seven modules were compiled sequentially with `-j1 -DwarningAsError=true`. No pre-existing object for any of these seven modules was reused.

The successful replay used the documented module/visibility port. It changes initial import and visibility declarations, preserving every theorem statement and proof body. The generated bridges use `import all ActualScalar` to expose definitions from the unchanged upstream source locally. This receipt certifies those exact generated sources; it is not presented as a complete byte-exact unported replay.

All fifteen transitive axiom reports contained only members of `propext`, `Classical.choice`, and `Quot.sound`. The lower finite kernel used only `propext` and `Quot.sound`. No `sorryAx`, custom axiom, or assumed Collatz convergence appeared in any audited dependency closure.

The actual-scalar floor and clock are derived from the actual convergent series. The upper and lower run theorems consequently apply to literal ordinary odd orbits, rather than requiring a hypothetical scalar recurrence. The ordinary-shadow theorem separately proves an infinite smaller nonconvergent ordinary trajectory under its explicit residue/language assumptions. Those assumptions are not proved universal.

## Separate upstream and worker checks

[Worker execution records](worker_checks/worker_executions.json) preserve successful byte-exact original compilations of PR182's actual-scalar source, the new `Std` ordinary-shadow theorem, and PR191's `TwoSidedPacking.lean`. The latter printed 13 axiom reports containing only standard Lean axioms. These checks are distinct from the integrating agent's complete fresh-source replay above.

An earlier attempt to compile other upstream candidates was interrupted during its first file under shared storage pressure. No file completed in that attempt, and it supplies no kernel evidence for those candidates. PS2–PS6's real approximation and unbounded realization arguments, and the cycle/Galois deductions, remain independently reviewed written mathematics with exact finite controls. The PR185 analytic input retains its source-qualified status.

## Source refresh and publication

[LIVE_SOURCE_DELTA.json](LIVE_SOURCE_DELTA.json) records the final review of PR189's concurrent head `a390a1a4c75ee95db98b4b683d17c503f4e4a118`. Its eleven-line attribution correction credits PR180 for the stationary collision gap and changes no theorem, proof or code. It requires no mathematical change to this packet. The initial PR146–191 inventory remains frozen at its recorded heads.

The contribution is published in [draft PR192](https://github.com/GettysburgResearch/collatz/pull/192). Its description records the final observed published head and complete-checkout repository validation separately from the Lean receipt. The required repository command is `python -X utf8 -B tools/validate.py`; repository integrity is not mathematical verification. The published Lean sources are authenticated individually by the replay receipt even when a later commit adds only reports and documentation.
