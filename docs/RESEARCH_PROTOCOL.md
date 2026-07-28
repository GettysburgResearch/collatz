# Research Protocol

## Purpose

This protocol helps Agentic Polymath #1 remain cumulative, auditable, and
creative. It expands on the main README; it is not intended to make all research
small, conservative, or centrally planned.

## Operating layers

The repository uses:

1. `README.md` for the primary operating rules and public orientation;
2. `STATE.md` for integrated mathematical state;
3. `ROADMAP.md` for active and open lanes;
4. Issues for tasks, broad programs, discussion, corrections, and handoffs;
5. pull requests for living, durable research artifacts;
6. reports for append-only session history;
7. the claim registry for canonical identifiers and statuses;
8. formalization and certificates for high-assurance results;
9. integration passes for dependency-aware incorporation into `main`.

Discussions may be useful for humans, but some agents cannot access them. Mirror
actionable outcomes into the durable layers above.

Private chat history is not a mathematical dependency.

## Agent identity

Substantial threads use a unique persistent identifier chosen by the agent.

Examples:

```text
human-gideon
gpt56-euler-01
claude-opus-03
cursor-sol-02
verifier-gauss-01
integrator-01
```

Record human sponsor and model where relevant. Independent work may use related
suffixes such as `gpt56-euler-01-a` and `gpt56-euler-01-b`.

Identity records provenance, not authority.

## Research shapes

### Open research program

A self-directed program, potentially large and multi-session.

### Focused task

A bounded target with a concrete statement or acceptance condition.

### Verification, correction, or refutation

Independent reconstruction, source audit, counterexample search, formal audit,
or computation replay.

### Synthesis and organization

Mapping, consolidation, comparison, dashboard creation, task decomposition, or
process improvement.

A thread may change shape.

## Issues and claims of work

Issues are the primary agent-readable coordination layer. They are coordination
aids, not exclusive licenses to think and not a boundary on allowed research.

Agents should normally comment:

```text
CLAIMED BY: <agent-id>
STARTED: <UTC timestamp>
STARTING COMMIT: <sha>
BRANCH: <branch>
APPROACH: <short plan>
```

A new exploration may begin before the Issue exists, but it should become
discoverable once substantial.

Multiple independent attempts are welcome. Comments may contain corrections,
small proofs, counterexamples, literature, computations, competing approaches,
and review findings.

## Branch and commit conventions

Suggested branch form:

```text
agent/<agent-id>/<issue-or-topic>-<short-name>
```

Commit prefixes:

```text
idea:
construction:
proof:
experiment:
verification:
refutation:
report:
organization:
docs:
formal:
```

These are conventions, not reasons to reject useful work.

## Long-lived PRs

Research PRs may receive many sessions and repeated extensions. Keep the summary
current and state the new delta.

Every review or integration action freezes an exact source SHA. Later changes
are not automatically covered.

A stable subset may be extracted into the canonical repository without closing
the source PR.

Only integrators should close or supersede another contributor's active PR.

## Claim identifiers

Use:

```text
D-####  definition
Q-####  open question
O-####  observation
C-####  conjecture
K-####  candidate counterexample
L-####  lemma
T-####  theorem
X-####  computational experiment
R-####  refutation or correction
M-####  methodological or organizational proposal
```

Namespaces may be reserved by research program. Branch-qualified historical IDs
must not be silently renumbered.

## Claim status

Primary status:

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

Orthogonal qualifiers:

```text
CONDITIONAL
FINITE_SCOPE
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
COMPUTATION_NOT_REPLAYED
FORMALLY_CHECKED
```

A prefix identifies the object type, not truth. Artifact integration and claim
promotion are separate.

## Claim-file structure

Recommended metadata:

```text
Claim ID:
Title:
Status:
Qualifiers:
Authoring contributors:
Reviewing contributors:
Created:
Last updated:
Starting commit:
Dependencies:
Scope:
Related candidates:
Formalization:
```

Recommended sections:

```text
Statement
Definitions
Motivation
Proof or construction
Dependency audit
Literature boundary
Gap audit
Adversarial tests
Remaining uncertainty
Suggested next attack
Organizational observations
```

## Gap audit

For major claims, check deliberately:

- hidden finiteness assumptions;
- unjustified induction;
- missing boundary cases;
- finite-to-infinite extrapolation;
- invalid interchange of limits;
- circular dependence;
- nonuniform estimates;
- positivity and integrality;
- whole-denominator versus proper-factor divisibility;
- symbolic versus physical dynamics;
- `2`-adic versus ordinary integers;
- assumptions equivalent to the desired conclusion;
- source normalization;
- mistaken novelty;
- unsupported translation between alternate maps and standard Collatz.

## Resolution candidates

A `K-####` counterexample candidate should include:

```text
Exact object
Claimed failure mode
Translation to Collatz
Existence
Integrality
Positivity
All-time consistency or finite cycle closure
Exact replay
Verification plan
Known doubts
```

A proof-side resolution candidate should include the exact standard theorem,
complete dependency graph, alternate-map equivalences, boundary cases, and every
computer-assisted certificate.

A candidate remains a candidate until the object and complete reasoning survive
the required reviews.

## Computational work

Every proof-relevant experiment should record:

```text
Experiment ID
Question
Code
Command
Environment
Parameters
Seeds
Output or digest
Certificate
Independent checker
Interpretation
Finite scope
Limitations
Claims affected
```

Large generated data should normally live in an immutable external artifact
store or release, with a manifest and checksum committed to the repository.

GitHub Actions and CI are for bounded verification, not distributed mathematical
compute. Large searches, solver campaigns, and model inference run elsewhere and
return compact reproducible artifacts.

## Literature behavior

A known open problem is not a stop sign.

An agent encountering an open boundary should:

- cite the exact literature;
- reconstruct the relevant theorem and hypotheses;
- distinguish theorem, repository consequence, overlap, analogy, and unverified
  source claim;
- identify whether the new target is weaker, equivalent, or stronger;
- attempt the new step;
- avoid false certainty.

## Formalization

Prioritize canonical definitions, equivalences, stable independently reviewed
lemmas, certificate checkers, and the resolution dependency spine.

Use a pinned toolchain. Promoted files should contain no admitted placeholders.
Audit the translation from encoded statement to intended mathematics.

## Reports

Suggested path:

```text
reports/<agent-id>/<YYYY-MM-DD>-<issue-or-topic>-<short-name>.md
```

Reports should preserve:

- starting commit and hypothesis;
- approaches attempted;
- new results and exact status;
- computations and literature;
- failed approaches;
- possible errors;
- files and claims affected;
- current blocker;
- next attacks;
- organizational suggestions.

## Handoffs

A useful handoff says:

```text
HANDOFF FROM:
HANDOFF TO:
CURRENT CLAIM OR PROGRAM:
FROZEN SOURCE SHA:
EXACT BLOCKER:
FILES TO READ:
WHAT HAS BEEN TRIED:
WHAT WOULD FALSIFY THE ROUTE:
MOST PROMISING NEXT MOVE:
MAIN RISK:
ORGANIZATIONAL IMPROVEMENT:
```

“Continue the proof” is not enough.

## Independent verification

A verifier should:

1. freeze the source commit;
2. restate the claim independently;
3. reconstruct dependencies;
4. check quantifiers, signs, and edge cases;
5. search for counterexamples;
6. audit source theorems and normalizations;
7. check ordinary versus `2`-adic realization;
8. check full denominator and exact replay for cycles;
9. check physical translation;
10. identify the first unsupported inference;
11. issue a precise verdict.

Suggested verdicts:

```text
PASSED WITHIN SCOPE
GAP
REFUTED
SCOPE NARROWING REQUIRED
SOURCE RECONSTRUCTION REQUIRED
COMPUTATION REPLAY REQUIRED
NOT YET REPRODUCED
SUPERSEDED
```

`NOT YET REPRODUCED` is neutral.

## Circularity audits

A program should periodically ask:

- Did recent passes strengthen the final implication?
- Is a new formalism doing mathematical work?
- Has finite compatibility been confused with ordinary existence?
- Has conditional growth been confused with construction?
- Is a proper denominator factor being confused with cycle closure?
- Is the remaining target just Collatz in disguise?
- Would a negative result eliminate an exhaustive class?
- Is there a concrete candidate on the positive side?

A loop audit is a steering tool, not an automatic shutdown.

## Integrator role

The integrator maintains:

```text
STATE.md
canonical claim registry
review queue
dependency map
integration backlog
```

The integrator preserves research freedom, reconciles status and notation,
prevents silent promotion, maps stacks, requests review, extracts reusable
packets, records refutations, identifies circular duplication, and improves
repository structure.

The integrator does not decide truth by authority.

## Process improvement

The project structure may change. Substantial proposals should state:

```text
Problem
Proposed change
Expected benefit
Risk
Trial
Success criterion
```

Agents and humans should propose improvements throughout the project.

## Non-negotiable boundaries

1. Never hide uncertainty.
2. Never call finite evidence an infinite proof.
3. Never rely on inaccessible chat context.
4. Never silently delete useful failed work.
5. Never silently promote speculation.
6. Never confuse a symbolic or `2`-adic object with an ordinary positive integer.
7. Never confuse proper-factor divisibility with full cycle closure.
8. Never treat model confidence, length, style, or credentials as evidence.
9. Never use open-problem status as a reason to refuse the research attempt.
10. Never use GitHub Actions as distributed mathematical compute.
11. Always leave a durable record.
