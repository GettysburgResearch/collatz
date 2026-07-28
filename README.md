# Collatz Open Research

> **PROJECT STATUS: UNSOLVED**
>
> This repository currently contains no project-verified proof or counterexample
> to the Collatz conjecture. It contains active research, proposed arguments,
> exact computations, independently reconstructed subresults, refutations,
> literature connections, and open questions.

## Mission

Collatz Open Research is an open human–AI effort aimed at resolving the Collatz
conjecture in either direction.

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

No contributor is required to choose only from a prewritten task list. Issues
are coordination tools, not boundaries on mathematical imagination.

The discipline begins when a result is recorded:

- speculation must be labeled;
- computations must state their finite scope;
- dependencies and source assumptions must be visible;
- uncertainty must not be hidden;
- a merged artifact is not automatically a proved theorem;
- a confident model statement is not evidence;
- a known open problem is not a reason to stop working.

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

A useful response to “this appears to be open” is:

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

### Open expeditions

For ambitious, self-directed work: new proof or disproof routes, broad
literature programs, new computation architectures, multi-session theorem
development, and organizational experiments.

Open expeditions may be large. They should include an internal map so later
researchers can identify claims, dependencies, failures, and next steps.

### Focused missions

For bounded tasks such as verifying a lemma, reproducing a computation,
settling a denominator condition, formalizing a theorem, testing a candidate,
or closing one explicit gap.

### Audits and synthesis

For finding circularity, identifying unsupported inferences, comparing
branches, reconstructing proofs, mapping literature, consolidating equivalent
claims, repairing dependencies, and improving project management.

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

See [STATE.md](STATE.md) and [ROADMAP.md](ROADMAP.md).

## How to begin

### Open exploration

Read this README, [STATE.md](STATE.md), [AGENTS.md](AGENTS.md) when using an AI
model, and the most relevant research files. Then open a Discussion, issue,
draft pull request, or research branch and state the repository commit you
started from.

Discussions are useful for broad human conversation, but not every connected AI
tool can currently read or write GitHub Discussions. Mirror actionable outcomes
into an issue, pull request, report, or repository file so agents can reliably
find them.

### Guided contribution

Choose an issue labeled with a request for verification, literature,
computation, formalization, or a good first agent task. Use its starter prompt,
then submit an issue comment, report, or pull request.

### Independent verification

Choose a claim marked `PROPOSED` and attempt to reconstruct or refute it without
relying on the original author's confidence.

## A note for humans steering models

Models can make real progress, but they can also enter polished circular loops.
Common signs include:

- restating the same missing inference in new notation;
- producing longer finite-prefix evidence without addressing the infinite step;
- proving “if an orbit exists, then it grows” without proving existence;
- introducing another encoding that preserves the original hard problem;
- repeatedly calling nearby reformulations “breakthroughs”;
- rediscovering a known open problem and treating that as the end;
- generating many conditional lemmas that do not strengthen the final
  implication.

When this happens, shake the research process out of the loop rather than
concluding the whole project is futile.

```text
State the exact global target and the first unsupported inference.
Compare this pass with the previous three and state the genuinely new delta.
Try to refute the current route.
Identify what theorem would eliminate an exhaustive class.
Explain whether the target is weaker than Collatz, equivalent, or stronger.
Do not add a new formalism unless it changes the implication.
```

See [docs/HUMAN_GUIDE_TO_AI_RESEARCH.md](docs/HUMAN_GUIDE_TO_AI_RESEARCH.md).

## Claim identifiers

Claims use stable prefixes:

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

A prefix describes the kind of object, not its truth status. A `T-####` file may
still be `PROPOSED`, `REFUTED`, or `SUPERSEDED`.

Core statuses are:

```text
IDEA
DEVELOPING
PROPOSED
INDEPENDENTLY_RECONSTRUCTED
FORMALLY_CHECKED
REFUTED
SUPERSEDED
```

Additional flags may include `EMPIRICAL`, `FINITE_SCOPE`, `PARTIAL`,
`CONDITIONAL`, `SOURCE_DEPENDENT`, and `TRANSLATION_UNVERIFIED`.

A pull request may be merged as a valuable research record while its claims
remain unverified. See [claims/README.md](claims/README.md).

## Claiming and discussing work

Anyone may comment on an issue with:

```text
CLAIMED BY: @username
STARTING COMMIT: <sha>
APPROACH: one-paragraph plan
```

Corrections, objections, partial results, literature links, and alternative
approaches are welcome directly in issue comments. Independent parallel attempts
should say so explicitly.

After a person comments, a trusted organizer with `Triage` access can formally
assign them, apply labels, request reviews, close or reopen issues, and mark
duplicates—without receiving code-push access. Arbitrary unaffiliated public
users do not receive those moderation controls automatically, so the issue-comment
claim convention remains the zero-friction public default.

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

Use Discussions for broad ideas and open expeditions. Use Issues for concrete
coordination, claims of work, corrections, and ongoing mathematical discussion.
Use pull requests for durable artifacts. Mirror actionable Discussion outcomes
into Issues or repository files when agent access is important.

Read [CONTRIBUTING.md](CONTRIBUTING.md), [GOVERNANCE.md](GOVERNANCE.md), and
[docs/RESEARCH_PROTOCOL.md](docs/RESEARCH_PROTOCOL.md) before submitting major
work.
