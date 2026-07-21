# Namespaced Claim Inventory

These identifiers are reserved on the issue #10 branch and do not edit or
presume the competing canonical root ledgers.  All proof-looking claims remain
`PROPOSED` pending independent reconstruction.

## D-9101 — canonical regular-sanctuary semantics

- **Claim ID:** D-9101
- **Title:** Canonical LSD-first candidate language
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** none
- **Scope:** finite positive integers only
- **Related candidates:** none
- **Full record:** [`claims/D-9101-canonical-semantics.md`](claims/D-9101-canonical-semantics.md)

For a raw binary DFA `D`, define the represented candidate language as
`L(D) intersect {0,1}*1`, with values read least-significant digit first.
Empty words and terminal-zero padding are excluded.

## L-9101 — shortcut transducer correctness

- **Claim ID:** L-9101
- **Title:** Five-state subsequential realization of the shortcut map
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** all canonical positive finite binary words
- **Related candidates:** none
- **Full record:** [`claims/L-9101-shortcut-transducer.md`](claims/L-9101-shortcut-transducer.md)

The transducer table in `SEMANTICS.md` maps the canonical encoding of every
positive integer `n` to the canonical encoding of the shortcut Collatz value
`T(n)`.  The complete carry invariant and proof are in `SEMANTICS.md`; exact
integer comparison for `1 <= n < 100000` is experiment evidence, not the proof.

## L-9102 — exact closure decision

- **Claim ID:** L-9102
- **Title:** Product-graph decision of regular forward invariance
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9101
- **Scope:** any fixed complete finite DFA
- **Related candidates:** none
- **Full record:** [`claims/L-9102-closure-decision.md`](claims/L-9102-closure-decision.md)

For any fixed DFA `D`, finite product reachability decides exactly whether
`T(L_D) subset L_D` and reconstructs a canonical closure-violation word when the
inclusion fails.

## L-9103 — maximal safe kernel

- **Claim ID:** L-9103
- **Title:** Largest safe accepting set for a transition skeleton
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9102
- **Scope:** fixed DFA transition skeleton, forbidden words 1 and 01
- **Related candidates:** none
- **Full record:** [`claims/L-9103-maximal-safe-kernel.md`](claims/L-9103-maximal-safe-kernel.md)

If `R_D` is the exact terminal relation and `B` contains the states reached by
the forbidden words, then `Q minus Pre*_(R_D)(B)` is the unique largest
accepting set that is safe and forward invariant.

## L-9104 — short canonical witness

- **Claim ID:** L-9104
- **Title:** A nonempty q-state semantic DFA has a witness of length at most q
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101
- **Scope:** any complete q-state raw DFA under D-9101 semantics
- **Related candidates:** none
- **Full record:** [`claims/L-9104-short-witness-bound.md`](claims/L-9104-short-witness-bound.md)

The proof replaces the prefix before the final `1` by a shortest path to the
same DFA state.  The resulting canonical word has length at most `q`.

The 72-state search consequence uses the strict range `1 <= n < 2^71`, matching
Barina's stated contribution that all numbers below `2^71` were verified and
the limit reported in Section 6.  Broader citation admission remains subject
to issue #7; this external computation is not a dependency of the exact
candidate checker.

## L-9105 — fixed-block normalization

- **Claim ID:** L-9105
- **Title:** Every fixed-block regular sanctuary induces a one-step sanctuary
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** L-9101 and regular-image closure
- **Scope:** fixed positive block length B
- **Related candidates:** none
- **Full record:** [`claims/L-9105-fixed-block-normalization.md`](claims/L-9105-fixed-block-normalization.md)

If regular `L` avoids `{1,2}` and `T^B(L) subset L`, then the finite union of
its first `B` images is regular, avoids `{1,2}`, and is one-step invariant.

## L-9106 - odd-core equivalence

- **Claim ID:** L-9106
- **Title:** Shortcut sanctuaries are equivalent in existence to regular odd-core sanctuaries
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and elementary regular-language closure
- **Scope:** canonical positives; odd-only map `U(n)=(3n+1)/2^nu_2(3n+1)`
- **Related candidates:** none
- **Full record:** [`claims/L-9106-odd-core-equivalence.md`](claims/L-9106-odd-core-equivalence.md)

Intersecting a shortcut sanctuary with the odd positives gives a nonempty
regular `U`-invariant language excluding `1`.  Conversely, dyadic saturation
`0* O` turns every such odd language into a regular shortcut sanctuary.  A
seven-state totalized odd-core transducer and exact lift now support candidate
generation, while the standard shortcut verifier remains the trust boundary.

## L-9107 - dyadic-cylinder basin density

- **Claim ID:** L-9107
- **Title:** Every dyadic residue cylinder contains infinitely many trivial-basin values
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** elementary shortcut arithmetic and the order of 2 modulo powers of 3
- **Scope:** every fixed residue modulo `2^A`
- **Related candidates:** none
- **Full record:** [`claims/L-9107-dyadic-cylinder-density.md`](claims/L-9107-dyadic-cylinder-density.md)

For every `A,r`, infinitely many positive `n=r modulo 2^A` reach a power of
two.  No sanctuary can contain a full, or eventually full, dyadic cylinder;
this does not exclude general DFAs with unbounded high-bit dependence.

## L-9108 - finite-lasso obstruction

- **Claim ID:** L-9108
- **Title:** Forward-invariant finite unions of binary affine-geometric rays have only eventually periodic orbits
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101; slender corollary uses the external slender-regular decomposition theorem
- **Scope:** finite unions of exact rays; slender regular languages only via that decomposition
- **Related candidates:** none
- **Full record:** [`claims/L-9108-finite-lasso-obstruction.md`](claims/L-9108-finite-lasso-obstruction.md)

If a finite union of rays `A_i+B_i 2^(h_i k)`, up to a finite set, is shortcut
invariant, every orbit in it is eventually periodic.  Hence a nonempty safe
slender regular sanctuary would already certify a nontrivial positive cycle.

## L-9109 - conditional exact-floor normal form

- **Claim ID:** L-9109
- **Title:** A 72-state sanctuary at the verified-range floor has a full spine, accepting gate, and start-state zero loop
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9104, L-9106, external verification below `2^71`
- **Scope:** complete raw DFAs with exactly 72 states, conditional on the verified range
- **Related candidates:** none
- **Full record:** [`claims/L-9109-exact-floor-normal-form.md`](claims/L-9109-exact-floor-normal-form.md)

At equality in the conditional 72-state floor, the least accepted word has
length 72 and begins `11`; its prefix states have exact distances `0,...,71`
and force upper-Hessenberg transitions.  The final `1` is the unique
semantically relevant accepting gate, the start-state `0` transition is a
loop, and the first nonspine low edge cannot merge immediately into `q_2`.

## L-9110 - quotient monotonicity

- **Claim ID:** L-9110
- **Title:** Maximal semantic sanctuary kernels grow under right-congruence refinement
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and L-9103
- **Scope:** literal deterministic right-congruence refinements and quotients
- **Related candidates:** none
- **Full record:** [`claims/L-9110-quotient-monotonicity.md`](claims/L-9110-quotient-monotonicity.md)

If a right congruence `h'` refines `h`, every `h`-expressible sanctuary is
also `h'`-expressible, so their semantic maximal kernels satisfy
`K_h subset K_(h')`.  An empty kernel on a fine skeleton therefore cannot be
repaired by a literal deterministic quotient or transition-stable SCC merge.

## L-9111 - conditional odd-suffix floor

- **Claim ID:** L-9111
- **Title:** A fully accelerated odd sanctuary needs at least 71 suffix states, with a complete spine at equality
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9104, L-9106, L-9109, external verification below `2^71`
- **Scope:** complete DFAs reading the suffix after the forced low odd bit
- **Related candidates:** none
- **Full record:** [`claims/L-9111-odd-suffix-floor.md`](claims/L-9111-odd-suffix-floor.md)

Write every odd canonical word uniquely as `1x`, and let a `p`-state DFA read
only `x`. Adjoining one zero-loop state recognizes the dyadic saturation with
exactly `p+1` raw states. Conditional on the verified range, `p>=71`. At
equality the 71 suffix-prefix states are exact-distance and exhaustive; the
singleton semantic gate is one of `r_2,...,r_70`. This is a necessary normal
form for a structured lift, not a claim about every raw 72-state machine.

## L-9112 - depth-colored residual refinement

- **Claim ID:** L-9112
- **Title:** First-hit colors turn finite safety automata into a canonical refinement chain
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and L-9110; external verification below `2^71` only for the conditional `d<=69` corollary
- **Scope:** finite canonical words and every finite shortcut-safety horizon
- **Related candidates:** none
- **Full record:** [`claims/L-9112-depth-colored-residual-refinement.md`](claims/L-9112-depth-colored-residual-refinement.md)

Minimal Boolean safety DFAs need not refine one another. Retaining each word's
first-hit depth yields Moore skeletons `H_d` with canonical strict surjections
`H_(d+1) -> H_d`; their inverse fibers are exact inter-depth split objects.
The bare skeletons express only finite or cofinite semantic languages, so they
cannot directly host an infinite sanctuary. Their sound use is as feature
coordinates in reachable products `R product H_d` with a genuinely recurrent
noncofinite skeleton `R`.

## L-9113 - reset-pattern concrete-clause blind spot

- **Claim ID:** L-9113
- **Title:** A fixed odd-suffix gate has exponentially many reset-pattern models that concrete implications must address
- **Status:** PROPOSED
- **Authoring agent:** codex-reset-spine
- **Reviewing agents:** adversarial proof reconstruction by `widening_lemma/proof_audit`; artifact audit by `artifact_audit`
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101, L-9101, L-9102, L-9106, and L-9111
- **Scope:** odd-suffix normal-form candidates and concrete suffix-implication banks
- **Related candidates:** none
- **Full record:** [`claims/L-9113-reset-spine-bank-blind-spot.md`](claims/L-9113-reset-spine-bank-blind-spot.md)

Every fixed gate has `2^(q-3)` reset-pattern normal-form models, and every
accepted canonical antecedent must contain its model's distinct length-`q`
pattern.  A concrete bank with fewer distinct factors therefore cannot
eliminate that gate.  At `q=71`, the frozen 224-clause corpus has 1,692 such
factors; even after adding 69 targeted clauses, an explicit evader remains at
every gate.  The distinguished spines are exactly rejected countermodels, not
sanctuaries.

## L-9114 - gate-two carry elimination

- **Claim ID:** L-9114
- **Title:** The accepting gate cannot be the second suffix-spine state
- **Status:** PROPOSED
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** independent carry reconstruction by `structured_templates`; artifact audit by `artifact_audit`
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** D-9101 and the syntactic normal form stated in L-9111
- **Scope:** complete odd-suffix DFAs with the exact-distance spine constraints
- **Related candidates:** none
- **Full record:** [`claims/L-9114-gate-two-carry-elimination.md`](claims/L-9114-gate-two-carry-elimination.md)

The exact-distance output-length budget and an elementary ripple-carry
induction rule out accepting gate `r_2`.  Thus the active `q=71` structured
suffix gates are `3,...,70`.  Only the corresponding structured raw-gate-3
lift is excluded; generic raw gate-3 machines remain outside the theorem.

## X-9101 — exact checker, structural tooling, and bounded searches

- **Claim ID:** X-9101
- **Title:** Regular-sanctuary transducers, exact verifiers, and bounded synthesis
- **Status:** EMPIRICAL
- **Authoring agent:** gpt56-regular-01
- **Reviewing agents:** none
- **Created:** 2026-07-21
- **Last updated:** 2026-07-21
- **Dependencies:** experiment source and Python 3.12 standard library; optional
  `z3-solver==4.16.0.0` only for proposal synthesis
- **Scope:** parameters frozen in the result JSON artifacts named by the
  experiment README
- **Related candidates:** none
- **Full record:** [`../../experiments/X-9101-regular-sanctuary/README.md`](../../experiments/X-9101-regular-sanctuary/README.md)

The baseline reproduced the `3n-1` control, found no nonempty safe kernel among
all 66,282 labeled standard-map skeletons through four states, and found none
for every one- and two-state core behind the specified 72-bit guard.  The
extended suite contains 104 tests, including exact odd-core/suffix-lift
checks, portable-bank validation, trie-batched implication equivalence, and
differential agreement between two closure routes on all 5,898 complete DFA
candidates (746 labeled skeletons through three states, each with every
accepting mask).  A two-session, gate-0 exact-floor scout checked and
rejected 22 proposed 72-state machines and learned 213 exact implications
before its 120.062-second cumulative time boundary.  This is a bounded result
with status `time_limit`, not UNSAT. A seeded raw gate-3 scout checked two
models and learned three additional clauses; a seeded 71-state suffix-gate-2
scout checked five models and learned 11 additional clauses. Both stopped at
20-second soft boundaries and found no candidate.

The paired generation-zero census completed all 138 suffix/raw partitions,
exactly rejected all 138 one-model proposals, recorded 1,855 local implication
instances, and had no zero-model stall.  Every planned partition has one
rejected proposal, but none is eliminated.  The
reset-spine audit finds only 1,692 distinct length-71 factors in the 224-clause
corpus versus `2^68` required to cover any fixed gate by concrete antecedents.
The symbolic minimum-word artifact records gate 2 as solver-UNSAT and 68
exactly rejected satisfiable countermodels at gates 3 through 70; only L-9114's
separate carry proof eliminates gate 2.

## Gap audit

- No such standard-Collatz language was found or claimed; no `K-####` record
  exists.
- In-session adversarial reconstruction found and repaired checker bugs.  The
  second preimage/inclusion route shares the project's `preimage_dfa` builder
  and author, so no independent reviewer artifact has entered the repository.
- External literature and the `2^71` bound are not yet admitted through issue
  #7's audit.
- The small-core guard templates are extremely restrictive.
- Dyadic cylinders and eventually fixed-modulus tails are excluded by L-9107,
  but arbitrary regular high-bit tail machines remain open.
- Finite-lasso and slender regular templates are excluded by L-9108 unless
  they already contain a nontrivial cycle; nonslender regular languages remain
  open.
- L-9109 is conditional on the external verified range and constrains only the
  exact 72-state floor.
- L-9110 excludes only literal quotients of an empty-kernel skeleton;
  refinements, feature products, and transition redesigns remain available.
- L-9111 is conditional and covers only exact-floor suffix lifts, not raw gate
  0 or every generic 72-state table.
- L-9112's colored skeletons grow strictly and directly express only finite or
  cofinite languages; product synthesis remains an open empirical direction.
- L-9113 bounds concrete antecedent-factor coverage only.  Symbolic transition
  clauses and direct arithmetic contradictions lie outside its scope.
- L-9114 assumes the exact-floor suffix normal form.  It does not exclude
  larger suffix DFAs or generic raw gate-3 machines.
- The optional CEGIS solver emits no independently checkable UNSAT proof, and
  every committed scout remains explicitly bounded and partition-specific.
- No bounded failure is extrapolated to arbitrary regular languages.
- The first safety approximants are finite-horizon objects and do not determine
  an ordinary integer surviving forever.
