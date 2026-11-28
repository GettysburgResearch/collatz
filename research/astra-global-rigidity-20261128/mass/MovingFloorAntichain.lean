import Lean.Elab.Tactic.Omega

/-! First-entrance antichains for any deterministic map, including the
accelerated odd Collatz map. The exclusion of the full forward image of the
floor is essential when the floor contains several vertices. -/

set_option autoImplicit false
set_option warningAsError true

namespace Collatz.MovingFloor

variable {α : Type}

def run (f : α → α) (x : α) : Nat → α
  | 0 => x
  | k+1 => f (run f x k)

theorem run_add (f : α → α) (x : α) (k j : Nat) :
    run f x (k+j) = run f (run f x k) j := by
  induction j with
  | zero => rfl
  | succ j ih => exact congrArg f ih

def firstAt (f : α → α) (floor : α → Prop) (x : α) (j : Nat) : Prop :=
  floor (run f x j) ∧ ∀ i < j, ¬floor (run f x i)

def outsideFuture (f : α → α) (floor : α → Prop) (x : α) : Prop :=
  ∀ y, floor y → ∀ k, run f y k ≠ x

def visits (f : α → α) (x y : α) : Prop := ∃ k, run f x k = y

theorem comparable_same_grade {f : α → α} {floor : α → Prop} {x y : α} {j : Nat}
    (hx : firstAt f floor x j) (hy : firstAt f floor y j)
    (avoid : outsideFuture f floor y) (relation : visits f x y) : x = y := by
  obtain ⟨k, hk⟩ := relation
  cases k with
  | zero => exact hk
  | succ k =>
    exfalso
    by_cases before : k+1 < j
    · have hit : floor (run f y (j-(k+1))) := by
        rw [← hk, ← run_add, show (k+1)+(j-(k+1)) = j by omega]
        exact hx.1
      exact hy.2 (j-(k+1)) (by omega) hit
    · apply avoid (run f x j) hx.1 (k+1-j)
      rw [← run_add, show j+(k+1-j) = k+1 by omega]
      exact hk

theorem common_predecessor_same_grade {f : α → α} {floor : α → Prop}
    {x y z : α} {j : Nat} (hx : firstAt f floor x j) (hy : firstAt f floor y j)
    (awayX : outsideFuture f floor x) (awayY : outsideFuture f floor y)
    (vx : visits f z x) (vy : visits f z y) : x = y := by
  obtain ⟨i, hi⟩ := vx
  obtain ⟨k, hk⟩ := vy
  by_cases order : i ≤ k
  · apply comparable_same_grade hx hy awayY
    refine ⟨k-i, ?_⟩
    rw [← hi, ← run_add, show i+(k-i) = k by omega, hk]
  · symm
    apply comparable_same_grade hy hx awayX
    refine ⟨i-k, ?_⟩
    rw [← hk, ← run_add, show k+(i-k) = i by omega, hi]

end Collatz.MovingFloor
