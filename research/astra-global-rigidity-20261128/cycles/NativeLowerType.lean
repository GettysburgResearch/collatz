import ShiftedRampCores

/-!
Finite arithmetic for actual inverse arrows, legal unit residue classes and
the full native suffix after an actual arrival at one. The asymptotic counting,
positive-operator estimates and Subspace Theorem arguments are not formalized.
-/
namespace Collatz.NativeLowerType

open Collatz.MersenneCrests (next run run_add)
open Collatz.ShiftedRampCores (halving_run)

def unitResidue (a e : Nat) : Bool :=
  let r := (2^e*a)%9
  r == 4 || r == 7

/-- Every unit has two intermediate unit-parent choices in each six-letter clock block. -/
theorem six_unit_choices (a : Fin 9) (ha : a.val % 3 ≠ 0) :
    ((List.range 6).filter (fun j => unitResidue a.val (j+1))).length = 2 := by
  exact (by decide : ∀ b : Fin 9, b.val % 3 ≠ 0 →
    ((List.range 6).filter (fun j => unitResidue b.val (j+1))).length = 2) a ha

theorem residue_period (a e : Nat) : unitResidue a (e+6) = unitResidue a e := by
  have h : 2^(e+6)*a = 64*(2^e*a) := by
    rw [Nat.pow_add]
    change 2^e*64*a = 64*(2^e*a)
    ac_rfl
  have hm : (64*(2^e*a))%9 = (2^e*a)%9 := by omega
  simp only [unitResidue, h, hm]

theorem residue_reduce (a e : Nat) : unitResidue (a%9) e = unitResidue a e := by
  have h : (2^e*(a%9))%9 = (2^e*a)%9 := by
    exact Nat.mul_mod_mod _ _ _
  simp only [unitResidue, h]

theorem arithmetic_unit_child (a : Nat) (ha : a%9 = 4 ∨ a%9 = 7) :
    3*((a-1)/3)+1 = a ∧ ((a-1)/3)%3 ≠ 0 := by omega

theorem inverse_residue (u v e : Nat) (h : 3*u+1 = 2^e*v) :
    u%3 ≠ 0 ↔ (2^e*v)%9 = 4 ∨ (2^e*v)%9 = 7 := by
  rw [← h]
  omega

/-- The native clock encoded by a supplied odd-parent affine identity. -/
theorem inverse_edge (u v f q : Nat) (hu : u%2 = 1)
    (h : 3*u+1 = 2^(f+1)*v) :
    run (u,q) (f+1) = (v,q+1) := by
  have hp : 2^(f+1)*v = 2*(2^f*v) := by rw [Nat.pow_succ]; ac_rfl
  have hh : (3*u+1)/2 = 2^f*v := by rw [hp] at h; omega
  have hs : next (u,q) = (2^f*v,q+1) := by simp [next, hu, hh]
  rw [show f+1 = 1+f by omega, run_add]
  change run (next (u,q)) f = (v,q+1)
  rw [hs, halving_run]

theorem alternating_two (q : Nat) : run (1,q) 2 = (1,q+1) := by
  simp [run, next]

theorem alternating_even (q m : Nat) : run (1,q) (2*m) = (1,q+m) := by
  induction m with
  | zero => simp [run]
  | succ m ih =>
    rw [Nat.mul_succ, run_add, ih, alternating_two]
    congr 1

theorem alternating_odd (q m : Nat) : run (1,q) (2*m+1) = (2,q+m+1) := by
  rw [run_add, alternating_even]
  simp [run, next]

/-- An actual arrival at one retains every subsequent native odd departure. -/
theorem arrived_full_count (u c h q j : Nat) (hit : run (u,c) h = (1,q)) :
    (run (u,c) (h+j)).2 = q+(j+1)/2 := by
  rw [run_add, hit]
  by_cases even : j % 2 = 0
  · let m := j/2
    have hj : j = 2*m := by dsimp [m]; omega
    rw [hj, alternating_even]
    omega
  · let m := j/2
    have hj : j = 2*m+1 := by dsimp [m]; omega
    rw [hj, alternating_odd]
    omega

end Collatz.NativeLowerType
