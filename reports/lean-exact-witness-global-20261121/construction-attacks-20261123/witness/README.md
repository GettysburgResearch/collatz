# Witness charge: actual execution and scope

23 November 2026. This report records new standalone Lean proofs and exact
finite controls for the
[witness-charge manuscript](../../../../research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/WITNESS_CHARGE_AND_POWER_INDUCTION.md).
The original residue-512 implication and the full Collatz conjecture remain
**OPEN**. The mathematical claims are at WC1--WC25 in that manuscript;
this execution report is not a claim of universal convergence.

## What is new and what is inherited

The complete-witness charge `2 * odd_steps - clock` classifies the stated
homogeneous half-map and power-family merger constructions. It gives an
all-clock exclusion of homogeneous half-map mergers on an infinite source
family, an obstruction to every finite-seed homogeneous power-merger
induction, and an unbounded lower bound on the number of one-coordinate
edits in any successful literal alignment.

For the retained family
`K = (2^(54*k) - 1) / 81`, `x = 256*K + 1`, `y = 128*K + 1`, every
successful alignment has at least `9*k + 2` edits, despite the source
having a four-odd-step witness. There is no clock bound in this statement,
and arbitrary padding around the `1 -> 2 -> 1` cycle is allowed.
This is a lower bound, not a construction of a successful alignment.

The four-odd-step source family, its forced target prefix to
`3^(27*k) + 1`, and the earlier separation of source and target witness
lengths are **inherited** from
`research/lean-exact-witness-global-20261121/lean/Collatz/WitnessLengthSeparation.lean`.
The new charge and edit-cost results are not a claim of priority for that
family or its old length-separation theorem. Frozen source identities and
the exact reuse boundary are in [SOURCES.json](SOURCES.json).

## Strict Lean execution

The new `WitnessCharge.lean` imports only `Std`. The following actual
command completed with exit code zero in the complete working checkout:

```text
/workspace/scratch/c6766c1207a3/collatz_work/nov23_runtime/lean-4.34.1-linux/bin/lean -j 1 -DwarningAsError=true /workspace/scratch/e15c6f8bf5c3/collatz-lean-global/research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/WitnessCharge.lean
```

The working directory was
`/workspace/scratch/e15c6f8bf5c3/collatz-lean-global`.
The actual output is [lean-strict-audit.log](lean-strict-audit.log).
All **21 public declarations** were audited by `#print axioms`:

```text
pad_complete
complete_tail
complete_charge_unique
profile_height
complete_clock_bound
cylinder_lift
half_germ_of_charge
half_germ_charge
half_germ_iff
half_germ_family
four_step_profiles
no_half_germ_four_step
power_germ_transport
power_germ_of_charge
power_germ_iff
power_germ_transitive
power_germ_family
power_signature_lower_bound
no_large_power_germ_to_seed
alignment_charge_bound
four_step_edit_lower_bound
```

Their axiom union is exactly `propext`, `Classical.choice`, and
`Quot.sound`; there is no `sorryAx` or custom axiom. The general
rational-slope affine classification and the prime-factor argument
connecting arbitrary fixed words to the formal germ definitions are
written-proof scope, explicitly identified in the manuscript. The finite
seed obstruction uses the formal transport theorem, transitivity, and
the formal unbounded signature estimate; the finite-set maximum argument
is written in the manuscript.

## Exact Python controls

Both of these commands completed with exit code zero in that same
working directory:

```text
python -X utf8 -B /workspace/scratch/e15c6f8bf5c3/collatz-lean-global/research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/check_witness_charge.py
python -O -X utf8 -B /workspace/scratch/e15c6f8bf5c3/collatz-lean-global/research/lean-exact-witness-global-20261121/construction-attacks-20261123/witness/check_witness_charge.py
```

The outputs [normal.json](normal.json) and [optimized.json](optimized.json)
are byte-identical, with SHA256
`9271bb7607b1a54d36a4b312d6ecd3d103587125a1251ee9f7207e6be3c6ddc0`.
Checks use explicit exceptions, so Python optimization does not remove
the checks. The coverage is:

| Control | Actual extent |
|---|---:|
| Complete-witness cycle padding | 640 cases |
| Literal binary-cylinder lift | 2,496 cases |
| Half-germ charge classification | 49 complete known pairs |
| Constructively lifted half-germ families | 36 parameter cases |
| Power-germ charge classification | 1,770 pairs among exponents 1--60 |
| Positive power-germ pairs | 155 |
| Explicit affine exponent-decrease cell | 12 parameter cases |
| Retained four-step source family | `k = 1,...,12` |
| Rejected unsupported strengthenings | 4 |

The first retained four-step pair has exact source and target first-hit
clocks 62 and 280, and complete charges -54 and 4. Exact 0--1 shortest-path
search on the finite, closed product of their two actual eventual-cycle
orbits proves minimum edit cost **138**. The full product has 17,703
states; the search settled 10,931 states and examined 27,327 edges. The
optimal 279-column alignment was replayed to equal endpoint 2. This is a
finite all-clock computation: repeated visits to the two-state cycle do
not create new product states. It supports the formal lower bound but is
not used to prove the all-parameter result.

The finite-seed illustration uses the actual complete profiles for
`3^a + 1`, `1 <= a <= 27`, whose maximum signature is 72. The signature
theorem excludes a homogeneous germ from exponent 219 to these seeds.
The checker does **not** assume or simulate convergence of `3^219 + 1`.

## Receipts and limits

[REPLAY.json](REPLAY.json) contains the actual commands, working directory,
exit codes, full emitted outputs, output hashes, and frozen science-file
hashes. [SOURCES.json](SOURCES.json) records the source boundary and prior
work used. No prior large suite was rerun as part of this report, and no
repository-wide validation, independent review, commit, or remote write
is claimed by these receipts.

The remaining constructive target is a universally successful procedure
using the supplied full source witness. The all-clock exclusions proved
here apply to the stated homogeneous affine architectures, and the edit
result only rules out a budget depending on source odd-step count alone.
They do not exclude an unbounded, source-dependent edit constructor or
other ordinary-integer witness constructions.
