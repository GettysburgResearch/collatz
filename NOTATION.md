# NOTATION.md — Frozen Definitions

Canonical notation for the symbolic-rewrite program (developed on
`gfreund123/math` branch `claude/collatz-symbolic-rewrite-2x60pa`,
HEAD `ff6992f`; continued here — issue #4). Definitions are transcribed
from the program documents cited per entry; those documents remain
authoritative for full context. See `CLAIMS.md` for the status of every
claim using these symbols.

**Freeze protocol.** These definitions are frozen: any change or
reinterpretation requires a pull request that (a) edits this file, (b)
records the change in `CLAIMS.md`, and (c) updates every dependent
claim's entry. New symbols are appended, never silently redefined.
(HANDOFF.md norm 5; README §16 lists NOTATION.md as a coordination
file.)

**Symbol collision warning.** `H` denotes the 64→81 digit-transfer map
(N2); `H(x)` with a real argument denotes the binary entropy function
(N8). `Lemma A/B` occur twice in the corpus: once in `RIGIDITY.md` §0
(constants of the affine form) and once inside Theorem 11
(`EQ.md`) — `CLAIMS.md` assigns them distinct IDs.

---

## N1. The shortcut Collatz map `T`

    T(n) = n/2            (n even)
    T(n) = (3n+1)/2       (n odd)

Extended to rationals with **odd denominator**: parity of `p/q` :=
parity of `p·q⁻¹ mod 2` = parity of `p` (since `q` is odd). Divergent
positive orbit ⟹ Collatz false.

Affine form on a parity class: for a parity word `w ∈ {0,1}^S` with
`A = Σwᵢ` ones, on the class of integers whose first `S` parities
are `w`,

    T^S(n) = (3^A n + c_w) / 2^S,
    c_w = Σ_{i: w_i=1} 3^{A−A(i+1)} 2^i,   A(j) = #ones among w_0..w_{j−1}.

Terras coordinates: the first `L` parities of `n` biject with
`n mod 2^L`. Tracking depth `v₂(n − ρ)` decreases by exactly 1 per
step and is never created (Lemma C, "fuel conservation").

Word convention (code): digit lists are LSD-first;
`value_word(digits, base) = Σ digits[i]·baseⁱ`.

Affine fixed point of a word `w` (length `p`, `a ≥ 1` ones):
`x_w = c_w/(2^p − 3^a)`, realizing `w^∞` (Lemma 1, sign-criticality:
supercritical ⟺ `3^a > 2^p` ⟺ `x_w < 0`).

*Sources:* `RIGIDITY.md` §0, `PAPER.md` §1, `experiments/core.py`.

## N2. The 64→81 collision map `H` and its charts

From the six-step collision `T⁶(64q+14) = T⁶(64q+15) = 81q+20`
(parity words 011101/111100, `B_u = 146`, `B_v = 65`), conjugating by
`Y = 17n + 146`:

    H(64B + ε) = 81B + ε,    ε ∈ {0,1},

defined on `A ∈ ℤ₂` whose low base-64 digit is in {0,1}. One H-step =
`T⁶` on the lifted integer; the class `A ≡ 6 (mod 17)` is invariant
(charts 0/8/3 analogous; chart classes are {6,0,8,3} mod 17, from the
four collision residues 14, 18, 54, 60 at L=6). Valid orbits grow
strictly: `A_{t+1} − A_t = 17B > 0` off the trivial digits.
The constant **17 = 81 − 64 = a − b**.

Generalized digit-transfer system (for multiplicatively independent
`a > b ≥ 2`, digit set `D ⊊ {0,…,b−1}`):

    H_{a,b,D}(bB + d) = aB + d,   d ∈ D,

with inverse branches `J_d(x) = (bx + (a−b)d)/a`. The Collatz L=6
subsystem is `(a,b,D) = (81, 64, {0,1})` in four charts. `M(a,b,D)`
denotes the master question: does `V∞(a,b,D) ∩ ℤ_{>0}` exceed the
trivial fixed digits?

*Sources:* `H64.md` (Verified exactly), `MINIMAL.md` (Setup),
`GENERAL.md` §1, `experiments/h64_system.py`.

## N3. The survivor set `V∞`

    V∞ = { A ∈ ℤ₂ : every H-iterate of A has base-64 digit ∈ {0,1} },

equivalently the attractor of the contractions
`J_ε(x) = (64x + 17ε)/81` on ℤ₂; homeomorphic to `{0,1}^ℕ`
(Theorem 2, coding). Generalized: `V∞(a,b,D) = {A : every
H_{a,b,D}-iterate has digit ∈ D}`.

*Sources:* `MINIMAL.md` (Setup), `H64.md` Theorem 2, `GENERAL.md` §1.

## N4. The coded residue sets `R_K`

    R_K = { A mod 64^K : A valid for K H-steps }   (|R_K| = 2^K),

the exactly `2^K` coded residues; explicitly, the residue of the digit
word `ε₀…ε_{K−1}` is the truncated 2-adic sum

    A(ε) = Σ_{t<K} 17 ε_t 64^t 81^{−(t+1)}   (mod 64^K).

Integers in `[1, 64^K]` valid for K steps are exactly the elements of
`R_K` read as integers. Recursion: `R_K = 81^{−1}(64·R_{K−1} + 17ε)`.

*Sources:* `MINIMAL.md` M3, `EQ.md` Theorem 7,
`experiments/minimal_survivors.py`.

## N5. The Fourier transform `S_K(θ)`

    S_K(θ) = Σ_{A ∈ R_K} e(θA/64^K),      e(x) := e^{2πix},

with the exact product formula (Theorem 7)

    S_K(θ) = Π_{t<K} (1 + e(θ c_t/64^K)),
    c_t = 17·64^t·81^{−(t+1)} mod 64^K,

so `|S_K(θ)|/2^K = Π_t |cos(π{θc_t/64^K})|`. `‖x‖` denotes distance
from `x` to the nearest integer. The **survivor (archimedean) range**
is `0 < |θ| ≤ 2^K`. **EQ** is the statement that the `R_K` are
archimedean-equidistributed at scale `64^K/2^K = 32^K` (see
`MINIMAL.md` M3 and `CLAIMS.md` C-0002).

*Sources:* `EQ.md` (Theorem 7 and preamble), `experiments/eq_attack.py`.

## N6. The atlas `D_L`

For `r ∈ [0, 2^L)`, `a_r` = number of odd steps among the first `L`
T-steps of `r` (Terras coordinate). Collision identity:

    T^L(2^L q + r) = 3^{a_r} q + T^L(r).

The level-L atlas is the supercritical non-injectivity locus of `T^L`:

    D_L = { r mod 2^L : ∃ s ≠ r, a_s = a_r, T^L(s) = T^L(r) },
    restricted to supercritical strata 3^{a_r} > 2^L.

`a_min` (per L) = least `a` with `3^a > 2^L`; `δ_L = a_min/L → log₃2`.

*Sources:* `GENERAL.md` §4, `experiments/atlas_spectrum.py` (docstring).

## N7. The atlas spectrum `γ_L` and fuel cost

    γ_L = log₂|D_L| / L,          cost(L) = (1 − γ_L)·L
    (bits of designed fuel per L-step block).

*Sources:* `GENERAL.md` §4, §7 (cost-floor theorem:
`γ_L ≤ H(log₃2) + o(1)`, per-step cost ≥ `1 − H(log₃2)`).

## N8. Constants and standard functions

* `H(x) = −x log₂ x − (1−x) log₂(1−x)` — binary entropy (argument
  form only; bare `H` is the map of N2). `H(log₃2) = 0.94996…`,
  `1 − H(log₃2) = 0.05004…`.
* `log₃2 = 0.63093…` — the critical odd-step density; a parity word
  of length `p` with `a` ones is **supercritical** iff `a/p > log₃2`
  (iff `3^a > 2^p`).
* `v₂`, `v₃` — 2-adic / 3-adic valuation. Tracking depth of `x`
  against `ρ`: `v₂(x − ρ)`.
* Spectrum-peak levels (`GENERAL.md` §4, stated there as CF-convergent
  denominators of `log₃2`): 6 (~2/3 doubled), 11 (↔ 7/11),
  19 (↔ 12/19), next 65.
* Negative integer T-cycles used throughout: −1 (density 1), −5 (2/3),
  −17 (7/11 > log₃2); the −17 cycle drives the `−21` family and the
  2-adic point of `z2adic_counterexample.py`.

*Sources:* `GENERAL.md` §§4,7, `RIGIDITY.md` §0, `PAPER.md` §1.
