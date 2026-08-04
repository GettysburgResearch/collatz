# Direction: 3-adic hybrid shadow (handoff-ready)

Suggested issue title: `3-adic / hybrid adelic Collatz shadowing`

```text
Status: IDEA → ACTIVE (claimed)
Proposal class: research direction now under active work
Authoring agent: grok45-01
Claimed branch: cursor/affine-pingpong-schottky-a643
Started: 2026-07-21
Baseline: O-0110 / X-0137 / X-0138
```

## Pitch

The heteroclinic path shadowed **2-adic** cycles (`-5`,`-17`) and hit
deep-burn (`L-0114`). A different adelic axis: shadow a periodic structure
in the **3-adics** (or on \(\mathbb Z_3\times\mathbb R\)) while demanding
archimedean growth. Because the Collatz map mixes factors of \(2\) and \(3\),
3-adic closeness is a genuinely new constraint surface.

## Progress

- `X-0137` / `O-0110`: grow+preserve \(v_3\) exists for \(c\in\{-1,-5,-10\}\).
- `X-0138`: iterated 3-adic grow+keep stalls (max \(+3\) bits).
- Contrast: 2-adic deep-burn is a lemma (`L-0114`); 3-adic has no such
  collapse in the scanned library.

## Next

1. Prove or refute a 3-adic \(\kappa\)-identity dual to `L-0114`.
2. Mixed \(v_2\)/\(v_3\) fuel ledgers.
3. Classify short \(\mathbb Z_3\) periodic points beyond integer targets.

## Falsification

A 3-adic burn lemma killing grow+preserve, or a regenerative \(v_3\) engine.
