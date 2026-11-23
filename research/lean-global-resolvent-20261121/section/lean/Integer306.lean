import Init

set_option maxRecDepth 10000
set_option maxHeartbeats 1000000
set_option exponentiation.threshold 200000

namespace CollatzBandCertificate

theorem small_lower_306 :
    899 * (2 : Nat) ^ 485 ≤ 900 * 3 ^ 306 := by decide

theorem small_upper_306 : (3 : Nat) ^ 306 ≤ 2 ^ 485 := by decide

theorem small_ratio_306 : (900 : Nat) ^ 306 ≤ 2 * 899 ^ 306 := by decide

theorem integer_bracket_306 :
    (2 : Nat) ^ 148409 ≤ 3 ^ 93636 ∧
      (3 : Nat) ^ 93636 ≤ 2 ^ 148411 := by
  have raised := Nat.pow_le_pow_left small_lower_306 306
  simp only [Nat.mul_pow, ← Nat.pow_mul] at raised
  rw [show (485 * 306 : Nat) = 148410 from rfl,
    show (306 * 306 : Nat) = 93636 from rfl] at raised
  have scaled : 899 ^ 306 * (2 : Nat) ^ 148410 ≤
      899 ^ 306 * (2 * 3 ^ 93636) := by
    calc 899 ^ 306 * (2 : Nat) ^ 148410 ≤ 900 ^ 306 * 3 ^ 93636 := raised
         _ ≤ (2 * 899 ^ 306) * 3 ^ 93636 :=
           Nat.mul_le_mul_right (3 ^ 93636) small_ratio_306
         _ = 899 ^ 306 * (2 * 3 ^ 93636) := by
           rw [Nat.mul_comm 2 (899 ^ 306), Nat.mul_assoc]
  have cancel : (2 : Nat) ^ 148410 ≤ 2 * 3 ^ 93636 :=
    Nat.le_of_mul_le_mul_left scaled (Nat.pow_pos_iff.mpr (Or.inl (by decide)))
  have powerid : (2 : Nat) ^ 148410 = 2 ^ 148409 * 2 := Nat.pow_succ _ _
  rw [powerid, Nat.mul_comm 2 (3 ^ 93636)] at cancel
  refine ⟨Nat.le_of_mul_le_mul_right cancel (by decide), ?_⟩
  have upper := Nat.pow_le_pow_left small_upper_306 306
  simp only [← Nat.pow_mul] at upper
  rw [show (485 * 306 : Nat) = 148410 from rfl,
    show (306 * 306 : Nat) = 93636 from rfl] at upper
  exact Nat.le_trans upper
    (Nat.pow_le_pow_right (by decide) (by decide : 148410 ≤ 148411))

#print axioms small_lower_306
#print axioms small_upper_306
#print axioms small_ratio_306
#print axioms integer_bracket_306

end CollatzBandCertificate
