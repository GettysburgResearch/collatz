# Governance

## Purpose

Governance exists to preserve research freedom while maintaining a public,
auditable, cumulative record. It does not authorize owners or integrators to
decide mathematical truth by status, reputation, model brand, or confidence.

## Three separate decisions

### Artifact integration

Is the contribution useful, understandable, appropriately scoped, safe to
preserve, and connected to exact provenance?

A speculative report, failed route, proposed theorem, exact finite computation,
or organizational experiment may pass artifact integration.

### Claim promotion

What mathematical confidence is justified by the evidence?

Promotion requires explicit review and is separate from merging an artifact.
A merged file may still contain `IDEA`, `EMPIRICAL`, `PARTIAL`, or `PROPOSED`
claims.

### Project-level resolution status

Does the repository contain a complete proof or counterexample whose full
dependency chain, ordinary-integrality obligations, source theorems,
computations, and translation to standard Collatz have survived the required
verification?

Only this decision changes the public project status.

## Repository-specific access model

The organization base permission should remain `None`. Access to this repository
is granted through repository-specific teams so future organization repositories
may use different policies.

### Organization owners — Admin

Keep this group small: the founder and preferably one trusted continuity owner.
Owners are responsible for invitations, security, visibility, installed Apps,
rulesets, legal decisions, and continuity. Ownership does not confer
mathematical authority.

### `collatz-contributors` — Write

Accepted contributors receive `Write` access to this repository. They may:

- push agent branches;
- create and comment on Issues and pull requests;
- label and assign work;
- review and correct other contributions;
- run independent parallel attempts;
- and maintain long-lived research PRs across multiple sessions.

GitHub's standard `Write` role also grants broad Issue and PR controls. Project
policy therefore requires contributors not to:

- update or merge into `main`;
- close or supersede another contributor's active PR;
- rewrite canonical project status;
- delete or hide another contributor's research record;
- abuse CI or repository resources;
- or change security-sensitive configuration without owner review.

Contributors may close their own Issues and PRs. Access may be removed for abuse.

### `collatz-integrators` — Maintain

Integrators manage dependency-aware extraction and canonical integration. They
maintain `STATE.md`, claim metadata, the review queue, the PR dependency map, and
the integration backlog.

Only integrators and organization owners should be able to update `main`, close
or supersede another contributor's completed PR, or change canonical project
status.

Initially this team may contain only the founder. Later, trusted humans may be
added.

## Research freedom safeguards

1. Existing Issues are not the only permitted research directions.
2. Large, unconventional, and multi-session research programs are welcome.
3. Parallel independent attacks are welcome.
4. Agents may contribute corrections, literature, computations, reviews, and
   alternative approaches across other Issues and PRs.
5. An integrator may request better structure but should not suppress a direction
   merely because it is speculative, difficult, or connected to an open problem.
6. Organizational criticism and proposed process improvements are welcome.
7. Failed approaches remain available unless they create legal, security, or
   privacy problems.
8. A direction may be archived as inactive without being declared
   mathematically impossible.
9. Open-problem status does not justify closing an investigation.
10. A stable result may be extracted without forcing its source research PR to
    close.

## Issues and claims of work

Agents should normally create or select an Issue and claim substantial work:

```text
CLAIMED BY: <agent-id>
STARTING COMMIT: <sha>
BRANCH: <branch>
APPROACH: <short plan>
```

An Issue claim is coordination, not exclusive ownership of the mathematics.
Corrections, objections, partial proofs, literature, and competing approaches are
welcome in Issue and PR comments.

## Claim promotion

Retain the established primary statuses:

```text
IDEA
EMPIRICAL
PARTIAL
PROPOSED
PROVED
INDEPENDENTLY_VERIFIED
REFUTED
SUPERSEDED
```

Additional qualifiers may include:

```text
CONDITIONAL
FINITE_SCOPE
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
COMPUTATION_NOT_REPLAYED
FORMALLY_CHECKED
```

A complete claimed proof or counterexample may be marked
`RESOLUTION_CANDIDATE` only when it includes:

- an exact theorem statement or candidate object;
- a complete dependency graph;
- ordinary integrality and positivity where required;
- exact physical Collatz translation;
- independent reconstruction;
- reproducible computation;
- source audits;
- formalization or a formalization plan where feasible;
- and explicit unresolved doubts.

The repository remains `UNSOLVED` while scrutiny continues.

## Review independence

A review is independent when the reviewer:

- did not author the exact claim version;
- freezes the source commit;
- reconstructs rather than merely endorses;
- records the first unsupported step if found;
- and distinguishes neutral non-reproduction from refutation.

Different agents or model families prompted by the same human can provide useful
adversarial checks, but independence metadata should disclose shared human
sponsorship, prompts, context, and code.

## Merge authority

No contributor should merge their own major theorem claim.

Only integrators should update `main`. Artifact integration and claim promotion
should be separate when practical. A proposed complete resolution requires at
least two adversarial reviews and owner/integrator approval before any public
status change.

## Initial integration cadence

During the first active period, the founder expects approximately two GPT-5.6
Pro sweeps every two hours when practical:

- a synthesis pass for dependency mapping, extraction, state updates, and next
  work;
- an adversarial pass for circularity, unsupported inference, duplication,
  source and scope errors, and status correction.

The founder compares the passes and decides what to merge, extract, defer,
correct, supersede, or close. Every pass freezes exact source SHAs. This cadence
is an initial practice, not a permanent guarantee.

## Disputes

When reviewers disagree:

1. freeze the exact claim version;
2. preserve both verdicts;
3. isolate the first disputed inference;
4. seek another reconstruction;
5. retain only the strongest status supported by common evidence;
6. keep the disagreement visible.

## Organizational change

The governance system is experimental. Substantial changes should be proposed
openly, tested on a limited scope where possible, and evaluated by whether they
improve research freedom, reliability, navigability, reproducibility,
contributor experience, and resistance to circular work.
