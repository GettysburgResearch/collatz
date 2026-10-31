# Positive-floor bridge: execution and source record

## Exact local checks

The new standard-library verifier passed in **normal and optimized Python**,
with byte-identical complete deterministic JSON. The fresh subprocess
receipt is [replay.json](replay.json), and the saved output is
[positive_floor_checks.json](../../experiments/positive-floor-bridge-20261031/positive_floor_checks.json).

Coverage includes 501 positive odd first/dead-letter profiles (1,503 exact
checks), 650 synchronized-clock frontiers (1,980 leaf evaluations), and
three finite killed models with 16, 32, and 64 states. The finite-model
portion contains 9,856 inequality/resolvent checks, 672 adaptive-clock
frontiers, and 4,032 inverse-tail checks. These counts describe actual
finite coverage, not a probability of proof correctness.

The finite models use exact Green functions with cycle renewal, not a time
cutoff. Ternary laws through level six sum the infinite geometric exponent
tails exactly. The test imports the hash-pinned recovered inverse-law helper.
It retains prefix-overlap and zero-residual-clock negative controls.

Together with the recovered packet's ten normal/optimized runs, the recorded
paired replay set contains **12 passing processes across six suites**.
Additional initial recovery/regeneration runs are recorded separately.

## Evidence ceiling

The new analytic proof received a same-assistant adversarial self-check,
not an independent-agent review. No external Lean source chain, canonical
infinite-state floor, or full Collatz result was verified computationally.
No complete-checkout structural validation was run in this partial payload.

## Source and integration boundary

The exact external source pin and claim names are in the
[rebuilt source ledger](../beeping-density-swarm-20261031/EXTERNAL_SOURCES.md).
PFB-001--002 are local implications from a finite nonnegative superharmonic
function with one target-uniform positive floor on units. PFB-003 invokes
external premises to instantiate that hypothesis. PFB-004 is unconditional;
PFB-005 distinguishes its elementary root-3 control from its conditional
infinite dead-frontier assertion.

This pass changes no accepted registry, integrated scientific verdict,
workflow, repository setting, license, or other contributor's branch.
The new bridge has not been pushed in this session. The earlier 13-file source
recovery is now verified at `3c0ce26d6021fbd700df61652d596293b661612c`; the
output patch adds only the remaining 19 files to that existing PR142 branch.
