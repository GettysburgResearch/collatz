import Mathlib.RingTheory.Coprime.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

namespace Collatz.RotationalExclusion

/-- Multiplication of the source in the unnormalized shortcut affine map. -/
def amp : List Bool → ℤ
  | [] => 1
  | b :: w => (if b then 3 else 1) * amp w

/-- Constant term of that same affine map, read in chronological order. -/
def carry : List Bool → ℤ
  | [] => 0
  | b :: w => (if b then 1 else 0) * amp w + 2 * carry w

theorem amp_append (v w : List Bool) : amp (v ++ w) = amp v * amp w := by
  induction v with
  | nil => simp [amp]
  | cons b v ih => simp [amp, ih, mul_assoc]

theorem carry_append (v w : List Bool) :
    carry (v ++ w) = carry v * amp w + 2^v.length * carry w := by
  induction v with
  | nil => simp [carry]
  | cons b v ih =>
    simp only [List.cons_append, carry, amp_append, ih, List.length_cons, pow_succ]
    ring

/-- Whole-period closure at two rotated positions cancels a common suffix.
The hypotheses are cleared closure equations with a common denominator. -/
theorem rotation_dvd (v v' w : List Bool) (D d n n' : ℤ)
    (hlen : v.length = v'.length) (hc : IsCoprime D (amp w))
    (h : D*n = d*carry (v ++ w)) (h' : D*n' = d*carry (v' ++ w)) :
    D ∣ d * (carry v - carry v') := by
  rw [carry_append, hlen] at h
  rw [carry_append] at h'
  apply hc.dvd_of_dvd_mul_right
  use n - n'
  linear_combination h' - h

/-- The reduced divisor K survives any common-denominator transposition once
the elementary binomial gcd has been factored off as G. -/
theorem transposition_dvd (G K U V d E : ℤ) (hG : G ≠ 0)
    (hU : IsCoprime K U) (hV : IsCoprime K V)
    (h : G*K ∣ d*E*V*(G*U)) : K ∣ d*E := by
  obtain ⟨z,hz⟩ := h
  have hh : G*(d*E*V*U) = G*(K*z) := by linear_combination hz
  have hk : K ∣ d*E*V*U := ⟨z, mul_left_cancel₀ hG hh⟩
  exact hV.dvd_of_dvd_mul_right (hU.dvd_of_dvd_mul_right hk)

#print axioms amp_append
#print axioms carry_append
#print axioms rotation_dvd
#print axioms transposition_dvd

end Collatz.RotationalExclusion
