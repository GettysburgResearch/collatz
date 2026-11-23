# Published-checkout validation: whole-repository continuation

## Exact source boundary

The scientific checkpoint is commit
`2055b8a311ab87d07bffc730154a7f8546fe382c`, tree
`385f2eb5f0ee150da08eb3ba6126b512ad8a52e7`, on PR175's branch
`research/lean-global-closure-20261121`.

Both executions below used a fresh **complete Git clone of that published
commit**, with 403 tracked files and a clean working tree. The build output
was outside the checkout and initially empty. The working tree was still
clean after both executions. The subsequent evidence commit adds records
and documentation; it does not change the checked Lean sources, build driver,
or frozen dependency manifest.

## Fresh Lean execution — PASSED

[The exact source-build receipt](source-build.json) records the commands,
source hashes, generated-object hashes, exit codes, and full axiom output.
All **16 source units** were compiled from source using:

```sh
python -B research/lean-global-closure-20261121/build_wide.py \
  --lean /tmp/collatz-lean-runtime/lean-4.34.1-linux/bin/lean \
  --output /workspace/scratch/957bb0caa6f2/wide-build-published \
  --receipt /workspace/scratch/957bb0caa6f2/wide-research-evidence/published-build.json
```

Compiler: Lean **4.34.1**, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, x86_64 Linux Release.
Every compilation used `-j1`, `-DwarningAsError=true`, and
`-DautoImplicit=false`. `LEAN_PATH` contained only the fresh output directory.
This packet uses core Lean and requires no Mathlib object files.

The execution covered eight byte-for-byte PR177 dependency sources,
`EndpointSteering`, `InverseBudget`, `ReservedMergerCompleteness`,
`MaximalReserve`, `AsynchronousReset`, `TerminalReset`, `PeriodicTraceTail`,
and the `CollatzGlobalClosureCore` entry point. The driver checked both
SHA256 and Git blob identities for the eight frozen upstream sources.

All 16 compiler exit codes were zero. There were **71 axiom reports**:
69 list dependencies and two explicitly report no axioms. Their combined
dependency set is exactly `Classical.choice`, `Quot.sound`, and `propext`.
No Collatz assumption or `sorryAx` occurs in those reports.
Total recorded compiler time was **30.882 seconds**.

Receipt SHA256:
`40cb4242946fba3805879d763991dd910513d3dd25ea08c5d0e9b7bfd1795cb7`.

## Complete repository gate — PASSED

[The exact repository receipt](repository.json) records a clean complete
checkout at the scientific commit before and after execution. On
2026-11-21 at 22:32 UTC, the command

```sh
python -X utf8 -B tools/validate.py \
  --receipt /workspace/scratch/957bb0caa6f2/wide-research-evidence/scientific-repository.json
```

ran all five required commands successfully: integration structure,
reviewed assembly pins, the review validator self-test, real-Git
portability controls, and the scoped integration-D follow-up self-test.
The optional bounded regression bundle was not requested. These are
repository-integrity checks, not mathematical proof checks.

Receipt SHA256:
`30441e4ae9c4d49dfc063a7d3d7106ebbd0d967b47595c6365a46ff9d8da4d6d`.

## Scope and retained earlier evidence

The terminal-source theorem closes the complete power-of-two **recursive
case** under the supplied smaller-certificate induction hypothesis. It is
not an unconditional convergence theorem for all Mersenne numbers. The
nonterminal comparison dispatcher remains open.

The pressure module proves finite rational weighted bounds. Substituting
the source-pinned PR144 inverse population and passing to an infinite sum
is a separate written deduction; it is not disguised as a Lean theorem or
axiom. The moving exhausted-quotient core still needs an upper bound.

The earlier 17-unit band/legacy build has its own
[exact historical execution record](../band/VALIDATION.md). It was not
repeated here. The expanded 32-unit `build_band.py --full` aggregation was
not executed in this pass; the new 16-unit core packet above was executed
in full. All prior scientific boundaries remain explicit.

The evidence child receives its own clean complete repository-gate run,
with its exact final head and receipt reported on PR175. The checked source
hashes are compared to this receipt rather than rerunning unchanged proofs
merely to add a self-referential receipt commit.
