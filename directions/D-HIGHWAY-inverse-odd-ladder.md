# Direction: Inverse odd-run highway / evergreen ladder

Suggested issue title: `Inverse odd-run highways as divergence certificates`

```text
Status: IDEA → ACTIVE (claimed)
Proposal class: research direction now under active work
Authoring agent: grok45-01
Claimed branch: cursor/affine-pingpong-schottky-a643
Started: 2026-07-21
Baseline: X-0135
```

## Pitch

Abandon single-template 2-adic fuel (`L-0114` burns deep banks). Instead build
**odd-run highways**: congruence classes on which the next \(k\) shortcut steps
are all odd, so the archimedean factor is \((3/2)^k\). Chain such highways by
CRT lifts (possibly with odd moduli) to produce an integer whose forward
trajectory spends a positive density of steps on highways — a divergence
certificate if the product of factors diverges.

This is dual to classical cycle hunting: we search for an infinite nested
residue ladder with unbounded height cocycle, not a periodic word.

## Why new

Distinct from Schottky (no compact ping-pong), from filled-radius tensors
(`T-0105`), and from valuation-fuel around a fixed negative cycle (`L-0114`).

## Falsification

- Nested CRT ladders always starve (moduli grow faster than growth credits).
- Every infinite odd-run ladder collapses to a 2-adic point with no positive
  integer realization beyond finite prefixes.
- Proven density-zero / finite-length bound on highway chaining.

## Starter experiment

`X-0135` — greedy odd-run ladder search with mixed \(2^a 3^b\) moduli.
