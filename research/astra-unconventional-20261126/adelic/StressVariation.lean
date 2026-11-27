import Mathlib.Tactic.Positivity
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Mixed-argument first and second variations for the fully invariant regulator
combination, and the strict quantitative curvature margin. -/

namespace Collatz.StressVariation

set_option autoImplicit false

variable {K : Type*} [Field K]

/-- The first variation cancels for arbitrary values of the derivative on the
four baseline arguments. The denominators are those in the actual symbol. -/
theorem first_variation [CharZero K] (u₁ u₂ v₁ v₂ : K) :
    (32*(u₁-v₁))/32 - (40*(u₁-v₂))/40 -
      (24*(u₂-v₁))/24 + (32*(u₂-v₂))/32 = 0 := by ring

/-- The second variation for the odd Rogers second derivative. -/
theorem second_variation (f : K → K) (odd : ∀ t, f (-t) = -f t) (b : K) :
    32*(f (-24*b)+f (8*b)) - 40*(f (-24*b)+f (16*b)) -
      24*(f (-16*b)+f (8*b)) + 32*(f (-16*b)+f (16*b)) =
        8*(f (8*b)-2*f (16*b)+f (24*b)) := by
  rw [show -24*b = -(24*b) by ring, show -16*b = -(16*b) by ring, odd, odd]
  ring

/-- The exact nearest-clock ratio gives more than a factor four in signed
curvature before controlling the small argument perturbation. -/
theorem curvature_margin [LinearOrder K] [IsStrictOrderedRing K] (r A B C : K) (hr : 0 ≤ r) (hsmall : r ≤ (3/4 : K)^8)
    (hA : 0 < A) (hC : 0 ≤ C) (hB : B = A*(2*r)/(1+r)^2) :
    4*A < 8*(A-2*B+C) := by
  have hbound : r < 1/8 := by
    have h : (3/4 : K)^8 < 1/8 := by norm_num
    exact lt_of_le_of_lt hsmall h
  have hden : 0 < (1+r)^2 := by positivity
  have hfactor : 8*r < (1+r)^2 := by nlinarith [sq_nonneg r]
  have hBA : 4*B < A := by
    rw [hB, ← mul_div_assoc]
    apply (div_lt_iff₀ hden).mpr
    nlinarith [mul_lt_mul_of_pos_left hfactor hA]
  linarith

/-- The signed exponents in the uncorrected norm-one product annihilate every
affine positive-logarithm part, in either clock direction. -/
theorem affine_checkerboard (a b c u₁ u₂ v₁ v₂ : K) :
    (a*u₁+b*v₁+c)-(a*u₁+b*v₂+c)-(a*u₂+b*v₁+c)+(a*u₂+b*v₂+c) = 0 := by ring

#print axioms first_variation
#print axioms second_variation
#print axioms curvature_margin
#print axioms affine_checkerboard

end Collatz.StressVariation
