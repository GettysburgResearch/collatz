import Mathlib.Tactic.GCongr
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Exact integer height charges used by the arbitrary-clock denominator proof. -/
set_option autoImplicit false
namespace Collatz.InfiniteDescent.PhysicalCharges

/-- Odd-step carry; the final division exponent does not affect the carry. -/
def carry : List ℕ → ℕ
  | [] => 0
  | e::es => 3^es.length + 2^e * carry es

theorem carry_budget (es : List ℕ) :
    2 * carry es + 2^es.sum ≤ 2^es.sum * 3^es.length := by
  induction es with
  | nil => simp [carry]
  | cons e es ih =>
    simp only [carry,List.sum_cons,List.length_cons,pow_add,pow_succ]
    have base : 1 ≤ 2^e * 2^es.sum := Nat.succ_le_of_lt (by positivity)
    calc
      2*(3^es.length+2^e*carry es)+2^e*2^es.sum =
          2*3^es.length+2^e*(2*carry es+2^es.sum) := by ring
      _ ≤ 2*3^es.length+2^e*(2^es.sum*3^es.length) := by gcongr
      _ ≤ (2^e*2^es.sum)*(3^es.length*3) := by
        have h := Nat.mul_le_mul_right (2*3^es.length) base
        nlinarith only [h]

theorem high_start_carry (es : List ℕ) (Y : ℕ) (sep : 2^es.sum≤Y) :
    2*carry es < 3^es.length*Y := by
  have positive : 0 < 2^es.sum := by positivity
  have b := carry_budget es
  have t : 2*carry es < 2^es.sum*3^es.length := by omega
  simpa [Nat.mul_comm] using lt_of_lt_of_le t (Nat.mul_le_mul_right (3^es.length) sep)

theorem higher_clock (es : List ℕ) (q Y Yend d : ℕ) (sep : 2^es.sum≤Y)
    (clock : 2^(es.sum+d)*Yend = 3^es.length*Y+q*carry es) :
    2*(2^(es.sum+d)*Yend) ≤ (2+q)*(3^es.length*Y) := by
  rw [clock]
  have b := Nat.mul_le_mul_left q (high_start_carry es Y sep).le
  nlinarith only [b]

theorem shifted_step (q y z e : ℕ) (branch : 2^e*z=3*y+q) (he : 1≤e) :
    2*(z+q) ≤ 3*(y+q) := by
  have h : 2^1 ≤ 2^e := Nat.pow_le_pow_right (by decide) he
  have zle := Nat.mul_le_mul_right z h
  simp only [pow_one] at zle
  omega

theorem charged_step (q y z e : ℕ) (branch : 2^e*z=3*y+q) (hz : 1≤z) :
    2^e*(z+q) ≤ 3*(q+1)*(y+q) := by
  have h := Nat.mul_le_mul_left q hz
  have shift : z+q≤(1+q)*z := by nlinarith only [h]
  calc
    2^e*(z+q) ≤ 2^e*((1+q)*z) := Nat.mul_le_mul_left _ shift
    _ = (q+1)*(2^e*z) := by ring
    _ = (q+1)*(3*y+q) := by rw [branch]
    _ ≤ (q+1)*(3*(y+q)) := Nat.mul_le_mul_left _ (by omega)
    _ = 3*(q+1)*(y+q) := by ring

end Collatz.InfiniteDescent.PhysicalCharges
