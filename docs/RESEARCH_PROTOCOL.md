# Research Protocol

## 1. Purpose

This protocol helps a large human–AI research effort remain cumulative,
auditable, and creative.

It is not intended to make all research small, conservative, or centrally
planned.

## 2. Operating layers

The repository uses:

1. `README.md` for public orientation;
2. `STATE.md` for integrated mathematical state;
3. `ROADMAP.md` for active and open lanes;
4. Discussions for broad exploration;
5. Issues for concrete coordination;
6. pull requests for durable artifacts;
7. reports for session history;
8. the claim registry for canonical status;
9. formalization and certificates for high-assurance results.

Chat history is not a durable mathematical dependency.

## 3. Contributor and agent identity

Substantial threads should use a persistent identifier.

Examples:

```text
human-gideon
gpt56-01
claude-03
cursor-sol-02
verifier-01
integrator-01
```

Record the human sponsor and model where relevant.

Independent work may use a related suffix:

```text
gpt56-01-a
gpt56-01-b
```

## 4. Research modes

### Open expedition

A self-directed program, potentially large.

### Focused mission

A bounded task with a concrete target.

### Verification

Independent reconstruction, refutation, source audit, or computation replay.

### Synthesis

Mapping, consolidation, comparison, or organizational improvement.

A thread may change modes.

## 5. Task ownership

Issues are coordination aids, not exclusive licenses to think.

A contributor may:

- claim a task;
- work independently on an already claimed task;
- open a new task;
- begin an expedition in Discussions or a draft pull request.

When multiple attempts exist, label whether they are:

```text
DEPENDENT
INDEPENDENT
REVIEW
SYNTHESIS
```

Claims of ownership expire when abandoned, but the prior work remains
preserved.

## 6. Branch conventions

Suggested branch form:

```text
agent/<agent-id>/<issue-or-expedition>-<short-name>
```

Fork contributors may use any clear branch name.

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

## 7. Claim identifiers

Use:

```text
D-####  definition
Q-####  open question
O-####  observation
C-####  conjecture
K-####  candidate counterexample
L-####  lemma
T-####  theorem
X-####  experiment
R-####  refutation
M-####  methodological proposal
```

Namespaces may be reserved by research program to avoid collisions.

## 8. Claim statuses

```text
IDEA
DEVELOPING
PROPOSED
INDEPENDENTLY_RECONSTRUCTED
FORMALLY_CHECKED
REFUTED
SUPERSEDED
```

Flags:

```text
EMPIRICAL
FINITE_SCOPE
PARTIAL
CONDITIONAL
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
```

Do not overload one status with several meanings.

## 9. Claim file structure

Recommended metadata:

```text
Claim ID:
Title:
Status:
Flags:
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

## 10. Gap audit

For major claims, deliberately check:

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
- mistaken novelty.

## 11. Candidate counterexamples

A `K-####` candidate should include:

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

A candidate remains a candidate until the object and the complete reasoning have
survived independent review.

## 12. Computational work

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
Limitations
Claims affected
```

Large generated files should normally live in an immutable external artifact
store or release, with a manifest and checksum committed to the repository.

## 13. Reports

Suggested path:

```text
reports/<agent-id>/<YYYY-MM-DD>-<topic>.md
```

Reports should preserve:

- starting hypothesis;
- approaches attempted;
- new results;
- failed approaches;
- possible errors;
- files changed;
- claims affected;
- current blocker;
- next attacks;
- organizational suggestions.

Reports may be exploratory. They should label epistemic status clearly.

## 14. Handoffs

A useful handoff says:

```text
HANDOFF FROM:
HANDOFF TO:
CURRENT CLAIM OR PROGRAM:
EXACT BLOCKER:
FILES TO READ:
WHAT HAS BEEN TRIED:
WHAT WOULD FALSIFY THE ROUTE:
MOST PROMISING NEXT MOVE:
MAIN RISK:
ORGANIZATIONAL IMPROVEMENT:
```

“Continue the proof” is not enough.

## 15. Independent verification

A verifier should:

1. freeze the source commit;
2. restate the claim independently;
3. reconstruct dependencies;
4. check quantifiers and edge cases;
5. search for counterexamples;
6. audit source theorems;
7. check ordinary versus `2`-adic realization;
8. check physical translation;
9. identify the first unsupported inference;
10. issue a precise verdict.

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

## 16. Open-problem behavior

The project does not treat “known open” as a prohibition.

An agent encountering an open boundary should:

- cite it;
- explain its relation;
- identify whether the current target is equivalent, stronger, or weaker;
- attempt a new route;
- avoid false certainty.

## 17. Circularity and loop audits

A research program should periodically ask:

- Did the last several passes strengthen the final implication?
- Is a new formalism doing mathematical work?
- Has finite compatibility been confused with ordinary existence?
- Has conditional growth been confused with construction?
- Is the remaining target just Collatz in disguise?
- Would a negative result eliminate an exhaustive class?
- Is there a concrete candidate on the positive side?

A loop audit is a steering tool, not an automatic shutdown.

## 18. Integrator role

The integrator maintains:

```text
STATE.md
canonical claim registry
review queue
dependency map
pre-public or release backlog
```

The integrator:

- preserves research freedom;
- reconciles status and notation;
- prevents silent promotion;
- maps stacks;
- requests review;
- extracts reusable tasks;
- records refutations;
- identifies circular duplication;
- improves repository structure.

The integrator does not decide truth by authority.

## 19. Process improvement

The project structure may change.

Substantial organizational proposals should state:

```text
Problem
Proposed change
Expected benefit
Risk
Trial
Success criterion
```

Agents and humans should propose improvements throughout the project, not only
at the end.

## 20. Non-negotiable boundaries

1. Never hide uncertainty.
2. Never call finite evidence an infinite proof.
3. Never rely on inaccessible chat context.
4. Never silently delete useful failed work.
5. Never silently promote speculation.
6. Never confuse a symbolic or `2`-adic object with an ordinary positive
   integer.
7. Never confuse proper-factor divisibility with full cycle closure.
8. Never treat model confidence, length, or style as evidence.
9. Never use open-problem status as a reason to refuse the research attempt.
10. Always leave a durable record.
