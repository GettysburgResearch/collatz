import Mathlib.Algebra.Field.Rat
import Mathlib.Tactic.Ring
import Mathlib.Tactic.LinearCombination

/-! Affine powers, exact changes of center, and accumulated defects. -/
namespace Collatz.InfiniteDescent.PoweredBlocks

structure Affine where
  slope : ℚ
  offset : ℚ

def act (a : Affine) (x : ℚ) := a.slope*x + a.offset

def repeatAct (a : Affine) : ℕ → ℚ → ℚ
  | 0, x => x
  | n+1, x => act a (repeatAct a n x)

theorem centered_power (a : Affine) {center : ℚ} (hc : act a center = center)
    (n : ℕ) (x : ℚ) :
    repeatAct a n x - center = a.slope^n * (x-center) := by
  induction n with
  | zero => simp [repeatAct]
  | succ n ih =>
    change a.slope*(repeatAct a n x)+a.offset-center = _
    change a.slope*center + a.offset = center at hc
    rw [pow_succ]
    linear_combination a.slope*ih + hc

theorem across_connector (u v : Affine) {s : ℚ} (hu : act u s = s)
    (t x : ℚ) (n : ℕ) :
    act v (repeatAct u n x) - t =
      v.slope*u.slope^n*(x-s) + (act v s - t) := by
  unfold act
  linear_combination v.slope*(centered_power u hu n x)

def walk : List Affine → ℚ → ℚ
  | [], x => x
  | f :: fs, x => walk fs (act f x)

def totalSlope : List Affine → ℚ
  | [] => 1
  | f :: fs => totalSlope fs * f.slope

def totalDefect : List Affine → ℚ
  | [] => 0
  | f :: fs => totalSlope fs * f.offset + totalDefect fs

theorem expand (fs : List Affine) (x : ℚ) :
    walk fs x = totalSlope fs * x + totalDefect fs := by
  induction fs generalizing x with
  | nil => simp [walk,totalSlope,totalDefect]
  | cons f fs ih => rw [walk, ih]; simp only [totalSlope,totalDefect,act]; ring

theorem closed_numerator (fs : List Affine) {z : ℚ} (hc : walk fs z = z) :
    (1-totalSlope fs)*z = totalDefect fs := by
  rw [expand] at hc
  linear_combination -hc

theorem zero_defects (fs : List Affine) (hh : ∀ a ∈ fs, a.offset=0) :
    totalDefect fs = 0 := by
  induction fs with
  | nil => rfl
  | cons a fs ih =>
    have ha := hh a (by simp)
    have ht := ih (fun u hu => hh u (by simp [hu]))
    simp [totalDefect, ha, ht]

#print axioms centered_power
#print axioms across_connector
#print axioms closed_numerator
#print axioms zero_defects

end Collatz.InfiniteDescent.PoweredBlocks
