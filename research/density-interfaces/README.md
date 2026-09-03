# Density interfaces — what averaged theorems can and cannot say about `SC*`, `FC*`, and a least counterexample

> **Collatz remains unsolved.** This directory is exploratory research in the sense of [`AGENTS.md`](../../AGENTS.md): every claim here is `PROPOSED` until independently reviewed; every external input keeps its own evidence state.

## Purpose

Two 2026 preprints by Mazur, each with a Lean formalization at a frozen commit, were imported as literature packets:

- [natural-density almost-bounded orbits in logarithmic time](../../literature/mazur-2026-natural-density-log-time/README.md) — for every `f→∞`, a natural-density-one set has `Col^m(N)<f(N)` with `m ≤ 436 log N`; quantitatively, the fixed-target bad set has natural density `≤ C_d (log N_0)^{-d}` for `d<5/143`;
- [certified `x^{9/10}` predecessor-set lower bounds](../../literature/mazur-2026-predecessor-x090/README.md) — `π_a(x) ≥ x^{9/10}` eventually for every `a` with `3∤a`.

Both are *averaged* or *inverse-tree* statements. The repository's central firewall says such statements never decide a question about one fixed positive integer. This directory makes the boundary exact: it states precisely which sub-lanes of the repository's roadmap an averaged theorem can touch, with the exact inequality that would have to be beaten, and it records the improvement map for both papers.

## Contents

| Item | Kind | Status | One-line content |
|---|---|---|---|
| [`claims/L-DI-001`](claims/L-DI-001-lane-A-running-max-growth.md) | lemma | `PROPOSED` (elementary, proof complete) | a Lane-A orbit satisfies `n ≤ T^k(n) ≤ 3^{M_k}(n+k/2)`; bounded surplus `≤H` forces at most linear growth and `≥ 2·3^{-H}x − 2n` distinct values below `x` |
| [`claims/T-DI-002`](claims/T-DI-002-bounded-surplus-density-interface.md) | theorem | `PROPOSED` (parts conditional on external Lean-checked input) | a Lane-A source with surplus `≤H` forces lower density `≥ 2·3^{-H}` in the fixed-target bad set `B_{n−1}`; any fixed-target density bound below `2·3^{-H}` empties that sub-lane; Mazur's bound gives `sup_k D_k ≥ d log_3 log(n−1) − log_3 C_d` |
| [`claims/T-DI-003`](claims/T-DI-003-counterexample-basin-squeeze.md) | theorem | `PROPOSED` (parts conditional on external input) | the basin of a least counterexample satisfies `x^{9/10} ≤ #M(x) ≤ 2C_d x(log(n_*−1))^{-d}`; a constraint, not a contradiction |
| [`experiments/X-DI-001`](experiments/X-DI-001-coefficient-stopping-records/README.md) | exact computation + bounded scan | `EMPIRICAL` / exact where stated | exact natural density of `S_N` (`N ≤ 400`) and the coefficient-stopping record holders `m_N` for `n ≤ 10^{10}` with their peak surplus |
| [`IMPROVEMENT_MAP.md`](IMPROVEMENT_MAP.md) | roadmap | strategy, not a proof | ranked strengthenings of each paper, structural targets, the interfaces into `SC*`/`FC*`, and an honest ledger of what a full solution would still need |

## Notation bridge

| Object | Repository | Mazur (density) | Mazur (predecessor) |
|---|---|---|---|
| map | shortcut `T` | raw `Col`, Syracuse `Syr` | shortcut `T` (`accelerated`) |
| `α` | `log 2/log 3 ≈ 0.6309` | `1001/1000` (block exponent) | `log_2 3 ≈ 1.585` |
| surplus / coefficient | `D_k = q_k − αk`, `C_k = 3^{D_k}` | — | — |
| Lane A | `D_k ≥ 0` for all `k ≥ 1` | — | — |
| fixed-target bad set | `B_{N_0} = {N : T^j(N) > N_0 ∀j}` | timed Syracuse bad set at target `N_0` | — |
| predecessor count | `π_a(x)` | — | `π_a(x)`, `π*_a(x)` |

## The exact boundary, in one paragraph

Lane A of `RD-SC-001` splits into a bounded-surplus sub-lane and an unbounded-surplus sub-lane (`L-DI-001`). A bounded-surplus orbit grows at most linearly, so it occupies positive lower natural density inside the fixed-target bad set of its own source; therefore any fixed-target density theorem whose bound beats `2·3^{-H}` empties the surplus-`≤H` sub-lane for that source (`T-DI-002`). The unbounded-surplus sub-lane, which is the generic case, is invisible to every averaged theorem. Separately, the basin of a least counterexample is pinned between the inverse-tree lower bound and the fixed-target upper bound (`T-DI-003`), and the two do not meet. Nothing here moves `SC*`, `FC*`, or `RD-BRIDGE-001` from `OPEN`/`PROPOSED`.

## Relation to open issues

- Issue #78 (both coefficient-stopping lanes of a least counterexample) lists Tao/Inselmann almost-all results as usable "only if their quantitative exceptional-set bounds can be coupled to an actual least-counterexample inverse tree". `T-DI-002` and `T-DI-003` are that coupling.
- Issue #25 (rooted Krasikov–Lagarias forests): its unconditional half is already the all-target Krasikov–Lagarias/Mazur theorem; the exponent is now `9/10`.

## What remains missing

1. Narrow independent review of `L-DI-001`, `T-DI-002`, `T-DI-003` (all elementary modulo the external theorems).
2. An **effective** fixed-target density bound; without it the quantitative clause of `T-DI-002` is not usable at any concrete source.
3. Any pointwise mechanism for the unbounded-surplus sub-lane; this is the actual `SC*` obligation and no averaged method reaches it.

## Replay

```bash
python3 literature/mazur-2026-checks/replay_paper_numerics.py
python3 research/density-interfaces/experiments/X-DI-001-coefficient-stopping-records/exact_density.py 400
gcc -O2 -o records research/density-interfaces/experiments/X-DI-001-coefficient-stopping-records/records.c -lm && ./records 1000000
```
