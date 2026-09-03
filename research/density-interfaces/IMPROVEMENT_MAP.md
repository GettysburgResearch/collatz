# Improvement map — the two Mazur 2026 results and their place on the road to a full solution

> Strategy document, not a proof. **Collatz remains unsolved.** Every item is labeled by what it would prove and by whether any current method reaches it.

## 0. Reading guide

- Section 1 restates both results in repository terms.
- Section 2 says why neither result, however strengthened, becomes a proof of Collatz by itself.
- Sections 3–4 list concrete strengthenings inside each paper, ranked by value and feasibility.
- Section 5 lists the interfaces into the repository's programs (the `DI` claims).
- Section 6 is the ledger of what a full solution would still need.
- Section 7 is a prioritized work plan.

Throughout, `T` is the shortcut map, `α = log 2/log 3`, `D_k = q_k − αk` is the surplus, Lane A is `D_k ≥ 0` for all `k ≥ 1`, and `B_{N_0} = {N : T^j(N) > N_0 ∀j}` is the fixed-target bad set. The density paper's `α = 1001/1000` and the predecessor paper's `α = log_2 3` are never used under that letter here.

## 1. What the two results say, in repository terms

| Result | Statement (translated to `T`) | Nature | Evidence state |
|---|---|---|---|
| Density, Theorem 1.1 | for every `f→∞` a natural-density-one set of `N` has an iterate `< f(N)` within `436 log N` raw steps (`145 log N` Syracuse steps for odd inputs) | almost-everywhere, uniform clock `∃C ∀f` | external Lean, not replayed |
| Density, Theorem 1.2 | `#(B_{N_0} ∩ [1,x]) ≤ 2C_d x (log N_0)^{-d}` for every `N_0 ≥ 3`, all `x>0`, each `d<5/143` (fiber-summed form, `T-DI-002`) | averaged, fixed target, ineffective `C_d` | external Lean, not replayed |
| Density, Corollary 1.3 | any raw witness below `√N` needs more than `log N/(2 log 2)` steps; the log-time budget is order-sharp | deterministic | elementary, replayed |
| Predecessor, Theorem 1.1 | `π_a(x) ≥ x^{9/10}` eventually for every `a` with `3∤a` | inverse-tree lower bound | external Lean + two `native_decide` certificates, not replayed |

Neither statement constrains one fixed positive integer. The repository's resident firewall (`IC-EXTRACT-001`, `IC-GHOST-001`) already explains why: finite-prefix or averaged information does not extract an ordinary all-depth witness, and a positive-density exceptional set is not needed for a counterexample to exist.

## 2. Why neither result extends by itself to a full solution

1. **Exceptional sets.** A density-one theorem tolerates an infinite exceptional set. A least counterexample `n_*` and its basin `M(n_*)` would be such a set; `T-DI-003` shows the basin is even forced to have at least `x^{9/10}` elements below `x`, and nothing in either paper contradicts that.
2. **Fixed source versus averaged source.** `SC*` and `FC*` are statements about one fixed `n` (Lane A) or one fixed first-crossing word. Averaging over sources loses exactly the information those obligations need. `T-DI-002` shows the *only* part of Lane A an averaged fixed-target theorem can see: the bounded-surplus sub-lane, and only when the density bound is effective.
3. **Lower bounds on the good set never reach density one.** The Krasikov–Lagarias program is a linear relaxation of inverse-tree counting whose optimum is at most `x^{1−ε}`; even its conjectured limit `λ_k → 2` gives `x^{1−ε}`, not `cx`, and never `x − o(x)`.
4. **Both are 2-adic/3-adic averaging methods.** The density paper equidistributes phases along an irrational rotation; the predecessor paper takes minima over 3-adic residue classes. The repository's `RD-SC-001` needs a valuation bound for one source, and `RD-FC-001` needs a complete-denominator obstruction for every word. Neither is an averaging statement.

Consequently the honest role of these papers is: (a) two exact sub-lane/basin interfaces (Section 5), (b) two first-rank strengthening targets that are open problems in their own right (`T1.5`, `T2.4`), and (c) a formalization standard the repository can adopt.

## 3. Targets inside the natural-density paper

### T1.1 — Raise the exponent `d`

- **Now:** `d < 1/(2κ) = 5/143 ≈ 0.035`, `κ = 14.3` from Rhin's `13.3` linear-form bound.
- **Route (a):** any effective irrationality measure with `κ < 10` for `log_2 3` (equivalently for `|q log 3 − p log 2|`) moves the cap to the next guard `d < 1/20`. Rhin's own sharper `7.616` line has an unprinted effective threshold; the Lean development already reconstructs Rhin's Padé argument, so a certified finite handoff for the sharper line is a formalization task rather than new mathematics. Gain: `0.035 → 0.05`.
- **Route (b):** the halving `1/(2κ)` is the `√(n_0 log n_0)` valuation tube. Removing it needs discrepancy control over the full `n_0 ≍ log B` horizon; unclear.
- **Route (c):** beyond `1/20` the terminal-approximation exponents (`1/20, 3/10, 9/5, 6, 6/5`) bind and Tao's Section 5 estimates must be reworked.
- **Ceiling:** even `κ = 2+ε` (true for almost every real, unproved for `log_2 3`) gives only `d < 1/4` on the phase line. The `(log N_0)^{-d}` form is intrinsic to this architecture; power saving is `T1.4`.
- **Value:** modest for the repository; `T-DI-002`'s clause scales linearly in `d`.

### T1.2 — Make the constants effective

- **Now:** `x_0`, `C_d`, `N_*`, `C_trace` are existential. Named sources of ineffectivity: the Rhin constant `c` (the formal proof establishes only an eventual large-height bound; Rhin's printed `H ≥ 2` statement would give `c = 2^{-13.3}/log 2` directly); `m_0(B) = ⌊log B/100000⌋`, vacuous below `B = e^{100000}`; "sufficiently large `B`" in the common-profile lemmas; the finite-prefix absorption.
- **Deliverable:** explicit `C_d` and `x_0`. Expect astronomically large constants unless the schedule and tube parameters are re-optimized.
- **Value:** this is the ingredient that turns `T-DI-002`(v) into a usable pointwise bound and is a prerequisite for `T1.5`. Without it every quantitative consequence stays symbolic.

### T1.3 — Tighten the clocks to the intrinsic rate

- **Now:** `C_Syr = (1001/1000)·1002/(10 log 2) ≈ 144.7`, `C_Coll = 3C_Syr + 1/log 2 ≈ 435.6`. Structure: per-scale schedule `n_0(B) = log B/(10 log 2) ≈ 0.144 log B`, summed geometrically over scales (`α/(α−1) = 1001`).
- **Intrinsic rate:** from `B^α` down to `B` the typical Syracuse passage takes `(α−1) log B / log(4/3) ≈ 0.0035 log B` steps, because one Syracuse step multiplies by `3/2^ν` with `E[ν] = 2` and `E[log(3/2^ν)] = log(3/4)`. The schedule is therefore about `41×` the typical time; summed over scales the intrinsic uniform clock is `1/log(4/3) ≈ 3.48` Syracuse steps per `log N`, exactly Inselmann's horizon, and `3/log(4/3) + 1/log 2 ≈ 11.9` raw steps per `log N` with the paper's exact telescope `W ≤ 2k + log_2 M` (`≈ 10.4` with a probabilistic `W ≈ 2k`).
- **Mechanism:** replace Tao's generous schedule by a `(1+ε)`-tight schedule with a Chernoff bound on the valuation sums; the scheduled no-hit error only needs to be *some* power of `x`, since it is absorbed into `(log x)^{-d}`. Check that the tube width `W = C√(n_0 log n_0)`, the interior/exterior split, and the reference depth tolerate the shorter horizon (they scale with `n_0 ≍ log B` either way).
- **Sharpness:** a uniform clock below `1/log(4/3)` fails on a density-one set for `f(N) = √N` by the law of large numbers for valuations, so `3.48(1+ε)` is the right target.
- **Value:** constant-factor, but it closes a `40×` gap and matches the fixed-power literature while keeping `∀f`. Low mathematical risk; substantial bookkeeping.

### T1.4 — Power-saving fixed-target rate

- **Target:** `#(B_{N_0} ∩ [1,x]) ≤ C x N_0^{-c}`.
- **Obstacle:** the phase-discrepancy technique lives at logarithmic scale (the tube is `√(log B)` long). Tao's Remark 1.16 names fine-scale mixing of the entire random affine map as the missing input.
- **Consequences if achieved:** `T-DI-002`(v) becomes `sup_k D_k ≥ c log_3(n−1) − O(1)`: every Lane-A orbit must climb above `n^{1+c}/O(1)`; and `T1.5` becomes approachable.
- **Value:** high; difficulty: research-level, no current route.

### T1.5 — Flagship: positive density for the basin of `1`

- **Statement to prove:** explicit `N_0` inside the computationally verified range (Barina's `2^68`; issue #78 cites a `2^71` verification) and explicit `ε < 1/2` with `#{N odd ≤ x : orbit never ≤ N_0} ≤ εx` for all large `x`. Then `π_1(x) ≥ (1/2 − ε)x − o(x)`.
- **Why it is the meeting point of both papers:** it is the fixed-target theorem at one bounded target with an explicit constant, and it would supersede `x^{9/10}` by the first positive-density bound for `Pred(1)`, which is open.
- **Distance:** at `N_0 = 2^{68}`, `d = 0.035`, `(log N_0)^{-d} ≈ 0.87`, so the architecture would need `C_d < 0.57`: essentially loss-free transport, far from the present `384256`-type ledgers. With a power-saving rate `C N_0^{-c}` one needs `c > log(2C)/(68 log 2)`, e.g. `c > 0.16` at `C = 10^3`.
- **Value:** first rank. Not reachable by constant-chasing in the present architecture; needs `T1.4` or a new effective descent argument.

## 4. Targets inside the predecessor paper

### T2.1 — Optimize the exponent at level 18

Bisection on `γ` with the same integer power iteration and the same exact checker; each candidate costs one `129,140,163`-row check and a `0.5 GB` payload. No infeasibility is known at level 18, so the headroom above `0.901` is unknown; expect at most a few thousandths.

### T2.2 — Level 21

`3^{20} = 3,486,784,401` principal rows; `14 GB` of `uint32` weights, `3.5 GB` of potential bytes. The level-15 fixed fallback failed at level 18; the adaptive least-potential fallback may in turn fail at level 21 and need a new rule. Expected gain `+0.01` to `+0.02`, judging by `.84 → .88 → .90` across levels `11 → 15 → 18`. Expensive; only worth it after `T2.3` indicates the trend.

### T2.3 — Chart the exact optimum `γ_k` at small levels

For `k ≤ 10` the program has at most `3^9 = 19683` rows and can be solved exactly (rational bisection on `λ` with exact feasibility on one side and a Farkas/dual infeasibility certificate on the other). Deliverable: certified two-sided bounds on `γ_k^{opt}` for `k = 2,…,10`, the increments, and an extrapolation. This is the cheapest experiment that says whether `λ_k → 2` is plausible and how fast. Also verify directly the elementary monotonicity: a level-`k` feasible vector lifted as a fiber-constant vector is level-`(k+1)` feasible (the auxiliary minimum over three lifts is at most any single lift), so `λ_k` is nondecreasing in `k`.

### T2.4 — Flagship: `λ_k → 2` as a nonlinear Perron–Frobenius problem

The system `c ≤ Φ_λ(c)` with `Φ_λ(c)_m = λ^{-2}c_{4m} + λ^{α−2} min_ℓ c_{(4m−2)/3 + ℓ 3^{k−1}}` (and its `D2`/`D3` variants) is monotone, concave, and positively homogeneous in `c`, and decreasing in `λ`. The optimal `λ_k` is a nonlinear spectral radius (Collatz–Wielandt type). The branch maps `x ↦ 4x`, `x ↦ (4x−2)/3`, `x ↦ (2x−1)/3` act on the 3-adic integers, so the level-`k` programs are finite quotients of one operator on functions on `Z_3`. Target: identify the limiting operator, prove `λ_k ↑ λ_∞`, and decide `λ_∞ = 2`. A proof would give `π_a(x) ≥ x^{1−ε}` for every `ε`, the paper's own stated limiting question, and would replace finite certificates by a theorem.

### T2.5 — A uniform potential

The adaptive potential `P_k` is level-specific data. Find a closed-form family (a 3-adic rank function of the residue) satisfying `P(F(i)) ≤ P(i)+6`, `P(D_1) ≤ P(i)+1`, `P(D_3)+2 ≤ P(i)` uniformly in `k`, or prove termination of the advanced-term expansion on the infinite tree directly. Either removes one of the two `native_decide` certificates.

### T2.6 — Effective thresholds

Materialize the finite normal forms to obtain `ν`, hence `Δ`, `C_a`, and `x_0(a)`. Changes nothing in the exponent; makes `π_a(x) ≥ x^{9/10}` checkable at concrete `x`.

### T2.7 — Beyond the linear program

Wirsching's conjecture `π_a(x) ≥ c_a x` is not a linear-programming statement: the program takes worst-case minima over residue classes and its optimum is at most `x^{1−ε}`. Positive density for `a = 1` is `T1.5`; for general `a` no route is visible.

## 5. Interfaces into the repository

- **I1 — bounded-surplus sub-lane of `SC*`** (`L-DI-001`, `T-DI-002`). Exact threshold: a Lane-A source `n` with surplus `≤ H` forces `d_(B_{n−1}) ≥ 2·3^{-H}`. Effective fixed-target bounds empty the sub-lane; the present ineffective bound gives only `sup_k D_k ≥ d log_3 log(n−1) − log_3 C_d`. The unbounded-surplus sub-lane is untouched and is the generic case.
- **I2 — basin squeeze** (`T-DI-003`). `x^{9/10} ≤ #(M(n_*) ∩ [1,x]) ≤ 2C_d x(log(n_*−1))^{-d}`. A constraint; closing it would need positive density for `Pred(a)` with a constant decaying slower than `(log a)^{-d}`.
- **I3 — the same Diophantine input as the cycle literature.** Rhin's `13.3` bound is the input of the Simons–de Weger `m`-cycle exclusions (later extended by others). Those results exclude cycle words with a bounded number of runs, which is an `FC*` subfamily in the repository's language. Recommended: import them as source-pinned literature for Program 2 with their exact normalization, then ask whether the repository's complete-denominator and support machinery can express the run-count restriction and whether it can be relaxed.
- **I4 — 3-adic duality.** The Krasikov–Lagarias level-`k` residues are the inverse-tree counterpart of depth-`k` parity cylinders. The repository's Program 4 objects `2^j − 3^q` live on both sides at once; the linear program sees only the 3-adic side. No theorem is proposed; the observation orients `T2.4`.
- **I5 — formalization standard.** Both papers freeze a commit, print the axiom footprint, and separate native computation from deduction. Pilot: formalize `IC-SC-001` (Theorems A and B), `L-DI-001`, and `T-DI-002`(i)–(iv) in Lean, reusing the published `Terras.accelerated` definition; they are short and elementary, and a checked spine would raise the repository's evidence standard from "independently reconstructed" to "machine-checked".

## 6. Ledger: what a full solution would still need

```text
Collatz                         ⇐  SC* ∧ FC*                        RD-BRIDGE-001: PROPOSED, pending narrow review
SC*                             ⇔  m_N → ∞                           IC-SC-001: VERIFIED
SC*                             ⇐  no bounded-surplus Lane-A source
                                   ∧ no unbounded-surplus Lane-A source   L-DI-001 split: PROPOSED (elementary)
no Lane-A source n, surplus ≤ H ⇐  d̄(B_{n−1}) < 2·3^{-H}             T-DI-002: PROPOSED
d̄(B_{N_0}) ≤ 2C_d (log N_0)^{-d}                                    external, Lean-checked, ineffective; not replayed
no unbounded-surplus Lane-A source                                   OPEN; needs a pointwise valuation bound; no averaged route
FC*                                                                  OPEN; bounded-run cycle subfamilies excluded in the literature, not imported
basin of n_*: x^{9/10} ≤ #M(x) ≤ 2C_d x (log n_*)^{-d}              T-DI-003: constraint only
```

Verdict: there is no route from these two papers to a full solution, and strengthening them along Sections 3–4 does not create one. What they add to the repository is one exact sub-lane interface, one two-sided constraint on any counterexample, two open first-rank targets (`T1.5`, `T2.4`) that are genuine strengthenings of the papers, and a verification standard. The residual core is unchanged: a fixed-source valuation bound for `SC*` and a complete all-word denominator obstruction for `FC*`.

## 7. Prioritized work plan

| Priority | Item | Cost | Risk | Deliverable |
|---|---|---|---|---|
| P0 | narrow review of `L-DI-001`, `T-DI-002`, `T-DI-003` | hours | low | verdicts; promotion or repair |
| P1 | `T2.3` exact `γ_k` chart, `k ≤ 10`, with dual certificates; check `λ_k` monotone | one day | low | table, extrapolation, decision on `T2.2` |
| P2 | `T1.3` clock tightening on paper: `(1+ε)`-tight schedule, Chernoff no-hit bound, dependency check through the tube/reference parameters | days | low–medium | `C_Syr ≈ 3.5(1+ε)`, `C_Coll ≈ 12(1+ε)` |
| P3 | effectivity audit (`T1.2`): list every existential threshold with its source and order of magnitude; decide whether `T1.5` is reachable in this architecture | days | low | obstruction note or explicit constants |
| P4 | `I3`: import the `m`-cycle literature as source-pinned Program 2 references with exact normalization | one day | low | literature packet |
| P5 | `T2.1`/`T2.2` computations | weeks, large storage | medium (fallback may fail) | improved exponent or a documented failure of the adaptive rule |
| P6 | `I5` Lean pilot for `IC-SC-001` and the `DI` claims | weeks | low | machine-checked spine |
| P7 | `T2.4`, `T1.4`, `T1.5` | open-ended | research | theorems, if any |

## 8. Evidence discipline for this program

- External theorems are cited with their frozen commits and are marked "not replayed" until someone in this repository builds and checks them.
- A density, almost-all, or lower-bound statement is never used as evidence for or against `SC*`, `FC*`, or a specific orbit, except through an explicit interface claim with its own status.
- Constants matter: an ineffective bound yields a symbolic consequence only; say so every time.
- Experiments (`X-DI-001`) are bounded evidence; exact computations are labeled exact; neither is an all-depth theorem.
