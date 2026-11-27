import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-! Algebraic local-unit relations and two actual scaled path swaps. -/

namespace Collatz.LocalUnitRelations

set_option autoImplicit false

section Algebra

variable {K : Type*} [Field K]

/-- Trace identities behind the exact dyadic and ternary logarithm valuations.
Cubing moves beyond the ternary boundary of the logarithm's first-term argument. -/
theorem local_trace_identities {e x : K} (he : e ≠ 0) (ht : e+e⁻¹ = 12*x+2) :
    (e+1)^2 = 4*(3*x+1)*e ∧ (e-1)^2 = 12*x*e ∧
      e^3-1 = 3*(e-1)*e*(4*x+1) := by
  field_simp [he] at ht
  refine ⟨?_, ?_, ?_⟩
  · linear_combination ht
  · linear_combination ht
  · linear_combination (e-1)*ht

/-- Distinct endpoint involutions are unnecessary for the two formal norm identities. -/
theorem asymmetric_norms {q y t v : K} (hs : t+v = 1-y) (hp : t*v = q*y) :
    (1-t)*(1-v) = (1+q)*y ∧ (1+t)*(1+v) = 2+(q-1)*y := by
  constructor
  · linear_combination -hs + hp
  · linear_combination hs + hp

/-- The trace of the ratio of the two complementary branch factors. -/
theorem third_field_trace {q y t v : K}
    (ht : 1-t ≠ 0) (hv : 1-v ≠ 0) (hs : t+v = 1-y) (hp : t*v = q*y) :
    (1-v)/(1-t) + (1-t)/(1-v) = (1+y)^2/((1+q)*y)-2 := by
  have hn := (asymmetric_norms hs hp).1
  rw [← hn]
  field_simp [ht, hv]
  linear_combination (t+v-y-3)*hs

/-- The hyperbolic Cayley coordinate of a combined interval is the ratio of its two
positive radicals, so successive interval coordinates multiply. -/
theorem interval_cayley {s t : K} (hs : s ≠ 0)
    (hm : t-s ≠ 0) (htwo : (2 : K) ≠ 0) :
    let b := (t+s)/(t-s)
    (b+1)/(b-1) = t/s := by
  dsimp
  have h : (t+s)/(t-s)-1 ≠ 0 := by
    intro he
    have hz : (t+s)/(t-s) = 1 := sub_eq_zero.mp he
    have heq := (div_eq_one_iff_eq hm).mp hz
    have : 2*s = 0 := by linear_combination heq
    exact (mul_ne_zero htwo hs) this
  apply (div_eq_div_iff h hs).mpr
  field_simp [hm]
  ring

end Algebra

/-- Positive odd source and successor with the displayed exact physical acceleration clock. -/
def Edge (x a y : ℕ) : Prop := 0 < x ∧ x % 2 = 1 ∧ y % 2 = 1 ∧ 2^a*y = 3*x+1

instance (x a y : ℕ) : Decidable (Edge x a y) := inferInstanceAs (Decidable (_ ∧ _ ∧ _ ∧ _))

/-- Five physical edges balance multiplicatively in each of two opposite scaled swaps. -/
theorem physical_swaps :
    (Edge 25 2 19 ∧ Edge 19 1 29 ∧ Edge 29 3 11 ∧ Edge 55 1 83 ∧ Edge 83 1 125 ∧
      25*55 = 11*125) ∧
    (Edge 7 1 11 ∧ Edge 143 1 215 ∧ Edge 215 1 323 ∧ Edge 323 1 485 ∧
      Edge 485 4 91 ∧ 7*143 = 11*91) := by decide

/-- The inequalities on the correction are the two swap inequalities implied by
convexity or concavity, respectively, after passing to the logarithmic input coordinate. -/
theorem no_corrected_prime_descent (f g : ℕ → ℚ)
    (additive : ∀ m n : ℕ, f (m*n) = f m+f n)
    (shape : g 25+g 55 ≤ g 11+g 125 ∨ g 7+g 143 ≤ g 11+g 91) :
    ¬ ∀ x a y, x ≠ 1 → Edge x a y → f y + g y < f x + g x := by
  intro hd
  obtain ⟨⟨e1,e2,e3,e4,e5,h1⟩,⟨e6,e7,e8,e9,e10,h2⟩⟩ := physical_swaps
  have b1 : f 25+f 55 = f 11+f 125 := by
    rw [← additive, ← additive, h1]
  have b2 : f 7+f 143 = f 11+f 91 := by
    rw [← additive, ← additive, h2]
  rcases shape with hg | hg
  · linarith only [b1, hg, hd 25 2 19 (by decide) e1, hd 19 1 29 (by decide) e2,
      hd 29 3 11 (by decide) e3, hd 55 1 83 (by decide) e4, hd 83 1 125 (by decide) e5]
  · linarith only [b2, hg, hd 7 1 11 (by decide) e6, hd 143 1 215 (by decide) e7,
      hd 215 1 323 (by decide) e8, hd 323 1 485 (by decide) e9, hd 485 4 91 (by decide) e10]

#print axioms local_trace_identities
#print axioms asymmetric_norms
#print axioms third_field_trace
#print axioms interval_cayley
#print axioms physical_swaps
#print axioms no_corrected_prime_descent

end Collatz.LocalUnitRelations
