import Mathlib.Data.Fintype.Prod
import Mathlib.Tactic.Ring

/-! The primitive direction of the two ordinary clocks has uniform fibers modulo every modulus.
A Bézout identity over the integers may be reduced into any finite commutative ring. -/

namespace Collatz.ReciprocalRigidity.ClockResidues

variable {R : Type*} [CommRing R]

/-- A full coordinate change with prescribed primitive first row. -/
def coordinates (a b u v : R) (h : a*u+b*v=1) : R × R ≃ R × R where
  toFun z := (a*z.1-b*z.2,v*z.1+u*z.2)
  invFun z := (u*z.1+b*z.2,-v*z.1+a*z.2)
  left_inv z := by
    apply Prod.ext
    · change u*(a*z.1-b*z.2)+b*(v*z.1+u*z.2)=z.1
      calc
        _ = (a*u+b*v)*z.1 := by ring
        _ = _ := by rw [h, one_mul]
    · change -v*(a*z.1-b*z.2)+a*(v*z.1+u*z.2)=z.2
      calc
        _ = (a*u+b*v)*z.2 := by ring
        _ = _ := by rw [h, one_mul]
  right_inv z := by
    apply Prod.ext
    · change a*(u*z.1+b*z.2)-b*(-v*z.1+a*z.2)=z.1
      calc
        _ = (a*u+b*v)*z.1 := by ring
        _ = _ := by rw [h, one_mul]
    · change v*(u*z.1+b*z.2)+u*(-v*z.1+a*z.2)=z.2
      calc
        _ = (a*u+b*v)*z.2 := by ring
        _ = _ := by rw [h, one_mul]

/-- Windows in the projected coordinate retain one free clock coordinate exactly. -/
def windowEquiv (a b u v : R) (h : a*u+b*v=1) (allowed : R → Prop) :
    {z : R × R // allowed (a*z.1-b*z.2)} ≃ {t : R // allowed t} × R where
  toFun z := (⟨_,z.property⟩,(coordinates a b u v h z.val).2)
  invFun z := ⟨(coordinates a b u v h).symm (z.1.val,z.2), by
    have he := congrArg Prod.fst ((coordinates a b u v h).apply_symm_apply (z.1.val,z.2))
    change allowed ((coordinates a b u v h) ((coordinates a b u v h).symm (z.1.val,z.2))).1
    rw [he]
    exact z.1.property⟩
  left_inv z := Subtype.ext ((coordinates a b u v h).symm_apply_apply z.val)
  right_inv z := by
    apply Prod.ext
    · apply Subtype.ext
      exact congrArg Prod.fst ((coordinates a b u v h).apply_symm_apply (z.1.val,z.2))
    · change ((coordinates a b u v h) ((coordinates a b u v h).symm (z.1.val,z.2))).2=z.2
      rw [Equiv.apply_symm_apply]

theorem card_window [Fintype R] (a b u v : R) (h : a*u+b*v=1)
    (allowed : R → Prop) [DecidablePred allowed] :
    Fintype.card {z : R × R // allowed (a*z.1-b*z.2)} =
      Fintype.card {t : R // allowed t} * Fintype.card R := by
  rw [Fintype.card_congr (windowEquiv a b u v h allowed), Fintype.card_prod]

end Collatz.ReciprocalRigidity.ClockResidues

#print axioms Collatz.ReciprocalRigidity.ClockResidues.coordinates
#print axioms Collatz.ReciprocalRigidity.ClockResidues.windowEquiv
#print axioms Collatz.ReciprocalRigidity.ClockResidues.card_window
