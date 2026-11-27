import ParitySeries
import Mathlib.Data.Nat.ModEq
import Mathlib.Topology.NoetherianSpace
import Mathlib.Topology.Clopen
import Mathlib.Data.Fintype.Pigeonhole

/-! A continuous update and a clopen physical parity observable on a
Noetherian space can represent only finitely many ordinary Collatz heights. -/
namespace Collatz.WeightedParity

open Function Set TopologicalSpace

/-- The parity-cylinder cancellation follows the proof at PR209,
    PhysicalEcho.agree_congruent, on this file pair's physical trajectory. -/
private theorem mod_of_bits (h x y : ℕ)
    (same : ∀ i < h, bit (trajectory x i) = bit (trajectory y i)) :
    x ≡ y [MOD 2^h] := by
  induction h generalizing x y with
  | zero => simp [Nat.ModEq, Nat.mod_one]
  | succ h ih =>
    have hp : x % 2 = y % 2 := same 0 (by omega)
    have ht : step x ≡ step y [MOD 2^h] :=
      ih (step x) (step y) (fun i hi => same (i+1) (by omega))
    have hm := ht.mul_left' 2
    rw [← pow_succ'] at hm
    by_cases hx : x % 2 = 0
    · have hy := hp.symm.trans hx
      have ex : 2 * step x = x := by simp [step, hx]; omega
      have ey : 2 * step y = y := by simp [step, hy]; omega
      rwa [ex, ey] at hm
    · have hy : y % 2 ≠ 0 := by omega
      have ex : 2 * step x = 3*x+1 := by simp [step, hx]; omega
      have ey : 2 * step y = 3*y+1 := by simp [step, hy]; omega
      rw [ex, ey] at hm
      have hc : Nat.Coprime (2 ^ (h+1)) 3 :=
        (show Nat.Coprime 2 3 from by decide).pow_left _
      exact Nat.ModEq.cancel_left_of_coprime hc (hm.add_right_cancel' 1)

theorem states_of_all_bits {x y : ℕ}
    (same : ∀ i, bit (trajectory x i) = bit (trajectory y i)) : x = y := by
  let h := max x y
  have hx : x < 2^h := (le_max_left x y).trans_lt h.lt_two_pow_self
  have hy : y < 2^h := (le_max_right x y).trans_lt h.lt_two_pow_self
  exact (mod_of_bits h x y (fun i _ => same i)).eq_of_lt_of_lt hx hy

variable {X : Type*} [TopologicalSpace X]

theorem height_constant_on_component (f : X → X) (hf : Continuous f)
    (height : X → ℕ) (physical : ∀ v, height (f v) = step (height v))
    (evenOpenClosed : IsClopen {v | bit (height v) = 0})
    {C : Set X} (hC : IsPreirreducible C) {u v : X} (hu : u ∈ C) (hv : v ∈ C) :
    height u = height v := by
  have runs (i : ℕ) (w : X) : height (f^[i] w) = trajectory (height w) i := by
    induction i generalizing w with
    | zero => rfl
    | succ i ih => rw [Function.iterate_succ_apply, ih, physical, trajectory]
  apply states_of_all_bits
  intro i
  rw [← runs, ← runs]
  let E : Set X := (f^[i]) ⁻¹' {v | bit (height v) = 0}
  have hE : IsClopen E := evenOpenClosed.preimage (hf.iterate i)
  have cover : C ⊆ E ∪ Eᶜ := by simp
  rcases (isPreirreducible_iff_isClosed_union_isClosed.mp hC)
      E Eᶜ hE.isClosed hE.isOpen.isClosed_compl cover with h | h
  · exact (h hu : _ = 0).trans (h hv : _ = 0).symm
  · have a : height (f^[i] u) % 2 ≠ 0 := h hu
    have b : height (f^[i] v) % 2 ≠ 0 := h hv
    unfold bit
    omega

/-- Applies also to the orbit subspace, so indeterminacy away from the
    physical hidden orbit plays no role. -/
theorem noetherian_finite_heights [NoetherianSpace X] (f : X → X) (hf : Continuous f)
    (height : X → ℕ) (physical : ∀ v, height (f v) = step (height v))
    (evenOpenClosed : IsClopen {v | bit (height v) = 0}) : (range height).Finite := by
  classical
  let : Finite (irreducibleComponents X) :=
    NoetherianSpace.finite_irreducibleComponents.to_subtype
  let representative (C : irreducibleComponents X) : X := C.property.1.nonempty.choose
  refine (Set.finite_range (fun C => height (representative C))).subset ?_
  rintro _ ⟨v, rfl⟩
  let C : irreducibleComponents X :=
    ⟨irreducibleComponent v, irreducibleComponent_mem_irreducibleComponents v⟩
  refine ⟨C, height_constant_on_component f hf height physical evenOpenClosed
    C.property.1.isPreirreducible ?_ ?_⟩
  · exact C.property.1.nonempty.choose_spec
  · exact mem_irreducibleComponent

#print axioms states_of_all_bits
#print axioms height_constant_on_component
#print axioms noetherian_finite_heights
end Collatz.WeightedParity
