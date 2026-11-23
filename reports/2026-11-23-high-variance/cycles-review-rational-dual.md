# Independent review of the signed rational-dual certificate

Reviewer: `nov23_cycle_ideal`, 23 November 2026.

**Result: PASS for the written Sections 2–7 and the finite replay logic.**

| Reviewed file | SHA256 |
|---|---|
| `research/high-variance-20261123/arithmetic/RATIONAL_DUAL_CERTIFICATE.md` | `71aeff76e8983a9f703229d8c07a7cc9b734f3e07b82a85c8d3576b337787d05` |
| `research/high-variance-20261123/arithmetic/check_rational_dual.py` | `7ee4c64b4203e7e8d2cc1ff6aac840eecc5bc16b0ce3c90f23c358efbe2a2a43` |

This is a mathematical and source-level implementation review. The reviewer
did not run an additional grid or certify the external literature. No
universal rational-dual existence claim or positive-cycle exclusion follows.

## Positive ordinary pairs

For opposite-parity positive integers, the exact product factor is
`(3+1/z)/4`, with `z` the odd member. It is at most one, and at most
`5/6` if `z≥3`. If the odd member is one, the next opposite-parity pair
has odd member at least three unless the pair is `(1,2)` or `(2,1)`.
Checking predecessors shows that only the exceptional pair can lead to
the other exceptional pair while retaining positive opposite parity.
Grouping departures in pairs proves (3) with `floor(k/2)` and yields
the finite-prefix height bound (4). No infinite compact limit is used.

## Signed product bounds

Before `x=1`, an odd positive `x` is at least three. If the numerator
remains negative, both cases in (7) are exact; the second requires the
stated negative successor and is then positive and below `3/4`.
A positive integer product cannot endure `N_-` strict contraction steps
with (8), so the negative-phase stopping bound has the claimed scope.

The negative-to-positive crossing factor is exactly
`(d/|w|-3)/4`, strictly below `d/4`. There is at most one crossing, and
the conservative charge `P_+≤d n|a|` is valid. This charge is separate
from the count of small positive numerators; it has not been hidden in
a budget of only `d` exceptional departures.

For positive large numerators, odd `x` gives `5/6≤q_d`; even `x` forces
odd `w≥d+2`, yielding exactly the advertised `q_d`. For positive small
numerators, `(3+d/w)/4≤(d+3)/4=R_d`, and the odd-`x` case is even
smaller. Before the first repeated small numerator, at most `d`
departures have a starting numerator in `{1,…,d}`. Thus (14) follows.
The floor-plus-one in (13) makes its final inequality strict, including
`P_+=1` and `R_d=1`. A rational implementation need not approximate a
logarithm.

The product bound (15) holds **through the first-event state**: its value
is controlled by the preceding departures. The author adopted this
wording clarification before the final hash above. It justifies using
that bound at both repeated states in the extra valuation clock.

## Zero, one, and the first repeated small numerator

Zero is split off before any logarithm. For `w=0`, the ordinary positive
trajectory has exactly `v_2(x+1)` initial odd steps, so the first failed
parity test is at that offset. An initial even `x` fails immediately.
At `x=1`, `w=2d` gives the displayed literal pair cycle. For every other
`w`, the nonzero difference from `2d` has a finite valuation and gives
the stated exact terminal mismatch. In the overlap `x=1,w=0`, both
rules predict offset one.

For repeated small numerator `w_i=w_j`, equality of the integer states
gives a literal deterministic pair cycle whose parity has been checked.
If the integer states differ, their trajectories share exactly
`r=v_2(x_i-x_j)` parity bits. To establish the **first** mismatch at
`j+r`, the proof correctly propagates previously valid parity using the
state one numerator period earlier. That earlier state has already been
checked either in the original prefix or in the induction. At the final
index, the two integer parities differ and numerator parities coincide.
The terminal-state convention is explicit and correct.

## Finite implementation

`decide_dual` tests parity before the exceptional and repetition rules.
Its rejection routine replays every intervening state and includes the
predicted terminal state. Its acceptance routine either checks the
standard pair or replays the full proposed pair period and checks its
endpoint. The example generator that reverses explicitly terminated
orbits is not called by the decider; it supplies finite test inputs only.
No precondition of infinite complementarity, Collatz convergence, or
bounded future search is present in the decider.

The local numerical validations use Python assertions in the ordinary
run; this review does not claim they remain active under optimized
Python. The all-input termination argument is the written product proof,
not the finite grid. A correct rational candidate therefore forces an
actual cycle; obtaining such a candidate for every positive source and
excluding nonstandard cycles remain separate open obligations.
