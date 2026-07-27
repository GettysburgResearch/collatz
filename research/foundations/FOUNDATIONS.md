# FOUNDATIONS.md — index of the 99xx foundations packet

Packet owner: fable-02 · Issue: #30 · Branch: `claude/subagent-spawn-limits-ihpcc2`
Created: 2026-07-22 · Status of this index: current as of the end of the fable-02 overnight session.

## What this packet is

A canonical, in-repo-proved layer of the *classical* load-bearing lemmas of Collatz research —
results that active branches previously imported from literature without proof (KTHM-xxxx
ledger) or re-proved piecemeal. Every file follows README §8 (full proof, dependency audit,
gap audit, adversarial tests, remaining uncertainty) and uses the shared notation in
[`NOTATION.md`](NOTATION.md) (D-9901–D-9910).

**Review provenance.** `PROVED` here means: authored by one prover agent, then passed a
detailed adversarial review by a *separate* verifier agent (fresh context; independent
reconstruction of every proof plus independent computational refutation attempts; README §13).
As of 2026-07-27 the packet holds **25 claim files (L-9901–L-9923, T-9924, L-9927), all
PROVED** after such review, plus L-9926 and T-9925 (both PROPOSED, verifiers assigned) and two
cross-branch review reports (PR #61; PRs #64/#65/#66 — see REVIEW-PR64-65-66-sixbranch-rigidity.md). An external cross-model
pass remains welcome and would justify `INDEPENDENTLY_VERIFIED`, which is set nowhere. No claim here is
`INDEPENDENTLY_VERIFIED` (reserved for cross-session/cross-model review). No file asserts any
resolution of the conjecture; conditional results say so prominently.

## Index

| ID | File | Status | Author / Reviewer | Headline |
|----|------|--------|-------------------|----------|
| L-9901 | [L-9901-map-equivalences.md](L-9901-map-equivalences.md) | **PROVED** | p1 / v1 | C, T, S orbits are equivalent (reaching 1, boundedness, cycles); every integer T-orbit is trivial-cycle, nontrivial-cycle, or divergent — with the pigeonhole step marked integer-only |
| L-9902 | [L-9902-parity-bijection.md](L-9902-parity-bijection.md) | **PROVED** | p2 / v2 | Terras bijection: residues mod 2^k ↔ parity words of length k; equivariance identity; two-lifts flip structure; bits i.i.d. uniform under uniform residues |
| L-9903 | [L-9903-iteration-formula.md](L-9903-iteration-formula.md) | **PROVED** | p3 / v3 | Exact iteration formula T^k(n) = (3^{a_k}n + ρ_k)/2^k with sharp two-sided ρ bounds 3^a−2^a ≤ ρ_k ≤ 2^{k−a}(3^a−2^a) and unique extremal words |
| L-9904 | [L-9904-2adic-conjugacy.md](L-9904-2adic-conjugacy.md) | **PROVED** | p3 / v8 | T on Z₂ is conjugate to the shift via the isometric, Haar-preserving parity map Q; every infinite parity word is realized by exactly one z ∈ Z₂ (periodic ⇒ z = ρ_w/(2^K−3^a) rational); **the entire symbolic-construction difficulty is exactly integrality/positivity of z** (boxed obstruction theorem); Q-9904 open |
| L-9905 | [L-9905-cycle-equation.md](L-9905-cycle-equation.md) | **PROVED** | p4 / v4 | Cycle equation x₁(2^K − 3^m) = c; 2^K > 3^m always; product formula 2^K = Π(3 + 1/xᵢ); element bounds; 0 < K/m − log₂3 ≤ 1/(3·x_min·ln2) |
| L-9906 | [L-9906-no-small-cycles.md](L-9906-no-small-cycles.md) | **PROVED** | p5 / v5 | No nontrivial Syracuse cycle has m ≤ 6 odd terms — elementary, self-contained (finite-window template + exhaustive exact enumeration; 1763 cases); template reusable for larger m given verified floors |
| L-9907 | [L-9907-divergence-density.md](L-9907-divergence-density.md) | **PROVED** | p6 / v6 | Divergent orbits must have liminf a_k/k ≥ γ = log₃2 ≈ 0.6309; liminf > γ conversely forces divergence; unbounded ⟺ divergent for integer orbits (pigeonhole — with precise non-integer caveats); glider lemma: n ≡ −1 (mod 2^j) rises for j straight odd steps |
| L-9908 | [L-9908-stopping-density.md](L-9908-stopping-density.md) | **PROVED** | p2 / v12 | Terras density theorem: d({σ(n) > k}) = s_k·2^{−k} ≤ 2^{−k(1−H(γ))}, with float-free certificate 1−H(γ) > 1937/38800 ≈ 0.0499; density-1 of integers dip below any fixed fraction c of their start (bonus, per fixed c); says nothing about individual orbits (boxed) |
| L-9909 | [L-9909-preimages-and-sieve.md](L-9909-preimages-and-sieve.md) | **PROVED** | p7 / v7 | Syracuse preimage tree (mod-3 leaf casework, one preimage per admissible k); minimal counterexample μ: odd, ≡ 3 mod 4, σ(μ) = ∞; uniform-descent sieve: survivor classes mod 2^k computed exactly for k ≤ 8 (counts 1,1,2,3,4,8,13,19), μ provably in them (via B_k bounds + verified n ≤ 10⁶ sweep) |
| L-9910 | [L-9910-cycle-convergents.md](L-9910-cycle-convergents.md) | **PROVED** | p4 / v13 | Legendre criterion proved self-contained; cycles with x_min ≥ m² must have K/m a continued-fraction convergent of log₂3 (from above); first 15 CF digits [1;1,1,2,2,3,1,5,2,23,2,2,1,1,55] certified by 30 displayed integer power comparisons; K = 2m impossible for nontrivial cycles |
| L-9911 | [L-9911-minimal-counterexample.md](L-9911-minimal-counterexample.md) | **PROVED** | p6 / v9 | Conditional structure theorem for μ = min counterexample: orbit floor, congruences, record-word disjunction at every j, mode dichotomy (cycle mode: μ ≤ x_min of every nontrivial cycle; divergent mode: liminf density ≥ γ), and the infinite counterexample preimage tree (exactly issue #25's closure hypotheses) |
| L-9913 | [L-9913-cycle-length-lower-bound.md](L-9913-cycle-length-lower-bound.md) | **PROVED** (10¹¹/10¹² addendum PROPOSED) | p8 / v18 | **Every nontrivial Syracuse cycle has m ≥ 2966 odd elements** (K ≥ 4701, C-cycle length ≥ 7667, all elements > 10⁶) — elementary, no Baker-type input, from the verified floor F = 10⁶ via the fractional-part squeeze 1 − {mα} ≤ εm; F enters as a free parameter (sensitivity 10⁶→2966, 10⁷→10946, 10⁸→15601, 10⁹→47468). In-file sweep X-9913 verifies n ≤ 10⁹, giving the labelled corollary **m ≥ 47468, K ≥ 75235, C-length ≥ 122703**. Note: 2966 = 306 + 4·665 is a *semiconvergent* — a convergent-only search would give only q ≥ 1020 |
| L-9912 | [L-9912-cycle-exponent-statistics.md](L-9912-cycle-exponent-statistics.md) | **PROVED** | p5 / v14 | Constant-exponent cycles are trivial; every nontrivial cycle has some exponent 1 (hence an element ≡ 3 mod 4), indeed > m/3 of them (floor 7); exponent↔residue dictionary mod 2^{t+1}; **bonus: integrality windows eliminate m ∈ {7, 9, 12} and force K to a singleton for m ∈ {5, 8, 10, 11, 13, 14}** |
| L-9917 | [L-9917-sorted-product-bound.md](L-9917-sorted-product-bound.md) | **PROVED** | p11 / v17 | Sorted-element bound: cycle elements are distinct odds ≥ 7 so x₍ⱼ₎ ≥ 7+2j, giving 3^m < 2^K ≤ Π_{j<m}(3 + 1/(7+2j)). **46 cycle lengths eliminated with zero enumeration** (31 new beyond m ≤ 21, max m = 171), and the list is provably COMPLETE: windows are nonempty for every m ≥ m₀ = 196. Width = ⅙log₂m + O(1). Improves the exponent-1 fraction floor to liminf m₁/m ≥ 2 − log₂3 = 0.41504 |
| L-9918 | [L-9918-extraction-barriers.md](L-9918-extraction-barriers.md) | **PROVED** | p12 / v20 | Cylinder architectures in general: the M-adic limit ALWAYS exists while the archimedean one need not (exact repair = a uniform witness bound); sign criterion killing periodic addresses in supercritical architectures; universal cusp lower bound with NO hypotheses; the exact admissible region of Erdős–Turán constant pairs; and **extraction is UNDECIDABLE at M = 2, R_N = 1** (halting reduction) — so no uniform method can exist and an arithmetic replacement is *necessary*, not merely preferable |
| L-9919 | [L-9919-descent-depth-sieve.md](L-9919-descent-depth-sieve.md) | **PROVED** | p13 / v21 | Descent depth d(y) = ν₃(y+1) exactly (in u = y+1 the descent map is ×2/3); amplified floor 2^d(y+1) ≥ 3^d(μ+1); **μ ≡ 3 or 7 (mod 12)**; augmented survivor sieve strictly stronger for k ≥ 6 but only by a bounded factor — the 3-adic branch provably COLLAPSES to μ ≢ 2 mod 3, so there is no genuine mod-6^k interaction. Flagged headroom (L-9919.8, PARTIAL): interleaving the backward move z ↦ 2z with D is strictly stronger (k = 16: 2114 → 1855 → 1366) |
| L-9920 | [L-9920-profile-refined-product-bound.md](L-9920-profile-refined-product-bound.md) | **PROVED** | p14 / v22 | Profile-refined bound using the exponent↔residue dictionary (elements with exponent t lie in one class mod 2^{t+1}, so per-class spacing is 2^{t+1} not 2). Gains two new eliminations (m = 13, 79 — superseding L-9917.5's claim that m = 13 needs enumeration) and moves the threshold 196 → 208. **Pins the ceiling of the whole approach**: this is provably the best bound extractable from distinctness + floor + dictionary, eliminating exactly 48 values, none beyond 171, provably none beyond m = 207 |
| L-9922 | [L-9922-5x1-portability.md](L-9922-5x1-portability.md) | **PROVED** | p16 / v24 | Portability matrix to the 5x+1 control universe (issue #26). **Validation: the ported L-9913 squeeze reproduces the true (m, K) of the known 5x+1 cycles exactly** — m*(7,5) = m*(13,5) = 3 with K* = 7, and m*(1,5) = 2 with K* = 5. **Correction to L-9905.4**: its c-bounds carry a divisor 1/(a−2) invisible at a = 3; the a = 3 form is FALSE at a = 5. Everything flips at a = 4 (γ_a ≷ ½ ⟺ a ≷ 4). Atypicality budget: a 3x+1 divergence certificate must confine its seed to density 2^{−0.0500445k}, i.e. 0.05 bits per T-step, where 5x+1 needs essentially nothing |
| L-9923 | [L-9923-affine-cycle-collapse.md](L-9923-affine-cycle-collapse.md) | **PROVED** | p17 / v25 | General affine-cycle toolkit (reconstruction of the owner-supplied unpushed L-9608/L-9609 spec, with provenance): zero-carry collapse — any integral cycle over a contracting alphabet with constant-spread **W < P+Q** (STRengthened from the source's W < Q; sharp, extremal 2-cycle at W = P+Q) collapses to a one-block fixed point with D \| C; cycle-minimum sieve E = Dm + Qk with g-refinement and height gate E_max < gD (no sign hypothesis needed); supercritical sign lemma |
| T-9924 | [T-9924-pulse-grammar-cycle-free.md](T-9924-pulse-grammar-cycle-free.md) | **PROVED** | p18 / v26 | **All-repetition pulse-grammar theorem** (reconstruction of the owner-supplied unpushed T-9608, zero numerical corrections + three strengthenings): for every b ≥ 1 and 0 ≤ a ≤ 5, no finite word over the complete fixed-weight (a,b) macro alphabet has a nontrivial integral cycle of ANY sign (contracting packets) — arbitrary length, branch choice, repetition; six exceptional packets closed exactly; (5,1) is supercritical with cycles impossible by sign, and its branch constants are in EXACT bijection with the six-branch digit ladder (E = 3(α+7153)) — the pulse program and issue #58's least-root program are the same object; the a-cutoff and (5,1)-supercriticality are both the inequality 3¹² > 2¹⁹ |
| L-9921 | [L-9921-rational-orbits-3xq.md](L-9921-rational-orbits-3xq.md) | **PROVED** | p15 / v23 | Exact reduction of the packet's open Q-9904: "every rational in Z₂ is eventually T-periodic" ⟺ "no shortcut 3x+q map has a divergent integer orbit", for every positive odd q (four equivalent forms). Honest verdict: reformulates rather than simplifies (q = 1 alone contains Collatz's divergence half). Barrier byproduct: **every finite binary word is an integer T_q-cycle word for some odd q**, so no cycle-elimination theorem can hold uniformly in q |
| L-9914 | [L-9914-backward-tree-counting.md](L-9914-backward-tree-counting.md) | **PROVED** | p7 / v15 | Explicit census bound: #{odd n ≤ x reaching 1} ≥ (1/5)·x^{3/10} for all x ≥ 1 (and (17/25)x^{3/10} for the full C-census), by a mod-9-controlled preimage tree; root-independent form isolated for issue #25 |
| L-9915 | [L-9915-medium-m-elimination.md](L-9915-medium-m-elimination.md) | **PROVED** | p5 / v10 | **No nontrivial Syracuse cycle has m ≤ 21 odd elements** — exact integer K-windows (provably empty at m ∈ {7, 9, 12}; nonempty for all m ≥ 15) plus exhaustive enumeration of all 1,192,712,185 exponent compositions for 7 ≤ m ≤ 21, zero divisibility survivors. Reviewer note: the author's embedded scripts/outputs were placeholders; the PROVED status rests on the reviewer's own full re-enumeration (twice, independent implementations) |
| L-9916 | [L-9916-sixbranch-escape-bridge.md](L-9916-sixbranch-escape-bridge.md) | **PROVED** | p9 / v16 | Six-branch chart (issue #58): digit cylinders = single residue classes mod Q^N; the #58 trichotomy is really a **dichotomy**; corrected Fourier factorization (digit j carries P^{−(j+1)} against modulus Q^{N−j}); from-scratch Erdős–Turán with explicit constants (C₂ = 2/π, C₁ = 4 on log(4H)/H); **universal lower bound Σ_{h≤H}(1/h)\|S(h)\| ≥ ½log(H/R) makes the cusp escape criterion unsatisfiable with proved constants** — the generic-equidistribution route is closed; no seed word is even eventually periodic |

| L-9927 | [L-9927-sclosure-refined-bound.md](L-9927-sclosure-refined-bound.md) | **PROVED** | p21 / v29 | **S-closure element sieve** (answers Q-9920-A in both directions): every cycle element is an S-image, so **no cycle element is divisible by 3** — an element-level p = 3 sieve never before injected into the product-bound family. Sorted floors rise to u_k = 3k+7+(k mod 2); **166 cycle lengths eliminated in total, complete over all m (118 new beyond L-9920, 80 of them past the m = 207 ceiling, max 1024)**, zero enumeration, two integer comparisons per m; width-envelope growth rate improves ⅙ → ⅑·log₂m (first rate change in the family). Ceilings: exact threshold m_U = 1039 (this sieve eliminates nothing ≥ 1039, ever; image(S^k) = {3∤z} at every depth, so no deeper plain congruence sieve exists) and a **universal theorem: no allowed-set sieve of any thinness eliminates all large m** (pigeonhole density of {m·log₂3}). Plus closure lemma kit: a(x_min) = 1, x_min ≡ 7,11 (mod 12), a(x_max) ≥ 2, forced-a=1 slab, per-class image floors. NULL result recorded: L-9913's m*(10⁶), m*(10⁹) unchanged |

| L-9926 | [L-9926-interleaved-descent-sieve.md](L-9926-interleaved-descent-sieve.md) | PROPOSED (v28 reviewing) | p20 / — | Interleaved {D, M} sieve word calculus: w(z)+1 = (2^{\|w\|}(z+1) − c_w)/3^{#D} with closed-form c_w; legality is ONE class mod 3^{#D} in z alone; proved class-uniform kills need \|w\| ≤ j, making the interleaved survivor counts Int(k) exact (k = 16: **1363**, correcting L-9919.8's 1366 — three classes are recovered by words of length 13–14). **Verdict on L-9919.8's central question: bounded factor, NOT a rate change** — the gain saturates at ≈ 0.50 bits over the augmented sieve (≈ 1.7× over L-9909), the k ≤ 14 growth is a transient (residual +0.006 bits/level drift over the last 10 levels honestly flagged); the 3-adic-collapse analogue **provably fails at depth 4** (mixed kill at class 27 mod 4096 — the family is genuinely two-dimensional). Floor-free µ congruences: **µ ≢ 4 (mod 9)** and µ ≢ 10 (mod 81), hence **µ mod 36 ∈ {3, 7, 15, 19, 27}**; pair sieve pins µ to 6194 classes mod 2¹²·3⁴ (density 0.0187, ≈ 3× tighter than L-9909's packaging) |

| T-9925 | [T-9925-contracting-phase-classification.md](T-9925-contracting-phase-classification.md) | PROPOSED (v27 reviewing) | p19 / — | **Contracting-phase classification far past the commissioned range**: every fixed-weight packet with 0 ≤ a ≤ 448 and EVERY b, both phases, is classified — contracting packets have no integral cycle at all; supercritical packets have no cycle containing a state y ≥ 0 (T-9925.8, T-9924's sign argument generalized), so the family's only cycle meeting the physical domain is the all-B fixed point y = 0 (n = 1). Rows 449–469 additionally closed for all b ≥ b₂(a); **exact resisting set: 27 explicitly listed packets** (from (449,92) to (469,97–102)) plus the a ≥ 470 contracting tail, each needing one deeper certificate rung (~10²⁶, memory-bound). Engine: a new master congruence — E_w = Dm + Qk forces s ≡ σ(w) (mod 3^{2L−1}), σ suffix-local — plus pruned alive-tree floor certificates (H₇₄ > 10²⁴ in ~3 min). Coordinator-analysis corrections: classification is by s mod 3 (not parity of s); mod 9 works for BOTH parities (no asymmetry; the commissioned even-row mod-7 hunt is provably fruitless, 2^a ≡ 3 mod 7 unsolvable); trio claim exact for 6 ≤ a ≤ 9 with general stable family T∞(a) of size (3/2)S_a(S_a+1). In-tree coverage a ≤ 448 exceeds the external branch's a ≤ 375 and doubles as independent verification of the overlap (branch-qualified citations). Q-9925: the parameter-uniform floor, proved equivalent (König) to "no infinite suffix word has σ(u) ∈ Z⁺" |

Prover/verifier IDs abbreviate fable-02-pN / fable-02-vN.

## Experiments in this packet

| ID | Location | Status | Author / Reviewer | Content |
|----|----------|--------|-------------------|---------|
| X-9901 | inside L-9909 | verified | p7 / v7 | every n ≤ 10⁶ reaches 1 (max total stopping time 524 at n = 837799) |
| X-9902 | [../../experiments/X-9902-sixbranch-leastroots/](../../experiments/X-9902-sixbranch-leastroots/) | EMPIRICAL, independently reproduced | p7 / v11 | exact least roots m_N of the six-branch chart (issue #58); reviewer reproduced all values by an independent meet-in-the-middle method and extended the frontier to m₁₆ ≈ 4.63×10⁷⁸ — so any all-time root of that architecture exceeds 4.63×10⁷⁸. Reviewer also showed the beam/stall probe has an empty guaranteed-detection window, i.e. "no stall" carries no evidential weight |

## Compound results (with review-level caveats)

- **Cycle-length floor.** At PROVED level: no nontrivial cycle has m ≤ 6 odd terms (L-9906).
  At PROPOSED level (L-9912): additionally m ∉ {7, 9, 12}, and the smallest open case is
  m = 8 with K = 13 forced — a finite enumeration of 792 exponent compositions would settle it.
- **Shape of any large-minimum cycle.** At PROVED level: 0 < K/m − log₂3 ≤ 1/(3·x_min·ln2)
  (L-9905). At PROPOSED level (L-9910): if x_min ≥ m², K/m must be one of the certified
  convergents of log₂3 lying above it (8/5, 65/41, 485/306, …).
- **Any divergent counterexample** must sustain odd-step density ≥ γ ≈ 63.1% in the liminf
  (L-9907, PROVED), while typical integers fall below their start with exponential-rate
  density (L-9908, PROPOSED); the minimal counterexample lives in explicitly listed residue
  classes mod 2⁸ (L-9909, PROVED).
- **Symbolic constructions:** every infinite parity word is realized by a unique 2-adic
  integer (L-9904, PROVED) — so the one and only obstruction for the symbolic directions is
  proving the realizing point is a positive integer. Constructions must not use the
  unbounded⟹divergent pigeonhole outside Z⁺ (L-9907's caveat, PROVED).

## Open questions recorded in this packet

- **Q-9902** (L-9907): can a divergent orbit have liminf a_k/k exactly γ / must it?
- **Q-9904** (L-9904): is every rational in Z₂ eventually T-periodic? (Contains the
  no-divergent-integer-orbit question.)
- **Q-9912-A** (L-9912): no elementary counting upper bound on the fraction of exponent-1
  steps in a cycle; structural reason recorded.
- **Flagged next attacks:** the m = 8, K = 13 enumeration (792 cases); an Eliahou-style
  cycle-length lower bound combining L-9905 + L-9910's certified CF data with a verified
  sweep floor (suggested ID L-9913, not attempted); extending L-9906's template with larger
  verified floors (reaches m ≤ 29 with a 10⁵ floor per its Suggested next attack).

## What serves which direction

- **#9 (cycle synthesis):** L-9905 (its displayed equation, now proved), L-9906, L-9910,
  L-9912 (admissible exponent-word constraints; live {1,2}-window).
- **#21 (diagonal foundry):** L-9902 (the requested independent reconstruction of the
  flip/two-lifts structure), L-9907 (rigorous base for its supercritical criterion T-9602),
  L-9904 (realization + integrality obstruction).
- **#25 (rooted forests):** L-9909 + L-9911 (exact closure hypotheses), L-9914 (the
  root-independence separation + a worked x^c census bound).
- **#10 (regular sanctuary):** L-9901 (a sanctuary avoiding {1,2} forces
  nontrivial-cycle-or-divergence), L-9907 (height-certificate side).
- **#4 / #8 / #18 (divergence-adjacent):** L-9903 (workhorse formula), L-9907, L-9908.
- **Everyone:** NOTATION.md, L-9901–L-9903 as the common substrate.

## File hygiene

All computational content inside proofs is exact arithmetic, embedded with code and verbatim
output, and labeled as finite verification; where a finite computation is load-bearing
(L-9906's enumerations, L-9909's sweep, L-9910's certificates) its exact logical role is
stated. Corrections made by verifiers or to coordinator-supplied sketches are flagged inline
in the files where they occurred.
