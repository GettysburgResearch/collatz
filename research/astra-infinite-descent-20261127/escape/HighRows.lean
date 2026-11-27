import FairGrid
import Mathlib.Tactic.FieldSimp

/-! Finite effective low-vertex tests for genuine ordinary rows. -/
set_option autoImplicit false
set_option warningAsError true

namespace HighRows
open CoreBranching PeakRigidity AsynchronousGuard FairGrid

/-- Additive affine numerator controlled by the grade and the smallest odd
departure on this very path. Repetitions are allowed in this finite statement. -/
theorem offset_of_high_odds (m z H : ℕ)
    (high : ∀ j<m, run j z%2=1 → H≤run j z) :
    3*H*offset m z ≤ grade m z*(2^m*run m z) := by
  induction m with
  | zero => simp [offset,grade]
  | succ m ih =>
    have before := ih (fun j hj => high j (by omega))
    have form : 2^(m+1)*run (m+1) z=
        3^(run m z%2)*(2^m*run m z)+(run m z%2)*2^m := by
      calc
        _ = 3^(grade (m+1) z)*z+offset (m+1) z := affine (m+1) z
        _ = _ := by rw [grade,offset,pow_add,affine m z]; ring
    rw [offset,grade,form]
    rcases Nat.mod_two_eq_zero_or_one (run m z) with even|odd
    · simpa [even] using before
    · have small := high m (by omega) odd
      have term := Nat.mul_le_mul_left (3*2^m) small
      have triple := Nat.mul_le_mul_left 3 before
      simp only [odd,pow_one,one_mul]
      calc
        _ = 3*(3*H*offset m z)+3*2^m*H := by ring
        _ ≤ 3*(grade m z*(2^m*run m z))+3*2^m*run m z := Nat.add_le_add triple term
        _ = (grade m z+1)*(3*(2^m*run m z)) := by ring
        _ ≤ (grade m z+1)*(3*(2^m*run m z)+2^m) :=
          Nat.mul_le_mul_left _ (Nat.le_add_right _ _)

/-- The normalized mark of an actual high odd-departure path lies in a narrow
interval just below one. -/
theorem mark_of_high_odds {m d y z H : ℕ} (yp : 0<y) (Hp : 0<H)
    (hit : run m z=y) (gr : grade m z=d)
    (high : ∀ j<m, run j z%2=1 → H≤run j z) :
    1-(d:ℝ)/(3*H) ≤ weight m d y*z := by
  have defect := offset_of_high_odds m z H high
  rw [hit,gr] at defect
  have eqn := affine m z
  rw [hit,gr] at eqn
  have dreal : (3:ℝ)*H*offset m z ≤ (d:ℝ)*((2:ℝ)^m*y) := by exact_mod_cast defect
  have ereal : (2:ℝ)^m*y = (3:ℝ)^d*z+offset m z := by exact_mod_cast eqn
  have hpos : (0:ℝ)<3*H := by positivity
  have ypos : (0:ℝ)<2^m*y := by positivity
  rw [weight,div_mul_eq_mul_div]
  apply (le_div_iff₀ ypos).mpr
  apply (mul_le_mul_iff_right₀ hpos).mp
  field_simp
  nlinarith [congrArg (fun t:ℝ => (3:ℝ)*H*t) ereal]

/-- Exact finite low-vertex cutoff, uniform in the positive target and clock.
All source marks above H are in the same grid interval, so a row exceeding
(d/3+1)/H must use a small source or have an odd departure below H. -/
theorem high_row {m d y H : ℕ} (yp : 0<y) (Hp : 0<H) (A : Finset ℕ)
    (actual : ∀ z∈A, run m z=y ∧ grade m z=d ∧ H≤z)
    (high : ∀ z∈A, ∀ j<m, run j z%2=1 → H≤run j z) :
    weight m d y*A.card ≤ (d:ℝ)/(3*H)+1/H := by
  have wp : 0≤weight m d y := by unfold weight; positivity
  have dl : (0:ℝ)≤d/(3*H) := by positivity
  have cover := interval_count A wp (show 1-(d:ℝ)/(3*H)≤1 by linarith) (fun z hz => by
    obtain ⟨hit,gr,_⟩ := actual z hz
    exact ⟨mark_of_high_odds yp Hp hit gr (high z hz),mark_le_one yp hit gr⟩)
  by_cases ne : A.Nonempty
  · obtain ⟨z,hz⟩ := ne
    obtain ⟨hit,gr,large⟩ := actual z hz
    have lower : (H:ℝ)≤z := by exact_mod_cast large
    have scale : weight m d y≤1/H := (le_div_iff₀ (by positivity)).mpr
      ((mul_le_mul_of_nonneg_left lower wp).trans (mark_le_one yp hit gr))
    linarith
  · have empty : A=∅ := Finset.not_nonempty_iff_eq_empty.mp ne
    simp only [empty,Finset.card_empty,Nat.cast_zero,mul_zero]
    positivity

#print axioms offset_of_high_odds
#print axioms mark_of_high_odds
#print axioms high_row
end HighRows

