import Mathlib.Data.Int.ModEq
import Mathlib.Tactic.Ring

/-! The centered ternary quotient on a two-gap ordinary path and its exact switch laws. -/

namespace Collatz.SixHour.TernaryQuotient

/-- A long gap is two, a short gap is one. -/
def scale (long : Bool) : ℤ := if long then 4 else 2

def sign (long : Bool) : ℤ := if long then 1 else -1

def defect (prev curr : Bool) : ℤ := (sign prev - sign curr) / 2

def quotient (prev : Bool) (x : ℤ) : ℤ := (x - sign prev) / 6

theorem exact_quotient {prev : Bool} {u x : ℤ}
    (edge : scale prev * x = 3*u+1) (odd : x % 2 = 1) :
    x = 6 * quotient prev x + sign prev := by
  cases prev <;> simp [scale, quotient, sign] at * <;> omega

theorem centered_edge {prev curr : Bool} {u x y : ℤ}
    (prevEdge : scale prev * x = 3*u+1) (edge : scale curr * y = 3*x+1)
    (ox : x % 2 = 1) (oy : y % 2 = 1) :
    scale curr * quotient curr y = 3 * quotient prev x + defect prev curr := by
  have hx := exact_quotient prevEdge ox
  have hy := exact_quotient edge oy
  cases prev <;> cases curr <;> simp [scale, sign, defect] at * <;> omega

theorem centered_below_floor {prev : Bool} {x s : ℤ}
    (hl : 8 < x) (hu : 3*x ≤ 16*s+7) (hs' : 5 < s) :
    0 < quotient prev x ∧ quotient prev x < s := by
  cases prev <;> simp [quotient, sign] <;> omega

theorem switch_odd {a b : ℤ} {prev curr : Bool} (switch : prev ≠ curr)
    (edge : scale curr * b = 3*a + defect prev curr) : a % 2 = 1 := by
  cases prev <;> cases curr <;> simp [scale, sign, defect] at * <;> omega

/-- A switch is followed by homogeneous steps for as long as the current gap repeats. -/
theorem homogeneous_run (d : ℤ) (v : ℕ → ℤ) (k : ℕ)
    (he : ∀ j < k, d * v (j+1) = 3 * v j) :
    d ^ k * v k = 3 ^ k * v 0 := by
  induction k with
  | zero => simp
  | succ k ih =>
    have h := ih (fun j hj => he j (by omega))
    calc
      d ^ (k+1) * v (k+1) = d ^ k * (d * v (k+1)) := by ring
      _ = 3 * (d ^ k * v k) := by rw [he k (by omega)]; ring
      _ = _ := by rw [h]; ring

theorem switch_run (d s a : ℤ) (v : ℕ → ℤ) (k : ℕ)
    (first : d * v 0 = 3*a+s) (he : ∀ j < k, d * v (j+1) = 3*v j) :
    d ^ (k+1) * v k = 3 ^ k * (3*a+s) := by
  calc
    d ^ (k+1) * v k = d * (d ^ k * v k) := by ring
    _ = 3 ^ k * (d * v 0) := by rw [homogeneous_run d v k he]; ring
    _ = _ := by rw [first]

end Collatz.SixHour.TernaryQuotient
