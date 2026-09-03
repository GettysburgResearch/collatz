# Mazur 2026 — natural-density almost-bounded Collatz orbits in logarithmic time

## Status

- **Kind:** external literature packet. Nothing here is a resident theorem of this repository.
- **Evidence state:** the author reports a Lean 4 formalization at frozen commit `f386357d453ac4dcf91242b76252d88a5a729906` (Lean `v4.30.0-rc2`, Mathlib `5450b53e5ddc75d46418fabb605edbf36bd0beb6`), axiom footprint `propext`, `Classical.choice`, `Quot.sound`, no `native_decide`, no `sorry`, and a `leanchecker` replay. **Not replayed in this repository.** The finitely many paper-exposed numerics were replayed exactly; see [Evidence](#evidence-replayed-here-and-not-replayed).
- **Collatz status:** an almost-everywhere theorem with an explicit time budget. It permits an infinite exceptional set of natural density zero and proves nothing about any single orbit.
- **Repository inferences:** `PROPOSED` claims only, in [`research/density-interfaces/`](../../research/density-interfaces/README.md).

## Source

Lech Mazur, *Natural-density almost-bounded Collatz orbits in logarithmic time*, version 2, dated July 21, 2026. MSC 11B83; 11J82, 37P99, 68V20.

- Local copy: [`source/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf`](source/Mazur_Natural_Density_Collatz_Orbits_in_Logarithmic_Time_v2.pdf), SHA-256 `08a46dd1cdd9183beb2e09af517361f24d3b7945a6ee00db563a944a4a2373cf`.
- Formal sources reported at `https://proofatlas.ai/sources/natural-density-log-time-collatz/`; paper import `Erdos1135.ND.LogTime.Paper`.
- The paper carries a generative-AI disclosure: AI systems contributed substantially to exploration, proof development, formalization, computation, and exposition; the author designed the harness, reconciled outputs, and takes responsibility for the manuscript.

## Normalization

Three maps occur. The repository's map is the shortcut `T`.

| Symbol | Definition | Domain | Relation to `T` |
|---|---|---|---|
| `Col` | `n/2` if even, `3n+1` if odd | positive integers | the `Col`-orbit value set is the `T`-orbit value set plus the intermediate values `3m+1` (`m` odd), all larger than their predecessor |
| `Syr` | `(3n+1)/2^{ν_2(3n+1)}` | odd integers | `Syr(n)=T^{ν_2(3n+1)}(n)`; the `Syr`-orbit is exactly the sequence of odd values of the `T`-orbit |
| `T` | `n/2` if even, `(3n+1)/2` if odd | positive integers | repository map |

Consequences used by the interface claims:

- For every `N`, "the `Col`-orbit never takes a value `≤N_0`" is equivalent to "the `T`-orbit never takes a value `≤N_0`".
- For odd `N`, "the `T`-orbit never takes a value `≤N_0`" implies "the `Syr`-orbit never takes a value `≤N_0`". The converse can fail at an even `T`-value.
- The two clocks count different objects: `C_Syr log N` counts odd-to-odd Syracuse steps of an odd input; `C_Coll log N` counts raw steps.

Other conventions: `log` is natural, `log_2` is base two; the machine-checked natural count is half-open, `D_X(A)=#(A∩[0,X))/X`; "relative natural density one among the odds" is encoded as natural density `1/2`; the fixed-target numerator uses the inclusive count through `⌊x⌋` with a positive odd guard; `α=1001/1000` is Tao's block exponent, **not** the repository's `α=log2/log3`.

## Exact statements

All constants below are the paper's.

**Theorem 1.1 (natural-density logarithmic-time theorem).** Put

```text
C_Syr  = 501501 / (5000 log 2)   < 145     (≈ 144.7026)
C_Coll = 1509503 / (5000 log 2)  < 436     (≈ 435.5505)
```

(i) If `f:N→R` tends to `+∞` along the odd integers, then the odd `N` for which some `m∈N` satisfies `m ≤ C_Syr log N` and `Syr^m(N) < f(N)` have relative natural density one among the odd integers.

(ii) If `f:N→R` tends to `+∞`, then the positive integers `N` for which some `m∈N` satisfies `m ≤ C_Coll log N` and `Col^m(N) < f(N)` have natural density one.

The quantifier order is `∃C ∀f`; the density-one set depends on `f`, the clock does not. The conclusion is strict.

**Theorem 1.2 (quantitative fixed-target theorem).** For every real `d` with `0<d<5/143` there is `C_d ≥ 0` such that for all integers `N_0 ≥ 2` and all real `x ≥ 2`,

```text
(1/x) · #{ N odd, 1 ≤ N ≤ ⌊x⌋ : no m ≤ C_Syr log N has Syr^m(N) ≤ N_0 }  ≤  C_d (log N_0)^{-d}.
```

One may take `d_0 = 6993/200000 = 0.034965` and `5/143 − d_0 = 1/28600000`. The prefactor `C_d` and the transport threshold are existential; `d_0`, the auxiliary no-hit exponent `1/32000`, and both clocks are explicit.

**Corollary 1.3 (raw-time order optimality).** On a natural-density-one set, some `m` satisfies `log N/(2 log 2) < m ≤ C_Coll log N` and `Col^m(N) < √N`; the lower inequality holds for every raw witness below `√N` (Proposition 7.2: `Col^m(N)<b` forces `m > (log N − log b)/log 2`, from `n ≤ 2^m Col^m(n)`).

**Theorem 3.1 (two-block transport and scheduled hitting).** With `s(x)=⌊log⌊x⌋/(10 log 2)⌋`, `C_hit=184`, `C_tr=384256`, blocks `B_y={N odd : ⌈y⌉ ≤ N ≤ ⌊y^α⌋}`, uniform law `U_y` and reciprocal law `L_y` on `B_y`: for fixed `0<d<5/143` there is `x_0` such that for `x ≥ x_0` and `y∈{x^α, x^{α^2}}`,

```text
P( T_x(U_y) > s(x) )                                   ≤ 184 · x^{-1/32000},
‖ L(Pass_x(U_y)) − L(Pass_x(L_y)) ‖_1                 ≤ 384256 · (log x)^{-d}.
```

**Proposition 3.2 (Rhin phase gap).** `‖q log_2 3‖_{R/Z} ≥ c q^{-133/10}` for all `q ≥ 1` and some `c∈(0,1]`; i.e. the form `‖qθ‖ ≥ c q^{1−κ}` holds with `κ = 143/10`. Source: Rhin's three-term bound `|u_0 + u_1 log 2 + u_2 log 3| ≥ H^{-13.3}`, `H=max(|u_1|,|u_2|) ≥ 2`, used only with `u_0=0`. The Lean development reconstructs a weaker eventual large-height statement from Rhin's Padé construction rather than installing the printed proposition as an axiom.

**Lemma 3.3 (phase discrepancy).** For the rotation `φ+nθ`, `θ=log_2 3`, both endpoint conventions satisfy `D_N(φ) ≤ min{1, (6 + 2/(πc)) N^{-1/κ}}` (Erdős–Turán).

**Proposition 3.6 (common band profile).** For `0<d<1/20`, `d<1/(2κ)`, uniformly in branch, band, event and flat/harmonic law, `|P^σ_{b,j}(E) − Z_B(E)| ≤ 7 (log B)^{-d}` for large `B`; the ledger continues `7 → 8` (whole source) `→ 16` (triangle) `→ 32` (full `ℓ^1`) `→ 384256` (real-floor adapter).

**Lemma 4.1 (timed geometric trace).** With `r=α^{-1}`, for `N_0 ≥ N_*` and `X>N_0` there is an integer `T ≤ (1001/(10 log 2)) log X` with `P_{N∼L_{X^r}}(no m ≤ T : Syr^m(N) ≤ N_0) ≤ C_trace (log N_0)^{-d}`. The `1001` is exactly `α/(α−1)`.

**Section 6 (two-adic fibers).** For `N=2^a M`, `M` odd, and `k` Syracuse steps with total stripped exponent `W`: `Col^{a+k+W}(2^a M) = Syr^k(M)` exactly, `W ≤ 2k + log_2 M`, and `a + log_2 M = log_2 N`; hence `C_Coll = 3 C_Syr + 1/log 2`.

## Proof architecture

Load-bearing chain, as the paper states it:

```text
Rhin phase gap ⇒ phase average ⇒ normalized band profile
             ⇒ exact source mixture and totalization ⇒ two-block passage transport
             ⇒ timed fixed-target estimate (top-block splice, geometric clock)
             ⇒ density one for every f→∞ (freeze a target K)
             ⇒ raw map by two-adic fibers (exact valuation telescope).
```

Where the exponent enters: the physical valuation tube has length `W ≍ √(n_0 log n_0)` with `n_0 ≍ log B`, so the discrepancy `N^{-1/κ}` over the tube is `(log B)^{-1/(2κ)}`; the halving is the tube. All other errors tolerate `d<1/20`. Since `1/(2κ)=5/143<1/20`, the Diophantine input is the binding guard.

Schedules: `n_0(B)=⌊log_2 B/10⌋` (Tao's passage horizon), `m_0(B)=⌊log B/100000⌋` (step-back time of the lost window), `m_B=⌈m_0(B)(log B)^{-2/5}⌉` (affine reference depth). The construction is asymptotic: `m_0(B)=0` for `B<e^{100000}`.

## What is new relative to prior work

As the paper positions itself and as read here: natural-density descent is classical (Terras, Everett, Möller, Heppner, Allouche; Korec for every `θ > log_4 3`); Inselmann has natural-density trajectory control to fixed power targets with far smaller clocks (`3/log(4/3) ≈ 10.43` raw, `1/log(4/3) ≈ 3.48` Syracuse steps per `log N`); Tao has arbitrary `f→∞` in logarithmic density; Gonçalves–Greenfeld–Madrid generalize Tao in logarithmic density. The new combination is: arbitrary `f→∞`, natural density, one explicit clock retained through the global statement, a quantitative natural-counting fixed-target bound, and a formal proof. The lower raw bracket is a deterministic complement, not a priority claim.

## Evidence replayed here, and not replayed

Replayed exactly ([`../mazur-2026-checks/replay_paper_numerics.py`](../mazur-2026-checks/replay_paper_numerics.py), all pass):

- `C_Coll = 3C_Syr + 1/log 2`; `C_Syr<145`, `C_Coll<436` using `0.693<log 2`; the `log_2`-form coefficients `100.3002`, `301.9006`;
- `1/(2κ)=5/143`, `5/143−d_0=1/28600000`, `5/143<1/20`;
- the constant ledgers `88+96=184` and `192+64+384000=384256`, `2/log(4/3) ≤ 8`, `α/(α−1)=1001`, `(1002/(10 log 2))·(1001/1000)=C_Syr`;
- the exact raw/Syracuse identity `Col^{a+k+W}(2^a M)=Syr^k(M)` and `W ≤ 2k+log_2 M` on sample inputs;
- Lemma 7.1 `n ≤ 2^m Col^m(n)` for `n<2000`, `m<60`.

Not replayed: the Lean development, the Rhin reconstruction, the transport ledger, any density statement. The repository records these as **external formal evidence, inspected in the paper's own description**.

## Boundaries and common misreadings

- Density one is not "all"; the exceptional set may be infinite. The theorem is compatible with the existence of divergent orbits and nontrivial cycles.
- The density-one set depends on `f`; only the clock is uniform.
- The fixed-target bound is `(log N_0)^{-d}` with `d<0.035` and an existential prefactor; it cannot be evaluated at any concrete `N_0`.
- Nothing is effective below `B=e^{100000}`.
- The Syracuse and raw clocks count different steps; the raw lower bracket has no Syracuse analogue.
- The theorem does not improve the exponent chain for predecessor sets and does not give positive density for the set of integers reaching `1`.

## Interfaces to the repository programs

- **Central firewall.** The result is an averaged statement; by the repository's extraction theorems it cannot decide `SC*`, `FC*`, or any least-root question. It sits on the far side of the firewall from every resident program.
- **Program 3 (`SC*`).** A fixed positive source in Lane A whose surplus `D_k=q_k−αk` stays below `H` has an orbit of lower natural density `≥ 2·3^{-H}` inside the fixed-target bad set `B_{n−1}`. Theorem 1.2 bounds that set's density by `2C_d(log(n−1))^{-d}` (after summing two-adic fibers). This is the exact interface `T-DI-002`; with the existential `C_d` it yields only `sup_k D_k ≥ d log_3 log(n−1) − log_3 C_d`.
- **Program 4 / Program 2.** The same Rhin bound is the Diophantine input of the classical `m`-cycle exclusions (Simons–de Weger). That literature is a natural source-pinned import for the periodic packet; it is not imported here.
- **Program 1.** No interface: densities say nothing about canonical least representatives.
- **Open issue #78** asks for Tao/Inselmann-type exceptional-set bounds to be "coupled to an actual least-counterexample inverse tree"; `T-DI-002` and `T-DI-003` are that coupling, and they show what it does and does not yield.

## Reviewer notes

Observations from a careful reading; none is a claimed error.

1. Theorem 1.2 is stated for all `N_0 ≥ 2`, `x ≥ 2`; the case `x ≤ N_0` is empty and the finitely many small targets are absorbed into `C_d` by `2(log N_*)^d`. The uniformity in `x` is what makes fiber sums over `x/2^a` legitimate.
2. The two-adic transfer uses `k ≤ C_Syr log M ≤ C_Syr log N`; the clock in (ii) is therefore in terms of `log N`, including the halving prefix `a ≤ log_2 N`.
3. The `d` of Theorem 3.1 and of Theorem 1.2 is the same literal `d`; the no-hit exponent `1/32000` is kept separate so as not to degrade it.
4. The Rhin input is used only as `u_0=0`, `(u_1,u_2)=(−p,q)` with `H ≤ 2q`; the paper is explicit that the sharper `7.616` line is unused because its effective threshold is not printed.
5. The novelty statement is candid about Inselmann and about the Terras–Korec line.

## Improvement targets

See [`research/density-interfaces/IMPROVEMENT_MAP.md`](../../research/density-interfaces/IMPROVEMENT_MAP.md), targets `T1.1`–`T1.6`. In brief: the exponent cap moves from `5/143` to `1/20` with any effective irrationality measure `κ<10` and no further without reworking the terminal estimates; the clocks carry a slack of roughly `40×` over the intrinsic `1/log(4/3)` Syracuse rate; effective constants are the decisive missing ingredient, and an explicit fixed-target bound below `1/2` at a computationally verified target would give positive density for the basin of `1`.
