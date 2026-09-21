# PSS exact finite experiment

Python standard library only. Raw shortcut clock throughout. All core-arrival
searches have a 10000-step bound and raise UNRESOLVED on budget exhaustion; they
do not silently assume universal convergence. The fixed corpus happens to
complete those searches for every input it uses.

```sh
python -B -S experiments/X-AEM-007-pointwise-signatures/run.py --full pss-full.json --check experiments/X-AEM-007-pointwise-signatures/canonical.json
python -B -S experiments/X-AEM-007-pointwise-signatures/verify.py pss-full.json --summary experiments/X-AEM-007-pointwise-signatures/canonical.json --self-test
python -O -B -S experiments/X-AEM-007-pointwise-signatures/verify.py pss-full.json --summary experiments/X-AEM-007-pointwise-signatures/canonical.json --self-test
```

## Fixed inventory

- H(C)=9C+2 and C at every C=1..65536, including the C=2 mod3 subpopulation.
- Seven specified affine collections at every valid point 1..64, plus 32
  power-of-two controls at point zero: 479 finite collection rows.
- Primitive lifts with equal, favorable, and unfavorable source-order slopes.
- Ten direct members of the strict escape family, including h=2^256.
- Root mine at every n=2..4096; an index of smaller verified trajectories is
  queried only before the original first coefficient crossing. Returned source
  inequalities are relative to n, never merely relative to an intermediate.
- Drift checks for every odd n=3..2049 through its initial above-source prefix,
  with six explicitly specified companion clocks at every observation.

The summary's hash binds the complete deterministic JSON corpus. Large rows are
regenerated rather than committed. The verifier reconstructs all H outcomes at
ALL future clocks via the first literal meeting and core phase. It also checks
whole affine progressions and the exact finite inventory of collection inputs.
It does NOT re-search negative/optimality decisions in the secondary root mine;
all 1130 returned successful affine families are nevertheless checked in full.

Self-tests reject 23 direct semantic/JSON controls. No claim of independently
resealing and revalidating 23 full corpora is made. The verifier imports no
run.py or repository module. This is same-author implementation diversity,
not independent mathematical review.

The scientific status is PROPOSED. Numeric counts are language classifications,
not a convergence census or a percentage of the conjecture solved. See the
research proof and the exact execution receipt for the noncomputational claims.
