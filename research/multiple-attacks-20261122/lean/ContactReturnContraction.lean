module

public import ShellCover
public import Mathlib.Basic.Real.Basic
public import Mathlib.Algebra.Order.BigOperators.Ring.Finset

@[expose] public section

/-!
# Finite contact-return contraction

The analytic construction of the ordinary harmonic flow and the arithmetic
two-parent bound are explicit inputs to the accompanying written theorem.
This module proves the finite weighted-row contraction, the exact finite
source-fiber aggregation, and its geometric iteration and physical-height
consequences. It does not assume or prove universal Collatz convergence.
-/

namespace CollatzContactReturn

open scoped BigOperators

/-- Squaring the harmonic reference gives a strictly subinvariant row
when no incoming atom exceeds `rho` times its target reference. -/
theorem square_reference_row {I : Type*} (s : Finset I) (w : I → ℝ)
    (v rho : ℝ) (hv : 0 ≤ v) (hrho : 0 ≤ rho)
    (hw : ∀ i ∈ s, 0 ≤ w i)
    (hmax : ∀ i ∈ s, w i ≤ rho * v)
    (hrow : (∑ i ∈ s, w i) ≤ v) :
    (∑ i ∈ s, (w i)^2) ≤ rho * v^2 := by
  calc
    (∑ i ∈ s, (w i)^2) ≤ ∑ i ∈ s, (rho * v) * w i := by
      apply Finset.sum_le_sum
      intro i hi
      have h := mul_le_mul_of_nonneg_right (hmax i hi) (hw i hi)
      nlinarith only [h]
    _ = (rho * v) * (∑ i ∈ s, w i) := by rw [Finset.mul_sum]
    _ ≤ (rho * v) * v :=
      mul_le_mul_of_nonneg_left hrow (mul_nonneg hrho hv)
    _ = rho * v^2 := by ring

/-- The normalized energy of one actual source fiber is contracted. Here
`w i * f i` is the original mass at source `i`, not a resampled endpoint. -/
theorem fiber_energy_bound {I : Type*} (s : Finset I) (w f : I → ℝ)
    (v rho : ℝ) (hv : 0 < v)
    (hrow : (∑ i ∈ s, (w i)^2) ≤ rho * v^2) :
    ((∑ i ∈ s, w i * f i) / v)^2 ≤ rho * (∑ i ∈ s, (f i)^2) := by
  have hc := Finset.sum_mul_sq_le_sq_mul_sq s w f
  have hf : 0 ≤ ∑ i ∈ s, (f i)^2 :=
    Finset.sum_nonneg (fun i _ => sq_nonneg (f i))
  have hb := mul_le_mul_of_nonneg_right hrow hf
  have hv2 : 0 < v^2 := sq_pos_of_pos hv
  rw [div_pow]
  apply (div_le_iff₀ hv2).2
  nlinarith only [hc, hb]

/-- Sum the exact disjoint source fibers. Each original source has one
forward next-contact target, so it is charged exactly once. -/
theorem finite_source_energy_contraction {I J : Type*} [DecidableEq J]
    (sources : Finset I) (targets : Finset J) (next : I → J)
    (maps : ∀ i ∈ sources, next i ∈ targets)
    (w f : I → ℝ) (v : J → ℝ) (rho : ℝ)
    (positive : ∀ j ∈ targets, 0 < v j)
    (rows : ∀ j ∈ targets,
      (∑ i ∈ sources.filter (fun i => next i = j), (w i)^2) ≤ rho * (v j)^2) :
    (∑ j ∈ targets,
      ((∑ i ∈ sources.filter (fun i => next i = j), w i * f i) / v j)^2)
      ≤ rho * (∑ i ∈ sources, (f i)^2) := by
  calc
    _ ≤ ∑ j ∈ targets,
        rho * (∑ i ∈ sources.filter (fun i => next i = j), (f i)^2) := by
      apply Finset.sum_le_sum
      intro j hj
      exact fiber_energy_bound _ w f (v j) rho (positive j hj) (rows j hj)
    _ = rho * (∑ j ∈ targets,
        ∑ i ∈ sources.filter (fun i => next i = j), (f i)^2) := by
      rw [Finset.mul_sum]
    _ = rho * (∑ i ∈ sources, (f i)^2) := by
      rw [Finset.sum_fiberwise_of_maps_to maps]

/-- Iterating a positive contraction gives the full geometric budget. -/
theorem geometric_energy_bound (E : ℕ → ℝ) (rho : ℝ) (hrho : 0 ≤ rho)
    (step : ∀ k, E (k+1) ≤ rho * E k) (k : ℕ) :
    E k ≤ rho^k * E 0 := by
  induction k with
  | zero => simp
  | succ k ih =>
      calc
        E (k+1) ≤ rho * E k := step k
        _ ≤ rho * (rho^k * E 0) := mul_le_mul_of_nonneg_left ih hrho
        _ = rho^(k+1) * E 0 := by rw [pow_succ]; ring

/-- Along a forward chain of actual contacts the harmonic masses grow
geometrically; this form avoids division by a small power. -/
theorem forward_contact_mass (v : ℕ → ℝ) (rho : ℝ) (hrho : 0 ≤ rho)
    (step : ∀ k, v k ≤ rho * v (k+1)) (k : ℕ) :
    v 0 ≤ rho^k * v k := by
  induction k with
  | zero => simp
  | succ k ih =>
      have h := mul_le_mul_of_nonneg_left (step k) (pow_nonneg hrho k)
      calc
        v 0 ≤ rho^k * v k := ih
        _ ≤ rho^k * (rho * v (k+1)) := h
        _ = rho^(k+1) * v (k+1) := by rw [pow_succ]; ring

/-- Bounded contact profiles turn geometric mass growth into deterministic
physical-height descent at successive forward contacts. -/
theorem forward_contact_height (h v : ℕ → ℝ) (rho gamma M : ℝ)
    (hrho : 0 ≤ rho) (height : ∀ k, 0 ≤ h k)
    (lower : gamma ≤ h 0 * v 0)
    (upper : ∀ k, h k * v k ≤ M)
    (step : ∀ k, v k ≤ rho * v (k+1)) (k : ℕ) :
    gamma * h k ≤ M * rho^k * h 0 := by
  have mass := forward_contact_mass v rho hrho step k
  calc
    gamma * h k ≤ (h 0 * v 0) * h k :=
      mul_le_mul_of_nonneg_right lower (height k)
    _ = (h 0 * h k) * v 0 := by ring
    _ ≤ (h 0 * h k) * (rho^k * v k) :=
      mul_le_mul_of_nonneg_left mass (mul_nonneg (height 0) (height k))
    _ = (rho^k * h 0) * (h k * v k) := by ring
    _ ≤ (rho^k * h 0) * M :=
      mul_le_mul_of_nonneg_left (upper k) (mul_nonneg (pow_nonneg hrho k) (height 0))
    _ = M * rho^k * h 0 := by ring

/-- The inverse orientation gives exponential height growth per contact.
The ordinary number of steps between contacts is not bounded here. -/
theorem inverse_contact_height (h v : ℕ → ℝ) (rho gamma M : ℝ)
    (hrho : 0 ≤ rho) (height : ∀ k, 0 ≤ h k)
    (lower : ∀ k, gamma ≤ h k * v k)
    (upper : h 0 * v 0 ≤ M)
    (step : ∀ k, v (k+1) ≤ rho * v k) (k : ℕ) :
    gamma * h 0 ≤ M * rho^k * h k := by
  have mass := geometric_energy_bound v rho hrho step k
  calc
    gamma * h 0 ≤ (h k * v k) * h 0 :=
      mul_le_mul_of_nonneg_right (lower k) (height 0)
    _ = (h k * h 0) * v k := by ring
    _ ≤ (h k * h 0) * (rho^k * v 0) :=
      mul_le_mul_of_nonneg_left mass (mul_nonneg (height k) (height 0))
    _ = (rho^k * h k) * (h 0 * v 0) := by ring
    _ ≤ (rho^k * h k) * M :=
      mul_le_mul_of_nonneg_left upper (mul_nonneg (pow_nonneg hrho k) (height k))
    _ = M * rho^k * h k := by ring

end CollatzContactReturn

#print axioms CollatzContactReturn.square_reference_row
#print axioms CollatzContactReturn.fiber_energy_bound
#print axioms CollatzContactReturn.finite_source_energy_contraction
#print axioms CollatzContactReturn.geometric_energy_bound
#print axioms CollatzContactReturn.forward_contact_mass
#print axioms CollatzContactReturn.forward_contact_height
#print axioms CollatzContactReturn.inverse_contact_height
