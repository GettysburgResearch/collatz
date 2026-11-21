/-
An unbounded, terminating ordinary-path macro for the expanding signed -5
cycle.  This is not a proof of the Collatz conjecture: after the macro exits,
its endpoint is another positive ordinary integer, with no proved global
decrease.  The module exposes that distinction explicitly.

Lean 4.34.1, core only.  Imports the unchanged PR174 ordinary-basin foundation.
-/
import Collatz.Closure

open CollatzReverseBasin CollatzClosure

namespace CollatzNegativeFive

/-- Literal shortcut iteration; the counter counts ordinary shortcut clocks. -/
def run : Nat → Nat → Nat
  | 0, n => n
  | k+1, n => run k (shortcut n)

theorem run_add (a b n : Nat) : run (a+b) n = run b (run a n) := by
  induction a generalizing n with
  | zero => simp [run]
  | succ a ih =>
    have e : a+1+b = (a+b)+1 := by omega
    rw [e, run, ih, run]

theorem run_basin (k n : Nat) : Basin (run k n) ↔ Basin n := by
  induction k generalizing n with
  | zero => simp [run]
  | succ k ih =>
    exact (ih (shortcut n)).trans (basin_step n)

/-- A positive traversal of the negative -5 cycle has exactly three clocks. -/
theorem negative_five_block (z : Nat) (hz : 0 < z) :
    run 3 (8*z-5) = 9*z-5 := by
  have h1 : shortcut (8*z-5) = 12*z-7 := by
    unfold shortcut
    split <;> omega
  have h2 : shortcut (12*z-7) = 18*z-10 := by
    unfold shortcut
    split <;> omega
  have h3 : shortcut (18*z-10) = 9*z-5 := by
    unfold shortcut
    split <;> omega
  simp only [run, h1, h2, h3]

/-- All-length exact expansion formula, including the literal ordinary path. -/
theorem negative_five_run (r z : Nat) (hz : 0 < z) :
    run (3*r) (8^r*z-5) = 9^r*z-5 := by
  induction r generalizing z with
  | zero => simp [run]
  | succ r ih =>
    have hpos : 0 < 8^r*z := Nat.mul_pos (Nat.pow_pos (by omega)) hz
    have e1 : 8^(r+1)*z = 8*(8^r*z) := by grind
    have e2 : 9*(8^r*z) = 8^r*(9*z) := by grind
    have e3 : 9^(r+1)*z = 9^r*(9*z) := by grind
    have e4 : 3*(r+1) = 3 + 3*r := by omega
    rw [e1, e3, e4, run_add, negative_five_block _ hpos, e2]
    exact ih (9*z) (by omega)

/-- Factor out every factor of eight.  The recursion decreases its input,
    even though the ordinary Collatz macro described by it can increase. -/
def stripEight (d : Nat) : Nat × Nat :=
  if hd : 0 < d ∧ d % 8 = 0 then
    let p := stripEight (d/8)
    (p.1+1, p.2)
  else (0,d)
termination_by d
decreasing_by omega

theorem stripEight_spec (d : Nat) (hd : 0 < d) :
    let p := stripEight d
    d = 8^p.1*p.2 ∧ 0 < p.2 ∧ p.2 % 8 ≠ 0 := by
  induction d using Nat.strong_induction_on with
  | h d ih =>
    rw [stripEight]
    split
    · rename_i hh
      have hq : 0 < d/8 := by omega
      have hr := ih (d/8) (by omega) hq
      rcases hr with ⟨he, hp, hn⟩
      dsimp only
      refine ⟨?_, hp, hn⟩
      have he' : d = 8*(d/8) := by omega
      rw [he', he]
      grind
    · rename_i hh
      dsimp only
      simp only [Nat.pow_zero, Nat.one_mul]
      exact ⟨True.intro, hd, by omega⟩

/-- Result and exact ordinary clock count of the maximal -5-cycle run. -/
def escape (n : Nat) : Nat × Nat :=
  let p := stripEight (n+5)
  (3*p.1, 9^p.1*p.2-5)

theorem nine_pow_mod_eight (r : Nat) : 9^r % 8 = 1 := by
  induction r with
  | zero => rfl
  | succ r ih =>
    rw [Nat.pow_succ, Nat.mul_mod, ih]

theorem eight_pow_le_nine_pow (r : Nat) : 8^r ≤ 9^r := by
  induction r with
  | zero => omega
  | succ r ih =>
    rw [Nat.pow_succ, Nat.pow_succ]
    omega

/-- The macro is total, follows the ordinary orbit, stays positive, and exits
    the exact cylinder supporting another -5 block.  No descent is asserted. -/
theorem escape_spec (n : Nat) (hn : 0 < n) :
    let out := escape n
    run out.1 n = out.2 ∧ 0 < out.2 ∧ out.2 % 8 ≠ 3 ∧
      (Basin out.2 ↔ Basin n) := by
  have hs := stripEight_spec (n+5) (by omega)
  rcases hs with ⟨he, hp, hm⟩
  let r := (stripEight (n+5)).1
  let z := (stripEight (n+5)).2
  change n+5 = 8^r*z at he
  change 0 < z at hp
  change z%8 ≠ 0 at hm
  have he' : n = 8^r*z-5 := by omega
  have hsize : 8^r*z ≤ 9^r*z := Nat.mul_le_mul_right z (eight_pow_le_nine_pow r)
  have hpos : 5 < 9^r*z := by omega
  have hpath : run (3*r) n = 9^r*z-5 := by
    rw [he']
    exact negative_five_run r z hp
  have hmod : (9^r*z)%8 ≠ 0 := by
    rw [Nat.mul_mod, nine_pow_mod_eight]
    simpa using hm
  change run (3*r) n = 9^r*z-5 ∧ 0 < 9^r*z-5 ∧
    (9^r*z-5)%8 ≠ 3 ∧ (Basin (9^r*z-5) ↔ Basin n)
  refine ⟨hpath, by omega, by omega, ?_⟩
  rw [← hpath]
  exact run_basin _ _

/-- Expanding-cycle escape is not ordinary numerical descent: the first
    post-exit halving can still be larger than the source. -/
theorem escape_need_not_descend :
    escape 262139 = (18,531436) ∧ shortcut 531436 = 265718 ∧
      262139 < 265718 := by
  simp [escape, stripEight, shortcut]

end CollatzNegativeFive
