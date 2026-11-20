# GettysburgResearch/collatz — Multi-Route Proof Ideas & Verification Package

**Date:** 2026-11-20  
**Target Repository:** [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz)  
**Baseline Context:** Aligned with [STATE.md](https://github.com/GettysburgResearch/collatz/blob/main/STATE.md), [docs/RESEARCH_MAP.md](https://github.com/GettysburgResearch/collatz/blob/main/docs/RESEARCH_MAP.md), [research/open-obligations](https://github.com/GettysburgResearch/collatz/tree/main/research/open-obligations), and Draft PRs [#146](https://github.com/GettysburgResearch/collatz/pull/146), [#147](https://github.com/GettysburgResearch/collatz/pull/147), [#148](https://github.com/GettysburgResearch/collatz/pull/148), and [#149](https://github.com/GettysburgResearch/collatz/pull/149).

---

## Explicit Non-Claim & Evidence Separation

In strict accordance with [GettysburgResearch/collatz](https://github.com/GettysburgResearch/collatz) standards:
* **This package does NOT claim a proof of the Collatz conjecture.**
* Every document strictly separates:
  1. **Established & Verified Local Lemmas** (elementary/algebraic theorems backed by deterministic Python verifiers with negative controls in this archive),
  2. **Conditional Reductions** (exact statements showing which specific unproved obligation would close a given lane), and
  3. **Research Attack Blueprints** (concrete next steps for autonomous agents to explore, compute, formalize in Lean 4, and open scoped PRs).
* Computational replay and script validation are not full mathematical verification; any promotion into `research/integrated/` requires independent narrow review and clean-checkout `python -X utf8 -B tools/validate.py --regressions`.

---

## Package Structure & Route Map

| Route Directory | Target PRs / Issues / Obligations | Core Mathematical Contribution | Executable Verifier |
| :--- | :--- | :--- | :--- |
| `route_1_merger_families_pr146/` | [PR #146](https://github.com/GettysburgResearch/collatz/pull/146), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148) | Infinite affine-collision congruence families for $(n, 3n)$ (43 witnesses, exact Haar density $41/256$ at $m \le 10$); proof that $(t, 5t+1)$ has no pure affine identity; contraction classes for $5t+1 < t$ (density $59/128$ at $m \le 8$). | `verify_merger_families.py` |
| `route_2_inverse_compiler_sub2_pr147_148/` | [PR #147](https://github.com/GettysburgResearch/collatz/pull/147), [PR #148](https://github.com/GettysburgResearch/collatz/pull/148), [PR #149](https://github.com/GettysburgResearch/collatz/pull/149) | Max-plus / Bellman finite-credit operator $F_\alpha$ analysis; exact threshold $\alpha < 2$ vs. PR #149's $W(1) < \infty$ basin boundary; Karp min-cycle-mean & adversarial-lift Bellman solver on $(\mathbb{Z}/3^r\mathbb{Z})^\times$. | `verify_inverse_compiler.py` |
| `route_3_all_word_potential_and_lyapunov_pr149/` | [PR #149](https://github.com/GettysburgResearch/collatz/pull/149), Issue #89, Obligation #4 | Exact Cramér–Chernoff strict contraction window $\alpha \in (0, 1)$ (minimum at $\alpha_{\min} \approx 0.488077$, $\Lambda(\alpha_{\min}) \approx 0.965907$) for $V_\alpha(x)=x^\alpha$ resolving $L^1$ unsafe first-moment explosion; finite-state Markov transfer spectral radius $\rho(M_{1/2}) \approx 0.965926$ and killed $\rho(K_{1/2}) \approx 0.612372$. | `verify_lyapunov_potential.py` |
| `route_4_diophantine_sc_fc_and_powered_cycles_pr148/` | [PR #148](https://github.com/GettysburgResearch/collatz/pull/148), Issues #75, #78, Obligations #2 & #6 | Clean `SC*`/`FC*` least-counterexample dichotomy ready for narrow review; continued-fraction Farey gate for $\log_2 3$; Type-I Hermite–Padé simultaneous approximant prototype ($O(z^8)$ vanishing) beyond the period-10 ceiling. | `verify_diophantine_cycles.py` |
| `route_5_transducer_merging_and_lean4_kernel/` | Issue #121, Issue #40, [PR #146](https://github.com/GettysburgResearch/collatz/pull/146), Obligations #5 & #7 | Bounded-depth lookahead merging transducers (Haar density $959/1024$ at $m \le 10$) with lexicographic well-founded rank resolving the source-121 inverse-only obstruction ($121 \to 91$ in 2 steps); Lean 4.34.1 skeleton for `SC*`/`FC*` & $(t, 5t+1)$ collisions. | `verify_transducer_merging.py` + `lean_skeleton/ScFcCrosswalk.lean` |

---

## Quick Start

Run the master verification suite from the root of this archive:

```bash
python3 -X utf8 -B run_all_verifiers.py
```

This executes all five route verifiers (including negative controls) and writes a deterministic SHA-256 verification receipt to `verification_receipt.json`. See `AGENT_HANDOFF.md` for git branching, PR creation, and `tools/validate.py --regressions` integration instructions.
