import Mathlib.Algebra.Ring.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! Exact shortcut-word algebra for the signed conformal entrance tree.
`true` is the odd inverse branch; `false` is the even inverse branch.
The word convention is outer composition, so reading the list backwards
is the chronological inverse path. No local legality is assumed here.
-/
namespace Collatz.ConformalTree

def inverse (odd : Bool) (x : ℚ) : ℚ :=
  if odd then (2*x-1)/3 else 2*x

def inverseWord : List Bool → ℚ → ℚ
  | [], x => x
  | b :: w, x => inverse b (inverseWord w x)

def inverseSlope : List Bool → ℚ
  | [] => 1
  | b :: w => (if b then 2/3 else 2) * inverseSlope w

def evenCount : List Bool → ℕ
  | [] => 0
  | b :: w => if b then evenCount w else evenCount w + 1

def wordWeight : List Bool → ℚ
  | [] => 1
  | b :: w => (if b then 9/4 else 1/4) * wordWeight w

def oddIterate : ℕ → ℚ → ℚ
  | 0, x => x
  | n+1, x => (3 * oddIterate n x + 1)/2

theorem inverseWord_affine (w : List Bool) (x d : ℚ) :
    inverseWord w (x+d) = inverseWord w x + inverseSlope w*d := by
  induction w with
  | nil => simp [inverseWord, inverseSlope]
  | cons b w ih =>
    simp only [inverseWord, inverseSlope, ih]
    cases b <;> simp only [inverse, Bool.false_eq_true, ite_false, ite_true] <;> ring

theorem oddIterate_formula (n : ℕ) (z : ℚ) :
    oddIterate n z = (3/2 : ℚ)^n*(z+1)-1 := by
  induction n with
  | zero => simp [oddIterate]
  | succ n ih => rw [oddIterate, ih, pow_succ]; ring

theorem slope_scaled (w : List Bool) :
    inverseSlope w * (3/2 : ℚ)^w.length = (3:ℚ)^(evenCount w) := by
  induction w with
  | nil => simp [inverseSlope, evenCount]
  | cons b w ih =>
    cases b <;> simp only [inverseSlope, evenCount, List.length_cons,
      Bool.false_eq_true, ite_false, ite_true, pow_succ]
    · calc
        2 * inverseSlope w * ((3/2)^w.length*(3/2)) =
            (inverseSlope w*(3/2)^w.length)*3 := by ring
        _ = 3^evenCount w*3 := by rw [ih]
    · calc
        (2/3) * inverseSlope w * ((3/2)^w.length*(3/2)) =
            inverseSlope w*(3/2)^w.length := by ring
        _ = 3^evenCount w := ih

/-- The finite signed-tree affine formula, at the actual all-odd target. -/
theorem entrance_identity (w : List Bool) (z : ℚ) :
    inverseWord w (oddIterate w.length z) =
      inverseWord w (-1) + (3:ℚ)^(evenCount w)*(z+1) := by
  rw [oddIterate_formula]
  have h : (3/2 : ℚ)^w.length*(z+1)-1 =
      -1 + (3/2)^w.length*(z+1) := by ring
  rw [h, inverseWord_affine, ← mul_assoc, slope_scaled]

theorem normalized_weight (w : List Bool) :
    (4/9 : ℚ)^w.length * wordWeight w = (1/9 : ℚ)^(evenCount w) := by
  induction w with
  | nil => simp [wordWeight, evenCount]
  | cons b w ih =>
    cases b <;> simp only [wordWeight, evenCount, List.length_cons,
      Bool.false_eq_true, ite_false, ite_true, pow_succ]
    · calc
        ((4/9)^w.length*(4/9))*((1/4)*wordWeight w) =
            ((4/9)^w.length*wordWeight w)*(1/9) := by ring
        _ = (1/9)^evenCount w*(1/9) := by rw [ih]
    · calc
        ((4/9)^w.length*(4/9))*((9/4)*wordWeight w) =
            (4/9)^w.length*wordWeight w := by ring
        _ = (1/9)^evenCount w := ih

/-- The branch weights really are the squares of the forward slopes. -/
theorem weight_inverse_square (w : List Bool) :
    wordWeight w * (inverseSlope w)^2 = 1 := by
  induction w with
  | nil => norm_num [wordWeight, inverseSlope]
  | cons b w ih =>
    cases b <;> simp only [wordWeight, inverseSlope,
      Bool.false_eq_true, ite_false, ite_true]
    · calc
        ((1/4)*wordWeight w)*(2*inverseSlope w)^2 =
            wordWeight w*(inverseSlope w)^2 := by ring
        _ = 1 := ih
    · calc
        ((9/4)*wordWeight w)*((2/3)*inverseSlope w)^2 =
            wordWeight w*(inverseSlope w)^2 := by ring
        _ = 1 := ih

theorem inverseWord_negative (w : List Bool) (x : ℚ) (hx : x < 0) :
    inverseWord w x < 0 := by
  induction w with
  | nil => exact hx
  | cons b w ih =>
    cases b <;> simp only [inverseWord, inverse, Bool.false_eq_true, ite_false, ite_true] <;>
      linarith

end Collatz.ConformalTree
