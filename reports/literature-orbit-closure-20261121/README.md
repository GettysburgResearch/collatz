# Verification and review receipts

Scientific statements and proofs are in `research/literature-orbit-closure-20261121/`.
This directory records evidence and its precise scope; repository validation is
separate from mathematical proof checking.

## First published checkpoint

- PR: https://github.com/GettysburgResearch/collatz/pull/185
- Published head: `3a2341f4b909cb83f6c2a0eabe946d3d96fc6148`.
- Exact tree: `e9163b0a6485dd2c5978890f298e0731d519d029`.
- The three initial Lean modules were actually compiled with warnings as errors.
- The 446-ray Python verifier passed, reporting all 130 unresolved classes.
- `python -X utf8 -B tools/validate.py` passed in a clean complete checkout of
  the actual published head (354 tracked files), leaving it clean.

The following follow-up receipts are actual development compilations, not
claims of a single end-to-end published-head replay:

- `symbolic-agent-replay.json`: the four symbolic/marked-family modules.
- `finite-resolvent-agent-replay.json`: the finite convolution kernel and audit.
- `explicit-seed-agent-replay.json`: the positive seed and baseline, with audit.

The final packet checker performs the complete replay and records the exact
Git head/tree, source hashes, all commands and exits, audit outputs, certificate
replay, and required repository validation. Its report is added after that
execution has completed.

## Independent source reviews

`REVIEW_SYMBOLIC_MARKED_ERASURE.md` independently checks the symbolic family
and preservation proof. Its small wording observation is applied in the final
proof note: the meeting occurs **by** the end of the native horizon, including
equality at the first family member. The four reviewed symbolic Lean sources are
unchanged.

`REVIEW_HARMONIC_CLOCK.md` checks the generic finite-mass, clock, and actual
return interfaces. Its ActualSurvivorMass hash predates two syntactic Lean
repairs (`ite_true` and explicit unfolding of `Hits`/`Basin`); ClockAbsorption
also received only a trailing-blank-line cleanup after the review. The final
survivor/closure review covers the repaired source separately. This reviewer
wrote FiniteResolvent, and explicitly does not claim independent review of
that own module.

`REVIEW_ACTUAL_EXPLICIT.md` independently checks the final source-fiber
construction and concrete closure implication. It pins the exact repaired
source, verifies the order of quantifiers, and preserves the explicit open
transport obligation.

No review claims novelty priority or turns the explicit uniform transport
hypothesis into a proved estimate. The universal physical cover and uniform
survivor improvement remain OPEN.

## First complete published-packet replay attempt

The actual published source at `6d2765ef462fb575c49d4133b54286be7ffe68ec`
compiled all 19 mathematical modules (the four inherited inputs and all 15
new mathematical modules). The combined final Audit entrypoint then failed
because a Lean module-mode entrypoint cannot import the two legacy `Std`
files. This was a checker integration error, not a mathematical proof failure.
`published2-first-replay.json` deliberately records `complete: false`, the
successful module exits, and that exact failure. The subsequent patch removes
only the Audit entrypoint's `module` header; every theorem source is unchanged.
A complete successful replay is recorded separately after it occurs.

## Parallel continuation

The additional three Lean modules have29 standard-only public theorem audits
in `residual-agent-replay.json`. The final assembled Audit now requests140
public theorems across18 new mathematical modules. The source review of the
residual selector predates its two additional stronger-partner/non-descent
theorems; those additions are separately kernel checked and reconstructed in
the root review. The half-selector proof and the global analytic consequences
are also covered by the scoped root reconstruction.

The Python arithmetic replay scripts were made read-only by default and their
assertions converted to explicit exceptions, so optimization cannot silently
disable their checks. Agent receipts preserve their original source snapshots;
the final checker records the exact published script inputs and executions.
