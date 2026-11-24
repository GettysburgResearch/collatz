import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Affine substitution on polynomial moment states

This checks the all-degree algebraic interface used by the written Weyl
rigidity argument. A moment state is an arbitrary function on polynomials;
no linearity, ordinary realization, topology, or ergodicity is assumed.
The compact solenoid and measurable arguments remain written mathematics.
-/

namespace CollatzShell.PolynomialLift

open Polynomial

noncomputable section

variable {K A B : Type*} [Field K]

def affine (a b : K) : Polynomial K := C a * X + C b

def lift (a b : K) (v : Polynomial K → A) : Polynomial K → A :=
  fun p => v (p.comp (affine a b))

/-- Exact affine composition, in the same order as the lifted actions. -/
theorem affine_comp (a b c d : K) :
    (affine a b).comp (affine c d) = affine (a * c) (a * d + b) := by
  simp only [affine, add_comp, mul_comp, C_comp, X_comp, C_add, C_mul]
  ring

/-- Polynomial substitution lifts the full affine composition law. -/
theorem lift_comp (a b c d : K) (v : Polynomial K → A) :
    lift a b (lift c d v) = lift (a * c) (a * d + b) v := by
  funext p
  simp only [lift, comp_assoc, affine_comp]

theorem lift_identity (v : Polynomial K → A) : lift 1 0 v = v := by
  funext p
  simp [lift, affine]

/-- Nonzero slopes give genuine inverse actions on every moment state. -/
theorem lift_inverse (a b : K) (ha : a ≠ 0) (v : Polynomial K → A) :
    lift a b (lift a⁻¹ (-a⁻¹ * b) v) = v := by
  rw [lift_comp]
  have h : a * (-a⁻¹ * b) + b = 0 := by field_simp; ring
  rw [mul_inv_cancel₀ ha, h, lift_identity]

theorem lift_surjective (a b : K) (ha : a ≠ 0) :
    Function.Surjective (lift a b : (Polynomial K → A) → Polynomial K → A) := by
  intro v
  exact ⟨lift a⁻¹ (-a⁻¹ * b) v, lift_inverse a b ha v⟩

/-- The lift agrees with ordinary affine evaluation on evaluation states. -/
theorem lift_evaluation (a b x : K) :
    lift a b (fun p : Polynomial K => p.eval x) =
      (fun p : Polynomial K => p.eval (a * x + b)) := by
  funext p
  simp [lift, affine, eval_comp]

/-- Constants remain fixed, so every fixed constant-moment slice is preserved. -/
theorem lift_constant (a b c : K) (v : Polynomial K → A) :
    lift a b v (C c) = v (C c) := by
  simp [lift]

/-- Every degree is represented by the exact affine-power substitution. -/
theorem lift_monomial (a b : K) (v : Polynomial K → A) (j : Nat) :
    lift a b v (X ^ j) = v ((C a * X + C b) ^ j) := by
  simp [lift, affine]

variable [CharZero K]

/-- The shortcut affine lifts have a literal translation commutator. -/
theorem shortcut_commutator (v : Polynomial K → A) :
    lift (3 / 2) (1 / 2)
      (lift (1 / 2) 0 (lift (4 / 3) (-1 / 3) v)) =
        lift 1 (1 / 4) v := by
  rw [lift_comp, lift_comp]
  norm_num

theorem quarter_translation_four (v : Polynomial K → A) :
    lift 1 (1 / 4) (lift 1 (1 / 4)
      (lift 1 (1 / 4) (lift 1 (1 / 4) v))) = lift 1 1 v := by
  rw [lift_comp, lift_comp, lift_comp]
  norm_num

/-- Separate shortcut invariance forces translation by one quarter. -/
theorem shortcut_quarter_invariant (f : (Polynomial K → A) → B)
    (even : ∀ v, f (lift (1 / 2) 0 v) = f v)
    (odd : ∀ v, f (lift (3 / 2) (1 / 2) v) = f v) :
    ∀ v, f (lift 1 (1 / 4) v) = f v := by
  have ab : ∀ v, f (lift (3 / 4) (1 / 4) v) = f v := by
    intro v
    have h := (even (lift (3 / 2) (1 / 2) v)).trans (odd v)
    rw [lift_comp] at h
    norm_num at h
    exact h
  have ba : ∀ v, f (lift (3 / 4) (1 / 2) v) = f v := by
    intro v
    have h := (odd (lift (1 / 2) 0 v)).trans (even v)
    rw [lift_comp] at h
    norm_num at h
    exact h
  intro v
  obtain ⟨w, rfl⟩ := lift_surjective (3 / 4 : K) (1 / 4) (by norm_num) v
  rw [lift_comp]
  norm_num
  rw [ba, ab]

/-- The same hypotheses imply the polynomial translation n -> n+1. -/
theorem shortcut_unit_invariant (f : (Polynomial K → A) → B)
    (even : ∀ v, f (lift (1 / 2) 0 v) = f v)
    (odd : ∀ v, f (lift (3 / 2) (1 / 2) v) = f v) :
    ∀ v, f (lift 1 1 v) = f v := by
  intro v
  rw [← quarter_translation_four v]
  simp only [shortcut_quarter_invariant f even odd]

end

end CollatzShell.PolynomialLift
