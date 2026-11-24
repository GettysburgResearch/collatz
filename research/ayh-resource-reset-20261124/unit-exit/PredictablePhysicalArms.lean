import Mathlib

/-! Exact ordinary arithmetic for one-bit-lag physical transport,
ternary truncation, and the signed current of an unshifted column.
No probability or color selection estimate is formalized here. -/

namespace Collatz.PredictablePhysicalArms

def step (x : ℕ) : ℕ := if x % 2 = 0 then x / 2 else (3 * x + 1) / 2

theorem affine_step (a x : ℕ) :
    step (2*a+x) = 3^(x%2)*a + step x := by
  by_cases he : x % 2 = 0
  · have hp : (2*a+x) % 2 = 0 := by omega
    simp [step, he, hp]
    omega
  · have ho : x % 2 = 1 := by omega
    simp [step, ho]
    omega

/-- The next coarse bit determines the parity and both successor
coefficients before any still higher bit of q is read. -/
theorem next_parameter (g q bit c : ℕ) :
    step (3^g*(2*q+bit)+c) =
      3^(g+((3^g*bit+c)%2))*q + step (3^g*bit+c) := by
  have h : 3^g*(2*q+bit)+c = 2*(3^g*q)+(3^g*bit+c) := by ring
  rw [h, affine_step, pow_add]
  ring

/-- Every trit truncation whose exponent fits in the entering slope
retains the same unrevealed quotient and has a known intercept. -/
theorem truncate_parameter (g u q c : ℕ) :
    (3^(g+u)*q+c) / 3^u = 3^g*q + c / 3^u := by
  have h : 3^(g+u)*q+c = c + (3^g*q)*3^u := by rw [pow_add]; ring
  rw [h, Nat.add_mul_div_right _ _ (by positivity)]
  omega

def current (f : ℕ → ℤ) (x : ℕ) : ℤ :=
  if x % 2 = 0 then 0 else f (x - 1) - f x

theorem current_eq (f : ℕ → ℤ) (evenOrbit : ∀ n, f (2*n) = f n) (x : ℕ) :
    f (x/2) - f x = current f x := by
  by_cases he : x % 2 = 0
  · rw [current, ite_eq_left he]
    have hx : 2*(x/2) = x := by omega
    have h := evenOrbit (x/2)
    rw [hx] at h
    omega
  · rw [current, ite_eq_right he]
    have hx : 2*(x/2) = x-1 := by omega
    have h := evenOrbit (x/2)
    rw [hx] at h
    omega

/-- The change in the signed edge is the difference of its two
ordinary adjacent currents, exactly for both endpoints. -/
theorem signed_flux (f : ℕ → ℤ) (evenOrbit : ∀ n, f (2*n) = f n) (x y : ℕ) :
    (f (x/2) - f (y/2)) - (f x - f y) = current f x - current f y := by
  rw [← current_eq f evenOrbit x, ← current_eq f evenOrbit y]
  ring

/-- Exact survival region of an even-suffix head under one shortcut
step. In the lower odd-parent region the new parent is one smaller. -/
theorem even_suffix_parent (q r : ℕ) (hr : r < 81) (he : r % 2 = 0) :
    (if q % 2 = 1 ∧ r < 28 then (step (81*q+r))/81+1
     else (step (81*q+r))/81) = step q := by
  by_cases hq : q % 2 = 0
  · have hx : (81*q+r) % 2 = 0 := by omega
    have hno : ¬ (q % 2 = 1 ∧ r < 28) := by omega
    simp only [step, ite_eq_right hno, ite_eq_left hx, ite_eq_left hq]
    omega
  · have hqo : q % 2 = 1 := by omega
    have hx : (81*q+r) % 2 ≠ 0 := by omega
    simp [step, hqo, hx]
    split <;> omega

end Collatz.PredictablePhysicalArms

#print axioms Collatz.PredictablePhysicalArms.affine_step
#print axioms Collatz.PredictablePhysicalArms.next_parameter
#print axioms Collatz.PredictablePhysicalArms.truncate_parameter
#print axioms Collatz.PredictablePhysicalArms.current_eq
#print axioms Collatz.PredictablePhysicalArms.signed_flux
#print axioms Collatz.PredictablePhysicalArms.even_suffix_parent
