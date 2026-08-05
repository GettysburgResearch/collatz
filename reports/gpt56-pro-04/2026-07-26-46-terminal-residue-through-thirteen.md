# Continuation report — terminal-residue sieve closes fixed-weight pulse grammars through thirteen A letters

**Agent:** `gpt56-pro-04` (`GPT-5.6 Pro`)  
**Date:** 2026-07-26  
**Host branch:** `agent/gpt56-pro-04/46-integer-first-counterexample-offense`  
**Issue:** #46  
**Status:** proposed theorem packet; no counterexample or `K-####` object

## 1. Starting point

The preceding packet proved an all-repetition theorem for every fixed-weight
negative-three pulse grammar with at most five unpulsed letters. The first open
aligned layer was `a=6`.

This continuation does not enumerate longer macro periods. It derives a new
cycle-minimum residue law that removes every packet in a large infinite region
at once, then closes four finite exceptional alphabets exactly.

## 2. New global interface `L-9610`

For a macro with `a` letters `A` and `b` letters `B`, put

```text
Q=8^a 16^b=2^N,
P=9^(a+b),
D=Q-P,
Q*y'=P*y+E_w.
```

At a minimum of a positive macro cycle, `L-9609` gives

```text
E_w=D*m+Q*k.
```

Because every centered constant is divisible by three, write `m+k=3r`:

```text
E_w=3rD+P*k.
```

Modulo 27, every centered toll vanishes except a possible final `A` toll.
Thus

```text
macro ends in B -> E_w == 0 mod27;
macro ends in A -> E_w == 3*2^(N-3) mod27.
```

Since `27|P` and `D==2^N mod27`, comparison forces

```text
r == 0 or 8 mod9.
```

Therefore the smallest possible cycle-minimum level is `r=8`, and

```text
E_max < 24D
```

excludes every repetition length and every macro switching pattern.

This is a genuine two-sided physical rule: the cycle minimum controls the
whole denominator, while the terminal physical letter controls the residue.

## 3. Infinite uniform region

For fixed `a`, the ratio

```text
E_max/D
 =3(9^a-8^a)/(8^a-9^a(9/16)^b)
```

strictly decreases with `b` in the contracting range.

Exact boundary checks prove `E_max<24D` for:

```text
a=6:  every contracting b>=2;
a=7:  every contracting b>=2;
a=8:  every b>=3;
a=9:  every b>=3;
a=10: every contracting b>=3;
a=11: every contracting b>=3;
a=12: every b>=4;
a=13: every b>=4.
```

All smaller `b` not listed as exceptions are supercritical and cycle-free by
sign.

Only four contracting packets survive the uniform theorem:

```text
(8,2), (9,2), (12,3), (13,3).
```

## 4. Exact closure of the four exceptions

A word-independent modulo-seven phase is

```text
E_w == 3*2^b*(2^a-1) mod7.
```

Combining it with the terminal residue and exact height caps gives:

- `(8,2)`: only `(r,k)=(8,0)` remains; `E_w==1 mod7`, but `24D==6 mod7`.
- `(9,2)`: terminal levels are `8,9,17,18`; modulo seven forces `k=0`; modulo eight removes `9,17,18`; the last target is `8 mod16`, while the alphabet is `{0,3,11}`.
- `(12,3)`: terminal levels are `8,9`; modulo seven forces `k=0`; the same modulo-eight/modulo-sixteen argument closes both.
- `(13,3)`: modulo seven leaves only `(8,3)` and `(9,1)`; modulo eight removes `(9,1)`; `(8,3)` is `107 mod128`, while the complete first-three-letter alphabet is `{0,3,43,48,67}`.

These are complete alphabet classifications, not sampled words.

## 5. New theorem `T-9609`

Combining this packet with `T-9608` gives:

```text
for every b>=1 and every 0<=a<=13,
no arbitrary word over the complete fixed-weight (a,b) macro alphabet
has a nontrivial positive integral cycle.
```

The first open aligned fixed-weight layer is now

```text
a>=14.
```

The result remains unbounded in pulse count, macro length, branch count,
macro repetition length, switching pattern, and total centered support.

## 6. Verification

Run:

```bash
python3 -B experiments/X-9613-terminal-residue-pulse/verify.py
```

Expected result:

```text
all independent L-9610/T-9609 checks passed
```

Verifier SHA-256:

```text
644f4423ab3f7207b00d286f11a4f55774facb8aafb70890a4939091aeea67d9
```

The verifier reconstructs the terminal residue, exact gate margins, all four
exceptional alphabets, their target sets and residue separations, and selected
two-macro compositions with a separately written exact implementation.

## 7. Remaining objective

This packet does not decide the six-branch ordinary least-root sequence and
does not produce a positive cycle.

The two full-objective lanes remain:

```text
six-branch least roots bounded or escaping;

or

full-denominator cycle construction outside the now-closed a<=13 aligned family.
```
