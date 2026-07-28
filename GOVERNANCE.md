# Governance

## Purpose

Governance exists to preserve research freedom while maintaining an auditable
record. It does not authorize maintainers to decide mathematical truth by
status or reputation.

## Three separate decisions

### Artifact integration

Is the contribution useful, understandable, appropriately scoped, and safe to
preserve? A speculative report, failed route, or proposed theorem may pass this
stage.

### Claim promotion

What level of mathematical confidence is justified by the evidence? Promotion
requires explicit review and is separate from merging the artifact.

### Project-level resolution status

Does the repository contain a complete proof or counterexample whose dependency
chain and translation to Collatz have survived the required verification? Only
this decision changes the public status.

## Roles

### Organization owners

Responsible for continuity, security, visibility, legal and administrative
decisions, and appointing integrators. Ownership does not confer mathematical
authority.

### Integrators

Responsible for dependency-aware merge planning, canonical claim metadata,
`STATE.md`, conflict reconciliation, review queues, provenance, duplicate and
circular-program detection, task extraction, and keeping ambitious work visible.

Integrators record the strongest status justified by evidence. They do not
promote claims by personal confidence alone.

### Maintainers

Responsible for a research or infrastructure area. They may review and merge
ordinary contributions within ruleset constraints.

### Triagers and research organizers

Trusted contributors may receive GitHub `Triage` access early. This role can
apply labels, assign contributors who have commented, close or reopen issues and
pull requests, request reviews, apply milestones, and mark duplicates—without
code-push access.

The initial launch may have only the founder performing integration while a
larger triage circle helps organize public contributions.

Arbitrary unaffiliated public users do not receive moderation controls merely
because the repository is public. They may claim work through an issue comment;
a triager can then mirror that claim into formal assignment and labels.

### Contributors

Anyone may contribute through Discussions, Issues, issue comments, reviews,
forks, and pull requests. Corrections and alternative approaches in issue
comments are first-class contributions. Formal assignment is not required before
beginning work.

## Research freedom safeguards

1. Existing issues are not the only permitted research directions.
2. Large research programs are welcome.
3. Parallel independent attacks are welcome.
4. The integrator may request better structure but should not suppress a
   direction merely because it is speculative, difficult, or connected to an
   open problem.
5. Organizational criticism and proposed process improvements are welcome.
6. Failed approaches remain available unless they create legal, security, or
   privacy problems.
7. A direction may be archived as inactive without being declared
   mathematically impossible.
8. Open-problem status does not justify closing an investigation.

## Claim promotion

Recommended ladder:

```text
IDEA
DEVELOPING
PROPOSED
INDEPENDENTLY_RECONSTRUCTED
FORMALLY_CHECKED
REFUTED
SUPERSEDED
```

`FORMALLY_CHECKED` means the formal statement compiles and has undergone a
statement-to-mathematics translation audit. It does not automatically imply a
project-level resolution.

A complete claimed proof or counterexample may be marked:

```text
RESOLUTION_CANDIDATE
```

only when it includes:

- an exact theorem statement or candidate object;
- a complete dependency graph;
- ordinary integrality and positivity where required;
- exact physical Collatz translation;
- independent reconstruction;
- reproducible computation;
- a formalization plan or proof where feasible;
- explicit unresolved doubts.

The repository remains publicly `UNSOLVED` while scrutiny continues.

## Review independence

A review is independent when the reviewer:

- did not author the claim;
- reconstructs rather than merely endorses;
- freezes the source version;
- records the first unsupported step if found;
- distinguishes neutral non-reproduction from refutation.

Different models prompted by the same human can provide useful adversarial
checks, but independence metadata should disclose the human sponsor, model
family, shared prompts, and shared code.

## Merge authority

No contributor should merge their own major theorem claim.

Ordinary research artifacts require at least one review. Canonical
claim-promotion changes require separate approval. Resolution candidates require
at least two independent adversarial reviews and owner/integrator approval.

## Disputes

When reviewers disagree:

1. freeze the exact claim version;
2. preserve both verdicts;
3. isolate the first disputed inference;
4. seek a third reconstruction;
5. retain only the strongest status supported by common evidence.

## Cadence

During active contribution waves:

- frequent triage may occur roughly every two hours;
- integration should occur in deliberate windows;
- `STATE.md` should be updated daily when the project changes rapidly;
- tagged research snapshots should be created periodically.

These are defaults, not mathematical rules.

## Organizational change

The governance system is experimental. Substantial changes should be proposed
openly, tested on a limited scope where possible, and evaluated by whether they
improve research freedom, reliability, navigability, reproducibility,
contributor experience, and resistance to circular work.
