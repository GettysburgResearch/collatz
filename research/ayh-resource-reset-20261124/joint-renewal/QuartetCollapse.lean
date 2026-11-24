import OffsetDescent

/-! The old head edge at 32q+23 has two different affine outputs at clock
five. Under either of two standard parameter dilations, both new arms share
the old upper output by clock five or six, respectively. -/
namespace CollatzShell.QuartetCollapse

open OffsetDescent

private theorem lift_coeff (t a b p e q : Nat)
    (hp : 3^(oddCount t b)*a=p) (he : orbit t b=e) :
    orbit t (a*(2^t*q)+b)=p*q+e := by
  rw [show a*(2^t*q)+b=2^t*(a*q)+b by ring, affine_lift, he, ← Nat.mul_assoc, hp]

/-- Two different ordinary affine outputs remain on the original cylinder. -/
theorem original_outputs (q : Nat) :
    orbit 5 (32*q+23)=27*q+20 ∧
    orbit 5 (81*(32*q+23)+73)=243*q+182 := by
  constructor
  · rw [show 32*q+23=1*(2^5*q)+23 by ring]
    exact lift_coeff 5 1 23 27 20 q (by decide) (by decide)
  · rw [show 81*(32*q+23)+73=81*(2^5*q)+1936 by ring]
    exact lift_coeff 5 81 1936 243 182 q (by decide) (by decide)

/-- Tripling with digit two collapses both new arms into the old upper arm. -/
theorem triple_outputs (q : Nat) :
    orbit 5 (3*(32*q+23)+2)=243*q+182 ∧
    orbit 5 (81*(3*(32*q+23)+2)+73)=243*q+182 := by
  constructor
  · rw [show 3*(32*q+23)+2=3*(2^5*q)+71 by ring]
    exact lift_coeff 5 3 71 243 182 q (by decide) (by decide)
  · rw [show 81*(3*(32*q+23)+2)+73=243*(2^5*q)+5824 by ring]
    exact lift_coeff 5 243 5824 243 182 q (by decide) (by decide)

/-- Doubling with digit one has the same collapse with its extra clock. -/
theorem double_outputs (q : Nat) :
    orbit 6 (2*(32*q+23)+1)=243*q+182 ∧
    orbit 6 (81*(2*(32*q+23)+1)+73)=243*q+182 := by
  constructor
  · rw [show 2*(32*q+23)+1=1*(2^6*q)+47 by ring]
    exact lift_coeff 6 1 47 243 182 q (by decide) (by decide)
  · rw [show 81*(2*(32*q+23)+1)+73=81*(2^6*q)+3880 by ring]
    exact lift_coeff 6 81 3880 243 182 q (by decide) (by decide)

/-- The remaining pair has canonical level two and offset two on every lift. -/
theorem residual_profile (q : Nat) :
    orbit 5 (81*(32*q+23)+73)=3^2*orbit 5 (32*q+23)+2 ∧
      orbit 5 (32*q+23)<orbit 5 (81*(32*q+23)+73) := by
  obtain ⟨hl,hu⟩ := original_outputs q
  rw [hu,hl]
  constructor <;> omega

end CollatzShell.QuartetCollapse
