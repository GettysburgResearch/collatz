# Independent reconstruction: forced cap-four routes

Reviewer: the in-session `escape_rigidity` agent, 2026-11-23.

**Verdict: PASS after a documentation clarification.** This is an
independent reconstruction of the written finite-route theorem and all
twelve public Lean statements. It is not external peer review, a new
review of every cited upstream source, or a claim that the source-surgery
attempt closes Collatz.

## Final source bindings

| File in `research/high-variance-20261123/` | SHA256 |
|---|---|
| `ForcedRoute.lean` | `1ec27b82a10b58427f854e8d178ffe7b304d13d3ca6ac253e17fa8e11ba9736a` |
| `SOURCE_SURGERY.md` | `47e2b45ce7a96b7d1e031e5dc294336c53e39e2c4762dbfd8a8b33573a9a8b63` |

The mathematical proof was unchanged by the clarification. The generic
`Edge` predicate requires a positive odd unit **output**, but does not
separately require an odd input. For example, `Edge 1 8 5` satisfies its
equation although it is not an accelerated-odd edge from 5 to 8. The
final theorem is nevertheless an actual ordinary route theorem: its
initial value is proved positive, odd and prime to three, and the
endpoint guard preserves those facts at every subsequent vertex. The
module's `Edge` comment and the written formalization boundary now state
that precise distinction.

## Reconstruction

The value used by Lean is

`value B i = 9*(2^(i+1)*3^(B-i))-1`.

For `i<=B` it equals the written
`2^(i+1)*3^(B+2-i)-1`. The natural subtraction outside that range is not
used to assert extra orbit steps. All values are positive and odd and
are eight modulo nine. The equality `value+1=9*(...)` is valid because
the subtracted positive product is at least nine.

For an input eight modulo nine, exponents two and four contradict the
edge equation modulo three. Exponent three forces its output to be
divisible by three. Thus every permitted cap-four unit edge must have
exponent one. For `i<B`, the exponent identity gives exactly

`3*value B (i+1)+1 = 2*value B i`.

The equation also makes that output unique. Since the output and input
are odd in this application, the displayed exponent is the actual
valuation, not merely a nonmaximal power-of-two factor.

`value_route` supplies each prefix as an existing route, so the final
avoidance statement is not only vacuous universal quantification over
an empty relation. The induction in `route_is_forced` handles an
arbitrary supplied route and proves both the full exponent word and
its endpoint. Its bound `i+length<=B` supplies the strict inequality
needed at every inductive edge; it does not apply the step identity
past the proved range.

Every resulting endpoint remains eight modulo nine and therefore cannot
be seven modulo 729. The final theorem starts from
`q_B=2*3^(B+2)-1` and quantifies over all routes of length at most `B`.
For `B=0` the only permitted length is zero and the initial state is 17,
so the empty-route case is covered. The starting integer depends on
`B`; no fixed all-time avoiding source is obtained.

The written extension using `v_3(q+1)=v>=2` also has the correct clock:
through indices zero to `v-2`, the vertices remain eight modulo nine.
A first arrival outside that class can occur no earlier than depth
`v-1`. It does not assert an extra forced step after the valuation
has been exhausted.

## Scope retained

The result excludes a routing depth uniform over all positive odd unit
roots. It leaves logarithmic root-dependent depths, restricted source
families, and target-aware edits open. The displayed roots are not
asserted to satisfy the full joint minimum-target/minimum-grade/
largest-source hypotheses of the repository's extremal certificate.

The fixed-word pumping discussion is algebraically sound: the fixed
point has denominator prime to three, and indefinitely integral inverse
iteration forces the initial displacement to have arbitrarily high
ternary valuation, hence to vanish. This controls a fixed repeated
block; it does not rule out adaptive words of changing lengths.

The formal statements prove the finite route result only. No cheap
subtree infinitude, successful universal dispatcher, actual escaping
integer, or positive-integer nontrivial cycle is inferred. Compiler and
axiom-audit receipts are separate execution evidence in this packet.
