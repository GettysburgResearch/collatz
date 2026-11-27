import Mathlib.Algebra.Order.Monoid.Unbundled.Pow
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! Arithmetic interfaces for the first ordinary terminal at the critical gate. -/
set_option autoImplicit false
set_option warningAsError true

namespace EscapeCriticalFirstClear

/-- Immediately before first clearance the reduced denominator is 3.
Its odd departure yields an ordinary terminal unequal to 2 modulo 3. -/
theorem terminal_mod_three (y v : ℕ) (oddStep : 2*y=v+1) (full : v%3≠0) :
    y%3≠2 := by omega

/-- Conversely, when a last odd departure has the displayed affine
congruence, the reported terminal suffices to certify a reduced input. -/
theorem full_input_last_odd (a C y Q : ℕ) (eqn : a+C=2*Q*y)
    (sourceResidue : C%3=Q%3) (unit : Q%3≠0) (target : y%3≠2) :
    a%3≠0 := by
  have mod3 := congrArg (fun x : ℕ => x%3) eqn
  rw [Nat.add_mod, Nat.mul_mod, Nat.mul_mod 2 Q, sourceResidue] at mod3
  have qcases : Q%3=1 ∨ Q%3=2 := by omega
  have ycases : y%3=0 ∨ y%3=1 := by omega
  rcases qcases with h|h <;> rcases ycases with k|k <;>
    simp [h,k] at mod3 <;> omega

/-- The fixed earlier real window and the bounded normalized intercept
keep the cleared numerator in the selected interval of width six. -/
theorem compact_window (s c q : ℚ) (ls : 29/8 ≤ s) (us : s < 29/4)
    (lc : 31/32 ≤ c) (uc : c ≤ 33/32) (lq : 1 ≤ q) (uq : q < 3) :
    1/2 ≤ s-q*c ∧ s-q*c < 13/2 := by
  have lo : 31/32 ≤ q*c := by
    calc
      31/32 ≤ c := lc
      _ ≤ q*c := by nlinarith [mul_nonneg (sub_nonneg.mpr lq) (show 0≤c by linarith)]
  have hi : q*c ≤ 99/32 := by
    nlinarith [mul_nonneg (sub_nonneg.mpr uc) (show 0≤q by linarith),
      mul_nonneg (show 0≤3-q by linarith) (show (0:ℚ)≤33/32 by norm_num)]
  constructor <;> linarith

/-- After the K-th odd departure at t=n-h, the h prescribed ticks
to the census always fit within the credited critical budget. -/
theorem automatic_to_census (n t h j K : ℕ) (clock : n=t+h)
    (wait : j≤h) (bank : 2^n≤3^K) : 2^(t+j)≤3^K := by
  exact (Nat.pow_le_pow_right (n:=2) (by decide) (show t+j≤n by omega)).trans bank

#print axioms terminal_mod_three
#print axioms full_input_last_odd
#print axioms compact_window
#print axioms automatic_to_census
end EscapeCriticalFirstClear
