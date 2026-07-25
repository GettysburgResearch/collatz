```text
Claim ID:            T-6102
Title:               The six-branch index is a function of v_2(x); legal valuations are {0,3,6,9,12,15}
Status:              PROVED
Authoring agent:     claude-opus5-61
Reviewing agents:    (none yet)
Created:             2026-07-25
Last updated:        2026-07-25
Dependencies:        none (self-contained); used by T-6101 claim 3 and by X-6110
Scope:               the fixed chart of T-6101
Related counterexample candidates: none
```

## Statement

With `P = 3^12`, `Q = 2^19`, `a_i = 7 * 3^(2i) * 2^(15-3i)`:

**(a)** If the chart step at `x` is legal with digit `a_i`, then

```text
v_2(x) = 15 - 3i.
```

**(b)** Consequently legality forces `v_2(x)` in `{0, 3, 6, 9, 12, 15}`, and the branch taken
is *not a free choice*: it is determined by `x` through

```text
i = (15 - v_2(x)) / 3.
```

**(c)** Writing `x = 2^(15-3i) u` with `u` odd, legality is equivalent to the single
congruence

```text
u = -7 * 3^(2i-12)   (mod 2^(4+3i)),
```

so the conditional probability of legality given the correct valuation is `2^-(3+3i)`, and
the total legality density is `sum_i 2^-(16-3i) * 2^-(3+3i) = 6 * 2^-19`, in agreement with
`|A|/Q`.

**(d)** Physical reading (with T-6101): the unique `1010` defect inside the 19-step macro
block `W_i = (110)^(5-i) . 1010 . (110)^i` is preceded by exactly `v_2(x)/3` copies of `110`.
The 2-adic valuation of the chart coordinate therefore *times the defect* in the real Collatz
parity word.

## Proof

**(a)** Legality means `Q x' = P x + a_i` for an integer `x'`, so `P x + a_i = 0 (mod 2^19)`,
i.e. `v_2(P x + a_i) >= 19`. Now `v_2(a_i) = 15 - 3i <= 15 < 19`. If `v_2(P x)` were different
from `v_2(a_i)`, then `v_2(P x + a_i) = min(v_2(P x), v_2(a_i)) <= 15 < 19`, a contradiction.
Hence `v_2(P x) = v_2(a_i) = 15 - 3i`, and since `P = 3^12` is odd, `v_2(x) = 15 - 3i`. `QED`

**(b)** Immediate from (a), because `i -> 15 - 3i` is injective on `{0,...,5}` with image
`{15,12,9,6,3,0}`.

**(c)** Write `x = 2^(15-3i) u`, `u` odd, and `a_i = 2^(15-3i) * 7 * 3^(2i)`. Then

```text
P x + a_i = 2^(15-3i) ( 3^12 u + 7 * 3^(2i) ),
```

so `2^19 | P x + a_i` iff `2^(4+3i) | 3^12 u + 7*3^(2i)` iff
`u = -7 * 3^(2i) * 3^-12 (mod 2^(4+3i))`, which is solvable since 3 is a 2-adic unit. Among
odd residues mod `2^(4+3i)` (there are `2^(3+3i)` of them) exactly one qualifies, giving the
stated conditional density. The unconditional density of `v_2(x) = 15-3i` is `2^-(16-3i)`, so
each branch contributes `2^-(16-3i) * 2^-(3+3i) = 2^-19`, and the six branches contribute
`6 * 2^-19` in total. `QED`

**(d)** By T-6101 claim 2 the word is `W_i = (110)^(5-i) . 1010 . (110)^i`, so the number of
leading `110` blocks is `5 - i = 5 - (15 - v_2(x))/3 = v_2(x)/3`. `QED`

## Motivation

Three uses.

1. It shows the chart is *deterministic* in a strong sense: there is no branching choice to
   optimise. Search strategies that treat the six branches as an alphabet to be steered (a
   recurring idea in the positive lane) are steering nothing — the letter is read off
   `v_2(x)`. Only the *initial value* is free.
2. It gives the exact per-step density `6/2^19` used by C-6111, decomposed branch by branch,
   which rules out the hope that some branch is "cheap" and could be chained indefinitely at
   low cost. Every branch costs exactly `2^-19`.
3. It supplies the transition rule in valuation form, used to sanity-check X-6110:
   with `x = 2^(15-3i) u`, `x' = 2^(15-3i')u'` and `u,u'` odd,

   ```text
   2^(19 + 3i - 3i') u' = 3^12 u + 7 * 3^(2i),
   ```

   so `v_2(3^12 u + 7*3^(2i)) = 19 + 3(i - i')` lies in `[4, 34]`.

## Gap audit

* *Is the transition graph restricted?* No. All 36 ordered pairs `(i, i')` are attainable:
  the constraint in use 3 above is `v_2(3^12 u + 7*3^(2i)) = 19 + 3(i-i')`, and for each
  target valuation in `[4,34]` odd `u` realising it exist by Hensel lifting. This is confirmed
  empirically: the digit words of the least roots in X-6110 (e.g. `205431351450115`) contain
  many distinct adjacent pairs. **There is therefore no finite-state obstruction to
  infinite legality**, and no proof of chart-emptiness can come from the transition graph.
* *Does (a) use positivity?* No; it holds for every integer and every 2-adic integer `x`.
* *Off-by-one in `v_2(a_i)`*: `a_0 = 7 * 2^15` gives `v_2 = 15`, `a_5 = 7 * 3^10` gives
  `v_2 = 0`; both endpoints checked explicitly in `crosswalk.py`.

## Adversarial tests

`replay.py` recomputes `v_2(x_n)` along the full legal orbits of `m_6` and `m_9` and compares
with `15 - 3 i_n` for the recorded digit word: exact agreement at all 15 checked steps.

## Suggested next attack

Use (b) to phrase the existence question purely in terms of valuations: an all-time seed is a
positive integer whose chart orbit has `v_2(x_n)` in `{0,3,6,9,12,15}` for every `n` *and*
satisfies the extra congruence (c) at each step. The valuation condition alone has density
`sum_i 2^-(16-3i) = 37449/65536 = 0.571426...` per step, and it is the congruence (c) that
carries the real cost. No obstruction is known for either.
