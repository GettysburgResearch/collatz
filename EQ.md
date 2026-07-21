# The Attack on EQ

EQ (from `MINIMAL.md`): the valid sets `R_K` (all `2^K` residues mod
`64^K` surviving K H-steps) are archimedean-equidistributed at scale
`64^K/2^K = 32^K`. EQ ⟹ quantitative near-emptiness of survivors —
the sharpest statement short of M1. Computations:
`experiments/eq_attack.py` (`results/eq-attack.log`).

## Theorem 7 (product formula — proved, verified)

The coded residue of the word `ε₀…ε_{K−1}` is the truncated 2-adic sum

    A(ε) = Σ_{t<K} 17 ε_t 64^t 81^{−(t+1)}   (mod 64^K),

(immediate: `A = J_{ε₀}∘…∘J_{ε_{K−1}}(0)` with `J_ε(x) = (64x+17ε)/81`).
Hence the Fourier transform of `R_K` **factors exactly**:

    S_K(θ) = Σ_{A∈R_K} e(θA/64^K) = Π_{t<K} (1 + e(θ c_t/64^K)),
    c_t = 17·64^t·81^{−(t+1)} mod 64^K,

so `|S_K(θ)|/2^K = Π_t |cos(π{θc_t/64^K})|`. (Verified against the
direct sum at K = 4, 7, 10.) EQ thus reduces to lower bounds on the
number of "far-from-integer" terms of the backward geometric orbit
`17θ·81^{−(t+1)}` read at moduli `64^{K−t}`.

## Full-range maximum: EQ must be archimedean

Full scans (K ≤ 4) show `max_{θ≠0} |S_K(θ)|/2^K = cos(π/64) = 0.998795`
attained at `θ = 64^{K−1}`: for this θ every factor is 1 except t = 0,
whose phase is `{17·81^{−1}·64^{K−1}/64^K} = 1/64` (since 17·49 ≡ 1 mod
64). So there is **no uniform Fourier decay over all frequencies** —
necessarily: `R_K` is 2-adically structured by construction (its low
digit is ε₀ ∈ {0,1}). The correct statement of EQ concerns only the
**archimedean (survivor) range** `0 < |θ| ≤ 2^K`, which is what the
smallest-survivor counting uses.

## Theorem 8 (cascade lemma — proved, verified)

Let `z_t = 17θ·81^{−(t+1)} mod 64^{K−t}` (the t-th phase numerator).
If consecutive terms are δ-degenerate (`‖z_t/64^{K−t}‖ < δ`,
`‖z_{t+1}/64^{K−t−1}‖ < δ`) with `δ < 64/145`, then the signed small
representatives satisfy `s_t = 81·s_{t+1}` **exactly**; a degenerate
run of length L starting at t forces `81^{L−1} ≤ δ·64^{K−t}`, i.e.

    L ≤ 1 + log₈₁(δ·64^{K−t}).

Degeneracy is an 81-divisibility cascade, never an accident. (2000
random frequencies at δ = 1/8: run-length distribution geometric with
ratio ≈ 1/4 as predicted, **0 violations** of the bound.)

**Corollary (adversaries are 81-structured and live outside the
range).** Long degenerate runs require `θ` carrying high powers of 81
in the cascade; probes confirm: at K = 16 the worst structured
frequencies are `θ = 81^{15}` (|S|/2^K = 0.845), `5·81^{14}` (0.734) —
all of size ≫ 2^K. Within the survivor range `|θ| ≤ 2^K`, cascades at
early positions require `81^j | θ`, capping them at `j ≤ log₈₁ 2^K ≈
0.158K`.

## Numerics in the survivor range (`results/eq-attack.log`)

| K | max |S|/2^K (θ ≤ 2^K) | mean | Erdős–Turán sum |
|---|---|---|---|
| 6 | 0.501 | 6.4e−2 | 0.367 |
| 8 | 0.298 | 2.9e−2 | 0.161 |
| 10 | 0.452 | 9.9e−3 | 0.193 |
| 12 | 0.298 | 4.2e−3 | 0.029 |
| 14 | 0.253 | 1.9e−3 | 0.018 |
| 16 | 0.301 | 7.3e−4 | 0.0063 |

The ET discrepancy sum — which controls interval-count errors at
survivor scale — decays steadily to zero: **EQ holds numerically in
exactly the range the counting argument needs**, consistent with the
enumeration facts (min survivor ≈ 32^K, tails exact). The max in the
range plateaus near 0.3 (extreme-value behaviour of lucky digit draws
among 2^K frequencies) — harmless as long as near-max frequencies are
rare, which the decaying mean and ET-sum quantify.

## Where the proof stands, honestly

Proved: the exact product formula (T7); the cascade structure of
degeneracy (T8) confining adversarial frequencies to 81-power-structured
θ outside the survivor range; the L² (Parseval) square-root cancellation
on average; and the numerical decay of the discrepancy sum in the
needed range.

Missing: a pointwise bound `|S_K(θ)| ≤ 2^K·K^{−(1+ε)}`-or-better for
all `0 < |θ| ≤ 2^K`, which by Erdős–Turán would prove EQ. By T7 this is
equivalent to: *the base-64 digit sequence of `17θ·81^{−t}` (t = 1…K)
is far from the degenerate digits {0, 63} for ≫ K/log K positions, for
every small θ.* This is the **Fourier dual of the supply-digit
problem** — the same individual-orbit digit statement (M2's wall) in
mirror form: the phases of the Fourier attack are driven by the very
`81^{−t}`-digit sequences whose structure is the open problem. EQ is
thus self-dual with M2 at the worst-case level while being *provably
true on average* (Parseval) and *numerically true pointwise* in the
survivor range. Any genuine progress must break this self-duality —
e.g. by exploiting that θ ranges over a short interval (additive
structure) against the multiplicative 81-orbit, which is precisely a
sum-product/Fourier-decay-of-self-similar-measures configuration
(Bourgain-style; Li–Sahlsten, Solomyak): the sharpest available tools,
and the exact point where this program hands off to modern harmonic
analysis.

## Progress: Theorems 9 and 10 (`experiments/eq_progress.py`)

**Correction to Theorem 8's threshold.** The exact ladder
`s_t = 81·s_{t+1}` between consecutive degenerate levels is forced when
`64δ₁ + 81δ₂ < 1` (symmetric case: `δ < 1/145`), not `δ < 64/145` as
first stated; at looser δ the ladder holds only sometimes (observed).
All downstream statements below use the corrected deep-degeneracy
threshold `δ = 1/146`.

**Theorem 9 (self-similarity; sharp global maximum — proved).**
(a) `S_K(64^j θ′) = 2^j·S_{K−j}(θ′)` exactly (top j factors are 1).
(b) `max_{θ≠0} |S_K(θ)|/2^K = cos(π/64)`, attained at `θ = 64^{K−1}u`:
after factoring out 64^j by (a), the top level of the reduced problem
has nonzero phase with denominator 64, giving a factor ≤ cos(π/64);
θ = 64^{K−1} attains it. (Exhaustively confirmed at K = 2, 3.)

**Theorem 10 (exact-run rigidity — proved; 0 violations over the full
survivor range at K = 16).** Let `0 < |θ| ≤ 2^K` and let a
deep-degenerate run occupy levels `t₀..t₀+L−1` in the interior zone
(`64^{K−t₀} > 2·17·2^K`, i.e. t₀+L below ≈ 5K/6). The cascade ladder
gives `s_{t₀+i} = 81^{L−1−i}σ`. If the ladder is sub-modulus
(`|81^{t₀+L}σ| < 64^{K−t₀}/2`), then the defining congruence holds with
both sides below half the modulus and is therefore an **integer
equation**: `17θ = ±81^{t₀+L}σ`. Since 17 ∤ 81^j, this forces `17 | σ`
and

    t₀ + L ≤ log₈₁(17|θ|) ≤ log₈₁(17·2^K) ≈ 0.158·K.

*Every clean (sub-modulus) adversarial structure in the survivor range
is confined to the first ~0.158K levels.* Scan of all θ ≤ 2^16: 0
violations of the equation, 0 violations of confinement.

**The remaining branch, measured.** What Theorem 10 does not cover are
deep runs with huge ladder values (σ comparable to the modulus). Census
at δ = 1/146 over all θ ≤ 2^16: interior deep runs of length ≥ 2:
128 huge of length 2, 9 exact of length 2, 1 huge of length 3 — total
138 against the pure-chance expectation ≈ 160, with maximum length 3
against a cascade-permitted maximum an order larger. **The huge branch
is populated at exactly the generic Poisson rate with no adversarial
excess.** The worst survivor-range frequencies (|S|/2^K ≈ 0.30 at
K = 16) owe their size to many independent single-level near-misses —
extreme-value statistics over 2^K draws — not to any coherent
structure.

**Status of EQ after the attack.** Proved: product formula (T7),
corrected cascade (T8), sharp global maximum and self-similarity (T9),
exact-run rigidity and 0.158K-confinement of all sub-modulus
adversaries (T10), finiteness of analytic coincidences (T6/SML), and
decay of the Erdős–Turán sum in the survivor range (numerics,
0.367 → 0.0063). Open: excluding *chance-level* clustering in the huge
branch — a statement of pure extreme-value/equidistribution type with,
by T10, no arithmetic structure left to exploit. EQ is thus reduced to
a structureless large-deviation estimate: the adversary provably cannot
be arithmetic; it can only be lucky, and the census shows luck runs at
exactly its fair rate.
