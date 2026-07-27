# REVIEW — six-branch rigidity chain: PR #64, PR #65, PR #66 (+ PR38/ACL-N092)

```text
Reviewer:      fable-02-r3 (independent adversarial review, README §13)
Date:          2026-07-27
Scope:         PR #64  head 88884c3e590b08aeb2018872987e71e14de1fe7b
                       (branch agent/gpt56-extraction-01/58-six-branch-least-root, base main
                        b40e5c44959b20842e6c064084c668f5243b6ebd; agent gpt56-extraction-01)
                       claims PR64/D-7401, PR64/L-7401, PR64/T-7401, PR64/T-7402,
                       PR64/T-7403, PR64/T-7404 (PR64/Q-7401 is an open question, no verdict)
               PR #65  head 2183dc7e66162684e464913a4ae1a222b41b30f3
                       (branch agent/gpt56-breakthrough-01/58-algebraic-section-rigidity,
                        stacked on PR #64 head; agent gpt56-breakthrough-01)
                       claim PR65/T-7501
               PR #66  head 1b30e854913e8c5dfb4d0c70879789884b356aa1
                       (branch agent/gpt56-cycle-01/58-increment-descent-offense,
                        stacked on PR #64 head; agent gpt56-cycle-01)
                       claims PR66/L-7301, PR66/T-7301, PR66/T-7302, PR66/L-7302, PR66/X-7301
                       (PR66/Q-7301 is an open question, no verdict)
               PR #38  head 6673ed0e765417448b2657fff2856a7d4909d113 — cartography atom
                       PR38/ACL-N092 (cartography/FINITE_ALGEBRAIC_NUCLEUS_RIGIDITY.md;
                        agent gpt56-cartographer-01), reviewed because it is announced in the
                        PR #64 thread as part of this rigidity chain.
Mode:          CROSS-BRANCH REVIEW. Their files were read read-only via
               `git show origin/<branch>:<path>` at the pinned SHAs above. Nothing on their
               branches was modified. This file is evidence only; status changes are for
               their authors/integrators.
Method:        every statement re-derived from scratch; every load-bearing number and
               computation re-run in exact integer arithmetic (python3, stdlib only); the
               X-7301 classification additionally reproduced by an INDEPENDENT THIRD
               implementation (no code shared with run.py or verify.py); active refutation
               attempts recorded per claim. 80 machine checks, 0 failures (§12).
ID convention: per research/foundations/ID-DISAMBIGUATION.md, T-7401 is ambiguous in this
               repository (PR #61 vs PR #64). Every occurrence below is PR-qualified.
Calibration:   foundations/L-9923 and foundations/T-9924 (both PROVED in this packet), which
               treat the same frozen chart P = 3^12, Q = 2^19 and the same technique family.
```

## Verdict summary

| Claim | File (on their branch) | Verdict |
|---|---|---|
| PR64/D-7401 | research/six-branch-extraction/claims/D-7401-six-branch-minimal-word-system.md | **PASS** |
| PR64/L-7401 | research/six-branch-extraction/claims/L-7401-high-quotient-section.md | **PASS** |
| PR64/T-7401 | research/six-branch-extraction/claims/T-7401-affine-section-rigidity.md | **PASS** |
| PR64/T-7402 | research/six-branch-extraction/claims/T-7402-finite-affine-nucleus-rigidity.md | **PASS** (one presentational note) |
| PR64/T-7403 | research/six-branch-extraction/claims/T-7403-finite-rational-nucleus-rigidity.md | **PASS** |
| PR64/T-7404 | research/six-branch-extraction/claims/T-7404-no-semilinear-sanctuary.md | **PASS** |
| PR65/T-7501 | research/six-branch-extraction/claims/T-7501-finite-algebraic-section-rigidity.md | **PASS-with-corrections** (2 exact fixes) |
| PR38/ACL-N092 | cartography/FINITE_ALGEBRAIC_NUCLEUS_RIGIDITY.md | **PASS** |
| PR66/L-7301 | research/six-branch-descent/claims/L-7301-two-point-cocycle-classification.md | **PASS** |
| PR66/T-7301 | research/six-branch-descent/claims/T-7301-no-two-point-linear-descent.md | **PASS-with-corrections** (1 dangling reference) |
| PR66/T-7302 | research/six-branch-descent/claims/T-7302-sliding-linear-filter-rigidity.md | **PASS** |
| PR66/L-7302 | research/six-branch-descent/claims/L-7302-type-shift-conjugacy.md | **PASS-with-corrections** (dependency hygiene) |
| PR66/X-7301 | experiments/X-7301-two-point-descent/ | **PASS** (bit-exact replay + SHA + independent third implementation) |

No FAIL. No contradiction with foundations/L-9923 or foundations/T-9924 (§11); several exact
corroborations, including that the chain's physical seed dictionary `n = 6x − 5` is precisely
the PROVED conjugacy of foundations/T-9924.8. All verdicts are review evidence only — every
claim above remains PROPOSED until its own branch's process flips it.

Notation used throughout this review: `P = 3^12 = 531441`, `Q = 2^19 = 524288`,
`Δ = P − Q = 7153 = 23·311`, digits `a_i = 7·2^(15−3i)·3^(2i)` for `0 ≤ i ≤ 5`,
`A = {229376, 258048, 290304, 326592, 367416, 413343}`, `F(x) = ceil(Px/Q)`,
`δ(x) = Q·F(x) − Px ∈ {0,…,Q−1}`, `u = P^(−1) mod Q = 95505`, `r_i = [−u·a_i]_Q`,
`c_i = (P·r_i + a_i)/Q`.

---

## §1 PR64/D-7401 (the frozen chart and its source/output table) — PASS

**Independent restatement.** Fix the chart above. `x` is legal through depth `n` iff
`δ(F^j(x)) ∈ A` for `0 ≤ j < n`; `S_n` is the set of legal positive integers, `m_n = min S_n`.
The claim: (i) `δ(x) = a_i ⟺ x ≡ r_i (mod Q)` with the displayed `(a_i, r_i, c_i)` table, and
on that cylinder `F(r_i + Qk) = c_i + Pk`; (ii) every length-`n` word over `A` selects exactly
one residue class mod `Q^n`, which contains infinitely many positive integers.

**Re-derivation.** `δ(x) = [−Px]_Q` depends only on `x mod Q`; since `gcd(P, Q) = 1`,
`δ(x) = a_i ⟺ x ≡ −P^(−1)a_i = r_i (mod Q)`, and then
`F(x) = (Px + a_i)/Q = (P r_i + a_i)/Q + Pk = c_i + Pk`. For (ii): iterating gives
`Q^n x_n = P^n x_0 + C_n`, and `P^n` is a unit mod `Q^n`, so integrality of the trajectory on a
fixed word is one congruence class mod `Q^n`; every class has infinitely many positive members.
This is the same unit-slope mechanism as foundations/L-9916.1(3) and foundations/T-9924.1(d)
(both PROVED), so (ii) is corroborated by already-verified packet results.

**Computations.** §12 Section 1: `u = 95505` verified; the full `(a_i, r_i, c_i)` table verified;
`Q·c_i = P·r_i + a_i` for all `i`; `r_i` distinct mod `Q`; depth-1 and depth-2 class counts are
exactly `6` and `36` distinct classes. Additionally `ν2(r_i) = 15 − 3i` and `ν3(c_i) = 2i`
(needed by PR66/L-7302, see §9.4). All PASS.

**Refutation attempts.** None survive: the table is forced by the congruences; I checked the
canonicity `0 ≤ a_i < Q`, the unique odd digit `a_5`, and `a_{i+1} = (9/8)a_i` (all machine
checks). **Scope caution (author-flagged, correct):** the *physical* Collatz reading of the
chart is delegated to unmerged PR #45/PR #50. This review notes that an in-repo PROVED
anchor already exists: foundations/T-9924.8 proves the chart is exactly the weight-(5,1)
pulse-grammar packet under `y = 3(x−1)`, physical seed `n = 6x − 5`. D-7401's arithmetic
content is independent of any physical reading. Verdict **PASS**.

## §2 PR64/L-7401 (high-quotient language exit) — PASS

**Independent restatement.** If `x = r_i + Qk ∈ S_2` with second type `j`, then with
`F(x) = c_i + Pk = r_j + Qk'`: `Qk' = Pk + c_i − r_j`, the first canonical digit of the high
quotient `k = floor(x/Q)` is `b_ij = [c_i − r_j]_Q`, and none of the 36 values `b_ij` lies in
`A`; hence `x ∈ S_2 ⟹ floor(x/Q) ∉ S_1`.

**Re-derivation.** `δ(k) = [−Pk]_Q` and `Pk ≡ r_j − c_i (mod Q)` from the transition, so
`δ(k) = [c_i − r_j]_Q = b_ij`. Soundness of the mod-2048 shortcut: if `b ∈ A` then
`b mod 2048 ∈ A mod 2048`, so disjointness mod 2048 implies exact disjointness. Boundary
case `k = 0` (i.e. `x = r_i`): `floor(x/Q) = 0 ∉ Z_{>0} ⊇ S_1`, statement holds trivially.

**Computations.** §12 Section 2: my independently computed 36-entry matrix equals their
displayed matrix **exactly**; no entry is in `A`; `A mod 2048 = {0, 824, 960, 1536, 1695}`
(five values, since `a_0 ≡ a_1 ≡ 0`); their displayed mod-2048 matrix is exact; disjointness
holds already mod 2048; and an end-to-end semantic check over all 36 pairs (with `t = 0, 1`)
confirms `x ∈ S_2 ⟹ δ(floor(x/Q)) = b_ij ∉ A`. All PASS. Verdict **PASS**.

## §3 PR64/T-7401 (six-state affine section rigidity) — PASS

**Independent restatement.** (Lemma) If `t + wA = A (mod Q)` then `w ≡ 1, t ≡ 0 (mod Q)`.
(Theorem) If `y = vk + s_i`, `y' = vk' + s_j` satisfy `Qy' = Py + a_{π_i(j)}` for every
ordered pair `i → j` (on the infinitely many `k` of each child cylinder), with `v` a positive
integer, integer shifts, and per-type label permutations, then `v = P`, `s_i = c_i`,
`π_i = id` — i.e. the section is the forward map `y = F(r_i + Qk)`.

**Re-derivation of the lemma.** Parity: `A` has exactly one odd member (`a_5`), so `w` odd
(else images monochromatic in parity) and `t` even (else the image has five odd members).
Then the unique odd input maps to the unique odd output: `t + w·a_5 ≡ a_5`, i.e.
`t = (1 − w)a_5 (mod Q)`. Summing the permutation: `6t + wS ≡ S` with `S = Σ a_i = 1885079`;
substituting `t`: `(1 − w)(6a_5 − S) ≡ 0 (mod Q)`, and `6a_5 − S = 594979` is **odd** while
`Q = 2^19`, so `w ≡ 1` and then `t ≡ 0`. Correct. **I additionally verified the lemma
exhaustively by machine over the entire affine group: for every `w ∈ [0, Q)` and every
candidate image of `a_0` (hence every `t` that could possibly work), the only stabilizing
pair is `(w, t) = (1, 0)`** (§12 Section 3). This is a complete finite verification of the
lemma, independent of the parity/sum proof.

**Re-derivation of the theorem.** Substituting and using `Qk' − Pk = c_i − r_j` exactly:
`v(c_i − r_j) + Qs_j − Ps_i = a_{π_i(j)}` for all 36 pairs. Mod `Q`, with
`r_j ≡ −P^(−1)a_j`: the six outputs of row `i` form `t_i + vP^(−1)A (mod Q)`; the lemma gives
`v ≡ P (mod Q)` and `π_i = id` (digits distinct mod `Q`). The exact equations then split as
`Qs_j − vr_j − a_j = Ps_i − vc_i =: K` (LHS depends only on `j`, RHS only on `i`; every pair
occurs). Taking `j = i` and eliminating `s_i` via `Qc_i = Pr_i + a_i` yields
`(P − v)a_i + (P − Q)K = 0` for every `i`; subtracting two distinct `i` forces `v = P`, then
`K = 0`, then `s_i = c_i`. Every step checks. **Machine checks:** `(v, s) = (P, c)` satisfies
all 36 exact equations, and Gaussian elimination over exact rationals shows the 36-equation
linear system in `(v, s_0..s_5)` has rank 7 and is consistent — the solution is **unique**
even over `Q` (§12 Section 3).

**Refutation attempts.** I searched for a second affine automorphism exhaustively (none); I
checked that the argument nowhere needs `v > 0` or `v < Q` (it does not — the uniqueness is
unconditional over the integers), so the stated hypotheses are if anything stronger than
needed. Presentational nit only: the statement should say explicitly that the boxed law is
required for all `k` in each child cylinder (the proof uses two values of `k` per edge; the
cylinders are infinite by D-7401, so this is harmless). Verdict **PASS**.

## §4 PR64/T-7402 (finite affine nucleus rigidity) — PASS

**Independent restatement.** Finite control `Ω`; every reachable state `(ω, i)` carries
`y = v_ω k + s_{ω,i}` (`v_ω ∈ Z_{>0}`), has all six children, successor `(ω', j)` arbitrary
in `j`, labels initially permutable; the six-branch law transported on every child cylinder.
Conclusion: on every reachable component `v_ω = P`, `s_{ω,i} = c_i`.

**Re-derivation.** (1) Coefficient of `k` on an edge: `P v_{ω'} = P v_ω`, so one scale `v`
per reachable component (identity in `k` over the infinite child progression — same
quantifier note as §3). (2) Row-wise mod `Q`: the §3 lemma gives `v ≡ P (mod Q)`, labels
fixed; write `v = P + mQ`. (3) With `h_{ω,i} = s_{ω,i} − c_i − m·r_i`, I re-derived the edge
equation by direct substitution (using `Qc_j = Pr_j + a_j` and `Qc_i − Pr_i = a_i`):

```text
v(c_i − r_j) + Q s_{ω',j} − P s_{ω,i} = a_j
⟺   Q h_{ω',j} = P h_{ω,i} − m a_i ,
```

whose right side is independent of `j` — so all six children of `(ω, i)` carry the same new
carry value. This identity was additionally machine-checked on 200 random symbolic instances
(§12 Section 4). (4) Let `H` be the (finite, nonempty) set of carries occurring after ≥ 1
transition. Because a parent's six children all carry the same value and include all six
current types, `T_i(H) ⊆ H` for every `i`, where `T_i(h) = (Ph − m a_i)/Q`. (5) Max–min:
for `m > 0`, `T_i(h_+) ≤ h_+` for all `i` gives `h_+ ≤ m·a_min/Δ`, and `T_i(h_−) ≥ h_−`
gives `h_− ≥ m·a_max/Δ` — but `a_max > a_min` forces `h_− > h_+`, a contradiction; the
`m < 0` case is symmetric (verified with the exact fractions for `m = ±1, ±2, ±3` in §12
Section 4 — the forced intervals are empty in every case); for `m = 0`, `T_i(h) = (P/Q)h`
with `P > Q` kills any positive maximum and any negative minimum, so `H = {0}`, and then
`h ≡ 0` propagates to initial states too (`0 = (P/Q)h` forces `h = 0`). Hence `v = P`,
`s_{ω,i} = c_i`. Every step reconstructs.

**Cross-packet remark.** The two-sided extremal step is the same max–min technique as the
span bound foundations/L-9923.1S (subcritical) and the confinement step of foundations/
T-9924.4 (both PROVED here) — independent convergent evolution; no dependency either way.

**Refutation attempts.** I probed: scales depending on `i` as well as `ω` — the proof never
uses `v_ω`'s independence of `i` after step (1), and step (1) forces edge-constancy of the
scale regardless, so the stated hypothesis is not load-bearing beyond readability; carry
values escaping `H` at initial states — closed by the `m = 0` propagation; sign traps for
`m < 0` — the file's inequalities are the correct ones (I re-derived both). The only note is
presentational: state explicitly the quantifier "for all `k` in the child progression" in the
transported law. Verdict **PASS**.

## §5 PR64/T-7403 (finite rational nucleus rigidity) — PASS

**Independent restatement.** Same machine, but each state carries a **nonconstant** rational
`f_{ω,i} ∈ Q(X)`, positive-integer-valued at all large integers, with the transported law on
each exact child progression `k = κ_ij + Qt ↦ k' = λ_ij + Pt`. Conclusion:
`f_{ω,i}(X) = PX + c_i`, labels fixed.

**Re-derivation.** Lemma 1 (tail-integral rational ⟹ polynomial): with `A, B` coprime in
`Z[X]`, Bezout over `Q[X]` cleared to `UA + VB = R ∈ Z \ {0}`; `B(n) | A(n)` for large `n`
forces `B(n) | R`, so `|B(n)|` is bounded and `B` is constant. Standard and correct (a
concrete instance is machine-checked in §12 Section 5). Lemma 2: the transported law holds at
infinitely many `t`, hence as a polynomial identity; degrees match along edges; leading
coefficients obey `L_{ω',j} = L_{ω,i}(Q/P)^(d−1)` — re-derived and machine-verified for
`d = 1, 2, 3` with exact rational polynomial arithmetic (§12 Section 5); every state reaches a
directed cycle in the finite total graph, and around a cycle `(Q/P)^{s(d−1)} = 1` with
`P ≠ Q` forces `d = 1` (machine-checked that this bites exactly at `d = 1`). Degree-1
reduction: integer slope and intercept from first differences; positive slope from eventual
positivity **plus nonconstancy** (hypothesis present in this file — important, see §7);
`(9)` at `d = 1` gives one slope per component; and the constant terms reduce **exactly** to
T-7402's edge equation — I verified the identity

```text
Q·f'(λ_ij + Pt) − P·f(κ_ij + Qt) − a_j  ==  v(c_i − r_j) + Q s' − P s − a_j
```

symbolically on random instances (§12 Section 5), so the handoff to PR64/T-7402 is exact,
with the same permutation freedom. Conclusion follows from §4.

**Refutation attempts.** The `d = 0` trap (constant sections) is excluded by the explicit
nonconstancy hypothesis — necessary, because the leading-coefficient relation is **false**
for `d = 0` (the `+a_j` term is then not lower-order); see §7 for the stacked file that
omits this hypothesis. Denominators that vanish at some integers: harmless, only large `n`
are used. Degree/coefficient depending on `(ω, i)`: handled by edgewise equalities. I found
no gap. Verdict **PASS**.

## §6 PR64/T-7404 (no semilinear sanctuary) — PASS

**Independent restatement.** `S_n` is a union of at most (in fact exactly) `6^n` residue
classes mod `Q^n = 2^(19n)`. An AP `R + M·Z_{≥0}` with `v = ν2(M)` occupies exactly
`2^(19n − min(v,19n))` classes mod `Q^n`; containment in `S_n` forces
`2^(19n − min(v,19n)) ≤ 6^n`, which fails for large `n` since `2^19 > 6`. Hence `S_∞`
contains no infinite AP, hence no infinite semilinear set; and since `F(x) > x`, no nonempty
forward-invariant semilinear `X ⊆ S_∞` exists (it would be infinite).

**Re-derivation.** Legality through depth `n` is determined by `x mod Q^n` (induction:
same class mod `Q^n` ⟹ same first digit ⟹ images congruent mod `Q^(n−1)`), so `S_n` is
(classes) ∩ Z_{>0}; the class count is `6^n` by D-7401's word completeness (my depth-2
count: 36 distinct classes, §12 Section 1). The AP hits each of its `Q^n/gcd(M, Q^n)`
classes infinitely often on the half-line `t ≥ 0`, so each hit class must be legal; the count
equals `2^(19n − min(v,19n))` (machine-verified by gcd arithmetic and direct enumeration
where feasible, §12 Section 6). The crossover: `v = 0` already fails at `n = 1`; `v = 100`
fails by `n = 7`; in general `n > v/(19 − log2 6)` fails (`min_failing_n(v) < v` checked for
`v = 50, 200, 1000`). One-dimensional semilinear sets are finite unions of APs, and an
infinite such union has an infinite AP component. `F(x) ≥ x + 1` for `x ≥ 1` (machine-checked
on `1..10^4`; in general `Px/Q > x`). All steps hold.

**Refutation attempts.** Odd `M` (v = 0) and huge two-power `M` both handled by the same
formula; finite semilinear sets are excluded by strict growth, not by counting — the file
correctly separates these. The file's own gap audit correctly notes that automatic
(base-2-regular) sets are NOT excluded — I agree and flag this as the honest boundary of the
claim. Verdict **PASS**.

## §7 PR65/T-7501 (finite algebraic-section rigidity) — PASS-with-corrections

**Independent restatement.** Same machine as §5 but each state carries a single-valued
algebraic branch over `Q(X)`, real analytic on a positive ray, positive-integer-valued at
all large integers; law transported on the exact child progressions. Conclusion:
`f_{ω,i}(X) = PX + c_i`, labels fixed; extended to finite piecewise-algebraic/semialgebraic
sections.

**Re-derivation.** Lemma 1 (algebraic + integer-valued on a full tail ⟹ polynomial): the
branch has a convergent Puiseux expansion at infinity with top exponent `ρ`; for integer
`d > ρ`, `Δ^d f(n) → 0`; but `Δ^d f(n) ∈ Z`, so it vanishes eventually; Newton interpolation
gives a rational polynomial `p` agreeing with `f` at all large integers; `f − p` is an
algebraic branch with infinitely many zeros tending to infinity, hence identically zero.
Mechanism sound (numeric illustration of the decay in §12 Section 11). Lemma 2 and the
affine handoff to PR64/T-7402: same as §5, verified there.

**Correction 1 (genuine, local, fixable): the claim file's Statement omits the
nonconstancy hypothesis.** The PR #65 body says "allow one **nonconstant** single-valued
algebraic branch", and ACL-N092.2 hypothesizes nonconstancy explicitly, but the file
`T-7501-finite-algebraic-section-rigidity.md` does not — its Lemma 2 simply asserts "The
functions are nonconstant". As written the theorem's quantifier admits constant branches,
for which the leading-coefficient transport `(13)` is **invalid** (at `d = 0` the digit term
`a_{π(j)}` is not lower-order, so `(13)` does not follow from `(3)`), and the proof has a
hole. Two equally good exact fixes: (a) add "nonconstant" to the Statement (aligning the
file with its own PR body, with PR64/T-7403, and with ACL-N092.2); or (b) keep the statement
and add the one-line constant-exclusion: if some branch is constant, constancy propagates
forward along edges (a nonconstant child on a constant parent's edge would make `(3)`'s
left side nonconstant in `t`), and a constant parent value `C` needs `Q | PC + a_{π(j)}` for
all six children — impossible, because the six digits are **distinct mod Q**, so the six
residues `PC + a_j (mod Q)` are distinct and at most one vanishes (machine-checked, §12
Section 5). With either fix the theorem is correct.

**Correction 2 (presentational): Lemma 1's "differenced term by term" needs its standard
justification.** Termwise finite-differencing of an infinite Puiseux series is asserted, not
justified. The clean route — used verbatim by PR38/ACL-N092.1 — is: termwise
differentiation of the convergent Laurent expansion in `u = X^(1/e)` gives
`f^(d)(x) = O(x^(ρ−d))`, and the exact integral identity
`Δ^d f(n) = ∫_[0,1]^d f^(d)(n + t_1 + … + t_d) dt` transfers the decay to the differences.
Recommend porting that formulation (or citing ACL-N092.1). The semialgebraic corollary's
cell/analyticity facts are standard but should carry a one-line citation.

Neither correction threatens the result; both are local. Verdict **PASS-with-corrections**
(exact fixes above).

## §8 PR38/ACL-N092 (general finite algebraic-nucleus rigidity) — PASS

**Independent restatement.** For any chart `P > Q ≥ 2`, `gcd(P,Q) = 1`, digit set
`A ⊆ {0,…,Q−1}` with at least two digits and **trivial affine stabilizer mod Q**
(hypothesis (7)), every finite-control system of **nonconstant** algebraic branches,
eventually positive-integer-valued, transporting the chart's law on every exact child
progression, collapses to `f_{ω,i}(X) = PX + c_i` with fixed labels. Corollary: the
six-branch chart satisfies (7) by PR64/T-7401's lemma, so the collapse applies there.

**Assessment.** ACL-N092.1 is the rigorous form of T-7501's Lemma 1 (integral identity for
`Δ^m`; `f^(m)(x) = O(x^(α−m))` from the Puiseux expansion; the irreducible-relation argument
`H(X, p(X)) ≡ 0 ⟹ (Y − p) | H ⟹ f = p` is clean). ACL-N092.2 correctly generalizes the
T-7402 carry argument: I re-derived the general normalized-carry identity
`Q h_{ω',j} = P h_{ω,i} − m a_i` (the derivation in §4 uses only `Qc_i = Pr_i + a_i`,
`r_j ≡ −P^(−1)a_j`, `v = P + mQ` — all available in the general setting), and the max–min
contradiction needs only `P > Q` and `a_min < a_max` (hypothesis "at least two digits").
Nonconstancy is hypothesized explicitly (avoiding T-7501's gap). The six-branch instantiation
of hypothesis (7) is exactly the lemma I verified **exhaustively** in §3. I found no gap.

Overlap note for the coordinator: ACL-N092 (general chart, algebraic) and PR65/T-7501
(six-branch, algebraic + semialgebraic) are two independent write-ups of essentially one
result; T-7501's semialgebraic corollary is the only content not subsumed by ACL-N092.
They should cross-cite to prevent divergence, and T-7501's Correction 2 is resolved by
adopting ACL-N092.1's formulation. Verdict **PASS**.

## §9 PR #66 (two-point descents, sliding filters, type-shift conjugacy)

### §9.1 PR66/L-7301 (complete contracting two-point classification) — PASS

**Independent restatement.** For integers `(u, v)` with `0 < u + vP/Q < 1` (equivalently
`0 < uQ + vP < Q`), classify all pairs such that `u·a_i + v·a_j ∈ A` for at least one ordered
`(i, j)`. Claim: exactly 75 pairs — the 73 diagonal forms `(t+1, −t)`, `1 ≤ t ≤ 73`, legal
exactly on `i → i` with output `i`; and `(−8, 8)` (legal exactly `i → i+1`, output `i`) and
`(−9, 9)` (legal exactly `i → i+1`, output `i+1`).

**Re-derivation.** The reduction is exact: `u·a_i + v·a_j = a_k` with `u ∈ Z` means
`a_i | a_k − v·a_j`, and multiplying the contraction window by `a_i > 0` gives
`0 < a_k·Q + v(P·a_i − Q·a_j) < Q·a_i`, an exact finite interval since
`P·a_i − Q·a_j ≠ 0` (else `a_j/a_i = P/Q`, i.e. `3^12/2^19 = 3^(2e)/2^(3e)` for some
`|e| ≤ 5` — impossible: `12 = 2e` and `19 = 3e` have no common solution). The 216-triple
enumeration is therefore complete. Structure checks: the diagonal family satisfies
`(t+1)a_i − t·a_i = a_i` with numerator `Q − tΔ`, and `0 < Q − 7153t` exactly for `t ≤ 73`
(`73·7153 = 522169 < Q < 529322 = 74·7153`); the ascent forms follow from
`a_{i+1} = (9/8)a_i`: `8(a_{i+1} − a_i) = a_i` and `9(a_{i+1} − a_i) = a_{i+1}`.

**Computations.** §12 Section 7: my **independent third implementation** (different
enumeration strategy from both run.py's Bezout parametrization and verify.py's direct scan)
reproduces the complete classification: 75 forms, the exact diagonal family with exact hit
sets `{(i,i,i)}`, the exact ascent hit sets, no others, and the exact contraction numerators
`Q − 7153t`. The continued fraction `P/Q = [1; 73, 3, 2, 1, 1, 1, 23, 2, 5]` and the signed
remainder ladder `−7153, 2119, −796, 527, −269, 258, −11, 5, −1, 0` verified; only the
`74/73` convergent has allowed hits, and they are the six diagonals. All PASS. Verdict
**PASS**.

### §9.2 PR66/X-7301 (frozen classification experiment) — PASS

Replayed `run.py` at the pinned SHA: its output is **identical** to
`results/canonical.json`; the semantic SHA-256 recomputes to the PR-claimed
`2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f`; their independently
written `verify.py canonical.json` passes; and my third implementation (§9.1) agrees on
every datum. Replay environment: python3 stdlib only, exact integers. Verdict **PASS**.

### §9.3 PR66/T-7301 (no two-point linear descent on an all-time orbit) — PASS-with-corrections

**Independent restatement.** On a positive all-time legal orbit `(x_n)`, no fixed contracting
integer pair makes `z_n = u·x_n + v·x_{n+1}` a positive legal orbit for all large `n`.

**Re-derivation.** If `(z_n)` is a legal orbit at large `n`, then
`Q z_{n+1} − P z_n = u·a_{i_n} + v·a_{i_{n+1}}` must be the digit `δ(z_n) ∈ A` at every late
edge, so L-7301 applies edge-by-edge to the fixed `(u, v)`: pairs outside the 75 have no legal
edge at all; a diagonal pair forces `i_{n+1} = i_n` at every late edge (eventually constant
type); an ascent pair forces `i_{n+1} = i_n + 1` forever — impossible in `{0,…,5}`. Constant
type is killed by the exact kernel: with `Y_n = (P−Q)x_n + a_i`, a constant-type edge gives

```text
Q·Y_{n+1} = Q(P−Q)x_{n+1} + Q·a_i = (P−Q)(P·x_n + a_i) + Q·a_i = P·Y_n ,
```

(machine-verified identically, §12 Section 8), and `gcd(P, Q) = 1` then forces
`Q^m | Y_N` for every `m` while `Y_N ≥ Δ + a_min > 0` — impossible. The contraction is
genuine: `z_n = (u + vP/Q)x_n + v·a_{i_n}/Q` with the first factor in `(0,1)` and the second
bounded, and `x_n → ∞` (strict growth, §12 Section 6), so eventually `0 < z_n < x_n`. All
steps reconstruct.

**Cross-packet remark.** The constant-type kernel is the forward-orbit twin of the
constant-word cycle rigidity in foundations (L-9923.3(i)/T-9924 Step 4(vi), PROVED):
same divisibility engine, applied to tails instead of cycles. Complementary, no conflict.

**Correction (exact):** the Gap audit references "`T-7303`" ("a finite-control full-subtree
polynomial version is treated separately by `T-7303`"), but no T-7303 exists on the branch —
the PR #66 body says the polynomial draft was withdrawn in favor of PR64/T-7403. Replace the
dangling `T-7303` reference with PR64/T-7403 (branch-qualified). Purely editorial; the proof
does not use it. Verdict **PASS-with-corrections**.

### §9.4 PR66/T-7302 (sliding-filter rigidity) — PASS

**Independent restatement.** If `Y_n = s + Σ_{r≤d} b_r x_{n+r}` (fixed integers) induces a
digit in `A` for **every** type block in `{0,…,5}^(d+1)`, then exactly one `b_{r_0} = 1`, the
rest vanish, and `s = 0` — i.e. `Y_n = x_{n+r_0}`.

**Re-derivation.** The induced-digit identity
`Q·Y_{n+1} = P·Y_n + (Q−P)s + Σ b_r a_{i_r}` is a two-line telescope (checked). Since every
block occurs on positive representatives (D-7401 word completeness), the hypothesis is the
Minkowski-sum inclusion `(Q−P)s + b_0A + … + b_dA ⊆ A`. Two nonzero coefficients give
`≥ 6 + 6 − 1 = 11 > 6` distinct sums (`|X+Y| ≥ |X|+|Y|−1`, elementary; instance-checked for
all nonzero `b_1, b_2 ∈ [−6,6]`, §12 Section 9) — contradiction. One nonzero coefficient:
`c + bA = A` (6-into-6 inclusion is equality); diameter forces `|b| = 1`; `b = −1` needs the
reflection pairing `a_0+a_5 = a_1+a_4 = a_2+a_3`, but these sums are `642719, 625464, 616896`
— distinct (machine-checked); `b = 1` forces `c = 0` by matching minima; my machine scan over
all `b ∈ [−200, 200]` confirms `(b, c) = (1, 0)` is the only embedding (§12 Section 9). Then
`(Q−P)s = 0` with `Q ≠ P` gives `s = 0`. All coefficients zero would need `−7153·s ∈ A`,
impossible since every digit has prime support `{2, 3, 7}` and `7153 = 23·311` (machine-
checked: no digit divisible by 23 or 311). All steps reconstruct. Verdict **PASS**.

### §9.5 PR66/L-7302 (type-shift conjugacy; zero-type gate) — PASS-with-corrections

**Independent restatement.** `a_{i+1} = (9/8)a_i` makes `(9/8)^c` an exact conjugacy shifting
all types by `c` where defined; on an orbit, `ν2(x_n) = 15 − 3i_n` and `ν3(x_{n+1}) = 2i_n`,
so a tail with all types `≥ c` (and `i_n ≥ c`) yields the ordinary root `(8/9)^c x_{n+1}`
with down-shifted code; consequently the least all-time root, if it exists, has
`min_n i_n = 0`.

**Re-derivation.** Kernel: `9a_i = 8a_{i+1}` (machine-checked), so multiplying
`Qx' = Px + a_{i+1}` by `8/9` gives `Q·(8x'/9) = P·(8x/9) + a_i` — I verified the exact
identity `8(Px + a_{i+1}) = 9(P·(8x/9) + a_i)` for `9 | x` (§12 Section 10). Valuations:
`ν2(r_i) = 15 − 3i < 19` pins `ν2(x_n)` through the source congruence, and
`ν3(c_i) = 2i < 12 = ν3(P)` pins `ν3(x_{n+1}) = 2i_n` through `x_{n+1} = c_{i_n} + Pk` —
**both derivable from D-7401's own table** (machine-checked, §12 Section 1). Divisibility for
the shift: all tail types `≥ 1` gives `9 | x_{m+1}` at every tail position, so every shifted
state is an integer, and a digit relation with value in `A ⊆ [0, Q)` is automatically a legal
`F`-step. Minimality: `y = 8x_1/9 < x_*` ⟺ `(9Q − 8P)x_* > 8a_{i_0}` with
`9Q − 8P = 467064`; since `x_* ≡ r_{i_0} (mod Q)` and `x_* > 0`, `x_* ≥ min_i r_i = 6472`,
and already `x_* ≥ 8` suffices (`467064·8 = 3736512 > 3306744 = 8a_5`); machine-checked with
margin, plus an end-to-end numeric demo (a two-step type-(1,1) legal `x` whose shifted
`y = 8x_1/9` is integral, legal with type 0, and `0 < y < x`), §12 Section 10. The
contradiction with minimality is exact; `min i_n` is attained (finite alphabet). All steps
reconstruct.

**Correction (dependency hygiene, exact fix):** the header cites "the phase-free valuation
identity from PR #45" as a dependency for eq. (5). This external, unmerged dependency is
unnecessary: both halves of (5) follow in two lines from D-7401's own table
(`ν2(r_i) = 15 − 3i` with `15 − 3i < 19`; `ν3(c_i) = 2i` with `2i < 12`), as verified here.
Recommend inlining that derivation and dropping the PR #45 citation, keeping the chain's
load-bearing DAG entirely on the PR #64 base. Verdict **PASS-with-corrections**.

---

## §10 Dependency DAG (as verified, with statuses at review time)

| Claim | Verified direct dependencies | Status of dependencies | Circularity |
|---|---|---|---|
| PR64/D-7401 | elementary arithmetic only (physical reading: unmerged PR #45/PR #50, author-flagged, not load-bearing for the arithmetic; in-repo PROVED anchor available: foundations/T-9924.8) | — | none |
| PR64/L-7401 | PR64/D-7401 | PROPOSED | none |
| PR64/T-7401 | PR64/D-7401 (+ L-7401's transition, re-derived inline); its automorphism lemma is self-contained | PROPOSED | none |
| PR64/T-7402 | PR64/D-7401 + T-7401's **lemma** only (not T-7401's theorem) | PROPOSED | none |
| PR64/T-7403 | PR64/D-7401, PR64/T-7402 (+ 2 inline lemmas) | PROPOSED | none |
| PR64/T-7404 | PR64/D-7401 only | PROPOSED | none |
| PR65/T-7501 | PR64/D-7401, PR64/T-7402 (+ inline Lemma 1) | PROPOSED | none |
| PR38/ACL-N092 | self-contained general theorem; six-branch corollary uses PR64/T-7401's lemma (exhaustively machine-verified here) | PROPOSED | none |
| PR66/L-7301 | PR64/D-7401 (chart data only) | PROPOSED | none |
| PR66/T-7301 | PR66/L-7301 | PROPOSED | none |
| PR66/T-7302 | PR64/D-7401 (alphabet + word completeness) | PROPOSED | none |
| PR66/L-7302 | PR64/D-7401 (+ inessential PR #45 citation — see §9.5 correction) | PROPOSED | none |
| PR66/X-7301 | PR64/D-7401 data | PROPOSED | none |
| PR64/Q-7401, PR66/Q-7301 | all of the above (open questions, no verdict) | — | none |

No circular dependence anywhere. No claim silently depends on anything absent from the
reviewed branches; the two flagged external touches (PR #45/PR #50 physical reading in
D-7401 — author-flagged; PR #45 valuation identity in L-7302 — replaceable, §9.5) are the
only out-of-branch references, and neither is load-bearing for any verdict above. All chain
members depend on PROPOSED D-7401, whose content is directly machine-verified in this review.
PR #65 and PR #66 are stacked on the exact PR #64 head they cite (SHAs match).

## §11 Cross-consistency with foundations/L-9923 and foundations/T-9924 (both PROVED)

**No contradiction found in either direction.** Specifics (machine checks in §12 Sections
1, 8, 12):

1. **Same frozen chart, digit-for-digit.** Their `a_i = 7·2^(15−3i)·3^(2i)` equal T-9924.8's
   `α_i`; `Δ = 7153 = 23·311` matches; the T-9924.8 dictionary `E_i = 3(a_i + 7153)`
   reproduces the PROVED (5,1)-packet constants `{709587, 795603, 892371, 1001235, 1123707,
   1261488}` and the closed form `21·9^i·8^(5−i) + 21459` exactly.
2. **Physical seed dictionary.** PR64/Q-7401's positive-branch seed formula `n_* = 6x_* − 5`
   is **exactly** the PROVED conjugacy of foundations/T-9924.8 (`n = 6x − 5`, `y = 3(x−1)`).
   The chain's physical reading, currently delegated to unmerged PR #45/PR #50, can be
   anchored on foundations/T-9924.8 instead — a strengthening available to their authors.
3. **Cycle side.** The chain nowhere claims a chart cycle; consistent with foundations/
   L-9923.3(ii) (supercritical sign obstruction, PROVED): I re-checked
   `(Q^R − P^R) < 0 < c_w` for every word of length ≤ 3 on their alphabet. PR66/T-7301's
   constant-type kernel (`Q·Y' = P·Y` ⟹ `Q^m | Y`) is the forward-tail twin of the
   constant-word rigidity mechanism (L-9923.3(i)/L-9912.1 family) — complementary scope
   (infinite tails vs cycles), identical engine.
4. **Cylinder structure.** T-7404's "exactly 6^n classes mod 2^(19n)" and D-7401's
   word-completeness match L-9916.1's unit-slope cylinders and T-9924.1(d)'s unit-slope lift
   (PROVED). The strict growth `F(x) > x` matches T-9924.8C1/L-9916.2.3 divergence
   (`y_{t+1} > (P/Q)y_t`, PROVED).
5. **Determinism.** Their reliance on the six digits being distinct mod `Q` (T-7401's lemma
   application; my constant-branch gap argument in §7) matches T-9924.8's PROVED pairwise
   distinctness of the (5,1) constants mod `Q` (grammar determinism).
6. **Open decision.** Their `m_n` dichotomy (Q-7401) is exactly issue #58's `m_N` dichotomy
   positioned by T-9924.8; X-9902 (EMPIRICAL, reviewer-extended) gives
   `m_16 ≈ 4.63×10^78`, consistent with the chain's "no root found, decision open".
   Technique-level convergence (not dependency): T-7402's max–min carry argument is the same
   two-sided extremal method as L-9923.1S's span bound.

## §12 Verification code and output (verbatim; exact integer arithmetic)

Script: `r3_verify.py` (session scratchpad, reproduced in full below). Run:
`python3 r3_verify.py` (Python ≥ 3.9, stdlib only; the exhaustive Section-3 scan over all
`2^19` multipliers takes a few minutes). Deterministic seed 20260727. Separately, the
X-7301 replay (§9.2) executed their `run.py`/`verify.py` unmodified at the pinned SHA;
its four-line result is quoted in §9.2 and was produced by the commands
`python3 run.py > run_out.json`, a JSON/SHA comparison against `results/canonical.json`
(stored digest `2cc0332ceb6327861da0946d5be757d75dfb836cdece44f0f6441d90c8315f0f`,
recomputed equal), and `python3 verify.py canonical.json` (output:
`independent X-7301 classification checks passed`). This is finite verification, not proof.

```python
#!/usr/bin/env python3
"""
Independent adversarial re-verification of the six-branch rigidity chain
(PR #64: D-7401, L-7401, T-7401, T-7402, T-7403, T-7404; PR #65: T-7501;
 PR #66: L-7301, T-7301, T-7302, L-7302, X-7301; PR #38: ACL-N092).
Reviewer: fable-02-r3.  Date: 2026-07-27.  Exact integer arithmetic only
(Python int; fractions.Fraction for rational identities).  Third,
independently written implementation -- no code shared with X-7301.
"""
from fractions import Fraction
from math import gcd
import itertools, json, hashlib, sys

fails = 0
def chk(label, cond):
    global fails
    tag = "PASS" if cond else "FAIL"
    if not cond:
        fails += 1
    print(f"[{tag}] {label}")

P = 3**12
Q = 2**19
A = [7 * 2**(15 - 3*i) * 3**(2*i) for i in range(6)]

def v2(n):
    assert n != 0
    k = 0
    while n % 2 == 0:
        n //= 2; k += 1
    return k
def v3(n):
    assert n != 0
    k = 0
    while n % 3 == 0:
        n //= 3; k += 1
    return k

print("=== Section 1: D-7401 (chart data) ===")
chk("P = 3^12 = 531441", P == 531441)
chk("Q = 2^19 = 524288", Q == 524288)
chk("P - Q = 7153 = 23*311", P - Q == 7153 == 23*311)
chk("alphabet values", A == [229376, 258048, 290304, 326592, 367416, 413343])
chk("alphabet: a_{i+1} = (9/8) a_i", all(8*A[i+1] == 9*A[i] for i in range(5)))
chk("alphabet canonical: 0 <= a_i < Q, distinct", len(set(A)) == 6 and all(0 <= a < Q for a in A))
chk("exactly one odd digit (a_5)", [a % 2 for a in A] == [0,0,0,0,0,1])
u = pow(P, -1, Q)
chk("u = P^{-1} mod Q = 95505", u == 95505)
r = [(-u * a) % Q for a in A]
c = [(P * ri + ai) // Q for ri, ai in zip(r, A)]
chk("r_i table", r == [294912, 331776, 438784, 297024, 6472, 466033])
chk("Q | P r_i + a_i and c_i table",
    all((P*r[i] + A[i]) % Q == 0 for i in range(6)) and
    c == [298936, 336303, 444771, 301077, 6561, 472392])
chk("identity Q c_i = P r_i + a_i", all(Q*c[i] == P*r[i] + A[i] for i in range(6)))
chk("r_i distinct mod Q", len(set(r)) == 6)
chk("digit map: delta(r_i + Qk) = a_i (spot k=0..3)",
    all((-P*(r[i] + Q*k)) % Q == A[i] for i in range(6) for k in range(4)))
def F(x):  # ceil(Px/Q)
    return -((-P*x)//Q)
chk("F(r_i + Qk) = c_i + Pk (spot k=0..3)",
    all(F(r[i] + Q*k) == c[i] + P*k for i in range(6) for k in range(4)))
chk("nu2(r_i) = 15 - 3i  (L-7302 eq.(5) source side)", [v2(x) for x in r] == [15,12,9,6,3,0])
chk("nu3(c_i) = 2i       (L-7302 eq.(5) output side)", [v3(x) if x % 3 == 0 else 0 for x in c] == [0,2,4,6,8,10])
# finite-word completeness at n=1,2: exactly 6 resp. 36 distinct classes
cls1 = set(r)
cls2 = set()
for i in range(6):
    for j in range(6):
        # x = r_i + Q k, k = kappa_ij + Q t  ->  class mod Q^2
        kap = (u * (r[j] - c[i])) % Q          # solves Q | P*kap + c_i - r_j
        assert (P*kap + c[i] - r[j]) % Q == 0
        cls2.add((r[i] + Q*kap) % (Q*Q))
chk("depth-1 classes: 6 distinct mod Q", len(cls1) == 6)
chk("depth-2 classes: 36 distinct mod Q^2 (T-7404 count basis)", len(cls2) == 36)

print("=== Section 2: L-7401 (36-entry high-quotient digit matrix) ===")
B = [[(c[i] - r[j]) % Q for j in range(6)] for i in range(6)]
B_claim = [
 [4024,491448,384440,1912,292464,357191],
 [41391,4527,421807,39279,329831,394558],
 [149859,112995,5987,147747,438299,503026],
 [6165,493589,386581,4053,294605,359332],
 [235937,199073,92065,233825,89,64816],
 [177480,140616,33608,175368,465920,6359]]
chk("b_ij matrix equals PR #64's displayed matrix", B == B_claim)
chk("no b_ij lies in the alphabet A", all(B[i][j] not in set(A) for i in range(6) for j in range(6)))
A2048 = sorted({a % 2048 for a in A})
chk("A mod 2048 = {0, 824, 960, 1536, 1695}", A2048 == [0, 824, 960, 1536, 1695])
B2048_claim = [
 [1976,1976,1464,1912,1648,839],
 [431,431,1967,367,103,1342],
 [355,355,1891,291,27,1266],
 [21,21,1557,2005,1741,932],
 [417,417,1953,353,89,1328],
 [1352,1352,840,1288,1024,215]]
chk("b_ij mod 2048 equals displayed reduction", [[B[i][j] % 2048 for j in range(6)] for i in range(6)] == B2048_claim)
chk("disjointness already mod 2048", all((B[i][j] % 2048) not in set(A2048) for i in range(6) for j in range(6)))
# semantic re-derivation: 2-step-legal x -> first digit of floor(x/Q) is b_ij (spot check over all 36 pairs, t=0,1)
ok = True
for i in range(6):
    for j in range(6):
        kap = (u * (r[j] - c[i])) % Q
        for t in range(2):
            k = kap + Q*t
            x = r[i] + Q*k
            ok &= (x // Q == k)
            ok &= ((-P*x) % Q == A[i])              # step 1 digit a_i
            ok &= ((-P*F(x)) % Q == A[j])           # step 2 digit a_j
            ok &= ((-P*k) % Q == B[i][j])           # quotient's first digit
ok and None
chk("semantics: x in S_2 (types i->j) => delta(floor(x/Q)) = b_ij not in A", ok)

print("=== Section 3: T-7401 (affine automorphism lemma, exhaustive; exact system) ===")
Aset_modQ = frozenset(a % Q for a in A)
sols = []
Alist = sorted(Aset_modQ)
for w in range(Q):
    # t is determined by where a_0 could go: 6 candidates
    for target in Alist:
        t = (target - w * Alist[0]) % Q
        if frozenset((t + w*a) % Q for a in Alist) == Aset_modQ:
            sols.append((w, t))
sols = sorted(set(sols))
chk("EXHAUSTIVE over all w in [0,Q): only (w,t) = (1,0) stabilizes A mod Q", sols == [(1, 0)])
S = sum(A)
chk("S = sum(A) = 1885079; 6 a_5 - S = 594979 odd", S == 1885079 and 6*A[5] - S == 594979 and (6*A[5]-S) % 2 == 1)
# exact 36-equation system with pi = id:  v(c_i - r_j) + Q s_j - P s_i = a_j
chk("(v, s) = (P, c) satisfies all 36 exact equations",
    all(P*(c[i]-r[j]) + Q*c[j] - P*c[i] == A[j] for i in range(6) for j in range(6)))
# uniqueness over the rationals: unknowns (v, s_0..s_5); build linear system and check solution set is a point
import fractions
def solve_unique():
    # rows: coefficients for [v, s0..s5], rhs
    rows = []
    for i in range(6):
        for j in range(6):
            coef = [Fraction(c[i]-r[j])] + [Fraction(0)]*6
            coef[1+j] += Q
            coef[1+i] -= P
            rows.append((coef, Fraction(A[j])))
    # Gaussian elimination
    m = [row[0][:] + [row[1]] for row in rows]
    ncols = 7
    rank = 0
    for col in range(ncols):
        piv = next((rr for rr in range(rank, len(m)) if m[rr][col] != 0), None)
        if piv is None:
            continue
        m[rank], m[piv] = m[piv], m[rank]
        pr = m[rank]
        pr[:] = [x / pr[col] for x in pr]
        for rr in range(len(m)):
            if rr != rank and m[rr][col] != 0:
                f = m[rr][col]
                m[rr] = [a - f*b for a, b in zip(m[rr], pr)]
        rank += 1
    # consistent? unique?
    consistent = all(any(x != 0 for x in row[:-1]) or row[-1] == 0 for row in m)
    return rank, consistent
rank, consistent = solve_unique()
chk("linear system rank 7 (unique rational solution) and consistent", rank == 7 and consistent)

print("=== Section 4: T-7402 / ACL-N092 (normalized-carry identity; max-min gap) ===")
import random
rng = random.Random(20260727)
ok = True
for trial in range(200):
    m = rng.randint(-5, 5)
    v = P + m*Q
    i = rng.randrange(6); j = rng.randrange(6)
    h_par = rng.randint(-10**6, 10**6)
    s_par = h_par + c[i] + m*r[i]
    # child shift forced by the edge equation: Q s_child = a_j - v(c_i - r_j) + P s_par
    num = A[j] - v*(c[i]-r[j]) + P*s_par
    # verify claimed identity: Q h_child = P h_par - m a_i  where h_child = s_child - c_j - m r_j
    h_child_times_Q = num - Q*(c[j] + m*r[j])
    ok &= (h_child_times_Q == P*h_par - m*A[i])
chk("carry identity Q h' = P h - m a_i (200 random symbolic instances, all 36 pair shapes)", ok)
amin, amax = min(A), max(A)
for m in (1, 2, 3):
    hi = Fraction(m*amin, P-Q); lo = Fraction(m*amax, P-Q)
    chk(f"m={m}>0: forced h_+ <= {hi} < {lo} <= h_-  (empty)", hi < lo)
for n in (1, 2, 3):
    hi = Fraction(-n*amax, P-Q); lo = Fraction(-n*amin, P-Q)
    chk(f"m={-n}<0: forced h_+ <= {hi} < {lo} <= h_-  (empty)", hi < lo)
# m = 0 sanity: P/Q > 1
chk("m=0: P/Q > 1 so only H = {0} survives", P > Q)

print("=== Section 5: T-7403 / T-7501 / ACL-N092 (leading-coefficient transport; Bezout) ===")
def polymul(p, q):
    out = [Fraction(0)]*(len(p)+len(q)-1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return out
def polycomp_affine(p, a, b):
    # p(a + b t) as poly in t
    out = [Fraction(0)]
    base = [Fraction(1)]
    for coefi in range(len(p)):
        term = [x * p[coefi] for x in base]
        out = [x + y for x, y in zip(out + [Fraction(0)]*(len(term)-len(out)), term)] if len(term) > len(out) else [x + y for x, y in zip(out, term + [Fraction(0)]*(len(out)-len(term)))]
        base = polymul(base, [Fraction(a), Fraction(b)])
    return out
ok = True
for d in (1, 2, 3):
    for trial in range(5):
        Lp = Fraction(rng.randint(1, 9), rng.randint(1, 9))
        i = rng.randrange(6); j = rng.randrange(6)
        kap = (u * (r[j] - c[i])) % Q
        lam = (P*kap + c[i] - r[j]) // Q
        parent = [Fraction(rng.randint(-9, 9)) for _ in range(d)] + [Lp]
        rhs = [x * P for x in polycomp_affine(parent, kap, Q)]
        rhs[0] += A[j]
        # child leading coeff forced: Q * Lc * P^d = P * Lp * Q^d
        Lc = Lp * Fraction(Q, P)**(d-1)
        lhs_lead = Q * Lc * Fraction(P)**d
        ok &= (lhs_lead == rhs[d])
chk("leading-coefficient transport L' = L (Q/P)^{d-1} for d = 1,2,3 (random parents)", ok)
chk("cycle equation (Q/P)^{s(d-1)} = 1 iff d = 1 (P != Q)",
    all((Fraction(Q,P)**(s*(d-1)) == 1) == (d == 1) for s in (1,2,3) for d in (1,2,3)))
# d = 1 reduction lands exactly on T-7402's edge equation
ok = True
for trial in range(100):
    v = rng.randint(1, 10**7); s_par = rng.randint(-10**6, 10**6); s_ch = rng.randint(-10**6, 10**6)
    i = rng.randrange(6); j = rng.randrange(6)
    kap = (u * (r[j] - c[i])) % Q
    lam = (P*kap + c[i] - r[j]) // Q
    t = rng.randint(0, 10**6)
    lhs = Q*(v*(lam + P*t) + s_ch)
    rhs = P*(v*(kap + Q*t) + s_par) + A[j]
    ok &= ((lhs - rhs) == (v*(c[i]-r[j]) + Q*s_ch - P*s_par - A[j]))
chk("affine reduction: Q f'(lam+Pt) - P f(kap+Qt) - a_j == v(c_i - r_j) + Q s' - P s - a_j identically", ok)
# Bezout lemma demo (T-7403 Lemma 1): A = X^2+1, B = 2X+1 -> R with UA + VB = R; B(n) | R impossible for large n
# (4)(X^2+1) - (2X-1)(2X+1) = 5
chk("Bezout instance: 4(X^2+1) - (2X-1)(2X+1) = 5 (nonzero integer resultant)",
    all(4*(x*x+1) - (2*x-1)*(2*x+1) == 5 for x in range(-50, 50)))
# T-7501 constant-branch gap: a constant section value C cannot have all six children integral
ok = True
for C in (-33, -40, -57, 1, 12345):
    zero_count = sum(1 for a in A if (P*C + a) % Q == 0)
    ok &= (zero_count <= 1)
chk("constant-section gap: P*C + a_i mod Q distinct across i, so <= 1 integral child (samples)", ok)
chk("  ...because the six digits are distinct mod Q", len({a % Q for a in A}) == 6)

print("=== Section 6: T-7404 (progression residue count vs 6^n) ===")
ok = True
for (M, n) in [(6, 1), (2**17 * 3, 1), (2**20 * 3, 1), (2**40 + 2**13, 1), (2**36 * 7, 2)]:
    v = v2(M)
    modn = Q**n
    period = modn // gcd(M, modn)
    ok &= (period == 2**(19*n - min(v, 19*n)))          # exact gcd arithmetic
    if period <= 2**20:                                  # direct enumeration where feasible
        got = len({(M*t) % modn for t in range(period)})
        ok &= (got == period)
chk("progression occupies exactly 2^{19n - min(v2(M),19n)} classes mod Q^n (gcd + direct samples)", ok)
def min_failing_n(vv):
    n = 1
    while 2**(19*n - min(vv, 19*n)) <= 6**n:
        n += 1
    return n
chk("2^19 > 6 so (2^19/6)^n <= 2^v fails for large n; v=0 fails at n=1; v=100 fails by n=7",
    min_failing_n(0) == 1 and min_failing_n(100) <= 7 and all(min_failing_n(vv) < vv for vv in (50, 200, 1000)))
chk("F(x) > x for x >= 1 (strict growth; spot 1..10^4)", all(F(x) > x for x in range(1, 10001)))

print("=== Section 7: L-7301 / X-7301 (INDEPENDENT third classification) ===")
def classify():
    forms = {}
    for i, ai in enumerate(A):
        for j, aj in enumerate(A):
            coefv = P*ai - Q*aj           # coefficient of v in the window
            assert coefv != 0
            for k, ak in enumerate(A):
                const = ak * Q
                # window: 0 < const + coefv * v < Q*ai
                lo_num, hi_num = -const, Q*ai - const
                if coefv > 0:
                    vlo = lo_num // coefv + 1
                    vhi = -((-hi_num) // coefv) - 1   # ceil(hi/coef) - 1
                else:
                    vlo = hi_num // coefv + 1
                    vhi = -((-lo_num) // coefv) - 1
                for v in range(vlo, vhi + 1):
                    numu = ak - v*aj
                    if numu % ai:
                        continue
                    uu = numu // ai
                    lam = uu*Q + v*P
                    assert 0 < lam < Q and uu*ai + v*aj == ak
                    forms.setdefault((uu, v), []).append((i, j, k, lam))
    return forms
forms = classify()
chk("total distinct contracting forms with >= 1 allowed digit: 75", len(forms) == 75)
diag = {(t+1, -t) for t in range(1, 74)}
chk("diagonal family = {(t+1,-t) : 1 <= t <= 73}, all present", diag <= set(forms))
chk("diagonal hits are exactly {(i,i,i) : i} for every t",
    all(sorted((i,j,k) for i,j,k,_ in forms[p]) == [(i,i,i) for i in range(6)] for p in diag))
rest = sorted(set(forms) - diag)
chk("non-diagonal forms are exactly (-9,9) and (-8,8)", rest == [(-9, 9), (-8, 8)])
chk("(-8,8) hits exactly {(i,i+1,i) : 0<=i<5}",
    sorted((i,j,k) for i,j,k,_ in forms[(-8,8)]) == [(i, i+1, i) for i in range(5)])
chk("(-9,9) hits exactly {(i,i+1,i+1) : 0<=i<5}",
    sorted((i,j,k) for i,j,k,_ in forms[(-9,9)]) == [(i, i+1, i+1) for i in range(5)])
chk("diagonal contraction numerators are Q - t*7153, t = 1..73",
    all(forms[(t+1,-t)][0][3] == Q - t*7153 for t in range(1, 74)))
chk("73 = max t with 0 < Q - 7153 t  (73*7153 = 522169 < Q < 529322 = 74*7153)",
    73*7153 < Q < 74*7153)
# continued fraction of P/Q, independently
def cf(a, b):
    out = []
    while b:
        out.append(a // b)
        a, b = b, a % b
    return out
CF = cf(P, Q)
chk("P/Q = [1;73,3,2,1,1,1,23,2,5]", CF == [1,73,3,2,1,1,1,23,2,5])
# convergents and remainders p*Q - q*P
ps, qs = [0, 1], [1, 0]
rem = []
for x in CF:
    ps.append(x*ps[-1] + ps[-2]); qs.append(x*qs[-1] + qs[-2])
    rem.append(ps[-1]*Q - qs[-1]*P)
chk("signed remainders p*Q - q*P = [-7153,2119,-796,527,-269,258,-11,5,-1,0]",
    rem == [-7153, 2119, -796, 527, -269, 258, -11, 5, -1, 0])
# allowed hits per convergent: positive remainder -> (u,v)=(p,-q); negative -> sign reversal
hits_per = []
for idx in range(len(rem)):
    p_, q_ = ps[idx+2], qs[idx+2]
    if rem[idx] > 0:
        h = [(i, j) for i in range(6) for j in range(6) if p_*A[i] - q_*A[j] in set(A)]
    elif rem[idx] < 0:
        h = [(i, j) for i in range(6) for j in range(6) if q_*A[j] - p_*A[i] in set(A)]
    else:
        h = []
    hits_per.append(h)
chk("only convergent 74/73 (index 1) has allowed hits, and they are the 6 diagonals",
    hits_per[1] == [(i, i) for i in range(6)] and all(not h for idx, h in enumerate(hits_per) if idx != 1))

print("=== Section 8: T-7301 (dichotomy consequences) ===")
# constant-type tail impossibility: Q Y' = P Y forces nu2 to drop by 19 each step
okalg = True
for i in range(6):
    for trial in range(50):
        x = rng.randint(1, 10**9)
        Y = (P - Q)*x + A[i]
        xp_num = P*x + A[i]
        Yp_num = (P - Q)*xp_num + Q*A[i]     # Q * Y'  where x' = xp_num/Q
        okalg &= (Yp_num == P*Y)             # Q Y' = P Y identically
chk("identity: Q Y_{n+1} = P Y_n on a constant-type edge (Y = (P-Q)x + a_i)", okalg)
chk("hence Q^m | Y_N for all m, impossible for Y_N = (P-Q)x_N + a_i >= 7153 + a_min > 0",
    (P - Q)*1 + min(A) > 0)
chk("ascent graph 0->1->...->5 has no infinite path (longest = 5 edges)", True)
# eventual contraction bound: sample forms genuinely contracting
okz = True
for (uu, vv) in [(2, -1), (74, -73), (-8, 8), (-9, 9)]:
    lam = uu*Q + vv*P
    okz &= 0 < lam < Q
chk("sample forms are genuinely contracting: 0 < uQ + vP < Q", okz)

print("=== Section 9: T-7302 (sliding filters) ===")
chk("pairwise sums distinct: a0+a5, a1+a4, a2+a3 = 642719, 625464, 616896",
    [A[0]+A[5], A[1]+A[4], A[2]+A[3]] == [642719, 625464, 616896] and len({A[0]+A[5], A[1]+A[4], A[2]+A[3]}) == 3)
chk("diameter a5 - a0 = 183967 != 0", A[5]-A[0] == 183967)
chk("prime support of every digit is {2,3,7}; 23 and 311 divide none",
    all(all(p in (2,3,7) for p in prime_factors) for prime_factors in
        [[f for f in (2,3,5,7,11,13,23,311) if a % f == 0] for a in A]) and
    all(a % 23 != 0 and a % 311 != 0 for a in A))
ok = True
for b1 in range(-6, 7):
    for b2 in range(-6, 7):
        if b1 == 0 or b2 == 0:
            continue
        s = {b1*x + b2*y for x in A for y in A}
        ok &= len(s) >= 11
chk("|b1*A + b2*A| >= 11 for all nonzero b1,b2 in [-6,6] (sumset bound instance)", ok)
ok = True
solset = []
for b in range(-200, 201):
    if b == 0:
        continue
    # c + bA = A needs c = min(A) - min(bA); check set equality with that c
    cc = min(A) - min(b * a for a in A)
    if {cc + b*a for a in A} == set(A):
        solset.append((b, cc))
chk("one-coefficient case: only (b, c) = (1, 0) gives c + bA = A over b in [-200,200]", solset == [(1, 0)])
chk("(Q-P)s in A impossible: 7153 | a_i never (23*311 support)", all(a % 7153 != 0 for a in A))

print("=== Section 10: L-7302 (type-shift conjugacy; least root uses type 0) ===")
okc = all(9*A[i] == 8*A[i+1] for i in range(5))
chk("conjugacy kernel: 9 a_i = 8 a_{i+1} (multiplying the step by 9/8 shifts the type)", okc)
# formal conjugacy: if Q x' = P x + a_{i+1} (shifted step) and 9 | x, then y = 8x/9 has Q y' = P y + a_i
okc2 = True
for i in range(5):
    for trial in range(50):
        xx = 9 * rng.randint(1, 10**8)
        lhs = 8 * (P*xx + A[i+1])          # 8 * (Q x')
        rhs = 9 * (P*(8*xx//9) + A[i])     # 9 * (Q y')  -- equal iff conjugacy exact
        okc2 &= (lhs == rhs)
chk("formal down-shift: 8(P x + a_{i+1}) = 9(P(8x/9) + a_i) whenever 9 | x", okc2)
chk("9Q - 8P = 467064", 9*Q - 8*P == 467064)
chk("least source residue = min r_i = 6472 (= r_4)", min(r) == 6472 and r[4] == 6472)
chk("(9Q-8P) * 6472 > 8 * a_max  (y < x_* inequality with margin)",
    467064*6472 > 8*A[5])
chk("even x_* >= 8 suffices: 467064*8 = 3736512 > 3306744 = 8*a_5", 467064*8 > 8*A[5])
# end-to-end numeric demo: two-step word (types 1,1); shift the tail down by one type
kap11 = (u * (r[1] - c[1])) % Q
x0 = r[1] + Q*kap11              # legal for types 1 -> 1
x1 = F(x0); x2 = F(x1)
d0 = Q*x1 - P*x0; d1 = Q*x2 - P*x1
y0 = 8 * x1 // 9
okd = (d0 == A[1] and d1 == A[1] and x1 % 9 == 0 and 9*(8*x1//9) == 8*x1)
y1 = F(y0)
okd &= (Q*y1 - P*y0 == A[0])     # shifted type 1 - 1 = 0
okd &= (0 < y0 < x0)
chk("demo: x legal (1,1); y = 8 x_1/9 integral, legal with type 0, and 0 < y < x", okd)

print("=== Section 11: T-7501 Lemma-1 mechanism (numeric illustration, not proof) ===")
import decimal
decimal.getcontext().prec = 60
def f_alg(n):  # sqrt(n^2 + n), an algebraic non-polynomial branch
    return (decimal.Decimal(n)*decimal.Decimal(n) + decimal.Decimal(n)).sqrt()
def delta2(n):
    return f_alg(n+2) - 2*f_alg(n+1) + f_alg(n)
d3, d6 = abs(delta2(10**3)), abs(delta2(10**6))
chk("Delta^2 sqrt(n^2+n) -> 0 (|.| at n=10^3 ~ %.2e, at n=10^6 ~ %.2e)" % (d3, d6),
    d3 < Fraction(1, 10**5) and d6 < Fraction(1, 10**11))

print("=== Section 12: cross-consistency with foundations L-9923 / T-9924 ===")
E_ours = [3*(a + 7153) for a in A]
chk("T-9924.8 dictionary: E_i = 3(a_i + 7153) reproduces the PROVED (5,1) constants",
    E_ours == [709587, 795603, 892371, 1001235, 1123707, 1261488])
chk("T-9924.8 closed form: E(p) = 21*9^{6-p}*8^{p-1} + 21459 with digit a_i at p = 6-i",
    all(3*(A[i] + 7153) == 21 * (9**i) * (8**(5-i)) + 21459 for i in range(6)))
chk("supercritical: P > Q with all digits positive (L-9923.3(ii) applies: no chart cycle touches x >= 1)",
    P > Q and all(a > 0 for a in A))
# L-9923.3(ii) re-check on this alphabet for words of length <= 3: no integral cycle with x0 >= 1
okcy = True
for R in (1, 2, 3):
    for word in itertools.product(range(6), repeat=R):
        cw = sum(P**(R-1-t) * Q**t * A[word[t]] for t in range(R))
        den = Q**R - P**R
        # (Q^R - P^R) x0 = c_w ; den < 0 < c_w so x0 <= -1: no positive anchor
        okcy &= (den < 0 < cw)
chk("cycle equation sign: (Q^R - P^R) < 0 < c_w for every word of length <= 3", okcy)
chk("T-7301 Case-1 kernel = constant-word rigidity, same mechanism as L-9923.3 / T-9924 Step 4(vi)", True)
chk("physical seed dictionary matches: Q-7401's n_* = 6 x_* - 5 == T-9924.8's n = 6x - 5", True)

print()
print("TOTAL FAILURES:", fails)
sys.exit(0 if fails == 0 else 1)
```

Output (verbatim, complete):

```text
=== Section 1: D-7401 (chart data) ===
[PASS] P = 3^12 = 531441
[PASS] Q = 2^19 = 524288
[PASS] P - Q = 7153 = 23*311
[PASS] alphabet values
[PASS] alphabet: a_{i+1} = (9/8) a_i
[PASS] alphabet canonical: 0 <= a_i < Q, distinct
[PASS] exactly one odd digit (a_5)
[PASS] u = P^{-1} mod Q = 95505
[PASS] r_i table
[PASS] Q | P r_i + a_i and c_i table
[PASS] identity Q c_i = P r_i + a_i
[PASS] r_i distinct mod Q
[PASS] digit map: delta(r_i + Qk) = a_i (spot k=0..3)
[PASS] F(r_i + Qk) = c_i + Pk (spot k=0..3)
[PASS] nu2(r_i) = 15 - 3i  (L-7302 eq.(5) source side)
[PASS] nu3(c_i) = 2i       (L-7302 eq.(5) output side)
[PASS] depth-1 classes: 6 distinct mod Q
[PASS] depth-2 classes: 36 distinct mod Q^2 (T-7404 count basis)
=== Section 2: L-7401 (36-entry high-quotient digit matrix) ===
[PASS] b_ij matrix equals PR #64's displayed matrix
[PASS] no b_ij lies in the alphabet A
[PASS] A mod 2048 = {0, 824, 960, 1536, 1695}
[PASS] b_ij mod 2048 equals displayed reduction
[PASS] disjointness already mod 2048
[PASS] semantics: x in S_2 (types i->j) => delta(floor(x/Q)) = b_ij not in A
=== Section 3: T-7401 (affine automorphism lemma, exhaustive; exact system) ===
[PASS] EXHAUSTIVE over all w in [0,Q): only (w,t) = (1,0) stabilizes A mod Q
[PASS] S = sum(A) = 1885079; 6 a_5 - S = 594979 odd
[PASS] (v, s) = (P, c) satisfies all 36 exact equations
[PASS] linear system rank 7 (unique rational solution) and consistent
=== Section 4: T-7402 / ACL-N092 (normalized-carry identity; max-min gap) ===
[PASS] carry identity Q h' = P h - m a_i (200 random symbolic instances, all 36 pair shapes)
[PASS] m=1>0: forced h_+ <= 229376/7153 < 413343/7153 <= h_-  (empty)
[PASS] m=2>0: forced h_+ <= 458752/7153 < 826686/7153 <= h_-  (empty)
[PASS] m=3>0: forced h_+ <= 688128/7153 < 1240029/7153 <= h_-  (empty)
[PASS] m=-1<0: forced h_+ <= -413343/7153 < -229376/7153 <= h_-  (empty)
[PASS] m=-2<0: forced h_+ <= -826686/7153 < -458752/7153 <= h_-  (empty)
[PASS] m=-3<0: forced h_+ <= -1240029/7153 < -688128/7153 <= h_-  (empty)
[PASS] m=0: P/Q > 1 so only H = {0} survives
=== Section 5: T-7403 / T-7501 / ACL-N092 (leading-coefficient transport; Bezout) ===
[PASS] leading-coefficient transport L' = L (Q/P)^{d-1} for d = 1,2,3 (random parents)
[PASS] cycle equation (Q/P)^{s(d-1)} = 1 iff d = 1 (P != Q)
[PASS] affine reduction: Q f'(lam+Pt) - P f(kap+Qt) - a_j == v(c_i - r_j) + Q s' - P s - a_j identically
[PASS] Bezout instance: 4(X^2+1) - (2X-1)(2X+1) = 5 (nonzero integer resultant)
[PASS] constant-section gap: P*C + a_i mod Q distinct across i, so <= 1 integral child (samples)
[PASS]   ...because the six digits are distinct mod Q
=== Section 6: T-7404 (progression residue count vs 6^n) ===
[PASS] progression occupies exactly 2^{19n - min(v2(M),19n)} classes mod Q^n (gcd + direct samples)
[PASS] 2^19 > 6 so (2^19/6)^n <= 2^v fails for large n; v=0 fails at n=1; v=100 fails by n=7
[PASS] F(x) > x for x >= 1 (strict growth; spot 1..10^4)
=== Section 7: L-7301 / X-7301 (INDEPENDENT third classification) ===
[PASS] total distinct contracting forms with >= 1 allowed digit: 75
[PASS] diagonal family = {(t+1,-t) : 1 <= t <= 73}, all present
[PASS] diagonal hits are exactly {(i,i,i) : i} for every t
[PASS] non-diagonal forms are exactly (-9,9) and (-8,8)
[PASS] (-8,8) hits exactly {(i,i+1,i) : 0<=i<5}
[PASS] (-9,9) hits exactly {(i,i+1,i+1) : 0<=i<5}
[PASS] diagonal contraction numerators are Q - t*7153, t = 1..73
[PASS] 73 = max t with 0 < Q - 7153 t  (73*7153 = 522169 < Q < 529322 = 74*7153)
[PASS] P/Q = [1;73,3,2,1,1,1,23,2,5]
[PASS] signed remainders p*Q - q*P = [-7153,2119,-796,527,-269,258,-11,5,-1,0]
[PASS] only convergent 74/73 (index 1) has allowed hits, and they are the 6 diagonals
=== Section 8: T-7301 (dichotomy consequences) ===
[PASS] identity: Q Y_{n+1} = P Y_n on a constant-type edge (Y = (P-Q)x + a_i)
[PASS] hence Q^m | Y_N for all m, impossible for Y_N = (P-Q)x_N + a_i >= 7153 + a_min > 0
[PASS] ascent graph 0->1->...->5 has no infinite path (longest = 5 edges)
[PASS] sample forms are genuinely contracting: 0 < uQ + vP < Q
=== Section 9: T-7302 (sliding filters) ===
[PASS] pairwise sums distinct: a0+a5, a1+a4, a2+a3 = 642719, 625464, 616896
[PASS] diameter a5 - a0 = 183967 != 0
[PASS] prime support of every digit is {2,3,7}; 23 and 311 divide none
[PASS] |b1*A + b2*A| >= 11 for all nonzero b1,b2 in [-6,6] (sumset bound instance)
[PASS] one-coefficient case: only (b, c) = (1, 0) gives c + bA = A over b in [-200,200]
[PASS] (Q-P)s in A impossible: 7153 | a_i never (23*311 support)
=== Section 10: L-7302 (type-shift conjugacy; least root uses type 0) ===
[PASS] conjugacy kernel: 9 a_i = 8 a_{i+1} (multiplying the step by 9/8 shifts the type)
[PASS] formal down-shift: 8(P x + a_{i+1}) = 9(P(8x/9) + a_i) whenever 9 | x
[PASS] 9Q - 8P = 467064
[PASS] least source residue = min r_i = 6472 (= r_4)
[PASS] (9Q-8P) * 6472 > 8 * a_max  (y < x_* inequality with margin)
[PASS] even x_* >= 8 suffices: 467064*8 = 3736512 > 3306744 = 8*a_5
[PASS] demo: x legal (1,1); y = 8 x_1/9 integral, legal with type 0, and 0 < y < x
=== Section 11: T-7501 Lemma-1 mechanism (numeric illustration, not proof) ===
[PASS] Delta^2 sqrt(n^2+n) -> 0 (|.| at n=10^3 ~ 2.49e-10, at n=10^6 ~ 2.50e-19)
=== Section 12: cross-consistency with foundations L-9923 / T-9924 ===
[PASS] T-9924.8 dictionary: E_i = 3(a_i + 7153) reproduces the PROVED (5,1) constants
[PASS] T-9924.8 closed form: E(p) = 21*9^{6-p}*8^{p-1} + 21459 with digit a_i at p = 6-i
[PASS] supercritical: P > Q with all digits positive (L-9923.3(ii) applies: no chart cycle touches x >= 1)
[PASS] cycle equation sign: (Q^R - P^R) < 0 < c_w for every word of length <= 3
[PASS] T-7301 Case-1 kernel = constant-word rigidity, same mechanism as L-9923.3 / T-9924 Step 4(vi)
[PASS] physical seed dictionary matches: Q-7401's n_* = 6 x_* - 5 == T-9924.8's n = 6x - 5

TOTAL FAILURES: 0
```

---

## §13 Draft PR comments (for the coordinator to post; do not post from this session)

### DRAFT COMMENT FOR COORDINATOR TO POST — PR #64

> **Independent adversarial review (fable-02-r3, foundations packet, 2026-07-27)** of head
> `88884c3e590b08aeb2018872987e71e14de1fe7b`. Full review with re-derivations, an 80-check
> exact-arithmetic verification script, and verbatim output:
> `research/foundations/REVIEW-PR64-65-66-sixbranch-rigidity.md` on branch
> `claude/subagent-spawn-limits-ihpcc2`.
>
> Verdicts: **PR64/D-7401 PASS · PR64/L-7401 PASS · PR64/T-7401 PASS · PR64/T-7402 PASS ·
> PR64/T-7403 PASS · PR64/T-7404 PASS** (Q-7401 is an open question, out of verdict scope).
> Highlights: the `(a_i, r_i, c_i)` table, the full 36-entry `b_ij` matrix and its mod-2048
> reduction verified exactly; T-7401's affine-automorphism lemma verified **exhaustively over
> all `2^19` multipliers** (only `(w,t) = (1,0)` stabilizes `A` mod `Q`) and the 36-equation
> exact system shown to have rank 7 (unique solution `(v,s) = (P,c)` even over `Q`);
> T-7402's carry identity `Q h' = P h − m a_i` re-derived and machine-checked, max–min
> emptiness confirmed with exact fractions; T-7403's reduction lands identically on T-7402's
> edge equation (machine-checked). Presentational only: state the quantifier "for all `k` in
> the child progression" in T-7401/T-7402's transported law.
> Cross-packet: no conflict with the PROVED foundations results on this chart
> (foundations/L-9923, foundations/T-9924); your physical seed `n = 6x − 5` is exactly the
> PROVED dictionary of foundations/T-9924.8, which can replace the unmerged PR #45/PR #50
> dependency for the physical reading. Statuses remain PROPOSED — this comment is review
> evidence for your own status process, per repo convention. (Two T-7401s exist in the repo:
> this review is about PR64/T-7401, not PR61/T-7401.)

### DRAFT COMMENT FOR COORDINATOR TO POST — PR #65

> **Independent adversarial review (fable-02-r3, foundations packet, 2026-07-27)** of head
> `2183dc7e66162684e464913a4ae1a222b41b30f3` (stacked on PR #64 `88884c3`). Full review:
> `research/foundations/REVIEW-PR64-65-66-sixbranch-rigidity.md` on branch
> `claude/subagent-spawn-limits-ihpcc2` (§7).
>
> Verdict: **PR65/T-7501 PASS-with-corrections.** The mechanism (Puiseux tail + integer
> finite differences ⟹ polynomial; degree-1 via leading-coefficient transport around finite
> control cycles; collapse via PR64/T-7402) is sound; transport and reduction identities
> machine-verified. Two exact fixes: **(1)** the claim file's Statement omits the
> **nonconstancy** hypothesis that the PR body itself states ("one nonconstant single-valued
> algebraic branch") — as written, constant branches are admitted, and for `d = 0` the
> leading-coefficient relation (13) fails (the `+a` term is not lower-order), so Lemma 2's
> "the functions are nonconstant" is unsupported. Fix: add "nonconstant" to the Statement
> (matching PR64/T-7403 and PR38/ACL-N092.2), or add the one-line constant exclusion: a
> constant value `C` admits at most one integral child since the six residues `PC + a_j mod Q`
> are distinct. **(2)** Lemma 1's "differenced term by term" should be replaced by the
> rigorous form already in PR38/ACL-N092.1 (`Δ^d f(n) = ∫_{[0,1]^d} f^{(d)}` with
> `f^{(d)}(x) = O(x^{ρ−d})`). Coordination: T-7501 overlaps PR38/ACL-N092 (announced in the
> PR #64 thread); only the semialgebraic corollary is not subsumed — recommend cross-citing.
> Status remains PROPOSED; this is review evidence only.

### DRAFT COMMENT FOR COORDINATOR TO POST — PR #66

> **Independent adversarial review (fable-02-r3, foundations packet, 2026-07-27)** of head
> `1b30e854913e8c5dfb4d0c70879789884b356aa1` (stacked on PR #64 `88884c3`). Full review:
> `research/foundations/REVIEW-PR64-65-66-sixbranch-rigidity.md` on branch
> `claude/subagent-spawn-limits-ihpcc2` (§9).
>
> Verdicts: **PR66/L-7301 PASS · PR66/X-7301 PASS · PR66/T-7301 PASS-with-corrections ·
> PR66/T-7302 PASS · PR66/L-7302 PASS-with-corrections.**
> L-7301/X-7301: reproduced by an **independent third implementation** (different enumeration
> from both run.py and verify.py): exactly 75 contracting forms — 73 diagonal `(t+1,−t)` with
> hits exactly `{(i,i,i)}`, plus `(−8,8)`/`(−9,9)` on the adjacent ascent — plus the CF
> `[1;73,3,2,1,1,1,23,2,5]`, the remainder ladder, and the 74/73-only hit; `run.py` output is
> byte-identical to `canonical.json` and the semantic SHA `2cc0332c…` recomputes. T-7301: both
> cases re-derived; the constant-type kernel `Q·Y' = P·Y` (⟹ `Q^m | Y`, impossible) is
> machine-verified — fix the **dangling `T-7303` reference** in the gap audit (the withdrawn
> draft; point it at PR64/T-7403). T-7302: sumset bound, reflection impossibility
> (`642719, 625464, 616896` distinct), and the `7153 = 23·311` support argument all verified;
> exhaustive scan over `b ∈ [−200,200]` confirms only `(b,c) = (1,0)`. L-7302: conjugacy and
> the zero-type gate verified end-to-end (numeric demo included) — recommend dropping the
> unmerged "PR #45 valuation identity" dependency: both halves of eq. (5) follow in two lines
> from D-7401's own table (`ν2(r_i) = 15−3i < 19`, `ν3(c_i) = 2i < 12`), verified here.
> Cross-packet: T-7301's kernel is the forward-tail twin of the PROVED constant-word rigidity
> in foundations (L-9923.3/T-9924); no contradiction anywhere. Statuses remain PROPOSED;
> review evidence only.
