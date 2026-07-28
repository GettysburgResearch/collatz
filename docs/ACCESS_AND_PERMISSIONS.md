# Access and Permission Model

## Public participation

Once the repository is public and Issues remain enabled, any GitHub user may:

- read and clone the repository;
- open Issues;
- comment on Issues and pull requests;
- participate in Discussions;
- fork the repository;
- push to their own fork;
- open a pull request from a branch they control.

Public visibility does not grant direct push access to
`GettysburgResearch/collatz`. Direct pushes require explicit repository `Write`
access.

## Claiming work without elevated access

Use an issue comment:

```text
CLAIMED BY: @username
STARTING COMMIT: <sha>
APPROACH: <short plan>
```

Multiple independent attempts are allowed. Formal assignment is helpful but not
required.

## Permission ladder

### Public

Issues, comments, Discussions, forks, reviews, and pull requests.

### Research organizer — Triage

A relatively low-trust role for contributors who have demonstrated constructive
participation. It permits label application and issue/PR organization without
code-push access.

### Maintainer — Write

For sustained contributors who need formal assignment, branch creation, or
direct work in the repository. `main` remains protected and integration is still
reviewed. GitHub currently requires `Write` access to formally assign issues or
pull requests.

### Integrator — Maintain

For dependency-aware merges, canonical state, and claim-ledger stewardship.
Initially this role may contain only the founder.

### Owner — Admin

For security, visibility, rulesets, Apps, and continuity. Keep this group very
small.

## Labels and duplicates

Arbitrary public users cannot apply repository labels. `Triage` access can be
granted to trusted research organizers for this purpose. Anyone may comment
`Possible duplicate of #123`; a triager can apply the duplicate label or close
the issue. GitHub's special “marked as duplicate” timeline event requires write
access, but the project does not depend on that event.

## ChatGPT and other agents

The standard ChatGPT GitHub app is a read/search connection. A contributor needs
a write-capable authenticated environment such as Codex, Cursor, local Git, or
another coding agent to push a branch or open a code pull request. The agent acts
with that contributor's GitHub permissions.

Some AI connectors do not expose GitHub Discussions. Actionable Discussion
content must therefore be mirrored into Issues, PRs, reports, or repository
documents.
