import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

namespace CollatzResearch.RandomDirectionLoops

def step (b : Bool) (x : Nat) : Nat :=
  if b then (3*x+1)/2 else (x+1)/2

/-- The head is executed last; all finite chronological words still occur. -/
def run : List Bool → Nat → Nat
  | [], x => x
  | b :: w, x => step b (run w x)

def ups : List Bool → Nat
  | [] => 0
  | b :: w => ups w + if b then 1 else 0

def error : List Bool → Nat → Nat
  | [], _ => 0
  | b :: w, x => (if b then 3 else 1) * error w x +
      2^w.length * (run w x % 2)

private theorem step_eq (b : Bool) (x : Nat) :
    2 * step b x = (if b then 3 else 1)*x + x%2 := by
  cases b <;> simp only [step, Bool.false_eq_true, ite_false, ite_true]
  all_goals omega

/-- The exact affine numerator uses the actual rounding errors. -/
theorem affine (w : List Bool) (x : Nat) :
    2^w.length * run w x = 3^ups w * x + error w x := by
  induction w with
  | nil => simp [run, ups, error]
  | cons b w ih =>
    have hs := step_eq b (run w x)
    have hsm := congrArg (fun z : Nat => 2^w.length * z) hs
    cases b <;> simp only [run, ups, error, List.length_cons, Bool.false_eq_true,
      ite_false, ite_true, Nat.add_zero, pow_succ] at * <;> nlinarith

/-- Appending any choice preserves the uniform integral error bound. -/
theorem error_bound (w : List Bool) (x : Nat) :
    error w x + 2^w.length ≤ 3^w.length := by
  induction w with
  | nil => simp [error]
  | cons b w ih =>
    have hm : run w x % 2 ≤ 1 := by omega
    have hp : 2^w.length * (run w x % 2) ≤ 2^w.length := by
      simpa using Nat.mul_le_mul_left (2^w.length) hm
    cases b <;> simp only [error, List.length_cons, Bool.false_eq_true,
      ite_false, ite_true, pow_succ] <;> nlinarith

private theorem powers_ne (t u : Nat) (ht : 0 < t) :
    (2^t : Nat) ≠ 3^u := by
  intro he
  have h2 : (2^t : Nat) % 2 = 0 := by
    rw [Nat.pow_mod]
    simp [Nat.ne_of_gt ht]
  have h3 : (3^u : Nat) % 2 = 1 := by
    rw [Nat.pow_mod]
    simp
  omega

/-- A genuine positive closed word is strictly contracting in its
homogeneous multiplier. -/
theorem loop_contracts (w : List Bool) (x : Nat)
    (hw : 0 < w.length) (hx : 0 < x) (hloop : run w x = x) :
    3^ups w < 2^w.length := by
  have ha := affine w x
  rw [hloop] at ha
  have hn := powers_ne w.length (ups w) hw
  have hc : 3^ups w ≤ 2^w.length := by nlinarith
  omega

/-- Every loop of length t starts below 3^t, with no restriction on
where the loop occurs in a longer trajectory. -/
theorem loop_height (w : List Bool) (x : Nat)
    (hw : 0 < w.length) (hx : 0 < x) (hloop : run w x = x) :
    x < 3^w.length := by
  have ha := affine w x
  rw [hloop] at ha
  have hc := loop_contracts w x hw hx hloop
  have hb := error_bound w x
  have hp : 0 < (2^w.length : Nat) := Nat.pow_pos (by decide)
  have hxe : x ≤ error w x := by nlinarith
  omega

end CollatzResearch.RandomDirectionLoops
