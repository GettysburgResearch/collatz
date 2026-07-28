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

After the contributor comments, a trusted organizer with `Triage` access may
formally assign the issue to them and apply the appropriate labels.

## Permission ladder

### Public

Issues, comments, Discussions, forks, reviews, and pull requests.

### Research organizer — Triage

For contributors who have demonstrated constructive participation. `Triage`
allows them to apply or dismiss labels, assign contributors, close or reopen
issues and pull requests, request reviews, apply milestones, and mark duplicates
without code-push access.

This is the recommended early trust role for community organizers.

### Maintainer — Write

For sustained contributors who need to push branches directly to the
organization repository. `main` remains protected and integration is still
reviewed.

### Integrator — Maintain

For dependency-aware merges, canonical state, and claim-ledger stewardship.
Initially this role may contain only the founder.

### Owner — Admin

For security, visibility, rulesets, Apps, and continuity. Keep this group very
small.

## Labels and duplicates

Arbitrary unaffiliated public users cannot apply repository labels or formally
moderate other people's issues. They may comment `Possible duplicate of #123`
and continue the mathematical discussion. A trusted triager can apply labels,
mark the formal duplicate relationship, assign contributors, or close the issue.

## ChatGPT and other agents

The standard ChatGPT GitHub app is a read/search connection. A contributor needs
a write-capable authenticated environment such as Codex, Cursor, local Git, or
another coding agent to push a branch or open a code pull request. The agent acts
with that contributor's GitHub permissions.

Some AI connectors do not expose GitHub Discussions. Actionable Discussion
content must therefore be mirrored into Issues, PRs, reports, or repository
documents.
