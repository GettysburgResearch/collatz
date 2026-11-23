# Independent review of source-tail transport

Date: 2026-11-23. Reviewer: atomic literature lane.

Reviewed artifact:
`../triadic/SOURCE_TAIL_TRANSPORT.md`

SHA-256:
`f9b97f4945e3adeaf7b7eb2d1bfc9e50bb59fb0d166db398c55f2f40011c2f8f`.

**Result: PASS for the written arguments in Propositions 1 and 3 and the
all-parameter corollary.** This review independently reconstructed the
algebra; it did not rerun or certify the companion Lean compilation.

## Proposition 1

A shortcut path from an ordinary source greater than two, stopped at its
first hit of one, must end with inputs four and two. The only ordinary
predecessor of one is two; the only predecessor of two consistent with
first hitting one later is four. Complementary backward transport of
the terminal dual two therefore gives two, one, one-third.

Once the reduced denominator exponent is positive, an original odd
inverse multiplies its unit numerator by two and preserves the exponent.
An original even inverse subtracts the positive power of three from
twice that numerator and adds one denominator power. Its numerator
remains a ternary unit, including when it is negative. The total exponent
is exactly the number of original even inputs minus one. Terminal cycle
padding multiplies numerator and denominator by the same power of three
and leaves the reduced source pair unchanged.

## Proposition 3

At every original even step inside the matched prefix, the assumption
`r > b_K` gives the current exponent at least two. Consequently the new
numerator `(w_i + 3^(r_i-1))/2` is a nonzero ternary unit. Division by
two is integral because the matched complementary parity is odd.
For the positive integer product
`P_i = T^i(n) * |w_i| * F(r_i)`, the even-step ratio is at most one
quarter, using `|w_i| >= 1` and
`F(r_i)/F(r_i-1) = 1 + 3^(r_i-1)`.

An original odd step divides the complementary numerator by two and
has product ratio `(3x_i+1)/(4x_i)`. This is at most five-sixths when
`x_i >= 3`. If `x_i = 1`, the ratio is one but the following ordinary
input is two, so its ratio is at most one quarter. Every consecutive
two-step block is therefore bounded by five-sixths, without assuming
that the target has not yet reached one.

Four such blocks strictly halve the product because
`2 * 5^4 < 6^4`. Repeating for the positive bit length `E` gives a
positive integer strictly below `P_0/2^E < 1` if `K >= 8E`. This proves
the stated strict horizon bound.

## Corollary and scope

The constructed numerator is a ternary unit for every target clock and
dyadic source lift, since the known reduced source exponent is positive.
Thus its complete reduced exponent is `s + t + b_K > b_K`, so
Proposition 3 applies to the whole family. The paid horizon `9E+1`
cannot hold. Neither cancellation by terminal source padding nor a
favorable subsequence changes this conclusion.

This excludes the displayed source-tail family from the specified
sufficient horizon. It does not disprove the original residue implication,
classify all triadic candidates, or establish full Collatz. The reviewed
note correctly keeps Propositions 1 and 3 and this corollary as written
arguments, rather than claiming that its ten finite Lean declarations
formalize them.
