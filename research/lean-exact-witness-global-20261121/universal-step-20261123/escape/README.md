# Ordinary escape: exact sibling collapse and a complete inverse-tree compiler

23 November 2026. **Escape exclusion and full Collatz remain OPEN.**

This attack keeps one fixed ordinary source and its full predecessor
basins. It develops two written all-parameter results:

1. [Summable sibling Green ratios](SIBLING_BASIN_COLLAPSE.md). For the
   actual escape pressure measure, basin mass is exactly
   `A(q)=mu(q) Z_s(q)`. The upper sibling subtrees of all points on one
   forward ray are pairwise disjoint. Consequently

   `sum_j sum_(h>=1) 64^(-hs) Z_s(S^h q_j)/Z_s(q_j)`

   is at most `(1-A(q_0))/A(q_0)`, where `S(q)=64q+21`. In particular
   a fixed-sibling ratio is summable along the unchanged ray. An ordinary
   lower comparison of order `1/(log q log log q)` would contradict this;
   the exact nonsingular denominator is stated in the note.
2. [Balanced complete inverse-tree transport](BALANCED_INVERSE_TRANSPORT.md).
   Every legal unit parent has a unique address `(c,j)` with actual
   parent colour `c mod 3` and exponent `e_c(q)+6j`. Matching this address
   between two roots in the same class modulo three recursively bijects
   their complete ordinary inverse path trees. The signed exponent cost
   is in `{-4,-2,0,2,4}` per edge. The exact weight multiplier is
   `2^(-s Delta)`, and an explicit physical-height cocycle retains the
   transported source. There is no collision loss or finite-exponent cap.

The compiler improves on changing the sibling to `S^(3^d)q` merely to
preserve a depth-d congruence. It does **not** yet amortize its signed
cost on the actual full predecessor pressure law. That estimate is the
unproved closing step; the presence of positive and negative costs is
not an independence or cancellation theorem.

The [finite checker](check_balanced_transport.py) exhausts the twelve
unit-residue/parent-colour entries and tests 1,554 explicitly scoped
paired ordinary paths with exact rational arithmetic. It rejects three
corrupted tables and passes identically with normal and optimized Python.
The complete infinite mathematics is written, not Lean-formalized.

The latest inspected PR180 source and Assani's nonsingular-operator paper
are pinned in the notes and [source ledger](../../../../reports/lean-exact-witness-global-20261121/universal-step-20261123/escape/SOURCES.json).
No recurrence, power bound, stationary drift classification, or Haar
regularity is silently imported as an ordinary sibling comparison.
