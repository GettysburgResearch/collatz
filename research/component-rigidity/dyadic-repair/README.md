# Dyadic elimination and actual odd-edge repair

**PROPOSED; no complete Collatz proof; no independent mathematical review.**
Read [PROOF.md](PROOF.md) for DR-001--006, exact hypotheses, proof bodies and the
first unsupported inference. This continues #138 at
`45c970ccb3d0b034f6e5696710d9a94df66b2b27` without changing its earlier packets.

## What is new

The preceding pin-only relaxation does not impose halving equalities on every
unpinned integer. This packet imposes ALL of them, at every height, and eliminates
unmarked dyadic subtrees into exact two-terminal capacities. The result is a
finite network of size bounded by the sum of marked source bit lengths. At
infinite horizon the structural formula is exact; numerical answers are rigorous
rational lower/upper enclosures, not claimed exact irrational minima.

Every nonconstant step completion of that network yields a specific violated
actual odd edge. For 3x+1, if its last dyadic grid has depth K, the constructed
source is below 16*2^K and its shortcut physical peak is below 24*2^K. This is
an effective finite-description obstruction, not a proof that infinitely refined
component separators are impossible.

The experiment alternates violated-edge insertion with an immutable-original-
source fairness step. Root-fair convergence is certified by a literal path;
it is not inferred from a flow value. Its recovery of 27's known convergence
is a regression test, not a new family eliminated from the full conjecture.
A cuts-only run on 27 remains unfinished at its retained cap. Actual 5x+1
non-core cycles and further unfinished runs are preserved.

## Reproduce everything

Python standard library only. The scripts work under `-S`, `-O` and `-OO`.
From the repository root:

```sh
python -B -S research/component-rigidity/dyadic-repair/tests.py \
  --corpus /tmp/dyadic-repair.json --summary /tmp/dyadic-models.json
python -B -S research/component-rigidity/dyadic-repair/verify.py \
  /tmp/dyadic-repair.json --models /tmp/dyadic-models.json --self-test
```

The first command generates the full payload rather than committing a large JSON.
The checker imports neither the generator nor flow code. It reconstructs dyadic
intervals and physical components, checks exact rational cut/flow certificates,
checks the full low-depth oracle inventory, and replays every asserted path.
[RESULTS.json](RESULTS.json) retains compact outcomes and canonical hashes;
[VALIDATION.json](VALIDATION.json) records the commands actually run and their
limits. Running the checker alone does not independently review the written
infinite theorems.

A single source:

```sh
python -B -S research/component-rigidity/dyadic-repair/run.py \
  --source 27 --ladder-depth 3 --rounds 96 --output /tmp/27.json
python -B -S research/component-rigidity/dyadic-repair/verify.py /tmp/27.json
```

Use `--policy cuts-only` to test whether candidate-exclusion alone suffices in a
chosen finite budget. It is not a completeness claim. `--multiplier 5` runs the
explicit control map. `--tail-terms L` controls the rational infinite-tail
enclosure. The model solver can also be called with a finite shell horizon;
those minimum values are exact rationals.

## Outcomes and resources

`CONVERGENCE` includes a literal path from the original N to 1.
`VERIFIED_OTHER_CYCLE` includes a literal path and a repeated state delimiting
a cycle excluding 1; the retained examples are all for 5x+1.
`UNRESOLVED_AT_RESOURCE_CAP` includes the last consistent cut and every inserted
constraint. None of these unresolved labels is a nonconvergence certificate.

Network size is O(sum of marked bit lengths), but the number and sizes of newly
marked sources are not bounded globally. Exact rational capacities can also
be expensive at high precision. The 513-bit source test with symbolic horizon
2^521 has only 513 compressed vertices; it is a selected-constraint energy
calculation, NOT a convergence verification of all integers below that height.

## Next actual mathematical task

Bound the cumulative cost of nonlocal odd-edge repairs, with one fixed ordinary
source and the critical energy weight, or force finite pin inconsistency using
arithmetic genuinely specific to 3x+1. The local 2*W_(d+1) birth cost alone is
not summable across all depths. Density, finite-step regularity and the 5x+1-
compatible pieces do not supply this missing theorem.
