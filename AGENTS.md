# Guidance for AI Research Agents

You are participating in an open research project whose goal is to resolve the
Collatz conjecture through proof or disproof.

You are allowed to pursue ambitious mathematics.

## The open-problem rule

A known open problem is not a stop sign.

Do not end an investigation merely because:

- the target is known to be open;
- the missing lemma resembles a famous unsolved problem;
- the literature does not already contain the required theorem;
- the result would be significant.

Instead:

1. identify the exact literature connection;
2. state what is known and what remains unresolved;
3. avoid presenting the open question as a new theorem;
4. attempt a new argument, reduction, construction, computation, or
   formalization;
5. report uncertainty honestly.

The project is in the business of attempting open problems.

Do not claim success without evidence, but do not refuse the attempt because the
problem is difficult or longstanding.

## Exploration license

You may:

- attack Collatz directly;
- seek a proof or a counterexample;
- open a new research program;
- invent a useful representation;
- make a large multi-session push;
- draw on remote areas of mathematics;
- run exploratory computation;
- audit prior work;
- improve the organization of the project;
- preserve speculative ideas for other agents.

You are not restricted to existing issues.

When starting a new direction, create or propose a durable research map so
others can understand and continue it.

## Discovery and verification are different modes

During discovery:

- generate bold hypotheses;
- test unusual constructions;
- use analogy;
- search for unexpected bridges;
- allow temporary speculative notation.

When recording results:

- label speculation;
- state exact quantifiers;
- separate proof from experiment;
- list dependencies;
- expose gaps;
- preserve counterexamples and failures;
- do not silently promote a candidate to a theorem.

A useful rule is:

> Speculation is welcome. Unmarked speculation is not.

## Startup orientation

Before substantial work, read as much of the following as the task requires:

- `README.md`;
- `STATE.md`;
- `ROADMAP.md`;
- relevant claims and research files;
- relevant open issues and pull requests;
- the latest reports in the area;
- relevant literature maps.

Do not spend the entire session reading everything when a focused target can be
started sooner. Orientation should prevent needless duplication without
eliminating independent thought.

Record the repository commit you used.

## Discussions and issue comments

GitHub Discussions are useful for broad ideation, but some AI repository
connectors do not expose them. Do not assume that Discussion-only context is
visible to every future agent.

When a Discussion produces an actionable question, correction, or research
program, mirror it into an Issue, pull request, report, or repository file.
Issue comments may contain substantive mathematics and should be read when they
are relevant to the target.

## Avoid inaccessible context

Do not rely on private chat history as a mathematical dependency.

A durable result must be understandable from repository files, exact sources,
and reproducible artifacts.

## Circular-loop detection

Long research can iterate productively. It can also circle.

Pause for a blocker audit when several of these occur:

- the same missing inference reappears under new notation;
- another encoding preserves the same existence problem;
- finite-prefix depth increases without a theorem about infinite realization;
- a result says only “if an infinite orbit exists, it grows”;
- compactness or inverse limits produce a `2`-adic object but not an ordinary
  integer;
- proper-factor divisibility is repeatedly substituted for full-denominator
  divisibility;
- the same conditional theorem is rediscovered;
- a “breakthrough” does not strengthen the final implication;
- the pass repeats prior work without a clear delta.

A blocker audit should answer:

```text
What exact final statement are we trying to prove?
What is the first unsupported inference?
Is the target genuinely weaker than Collatz?
What exhaustive class would a negative result eliminate?
What concrete candidate would a positive result produce?
What changed relative to the previous approach?
Can the current route be refuted?
```

Do not automatically abandon the direction. Decide whether to:

- repair the missing inference;
- prove the architecture cannot supply it;
- change methods;
- extract a useful negative theorem;
- hand off the route clearly.

## Ordinary-integer warning

Many Collatz constructions naturally produce:

- compatible residue classes;
- inverse-limit points;
- `2`-adic trajectories;
- symbolic infinite paths;
- arbitrarily long finite ordinary realizations.

These do not automatically produce one ordinary positive integer realizing the
entire path.

Whenever this distinction matters, state the exact extraction obligation.

## Cycle warning

For a proposed positive cycle, approximate agreement or divisibility by a
proper factor is not enough.

State the entire denominator condition and replay the actual branches exactly.

## Literature behavior

When a relevant theorem is found:

- record the exact source;
- verify the normalization;
- distinguish theorem from analogy;
- translate its hypotheses explicitly;
- test whether it really closes the needed implication.

When literature says the target remains open:

- map the boundary;
- do not stop;
- attempt the new step.

## Computation behavior

Exploratory computation may inspire a theorem.

For proof-relevant computation, produce:

- exact code;
- exact command;
- environment;
- deterministic output or seed;
- certificate or digest;
- independent verifier when feasible;
- explicit finite scope.

Do not extrapolate a finite search into an infinite theorem.

## Large research pushes

A large push is welcome when it leaves a navigable record.

Maintain:

```text
README or program map
claim inventory
definitions
dependency graph
experiment index
failed approaches
current blocker
next attacks
session reports
```

Do not force a substantial mathematical program into a tiny pull request merely
to appear atomic.

At the same time, isolate load-bearing claims so they can be reviewed
independently.

## Verification mode

When reviewing another contribution:

1. restate the exact claim independently;
2. freeze the source commit;
3. reconstruct the proof from explicit dependencies;
4. check quantifiers, signs, boundary cases, positivity, and divisibility;
5. search for small counterexamples;
6. check ordinary versus `2`-adic realization;
7. locate the first unsupported inference;
8. distinguish source failure, proof failure, scope narrowing, and lack of
   reproduction;
9. submit a clear verdict.

Neutral non-reproduction is not refutation.

## Organizational responsibility

You may propose improvements to the repository structure and research process.

A useful research session may produce:

- mathematics;
- a refutation;
- a clearer map;
- a better verification protocol;
- a new task decomposition;
- a data or formalization interface.

Leave the repository more understandable than you found it.

## End-of-session record

For a substantial session, record:

```text
Agent:
Starting commit:
Research question:
Approaches attempted:
New results:
Proof status:
Computational status:
Literature connections:
Failed approaches:
Potential errors:
Claims affected:
Files changed:
Current blocker:
Suggested next attacks:
Organizational suggestions:
```

The final report should distinguish clearly among:

- proved in the report;
- proposed;
- computationally observed;
- conditional;
- speculative;
- refuted;
- source-dependent.
