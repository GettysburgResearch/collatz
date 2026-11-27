import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Exact ordinary-map and affine identities used in the powered-word height
argument. The Subspace Theorem and its asymptotic application are not
formalized here. No convergence or denominator-exclusion premise is hidden.
-/
set_option autoImplicit false
set_option warningAsError true

namespace Collatz.PoweredAffine

def step (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def orbit (n : ℕ) : ℕ → ℕ
  | 0 => n
  | k + 1 => orbit (step n) k

def letter (b : Bool) (x : ℚ) : ℚ :=
  if b then (3 * x + 1) / 2 else x / 2

def evalWord : List Bool → ℚ → ℚ
  | [], x => x
  | b :: w, x => evalWord w (letter b x)

def ones : List Bool → ℕ
  | [] => 0
  | b :: w => (if b then 1 else 0) + ones w

def numerator : List Bool → ℕ
  | [] => 0
  | b :: w => 3 ^ ones w * (if b then 1 else 0) + 2 * numerator w

def Realizes : ℕ → List Bool → Prop
  | _, [] => True
  | n, b :: w => n % 2 = (if b then 1 else 0) ∧ Realizes (step n) w

theorem step_positive {n : ℕ} (hn : 0 < n) : 0 < step n := by
  unfold step
  split_ifs <;> omega

theorem orbit_positive {n : ℕ} (hn : 0 < n) (k : ℕ) : 0 < orbit n k := by
  induction k generalizing n with
  | zero => exact hn
  | succ k ih => exact ih (step_positive hn)

theorem even_step {n : ℕ} (h : n % 2 = 0) : 2 * step n = n := by
  simp only [step, h, ite_true]
  omega

theorem odd_step {n : ℕ} (h : n % 2 = 1) : 2 * step n = 3 * n + 1 := by
  simp only [step, h, show ¬ (1 : ℕ) = 0 by decide, ite_false]
  omega

theorem letter_actual {n : ℕ} {b : Bool}
    (h : n % 2 = (if b then 1 else 0)) :
    letter b (n : ℚ) = (step n : ℚ) := by
  cases b with
  | false =>
    have hn := even_step h
    have he : 2 * (step n : ℚ) = (n : ℚ) := by exact_mod_cast hn
    simp only [letter, Bool.false_eq_true, ↓reduceIte]
    linarith
  | true =>
    have hn := odd_step h
    have he : 2 * (step n : ℚ) = 3 * (n : ℚ) + 1 := by exact_mod_cast hn
    simp only [letter, ↓reduceIte]
    linarith

theorem evalWord_actual {n : ℕ} {w : List Bool} (h : Realizes n w) :
    evalWord w (n : ℚ) = (orbit n w.length : ℚ) := by
  induction w generalizing n with
  | nil => rfl
  | cons b w ih =>
    have hs := letter_actual h.1
    simpa only [evalWord, hs, List.length_cons, orbit] using ih h.2

theorem evalWord_append (v w : List Bool) (x : ℚ) :
    evalWord (v ++ w) x = evalWord w (evalWord v x) := by
  induction v generalizing x with
  | nil => rfl
  | cons b v ih => exact ih (letter b x)

theorem word_affine (w : List Bool) (x : ℚ) :
    (2 : ℚ) ^ w.length * evalWord w x =
      (3 : ℚ) ^ ones w * x + (numerator w : ℚ) := by
  induction w generalizing x with
  | nil => simp [evalWord, ones, numerator]
  | cons b w ih =>
    have hh := ih (letter b x)
    cases b <;>
      simp only [List.length_cons, evalWord, ones, numerator, letter, Bool.false_eq_true,
        ↓reduceIte, Nat.cast_add, Nat.cast_mul, Nat.cast_pow, Nat.cast_ofNat,
        mul_zero, zero_add, mul_one,
        pow_add, pow_one] at hh ⊢ <;>
      nlinarith [hh]

theorem actual_word_affine {n : ℕ} {w : List Bool} (h : Realizes n w) :
    2 ^ w.length * orbit n w.length = 3 ^ ones w * n + numerator w := by
  have hf := word_affine w (n : ℚ)
  rw [evalWord_actual h] at hf
  exact_mod_cast hf

/-- A center is supplied through its exact rational defining equation. -/
theorem word_centered (w : List Bool) (x a : ℚ)
    (ha : ((2 : ℚ) ^ w.length - (3 : ℚ) ^ ones w) * a = numerator w) :
    (2 : ℚ) ^ w.length * (evalWord w x - a) =
      (3 : ℚ) ^ ones w * (x - a) := by
  have hf := word_affine w x
  nlinarith [ha]

def repeatEval (w : List Bool) (x : ℚ) : ℕ → ℚ
  | 0 => x
  | r + 1 => evalWord w (repeatEval w x r)

theorem repeated_centered (w : List Bool) (x a : ℚ) (r : ℕ)
    (ha : ((2 : ℚ) ^ w.length - (3 : ℚ) ^ ones w) * a = numerator w) :
    (2 : ℚ) ^ (r * w.length) * (repeatEval w x r - a) =
      (3 : ℚ) ^ (r * ones w) * (x - a) := by
  induction r with
  | zero => simp [repeatEval]
  | succ r ih =>
    have hs := word_centered w (repeatEval w x r) a ha
    simp only [repeatEval, Nat.succ_mul, pow_add]
    calc
      2 ^ (r * w.length) * 2 ^ w.length *
          (evalWord w (repeatEval w x r) - a) =
          2 ^ (r * w.length) * (3 ^ ones w * (repeatEval w x r - a)) := by
            rw [mul_assoc, hs]
      _ = 3 ^ ones w * (2 ^ (r * w.length) * (repeatEval w x r - a)) := by ring
      _ = 3 ^ ones w * (3 ^ (r * ones w) * (x - a)) := by rw [ih]
      _ = 3 ^ (r * ones w) * 3 ^ ones w * (x - a) := by ring

/-- Changing centers are retained rather than discarded as bounded errors. -/
theorem center_telescope (u x a : ℕ → ℚ) (k : ℕ)
    (h : ∀ i ≤ k, u (i + 1) * (x (i + 1) - a i) = u i * (x i - a i)) :
    u (k + 1) * (x (k + 1) - a k) =
      u 0 * (x 0 - a 0) +
        ∑ i ∈ Finset.range k, u (i + 1) * (a i - a (i + 1)) := by
  induction k with
  | zero => simpa using h 0 (by omega)
  | succ k ih =>
    have hi := ih (fun i hi => h i (by omega))
    have hs := h (k + 1) (by omega)
    rw [Finset.sum_range_succ]
    nlinarith [hi, hs]

/-- More generally each physical arc can carry a different rational reference
at its two ends. The join defect stays attached to the same original path. -/
theorem reference_telescope (u x a b : ℕ → ℚ) (k : ℕ)
    (h : ∀ i ≤ k, u (i + 1) * (x (i + 1) - b i) = u i * (x i - a i)) :
    u (k + 1) * (x (k + 1) - b k) =
      u 0 * (x 0 - a 0) +
        ∑ i ∈ Finset.range k, u (i + 1) * (b i - a (i + 1)) := by
  induction k with
  | zero => simpa using h 0 (by omega)
  | succ k ih =>
    have hi := ih (fun i hi => h i (by omega))
    have hs := h (k + 1) (by omega)
    rw [Finset.sum_range_succ]
    nlinarith [hi, hs]

end Collatz.PoweredAffine
