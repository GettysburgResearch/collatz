import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-! The split sorted-CRT interval and failure-of-trapping implications. -/
set_option autoImplicit false
set_option warningAsError true

namespace SixHour.MinimumCensus

/-- In one CRT period, the ordered residue search has just two runs. -/
theorem only_two_runs {P a b t j : ℤ} (hP : 0 < P)
    (ha : 0 ≤ a ∧ a < P) (hb : 0 ≤ b ∧ b < P) (ht : 0 ≤ t ∧ t < P)
    (eqn : b+t = a+j*P) : (j=0 ∧ t=a-b) ∨ (j=1 ∧ t=a+P-b) := by
  have lo : 0 ≤ j := by
    by_contra! neg
    have hj : j ≤ -1 := by omega
    have mul := mul_le_mul_of_nonneg_right hj hP.le
    nlinarith
  have hi : j ≤ 1 := by
    by_contra! pos
    have hj : 2 ≤ j := by omega
    have mul := mul_le_mul_of_nonneg_right hj hP.le
    nlinarith
  rcases (show j=0 ∨ j=1 by omega) with h | h
  · left
    subst j
    simp at eqn
    exact ⟨rfl, by omega⟩
  · right
    subst j
    simp at eqn
    exact ⟨rfl, by omega⟩

/-- Native odd transition restricted to the first two valuation grades. -/
def next (x : ℕ) : Option ℕ :=
  if (3*x+1)%4=2 then some ((3*x+1)/2)
  else if (3*x+1)%8=4 then some ((3*x+1)/4)
  else none

def stays (low high : ℕ) : ℕ → ℕ → Prop
  | 0, x => low ≤ x ∧ x ≤ high
  | n+1, x => low ≤ x ∧ x ≤ high ∧ ∃ y, next x = some y ∧ stays low high n y

/-- A true bounded native orbit must pass every finite physical exit test. -/
theorem orbit_stays (x : ℕ → ℕ) {low high : ℕ}
    (bounds : ∀ i, low ≤ x i ∧ x i ≤ high)
    (edges : ∀ i, next (x i) = some (x (i+1))) (n i : ℕ) :
    stays low high n (x i) := by
  induction n generalizing i with
  | zero => exact bounds i
  | succ n ih =>
    exact ⟨(bounds i).1, (bounds i).2, x (i+1), edges i, ih (i+1)⟩

#print axioms only_two_runs
#print axioms orbit_stays

end SixHour.MinimumCensus
