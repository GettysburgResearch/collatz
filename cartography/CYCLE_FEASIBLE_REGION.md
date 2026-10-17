# Positive-cycle feasible region after pass 5

**Agent:** `gpt56-cartographer-01`  
**Classification:** exact cartography synthesis from proposed/source-exact inputs  
**Full-objective role:** removes globally impossible search regions and isolates the actual scale of any finite counterexample

## 1. Coordinates

Let an accelerated valuation word have:

```text
k = number of odd states,
s = number of valuations different from 2,
R = k-s = number of neutral valuations 2,
B = sum of the s non-neutral valuations,
A = total valuation sum = B+2R.
```

Every non-neutral valuation is a positive integer different from two, hence

```text
B>=s
```

and therefore

```text
A=B+2(k-s)>=2k-s.                         (1)
```

## 2. Least-state product window

For a nontrivial positive cycle, every odd state is at least seven. The exact cycle product identity gives

```text
2^A / 3^k
 = product_j (1+1/(3n_j))
 <= (22/21)^k.
```

Equivalently,

```text
2^A 7^k <= 22^k.                         (2)
```

Using `(1)` in `(2)` yields

```text
2^(2k-s) 7^k <=22^k,
```

or the exact length-support inequality

```text
boxed: 14^k <=11^k 2^s.                 (3)
```

Thus every positive cycle satisfies

```text
s >= ceil(k log_2(14/11)).               (4)
```

No floating-point computation is needed to use `(3)`.

## 3. Combining with the proposed 50,000-state floor

PR #45 `T-8401` proposes, with an exact computer-assisted first-drop packet, that no nontrivial positive accelerated cycle has at most 50,000 odd states. Conditional on that proposed theorem,

```text
k>=50001.
```

The exact integer threshold at `k=50001` is

```text
11^50001 2^17396 < 14^50001
                    <=11^50001 2^17397.
```

Therefore:

```text
boxed:
conditional on proposed T-8401,
every nontrivial positive cycle has s>=17397.
```

The certificate is frozen in:

- `cartography/check_cycle_feasible_region.py`;
- `cartography/cycle-feasible-region.json`.

Semantic SHA-256:

```text
694813ec58932ca4c6e13edd7dcb904e02d8f59e32905a0435ed3a2a3e40051a
```

## 4. Consequence for the sparse-support packets

The repository has several distinct evidence levels:

| Support layer | Source | Standing at cutoff |
|---:|---|---|
| 5–6 | PR #34 | proposed complete exclusions |
| 7–11 | PR #47 | proposed exact finite certificates |
| 7–15 | PR #42 `T-8603` | proposed theorem packet |
| 16 | PR #42 `X-8610` | complete source-exact necklace computation; zero formal matches; independent implementation pending |
| 17 | PR #42 `X-8611` | complete source-exact necklace computation; zero formal matches; independent implementation pending |

The support-16 cell formerly described as the first open sparse layer is no longer the **global** positive-cycle frontier under the combined proposed chain. It remains a useful verifier and method-development frontier, but it lies far below the conditional support floor `17397` forced by `k>50000` plus `(3)`.

This distinction prevents a common cartography error:

```text
first unproved cell inside one isolated parameterization
!=
first globally feasible counterexample cell.
```

## 5. Actual cycle offense after the reduction

A globally relevant finite-cycle construction must now satisfy all of the following:

1. odd-state length beyond the proposed 50,000 floor;
2. defect support at least 17,397 under the combined proposed chain;
3. primitive-necklace normalization;
4. full-denominator compatibility across every prime power;
5. exact positivity and valuation replay;
6. no reduction to a fixed finite pulse cone, bounded block library, proper denominator factor, or near-integer quotient.

The most relevant constructive interfaces are therefore:

```text
critical mechanical / fixed-weight straight-line program
 -> quotient-Hensel lifting at every prime power
 -> normalized half-joins and block-carry decoding
 -> commutator or sparse-resultant elimination of fixed subfamilies
 -> full exponential-circuit equality
 -> independent physical replay.
```

## 6. Atomic decision

`ACL-N084` asks an independent reviewer to reconstruct both inputs and this exact bridge. A positive outcome certifies the conditional global region

```text
k>=50001,
s>=17397.
```

A failure must identify the first invalid source theorem or algebraic implication. A divisor hit must be converted immediately into a full positive cycle certificate.
