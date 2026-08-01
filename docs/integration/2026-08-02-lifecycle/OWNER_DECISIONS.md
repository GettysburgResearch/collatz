# Human-owner and later-integrator decisions

The lifecycle system is advisory. The following decisions should not be made silently by an integration agent.

## 1. Acceptance gate for PR #84

Decide whether:

```text
independent review + merge of PR #84
```

is sufficient to change the eight records from:

```text
candidate_in_draft_pr
```

to:

```text
accepted_reference_record
```

or whether any record should remain candidate until its local proof packet is imported.

Recommended default:

- merge accepts the registry/reference record;
- proof residency remains `frozen_source_reference`;
- local proof import is tracked separately;
- IC-PERIODIC-001 and RD-BRIDGE-001 require explicit narrow mathematical review before acceptance.

## 2. PR #74 supersession

Recommended decision:

- retain #74 open until PR #84 is independently reviewed and merged;
- move unresolved security, licensing, settings and public-launch tasks to a dedicated owner issue/checklist;
- then close #74 as superseded with the durable comment in `pr-lifecycle.json`.

This is organizational supersession, not a publication-readiness declaration.

## 3. Canonical proof residency

Approve or modify the proposed location:

```text
claims/integrated/<canonical-id>/
```

The goal is a stable local proof home without rewriting source claim IDs. A different path is acceptable if manifests, exact SHAs and aliases remain clear.

## 4. Source-PR cleanup policy

Approve the default rule:

> Import or merge unique accepted content first; create a closure manifest and durable pointer; only then close the source PR.

A closed PR remains searchable, but main should contain enough context that future agents do not depend on private archaeology.

## 5. Active research successors

For large mixed/active PRs, decide whether continuing work should:

- remain on the existing PR until the stable core is extracted; or
- move immediately to a focused successor while the original becomes an extraction/closure target.

Highest-impact cases:

```text
#13, #19, #49, #51, #53, #80, #81
```

## 6. Merge versus clean import

Some verified packets are mergeable after fixes; others are better imported to avoid stacked history and duplicate files.

Recommended direct-merge candidates:

```text
#6, #20, #33, #48, #66, #76, #79
```

The owner may prefer clean imports for any of these. The mathematical status does not change.

## 7. SC*/FC* bridge language

Until `RD-BRIDGE-001` receives narrow review, approve the wording:

```text
principal proposed roadmap bridge
```

and avoid:

```text
established logically exhaustive reduction
```

## 8. Public release

Nothing in PR #84 or this continuation authorizes:

- making the repository public;
- announcing readiness;
- changing branch protection or team permissions;
- adopting a license for legacy content without audit;
- enabling Actions;
- closing public-readiness blockers.

Those remain owner decisions outside this integration pass.
