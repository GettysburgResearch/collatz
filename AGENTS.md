# Agent entrypoint

You are entering an **unsolved** research repository. Produce durable, correctly scoped progress; do not make the project look solved.

## Read before acting

1. [`README.md`](README.md)
2. [`docs/RESEARCH_MAP.md`](docs/RESEARCH_MAP.md)
3. The relevant resident packet under [`research/integrated/`](research/integrated/README.md), or the relevant source-pinned family in [`research/RESULTS_CATALOG.md`](research/RESULTS_CATALOG.md)
4. The active source issue, PR, or research directory

Use [`archive/README.md`](archive/README.md) only for exact historical review, head, or lifecycle evidence.

## Choose one mode

### Explore

Unconventional proofs, constructions, analogies, computations, and literature connections are welcome. Free-form work belongs in `research/`, `experiments/`, `literature/`, or `reports/`.

Minimum discipline:

- state the map, normalization, and quantifiers;
- label the result `PROPOSED`, `EMPIRICAL`, `SOURCE-QUALIFIED`, `REFUTED`, or `OPEN`;
- separate finite evidence from all-depth conclusions;
- identify the first unsupported inference;
- preserve exact code and artifacts when they matter;
- say what remains missing.

No registry form is required before exploration.

### Review

Freeze the exact SHA first. Check hypotheses, algebra, quantifiers, notation, dependencies, citations, ordinary versus 2-adic realization, finite versus global scope, and artifact provenance. A verdict never extends to a later head without a delta review.

Use `VERIFIED`, `VERIFIED WITH FIXES`, `GAP/BLOCKED`, or `REJECTED`, with claim-level exceptions for mixed packets.

### Integrate

Prefer a clean proof packet over importing a long branch history. A durable packet needs:

- precise statement and scope;
- readable proof or exact proof extract;
- dependencies and notation;
- finite/ordinary/2-adic/all-depth boundaries;
- failed strengthenings and common misreadings;
- exact source PR, SHA, paths, review report, and evidence state;
- the next missing lemma.

Never silently repair a source theorem. Preserve the false original and give the repair a separate identity and review boundary.

For choosing source work, extracting packets, reviewing integrated wording, superseding duplicates, archiving evidence, and later closing source PRs, follow the gentle [`integration practice`](docs/INTEGRATION_PRACTICE.md). It is a lifecycle guide, not a prerequisite for exploratory research.

## Nonnegotiable mathematical checks

Before claiming progress toward a counterexample, ask:

1. Is there one fixed positive ordinary integer, or different witnesses at each depth?
2. Is the object ordinary, or merely in `Z_2`?
3. Is legality proved forever, or through a finite prefix?
4. For a cycle, is the **entire** denominator closed with exact replay?
5. Is every external theorem used in its exact normalization?
6. Was a computation independently replayed, merely inspected, or not run?

## Highest-value targets

- a fixed-source valuation bound proving SC\*;
- a complete all-word displacement obstruction proving FC\*;
- narrow review of the source-qualified periodic synthesis;
- narrow review of the proposed SC\*/FC\* bridge;
- boundedness or escape of a concrete aperiodic least-root sequence;
- an unbounded-state mechanism that survives the known automata and rigidity barriers.

## Repository safety

Work on a branch. Do not rewrite history, change settings, add workflows, push directly to `main`, or close another contributor’s PR without explicit authority. Do not run expensive searches merely to produce activity.

Finish by committing and pushing the result or refutation, recording the exact head, files to review, checks actually run, strongest uncertainty, and one useful handoff.
