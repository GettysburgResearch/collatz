import Mathlib.Logic.Function.Iterate
import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Field
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Exact finite ingredients for the ordinary Green entrance law.

The phase lemmas keep one deterministic map, one injective forward ray,
and one unchanged source. The algebraic lemmas keep the killing term in
the potential transform. Infinite probability measures, total variation,
root variation and entropy are proved in the companion written note.
-/

set_option autoImplicit false

namespace CollatzEntranceLaw

theorem merge_later {α : Type*} (f : α → α) (n p : α)
    (k m t : Nat) (hit : (f^[k]) n = (f^[m]) p) :
    (f^[k + t]) n = (f^[m + t]) p := by
  rw [Nat.add_comm k t, Nat.add_comm m t,
    Function.iterate_add_apply, Function.iterate_add_apply, hit]

theorem merge_phase_unique {α : Type*} (f : α → α) (n p : α)
    (ray : Function.Injective (fun j : Nat => (f^[j]) p))
    (k m l r : Nat)
    (left : (f^[k]) n = (f^[m]) p)
    (right : (f^[l]) n = (f^[r]) p) : k + r = l + m := by
  have hl := merge_later f n p k m l left
  have hr := merge_later f n p l r k right
  have heq : (f^[m + l]) p = (f^[r + k]) p := by
    rw [← hl, ← hr, Nat.add_comm k l]
  have hi := ray heq
  omega

theorem integer_phase_unique {α : Type*} (f : α → α) (n p : α)
    (ray : Function.Injective (fun j : Nat => (f^[j]) p))
    (k m l r : Nat)
    (left : (f^[k]) n = (f^[m]) p)
    (right : (f^[l]) n = (f^[r]) p) :
    (k : Int) - m = (l : Int) - r := by
  have := merge_phase_unique f n p ray k m l r left right
  omega

theorem phase_at_late_root {α : Type*} (f : α → α) (n p : α)
    (k m j : Nat) (hit : (f^[k]) n = (f^[m]) p) (late : m ≤ j) :
    ∃ τ : Nat, (f^[τ]) n = (f^[j]) p ∧
      (τ : Int) - j = (k : Int) - m := by
  refine ⟨k + (j - m), ?_, ?_⟩
  · simpa [Nat.add_sub_of_le late] using merge_later f n p k m (j - m) hit
  · omega

theorem ray_hit_unique {α : Type*} (f : α → α) (n p : α)
    (ray : Function.Injective (fun j : Nat => (f^[j]) p))
    (k l m : Nat)
    (left : (f^[k]) n = (f^[m]) p)
    (right : (f^[l]) n = (f^[m]) p) : k = l := by
  have := merge_phase_unique f n p ray k m l m left right
  omega

noncomputable def rawWeight (w : Nat → Real) : Nat → Real
  | 0 => 1
  | k + 1 => rawWeight w k * w k

noncomputable def transformedWeight (w z : Nat → Real) : Nat → Real
  | 0 => 1
  | k + 1 => transformedWeight w z k * (w k * z (k + 1) / z k)

theorem transformed_telescope (w z : Nat → Real)
    (nonzero : ∀ k, z k ≠ 0) (k : Nat) :
    transformedWeight w z k = rawWeight w k * z k / z 0 := by
  induction k with
  | zero => simp [transformedWeight, rawWeight, nonzero]
  | succ k ih =>
    rw [transformedWeight, rawWeight, ih]
    field_simp [nonzero]

theorem stopped_path_weight (w z : Nat → Real)
    (nonzero : ∀ k, z k ≠ 0) (k : Nat) :
    transformedWeight w z k / z k = rawWeight w k / z 0 := by
  rw [transformed_telescope w z nonzero k]
  field_simp [nonzero]

theorem finite_killed_row {ι : Type*} (a : Finset ι)
    (w z : ι → Real) (Z : Real) (nonzero : Z ≠ 0)
    (potential : Z = 1 + ∑ i ∈ a, w i * z i) :
    1 / Z + ∑ i ∈ a, (w i * z i / Z) = 1 := by
  simp only [← Finset.sum_div]
  rw [← add_div]
  rw [← potential, div_self nonzero]

theorem normalized_tilt_rescaling (p w c Z : Real)
    (hc : c ≠ 0) (hZ : Z ≠ 0) :
    (c * w * p) / (c * Z) = (w * p) / Z := by
  field_simp

#print axioms merge_later
#print axioms merge_phase_unique
#print axioms integer_phase_unique
#print axioms phase_at_late_root
#print axioms ray_hit_unique
#print axioms transformed_telescope
#print axioms stopped_path_weight
#print axioms finite_killed_row
#print axioms normalized_tilt_rescaling

end CollatzEntranceLaw
