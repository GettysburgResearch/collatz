import descent

namespace Collatz.FixedSource
open PoweredInverse

/-- A positive shortcut trajectory gains at most a factor 3/2 in x+1 per odd edge. -/
theorem odd_growth {w x y} (run : Runs w x y) (hx : 0 ≤ x) :
    2 ^ odds w * (y+1) ≤ 3 ^ odds w * (x+1) := by
  induction run with
  | nil x => simp [odds]
  | @even w x y _ ih =>
    have h := ih (by omega)
    simp only [odds]
    exact Int.le_trans h (Int.mul_le_mul_of_nonneg_left (by omega) (Int.pow_nonneg (by decide)))
  | @odd w x z y edge _ ih =>
    have h := ih (by omega)
    simp only [odds, Int.pow_succ]
    have hh := Int.mul_le_mul_of_nonneg_left h (by decide : (0:Int) ≤ 2)
    calc
      _ = 2 * (2 ^ odds w * (y+1)) := by ac_rfl
      _ ≤ 2 * (3 ^ odds w * (z+1)) := hh
      _ = 3 ^ odds w * (2 * (z+1)) := by ac_rfl
      _ = 3 ^ odds w * (3 * (x+1)) := by rw [show 2*(z+1) = 3*(x+1) by omega]
      _ = _ := by ac_rfl

/-- Matched carries force separated integral mid- and endpoints on a nonreturn. -/
theorem matching_separation {w₁ w₂ x z y} (h₁ : Runs w₁ x z) (h₂ : Runs w₂ z y)
    (hc : B w₁ = B w₂) (hp : A w₁ = A w₂) (hm : A w₂ ∣ carry w₁ - carry w₂)
    (hne : y ≠ z) : 3 ^ odds w₂ ≤ (y-z).natAbs := by
  obtain ⟨k,hk⟩ := hm
  have e₁ := affine h₁
  rw [hc,hp] at e₁
  have e₂ := affine h₂
  have diff : B w₂ * (y-z) = A w₂ * (z-x-k) := by grind
  have ab := congrArg Int.natAbs diff
  simp only [Int.natAbs_mul, B, A, Int.natAbs_pow] at ab
  change 2 ^ w₂.length * (y-z).natAbs = 3 ^ odds w₂ * (z-x-k).natAbs at ab
  have cop := Nat.Coprime.pow (odds w₂) w₂.length (by decide : Nat.Coprime 3 2)
  exact Nat.le_of_dvd (Int.natAbs_pos.mpr (by omega)) (cop.dvd_of_dvd_mul_left ⟨_,ab⟩)

#print axioms Collatz.FixedSource.odd_growth
#print axioms Collatz.FixedSource.matching_separation
end Collatz.FixedSource
