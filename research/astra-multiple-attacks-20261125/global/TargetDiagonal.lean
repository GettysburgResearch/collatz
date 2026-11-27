import Std

set_option autoImplicit false

namespace TargetDiagonal

def step (n : Nat) : Nat :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def walk (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => step (walk n k)

def Hits (n target : Nat) : Prop := ∃ k, walk n k = target

private theorem walk_add (n k j : Nat) : walk n (k+j) = walk (walk n k) j := by
  induction j with
  | zero => simp [walk]
  | succ j ih =>
    rw [show k+j.succ = (k+j)+1 by omega]
    exact congrArg step ih

private theorem hits_sequential {n a b : Nat} (ha : Hits n a) (hb : Hits n b) :
    Hits a b ∨ Hits b a := by
  obtain ⟨i,hi⟩ := ha
  obtain ⟨j,hj⟩ := hb
  by_cases h : i ≤ j
  · left
    refine ⟨j-i, ?_⟩
    rw [←hi, ←walk_add, show i+(j-i) = j by omega, hj]
  · right
    refine ⟨i-j, ?_⟩
    rw [←hj, ←walk_add, show j+(i-j) = i by omega, hi]

private theorem trapped {P : Nat → Prop} (closed : ∀ n, P n → P (step n))
    {n : Nat} (start : P n) (k : Nat) : P (walk n k) := by
  induction k with
  | zero => exact start
  | succ k ih => exact closed _ ih

abbrev fromFive (n : Nat) : Prop := n=5 ∨ n=8 ∨ n=4 ∨ n=2 ∨ n=1

abbrev fromEightyFive (n : Nat) : Prop :=
  n=85 ∨ n=128 ∨ n=64 ∨ n=32 ∨ n=16 ∨ n=8 ∨ n=4 ∨ n=2 ∨ n=1

/-- The two ordinary visit sets are disjoint even though their forward
paths eventually meet. -/
theorem incompatible (n : Nat) (h : Hits n 5) : ¬ Hits n 85 := by
  intro h'
  rcases hits_sequential h h' with ⟨k,hk⟩ | ⟨k,hk⟩
  · have closed : ∀ x, fromFive x → fromFive (step x) := by
      intro x hx
      rcases hx with rfl|rfl|rfl|rfl|rfl <;> decide
    have t := trapped closed (n := 5) (by decide) k
    rw [hk] at t
    exact (by decide : ¬ fromFive 85) t
  · have closed : ∀ x, fromEightyFive x → fromEightyFive (step x) := by
      intro x hx
      rcases hx with rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl|rfl <;> decide
    have t := trapped closed (n := 85) (by decide) k
    rw [hk] at t
    exact (by decide : ¬ fromEightyFive 5) t

/-- Every row is empty on the prescribed diagonal for targets 5,5,85. -/
theorem diagonal (n : Nat) (h : Hits n 5) : ¬ Hits (n+n) 85 := by
  obtain ⟨k,hk⟩ := h
  apply incompatible
  refine ⟨1+k, ?_⟩
  rw [walk_add]
  have first : walk (n+n) 1 = n := by
    have even : (n+n)%2=0 := by omega
    simp [walk, step, even]
    omega
  rw [first, hk]

#print axioms incompatible
#print axioms diagonal

end TargetDiagonal
