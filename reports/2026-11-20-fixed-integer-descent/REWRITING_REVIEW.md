# Independent review of the six-run guarded AYH transfer

**Verdict: VERIFIED WITH A SCOPE WORDING FIX.** RW-1 and RW-2 are valid
for the stated stopped relation on proper words, using the separately
specified universal cap-six odd clock. The author corrected the description
of the new guard: it is not a superset of the previous ten-popcount guard.
No mathematical proof or checker change was needed.

Reviewer: the fixed-source-drift agent, separate from the rewriting author.
This is independent mathematical reconstruction and bounded execution,
not a proof-assistant build, external peer review, or unrestricted
Collatz/rewriting termination proof.

## Final review pins

| Artifact | SHA-256 |
|---|---|
| `research/fixed-integer-descent/rewriting.md` | `bf6fe9b98ca229bac30f82703c0c8ac2727ee16318f2b6a414b2a2573099be07` |
| `experiments/fixed_integer_rewriting.py` | `502999ab238a79053bc63113006c36ada5cabc83d1092b16f3cb5afce024fc4f` |
| `reports/2026-11-20-fixed-integer-descent/rewriting-report.json` | `68d2e93156d254bd7dff21acf63f056a7b107d01deb78163beb83936c05fbc0c` |

The independent execution report records the manuscript hash
`1a1eed215f2602feb65f960097fd5956e404d69fb1007b63bd31664bf552cc4b`,
which preceded the guard-comparison wording fix. The production checker
was unchanged. The final corrected manuscript was read after that fix;
the final proof review is pinned above. The original execution receipt
is preserved rather than silently changing its recorded hash.

## 1. All administrative rules

Let `x>=1` be the decoded prefix value before an internal two-letter
left-hand side. Direct composition gives:

| Rule | Common affine value |
|---|---|
| `ae -> ea` | `6x` |
| `af -> eb` | `6x+1` |
| `ag -> fa` | `6x+2` |
| `be -> fb` | `6x+3` |
| `bf -> ga` | `6x+4` |
| `bg -> gb` | `6x+5` |

Each left side has its ternary letter after a binary letter, so the
ternary contribution is `b(2x)` or `b(2x+1)`, both exactly `b(x)+1`.
The right side places its ternary letter at prefix `x`. The common
affine value preserves the prefix value at every later ternary letter.
Thus each of these six rules preserves `N` and decreases `H` by exactly
one, in arbitrary *proper-word* prefixes and suffixes.

The three boundary identities are `ce = cb = 3`, `cf = caa = 4`, and
`cg = cab = 5`. They remove precisely one ternary letter of prefix
value one and weight one, while preserving all later prefix values.
Thus all nine administrative rules have the claimed exact `H` change.

This proof uses bitlength of the decoded prefix, not the number of
ternary symbols. Simply counting ternary symbols would not decrease on
any of the six internal swaps.

## 2. Dynamic rules and the total odd clock

For a proper word ending in `ad`, its last binary operation gives an
even value `N=2x`. The rule removes that operation, so `N` becomes `x`,
its odd part is unchanged, `v2(N)` drops by one, and no ternary weight
changes.

For a proper word ending in `bd`, its value is `N=2x+1>=3`. Replacing
the final binary letter by `g` gives `3x+2=(3N+1)/2`. Its odd part is
exactly `U(N)`. Under the source guard, `N` is an active odd source, so
the first-hit definition gives `q(U(N))=q(N)-1`. The new ternary weight
is `b(x)=b(N)-1`.

Consequently `(q(oddpart N),v2(N),H)` strictly decreases on each of the
eleven permitted rules. This includes a last odd step whose destination
exceeds the run cap: that destination has `q=0` and then no further step
is permitted. Powers of two have `q=0` throughout their halving phase;
the second coordinate still decreases. The only value-one proper word
is `cd`, since every interior letter strictly increases a positive
prefix value.

The totality and bound `q<=107` are the named RC-5/M3 input. This review
does not infer them from the small rewriting corpus and does not repeat
the complete 19,371,072-source cap-six enumeration. The earlier
[run-core review](RUN_CORE_REVIEW_BY_DRIFT.md) records the separate proof
reconstruction and the exact scope of independent core execution.

## 3. Scheduling-independent literal budget

For any finite guarded rewrite prefix, let `d` count odd dynamic events,
`e` count even dynamic events, and `A` count administrative events. The
rank's first coordinate gives `d<=107` without assuming convergence.
Dynamic positivity and the per-event multiplier bound give

\[
1\le N_{\mathrm{current}}\le N_0\,2^{d-e},
\qquad d+e\le b(N_0)-1+2d.
\]

Before the `j`-th odd event, the current value is at most
`2^(j-1) N_0`; halvings can only decrease it. Hence that event creates
at most `b(N_0)+j-2` units of `H`. As administrative events each consume
one unit and even events consume none,

\[
A\le H_0+d(b_0-1)+\frac{d(d-1)}2.
\]

Adding dynamic and administrative counts gives

\[
A+d+e\le H_0+(d+1)(b_0-1)+\frac{d(d-1)}2+2d
\le H_0+108(b_0-1)+5885.
\]

The constant is exactly `107*106/2+214=5885`. These estimates apply to
every finite prefix, so they do not assume the termination conclusion
that the bound establishes. The administrative conservation identity
was also checked literally under three independent scheduling policies.

## 4. Guard and context boundaries

The source guard is exactly `N>1` and `runs(oddpart(N))<=6`; after failure,
the process stops. It is not a predicate on how many mixed symbols the
word contains. Removing the guard is refuted by the actual step from
the binary representation of 5461 to a mixed representation of 8192:

\[
(q,v_2,H)=(0,0,0)\longrightarrow(0,13,12).
\]

The corrected comparison with the old guard is exact. For example,
`349525=sum_(j=0)^9 2^(2j)` has ten set bits and ten one-runs; it passes
the old ten-popcount guard and fails the new guard. Conversely,
`1048575=2^20-1` has twenty set bits but one one-run. Both examples were
checked with the independent binary-string routine.

The manuscript correctly makes no claim of context compatibility on
arbitrary strings and no unrestricted reduction-order claim. Guard
failure cannot be repaired by resetting a larger run cap without a
separate decreasing comparison. An active proper word cannot be stuck:
the leftmost ternary symbol permits an administrative rule, or a
nonempty binary interior ends in an applicable dynamic rule.

## 5. Independent finite execution

The separate checker
[check_rewriting_independent.py](check_rewriting_independent.py) imports
neither the author's checker nor its functions. It defines its own rule
table, scans every occurrence of each left-hand side, decodes ordinary
values, counts one-runs through binary-string transitions, and obtains
odd events by repeated halving. Its schedules use leftmost, rightmost,
and seeded random choices.

Executed command:

```bash
python -X utf8 -B reports/2026-11-20-fixed-integer-descent/check_rewriting_independent.py
```

Exact result: [rewriting-independent-report.json](rewriting-independent-report.json).

| Check | Actually executed |
|---|---:|
| All proper words with interior length at most 7 | 97,656 |
| Applicable rule occurrences | 232,421 |
| Guarded rank-decreasing edges | 232,421 |
| Distinct odd clock inputs replayed in that corpus | 2,197 |
| Scheduled trajectories, using two encodings of each input 1--512 | 3,072 |
| Literal scheduled rewrite steps | 496,587 |
| Largest observed schedule length | 524 |

Every rule was checked: 19,531 occurrences each for the two dynamic
rules and three boundary rules, and 22,461 each for the six internal
administrative rules. All value identities, exact `H` changes, rank
comparisons, dynamic-event budgets, creation budgets, administrative
conservation identities, and final guard checks passed.

A separate targeted execution of the same independent literal odd-map
routine confirmed `q(74475)=107` and the constant 5885. The production
report's 501 schedules, large one-run stress cases, and 107-event
schedule witness are distinct evidence and are not added to the
independent counts above.

## Remaining mathematical boundary

This establishes the transfer of the finite run-cap theorem to every
literal rule and every scheduling choice under the stated guard. It
does not establish a global run cap, a way to pay for repeated cap
increases, unrestricted AYH termination, or full Collatz convergence.
