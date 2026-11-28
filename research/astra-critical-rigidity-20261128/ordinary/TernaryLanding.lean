import AffineOrbit
import Mathlib.Tactic.FieldSimp

/-! Native prefixes on positive rationals with denominator a power of three
times an odd cofactor. The recursion stops when the ternary height is zero. -/

namespace Collatz.TernaryLanding
open Collatz.PoweredAffine

/-- The physical parity is read from the numerator of the odd-denominator state. -/
inductive Run (q : ℕ) : ℕ → ℕ → List Bool → ℕ → ℕ → Prop where
  | nil (h d : ℕ) : Run q h d [] h d
  | even {h d h' d' : ℕ} {w : List Bool} (bit : d % 2 = 0)
      (tail : Run q (h + 1) (d / 2) w h' d') :
      Run q (h + 1) d (false :: w) h' d'
  | odd {h d h' d' : ℕ} {w : List Bool} (bit : d % 2 = 1)
      (tail : Run q h ((d + q * 3 ^ h) / 2) w h' d') :
      Run q (h + 1) d (true :: w) h' d'

private theorem three_mod_two (h : ℕ) : 3 ^ h % 2 = 1 := by
  induction h with
  | zero => decide
  | succ h ih => rw [pow_succ, Nat.mul_mod, ih]

theorem consumed_grade {q h d h' d' : ℕ} {w : List Bool}
    (run : Run q h d w h' d') : h = ones w + h' := by
  induction run with
  | nil => simp [ones]
  | even _ _ ih => simpa [ones] using ih
  | odd _ _ ih => simp only [ones, ↓reduceIte]; omega

theorem prefix_carry {q h d h' d' : ℕ} {w : List Bool} (hq : q % 2 = 1)
    (run : Run q h d w h' d') :
    2 ^ w.length * d' = d + q * 3 ^ h' * numerator w := by
  induction run with
  | nil => simp [numerator]
  | @even h d h' d' w bit _ ih =>
    have hd : 2 * (d / 2) = d := by omega
    simp only [List.length_cons, pow_succ, numerator, Bool.false_eq_true, ↓reduceIte,
      mul_zero, zero_add]
    calc
      2 ^ w.length * 2 * d' = 2 * (2 ^ w.length * d') := by ring
      _ = 2 * (d / 2 + q * 3 ^ h' * numerator w) := by rw [ih]
      _ = d + q * 3 ^ h' * (2 * numerator w) := by rw [mul_add, hd]; ring
  | @odd h d h' d' w bit tail ih =>
    have hpar : (d + q * 3 ^ h) % 2 = 0 := by
      simp [Nat.add_mod, Nat.mul_mod, bit, hq, three_mod_two]
    have hd : 2 * ((d + q * 3 ^ h) / 2) = d + q * 3 ^ h := by omega
    have hg : 3 ^ h = 3 ^ ones w * 3 ^ h' := by rw [consumed_grade tail, pow_add]
    simp only [List.length_cons, pow_succ, numerator, ↓reduceIte, mul_one]
    calc
      2 ^ w.length * 2 * d' = 2 * (2 ^ w.length * d') := by ring
      _ = 2 * ((d + q * 3 ^ h) / 2 + q * 3 ^ h' * numerator w) := by rw [ih]
      _ = d + q * 3 ^ h' * (3 ^ ones w + 2 * numerator w) := by
        rw [mul_add, hd, hg]
        ring

/-- A positive reduced start reaches ternary height zero on its nth odd departure. -/
theorem exists_landing (q : ℕ) (hq : q % 2 = 1) (h m : ℕ) (hm : 0 < m) :
    ∃ w P, Run q h m w 0 P ∧ 0 < P ∧ ones w = h := by
  have exists_run (height : ℕ) :
      ∀ d, 0 < d → ∃ w P, Run q height d w 0 P ∧ 0 < P := by
    induction height with
    | zero => exact fun d hd => ⟨[], d, Run.nil 0 d, hd⟩
    | succ height lower =>
      intro d
      induction d using Nat.strong_induction_on with
      | h d smaller =>
        intro hd
        by_cases bit : d % 2 = 0
        · obtain ⟨w, P, tail, hp⟩ := smaller (d / 2) (by omega) (by omega)
          exact ⟨false :: w, P, Run.even bit tail, hp⟩
        · have hpos : 0 < q * 3 ^ height := Nat.mul_pos (by omega) (by positivity)
          obtain ⟨w, P, tail, hp⟩ := lower ((d + q * 3 ^ height) / 2) (by omega)
          exact ⟨true :: w, P, Run.odd (by omega) tail, hp⟩
  obtain ⟨w, P, run, hp⟩ := exists_run h m hm
  exact ⟨w, P, run, hp, by simpa using (consumed_grade run).symm⟩

theorem positive_level_unit {q h d h' d' : ℕ} {w : List Bool}
    (hq : q % 2 = 1) (hd : ¬ 3 ∣ d) (hp : 0 < h') (run : Run q h d w h' d') :
    ¬ 3 ∣ d' := by
  intro divisible
  apply hd
  have hpow : 3 ∣ 3 ^ h' := dvd_pow_self 3 (by omega)
  have hleft : 3 ∣ 2 ^ w.length * d' := dvd_mul_of_dvd_right divisible _
  have hright : 3 ∣ q * 3 ^ h' * numerator w :=
    dvd_mul_of_dvd_left (dvd_mul_of_dvd_right hpow q) _
  rw [prefix_carry hq run] at hleft
  exact (Nat.dvd_add_iff_left hright).mpr hleft

/-- The semantically evaluated rational word agrees with the exact numerator recursion. -/
theorem rational_value {q h d h' d' : ℕ} {w : List Bool}
    (hq : q % 2 = 1) (run : Run q h d w h' d') :
    evalWord w ((d : ℚ) / (q * 3 ^ h)) = (d' : ℚ) / (q * 3 ^ h') := by
  have qpos : 0 < q := by omega
  have hqQ : (q : ℚ) ≠ 0 := by positivity
  have hc : (2 : ℚ) ^ w.length * d' = (d : ℚ) + q * 3 ^ h' * numerator w := by
    exact_mod_cast prefix_carry hq run
  have hf := word_affine w ((d : ℚ) / (q * 3 ^ h))
  rw [consumed_grade run, pow_add] at hf ⊢
  field_simp at hf ⊢
  apply mul_left_cancel₀ (show (2 : ℚ) ^ w.length ≠ 0 by positivity)
  calc
    _ = _ := by simpa only [mul_assoc] using hf.trans hc.symm

/-- Adding one complete dyadic word modulus to the initial numerator translates
the terminal numerator by one, with all physical bits unchanged. -/
theorem dyadic_translation {q h d h' d' : ℕ} {w : List Bool}
    (run : Run q h d w h' d') (z : ℕ) :
    Run q h (d + 2 ^ w.length * z) w h' (d' + z) := by
  induction run with
  | nil => simpa using Run.nil (q := q) _ (_ + z)
  | @even h d h' d' w bit tail ih =>
    have hs : 2 ^ (false :: w).length * z = 2 * (2 ^ w.length * z) := by
      simp only [List.length_cons, pow_succ]
      ring
    rw [hs]
    apply Run.even (by omega)
    have he : (d + 2 * (2 ^ w.length * z)) / 2 = d / 2 + 2 ^ w.length * z := by omega
    rw [he]
    exact ih
  | @odd h d h' d' w bit tail ih =>
    have hs : 2 ^ (true :: w).length * z = 2 * (2 ^ w.length * z) := by
      simp only [List.length_cons, pow_succ]
      ring
    rw [hs]
    apply Run.odd (by omega)
    have he : (d + 2 * (2 ^ w.length * z) + q * 3 ^ h) / 2 =
        (d + q * 3 ^ h) / 2 + 2 ^ w.length * z := by omega
    rw [he]
    exact ih

end Collatz.TernaryLanding
