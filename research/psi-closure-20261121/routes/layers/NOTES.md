# Route "layers": layer structure of the closure statement

**Status: OPEN. VERDICT: PARTIAL.** Collatz is not proved here and no layer is proved.
What is proved (Lean) is the exact shape of each layer; what is measured (finite
computation) is that the layers stop reducing to one-parameter families at rank 1.

Claim labels: PROVED-LEAN / PROPOSED / EMPIRICAL / REFUTED / OPEN.

## 0. Map, normalization, definitions

`T(n) = n/2` (n even), `(3n+1)/2` (n odd); `C` = basin of 1 (Lean `Basin`);
`S(c) = c/2` (c even), `(3c-1)/2` (c odd). `a ~ b`: same component.
`Rank r n`: the T-orbit of `n` reaches 1 with exactly `r` odd steps before its first visit
to 1 (Lean inductive predicate; `rank_unique` shows `r` is a function of `n`).
`FwdLayer r`: `∀ x, Rank r x → 3x-1 ∈ C`. `RevLayer r`: `∀ m>0, Rank r (3m-1) → m ∈ C`.
`y_n = (4^n - 1)/3` (the odd numbers of rank 1 are `y_n`, `n ≥ 2`).
`S^t(c)` = Lean `Sit t c`; `o_t(c)` = number of odd points among `c, Sc, …, S^(t-1)c` = Lean `Sodd t c`.

## 1. Lean theorems (all PROVED-LEAN)

File: `routes/layers/Layers.lean` (1088 lines, Lean 4.34.1 core, `import Collatz`, no Mathlib,
no `sorry`, no `native_decide`). Compiled in this session with

```
LEAN_PATH=<repo>/research/psi-closure-20261121/lean/.lake/build/lib/lean \
  <scratchpad>/lean/lean-4.34.1-linux/bin/lean -DwarningAsError=true Layers.lean
```

Result (`lean_build.log`): exit 0, no error, no warning; 29 `#print axioms` lines, each a
subset of `propext, Classical.choice, Quot.sound`. This is a standalone compile against the
prebuilt `Collatz` olean; `lake build` was not run.

| Lean name | Statement |
|---|---|
| `rank_unique`, `basin_iff_exists_rank` | the rank is a function; `n ∈ C ⟺ ∃ r, Rank r n` |
| `collatz_iff_fwd_layers` | Collatz ⟺ `∀ r, FwdLayer r` |
| `collatz_iff_rev_layers` | Collatz ⟺ `∀ r, RevLayer r` |
| `fwd_layer_iff r` | `FwdLayer r` ⟺ `∀ b, ∀ odd u of rank r: 3^(b+1)·u − 1 ∈ C` |
| `rev_layer_iff r` | `RevLayer r` ⟺ over odd `u` of rank `r`: `(u+1)/3 ∈ C` (when `3 ∣ u+1`), and `3^i·u+1 ∈ C` (`u ≡ 1 mod 3`), and `2·3^i·u+1 ∈ C` (`u ≡ 2 mod 3`), all `i` |
| `rank_one_odd`, `rank_one_of_eq` | odd `u` has rank 1 ⟺ `3u+1 = 4^(j+2)` for some `j` |
| `rank_two_odd`, `rank_two_of_eq` | odd `u` has rank 2 ⟺ `3u+1 = 2^(e+1)·y`, `3y+1 = 4^(j+2)` |
| `fwd_layer_zero_iff(_mersenne)` | `FwdLayer 0` ⟺ `∀ b, 3^(b+1)−1 ∈ C` ⟺ `∀ a, 2^(a+1)−1 ∈ C` |
| `fwd_layer_one_iff` | `FwdLayer 1` ⟺ `∀ b j, 3^b·4^(j+2) − (3^b+1) ∈ C` |
| `fwd_layer_two_iff` | `FwdLayer 2` ⟺ `∀ b e j, [2^(e+1)·y ≡ 1 mod 3] → 3^b·2^(e+1)·y − (3^b+1) ∈ C`, `y = y_(j+2)` |
| `rev_layer_zero_iff` | `RevLayer 0` ⟺ `∀ i, 3^i ∈ C` (cf. `first_layer_iff_pow_three`) |
| `rev_layer_one_iff` | `RevLayer 1` ⟺ five families: `3^i` when `9 ∣ 4^(i+3)+2`; `3^j` and `3^k·4^(j+2) − (3^k−1)` when `y_(j+2) ≡ 1 mod 3`; `3^(j+1)` and `3^k·2·4^(j+2) − (2·3^k−1)` when `y_(j+2) ≡ 2 mod 3` |
| `rev_layer_two_iff` | `RevLayer 2` ⟺ the three families of `rev_layer_iff` over `u = (2^(e+1)·y_(j+2) − 1)/3` |
| `shortcut_shadow` | `T(2Y − c) = 3^(c mod 2)·Y − S(c)` for `c < 2Y` |
| `basin_shadow_iter` | **landing law**: `2^t·w − c ~ 3^(o_t(c))·w − S^t(c)` for `c < 2^t·w` |
| `basin_landing` | `2^t·3^k − c ~ 3^(k+o_t(c)) − S^t(c)` |
| `fwd_one_landing`, `fwd_layer_one_iff_landing` | `3^b·4^(j+2) − (3^b+1) ~ 3^(b+o) − S^(2j+4)(3^b+1)`; `FwdLayer 1` ⟺ all these landings in `C` |
| `rev_one_a_landing`, `rev_one_b_landing` | the same for the two reverse rank-1 families (constants `3^k−1`, `2·3^k−1`) |
| `fwd_one_cone` | if `S^s(3^b+1) = 1` and `2(j+2) ≥ s`: member `~ 3^(b+o_s+(2j+4−s)) − 1` |
| `fwd_one_cone_cycle` | **cone rule**: if the S-orbit of `3^b+1` is periodic from time `s` (period `p`), every member with `2(j+2) = s+p·i+d` is `~ 3^(b+o_s+i·q+o_d) − S^d(c)`; no list of cycles assumed |
| `fwd_one_b6` | instance: `19 ≤ 2(j+2)` ⟹ `3^6·4^(j+2) − 730 ~ 3^(12+(2j+4−19)) − 1` (by `decide`) |
| `fwd_two_stage`, `fwd_two_cone` | rank 2, first stage: `3^b·2^(e+1)·y − (3^b+1) ~ 3^(b+o)·y − S^(e+1)(3^b+1)`; if that constant is 1 the member is `~` a member of the **rank-1** family |
| `basin_pred_fold`, `fwd_family_fold` | `x ≡ 3 mod 4` ⟹ `x−1 ~ 3x−1`; hence `3^k·u−1 ~ 3^(k+1)·u−1` when `3^k·u ≡ 3 mod 4` |
| `fwd_one_fold`, `fwd_one_fold_landing` | the rank-1 family folds 2:1 in `b`: `F1(2n,j) ~ F1(2n+1,j) ~ 18·9^n·4^j − (9^(n+1)−1)/8` |
| `fwd_layer_one_iff_folded` | `FwdLayer 1` ⟺ `∀ n j, 18·9^n·4^j − (9^(n+1)−1)/8 ∈ C` |
| `basin_triple_form` | `3^(i+1)·u + 1 ~ 3^i·u` (u odd): the second reverse family is tripling closure |
| `basin_pred_five`, `rev_fwd_one_link` | `x ≡ 5 mod 8` ⟹ `x ~ x−1`; hence `3^(2n+2)·4^(j+2) − (3^(2n+2)−1) ~ 3^(2n+1)·4^(j+2) − (3^(2n+1)+1)` (reverse rank-1 family at even exponent = forward rank-1 family) |
| `rev_one_b_k0` | the `k=0` slice of the second reverse family is `2^(2j+5) − 1` |

Technical note for other agents: `omega` failed ("No usable constraints found") on
`9*m = 4^(i+3) + 2 ⊢ 3*(3*m-1) + 1 = 4^(i+3)`; `generalize 4^(i+3) = X at hm ⊢` first fixes it.

## 2. Structure found

1. **Every layer is "odd numbers of rank r, times a power of three, ± 1".** PROVED-LEAN
   (`fwd_layer_iff`, `rev_layer_iff`). Odd numbers of rank `r` carry `r` exponents, so layer
   `r` is an `(r+1)`-parameter family of sums of `r+2` terms `±2^a·3^b`
   (general-`r` closed form: PROPOSED; ranks 0,1,2: PROVED-LEAN; rank sets 0,1,2 also
   brute-forced up to 300000: EMPIRICAL).
2. **Landing law.** PROVED-LEAN. Halving steps of `w·2^t` move the subtracted constant along
   its `3x−1` orbit and count its odd steps into the exponent of 3. Consequently the
   rank-1 families are exactly the sets of decorated `3x−1` orbit points
   `(K, c) = (k + o_t(c₀), S^t(c₀))` of the seeds `c₀ = 3^b+1` (forward), `3^k−1`,
   `2·3^k−1` (reverse), read as the numbers `3^K − c`.
3. **Cone rule.** PROVED-LEAN (`fwd_one_cone_cycle`), conditional on its hypothesis: for a
   fixed `b` whose seed orbit is eventually periodic, all `j` beyond the entry time land in
   at most `p` one-parameter families `3^K − c`, `c` on that cycle.
   EMPIRICAL: for all `b ≤ 1000` the three seed types enter one of the three known `3x−1`
   cycles `{1}`, `{5,7,10}`, `{17,25,37,55,82,41,61,91,136,68,34}` (counts for `3^b+1`:
   287 / 476 / 238; entry time `σ(b) ≈ 7.5·b`, range 5.85–9.16 for `b ≥ 50`). So inside the
   cone `2(j+2) ≥ σ(b)` the rank-1 layers reduce to the 15 families `3^K − c`, `c` cyclic
   (EMPIRICAL for the cycle list; that every seed is eventually periodic is OPEN — it is
   an instance of the `3x−1` problem).
4. **Folds and links.** PROVED-LEAN: `F1(2n,j) ~ F1(2n+1,j)`; reverse family at even
   exponent `~` forward family. EMPIRICAL: seed orbits also coalesce in larger groups
   (e.g. `b = 8,…,11` share the landing `(29, 61)` from time 40 on), on residue classes of
   `b`; no collapse of a whole parameter was observed (1137 distinct landings among 3219
   pre-cone members of the box).
5. **Rank 2.** PROVED-LEAN: three-parameter family; in the cone of its first stage it lands
   on the two-parameter rank-1 family, not on a one-parameter family. EMPIRICAL (asserted
   on every admissible triple with `b < 16`, `e < 20`, `2 ≤ j < 14`): full landing
   `3^(k−1+o) − S^(2j)(S^e(3^b+1) + 3^(k−1))`, `k = b + o_e(3^b+1)`.

## 3. Hypothesis H ("every layer reduces by exponent identities to finitely many one-parameter families")

- Rank 0: holds trivially (Mersenne numbers; powers of three). PROVED-LEAN.
- Rank 1, inside the cone: holds for each `b` with eventually periodic seed orbit.
  PROVED-LEAN (conditional), EMPIRICAL for `b ≤ 1000`.
- Rank 1, outside the cone (`2(j+2) < σ(b)`, e.g. `j` fixed and `b → ∞`): **no uniform
  rule found; evidence against.** The landing is `3^K − c` with `c = S^(2j+4)(3^b+1)`
  unbounded (heuristically `log₂ c ≈ 1.585·b − 0.415·j`; in the box up to more than 64 bits).
  EMPIRICAL (box `b ≤ 60`, `j ≤ 80`, members ≥ 2^64, 68 one-parameter labels
  `3^K − c` (c ≤ 40 and all cyclic c), `3^K + c` (c ≤ 10), `2^K ± c` (c ≤ 9), merge
  required above 2^40):
  - 3219 forward pre-cone members (c not listed); 2049 share an orbit point ≥ 2^40 with a
    listed member. With `β = bits(c)` and `D` = bits lost between the landing and the merge
    point: `min(D − β) = −8`, and no merge with `D < β − 8` in any β-bin (β up to >64).
    Same for the reverse families (1051 and 1127 members, `min(D − β) = −7, −8`).
  - every one of the 3420 merges with a `3^K' ± c'` member is synchronous (same number of
    steps, odd-count gap exactly `K − K'`);
  - no orbit point of a member with `β ≥ 24` is `≡` a constant of size ≤ 200 modulo `3^25`
    or `2^40` after the landing (1 439 019 points scanned, 0 hits).
  - **Coalescence inequality** (PROPOSED; two-line proof, not formalized; 0 violations on
    the 3429 merges): if `T^s(n) = T^(s')(n')`, with `o, o'` odd steps and least odd points
    `μ, μ'` before the merge, then
    `|ln(n/n') − (o'−o)·ln 3 − (s−s')·ln 2| ≤ max(o/(3μ), o'/(3μ'))`
    (each odd step multiplies by `(3/2)(1 + 1/(3x))`). For `n = 3^K − c`,
    `n' = 3^K' − c'` this forces an orbit point `≲ max(o,o')·3^K/(3c)` before any
    synchronous merge: joining a one-parameter family costs a real descent of about
    `log₂ c` bits. Each observed merge is an identity in `K` on a residue class for fixed
    `(c, c')`, not an identity in both parameters.
  Status of H as a mathematical statement: OPEN (it cannot be refuted outright — Collatz
  would put every family in `C`). Status of "a uniform identity rule exists": not found;
  EMPIRICAL evidence against, as above.
- **First genuinely two-parameter family** (canonical folded form; `fwd_layer_one_iff_folded`,
  PROVED-LEAN, says it is exactly the rank-1 forward layer): `G(n,j) = 18·9^n·4^j − (9^(n+1) − 1)/8 = 9^(n+1)·2^(2j+1) − (9^(n+1)−1)/8`,
  on the region `2j+4 < σ(2n)`. Each fixed `j` gives a one-parameter family
  (`j = 0`: `5·3^(b+1) − 1`); infinitely many `j` are needed.

## 4. First statements needed and not proved (OPEN)

1. `∀ a, 2^(a+1) − 1 ∈ C` (= `FwdLayer 0`) and `∀ i, 3^i ∈ C` (= `RevLayer 0`).
2. Every `3x−1` orbit of `3^b + 1` is eventually periodic (needed for the cone rule to
   cover every `b`).
3. `3^K − S^(2j+4)(3^b+1) ∈ C` for `2j+4 < σ(b)`: the pre-cone part of `FwdLayer 1`.
   No identity reduces it; by §3 a reduction must contain a descent of `≈ log₂ c` bits.

## 5. Negative findings

- No uniform one-parameter reduction beyond rank 0 (§3). EMPIRICAL + PROPOSED inequality.
- The cone reduction is conditional on `3x−1` dynamics; the rank-1 problem for `3x+1`
  contains orbit data (not just convergence) of the `3x−1` map on `3^b ± 1`, `2·3^b − 1`.
  PROVED-LEAN (landing law) / PROPOSED (interpretation).
- Rank 2 does not land on one-parameter families even in its first cone. PROVED-LEAN
  (`fwd_two_cone`), EMPIRICAL (box: 4 of 2589 members have a listed landing constant).
- Merge counts between pre-cone members reflect nearby-number coalescence
  (`3^K − c` vs `3^K − c'`), which obeys the same cost bound; it is not a parameter collapse.

## 6. Concurrent work (credited, not re-claimed; sources read with `git show`, not rebuilt)

- PR #176 `ad9a0611…`, `MersenneRecursion.lean`: `ternary_even_exponent_fold`,
  `mersenne_even_exponent_fold` = the `u = 1` case of `fwd_family_fold` here. Also in PR #176.
- PR #177 `23bbf738…`, `ResetFamily.lean`: source `u = (2^(b+3) − 11)/9`, target `2u+1`,
  `b = 12j+10`. In this route's terms the target is the reverse rank-1 member with
  `3m − 1 = 16·y_(b/2)`, i.e. the slice `k = 0`, exponent `≡ 5 mod 6` of the second reverse
  family, `2·4^(b/2) − 1 = 2^(b+1) − 1` (`rev_one_b_k0`). It lies in the cone from time 0
  (constant `2·3^0 − 1 = 1`), which is why it lands on a one-parameter family. Also in PR #177.
- PR #179 `27a2c741…`, `TernaryLadder.lean` (`ones_block`, `twos_block`, `ladder_path`) and
  PR #181 `5f03d809…`, `PsiDescent.lean` (`power_four_profile`, `paired_descent`): exact
  step and odd-count profiles of the two ladders used here only as basin equivalences.
  `paired_descent` lowers the rank of both arms by `r+1` on `3m = 4^(r+1)·v + 2`
  (PROPOSED reading in layer terms; not formalized here).

## 7. Files, reproduction, evidence levels

- `Layers.lean` — Lean source. `lean_build.log` — output of the compile above.
- `layers_numeric.py` — exact big-integer experiments (Python 3.13, no dependency);
  `python3 -I layers_numeric.py > numeric_results.txt`, 170 s. `numeric_results.txt` — its
  complete output (exit 0). All of it is EMPIRICAL.
- Not run: `lake build`, `tools/validate.py`, any rebuild of PR #176/#177/#179/#181.
- Nothing was committed by this route. Earlier snapshots of these files were committed by
  another process as "wip … (unverified)"; `Layers.lean`, `lean_build.log` and
  `numeric_results.txt` in the working tree are newer than those snapshots.

## 8. Handoff

- The landing law turns every statement "family ⊂ C" into a statement about decorated
  `3x−1` orbits; a proof of a layer must control `3^K − c` for `c` on those orbits.
- A cheap next Lean target: the `+` analogue of the landing law
  (`2^t·w + c ~ 3^(o)·w + T^t(c)`), which would put `3^a·2^e + c` with `c` of stopping time
  `≤ e` on the families `3^K + 1`, `3^K + 2` (PROPOSED, not checked).
- The coalescence inequality is short enough to formalize once logarithms are replaced by
  the product identity `2^s·T^s(n)·∏3x = 3^o·n·∏(3x+1)`.
