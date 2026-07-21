# L-9110 - Quotient monotonicity

- **Claim ID:** L-9110
- **Title:** Maximal semantic sanctuary kernels grow under right-congruence refinement
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and L-9103
- **Scope:** literal deterministic right-congruence refinements and quotients of a fixed transition skeleton
- **Related counterexample candidates:** none

## Statement

Let `h: {0,1}* -> Q` and `h': {0,1}* -> Q'` be the reachable-state maps of
finite complete deterministic transition skeletons.  Suppose `h'` refines
`h`, meaning

$$
h'(u)=h'(v)\quad\Longrightarrow\quad h(u)=h(v).
$$

Equivalently, there is a surjective transition-preserving map
`pi: Q' -> Q` with `h=pi composed with h'`.

Let `K_h` denote the largest semantic language expressible by choosing an
accepting set on `h` that is shortcut invariant and excludes `{1,2}`; define
`K_(h')` similarly.  Then

$$
K_h\subseteq K_{h'}.
$$

Consequently, if the maximal kernel is empty on a fine skeleton, every literal
deterministic quotient of that skeleton also has empty maximal kernel.

## Definitions

An `h`-expressible semantic language has the form

$$
L_F=\{w\in\mathcal C:h(w)\in F\}
$$

for some `F subset Q`.  The word **semantic** is important: unreachable raw
states and noncanonical words do not contribute to `K_h`.

A literal quotient merges states by a transition-stable equivalence, so its
projection commutes with both binary transitions.  An arbitrary state merge
followed by repaired or redirected transitions is a new skeleton, not a
quotient in this claim.

## Motivation

Finite-horizon safety automata can be large, and merging their SCCs is an
attractive widening heuristic.  The lemma shows that literal quotienting
cannot create a sanctuary once the finer skeleton's maximal accepting kernel
is already empty.  Useful generalization must instead add or rearrange
distinctions rather than merely forget them.

## Proof or construction

Take any `h`-expressible sanctuary `L_F`.  Set

$$
F'=\pi^{-1}(F)\subseteq Q'.
$$

For every raw word `w`,

$$
h'(w)\in F'
\quad\Longleftrightarrow\quad
\pi(h'(w))=h(w)\in F.
$$

Thus `F'` expresses exactly the same raw language, and therefore exactly the
same canonical semantic language, on the refined skeleton.  Its arithmetic
safety and shortcut invariance are unchanged.  Every `h`-expressible
sanctuary is consequently `h'`-expressible.

For a fixed finite skeleton, the union of all expressible sanctuaries is again
expressible by the union of their accepting sets.  It remains safe and forward
invariant, so it is the semantic maximal kernel computed by L-9103.  Since
`K_h` is one of the sanctuaries expressible on `h'`, maximality gives
`K_h subset K_(h')`.

If `h` is a quotient of `h'` and `K_(h')` is empty, the inclusion forces
`K_h` to be empty.

## Dependency audit

- D-9101 supplies semantic intersection with canonical positive words.
- L-9103 identifies the largest safe accepting set on each fixed skeleton.
- The pullback `pi^(-1)(F)` is elementary DFA homomorphism theory; no Collatz
  orbit premise or external citation is used.

## Gap audit

- The empty object must be the **maximal kernel of the transition skeleton**,
  not merely the particular accepting set defining a finite-horizon language.
- A proposed SCC partition must be transition stable to be a literal
  deterministic quotient.
- Refinements, products with new features, added states, altered transitions,
  nondeterministic abstractions, and independently learned automata are not
  excluded.
- Minimized automata at different safety depths need not form a refinement
  chain, so the lemma cannot compare them without an explicit homomorphism.

## Adversarial tests

- Pulling a coarse accepting set back along `pi` gives word-for-word equality,
  not merely inclusion; this checks the orientation of the refinement claim.
- The converse monotonicity is false in general: splitting states can express
  accepting sets unavailable after merging.
- Merging two states whose outgoing transitions land in different quotient
  blocks is outside the theorem because no deterministic quotient map exists.

## Remaining uncertainty

The proof appears complete.  Its practical force depends on checking and
recording explicit quotient homomorphisms rather than relying on visual SCC
similarity.

PR #14's independently proposed L-9201 is complementary evidence for the
specific finite-safety family: it reconstructs those automata from reverse
trees and proves that their only within-depth cyclic SCC is the cofinite
canonical tail.  That result is not a dependency here and does not promote
either claim; it identifies the tail that should be stripped before seeking
inter-depth structure.

## Suggested next attack

Compare PR #14's sink-stripped boundary DAGs across depths.  If a motif
recurs, use it to propose a non-cofinite refinement, feature product, or
transition redesign and return that proposal to the exact checker.  Treat no
literal quotient as capable of repairing an empty fine-skeleton kernel.
