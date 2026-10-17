# Claim map — literature audit wave 9

All native IDs remain branch-qualified. No native status promotion is performed here.

| Native object | Literature / imported result | Mapping verdict | Main remaining obligation |
|---|---|---|---|
| `PR64/D-7401` six-branch minimal-word map | `LIT-KTHM-0056`; Dubickas–Mossinghoff approximate multiplication | **EXACT IDENTIFICATION** | Decide termination for the six source residues |
| `PR64/Q-7401` least-root decision | `LIT-KTHM-0057`; rational-base zero-digit gate | **STRICTLY SMALLER NEGATIVE TARGET** | Prove every positive orbit hits one multiple of `2^19` |
| `PR64/T-7403` finite rational nucleus rigidity | Dubickas 2009 Theorem 1; `LIT-KTHM-0055` | **STRONG METHOD NEIGHBOR / DIFFERENT SCOPE** | Native theorem concerns nonlinear rational sections; source classifies fixed linear observables |
| `PR66/T-7302` sliding linear-filter rigidity | `LIT-KTHM-0055` | **EXTERNAL STRUCTURAL SUPPORT** | Source says every bounded linear observable factors through digits; native theorem additionally classifies alphabet-preserving filters |
| `PR45/T-8404` complexity floor | Dubickas 2009 Theorem 3 | **KNOWN — EXACT COROLLARY** | Complexity alone does not force digit zero |
| `PR45/T-8405` no C-finite top boundary | Dubickas 2009 Theorem 2 | **KNOWN NEIGHBOR / NATIVE EXTENSION** | Unbounded nonlinear ordinary state remains possible |
| `PR57/Q-7601` six-branch bounded minima | `LIT-KTHM-0056/0057` | **SAME GLOBAL DECISION, SHARPER NEGATIVE FACE** | Bounded roots yield a candidate; one-letter zero hitting eliminates the chart |
| `PR67/L-8702...` centered `64->81` renewal | Dubickas 2006/2008/2009 centered-power papers | **HIGH-PRIORITY SOURCE MATCH PENDING FULL TEXT** | Compute exact `(81,64)` constants and equality language |
| `PR70` three-pulse all-repetition theorem | Matveev 2000; de Weger 1987; Chim 2025; Bugeaud 2002 | **SOURCE-DEPENDENT / EFFECTIVE PIPELINE** | Verify exact Matveev normalization, then reduce large bounds with real and p-adic lattices |
| `PR53/L-8201` arbitrary fixed-support caps | same logarithmic-form pipeline | **NATIVE ELIMINATION + NEXT PARAMETER BRIDGE** | Expose one repetition-only equation after pulse caps |
| `PADIC/T-9412...T-9422` periodic stack values | Väänänen–Wallisser 1991 | **RETAINED FINITE-DIMENSIONAL FIREWALL** | Does not decide ordinary least-root stabilization |

## Cross-program synthesis

The six-branch problem now has three nested formulations:

```text
full positive face:
  one positive minimal word confined to six digits forever;

exact least-root decision:
  m_n bounded versus m_n -> infinity;

strictly smaller negative target:
  every positive ceiling orbit emits digit 0 once
  <=> every orbit hits a multiple of 2^19.
```

The final line is sufficient because zero is not one of the six physical digits. It is much weaker than full rational-base normality or occurrence of all `2^19` digits.

The cycle/pulse program has a separate effective ladder:

```text
sparse resultant caps pulse coordinates
 -> one repetition-only exponential equation
 -> Matveev real logarithmic bound
 -> p-adic logarithmic bound when available
 -> de Weger/LLL reduction
 -> exact finite replay.
```

No source in this wave supplies an ordinary Collatz counterexample.