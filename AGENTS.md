# Agent entrypoint

You are entering an **unsolved** open-research repository. Your job is to create durable, correctly scoped progress—not to make the project look solved.

## Read before acting

1. [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md)
2. [`FRONTIERS.md`](FRONTIERS.md)
3. The relevant packet under [`research/integrated/`](research/integrated/README.md)
4. The active source issue, PR, or research directory for your chosen task

Use [`archive/`](archive/README.md) only when you need exact historical review or lifecycle evidence.

## Choose one mode

### Explore

You may pursue an unconventional proof, counterexample architecture, analogy, computation, representation, or literature connection. Free-form work belongs in an existing `research/`, `experiments/`, `literature/`, or `reports/` area, or in a focused new directory.

Minimal requirements:

- state the map and normalization;
- label the claim `PROPOSED`, `EMPIRICAL`, `SOURCE-QUALIFIED`, `REFUTED`, or `OPEN` as appropriate;
- separate finite evidence from all-depth conclusions;
- identify the first unsupported inference;
- preserve exact code/artifacts when they matter;
- write what remains missing.

No registry form is required for exploration.

### Review

Freeze the exact source SHA first. Check hypotheses, quantifiers, algebra, notation, dependencies, citations, finite-versus-global scope, ordinary-versus-2-adic realization, and artifact provenance. Do not let a verdict drift to a later head without a delta review.

Use verdicts:

- `VERIFIED`
- `VERIFIED WITH FIXES`
- `GAP/BLOCKED`
- `REJECTED`

A branch-level verdict may contain passing and failing claims. Record claim-level exceptions.

### Integrate

Prefer clean extraction over importing a long branch history. An integrated packet needs:

- a precise statement and scope;
- a readable proof or exact proof extract;
- dependencies and notation;
- ordinary/2-adic/finite/all-depth boundaries;
- failed strengthenings and common misreadings;
- exact source PR, SHA, files, review report, and evidence state;
- the next missing lemma.

Never silently repair a source theorem. Preserve the original and give the repair a separate identity and review boundary.

## Nonnegotiable mathematical checks

Before claiming progress toward a positive counterexample, ask:

1. Is there one fixed positive ordinary integer, or only different witnesses at each depth?
2. Is the object ordinary, or merely in `Z_2`?
3. Is legality proved forever, or only through a finite prefix?
4. For a cycle, is the **entire** denominator closed with exact replay?
5. Is an external theorem used in its exact normalization?
6. Was a large computation independently replayed, merely inspected, or not run?

## Current highest-value targets

- a fixed-source valuation bound proving SC\*;
- a complete all-word displacement obstruction proving FC\*;
- narrow independent review of the integrated periodic-tail synthesis;
- narrow independent review of the proposed SC\*/FC\* bridge;
- boundedness or escape of a concrete aperiodic least-root sequence;
- a genuinely unbounded-state mechanism that survives the known automata and rigidity barriers.

See [`FRONTIERS.md`](FRONTIERS.md) for exact formulations.

## Git and repository safety

- Work on a branch and use a draft PR for unfinished work.
- Do not rewrite history, change settings, enable workflows, or push directly to `main`.
- Do not merge or close another contributor’s PR without explicit integration authority.
- Do not run expensive searches merely to produce activity. Pilot first and state the cost and proof role.

## Finish every session durably

Commit and push the result or the refutation. Update the PR or issue with:

- exact head SHA;
- what was proved, observed, refuted, or left open;
- files to review first;
- checks actually run;
- strongest uncertainty;
- one useful handoff.

A failed approach with a clear first obstruction is useful research. An unrecorded insight is not.
