# Mazur 2026 — certified `x^{9/10}` lower bounds for Collatz predecessor sets

## Status

- **Kind:** external literature packet. Nothing here is a resident theorem of this repository.
- **Evidence state:** the author reports a Lean 4 formalization at frozen commit `0bb368e3b51b980ef5c3b33bb86316e3001c37ac` (Lean `4.30.0-rc2`, Mathlib `5450b53e5ddc75d46418fabb605edbf36bd0beb6`) with axiom footprint `propext`, `Classical.choice`, `Quot.sound` plus **two generated `native_decide` assertions** (the level-18 LP certificate and the adaptive potential), each also replayed by separate exact Python and C++ verifiers. **Neither the Lean build nor the 344,373,768 certificate inequalities were replayed in this repository.** The paper-exposed numerics were replayed exactly; see [Evidence](#evidence-replayed-here-and-not-replayed).
- **Collatz status:** an unconditional lower bound on inverse trees. It does not imply positive density for any predecessor set and does not constrain any single forward orbit.
- **Repository inferences:** `PROPOSED` claims only, in [`research/density-interfaces/`](../../research/density-interfaces/README.md).

## Source

Lech Mazur, *Certified `x^{0.90}` lower bounds for Collatz predecessor sets*, public version of July 17, 2026. MSC 11B83; 37P99, 68V20, 90C05.

- Local copy: [`source/Mazur_Certified_x090_Lower_Bounds_for_Collatz_Predecessor_Sets_v2.pdf`](source/Mazur_Certified_x090_Lower_Bounds_for_Collatz_Predecessor_Sets_v2.pdf), SHA-256 `cbae5d71ead733b380c3325503e46a7094fb4641244853a37dc220207d133a61`.
- Project page reported at `https://www.proofatlas.ai/collatz-predecessor-090/`; preservation manifest SHA-256 `6120dd80c95b24b30f440b4394f736db0945271082ed69ced5eddb9f0e80b459`; LP payload SHA-256 `fc96181c552398be8bbc4c0a47482a53c4ff847059bf7fd4b9be11837ca7c34c` (516,560,652 bytes); potential payload SHA-256 `778584ce7635639ab2a0c7de766f81e8f551b0a52f96ca51eb2bb128c3248f52`. Raw payloads total 645,700,815 bytes and are distributed separately from the small bundle.
- The paper carries a generative-AI disclosure: AI systems contributed substantially to discovery, derivation, formalization, computation, and exposition; the author curated and reconciled outputs and takes responsibility for the manuscript.

## Normalization

The map is exactly the repository's shortcut `T` (Lean `Erdos1135.Terras.accelerated`). Reachability permits zero steps. For a target `a`,

```text
π_a(x)  = #{ n : 1 ≤ n ≤ x, T^j(n) = a for some j ≥ 0 },
π*_a(x) = #{ n : 1 ≤ n ≤ x, T^j(n) = a for some j, and T^i(n) ≤ x for 0 ≤ i ≤ j }   (bounded-orbit count).
```

The paper's `α = log_2 3 ≈ 1.585` is the **reciprocal** of the repository's `α = log 2/log 3`; the letter clash must be resolved on every citation.

Residues are 3-adic: level `k` works modulo `3^k`; the principal residue set is `P_k = {m mod 3^k : m ≡ 2 mod 3}`, `|P_k| = 3^{k−1}`. The odd inverse branch `(2y−1)/3` exists exactly when `y ≡ 2 mod 3`; a target divisible by `3` has only the even branch and `π_a(x)=Θ(log x)`. This is the 3-adic dual of the repository's 2-adic parity cylinders: the forward map branches on `n mod 2`, the inverse map branches on `y mod 3`.

## Exact statements

**Theorem 1.1 (main).** For every positive integer `a` with `3∤a` there is `x_0(a)` with `π_a(x) ≥ x^{9/10}` for all real `x ≥ x_0(a)`.

**Theorem 1.2 (constant-factor form).** For every such `a` there are `C_a>0` and `X_a` with `π_a(x) ≥ C_a x^{901/1000}` for `x ≥ X_a`. Theorem 1.1 follows once `C_a x^{1/1000} ≥ 1`.

Published exponent chain: `.05 → .30 → 3/7 → .48 → .65 → .81 → .84` (Crandall, Sander, Krasikov, Wirsching, Applegate–Lagarias, Krasikov–Lagarias 2003 at level 11); the author's preceding level-15 certificate gave `.88`; this paper gives `.90` at level 18. The paper reports a dated search through July 15, 2026 finding no published improvement of `.84` after 2003.

**Envelopes and difference system.** For `m∈P_k`, `φ^m_k(y) = inf_{a∈A_k(m)} π*_a(2^y a)` over positive nonperiodic `a ≡ m mod 3^k`; `(P1)` `φ ≥ 1`, `(P2)` nondecreasing, `(P3)` `φ^r_{k−1}(y) = min_{0≤ℓ<3} φ^{r+ℓ3^{k−1}}_k(y)`. For `y ≥ 2`:

```text
m ≡ 2 (mod 9):  φ^m_k(y) ≥ φ^{4m}_k(y−2) + φ^{(4m−2)/3}_{k−1}(y+α−2)       (D1)
m ≡ 5 (mod 9):  φ^m_k(y) ≥ φ^{4m}_k(y−2)                                    (D2)
m ≡ 8 (mod 9):  φ^m_k(y) ≥ φ^{4m}_k(y−2) + φ^{(2m−1)/3}_{k−1}(y+α−1)        (D3)
```

The shifts are `−2`, `α−2<0`, and `α−1>0`. The `D3` term is **advanced**: it asks for an envelope value at a later time, which blocks direct induction.

**Linear program `L^NT_k(λ)`** (`1<λ<2`, positive principal weights `c_m`, `c_r=min_ℓ c_{r+ℓ3^{k−1}}` for lower-level residues):

```text
m ≡ 2:  c_m ≤ λ^{-2} c_{4m} + λ^{α−2} c_{(4m−2)/3}
m ≡ 5:  c_m ≤ λ^{-2} c_{4m}
m ≡ 8:  c_m ≤ λ^{-2} c_{4m} + λ^{α−1} c_{(2m−1)/3}
```

Level `k=18`, `γ=901/1000`, `λ=2^γ`; `3^{17}=129,140,163` principal rows, `43,046,721` of each type.

**Integer formulation.** `Q=2^{28}`, `A=76,981,049`, `B_1=207,142,911`, `B_3=386,810,365` with certified directions `A/Q ≤ λ^{-2}`, `B_1/Q ≤ λ^{α−2}`, `B_3/Q ≤ λ^{α−1}`, proved by the exact integer comparisons

```text
A^{1000} · 2^{1802}   ≤ Q^{1000},
B_1^{1000} · 2^{1802} ≤ Q^{1000} · 3^{901},
B_3^{1000} · 2^{901}  ≤ Q^{1000} · 3^{901}.
```

Rows: `Q w_i ≤ A w_{f(i)} + B_1 w_{u_1(i)}` (`i≡0 mod 3`), `Q w_i ≤ A w_{f(i)}` (`i≡1`), `Q w_i ≤ A w_{f(i)} + B_3 w_{u_3(i)}` (`i≡2`), with `w_u = min{w_u, w_{u+3^{16}}, w_{u+2·3^{16}}}`. Table 1: minimum/maximum weight `1,048,576 / 1,859,404,226`; minimum row margin `4,147,742,755` at index `18,958,255`; zero failed rows. The vector was found by integer normalized power iteration; search is not a proof input.

**Adaptive advanced-term elimination.** Expression trees over shifted leaves `(i,β)`, addition and minimum; coefficient functional `C_λ((i,β);c)=c_i λ^β`; identity `(E[(Δ c_i λ^·)_i])(y) = Δ λ^y C_λ(E;c)`. Shift codes `(p,q)` with `s(p,q)=pα−q`; edges: principal `(p,q+2)`, `D1` `(p+1,q+2)`, `D3` `(p+1,q+1)`. Only nodes with `s ≥ 0` are expanded; a fresh auxiliary lift `v` is **dominated** if an earlier node `u` on its root path has `i(u)=i(v)` and `s(u)<s(v)`; survivors are retained; when all three lifts are dominated, the fallback is the lift of least potential (ties `0,1,2`).

**Lemma 4.1 (adaptive forced-transition potential).** There is `P:{0,…,3^{17}−1}→{0,…,34}` with `P(F(i)) ≤ P(i)+6`; `P(D_1(i,ℓ^P_1(i))) ≤ P(i)+1` for `i≡0`; `P(D_3(i,ℓ^P_3(i)))+2 ≤ P(i)` for `i≡2`. Checked at `215,233,605` inequalities. Selected-lift counts in each auxiliary family: `42,561,920 / 484,085 / 716` for lifts `0/1/2`; e.g. `D3` index `83` (residue `251`) has successor potentials `(10,9,9)` and selects lift `1`.

With `H(v)=3s(v)+P(i(v))` and `δ=5−3α>0` (`27<32`): principal edges have `ΔH ≤ 0`; each selected auxiliary edge has `ΔH ≤ 3α−5 = −δ`.

**Lemma 4.2 (syndetic rotation obstruction).** If `S⊆N` has bounded gaps, `κ:S→` a finite set, and `s_n = nα−q_n ≥ 0` with `q_n∈N`, it is impossible that `n<n'`, `κ(n)=κ(n')` always forces `s_{n'} ≤ s_n`.

**Theorem 4.3.** From every level-18 principal root the adaptive expansion is finite; every terminal shift is negative. **Lemma 4.5 / Proposition 4.6:** a lift attaining the actual functional minimum is never dominated, so a time-local pruning `E_{i,y}` exists with leaf shifts in `[−ν,−μ]`, `c_i ≤ C_λ(E_{i,y};c)`, and `(E_{i,y}[F])(y) ≤ F_i(y)`. **Lemma 5.1 (choice-valued retarded induction)** then gives **Theorem 5.2:** `φ^{m_i}_{18}(y) ≥ Δ w_i (2^{901/1000})^y` with `Δ = λ^{-ν}/Σ_i w_i > 0`, `ν` unevaluated.

**Lemma 6.1 (nonperiodic source reduction).** For every `a>0`, `3∤a`, there is a positive nonperiodic `b ≡ 2 mod 3` and `r ≥ 0` with `T^r(b)=a` (`b∈{a, 2a, 2^{2p}a, 2^{2p+1}a}`). Then `φ^{m_i}_{18}(y) ≤ π*_b(2^y b) ≤ π_b(2^y b) ≤ π_a(2^y b)` gives `C_a = Δ w_i / b^{901/1000}`.

## Proof architecture

Five interfaces, as the paper lists them: (1) inverse branches give the difference system; (2) an exact level-18 vector satisfies the LP at `λ=2^{901/1000}`; (3) history-sensitive expansion plus a finite adaptive potential produce finite normal forms with uniformly negative terminal shifts; (4) time-local critical pruning follows lifts that attain the functional minima, preserving the functional inequality and only improving the coefficient inequality; (5) a choice-valued retarded induction gives exponential envelope growth, and target reduction plus the exponent reserve `1/1000` give Theorem 1.1.

The reusable mechanism, in the paper's words: finite potential + strict fallback loss + history domination ⇒ retarded time-local choice witnesses. The Lean consumer is generic in the level and in the selected lifts; only the two payloads are level-specific.

## Evidence replayed here, and not replayed

Replayed exactly ([`../mazur-2026-checks/replay_paper_numerics.py`](../mazur-2026-checks/replay_paper_numerics.py), all pass):

- the three coefficient inequalities (15)–(17), and that each is **tight**: replacing `A`, `B_1`, or `B_3` by its successor breaks the inequality, so the dyadic constants are the largest admissible at precision `2^{-28}`;
- `Q=2^{28}`, `901/1000−9/10=1/1000`, `δ>0 ⇔ 3^3<2^5`, and the symbolic identity `3(α−2)+1 = 3(α−1)−2`;
- the Appendix A index maps `f, u_1, u_3` and the displayed auxiliary index triples for `i=0` and `i=2`;
- the three worked first rows `L1, L2, L3` (right-hand arithmetic, divisibility of the left sides by `Q`, the implied weights `7,950,440`, `3,862,897`, `6,357,317` lying inside the reported `[min,max]`, and the row inequalities);
- the residue arithmetic behind `D1/D2/D3`, and the primitive-root fact behind class nonemptiness (spot-checked modulo `3^7`).

Not replayed: the `129,140,163` LP rows, the `215,233,605` potential inequalities, the Lean build, the Python/C++ verifiers, or the payload hashes (the payloads are not in this repository). The repository records the theorem as **external formal evidence with two explicit compiler trust points, inspected in the paper's own description**.

## Boundaries and common misreadings

- `x^{9/10}` is far from positive density; the standard conjecture is `π_a(x) ≥ c_a x`. Nothing here gives `π_1(x) ≥ cx`.
- `3∤a` is forced by the problem, not by the method.
- `901/1000` is a certified feasible value, not the level-18 optimum; no infeasibility is proved for larger exponents; nothing is concluded about levels 16, 17, or the limit question `λ_k → 2`.
- Constants are not extracted: `ν`, `Δ`, `C_a`, and `x_0(a)` exist but are not computed; the theorem is effective in principle at fixed level, not as proved.
- The adaptive potential is level-specific data.
- The result concerns inverse trees; it says nothing about the forward orbit of any specific integer and does not touch `SC*`, `FC*`, or extraction.

## Interfaces to the repository programs

- **Least-counterexample basin.** For a least counterexample `n_*`, the basin of its orbit contains the predecessor set of `a=T(n_*) ≡ 2 mod 3`, so it has at least `x^{9/10}` elements below `x` eventually; combined with the fixed-target density theorem this gives the two-sided constraint `T-DI-003`. It is a constraint, not a contradiction.
- **Open issue #25** asks, as its unconditional "reshaping half", for the Krasikov–Lagarias system to be ported from root `1` to an arbitrary root. The Krasikov–Lagarias theorem and this paper are already stated for every target `a` with `3∤a`, so that half is settled by the literature at exponent `9/10`; what remains of #25 is its conditional disproof half.
- **3-adic duality.** Level-`k` residues are the inverse-tree analogue of the repository's depth-`k` parity cylinders. The repository's Program 4 quantities `2^j−3^q` are 2-adic and 3-adic simultaneously; the KL system sees only the 3-adic side.
- **Termination technique.** The syndetic rotation obstruction (Lemma 4.2) is a Diophantine well-foundedness principle for shifts `nα−q_n ≥ 0` under finite coloring. It is similar in spirit to the repository's `L-0042` (bounded-gap integrality forces polynomiality) and may be reusable wherever a finite-state expansion has one advanced term.

## Reviewer notes

1. Disjointness of the two inverse-branch predecessor families in Proposition 2.2 relies on nonperiodicity of the target; the paper argues it by return times. The bounded-orbit normalization `π* ≤ π` is what keeps every branch under one cutoff.
2. Lemma 4.2 is proved by a sketch in the paper (irrational rotation, order-preserving translations on a short interval, pigeonholing offsets); the Lean development is the full proof.
3. The fallback selector is consulted only in the all-dominated case; the separation between coefficient transport (any nonempty subfamily) and functional choice (actual minimizer, never dominated) is the point that makes adaptivity safe.
4. The `native_decide` trust points are explicitly listed; the separate verifiers include a deliberate mutation test.
5. The exponents across levels (`.84` at 11, `.88` at 15, `.90` at 18) suggest diminishing returns per level; see the improvement map.

## Improvement targets

See [`research/density-interfaces/IMPROVEMENT_MAP.md`](../../research/density-interfaces/IMPROVEMENT_MAP.md), targets `T2.1`–`T2.7`: optimize the exponent at level 18; level 21 (`3^{20}` rows); dual certificates at small levels to chart the exact optimum `γ_k`; a nonlinear Perron–Frobenius formulation of `λ_k → 2`; a uniform potential family; effective thresholds; and the positive-density question.
