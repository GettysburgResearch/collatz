import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum

set_option autoImplicit false
set_option maxRecDepth 10000
set_option maxHeartbeats 8000000

namespace TwoBlockSwap

/-- The four physical block relations at an identical terminal give a signed
    integral source difference. Substitute a=2^t, p=2^b, h=3^t, and likewise
    d=2^u, q=2^c, j=3^u. -/
theorem source_difference (a p h d q j x y z x' y' : ℤ)
    (A : a*p*y=h*x+a*(p-1)) (B : d*q*z=j*y+d*(q-1))
    (C : d*q*y'=j*x'+d*(q-1)) (D : a*p*z=h*y'+a*(p-1)) :
    h*j*(x'-x) = (p-1)*a*j-(q-1)*d*h+(q-p)*a*d := by
  nlinarith only [congrArg (fun k : ℤ => j*k) A, congrArg (fun k : ℤ => a*p*k) B,
    congrArg (fun k : ℤ => h*k) C, congrArg (fun k : ℤ => d*q*k) D]

/-- A finite parameter test, independently of any sampled numerical sources. -/
def passes (t b u c : ℕ) : Bool := decide (
  (t ≠ u ∨ b ≠ c) ∧ b+c ≤ 12 ∧ 2^(t+u+b+c) ≤ 12*3^(t+u) ∧
  ((2^b-1)*2^t*3^u + 2^c*2^(t+u)) % 3^(t+u) =
    ((2^c-1)*2^u*3^t + 2^b*2^(t+u)) % 3^(t+u))

/-- min(t,u) ≤ 2, max(t,u) ≤ 10, all exponents positive, oriented using
    symmetry. The integer clock and the congruence never both hold. -/
theorem bounded_swap_exclusion :
    ∀ t : Fin 2, ∀ u : Fin 10, ∀ b : Fin 12, ∀ c : Fin 12,
      passes (t.val+1) (b.val+1) (u.val+1) (c.val+1) = false := by
  decide

#print axioms source_difference
#print axioms bounded_swap_exclusion
end TwoBlockSwap
