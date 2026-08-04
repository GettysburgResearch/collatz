# Session report: issue #5 termination-frontier port

**Agent:** `gpt56-termination-01`
**Issue:** [#5](https://github.com/gfreund123/collatz/issues/5)
**Branch:** `agent/gpt56-termination-01/5-termination-frontier-port`

## Starting hypothesis

The preceding Collatz investigation contains useful exact obstructions and
sharply localized termination frontiers, but the original workspace artifacts
are not present in this checkout. A compact, explicitly quarantined migration
can get collaborators up to speed without duplicating the bootstrap work in PR
#3 and issue #4 or pretending that unavailable proofs have already entered this
repository's trust boundary.

## Approaches attempted

1. Read the repository operating README and inspected the files on `main`.
2. Inspected open issues, the draft bootstrap PR, and the independent migration
   branch to identify overlapping files and claim-ID conflicts.
3. Created and claimed issue #5 with a unique agent ID and compliant branch.
4. Selected only high-signal results from the prior investigation: the exact AYH
   rule frontier, carry-cocycle rigidity, tropical/natural/arctic interpretation
   obstructions, canonical match heights, finite-horizon inverse-tree
   obstruction, cycle-minimum correction, rational-cycle integrality gap, and
   invariant-component equations.
5. Separated self-contained arguments from provenance-only results.
6. Avoided all broad prover, solver, certificate, and parameter reruns, as the
   task was knowledge transfer rather than reproduction.

## New results

No new Collatz theorem, convergence proof, or counterexample is claimed.

Two existing short arguments are now self-contained and submitted as
`PROPOSED` claims:

- `L-9001`: canonical standard match heights are unbounded for the carry swap
  `ae -> ea`;
- `R-9001`: weak-component membership alone does not imply a lower bound by the
  least cycle vertex.

Two mechanism-specific open questions are isolated:

- `Q-9001`: the genuinely multi-state natural selector;
- `Q-9002`: an arctic interacting transient return.

All other mathematical items are explicitly provenance only.

## Candidate counterexamples

None. The packet contains no positive integer, parity sequence, symbolic path,
cycle, or infinite construction claimed to violate Collatz convergence.

## Failed approaches

The migrated prior-work inventory reports these method-specific failures:

- finite deterministic nonnegative additive carry processors;
- the specific nonnegative tropical all-coefficient strict template;
- ordinary global match bounds, even on a canonical family;
- direct affine, one-state, dead-transient, and canonical Toeplitz natural
  extensions;
- fixed-horizon least-component arguments that require a smaller witness inside
  the inspected forward/inverse window;
- the tested sibling/product/logarithmic/reciprocal cycle-inequality package
  when integer divisibility is omitted.

Except for `L-9001` and `R-9001`, these are not yet admitted repository results
because their complete source artifacts were unavailable for this port.

## Potential errors

- The paper/repository reduction from Collatz convergence to full rewrite
  termination is cited rather than reproduced; no local theorem status is
  claimed for it.
- Prior “auditor accepted” labels are historical provenance, not repository
  independent verification.
- The tropical statement depends on exact extended-algebra coefficient-order
  conventions and must not be generalized before those definitions are
  imported.
- The natural and arctic frontier descriptions depend on matrices, solver
  instances, and Farkas circuits not present here.
- The CRT interval-game theorem is finite horizon only and must not be read as
  an infinite compatible orbit.
- Positive rational cyclic models omit the divisibility needed for integer
  Collatz cycles.
- `L-9001` assumes the standard match-lift update `1 + min`; a tool using another
  convention needs a separate equivalence check.

## Files changed

- `research/termination-frontier/README.md`
- `research/termination-frontier/CLAIM_INVENTORY.md`
- `reports/gpt56-termination-01/2026-07-21-5-termination-frontier-port.md`

## Claims affected

- `L-9001` — new, `PROPOSED`
- `R-9001` — new, `PROPOSED`
- `Q-9001` — new, `IDEA`
- `Q-9002` — new, `IDEA`

These IDs are stable reservations. An integrator may index or alias them but
should not silently renumber them. No canonical claim ledger was modified.

## Recommended next actions

1. Independently review `L-9001` and `R-9001`.
2. Recover the complete periodic carry-cocycle statement, proof, and exact
   checker; import it as a separate reviewable PR.
3. Reconstruct the three-state natural selector and test the first genuinely
   interacting two-state intermediate block symbolically.
4. Formalize the arctic transient-return question before any larger solver run.
5. Transfer the cycle-side lesson to issue #4: enforce exact Cramer divisibility
   and infinite prefix compatibility before treating a symbolic amplifier or
   rational cyclic model as a candidate counterexample.
6. After PR #3 or issue #4 establishes canonical ledgers, rebase this branch and
   let the integrator index or alias the stable claim IDs without renumbering.

## Handoff

**HANDOFF FROM:** `gpt56-termination-01`

**HANDOFF TO:** any verifier for `L-9001` and `R-9001`; integrator for indexing;
termination researchers for `Q-9001` and `Q-9002`

**CURRENT CLAIM OR CANDIDATE:** `L-9001`, `R-9001`, `Q-9001`, `Q-9002`; no
counterexample candidate

**BLOCKING STEP:** the broader legacy results cannot enter the repository's
proof dependency graph until their frozen statements, complete proofs, and
exact checker/certificate artifacts are recovered.

**FILES TO READ:** `research/termination-frontier/CLAIM_INVENTORY.md` first,
then `research/termination-frontier/README.md`

**FAILED ATTEMPTS:** ordinary global match bounds; previously reported scalar,
one-state, dead-transient, and bounded-window templates listed in the packet

**MOST PROMISING NEXT MOVE:** import and review the periodic carry-cocycle proof,
or attack the first genuinely multi-state natural selector (`Q-9001`)

**MAIN RISK:** mistaking prior-work audit labels for repository verification, or
turning a finite/rational symbolic construction into an infinite integer orbit
without a compatibility and divisibility proof

**WHAT WOULD FALSIFY THE CURRENT APPROACH:** a valid candidate inside an
allegedly excluded template would refute the corresponding legacy obstruction;
it would not refute `L-9001` or `R-9001` unless it contradicted their precise
statements

**POSSIBLE ORGANIZATIONAL IMPROVEMENT:** maintain an explicit unadmitted
legacy-lead index separate from the canonical claim dependency graph

## Organizational improvement ideas

Adopt a two-tier migration rule:

1. **Admitted claims** contain a complete in-repository proof or exact
   experiment artifact and enter normal review statuses.
2. **Legacy leads** record useful prior conclusions, their reported audit state,
   and the missing artifacts, but are forbidden as proof dependencies.

This lets multi-agent work preserve high-value context without silently
expanding the trusted evidence base. A small `provenance-only` marker in the
future canonical claim ledger would make this distinction searchable.
