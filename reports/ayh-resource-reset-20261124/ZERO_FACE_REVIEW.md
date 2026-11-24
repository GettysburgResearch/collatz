# Independent review of the nonnegative-orthant extension

**Verdict.** The last section of `GLOBAL_METHODS.md` gives a valid written
extension to the entire nonnegative three-dimensional orthant. The word
trace and Boolean-map census are finite exact computations. The separate
Lean proof for the positive orthant does not formalize this extension.

| Source path at review | SHA-256 |
|---|---|
| `agent_global/GLOBAL_METHODS.md`, last section only | `ae015ac06411a6b2a6c024189a35f0e15eca4147f91b972623f748e4f55e9c79` |
| `agent_global/check_zero_faces.py` | `6701e7b63ae932b01aea3d25aa306fa0bc1c5e6b6954017c73d8b215e7edcf09` |

For fixed auxiliary inputs, each letter’s first output is strictly
increasing on the natural-number chain, hence at least its first input.
All seven maps therefore preserve positive first coordinate. The
binary-zero letter A may have coordinates given by zero polynomials.
In a nonnegative polynomial, positivity of any output depends exactly
on which variables are positive. On the four masks of auxiliary
variables its action is monotone. A cycle is an antichain because the
map is a bijection on that cycle, so distinct comparable cyclic elements
would give a strict circular chain. The only two-cycle can interchange
the two singleton masks. Every starting mask enters its cycle by time 3.

For a fixed mask, substitution of zero leaves a positive-polynomial map
on its active coordinates. Apply the positive theorem to the state at
time n−2, with n at least 5, to compare A at times n and n+2. In the
two-cycle take G=A², substitute zero on the inactive coordinate, and
use that the return has only one free positive coordinate. Its polynomial
either dominates that coordinate on the positive face, or depends only
on the extensive first coordinate. Thus G²(v)≥G(v), giving the same
n-to-n+2 inequality from time n−2 on either phase. The compared
inactive coordinates both vanish.

I separately replayed the leftmost derivation using the eleven ASCII
rules, decoding after every step. It rewrites `c a^7 b b d` to
`c a^9 b b d` in 308 steps, including 52 shortcut steps from 515 to
2051. The per-rule counts, in the standard order
`ad bd ae af ag be bf bg ce cf cg`, were
`18 34 26 36 50 22 25 63 14 11 9`.
The common suffix maps a positive-first test state to another
positive-first state. The n=7 inequality then opposes the strict
decrease that any uniformly strict rule would force across this trace.
The supplied checker also passed under Python’s optimized mode.
