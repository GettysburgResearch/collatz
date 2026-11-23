# Bounded inverse-tree steering: attempted induction and remaining gap

This is an unfinished constructive route. It is not an all-modulus coverage
theorem and is not used by `LocalProfileObstruction.lean`.

## Proposed target

For every positive ternary unit `q`, every `p ≥ 1`, and every unit residue
`c mod 3^p`, seek an actual descendant of `q` in that residue after at most
`C p` generations, with an absolute constant `C`. Each generation chooses
`L0 ∈ {6,…,11}` such that `2^L0 q ≡ 7 (mod 9)` and retains the two unit
children among

\[
x_j=\frac{2^{L_0+6j}q-7}{9},\qquad j=0,1,2.
\]

These are positive ordinary predecessors. In the physical-five application,
the paths from `x_j` and `5x_j` reach `q` and `5q` at the same clock. Thus
the construction retains the fixed ordinary endpoint and its comparison.

A depth bound would also give a height bound, since each child is at most
`(2^23/9)q`. Linear depth in `p` would therefore give a height polynomial
in `3^p`, substantially improving the unrestricted sibling-exponent route.
An additional argument would still be needed to close the global shell
construction.

## Exact sibling structure

The siblings satisfy

\[
x_{j+1}=B(x_j),\qquad B(x)=64x+49.
\]

The three consecutive siblings occupy the three residue classes modulo 3,
so exactly two are units. Also

\[
B^m(x)-x=\frac{64^m-1}{9}(9x+7).
\]

For `m>0`, the elementary lifting-the-exponent identity gives
`v_3(B^m(x)−x)=v_3(m)`. Hence `B` has a full orbit modulo every `3^p`.
This supplies residue steering with an unrestricted sibling exponent. It
does not bound that exponent linearly in `p` or implement it by a linear
number of the bounded child choices above.

## The digit-lifting gap

Computing one child's residue modulo `3^p` generally requires the parent's
residue modulo `3^(p+2)`: division by 9 loses two digits of input precision.
The three sibling choices provide one immediate controlled ternary digit,
with the zero class then excluded. Further generations also change the
previously steered digits. The missing induction must arrange those changes
so that an additional target digit can be imposed while preserving all
previously imposed target digits at bounded additional depth.

A useful formal 3-adic coordinate makes the issue explicit. For the chosen
`L0`, write

\[
q=(7/2^{L_0})64^z,
\qquad
H(x)=\frac{\log(1+9x/7)}{\log 64}.
\]

The map `H` is an isometry of `Z_3`, and the children are
`H⁻¹(z+j)` for `j=0,1,2`. This isolates the low-digit choice but does not
give the missing preservation rule for successive target digits. No
bounded-depth simulation of large powers of `B`, no suitable uniform
commutator construction with all ordinary guards preserved, and no
countermodel to the proposed all-`p` statement was obtained in this pass.

Finite-level coverage and averaged Haar coverage were not promoted to a
pointwise all-`p` assertion. The exact all-width result preserved from this
agent's pass is the separately compiled local-profile obstruction.
