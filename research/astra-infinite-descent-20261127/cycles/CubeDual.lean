import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith

/-! A weighted affine upper bound on an entire real unit cube.
The integer rows can be stored as sparse lists; coordinate zero is the constant. -/
set_option autoImplicit false
namespace Collatz.InfiniteDescent.CubeDual

abbrev Coeff := ℕ → ℤ

def value (c : Coeff) (x : ℕ → ℝ) : ℕ → ℝ
  | 0 => c 0
  | n+1 => value c x n + (c (n+1) : ℝ) * x n

def cap (c : Coeff) : ℕ → ℤ
  | 0 => c 0
  | n+1 => cap c n + max (c (n+1)) 0

theorem value_le_cap (c : Coeff) (x : ℕ → ℝ)
    (hx : ∀ i, 0 ≤ x i ∧ x i ≤ 1) (n : ℕ) : value c x n ≤ (cap c n : ℝ) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp only [value, cap, Int.cast_add]
    apply add_le_add ih
    by_cases h : 0 ≤ c (n+1)
    · rw [max_eq_left h]
      have h' : (0 : ℝ) ≤ (c (n+1) : ℝ) := by exact_mod_cast h
      simpa using mul_le_mul_of_nonneg_left (hx n).2 h'
    · have h' : (c (n+1) : ℝ) ≤ 0 := by exact_mod_cast le_of_not_ge h
      rw [max_eq_right (le_of_not_ge h), Int.cast_zero]
      exact mul_nonpos_of_nonpos_of_nonneg h' (hx n).1

structure Row where
  name : String
  weight : ℕ
  base : List (ℕ × ℤ)
  delta : List (ℕ × ℤ)
  deriving Repr

def sparse (j : ℕ) : List (ℕ × ℤ) → ℤ
  | [] => 0
  | (k,a)::xs => (if k = j then a else 0) + sparse j xs

def rowCoeff (edge : Bool) (r : Row) (j : ℕ) : ℤ :=
  sparse j r.base + if edge then sparse j r.delta else 0

def total : List Row → ℕ
  | [] => 0
  | r::rs => r.weight + total rs

def combine (edge : Bool) : List Row → Coeff
  | [], _ => 0
  | r::rs, j => (r.weight : ℤ) * rowCoeff edge r j + combine edge rs j

theorem value_smul_add (r s : Coeff) (w : ℤ) (x : ℕ → ℝ) (n : ℕ) :
    value (fun i => w*r i+s i) x n = (w : ℝ)*value r x n + value s x n := by
  induction n with
  | zero => simp [value]
  | succ n ih => simp only [value, ih, Int.cast_add, Int.cast_mul]; ring

theorem rows_lower (edge : Bool) (rs : List Row) (x : ℕ → ℝ) (n : ℕ) (t : ℝ)
    (h : ∀ r ∈ rs, t ≤ value (rowCoeff edge r) x n) :
    (total rs : ℝ)*t ≤ value (combine edge rs) x n := by
  induction rs with
  | nil =>
    simp only [total, Nat.cast_zero, zero_mul]
    induction n with
    | zero => simp [value, combine]
    | succ n ih => simpa [value, combine] using ih
  | cons r rs ih =>
    have tail := ih (fun a ha => h a (List.mem_cons_of_mem _ ha))
    have head := mul_le_mul_of_nonneg_left (h r (List.mem_cons_self)) (Nat.cast_nonneg r.weight : (0 : ℝ) ≤ r.weight)
    change ((r.weight + total rs : ℕ) : ℝ)*t ≤
      value (fun j => (r.weight : ℤ)*rowCoeff edge r j + combine edge rs j) x n
    rw [value_smul_add, Int.cast_natCast, Nat.cast_add, add_mul]
    exact add_le_add head tail

theorem some_row_lt (edge : Bool) (rs : List Row) (x : ℕ → ℝ)
    (hx : ∀ i, 0 ≤ x i ∧ x i ≤ 1) (n : ℕ) (t : ℝ)
    (h : (cap (combine edge rs) n : ℝ) < (total rs : ℝ)*t) :
    ∃ r ∈ rs, value (rowCoeff edge r) x n < t := by
  by_contra! allLarge
  exact (not_lt_of_ge (le_trans (rows_lower edge rs x n t allLarge)
    (value_le_cap _ _ hx n))) h

structure Certificate where
  dimension : ℕ
  cuts : ℕ
  wrapped : ℕ
  reciprocalMargin : ℤ
  rows : List Row
  deriving Repr

/-- All row coefficients are scaled by 10000. Each endpoint must beat the given margin. -/
def endpointPass (c : Certificate) (edge : Bool) : Bool :=
  decide (c.reciprocalMargin * cap (combine edge c.rows) c.dimension +
    10000 * (total c.rows : ℤ) < 0)

def passes (c : Certificate) : Bool := endpointPass c false && endpointPass c true

end Collatz.InfiniteDescent.CubeDual
