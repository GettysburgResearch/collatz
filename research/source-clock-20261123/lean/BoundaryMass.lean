import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Finset
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Group.Finset.Piecewise
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.Ring

/-!
Finite inequalities used in BOUNDARY_OVERLAP.md. The supplied quantities retain
their original weights; there is no uniform replacement of the inverse law.
These declarations do not assert existence, harmonicity, or selection for the
canonical infinite trace. Nor do they formalize the local-dimension theorem.
-/

namespace CollatzSourceClock.BoundaryMass

open scoped BigOperators

/-- A positive term in an iterated harmonic equation, together with a path
product lower bound, forces a floor for the numerical ancestor. This is the
cross-multiplied form of u >= (alpha * delta / B) * n. -/
theorem cone_floor_of_path_term
    (alpha delta n u omega fAncestor fRoot B : ℝ)
    (halpha : 0 ≤ alpha) (hu : 0 ≤ u) (homega : 0 ≤ omega)
    (hfloor : alpha ≤ fAncestor) (hterm : omega * fAncestor ≤ fRoot)
    (hprofile : fRoot ≤ B) (hproduct : delta * n ≤ omega * u) :
    alpha * delta * n ≤ B * u := by
  calc
    alpha * delta * n = alpha * (delta * n) := by ring
    _ ≤ alpha * (omega * u) := mul_le_mul_of_nonneg_left hproduct halpha
    _ = (omega * alpha) * u := by ring
    _ ≤ (omega * fAncestor) * u :=
      mul_le_mul_of_nonneg_right (mul_le_mul_of_nonneg_left hfloor homega) hu
    _ ≤ fRoot * u := mul_le_mul_of_nonneg_right hterm hu
    _ ≤ B * u := mul_le_mul_of_nonneg_right hprofile hu

/-- At each selected departure, a second possible edge of mass at least eta
caps the chosen edge by 1-eta. Multiply the actual chosen probabilities. -/
theorem selected_prefix_product
    {ι : Type*} (s : Finset ι) (low : ι → Prop) [DecidablePred low]
    (p : ι → ℝ) (eta : ℝ)
    (hp0 : ∀ i ∈ s, 0 ≤ p i) (hp1 : ∀ i ∈ s, p i ≤ 1)
    (hlow : ∀ i ∈ s, low i → p i ≤ 1 - eta) :
    (∏ i ∈ s, p i) ≤ (1 - eta) ^ (s.filter low).card := by
  calc
    (∏ i ∈ s, p i) ≤ ∏ i ∈ s, (if low i then 1 - eta else 1) := by
      apply Finset.prod_le_prod₀ hp0
      intro i hi
      split_ifs with h
      · exact hlow i hi h
      · exact hp1 i hi
    _ = (1 - eta) ^ (s.filter low).card := by
      rw [Finset.prod_ite, Finset.prod_const, Finset.prod_const_one, mul_one]

/-- The harmonic cylinder identity converts the retained prefix probability
bound into a bound for its actual affine multiplier. The endpoint trace floor
is essential; no law over endpoints is changed. -/
theorem cylinder_multiplier_bound
    {ι : Type*} (s : Finset ι) (low : ι → Prop) [DecidablePred low]
    (p : ι → ℝ) (eta a alpha fEnd fRoot : ℝ)
    (hp0 : ∀ i ∈ s, 0 ≤ p i) (hp1 : ∀ i ∈ s, p i ≤ 1)
    (hlow : ∀ i ∈ s, low i → p i ≤ 1 - eta)
    (ha : 0 ≤ a) (halpha : 0 < alpha) (hEnd : alpha ≤ fEnd)
    (hRoot : 0 ≤ fRoot) (htelescope : a * fEnd = fRoot * ∏ i ∈ s, p i) :
    a ≤ (fRoot / alpha) * (1 - eta) ^ (s.filter low).card := by
  have h : a * alpha ≤ fRoot * (1 - eta) ^ (s.filter low).card := by
    calc
      a * alpha ≤ a * fEnd := mul_le_mul_of_nonneg_left hEnd ha
      _ = fRoot * ∏ i ∈ s, p i := htelescope
      _ ≤ fRoot * (1 - eta) ^ (s.filter low).card :=
        mul_le_mul_of_nonneg_left
          (selected_prefix_product s low p eta hp0 hp1 hlow) hRoot
  calc
    a = (a * alpha) / alpha := (mul_div_cancel_right₀ a (ne_of_gt halpha)).symm
    _ ≤ (fRoot * (1 - eta) ^ (s.filter low).card) / alpha :=
      div_le_div_of_nonneg_right h (le_of_lt halpha)
    _ = (fRoot / alpha) * (1 - eta) ^ (s.filter low).card := by ring

/-- The finite heavy-cell comparison. A restriction of the actual law has
mass at most M in each cell. Every selected cell's enlarged reference mass is
at least h, and all enlarged reference masses sum to at most K. The reference
measure is independent of the sampled law. In the written application K=4,
M=(2*B/F(q))*t and h=t^s. -/
theorem heavy_cell_mass
    {ι : Type*} (s : Finset ι) (actual reference : ι → ℝ)
    (M h K : ℝ) (hM : 0 ≤ M) (hh : 0 < h)
    (hactual : ∀ i ∈ s, actual i ≤ M)
    (hheavy : ∀ i ∈ s, h ≤ reference i)
    (hbudget : ∑ i ∈ s, reference i ≤ K) :
    (∑ i ∈ s, actual i) ≤ M * K / h := by
  apply (le_div_iff₀ hh).2
  calc
    (∑ i ∈ s, actual i) * h = ∑ i ∈ s, actual i * h := Finset.sum_mul s actual h
    _ ≤ ∑ i ∈ s, M * reference i := by
      apply Finset.sum_le_sum
      intro i hi
      exact (mul_le_mul_of_nonneg_right (hactual i hi) (le_of_lt hh)).trans
        (mul_le_mul_of_nonneg_left (hheavy i hi) hM)
    _ = M * ∑ i ∈ s, reference i := (Finset.mul_sum s reference M).symm
    _ ≤ M * K := mul_le_mul_of_nonneg_left hbudget hM

end CollatzSourceClock.BoundaryMass
