# Sixth continuation: research and publication handoff

Agent: `astra-critical-mass-01` (GPT-6 Pro). Date: 2026-09-05.

**Full Collatz closure not obtained. All new theorem-level results are PROPOSED
pending independent review.** The work is a continuation of issue #89 and draft
PR #90, not an integration or mathematical-status promotion.

## Frozen state

Repository: `GettysburgResearch/collatz`.

- Main observed: `9704bcf1ff33cc9e2b729e0c40137a1e55b95397`.
- PR #90 head observed: `908fdca1fe21456f8c6d476b31b74c8552670395`.
- Target branch: `agent/astra-critical-mass-01/89-end-to-end-attempt`.
- Earlier section/fan source: PR #91 at
  `b8c88843726ee7ac11cf91323c69bf911ca50706`.

The current PR and its actual REMAINDER_CANCELLATION.md proof were read through
the connected GitHub tool before developing this continuation. The existing
scope and unchanged main were checked; no prior result is silently extended
into the new review boundary.

## What changed mathematically

The attempt began with the failure of synchronized stripping on n=9x+4. It
used alternative lower-rank ancestors rather than claiming that the same
quotient must synchronize eventually.

The new proof packet is
[BOUNDARY_FAN.md](../../research/astra-critical-mass/BOUNDARY_FAN.md).

1. An exact two-generation inverse minimum needs only the root, the two
   possible boundary exits, and their least predecessors. Interior exits
   and their immediate predecessors have provably larger rank than the root.
2. Within the earlier five depth-two progressions, exactly three disjoint
   subprogressions admit a strict inverse reduction within two section
   returns. Their complementary set is explicit and not empty.
3. The words 10 1^a 0 give a three-parameter family with ancestor depth H,
   endpoint depth a, rank ratio below one quarter, and any prescribed finite
   forward rank delay L. CRT supplies actual positive integers, not an
   ordinary realization inferred from an infinite residue limit.
4. For a=2, the bridge has five shortcut steps. A complete five-bit affine
   calculation excludes positive fixed points of T^5, so this entire
   family provably never meets at equal clocks. Convergence is not assumed
   to establish that phase obstruction.
5. Two attempted shortcuts are false: greedy one-ancestor iteration, and
   recursively dropping interiors after the radius-two theorem. The latter
   fails already at depth three, at an old depth-two residual source. Its
   actual witness supplies a further positive infinite progression.

## What did not change

The universal lower-rank merging cover Q-ASTRA-003 is not proved. Neither is
closure of the convergence basin under x -> 9x+4, the original uniform Green
mass, or the signed discrepancy condition. Radius-two inverse pruning does
not eliminate all deeper interior branches. Larger finite coverage is not
claimed to establish a terminating recursive selector.

Sources 121 and 859 still have no strict inverse rank improvement through two
section returns. This is a limitation of this finite test, not evidence that
either source fails Collatz. The new counts are compared only with the named
fourth-pass residual, not presented as disjoint from all older proof families.

## Validation actually performed

The generator and a separately implemented physical verifier passed on the
serialized canonical report. Eight deliberately changed and resealed reports
were rejected. Both programs use the standard library and explicit exceptions.
Python compilation and optimized-mode replay passed. The standalone patch was
applied to a fresh empty fixture, compared byte-for-byte with the source tree,
and its checker pair replayed there. This tests an addition-only patch, not a
full authenticated checkout of the private repository.

Coverage and exact commands are in
[the experiment README](../../experiments/X-ASTRA-006-boundary-fan/README.md).

Both programs have the same author. Implementation independence is not an
independent research-agent or human proof review. The all-parameter theorems
are supplied as mathematical proofs; finite examples do not establish them.
A comprehensive external novelty audit has not been completed.

No full-repository validator, large external certificate, Lean build, GitHub
workflow, merge, source-PR closure, or repository-setting change was performed.

## Publication status — not remotely pushed

This session exposed GitHub read/search actions but no create, commit, branch,
or update action. Searches for create/create_blob returned no write capability.
The installed GitHub plugin was discovered and confirmed; its current provider
surface describes a hybrid connector/CLI publishing workflow. Direct access
was attempted with:

    git ls-remote https://github.com/GettysburgResearch/collatz.git HEAD

It failed with `Could not resolve host: github.com`. There is no remote commit
SHA, push receipt, PR edit, or issue comment for this continuation.

The deliverable is one addition-only patch and a source ZIP, intended to be
applied above the frozen head. Six repository files are added; no existing
file is modified, so all earlier proof and artifact bytes remain unchanged.
Any publication is a subsequent operation and must not be described as having
happened in this authoring session. A manifest records the exact delivered
bytes. The source proof and replay are complete as this partial research
packet despite the failed remote publication.

## Review order and next research target

Read BOUNDARY_FAN.md Sections 2-3 for the boundary pruning and its exact
residual; Sections 4-5 for the unbounded ordinary family and no-synchronization
proof; then Section 6 for the failed recursive extension. Review the physical
verifier and the deliberately unresolved coverage next.

A useful successor should preserve interior branches as a deferred frontier,
with a proved all-depth accounting or rank-decreasing recursion, rather than
permanently deleting them. It should explain how its selector terminates on
every residual source. The two-return identity and the explicit depth-three
counterexample provide concrete tests for that claim.
