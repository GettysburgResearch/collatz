# X-ASR-001: exact suffix rotation and attempted coverage

**Finite evidence only; no complete Collatz proof.** The all-parameter claims
are proved in [PROOF.md](../../research/astra-suffix-rotation/PROOF.md) and
remain proposed pending independent review. Python 3.10+ and the standard
library suffice.

From the repository root:

```bash
python -B experiments/X-ASR-001-suffix-rotation/run.py \
  --check experiments/X-ASR-001-suffix-rotation/results/canonical.json
python -B experiments/X-ASR-001-suffix-rotation/verify.py \
  experiments/X-ASR-001-suffix-rotation/results/canonical.json --self-test
python -O -B experiments/X-ASR-001-suffix-rotation/verify.py \
  experiments/X-ASR-001-suffix-rotation/results/canonical.json --self-test
```

`--check` never replaces the artifact. Both programs accept `--full-output`
for all reconstructed rows. The generator additionally exports `select(n)`,
which returns a physical reduction, CORE, or UNRESOLVED. Every selected output
is independently reconstructed in the finite corpus.

## Fixed protocol

- All 8191 sources 2..8192; all ties in their minimizing-prefix lists.
- 8393 eligible suffix rotations, checking positive ordinary preimages,
  physical words, exact displaced-candidate transport and the common-rank bound.
- 3906 sources with a length-one minimizer; every one has an accepted reduction.
- 7470 inputs with a forward certificate, 303 additional backward-only inputs,
  and 418 explicitly unresolved inputs. These are NOT complete convergence claims.
- 40 ternary-unit spike sources and their explicit backward witnesses.
- Every Mersenne exponent 2..64 and all 2016 early phase positions.
- Eight long-suffix fixtures: words 1^a0 at a=18,19,24,32 and two ternary
  precisions each. Their high-odd-density guard is checked with exact powers.
- Nine COMPLETE Psi sublevels through 8^8; the source cutoff follows from
  Psi(n)>=n(n+1), not a sampled truncation. Infinite-tail formula checks are
  arithmetic-geometric identities, not a numerical all-time estimate.
- The 11/17 incompatible-rank cycle and a failed inverse integrality control.

The generator evaluates Gamma through actual differences with a running
minimum. The verifier independently reconstructs raw affine numerators over
the whole baseline window, and obtains inverse witnesses by literal backward
rational steps. Its long fixtures use extended Euclid rather than modular
`pow`. Neither imports the other or any repository mathematics module.

Both compare canonical typed JSON, so integers, booleans and integral floats
are not silently aliased. Twelve deliberate mutations are resealed, then
rejected by reconstructed mathematics, scope or typed coverage. Assertions
are not used for acceptance, and the checks remain active under `-O`.

The compact digest also commits to a separately reproducible full-payload
digest. Neither hash proves the universal mathematical statements. Both
implementations have the same author, so their agreement is implementation
independence, not independent mathematical peer review. Exact execution
receipts are in [validation.json](../../reports/astra-suffix-rotation-01/validation.json).
