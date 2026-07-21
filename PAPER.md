# A Symbolic-Rewrite Program for Collatz Divergence:
# Exact Amplifiers, Rigidity Theorems, and the 2-adic Mahler Boundary

*Consolidated account of the program on branch
`claude/collatz-symbolic-rewrite-2x60pa`. Every numbered claim is
machine-verified in exact arithmetic; the verifying script is cited
inline. Detailed proofs live in `RIGIDITY.md`, `H64.md`, `MINIMAL.md`,
`EQ.md`; logs in `experiments/results/`.*

---

## Abstract

We pursue the program of refuting the Collatz conjecture by a *finite
symbolic nontermination certificate*: finitely many rewrite lemmas,
valid for an unbounded parameter, whose induction would force one
positive integer to have an infinite orbit. Two exact rewrite
constructions are developed and fully verified: a three-phase amplifier
built on the negative cycle −5 → −7 → −10 of the shortcut map, and a
supercritical 64→81 collision subsystem built on a six-step collision
`T⁶(64q+14) = T⁶(64q+15) = 81q+20`. Both support genuine parametric
amplification lemmas, exact for every value of the parameter. Against
this, we prove a sequence of rigidity theorems showing that the natural
certificate formats cannot close: single-parameter geometric schemas
(dichotomy via `log₃2 ∉ ℚ`), all schemas inside the collision subsystem
(unique factorization alone), periodic and k-automatic schedules
(Cobham + Gelfond–Schneider), and statistical or analytic coincidence
(a 2-adic isometry theorem and Skolem–Mahler–Lech). The program
terminates at a single clean open statement — a 2-adic analogue of
Mahler's Z-number problem for 81/64 — together with an attackable
equidistribution problem (EQ) whose solution would make the emptiness
of survivors quantitative. Complete enumeration of all valid residues
to depth 20 (implicitly searching 1.3×10³⁶ integers) confirms every
prediction of the equidistribution model with no anomalies.

---

## 1. Setup

Shortcut map `T(n) = n/2` (even), `(3n+1)/2` (odd), extended to
rationals with odd denominator. Divergent positive orbit ⟹ Collatz
false. Terras coordinates: the first `L` parities of `n` biject with
`n mod 2^L` (`verify_outline.py` §2); **tracking depth `v₂(n − ρ)`
decreases by exactly 1 per step and is never created** (Lemma C,
`RIGIDITY.md` — "fuel conservation", the single most used fact below).

**Lemma 1 (sign–criticality; `amplifier_catalog.py`).** Every parity
word `w` (length p, a ≥ 1 ones) has a unique affine fixed point
`x_w = c_w/(2^p − 3^a)`, `c_w > 0`, realizing `w^∞`; hence `x_w < 0 ⟺
3^a > 2^p`. *Negative rational cycles are exactly the supercritical
amplifiers; positive ones are all subcritical sinks.* (Verified over
all 32,752 words, p ≤ 14.) Integer negative cycles: −1 (density 1),
−5 (2/3), −17 (7/11 > log₃2 = 0.63093).

## 2. The first construction: the −5 phase system

The submitted construction (radix rewrite `b_i, t_j`; radix-replacement
`T^L(2^L x + r) = 3^a x + c`; three phases A/B/C with nine state rules;
carry normalization) verifies exactly in every part
(`verify_outline.py`, ALL PASS), including the growth gadget
`A6^{k+1} ⟹ B5^k7 ⟹ C3^{k−1}501 ⟹ B6^{k−2}0611` (9 steps, all k) and
the 15-step bridge lemma with parity word `101111110000011` (template
−97/7). One sharpening: the bridge's value identity holds already at
m = 4; sharpness is at m = 3.

A symbolic block calculus (stable carries, transient ≤ 2, block digits
permuted by `(0)(124)(365)(7)`; `blockmachine.py`) executes the system
on run-length-encoded words with a pumped block. A sweep of 14,016
symbolic seeds found **no self-similar in-system loop with δ ≥ 0**
(which would have been a counterexample) and cataloged all exits.

**Splice census (`splice_search.py`).** Each exit family converges
2-adically to a rational template whose landing cycle decides its fate
(Lemma 1). Of 13,944 exits: 10,512 sink at 5/7 (the submitted gadget's
fate), 1,664 at 1↔2, and **1,768 land on negative cycles** — the
mechanism being that the octal digit 7 is carry-invariant and
unconsumable, so 7-blocks always exit into deep negative-integer
neighborhoods. This is the splice class the original §5 was missing,
and it yields the corrected one-line supercritical amplifier
(`neg21_family.py`):

    T^{4+11j}(8^{k+2} − 21) = 27·3^{7j}·2^{3k+2−11j} − 34,   0 ≤ 11j ≤ 3k+2,

riding the −17 cycle at density 7/11 > log₃2 for its whole stored
depth (e.g. k = 33: 103 steps, 66 odd, 105 → 107 bits, *expanding* —
versus the original 24-step gadget's ×0.855 contraction). Steering
before exhaustion is free (CRT); after exhaustion it is provably
impossible (value forced ≡ −34 mod 2^e). Any *finite* tower of stages
is constructible; closure of an infinite tower is the entire problem.

## 3. Rigidity I: the schema dichotomy (`RIGIDITY.md`, `rigidity_check.py`)

**Theorem (dichotomy).** For any single-parameter schema family (values
exponential-polynomial in k — exactly the RLE word families) with
affine step counts, an expanding certificate identity
`T^{S(k)}(N(k)) = N(k+Δ)`, Δ ≥ 1, is impossible unless it degenerates
to a constant bounded integer asserted to have an unbounded orbit
(circular). Ingredients: `c ≥ 0`; the suffix-multiplier bound; linear
independence of geometric sequences; irrationality of log₃2.
Search confirms: 0 expanding identities, 84 contracting ones in range.

Corollaries: the periodic-schedule obstruction (§7 of the submission)
extends to all geometric schemas; optimizing certificates accumulate at
density log₃2⁻ (observed 15/24 = 0.625 — the near-miss was structural,
not bad luck); fixed-shift multi-parameter certificates reduce to the
single-parameter case along orbit lines.

## 4. The 2-adic boundary of the first construction

The route *does* produce counterexamples — in ℤ₂
(`z2adic_counterexample.py`): an explicit computable `Z` (Terras
inverse of the −17-cycle parity word with aperiodic defects,
gcd(173,11) = 1) whose orbit has density ≥ 7/11 forever, provably on no
cycle; every truncation `Z mod 2^B` is a positive integer with an
exact supercritical certificate of length B (at B = 2000: 1995 → 2021
bits). Collatz is precisely the statement that no such point lies in
ℤ. Post-exhaustion measurements (`free_fuel_test.py`): 0 of 26 free
windows supercritical, mean density 0.4999 — the dynamics mints no
fuel. Record hunt (`free_fuel_records.py`): the supercritical-horizon
ratio record is n = 27 with L* = 63 = 13.25× its designed bits,
unbeaten through 2×10⁶.

## 5. The second construction: the 64→81 collision subsystem (`h64_system.py`)

The six-step collision `T⁶(64q+14) = T⁶(64q+15) = 81q+20` (words
011101/111100, B_u = 146, B_v = 65) conjugates via `Y = 17n+146` to

    H(64B+ε) = 81B+ε,  ε ∈ {0,1},   class A ≡ 6 (mod 17) invariant,

with one H-step = T⁶ on the lifted integer and strict growth. All of
the submitted §§1–9 verify, plus: the **four-chart atlas is complete**
(census: the only supercritical collisions at L = 6 are the four t = 1
pairs at residues 14, 18, 54, 60); **H is injective** — the collision
discount (5 designed bits per 6 steps instead of 6) happens exactly
once, no second level; the unified atlas frame has 8/64 valid residues
(**3 bits per block**, the best frame found) with measured continuation
exactly Geometric(1/8) and record natural runs matching the null at
every scale probed (`atlas_runs.py`, to 3×10⁷). The carry nine-cycle
(×19 mod 81) yields the exact stack amplifier
`H^{9m+1}(S_m(x)) = 81^{9m}(81x+1)`, fully lifted to Collatz integers,
and an explicit steered two-stage tower verified as T¹⁷⁴ on a 180-bit
integer. No Wieferich luck: `ord(64 mod 81^k)` is generic, so level-k
gadgets have length 9·81^{k−1}.

## 6. Rigidity II: the H-frame theorems (`h64_theory.py`)

**Theorem 1 (H-rigidity).** `A_S = (81^S A₀ − 17C)/64^S` with
`0 ≤ 17C ≤ 81^S` pins every valid orbit two-sidedly to `(81/64)^S`;
an expanding exp-poly identity forces S eventually constant and then
`81^S = 64^{S+mΔ}` — impossible. *No hypothesis on S(k) at all*: the
subsystem freezes density, and the entire dichotomy of §3 collapses to
three lines by unique factorization.

**Theorem 2 (coding).** `V∞ = {A ∈ ℤ₂ : all H-iterates have digit ∈
{0,1}} ≅ {0,1}^ℕ`; periodic codes are the rationals
`17C_w/(81^p−64^p) ∈ [0, 81/17]`, whence a one-line proof that the
only integer valid cycles are the digits 0, 1.

**Theorem 3 (automaticity/Cobham).** The regeneration residues of the
stack tower satisfy `r_m mod 64^j =` function of `m mod 2^{6j−4}`
(exact period — all arithmetic data of a certificate is 2-automatic),
while the required schedule has transcendental gap-frequency
(Gelfond–Schneider on log₆₄81) and by Cobham's theorem is not
k-automatic for any k. The certificate's two halves live in provably
different complexity classes; the surviving format is
Sturmian/Ostrowski-computable, outside every Cobham class.

**Theorem 4 (schedule locking; `schedule_demands.py`).** Periodic-gap
schedules lock demands only to depth `(v₂(G)+4)/6` (bounded); Sturmian
schedules never lock but their demand stream is exactly
Ostrowski-computable. Closure is a supply≡demand fixed point.

## 7. Rigidity III: the supply stream (`supply_stream.py`)

**Theorem 5 (supply isometry).** First-step validity of `81^N u` is
pure coset arithmetic (possible iff `u ≡ 1 mod 16`, then density 1/4 —
an 8× boundary enhancement; otherwise density 0). Beyond:
`M ↦ (81^{4M}−1)/64` is a **2-adic isometry** (LTE:
`v₂(81^{4d}−1) = 6 + v₂(d)`), so every deeper validity event has
*exactly* generic density `1/32`. Confirmed by exact class counts
64 → 128 → 256 → 512 → 1024 → 2048 (depth 6). Ensemble statistics are
provably useless to a certificate.

**Theorem 6 (SML).** Demands are ≡ 0 (mod 16); one digit of unsteered
agreement already needs the designed coset `x ≡ 15 (mod 16)`
(conditioned agreement measured exactly generic: 0.24975 vs 1/4).
Unbounded-depth coincidences are zeros of a nondegenerate three-term
power sum — finite by Skolem–Mahler–Lech. All but finitely many stages
require active steering.

## 8. The minimal statement (`MINIMAL.md`, `minimal_survivors.py`)

Everything funnels into:

* **M1:** does `V∞` contain a positive integer in a chart class mod 17?
  (Yes ⟹ Collatz false, explicitly.)
* **M2:** equivalently, a **2-adic Mahler Z-number problem** for 81/64
  with digit set {0,1}. The FLP interval obstruction does not transfer
  (measure 1/32 > 1/81); the real-side IFS attractor is all of [0,1]
  — there is provably no archimedean obstruction.
* **M3 (counting):** integers valid for K steps are exactly the `2^K`
  coded residues `R_K`; the quantitative question is how small a
  nontrivial element of `R_K` can be. Equidistribution (**EQ**)
  predicts `≍ 32^K`.

Complete enumeration to K = 20: `|R_K| = 2^K` exactly; the minimum
nontrivial survivor tracks `32^K` within a factor [0.19, 1.9] with no
drift; the extremal K = 20 survivor (101 bits) exceeds its fair window
by only 1.19×; tail counts match equidistribution exactly (4 vs 4.0;
16,397 vs 16,384); chart classes independent (0.2352 vs 4/17). No
anomalies anywhere.

## 9. The attack on EQ (`EQ.md`, `eq_attack.py`)

EQ is the program's one isolated attackable problem. The attack so far
(see `EQ.md` for statements, proofs, and numerics): an exact **product
formula** for the Fourier transform of `R_K`,

    S_K(θ) = Π_{t<K} (1 + e(θ c_t / 64^K)),   c_t = 17·64^t·81^{−(t+1)} mod 64^K,

reducing EQ to lower bounds on the number of "far" terms of the
backward geometric orbit `17θ·81^{−(t+1)}`. Results: the full-range
worst case is exactly `cos(π/64)` at `θ = 64^{K−1}` — so EQ is
necessarily an archimedean-range statement (`|θ| ≤ 2^K`), as the
counting application demands; the **cascade lemma** (consecutive
degenerate terms force an exact 81-divisibility chain, runs ≤
`1 + log₈₁(δ·64^{K−t})`; 0 violations in 2000 random frequencies)
confines adversarial frequencies to 81-power-structured θ of size
≫ 2^K, outside the survivor range; within the range, the Erdős–Turán
discrepancy sum decays 0.367 → 0.0063 (K = 6 → 16). The remaining gap
is a pointwise bound in the survivor range, shown in `EQ.md` to be the
exact Fourier dual of the supply-digit problem (self-dual with M2 at
worst case, provably true on average by Parseval) — a
sum-product/self-similar-Fourier-decay configuration, the program's
hand-off point to modern harmonic analysis.

## 10. Conclusions

The two constructions are real: exact, parametric, supercritical
amplifiers exist in abundance, and every finite schedule of them is
constructible inside Collatz. The certificate formats that would close
them are dead by seven theorems whose union is: *every finite-format
induction either implies a rational value of an irrational (or
transcendental) constant, or presupposes a bounded divergent seed, or
demands data provably outside its own complexity class, or relies on
statistics that are provably exactly generic, or on coincidences that
are provably finite.* What remains is M1/M2 — the 2-adic Mahler
problem — with EQ as its quantitative shadow. The program's empirical
layer is fully consistent with its theorems: across every frame, scale
and statistic measured, the dynamics behaves exactly like its null
model, with n = 27 as the lone (and model-consistent) windfall.

*Open problems:* (1) EQ — Fourier decay for the twisted self-similar
sets `R_K`. (2) The individual-orbit normality statement for 81-power
orbits (Furstenberg ×64/×81 territory). (3) Whether any of the modern
measure-rigidity results (Rudolph, Shmerkin–Wu) can be made to say
anything about `V∞ ∩ ℤ`.
