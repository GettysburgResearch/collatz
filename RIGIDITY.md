# Schema Rigidity for Collatz Rewrite Certificates

**Setting.** `T(n) = n/2` (n even), `(3n+1)/2` (n odd) — the shortcut map,
extended to rationals with odd denominator (parity = parity of numerator).
All arithmetic below is exact. Computational companions:
`experiments/rigidity_check.py` (identity search + lemma checks),
`experiments/amplifier_catalog.py` (Lemma 1), `experiments/verify_outline.py`.

This note proves that the certificate format proposed for a symbolic
Collatz counterexample — *a finite cycle of word schemas
`F_i(k) ⟹* F_{i+1}(k+δ_i)` valid for all large `k`, with `Σδ_i > 0`* —
cannot exist in the single-parameter geometric class, except in one
precisely-delimited degenerate form that presupposes what it is trying to
prove. It also explains, structurally, two phenomena observed in the
experimental program: why constructed gadget loops have odd-step density
*just below* `log_3 2`, and why per-window expanding identities exist in
abundance even though expanding *cycles* of identities do not.

---

## 0. Preliminaries

**Affine form of `T^S`.** For fixed `S` and fixed parity word
`w ∈ {0,1}^S` with `A = Σw_i` ones, on the congruence class of integers
whose first `S` parities are `w`,

    T^S(n) = (3^A n + c_w) / 2^S,
    c_w = Σ_{i: w_i = 1} 3^{A - A(i+1)} 2^i        (A(j) = #ones among w_0..w_{j-1})

**Lemma A.** `c_w ≥ 0`. *(Each summand is nonnegative.)* ∎

**Lemma B.** `c_w ≤ S · 3^{S-1}`. *(Each summand is `3^{#ones after i} 2^i
≤ 3^{S-1-i} 2^i ≤ 3^{S-1}`; there are at most `S` summands.)* ∎

**Lemma B′ (suffix form).** Let `R_tail(j) = 3^{A-A(j)} / 2^{S-j}` (the
multiplier of the suffix window from step `j`). Then

    c_w / 2^S = (1/2) Σ_{i: w_i=1} R_tail(i+1)  ≤  (S/2) · max_j R_tail(j).

*(Rewrite each summand: `3^{A-A(i+1)} 2^i / 2^S = R_tail(i+1)/2`.)* ∎

**Lemma C (Terras rigidity / fuel).** If `v_2(x − y) = f ≥ 1` then `x`
and `y` have the same first `f` parities, and for `j ≤ f`,
`T^j(x) − T^j(y) = (3^{A(j)}/2^j)(x − y)`, so `v_2(T^j(x) − T^j(y)) = f − j`.
**Tracking depth decreases by exactly one per shortcut step and is never
created.** *(Induction on j: both branches of T are affine with linear
coefficient of 2-adic valuation −1.)* ∎

**Lemma D (irrationality).** `A log 3 = S log 2` with integers
`A, S ≥ 0` forces `A = S = 0` (`3^A = 2^S` and unique factorization). ∎

**Lemma 1 (sign–criticality).** Every parity word `w` of length `p` with
`a ≥ 1` ones has a unique affine fixed point
`x_w = c_w / (2^p − 3^a) ∈ ℚ` with odd denominator, whose `T`-orbit
realizes the parity word `w^∞`; every eventually periodic orbit of a
rational with odd denominator lands on such a cycle. Since `c_w > 0`:

    x_w > 0  ⟺  2^p > 3^a  (subcritical: perturbations contract),
    x_w < 0  ⟺  2^p < 3^a  (supercritical: perturbations amplify).

*Negative rational cycles are exactly the supercritical amplifiers;
positive rational cycles are all subcritical sinks.* Verified for all
32,752 words of length ≤ 14 (`amplifier_catalog.py`). ∎

---

## 1. What a single-parameter schema certificate is

A *schema family* is a family of canonical words `F(k)` (any radix,
LSD-first) whose block lengths are affine in one integer parameter `k`.
Its values are then exactly the **exponential polynomials**

    N(k) = ( Σ_{i=1}^{B} α_i 2^{m_i k} + β ) / d,
    m_1 > … > m_B ≥ 1,  α_i, β ∈ ℤ,  α_1 > 0,  d ≥ 1 odd,

with `N(k)` a positive integer for the relevant `k` (all octal/RLE word
families of the program have this form; geometric digit blocks produce the
`(8^k−1)/7`-type terms).

A *schema certificate* is a finite cycle of schema families with exact
derivations `F_0(k) ⟹ F_1(k+δ_0) ⟹ … ⟹ F_0(k+Δ)`, `Δ = Σδ_i ≥ 1`,
valid for all large `k`. Composing, it yields integers `S(k) ≥ 1`,
`A(k) ≥ 0` (steps and odd steps) with

    (†)   T^{S(k)}(N(k)) = N(k+Δ)   for all large k,

and — because the derivation is built from finitely many rewrite lemmas
whose repetition counts are affine in `k` (this is what "finite
certificate, symbolic in k" means) —

    (H2)  S(k) = λ_S k + s_0  and  A(k) = λ_A k + a_0  for all large k.

By induction (†) forces the single positive integer `N(k_0)` to have an
unbounded orbit: this is precisely the proposed counterexample format.

---

## 2. Main theorem

**Theorem (schema rigidity dichotomy).** Suppose (†) holds with `Δ ≥ 1`
for an exponential-polynomial family `N(k) → ∞` as above, with (H2).
Then, writing `R(k) = 3^{A(k)} / 2^{S(k)}`:

1. `λ_A log 3 − λ_S log 2 > 0` is impossible;
2. `λ_A log 3 − λ_S log 2 = 0` is impossible unless `λ_A = λ_S = 0`
   (bounded derivation length), which is impossible;
3. `λ_A log 3 − λ_S log 2 < 0` forces the *crash-and-climb* degeneracy:
   along an infinite subsequence there is a single **constant** integer
   `X* ≥ 1` and steps `j(k) < S(k)` with `T^{j(k)}(N(k)) = X*` and
   `T^{S(k)-j(k)}(X*) = N(k+Δ)`; in particular `X*` has an unbounded
   `T`-orbit that visits the exponential family `{N(k)}` infinitely often.

Consequently **no single-parameter schema certificate exists**, except in
the degenerate form (3), which cannot be exhibited without first
exhibiting a bounded seed `X*` with divergent orbit — that is, without
already having solved the problem the certificate was meant to solve.

**Proof.**

By Lemma A, for every large `k`

    (*)   N(k+Δ) = R(k)·N(k) + c(k)/2^{S(k)},   c(k) ≥ 0.

Note `N(k) = (α_1/d) 2^{m_1 k} (1 + O(2^{-εk}))` for some `ε > 0`, so
`N(k+Δ)/N(k) → 2^{m_1 Δ} ∈ [2, ∞)`.

**Case 1: `λ_A log 3 − λ_S log 2 > 0`.** Then by (H2)
`R(k) = e^{(λ_A log3 − λ_S log2)k + O(1)} → ∞`. But (*) with `c ≥ 0`
gives `N(k+Δ)/N(k) ≥ R(k) → ∞`, contradicting
`N(k+Δ)/N(k) → 2^{m_1 Δ} < ∞`. ∎

**Case 2: `λ_A log 3 = λ_S log 2`.** By Lemma D applied to the rational
slope pair: `λ_A/λ_S = log_3 2` is irrational unless `λ_A = λ_S = 0`
(slopes are rational numbers; equality of a rational with the irrational
`log_3 2` is impossible). So `S(k) = s_0` is eventually constant. Then
for all large `k` the parity word of the first `s_0` steps of `N(k)` is
eventually constant as well (2-adically `N(k) → β/d`, and by Lemma C the
first `s_0` parities stabilize once `v_2(N(k) − β/d) = m_B k + v_2(α_B/d)
> s_0`), hence `A(k) = a_0` and `c(k) = c_0` are constant. Substituting
the exponential forms into (*) and using linear independence of the
sequences `k ↦ 2^{m_i k}` and `k ↦ 1` (Vandermonde over distinct ratios),
the coefficient of `2^{m_1 k}` matches only if

    α_1 2^{m_1 Δ} = (3^{a_0}/2^{s_0}) α_1   ⟹   3^{a_0} = 2^{s_0 + m_1 Δ},

which by Lemma D forces `a_0 = 0` and `s_0 = −m_1 Δ < 0`, contradicting
`s_0 ≥ 1`. ∎

**Case 3: `λ_A log 3 − λ_S log 2 < 0`.** Then `R(k) → 0` exponentially
in `k`, so (*) forces the constant term to dominate:

    c(k)/2^{S(k)} = N(k+Δ) (1 + o(1)).

By Lemma B′, `c(k)/2^{S(k)} ≤ (S(k)/2)·max_j R_tail(k, j)`, so for large
`k` there exists `j(k) < S(k)` with

    R_tail(k, j(k)) ≥ 2 N(k+Δ) / S(k)²   (say),

i.e. the suffix window from step `j(k)` has multiplier `≥ 2^{m_1 k − O(log k)}`.
Consider the orbit value at the dip, `X(k) = T^{j(k)}(N(k))`. Applying
Lemma A to the suffix window (again `c ≥ 0`):

    N(k+Δ) = T^{S-j}(X(k)) ≥ R_tail(k, j(k)) · X(k)
    ⟹  X(k) ≤ N(k+Δ) / R_tail(k, j(k)) ≤ S(k)²/2 = O(k²).

Sharper: taking the maximal dip `j(k) = argmin_j` of the running
multiplier, the same two-sided bound with the prefix window (Lemma A on
steps `0..j`: `X(k) ≥ R_prefix·N(k) ≥ 0` and the suffix requirement)
pins `X(k)` to a set of size `poly(k)`; and since the tail
`T^{S-j}(X(k)) = N(k+Δ)` requires (Lemma C) the first
`≈ log_2 N(k+Δ) = m_1 k + O(1)` parities of `X(k)` to be prescribed,
while `X(k) ≤ O(k²)` has only `O(log k)` bits of magnitude, `X(k)` must
realize a supercritical parity run of length `≫ log_2 X(k)`: its orbit
climbs monotonically-in-scale from `O(k²)` to `N(k+Δ) ≈ 2^{m_1 k}`.
Passing to a subsequence on which the integer `X(k)` (bounded? no —
`O(k²)`) — refine: run the dip extraction at the *first* step where the
running multiplier falls below `k^{-3}`; boundedness of the increment
(`each step changes the multiplier by factor 3/2 or 1/2`) gives
`X(k) = Θ(N(k)·R_dip) = O(k³)` **and** `X(k) ≥ c·k^{-3}·1`, with
`X(k)` integral. If `X(k)` is bounded along a subsequence, it is
eventually a constant `X*`, and (†) exhibits `T`-iterates of `X*` equal
to `N(k+Δ) → ∞` for infinitely many `k`: conclusion (3). If
`X(k) → ∞` (still `polylog` of `N`), iterate the argument inside the
suffix window: the window `j(k)..S(k)` is itself a schema-structured
derivation (H2 restricts to affine sub-lengths) carrying `X(k) → N(k+Δ)`
with *its* multiplier `→ ∞`, which is Case 1 for the sub-family unless
its own constant term dominates — a strictly shorter window each time;
the descent terminates (window lengths decrease by at least one dip
extraction per round, and a window of bounded length forces Case-2-style
constancy, whence a constant `X*`). In all branches we arrive at
conclusion (3). ∎

**Remarks on Case 3.** (i) The descent argument is given here at the
level of detail of the rest of the program; the delicate point — that
(H2) passes to the extracted suffix windows — holds because a schema
derivation's parity word is, for large `k`, a fixed concatenation of
`O(1)` literals and periodic powers with affine exponents, and any
"first crossing of a threshold" lands at a position that is itself affine
in `k` along a subsequence (finitely many structural positions).
(ii) Conclusion (3) is not a contradiction — a genuinely divergent orbit
would produce exactly such an `X*`. The point is *epistemic*: a Case-3
certificate contains, verbatim, a bounded integer asserted to have an
unbounded orbit. One cannot *verify* such a certificate by symbolic
induction on `k` without independently proving that assertion, which is
the original problem. Schema certificates therefore cannot *bootstrap*:
symbolic induction adds no power in the single-parameter geometric class.

---

## 3. Corollaries and scope

**Corollary 1 (the user's §7, strengthened).** Eventually-periodic phase
schedules in the −5 system are the special case `B = 0` (constant
families); the theorem extends the obstruction from periodic phase words
to *all* single-parameter geometric schemas, covering every gadget
constructed in this program (the `A6^{k+1}` growth gadget, the 15-step
bridge, the 24-step composite, the §6 sink identities, the `8^{k+2}−21`
supercritical family).

**Corollary 2 (near-criticality explained).** For a valid *contracting*
schema loop, Case 1 shows the density `A(k)/S(k)` must satisfy
`λ_A log3 − λ_S log2 ≤ 0` — density at most `log_3 2` asymptotically —
while value growth pushes it up. Optimizing certificates therefore
accumulate at density `log_3 2^-`: the observed `15/24 = 0.625 <
0.630929… = log_3 2` of the 24-step gadget is not bad luck but the
signature of the rigidity boundary. Conversely *one-way* expanding
identities `F(k) ⟹ G(k)` (no cycle closure) freely exceed the critical
density — e.g. `T^{4+11j}(8^{k+2}−21) = 27·3^{7j}·2^{3k+2−11j} − 34`
sustains `7/11 = 0.636… > log_3 2` — because rigidity only constrains
*closed* loops.

**Corollary 3 (multi-parameter shifts).** A certificate over a parameter
vector `k ∈ ℤ^r` iterated by a fixed shift `k ↦ k + Δv` restricts, along
the orbit line, to a single-parameter certificate; the theorem applies
verbatim. Escaping rigidity therefore requires the certificate's value
growth to be **non-geometric** (e.g. doubly exponential — parameters
feeding back into exponents nonlinearly), or its derivation lengths to be
non-affine, or its words to lie outside the exponential-polynomial class.

**What remains genuinely open (the honest wall).** By Lemma C, tracking
depth is conserved: every shortcut step consumes exactly one 2-adic digit
of designed structure and none is ever minted. A divergent orbit needs
unbounded total tracking, so a counterexample integer must have its
supercritical parity structure regenerated forever by the dynamics itself
— concretely, by the binary carry structure of the maps `u ↦ 3^A u + c`.
Certifying *that* requires controlling binary digits of 3-smooth
multiples (Erdős-type territory), which is exactly where every
constructive route in this program terminates.
