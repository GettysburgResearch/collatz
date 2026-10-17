# LIT-KTHM-0010 — Mahler Z-numbers and the FLP real range obstruction

**Sources:** [@Mahler1968], [@FlattoLagariasPollington1995]; recent conditional context [@Strauch2022]
**Inspection:** Mahler official reprint record; FLP full text
**Proof status:** BLACK BOX statements with exact scope

## Mahler's problem

A classical Z-number is a positive real number `xi` such that

```text
0 ≤ {xi (3/2)^n} < 1/2
```

for every `n≥0`. Mahler conjectured that no Z-numbers exist and proved strong countability/growth restrictions. The existence question remains open in the located literature. Strauch gives a recent conditional distribution theorem for any hypothetical Z-number, not an existence or nonexistence theorem.

## Flatto–Lagarias–Pollington theorem

Let `p>q≥2` be coprime integers. For every positive real `xi`,

```text
limsup_{n→∞} {xi(p/q)^n}
 - liminf_{n→∞} {xi(p/q)^n}  ≥ 1/p.               (1)
```

Equivalently, no Euclidean interval of length `<1/p` can contain all fractional parts `{xi(p/q)^n}`.

FLP also formulate generalized Z-number sets `Z_(p/q)(s,s+t)` and analyze them through symbolic dynamics of an integer map and a real linear mod-one transformation.

## Native mapping

`CLAUDE/Q-0002` is legitimately called a **2-adic analogue**: both problems constrain every iterate of a rational expansion by a small digit/window condition. It is not the same problem and no equivalence was located.

## Non-applications

- Equation (1) is about Euclidean limsup/liminf and interval width.
- It does not compare 2-adic Haar measures.
- It does not imply that a 2-adic digit set of measure `1/32` is possible or impossible for ratio `81/64`.
- The numerical comparison between `1/32` and `1/81` is not an FLP threshold theorem.
