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
