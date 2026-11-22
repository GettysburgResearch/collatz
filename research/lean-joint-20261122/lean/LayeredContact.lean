import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite scalar core of the contact-layer reference construction.
The actual harmonic flow, finite future-contact count, inverse contact
law, and infinite summations are source-qualified written inputs in
ORDINARY_BOUNDARY.md. They are not asserted here as Lean axioms.
-/

namespace CollatzShell.LayeredContact

open Finset

/-- A contact atom keeps the original root's density bound when the
forward harmonic mass grows and its contact-layer weight grows. -/
theorem contact_atom_reference_bound
    (κ c₀ c ν₀ ν νx μ σ : ℝ)
    (hκ : 0 < κ) (hc₀ : 0 < c₀) (hν₀ : 0 < ν₀)
    (hc : c₀ ≤ c) (hν : ν₀ ≤ ν) (hμ : 0 ≤ μ)
    (atom : μ*ν = νx) (reference : κ*c*νx ≤ σ) :
    μ ≤ σ/(κ*c₀*ν₀) := by
  have hcp : 0 ≤ c := le_trans hc₀.le hc
  have hνp : 0 < ν := lt_of_lt_of_le hν₀ hν
  have hd : 0 < κ*c₀*ν₀ := by positivity
  apply (le_div_iff₀ hd).2
  calc
    μ*(κ*c₀*ν₀) = κ*c₀*(μ*ν₀) := by ring
    _ ≤ κ*c₀*(μ*ν) := mul_le_mul_of_nonneg_left
      (mul_le_mul_of_nonneg_left hν hμ) (by positivity)
    _ = κ*c₀*νx := by rw [atom]
    _ ≤ κ*c*νx := by
      have hx : 0 ≤ νx := by rw [← atom]; positivity
      exact mul_le_mul_of_nonneg_right
        (mul_le_mul_of_nonneg_left hc hκ.le) hx
    _ ≤ σ := reference

/-- All original labels and all their endpoint collisions survive this
finite summation. An infinite-source conclusion additionally needs the
explicit summable majorant supplied in the written theorem. -/
theorem original_packet_bound {ι : Type*} (F : Finset ι)
    (weight kernel budget : ι → ℝ) (σ : ℝ)
    (positive : ∀ i ∈ F, 0 ≤ weight i)
    (bound : ∀ i ∈ F, kernel i ≤ σ*budget i) :
    (∑ i ∈ F, weight i*kernel i) ≤
      σ*(∑ i ∈ F, weight i*budget i) := by
  calc
    (∑ i ∈ F, weight i*kernel i) ≤
        ∑ i ∈ F, weight i*(σ*budget i) :=
      sum_le_sum (fun i hi => mul_le_mul_of_nonneg_left (bound i hi) (positive i hi))
    _ = σ*(∑ i ∈ F, weight i*budget i) := by
      rw [mul_sum]
      apply sum_congr rfl
      intro i _
      ring

/-- The square-root layer weights have a useful polynomial lower bound.
Here A and B are successive positive square roots; their square
identities are retained explicitly, so no analytic limit is hidden. -/
theorem reciprocal_root_weight_lower (A B : ℝ)
    (hA : 0 < A) (hB : 0 < B) (ordered : A ≤ B)
    (square_step : B^2-A^2 = 1) :
    1/(2*B^3) ≤ 1/A-1/B := by
  have hAB : 0 < A*B := mul_pos hA hB
  have hden : 0 < 2*B^3 := by positivity
  have hsum : 0 < A+B := by positivity
  have factor : (B-A)*(B+A) = 1 := by nlinarith [square_step]
  have diff : 0 < B-A := by
    by_contra hn
    have hzero : B-A = 0 := by linarith
    rw [hzero, zero_mul] at factor
    norm_num at factor
  have base : A*(B+A) ≤ 2*B^2 := by nlinarith
  have paid := mul_le_mul_of_nonneg_right base diff.le
  have cancel : A*(B+A)*(B-A) = A := by
    calc
      _ = A*((B-A)*(B+A)) := by ring
      _ = A := by rw [factor, mul_one]
  rw [cancel] at paid
  have rewrite_diff : 1/A-1/B = (B-A)/(A*B) := by field_simp
  rw [rewrite_diff]
  apply (div_le_div_iff₀ hden hAB).2
  nlinarith only [mul_le_mul_of_nonneg_right paid hB.le]

/-- Bounded nonnegative densities turn L1 convergence into each finite
integer Lp convergence. The written result also covers real p>=1. -/
theorem bounded_density_power (g h M : ℝ) (p : ℕ)
    (hg : 0 ≤ g) (hh : 0 ≤ h) (gM : g ≤ M) (hM : h ≤ M) :
    |g-h|^(p+1) ≤ M^p*|g-h| := by
  have bound : |g-h| ≤ M := abs_le.mpr ⟨by linarith, by linarith⟩
  have powers : |g-h|^p ≤ M^p := pow_le_pow_left₀ (abs_nonneg _) bound p
  simpa only [pow_succ] using mul_le_mul_of_nonneg_right powers (abs_nonneg (g-h))

#print axioms contact_atom_reference_bound
#print axioms original_packet_bound
#print axioms reciprocal_root_weight_lower
#print axioms bounded_density_power

end CollatzShell.LayeredContact
