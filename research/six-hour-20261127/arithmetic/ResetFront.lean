import PeakRigidity

/-! Finite native prefixes in the zero- and one-symbol expansions.  The
infinite Subspace Theorem application is given in RESET_FRONT.md. -/
set_option autoImplicit false
set_option warningAsError true
namespace SixHour.ResetFront

open CoreBranching
open PeakRigidity (grade)

/-- The integer obtained by clearing the power of three in the prefix sum.
With `shift = true` only even departures supply new terms. With `false`
only odd departures do. -/
def carry (shift : Bool) : ℕ → ℕ → ℕ
  | 0, _ => 0
  | j + 1, x =>
      if run j x % 2 = 0 then carry shift j x + (if shift then 2 ^ j else 0)
      else 3 * carry shift j x + (if shift then 0 else 2 ^ j)

/-- The same native clock and the same actual odd grade work for both anchors. -/
theorem prefix_identity (shift : Bool) (j x : ℕ) :
    3 ^ grade j x * (x + shift.toNat) + carry shift j x =
      2 ^ j * (run j x + shift.toNat) := by
  induction j with
  | zero => simp [grade, carry, run]
  | succ j ih =>
    have last : run (j+1) x = step (run j x) := by
      simpa [run] using run_add j 1 x
    by_cases h : run j x % 2 = 0
    · have e : 2 * step (run j x) = run j x := by simp [step,h]; omega
      simp only [carry, h, ↓reduceIte, grade, Nat.add_zero, last, pow_succ]
      cases shift <;> simp at ih ⊢
      all_goals nlinarith [congrArg (fun v : ℕ => 2 ^ j * v) e]
    · have h' : run j x % 2 = 1 := by omega
      have e : 2 * step (run j x) = 3 * run j x + 1 := by simp [step,h]; omega
      simp only [carry, grade, h', last, pow_succ]
      cases shift <;> simp at ih ⊢
      all_goals nlinarith [congrArg (fun v : ℕ => 2 ^ j * v) e]

/-- At an occurrence of the selected symbol the numerator has exactly the
stated dyadic order, independently of how long the earlier prefix is. -/
theorem exact_dyadic_order (shift : Bool) (j x : ℕ)
    (occurs : (run j x + shift.toNat) % 2 = 1) :
    let numerator := 3 ^ grade j x * (x + shift.toNat) + carry shift j x
    2 ^ j ∣ numerator ∧ ¬ 2 ^ (j+1) ∣ numerator := by
  dsimp only
  rw [prefix_identity, pow_succ, Nat.mul_dvd_mul_iff_left (by positivity : 0 < 2 ^ j)]
  exact ⟨dvd_mul_right _ _, by omega⟩

#print axioms prefix_identity
#print axioms exact_dyadic_order

end SixHour.ResetFront
