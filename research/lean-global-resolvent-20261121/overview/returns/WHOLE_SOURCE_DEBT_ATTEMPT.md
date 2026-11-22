# Whole-source arithmetic attempt: exact alignment, unresolved exchange

**Status:** no proof of the universal `FloorIntervalStep` was obtained. The
positive structural observation below retains all parity disagreements in an
integer recurrence. A finite control shows why forcing its cancellation at the
original complete source clock cannot finish the argument.

## Inputs and scope

The inputs are PR177 at `e4ca639326bac73da8c2a698dec8a749e5efbe68`
(`JOINT_MINIMAL_COUNTEREXAMPLE.md`), PR180 at
`a66a44c9bf058cd7efe1018827ddda9a13297a21` (`ARITHMETIC_RIGIDITY.md`), and
PR185 at `980d40fc4afeaaf8f2a9256f322acf3e4568e013`
(`ARITHMETIC_ATTACK.md`), in their respective dated research directories.
The original witness and its original grade must be retained throughout.

Write `T(n) = n/2` for even `n`, and `(3n+1)/2` for odd `n`.
Let the complete positive-gap source word be `W`, with odd source `q`,
total ordinary clock `A`, and length `r`. Write
`x_j = T^j(q)`, `y_j = T^j(t)`.
The joint witness supplies, among other conditions:

- Every nonempty literal odd-source prefix of length `i` contracts its linear
  coefficient: `3^i < 2^(a_1 + ... + a_i)`.
- `2A < t`; if the target has not descended, `y_j >= t` for `0 <= j <= A`.
- A grade-minimal capturing powered source, maximal among sources of that same
  grade, and the lower-grade and larger-same-grade hypotheses from PR177.

PR180's survival buffer gives, for the target odd count `o_j`,

`3^o_j / 2^j >= 1 - j/(3t+1) > 5/6` for `0 <= j <= A`.

## Prefixwise count dominance

Let `r_j` be the source odd count by ordinary clock `j`. Then

`o_j >= r_j` at every `0 <= j <= A`.

Indeed, if `r_j = i > 0`, the `i`th source odd step occurs after the first
`i-1` complete gaps. Consequently
`j >= a_1 + ... + a_(i-1) + 1`.
For `i > 1`, the contracting-prefix hypothesis gives
`3^(i-1) < 2^(j-1)`; for `i = 1` the corresponding weak inequality is enough.
If `o_j <= i-1`, the target coefficient is at most `1/2`, contradicting the
buffer. The case `r_j = 0` is immediate.

Thus the difference `z_j = o_j-r_j` is a nonnegative integer walk. A decrease
in this difference always has an earlier increase available to fund it.

## Exact debt including every parity disagreement

Define the integer multiplier and signed integer debt

`c_j = 3^z_j`,  `D_j = y_j - c_j*x_j`.

Let `epsilon` and `eta` be the source and target parities at clock `j`.
Direct substitution in the two actual recurrences gives this entire table:

| Source parity | Target parity | New multiplier | Twice the new debt |
| --- | --- | --- | --- |
| 0 | 0 | `c` | `D` |
| 1 | 1 | `c` | `3D + 1 - c` |
| 0 | 1 | `3c` | `3D + 1` |
| 1 | 0 | `c/3` | `D - c/3` |

In the final row, prefixwise dominance ensures `3` divides `c`.
This is an integer comparison of actual source and target orbits. It does not
evaluate a source branch word illegally at the target.

Initially `c_0 = 1`, `D_0 = t-q`. At source completion,

`y_A = c_A + D_A`,  `c_A = 3^(o_A-r) > 5q/6`.

The attempted global cancellation would have to show that the right side drops
below `t`, or transform it into a **different legal complete word** whose grade
is funded by the original source. No such inequality or transformation was
proved. The count surplus alone bounds the multiplier in the wrong direction.

## Finite control: cancellation need not occur at the source clock

Take

`t = 3711`, `S = 2184 = 2^3 * 273`,

`W = [2,3,3,3,1,2,3,4]`, `A = 21`,

`Gamma = [8,7,6,6,6,6,4,4,2]` in decreasing order.

This source is actually grade-minimal among complete capturing sources and
maximal at its grade. The finite justification is short: a grade at most
`Gamma` allows no gap above `4`, at most one gap `4`, and an initial exponent
at most `3`. Without a gap `4`, the only complete odd source is `1`. With
exactly one gap `4`, remove terminal gap-`2` padding at `1`; every remaining
source is a predecessor of `5` using only gaps `1,2,3`. That inverse cluster is
closed and has exactly the following 16 elements:

`{3,5,7,9,11,13,17,19,25,29,33,45,51,77,205,273}`.

Enumerating the four possible initial exponents on this closed cluster gives
maximum source `1640` at grades strictly below `Gamma` and maximum source
`2184` at grades at most `Gamma`. Terminal padding can only increase grade
without changing source value. Since `3711 > 2*1640+1` and
`3711 <= 2*2184+1`, the claimed extremality follows. The attached script lists
every edge of this finite cluster and checks these comparisons exactly.

The source also has the required nonempty prefix before `[1,2,3,4]`, contracts
at every nonempty odd prefix, and all its positive-time ordinary iterates are
at most the floor `1855`. Nevertheless,

`T^21(3711) = 76196`,

and every iterate through both clock `21` and the powered-source completion
clock `24` is at least `3711`. The first descent is

`T^37(3711) = 2543 < 3711`.

At clock `21`, the source and target have `8` and `16` odd steps, respectively.
The exact recurrence ends with

`c_21 = 6561`, `D_21 = 69635`, `c_21 + D_21 = 76196`.

**This is not a counterexample to the global `FloorIntervalStep`.** It refutes
the tempting stronger assertion that the extremal source geometry forces
target descent by that source's completion clock. The target does descend
later. The calculation does not establish all other counterexample-specific
hypotheses, including the false assertion that this target is nonconvergent.

## Last changed-word attempt and the precise gap

Count dominance injects the source's `r` odd events into earlier target odd
events. Moving source odd positions earlier while keeping `A` and `r` fixed
reduces the affine correction `C`, formally increasing
`q' = (2^A-C)/3^r`. This looked capable of contradicting same-grade source
maximality.

It does not yet give a legal exchange: `3^r` must divide `2^A-C`, and the
changed gap multiset must be no larger than the original grade. Choosing the
first `r` target odd events can leave a long final gap and violate that grade
budget. Keeping the gap multiset fixed leaves precisely the nontrivial
integrality problem; PR185's permutation rigidity rules out treating this as
an automatic rearrangement. No deletion or matching theorem providing both
conditions was obtained.

Any continuation using this alignment must retain the unbounded target-time
problem and prove an actual legal, originally funded changed-word operation.
The present note claims no closure and introduces no additional assumed
criterion. No Lean theorem was added for this unsuccessful attack.

Reproduction: `python check_horizon.py` (Python standard library only).
