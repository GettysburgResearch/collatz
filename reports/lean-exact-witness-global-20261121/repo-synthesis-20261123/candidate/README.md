# Joint-edit compiler: execution and scope

The scientific argument and exact interfaces are in
[`JOINT_EDIT_COMPILER.md`](../../../../research/lean-exact-witness-global-20261121/repo-synthesis-20261123/candidate/JOINT_EDIT_COMPILER.md).
This record concerns only the new candidate lane, not the repository-wide
integrity gate or a full Collatz proof.

## Fresh executions

[`REPLAY.json`](REPLAY.json) binds all three scientific files and records
three actual executions. The Lean module compiled under Lean 4.34.1,
compiler `5045d0056413266e57c625dcd7c365b10e377c52`, with `-j 1` and
`-DwarningAsError=true`. It imports only `Std`. All **23** public theorem
declarations were audited. Twenty-two print axiom sets contained in
`propext`, `Classical.choice`, `Quot.sound`; `orbit_succ` uses no axioms.
The complete output is [`lean-audit.log`](lean-audit.log). No `sorryAx`
or custom research axiom appears.

The new Python checker ran normally and with `-O`; both exited zero and
their complete output is byte-identical:

`72d0ad51853ff66e18c5ec5265767a125b211a67954434b47a438bf720b8495b`.

[`normal.json`](normal.json) and [`optimized.json`](optimized.json) retain
the complete results, including actual source and target tuples. They
record 1,024 independent grid comparisons, 270 accepted cases, 2,016 exact
common-run valuation checks, four damaged-certificate rejections, the
45/19 joint repair in both directions, and complete witness transport
from 385 to 193 including valid source terminal padding.

The all-clock minimum radius 39 for 193/385 has a separate finite ordinary
graph check over all 1,848 pairs of reachable states. Every Bellman lower
inequality is checked, and the recursive compiler supplies a matching
39-edit upper certificate. This includes arbitrary repetition of the
terminal two-cycle. It is not a claim based only on first-hit word lengths.

## Formal boundary

The formal proof includes the actual shortcut map, literal common runs,
raw first-merger alignments, their normalization, exact search soundness
and completeness, the bound `N*(2^t-1)`, negative-answer completeness, and
ordinary source-witness transport with clock at most `2*N*(2^t-1)+L`.

The sharper real bound, Python valuation optimization, original exponent
tuple conversion, and the concrete 39-edit optimum retain their written
or executable scope. Python was not extracted from Lean. The complete
tuple identities and literal trajectories are explicitly checked.

The compiler decides each prescribed edit radius. It does **not** prove
that a successful radius exists for every required source, and an
unbounded outer search is not claimed to terminate. The original
residue-512 implication and full Collatz remain open.

## Source reading and review

[`SOURCES.json`](SOURCES.json) records immutable PR heads, paths, Git blob
identities, and actual inspection scopes. The one-sided gap-one insertion
theorem in PR176 is a credited precursor; its count bound does not carry
over to arbitrary two-sided edits. The other refreshed source families
provide context rather than imported assumptions.

Source inspection, fresh execution, a hash-bound independent in-session
review, and repository integrity are different evidence. No external
referee acceptance or historical-corpus replay is claimed here.
