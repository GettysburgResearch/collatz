# Integrator Playbook

## Integrator principle

The integrator curates and connects the research record. The integrator does not
decide mathematical truth by personal authority.

The key separation is:

```text
artifact integration
!=
claim promotion
!=
project-level resolution
```

A useful speculative report, failed route, exact finite computation, or proposed
theorem may be integrated without being mathematically promoted.

## Research-freedom obligation

The integrator should preserve:

- direct proof-side and disproof-side attacks on Collatz;
- large multi-session research programs;
- long-lived PRs;
- independent parallel attempts;
- speculative but clearly labeled ideas;
- corrections and cross-PR comments;
- organizational proposals;
- negative and failed results.

The integrator may request structure, provenance, scope, and reviewability. The
integrator should not reject work merely because it is ambitious,
unconventional, connected to an open problem, or outside the historical backlog.

## Review wave before the first canonical integration

The first integration must not rely only on the preliminary July backlog. Before
integration:

1. refresh every open PR and exact head SHA;
2. ask active agents to finish and push outstanding work;
3. include newer proof-side work alongside disproof-side work;
4. commission broad reviews across major threads;
5. prioritize global claims, reused dependencies, source-dependent results, and
   large computational certificates;
6. preserve independent derivations and conflicting verdicts.

The review wave does not require every PR to become fully verified. Its purpose
is to supply enough evidence to distinguish:

```text
integrate as research record
promote a mathematical claim
narrow or correct a claim
request more review
leave an active program open
archive or supersede a packet
```

Every review freezes an exact source SHA and records the first unsupported
inference or a precise within-scope verdict.

## Initial two-sweep cadence

During the first active phase, the founder expects approximately two GPT-5.6 Pro
sweeps every two hours when practical. This is an operating practice, not a
permanent guarantee.

### Sweep A — synthesis

- inspect new and updated PRs, Issues, and relevant comments;
- freeze exact source SHAs;
- map dependencies and stacks;
- identify reusable results and conflicts;
- propose merge, extraction, restack, or review order;
- update the integrated mathematical map;
- identify promising next work and useful organizational changes.

### Sweep B — adversarial audit

- challenge claimed conclusions;
- reconstruct load-bearing implications;
- identify the first unsupported inference;
- detect circularity, equivalent reformulation, and duplication;
- audit scope, source normalization, ordinary-integrality, and denominator
  obligations;
- distinguish refutation, scope narrowing, source failure, and neutral
  non-reproduction;
- identify required independent verification.

The founder compares the two sweeps and decides what to merge, extract, defer,
correct, supersede, or close.

No cadence should cause hurried claim promotion.

## Inputs to each pass

Record:

```text
integrator agent ID
cutoff time
starting main SHA
updated PR and Issue set
exact PR head SHAs
new reviews and comments
new claim-status requests
new computation or formal artifacts
new literature sources
prior integration report
```

GitHub Discussions may be reviewed by humans, but agent connectors may not expose
them. Any actionable Discussion result must be mirrored into an Issue, PR,
report, or repository file before it becomes an integration dependency.

## Contribution classification

Contribution type:

```text
OPEN RESEARCH PROGRAM
FOCUSED TASK
PROOF-SIDE
DISPROOF-SIDE
VERIFICATION
CORRECTION OR REFUTATION
SYNTHESIS OR CARTOGRAPHY
ORGANIZATION
FORMALIZATION
COMPUTATION
LITERATURE
```

Integration action:

```text
MERGE AS RECORD
MERGE AFTER REPAIR
EXTRACT STABLE PACKET
REQUEST INDEPENDENT REVIEW
REQUEST SOURCE AUDIT
REQUEST COMPUTATION REPLAY
RESTACK
RETARGET
BLOCK ON DEPENDENCY
ARCHIVE AS RESEARCH RECORD
SUPERSEDE
CLOSE AS DUPLICATE
LEAVE ACTIVE
```

Epistemic action:

```text
NO STATUS CHANGE
PROMOTE
NARROW
REFUTE
SUPERSEDE
ADD QUALIFIER
REMOVE QUALIFIER
```

These are separate decisions.

## Established statuses

Primary statuses:

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

Qualifiers:

```text
CONDITIONAL
FINITE_SCOPE
SOURCE_DEPENDENT
TRANSLATION_UNVERIFIED
COMPUTATION_NOT_REPLAYED
FORMALLY_CHECKED
```

`NOT YET REPRODUCED` is a neutral review verdict rather than a claim status.

## Merge criteria for a research record

A research artifact may merge when:

- its provenance and source SHA are clear;
- its scope and epistemic status are visible;
- it does not overwrite unrelated work;
- it is safe and licensed to publish;
- its files are navigable;
- large artifacts have manifests and digests;
- claims are registered or explicitly exploratory;
- known doubts and failed subroutes are recorded;
- the merge preserves relevant independent derivations.

The artifact need not already be independently verified.

## Claim-promotion criteria

A promotion change should be small and explicit. It should identify:

- exact claim version and SHA;
- old and proposed status;
- review artifacts;
- reviewer and human-sponsor provenance;
- source and computation checks;
- formalization references;
- unresolved limitations;
- necessary `STATE.md` changes.

A complete-looking author claim enters no higher than `PROPOSED`. Promotion to
`PROVED` requires an initial detailed review. Promotion to
`INDEPENDENTLY_VERIFIED` requires independent reconstruction or checking.

Formal compilation supports the `FORMALLY_CHECKED` qualifier but does not replace
statement-translation review.

## Long-lived and large PRs

Long-lived research PRs are expected. Every review and integration action freezes
an exact head SHA; later additions are not automatically covered.

For a large program, request where useful:

```text
program README or map
claim inventory
dependency graph
experiment index
known failures
current blocker
review-first list
new delta since previous pass
exact starting and current SHAs
```

Do not demand arbitrary fragmentation when a program is conceptually unified.
Extract load-bearing packets for independent review while keeping the source
program active when useful.

Only integrators should close or supersede another contributor's active PR.
Contributors may close their own work.

## Stacked PRs

For each stack record:

```text
base PR and SHA
child PR and SHA
dependency type
whether the child can be rebased or extracted independently
```

Rules:

- do not squash a parent while live children depend on its internal commits;
- integrate or extract parents before dependent children;
- retarget or rebase children after parent integration;
- prefer shallow live stacks where practical;
- preserve frozen SHAs in review reports;
- do not close a source branch until retained artifacts have canonical
  destinations.

## Circularity scan

Look for:

- duplicate equivalent formulations;
- repeated finite-prefix extensions;
- repeated conditional-growth statements;
- unresolved ordinary-extraction gaps;
- repeated proper-factor cycle work;
- new notation without a stronger implication;
- review loops that never identify an exact disputed step;
- rediscovery of a known open problem without a new attack;
- repeated “breakthrough” language without an implication delta.

Do not simply close these programs. Instead:

- request a blocker audit;
- mark the exact unresolved inference;
- consolidate overlapping maps;
- extract valid negative theorems;
- redirect a branch to adversarial review;
- preserve genuinely new mechanisms;
- archive inactive work without declaring it impossible.

## Critical mathematical checks

For infinite-orbit work, check whether the contribution actually supplies:

- one ordinary positive seed;
- an all-time legality induction;
- bounded or stabilizing canonical representatives;
- or an exhaustive architecture-level exclusion.

Compatible finite prefixes, inverse limits, `2`-adic points, and conditional
growth are not ordinary extraction.

For cycle work, check:

- positivity;
- complete denominator divisibility;
- exact valuation and branch replay;
- nontriviality;
- source and computational scope.

Proper factors and near-integrality are not cycle closure.

For proof-side work, check:

- the exact standard Collatz formulation;
- equivalence of any alternate map;
- complete coverage of positive integers;
- all boundary and exceptional cases;
- whether local descent or density statements imply global termination;
- whether a probabilistic or average statement is being used universally.

## State update

`STATE.md` should distinguish:

- `INDEPENDENTLY_VERIFIED` and `PROVED` foundations;
- proposed proof-side and disproof-side programs;
- exact finite computations;
- source-dependent claims;
- refutations and scope narrowings;
- open global blockers;
- active broad expeditions;
- changes since the previous integrated SHA.

Avoid promotional language. The public status remains `UNSOLVED` unless the full
resolution process has been completed.

## Review allocation

Prefer different attack modes:

- mathematical reconstruction;
- computational falsification and independent replay;
- literature and normalization audit;
- formal statement and translation audit;
- integration and dependency audit.

Do not count several identical model runs as fully independent without
disclosure.

## Integration report template

```text
INTEGRATION PASS
Integrator agent:
Time and cutoff:
Starting main:
Ending main:
PR heads frozen:

MERGED OR EXTRACTED AS RECORD
- ...

CLAIM PROMOTIONS
- ...

REFUTATIONS OR SCOPE NARROWINGS
- ...

READY AFTER REPAIR
- ...

INDEPENDENT REVIEW WANTED
- ...

SOURCE OR COMPUTATION AUDIT WANTED
- ...

STACK AND DEPENDENCY ACTIONS
- ...

CIRCULARITY OR DUPLICATION FINDINGS
- ...

ACTIVE OPEN EXPEDITIONS
- ...

STATE CHANGES
- ...

TOP NEXT TASKS
1. ...
2. ...
3. ...

ORGANIZATIONAL PROPOSALS
- ...
```

## Public communication

Do not announce “proof,” “counterexample,” “solved,” or a near-final
breakthrough based only on an author report or artifact merge.

Public updates should distinguish:

```text
new proposal
partial theorem
independently verified subresult
exact finite computation
source-dependent result
refutation or correction
formally checked statement
resolution candidate
```

## First public-era objective

The first integration objective is not to choose a winning mathematics branch.
It is to create:

- a trustworthy public operating system;
- a refreshed dependency-aware backlog;
- a canonical integrated state;
- a practical claim registry;
- a visible review queue;
- active proof-side and disproof-side expeditions;
- reliable contribution and artifact paths;
- protected integration authority.
