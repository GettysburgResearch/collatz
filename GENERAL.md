# The Digit-Transfer Framework

*The step-back generalization of the whole program. Seed computations:
`experiments/` (spectrum table below); everything else in this file is
definition, instance-mapping, and program.*

## 1. The master object

For multiplicatively independent integers `a > b ≥ 2` and a digit set
`D ⊊ {0,…,b−1}`, the **digit-transfer system**

    H_{a,b,D}(bB + d) = aB + d,   d ∈ D,

with survivor set `V∞(a,b,D) = {A : every H-iterate has digit ∈ D}`.
All structure constants of our theory are functions of (a, b) alone:
the inverse branches `J_d(x) = (bx + (a−b)d)/a` — **the mysterious 17
is just a − b = 81 − 64** — the Fourier coefficients
`c_t = (a−b)b^t a^{−(t+1)}`, the coset index, the AP-subgroup.

**M(a,b,D):** does `V∞ ∩ ℤ_{>0}` exceed the trivial fixed digits?
Any nontrivial survivor grows forever (`A′ − A = (a−b)B > 0`).

## 2. The instances (one theory, four famous problems)

| instance | (a, b, D) | statement |
|---|---|---|
| Collatz L=6 subsystem | (81, 64, {0,1}) ×4 charts | M ⟹ Collatz false (this program) |
| Collatz L-atlas | (3^{a_L}, 2^L, D_L) | hierarchy below |
| Erdős 2^n base-3 digits | ×2-orbit vs base-3 Cantor set | dual form of M(·) |
| Mahler Z-numbers | archimedean (3, 2, [0,½)) | frac-parts version |
| Furstenberg ×p×q | measure/dimension version | rigidity theory |

## 3. What transfers (theorem → hypothesis)

T1 rigidity (unique factorization): any (a,b). T2 coding `V∞ ≅ D^ℕ`
and no-integer-cycles bound `A ≤ (a−b)·max(D)·a^p/(a^p−b^p)`-type: any
(a,b). T5 isometry (LTE): needs p-adic valuation structure of a−1 vs
b. T6 SML: any. T7 product formula: any. T8 cascade with threshold
`bδ₁ + aδ₂ < 1`: any. T9 self-similarity/max: b a prime power. T10
exact-run rigidity: needs gcd(a−b, a) = 1 (automatic). T11 block-mean
decay with constant `2/π + O(1/a)`: any. T12 a.e.-depth decay: needs
the AP-subgroup fact `⟨b⟩ = 1 + qℤ mod a^j` — holds when b ≡ 1 mod q,
q² ∥ b−1-type conditions (for (81,64): 64 ≡ 1 mod 9). **The entire
12-theorem corpus is a theory of digit-transfer systems, not of
Collatz.**

## 4. The atlas hierarchy and its spectrum (new)

Collatz contains one digit-transfer system per block length L:
`T^L(2^L q + r) = 3^{a_r} q + T^L(r)`, so collisions are exactly the
non-injectivity classes of `T^L` stratified by odd count — the atlas
`D_L = {r : ∃s ≠ r, a_s = a_r, T^L(s) = T^L(r)}` restricted to
supercritical `3^{a_r} > 2^L`. Spectrum `γ_L = log₂|D_L|/L`, fuel cost
`(1−γ_L)L` bits per L-step block (verified L ≤ 20):

    L:      6    9    11    14    17    19    20
    γ_L:  .500 .664  .752  .781  .801  .833  .816
    cost: 3.00 3.02  2.73  3.06  3.38  3.17  3.69

**Findings.** (i) γ_L rises toward 1 in a sawtooth; (ii) absolute cost
per block stays bounded (~3 bits) while blocks lengthen — per-step cost
→ 0; (iii) the peaks sit at **the denominators of the continued-fraction
convergents of log₃2** (6~2/3-doubled, 11 ↔ 7/11, 19 ↔ 12/19; next:
65) — the same CF that governs the S-adic schedule theory and the
boundary slope. The hierarchy interpolates between the rigid (81,64)
system (γ = ½) and full Collatz divergence (the γ → 1 limit).

## 5. The two pivots for the original goal

**Pivot A (parameter dial on the interchange lemma).** The one gap left
in EQ — the T11×T12 interchange — now has tunable parameters: prove it
first in extreme regimes (b ≫ a-relative, |D| = 2: per-level decay
constant 2/π fixed while frequency growth log b grows — the counting
closes when the dial is favorable), then push the constants toward
(81, 64, 2). Deliverable shape: "M(a,b,D) has no nontrivial small
survivors whenever [explicit inequality in a, b, |D|]" — with the
Collatz instance's distance to the provable region measured exactly.

**Pivot B (the convergent-atlas hunt — a genuinely new search space).**
Every search so far lived in the L = 6 atlas. The L = 11 and L = 19
atlases have 2–3× weaker per-step constraints (0.25 and 0.17 bits/step)
and have never been searched: enumerate their coded survivor sets
R_K^{(L)} (same recursion, base 2^L → 3^{a_L}), find their extremal
integer survivors, and test whether the survivor law (min ≈
(2^L/|D_L|)^K) persists as γ_L → 1. If the law bends at high L, that is
the first crack ever observed; if it holds, the cost-boundedness
conjecture — **(1−γ_L)L ≥ c > 0 for all L** — becomes the sharpest
finite-parameter form of the Collatz divergence conjecture itself:
divergence-freedom ⟺ every atlas level keeps a positive constant fuel
cost. Proving cost-boundedness for the peak subsequence is a concrete,
finite-computation-guided target; refuting it would locate the level
at which Collatz's defense fails.

## 6. Where this leaves the original goal

The counterexample hunt is no longer "search integers" (dead by twelve
theorems) nor "close one lemma" (the interchange) — it is now: climb
the atlas hierarchy along the CF convergents of log₃2, where the
constraint provably thins, and determine whether the ~3-bit cost floor
is a theorem (Collatz survives, quantitatively) or an artifact of small
L (the hunt continues at L = 65 with 0.05 bits/step). Either resolution
of the cost-floor question is a fundamental result about the problem.
