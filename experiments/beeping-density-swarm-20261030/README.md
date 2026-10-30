# Bounded replay: beeping machine, density, and rank envelopes

These programs accompany the [research packet](../../research/beeping-density-swarm-20261030/README.md).
They use Python's standard library. Run them with Python 3.11 or later.
All acceptance checks use explicit exceptions and remain enabled under `-O`.
No program decides full Collatz, establishes an asymptotic empirical limit,
or replays an external Lean development.

## Replay the complete packet without changing saved evidence

From the repository root:

```bash
python -X utf8 -B experiments/beeping-density-swarm-20261030/replay_packet.py --output /tmp/collatz-beeping-density-replay.json
```

The driver runs all six suites in normal and optimized modes, using temporary
output files. It requires equality of each complete regenerated JSON object
with its saved receipt, rather than checking only a status field or selected
counts. It compares exact JSON numbers and strings; floating descriptive
diagnostics retain the interpreter's reported values. `--jobs 1` selects
sequential execution; the default is three independent suites at a time.
Every subprocess has a 180-second timeout, which is a failure, not an
unresolved success. A passing driver prints `PASS` and reports 12 executions.

The [publication replay receipt](../../reports/beeping-density-swarm-20261030/packet_replay.json)
records the actual interpreter, source hashes, and complete-payload semantic
hashes for both modes. Its hash covers the whole JSON object; it is distinct
from the inner payload hash in the near-invariant receipt.

## Programs and actual bounded coverage

| Program | Coverage | Saved evidence |
|---|---|---|
| [verify_beeping.py](verify_beeping.py) | 1,068 complete canonical macros, 5,944,690 literal transitions; a separate blank-tape trace through input 26 with 351 beeps; 10,000 arithmetic energy checks. | [beeping_evidence.json](beeping_evidence.json) |
| [check_density_bridge.py](check_density_bridge.py) | Inputs through 100,000; 24,180 scalar rational identities; 99,997 orbit-defect checks; parity bijection and Haar residue balance through 12 bits. | [density_bridge_report.json](density_bridge_report.json) |
| [check_negative_spikes.py](check_negative_spikes.py) | Exact infinite-geometric residue laws through level 6; 21 clipping and 21 annulus checks; 3,006 positive-target density bounds; 5,001 initial-run caps; fixed-depth injectivity and valuation-layer tests. | [negative_spikes_report.json](negative_spikes_report.json) |
| [check_rank_envelope.py](check_rank_envelope.py) | Rank bounds, Bellman identity and contacts through 10,000; independent prefix/envelope implementations through 1,000; 552 complete inverse fans and 1,011 leaf paths; selected critical rational envelopes and power families. | [rank_envelope_results.json](rank_envelope_results.json) |
| [verify_near_invariants.py](verify_near_invariants.py) | 349,524 literal source residues over nine majority lengths; five finite-anchor lengths; explicitly separated formula-only larger cases. | [near_invariants_evidence.json](near_invariants_evidence.json) |
| [check_regularity_review.py](check_regularity_review.py) | A separately written finite majority and soft-clock reconstruction, with 4,999 soft-clock starts. | [regularity_review_checks.json](regularity_review_checks.json) |

The [rank_envelope.py](rank_envelope.py) module contains the actual finite
Gamma/Phi evaluators, contact selector, critical rational envelope, and full
inverse-fan enumerator. It also supports a small inspection command:

```bash
python -B experiments/beeping-density-swarm-20261030/rank_envelope.py 11 17 26 19 29 44
```

## Individual replays

The driver is the simplest immutable replay. To inspect a single suite, use
these commands from the repository root; add `-O` after `python` for optimized
execution.

```bash
python -B experiments/beeping-density-swarm-20261030/verify_beeping.py --output /tmp/beeping.json
python -B experiments/beeping-density-swarm-20261030/check_density_bridge.py --maximum 100000 --output /tmp/density-bridge.json
python -B experiments/beeping-density-swarm-20261030/check_negative_spikes.py --output /tmp/negative-spikes.json
python -B experiments/beeping-density-swarm-20261030/check_rank_envelope.py --bound 10000 --out /tmp/rank-envelope.json
python -B experiments/beeping-density-swarm-20261030/verify_near_invariants.py --output /tmp/near-invariants.json
python -B experiments/beeping-density-swarm-20261030/check_regularity_review.py
```

The rank checker defaults to regenerating its neighboring saved result if
`--out` is omitted. The commands above and the complete driver avoid that
mutation. These tests substantiate implementations and finite examples; the
universal statements depend on the written proofs and their explicit
hypotheses. A tested contact range is not a uniform contraction theorem, and
finite variance measurements cannot establish the missing concentration.
