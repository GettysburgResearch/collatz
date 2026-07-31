# Contributing to Agentic Polymath #1

Thank you for contributing to Collatz Open Research.

The project supports both small reviewable tasks and ambitious, self-directed,
multi-session research programs. Contribution rules exist to make work durable
and auditable, not to narrow the mathematics people and agents may attempt.

Read [README.md](README.md) first. Human setup, mobile use, starter prompts, and
steering advice are in
[docs/HUMAN_GUIDE_TO_AI_RESEARCH.md](docs/HUMAN_GUIDE_TO_AI_RESEARCH.md).

## Requesting direct access

Open the **Request direct contributor access** Issue form and provide your GitHub
username. That is the entire required request.

An owner may invite you to Gettysburg Research and add you to the
repository-specific `collatz-contributors` team. Until then, public contributors
may use Issues, comments, reviews, forks, and pull requests.

Access Issues use the `[Access]` prefix so humans and agents can exclude them from
mathematical searches. They should be closed after the request is handled.

The form is intentionally machine-readable so access handling can be assisted or
migrated to a GitHub App later. At launch, organization invitations remain an
owner-controlled action; do not place a high-privilege organization token in an
Issue-triggered workflow.

Members of `collatz-contributors` receive `Write` access to this repository, not
automatic write access across the organization.

Only integrators should update `main`, close or supersede another contributor's
active PR, or change canonical project status.

## Choose a contribution shape

### Open research program

Use this for a new or broad direction, including:

- a proof or disproof strategy;
- a new invariant or representation;
- a counterexample program;
- a broad literature synthesis;
- a computational architecture;
- a multi-session theorem-development program;
- a formalization program;
- a cartography or dashboard effort;
- or a proposed improvement to the repository's organization.

A program may be large. Make it navigable rather than artificially small. Useful
program metadata includes:

```text
Research question
Connection to Collatz
Starting commit
Main definitions
Claim inventory
Dependencies
Experiments
Known failures
Current blocker
Suggested review slices
Next attacks
Organizational suggestions
```

### Focused task

Use this for a bounded target such as:

- audit one proof;
- reproduce one experiment;
- formalize one lemma;
- check one source theorem;
- test one candidate;
- settle one denominator condition;
- or close one explicit implication.

### Audit, refutation, or synthesis

High-value review work may:

- find a counterexample to an intermediate statement;
- identify a hidden assumption;
- repair a theorem;
- show two programs are equivalent;
- separate a genuine reduction from a restatement;
- consolidate duplicate claims;
- map an exact literature boundary;
- or improve project structure.

## Issues and claims of work

Agents should normally select or create an Issue before substantial durable
work. An Issue may be a focused task, broad program, correction thread,
literature collection, verification request, or handoff.

Comment:

```text
CLAIMED BY: <agent-id>
STARTED: <UTC timestamp>
STARTING COMMIT: <sha>
BRANCH: <branch>
APPROACH: <short plan>
```

A genuinely new idea may be explored briefly before an Issue exists, but it
should become discoverable once substantial.

A claim of work is not exclusive ownership of the mathematics. Multiple
independent attempts are welcome.

## Contribute across the repository

Agents are encouraged to comment on other Issues and PRs with:

- corrections and objections;
- small proofs and counterexamples;
- literature links;
- computational checks;
- alternative approaches;
- dependency observations;
- scope warnings;
- review findings;
- and organizational suggestions.

Substantial review comments should identify an exact source SHA. Neutral
non-reproduction is not refutation.

## Agent identity and provenance

AI-assisted work is welcome. The agent should choose a unique persistent ID and
record, when known:

- model or tool;
- human sponsor;
- date;
- starting repository commit;
- approximate run duration for major research sessions;
- whether external literature was read;
- which computations were actually executed;
- and which statements remain model-generated and unverified.

Model identity records provenance, not authority.

## Claim identifiers

Use the established prefixes:

```text
D-####  Definition
Q-####  Open question
O-####  Observation
C-####  Conjecture
K-####  Candidate counterexample
L-####  Lemma
T-####  Theorem
X-####  Computational experiment
R-####  Refutation or correction
M-####  Methodological or organizational proposal
```

The prefix is a document type, not a verification status. A complete-looking
proof enters no higher than `PROPOSED` before review.

## Pull requests

A pull request may contain one atomic claim, a coherent experiment, a review
report, a broad research program, a formalization packet, a synthesis, or an
organizational proposal.

Draft PRs are encouraged for ongoing research. A research PR may receive many
sessions and passes. Agents may add stronger results, corrections, computations,
responses to review, reports, and organizational improvements.

Every review and integration verdict freezes an exact source SHA. Later changes
are not automatically covered by an earlier verdict.

A stable subset may be extracted into `main` without closing the source PR.

PRs should state:

```text
Agent ID
Issue or research program
Starting commit
Exact contribution and new delta
Relationship to proving or disproving Collatz
Claim IDs and statuses
Dependencies and stacked PRs
Verification performed
Unresolved doubts
Failed approaches worth preserving
Files to inspect first
Suggested next attacks
Organizational suggestions
```

## Literature

Discovering that a target is a known open problem is useful information, but it
does not end the task.

Distinguish exact imported theorems, repository-native consequences, partial
overlap, analogy, and unverified source claims. Include exact citations, theorem
numbers, versions, and page ranges when available. Verify hypotheses and
normalization.

Do not upload copyrighted material without redistribution rights. A human may
supply a legally obtained paper or permitted excerpt directly to an agent when
the agent cannot access it itself.

## Computation

Record exact code and commands, environment, parameters, seeds, output or
digest, finite scope, interpretation, limitations, and an independent checker
where feasible.

Run a small representative job before scaling a large search. Measure runtime and
memory, validate the output and checker, estimate the full cost, and add
checkpoints.

Large searches should run outside GitHub Actions. Submit compact certificates,
manifests, hashes, and reproducible verifiers. GitHub Actions is verification
infrastructure, not distributed mathematical compute.

## Formalization

Formalization is welcome for stable definitions, equivalences, load-bearing
lemmas, certificate checkers, and the dependency spine of a proposed resolution.

Use a pinned toolchain. Promoted formal files should contain no admitted
placeholders such as `sorry`, and the connection between the formal statement
and intended mathematics must be audited.

## Failed work and organization

Do not erase a failed route when it teaches something reusable. Record what was
attempted, why it failed, what remains viable, and what future researchers should
not repeat.

The project's organization is itself experimental. The first integration pass
is expected to refine the canonical file layout, claim organization, review
workflow, and contributor practices in light of the actual research backlog.

## Licensing

By contributing to this repository, you agree that your contribution is licensed
under the repository's MIT License unless a file clearly states a different
compatible license. Third-party material remains under its original license.

## Conduct

Be direct about mathematical disagreement and respectful toward contributors.
Critique claims, proofs, computations, sources, and processes—not people.

Finding an error is a contribution. Admitting uncertainty is a strength.
