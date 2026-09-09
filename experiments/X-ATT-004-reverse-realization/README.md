# X-ATT-004 — reverse-realization finite protocol

All underlying claims are PROPOSED pending independent mathematical review.
The protocol is bounded exact evidence, not a proof of global convergence.
Parent: `912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`.

From the repository root:

```bash
python -B experiments/X-ATT-004-reverse-realization/run.py \
  --check experiments/X-ATT-004-reverse-realization/results/canonical.json
python -B experiments/X-ATT-004-reverse-realization/verify.py \
  experiments/X-ATT-004-reverse-realization/results/canonical.json --self-test
python -O -B experiments/X-ATT-004-reverse-realization/verify.py \
  experiments/X-ATT-004-reverse-realization/results/canonical.json --self-test
```

Only the generator's explicit `--write` option writes a report. Both scripts
use explicit exceptions, not assertions removed by optimization. No generator,
prior verifier, or other repository module is imported.

## Independent implementation directions

`run.py` composes formal binary words, enumerates all eligible components under
the proved finite length bound, computes ternary valuations, and reconstructs
every qualifying smaller ancestor. It obtains the complete rank table by
literal component minimization.

`verify.py` instead starts with all POSITIVE sources x<N and follows their actual
shortcut trajectories for the complete clock bound. At endpoints n in the
range, it reconstructs the component from the orbit gap, g(Z)=3^q*g(n-x).
It independently obtains the complete rank table and source/word pairs by this
route. Separately, it reconstructs the word census from actual residue paths.
Normalization outcomes are assembled in increasing source order, rather than
rerunning the generator's per-source loop. Large inverse words are evaluated
in reverse with rational numerators and denominators; CRT echoes use a different
congruence construction.

The verifier compares the ENTIRE regenerated payload, including all coverage
and status strings and transcript hashes. Twelve distinct alterations change
coverage, counts, ranks, source bounds, a physical family, a CRT source, or status
labels; each digest is recomputed before rejection. A no-op mutation is rejected
by the self-test itself.

## Exact coverage

- Ordinary source range 2..4096: 4095 exact rho values.
- All 16382 binary words of lengths 1..13 in the independent word census.
- All 1688 qualifying source/word pairs under that COMPLETE source-specific
  length bound, independently reconstructed through positive forward paths.
- Complete rank balls at X=64,256,1024,4095: 19,47,94,192 sources respectively.
  Properness rho(n)>=n-1 makes the ordinary range sufficient for these balls.
- One-step normalizer counts: 2048 even, 1023 forward-10, 341 inverse-1,
  113 inverse-110, 1 additional dictionary reduction, 569 residual labels.
- All 4095 composed physical merging diagrams: 184 terminate at core 1;
  maximum 16 successful normalization edges, maximum summed two-source clock 24.
  Ending at a residual is not classified as divergence.
- Six old even-exit substitutions and five odd illegal-minimizer substitutions.
  Large rho formulas are checked by the exact sufficient premises of parent
  ATT-204, NOT by exhaustive large dictionary evaluation.
- Twenty-one ordinary echo sources: three at each K=1,2,4,8,16,32,64.
  They test 381 forward positions and their exact inverse cancellations.
- The near-critical control 110 at n=7: g(Z)=48<=49 but the inverse is 17/3.
- Twelve resealed corruption rejections in each verifier mode.

Semantic SHA-256:

```text
a6f7d63e6c6f54f0d0078d02768ebc56226880f436f3365bbaef0e738d7cf75f
```

## Evidence ceiling

The all-word physicalization, sharp spectrum and infinite tails are written
proofs, not finite extrapolations. The code does not prove Q-ATT-301, produce
an exhaustive residual cover, establish a uniform transported moment, or
independently peer-review its own mathematical premises. Both implementations
have the same author.

No full-repository structural validation is claimed in this continuation.
An actual direct Git read failed DNS; the publication receipt separately records
GitHub API writes and readback. Existing parent experiments are unchanged and
are not claimed to have been rerun by this protocol.
