# Integrator Playbook

## Integrator principle

The integrator curates the research record.

The integrator does not decide mathematical truth by personal authority.

The key distinction is:

```text
merge the artifact
!=
promote the claim
```

## Research-freedom obligation

The integrator should preserve:

- open expeditions;
- large research programs;
- independent parallel attempts;
- speculative but clearly labeled ideas;
- organizational proposals;
- negative and failed results.

The integrator may request structure, provenance, and scope.
The integrator should not reject work merely because it is ambitious, open,
unconventional, or not on the current roadmap.

## Pass cadence

During active waves:

- triage approximately every two hours;
- integrate in deliberate windows;
- update the state daily;
- create periodic tagged snapshots.

No cadence should cause hurried theorem promotion.

## Inputs to each pass

Record:

```text
last integrated commit
time cutoff
new and updated pull requests
new issues and Discussions
new reviews
new claim-status requests
new computation artifacts
new literature sources
```

## Classify each contribution

Contribution mode:

```text
OPEN EXPEDITION
FOCUSED MISSION
VERIFICATION
REFUTATION
SYNTHESIS
ORGANIZATION
FORMALIZATION
COMPUTATION
LITERATURE
```

Integration action:

```text
MERGE AS RECORD
MERGE AFTER REPAIR
EXTRACT ATOMIC PACKET
REQUEST INDEPENDENT REVIEW
RESTACK
RETARGET
BLOCK ON SOURCE
BLOCK ON REPRODUCTION
ARCHIVE
SUPERSEDE
CLOSE AS DUPLICATE
```

Epistemic action:

```text
NO STATUS CHANGE
PROMOTE
NARROW
REFUTE
SUPERSEDE
ADD FLAG
REMOVE FLAG
```

These are separate decisions.

## Merge criteria for a research record

A research artifact may merge when:

- its provenance is clear;
- its scope is visible;
- its status labels are honest;
- it does not overwrite unrelated work;
- it is safe and licensed to publish;
- its files are navigable;
- large artifacts have manifests;
- claims are registered or explicitly exploratory;
- known doubts are recorded.

The artifact need not already be mathematically verified.

## Claim-promotion criteria

A promotion pull request should be small.

It should change only:

- claim status;
- review links;
- reviewer metadata;
- flags;
- formalization references;
- integrated state.

Require an independent reconstruction for promotion beyond `PROPOSED`.

## Large-packet integration

Large research pushes are allowed.

Before merging, require:

```text
program README
claim inventory
dependency map
experiment index
review-first list
current blocker
known failures
exact starting commit
```

Do not demand arbitrary fragmentation when the program is conceptually unified.

Extract load-bearing theorem packets for independent review.

## Stacked pull requests

For every stack record:

```text
base PR
base SHA
head PR
head SHA
dependency type
```

Rules:

- do not squash a parent while live children depend on its internal commits;
- integrate parents before children;
- retarget or rebase children after parent integration;
- maximum preferred live depth: two;
- preserve exact frozen SHAs in review reports.

## Circularity scan

During each pass, look for:

- duplicate equivalent formulations;
- repeated finite-prefix extensions;
- repeated conditional-growth statements;
- unresolved ordinary-extraction gaps;
- repeated proper-factor cycle work;
- new notation without a stronger implication;
- review loops that never identify an exact disputed step.

Do not simply close these programs.

Instead:

- consolidate;
- request a blocker audit;
- mark the exact unresolved inference;
- extract negative theorems;
- redirect one branch to adversarial review;
- keep genuinely new approaches open.

## State update

`STATE.md` should say:

- what is verified;
- what is proposed;
- what is refuted;
- what changed;
- what remains open;
- what would constitute genuine progress;
- which broad expeditions remain active.

Avoid promotional language.

## Review allocation

Prefer diversity:

- mathematical reconstruction;
- computational falsification;
- source audit;
- formal statement audit.

Do not count several identical model runs as fully independent without
disclosure.

## Integration report template

```text
INTEGRATION PASS
Time:
Cutoff:
Starting main:
Ending main:

MERGED AS RECORD
- ...

CLAIM PROMOTIONS
- ...

REFUTATIONS OR NARROWINGS
- ...

READY AFTER REPAIR
- ...

INDEPENDENT REVIEW WANTED
- ...

STACK OR DEPENDENCY ACTIONS
- ...

CIRCULARITY OR DUPLICATION FINDINGS
- ...

NEW OPEN EXPEDITIONS
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

Do not announce:

- “proof”;
- “counterexample”;
- “solved”;
- “breakthrough toward completion”;

based only on a merged author report.

Public updates should distinguish:

```text
new proposal
independently reconstructed subresult
exact finite computation
refutation
formalized lemma
resolution candidate
```

## First public-era objective

The first integration objective is not to choose a winning mathematics branch.

It is to create:

- a trustworthy public front door;
- a frozen backlog;
- a canonical state;
- a claim registry;
- a review queue;
- visible open expeditions;
- reliable contribution and artifact paths.
