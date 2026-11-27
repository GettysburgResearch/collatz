import NativeTightness

/-! Finite true-orbit estimates for centered native parity counts after a physical
hit. The analytic source-clock and Brownian assertions are outside this module. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.NativeGate.CriticalCount

open Collatz.NativeGate

/-- Twice the excess over the alternating odd frequency, retaining its sign. -/
def twiceCentered (x k : ℕ) : ℤ := 2 * (odds x k : ℤ) - (k : ℤ)

theorem twiceCentered_add (x k r : ℕ) :
    twiceCentered x (k + r) = twiceCentered x k + twiceCentered (orbit x k) r := by
  simp only [twiceCentered, odds_add, Nat.cast_add]
  ring

theorem one_score (r : ℕ) : twiceCentered 1 r = (r % 2 : ℕ) := by
  obtain ⟨j, hj | hj⟩ : ∃ j : ℕ, r = 2 * j ∨ r = 2 * j + 1 := ⟨r / 2, by omega⟩
  · rw [hj]
    simp only [twiceCentered, (one_even_clock j).2]
    omega
  · rw [hj]
    simp only [twiceCentered, odds, (one_even_clock j).1, (one_even_clock j).2]
    omega

theorem centered_after_one (x k r : ℕ) (hit : orbit x k = 1) :
    twiceCentered x (k + r) - twiceCentered x k = (r % 2 : ℕ) := by
  rw [twiceCentered_add, hit, one_score]
  omega

/-- Uniform rational drift beyond the preverified floor with a fixed start cost. -/
theorem protected_fixed_start (a r m : ℕ) (ha : 0 < a) (small : a ≤ 2^m)
    (floor : ∀ i < r, 3 ≤ orbit a i) :
    (r : ℤ) ≤ 7 * twiceCentered a r + 8 * (m : ℤ) := by
  have hb := protected_bound a r floor
  have ho := orbit_positive ha r
  have hp : 0 < (orbit a r)^4 := by positivity
  have hs := Nat.pow_le_pow_left small 4
  have hpow : (2 : ℕ)^(4*r) ≤ 2^(7*odds a r + m*4) := by
    calc
      (2 : ℕ)^(4*r) = 2^(4*r) * 1 := (Nat.mul_one _).symm
      _ ≤ 2^(4*r) * (orbit a r)^4 := Nat.mul_le_mul_left _ hp
      _ ≤ 2^(7*odds a r) * a^4 := hb
      _ ≤ 2^(7*odds a r) * (2^m)^4 := Nat.mul_le_mul_left _ hs
      _ = 2^(7*odds a r + m*4) := by rw [pow_add, pow_mul]
  have he := (Nat.pow_le_pow_iff_right (by decide : 1 < (2 : ℕ))).mp hpow
  unfold twiceCentered
  omega

/-- Nonconvergence supplies the floor for every actual future vertex. -/
theorem nonconvergent_floor (a : ℕ) (ha : 0 < a) (bad : ¬ ReachesOne a) (i : ℕ) :
    3 ≤ orbit a i := by
  have hi := orbit_positive ha i
  have hone : orbit a i ≠ 1 := fun h => bad ⟨i, h⟩
  have htwo : orbit a i ≠ 2 := by
    intro h
    apply bad
    refine ⟨i + 1, ?_⟩
    rw [orbit_add, h]
    decide
  omega

/-- The bound follows a supplied source to its same ordinary, bad anchor. -/
theorem centered_after_nonconvergent (x k a r m : ℕ) (hit : orbit x k = a)
    (ha : 0 < a) (bad : ¬ ReachesOne a) (small : a ≤ 2^m) :
    (r : ℤ) ≤ 7 * (twiceCentered x (k + r) - twiceCentered x k) + 8 * (m : ℤ) := by
  have h := protected_fixed_start a r m ha small (fun i _ => nonconvergent_floor a ha bad i)
  rw [twiceCentered_add, hit]
  omega

end Collatz.NativeGate.CriticalCount
