# Contributing to Collatz Open Research

Thank you for contributing.

This project is designed to support both small, reviewable tasks and ambitious,
self-directed research programs. The contribution process should help preserve
work without narrowing the range of ideas people are allowed to pursue.

## Choose a contribution mode

### Open expedition

Use this for a new or broad research direction.

Examples:

- a proof strategy;
- a counterexample program;
- a new invariant or representation;
- a large literature synthesis;
- a computational architecture;
- a multi-session theorem-development program;
- a proposed improvement to the organization of the repository.

An issue is helpful but not mandatory before the first exploratory work.
A Discussion or draft pull request is also an acceptable starting point.

For a large expedition, include a map:

```text
Research question
Connection to Collatz
Main objects and definitions
Claim inventory
Dependencies
Experiments
Known failures
Open blockers
Suggested review slices
Organizational suggestions
```

Large contributions are welcome. Make them navigable rather than artificially
small.

### Focused mission

Use this for a bounded task with an acceptance criterion.

Examples:

- audit a proof;
- reproduce an experiment;
- formalize a lemma;
- check a source theorem;
- test a candidate;
- settle one explicit implication.

Focused missions should normally reference an issue.

### Audit, refutation, or synthesis

Use this to improve the reliability or navigability of existing work.

A high-value audit may:

- find a counterexample;
- identify a hidden assumption;
- repair a statement;
- show two programs are equivalent;
- separate a genuine reduction from a restatement;
- consolidate duplicate claims;
- map the exact literature boundary;
- improve the project structure.

## Claim identifiers

Use the established claim prefixes:

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

The prefix is a document type, not a verification status.

## Issues, comments, and claims of work

Issue comments are a normal research surface. They may contain corrections,
small proofs, counterexamples, literature links, progress reports, or competing
approaches.

To claim work without elevated GitHub permissions, comment:

```text
CLAIMED BY: @username
STARTING COMMIT: <sha>
APPROACH: <short plan>
```

Formal GitHub assignment is optional. Multiple independent claims are allowed.

Broad work may begin in a Discussion or draft pull request. Because not every
AI connector exposes Discussions, any actionable outcome should be copied into
an Issue, PR, report, or repository document.

## Minimum information for durable work

Every substantial contribution should state:

```text
Contributor or agent ID:
Contribution mode:
Starting commit:
Research question:
What is new:
Claim IDs affected:
Dependencies:
Evidence:
Known uncertainty:
Files to inspect first:
Suggested next move:
```

This is a minimum record, not a restriction on the mathematical style of the
work.

## AI-assisted contributions

AI-assisted work is welcome.

Record:

- model or tool used, when known;
- date;
- starting repository commit;
- whether the model read external literature;
- which computations were actually executed;
- which statements remain model-generated and unverified.

Human sponsors remain responsible for submitting work honestly and for not
presenting model confidence as evidence.

No particular paid model or subscription is required.

## Literature

Discovering that a target is a known open problem is useful information, but it
does not end the task.

A literature contribution should distinguish:

```text
exact prior theorem
partial overlap
analogy
repository-native formulation
unverified source claim
```

Include exact citations, theorem numbers, editions or versions, and page ranges
when available.

Do not upload copyrighted material unless redistribution is permitted.

## Computation

Computational work should record:

- exact code;
- command;
- environment or lockfile;
- parameters;
- seeds;
- output or digest;
- independent checker where feasible;
- finite scope;
- mathematical interpretation;
- limitations.

A large search may run outside GitHub Actions. Submit a compact certificate,
manifest, and reproducible verifier.

## Proof and theorem claims

A complete-looking proof enters as `PROPOSED`.

The author does not promote it to `INDEPENDENTLY_RECONSTRUCTED`.
Promotion requires an independent review artifact.

A result may be:

- mathematically valuable;
- merged into the research record;
- still unverified.

These are compatible states.

## Pull requests

A pull request may contain:

- one atomic claim;
- a coherent experiment;
- a review report;
- a broad research packet;
- a synthesis or organizational proposal.

Large pull requests should provide a review map and divide the work into
independently inspectable claims or sections.

Draft pull requests are encouraged for long-running expeditions.

## Parallel work

Independent parallel attempts are welcome, including attempts on the same
question.

When overlap is discovered:

- cross-link the work;
- preserve independent derivations;
- identify genuine duplication;
- avoid rewriting another contributor's history;
- allow the integrator to reconcile canonical notation and status.

## Failed work

Do not erase a failed route when it teaches something reusable.

Record:

- what was attempted;
- why it failed;
- whether the failure is local or general;
- what remains viable;
- what future researchers should not repeat.

## Organizational proposals

The project's organization is itself experimental.

Contributors are encouraged to propose improvements to:

- issue structure;
- claim metadata;
- verification;
- integration;
- dashboards;
- literature mapping;
- data sharing;
- formalization;
- contributor onboarding;
- human–model collaboration.

Substantial proposals may use an `M-####` identifier.

## Conduct

Be direct about mathematical disagreement and respectful toward contributors.

Critique statements, proofs, computations, and processes—not people.

Finding an error is a contribution.
Admitting uncertainty is a strength.
