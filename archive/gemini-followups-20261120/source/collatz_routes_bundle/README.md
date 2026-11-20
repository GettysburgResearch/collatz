# Multi-Route Proof Proposals & Verification Bundle for `GettysburgResearch/collatz`

- **Target Repository:** [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz)
- **Baseline Audited:** [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md), [PR #101](https://github.com/GettysburgResearch/collatz/pull/101), and Open Draft PRs [#145](https://github.com/GettysburgResearch/collatz/pull/145), [#146](https://github.com/GettysburgResearch/collatz/pull/146), [#147](https://github.com/GettysburgResearch/collatz/pull/147), [#148](https://github.com/GettysburgResearch/collatz/pull/148), and [#149](https://github.com/GettysburgResearch/collatz/pull/149) (as of November 20, 2026).
- **Scientific Status:** `PROPOSED` / `VERIFIED_COMPUTATIONAL` / `OPEN_OBLIGATION` (per repo `Explore -> Review -> Integrate -> Consolidate` conventions). **No full proof of the Collatz conjecture is claimed here**; instead, this bundle provides concrete, falsifiable completion blueprints, barrier audits, runnable Python certifiers, and Lean 4 skeletons directly targeting the exact bottlenecks in PRs #145–#149.

## Executive Summary of Bottlenecks & Routes

| Route | Target PRs / Repo Hooks | Core Bottleneck Diagnosed | Proposed Mathematical Attack | Included Runnable / Formal Assets |
| :--- | :--- | :--- | :--- | :--- |
| **Route 1** | [PR #146](https://github.com/GettysburgResearch/collatz/pull/146) (`D(X) >= c X^0.84`), [PR #145](https://github.com/GettysburgResearch/collatz/pull/145) (`(2n, 2n+1)` criterion) | Pure finite-depth $2$-adic algebraic coalescence has survivor box-dimension $\approx 0.972 > 0.84$, so it cannot contradict PR #146 alone. | Combine **asynchronous Syracuse 2-orbit Markov coupling** (Tao-style $3$-adic mixing on ratio/difference cocycles) with **minimality-based residue sieving** for $x_{\min}$. | `route1_tripling_and_sibling_mergers/algebraic_coalescence_sieve.py`, `lean4_x_min_exclusions_skeleton.lean` |
| **Route 2** | [PR #147](https://github.com/GettysburgResearch/collatz/pull/147) (`13/6` & conditional `39/20`), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (`25/12` compiler) | PR #147's $39/20$ slope relies on an unproved **unique-stationarity hypothesis** at cap $R \ge 6$; PR #148's $25/12$ policy is a $1.87\text{ MB}$ table. | Replace stationarity with **deterministic Bellman–Isaacs minimax potential certificates** $h(z)$ on $(\mathbb{Z}/3^P\mathbb{Z})^\times$ (plus credit cap $R$) and **Birkhoff–Hopf cone contraction** for unique ergodicity. | `route2_inverse_compiler_and_bellman/bellman_potential_certifier.py` |
| **Route 3** | [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) (rational-cycle barrier & $W(1)<\infty$), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) (`CUBE-4`) | PR #149's positive noninteger rational cycles satisfy all local $2$-adic/$3$-adic + floor constraints; `CUBE-4` finiteness is ineffective (Subspace Theorem). | Inject **global integrality at primes $p \ge 5 \mid (2^K - 3^L)$** via the adelic product formula; make `CUBE-4` effective via **LMN/Matveev + Bugeaud–Laurent $p$-adic linear forms + Baker–Davenport reduction**. | `route3_global_integrality_and_cube4/rational_barrier_and_diophantine.py` |
| **Route 4** | [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md) (horizon `#N(X)` & entropy $h_2$), [PR #145](https://github.com/GettysburgResearch/collatz/pull/145) (depth-30 winding) | Naive $L^2(\mathbb{Z}_2)$ transfer operators forget archimedean growth; $C(\mathbb{Z}_2)$ has essential spectral radius $1$ (admitting ghost eigenfunctions like $-19/11$). | Construct **Esscher-tilted anisotropic / adelic Banach spaces** $\mathcal{B}_{\alpha,\beta}$ penalizing prime denominators $p \ge 5$ to isolate $\{1,2\}$ as the unique eigenvalue-$1$ fixed point. | `route4_adelic_spectral_operators/transfer_operator_spectrum.py` |
| **Route 5** | Repo CI, `claims/registry.json`, Lean 4 pipeline | Agents risk rediscovering local-only arguments already killed by PR #149's rational cycles or merging unverified heuristic bridges. | Four concrete, immediately actionable **PR blueprints (`PR-A`–`PR-D`)** plus an automated **Barrier Falsification Harness** to gate new lemmas against rational cycles and the $-19/11$ ghost. | `route5_agentic_pr_roadmap/PR_BLUEPRINTS.md`, `barrier_falsification_harness.py` |

## Quickstart for a Git-Connected Agent

1. Inspect `BARRIER_AUDIT.md` first so any downstream agent enforces the PR #149 rational-cycle barrier as a hard invariant.
2. Run all verification scripts (standard Python 3 + `numpy` only):
   ```bash
   python3 route1_tripling_and_sibling_mergers/algebraic_coalescence_sieve.py
   python3 route2_inverse_compiler_and_bellman/bellman_potential_certifier.py
   python3 route3_global_integrality_and_cube4/rational_barrier_and_diophantine.py
   python3 route4_adelic_spectral_operators/transfer_operator_spectrum.py
   python3 route5_agentic_pr_roadmap/barrier_falsification_harness.py
   ```
3. Compare outputs against `results/verified_computations.json`.
4. Use `route5_agentic_pr_roadmap/PR_BLUEPRINTS.md` to open scoped `PROPOSED` branches/PRs against `GettysburgResearch/collatz`.
