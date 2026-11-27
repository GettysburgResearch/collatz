import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Logic.Function.Iterate
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! The positive 3x+5 comparison retains an exact scaled copy of the
ordinary odd Collatz map. It supplies a separate fixed ordinary cycle in
a map with rescaled real/ternary iid affine data. -/
namespace Collatz.Diagonal.ScaledSource

def step (c x : ℕ) : ℕ := ordCompl[2] (3 * x + c)

theorem scaled_step (x : ℕ) : step 5 (5*x) = 5*step 1 x := by
  unfold step
  rw [show 3*(5*x)+5 = 5*(3*x+1) by ring, Nat.ordCompl_mul]
  have h : ordCompl[2] 5 = 5 :=
    (Nat.ordCompl_eq_self_iff_zero_or_not_dvd 5 Nat.prime_two).2 (Or.inr (by decide))
  rw [h]

theorem scaled_iterate (n x : ℕ) : (step 5)^[n] (5*x) = 5*(step 1)^[n] x := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih =>
    simp only [Function.iterate_succ_apply, scaled_step, ih]

theorem dvd_step_iff (x : ℕ) : 5 ∣ step 5 x ↔ 5 ∣ x := by
  constructor
  · intro h
    have hg : 5 ∣ 3*x+5 := by
      rw [← Nat.ordProj_mul_ordCompl_eq_self (3*x+5) 2]
      exact dvd_mul_of_dvd_right h _
    omega
  · rintro ⟨z, rfl⟩
    exact ⟨step 1 z, scaled_step z⟩

theorem dvd_iterate_iff (n x : ℕ) : 5 ∣ (step 5)^[n] x ↔ 5 ∣ x := by
  induction n generalizing x with
  | zero => rfl
  | succ n ih => rw [Function.iterate_succ_apply, ih, dvd_step_iff]

theorem fixed_points : step 5 1 = 1 ∧ step 5 5 = 5 := by
  constructor
  · change ordCompl[2] (2^3 * 1) = 1
    exact Nat.ordCompl_pow_mul_of_not_dvd 3 Nat.prime_two (by decide)
  · change ordCompl[2] (2^2 * 5) = 5
    exact Nat.ordCompl_pow_mul_of_not_dvd 2 Nat.prime_two (by decide)

theorem scaled_never_reaches_one (n x : ℕ) : (step 5)^[n] (5*x) ≠ 1 := by
  rw [scaled_iterate]
  omega

end Collatz.Diagonal.ScaledSource
