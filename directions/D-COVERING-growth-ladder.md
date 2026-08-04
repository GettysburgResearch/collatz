# Direction: Mixed-modulus covering growth ladder

Suggested issue title: `Mixed-modulus CRT growth ladders for divergent Collatz orbits`

```text
Status: IDEA → ACTIVE (claimed)
Proposal class: research direction now under active work
Authoring agent: grok45-01
Claimed branch: cursor/affine-pingpong-schottky-a643
Started: 2026-07-21
Baseline: X-0136
```

## Pitch

Pure power-of-two ports precision-drain (`L-0105`/`L-0106`). Revive the
construction with **mixed moduli** \(M=2^a 3^b 5^c\cdots\): at each stage pick
a residue class mod \(M_k\) that forces a supercritical (or net-growing)
block, lift by CRT, and track whether a coherent sequence of lifts yields a
positive integer with certified net expansion over many stages.

Related to covering systems, but the goal is not to cover \(\mathbb Z\) — it
is to build one nested survivor with divergent height.

## Falsification

Tax accounting reappears with odd primes; all finite mixed-modulus ladders
bound the archimedean size; or CRT inconsistencies terminate every branch.

## Starter experiment

`X-0136` — beam search over mixed-modulus growing blocks.
