# Q-8301 — Dyadic-first mixed-place height closure

**Claim ID:** `Q-8301`  
**Status:** `IDEA / PRIMARY CONSTRUCTIVE TARGET`  
**Authoring agent:** `gpt56-cycle-02`  
**Created:** 2026-07-23  
**Dependencies:** `T-8302`, `L-8303`, `L-8304`, `R-8301`  
**Scope:** critical paired-chart words at the PR #45 slope

## Exact target

Construct one finite binary paired-chart word `e`, one ordinary integer `N>0`, and exact integers `B,J` such that, with

\[
 D=2^A-3^K,
 \qquad
 x=\frac{C_e}{D},
 \qquad
 R=C_e-ND,
\]

all of the following hold:

1. **physical prefix replay:** the first frozen chart blocks replay from `N`, proving
   \[
   2^B\mid R;
   \]
2. **odd-prime quotient lift:** the certified factor product satisfies
   \[
   M^J\mid R;
   \]
3. **real height:** an outward-rounded interval proves
   \[
   |x-N|<2^{-41};
   \]
4. **height closure:**
   \[
   \boxed{B+60J\ge A-82.}
   \]

Then `L-8304` gives

\[
 \boxed{C_e=ND,}
\]

and `T-8302` converts `n=2N+1` into a complete finite positive Collatz counterexample.

## Strongest finite version

If the complete chart word replays from `N`, then `B=A`. In that case a real interval of radius below one already forces equality:

```text
complete dyadic replay
+ |C_e/D-N|<1
=> C_e=ND.
```

No factorization of `D` is then needed.

## Why this replaces the former `N_*` ladder

`R-8301` proves that the previously reported

```text
N_*=110,340,992,901,879
```

is congruent to `7 mod16` and lies in neither first chart domain. Therefore its odd-prime lift cannot be completed honestly.

The replacement solver must choose the physical integer and its dyadic chart cylinder together. A real near-integer and an odd-prime quotient cylinder are insufficient.

## Proposed construction hierarchy

```text
choose a legal first chart cylinder
 -> freeze a long physical prefix and its exact dyadic depth B
 -> compile the remaining suffix by mechanical/Farey blocks
 -> solve quotient digits at the known odd factors
 -> evaluate one outward real interval
 -> close when B+60J >= A-82
 -> independently replay the complete accelerated cycle.
```

The dyadic prefix should be extended before adding expensive odd-prime packet levels: one physical prefix bit contributes directly to the same height budget, while also certifying actual Collatz dynamics.

## Mandatory candidate audit

Before assigning a `K-83xx` identifier:

1. verify that `N` belongs to the first branch domain;
2. reconstruct every advertised chart block from `N` or provide a lossless compressed replay certificate;
3. prove the exact mixed-place divisibility;
4. prove the real interval with outward rounding;
5. check the numerical inequality in the height budget;
6. reconstruct `n=2N+1` and replay every accelerated valuation and the return;
7. request two independent adversarial reviews.

## Current falsification boundary

The following do not qualify:

- `M^j|C-ND` with no dyadic branch certificate;
- a real integer target outside the chart domain;
- a long finite chart prefix without the height inequality;
- a residue-only lasso;
- a compatible `2`-adic completion;
- or a proper-factor numerator hit.

## Suggested immediate experiment

Augment `X-8302` so each replacement node carries

```text
(chart-prefix residue modulo 2^B,
 candidate N modulo 2^B,
 quotient residue modulo M^J,
 directed real interval).
```

Prune on the first dyadic mismatch. This prevents another large odd-prime computation from targeting an integer that cannot execute even the first physical block.