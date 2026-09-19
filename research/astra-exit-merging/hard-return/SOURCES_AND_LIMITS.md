# Sources, status and evidence limits

All AHR-001--005 statements and the countercontrol argument are **PROPOSED
pending independent mathematical review**. The proofs are elementary and
self-contained. No computation or external theorem is a mathematical premise.
No exhaustive external novelty or priority claim is made.

## Exact parent and related sources

- Parent PR #122, `65c91ecea97d9ebf931eb1d9284b7950182a298e`,
  `research/astra-exit-merging/PROOF.md`: AEM-003 entry bridge, AEM-004
  one-third companion, AEM-005 source/clock distinctions. This continuation
  restates the required arithmetic and preserves every parent file and status.
- Strategy issue #121 supplies the immutable-source and compositional objective.
- Sodelin/Collatz-Conjecture-Work at
  `026aa4ad4be6453a005ab950b160a9f2204c5271`,
  `proof-search/lemmas/L6_Minimal_Counterexample_Exit_Constraint.md`: prior
  good odd-exit identity credited by the parent.
- Same external pin, `proof-search/lemmas/L13_Refined_Mersenne_Child_Macros.md`,
  read in this continuation: guarded child macros and exact successor
  normalization, including warnings about growing local ranks and changed
  labels. Its claimed Lean receipts were NOT rebuilt here. It is context,
  not a premise or an independent review of this new packet.

A bounded web search for paired Collatz coalescence and hard exits was used for
context. It is not an exhaustive priority audit. The new role-swapping assembly
must not be marketed as a known-new theorem on that basis.

## Actual computational scope

The native corpus has 635 family case rows (634 distinct parameter tuples;
one k=82 example is intentionally repeated as a named stress case). There
are 113 rows under the sufficient no-forward-descent threshold and 304 rows
with at least one growing return. The generator and verifier reconstruct:

- all C in 1..65536 with a stage budget of eight: 2114 merging and 63422
  outside-language results;
- all k=1..6 and odd u in 1..4095: 12288 ambient inputs. Of these, 11520
  fail the entry guard, 381 satisfy the parent's separate good-exit guard,
  11 are newly merged by this language, and 376 remain outside it;
- full controls for 3003/999 and 128/14, 21 compiled label patterns,
  and long-budget controls that deliberately return unfinished.

These are local certificate classifications, not a convergence census, survivor
bound, density estimate or fraction of Collatz solved. Complete finite rows
are reproducible with `run.py --full`; their hashes are in the canonical file.

The verifier independently solves for u rather than the generator's C, compiles
cylinders forward rather than backward, reconstructs actual parities and affine
endpoints, and checks the lower-source inequality using integers. Sixteen
resealed corruptions plus four direct bad witnesses are rejected in its
self-test. Same-author implementation diversity is NOT independent mathematical
peer review or formal verification.

Before publication, an initial generator draft used a floating comparison
`x<n/3`; giant integers exposed rounding at this boundary. It was replaced
by the exact integer comparison `3*x<n`, then all final runs were repeated.
No theorem, existing source, or published artifact used that draft failure.

## Execution and publication boundaries

See `reports/astra-exit-merging-02/validation.json` for commands and receipts.
No complete-checkout root validator, external Lean build, browser test or CI
run is attributed to this authoring pass. Direct Git failed DNS; GitHub API
access was available. The parent's publisher validation belongs to the parent,
not automatically to this addition. Remote file identities must be checked
separately when this packet is published.

No main branch, canonical status, old proof, workflow, setting, license or
other contributor's PR is changed. Review should prioritize the role swap,
compiler completeness, physical clock composition, and the all-states lower
bound; a successful finite replay cannot establish their universal quantifiers.
