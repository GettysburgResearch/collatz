import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Finite interfaces for raw harmonic cycle mass and delayed marked traces. -/
set_option autoImplicit false
namespace Collatz.Global.CycleTrace

variable {F : Type*} [Field F] [LinearOrder F] [IsStrictOrderedRing F]

/-- After clearing dyadic clocks at adjacent depths, the two cross products
have different ternary valuations when the old source and the new target
are units modulo three. -/
theorem adjacent_mark_separation (d s r x y X Y : ℕ)
    (hx : ¬3 ∣ x) (hY : ¬3 ∣ Y) :
    3 ^ d * (x * (2 ^ r * Y)) ≠
      3 ^ (d+1) * (X * (2 ^ s * y)) := by
  intro heq
  have hpos : 0 < (3:ℕ)^d := by positivity
  have reduced : x * (2^r * Y) = 3 * (X * (2^s*y)) := by
    apply Nat.eq_of_mul_eq_mul_left hpos
    simpa only [pow_succ, Nat.mul_assoc] using heq
  have hdiv : 3 ∣ x * (2^r * Y) := ⟨X * (2^s*y), reduced⟩
  have hprime : Nat.Prime 3 := by decide
  rcases hprime.dvd_mul.mp hdiv with he | he
  · exact hx he
  rcases hprime.dvd_mul.mp he with he | he
  · exact (by norm_num : ¬ (3:ℕ) ∣ 2) (hprime.dvd_of_dvd_pow he)
  · exact hY he

/-- A jump in either signed CDF is paid by at least one of its two adjacent
values. The real-analysis left-limit passage uses the written argument. -/
theorem cdf_jump_charge (before after bound mass : F)
    (hb : |before| ≤ bound) (ha : |after| ≤ bound)
    (hj : after - before = mass) : mass ≤ 2 * bound := by
  have hb' := (abs_le.mp hb).1
  have ha' := (abs_le.mp ha).2
  linarith

/-- The exact linear lower barrier under the physical single-edge survival. -/
theorem raw_barrier_step (x c : F) (hx : 0 < x) :
    (3*x / (3*x+1)) * (c*(3+1/x)) = 3*c := by
  have hx' : x ≠ 0 := ne_of_gt hx
  have hden : 3*x+1 ≠ 0 := by positivity
  field_simp

/-- Closing any lap with survival strictly less than one forces a
subsolution below the actual harmonic mass. -/
theorem close_raw_barrier (a lower survival : F)
    (hl : survival < 1) (h : survival * (a-lower) ≤ a-lower) : lower ≤ a := by
  by_contra! hbad
  have hp := mul_pos (sub_pos.mpr hl) (sub_pos.mpr hbad)
  nlinarith

omit [LinearOrder F] [IsStrictOrderedRing F] in
/-- Every circular offset together with every source enumerates all ordered
pairs once, independently of the period and the shape of the profile. -/
theorem all_offset_mass {G : Type*} [AddCommGroup G] [Fintype G]
    (f : G → F) : ∑ r : G, ∑ i : G, f i * f (i-r) = (∑ i : G, f i)^2 := by
  classical
  have reindex (i : G) : (∑ r : G, f (i-r)) = ∑ j : G, f j := by
    let e : G ≃ G := {
      toFun := fun r => i-r
      invFun := fun r => i-r
      left_inv := fun r => sub_sub_cancel i r
      right_inv := fun r => sub_sub_cancel i r }
    exact e.sum_comp f
  rw [Finset.sum_comm]
  simp_rw [← Finset.mul_sum, reindex]
  rw [← Finset.sum_mul, pow_two]

end Collatz.Global.CycleTrace

#print axioms Collatz.Global.CycleTrace.adjacent_mark_separation
#print axioms Collatz.Global.CycleTrace.cdf_jump_charge
#print axioms Collatz.Global.CycleTrace.raw_barrier_step
#print axioms Collatz.Global.CycleTrace.close_raw_barrier
#print axioms Collatz.Global.CycleTrace.all_offset_mass
