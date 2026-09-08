# X-ATT-001 — exact critical-tail interfaces

These are finite regression checks for [ATT-001..006](../../research/astra-tail-transport/PROOF.md),
not an all-time tightness certificate or a Collatz proof.

From the repository root:

```bash
python -B experiments/X-ATT-001-critical-tails/run.py --check experiments/X-ATT-001-critical-tails/results/canonical.json
python -B experiments/X-ATT-001-critical-tails/verify.py experiments/X-ATT-001-critical-tails/results/canonical.json --self-test
python -O -B experiments/X-ATT-001-critical-tails/verify.py experiments/X-ATT-001-critical-tails/results/canonical.json --self-test
```

Only an explicit `--output PATH` writes a report. Check and self-test commands
are nonmutating. Both scripts use standard-library integers and Fraction; no
floating-point comparison decides a proof condition. Predicates use explicit
exceptions and remain active under optimization.

## Frozen finite coverage

- Ordinary source cutoff: 4096; exact moving rank and module checks for 4095
  positive non-core inputs; 1469 are quarter-unsafe.
- Six source-tail enclosures, nine raw clocks and six rank cutoffs: 54 raw
  tail rows and six induced-tail rows.
- Every displayed tail enclosure covers ALL omitted sources using `43/4096^2`.
  For raw transport it still covers ONLY its declared finite clock.
- 28 exact power-of-three source/clock cases (seven clocks, four exponents).
- Four explicit clock-change family instances, j=2,4,6,8; both parity classes
  of the sharp clock-growth theorem are tested by their adjacent clocks.
- Separate shift/two-cycle model controls guard the order-of-limits and
  tightness-versus-cycle distinction. They are not Collatz counterexamples.
- Eight altered reports with freshly recomputed hashes are rejected.

Semantic SHA-256:

```
d55d976e9aca871c5f341927d6487df8f6771ef27565706635a4ae5a76e7567e
```

## Implementation independence

| Object | Generator | Verifier |
|---|---|---|
| R_* | At most four input-dependent components | Component scan stopped by increasing absolute-form lower bound |
| Maximal A module | Exact affine closed form | Literal shortcut iteration with maximal active mode |
| Raw transported tails | Source trajectories and threshold accumulation | Endpoint-first aggregation with original source rounding counts |
| Affine remainder | Coefficient recurrence | Reconstructed from actual endpoint, clock and odd count |
| Model shift tail | Closed geometric formula | Complement of an exact finite geometric sum |

The verifier imports neither the generator nor a source research module.
Both programs were written by the same author in this session, so this does
not constitute independent mathematical review.

## Scope of errors and hashes

A floor at scale 2^80 underestimates each enumerated source weight by less than
2^-80. The upper endpoint adds one unit per contributing source plus the proved
infinite source tail. Merging endpoints never collapses those rounding counts.
No termination assumption is made for the omitted inputs.

The digest identifies the full canonical payload. The verifier reconstructs
and compares that payload; it does not accept a submitted mathematical claim
merely because its hash is internally consistent. Mutations cover status/scope,
base SHA, source cutoff, missing rows, unsafe population, physical rank,
analytic constant and the limit-order model.

These scripts may discover a proof error, but a finite PASS cannot prove the
universal inequalities or the open closure condition. All those boundaries
are stated in the [proof and source ledger](../../research/astra-tail-transport/README.md).
