# Agent entrypoint

This is an **unsolved** research repository. Produce durable, correctly scoped progress; do not make the project look solved.

## Start with the science

Read [README.md](README.md), the [research map](docs/RESEARCH_MAP.md), and the relevant [resident packet](research/integrated/README.md) or [reviewed source family](research/RESULTS_CATALOG.md). Then inspect the current source issue/PR and freeze its head. Read [scoped errata](research/integrated/ERRATA.md) before reusing a corrected statement. Contributor access and peer review are explained in [CONTRIBUTING.md](CONTRIBUTING.md) and [shared review](docs/REVIEWING.md).

## Choose a mode

**Explore.** Free-form proofs, constructions, experiments, countermodels and literature connections belong in `research/`, `experiments/`, `literature/` or `reports/`. State the map, normalization, claim status, exact dependencies, evidence level and first unsupported step. Use PROPOSED, EMPIRICAL, SOURCE-QUALIFIED, REFUTED or OPEN appropriately. No registry form is required before exploration.

**Review.** Freeze the full SHA and identify each source by `(PR, full SHA, path, claim ID)`: a single PR can reuse the same ID in different files. Reconstruct hypotheses, algebra, quantifiers, normalizations, ordinary realization, dependencies and computation coverage. Report VERIFIED, VERIFIED WITH FIXES, GAP/BLOCKED or REJECTED at the narrow claim level. Verdicts do not extend to later heads or neighboring statements. Independence means checking the argument, not merely agreeing with another agent.

**Integrate.** Prefer a readable proof packet or qualified reference assembly to a long branch-history import. Keep statement, proof, scope, dependencies, source/review pins, failed strengthenings and the next missing lemma close together. A false original remains preserved; a repair has its own identity and review boundary. Follow [integration practice](docs/INTEGRATION_PRACTICE.md). Frozen A/B assignments and D's separate follow-up are historical evidence, not a mutable global reviewer list.

## Mathematical safeguards

Ask whether a claim concerns one fixed positive ordinary integer or changing finite witnesses; an ordinary value or merely a 2-adic completion; exact finite legality or all-time legality; a complete cycle denominator or only its factors. Keep ordinary orbits separate from their predecessor basins and finite counts separate from all-depth conclusions.

Transfer arguments must state the map, source/endpoint projections, killed states, function space and input domain. Fresh-shell contraction does not automatically survive transport. Ranks and clocks from different programs are not interchangeable, and a total guard returning UNRESOLVED is not a total successful selector. Preserve failed strengthening counterexamples rather than averaging them away.

## Productive next steps

Choose a precise [open obligation](research/open-obligations/README.md): fixed-floor survivor mass, actual unsafe-return control, complete lower-rank merging, coefficient stopping, full-denominator exclusion, or an ordinary least-root decision. All original SC*/FC*, periodic-synthesis and bridge boundaries remain explicit. An alternative architecture is welcome when its status and missing inference are clear.

## Validate and publish

In a clean complete checkout, run `python -X utf8 -B tools/validate.py`; add `--regressions` for the bounded replay bundle. [Replay policy](docs/REPLAY_POLICY.md) explains evidence tiers, Windows mode handling and exact receipts. A fixture, a source inspection, an API tree read and a complete execution are different events. Never invent command output or claim that repository integrity proves mathematics.

Work on a branch; do not rewrite history, directly push to `main`, close another contributor's PR, or change settings, membership, visibility, licensing or workflows without explicit authority. The read-only integrity workflow is a separately authorized infrastructure addition, not permission to add privileged research automation. Do not run expensive searches merely for integration activity.

Finish with a real commit/PR, exact head, affected files, checks actually run, strongest uncertainty and useful handoff. Re-query the remote before saying a write landed. Keep process receipts in [the archive](archive/README.md) and reports, not in a competing scientific front door.
