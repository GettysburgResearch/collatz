import Mathlib

namespace TwoEndBridge

theorem compose_three
    (x y z q A B C P Q R u v w : ℤ)
    (hu : A*y = P*x+u) (hm : B*z = Q*y+v)
    (hv : C*q = R*z+w) :
    A*B*C*q = P*Q*R*x+Q*R*u+A*R*v+A*B*w := by
  calc
    A*B*C*q = A*B*(C*q) := by ring
    _ = A*B*(R*z+w) := by rw [hv]
    _ = A*R*(B*z)+A*B*w := by ring
    _ = A*R*(Q*y+v)+A*B*w := by rw [hm]
    _ = Q*R*(A*y)+A*R*v+A*B*w := by ring
    _ = Q*R*(P*x+u)+A*R*v+A*B*w := by rw [hu]
    _ = P*Q*R*x+Q*R*u+A*R*v+A*B*w := by ring

theorem lift_congruence
    (A P x y u r m : ℤ)
    (h : A*y = P*x+u) (hP : P ≠ 0)
    (hr : P*m ∣ A*y-(P*r+u)) :
    m ∣ x-r := by
  obtain ⟨k,hk⟩ := hr
  refine ⟨k, ?_⟩
  have h0 : P*(x-r-m*k)=0 := by
    calc
      P*(x-r-m*k) = (P*x+u)-(P*r+u)-P*m*k := by ring
      _ = A*y-(P*r+u)-P*m*k := by rw [h]
      _ = 0 := by rw [hk]; ring
  rcases mul_eq_zero.mp h0 with h1 | h1
  · exact False.elim (hP h1)
  · linarith

theorem retain_relative_offset
    (q betaTail betaPrefix L epsilon : ℚ)
    (h : epsilon*q ≤ betaTail)
    (hL : 0 ≤ L) (hP : 0 ≤ betaPrefix) :
    epsilon*q ≤ betaTail+L*betaPrefix := by
  have hprod := mul_nonneg hL hP
  linarith

theorem normalization_transfer
    (q0 qi D L : ℚ)
    (hq : qi = q0*D*L)
    (hq0 : q0 ≠ 0) (hD : D ≠ 0) :
    L = qi/(q0*D) := by
  apply (eq_div_iff (mul_ne_zero hq0 hD)).2
  rw [hq]
  ring

end TwoEndBridge

#print axioms TwoEndBridge.compose_three
#print axioms TwoEndBridge.lift_congruence
#print axioms TwoEndBridge.retain_relative_offset
#print axioms TwoEndBridge.normalization_transfer
