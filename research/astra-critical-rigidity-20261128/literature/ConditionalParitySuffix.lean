import AdjacentWordClosure
import Mathlib.Data.Nat.ModEq
import Mathlib.Data.Nat.Prime.Basic

/-! The actual finite conditional word permutation used in dyadic multiplier
release. The statement ranges over ordinary integer shortcut sources. -/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.ConditionalParitySuffix
open Collatz.PoweredAffine Collatz.AdjacentWordClosure

private theorem three_odd (n : ℕ) : (3 ^ n) % 2 = 1 := by
  induction n with
  | zero => decide
  | succ n ih => rw [pow_succ, Nat.mul_mod, ih]

private theorem word_congr {w : List Bool} {x y : ℕ}
    (h : x ≡ y [MOD 2 ^ w.length]) : Realizes x w ↔ Realizes y w := by
  rw [realizes_iff_dvd, realizes_iff_dvd, ← Nat.modEq_zero_iff_dvd, ← Nat.modEq_zero_iff_dvd]
  have ht := (h.mul_left (3 ^ ones w)).add_right (numerator w)
  exact ⟨fun hx => ht.symm.trans hx, fun hy => ht.trans hy⟩

private theorem same_word_congr {w : List Bool} {x y : ℕ}
    (hx : Realizes x w) (hy : Realizes y w) : x ≡ y [MOD 2 ^ w.length] := by
  have h₁ := ((realizes_iff_dvd w x).mp hx).modEq_zero_nat
  have h₂ := ((realizes_iff_dvd w y).mp hy).modEq_zero_nat
  have h₃ := Nat.ModEq.add_right_cancel' (numerator w) (h₁.trans h₂.symm)
  have cop : Nat.Coprime (2 ^ w.length) (3 ^ ones w) :=
    ((by decide : Nat.Coprime 2 3).pow_left w.length).pow_right (ones w)
  exact Nat.ModEq.cancel_left_of_coprime cop h₃

/-- On an odd-step arithmetic progression, precisely one complete parameter
residue realizes any prescribed ordinary parity word. -/
theorem unique_progression_word (v : List Bool) (a b : ℕ) (ha : a % 2 = 1) :
    ∃! k : Fin (2 ^ v.length), Realizes (a * (k : ℕ) + b) v := by
  obtain ⟨j, hj⟩ := progression_realizes v a b ha
  have hp : 0 < 2 ^ v.length := by positivity
  let k : Fin (2 ^ v.length) := ⟨j % 2 ^ v.length, Nat.mod_lt _ hp⟩
  have hkmod : (k : ℕ) ≡ j [MOD 2 ^ v.length] := Nat.mod_modEq _ _
  have hk : Realizes (a * (k : ℕ) + b) v :=
    (word_congr ((hkmod.mul_left a).add_right b)).mpr hj
  refine ⟨k, hk, ?_⟩
  intro l hl
  have same := Nat.ModEq.add_right_cancel' b (same_word_congr hl hk)
  have cop : Nat.Coprime (2 ^ v.length) a :=
    (Nat.coprime_two_left.mpr (Nat.odd_iff.mpr ha)).pow_left _
  exact Fin.ext ((Nat.ModEq.cancel_left_of_coprime cop same).eq_of_lt_of_lt l.isLt k.isLt)

/-- A complete modulus shift preserves the whole actual prefix and moves the
actual terminal state by the odd affine multiplier. -/
theorem translate_word_endpoint {w : List Bool} {y : ℕ} (hw : Realizes y w) (z : ℕ) :
    Realizes (y + 2 ^ w.length * z) w ∧
      orbit (y + 2 ^ w.length * z) w.length = orbit y w.length + 3 ^ ones w * z := by
  have hmod : y + 2 ^ w.length * z ≡ y [MOD 2 ^ w.length] := by
    simp [Nat.ModEq, Nat.add_mod]
  have hshift := (word_congr hmod).mpr hw
  refine ⟨hshift, ?_⟩
  apply Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2 ^ w.length)
  calc
    _ = 3 ^ ones w * (y + 2 ^ w.length * z) + numerator w := actual_word_affine hshift
    _ = (3 ^ ones w * y + numerator w) + 2 ^ w.length * (3 ^ ones w * z) := by ring
    _ = _ := by rw [← actual_word_affine hw, Nat.mul_add]

private theorem realizes_append {w v : List Bool} {n : ℕ} (hw : Realizes n w) :
    Realizes n (w ++ v) ↔ Realizes (orbit n w.length) v := by
  induction w generalizing n with
  | nil => rfl
  | cons bit w ih =>
    change (_ ∧ Realizes (step n) (w ++ v)) ↔ Realizes (orbit (step n) w.length) v
    exact ⟨fun h => (ih hw.2).mp h.2, fun h => ⟨hw.1, (ih hw.2).mpr h⟩⟩

/-- Conditional on a realized word of a*x and the odd input x, a uniform
coefficient K modulo the next word's modulus gives exactly one copy of each
possible suffix. The quantified condition refers to the physical concatenated
word at the ordinary source (a + 2^|w| K)x. -/
theorem unique_multiplier_suffix {a x : ℕ} (hx : x % 2 = 1) {w : List Bool}
    (hw : Realizes (a * x) w) (v : List Bool) :
    ∃! k : Fin (2 ^ v.length),
      Realizes ((a + 2 ^ w.length * (k : ℕ)) * x) (w ++ v) := by
  have odd : (3 ^ ones w * x) % 2 = 1 := by rw [Nat.mul_mod, three_odd, hx]
  have transfer (k : Fin (2 ^ v.length)) :
      Realizes ((a + 2 ^ w.length * (k : ℕ)) * x) (w ++ v) ↔
        Realizes ((3 ^ ones w * x) * (k : ℕ) + orbit (a * x) w.length) v := by
    have hs := translate_word_endpoint hw (x * (k : ℕ))
    rw [show (a + 2 ^ w.length * (k : ℕ)) * x =
        a * x + 2 ^ w.length * (x * (k : ℕ)) by ring,
      realizes_append hs.1, hs.2,
      show orbit (a * x) w.length + 3 ^ ones w * (x * (k : ℕ)) =
        (3 ^ ones w * x) * (k : ℕ) + orbit (a * x) w.length by ring]
  obtain ⟨k, hk, uniq⟩ := unique_progression_word v (3 ^ ones w * x) (orbit (a * x) w.length) odd
  exact ⟨k, (transfer k).mpr hk, fun l hl => uniq l ((transfer l).mp hl)⟩

end Collatz.ConditionalParitySuffix
