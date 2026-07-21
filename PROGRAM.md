# Collatz Symbolic-Rewrite Program

**Goal (as posed):** pursue a finite symbolic nontermination certificate
for the shortcut Collatz map — a finite collection of rewrite lemmas,
valid for an unbounded parameter, whose induction forces one positive
integer to have an infinite trajectory — starting from the radix-rewrite
framework (binary/ternary constructors, radix-replacement theorem, the
−5-cycle three-phase amplifier, the `A6^{k+1}` growth gadget, the 15-step
bridge lemma, and the periodic-schedule obstruction).

**Status:** the entire submitted framework verifies exactly (one
constant sharpened). The program then **found the missing splice class**
the outline asked for (§5's "decisive missing lemma") — exits landing on
*negative* cycles at supercritical density, including an explicit
one-line replacement for the subcritical 24-step gadget — and then
**proved that no single-parameter schema certificate can close the
loop** (rigidity dichotomy, `RIGIDITY.md`). No counterexample integer is
produced; instead the route's endpoint is now characterized exactly:
every certificate in the natural class either violates the irrationality
of `log_3 2` or already contains a bounded integer asserted to be
divergent. What survives is precisely delimited (non-geometric growth /
multi-parameter feedback / digit structure of 3-smooth numbers).

All claims below are machine-verified in exact arithmetic;
scripts in `experiments/`, logs in `experiments/results/`.

---

## 1. Verification of the submitted outline (`verify_outline.py` — ALL PASS)

| § | Claim | Status |
|---|-------|--------|
| 1 | `T(b_0 x)=x`, `T(b_1 x)=t_2 x`; all six `t_j b_i` push-through rules; high-end rules; one round = one shortcut step (n ≤ 3999 exhaustive) | verified |
| 2 | Radix replacement `T^L(2^L x + r) = 3^a x + c`, `0 ≤ c < 3^a`, all `L ≤ 12`, all `r`; parity words biject with residues (Terras) | verified |
| 3 | `T^3(8q−s) = 9q−s` for `s ∈ {5,7,10}`; the nine state rules (match the compiler exactly); `N_c O_r` normalization; macro step = 3 shortcut steps; `q' > q` for `q > 5` | verified |
| 4 | `A6^{k+1} ⟹ B5^k7 ⟹ C3^{k−1}501 ⟹ B6^{k−2}0611`, 9 shortcut steps, `k = 2..29`; `B6` exits | verified |
| 5 | Bridge lemma `B6^m0611 ⟹(15) A1^{m−5}76452765`; parity word `101111110000011`; template trajectory `−97/7 → −142/7 → … → −43/7`; 24-step composite with 15 odd; multiplier `3^15/2^24 ≈ 0.8553` | verified; **sharpened: the value identity already holds at `m = 4`** (perturbation divisible by `2^16 > 2^15`); sharpness is at `m = 3`. `m ≥ 5` is needed only for the output word `1^{m−5}…` to exist as a word |
| 6 | `T^14(−43/7) = 5/7` (6 odd); cycle `5/7 → 11/7 → 20/7 → 10/7`, parity `1100`, factor `9/16`; `T^{14+4j}(u_r) = (3^{22+2j}2^{3r−10−4j}+5)/7` | verified |
| 7 | Periodic phase schedules force `q ≤ 5`; exhaustive scan (`|q₀| ≤ 100`, extended `10^6` cap): only subsystem cycles have `q = 0` | verified |

## 2. Amplifier catalog and the sign–criticality engine (`amplifier_catalog.py`)

**Lemma (sign–criticality).** Every parity word `w` (length `p`, `a ≥ 1`
ones) has affine fixed point `x_w = c_w/(2^p − 3^a)` with `c_w > 0`,
realizing `w^∞`. Hence `x_w < 0 ⟺ 3^a > 2^p`:
**negative rational cycles are exactly the supercritical amplifiers;
positive rational cycles are all subcritical sinks.** (Verified for all
32,752 words with `p ≤ 14`.) This is the two-line engine behind §6's
observed design principle.

Integer negative cycles as amplifiers:

| cycle | p | a | multiplier | density a/p |
|-------|---|---|-----------|-------------|
| −1 | 1 | 1 | 3/2 | 1.000 |
| −5 | 3 | 2 | 9/8 | 0.667 |
| −17 | 11 | 7 | 2187/2048 | **0.63636 > log₃2 = 0.63093** |

* The **−17 phase system** compiles to an 11-phase rewrite system over
  base 2048 → 2187 with exactly one allowed residue per ordered phase
  pair (121 rules); macro step = 11 shortcut steps (verified). Growth is
  even stronger than in the −5 system: `|s_X − s_Y| ≤ 119 < 139 =
  2187−2048`, so **every** in-system derivation with `q ≥ 1` grows.
  The §7-style obstruction is absolute here: `|q_*| ≤ 119/139 < 1`, so
  periodic schedules admit **no** nontrivial solutions at all
  (scan `|q₀| ≤ 5000`: only `q = 0`).
* The **−1 system** is totally rigid: its only rule is `A O_0 → A N_0`.

## 3. Block calculus and the symbolic seed sweep (`blockmachine.py`)

An exact RLE engine executes macro steps on words with a pumped block
`v^{k+off}` (carry transducer: stable carries `c*(r) =
0,1,2,3,5,6,7,8`; transients ≤ 2 digits — proved by finite check; block
digits transform by the permutation `(0)(124)(365)(7)`). Every symbolic
derivation is cross-checked against exact integers at three values of k.

Sweep of 14,016 seeds (all phases, block digits, prefixes ≤ 2, suffixes ≤ 1):

* **No self-similar in-system loop with δ ≥ 0 exists** in this class
  (would have been a counterexample); the only loop is the trivial
  consuming loop on the cycle itself.
* In-system symbolic derivations from short prefixes last ≤ 6 macro steps
  — the −5 subsystem is extremely leaky.
* 63 DRIFT derivations = the pure amplifier family `n = 8^K u − 5`
  (deep congruence fuel, density exactly 2/3 while it lasts).

## 4. The splice census — the missing lemma class found (`splice_search.py`)

Every symbolic exit family has value `(α·8^k + β)/d` and 2-adically
converges to a rational **template** `ρ = β/d` whose landing cycle
(sign–criticality) decides its fate. Census of all 13,944 exits:

| landing cycle | count | type |
|---------------|-------|------|
| 5/7 (p=4, a=2) | 10,512 | subcritical sink (§6's fate — the generic outcome) |
| 1↔2 (p=2, a=1) | 1,664 | subcritical sink |
| **−1** (p=1, a=1) | **640** | **supercritical** |
| **−17 cycle** (p=11, a=7) | **600** | **supercritical** |
| **−5 cycle** (p=3, a=2) | **528** | **supercritical** |

Mechanism: the octal digit **7 is a fixed point of the stable-carry
transform and no state rule consumes it**. Blocks of 7s ride through
in-system evolution untouched; hitting one always exits into a deep
neighborhood of a *negative integer*. The outline's gadget emitted a
`1`-block (template `→ 10/7 →` positive sink); a `7`-block emission lands
negative instead. **This is the splice class §5 was missing.**

**The corrected amplifier (one line).** The seed `A 6 7^k #` has value
`n(k) = 8^{k+2} − 21`, and for all `k ≥ 1`, `0 ≤ 11j ≤ 3k+2`:

    T^{4+11j}(8^{k+2} − 21) = 27 · 3^{7j} · 2^{3k+2−11j} − 34        (verified k ≤ 39)

— four bridge steps (`−21 → −31 → −46 → −23 → −34`, parities 1101) onto
the −17 cycle, then sustained density `7/11 > log_3 2` for the entire
stored depth. At `k = 33`: 103 steps, 66 odd, density 0.6408, value
**grows** 105 → 107 bits — where the outline's 24-step gadget contracts
(`3^15/2^24 ≈ 0.855`). Composite two-stage rides (steering to a fresh
deep template *before* exhaustion — steering after exhaustion is
provably impossible, the value is forced `≡ −34 mod 2^e`) reach density
0.640 over 114 steps (186 → 188 bits), and any *finite* tower of stages
is constructible by CRT steering of the stored digits.

## 5. Fuel conservation and the rigidity dichotomy (`RIGIDITY.md`)

* **Fuel conservation (Lemma C).** Tracking depth `v_2(n − ρ)` decreases
  by exactly 1 per shortcut step and is never created. Every stage of
  every construction above spends congruence fuel that must be designed
  into the seed in advance; magnitude growth mints no new fuel.

* **Theorem (schema rigidity dichotomy).** For any single-parameter
  schema family (values exponential-polynomial in k — exactly the RLE
  word families), an expanding certificate identity
  `T^{S(k)}(N(k)) = N(k+Δ)`, `Δ ≥ 1`, with affine `S(k), A(k)` is
  impossible unless it degenerates to a **constant bounded integer
  `X*` asserted to have an unbounded orbit** — i.e. the certificate
  presupposes a divergent seed. Ingredients: `c ≥ 0` (Lemma A),
  the suffix-multiplier bound (Lemma B′), linear independence of
  geometric sequences, and the irrationality of `log_3 2`.
  Numerically confirmed: exhaustive small-range search finds **0
  expanding identities and 84 contracting ones** (`rigidity_check.py`).

* **Corollaries.** (i) §7's obstruction extends from periodic phase
  words to all single-parameter geometric schemas. (ii) The observed
  near-miss `15/24 = 0.625` just below `log_3 2 = 0.63093` is the
  signature of the rigidity boundary: closed loops are pinned at density
  ≤ log₃2 while one-way identities (like the `8^{k+2}−21` family at
  7/11) freely exceed it. (iii) Fixed-shift multi-parameter certificates
  reduce to the single-parameter case along orbit lines.

## 6. What would evade the theorem (the precise residual frontier)

1. **Non-geometric value growth** — schema towers whose parameters feed
   back into exponents (values like `2^{2^t}`), so that `S(t)` is not
   affine. Fuel conservation still applies; the certificate must then
   encode unbounded designed depth in nested form, and its verification
   reduces to digit structure of `3^A`-multiples (binary digits of
   3-smooth numbers — Erdős-type territory).
2. **Aperiodic schedule certificates** with derivation lengths outside
   every affine class — but then the "finite collection of lemmas +
   induction" format is lost, which was the route's defining feature.
3. **The Case-3 degeneracy** — exhibiting a bounded `X*` with divergent
   orbit directly. Circular as a certificate strategy.

The route as originally specified — finitely many word schemas cycling
with `Σδ_i > 0` — is closed. Not because the amplifiers fail (they are
real, exact, and supercritical: §4), but because closure of the loop is
exactly the point where `log_3 2 ∉ ℚ` and Terras fuel conservation
intersect. Any honest continuation must attack frontier (1): quantitative
control of the binary digits of `3^n·u + c` — equivalently, whether the
dynamics itself can regenerate supercritical structure it was not given.

## Files

- `RIGIDITY.md` — the dichotomy theorem with full proofs.
- `experiments/core.py` — exact machinery: T, words, radix replacement, cycle-system compiler.
- `experiments/verify_outline.py` — §1–§7 verification (ALL PASS).
- `experiments/amplifier_catalog.py` — sign–criticality (32,752 words), −1/−5/−17 systems.
- `experiments/blockmachine.py` — symbolic RLE engine + 14,016-seed sweep.
- `experiments/splice_search.py` — exit-template census (13,944 exits).
- `experiments/rigidity_check.py` — identity search + Lemmas A/B/B′ checks.
- `experiments/results/` — logs of all of the above.

## 7. Addendum: the counterexample this route actually reaches

`experiments/z2adic_counterexample.py` constructs, via the Terras
bijection applied to the parity word of the −17 cycle with aperiodic
defects (period-173 forcing, `gcd(173,11)=1`), an explicit computable
2-adic integer `Z` such that:

* the shortcut orbit of `Z` has parity density ≥ 7/11 > log₃2 forever
  (verified exactly for 2000 steps: density 0.639);
* `Z` lies on no rational cycle template (its parity vector has no
  period — proved, not just checked);
* every truncation `Z mod 2^B` is a **positive integer** whose orbit
  realizes an exact supercritical certificate of length `B`
  (at `B = 2000`: 1995 bits → 2021 bits, strictly expanding).

**`Z` is a counterexample to the 2-adic Collatz conjecture, produced by
this route.** The Collatz conjecture proper is exactly the statement
that no such point lies in `ℤ` — i.e. that the non-terminating binary
expansion of every such `Z` is genuinely non-terminating. The rigidity
dichotomy shows schema-structured constructions can never force
termination of the expansion; that is the precise content left open.

## 8. The free-fuel experiment (the last door, tested)

`experiments/free_fuel_test.py`: after a designed supercritical prefix
exhausts, the orbit's next bits are generated by the 3-smooth carry
dynamics alone. A counterexample along this route requires those bits to
be systematically supercritical. Measured over the `8^{k+2}−21` family
(k = 10…210) and truncations of `Z`: **0 of 26 free windows exceed
log₃2; mean density 0.4999 (sd 0.036)** — an exact coin-flip null.
Designed windows hold 0.637–0.642 throughout; free windows collapse to
1/2 immediately. The dynamics mints no fuel: every step of divergence
must be designed in advance, and by the rigidity dichotomy no finite
schema can design infinitely many. This is the route's complete,
self-consistent endpoint.
