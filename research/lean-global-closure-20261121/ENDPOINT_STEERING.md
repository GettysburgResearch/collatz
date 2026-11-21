# Exact obligation for adaptive endpoint steering

This checkpoint is an ordinary-integer Lean contract for a potential global
construction. It does not provide the universal selector and does not prove
Collatz.

## Source work

- PR146, commit `f431078244e868dc699fad011044f0d5e7f76437`, especially
  `research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md` and
  `research/upper-bit-mergers/FIVE_RETURN_IN_EVERY_CLASS.md`.
- PR173, commit `8596fdfd4d6378b57f83d843e94a206f45604b1b`,
  `research/lean-shell-cover/ShellCover.lean`.

PR146 constructs simultaneous returns of whole intervals and then prescribes
the final endpoint by solving a power-of-two congruence. The available final
halving exponent can be exponential in the current ternary precision.

## What Lean proves

Let `orbit k n` be the actual shortcut Collatz orbit and `odds k n` its actual
number of odd inputs. For every finite word, every old ternary precision `p`,
and every nonnegative integer lift `t`, the file proves

\[
T^k(n+2^k3^p t)=T^k(n)+3^{p+\operatorname{odds}(k,n)}t.
\]

It also proves that the number of odd inputs is unchanged on the entire binary
lift. Therefore the existence of a legal nonnegative lift with endpoint
`2^b*q` is exactly

\[
T^k(n)\le 2^bq,
\qquad
3^{p+\operatorname{odds}(k,n)}\mid 2^bq-T^k(n).
\]

The source is constructed explicitly by taking

\[
t=\frac{2^bq-T^k(n)}{3^{p+\operatorname{odds}(k,n)}}.
\]

The construction is positive when `n>0`; that guard is stated separately in
`construct_positive_source`. All results concern actual natural-number
trajectories, with all parity guards supplied by the binary-lift identity.

## Remaining global construction

Appending a suffix with `r` odd inputs raises the final ternary precision from
`p` to `p+r`. Steering the newly introduced low ternary digits leaves the `p`
old constraints. Finite-modulus transitivity or a contraction of the ternary
offset alone does not construct the desired ordinary endpoint.

A possible route is an adaptive tree of legal equal-clock five predecessors.
The known block `A(z)=(9z+7)/64`, valid for `z=49 mod64`, supplies

\[
x_L=(2^Lq-7)/9.
\]

For any ternary unit `q`, one may take `L0` in `[6,11]` with
`2^L0*q=7 mod9`; among `L0,L0+6,L0+12`, exactly two give ternary-unit
children. Every such positive child is an actual simultaneous predecessor of
`q,5q`. The sibling operation is `x -> 64*x+49`. Iterating that operation
alone has a full cycle modulo every power of three, but the resulting
exponent can again be exponential in the precision.

The unresolved proposed improvement is a uniform bound on the depth of the
**nested bounded-child tree** needed to enter a prescribed unit residue
modulo `3^p`, retaining ordinary positivity and all actual word guards.
Neither a polynomial nor a linear all-`p` depth bound is proved here. Such a
bound would improve endpoint height; an additional quantitative argument
would still be needed to meet PR173's clean-shell size condition.

## Check

The file was checked with Lean `4.34.1` and Mathlib commit
`d13f23b723b8a846827a245b89c10fc7d3f11612`. It contains no `sorry` or custom
axiom. Every proved declaration has a `#print axioms` report; the reports
contain only `propext` and `Quot.sound`.
