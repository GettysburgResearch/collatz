# Whole-source attack: cheap inverse growth and a forced routing clock

**Status: failed closing attempt, with an exact all-depth control.**
This pass tried to use the multiset rank's unlimited allowance of smaller
letters to build a large replacement source while retaining the actual
complete tail. No universal successful source surgery, merger, or Collatz
convergence theorem was obtained. The finite route control is formalized in `ForcedRoute.lean`; the
source-surgery attempt supplies no universal dispatcher. The argument below records the attempted mechanism and the arithmetic reason
one proposed uniform routing step cannot be used.

## 1. Inputs and the attempted global mechanism

The source is a complete positive ordinary certificate for the accelerated
odd map `U(n)=(3n+1)/2^v2(3n+1)`. Its grade is the repository's original
multiset of `2a` for odd gaps `a`, together with `2e+1` for a positive initial
even exponent `e`. The original target, full supplied tail, minimum grade,
and maximum source at that grade are all retained.

The relevant exact source files read in this pass were:

- PR177, `0444986571f09f302cb3687b4bba3552600e4119`,
  `research/lean-exact-witness-global-20261121/JOINT_MINIMAL_COUNTEREXAMPLE.md`
  and `WITNESS_CLOSURE_CONTINUATION.md`: the joint source selection and the
  arbitrary-context, nonnegative carry program.
- PR180, `5e29f56f6d44669a8aa9134e5617b78d65c074c2`,
  `research/retained-source-attacks-20261122/LEGAL_DESCENT.md`: arbitrary
  single-window deletion, residue records, and positive propagated debt.
- PR176, `fdcb137214f4be8ac30dbb025d6eeb6568e22e2a`,
  `research/lean-global-resolvent-20261121/overview/returns/WHOLE_SOURCE_DEBT_ATTEMPT.md`:
  prefixwise odd-count dominance and the exact debt with every parity
  disagreement retained.

Removing one gap four permits arbitrarily many newly inserted gaps at most
three. Thus an unbounded inverse subtree using only those smaller gaps, at
an appropriate supplied endpoint, would produce replacements larger than
any requested target without a length bound. This is a possible mechanism,
not an established property of those inverse trees. It must also apply at
the endpoint supplied by the actual extremal witness. An infinite tree at
one unrelated endpoint would not provide universal coverage.

Fixed-word pumping does not give this construction. If an inverse block
has affine form `F(x)=(2^A*x-C)/3^r`, with `r>=1`, all iterates can be integral only when
its starting integer agrees to arbitrarily high ternary precision with
`C/(2^A-3^r)`. Since `2^A` is a ternary unit, the familiar exact displacement
identity makes that conclusion immediate. The resulting fixed-point case
is not an expanding family of distinct sources. This is the inverse version
of the already published fixed-block precision argument, not a new
termination theorem.

Direct tree experiments also failed to supply a constructive invariant.
They were not used to infer infinity or to establish the theorem below.
In particular, surviving a finite search cutoff was never treated as
an unbounded ordinary source family.

## 2. A concrete improvement that was sought

PR182 at `9dacd610ba7735e89e2e29e4ab01795983317980`,
`research/lean-dyadic-descent-20261121/LITERATURE_CERTIFICATE_BRIDGE.md`,
proves an all-length, sharp source ceiling at an endpoint

`u=729j+7`, `q=(16u-1)/3`, `S=4q`.

Every strictly lower-grade replacement that retains the literal tail at
`u` satisfies `9S'+14<=8S`. Its earlier unbounded fully certified examples
use a large gap in that tail. I tried to remove this qualification by
constructing cofinally many actual complete cap-four sources in the
cylinder `u=7 mod729`. Such a construction would let the same interval
argument produce arbitrary finite target delays inside the bounded-four
source language. It would sharpen a known obstruction; it would not itself
prove universal Collatz convergence.

One attempted route was to combine an unbounded cap-four inverse tree with
a uniformly bounded return to this cylinder. The next calculation rules out
that uniform routing premise directly, at every proposed depth.

## 3. Exact all-depth forced-route control

An odd inverse edge has the form

`I_a(x)=(2^a*x-1)/3`.

Here a **unit edge** has positive odd integral output not divisible by three,
and its allowed exponent belongs to `{1,2,3,4}`.

**Proposition.** For every natural number `B`, there is a positive odd unit
`q_B` for which every unit inverse path of length at most `B` is forced,
and no such path reaches `7 mod729`.

**Proof.** Set

`q_B=2*3^(B+2)-1`

and, for `0<=i<=B`, set

`x_i=2^(i+1)*3^(B+2-i)-1`.

Every `x_i` is positive and odd, and `x_i=8 mod9`. At any input `x=8 mod9`,
exponents two and four fail integrality modulo three. Exponent three gives
an integer divisible by three. Exponent one gives an integer prime to
three. Thus exponent one is the only permitted unit edge.

For `i<B` the ordinary identities are exact:

`3*x_(i+1)+1=2*x_i`.

Consequently induction on the path length forces the inverse prefix to be
`x_0,...,x_i`. Every one of its vertices is eight modulo nine, whereas a
vertex seven modulo 729 is seven modulo nine. None is a target. This
includes the allowed empty path when `B=0`. All sources and intermediate
states are positive ordinary integers. QED.

More generally, if `v=v3(q+1)>=2`, any such route to a target outside
`8 mod9` has length at least `v-1`: the first `v-1` vertices follow the
same exact gap-one formula. These examples are different ordinary sources
as the proposed horizon changes. They do not produce one all-time avoiding
positive integer.

The control excludes a bound uniform over all unit roots. It does not
exclude logarithmic root-dependent routing, a return theorem restricted
to a suitable unbounded family, or a target-aware source transformation.
It also explains why enlarging a finite all-residue routing census cannot
repair this particular uniform claim.

## 4. Literature comparison and the remaining construction

[Weaver and Wren, *Exact avoidance in the Collatz inverse graph with
exponents at most four*, version 2](https://rstation.ai/problems/collatz/papers/96)
was read as an external primary research manuscript. It studies unit paths
and different targets, `11` or `19 mod27`. Its positive branching-root
routing theorem retains a logarithmic depth; the full integer avoidance
question reduces to a forced-only survivor. Those results do not assert
uniform routing to `7 mod729` or absence of positive integers in that
survivor. Its finite certificates and analytic claims were not replayed or
imported into Lean here. The elementary proposition above does not depend
on that manuscript.

The whole-source construction still needs an actual legal family that pays
its original multiset grade, reaches the required literal endpoint, and
captures the original target. Neither independent choices of inverse words,
finite survival of a cheap subtree, nor arbitrary real affine normalization
supplies those three facts simultaneously. No simultaneous multiwindow edit
with that property was found in this pass.

## 5. Formalization boundary

`ForcedRoute.lean` defines inverse equations with positive odd unit outputs
and arbitrary finite route words. The displayed initial states are proved
to be positive odd units, so the constructed routes are actual odd-map
paths at every vertex. Its twelve public statements verify the local exponent
classification, the explicit values, their positivity and residues, each
actual step, and existence of every prefix through the supplied depth.
An induction over an arbitrary supplied route proves that its word is
exactly the gap-one repetition and its endpoint is the displayed value.
The final theorem quantifies over every proposed horizon and every
permitted route through that horizon. No route conclusion is supplied as
an assumed hypothesis.

The module uses focused Mathlib `NormNum` and `Ring` imports, and no prior
project proof module. Development compilation with Lean 4.34.1, one compiler
thread, and warnings treated as errors passed. The parent checkpoint
records its separate fresh replay and exhaustive theorem dependency audit.
The integer family varies with the horizon. The theorem does not construct
an all-time inverse avoider, a nonconvergent positive integer, or a failed
query carrying the complete joint source-minimum hypotheses.
