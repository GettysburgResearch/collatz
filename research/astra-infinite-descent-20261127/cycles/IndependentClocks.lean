import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Ring

/-! Forced affine recurrences with independent periodic forcings in equal-weight cells. -/
namespace Collatz.InfiniteDescent.IndependentClocks

def carry (a b : ℤ) : List ℤ → ℤ
  | [] => 0
  | c::cs => b^cs.length*c + a*carry a b cs

theorem carry_append (a b : ℤ) (u v : List ℤ) :
    carry a b (u++v)=b^v.length*carry a b u+a^u.length*carry a b v := by
  induction u with
  | nil => simp [carry]
  | cons c cs ih => simp only [List.cons_append,carry,List.length_cons,List.length_append,pow_add,pow_succ,ih]; ring

theorem carry_add (a b : ℤ) (u v : List ℤ) (len : u.length=v.length) :
    carry a b (List.zipWith (·+·) u v) = carry a b u+carry a b v := by
  induction u generalizing v with
  | nil => cases v <;> simp_all [carry]
  | cons x xs ih =>
    cases v with
    | nil => simp at len
    | cons y ys =>
      have h : xs.length=ys.length := by simpa using len
      simp [carry,ih ys h,List.length_zipWith,h]
      ring

def copies {α : Type*} (w : List α) : ℕ → List α
  | 0 => []
  | n+1 => copies w n ++ w

@[simp] theorem copies_length {α : Type*} (w : List α) (n : ℕ) :
    (copies w n).length=w.length*n := by
  induction n with
  | zero => simp [copies]
  | succ n ih => simp [copies,ih,Nat.mul_succ]

/-- An arbitrary periodic forcing has its shorter block denominator even
when it is evaluated at a longer joint return. No division is used. -/
theorem periodic_denominator (a b : ℤ) (w : List ℤ) (n : ℕ) :
    (a^w.length-b^w.length)*carry a b (copies w n) =
      (a^(w.length*n)-b^(w.length*n))*carry a b w := by
  induction n with
  | zero => simp [copies,carry]
  | succ n ih =>
    simp only [copies,carry_append,copies_length,Nat.mul_succ,pow_add]
    linear_combination b^w.length * ih

/-- An exact denominator for the sum of any finite collection of individually
periodic fixed-point coordinates, using any common multiple of their denominators. -/
theorem add_cleared {x y : ℚ} {l a b : ℤ}
    (hx : (l:ℚ)*x=a) (hy : (l:ℚ)*y=b) : (l:ℚ)*(x+y)=a+b := by
  linear_combination hx+hy

#print axioms carry_add
#print axioms carry_append
#print axioms periodic_denominator
#print axioms add_cleared

end Collatz.InfiniteDescent.IndependentClocks
