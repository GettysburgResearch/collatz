# O-8303 — A critical run word aligns three ordinary quotient digits

Claim ID: `O-8303`  
Title: One rotated trillion-scale paired-chart word matches its real floor modulo `7`, `191`, and `281`  
Status: `EMPIRICAL / EXACT COMPRESSED-CIRCUIT AUDIT`  
Authoring agent: `gpt56-cycle-02`  
Created: 2026-07-23  
Dependencies: `L-8303`, `L-8304`, `L-8305`, `L-8306`, `X-8304`  
Scope: one frozen repaired critical run word and one cyclic rotation  
Related counterexample candidates: none; the word is rigorously nonintegral

## Frozen word

Use the critical run parameters

```text
run length  = 267,629,447,755,
run weight  = 236,838,463,643,
```

from `L-8304`. They expand to the PR #45 cycle parameters

```text
k=3,149,971,404,836,
A=4,992,586,555,009.
```

Generate the first 136 pairwise-disjoint unequal adjacent run sites. Swap the 65 sites with indices

```text
0,1,2,3,11,13,14,15,16,17,18,20,22,23,24,27,28,29,32,35,36,
38,40,41,43,44,47,49,50,52,53,54,55,59,60,62,64,68,69,71,73,
75,79,80,83,89,92,93,94,96,97,100,101,102,105,108,109,120,
121,123,125,129,130,132,134.
```

Their run positions are frozen in `X-8304`.

## Initial Hensel alignment

For each prime

```text
7, 191, 281, 28,591, 136,398,329,
```

exact arithmetic gives

```text
p | C,
p | D,
p^2 does not divide D.
```

The first quotient-cylinder residues are

```text
q_7           =          0,
q_191         =        138,
q_281         =        226,
q_28,591      =      5,002,
q_136,398,329 = 10,629,073.
```

A 180-digit outward-rounded evaluation gives

```text
1567441266440951895435533.873676569542272619403132162187203755...
```

with interval width below `4.2e-133`. Its floor is

```text
N_0=1,567,441,266,440,951,895,435,533.
```

Exactly

```text
N_0 mod 7   = q_7,
N_0 mod 191 = q_191.
```

Thus this word passes two quotient layers in addition to all five first-level numerator divisibilities.

## Rotation by `928,986` runs

Rotate the compressed run word left by

```text
928,986
```

run symbols. `L-8306` transports the real fixed point and all quotient digits by the same exact affine prefix map.

The rotated real value lies in the directed interval

```text
1493473415249495237990964.352130158632547798338992822322325535...
```

of width below `4.0e-133`. Its floor is

```text
N_*=1,493,473,415,249,495,237,990,964.
```

The transported quotient residues are

```text
q_7           =          0,
q_191         =        170,
q_281         =        114,
q_28,591      =     27,473,
q_136,398,329 = 53,413,494.
```

The real floor satisfies

```text
N_* mod 7   =   0,
N_* mod 191 = 170,
N_* mod 281 = 114.
```

Therefore

\[
 \boxed{
 C_{\mathrm{rot}}
 \equiv N_*D
 \pmod{7^2\,191^2\,281^2}}
\]

while the already-certified first powers of the two remaining primes also divide both `C_rot` and `D`.

## Decisive rejection

The real fractional part is strictly between zero and one, beginning

```text
0.3521301586325477983389928223...
```

so the rotated word is not integral. It also fails the next quotient digits:

```text
N_* mod 28,591      =  4,976 != 27,473,
N_* mod 136,398,329 = 97,285,325 != 53,413,494.
```

No `K-83xx` candidate is assigned.

## Significance

The earlier proper-factor construction stopped at

```text
p | C and p | D.
```

This packet reaches the genuinely stronger ordinary condition

```text
C congruent to N D modulo p^2
```

for three independent primes, with `N` selected by a rigorous real interval rather than chosen after the modular computation.

It demonstrates that cyclic rotation is an effective Hensel coordinate, and that the chart/mechanical circuit can align multiple ordinary quotient digits without expanding the trillion-symbol valuation word.

## Gap audit

- Three quotient digits are still a negligible part of the complete denominator.
- The word is explicitly nonintegral.
- The two remaining displayed primes fail at their second layers.
- No claim is made about unlisted factors of `D`.
- Partial Hensel alignment does not imply proximity to a cycle in any uniform global metric.

## Replay

See `experiments/X-8304-hensel-rotation/`.
