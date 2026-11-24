import Std

/-! The affine coefficient identities used in the two-place proof. -/
namespace WeightedOddClock

theorem weighted_step (x y f b : Int) (a : Nat)
    (h : (2 : Int) ^ (a + 1) * y = 3 * x + b) :
    2 * ((2 ^ a * f) * y) = 3 * (f * x) + f * b := by
  calc
    2 * ((2 ^ a * f) * y) = f * (2 ^ (a + 1) * y) := by
      simp [Int.pow_succ, Int.mul_comm, Int.mul_left_comm]
    _ = _ := by rw [h, Int.mul_add]; grind

theorem normalized_block_defect (P Q upstream downstream before after : Int)
    (h : Q * downstream = P * upstream) :
    Q * (downstream - after) - P * (upstream - before) = P * before - Q * after := by
  rw [Int.mul_sub, Int.mul_sub, h]
  omega

theorem inverse_ones_step (x y : Nat) (h : 2 * (y + 1) = 3 * (x + 1)) :
    2 * y = 3 * x + 1 := by omega

#print axioms weighted_step
#print axioms normalized_block_defect
#print axioms inverse_ones_step

end WeightedOddClock
