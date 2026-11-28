import AffineOrbit
import Mathlib.Algebra.BigOperators.Group.List.Defs
import Mathlib.Data.List.Nodup

/-!
The exact carry generating function over all native parity words. This file
does not assume fresh binary digits for a bounded ordinary population. A full
ordinary inverse profile still needs its whole ternary divisor and real cut.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.AggregateProfile
open Collatz.PoweredAffine

def words : ℕ → List (List Bool)
  | 0 => [[]]
  | h + 1 => (words h).map (false :: ·) ++ (words h).map (true :: ·)

theorem mem_words_iff (h : ℕ) (w : List Bool) :
    w ∈ words h ↔ w.length = h := by
  induction h generalizing w with
  | zero => simp [words]
  | succ h ih =>
    cases w with
    | nil => simp [words]
    | cons b w =>
      cases b <;> simp [words, List.mem_map, ih]

theorem words_nodup (h : ℕ) : (words h).Nodup := by
  induction h with
  | zero => simp [words]
  | succ h ih =>
    simp only [words]
    apply List.Nodup.append
    · exact ih.map (by intro a b hab; exact List.cons.inj hab |>.2)
    · exact ih.map (by intro a b hab; exact List.cons.inj hab |>.2)
    · rw [List.disjoint_left]
      intro w hwf hwt
      simp only [List.mem_map] at hwf hwt
      rcases hwf with ⟨v, _, hv⟩
      rcases hwt with ⟨u, _, hu⟩
      rw [← hv] at hu
      exact Bool.noConfusion (List.cons.inj hu).1

theorem words_length (h : ℕ) : (words h).length = 2 ^ h := by
  induction h with
  | zero => simp [words]
  | succ h ih => simp [words, ih, pow_succ, Nat.mul_two]

private theorem numerator_first_parity (b : Bool) (w : List Bool) :
    numerator (b :: w) % 2 = if b then 1 else 0 := by
  cases b <;> simp [numerator, Nat.add_mod, Nat.pow_mod]

/-- Within one length and grade the full carries have no multiplicities. -/
theorem word_determined_by_carry (w v : List Bool)
    (hl : w.length = v.length) (hg : ones w = ones v)
    (hA : numerator w = numerator v) : w = v := by
  induction w generalizing v with
  | nil =>
    have hv : v = [] := List.length_eq_zero_iff.mp (by simpa using hl.symm)
    exact hv.symm
  | cons b w ih =>
    cases v with
    | nil => simp at hl
    | cons c v =>
      have hp : (if b then 1 else 0 : ℕ) = (if c then 1 else 0) := by
        simpa only [numerator_first_parity] using
          congrArg (fun n : ℕ => n % 2) hA
      have hbc : b = c := by
        cases b <;> cases c <;> simp_all
      subst c
      have hl' : w.length = v.length := by simpa using hl
      have hg' : ones w = ones v := by
        cases b <;> simp_all [ones]
      have hA' : numerator w = numerator v := by
        simp only [numerator, hg'] at hA
        omega
      exact congrArg (List.cons b) (ih v hl' hg' hA')

variable {R : Type*} [CommSemiring R]

def gradeSum (ws : List (List Bool)) (a : ℕ) (z : R) : R :=
  (ws.map (fun w => if ones w = a then z ^ numerator w else 0)).sum

def aggregate (h a : ℕ) (z : R) : R := gradeSum (words h) a z

private theorem gradeSum_append (ws vs : List (List Bool)) (a : ℕ) (z : R) :
    gradeSum (ws ++ vs) a z = gradeSum ws a z + gradeSum vs a z := by
  simp [gradeSum, List.map_append, List.sum_append]

private theorem gradeSum_false (ws : List (List Bool)) (a : ℕ) (z : R) :
    gradeSum (ws.map (false :: ·)) a z = gradeSum ws a (z ^ 2) := by
  unfold gradeSum
  induction ws with
  | nil => simp
  | cons w ws ih =>
    simp only [List.map_cons, List.sum_cons, ih]
    congr 1
    simp [ones, numerator, pow_mul]

private theorem gradeSum_true_succ (ws : List (List Bool)) (a : ℕ) (z : R) :
    gradeSum (ws.map (true :: ·)) (a + 1) z =
      z ^ (3 ^ a) * gradeSum ws a (z ^ 2) := by
  unfold gradeSum
  induction ws with
  | nil => simp
  | cons w ws ih =>
    simp only [List.map_cons, List.sum_cons, ih, mul_add]
    congr 1
    by_cases hw : ones w = a
    · simp [ones, numerator, hw, pow_add, pow_mul, Nat.add_comm]
    · have hw' : 1 + ones w ≠ a + 1 := by omega
      simp [ones, hw, hw']

private theorem gradeSum_true_zero (ws : List (List Bool)) (z : R) :
    gradeSum (ws.map (true :: ·)) 0 z = 0 := by
  unfold gradeSum
  induction ws with
  | nil => simp
  | cons w ws ih =>
    simp only [List.map_cons, List.sum_cons, ih]
    simp [ones]

/-- The one-frequency triangular recurrence, over any commutative semiring. -/
theorem aggregate_succ_grade (h a : ℕ) (z : R) :
    aggregate (h + 1) (a + 1) z =
      aggregate h (a + 1) (z ^ 2) +
        z ^ (3 ^ a) * aggregate h a (z ^ 2) := by
  simp only [aggregate, words, gradeSum_append, gradeSum_false, gradeSum_true_succ]

/-- The zero-odd-grade family consists of the all-zero word. -/
theorem aggregate_grade_zero (h : ℕ) (z : R) :
    aggregate h 0 z = 1 := by
  induction h generalizing z with
  | zero => simp [aggregate, words, gradeSum, ones, numerator]
  | succ h ih =>
    simp only [aggregate, words, gradeSum_append, gradeSum_false, gradeSum_true_zero,
      add_zero]
    exact ih (z ^ 2)

/-- Initial data retain the exact grade filter. -/
theorem aggregate_initial (a : ℕ) (z : R) :
    aggregate 0 a z = if a = 0 then 1 else 0 := by
  simp [aggregate, words, gradeSum, ones, numerator, eq_comm]

/-- The full word law has critical first-moment growth, with no real cutoff. -/
theorem total_word_real_value (h : ℕ) (x : ℚ) :
    ((words h).map (fun w => evalWord w x)).sum =
      (2 : ℚ) ^ h * (x + (h : ℚ) / 4) := by
  induction h generalizing x with
  | zero => simp [words, evalWord]
  | succ h ih =>
    simp only [words, List.map_append, List.sum_append, List.map_map,
      Function.comp_def, evalWord]
    rw [ih, ih]
    simp only [letter, Bool.false_eq_true, ↓reduceIte, Nat.cast_add, Nat.cast_one,
      pow_succ]
    ring

end Collatz.AggregateProfile
