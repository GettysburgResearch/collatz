import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-! Exact carry decoding and signed unrolling for punctured physical windows. -/

namespace Collatz.PuncturedWindows

set_option autoImplicit false

/-- The initial power of two is uniquely recoverable from an odd residual. -/
private theorem dyadic_order_unique {a b u v : ℕ} (hu : Odd u) (hv : Odd v)
    (eqn : 2^a * u = 2^b * v) : a = b := by
  induction a generalizing b with
  | zero =>
    cases b with
    | zero => rfl
    | succ b =>
      obtain ⟨w, hw⟩ := hu
      simp only [pow_zero, one_mul, pow_succ] at eqn
      have h : u = 2 * (2^b * v) := by rw [eqn]; ring
      omega
  | succ a ih =>
    cases b with
    | zero =>
      obtain ⟨w, hw⟩ := hv
      simp only [pow_zero, one_mul, pow_succ] at eqn
      have h : v = 2 * (2^a * u) := by rw [← eqn]; ring
      omega
    | succ b =>
      apply congrArg Nat.succ
      apply ih
      simp only [pow_succ] at eqn
      have h : 2 * (2^a*u) = 2 * (2^b*v) := by linear_combination eqn
      omega

/-- Entries count the even inputs preceding each successive odd input. -/
def rawCarry : List ℕ → ℕ
  | [] => 0
  | a :: rest => 2^a * (3^rest.length + 2 * rawCarry rest)

/-- Ordinary carry, fixed odd count, and total native length recover the word.
Here the list records every odd position. The supplied total native length
determines how many trailing even steps follow the list. -/
theorem fixed_grade_injective {xs ys : List ℕ} (grade : xs.length = ys.length)
    (eqn : rawCarry xs = rawCarry ys) : xs = ys := by
  induction xs generalizing ys with
  | nil => simpa using grade.symm
  | cons a rest ih =>
    cases ys with
    | nil => simp at grade
    | cons b tail =>
      simp only [List.length_cons, Nat.succ.injEq] at grade
      simp only [rawCarry] at eqn
      have oddCore (ls : List ℕ) : Odd (3^ls.length + 2 * rawCarry ls) :=
        ((by decide : Odd 3).pow).add_even (even_two_mul _)
      have ab := dyadic_order_unique (oddCore rest) (oddCore tail) eqn
      subst b
      have recCore := Nat.eq_of_mul_eq_mul_left (by positivity : 0 < 2^a) eqn
      rw [grade] at recCore
      have eqTail : rawCarry rest = rawCarry tail := by omega
      rw [ih grade eqTail]

structure Block where
  divisor : ℤ
  multiplier : ℤ
  error : ℤ

def divisorProduct : List Block → ℤ
  | [] => 1
  | b :: rest => b.divisor * divisorProduct rest

def gainProduct : List Block → ℤ
  | [] => 1
  | b :: rest => b.multiplier * gainProduct rest

def joinedError : List Block → ℤ
  | [] => 0
  | b :: rest => b.error * gainProduct rest + b.divisor * joinedError rest

/-- States are signed differences of the two physical trajectories. A shared
block has zero error, and an altered block has its literal carry difference. -/
inductive Run : List Block → ℤ → ℤ → Prop where
  | nil (x : ℤ) : Run [] x x
  | cons {b : Block} {bs : List Block} {x y z : ℤ}
      (edge : b.divisor * y = b.multiplier * x + b.error) (tail : Run bs y z) :
      Run (b :: bs) x z

/-- The full comparison keeps every altered block's two place multipliers. -/
theorem unroll {bs : List Block} {x y : ℤ} (run : Run bs x y) :
    divisorProduct bs * y = gainProduct bs * x + joinedError bs := by
  induction run with
  | nil x => simp [divisorProduct, gainProduct, joinedError]
  | @cons b bs x y z edge tail ih =>
    simp only [divisorProduct, gainProduct, joinedError]
    linear_combination b.divisor * ih + gainProduct bs * edge

#print axioms fixed_grade_injective
#print axioms unroll

end Collatz.PuncturedWindows
