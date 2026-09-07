# X-ATT-002 — source-tagged first exits and clearance forests

**Finite exact computation plus a separately proved analytic all-source,
all-future remainder. Not a full Collatz proof or a cofinal clearance
certificate.** Parent: PR105 @ `3c7fa4a0a2c5c48792c8efd5f5e90e94e44dab0f`.

Read [the proof](../../research/astra-tail-transport/repeated-spikes/PROOF.md),
especially ATT-102/103/104, before interpreting a small numerical bound.

## Reproduction

```bash
python -B experiments/X-ATT-002-repeated-spikes/run.py \
  --check experiments/X-ATT-002-repeated-spikes/results/canonical.json
python -B experiments/X-ATT-002-repeated-spikes/verify.py \
  experiments/X-ATT-002-repeated-spikes/results/canonical.json --self-test
python -O -B experiments/X-ATT-002-repeated-spikes/verify.py \
  experiments/X-ATT-002-repeated-spikes/results/canonical.json --self-test
```

Only an explicit `run.py --output PATH` writes data. Default verification
never rewrites the canonical report. Standard library only; explicit checks
remain active under optimized Python. Run from any working directory using
the appropriate file paths.

## Exact canonical scope

The protocol reconstructs complete rank balls at `2^8,2^12,...,2^32`, and
first-exit graphs in their quarter-unsafe subsets. It separately follows all
physical exits to attempt finite clearance at `2^24,2^28,2^32`. There is a
1024-return per-root protocol cap; a cycle or resource limit is a failure, not
an accepted source. The verifier independently bounds total expansion by two
million vertices and checks every resulting root label. These are resource
guards on the finite protocol, not universal Collatz bounds.

| Largest-cutoff check | Coverage |
|---|---:|
| All positive non-core sources with R<=2^32 | 163,168 |
| Quarter-unsafe initial sources | 78,828 |
| Actual reachable B-forest vertices | 111,763 |
| Forest vertices with R>2^32 | 32,935 |
| Maximum B hitting time | 52 |
| Maximum physical shortcut hitting time | 261 |
| Maximum ordinary value along those physical paths | 21,206,132,666 |

There are also 7 first-exit rows, 3 complete clearance rows, 42 finite-time
survival enclosures, 9 actual unsafe-shadow controls (up to 128 returns), low
rank-ball checks by exhaustive ordinary enumeration, and separate cycle/inflow
models. The three forests are nested computations; their counts must not be
added as numbers of distinct sources.

Finite source sums are enclosed with outward dyadic rounding at denominator
`2^128`. The omitted INITIAL rank tail is bounded by `12Y^(-3/2)` for all Y.
The resulting enclosure error is independent of how many subsequent returns
are taken. Aggregate graph/source transcripts are SHA-256 hashed after full
reconstruction; the report stores all declared protocol fields and constants.
The code and deterministic protocol reconstruct the complete source and edge
sets, not just the listed samples.

## What a successful check establishes

It proves that this finite set of source atoms is absorbed with the recorded
clocks and peaks. Combining that event with the written initial-tail and
source-truncation theorems yields an all-source bound valid at EVERY future
return after the displayed clock. The remaining source atoms are not declared
absorbed: their total original mass is an explicit positive error.

For the canonical input at Y=2^32:

- all future surviving mass after 52 returns is at most `12/2^48`;
- total new entry from outside the certified forest is at most that amount;
- the sum of late forest-occupation masses is at most `52*12/2^48`;
- all-time ever-spike mass above rank `449700062647992267556` is at most
  `12/2^48`, even at source-dependent shortcut clocks.

The cutoff in the last item is a squared ordinary peak bound, not an asserted
exact maximum rank. Unweighted mass is not a first rank moment. The unsafe
shadows certify mass-norm one on unit atoms, preventing an invalid
multiplication of the canonical small bound at every 52-return block.

## Implementation independence and tamper tests

`verify.py` does not import `run.py` or any parent/repository module. It uses a
component scan, all-component rank sublevels, literal physical modules,
reverse graph propagation, parity-bit lifting and Euclidean CRT. The generator
uses a different implementation for each of these interfaces. They share the
stated mathematical definitions and the canonical output schema.

Both were authored in the same session. This is not a second mathematical
review. Twelve distinct altered reports are deliberately resealed and rejected,
including zeroing the residual, shortening clocks, removing outside vertices,
changing the safe set, dropping coverage and promoting full closure.

Canonical semantic SHA-256:

`fe33d4ff6c6df3d5b3518f8f8129fad45274e8836b2df907cecb496fd1117f4b`.

No full repository integrity run, proof-assistant build, or large external
payload replay is included in this experiment's PASS.
