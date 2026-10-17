# O-8302 — A critical run-level repair passes the certified factor product and is not integral

Claim ID: `O-8302`  
Status: `EMPIRICAL / EXACT FINITE-CIRCUIT AUDIT`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8303`, `L-8304`, `L-8305`  
Scope: one frozen compressed word  
Related counterexample candidates: none

## Frozen circuit

Use the critical run word

```text
L(236,838,463,643,
  267,629,447,755)
```

from `L-8304`. Generate its first 80 pairwise-disjoint unequal neighboring run pairs. A deterministic exact four-list join selects 46 transpositions, at run-word positions

```text
7,33,42,59,77,103,111,120,129,146,155,164,
181,190,207,216,224,233,242,259,277,285,294,
303,311,337,346,364,372,398,407,450,477,485,
503,511,537,546,555,563,572,590,607,616,642,659.
```

Every transposition preserves the complete `(A,k)` pair and has the monomial delta of `L-8305`.

## Exact proper-factor repair

Let

```text
M=
7*191*281*28,591*136,398,329
 =1,465,129,870,107,858,983.
```

The base numerator is

```text
C_base mod M
 =1,274,355,650,519,809,298.
```

The 46 exact deltas give

```text
boxed:
C_modified=0 mod M.                                      (1)
```

Factor seven is automatic for every word at the frozen shape by `L-8305`; the solver works modulo `M/7` and verifies `(1)` modulo the full product afterward.

## Directed real rejection

A 170-digit outward-rounded affine computation gives

```text
1567441266429151808728248.4154867702110835202001656648550663160616228665661694978049322093823618472370849137924106373341918760540178859278353010050594027929720000706283796
< C_modified/(2^A-3^k) <
1567441266429151808728248.4154867702110835202001656648550663160616228665661694978049322093823618472370849137924106373341918760540178859278353010050635719007615146833646836.
```

The interval width is below

```text
4.17e-123,
```

and its distance from the nearest integer exceeds

```text
boxed:
0.4154867702110835202001656649.                           (2)
```

Thus the word is not an integral cycle.

## Independent quotient-cylinder rejection

Lifting `(1)` one prime-power digit gives quotient residues

```text
N mod 7           =6,
N mod 191         =151,
N mod 281         =261,
N mod 28,591      =10,636,
N mod 136,398,329 =105,593,704.
```

CRT gives

```text
boxed:
N congruent
1,100,378,267,524,741,582
mod M.                                                   (3)
```

The sole real floor and ceiling have residues

```text
1,377,491,661,032,945,358,
1,377,491,661,032,945,359
mod M,
```

neither of which equals `(3)`. This independently excludes integrality using the same finite rational coefficients.

## Interpretation

This circuit is cleaner than the symbol-level repairs:

- its word is compressed twice by the Euclidean algorithm;
- every modification is a macro-run transposition;
- every delta is one signed `{2,3,7}`-unit;
- structural factor seven is separated from genuine repair factors;
- and the ordinary quotient is tested, not only numerator divisibility.

The object is nevertheless decisively rejected and receives no `K-####` identifier.

## Replay

```bash
g++ -O3 -std=c++17 \
  experiments/X-8303-critical-run-repair/solve.cpp \
  -o /tmp/x8303-solve
/tmp/x8303-solve

python3 -B experiments/X-8303-critical-run-repair/run.py \
  --check-results \
  experiments/X-8303-critical-run-repair/results/canonical.json

python3 -B experiments/X-8303-critical-run-repair/verify.py \
  experiments/X-8303-critical-run-repair/results/canonical.json
```

Canonical JSON SHA-256:

```text
d2a85dbd403b5d3b1a899cc42502d31f3cf7c43c4407cadbd0fa0e90ed31a585
```

## Gap audit

- `M` is only a proper divisor of the complete denominator.
- The selected word misses the nearest integer by a large certified margin.
- The quotient cylinder uses only the five certified factors.
- No prime-square-compatible repair, positive cycle, infinite path, or Collatz counterexample is claimed.

## Suggested next attack

Replace the 80 flat binary choices by the full Farey hierarchy. Its block commutators remain monomials by `L-8305` and supply enough independent entropy to target the prime-square quotient cylinder rather than repeat another proper-factor solve.
