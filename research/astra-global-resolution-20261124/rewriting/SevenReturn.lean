import Std

namespace SevenReturn

def T (n : Nat) : Nat := if n % 2 = 0 then n / 2 else (3*n+1)/2

def run (n : Nat) : Nat → Nat
  | 0 => n
  | k+1 => T (run n k)

private theorem invRun (P : Nat → Prop) (h : ∀ n, P n ↔ P (T n))
    (n k : Nat) : P n ↔ P (run n k) := by
  induction k with
  | zero => rfl
  | succ k ih => exact ih.trans (h _)

theorem half (u : Nat) : run (2*u+0) 1 = 1*u+0 := by
  have s0 : T (2*u+0) = 1*u+0 := by unfold T; split <;> omega
  simp only [run, s0]

theorem fourOne (u : Nat) : run (4*u+1) 2 = 3*u+1 := by
  have s0 : T (4*u+1) = 6*u+2 := by unfold T; split <;> omega
  have s1 : T (6*u+2) = 3*u+1 := by unfold T; split <;> omega
  simp only [run, s0, s1]

theorem sixteenThree (u : Nat) : run (16*u+3) 4 = 9*u+2 := by
  have s0 : T (16*u+3) = 24*u+5 := by unfold T; split <;> omega
  have s1 : T (24*u+5) = 36*u+8 := by unfold T; split <;> omega
  have s2 : T (36*u+8) = 18*u+4 := by unfold T; split <;> omega
  have s3 : T (18*u+4) = 9*u+2 := by unfold T; split <;> omega
  simp only [run, s0, s1, s2, s3]

theorem thirtyTwoEleven (u : Nat) : run (32*u+11) 5 = 27*u+10 := by
  have s0 : T (32*u+11) = 48*u+17 := by unfold T; split <;> omega
  have s1 : T (48*u+17) = 72*u+26 := by unfold T; split <;> omega
  have s2 : T (72*u+26) = 36*u+13 := by unfold T; split <;> omega
  have s3 : T (36*u+13) = 54*u+20 := by unfold T; split <;> omega
  have s4 : T (54*u+20) = 27*u+10 := by unfold T; split <;> omega
  simp only [run, s0, s1, s2, s3, s4]

theorem reverseOdd (u : Nat) : run (6*u+5) 1 = 9*u+8 := by
  have s0 : T (6*u+5) = 9*u+8 := by unfold T; split <;> omega
  simp only [run, s0]

theorem firstReturnA (u : Nat) : run (7*(8*u+7)) 3 = 7*(9*u+8) := by
  have s0 : T (56*u+49) = 84*u+74 := by unfold T; split <;> omega
  have s1 : T (84*u+74) = 42*u+37 := by unfold T; split <;> omega
  have s2 : T (42*u+37) = 63*u+56 := by unfold T; split <;> omega
  have src : 7*(8*u+7) = 56*u+49 := by omega
  simp only [src, run, s0, s1, s2]
  omega

theorem firstReturnB (u : Nat) : run (7*(32*u+27)) 5 = 7*(27*u+23) := by
  have s0 : T (224*u+189) = 336*u+284 := by unfold T; split <;> omega
  have s1 : T (336*u+284) = 168*u+142 := by unfold T; split <;> omega
  have s2 : T (168*u+142) = 84*u+71 := by unfold T; split <;> omega
  have s3 : T (84*u+71) = 126*u+107 := by unfold T; split <;> omega
  have s4 : T (126*u+107) = 189*u+161 := by unfold T; split <;> omega
  have src : 7*(32*u+27) = 224*u+189 := by omega
  simp only [src, run, s0, s1, s2, s3, s4]
  omega

/-- The two directed transfers, together with ordinary step invariance, force
    every positive integer to have the label of 1. -/
theorem cover (P : Nat → Prop) (one : P 1) (inv : ∀ n, P n ↔ P (T n))
    (a : ∀ u, P (9*u+8) → P (8*u+7))
    (b : ∀ u, P (27*u+23) → P (32*u+27)) :
    ∀ n, n > 0 → P n := by
  intro n
  induction n using Nat.strongRecOn with
  | ind n ih =>
    intro pos
    by_cases h1 : n = 1
    · simpa [h1] using one
    by_cases he : n % 2 = 0
    · let u := n/2
      have eq : n = 2*u+0 := by dsimp [u]; omega
      rw [eq]
      apply (invRun P inv _ 1).mpr
      rw [half]
      apply ih <;> dsimp [u] <;> omega
    by_cases h4 : n % 4 = 1
    · let u := n/4
      have eq : n = 4*u+1 := by dsimp [u]; omega
      rw [eq]
      apply (invRun P inv _ 2).mpr
      rw [fourOne]
      apply ih <;> dsimp [u] <;> omega
    by_cases h8 : n % 8 = 7
    · let u := n/8
      have eq : n = 8*u+7 := by dsimp [u]; omega
      rw [eq]
      apply a
      rw [← reverseOdd u]
      apply (invRun P inv _ 1).mp
      apply ih <;> dsimp [u] <;> omega
    by_cases h16 : n % 16 = 3
    · let u := n/16
      have eq : n = 16*u+3 := by dsimp [u]; omega
      rw [eq]
      apply (invRun P inv _ 4).mpr
      rw [sixteenThree]
      apply ih <;> dsimp [u] <;> omega
    by_cases h32 : n % 32 = 11
    · let u := n/32
      have eq : n = 32*u+11 := by dsimp [u]; omega
      rw [eq]
      apply (invRun P inv _ 5).mpr
      rw [thirtyTwoEleven]
      apply ih <;> dsimp [u] <;> omega
    · let u := n/32
      have eq : n = 32*u+27 := by dsimp [u]; omega
      rw [eq]
      apply b
      apply ih <;> dsimp [u] <;> omega

end SevenReturn
