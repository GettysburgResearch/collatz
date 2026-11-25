import TernaryItinerary
import Mathlib.Tactic.Ring

/-! A positive two-parameter family of ordinary mergers in every smooth-tower
row. The larger sibling is the candidate frontier input. -/

namespace Collatz.TensorBridge

open Collatz.Itinerary

/-- The 3-unit (4^(3^r)-1)/3^(r+1), computed without natural subtraction. -/
def rowOffset : Nat → Nat
  | 0 => 1
  | r+1 => rowOffset r * (1 + 3^(r+1)*rowOffset r + 3^(2*r+1)*(rowOffset r)^2)

theorem rowOffset_identity (r : Nat) :
    4^(3^r) = 1 + 3^(r+1) * rowOffset r := by
  induction r with
  | zero => decide
  | succ r ih =>
    rw [pow_succ 3 r, pow_mul, ih, rowOffset]
    rw [show 2*r+1 = r+r+1 by omega, pow_add 3 (r+r) 1, pow_add 3 r r]
    simp only [pow_succ]
    ring

theorem rowOffset_unit (r : Nat) : rowOffset r % 3 = 1 := by
  induction r with
  | zero => decide
  | succ r ih =>
    rw [rowOffset, Nat.mul_mod, ih]
    simp [pow_succ, Nat.add_mod, Nat.mul_mod]

theorem rowOffset_odd (r : Nat) : rowOffset r % 2 = 1 := by
  have eq := congrArg (· % 2) (rowOffset_identity r)
  obtain ⟨v, hv⟩ := Nat.exists_eq_succ_of_ne_zero
    (Nat.ne_of_gt (Nat.pow_pos (by decide : 0<3) : 0<3^r))
  have hk2 : 4^(3^r)%2=0 := by rw [hv, pow_succ]; omega
  have hp3 : 3^(r+1)%2=1 := by simp [Nat.pow_mod]
  rw [hk2, Nat.add_mod 1, Nat.mul_mod (3^(r+1)), hp3] at eq
  omega

private theorem shortcut_halve (h y : Nat) : run h (2^h*y) = y := by
  induction h with
  | zero => simp [run]
  | succ h ih =>
    rw [Nat.pow_succ, Nat.mul_right_comm, Nat.mul_comm _ 2, run]
    simpa [step] using ih

/-- An affine identity between two odd sources realizes an actual pair of
possibly different shortcut clocks. -/
theorem sibling_clocks {n p h : Nat} (hn : n%2=1) (hp : p%2=1)
    (heq : 3*n+1 = 4^h*(3*p+1)) : run (2*h+1) n = run 1 p := by
  have heven : 2*((3*p+1)/2) = 3*p+1 := by omega
  have h4 : 4^h = 2^(2*h) := by rw [pow_mul]; rfl
  have hstep : step n = 2^(2*h) * step p := by
    simp only [step, hn, hp, Nat.one_ne_zero, ite_false]
    have eq : 2*(2^(2*h)*((3*p+1)/2)) = 3*n+1 := calc
      _ = 4^h*(2*((3*p+1)/2)) := by rw [h4]; ring
      _ = _ := by rw [heven, ← heq]
    omega
  simp only [run, hstep, shortcut_halve]

private theorem row_affine (r b : Nat) :
    3*(3^r*(4^(3^r)*b+rowOffset r))+1 = 4^(3^r)*(3*(3^r*b)+1) := by
  have heq := rowOffset_identity r
  rw [pow_succ] at heq
  calc
    _ = 4^(3^r)*(3*(3^r*b)) + (1+3^r*3*rowOffset r) := by ring
    _ = _ := by rw [← heq]; ring

/-- Each row r has an infinite increasing family of unit bases w with a
strictly smaller comparison base in that very row. -/
theorem every_row_lower_base (r t : Nat) :
    let h := 3^r
    let b := 6*t+3
    let w := 4^h*b+rowOffset r
    0 < b ∧ b<w ∧ w%2=1 ∧ w%3=1 ∧
      run (2*h+1) (3^r*w) = run 1 (3^r*b) := by
  dsimp
  have hp : 0 < 3^r := Nat.pow_pos (by decide)
  have e4 : 4^(3^r) % 2 = 0 := by
    obtain ⟨u, hu⟩ := Nat.exists_eq_succ_of_ne_zero (Nat.ne_of_gt hp)
    rw [hu, pow_succ]; omega
  have h3 : 3^r%2=1 := by simp [Nat.pow_mod]
  have ho := rowOffset_odd r
  have hb : 0 < 6*t+3 := by omega
  have hk : 1 ≤ 4^(3^r) := Nat.pow_pos (by decide)
  have hle : 6*t+3 ≤ 4^(3^r)*(6*t+3) := by
    simpa using Nat.mul_le_mul_right (6*t+3) hk
  have hw2 : (4^(3^r)*(6*t+3)+rowOffset r)%2=1 := by
    simp [Nat.add_mod, Nat.mul_mod, e4, ho]
  have hw3 : (4^(3^r)*(6*t+3)+rowOffset r)%3=1 := by
    simp [Nat.add_mod, Nat.mul_mod, rowOffset_unit]
  refine ⟨hb, by omega, hw2, hw3, sibling_clocks ?_ ?_ (row_affine r (6*t+3))⟩
  · rw [Nat.mul_mod, h3, hw2]
  · rw [Nat.mul_mod, h3]; omega

/-- Both published frontier guards hold throughout the family: the first
clock is one, and rows r≥2 miss the old 85 mod 512 exclusion. -/
theorem every_row_frontier_guards (r t : Nat) (hr : 0 < r) :
    let b := 6*t+3
    let w := 4^(3^r)*b+rowOffset r
    let n := 3^r*w
    (∃ a : Nat, 0<a ∧ a%2=1 ∧ n+1=2*a ∧ 2≤3^r) ∧
      (2≤r → n%512≠85) := by
  dsimp
  generalize 6*t+3 = b
  let n := 3^r*(4^(3^r)*b+rowOffset r)
  change (∃ a : Nat, 0<a ∧ a%2=1 ∧ n+1=2*a ∧ 2≤3^r) ∧
    (2≤r → n%512≠85)
  have id : 3*n+1=4^(3^r)*(3*(3^r*b)+1) := row_affine r b
  have mod_of_power (k : Nat) (hk : k≤3^r) : 4^k ∣ 3*n+1 := by
    obtain ⟨u, hu⟩ := Nat.exists_eq_add_of_le hk
    refine ⟨4^u*(3*(3^r*b)+1), ?_⟩
    calc
      _ = 4^(3^r)*(3*(3^r*b)+1) := id
      _ = _ := by nth_rw 1 [hu]; rw [pow_add, Nat.mul_assoc]
  have hp : 3^1 ≤ 3^r := Nat.pow_le_pow_right (by decide) hr
  constructor
  · obtain ⟨q, hq⟩ := mod_of_power 1 (by omega)
    refine ⟨(n+1)/2, by omega, by omega, by omega, by omega⟩
  · intro hr2
    have hp2 : 3^2 ≤ 3^r := Nat.pow_le_pow_right (by decide) hr2
    obtain ⟨q, hq⟩ := mod_of_power 5 (by omega)
    omega

end Collatz.TensorBridge
