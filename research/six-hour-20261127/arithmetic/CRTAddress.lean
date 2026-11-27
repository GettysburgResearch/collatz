import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Additive CRT characters, finite word rounding and the centered convolution
estimate used in the bounded-period exclusion. -/
set_option autoImplicit false
set_option warningAsError true
open scoped BigOperators

namespace SixHour.CRTAddress

/-- The additive address of two physical residues on a single CRT circle. -/
theorem address {P Q u v a b y : ℤ} (bez : Q*u+P*v=1)
    (pa : P ∣ a-y) (qb : Q ∣ b-y) :
    P*Q ∣ a*Q*u+b*P*v-y := by
  obtain ⟨i, hi⟩ := pa
  obtain ⟨j, hj⟩ := qb
  refine ⟨i*u+j*v, ?_⟩
  calc
    a*Q*u+b*P*v-y = (a-y)*Q*u+(b-y)*P*v+y*(Q*u+P*v-1) := by ring
    _ = P*Q*(i*u+j*v) := by rw [hi,hj,bez]; ring

/-- Downward binning of each letter costs no more than one bin per letter. -/
theorem word_rounding {n : ℕ} (x z : Fin n → ℚ)
    (lo : ∀ i, z i ≤ x i) (hi : ∀ i, x i ≤ z i+1) :
    0 ≤ (∑ i, x i)-(∑ i, z i) ∧
      (∑ i, x i)-(∑ i, z i) ≤ (n : ℚ) := by
  have a := Finset.sum_le_sum (s := (Finset.univ : Finset (Fin n))) (fun i _ => lo i)
  have b := Finset.sum_le_sum (s := (Finset.univ : Finset (Fin n))) (fun i _ => hi i)
  simp only [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ,
    Fintype.card_fin, nsmul_eq_mul, mul_one] at b
  constructor <;> linarith

private theorem covariance {m : ℕ} (x y : Fin m → ℤ) :
    ∑ i, (((m : ℤ)*x i-(∑ j, x j))*((m : ℤ)*y i-(∑ j, y j)))
      = (m : ℤ)*((m : ℤ)*(∑ i, x i*y i)-(∑ i, x i)*(∑ i, y i)) := by
  have expand (i : Fin m) :
      ((m : ℤ)*x i-(∑ j, x j))*((m : ℤ)*y i-(∑ j, y j)) =
      (m : ℤ)^2*(x i*y i) - (m : ℤ)*(∑ j, y j)*x i
        - (m : ℤ)*(∑ j, x j)*y i + (∑ j, x j)*(∑ j, y j) := by ring
  simp_rw [expand]
  rw [Finset.sum_add_distrib, Finset.sum_sub_distrib, Finset.sum_sub_distrib,
    ← Finset.mul_sum, ← Finset.mul_sum, ← Finset.mul_sum]
  simp only [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_eq_mul]
  ring

/-- Apply this to a histogram and the reversed translate of the other.
The integer peak estimate then follows by taking the floor of a square root. -/
theorem centered_peak {m : ℕ} (hm : 0 < m) (x y : Fin m → ℤ) :
    ((m : ℤ)*(∑ i, x i*y i)-(∑ i, x i)*(∑ i, y i))^2 ≤
      ((m : ℤ)*(∑ i, x i^2)-(∑ i, x i)^2) *
      ((m : ℤ)*(∑ i, y i^2)-(∑ i, y i)^2) := by
  let X (i : Fin m) := (m : ℤ)*x i-(∑ j, x j)
  let Y (i : Fin m) := (m : ℤ)*y i-(∑ j, y j)
  have cs := Finset.sum_mul_sq_le_sq_mul_sq (Finset.univ : Finset (Fin m)) X Y
  simp only [pow_two, X, Y] at cs
  rw [covariance, covariance, covariance] at cs
  have pos : 0 < (m : ℤ)^2 := by positivity
  apply le_of_mul_le_mul_left (a := (m : ℤ)^2)
  · convert cs using 1 <;> ring_nf
  · exact pos

#print axioms address
#print axioms word_rounding
#print axioms centered_peak

end SixHour.CRTAddress
