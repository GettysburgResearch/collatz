# X-A3-001: exact finite checks for the three-route packet

These are standard-library, deterministic finite certificates. They do not
verify the open all-time Mellin bound, SC*, FC*, or Collatz. The finite arithmetic
also does not replace independent review of the proposed all-length proofs.

From the repository root:

```bash
python experiments/X-ASTRA3-001-three-routes/run.py \
  --check experiments/X-ASTRA3-001-three-routes/results/canonical.json
python experiments/X-ASTRA3-001-three-routes/verify.py \
  experiments/X-ASTRA3-001-three-routes/results/canonical.json
python experiments/X-ASTRA3-001-three-routes/test_verifier.py
```

To regenerate deliberately, use `run.py --output <new-path>` and compare before
replacing the canonical file. No optional solver or external package is needed.
The largest inverse cone in this protocol contains 2,510,783 integers; the scripts
keep that cone in memory and are not intended as a large-scale distributed job.

## Independence of implementations

The verifier imports neither the generator nor any repository module.

| Interface | Generator | Verifier |
|---|---|---|
| Inverse cone | Newly discovered set frontiers | FIFO shortest-distance traversal |
| Fractional weights | isqrt(B^2 // n^3) | Reciprocal square-root estimate, then both squared integer inequalities |
| Crossing words | Prefix tree with coefficient pruning | Fixed-weight odd-position combinations |
| Echo filtering | Affine numerator inequalities | Rational parity replay at the forced disagreement |
| Carry normalization | Leftmost adjacent swaps | Rightmost swaps plus arithmetic mixed-radix decoding |
| Odd macro | Run formula against a run-based iterator | Exact stipulated a+b branch replay |

Both were authored in this session. This is implementation independence, not an
independent research-agent or human review.

## Scope and integrity

The JSON contains an explicit finite scope, exact integer interval endpoints,
per-horizon coverage, and transcript hashes. Decimal values printed by the
program are presentation only. Critical fractional-power brackets are checked
by integer exponentiation; their floating-point proposal is not a proof input.
The verifier rejects resealed changes to scope, horizon coverage, and physical
rank witnesses, not just an unchanged outer hash.

The mass certificate covers every positive source at its **finite** horizons.
The crossing-sieve certificate enumerates formal **rational** sources before the
whole-denominator integrality gate. It does not count these as ordinary
counterexamples. The rank examples are finite regressions; T-A3-301's proof is
the justification of its all-class statement. Six additional exact macro rank
witnesses test the separately proved T-A3-302 interface.

Proofs and provenance: [research packet](../../research/astra-three-routes/README.md).
