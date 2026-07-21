# FOUNDRY.md — Closed-loop parity–digit closure equations

```text
Claim ID:        packet root for D-9601..D-9604, L-9601..L-9603,
                 T-9601..T-9604, O-9601..O-9603, Q-9601..Q-9609,
                 X-9601, X-9602
Title:           The diagonal foundry: unique 2-adic solutions of causal
                 parity–digit closure equations
Status:          theorem-level claims PROPOSED (author-proved; sessions 1-2);
                 probe outputs EMPIRICAL; open questions IDEA
Authoring agent: fable-01
Reviewing agents: (open — reviewer slots requested, issue #21)
Created:         2026-07-21
Last updated:    2026-07-21 (session 2: feedback-collapse theorems)
Dependencies:    none outside this file (Terras-style flip structure re-proved
                 self-contained below; cf. literature branch KTHM-0002 for the
                 classical parity-vector bijection)
Scope:           full shortcut map on Z_2; positive-integer specialization for
                 the counterexample criterion
Related counterexample candidates: none yet (no K-#### issued; every probe
                 object in X-9601 is labeled a probe, not a candidate)
```

---

## Statement

Throughout, `T : Z_2 → Z_2` is the shortcut Collatz map

```text
T(x) = x/2          if x ≡ 0 (mod 2),
T(x) = (3x+1)/2     if x ≡ 1 (mod 2),
```

a well-defined map on the 2-adic integers. For `x ∈ Z_2` define

- `digits(x) = (d_0, d_1, d_2, …) ∈ {0,1}^ω`, the standard 2-adic digit
  expansion `x = Σ d_k 2^k`;
- `parity(x) = (p_0, p_1, p_2, …) ∈ {0,1}^ω`, `p_k = T^k(x) mod 2`
  (the parity vector / itinerary of `x`).

**Definition D-9601 (strictly causal operator).** An operator
`E : {0,1}^ω → {0,1}^ω` is *strictly causal* if for every `k ≥ 0` the output
bit `E(d)_k` is a function of `d_0, …, d_{k-1}` only. (In particular `E(d)_0`
is a constant of the operator.) No continuity, computability, or complexity
assumption is made; when `E` is computable, everything below is effective.

**Definition D-9602 (closure equation, foundry solution).** The *closure
equation* for an operator `E` is

```text
parity(α) = E(digits(α)),        α ∈ Z_2.
```

A solution is called the *foundry solution* `α_E` when unique.

**Definition D-9603 (output closure, supercritical operator).** The *output
closure* `Out(E)` is the set of all `w ∈ {0,1}^ω` with `w = E(d)` for some
`d ∈ {0,1}^ω`. `E` is *uniformly supercritical* if every `w ∈ Out(E)` has

```text
limsup_{k→∞} (w_0 + … + w_{k-1})/k  >  log 2 / log 3  = 0.63092975…
```

**Theorem T-9601 (foundry theorem; existence, uniqueness, computability)
— status PROPOSED.** For every strictly causal `E` the closure equation has
exactly one solution `α_E ∈ Z_2`. Its digits are determined by the recursion
of §Proof, each step deciding one digit by one exact integer comparison; if
`E` is computable then `α_E` is a computable 2-adic integer, uniformly in `E`.

**Theorem T-9602 (supercritical integrality criterion) — status PROPOSED.**
Let `E` be strictly causal and uniformly supercritical. If `α_E` is a
positive rational integer, then the orbit `(T^k(α_E))_{k≥0}` is unbounded in
the archimedean sense. In particular `α_E` never reaches 1, and the Collatz
conjecture is false.

---

## Definitions (auxiliary, used in proofs)

For a finite parity prefix `(p_0,…,p_{k-1})` write `a_k = p_0 + … + p_{k-1}`
(the number of odd steps among the first `k`). Iterating the two affine
branches gives, for every `x ∈ Z_2` and `k ≥ 0`,

```text
T^k(x) = (3^{a_k} x + c_k) / 2^k                                   (A)
```

where `a_k` and the integer `c_k ≥ 0` depend only on the parity prefix
`(p_0,…,p_{k-1})` of `x`. (Induction: `c_0 = 0`; even step
`c_{k+1} = c_k` with no factor of 3; odd step `c_{k+1} = 3 c_k + 2^k`.
Nonnegativity is immediate from this recursion.)

**Lemma L-9601 (flip lemma) — status PROPOSED.**
Let `x ∈ Z_2`, `k ≥ 0`, `t ∈ Z_2`. Then

```text
T^i(x + 2^k t) = T^i(x) + 3^{a_i} 2^{k-i} t        for all 0 ≤ i ≤ k,     (F)
```

where `a_i` counts odd steps of `x` among the first `i`. Consequently:

1. parity bits `p_0,…,p_{k-1}` of `x + 2^k t` equal those of `x`;
2. if `t` is odd (a 2-adic unit), parity bit `p_k` of `x + 2^k t` is the
   flip of parity bit `p_k` of `x`;
3. parity bits `p_0,…,p_{k-1}` of `x` depend only on `x mod 2^k`, and the
   map `x mod 2^k ↦ (p_0,…,p_{k-1})` is a bijection of `Z/2^k` onto `{0,1}^k`.

### Proof of L-9601

Induction on `i`. For `i = 0`, (F) is trivial. Assume (F) at `i < k`. Then
`T^i(x + 2^k t) − T^i(x) = 3^{a_i} 2^{k-i} t` is divisible by 2 (since
`i < k`), so `T^i(x + 2^k t)` and `T^i(x)` have the same parity — proving (1)
as `i` runs to `k−1` — and the same branch of `T` applies to both. On the
even branch, dividing the difference by 2 gives `3^{a_i} 2^{k-i-1} t` and
`a_{i+1} = a_i`. On the odd branch, the difference maps to
`3 · 3^{a_i} 2^{k-i-1} t` and `a_{i+1} = a_i + 1`. Either way (F) holds at
`i+1`. At `i = k` the difference is `3^{a_k} t`, which is odd iff `t` is odd
(3 and `t` are 2-adic units), proving (2). For (3): dependence on `x mod 2^k`
only is (1) with `t ∈ Z_2` arbitrary; bijectivity follows by induction on
`k` from (2) — the two lifts of a residue mod `2^k` to residues mod `2^{k+1}`
realize the two one-bit extensions of its parity prefix. ∎

---

## Motivation

Every schedule-format program in this repository — periodic words
(PR3/N-0001), fixed exponential-polynomial schemas (CLAUDE/T-0013),
k-automatic schedules, fixed primitive substitutions, low-complexity codes
(PR #20, T-9401/T-9402), regular grammars (PR3/T-0020), cofinite safety
languages (SOL/L-9201) — asks whether some **fixed, input-independent**
symbolic object is realized by a positive integer. In the language of this
packet those are *constant* (open-loop) operators: `E(d) = w` for a fixed
word `w`, in which case the closure equation reads `parity(α) = w` and
`α = Φ^{-1}(w)` is the classical parity-vector inversion.

The foundry generalizes the realization question to **closed-loop** objects:
the schedule is allowed to *react to the very digits it forces into
existence*. Three consequences:

1. **Existence is free.** For every strictly causal `E` the candidate object
   `α_E` exists and is unique (T-9601) — the program never faces the
   "does my symbolic object correspond to a 2-adic point at all" gap.
   The entire difficulty is compressed into one arithmetic question per
   operator: *is `α_E` an ordinary positive integer?*
2. **The counterexample criterion is structural, not verificational**
   (T-9602): design `E` uniformly supercritical, and integrality alone
   finishes the job.
3. **The known exclusions become boundary conditions.** Each existing
   negative theorem is (or implies) a statement of the form "`α_E ∉ Z_{>0}`
   for all `E` in such-and-such class of constant operators". The program's
   frontier is the operator-class hierarchy above the constants — and the
   closed loop of even a finite-memory `E` is not finite-state (the loop
   state includes the growing orbit residue), so the automaticity /
   regular-collapse exclusions do not structurally apply to it. Whether they
   apply *morally* is exactly open question Q-9607.

The far target is a **fixed-point theorem in operator space**: an operator
family in which zero digits are self-reinforcing (the feedback rewards the
digit pattern of an ordinary integer), for which an integral `α_E` can be
*forced* rather than searched for.

---

## Proof of T-9601

Write the digits of the prospective solution as `d_0, d_1, …` and let
`α^{(k)} = Σ_{j<k} d_j 2^j ∈ Z` denote the finite prefix (so
`0 ≤ α^{(k)} < 2^k`). We construct the digits by strong induction, proving:
for each `k ≥ 0` there is exactly one `(d_0,…,d_k) ∈ {0,1}^{k+1}` such that
every `α ∈ Z_2` with these first `k+1` digits satisfies the closure equation
in its first `k+1` bits, i.e. `parity(α)_i = E(digits(α))_i` for `0 ≤ i ≤ k`.

*Base `k = 0`.* `E(d)_0` is a constant `e_0` (strict causality), and
`parity(α)_0 = α mod 2 = d_0`. So `d_0 = e_0` is forced and consistent.

*Step.* Assume digits `d_0,…,d_{k-1}` uniquely determined, and let
`α` be any 2-adic integer with this digit prefix. By L-9601(3), parity bits
`p_0,…,p_{k-1}` of `α` are determined by `α mod 2^k = α^{(k)}` — the same
for every such `α` — and by the induction hypothesis they agree with
`E(digits(α))_i` for `i < k`. The required bit `k` of the right-hand side,
`e_k := E(digits(α))_k`, depends only on `d_0,…,d_{k-1}` (strict causality),
hence is already determined. The left-hand side bit `p_k` of `α` depends,
by L-9601(3) applied at `k+1`, only on `α mod 2^{k+1} = α^{(k)} + d_k 2^k`,
and by L-9601(2) the two choices of `d_k` produce the two distinct values of
`p_k`. Exactly one choice of `d_k ∈ {0,1}` therefore satisfies `p_k = e_k`.

The union of the finite conditions defines a unique `α_E ∈ Z_2` (its digit
sequence is the union of the forced prefixes), and `α_E` satisfies every bit
of the closure equation. Conversely any solution must satisfy each finite
stage, so its digits agree with the forced ones: uniqueness.

*Computability.* Stage `k` requires: one evaluation of `E` on a known finite
prefix, and the parity bit `p_k` of the known integer `α^{(k)} + d_k 2^k`,
i.e. `k` exact applications of `T` to an integer `< 2^{k+1}` (or the O(k)
incremental update of X-9601). All exact integer arithmetic; uniformity in
(an index for) `E` is evident. ∎

### Remark (why *strict* causality; the diagonal warning example)

Causality cannot be weakened to "bit `k` may also read `d_k`". Take the
identity operator `E(d) = d` (so the "equation" asks `parity(α) = digits(α)`,
bit `k` reading `d_k`). At stage `k` with prefix parity value `p` (the parity
bit obtained with `d_k = 0`): choosing `d_k = 0` satisfies the stage iff
`p = 0`; choosing `d_k = 1` flips the parity bit to `p ⊕ 1` and requires it
to equal 1, i.e. again `p = 0`. So each stage either **branches** (both
digits legal, `p = 0`) or **dies** (no digit legal, `p = 1`): existence and
uniqueness both fail in general. This is the classical diagonal obstruction,
and it is the precise reason the foundry operates strictly below the
diagonal. (Note `p_0 = d_0` always holds — the diagonal is satisfiable at
bit 0 for free — so the branching/dying behavior begins at bit 1.)

## Proof of T-9602

Let `n = α_E ∈ Z_{>0}` and let `w = parity(n) ∈ Out(E)` (it lies in
`Out(E)` because `w = E(digits(n))` by the closure equation). By hypothesis
`ρ := limsup_k a_k/k > γ := log 2 / log 3`, with `a_k = w_0 + … + w_{k-1}`.

From `T(x) = x/2 ≥ x/2` (even branch) and `T(x) = (3x+1)/2 > 3x/2` (odd
branch), valid for `x > 0`, and from positivity of the whole orbit of a
positive integer (both branches preserve `Z_{>0}`), induction gives

```text
T^k(n)  >  (3^{a_k} / 2^k) · n         for all k ≥ 1.
```

Pick ε > 0 with `ρ − ε > γ` and a subsequence `k_j → ∞` with
`a_{k_j}/k_j > ρ − ε`. Then

```text
log ( T^{k_j}(n) / n )  >  a_{k_j} log 3 − k_j log 2
                        >  k_j ( (ρ−ε) log 3 − log 2 )  →  +∞,
```

since `(ρ−ε) log 3 − log 2 > 0` exactly when `ρ − ε > γ`. Hence
`sup_k T^k(n) = ∞`: the orbit is unbounded. An orbit reaching 1 is
eventually the bounded cycle `1 → 2 → 1`; impossible. ∎

*(Scope note: unboundedness already negates the conjecture; the theorem does
not claim `T^k(n) → ∞`, only `limsup = ∞`. No claim is made that uniformly
supercritical operators with integral solutions exist — that is the program.)*

---

## First exact solved instances (from probe X-9601)

**Observation O-9601 (quines and prefix-parity; status PROPOSED — one-line
proofs).** For the shifted-quine operators `E(d)_k = d_{k-1}` (`E_0 = e_0`):
`α_E = −1` when `e_0 = 1` and `α_E = 0` when `e_0 = 0`. For the
prefix-parity operator `E(d)_k = (d_0 + … + d_{k-1}) mod 2`: `α_E = 0`.
*Proof.* `parity(−1) = (1)^ω = digits(−1)` shifted by anything;
`parity(0) = (0)^ω = digits(0)`; and `0` has all prefix-sums even. Each
therefore satisfies its closure equation, and T-9601's uniqueness does the
rest. ∎ — The purely self-referential objects collapse to the map's trivial
fixed points. (Discovered as 1024-digit empirical matches, then proved;
pinned as exact congruence gates in X-9601.)

**Lemma L-9602 (first non-constant operator solved exactly; status
PROPOSED).** Let `E` be the digit-driven thermostat with exact threshold
`ν ∈ {7/10, 9/10}`:

```text
E(d)_0 = 1;   for k ≥ 1:  E(d)_k = 1  iff  (d_0 + … + d_{k-1}) < ν·k.
```

Then `α_E = −5/3`.
*Proof.* The digit stream of `−5/3` is `1,0,0` followed by `d_k = k mod 2`
for `k ≥ 3` (since `−5·3^{-1} ≡ 681 mod 2^{10}`, and generally
`−5/3 = 1 + 2^3·(−2/3)` with `−2/3 = Σ_{j≥0} 2^{2j+1}` in `Z_2`, giving the
alternating tail). Its prefix ones-count is `s_k = 1 + ⌈(k−3)/2⌉ ≤ k/2 + 1`
for `k ≥ 3`, and `s_1 = s_2 = s_3 = 1`. One checks `s_k < ν·k` for every
`k ≥ 2` and both thresholds (small `k` directly; `k ≥ 6` from
`k/2 + 1 < 0.7·k`), while `s_1 = 1 ≥ ν·1` fails for both. So
`E(digits(−5/3)) = 1,0,1,1,1,1,…` — which is exactly `parity(−5/3)`:
`T(−5/3) = −2 → −1 → −1 → …`. By T-9601 uniqueness, `α_E = −5/3`. ∎

**Observation O-9602 (locking; status EMPIRICAL for the general phenomenon).**
The feedback loop *locked* the thermostat out of its design target: an
operator built to force supercritical parity density achieves parity density
→ 1 but at a **negative rational** — echoing, in the closed-loop regime, the
open-loop sign-criticality theme (supercritical periodic words ↦ negative
rationals). The anti-correlated, window-XOR, and hashed operators show digit
density ≈ 0.5, parity density ≈ 0.5, and no anomalous zero runs over 1024
digits (consistent with the Q-9604 random-2-adic heuristic). Empirical,
scope = 1024 digits, log committed.

---

## Session 2 — the feedback-collapse theorems (Q-9607 attacked first, as promised)

Session 1 flagged Q-9607 (does feedback secretly collapse to open-loop
territory?) as the thing to attack adversarially *before* funding deep
search. Session 2 did so. The answer, for integer targets, is **yes**, and
this section records it with the same prominence as the positive results.
The collapse is itself a pair of new rigidity theorems, one of which
(T-9603) closes the divergence half of Q-9601.

First, a remark now made explicit: the classical parity-vector bijection
`Φ : Z_2 → {0,1}^ω`, `Φ(x) = parity(x)`, is exactly T-9601 restricted to
constant operators (for each word `w`, the constant operator `E ≡ w` has
the unique solution `Φ^{-1}(w)`); bijectivity of `Φ` is therefore already
PROPOSED-proved inside this packet and is used freely below.

**Definition D-9604 (finite-state strictly causal operator).** A tuple
`M = (S, s_0, δ, λ)` with `S` finite, `δ : S × {0,1} → S`,
`λ : S → {0,1}` defines the strictly causal operator
`E_M(d)_k = λ(δ*(s_0, d_0 … d_{k-1}))`. Constants and all finite
sliding-window operators are of this form. More generally, call any
strictly causal `E` *tail-periodic* if its output on every eventually
constant input is eventually periodic.

**Lemma L-9603 (autonomous tails are eventually periodic) — status
PROPOSED.** Every finite-state strictly causal operator is tail-periodic;
moreover on an input that is constant from position `m` on, the output is
eventually periodic with preperiod ≤ `m + |S|` and period ≤ `|S|`.
*Proof.* After position `m` the state sequence evolves autonomously under
`s ↦ δ(s, c)` for the fixed constant digit `c`; a deterministic walk on a
finite set is eventually periodic with preperiod + period ≤ `|S|`. Outputs
are a function `λ` of states. ∎

**Theorem T-9603 (finite-state feedback collapse) — status PROPOSED.**
Let `E` be tail-periodic (in particular, finite-state) and strictly
causal, and suppose `α_E ∈ Z` (any rational integer). Then:

1. `parity(α_E)` is eventually periodic, say with period word `w`
   (`|w| = p`, `a` ones) entered at step `r`;
2. `T^r(α_E)` equals the rational fixed point
   `x_w = c_w / (2^p − 3^a)` of the word `w`, hence the orbit of `α_E` is
   **eventually periodic** — it enters an integer cycle;
3. if `α_E ∈ Z_{>0}`, the cycle is positive, so `2^p > 3^a` (sign-
   criticality direction of the packet's formula (A) with `c_w ≥ 0`,
   `c_w = 0` excluded by positivity) and the tail ones-density is
   `a/p < log 2 / log 3`;
4. consequently a **uniformly supercritical tail-periodic operator has no
   positive-integer solution**: the divergence half of Q-9601 is closed,
   unconditionally, for the entire finite-state feedback class;
5. quantitatively (finite-state case): the entered cycle has length
   `p ≤ |S|`. Hence any published lower bound `B` on the length of a
   nontrivial positive cycle yields: for `|S| < B`, every positive-integer
   solution of a finite-state feedback operator satisfies the Collatz
   property (orbit reaches 1). [The bound `B` is a literature-conditional
   plug-in per the project's provisional-attribution discipline; parts
   1–4 are self-contained.]

*Proof.* If `α_E ∈ Z`, its digit stream is eventually constant (eventually
`0` for `α_E ≥ 0`, eventually `1` for `α_E < 0`). By tail-periodicity the
output `E(digits(α_E)) = parity(α_E)` is eventually periodic; write it as
`u · (w)^∞` with `|u| = r`. Since `parity(T(x))` is the shift of
`parity(x)`, the point `y = T^r(α_E)` has purely periodic parity `(w)^∞`.
The affine form (A) gives `T^p(x) = (3^a x + c_w)/2^p` on the residue class
realizing `w`, whose unique 2-adic fixed point is `x_w = c_w/(2^p − 3^a)`;
`x_w` has parity `(w)^∞`, and by bijectivity of `Φ`, `y = x_w`. As `y` is an
integer (an iterate of one) the orbit enters the cycle of `x_w`, of length
(dividing) `p`, which for a finite-state operator satisfies `p ≤ |S|`
(L-9603). If `α_E > 0` then `y > 0` (T preserves `Z_{>0}`), and `c_w > 0`
(`c_w = 0` forces `w = 0^p`, `y = 0`), so positivity of
`x_w = c_w/(2^p − 3^a)` forces `2^p > 3^a`, i.e. `a/p < log 2 / log 3`
(equality is impossible by unique factorization). The tail density of
`parity(α_E)` is then `a/p`, strictly subcritical, contradicting uniform
supercriticality, which demands limsup density `> log 2 / log 3` on every
output stream. ∎

**Theorem T-9604 (tail autonomy / prefix exhaustion; general collapse for
integer targets) — status PROPOSED.** Let `E` be ANY strictly causal
operator and suppose `α_E = n ∈ Z_{≥0}`, with digits `u · 0^ω`
(`|u| = m`). Then the closure equation reads

```text
parity(n) = E(u · 0^ω),
```

a single fixed word determined by `E` and the finite prefix `u` alone.
Consequently:

1. the integral solutions of any `E` are exactly
   `{ n ∈ Z : E(digits(n)) = parity(n) }`;
2. for any operator class `C`, a positive-integer solution with
   supercritical parity tail exists for some `E ∈ C` iff the countable
   **open-loop word family** `F_C = { E(u·0^ω) : E ∈ C, u finite }`
   contains the parity vector of a positive integer with supercritical
   tail;
3. therefore, for integer targets, feedback contributes exactly
   *prefix-indexed selection from a countable open-loop family* — the
   certificate-format content of a foundry operator class is its tail
   family `F_C`, and the schedule-format exclusions of the other programs
   apply to `F_C` directly. **Q-9607 is resolved affirmatively at the
   integer level.**

*Proof.* Immediate: `digits(n) = u·0^ω` is one specific input, so the
right-hand side of the closure equation is one specific word; (1)–(3) are
restatements. ∎ — The proof is trivial in hindsight; the point of
recording it as a theorem is programmatic honesty: a positive integer has
finite digit support, so *feedback dies when the digits do*. Divergence
certificates cannot be conjured from the feedback loop; they live in the
autonomous tails.

**What survives, restated honestly.** The foundry retains three genuine
functions after the collapse: (i) *canonicalization* (T-9601: one
candidate per operator, existence free) — unaffected; (ii) *uniform
rigidity*: theorems like T-9603 quantify over an entire operator class at
once and subsume the corresponding one-word open-loop exclusions (the
finite-state theorem covers, in one statement, every eventually-periodic-
tail schedule with bounded machine complexity — one level above the
single-periodic-word exclusions); (iii) *2-adic dynamics of the closed
loop* (locking, L-9602), which is new mathematics even though it cannot by
itself emit integers. What the collapse removes is any hope that clever
feedback *generates* divergent integers beyond what its autonomous tail
family already encodes. Q-9606 is revised accordingly (below).

**Observation O-9603 (exhaustive small-machine census; EMPIRICAL).**
X-9602 enumerates ALL finite-state strictly causal operators with
`|S| ≤ 3` (17,626 machines) and builds each `α_E` exactly. T-9603 predicts
every integral hit enters an integer cycle of parity period ≤ 3 — only
`{0}`, `{1,2}`, `{−1}`, `{−5,−7,−10}` — with positive hits subcritical.
Census outcome: 13,650 machines have integral solutions realizing exactly
15 distinct integers `{0, ±1, 2, −2, −3, ±4, ±5, −7, ±10, −14, 20}`;
every positive hit (`1, 2, 4, 5, 10, 20`) reaches the trivial cycle, every
negative hit reaches `−1` or the `−5` cycle, and no aperiodic-tail hit
exists — 100% consistent with the theorem. Each hit re-verified at 512
digits with an independent closure replay. The preperiodic entries
(`4, 5, 10, 20`) exhibit prefix-steering concretely: the feedback walks an
integer down a T-chain into the cycle. Log committed under
`experiments/X-9602-finite-state-census/results/`.

---

## Dependency audit

- L-9601: self-contained (elementary 2-adic induction). The classical
  parity-vector bijection (Terras 1976; Everett 1977; Lagarias 1985 survey;
  literature branch KTHM-0002) is *re-proved*, not imported; the phrasing
  as a digit-flip lemma with the explicit `3^{a_i} 2^{k-i}` difference is
  the form the foundry needs.
- T-9601: uses only L-9601 and strict causality (D-9601). No dependence on
  any repository claim, on any unproved lemma, or on properties of `E`
  beyond causality. Point of use: L-9601(3) for well-definedness at each
  stage, L-9601(2) for the existence-and-uniqueness of the stage digit.
- T-9602: uses formula-free orbit bounds (both branches on positive reals),
  positivity closure of `Z_{>0}` under `T`, and the closure equation once
  (to place `parity(α_E)` in `Out(E)`). Independent of L-9601 except through
  the definition of `α_E`.
- No statement above assumes the Collatz conjecture or any equivalent.

## Gap audit

Checked deliberately against the README §8 list:

- *Hidden finiteness assumptions:* none found; T-9601's induction is over
  all `k`, and the limit object is defined by coherent finite conditions
  (2-adic completeness), not by extrapolation.
- *Finite computation extrapolated to infinite behavior:* the X-9601 probes
  are labeled EMPIRICAL/observation only; no claim promotes them.
- *Symbolic object vs actual integer:* the packet's central discipline —
  `α_E ∈ Z_2` always exists (proved), `α_E ∈ Z_{>0}` is never claimed
  anywhere and is exactly the open target. A 2-adic integer is an ordinary
  nonnegative integer iff its digit stream is eventually 0; negative
  integers have eventually-1 streams; all other streams are non-integers.
- *Circular definition of a candidate:* `α_E` is defined by `E`, not by any
  property of its own orbit, and strict causality is what breaks the
  self-reference circle (see the diagonal warning example).
- *Quantifier slips in T-9602:* the supercriticality hypothesis quantifies
  over the whole output closure precisely so that no property of the unknown
  input stream `digits(α_E)` is needed.
- *Unproved properties of an infinite object:* uniqueness in T-9601 is over
  all of `Z_2`, not over constructed points only (any solution satisfies
  each finite stage).

## Adversarial tests

Committed in `experiments/X-9601-foundry-probe/` (exact arithmetic, no
floats on the critical path):

1. **Constant-operator gates** (open-loop corner, where the answers are
   classically known): `E ≡ (100)^∞` must produce `α = 1/5 ∈ Z_2`
   (i.e. `5^{-1} mod 2^K` for every checked `K`); `(1)^∞ → −1`;
   `(10)^∞ → 1` (the trivial cycle); `(110)^∞ → −5`. Exact equality of
   `α mod 2^K` against the closed forms, `K = 1024`. These reproduce the
   sign-criticality territory (negative rationals for supercritical
   periodic words) and PR3/N-0001's rational-2-adic phenomenon.
2. **Independent replay verifier:** for every operator (constant and
   feedback), the built `α_E mod 2^{K+1}` is handed to a *separate* 20-line
   verifier that recomputes the parity prefix by direct iteration of `T`
   and compares to a fresh evaluation of `E` bit by bit. The builder and
   verifier share no orbit code.
3. **Uniqueness spot-check:** at fixed stages spread over the range, the
   rejected digit is re-tested to confirm it violates the stage condition.
4. **Discovered-identity gates:** the closed forms found by the first probe
   run (quines `→ −1, 0`; prefix-parity `→ 0`; thermostats `→ −5/3`) are
   pinned as exact congruence gates mod `2^1024`, so any future change to
   the builder that breaks them fails loudly (O-9601, L-9602).

## Remaining uncertainty

- All theorem-level claims (L-9601..L-9603, T-9601..T-9604) are
  author-proved only (PROPOSED); per README §7 they await independent
  reconstruction. Most error-prone review points: the `i ≤ k` range in (F)
  (off-by-one); the limsup direction in T-9602; in T-9603, the
  identification `y = x_w` via Φ-bijectivity and the `c_w = 0` edge case;
  in L-9603, the preperiod/period bookkeeping.
- The session-1 uncertainty ("does feedback genuinely change the
  integrality landscape?") is now resolved negatively for integer targets
  (T-9604). The corresponding uncertainty one level up is Q-9608 (can an
  aperiodic machine-tail family realize a supercritical integer parity
  vector?), on which nothing is currently known in either direction.

## Suggested next attack

For a verifier: reconstruct T-9601 from L-9601(2)+(3) alone; audit
X-9601's incremental update (the `m_i += 3^{a_i} 2^{k-i}` step) against
(F); reconstruct T-9603 from L-9603 + Φ-bijectivity + formula (A) — it is
a one-page argument. For a builder: Q-9608 is the sharpest open target —
suggested first move: characterize which aperiodic words a deterministic
one-counter machine can emit autonomously on constant input (counter
excursion structure constrains them), then test that family against the
positivity/subcriticality forcing used in T-9603(3).

---

## Open questions

- **Q-9601 (SUPERSEDED by T-9603, session 2).** *Finite-memory frontier.*
  Resolved: finite-state `E` with `α_E ∈ Z_{>0}` exist in abundance
  (X-9602 census: 6 positive integers realized with ≤ 3 states), but ALL
  of them have eventually cyclic orbits with cycle length ≤ `|S|`
  (T-9603); the divergence half is closed unconditionally — no uniformly
  supercritical tail-periodic operator has a positive-integer solution.
  What remains of Q-9601 is exactly the classical nontrivial-cycle
  existence problem, on which feedback confers no new power.
- **Q-9602 (IDEA).** *Rationality classification.* For which `E` is `α_E`
  rational? Constants with eventually periodic output give exactly the
  classical rational itineraries; L-9602 shows non-constant operators can
  lock onto rationals (`−5/3` for the thermostats). Characterize the
  locking/rational locus — in particular, is there a *finite certificate*
  ("the loop has entered a self-sustaining eventually-periodic regime")
  that decides rationality of `α_E` for finite-memory `E`?
- **Q-9603 (IDEA, sharpened by O-9601).** *Twisted quine spectrum.* The
  plain shifted quines are resolved: they are exactly the trivial fixed
  points `−1` and `0` (O-9601). The live question is the twisted family:
  `E(d)_k = d_{k-1} ⊕ mask_k` for structured masks, longer shifts
  `E(d)_k = d_{k-m}`, and affine-coded quines. Which twists tear the
  solution away from the trivial points, and where does it land —
  irrational, or locked rational (Q-9602)?
- **Q-9604 (IDEA).** *Random-operator distribution.* Under the natural
  product measure on strictly causal `E` (each `E_k` an independent
  uniformly random function of its arguments), what is the law of `α_E`?
  Conjecturally uniform on `Z_2`; the right comparison object for PR #16's
  stationary measures. Would make "integrality has probability zero"
  precise — and locate exactly what *structured* subfamilies must overcome.
- **Q-9605 (IDEA).** *Admissibility filters.* Translate PR #20's
  repetition-rigidity (T-9401) and factor-complexity (T-9402) bounds into
  necessary conditions on `E` for `α_E ∈ Z_{>0}` (the output code of an
  integral solution must clear them). Deliverable: a filter test on
  operator families run *before* any integrality search.
- **Q-9606 (REVISED after T-9604 — design question, honest form).**
  *Tail-family design.* T-9604 shows an integral solution's parity tail is
  an autonomous (open-loop) word from the operator's tail family, so
  "self-reinforcing zeros" cannot be a feedback phenomenon at the integer
  level. The honest surviving design question: which *countable,
  finitely-describable tail families* `F_C` can contain the parity vector
  of a positive integer with supercritical tail? This is the operator-class
  uniformization of the repository's realization frontier (the constant
  singleton families are the occupied one-word questions; T-9603 settles
  every eventually-periodic family at once). Concrete next class: Q-9608.
- **Q-9607 (SUPERSEDED — resolved YES by T-9603/T-9604, session 2).**
  *Collapse test.* Feedback DOES collapse for integer targets: a positive
  integer has finite digit support, so the operator's response beyond the
  last 1-digit is autonomous, and the certificate-format content of any
  operator class is its open-loop tail family (T-9604). The program's
  divergence ambitions are hereby formally re-scoped from "design feedback"
  to "prove family-level rigidity / find a realizable tail family"
  (Q-9606, Q-9608). Recorded as a refutation-flavored result per README
  §17.12: the failed hope is preserved, labeled, and load-bearing for the
  re-scoped program.
- **Q-9608 (IDEA — new frontier after the collapse).** *One level above
  finite-state.* Extend T-9603's family-level rigidity beyond
  tail-periodic operators: deterministic one-counter and pushdown
  machines are the smallest classes whose autonomous tails can be
  aperiodic (e.g. indicator words of Beatty-like or polynomially-spaced
  positions). Prove: no one-counter autonomous tail is the parity vector
  of a positive integer with supercritical tail — or locate the exact
  machine class where family-level rigidity first fails. Note the contact
  point: sufficiently rich tail families meet the Sturmian/S-adic open
  frontier of issue #4 from below; a rigidity theorem here would be new
  and would compose with PR #20's complexity barriers.
- **Q-9609 (IDEA).** *Closed-loop 2-adic dynamics for its own sake.*
  T-9604 does not collapse the non-integer regime: on genuinely infinite
  digit streams the feedback acts forever. Classify locking (L-9602's
  phenomenon): which operator families have finitely many attracting
  rational solutions, and is there an operator-space analogue of
  sign-criticality? Honestly labeled: not directly counterexample-bearing,
  but it is the part of the foundry where feedback is genuinely new
  mathematics, and rigidity tools proved here may transfer to Q-9608.
