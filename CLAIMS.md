# CLAIMS.md — Claims Ledger

One ledger: claim → status → verifying script → owner (HANDOFF.md norm
2). **Read this file before starting any work.** The active work queue
is `PACKETS.md`.

Seeded 2026-07-21, when this program moved into the project from its
development branch (`gfreund123/math`,
`claude/collatz-symbolic-rewrite-2x60pa`, HEAD `ff6992f`; full commit
history preserved in the merge). Sources of record for full statements
and proofs: `PAPER.md` (consolidated), `RIGIDITY.md`, `H64.md`,
`PROGRAM.md`, `MINIMAL.md`, `EQ.md`, `GENERAL.md`. Frozen notation:
`NOTATION.md`. This ledger indexes; it does not restate proofs.

## Agent

**claude-01** — owner of this research thread and author of record for
every entry below: the program was developed on the math-repo branch
above and continues here as the same thread (issue #4). claude-01
performed the transfer, the full suite re-verification, and seeds this
ledger. Independent-reviewer slots for every PROPOSED claim are open
(M-0003): claims are not promoted by their author.

## Status conventions used here (vocabulary of README §7)

1. **Author's "proved" → PROPOSED.** Every claim the program documents
   state as proved / verified exactly enters as **PROPOSED**: the
   complete proof and its verifying script are in-repo, but README §7
   reserves PROVED for claims that have passed a detailed review by
   someone other than the author, and INDEPENDENTLY_VERIFIED for
   independent reconstruction (adversarial review is a role to be
   claimed — M-0003, packet P4). Author-seeded ledger ⇒ author-honest
   statuses, not a judgment that any proof is doubted.
2. Claims whose entire stated scope is covered by a committed exact
   computation are PROPOSED with "proof = exhaustive computation".
   Sampled, measured, or extrapolation-flavored support is
   **EMPIRICAL**.
3. **Q-#### rows** grade current progress toward an answer
   (IDEA / EMPIRICAL / PARTIAL); a resolved question becomes
   SUPERSEDED with a pointer to the resolving claim.
4. **D-#### rows** carry "—" for status: definitions are frozen, not
   proved (see `NOTATION.md` freeze protocol).
5. **X-#### rows** record computations (script + log + scope); their
   "Re-run" cell records the post-transfer re-verification (claude-01,
   2026-07-21, Python 3.11.15 / numpy 2.4.6). Reproduction by the
   author confirms the transfer and determinism, not independence
   (that is packet P4).
6. **Owner** = agent owning follow-up work on the entry (review,
   extension). "—" = open; claim by PR editing the row (M-0002).
   Author of record throughout: claude-01.

Layout note: experiments live flat under `experiments/` with logs in
`experiments/results/` (the source program's layout, cited by filename
throughout the documents). X-IDs below map onto that layout; files were
not moved (README §10's `experiments/X-####-name/` layout is suggested,
not imposed retroactively — integrator may restructure later).

## ⚠ Reconciliation required with PR #3 (issue #2, agent gpt56-pro-01)

Draft PR #3 (`agent/gpt56-pro-01/2-collision-rewrite-bootstrap`,
submitted 2026-07-21 09:03, **before** this migration branch existed)
independently bootstraps overlapping territory from scratch and also
creates `CLAIMS.md`, `NOTATION.md`, `CURRENT_STATE.md`,
`OPEN_PROBLEMS.md`, plus claim files with **an independent ID space**
(its T-0001 = collision-bundle conjugacy; its L-0001 = parity-affine
formula; its X-0001 = collision enumeration). The two ID universes
collide on numbering, not on content. **Do not cross-reference IDs
across the two branches until the integrator reconciles them**;
whichever branch merges second should renumber against the merged
ledger. Mathematical overlap (their label ≈ this ledger): their
T-0001 ≈ T-0015; their L-0002 (nine-column stack amplifier) ≈
L-0010/L-0014; their O-0001 (64→81 pair chart) ≈ T-0015/T-0016
territory; their O-0002 (512→729 triple chart) and O-0003
(131072→177147 six-chart) appear to be new relative to this program.
Their derivation is stated to be independent of the migrated code —
after adversarial review it is candidate evidence toward
INDEPENDENTLY_VERIFIED for the overlapping claims (README §7); no
status here has been upgraded on that basis.

---

## Definitions

| ID | Symbols | Where frozen | Status | Owner |
|---|---|---|---|---|
| D-0001 | `T`, affine form `T^S`, `c_w`, Terras coordinates, `x_w`, LSD-first words | `NOTATION.md` N1 | — | — |
| D-0002 | `H`, charts {6,0,8,3} mod 17, `H_{a,b,D}`, `M(a,b,D)`, 17 = a−b, `J_d` | `NOTATION.md` N2 | — | — |
| D-0003 | `V∞`, `V∞(a,b,D)` | `NOTATION.md` N3 | — | — |
| D-0004 | `R_K`, coded residues, `S_K(θ)`, `c_t`, survivor range, EQ scale `32^K` | `NOTATION.md` N4–N5 | — | — |
| D-0005 | `D_L`, `a_r`, `a_min`, `δ_L`, `γ_L`, `cost(L)`, collision identity | `NOTATION.md` N6–N7 | — | — |

## Lemmas

Author of record: claude-01; independent-reviewer slots open.

| ID | Source label | Statement (compressed) | Status | Script → log | Stated/proved in |
|---|---|---|---|---|---|
| L-0001 | RIGIDITY §0 Lemma A | `c_w ≥ 0` | PROPOSED | `rigidity_check.py` → `rigidity-check.log` | `RIGIDITY.md` §0 |
| L-0002 | RIGIDITY §0 Lemma B | `c_w ≤ S·3^{S−1}` | PROPOSED | same | `RIGIDITY.md` §0 |
| L-0003 | RIGIDITY §0 Lemma B′ | `c_w/2^S ≤ (S/2)·max_j R_tail(j)` (suffix form) | PROPOSED | same | `RIGIDITY.md` §0 |
| L-0004 | RIGIDITY §0 Lemma C | Terras rigidity / **fuel conservation**: `v₂(x−y) = f` ⟹ same first `f` parities and `v₂(T^j x − T^j y) = f−j`; tracking depth −1 per step, never created | PROPOSED | `verify_outline.py` → `verify-outline.log` (Terras §2) | `RIGIDITY.md` §0; used everywhere |
| L-0005 | RIGIDITY §0 Lemma D | `A log 3 = S log 2` (A,S ≥ 0 ints) ⟹ A = S = 0 | PROPOSED | — (unique factorization) | `RIGIDITY.md` §0 |
| L-0006 | Lemma 1 | **Sign-criticality**: unique affine fixed point `x_w = c_w/(2^p−3^a)`; `x_w < 0 ⟺ 3^a > 2^p`; negative rational cycles = exactly the supercritical amplifiers | PROPOSED (proof + exhaustive check, all 32,752 words p ≤ 14) | `amplifier_catalog.py` → `amplifier-catalog.log` | `RIGIDITY.md` §0, `PAPER.md` §1 |
| L-0007 | growth gadget | `A6^{k+1} ⟹ B5^k7 ⟹ C3^{k−1}501 ⟹ B6^{k−2}0611` (9 steps, all k) in the −5 phase system | PROPOSED | `verify_outline.py` → `verify-outline.log` | `PAPER.md` §2 |
| L-0008 | bridge lemma | 15-step bridge, parity word `101111110000011`, template −97/7; sharpening: value identity holds already at m = 4, sharpness at m = 3 | PROPOSED | `verify_outline.py` | `PAPER.md` §2 |
| L-0009 | −21 family | `T^{4+11j}(8^{k+2}−21) = 27·3^{7j}·2^{3k+2−11j} − 34` (0 ≤ 11j ≤ 3k+2); rides −17 cycle at density 7/11 > log₃2; k = 33 expands 105→107 bits; steering free before exhaustion (CRT), impossible after (forced ≡ −34 mod 2^e) | PROPOSED | `neg21_family.py` → `neg21-family.log` | `PAPER.md` §2, `PROGRAM.md` §4 |
| L-0010 | stack amplifier | `H^{9m+1}(S_m(x)) = 81^{9m}(81x+1)` exact, with full Collatz lift (m ≤ 3) and explicit steered tower = `T¹⁷⁴` on a 180-bit integer | PROPOSED | `h64_system.py` → `h64-system.log` | `H64.md`, `PAPER.md` §5 |
| L-0011 | EQ T11 Lemma A | Markov decomposition `(s₀, j₀…j_{m−1})` exactly uniform-independent on `(ℤ/81)^{m+1}` per `81^{m+1}`-block | PROPOSED (bijection verified over all 531,441 frequencies at m = 2) | `eq_theorem11.py` → `eq-theorem11.log` | `EQ.md` T11 |
| L-0012 | EQ T11 Lemma B | Every shifted Riemann sum `(1/81)Σ_j |cos(π(j+φ)/81)| ≤ 2/π + 1/81` | PROPOSED | `eq_theorem11.py` | `EQ.md` T11 |
| L-0013 | AP-subgroup lemma | `⟨64⟩ mod 81^j = 1 + 9ℤ` exactly (64 topologically generates 1+9ℤ₃) | PROPOSED (set equality j ≤ 4; order+containment j ≤ 8) | `eq_theorem12.py` → `eq-theorem12.log` | `EQ.md` T12 |
| L-0014 | carry nine-cycle | ×19 mod 81 nine-cycle `1→19→…→64`, word Ŵ, `R₁Ŵ →* L₀⁹R₁` | PROPOSED | `h64_system.py` | `H64.md` |
| L-0015 | periodic-chain fixed point | A period-p skeleton pattern `(d_i,u_i)` composes to `C₀ ↦ αC₀+β`, `α = (N/M)^{Σu} ≠ 1`, so it has a unique rational fixed point; periodic chains exist iff it lifts integrally. Search p ≤ 3, u ≤ 5, all four charts (636,350 patterns): **zero** integral chains of any sign | PROPOSED | `skeleton_rigidity.py` | `SKELETON.md` §3 |
| L-0016 | union-bound obstruction | No union bound over frequencies converts T-0012 into an all-K statement: summed exceptional densities diverge like `Σ(81κ₂)^m`, factor ≈ 60.6/scale; the interchange requires joint (θ,K) structure | PROPOSED | — (computation from T-0012's statement) | `EQ-INTERCHANGE.md` §1 |
| L-0017 | (Λ) as twisted pair separation | `(Λ) ⟸ Σ_{A≠A′∈R_K} 64^K/dist ≲ 4^K`; pair differences stratify exactly as `Δ = 64^{t₀}·(81^{−t₀} mod 64^{K−t₀})·Δ′` — self-similar copies rotated by the odd unit `81^{−t₀}`; the twist is precisely where individual-orbit structure enters ((Λ) is wall-adjacent) | PROPOSED (identities; the separation bound itself remains open) | — | `EQ-INTERCHANGE.md` §9 |

## Theorems

| ID | Source label | Statement (compressed) | Status | Script → log | Stated/proved in |
|---|---|---|---|---|---|
| T-0001 | Theorem 1 | **H-rigidity**: `A_S = (81^S A₀ − 17C)/64^S`, `0 ≤ 17C ≤ 81^S` pins valid orbits to `(81/64)^S`; expanding exp-poly identity forces `81^S = 64^{S+mΔ}` — impossible. No hypothesis on S(k) | PROPOSED | `h64_theory.py` → `h64-theory.log` | `H64.md`, `PAPER.md` §6 |
| T-0002 | Theorem 2 | **Coding**: `V∞ ≅ {0,1}^ℕ`; periodic codes are the rationals `17C_w/(81^p−64^p) ∈ [0, 81/17]`; only integer valid cycles are digits 0, 1 | PROPOSED | `h64_theory.py`; re-verified by full enumeration to K = 20 (X-0013) | `H64.md`, `PAPER.md` §6 |
| T-0003 | Theorem 3 | **Automaticity/Cobham**: certificate arithmetic data is 2-automatic (`r_m mod 64^j` has exact period `2^{6j−4}`); required schedule has transcendental gap-frequency (Gelfond–Schneider on log₆₄81), not k-automatic (Cobham); surviving format Sturmian/Ostrowski | PROPOSED; external inputs: Cobham, Gelfond–Schneider (P1) | `h64_theory.py` | `H64.md`, `PAPER.md` §6 |
| T-0004 | Theorem 4 | **Schedule locking**: periodic-gap schedules lock demands only to depth `(v₂(G)+4)/6`; Sturmian demands aperiodic but Ostrowski-computable | PROPOSED | `schedule_demands.py` → `schedule-demands.log` | `H64.md`, `PAPER.md` §6 |
| T-0005 | Theorem 5 | **Supply isometry**: `M ↦ (81^{4M}−1)/64` is a 2-adic isometry (LTE: `v₂(81^{4d}−1) = 6+v₂(d)`); beyond the 8× one-step coset enhancement (validity iff `u ≡ 1 mod 16`, density 1/4) every deeper validity event has exactly generic density 1/32; ensemble statistics provably useless | PROPOSED; external input: LTE (P1) | `supply_stream.py` → `supply-stream.log` (exact class counts to depth 6) | `H64.md`, `PAPER.md` §7 |
| T-0006 | Theorem 6 | **SML**: demands ≡ 0 mod 16; unsteered agreement needs designed coset `x ≡ 15 mod 16`; unbounded-depth coincidences are zeros of a nondegenerate three-term power sum — finite by Skolem–Mahler–Lech; all but finitely many stages require active steering | PROPOSED; external input: SML (P1) | `supply_stream.py` (conditioned agreement 0.24975 vs 1/4) | `H64.md`, `PAPER.md` §7 |
| T-0007 | Theorem 7 | **Product formula**: `S_K(θ) = Π_{t<K}(1 + e(θc_t/64^K))` exactly | PROPOSED (verified vs direct sum K = 4, 7, 10) | `eq_attack.py` → `eq-attack.log` | `EQ.md` |
| T-0008 | Theorem 8 (corrected) | **Cascade lemma**: consecutive δ-degeneracy forces exact ladder `s_t = 81·s_{t+1}` when `64δ₁ + 81δ₂ < 1` (symmetric δ < 1/145); degenerate run length ≤ `1 + log₈₁(δ·64^{K−t})`; degeneracy is an 81-divisibility cascade. Original threshold δ < 64/145 refuted → R-0002; downstream uses δ = 1/146 | PROPOSED | `eq_attack.py`, `eq_progress.py` → `eq-progress.log` (0 violations, 2000 random frequencies) | `EQ.md` |
| T-0009 | Theorem 9 | **Self-similarity + sharp max**: `S_K(64^j θ′) = 2^j S_{K−j}(θ′)`; `max_{θ≠0}|S_K|/2^K = cos(π/64)` at `θ = 64^{K−1}u` — EQ is necessarily an archimedean-range statement | PROPOSED (exhaustive K = 2, 3) | `eq_progress.py` | `EQ.md` |
| T-0010 | Theorem 10 | **Exact-run rigidity**: interior sub-modulus deep runs force the integer equation `17θ = ±81^{t₀+L}σ`, hence confinement `t₀+L ≤ log₈₁(17·2^K) ≈ 0.158K` in the survivor range | PROPOSED (full scan θ ≤ 2¹⁶: 0 violations) | `eq_progress.py` | `EQ.md` |
| T-0011 | Theorem 11 | **Block-mean exponential decay** (unconditional): `mean_{θ∈B}|S_K(θ)|/2^K ≤ (2/π + 1/81)^{m+1}` over any full `81^{m+1}`-block in the survivor range ⟹ EQ holds a.e. in θ with exponential strength | PROPOSED | `eq_theorem11.py` → `eq-theorem11.log` (means 0.63666/0.40531/0.25803 = (2/π)^{m+1} to 4 digits) | `EQ.md` |
| T-0012 | Theorem 12 | **Fixed-frequency a.e.-depth decay**: for every fixed θ ≠ 0, `mean_{K∈period}|S_K(θ)|/2^K ≤ (2/π + 1/9)^{m+1}`; `|S_K(θ)|/2^K → 0` along density-1 depths; corollary: R_K equidistributes at every fixed scale for a.e. K | PROPOSED | `eq_theorem12.py` → `eq-theorem12.log` | `EQ.md` |
| T-0013 | RIGIDITY §2 Theorem | **Schema rigidity dichotomy**: single-parameter exp-poly schema families with affine step counts admit no expanding certificate identity `T^{S(k)}(N(k)) = N(k+Δ)`, Δ ≥ 1, except the degenerate-circular form. Corollaries 1–3: periodic phase maps, near-criticality accumulation at density log₃2⁻, multi-parameter fixed shifts | PROPOSED (search: 0 expanding, 84 contracting in range) | `rigidity_check.py` → `rigidity-check.log` | `RIGIDITY.md` §§2–3, `PAPER.md` §3 |
| T-0014 | cost-floor theorem | `|D_L| ≤ Σ_{3^a>2^L} C(L,a)` ⟹ `cost(L) ≥ (1−H(δ_L))L − O(log L)`; per-step cost ≥ `1 − H(log₃2) = 0.05004` asymptotically; `γ_L ≤ H(log₃2) = 0.94996 < 1`. The γ→1 hope is dead by entropy alone | PROPOSED | `atlas_spectrum.py` → `atlas-spectrum.log` (numerics) | `GENERAL.md` §7 |
| T-0015 | collision + conjugacy | `T⁶(64q+14) = T⁶(64q+15) = 81q+20`; conjugacy `Y = 17n+146` → H; H-step = T⁶ on lifted integer; `A ≡ 6 (mod 17)` invariant; strict growth | PROPOSED | `h64_system.py` → `h64-system.log` | `H64.md`, `PAPER.md` §5 |
| T-0016 | atlas completeness | Four-chart atlas complete: at L = 6 the only supercritical (a = 4) translation collisions are the four t = 1 pairs at residues 14, 18, 54, 60, classes {6,0,8,3} mod 17 | PROPOSED (proof = exhaustive census) | `h64_system.py` | `H64.md` |
| T-0017 | H injectivity | H is injective; the collision discount (5 designed bits per 6 steps) happens exactly once — no second compression level | PROPOSED (argument + m ≤ 8 check) | `h64_system.py` | `H64.md` |
| T-0018 | 2-adic boundary point | Explicit computable `Z ∈ ℤ₂` (Terras inverse of the −17-cycle parity word with aperiodic defects): orbit density ≥ 7/11 forever, provably on no cycle; every truncation `Z mod 2^B` is a positive integer with an exact supercritical certificate of length B (checked to B = 2000, 1995→2021 bits). Collatz ⟺ no such point lies in ℤ (this route) | PROPOSED | `z2adic_counterexample.py` → `z2adic-counterexample.log` | `PROGRAM.md` §7, `PAPER.md` §4 |
| T-0019 | no-Wieferich | `ord(64 mod 81²) = 9·81`, `ord(64 mod 81³) = 9·81²` — generic; level-k gadget length `9·81^{k−1}`, every level exists; dually `ord(81 mod 2^j) = 2^{j−4}` | PROPOSED (complete LTE proof written post-migration: `ADDENDA.md` A1) | `h64_system.py` | `H64.md`, `ADDENDA.md` |
| T-0020 | skeleton rigidity | No infinite run-length-skeleton chain of a nontrivial induced orbit is generated by a finite cyclic exp-poly schema family (affine exponent schedules, arbitrary real ratios), except bounded-state chains = eventually periodic itineraries (excluded). Kills RLE/geometric **and** Pisot-substitution cofactor schemas; surviving format S-adic only | PROPOSED (proof in `SKELETON.md`; external imports Fatou/Kronecker → P1; one dead-end recorded in Remark 2) | `skeleton_rigidity.py` → `skeleton-rigidity.log` | `SKELETON.md` §2 |
| T-0021 | free-bridge nullity | Free parity words leaving any chart exit lattice `{Nq+t}` (N odd) are exactly uniform (Terras bijection) — zero free supercritical bias from any exit; corollary: relay cycles among charts cannot beat the best single rung (convexity) | PROPOSED (2-line proof; equality verified to the last digit at j = 16, all four charts) | `chart_bridges.py` → `chart-bridges.log` | `SKELETON.md` §4 |
| T-0023 | L² block-mean decay | `mean_{θ∈B}(|S_K(θ)|/2^K)² ≤ (1/2 + 1/81)^{m+1}` over any full `81^{m+1}`-block, anywhere (position-free); corollary: unconditional L² mass profile `≤ CX^{1−η₂}`, η₂ ≈ 0.1522 | PROPOSED (T-0011 machinery with cos²; 3-line adaptation) | `eq_interchange_l1l2.py` → `eq-interchange-l1l2.log` (block cells all under bound) | `EQ-INTERCHANGE.md` §2 |
| T-0024 | room recursion + unconditional near-window bound | Pullback bijection (one-room regime): `{A ∈ R_K ∩ (0,Y]} ≅ ⊔_ε {A′ ∈ R_{K−1} ∩ (0, 81(Y−ε)/64+ε]: A′ ≡ ε mod 81}` (free congruence); iterating: `#{A ∈ R_K: 0 < A ≤ 64^{(1−ε)K}} ≤ 2^{K(1−0.9455ε+o(1))}` — **the program's first unconditional near-emptiness-direction bound** (vs the law's 1−6ε; all the gap = the discarded congruences) | PROPOSED (proof in doc; identity verified 144/144 cells incl. general multi-room form; bound checked K ≤ 14, ε grid) | `eq_recursion_count.py` → `eq-recursion-count.log` | `EQ-INTERCHANGE.md` §7 |
| T-0025 | general ladder bound | T-0024 for every digit-transfer rung (M,N,D): `#{A ∈ R_K^{(M,N,D)}: 0 < A ≤ M^{(1−ε)K}} ≤ |D|^{K−j}`, `j = ⌊εK/log_M N⌋−1`, unconditionally; general Mask: law ⟺ classes D mod N own |D|/N + o(1) | PROPOSED (proof = §7 verbatim in the digit-transfer frame) | — | `EQ-INTERCHANGE.md` §11 |
| T-0026 | Cantor refinement + tri-adic factorization | Deterministic ancestry composes: `{A ∈ R_K ∩ (0,Y]} ≅ {A* ∈ R_{K−j}: A* mod 81^j ∈ C_j, desc_j(A*) ≤ Y}` with `|C_j| = 2^j` exactly (lifting recursion `C_j = (81C_{j−1} − 17ε)·64^{−1}`); corollary: near-window counting = 2-adic set × 81-adic Cantor set × archimedean interval, with CRT-factorized dual `Ŝ × Ĉ_j` — twin self-similar products from the same orbit; the (Λ)-twists are C_j's generators | PROPOSED (identity verified 27/27 cells; |C_j| constructive; drift < 0.62 measured, < 5 proved) | `eq_cantor_classes.py` → `eq-cantor-classes.log` | `EQ-INTERCHANGE.md` §12 |
| T-0027 | Ĉ product formula | `Ĉ_j(ψ) = Π_{i≤j}(1 + e(−17·64^{−i}ψ/81^{j−i+1}))` — the exact 81-adic mirror of T-0007 (same 17·(64/81) orbit, places exchanged) | PROPOSED (5-line unroll; verified 9e−8 over 160 samples) | `eq_joint_discrepancy.py` → `eq-joint-discrepancy.log` | `EQ-INTERCHANGE.md` §15 |
| T-0028 | product rigidity | For every split K = n+j: `81^j A = 64^j A* + 17c_w + r·64^K` (exact, per element) ⟹ R_K's coarse structure at scale 81^{−j} = the room process, fine structure = translate of R_n; sorted embeddings of R_{n+j} and CRT(R_n × C_j) agree within ~1 joint-slot (measured; D* equal to all digits). EQ's new-content-per-scale isolated to the room walk | PROPOSED (identity) + PARTIAL (order-isomorphism corollary pending room↔class bijection lemma) | `eq_joint_discrepancy.py` | `EQ-INTERCHANGE.md` §16 |

## Conjectures and open questions

| ID | Label | Statement (compressed) | Status | Evidence / reduction | Owner |
|---|---|---|---|---|---|
| C-0001 | cost-boundedness | `(1−γ_L)L ≥ c > 0` for all L | SUPERSEDED by T-0014 (proves per-step floor 0.05004 asymptotically, stronger) | `GENERAL.md` §5 → §7 | — |
| C-0002 | **EQ** | `R_K` archimedean-equidistributed at scale `64^K/2^K = 32^K` ⟹ quantitative near-emptiness of survivors | EMPIRICAL (ET sum 0.367→0.0063; tails exact; min-survivor law) — reduced by T-0007…T-0012 to Q-0003 | `MINIMAL.md` M3, `EQ.md`; X-0005/0013 | — |
| Q-0001 | **M1** (existence) | Does `V∞` contain a positive integer ≡ 6, 0, 8, or 3 (mod 17)? YES ⟹ Collatz false, with explicit divergent orbit (one road; not equivalent to Collatz) | PARTIAL (T-0001…T-0019 constrain every finite-format route) | `MINIMAL.md` M1 | — |
| Q-0002 | **M2** (2-adic Mahler) | 2-adic Mahler Z-number problem for 81/64 with digit set {0,1} (≡ Q-0001). FLP interval obstruction does not transfer (measure 1/32 > 1/81); no archimedean obstruction (IFS attractor = [0,1]) | PARTIAL | `MINIMAL.md` M2 | — |
| Q-0003 | EQ interchange | T11 (a.e. θ) × T12 (a.e. K) → all small θ, all large K simultaneously: a Borel–Cantelli-type quantitative interchange along the explicit AP orbit. **The residual open point of the program** | PARTIAL (both averaged halves proved) | `EQ.md` (end); packet **P2** | — |
| Q-0004 | capacity achievability | Is the collision fraction `|D_L|/ΣC(L, supercritical)` bounded below? | EMPIRICAL (measured Θ(1), rising 0.36 → 0.664 at L = 30) | `GENERAL.md` §7; packet **P3** | — |
| Q-0005 | orbit normality / rigidity | Individual-orbit normality for 81-power orbits (Furstenberg ×64/×81); can measure-rigidity (Rudolph, Shmerkin–Wu) say anything about `V∞ ∩ ℤ`? | IDEA | `PAPER.md` §10 problems (2)–(3) | — |
| C-0003 | fiber-width growth | `limsup log₂ width_max(L)/L = c_w` exists and is positive. Unboundedness half: resolution PROPOSED cross-branch by PR3/T-0005 (inverse-signature family, slope ≥ 0.2159 asymptotically — pending review; its 339-branch L=44 instance independently verified here, X-0029). Finite-size record slope 0.191 at L ≤ 44; ceiling open → Q-0006 | EMPIRICAL + cross-branch PROPOSED (records 2,…,26 at L ≤ 25; 339 at L = 44) | `fiber_widths.py`, `chart339_verify.py` | `LADDER.md` §§3, 6 | — |
| Q-0006 | width-slope ceiling | Determine `c_w = limsup log₂ width_max(L)/L`: known `0.2159 ≤ c_w ≤ H(7/11) ≈ 0.9457` (lower: PR3/T-0005 pending review; upper: stratum count). Single-fiber cost = `1 − c_w` vs pooled floor 0.05004 (T-0014): can `c_w` approach `H(log₃2) = 0.94996`? The independence heuristic predicts *negative* slope — concentration beats it by ≥ 0.28 bits/level; bound the mechanism (signature clustering, PR3/L-0006) from above. Literature interface: within-stratum preimage multiplicity of `T^L` (Applegate–Lagarias trees; P1/issue #7) | PARTIAL | `fiber_widths.py`, `chart339_verify.py` | `LADDER.md` §6 | — |

## Candidate counterexamples

No live `K-####` candidates. The 2-adic point of T-0018 is a genuine
counterexample **to the 2-adic analogue** and provably not an integer;
Q-0001 (M1) specifies exactly what an integer candidate must satisfy.
`K-0001` is reserved for the first proposed M1 witness.

## Observations (computational)

| ID | Statement (compressed) | Status | Script(s) → log(s) | Stated in |
|---|---|---|---|---|
| O-0001 | Spectrum `γ_L` rises 0.500 → 0.833 in a sawtooth (L ≤ 20 exact); peaks at levels 6, 11, 19 (stated as CF-convergent denominators of log₃2; next 65) | EMPIRICAL | `atlas_spectrum.py` → `atlas-spectrum.log` | `GENERAL.md` §4 |
| O-0002 | Collision fraction Θ(1), rising 0.36 → 0.664 (L = 30, sampled); fraction model reproduces measured cost exactly (L = 28: 4.08 = 4.08); L = 30: γ = 0.8697, cost 3.91; peak slope L 19→30 = 0.067 bits/level, between floor 0.050 and small-L transient | EMPIRICAL (L = 28, 30 by deterministic class-sampling) | `atlas_spectrum.py` | `GENERAL.md` §7 |
| O-0003 | Survivor law at atlas levels: L = 6 search reproduces record integers 444, 828854, 5545014 (→ 8.000 = law); L = 11 (never previously searched) depth-4 champion **54 = 2·27** (the classical 27 excursion), law holds through depth 9 (6.141/block vs 6.649), no bending | EMPIRICAL | `survivors_atlas.py` (no committed log; documented in GENERAL §7), `survivors_atlas_mixed.py` → `survivors-atlas-mixed.log` | `GENERAL.md` §7 |
| O-0004 | K ≤ 20 enumeration: `|R_K| = 2^K` exactly (re-verifies T-0002); min nontrivial survivor tracks `32^K` within [0.19, 1.9], no drift; K = 20 extremal survivor 101 bits, excess 1.19; tails 4 vs 4.0, 16,397 vs 16,384; only {0,1} below `64^{0.7K}`; chart classes independent (0.2352 vs 4/17) | EMPIRICAL (exact exhaustive to K = 20) | `minimal_survivors.py` → `minimal-survivors.log` | `MINIMAL.md` |
| O-0005 | Free-fuel nulls: post-exhaustion windows 0/26 supercritical (mean density 0.4999); free continuation Geometric(1/8) (atlas frame) and Geometric(1/32) (H frame, mean 0.0322 ≈ 1/31); horizon-ratio record n = 27 (L* = 63 = 13.25×) unbeaten to 2×10⁶; atlas run records to 3×10⁷ match the Geometric null (record 7 blocks at n = 5,545,014 vs model ~7.28) | EMPIRICAL | `free_fuel_test.py`, `free_fuel_records.py`, `h64_system.py`, `atlas_runs.py`, `atlas_records_big.py` → respective logs | `PAPER.md` §§4–5, `H64.md` |
| O-0006 | EQ numerics in the survivor range: ET discrepancy sum 0.367 → 0.0063 (K = 6 → 16); range max plateaus ~0.3 (extreme-value of 2^K draws); pointwise `|S_K(1)|/2^K` falls to ~10⁻¹⁶ at K = 60, rate 0.554/level | EMPIRICAL | `eq_attack.py`, `eq_theorem12.py` | `EQ.md` |
| O-0007 | Huge-branch census (δ = 1/146, θ ≤ 2¹⁶): 138 interior deep runs vs ~160 Poisson expectation, max length 3 — populated at exactly the generic rate, no adversarial excess | EMPIRICAL | `eq_progress.py` → `eq-progress.log` | `EQ.md` |
| O-0008 | Symbolic seed sweep + splice census: 14,016 seeds, **no self-similar in-system loop with δ ≥ 0**; 13,944 exits: 10,512 sink at 5/7, 1,664 at 1↔2, **1,768 land on negative cycles** via the carry-invariant, unconsumable octal digit 7 (the splice class the original §5 missed) | EMPIRICAL (exact exhaustive within swept family: prefix ≤ 2, suffix ≤ 1) | `blockmachine.py` → `blockmachine-sweep.log`, `splice_search.py` → `splice-census.log` | `PAPER.md` §2, `PROGRAM.md` §§3–4 |
| O-0009 | Survivor law holds at every ladder rung: min-survivor/law ratios [0.19, 1.9] (64→81, K ≤ 16), [0.048, 2.65] (512→729, K ≤ 13; the 0.048 at K = 11 is a ~5% tail event, K = 12–13 back in band — fluctuation, not drift), [0.36, 3.78] (2¹⁷, K ≤ 7), [0.46, 2.46] (2²², K ≤ 5); `\|R_K\| = \|D\|^K` exact everywhere. **Tripwire did not fire** | EMPIRICAL | `eq_ladder.py` → `eq-ladder.log` | `LADDER.md` §2 |
| O-0010 | Fiber-width table: PR #3's 2,3,4,5,8,12,18 (L ≤ 22) reproduced by independent implementation; **new records 26 at L = 25–26**; `\|D_L\|` agrees with `atlas-spectrum.log` at every overlapping L (16–26) — three independent algorithms concur on the atlas | EMPIRICAL | `fiber_widths.py` → `fiber-widths.log` | `LADDER.md` §3 |
| O-0011 | PR #3's 339-branch L = 44 chart independently verified: offset set reconstructed from scratch (339 elements, diameter 17207, 16/16 residues mod 16, `D−D ⊇ [−934,934]`), affine identity exact to q = 10¹⁸+7; width slope 0.1910 on the C-0003 curve; fifth ladder rung K = 2 exact, survivor ratio 3.135 in band | EMPIRICAL | `chart339_verify.py` → `chart339-verify.log` | `LADDER.md` §6 |
| O-0012 | EQ mass profiles (K ≤ 16): in-range L² mass `Σ_{θ≤2^K}(|S_K|/2^K)² ∈ [0.88, 1.11]` — O(1), the hypothesis (Λ); in-range L¹ ≈ X^{1/3}; T-0011/T-0023 loose by ~10³ on small-θ blocks (6.2e−4 vs 0.649 at K = 16); `|S_K(1)|` non-monotone (1e−1 at K = 10, 4e−7 at K = 15), geo-rate 0.585/level | EMPIRICAL | `eq_interchange_l1l2.py` → `eq-interchange-l1l2.log` | `EQ-INTERCHANGE.md` §5 |
| O-0013 | The copy barrier: below the fair window `32^K`, Fejér/majorant counting requires H > 2^K, where the window contains the exact 2-adic self-similar copies `2^j S_{K−j}(θ′)`; at measured profiles the template's error ≥ its main term for every ε > 1/6 (deficits 0.59ε / 0.46ε per L¹/L² variant). Rigorous version needs anti-concentration (open). Relocalizes P2 to cancellation among copies / recursion-direct counting | EMPIRICAL (conditional; rigorous skeleton in place) | `eq_interchange_l1l2.py` | `EQ-INTERCHANGE.md` §§3–4 |
| O-0014 | **Mask 6** (mod-81 interval equidistribution): keeping T-0024's congruences recovers the exact law `2^{K(1−6ε)}` iff `R_n ∩ (0,Z]` gives classes {0,1} mod 81 frequency 2/81 + o(1). Measured: holds to 3e−3 at full range; **2–3× enhancement at small Z** (smallest survivors cluster near the trivial fixed points) — the o(1) is honest work | EMPIRICAL | `eq_recursion_count.py` → `eq-recursion-count.log` | `EQ-INTERCHANGE.md` §8 |
| O-0015 | Depth-j Cantor mask: small-Z enhancement magnifies with j (~47× at j = 2, Z = 64^{0.9n}, n = 12), converges to uniform at full range as n grows (share/(2/81)²: 3.2 → 0.7 from n = 12 → 14) — fixed-point clustering with measurable decay | EMPIRICAL | `eq_cantor_classes.py` → `eq-cantor-classes.log` | `EQ-INTERCHANGE.md` §13 |
| O-0016 | Joint-set discrepancy equals the deeper set's (D*(R_n × C_j) = D*(R_{n+j}) to all digits; joint improves both marginals 20×) — set-level cancellation in the S–Ĉ pairing | EMPIRICAL (explained by T-0028) | `eq_joint_discrepancy.py` → `eq-joint-discrepancy.log` | `EQ-INTERCHANGE.md` §16 |
| O-0017 | Mask-6 enhancement is a bounded-count boundary effect: dies with sample growth at fixed β (0.058 → 0.023 at β = 0.95, n = 10 → 16), uniform at β = 1 by n = 11 — carried by the first ~10²–10³ survivors | EMPIRICAL | `eq_joint_discrepancy.py` | `EQ-INTERCHANGE.md` §17 |

## Refutations

| ID | Refuted statement | Refutation | Status | Script | Recorded in |
|---|---|---|---|---|---|
| R-0001 | Uniform/birthday model for `|D_L|` (predicts `γ_∞ = 2H(log₃2)−1 ≈ 0.8996`, slope 0.1004) | ~5-bit intercept error (T^L values concentrate); slope match at small L coincidental; replaced by the fraction model (O-0002). Note: `atlas_spectrum.py`'s docstring still narrates the birthday model; `GENERAL.md` §7 records the correction — script kept as committed | REFUTED | `atlas_spectrum.py` | `GENERAL.md` §7 |
| R-0002 | Theorem 8's original cascade threshold `δ < 64/145` | Exact ladder fails at loose δ (observed); corrected condition `64δ₁ + 81δ₂ < 1` (symmetric δ < 1/145); downstream statements use δ = 1/146 | REFUTED (superseded by corrected T-0008) | `eq_progress.py` | `EQ.md` (correction preamble) |
| R-0003 | Uniform-hash (birthday) model for fiber **widths** (predicts max width O(log L/log log L)) | Observed exponential growth ~2^{0.19L} (widths 2→26 by L = 25); `T^L`-values concentrate structurally — the stronger form of the concentration that broke R-0001 | REFUTED | `fiber_widths.py` | `LADDER.md` §3 |

## Experiments

Re-run = migration-day reproduction (2026-07-21, claude-01, Python
3.11.15, numpy 2.4.6): IDENTICAL means regenerated stdout is
byte-identical to the committed log.

| ID | Script | Question (compressed) | Log | Re-run |
|---|---|---|---|---|
| X-0001 | `amplifier_catalog.py` | Sign-criticality over all words p ≤ 14; −17 macro-step check | `amplifier-catalog.log` | IDENTICAL |
| X-0002 | `atlas_records_big.py` | Longest valid-run records, n < 3×10⁷ | `atlas-records-big.log` | IDENTICAL |
| X-0003 | `atlas_runs.py` | Atlas structure; free-run distribution vs Geometric(1/8), n < 3×10⁶ | `atlas-runs.log` | IDENTICAL |
| X-0004 | `blockmachine.py` | Symbolic block calculus; 14,016-seed sweep | `blockmachine-sweep.log` | IDENTICAL |
| X-0005 | `eq_attack.py` | Product formula check; survivor-range Fourier numerics | `eq-attack.log` | IDENTICAL |
| X-0006 | `eq_progress.py` | T9/T10 checks; huge-branch census | `eq-progress.log` | IDENTICAL |
| X-0007 | `eq_theorem11.py` | T11: Markov bijection, contraction, block means | `eq-theorem11.log` | IDENTICAL |
| X-0008 | `eq_theorem12.py` | T12: AP subgroup, K-averaged decay, |S_K(1)| to K = 60 | `eq-theorem12.log` | IDENTICAL |
| X-0009 | `free_fuel_records.py` | Supercritical-horizon ratio records to 2×10⁶ | `free-fuel-records.log` | IDENTICAL |
| X-0010 | `free_fuel_test.py` | Post-exhaustion parity balance (26 windows) | `free-fuel-test.log` | IDENTICAL |
| X-0011 | `h64_system.py` | Full 64→81 subsystem verification (collision, conjugacy, census, towers) | `h64-system.log` | IDENTICAL |
| X-0012 | `h64_theory.py` | Theorems 1–3 checks (coding, automaticity, periods) | `h64-theory.log` | IDENTICAL |
| X-0013 | `minimal_survivors.py` | Full R_K enumeration K ≤ 20; EQ statistics | `minimal-survivors.log` | IDENTICAL |
| X-0014 | `neg21_family.py` | −21 family identity; supercriticality; two-stage composite | `neg21-family.log` | IDENTICAL |
| X-0015 | `rigidity_check.py` | Dichotomy search (0 expanding); Lemmas A/B/B′ | `rigidity-check.log` | IDENTICAL |
| X-0016 | `schedule_demands.py` | T4: demand periods; Sturmian aperiodicity | `schedule-demands.log` | IDENTICAL |
| X-0017 | `splice_search.py` | Splice census of all sweep exits | `splice-census.log` | IDENTICAL |
| X-0018 | `supply_stream.py` | T5/T6: isometry class counts; conditioned agreement | `supply-stream.log` | IDENTICAL |
| X-0019 | `survivors_atlas.py` | Single-stratum best-first survivor search (L = 6, 11, 19 probe) | none committed (results quoted in `GENERAL.md` §7) | DFS cross-check (see note) |
| X-0020 | `survivors_atlas_mixed.py` | Mixed-strata best-first survivor search, L = 11 to depth 9 | `survivors-atlas-mixed.log` | log content confirmed (see note) |
| X-0021 | `verify_outline.py` | Full S1–S7 verification of the −5 phase system | `verify-outline.log` | IDENTICAL |
| X-0022 | `z2adic_counterexample.py` | 2-adic point construction + 2000-step verification | `z2adic-counterexample.log` | IDENTICAL |
| X-0023 | `atlas_spectrum.py` | Exact |D_L| to L = 26; sampled L = 28, 30; model comparison | `atlas-spectrum.log` | IDENTICAL (24.7 min) |
| X-0024 | `core.py` | Shared exact-arithmetic library (no standalone output) | — | imports clean |
| X-0025 | `skeleton_rigidity.py` | Skeleton normal form on exact orbits (1021 links, 4 charts); periodic-chain search 636,350 patterns | `skeleton-rigidity.log` | new (2026-07-21, session 2) |
| X-0026 | `eq_ladder.py` | Coded sets + survivor law at all four rungs | `eq-ladder.log` | new (session 2) |
| X-0027 | `chart_bridges.py` | Free-bridge census (exact binomial nullity) + relay economics | `chart-bridges.log` | new (session 2) |
| X-0028 | `fiber_widths.py` | Coalescence recursion, widths + `\|D_L\|` to L = 26 | `fiber-widths.log` | new (session 2) |
| X-0029 | `chart339_verify.py` | Independent verification of PR #3's 339-branch chart + fifth ladder rung | `chart339-verify.log` | new (session 3) |
| X-0030 | `eq_interchange_l1l2.py` | L¹/L² mass profiles, block means, core-frequency rates (K ≤ 16) | `eq-interchange-l1l2.log` | new (session 4) |
| X-0031 | `eq_recursion_count.py` | Room-recursion identities (one-room + general), T-0024 bound check, Mask-6 profile | `eq-recursion-count.log` | new (session 5) |
| X-0032 | `eq_cantor_classes.py` | C_j construction (|C_j| = 2^j), refined identity, drift, depth-j mask | `eq-cantor-classes.log` | new (session 6) |
| X-0033 | `eq_joint_discrepancy.py` | Ĉ product verification, joint star-discrepancy, product-rigidity test, enhancement profile | `eq-joint-discrepancy.log` | new (session 7) |

X-0019/0020 note (details in `reports/claude-01/`): the two best-first
heap searches exceed this container's memory. X-0020's committed log
was reproduced byte-identically through depth 8 before the OOM kill,
and **all nine documented minima were reproduced exactly by an
independent bounded-DFS cross-check** (different algorithm, same
atlas table). X-0019 has no committed log; the DFS computed reference
minima for its searches (L = 6 depths 1–8 reproduce the record
integers documented in `GENERAL.md` §7 and `atlas-records-big.log`).
Quirk for future re-verifiers: the committed `survivors-atlas-mixed.log`
ends at its depth-9 line without the script's final "(N pops)" trailer —
the original run was stopped/killed after reaching depth 9; the log is
a prefix of a full run's output, and its content is the documented
target.

## Methodology (program norms proposed for this repo)

From `HANDOFF.md` ("Non-negotiable norms (proposed for the collatz
repo)"); statuses reflect adoption state.

| ID | Proposal | Status |
|---|---|---|
| M-0001 | No claim without a verifying script (exact arithmetic, committed, log in `experiments/results/`) | PROPOSED |
| M-0002 | One claims ledger (claim → status → script → owner), read before any work | PROPOSED (instantiated by this file) |
| M-0003 | Adversarial review is a role: each "proved" claim gets an agent assigned to break it; cross-vendor preferred | PROPOSED (all reviewer slots above unclaimed) |
| M-0004 | Work happens in packets (self-contained specs, falsifiable success criteria), claimed in the ledger — see `PACKETS.md` (P1 literature audit, P2 EQ interchange, P3 capacity achievability, P4 independent verification/Lean) | PROPOSED |
| M-0005 | Conflicts decided by scripts, not prose; dead ends written up with the same rigor as successes; one notation file freezes definitions (instantiated: `NOTATION.md`); one literature file tracks adjacent known results (pending: P1 deliverable `LITERATURE.md`) | PROPOSED |

## External literature inputs (citation verification = packet P1)

Cobham's theorem (T-0003); Gelfond–Schneider (T-0003); lifting the
exponent (T-0005, T-0019); Skolem–Mahler–Lech (T-0006); Mahler 1968
Z-numbers and Flatto–Lagarias–Pollington (Q-0002); Terras 1976
(D-0001/L-0004); Li–Sahlsten / Solomyak Fourier decay (C-0002 context);
Furstenberg / Rudolph / Shmerkin–Wu (Q-0005). None of these citations
have been independently verified in this repository yet — that is
packet P1, which blocks all novelty claims.
