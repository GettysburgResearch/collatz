import RepeatedTail
import Mathlib.Algebra.Order.BigOperators.Ring.Finset

/-! Complete-fiber quadratic transport and the actual first-return clock.

The moment theorem and infinite L^p estimate are proved in RETURN_ATTACK.md.
This file checks the finite quadratic inequality without dropping collisions,
and derives the actual positive return clock from the existing section theorem.
-/

namespace CollatzShell.ReturnCritical

open Finset ForwardSection InverseDensityPotential WideRepeatedTail

private theorem bounded_odd_section (n : Nat) (hn : n % 2 = 1) :
    ∃ j, j < 2 * n.sqrt ∧ InSection (oddOrbit n j) := by
  induction n using Nat.strong_induction_on with
  | h n ih =>
    obtain ⟨i, hi, drop | mark⟩ := descent_or_section n hn
    · let y := oddOrbit n i
      have hy : y < n := by change 4*y < n at drop; omega
      have yo := (odd_orbit_positive_odd n (by omega) hn i).2
      obtain ⟨j, hj, hm⟩ := ih y hy yo
      have budget : 2*y.sqrt ≤ n.sqrt := Nat.le_sqrt.mpr (by
        have sq := Nat.sqrt_le y
        change 4*y < n at drop
        nlinarith only [sq, drop])
      refine ⟨i+j, by omega, ?_⟩
      rw [odd_orbit_add]
      exact hm
    · exact ⟨i, by omega, mark⟩

/-- The positive marked return exists within a quadratic source budget.
The source is the actual original odd integer, with no refreshed law. -/
theorem positive_return_clock (n : Nat) (hn : n % 2 = 1) :
    ∃ t : Nat, 0 < t ∧ t*t ≤ 8*n ∧ Marked (oddOrbit n t) := by
  have pos : 0 < n := by omega
  have ho := (odd_step_unit n).2.1
  obtain ⟨j, hj, hm⟩ := bounded_odd_section (oddStep n) ho
  have sz := odd_step_le_double n pos hn
  have sq := Nat.sqrt_le (oddStep n)
  have bound : (j+1)*(j+1) ≤ 8*n := by
    have hle : j+1 ≤ 2*(oddStep n).sqrt := by omega
    nlinarith [sq_nonneg (Int.ofNat (2*(oddStep n).sqrt - (j+1)))]
  refine ⟨j+1, by omega, bound, ?_⟩
  have eq : oddOrbit n (j+1) = oddOrbit (oddStep n) j := by
    rw [Nat.add_comm j 1, odd_orbit_add]
    rfl
  rw [eq]
  exact ⟨(odd_orbit_positive_odd (oddStep n) (odd_step_unit n).1 ho j).2, hm⟩

/-- Minimality transfers the same source budget to the actual first
strictly positive return, including a return within a periodic orbit. -/
theorem first_return_clock_square_bound (n t : Nat) (hn : n % 2 = 1)
    (first : ∀ j : Nat, 0 < j → j < t → ¬ Marked (oddOrbit n j)) :
    t*t ≤ 8*n := by
  obtain ⟨j, hj, bound, mark⟩ := positive_return_clock n hn
  have lower : t ≤ j := by
    by_contra h
    exact first j hj (by omega) mark
  nlinarith

/-- Weighted Cauchy--Schwarz on one complete endpoint fiber. Original
source weights remain literal; the reference may contain additional mass. -/
theorem fiber_quadratic_bound {ι : Type*} (S : Finset ι)
    (w c : ι → ℝ) (lam : ℝ)
    (hw : ∀ i ∈ S, 0 ≤ w i) (hc : ∀ i ∈ S, 0 < c i)
    (hlam : 0 < lam) (reference : ∑ i ∈ S, c i * w i ≤ lam) :
    (∑ i ∈ S, w i)^2 / lam ≤ ∑ i ∈ S, w i / c i := by
  have hn : 0 ≤ ∑ i ∈ S, w i / c i :=
    sum_nonneg (fun i hi => div_nonneg (hw i hi) (hc i hi).le)
  have cs := sum_sq_le_sum_mul_sum_of_sq_le_mul S
    (fun i hi => mul_nonneg (hc i hi).le (hw i hi))
    (fun i hi => div_nonneg (hw i hi) (hc i hi).le)
    (fun i hi => show (w i)^2 ≤ (c i * w i) * (w i / c i) by
      have ne := (hc i hi).ne'
      field_simp
      nlinarith)
  apply (div_le_iff₀ hlam).mpr
  calc
    (∑ i ∈ S, w i)^2 ≤ (∑ i ∈ S, c i*w i) * ∑ i ∈ S, w i/c i := cs
    _ ≤ lam * ∑ i ∈ S, w i/c i := mul_le_mul_of_nonneg_right reference hn
    _ = (∑ i ∈ S, w i/c i) * lam := mul_comm _ _

/-- Aggregate quadratic transport, with all collisions grouped by their
actual common endpoint. Its bound is a sum over the original sources. -/
theorem aggregate_quadratic_bound {ι κ : Type*} [DecidableEq κ]
    (S : Finset ι) (f : ι → κ) (w c : ι → ℝ) (lam : κ → ℝ)
    (hw : ∀ i ∈ S, 0 ≤ w i) (hc : ∀ i ∈ S, 0 < c i)
    (hlam : ∀ m ∈ S.image f, 0 < lam m)
    (reference : ∀ m ∈ S.image f,
      ∑ i ∈ S with f i = m, c i*w i ≤ lam m) :
    (∑ m ∈ S.image f, (∑ i ∈ S with f i = m, w i)^2 / lam m)
      ≤ ∑ i ∈ S, w i/c i := by
  calc
    _ ≤ ∑ m ∈ S.image f, ∑ i ∈ S with f i = m, w i/c i := by
      apply sum_le_sum
      intro m hm
      exact fiber_quadratic_bound (S.filter (fun i => f i=m)) w c (lam m)
        (fun i hi => hw i (mem_filter.mp hi).1)
        (fun i hi => hc i (mem_filter.mp hi).1)
        (hlam m hm) (reference m hm)
    _ = _ := sum_fiberwise_of_maps_to (fun i hi => mem_image_of_mem f hi) _

#print axioms positive_return_clock
#print axioms first_return_clock_square_bound
#print axioms fiber_quadratic_bound
#print axioms aggregate_quadratic_bound

end CollatzShell.ReturnCritical
