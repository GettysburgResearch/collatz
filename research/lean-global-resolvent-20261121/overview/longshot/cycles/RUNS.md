# Recorded runs for the identity-atom attempt

Date: 2026-11-23 UTC. Runtime: Python 3.12.14; g++ (Debian 14.2.0-19) 14.2.0.

All commands below were actually run in this directory. The two complete word enumerations were run once each. The small witness and parameter verifiers were run after writing the final retained scripts. No output here is a proof for untested parameters, and this checkpoint contains no new general cycle exclusion.

## Small independent checks

```sh
python fiber_8_5.py > fiber_8_5.txt
python verify_witnesses.py --complete-fiber > verify_witnesses.txt
python validate_recorded_parameters.py > validate_recorded_parameters.txt
```

`verify_witnesses.py` without its option checks only the nine supplied witnesses and the comparable pair. The recorded option additionally recovers the selected fiber from 86,283 exact numerator candidates. It does not redo either large word enumeration.

## Two complete fixed-weight word enumerations

```sh
g++ -O3 -std=c++17 full_fibers.cpp -o full_fibers
./full_fibers 32 20 > full_32_20.txt
./full_fibers 35 22 > full_35_22.txt
```

The second command allocates roughly 0.81 GB for its counters, and the third roughly 2.98 GB. Their outputs were:

```text
A=32 p=20 D=808182895 words=225792840 max_fiber=7 residue=373007490 zero_fiber=0
A=35 p=22 D=2978678759 words=1476337800 max_fiber=9 residue=2209100811 zero_fiber=0
```

The exact scope is all words of the indicated length and weight. It is not all words up to either length. The existing PR175 enumeration at `(27,17)` was not repeated.

## Four complete rational-denominator slices

```sh
g++ -O3 -std=c++17 rational_slice.cpp -o rational_slice
./rational_slice 46 29 39409 15407792 > slice_46_29_39409.txt
./rational_slice 65 41 551 660519 > slice_65_41_551.txt
./rational_slice 149 94 343 1151678 > slice_149_94_343.txt
./rational_slice 233 147 5 33744 > slice_233_147_5.txt
```

Their summary lines were:

```text
A=46 p=29 d=39409 bound=15407792 cycles=874 points=40204 max_fiber=7 residue=8698 last_minimum=4932331
A=65 p=41 d=551 bound=660519 cycles=9 points=585 max_fiber=9 residue=152 last_minimum=134045
A=149 p=94 d=343 bound=1151678 cycles=1 points=149 max_fiber=2 residue=32 last_minimum=177337
A=233 p=147 d=5 bound=33744 cycles=0 points=0 max_fiber=0 residue=0 last_minimum=0
```

The exact scope of each run is the `d` residue fibers `rD/d mod D`, `0<=r<d`, for its pair `(A,p)` and `D=2^A-3^p`. The complete nonzero slice histograms follow the summary line in the retained output files. The `last_minimum` value is a diagnostic from the last enumerated cycle contributing to the first maximizing residue, not an extremal claim about all cycles.

The executable takes its minimum bound as an input. `validate_recorded_parameters.py` verifies the exact bound, divisibility `d|D`, coprimality conditions, and arithmetic ranges for these recorded invocations. The proof of slice completeness is in `IDENTITY_ATOM_ATTEMPT.md`.

## Files and integrity

`MANIFEST.sha256` records SHA-256 hashes of the retained note, scripts, witness JSON, this run record, and all textual outputs. It deliberately excludes itself and the locally compiled executables; the latter are reproducible from the listed source and compiler commands.

The checked small commands are sufficient to review the numerical comparable-pair obstruction without repeating the larger enumerations. The large outputs substantiate only the explicitly recorded finite scopes.
