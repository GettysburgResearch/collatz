# Independent candidate-lane reconstruction of the commutator theorem

23 November 2026. **VERIFIED at the stated written-theorem scope.**

Reviewed source:
`research/lean-exact-witness-global-20261121/universal-step-20261123/commutator/UNEQUAL_BLOCK_COMMUTATOR.md`.

SHA256:
`2a85e4a68a8ee6b5107b9cbccfc06f5e5bf8295ac2e380353ef9f65d3449ebde`.

Reviewer: the candidate-construction lane, which did not develop the
commutator theorem or its strengthening. This is an internal mathematical
reconstruction, not external referee acceptance or Lean verification.
No additional computational census was needed for the symbolic claims.

## Claims reconstructed

**UC-D, common residue from the complete cycle.** For the initial
odd-containing reference block, `d_0=2^A_0-3^p_0` is a unit modulo every
6-smooth s. The cross-carry divisibilities give `d_i a=C_i mod s` for
every label by cancellation of d_0 alone. Subtracting a from an actual
integer boundary edge gives `Q_i z'=P_i z mod s`. Composing the complete
finite word without dividing by any Q_i produces
`(product Q-product P) z=0 mod s`. Its whole denominator is positive
and coprime to six. It therefore forces the same residue at every cyclic
cut. The proof does not incorrectly invert an even Q_i modulo s.

**UC-D, the minimum corner and plateaus.** A nonconstant finite cyclic
boundary path has an entry to its minimum from a larger value and an exit
from that minimum to a larger value. These need not be adjacent; their
shared ordinary minimum value suffices. The common residue makes both
gaps positive multiples of s. Eliminating that same minimum yields

`E_ij=s(d_i Q_j beta+d_j P_i alpha)`

with alpha,beta at least one. Both d factors are positive. Thus the
right-hand side is at least
`s(d_i Q_j+d_j P_i)=s(Q_i Q_j-P_i P_j)`, contradicting the stated strict
pairwise bound. Plateau edges need not be charged or deleted by an
unproved path operation.

**UC-2 and strictness.** For two distinct fixed points, a mixed constant
boundary path is impossible. Taking the smooth part of the one nonzero
cross expression and applying UC-D contrapositively proves the stated
cofactor lower bound. Equal shapes cancel exactly one common factor
`Q-P`, which is coprime to six. The abstract control
`4 -> 3 -> 4` has cross expression and two-block denominator both 23,
so the strict boundary is accurately retained. The note correctly
distinguishes that affine control from legal Collatz blocks.

**Pure-even extension.** Only the chosen reference block needs an
invertible d. When a closed path uses an odd-containing block, choose it
as reference; the complete denominator remains a unit modulo six. The
minimum argument needs positivity of each d, not invertibility of each d.
An all-pure-even positive closed path is separately impossible. This
extension introduces no invalid cancellation modulo three.

**UC12, variable-length sparse defects.** With the composition order
`u^k` followed by `t`, the stated complete carry is
`R C sum_(j<k) Q^(k-1-j)P^j + Q^k B`. Multiplying by `Q-P` and using
the finite geometric identity cancels the intermediate `R P^k C` terms,
leaving exactly `Q^k((Q-P)B-(S-R)C)`. Since Q is a power of two,
the part coprime to six is independent of k. Both eventual contraction
and divergence to positive infinity of
`S Q^(k+1)-R P^(k+1)` follow from `Q>P>0`. Therefore UC-2 excludes
all mixed closed integer paths over each sufficiently large fixed
dictionary `{u,u^k t}`. The note explicitly does not combine varying k
into an unproved infinite-dictionary statement.

## Preserved limitations

The review does not supply a decomposition of every hypothetical Collatz
cycle into a dictionary satisfying UC4. A constant boundary path still
requires the one-block integer fixed-point test and physical replay.
An expanding dictionary block invalidates the positivity used in the
minimum-corner lower bound. The note states all three limitations.

No corrections were required for the reviewed source hash. The verdict
does not extend to subsequent edits, other files, or full cycle exclusion.
