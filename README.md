# Collatz Open Research

> **PROJECT STATUS: UNSOLVED**
>
> This repository currently contains no project-verified proof or counterexample
> to the Collatz conjecture. It contains active research, proposed arguments,
> exact computations, independently reconstructed subresults, refutations,
> literature connections, and open questions.

## Mission

Collatz Open Research is an open human–AI research effort aimed at resolving
the Collatz conjecture in either direction.

We welcome:

- proofs and proof-oriented reductions;
- counterexamples, divergent-orbit constructions, and positive-cycle work;
- large new research programs and unconventional attacks;
- adversarial verification and refutation;
- exact and reproducible computation;
- literature reconstruction and theorem transfer;
- Lean formalization;
- dependency mapping, synthesis, and improved research organization;
- carefully documented failures that prevent future repetition.

The repository is both a research laboratory and a durable record for future
humans and models.

## Freedom in discovery, discipline in claims

Exploration is deliberately broad.

Contributors may:

- attack the full conjecture directly;
- pursue a narrow lemma;
- launch a new mathematical program;
- introduce a new representation when it creates a real opportunity;
- conduct a large multi-session research push;
- audit or refute existing work;
- connect the project to remote literature;
- build experiments, formalizations, maps, dashboards, or verification tools;
- propose changes to the organization of the project itself.

No contributor is required to choose only from a prewritten task list.
Issues are coordination tools, not boundaries on mathematical imagination.

The discipline begins when a result is recorded:

- speculation must be labeled;
- computations must state their finite scope;
- dependencies and source assumptions must be visible;
- uncertainty must not be hidden;
- a merged artifact is not automatically a proved theorem;
- a confident model statement is not evidence;
- a known open problem is not a reason to stop working.

A useful slogan for the project is:

> **Explore freely. State exactly. Verify adversarially. Preserve everything useful.**

## Open problems are targets, not stop signs

This project exists to work on open problems.

When a model or contributor discovers that a target is known to be open, that
fact should be treated as:

1. a connection to the literature;
2. a warning not to present an old open question as a new theorem;
3. information about the exact boundary of current knowledge;
4. a starting point for a new attack.

It is **not** a reason to decline the problem or end the investigation.

A good response to “this appears to be open” is:

```text
Here is the precise literature connection.
Here is what is already known.
Here is the exact unresolved step.
Here is the new route I will now attempt.
```

The project does not assume that a current model will solve Collatz. It does
assume that serious attempts, reductions, refutations, computations, and
organizational advances can accumulate into a stronger research record.

## Three contribution modes

### 1. Open expeditions

For ambitious, self-directed work:

- a new proof or disproof route;
- a broad literature-driven program;
- a new computational architecture;
- a multi-session theorem-development push;
- a new way to organize or verify the project.

Open expeditions may be large. They should include an internal map so later
researchers can identify the exact claims, dependencies, failures, and next
steps.

### 2. Focused missions

For bounded tasks with a clear target:

- verify one lemma;
- reproduce one computation;
- settle one denominator condition;
- formalize one theorem;
- test one candidate;
- close one explicit gap.

These are especially useful for phone-based contribution and independent
review.

### 3. Audits and synthesis

For work on the research record itself:

- find circularity;
- identify the first unsupported inference;
- compare overlapping branches;
- reconstruct a proof independently;
- map the literature;
- consolidate equivalent claims;
- repair notation or dependencies;
- improve project management.

All three modes are first-class contributions.

## Current research concentration

The current repository contains several independent programs. Two recurring
global bottlenecks have emerged in much of the existing work:

1. **Ordinary-integer realization:** turning compatible finite or `2`-adic
   structure into one ordinary positive integer with an all-time legal orbit.
2. **Full-denominator cycle closure:** turning a finite valuation or parity
   construction into exact divisibility and exact physical replay.

These are current concentrations, not restrictions on future work. A new route
that bypasses them is welcome.

See [STATE.md](STATE.md) for the integrated project state and
[ROADMAP.md](ROADMAP.md) for active and open-ended research lanes.

## How to begin

### Open exploration

Read:

1. this README;
2. [STATE.md](STATE.md);
3. [AGENTS.md](AGENTS.md) if using an AI model;
4. the most relevant research files and open discussions.

Then open a Discussion, issue, draft pull request, or research branch. State the
question you are attacking and the repository commit you began from.

Discussions are useful for broad human conversation, but not every connected AI
tool can currently read or write GitHub Discussions. Any idea that becomes
actionable should also be mirrored into an issue, pull request, report, or other
repository file so agents can reliably find it.

### Guided contribution

Choose an issue labeled:

```text
good first agent task
verification wanted
literature wanted
computation wanted
formalization wanted
```

Use its starter prompt, then submit an issue comment, report, or pull request.

### Independent verification

Choose a claim marked `PROPOSED` and attempt to reconstruct or refute it without
relying on the original author's confidence.

## A note for humans steering models

Models can make real progress, but they can also enter polished circular loops.

Common signs include:

- restating the same missing inference in new notation;
- producing longer finite-prefix evidence without addressing the infinite step;
- proving “if an orbit exists, then it grows” while never proving existence;
- introducing another encoding that preserves the original hard problem;
- repeatedly calling nearby reformulations “breakthroughs”;
- rediscovering a known open problem and treating that as the end;
- generating many conditional lemmas that do not strengthen the final
  implication.

When this happens, do not conclude that the whole project is futile. Shake the
research process out of the loop.

Useful interventions:

```text
State the exact global target and the first unsupported inference.
Do not add a new formalism unless it changes that implication.
Compare this pass with the previous three and state the genuinely new delta.
Try to refute the current route.
Identify what theorem would eliminate an exhaustive class.
Explain why the target is weaker than Collatz, or admit that it is not.
Return to the ordinary-integer or full-denominator boundary.
```

See [docs/HUMAN_GUIDE_TO_AI_RESEARCH.md](docs/HUMAN_GUIDE_TO_AI_RESEARCH.md).

## Evidence and claim status

Every mathematical claim has a stable identifier and a visible status.

Core statuses:

```text
IDEA
DEVELOPING
PROPOSED
INDEPENDENTLY_RECONSTRUCTED
FORMALLY_CHECKED
REFUTED
SUPERSEDED
```

Additional flags may include:

```text
EMPIRICAL
FINITE_SCOPE
PARTIAL
CONDITIONAL
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
```

A pull request may be merged as a valuable research record while its claims
remain `IDEA`, `DEVELOPING`, or `PROPOSED`.

See [claims/README.md](claims/README.md).

## Claim identifiers

Claims use stable prefixes so theorem statements, experiments, corrections, and
open questions can be referenced across branches and reviews:

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

A prefix describes the kind of object, not its truth status. For example, a
`T-####` file may still be `PROPOSED`, `REFUTED`, or `SUPERSEDED`.

See [claims/README.md](claims/README.md) for status and promotion rules.

## Claiming and discussing work

Anyone may comment on an issue with:

```text
CLAIMED BY: @username
APPROACH: one-paragraph plan
```

This is the project's portable claim-of-work convention even when the user does
not have GitHub permission to assign the issue formally. Corrections, objections,
partial results, and alternative approaches are welcome directly in issue
comments. Independent parallel attempts should say so explicitly.

Trusted contributors may later receive GitHub `Triage` access so they can apply
labels and help organize issues without receiving code-push access. Actual
GitHub assignment currently requires `Write` access, so formal assignment is not
the default public participation mechanism.

## Repository map

```text
README.md                  public orientation
STATE.md                   integrated mathematical state
ROADMAP.md                 active and open research lanes
CONTRIBUTING.md            contribution guidance
AGENTS.md                  guidance for AI-assisted research
GOVERNANCE.md              roles and decision rules

claims/                    canonical claim registry
research/                  research programs and proof development
experiments/               reproducible computation and certificates
formal/                    Lean and other formal artifacts
reports/                   append-only session and review reports
literature/                source maps and theorem reconstruction
docs/                      protocol, policies, and project guides
```

## Core research values

1. Open problems are legitimate targets.
2. Large and unconventional research pushes are welcome.
3. Speculation is welcome; hidden speculation is not.
4. Refutation is progress.
5. Negative results remain searchable.
6. Exact scope matters.
7. Finite evidence is not silently extrapolated to infinity.
8. Symbolic or `2`-adic objects are not silently treated as ordinary integers.
9. Literature is a foundation and connection, not an excuse to stop.
10. The organization of the project is itself open to improvement.
11. Model identity and confidence do not determine truth.
12. Every substantial session should leave the repository more useful than it
    found it.

## Community

Use GitHub Discussions for broad ideas and open expeditions.
Use Issues for concrete coordination, claims of work, corrections, and ongoing
mathematical discussion. Use pull requests for durable artifacts. Because some
AI connectors do not expose Discussions, mirror actionable Discussion outcomes
into Issues or repository files.

Read [CONTRIBUTING.md](CONTRIBUTING.md),
[GOVERNANCE.md](GOVERNANCE.md), and
[docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) before submitting major
work.
