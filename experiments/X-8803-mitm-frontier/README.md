# X-8803 — Exact meet-in-the-middle depth frontier

Experiment ID: X-8803  
Agent: `gpt56-drift-01`  
Issue: #26  
Classification: **EXACT FINITE COMPUTATION**

## Research question

What is the exact least positive root whose base-`5/4` bottom word remains in
`{0,1}` for fifty digits?

A direct frontier has `2^50` residues. L-8804 factors it into two exact
`2^25` frontiers and reduces minimization to cyclic successor queries after one
modular translation.

## Build and replay

```bash
g++ -O3 -std=c++17 -Wall -Wextra -Wpedantic \
  experiments/X-8803-mitm-frontier/run.cpp \
  -o /tmp/x8803

/tmp/x8803 50 \
  > /tmp/x8803.json

diff -u \
  experiments/X-8803-mitm-frontier/results/canonical.json \
  /tmp/x8803.json
```

No third-party library is required.

## Frozen scope

```text
target depth:          50
split:                 25+25
left frontier size:    33,554,432
right frontier size:   33,554,432
integer arithmetic:    unsigned 64-bit, checked before final product
```

The implementation:

1. generates exact survivor residues and endpoints at each split depth;
2. checks the modular inverse of `5^25 modulo 4^25`;
3. checks injectivity of the transformed right frontier;
4. performs exact cyclic successor minimization from L-8804;
5. excludes the all-zero root explicitly;
6. physically replays the resulting root through the first forbidden digit.

## Canonical result

```text
least positive root X: 4538335001132531
physical seed A=X-1:   4538335001132530
survival depth:        50
first forbidden digit: 3
```

The full prefix and exit state are frozen in `results/canonical.json`.

## Independent finite audit

A separate direct-frontier implementation was compared with the
meet-in-the-middle result at every depth `1..20`. All minima agreed exactly.
This small-depth audit is not needed for L-8804's proof, but is designed to
catch orientation, wraparound, and zero-root errors in the implementation.

## Resource profile of the frozen run

On the authoring container, the depth-50 replay used approximately:

```text
elapsed wall time: 25.4 seconds
peak resident set: 1.31 GB
```

These figures are informational and environment-dependent.

## Digests

```text
run.cpp:
5fdd467f286e891a33592b412e5b46c356addd936c1391f396f3b0ef51cc3b0d

canonical.json:
c3f40c098cd9fd16255a8984e750e8167c443f724742ee2c3088bade1ae66a6b
```

## Interpretation boundary

The result proves a sharp finite theorem: every smaller positive root exits
before depth 50, and the displayed root survives exactly 50. It does not prove
that every root eventually exits, and no growth law is extrapolated from the
finite minima.
