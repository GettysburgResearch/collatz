# X-AEM-004: exact shadow-switching certificate experiment

**Finite evidence supporting PROPOSED mathematics.**
Statement and proof: `research/astra-exit-merging/shadow-switching/PROOF.md`.
No external package, proof oracle, floating-point guard, or network service
is used. The generator and verifier are standalone standard-library programs.

## Interface

`run.py --source N --budget J` accepts a positive ordinary source at least
two and a nonnegative hard-return stage budget. It returns a certificate,
an explicit outside-burst/return result, or a budget result. The complete
odd-u representation is read by v2(N+5); it is not assigned to every source.

`run.py --check results/canonical.json` rebuilds the declared compact
payload and checks canonical typed JSON bytes. `--full PATH` writes all
family and ambient rows, including unsuccessful outcomes, parent comparison
rows, path words, exact clocks, endpoints and path minima.

`verify.py results/canonical.json --self-test` independently reconstructs
the expected payload and rejects a matching digest with incorrect content.
It checks branch legality and a separately accumulated affine endpoint for
every new source witness. It also checks whole-cylinder polynomial identities
and parity on every translate of 411 specified families.

Run both commands from the repository root with the full paths shown in the
research guide. Repeat the verifier under `-O` and `-OO`; the safety checks
use explicit exceptions, not assertions. JSON integer/boolean/integral-float
aliases are rejected by typed canonical encodings.

## Declared corpus

* 711 new family rows: k in {1,2,3,15,26,40}, exact t=4..40 for direct
  cases; both t parities and arbitrary changing finite hard-label lists for
  return cases; additional k=200, t=128/129 and twenty growing-return controls.
* 108 general-period cases from the negative centres 5 and 17, including
  their uniform no-forward-descent thresholds and larger values.
* Every k=1..6, positive odd u<8192: 24,576 original sources. The old
  selector is also reconstructed on exactly those inputs.
* Core n=3, new seed examples, the old 3003 alternate companion, two large
  no-descent examples, and an explicit exhausted-budget H itinerary.

Canonical payload SHA-256:
`32c047148186cd9b35a6f1d34d48be3af9130df28cc7a28ce070289d36293056`.
The full row digests are inside that payload. A digest alone does not prove
any mathematical claim; the verifier reconstructs the declared content.

The adversarial suite contains 22 re-sealed mutations and six direct
physical-witness corruptions. The bounded counts are 14,193 successful
mergers and 10,383 OUTSIDE_RETURN results. There is no OUTSIDE_SEED within
this representation, but outside-burst inputs still exist and a bounded
successful count is not universal convergence.

See `reports/astra-exit-merging-04/validation.json` for commands actually run,
file identities and evidence ceilings. Same-author implementation diversity
is not independent mathematical review.
