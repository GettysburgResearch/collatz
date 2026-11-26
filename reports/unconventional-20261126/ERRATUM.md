# Scoped correction to PR201's record-renewal packet

**Source:** PR201, `94ce06ccbd312ccd0ce4450b567cc514a2f0b54a`,
`research/killed-green-head-closure-20261124/record-renewal/README.md`,
section 5.2 (isolated wrong-gap shadow).

The sentence placing `-2/2^e` in `[-1/2,-1/4]` for every `e>=2` is false:
`e=4` gives `-1/8`. The correct range is **`[-1/2,0)`**.
The subsequent two affine steps still have the asserted positive endpoint
and bounds; neither the construction nor the theorem changes. The active
sentence is corrected and links to this note. The original remains available
at the exact source commit above.

The renewal audit reconstructed the bounded-alphabet parsing argument and
checked Caravenna's stated ladder-tail input. The new coordinator separately
replayed the exact integer controls. The first naive JSON comparison failed
because it compared an execution payload with its enclosing published
metadata object. The corrected comparison checks the actual integer fields
exactly and records the approximately machine-epsilon differences in the
illustrative floating roots. Both events are preserved in
[BASELINE_CONTROLS.json](BASELINE_CONTROLS.json).

The historical statements that the original authoring session did not
compile Lean remain historical statements. In this pass the unmodified
`import Mathlib` candidates failed on a missing cached dependency. Replacing
only that import with the listed narrow imports allowed the **unchanged
proof bodies** to compile: ten record-renewal declarations and four thin-band
declarations. Their original benign warnings were retained. This is recorded
as import-only replay, not compilation of the original complete file bytes.
PR206 separately reports its earlier native check; no priority is claimed.

The new 53-declaration packet has its own exact-source receipt and does not
inherit the verification status of either older execution.
