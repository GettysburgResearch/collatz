import Std

set_option autoImplicit false

namespace ComponentGram

def disagreement {α : Type} [DecidableEq α] (x y : α) : Nat :=
  if x = y then 0 else 1

private theorem triangle {α : Type} [DecidableEq α] (x y z : α) :
    disagreement x z ≤ disagreement x y + disagreement y z := by
  by_cases h : x = y
  · subst y
    simp [disagreement]
  · by_cases h' : y = z
    · subst z
      simp [disagreement]
    · simp [disagreement, h, h']
      split <;> omega

/-- Disagreement count for any common finite family of ordinary-source
indexings, with values given by arbitrary component labels. -/
def dist {α : Type} [DecidableEq α] (label : Nat → Nat → α) (i j : Nat) : Nat → Nat
  | 0 => 0
  | n+1 => dist label i j n + disagreement (label n i) (label n j)

private theorem distTriangle {α : Type} [DecidableEq α] (label : Nat → Nat → α)
    (i k j r : Nat) : dist label i j r ≤ dist label i k r + dist label k j r := by
  induction r with
  | zero => simp [dist]
  | succ r ih =>
    have t := triangle (label r i) (label r k) (label r j)
    simp only [dist]
    omega

/-- An exact anchor at 1,2 and near-constant adjacent averages bound the
root separation at the fixed positive input k+2 by k times that error. -/
theorem anchored {α : Type} [DecidableEq α] (label : Nat → Nat → α)
    (r E k : Nat) (anchor : dist label 1 2 r = 0)
    (adjacent : ∀ i, 2 ≤ i → i < k+2 → dist label i (i+1) r ≤ E) :
    dist label 1 (k+2) r ≤ k*E := by
  induction k with
  | zero => simpa using Nat.le_of_eq anchor
  | succ k ih =>
    have prev := ih (fun i h₂ hi => adjacent i h₂ (by omega))
    have last := adjacent (k+2) (by omega) (by omega)
    have t := distTriangle label 1 (k+2) (k+2+1) r
    rw [Nat.succ_mul, show k.succ+2 = k+2+1 by omega]
    omega

#print axioms anchored

end ComponentGram
