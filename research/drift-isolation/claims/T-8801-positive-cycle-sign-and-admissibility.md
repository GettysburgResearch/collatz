# T-8801 — Positive-cycle sign and admissibility criterion

Claim ID: T-8801  
Title: Exact reconstruction criterion for positive cycles of `T_a`  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801, L-8801  
Scope: every odd `a >= 3` and every nonempty finite binary word  
Related counterexample candidates: issue #26; no `K-####` candidate

## Statement

Let `w` be a nonempty binary word of length `L`, weight `s`, and correction
`B=B_a(w)`. Suppose a positive integer `n` follows `w` and returns after `L`
steps:

```text
T_a^L(n)=n.
```

Then `w` contains an odd step and

```text
(2^L-a^s)*n = B > 0.
```

In particular,

```text
2^L > a^s.
```

Conversely, define

```text
D = 2^L-a^s.
```

The word `w` reconstructs a positive cycle exactly when all of the following
hold:

1. `D>0`;
2. `D` divides `B`;
3. `n=B/D` is positive;
4. physical replay from `n` has parity word exactly `w`.

Under these conditions the replay endpoint is automatically `n`. The resulting
cycle may have a smaller primitive period when `w` is a repeated word.

## Definitions

A cycle here is for the shortcut map in D-8801. Rotations of one physical cycle
are not treated as distinct objects.

## Motivation

This gives a mandatory positive control for every cycle-exclusion or parity-word
pipeline. It also shows that the sign inequality is completely portable: the
format is universal and only the critical slope `L/s > log_2(a)` changes with
the multiplier.

## Proof or construction

By L-8801,

```text
2^L*T_a^L(n)=a^s*n+B.
```

If the orbit returns to `n`, then

```text
(2^L-a^s)*n=B.
```

A positive periodic orbit cannot have an all-zero parity word: repeated even
steps would give `T_a^L(n)=n/2^L<n`. Thus the word contains a `1`, and L-8801
gives `B>0`. Since `n>0`, the factor `2^L-a^s` must be positive.

For the converse, let `n=B/D>0` and assume physical replay yields `w`. Applying
L-8801 to that replay gives

```text
2^L*T_a^L(n)
 = a^s*n+B
 = a^s*n+(2^L-a^s)n
 = 2^L*n.
```

Therefore `T_a^L(n)=n`. The four listed conditions are also necessary by the
forward direction and integrality of `n`. **QED**

## Exact `a=5` controls

The criterion recovers the two issue-#26 nontrivial controls.

For `w=1110000`,

```text
L=7, s=3, B_5(w)=39,
2^7-5^3=3,
n=39/3=13,
```

and replay gives

```text
13 -> 33 -> 83 -> 208 -> 104 -> 52 -> 26 -> 13.
```

For `w=1100100`,

```text
L=7, s=3, B_5(w)=51,
2^7-5^3=3,
n=51/3=17,
```

and replay gives

```text
17 -> 43 -> 108 -> 54 -> 27 -> 68 -> 34 -> 17.
```

X-8801 also recovers the positive cycle containing `1` for `a=5`.

## Dependency audit

- L-8801 supplies the exact affine identity and positivity of the correction.
- D-8801 supplies the physical parity convention.

No claim about the completeness of any unbounded cycle search is used.

## Gap audit

- Divisibility and sign are not enough: parity admissibility must be replayed.
- A successful word may be an iterate of a shorter primitive word.
- Exhausting words only through a finite length never excludes longer cycles.
- The theorem identifies positive cycles; `2`-adic periodic points outside the
  positive integers are not accepted as counterexamples.

## Adversarial tests

X-8801 exhausts every binary word through length `14`, requires divisibility,
positivity, full parity replay, and exact return, and deduplicates rotations and
repetitions. In that finite scope it finds the usual `a=3` cycle and three
`a=5` cycles, including both required nontrivial controls.

## Remaining uncertainty

None known in the equivalence. The finite census is deliberately not promoted
to a global cycle classification.

## Suggested next attack

Search for same-phase **expanding** words using the complementary denominator
`a^s-2^L`, while requiring exact physical replay. This leads directly to
T-8802.
