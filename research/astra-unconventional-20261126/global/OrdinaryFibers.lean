import Mathlib.Logic.Function.Iterate
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-! The fiber inequalities used here are the positive real roots of
the mass inequalities for an invariant inverse-transfer measure. -/

namespace OrdinaryFibers

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

def step (n : ℕ) : ℕ := if n % 2 = 0 then n/2 else (3*n+1)/2

def slope (n : ℕ) : K := if n % 2 = 0 then 1/2 else 3/2

private theorem slope_pos (n : ℕ) : 0 < slope (K := K) n := by
  unfold slope
  split <;> norm_num

theorem shifted_affine (n : ℕ) :
    (step n : K) + 1/2 = slope n * ((n:K) + 1/2) + 1/4 := by
  by_cases he : n % 2 = 0
  · have h : (2:K) * (step n) = n := by
      exact_mod_cast (show 2*step n=n by simp only [step, he, ite_true]; omega)
    simp only [slope, he, ite_true]
    linarith
  · have h : (2:K) * (step n) = 3*n+1 := by
      exact_mod_cast (show 2*step n=3*n+1 by simp only [step, he, ite_false]; omega)
    simp only [slope, he, ite_false]
    linarith

/-- The binary coordinate fixes the true forward shortcut. A ternary
admissibility gate is allowed to discard positive mass on its inverse. -/
def FiberInequality (v : ℕ → K) : Prop := ∀ n, v n ≤ slope n * v (step n)

private theorem next_pos {v : ℕ → K} (h : FiberInequality v) {n : ℕ} (hn : 0 < v n) :
    0 < v (step n) := pos_of_mul_pos_right (hn.trans_le (h n)) (slope_pos (K := K) n).le

private def score (v : ℕ → K) (n : ℕ) : K := ((n:K)+1/2) * v n

theorem score_increases {v : ℕ → K} (h : FiberInequality v) {n : ℕ} (hn : 0 < v n) :
    ((n:K)+1/2)*v n < ((step n:K)+1/2)*v (step n) := by
  have hp := next_pos h hn
  have le := mul_le_mul_of_nonneg_left (h n) (show 0 ≤ (n:K)+1/2 by positivity)
  rw [shifted_affine]
  nlinarith

/-- Every clock produces a distinct ordinary state from a positive-mass fiber. -/
theorem positive_fiber_injective {v : ℕ → K} (h : FiberInequality v)
    {n : ℕ} (hn : 0 < v n) : Function.Injective (fun k : ℕ => step^[k] n) := by
  have pos (k : ℕ) : 0 < v (step^[k] n) := by
    induction k with
    | zero => exact hn
    | succ k ih => rw [Function.iterate_succ_apply']; exact next_pos h ih
  have mono : StrictMono (fun k : ℕ => score v (step^[k] n)) := by
    apply strictMono_nat_of_lt_succ
    intro k
    rw [Function.iterate_succ_apply']
    exact score_increases h (pos k)
  intro i j eq
  exact mono.injective (congrArg (score v) eq)

#print axioms shifted_affine
#print axioms positive_fiber_injective

end OrdinaryFibers
