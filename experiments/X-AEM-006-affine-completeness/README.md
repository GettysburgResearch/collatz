# Exact affine completeness and fixed-companion clock checks

Standard-library Python research experiment for proposed ACS-001--004.
The checker imports no generator or repository module. There are no assert-based
safety predicates that disappear under Python optimization.

## Commands

```sh
python -B -S experiments/X-AEM-006-affine-completeness/run.py --full acs-full.json --check experiments/X-AEM-006-affine-completeness/canonical.json
python -B -S experiments/X-AEM-006-affine-completeness/verify.py acs-full.json --summary experiments/X-AEM-006-affine-completeness/canonical.json --self-test
python -O -B -S experiments/X-AEM-006-affine-completeness/verify.py acs-full.json --summary experiments/X-AEM-006-affine-completeness/canonical.json --self-test
python -OO -B -S experiments/X-AEM-006-affine-completeness/verify.py acs-full.json --summary experiments/X-AEM-006-affine-completeness/canonical.json --self-test
```

For a custom uniform family, use canonical AP residue 0<=a<M:

```sh
python -B experiments/X-AEM-006-affine-completeness/run.py --family '[[8,-5],[4,-1],[3,-5]]' --ap '[7,24]'
```

This **refines** the supplied progression; it does not claim all its inputs
succeed. The result includes the base, modulus, actual words, and a common
affine endpoint. `incompatible_slopes` means no infinite uniform fixed-word
merger, not that any particular positive source diverges. JSON quoting follows
the shell in use. Imported functions accept arbitrary finite compatible lists;
no user-supplied code is executed.

## Exact finite coverage

The deterministic full corpus contains 6,825 rows:

- 1,713 chart cases: all d=0..12 and b=-64..64, plus the specified large signed
  and zero-intercept controls for d=1,2,7,17,33,64.
- 1,013 affine-family classifications: every slope pair A,C=1..18 with three
  intercept choices; 32 three-template cases; nine explicit examples. Of these,
  388 return uniform merger certificates and 625 have incompatible slope cores.
- 4,095 first-entry cases, exactly n=2..4096. All 1,023 H entries retain both
  #123 and #125 traces, the same original companion, its independently checked
  first core-hit time, and a conservative physical-clock bound. The other
  3,072 cases merge in the initial entry rule.
- Four raw core-phase controls. No phase mismatch is inferred merely from a
  failed bounded search; the first-hit times supply the relevant exact evidence.

The checker verifies symbolic parity legality on each FULL progression,
identical affine endpoints across all arms, forced clock/odd-count differences,
the original AP, positive thresholds, exact inventory, and raw replay at
parameter increments 0,1,7. Type construction is checked through its controlled
reductions, including the required zero-intercept step. All finite failures
and no-uniform classifications remain in the artifact.

The self-test rejects 22 independently re-sealed full-corpus mutations, including
integer/bool aliasing, false clocks/order/cylinders/cores, modified input
progressions, and a same-length coverage replacement. These mutations are checked
without relying on the external canonical summary. Separate input-contract tests
are recorded in the validation receipt.

Additional deterministic contract and multi-family checks:

```sh
python -O -B -S experiments/X-AEM-006-affine-completeness/contract_check.py
```

This separate harness rejects 17 invalid inputs/type/duplicate-key cases and
checks 256 additional multi-source families using the recorded deterministic
seed. It loads both implementations; it is not a third independent mathematical
review or a new coverage theorem.

## Reproducibility and scope

`canonical.json` is only a small summary with a typed canonical JSON SHA-256 over
the complete ordered rows. `--full` regenerates the full payload; the large file
is not required in Git. The separate verifier checks the payload semantically,
then checks its exact stated coverage and (when requested) the published summary.

Full-row SHA-256:
`7660208731d85943bd662ac2ede13e3a10b5a812b6b4a1434fc3cb360f0a6d8c`.

Maximum compiled chart-word length in this fixed corpus: 261. This is a finite
statistic, not a universal word-length bound; the symbolic bound is in PROOF.md.
No new Lean build, remote CI or full-checkout root-validator run is inferred
from these tests. They are implementation evidence, not independent mathematical
acceptance of the universal statements.
