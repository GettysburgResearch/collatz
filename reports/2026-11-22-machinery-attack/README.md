# Checkpoint 12: focused machinery replay and review

## Executed proof check

The [fresh Lean receipt](lean-fresh-replay.json) records a successful
execution of the checkpoint's
[replay driver](../../research/lean-global-resolvent-20261121/overview/machinery/check_machinery.py).
It compiled thirteen project modules into an initially empty output
directory: nine exact legacy imports, two new proof modules and two new
audit modules. The legacy project objects were rebuilt from the pinned
sources; they were not taken from an earlier checkpoint's object cache.
The pinned Mathlib and Lean runtime objects were reused.

All thirteen commands exited zero with `-DwarningAsError=true`. The two
audits checked seven certificate-language statements and one finite
division-clock statement. The only reported axioms were `propext`,
`Classical.choice` and `Quot.sound`. All project source hashes remained
unchanged during execution. The driver also verified the direct Mathlib
source hashes, its toolchain and lake manifest, and the four reviewed
note hashes before compilation.

Exact runtime pins:

- Lean: `5045d0056413266e57c625dcd7c365b10e377c52` (4.34.1).
- Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The full command arguments and outputs are in the JSON receipt. These
are evidence for the finite Lean statements and their stated hypotheses,
not for an unproved global closing estimate.

After the replay, one redundant final blank line was removed from the
certificate-language written note. Its receipt hash is
`c33cc4288876cd02db54249495086b3223e11d6254541aa23b40e6eb0bff5ceb`; its published hash appears below. No Lean source or mathematical text changed.
The replay was not repeated for this formatting-only change.

## Mathematical review

The cross-reviews were source inspections and independent mathematical
reconstructions; they are not represented as separate execution receipts.

| Reviewed item | Frozen SHA-256 | Review result |
| --- | --- | --- |
| Certificate proof module | `96afea745942162df7007f0d03d9d2a60dd5d6f14f1c8508f16ad84a8dc4849a` | Rigidity lane independently reconstructed and inspected all seven theorem proofs; no correction required. |
| Certificate written proof | `7f85995926e7d17bc3770006fea8fb8e6720c2662ffb51ddb61c773dca628de8` | Coupled pumping, empty blocks, shortening and bounded-alphabet scope verified. |
| Low-clock and renewal note | `96b369f8ff4fe0f4df93828996dc2d130404b0be6028f28a8c87ba8c3adc3fbf` | Arithmetic lane verified the count, norm, exact source-law factors and external theorem hypotheses. Its final review also checked the added tent-window argument and exact exponential-base inequality. |
| Actual compact joining | `031708db20aa1c99b1b46eac25d94f85425826e154b1ace4ed22780ada1e7782` | Root checked the pole cutoff, invariance, rotation control, binary-run observation and ordinary finite-shadow distinction. |
| Critical ordinary network | `47a45d89861bdc89c5219515f91884143ce240c80778acba932804d1615e81c4` | Harmonic lane verified the null functions, finite-support approximation, constants and criticality application under the pinned inputs. |

## Evidence limits

The context-free-language corollary uses the classical pumping lemma in
writing; the Lean result starts from the explicit `PumpsAt` property.
The norm estimates, renewal application, compact joining and infinite
network results are written proofs, not new Lean imports. Their external
inputs and the source-qualified canonical constructions retain the
qualifications stated in the research packet.

No full-repository bounded search or historical proof replay was run for
this checkpoint. The standard complete-checkout repository validation is
a separate publication gate. Its output is not a substitute for the
mathematical argument or the fresh proof receipt above. The published PR
description records the actual gate outcome and remote-head verification.

The research result remains: **no positive global closing estimate and
no proof of full Collatz were obtained.** The substantive output is the
precisely scoped new theorems and the demonstrated boundaries of the
four attempted applications.
