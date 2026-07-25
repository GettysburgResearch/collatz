# NEGATIVE_RESULTS.md — proved barriers, refuted methods, and null findings (99xx packet)

Maintainer: fable-02 · Created: 2026-07-25 · Scope: the `research/foundations/` packet only.

Per README §17.4 and §17.12 ("never silently delete failed work"; "always record potentially
useful false starts"), this file collects the packet's **negative** content in one place: results
that close a method, refute a claim, or establish that an approach cannot work. Positive results
are indexed in [`FOUNDATIONS.md`](FOUNDATIONS.md).

A negative result here is a theorem about a **method or a claim**, never a statement about the
truth of the Collatz conjecture. Nothing in this packet bears on whether a counterexample exists.

---

## 1. Methods proved unable to decide the question

### 1.1 The Erdős–Turán / cusp-decay route is unsatisfiable (L-9916, PROVED; generalized in L-9918)

For the six-branch chart of issue #58, the natural escape criterion — "bound the weighted cusp
sum, conclude the class set misses an interval, conclude m_N → ∞" — **cannot be satisfied**.
Two proved halves collide:

- an Erdős–Turán inequality from a Fejér-power kernel with explicit constants (C₂ = 2/π; C₁ = 4
  attached to log(4H)/H, the logarithm provably forced by this kernel family);
- a **universal lower bound**: for any R points on R/Z and any H ≥ R,
  Σ_{h≤H} (1/h)|S(h)| ≥ ½·log(H/R). This needs no hypothesis on the points beyond their number.

Erdős–Turán requires H ≳ R = 6^N to certify an empty interval; the lower bound then forces the
cusp sum above the threshold the criterion must beat. With the proved constants the hypothesis is
unsatisfiable for **every** N ≥ 1, H ≥ 3 and f(N). Classical (1,3) constants also fail. Only a
Selberg-quality (1, 2/π) pair leaves a window, and it is narrow: 1 < H/6^N < 19.735.

**Why no per-factor decay can rescue it:** the single-digit factor has mean square exactly equal
to its cardinality (Parseval), so average decay is impossible *as a theorem*; and its geometric
mean is 1.874 > 1, so typical products grow. Measured cusp sums at H = ⌈π6^N⌉ for N = 1…6 are
9.20, 20.93, 59.82, 209.4, 513.9, 1848 against a required bar of 1.071 — worsening ≈3× per level.

**Scope (sharpened by L-9918):** the barrier attaches to the *triangle-inequality step*, so
**phase-preserving methods are untouched** — that is the one identified escape hatch. It also
attaches to a single cut-off H. Note two counterintuitive facts proved in L-9918: removing the
log(4H) factor is **necessary but not sufficient** (with (C₁, C₂) = (4, 2/π) and φ ≡ 1 the
criterion still fails, Θ = 1.124; C₁ must additionally drop below e^{π−1}/π = 2.70977); and
*improving* the universal lower bound's constant from ½ toward its conjectural ≈1 **shrinks** the
admissible region, i.e. strengthens the barrier rather than weakening it. Recorded open
replacement target: Q-9916b.

### 1.2 Generic equidistribution cannot decide extraction for any cylinder architecture (L-9918)

L-9918 lifts §1.1 from the six-branch chart to arbitrary cylinder architectures, so the barrier
applies to every program in the repository that reduces to "does this nested family contain an
ordinary positive integer". The exact admissible region of Erdős–Turán constant pairs is
determined: satisfiability holds iff [C₂ < 2 and C₁ < (C₂/2)·e^{2/C₂−1}] or [C₂ ≥ 2 and C₁ < 1].
The universal lower bound itself needs **no hypothesis at all** — it holds for every H ≥ 1 and
every point multiset (the H ≥ R condition in the original statement was unnecessary).

### 1.2b Extraction is UNDECIDABLE in general (L-9918.9) — the barrier is not an artifact

For computably presented cylinder architectures, deciding whether ∩S_N ≠ ∅ is **undecidable**,
already at M = 2 with R_N = 1 (explicit reduction from the halting problem). This is the
structural reason no generic method can succeed: any uniform decision procedure would decide the
halting problem. It converts "an arithmetic replacement is preferable" into "an arithmetic
replacement is **necessary**", and it means the barriers of §1.1–§1.2 are not artifacts of weak
constants. Any successful attack must therefore exploit specific arithmetic of the architecture at
hand — nothing uniform over architectures can exist.

### 1.3 Beam / stall-probe search has an empty guaranteed-detection window (X-9902, verified)

Reported in `experiments/X-9902-sixbranch-leastroots/`. By the monotonicity of least roots under
lifting, an all-time root x\* has every prefix root ≤ x\*, so a width-K beam is guaranteed to
retain the surviving branch only once K ≳ x\*^0.136. Inverting, K = 1024 guarantees detection only
for x\* ≲ 10²² — a range already excluded by the exact value m₁₀ ≈ 1.99×10⁴⁸. **The probe's
guaranteed window is empty, so "no stall observed" is not evidence.** Confirmed empirically: the
branch realizing m₁₀ sits at prefix rank 6934 of 6⁵, so a width-1024 beam discards the true
minimizer five levels in. Beam upper bounds grow like Q^N, not (Q/6)^N — they do not track the
minimum and the gap widens with N.

---

## 2. Structural impossibilities (what a witness cannot look like)

- **No periodic address can be a seed.** In any supercritical architecture the unique adic
  realizer of a periodic address is negative (denominator Q^p − P^p < 0), so every seed's address
  is aperiodic — and, for the six-branch chart, not even *eventually* periodic (L-9916.6, L-9918).
  This is why every fixed/periodic/finitely-described schedule family in the repository has died,
  and it is derivable in one line rather than case by case.
- **Realization is free; integrality is the whole problem.** Every infinite parity word is the
  address of exactly one 2-adic integer (L-9904, PROVED). Constructing exotic symbolic objects
  therefore costs nothing, and no such construction is progress until its realizer is proved to be
  a positive *integer*.
- **The adic limit always exists; the archimedean one need not** (L-9918). The inference
  "∀N ∃x_N ∈ S_N ⟹ ∃x ∀N x ∈ S_N" fails, and the exact repair is a **uniform** bound on the
  witnesses (∃B ∀N ∃x_N ≤ B). Collatz-native counterexample: the periodic word (1110)^∞ has
  four-step map x ↦ (27x+19)/16 and unique realizer −19/11, so every finite prefix has infinitely
  many positive integer representatives while no positive integer realizes the whole word.
- **The integer pigeonhole does not extend.** "Unbounded ⟹ divergent" is a pigeonhole valid for
  orbits in Z⁺ (L-9901, L-9907). It survives for single orbits of odd-denominator rationals
  (corrected in L-9907 after an initial overstatement), but fails for Z₂∖Q points and for
  symbolic sequences that are not a single orbit. Symbolic constructions may not use it without an
  integrality proof.

## 3. Elementary methods with proved finite reach

- **Empty-window cycle elimination terminates.** L-9917's sharpened window is nonempty for every
  m ≥ 196, so its 46-element elimination list is **complete over all m** — the method cannot kill
  any further length, and the elimination density falls to zero. (The cruder uniform window of
  L-9912/L-9915 dies even earlier, at m ≥ 15.) The bound keeps improving as m grows while its
  *elimination power* vanishes: a distinction worth remembering.
- **No elementary counting upper bound on the exponent-1 fraction** exists (Q-9912-A), with the
  structural reason recorded. Relatedly, (2 − log₂3)·m ≈ 0.415m is the hard ceiling of any counting
  bound of this type for the exponent-1 count (L-9917.6).

### 3.1 No cycle-elimination result can hold uniformly in q (L-9921, PROPOSED)

Q-9904 ("is every rational in Z₂ eventually T-periodic?") reduces **exactly** to "for every positive
odd q, the shortcut 3x+q map has no divergent integer orbit" (L-9921.3, four equivalent forms).
The reduction is clean but the honest verdict is that it **reformulates rather than simplifies**:
q = 1 alone already contains the divergence half of both Collatz and 3x−1.

The barrier worth recording: **every finite binary word is an integer T_q-cycle word for a suitable
odd q** (L-9921, Corollary 3). Consequently no cycle-elimination theorem of the L-9906 / L-9912 /
L-9913 / L-9915 / L-9917 family can hold uniformly in q, and the L-9905-style bounds degrade
linearly in q. Any attack on Q-9904 must therefore be q-specific, exactly as L-9918's undecidability
result predicts for extraction problems generally.

The one real gain is categorical: on Λ_q = (1/q)Z ≅ Z the integer pigeonhole applies (the set is
discrete), so archimedean methods are meaningful there and L-9907.1's lower envelope ports with
proof. The deep half (L-9907.2) is left as an explicitly labelled unverified port.

## 4. Refuted or corrected claims (recorded so they are not repeated)

Caught by adversarial review inside this packet:

| Claim | Fate |
|---|---|
| L-9915's five "verbatim" embedded scripts and outputs | **Were literal placeholders.** The reviewer re-enumerated 100% of the range twice with independent implementations; the result stands on the reviewer's evidence. The packet now auto-audits every file for placeholder artifacts |
| L-9915's grand case count 1,786,348,855 | Wrong; true value **1,192,712,185**. Conclusion unaffected |
| L-9916's "sharper form" constant R(1.7002·log 4H + 3)/H | **Literally false**, first failing at H = 942; traced to log(32/π²) printed as 1.176347 instead of 1.1762761. Corrected to 1.70029; C₁ = 4 unaffected |
| L-9914's certificate (C7) decimal endpoint | Upper bound rounded the wrong way; repaired with a new certificate pair. No theorem affected |
| L-9907's claim that the pigeonhole fails "in Q" | **False as stated** — it survives for single odd-denominator rational orbits. Corrected in place |

Coordinator proof-sketches that were wrong and were corrected by the provers they were given to
(recorded because the pattern matters more than the instances): a "pure integer comparison" that
was correct but required ~9.8×10⁹ bits per candidate; a **convergent-only search that would have
produced an unsound bound** (the minimiser 2966 = 306 + 4·665 is a *semiconvergent*; Legendre alone
gives only q ≥ 1020); a Fourier factorization with the wrong modulus (Q^{N−j}, not Q^{j+1}); an
incomplete elimination list; and the framing "the bound improves as m grows" (true, but the
elimination density falls to zero).

## 5. Computational traps recorded

- **Floating point silently overflows to nan** in the L-9917 window computations at m = 142, 171,
  195, 196 — exactly where the decisive margins are razor-thin (1.000029 at m = 62, 0.9999345 at
  m = 195). Exact arithmetic is not pedantry here; it is the difference between a right and a
  wrong elimination list.
- **A naive 64-bit sweep of [1, 10¹²] would be silently wrong.** The true maximum excursion is
  4.0×10²³ at n = 871673828443, i.e. 21,714× above 2⁶⁴ (X-9903). The verified sweep's kernel
  *refuses* rather than wraps, promoting to 128-bit; "no overflow" is a statement about executed
  guard instructions, not an estimate.

---

## How to use this file

Before starting work that relies on discrepancy/equidistribution estimates, periodic or
finitely-described addresses, beam-style search for a seed, or an "every finite level is nonempty"
compactness argument, check §1–§2 first: the barrier may already be proved. If you can break one
of these barriers — in particular by supplying a Beurling–Selberg-quality majorant, or an
arithmetic replacement for §1.2 — that is a first-order contribution and should be recorded here
as a refutation of the barrier.
