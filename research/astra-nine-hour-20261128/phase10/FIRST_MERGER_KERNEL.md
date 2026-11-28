# First mergers at actual nonperiodic Collatz targets

`FirstMerger.lean` proves the deterministic graph fact used by the ordinary
collision-energy argument. It then specializes the result to the actual
valuation-defined accelerated map

\[
 U(x)=(3x+1)/2^{v_2(3x+1)}.
\]

The theorem keeps the two source clocks separate. If two fixed source paths
enter distinct immediate predecessors of a nonperiodic target, they cannot
also enter distinct immediate predecessors of a different nonperiodic target.
The first target and both incoming vertices are unique. It is not necessary
for the two sources to arrive at the same time.

The proof first establishes uniqueness of a hitting time at a nonperiodic
target. It derives disjointness of the predecessor cones of distinct parents,
then compares two alleged merger dates on one source path. If those dates
differ, determinism forces the other source to hit the later target through
the same parent, a contradiction.

This is the exact combinatorial reason the ordered source-pair events in
[the ordinary collision-energy proof](../escape/phase10/ORDINARY_COLLISION_ENERGY.md)
are disjoint. The subsequent natural-density bound, dominated convergence,
operator recursion, and identification of the escape flux are written
arguments; this module does not formalize that analysis.

The complete module, including the actual `padicValNat` formula, passed a
strict local development compile with the pinned Lean and Mathlib versions.
The next checkpoint's isolated all-module replay is the authoritative
publication receipt. No assumption that every Collatz orbit terminates or
that only one positive cycle exists is used.
