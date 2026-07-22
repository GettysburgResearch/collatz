# Drift isolation at `5x+1`

Agent: `gpt56-drift-01`  
Issue: #26  
Branch: `agent/gpt56-drift-01/26-5x1-portability`  
Packet status: **PARTIAL**  
Claim namespace: `88xx`

## Headline

The `5x+1` shortcut map

```text
T_5(n) = n/2       when n is even,
         (5n+1)/2  when n is odd
```

contains an exact two-phase expanding chart:

```text
T_5^2(4q-1) = 5q-1,   parity word 10,
T_5^2(4q-2) = 5q-2,   parity word 01.
```

Thus the positive-drift control universe has a genuine `4 -> 5` same-phase
amplifier, not merely a heuristic analogue. It is simpler than the active
`64 -> 81` constructions and gives a clean stress test for every proposed
ordinary-section, completion-height, repetition, automata, and symbolic
certificate method.

The first portability result is unexpectedly discriminating:

> The ordinary-section repetition/height squeeze survives intact in the
> positive-drift `5x+1` chart.

For a hypothetical positive ordinary integer `A` that remains forever in this
two-phase chart, write its phase directive as `d_j in {-2,-1}` and normalize

```text
eps_j = d_j + 2 in {0,1}.
```

Then in `Z_2`,

```text
A + 2 = (1/5) * sum_(j>=0) eps_j * (4/5)^j.
```

If two length-`ell` factors of `eps` begin at `r<t`, then

```text
4^(t+ell) < (A+2) * 5^t
```

and therefore

```text
ell < (log_4(5)-1)t + log_4(A+2).
```

Consequently every such nontrivial ordinary survivor code has lower factor
complexity slope at least

```text
1/(log_4(5)-1) = 6.212567439010779752...
```

This is smaller than the `64 -> 81` constant
`17.654847577085155652...`, but it is still far above the Sturmian slope `1`.
Low-complexity exclusion therefore persists in a map with positive fair-parity
drift. That makes the exclusion primarily **format-driven**; its quantitative
strength is amplified by near-criticality through the exact constant

```text
delta(U,V) = log_U(V)-1.
```

## Portability matrix

| Repository mechanism | `ax+1` verdict | Exact discriminator | Meaning |
|---|---|---|---|
| Affine parity-word formula | **HOLDS-VERBATIM** for every odd `a` | none | Pure branch algebra |
| Positive-cycle sign criterion | **HOLDS-VERBATIM** for every odd `a` | `2^L-a^s` | Recovers both nontrivial `5x+1` cycles exactly |
| One-step `2`-adic fuel loss on a shared branch | **HOLDS-VERBATIM** for every odd `a` | oddness of `a` | Format-driven precision drain |
| Direct `T_5^2` same-phase amplifier | **EXISTS** | `5-4=1` | Exact phases `-1,-2`; genuine positive-drift control |
| Literal direct length-6, weight-4 phase port | **BREAKS** | `5^4-2^6=561` divides none of the 15 corrections | Arithmetic chart-realization failure, not a convergence theorem |
| Repetition/height squeeze | **HOLDS** on the actual `4 -> 5` chart | `delta=log_4(5)-1` | Format-driven theorem with drift-sensitive strength |
| Fair-parity drift model | **CHANGES SIGN** | `(1/2)log_2(a)-1` | Negative at `a=3`, positive at `a=5`; model statement only |
| Divergence of the `T_5` orbit of `7` | **UNRESOLVED** | infinite behavior | One million exact steps are evidence, never proof |

## Exact finite controls

Experiment `X-8801` supplies:

- 12,288 exact affine-formula checks for `a in {3,5,7,9}`;
- 65,024 exact one-step fuel-loss checks;
- 200,000 exact checks of the two `4 -> 5` phase identities;
- an exhaustive direct fixed-phase census for the relevant small block shapes;
- cycle reconstruction through parity-word length `14`;
- exact recovery of the `5x+1` cycles
  `1 -> 3 -> 8 -> 4 -> 2 -> 1`,
  `13 -> 33 -> 83 -> 208 -> 104 -> 52 -> 26 -> 13`, and
  `17 -> 43 -> 108 -> 54 -> 27 -> 68 -> 34 -> 17`;
- a streaming exact ledger for the first `10^6` shortcut steps of seed `7`.

For that finite prefix, the orbit never returns to or below `7`, ends at a
48,521-decimal-digit value, and has nearly balanced parity counts. These are
exact finite observations. They do **not** prove divergence or exclude a later
cycle.

## Claims

- `D-8801`: generalized shortcut and expanding-chart definitions.
- `L-8801`: universal affine parity-word formula.
- `T-8801`: positive-cycle sign and admissibility criterion.
- `L-8802`: exact one-step `2`-adic fuel loss.
- `T-8802`: exact `5x+1` `4 -> 5` chart and its completion formula.
- `T-8803`: parameterized repetition rigidity and the `5x+1` complexity bound.
- `O-8801`: fair-parity drift threshold, explicitly model-level.

All theorem-level entries are **PROPOSED** pending independent reconstruction.

## Strategic consequence

A certificate format should not be trusted merely because it excludes simple
`3x+1` constructions. The `4 -> 5` control chart shows that ordinary-section
completion and low-complexity obstructions can remain severe even when the
underlying macro map expands and the fair-parity drift is positive.

The next high-upside attack is therefore not another isolated numerical orbit.
It is a **connector/replenishment theorem** for the exact phases `-1,-2`:

1. construct a finite connector family that repeatedly replenishes the dyadic
   precision consumed by the `4 -> 5` amplifier; or
2. prove that every finite-state connector family has a quantitative net
   precision deficit.

A positive result would be the cleanest certificate-format success currently
available in the repository. A negative result would identify a genuinely
format-level obstruction that must be bypassed before analogous `3x+1`
amplifiers can close.

## Claim boundary

This packet claims no divergent positive `5x+1` seed, no positive-integer
Collatz counterexample, and no resolution of either conjecture. It establishes
exact control identities and conditional rigidity theorems designed to expose
where existing methods depend on drift, arithmetic realization, or certificate
format.
