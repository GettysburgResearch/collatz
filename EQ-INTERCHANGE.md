# P2 deep-dive I: the interchange, the copies, and where the difficulty actually lives

*Packet P2 (issue #4). New claims: T-0023, L-0016, O-0012, O-0013 in
`CLAIMS.md`. Measurement companion: `experiments/eq_interchange_l1l2.py`
(→ `results/eq-interchange-l1l2.log`). Notation as in `NOTATION.md`;
κ₁ = 2/π + 1/81, κ₂ = 2/π + 1/9.*

## 1. The union-bound obstruction, quantified (L-0016)

**Lemma.** No union bound over frequencies can convert T-0012 into an
all-K statement: T-0012 gives, for each θ of scale m(θ) = ⌊log₈₁θ⌋ and
threshold t, exceptional-depth density ≤ κ₂^{m+1}/t; summing over
θ ≤ 81^{M} costs Σ_m 80·81^m κ₂^{m+1} = 80κ₂ Σ_m (81κ₂)^m with
81κ₂ ≈ 60.6 — geometric divergence by a factor ~60 per scale. Even
restricting to one scale, the 80·81^m frequencies of scale m overwhelm
the κ₂^{m+1} density gain. Any successful interchange must therefore
use joint (θ, K) structure, not the two marginal theorems. ∎
(Statement about the *method* T-0011/T-0012 provide; rigorous as
stated.)

## 2. T-0023: L² block-mean decay (T-0011 squared)

**Theorem.** For every full block B of 81^{m+1} consecutive
frequencies (anywhere, not only the survivor range),

    mean_{θ∈B} (|S_K(θ)|/2^K)² ≤ (1/2 + 1/81)^{m+1}.

**Proof.** Identical to T-0011 with cos² in place of |cos|:
`|S_K(θ)|²/4^K = Π_t cos²(π{θc_t/64^K})`; the Markov decomposition
(T-0011 Lemma A) is arithmetic and position-free — over any full
81^{m+1}-block the top phase data (s₀, j₀…j_{m−1}) is exactly uniform
and independent; the contraction step replaces Lemma B by: every
shifted Riemann sum `(1/81)Σ_j cos²(π(j+φ)/81) = 1/2 + (1/162)Σ_j
cos(2π(j+φ)/81)·2 ≤ 1/2 + 1/81` (the cosine sum over a full period of
the doubled angle telescopes to a single term of modulus ≤ 1; same
variation bound as Lemma B). Discarding the deeper factors (≤ 1)
gives the claim. ∎

Corollary (unconditional L² mass profile): Σ_{θ≤X}(|S_K(θ)|/2^K)² ≤
C·X^{1−η₂} with η₂ = −log₈₁(1/2 + 1/81) ≈ 0.1522, for all X, K.

## 3. The counting template and the exact copy decomposition

**Lemma M (Fejér majorant; standard).** For R ⊂ ℤ_Q, |R| = N, interval
I of length Y, any H ≥ 2: #(R∩I) ≤ C₀(Y/Q + 1/H)(N + Σ_{0<h≤H}|Ŝ(h)|)
with absolute C₀ (convolve 𝟙_{I extended by Q/H} with the Fejér kernel
of order H; the majorant's transform is supported in |h| < H and
bounded by C(Y/Q + 1/H)).

**Copy decomposition (exact; from T-0009(a)).** Every 0 < h < 64^K is
uniquely h = 64^j θ′ with 64 ∤ θ′, and |S_K(h)| = 2^j |S_{K−j}(θ′)|.
Hence for any H,

    Σ_{0<h≤H} |S_K(h)| = Σ_{j≥0} 2^j Σ_{64∤θ′≤H/64^j} |S_{K−j}(θ′)|,

and likewise with squares and 4^j. The "beyond-range" part of any
frequency window is exactly a union of rescaled copies of shallower
survivor problems. **The structured large-|S| frequencies are not
noise: they are the 2-adic self-similarity of R_K itself.**

## 4. The copy barrier (O-0013): why every majorant variant stalls at the fair window

To resolve an interval of length Y = 64^{(1−ε)K} (ε > 1/6 is the
near-emptiness regime; the fair window is 32^K = 64^{5K/6}), Lemma M
needs H ≈ Q/Y = 64^{εK} > 2^K — the window necessarily includes copy
frequencies. Assembling §3 with the best available inputs:

* **L¹ variant.** In-range parts, with the measured profile
  Σ_{θ≤X}|S_K(θ)|/2^K ≈ X^{1/3} (see §5) or even with in-range L²
  = O(1) + Cauchy–Schwarz, contribute error exponent 2^{K(3/2−6ε)} —
  harmless for ε > 1/4. The copy parts, bounded by the T-0011 block
  profile X^{1−η₁} (η₁ ≈ 0.0983), contribute ≥ 2^{K(1−0.59ε)} —
  **divergent for every ε ≤ 1**.
* **L² variant.** Same structure with T-0023: copy contribution
  2^{K(1−0.46ε)} — again divergent for every ε ≤ 1.

And this is not merely a weakness of the block bounds: the copy sum
*genuinely* contains terms 2^j|S_{K−j}(θ′)| at the 79 core θ′ per
level, whose measured size (|S_n(1)|/2^n ~ 0.585^n geometric mean)
makes Σ_{h≤64^{εK}}|S(h)| comparable to 2^K — the template's error
term is then comparable to its main term at every ε > 1/6. A rigorous
version of this barrier needs *anti-concentration* (lower bounds on
|S_n(θ′)| along subsequences), not attempted here; at the measured
profiles the deficit is as computed. **Conclusion (the honest
relocalization):** below the fair window, majorant-type harmonic
counting fails not for lack of decay but because the count really is
governed by the copies — i.e. by the recursion
`R_K = J₀(R_{K−1}) ⊔ J₁(R_{K−1})` itself. What is missing is
cancellation/positivity structure *among copies* (the majorant adds
their moduli), or a genuinely 2-adic-aware counting argument. This
sharpens EQ.md's "EQ must be archimedean" observation into a
quantitative statement about proof templates.

## 5. Measurements (O-0012; K = 8…16, exact-phase floats)

1. **In-range L² mass is O(1)**: Σ_{0<θ≤2^K}(|S_K|/2^K)² ∈
   [0.88, 1.11] across K = 8…16 (λ_K = log₂(mass)/K drifting
   −0.017 → +0.009). The natural uniform hypothesis
   (Λ): sup_K mass ≤ c₁ — the cleanest currently-unproved input for
   any future route.
2. **In-range L¹ mass** ≈ X^{1/3}-profile: 8.9 → 47.9 over
   K = 9 → 16 (≈ ×1.25/level).
3. **T-0011/T-0023 are astronomically loose for small-θ blocks at
   large K**: measured mean over (0, 81] at K = 16 is 6.2×10⁻⁴
   against the bound 0.649 (the bound uses only m+1 of the K
   contracting levels). The earlier "essentially sharp" reading of
   T-0011 applies to the truncated top-level products, not to |S_K|
   itself. Encouraging for (Λ): the truth is far below the provable.
4. **The core frequency is genuinely delicate**: |S_K(1)|/2^K =
   1.0×10⁻¹ at K = 10 but 4.2×10⁻⁷ at K = 15 and 2.3×10⁻⁴ at K = 16 —
   non-monotone with near-exceptional depths (K = 10), exactly the
   behavior that makes T-0012's density-1 (not all-K) conclusion
   honest. Geometric-mean rate 0.585/level over K = 8…16.

## 6. Revised P2 program

1. **Prove (Λ)** — in-range L² mass O(1) (or 2^{o(K)}): a
   two-variable Markov/block argument on cos² over (θ, K) jointly;
   T-0023 is the one-variable shadow. This replaces "pointwise decay
   at the 79 cores" as P2's isolated analytic target and is an
   average-form statement, plausibly within the existing machinery's
   reach.
2. **Count through the recursion, not around it**: the copies ARE
   `R_K = J₀R_{K−1} ⊔ J₁R_{K−1}` with archimedean contraction 64/81;
   direct recursive counting of `#(R_K ∩ [0,Y])` with congruence
   input (chart classes mod 17) — positivity is automatic there,
   which is exactly what the majorant lacks.
3. **Anti-concentration** for a rigorous form of the §4 barrier
   (lower bounds on core |S_n|): would convert the barrier from
   measured to proved and delimit the method space definitively.
4. **The dial**: rerun §2–§5 at the other ladder rungs (M, N, |D|) —
   the constants 2/π and 1/2 + 1/81 shift with the alphabet; a rung
   where the copy deficit closes would be a provable-near-emptiness
   instance (Pivot A of `GENERAL.md`, now with a precise inequality
   to chase).

*Statuses: §1 L-0016 and §2 T-0023 PROPOSED (proofs above); §4 is
EMPIRICAL-conditional (O-0013) except its rigorous skeleton; §5
O-0012 EMPIRICAL. The exponent bookkeeping in §4 deserves independent
re-derivation (M-0003 slot open).*

---

# P2 deep-dive II: the room recursion, an unconditional bound, and the sixth mask

*Same packet, second session. New claims T-0024, L-0017, O-0014.
Companion: `experiments/eq_recursion_count.py`
(→ `results/eq-recursion-count.log`).*

## 7. The room recursion (T-0024)

**Lemma (pullback identity).** Let 0 < Y with 81Y/64 + 1 < 64^{K−1}
(the one-room regime — all near-emptiness regimes qualify). Then the
map A ↦ (A′, ε), ε = A mod 64 ∈ {0,1}, A′ = 81·(A−ε)/64 + ε, is a
bijection

    {A ∈ R_K : 0 < A ≤ Y}  ≅  ⊔_{ε∈{0,1}} {A′ ∈ R_{K−1} :
        0 < A′ ≤ 81(Y−ε)/64 + ε,  A′ ≡ ε (mod 81)}.

*Proof.* Validity of A forces its low digit ε ∈ {0,1}; B = (A−ε)/64
satisfies A′ = 81B + ε ∈ R_{K−1} (one H-step), and in the stated
regime no mod-64^{K−1} reduction occurs, so A′ is the integer 81B+ε —
whence the **free congruence** A′ ≡ ε (mod 81) and the interval bound.
Inverse: B = (A′−ε)/81 (integral by the congruence), A = 64B + ε. ∎
(Beyond the regime, children wrap into rooms r ≥ 1 with classes
ε − r·64^{K−1} mod 81 — general form verified exactly in the script:
144/144 cells, both forms.)

**Theorem T-0024 (unconditional near-window bound).** For every
ε ∈ (0, 1),

    #{A ∈ R_K : 0 < A ≤ 64^{(1−ε)K}}  ≤  2^{K−j},
    j = ⌊εK/log₆₄81⌋ − 1  =  (0.9455… ε − o(1))K.

*Proof.* Iterate the Lemma, discarding the congruence (the two
ε-classes are disjoint subsets of the depth-(K−1) interval count, so
their sum is at most the unrestricted count) and enlarging the
interval Y ↦ 81Y/64 + 1 each step. After j steps in the one-room
regime — which persists precisely while 81^{j+1}Y ≲ 64^K, i.e.
j ≤ εK/log₆₄81 − 1 — the count is at most #(R_{K−j} ∩ anything)
≤ 2^{K−j}. ∎ (Checked at K = 10, 12, 14, ε = 0.1…0.9: no violation.)

This is the program's **first unconditional quantitative statement
toward near-emptiness**: survivors below 64^{(1−ε)K} number at most
2^{K(1−0.9455ε)} — exponentially fewer than |R_K| for every ε > 0.
It is far from the law's 2^{K(1−6ε)} (all the distance lies in the
discarded congruences), but it is a strict, free-standing theorem
where previously there was only the trivial 2^K.

## 8. The sixth mask, and where the factor 6 lives

Keeping the congruences instead of discarding them, the recursion
composes to: **if interval-restricted R_n equidistributes mod 81
(classes {0,1} jointly owning 2/81 + o(1)), then
count(K, 64^{(1−ε)K}) ≈ (2/81)^{j}·2^{K−j} = 2^{K(1−(6−o(1))ε)}** —
the exact equidistribution law. So EQ's irreducible core acquires a
sixth equivalent mask, and the most elementary one yet:

> **(Mask 6)** For Z in the near-window range, R_n ∩ (0, Z] occupies
> the residue classes {0, 1} mod 81 with frequency 2/81 + o(1).

No Fourier analysis, no products — a congruence-counting statement
about the coded sets, in which the entire factor 6 = log₂64 vs
log₂(81/2)-per-level gap between T-0024 and the law is the
equidistribution content. Measured (O-0014): at full range the mask
holds to 3×10⁻³; at small Z the classes {0,1} are genuinely
**enhanced 2–3×** (share 0.086 at n = 12, Z = 64^{0.9n}, sample 35;
0.058 at n = 14) — the smallest survivors cluster near the trivial
fixed points {0,1} (which are ≡ 0, 1 mod 81). The mask's o(1) is
therefore honest work at small Z, not bookkeeping: any proof must see
the enhancement die off as Z grows through the window.

## 9. (Λ) as twisted pair separation (L-0017)

Expanding |S_K(θ)|² over pairs and summing over 0 < θ ≤ 2^K with the
Dirichlet kernel bound ‖D‖ ≤ min(2^K, ½‖Δ/64^K‖⁻¹):

    Σ_{0<θ≤2^K} (|S_K(θ)|/2^K)²  ≤  1 + 2^{−2K} Σ_{A≠A′∈R_K}
        min(2^K, 64^K/(2·dist(A, A′))),

so (Λ) is implied by the **pair-separation bound**
Σ_{A≠A′} 64^K/dist(A,A′) ≲ 4^K. The pair differences stratify
exactly by the first differing digit t₀: every difference is

    Δ = 64^{t₀} · (81^{−t₀} mod 64^{K−t₀}) · Δ′,

with Δ′ a depth-(K−t₀) code difference at t₀′ = 0 — a rescaled copy
**rotated by the odd unit 81^{−t₀}**. Without the twist, pair
separation would be exactly self-similar and (Λ) would follow by
recursion; the twist is the precise point where individual-orbit
structure (the archimedean size of 2-adic representatives of
81-power inverses) enters. (Λ) is thus wall-adjacent — equivalent in
difficulty to the equidistribution of the twisted copies — and its
measured truth (O-0012: mass ∈ [0.88, 1.11]) is another face of the
same coin as Mask 6. The honest priority order is therefore:
**Mask 6 (congruence form) first** — it is finite, combinatorial,
and its small-Z enhancement is already understood mechanically.

## 10. Standing after deep-dive II

Unconditional: T-0024 (the first near-window count bound), T-0023,
L-0016, the exact recursion identities. Conditional/equivalent forms
of the core, now six masks deep, with Mask 6 (mod-81 interval
equidistribution) as the recommended attack surface. The copy
barrier (§4) explains *why* harmonic templates stall; the room
recursion (§7) is the positivity-native replacement, and every future
improvement is now measured by how much of the discarded congruence
information it recovers — from 0.9455ε (none) toward 6ε (all).

---

# P2 deep-dive III: the Cantor refinement and the tri-adic factorization

*Same packet, third session. New claims T-0025, T-0026, O-0015.
Companion: `experiments/eq_cantor_classes.py`
(→ `results/eq-cantor-classes.log`).*

## 11. The general ladder bound (T-0025)

T-0024's pullback argument uses only the digit-transfer shape: for any
chart `H_D(MB+d) = NB+d` (coprime M < N), the child map carries the
free congruence `A′ ≡ d (mod N)`, and iterating in the one-room regime
gives, unconditionally, for every rung of the ladder:

    #{A ∈ R_K^{(M,N,D)} : 0 < A ≤ M^{(1−ε)K}}  ≤  |D|^{K−j},
    j = ⌊εK/log_M N⌋ − 1.

The general Mask: the law at rung (M,N,D) ⟺ interval-restricted
R_n^{(M,N,D)} gives the classes D mod N total frequency |D|/N + o(1).
(Proof identical to §7; the whole §7–§10 analysis is
digit-transfer-generic, per `GENERAL.md` §3.)

## 12. The Cantor refinement (T-0026)

Because the pullback's ε is *forced* (ε = A′ mod 81 must lie in
{0,1}), the small-survivor ancestry is deterministic, and j
iterations compose into an exact identity. Define the **admissible
seed classes** `C_j ⊂ ℤ/81^j` by the chain condition (the j-step
child orbit keeps every iterate ≡ 0 or 1 mod 81), equivalently by the
lifting recursion

    C_1 = {0,1},   C_j = {(81c − 17ε)·64^{−1} mod 81^j :
                          c ∈ C_{j−1}, ε ∈ {0,1}}.

**(a) |C_j| = 2^j exactly** (the lifting map is injective and its
image automatically satisfies the level-0 condition — three lines).
**(b) Refined identity** (verified 27/27 cells): in the iterated
one-room regime,

    {A ∈ R_K : 0 < A ≤ Y}  ≅  {A* ∈ R_{K−j} :
        A* mod 81^j ∈ C_j,  0 < desc_j(A*) ≤ Y},

with `desc_j(A*) = (64/81)^j A* + O(1)` (measured drift < 0.62,
proved < 81/17·(max ε) trivially).
**(c) Corollary (the tri-adic form of EQ's core).** Near-window
counting is exactly: count a 2-adically prescribed set (R_{K−j},
2^{K−j} residues mod 64^{K−j}) inside an 81-adically prescribed
Cantor set (C_j, 2^j residues mod 81^j, density (2/81)^j) inside an
archimedean interval. By CRT the joint Fourier analysis **factorizes**:
the error terms are Σ Î(h)·Ŝ(h₂)·Ĉ_j(h₈₁) with Ŝ the coded-set
product (T-0007) and Ĉ_j an 81-adic product transform generated by
the same lifting recursion — a *twin self-similar product on the dual
side*. The 81^{−t}-twists that obstruct (Λ) (L-0017) are exactly the
generators of C_j: the two products are built from the same orbit.
Whether their pairing exhibits provable cancellation is now a
concrete, well-posed question — and the first genuinely *new attack
surface* on the interchange in the program's own terms.

## 13. Measurements (O-0015)

Depth-j Mask at small Z magnifies the fixed-point enhancement
(share 0.0286 vs (2/81)² = 0.00061 at n = 12, j = 2, Z = 64^{0.9n} —
~47×), and converges to uniform at full range as n grows (0.00195 →
0.00043 vs 0.00061 from n = 12 → 14). The enhancement's j-scaling is
consistent with clustering near the trivial fixed points (which are
admissible at every depth); its decay in n is the concrete
provability target flagged in §8.

## 14. Standing after deep-dive III

The near-emptiness problem now has a fully explicit skeleton:
unconditional exponent 0.9455ε (T-0024/T-0025, all rungs), exact
deficit = Cantor-class equidistribution (T-0026), dual factorization
S × Ĉ with both factors self-similar products from the same orbit.
Next iterations: (i) the Ĉ_j product formula written out and its
pairing with S tested for cancellation; (ii) the enhancement-decay
lemma (fixed-point cluster thinning); (iii) the same refinement at
the other ladder rungs (T-0025 makes it generic).

---

# P2 deep-dive IV: the Ĉ product formula and product rigidity

*Same packet, fourth session (loop iteration 2). New claims T-0027,
T-0028, O-0016, O-0017. Companion: `experiments/eq_joint_discrepancy.py`
(→ `results/eq-joint-discrepancy.log`).*

## 15. T-0027: the Cantor transform is the mirror product

Unrolling C_j's lifting recursion through the character sum:

    Ĉ_j(ψ) = Σ_{x∈C_j} e(ψx/81^j)
           = Π_{i=1}^{j} (1 + e(−17·64^{−i}ψ / 81^{j−i+1})),

with 64^{−i} the inverse mod 81^{j−i+1} — **the exact 81-adic mirror
of T-0007**: same constant 17, same 64/81-orbit, places exchanged.
(Verified: max |direct − product| = 9×10⁻⁸ over 160 samples, j ≤ 4.)

## 16. T-0028: product rigidity of the survivor sets

Measured first (O-0016): D*(CRT(R_n × C_j)) equals D*(R_{n+j}) to
every printed digit — e.g. D*(R₁₀×C₂) = D*(R₁₂) = 0.003613,
D*(R₁₀×C₃) = D*(R₁₂×C₁) = D*(R₁₃) = 0.002204 — and the joint set
*improves* on both marginals (n = 10: 0.0449 alone → 0.0022 at
j = 3). Explanation, then verified at element level:

**Theorem (statement).** For every split K = n + j, each A ∈ R_K
satisfies the exact identity `81^j A = 64^j A* + 17 c_w + r·64^K`
where A* ∈ R_n is its j-fold H-image, w its low-j digit word (c_w the
word constant), and r ∈ [0, 81^j) the room index; consequently A's
normalized position is `(r + position(A*) + O(64^{−n}))/81^j`: **the
coarse structure of R_K at scale 81^{−j} is the room process, and the
fine structure inside each room is an exact translate of R_n.**
Sorted-embedding comparison (element-by-element, exact
cross-multiplied arithmetic): positions of R_{n+j} and CRT(R_n × C_j)
agree within ~one joint-modulus slot (max 1.03 slots over all tested
(n,j), with 1024–4096 exact equalities per set). Status: the
per-element identity is proved (it is the coding identity read
archimedeanly); the full order-isomorphism corollary needs the
(room ↔ Cantor-class) bijection lemma per A*-fiber — written as
PARTIAL pending that lemma.

**Why it matters.** (i) The S–Ĉ pairing question of §12 has a
positive answer at the set level: the product does not degrade
equidistribution — it *is* the deeper set. (ii) EQ's core becomes a
statement about the **room process alone**: the fine structure is
recursively identical, so all new equidistribution content at each
scale is the room walk — an 81-adic process driven by the same
17·(64/81)-orbit, now isolated as a single object. (iii) The
self-similar-measure literature interface (Li–Sahlsten/Solomyak,
already flagged in MINIMAL.md) now has the product structure explicit
rather than heuristic.

## 17. O-0017: the enhancement is a boundary effect

Mask-6 enhancement profile across n = 10…16: at fixed β the
enhancement dies as the sample count grows — share of C₁ classes at
β = 0.95: 0.058 → 0.023 (n = 10 → 16, samples 139 → 2357); at
β = 1.0 uniform (0.0247) already by n = 11. The enhancement is
carried by the first ~10²–10³ survivors (the fixed-point cluster),
not by a persistent β-range: **Mask 6's o(1) is a bounded-count
boundary effect** — the strongest empirical evidence yet that the
mask is provable, since bounded-count effects vanish automatically at
the law's scale.

## 18. Loop queue after deep-dive IV

1. Prove the (room ↔ class) bijection lemma → upgrade T-0028's
   corollary from PARTIAL.
2. The room process: write its exact transition law (it is
   NOT i.i.d.; it is the 81-adic shift of the 17-orbit) and attack
   its equidistribution directly — this is now the single object
   carrying EQ.
3. Bounded-count formalization of O-0017 → the enhancement-decay
   lemma → Mask 6 with explicit o(1).
