# Central-step research receipts

23 November 2026. New packet over base
`e6ed7f1429ced4b58b85ca9006edd9a3a12ca193`.

Read the [research index](../../research/central-step-20261123/README.md)
for the results and their open construction obligations. The complete
finite rational certificate, equivalent-flow theorem, and cycle capacity
theorem have written proof scope. Twelve finite numerical/arithmetic
lemmas are Lean checked. These are separate verification levels.

## Independent work and review

| Packet | Author | Independent reviewer | Review |
| --- | --- | --- | --- |
| Finite rational certificate | `/root` | `triadic_selector` | [rational-review.md](rational-review.md) |
| Fast equivalent flow | `stationary_rigidity` | `/root` | [stationary-review.md](stationary-review.md) |
| Complementary denominator capacity | `cycle_symmetry` | `stationary_rigidity` | [stationary-review-cycles.md](stationary-review-cycles.md) |
| Complete triadic selector and height | `triadic_selector` | `cycle_symmetry` | [cycles-review-triadic.md](cycles-review-triadic.md) |

Each written review identifies the exact source bytes it covers. No
review upgrades a universal candidate or collision assertion to a theorem.

## Lean evidence

The runtime is Lean 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

| Scope | Author receipt | Independent receipt |
| --- | --- | --- |
| Seven rational-excursion lemmas and their audit | [rational-lean-receipt.json](rational-lean-receipt.json) | [rational-review-receipt.json](rational-review-receipt.json) |
| Five weighted-selector lemmas and their audit | [triadic-lean-receipt.json](triadic-lean-receipt.json) | [cycles-selector-lean-receipt.json](cycles-selector-lean-receipt.json) |

All commands use `-DautoImplicit=false` and `-DwarningAsError=true`.
Author and reviewer builds use distinct external output directories;
mathlib dependency objects are reused. The receipts bind source bytes
and raw output logs. Every authored theorem, including the selector's
positivity helper, appears in the corresponding axiom audit.
Only `propext`, `Classical.choice`, and `Quot.sound` occur; several
theorems use proper subsets of these. The earlier Lean corpus was not
rebuilt for this packet.

## Sources and archived PR state

- [source-snapshot.json](source-snapshot.json) records the initial
  latest-30-PR refresh, PR178, and main.
- [rational-sources.json](rational-sources.json),
  [stationary-sources.json](stationary-sources.json),
  [cycles-sources.json](cycles-sources.json), and
  [triadic-sources.json](triadic-sources.json) distinguish direct
  dependencies, comparisons, and inspected attempts.
- [PR178-before.json](PR178-before.json) preserves the exact previous
  fetched PR body. [PR178-before.md](PR178-before.md) is its readable
  copy with trailing whitespace normalized.

## Integrity and publication gate

[manifest.json](manifest.json) records byte counts, SHA-256 digests,
and Git blob identities for every new research and report file other
than itself. The manifest is checked against the exact publication
tree, along with the frozen review hashes and compiled-source hashes.
It attests bytes and coverage, not mathematical truth.

Before moving the owned remote branch, the default repository command
`python -X utf8 -B tools/validate.py --receipt <external-path>` is run
in a clean, complete checkout of the newly created commit. Its receipt
stays outside the checkout to avoid a self-referential publication
claim. The exact commit, gate outcome, and receipt digest are reported
in PR178 after the gate succeeds. The remote branch move is guarded
against an unexpected head change and does not force-rewrite history.
