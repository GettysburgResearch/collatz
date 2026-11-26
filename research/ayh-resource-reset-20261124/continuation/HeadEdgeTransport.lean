import TernaryHeadDescent
import Mathlib.Dynamics.Ergodic.Ergodic
import Mathlib.Algebra.Order.Floor.Semifield

/-! Exact digit cells, their ordinary Collatz color, and the local ergodic
step used in the written four-trit edge-rigidity theorem. -/

namespace CollatzShell.TernaryHead

/-- Taking the child digit cell and then truncating gives the parent cell. -/
theorem radix_floor_parent (j : ℕ) (t : ℝ) :
    ⌊(81 : ℝ)^(j+1)*t⌋₊ / 81 = ⌊(81 : ℝ)^j*t⌋₊ := by
  convert Nat.mul_cast_floor_div_cancel (R := ℝ) (n := 81) (by decide) ((81:ℝ)^j*t) using 1
  push_cast
  ring_nf

/-- On an explicit subinterval of each fine radix cell the two integer
samples are connected by physical halving clocks. -/
theorem doubled_floor_mask (k : ℕ) {y : ℝ} (hy : 0 ≤ y)
    (mask : (2:ℝ)^k * (y - (⌊y⌋₊ : ℝ)) < 1) :
    Hits ⌊(2:ℝ)^k*y⌋₊ ⌊y⌋₊ := by
  have eq : ⌊(2:ℝ)^k*y⌋₊ = 2^k*⌊y⌋₊ := by
    apply (Nat.floor_eq_iff (by positivity)).2
    push_cast
    exact ⟨mul_le_mul_of_nonneg_left (Nat.floor_le hy) (by positivity), by linarith [mask]⟩
  exact ⟨k, by rw [eq, orbit_pad]⟩

open MeasureTheory Set
open scoped MeasureTheory

/-- If no nonnegative return of one color class meets the other on a
positive-measure set, the two classes cannot both have positive measure.
The classes may occupy only a proper part of the whole space. -/
theorem local_return_rigidity {α : Type*} [MeasurableSpace α] {μ : Measure α}
    [IsFiniteMeasure μ] {T : α → α} (hT : Ergodic T μ) (P Q : Set α)
    (hQ : MeasurableSet Q) (h : ∀ k : ℕ, μ (P ∩ (T^[k]) ⁻¹' Q) = 0) :
    μ P = 0 ∨ μ Q = 0 := by
  let V := ⋃ k : ℕ, (T^[k]) ⁻¹' Q
  have hV : MeasurableSet V :=
    MeasurableSet.iUnion fun k => (hT.measurable.iterate k) hQ
  have hpre : T ⁻¹' V ⊆ V := by
    intro x hx
    obtain ⟨k, hk⟩ := mem_iUnion.1 (show T x ∈ V from hx)
    exact mem_iUnion.2 ⟨k+1, by simpa only [Set.mem_preimage, Function.iterate_succ_apply] using hk⟩
  have hPV : μ (P ∩ V) = 0 := by
    simpa only [V, inter_iUnion, measure_iUnion_null_iff] using h
  rcases hT.ae_empty_or_univ_of_preimage_ae_le hV.nullMeasurableSet hpre.eventuallySubset with hz|hf
  · right
    have hQV : Q ⊆ V := fun x hx => mem_iUnion.2 ⟨0,hx⟩
    exact measure_mono_null hQV (by simpa using measure_congr hz)
  · left
    have he : P ∩ V =ᵐ[μ] P := by
      filter_upwards [hf] with x hx
      simp only [Set.mem_inter_iff, hx, Set.mem_univ, and_true]
    rwa [← measure_congr he]

#print axioms radix_floor_parent
#print axioms doubled_floor_mask
#print axioms local_return_rigidity

end CollatzShell.TernaryHead
