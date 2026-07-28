# Governance

## Purpose

Governance exists to preserve research freedom while maintaining an auditable
record.

It does not authorize maintainers to decide mathematical truth by status or
reputation.

## Core separation

The project makes three different decisions.

### 1. Artifact integration

Is the contribution useful, understandable, appropriately scoped, and safe to
preserve in the repository?

A speculative report, failed route, or proposed theorem may pass artifact
integration.

### 2. Claim promotion

What level of mathematical confidence is justified by the evidence?

Claim promotion requires explicit review and is separate from merging the
artifact.

### 3. Project-level resolution status

Does the repository contain a complete proof or counterexample whose entire
dependency chain and translation to Collatz have survived the required
verification?

Only this decision changes the public project status.

## Roles

### Organization owners

Responsible for:

- repository continuity;
- security;
- visibility;
- legal and administrative decisions;
- appointing integrators.

Owners do not gain mathematical authority from the role.

### Integrators

Responsible for:

- dependency-aware merge planning;
- canonical claim metadata;
- `STATE.md`;
- conflict reconciliation;
- review queues;
- preserving provenance;
- detecting duplicate and circular programs;
- extracting reusable tasks;
- keeping ambitious work visible.

Integrators record the strongest status justified by evidence. They do not
promote claims by personal confidence alone.

### Maintainers

Responsible for a research or infrastructure area.

They may review and merge ordinary contributions within ruleset constraints.

### Triagers and research organizers

Trusted contributors may receive GitHub `Triage` access early. They can help
with labels, issue cleanup, duplicate handling, review routing, and Discussion
organization without receiving code-push access. The initial launch may have
only the founder performing integration while the triage circle grows.

GitHub does not provide a permission level that gives arbitrary public users
formal self-assignment without also granting broader repository access. The
portable project convention is therefore a `CLAIMED BY` issue comment; a
triager, maintainer, or later automation may mirror it into labels or formal
assignment.

### Contributors

Anyone may contribute through Discussions, Issues, issue comments, reviews,
forks, and pull requests. Corrections and alternative approaches in issue
comments are first-class contributions. Contributors do not need formal
assignment before beginning work.

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

A special label:

```text
RESOLUTION_CANDIDATE
```

may be applied only to a complete proof or counterexample packet that includes:

- exact theorem statement or exact candidate object;
- complete dependency graph;
- proof of ordinary integrality and positivity where required;
- exact physical Collatz translation;
- independent reconstruction;
- reproducible computation;
- formalization plan or formal proof where feasible;
- explicit unresolved doubts.

The repository remains publicly `UNSOLVED` while external and internal scrutiny
continues.

## Review independence

A review is independent when the reviewer:

- did not author the claim;
- reconstructs rather than merely endorses;
- freezes the source version;
- records the first unsupported step if found;
- distinguishes neutral non-reproduction from refutation.

Different models prompted by the same human can provide useful adversarial
checks, but independence metadata should state the human sponsor, model family,
shared prompts, and shared code.

## Merge authority

No contributor should merge their own major theorem claim.

Ordinary research artifacts require at least one review.
Canonical claim-promotion changes require a separate approval.
Resolution candidates require at least two independent adversarial reviews and
owner/integrator approval.

## Disputes

When reviewers disagree:

1. freeze the exact claim version;
2. write both verdicts;
3. isolate the first disputed inference;
4. seek a third reconstruction;
5. keep the status at the strongest level supported by common evidence;
6. preserve both analyses.

## Cadence

During active contribution waves:

- frequent triage may occur roughly every two hours;
- integration should occur in deliberate windows;
- `STATE.md` should be updated at least daily when the project is changing
  rapidly;
- a tagged research snapshot should be created periodically.

These are operating defaults, not mathematical rules.

## Organizational change

The governance system is itself experimental.

Substantial changes should be proposed openly, tested on a limited scope where
possible, and evaluated by whether they improve:

- research freedom;
- reliability;
- navigability;
- reproducibility;
- contributor experience;
- resistance to circular work.
