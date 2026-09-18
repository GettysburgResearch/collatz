# Observatory roadmap: v0.2 → v1.0

Parent programme: [#118](https://github.com/GettysburgResearch/collatz/issues/118). Status: **PROPOSED engineering/research roadmap**, not implemented functionality or a promise of a mathematical breakthrough. v0.1 is the runnable bounded research desk described in [README](README.md).

## North star

Notice a feature → recover its exact support → move to a different representation → perturb or compare it → seek counterexamples → preserve a replayable observation. Adding fifty independent plots would not achieve this. Prioritize links, exact identities, explicit coverage and useful research questions.

## v0.2 — The symbolic and experimental workspace

### P0: make the first slice a robust platform

**V02-01 · Modular view and operation contracts.** Split `app.mjs` into laboratory controllers, a selection store, job client and experiment store. Publish versioned request/result/selection schemas and a small panel registration interface. Include one external-to-the-core example observable, such as low-bit run length, to demonstrate extension without rewriting the workspace. Keep user plugins trusted/local; do not execute submitted code through HTTP. A framework migration is optional, not a prerequisite.

Acceptance: all v0.1 tests still pass; two independently written panels share an exact selection; a missing optional plugin does not prevent old recipes from opening; unsupported schema versions fail visibly. Expand strict parsing and compatibility tests before promoting a stable plugin API.

**V02-02 · Workspace and experiment quality.** Add panel resizing/docking, undo/redo for commands, named local experiment storage, restoration of workspace state, multi-orbit comparison, exact event bookmarks, progress history and an experiment-diff viewer. Make replay transactional or clearly show which panel failed. Add keyboard-only navigation and screen-reader descriptions for all plotted selections.

Acceptance: a fresh session can reproduce a saved observation, including seeds, parameters, viewports and comparison populations; changing a control cannot leave stale data masquerading as the new experiment. Add actual Windows and served-browser integration receipts, including CSP, clipboard, native save/load, cancellation and mobile touch interactions.

**V02-03 · Resource management before bigger workloads.** Introduce process-isolated workers and a durable local job/artifact store only after profiling. Add resumable checkpoints and explicit partial results on cancellation/timeouts. Separate compute progress from serialization and drawing. Preserve the simple one-command launcher and zero-account local mode.

Acceptance: cancelling a deliberately heavy workload releases resources promptly; restarts recover checkpointed work; two tabs do not corrupt experiment state; quotas measure bytes/work as well as source count. Define reproducible benchmark scenarios rather than publishing a single maximum seed-size boast.

### P1: the genuinely new mathematical laboratories

**V02-04 · Faithful string-rewriting studio.** Implement one pinned mixed binary–ternary Collatz rewriting system based on the programme's Yolcu–Aaronson–Heule reference. Start with legal input encoders/decoders, complete rules, applicable occurrences, deterministic strategy traces, alternative legal choices and rule-use histograms. Add rule ablation and a small bounded derivation graph. Keep a clear distinction between one halted execution and termination of all legal derivations.

Acceptance: independent arithmetic fixtures confirm the intended map/clock correspondence; malformed words and boundary errors are rejected; edited rules receive a new system identity and lose any inherited Collatz-equivalence label. An arbitrary custom rewrite board must never claim the published equivalence. Audit upstream licensing and pin the source before reuse.

**V02-05 · Carry traces and perturbation experiments.** Replace the simple arithmetic text with bitwise addition/carry events and exact input-dependency traces. Support changing a specified seed bit, paired legal recomputation, difference spacetime, selected-event alignment and matched controls. Provide a ternary view where the representation semantics are actually defined.

Acceptance: every drawn carry corresponds to the specified arithmetic operation; comparing two alignments cannot silently change the population or prediction target. Do not call a descriptive before-the-drop alignment a prospective predictor. A full Stérin–Woods cellular-automaton adapter is a separate scoped implementation, not a label applied to an ordinary bit plot.

**V02-06 · Richer symbolic and cycle tools.** Add valuation words with an explicit odd clock, word rotation/repetition controls, compositional affine block summaries, exact numerator/denominator residues, and searchable obstruction profiles. Add bounded parity-cylinder sweeps and visible least-root jump events. Include selected positive/negative control systems through a map plugin, not by mutating the `3n+1` definition in place.

Acceptance: one compressed block's summary agrees with independent literal expansion on exhaustive small cases; whole-denominator and physical-replay checks remain decisive. Rational, signed, modular and ordinary positive cycles are visually and structurally different object types. A modular near-pass is not a probability of a cycle.

**V02-07 · Families, anomalies and physical merging.** Add residue-defined families, shared-tail DAGs, exact meeting diagrams `T^a(n)=T^b(m)`, source filters, valuations/motifs as observables, and comparisons aligned at named events. Search a bounded corpus for the smallest witness or strongest counterexample to a user-specified predicate. Record both selected and rejected examples.

Acceptance: population denominators remain visible; trajectory suffix overlap is handled before reporting held-out predictive accuracy; graph aggregation cannot fabricate a lifted path or integer cycle. A physical merge record contains both source values, both clocks and the common endpoint.

### A sensible first implementation order

Take V02-01 and the served-browser/Windows part of V02-02 first. Then develop V02-04 and V02-05 as independent panels using those contracts. Add V02-06 and V02-07 with bounded fixtures. Let measurements, not speculative infrastructure, determine when V02-03 needs process workers and persistent storage.

The v0.2 exit gate is **one complete symbolic investigation**: a selected orbit segment becomes a faithful rewrite/carry trace; a perturbation is recomputed; a motif is tested on another exact family; a counterexample is inspected; the whole experiment replays in a new session. A menu full of unfinished panels is not an exit gate.

## v0.3 — Repository-native research and falsifiable observations

Build adapters rather than reinterpreting inherited results:

- **Coefficient/first-crossing desk:** exact affine remainder versus coefficient multiplier; common displacement; proper-prefix constraints; raw versus physical descent. Treat the zero remainder before logarithms.
- **Ordinary-realization desk:** nested cylinders, least-positive roots, rational/signed examples and root-jump witnesses. A changing positive finite source never becomes one all-time source merely through visualization.
- **Rank/merging desk:** compute the particular section or moving-envelope rank, label it, show actual two-source merger diagrams and repayment failures. No theorem transfers between ranks or clocks automatically.
- **Transport desk:** compare fresh and actually transported finite populations, killed states, boundary flux and safe/unsafe returns. Keep source and endpoint counts separate.
- **Observation workbench:** an observation stores a predicate, exact supporting and falsifying witnesses, controls, population definition and experiment revision. Suggested patterns remain empirical until independently proved.

Add a faithful cellular-automaton adapter and richer compressed symbolic grammars once their local rules, boundary conditions and clocks have independent tests. Maintain an adversarial example gallery drawn from the repository's corrections, not only visually pleasing examples.

Exit gate: at least three repository-motivated studies are reproducible by another contributor and include negative controls. No new theorem status is assigned by the UI. Whether a study yields a genuinely new mathematical statement is an outcome to assess, not an acceptance criterion that encourages overclaiming.

## v0.4 — Scale that preserves meaning

Introduce out-of-core artifacts, indexed exact traces, per-observable tile pyramids, asynchronous refinement, large graph frontiers, compressed-word query plans and verified resume. Profile arithmetic, storage, serialization and rendering separately.

Every reduction must declare its losses: extrema envelopes for curves, occupancy/computed masks for digit tiles, boundary context for word motifs, and compatible witnesses for graph paths. Reserve the right to expand original data for a new question; there is no universal downsampler that preserves every undiscovered pattern.

Add a public **bounded viewer** of curated artifacts separately from local full compute. Authenticated shared workers require a production API, process/container isolation, durable queues, ownership, quotas, cancellation, cost ceilings and monitoring. Do not expose the v0.1 loopback server.

Exit gate: a published benchmark suite demonstrates responsive navigation and faithful exact refinement at specified scales. Replay/manifests survive interrupted jobs and storage migrations. A service operator can enforce hard compute and artifact limits without destroying other users' work.

## v1.0 — Stable, extensible research infrastructure

Stabilize the plugin/schema ABI, provide trusted-plugin installation and compatibility tooling, maintain regression artifacts and independent witness/certificate interfaces, and document accessibility and agent operation end to end. Ship robust local packages and a separately secured shared deployment reference.

Share suitable experiment, coordinate and workspace primitives with Riemann Observatory and later Polymath tools. Keep distinct mathematics, maps, exact kernels and proof statuses separate. Neither application should wait for a universal framework to become useful.

The v1.0 criterion is not a solved conjecture. It is a reliable instrument that repeatedly turns visual curiosity into exact, testable and shareable research.
