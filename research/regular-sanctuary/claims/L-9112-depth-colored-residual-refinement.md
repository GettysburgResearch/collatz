# L-9112 - Depth-colored residual refinement

- **Claim ID:** L-9112
- **Title:** First-hit colors turn finite safety automata into a canonical refinement chain
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and L-9110; the `d<=69` corollary additionally uses external verification below `2^71`; motivated by PR #14's sink-stripped safety construction
- **Scope:** finite canonical LSD-first words and every finite shortcut-safety horizon
- **Related counterexample candidates:** none

## Statement

Let

$$
\tau(n)=\min\{j\geq 0:T^j(n)\in\{1,2\}\},
$$

with `tau(n)=infinity` if the set is empty.  For every horizon `d >= 0`, color
every raw binary word `w` by

$$
c_d(w)=
\begin{cases}
\bot,&w\text{ is not a canonical positive word},\\
j,&w\text{ encodes }n\text{ and }\tau(n)=j\leq d,\\
\star_d,&w\text{ encodes }n\text{ and }\tau(n)>d.
\end{cases}
$$

For `k>=0`, define the Boolean finite-horizon safety language

$$
S_k=\{w\in\mathcal C:\tau([w])>k\}.
$$

Let `H_d` be the minimal reachable deterministic Moore automaton computing
`c_d`.  Then:

1. `H_d` is finite.  Its only cyclic strongly connected component is the
   two-state canonical tail; deleting that component leaves a boundary DAG.
2. The right congruence of `H_(d+1)` refines that of `H_d`.  There is a unique
   surjective transition homomorphism

   $$
   \pi_{d+1,d}:H_{d+1}\longrightarrow H_d
   $$

   that sends the state reached by a prefix `p` to the state reached by the
   same prefix in `H_d`.  Its colors satisfy
   `out_d(pi_(d+1,d)(q'))=rho_d(out_(d+1)(q'))`, where `rho_d` is the color
   truncation defined below.  Thus this is a transition-skeleton homomorphism,
   not an output-preserving Moore homomorphism between different color sets.
3. If `C_d` is the two-state tail and `B_d` is the remaining boundary, then
   `pi_(d+1,d)(C_(d+1))=C_d` and the next boundary has the canonical disjoint
   decomposition

   $$
   B_{d+1}
   =\pi_{d+1,d}^{-1}(B_d)
   \;\dot\cup\;
   \left(\pi_{d+1,d}^{-1}(C_d)\setminus C_{d+1}\right). \tag{1}
   $$

   The second term is the exact new frontier: distinctions that horizon `d`
   collapsed into its cofinite tail but horizon `d+1` exposes.  It is nonempty
   at every depth, so each displayed refinement is strict.  In particular,
   `|H_(d+1)|>|H_d|`; the colored ladder itself never stabilizes as a finite
   automaton.
4. For every `k <= d`, the Boolean safety language `S_k` is recognized on
   `H_d` by accepting precisely the colors

   $$
   \{k+1,k+2,\ldots,d,\star_d\}.
   $$

   Consequently, the ordinary minimal Boolean DFA for `S_k` is a literal
   deterministic quotient of `H_d`.
5. Writing `K_d` for the maximal semantic sanctuary kernel expressible on the
   transition skeleton of `H_d`, L-9110 gives

   $$
   K_d\subseteq K_{d+1}.
   $$

6. The direct skeleton `H_d` cannot express an infinite noncofinite semantic
   language.  Accepting its final-`1` tail state makes the language cofinite;
   rejecting that state leaves only finitely many accepted canonical words.
   Thus any nonempty sanctuary expressible directly on `H_d` already contains
   a nontrivial positive cycle.  Conditional on verification below `2^71`,
   `K_d` is empty for every `d<=69`.
7. For any fixed complete deterministic skeleton `R`, let `G_d` be the
   reachable product skeleton `R product H_d`.  Then `G_(d+1)` refines `G_d`
   through the restriction of `id_R product pi_(d+1,d)` to reachable product
   states, and its maximal kernels are monotone.  These products, rather than
   bare `H_d`, are the exact synthesis ladder.  A recurrent `R` coordinate can
   let the product skeleton express infinite noncofinite distinctions, while
   the `H_d` coordinate supplies canonical finite-safety features.

Thus the colored automata, unlike the independently minimized Boolean safety
DFAs, form an exact feature-refinement ladder.  The fibers of `pi_(d+1,d)` are
canonical, state-label-independent split certificates for inter-depth
comparison.  Their automata grow strictly forever, so only recurring fiber
motifs or product features—not stabilization of `H_d` itself—can support a
finite PDR-style conjecture.

## Why Boolean minimization loses the map

The safety languages are nested, but their minimal Boolean right congruences
need not be.  This already occurs at depths zero and one.  In LSD-first form,

~~~text
F_0 = {1, 01}
F_1 = {1, 01, 001}.
~~~

For `S_0`, the prefixes `1` and `00` have the same residual: both reject the
empty continuation and accept exactly the nonempty continuations ending in
`1`.  For `S_1`, suffix `1` distinguishes them because `11` encodes the safe
value `3`, whereas `001` encodes the forbidden value `4`.

In the opposite direction, `1` and `001` have the same residual for `S_1`:
both are exact forbidden words with no forbidden extension.  They differ for
`S_0`, where `001` itself is accepted and `1` is not.  Hence neither ordinary
minimal DFA refines the other.  An attempted state-by-state embedding between
those Boolean machines is therefore not canonical even at the first step.

The colors retain the reason for rejection: noncanonical, first hit at time
zero, first hit at time one, and so on.  That information is exactly what
restores refinement.

## Proof

### Finiteness and the tail

For fixed `d`, the set

$$
F_d=\{n:\tau(n)\leq d\}
$$

is finite.  Because `{1,2}` is forward invariant,

$$
F_0=\{1,2\},\qquad F_{d+1}=T^{-1}(F_d).
$$

Each positive target has the even preimage `2n` and at most one positive odd
preimage `(2n-1)/3`; iterating this finite branching operation only `d` times
gives a finite set.  Moreover,

$$
\max F_d=2^{d+1}. \tag{2}
$$

Indeed the formula holds at depth zero.  Every predecessor of `y` is at most
`2y`, while the even predecessor of `max F_d` attains `2 max F_d`.  Thus
`max F_(d+1)=2 max F_d`, and induction proves (2).

Let `P_d` be the finite prefix closure of the canonical encodings of `F_d`.
If `p` is not in `P_d`, no continuation of `p` encodes a member of `F_d`, so
its residual depends only on the final bit.  Thus every non-tail state has a
representative in `P_d`, while all other prefixes enter two final-bit tail
states.  At either tail state, the empty continuation has color `bot` or
`star_d` according as the prefix ends in `0` or `1`; every nonempty
continuation is classified by its own final bit.  The states are distinct,
and from either one input `0` reaches the first while input `1` reaches the
second.  They form the canonical tail.

If a state outside that tail lay on a directed cycle, a word reaching it
followed by arbitrarily many repetitions of a nonempty cycle label would give
arbitrarily long prefixes whose residual stayed outside the tail.  This
contradicts the preceding paragraph.  The remaining boundary is a DAG.

### Refinement and the canonical projection

There is a fixed color truncation

$$
\rho_d:\{\bot,0,\ldots,d+1,\star_{d+1}\}
\longrightarrow\{\bot,0,\ldots,d,\star_d\}
$$

that fixes `bot` and `0,...,d` and sends both `d+1` and `star_(d+1)` to
`star_d`.  Pointwise,

$$
c_d=\rho_d\mathbin{\circ}c_{d+1}. \tag{3}
$$

The minimal Moore right congruence is

$$
u\equiv_d v
\quad\Longleftrightarrow\quad
c_d(ux)=c_d(vx)\text{ for every suffix }x.
$$

If `u` and `v` are equivalent at depth `d+1`, applying (3) for every suffix
shows that they are equivalent at depth `d`.  Therefore

$$
[u]_{d+1}\longmapsto [u]_d
$$

is well defined.  It is onto because every reachable shallow state has a
prefix representative, and it commutes with both transitions by
construction.  Reachability also makes it the unique homomorphism having the
stated prefix property.

The two tail residuals plainly map to their same-final-bit counterparts.
Every deeper state maps either to the old boundary or to the old tail; after
removing the two deeper tail states, this dichotomy is exactly (1).

The canonical word for `2^(d+2)` has length `d+3`, greater than the maximum
word length `d+2` in `F_d` by (2), so it reaches the final-`1` tail state of
`H_d`.  Its first hit occurs at time `d+1`, so in `H_(d+1)` the same word has
output color `d+1` rather than `star_(d+1)` and reaches a boundary state.
That state belongs to the second term of (1), proving that the new frontier is
nonempty and that `pi_(d+1,d)` is not injective.
Because the map is a surjection between finite state sets, noninjectivity also
gives `|H_(d+1)|>|H_d|`.

### Boolean safety quotients and kernel monotonicity

For a canonical word encoding `n`, membership in `S_k` means `tau(n)>k`.
When `k<=d`, this is exactly the displayed union of output colors.  Treating
those Moore colors as accepting states turns `H_d` into a DFA for `S_k`.
The minimal DFA for `S_k` is therefore its standard reachable deterministic
quotient.

Finally `H_(d+1)` refines `H_d`, so the pullback argument of L-9110 applies to
every accepting set, not just the safety-color set.  Every sanctuary
expressible on `H_d` remains expressible on `H_(d+1)`, proving
`K_d subset K_(d+1)`.

### Direct-language obstruction and product refinement

Put `ell_d=d+2`, the maximum bit length of a value in `F_d` by (2).  Every
canonical word longer than `ell_d` reaches the final-`1` canonical-tail state
of `H_d`.  If that state is accepting, the semantic language contains every
sufficiently long canonical word and is cofinite.  Forward invariance then
propagates an accepted sufficiently large power of two into `{1,2}`, so the
language is unsafe.

If the final-`1` tail state is rejected, every accepted canonical word ends in
the boundary DAG and has length at most `ell_d`.  There are only finitely many
such words.  Every nonempty finite forward-invariant set contains an eventual
cycle, and safety makes that cycle nontrivial.  This proves the direct
obstruction in item 6.

Under the external premise that every positive integer below `2^71` reaches
the trivial cycle, for `d<=69` every boundary-ending canonical
word has length at most `d+2<=71`, hence value strictly below
`2^(d+2)<=2^71`.  The finite alternative is therefore impossible as well, so
the semantic maximal kernel `K_d` is empty.  The endpoint `d=69` is included:
a 71-bit positive integer is still strictly below `2^71`.

Now fix any deterministic skeleton `R`.  The reachable state maps of the
products are

$$
g_d(w)=(r(w),h_d(w)).
$$

Equality under `g_(d+1)` implies equality of the `R` coordinates and, by the
proved refinement, equality of the `H_d` coordinates.  Thus `G_(d+1)` refines
`G_d`; on reachable pairs its projection is

$$
(r,q')\longmapsto(r,\pi_{d+1,d}(q')).
$$

The map is onto because every shallow reachable pair has a prefix witness and
the same prefix reaches a deep pair above it.  L-9110 therefore gives monotone
maximal kernels on the product chain.  Unlike a bare safety skeleton, the
product can retain distinctions on arbitrarily long canonical words when `R`
carries recurrent noncofinite distinctions.

## Exact construction and proposal generator

The chain can be built without comparing arbitrary state labels.

1. Reverse-BFS from `{1,2}` and record the first level at which each integer
   appears.  This level is its exact finite `tau` color.
2. Build the trie of the canonical encodings with `tau<=d`.  Give each node
   its whole-word color: `bot` after an empty or final-zero word, its exact
   `tau` at a forbidden terminal, and `star_d` at every other canonical node.
   Send every missing edge to the appropriate final-bit tail state.
3. Moore-minimize by the exact signature

   ~~~text
   (output_color, zero_child_block, one_child_block).
   ~~~

   Because the non-tail part is acyclic, the same result can be obtained by
   bottom-up structural hash-consing with the two tail states as fixed atoms.
   Structural tuples, rather than a cryptographic digest alone, are the proof
   objects.
4. Compute `pi_(d+1,d)` by synchronous BFS from the two start states.  Each
   deep state must pair with exactly one shallow state; failure is an exact
   implementation error.  The inverse fibers and decomposition (1) are the
   canonical inter-depth fingerprints.
5. Use the bare `H_d` maximal kernel only as an obstruction/control; under the
   verified-range premise it is already empty through `d=69`.  For synthesis,
   choose a genuinely recurrent skeleton `R`, form the reachable products
   `R product H_d`, and run the existing maximal-safe-kernel construction on
   those products.  Advance by the proved product refinement and submit every
   nonempty semantic result immediately to the unchanged exact shortcut
   verifier.  No finite-depth color or solver status substitutes for that
   certificate.

This is a proposal generator rather than a convergence argument.  Its value
is that every step is a proved refinement, so state splits have exact ancestry
and L-9110 applies with the correct orientation.  Since the `H_d` state counts
increase strictly, a finite conjecture must be distilled from recurring split
features or supplied by `R`; it cannot be justified by stabilization of the
colored automata themselves.

## Dependency audit

- D-9101 supplies canonical LSD-first semantics.
- L-9110 supplies maximal-kernel monotonicity once the explicit homomorphism
  is proved.
- The external verification below `2^71` supplies only the conditional empty-
  kernel corollary through depth 69; the colored refinement theorem is
  unconditional.
- PR #14 (`cursor/sink-stripped-pdr-8f0f`) independently establishes the
  cofinite-tail and boundary-DAG view for the Boolean `S_d` automata and
  motivates stripping the two universal tail states.  The refinement proof
  above is self-contained and does not assume its depth-32 data.
- Apart from the explicitly conditional `d<=69` corollary, no verified
  Collatz range or convergence premise is used.

## Gap audit

- The refinement chain is for the depth-colored Moore skeletons, not for the
  independently minimized Boolean `S_d` automata.  The explicit depth-zero/
  depth-one example shows why that distinction is necessary.
- A projection is not an injection.  The canonical inter-depth objects are
  its inverse fibers and the old-boundary/new-frontier decomposition, not an
  arbitrarily chosen representative state.
- `K_d` may remain empty at every computed depth.  No infinite noncofinite
  sanctuary can become expressible on a bare `H_d`, and no completeness claim
  is made for the product templates.
- In fact a bare `H_d` expresses only cofinite or finite semantic languages,
  and its state count grows strictly with `d`.  It is a source of canonical
  features, not a direct infinite-sanctuary template or a stabilizing finite
  invariant.
- The two-state tail is still the cofinite artifact identified by PR #14; it
  is retained while constructing the homomorphism and stripped only when
  reporting boundary structure.
- Literal quotients of an empty-kernel `H_d` cannot help by L-9110.  Useful
  moves are the proved refinement to `H_(d+1)`, a feature product, or a genuine
  transition redesign.

## Adversarial checks

- Verify the two non-refinement pairs `1` versus `00` and `1` versus `001`
  directly before trusting any Boolean inter-depth state map.
- For every constructed adjacent pair, synchronous product reachability must
  associate each deep state with exactly one shallow state and must cover all
  states of both machines.
- Color truncation must commute at every paired state, and both labeled
  transitions must commute with `pi_(d+1,d)`.
- The new-frontier term in (1) may be nonempty: deeper boundary states are
  allowed to map to the shallower tail.  Reject implementations that assume a
  total boundary-to-boundary map.

## Remaining uncertainty

The theorem and construction appear complete, but no separately authored
implementation or proof review has yet been committed.  The synthesis power
of the resulting refinement ladder is an empirical question.

## Suggested next attack

Implement the colored trie/minimizer beside X-9101 and validate the projection
contract through PR #14's frozen depth range.  Use newly exposed fibers as a
feature coordinate in products with nonslender odd-core or other genuinely
recurrent skeletons, then compute the exact maximal kernel on each product.
Rank repeated fiber motifs by their transition interaction with the previous
boundary, but promote only a nonempty kernel accepted by the standard
verifier.

The smallest concrete recurrent control is **popcount parity**:

$$
R=\mathbb Z/2\mathbb Z,\qquad
\delta(r,0)=r,\quad \delta(r,1)=r+1\pmod 2.
$$

Both parity classes contain exponentially many arbitrarily long canonical
words and neither is determined by a fixed low-bit cylinder, so this product
is outside the scopes of L-9107 and L-9108.  Powers of two occupy only the
popcount-one canonical-tail fiber, leaving the other fiber available to the
exact kernel calculation.  Start with `R product H_24`, replaying depths
`8,12,16,20` as controls, and then try the four-state statistic that records
the parity of adjacent `11` occurrences.  Empty kernels remain bounded
negative results; the first interesting signal is a proper nonempty set of
canonical tail fibers, followed immediately by full exact verification.
