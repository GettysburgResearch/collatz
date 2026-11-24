import Mathlib.Tactic

/-! Centerwise comparison after the matched pullback of one actual valley.
The positive real variables encode the integer affine coefficients, positive
rational center magnitude numerator and denominator, and dyadic numerator.
The existence of a maximizing center is deliberately not assumed here.
-/

namespace RestrictedEnvelope

theorem strict_matched_nonlinear_transport (P Q C y z h q c g a : ℝ)
    (hP : 0 < P) (hQ : 0 < Q) (hC : 0 < C) (hy : 0 < y) (hz : 0 < z)
    (hh : 0 < h) (hq : 0 < q) (hc : 1 < c) (hg : 1 ≤ g) (ha : 0 < a)
    (actual : Q*z = P*y+C) :
    a / (h+c*q*z) < Q*g*a / (Q*h+C*q+c*P*q*y) := by
  have hc0 : 0 < c := by linarith
  have hdst : 0 < h+c*q*z := by positivity
  have hsrc : 0 < Q*h+C*q+c*P*q*y := by positivity
  have hextra : 0 < (c-1)*C*q := mul_pos (mul_pos (sub_pos.mpr hc) hC) hq
  have hid : Q*(h+c*q*z) = Q*h+C*q+c*P*q*y+(c-1)*C*q := by
    linear_combination c*q*actual
  apply (div_lt_div_iff₀ hdst hsrc).2
  calc
    a*(Q*h+C*q+c*P*q*y) < a*(Q*(h+c*q*z)) :=
      mul_lt_mul_of_pos_left (by linarith) ha
    _ = Q*a*(h+c*q*z) := by ring
    _ ≤ Q*g*a*(h+c*q*z) := by
      have hmul := mul_le_mul_of_nonneg_left hg (le_of_lt hQ)
      have hw : Q ≤ Q*g := by simpa using hmul
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_right hw (le_of_lt ha)) (le_of_lt hdst)

#print axioms strict_matched_nonlinear_transport

end RestrictedEnvelope
