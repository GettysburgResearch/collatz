import Mathlib

/-!
Finite candidate core for the critical inverse strip and the barrier-head count.
This file has NOT been compiled in this checkpoint. No sorry/axiom declarations
are used. It does not formalize the external analytic density or phase-gap inputs.
-/

namespace OptimalCriticalAncestors

theorem inverse_pair (n m u a : ℤ)
    (h : 3*n+1 = a*u) (h' : 3*m+1 = 4*a*u) :
    m = 4*n+1 := by
  linarith

theorem unit_alternative (z : ℕ) :
    z % 3 ≠ 0 ∨ (4*z+1) % 3 ≠ 0 := by
  omega

theorem octave_shift (n d : ℕ)
    (hl : 2^d ≤ n) (hu : n < 2^(d+1)) :
    2^(d+2) ≤ 4*n+1 ∧ 4*n+1 < 2^(d+3) := by
  have h1 : (2:ℕ)^(d+1) = 2 * 2^d := by
    norm_num [pow_add] <;> omega
  have h2 : (2:ℕ)^(d+2) = 4 * 2^d := by
    norm_num [pow_add] <;> omega
  have h3 : (2:ℕ)^(d+3) = 8 * 2^d := by
    norm_num [pow_add] <;> omega
  rw [h1] at hu
  rw [h2, h3]
  omega

def surplus (k e d : ℤ) : ℤ := k*e-(d+1)

theorem surplus_step (k e d : ℤ) :
    surplus k (e+2) (d+2) = surplus k e d + 2*(k-1) := by
  unfold surplus
  ring

theorem strip_unique (k e d j : ℤ) (hk : 2 ≤ k) (hj : 1 ≤ j)
    (h : 0 ≤ surplus k e d ∧ surplus k e d < 2*(k-1))
    (h' : 0 ≤ surplus k (e+2*j) (d+2*j) ∧
       surplus k (e+2*j) (d+2*j) < 2*(k-1)) : False := by
  have hp : 0 ≤ 2*(k-1)*(j-1) := by positivity
  unfold surplus at h h'
  nlinarith [h.1, h'.2]

theorem small_unit_inverse (y : ℕ) (hy : 0 < y)
    (hu : y % 3 ≠ 0) :
    ∃ e z : ℕ, 1 ≤ e ∧ e ≤ 4 ∧ 0 < z ∧ z % 2 = 1 ∧
      z % 3 ≠ 0 ∧ 3*z+1 = 2^e*y := by
  by_cases h : y % 3 = 1
  · let z := (4*y-1)/3
    have hz : 3*z+1 = 4*y := by dsimp [z]; omega
    have hp : 0 < z := by omega
    have ho : z % 2 = 1 := by omega
    by_cases hunit : z % 3 ≠ 0
    · exact ⟨2,z,by decide,by decide,hp,ho,hunit,by norm_num; omega⟩
    · refine ⟨4,4*z+1,by decide,by decide,by omega,by omega,?_,?_⟩
      · omega
      · norm_num <;> omega
  · have h2 : y % 3 = 2 := by omega
    let z := (2*y-1)/3
    have hz : 3*z+1 = 2*y := by dsimp [z]; omega
    have hp : 0 < z := by omega
    have ho : z % 2 = 1 := by omega
    by_cases hunit : z % 3 ≠ 0
    · exact ⟨1,z,by decide,by decide,hp,ho,hunit,by norm_num; omega⟩
    · refine ⟨3,4*z+1,by decide,by decide,by omega,by omega,?_,?_⟩
      · omega
      · norm_num <;> omega

theorem inverse_height (y z : ℕ) (h : 3*z+1 = 2*y ∨
    3*z+1 = 4*y ∨ 3*z+1 = 8*y ∨ 3*z+1 = 16*y)
    (hy : 0 < y) : y ≤ 3*z ∧ 3*z ≤ 16*y := by
  rcases h with h | h | h | h <;> omega

theorem truncation_identity (n : ℕ) :
    (n / 81) / 81 = n / 6561 := by
  omega

#print axioms inverse_pair
#print axioms unit_alternative
#print axioms octave_shift
#print axioms surplus_step
#print axioms strip_unique
#print axioms small_unit_inverse
#print axioms inverse_height
#print axioms truncation_identity

end OptimalCriticalAncestors
