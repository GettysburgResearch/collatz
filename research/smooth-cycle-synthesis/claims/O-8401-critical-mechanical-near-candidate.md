# O-8401 — Critical mechanical near-candidate is not integral

Claim ID: `O-8401`  
Title: A trillion-step balanced valuation word can pass a 61-bit denominator component and still miss integrality by a certified real margin  
Status: `EMPIRICAL / EXACT FINITE-CIRCUIT AUDIT`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Dependencies: `L-8401`, `L-8402`, `L-8403`  
Scope: one frozen compressed valuation word  
Related counterexample candidates: none

## Frozen global parameters

```text
k=3,149,971,404,836,
A=4,992,586,555,009,
p=A-k=1,842,615,150,173.
```

The base valuation word is

```text
a_i=1+epsilon_i,
epsilon=L(p,k)_i,
```

where `L(p,k)` is the lower mechanical word of `L-8403`.

The pair `(A,k)` is a source-admissible upper approximation in the critical
window used by the cycle program.  This file does not promote the numerical
source bound; it only freezes the pair used by the experiment.

## Certified denominator component

The following primes satisfy

```text
2^A=3^k mod prime:
```

```text
7,
191,
281,
28,591,
136,398,329.
```

Their product is

```text
M=1,465,129,870,107,858,983.
```

Hence

```text
M | D(k,A)=2^A-3^k.                                   (1)
```

The factor search that located them is a bounded scanner through `10^9`.
`X-8401` re-verifies every displayed factor independently; completeness of the
scan is not a theorem dependency.

## Base residue and local repair

The Euclidean monoid compiler gives

```text
C_base mod M=655,756,015,106,852,524.                 (2)
```

Generate the first 80 pairwise-disjoint positions at which the mechanical word
has an adjacent `01` or `10`.  A four-list exact modular join selects the masks

```text
first 40 sites : 679,923,852,302,
last  40 sites : 1,092,615,932,587.                   (3)
```

They choose 43 swaps, at positions

```text
2,4,6,23,30,35,39,42,44,47,54,59,61,64,71,
78,80,83,85,92,95,97,102,107,112,117,121,138,
141,143,145,148,150,158,165,167,174,177,179,
182,184,186,189.
```

Every swap is replayed through `L-8402/(5)`.  Their exact sum gives

```text
boxed:
C_modified=0 mod M.                                   (4)
```

The word keeps its length and total valuation.  Its cyclic local-minimum count
is exactly

```text
1,307,356,254,653.                                    (5)
```

Thus this is not a toy short-word failure: it lies well beyond the current
minimum-count scale and passes a nontrivial factor component.

## Directed real fixed-point audit

Let the normalized affine action be

```text
n -> r n+t,
r=3^k/2^A,
t=C_modified/2^A.
```

The unique real fixed point is `t/(1-r)=C_modified/D`.  A 120-digit directed
interval monoid, including outward rounding at every multiplication and
addition, gives

```text
1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085257269769107803891195190
< C_modified/D <
1791361447298439130709020.99752835390985101078597115625463997678316699077019108974634764751200085455151399874064825798230.
```

The interval width is below `2e-72`.  In particular,

```text
boxed:
distance(C_modified/D, Z)>0.002471646090148989.       (6)
```

Therefore the frozen word does **not** define an integral cycle.

## Interpretation

This record demonstrates both sides of the constructive architecture:

```text
positive:
  trillion-step SLP,
  exact local-minimum count,
  61-bit certified denominator divisibility,
  43 proof-carrying local repairs;

negative:
  the same completion-safe real coordinate excludes integrality decisively.
```

A larger gcd or a closer real fixed point would still not be sufficient.  A
counterexample requires the complete identity `C=nD` and exact orbit replay.

## Dependency audit

- `L-8402` supplies every local residue delta.
- `L-8403` supplies the base word in residue and directed interval monoids.
- No unpublished full factorization is assumed.
- No floating-point equality is used: the final interval uses directed Decimal
  rounding and lies strictly between consecutive integers.

## Gap audit

- Only a proper divisor component of `D` is controlled.
- The selected word is refuted, not a counterexample candidate.
- The bounded factor scan says nothing about the remaining factor spectrum.
- The result does not exclude other block-replacement circuits at the same
  `(A,k)`.

## Replay

```bash
python3 -B experiments/X-8401-critical-mechanical-cycle/run.py \
  --check-results \
  experiments/X-8401-critical-mechanical-cycle/results/canonical.json
```

Canonical SHA-256:

```text
7f9c69b95598326f9593ad5fb59f222e0c2355c31ac9c28ac49b882d041171b6
```