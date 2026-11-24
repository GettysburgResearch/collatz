# Execution record for the closing-target attack

The mathematical packet is [here](../../research/astra-closure-attack-20261124/README.md). Collatz remains open. Source-qualified written arguments, finite exact controls, Lean kernel acceptance, and repository integrity are distinct evidence levels.

## Successful integrating replay

**PASS.** The integrating agent fetched published source commit `4bec21d9257348588710a3c635af14f4486e72e8`, tree `8c4901528c023fe57ab34fe6768be87e26d0d6ad`, into a clean complete checkout with 407 tracked files. The head, source bytes, and clean status remained unchanged through completion. The replay ran from `2026-11-24T05:15:21.406621+00:00` to `2026-11-24T05:15:49.652202+00:00`.

All six new modules were compiled sequentially from their exact published source bytes, each to a fresh object. They import only `Std`. The environment was Lean 4.34.1, release commit `5045d0056413266e57c625dcd7c365b10e377c52`, with `-j1 -DwarningAsError=true`. No source port, cached project object, or Mathlib module was used.

[The complete receipt](fresh_replay/receipt.json) records the commands, source and fresh-object hashes, exit codes, durations, output hashes, and thirteen transitive axiom inventories. Every inventory is a subset of `propext`, `Classical.choice`, and `Quot.sound`; none contains `sorryAx` or a custom mathematical axiom. Fresh compiled objects were retained locally, while their identities and all stdout/stderr logs are recorded here.

## Formal scope

| Module | Public declarations audited | Scope |
|---|---|---|
| descent_Separated.lean | integral, shadow_edge, smaller_boundary, descent_all_phases, separated_descent | Complete smaller ordinary nonconvergent shadow, including both odd phases and raw Boolean input |
| descent_Triple.lean | triple_paid_merger | Complete finite half-partner merger through an arbitrary L prefix and PPP |
| descent_Extension.lean | paid_three_light_core, ramp_merger, light_paid_merger | Complete smaller odd ramp target and literal endpoint through an arbitrary long L prefix and PLLL |
| source_VirtualWindow.lean | virtual_window | Full finite translated-window defect telescope |
| cycle_two_centers.lean | displacement, bezout_payment | Integer centered displacement and complete-modulus Bezout cancellation |
| cycle_extension.lean | centered_telescope | Centered telescope for an arbitrary number of windows |

The Diophantine estimates and the stationary-limit theorem are written results, not Lean-checked consequences of these finite identities. Only the identified merger cases are formally covered; the remaining finite code and language consequences are written whole-cylinder proofs with exact controls.

## Exact controls executed

All five scripts passed in normal Python and with `-O`, with byte-identical paired output. Their guards use explicit exceptions.

| Script | Actual bounded coverage |
|---|---|
| descent_controls.py | 86 ordinary finite paths; 1,204 boundary comparisons; 83 sources outside the old guard; 52 rejected rational-slope candidates; 130 triple-paid mergers |
| descent_Extension.py | Six exact accepting prefix certificates; exactly three unresolved length-five words; 66 signed-cycle base cases; 396 ordinary endpoint comparisons |
| source_controls.py | 13,125 virtual windows; 3,050 matched edges; 4,500 primitive tuples; 13,500 outside-product identities; positive and signed carry controls |
| cycle_closure_controls.py | 6,315 primitive positive words; 63,382 cuts, of which 4,046 have dependent clocks; 57,920 exact complete-denominator certificates; 32 sharp-family cases |
| cycle_extension.py | Two centered segments, including a low terminal boundary; 256 primitive period-65 positive rational itineraries, all nonintegral |

The full counts appear in the individual logs and receipt. They do not establish an unbounded mathematical claim.

## Complete-checkout repository validation

At the same clean published source commit, `python -X utf8 -B tools/validate.py` exited zero. All five default commands passed. [The validator log](fresh_replay/repository-validation.stdout.log) records the exact checkout identity and each component result. No optional legacy regression bundle was run. Repository integrity is not mathematical verification.

The successor report commit adds these receipts and the separately pinned late-source comparison. It does not change any of the six Lean modules or five tested scripts. The PR description records the final published-head validation, avoiding a self-referential receipt commit.

## Reproduction

Compile each file directly with Lean 4.34.1 using `-j1 -DwarningAsError=true`. No additional project module, Mathlib checkout, source transformation, or visibility patch is required for these six files. A fresh direct compilation reads each proof body from the recorded source.

Run the five exact control scripts in ordinary and optimized Python:

* `descent_controls.py`
* `descent_Extension.py`
* `source_controls.py`
* `cycle_closure_controls.py`
* `cycle_extension.py`

Their guards use explicit exceptions and remain active under `-O`; normal and optimized outputs must agree byte for byte. The finite counts are not proof of the external Diophantine theorems or the unbounded assertions.

Finally run `python -X utf8 -B tools/validate.py` in a clean complete checkout. Its integrity result is not mathematical verification. Exact head, commands, logs, exit status, and source hashes belong in the completed replay receipt.
