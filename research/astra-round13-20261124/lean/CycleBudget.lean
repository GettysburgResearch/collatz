import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Data.Rat.Cast.Order
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

namespace Collatz.CycleBudget

/-- A product of positive affine corrections is controlled by their sum.
This rational estimate avoids exponential or logarithmic rounding. -/
theorem product_complement (x : ℕ → ℚ) (n : ℕ) (hn : ∀ i < n, 0 ≤ x i)
    (hs : (∑ i ∈ Finset.range n, x i) < 1) :
    (∏ i ∈ Finset.range n, (1 + x i)) * (1 - ∑ i ∈ Finset.range n, x i) ≤ 1 := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hx := hn n (by omega)
    rw [Finset.sum_range_succ] at hs
    have hsum : 0 ≤ ∑ i ∈ Finset.range n, x i :=
      Finset.sum_nonneg fun i hi => hn i ((Finset.mem_range.mp hi).trans (Nat.lt_succ_self n))
    have hprod : 0 ≤ ∏ i ∈ Finset.range n, (1 + x i) :=
      Finset.prod_nonneg fun i hi => by
        have h := hn i ((Finset.mem_range.mp hi).trans (Nat.lt_succ_self n))
        linarith
    have h := ih (fun i hi => hn i (by omega)) (by linarith)
    rw [Finset.sum_range_succ, Finset.prod_range_succ, mul_assoc]
    apply le_trans (mul_le_mul_of_nonneg_left _ hprod) h
    nlinarith [mul_nonneg hx hsum, sq_nonneg (x n)]

/-- A second product estimate reuses the first to obtain a half-bit bound
using only rational arithmetic. -/
theorem product_second (x : ℕ → ℚ) (n : ℕ) (hn : ∀ i < n, 0 ≤ x i)
    (hs : (∑ i ∈ Finset.range n, x i) < 1) :
    (∏ i ∈ Finset.range n, (1 + x i)) * (2 - ∑ i ∈ Finset.range n, x i) ≤
      2 + ∑ i ∈ Finset.range n, x i := by
  induction n with
  | zero => simp
  | succ n ih =>
    have hx := hn n (by omega)
    rw [Finset.sum_range_succ] at hs
    have hn' : ∀ i < n, 0 ≤ x i := fun i hi => hn i (by omega)
    have hs' : (∑ i ∈ Finset.range n, x i) < 1 := by linarith
    have h := ih hn' hs'
    have hfirst := product_complement x n hn' hs'
    have hp : 0 ≤ ∏ i ∈ Finset.range n, (1 + x i) :=
      Finset.prod_nonneg fun i hi => by
        have hh := hn' i (Finset.mem_range.mp hi)
        linarith
    have hlast : (∏ i ∈ Finset.range n, (1 + x i)) *
        (1 - ∑ i ∈ Finset.range n, x i - x n) ≤ 1 := by
      nlinarith [mul_nonneg hp hx]
    have hstep := add_le_add h (mul_le_mul_of_nonneg_left hlast hx)
    rw [Finset.sum_range_succ, Finset.prod_range_succ]
    linarith only [hstep]

/-- The half-bit correction bound is purely rational, including its strict endpoint. -/
theorem half_bit (x : ℕ → ℚ) (n : ℕ) (hn : ∀ i < n, 0 ≤ x i)
    (hs : (∑ i ∈ Finset.range n, x i) < 17 / 50) :
    (∏ i ∈ Finset.range n, (1 + x i)) ^ 2 < 2 := by
  have h := product_second x n hn (by linarith)
  have hp : 0 ≤ ∏ i ∈ Finset.range n, (1 + x i) :=
    Finset.prod_nonneg fun i hi => by
      have hh := hn i (Finset.mem_range.mp hi)
      linarith
  have hb : (∏ i ∈ Finset.range n, (1 + x i)) < 117 / 83 := by
    nlinarith [mul_nonneg hp (show 0 ≤ 17 / 50 - ∑ i ∈ Finset.range n, x i by linarith)]
  have hh := mul_self_lt_mul_self hp hb
  nlinarith

/-- A primitive cycle satisfying the explicit sum envelope has a unique possible
binary clock, expressed by the consecutive powers bracketing its ternary clock. -/
theorem primitive_clock (x : ℕ → ℚ) (k A : ℕ)
    (hn : ∀ i < k, 0 ≤ x i) (hs : (∑ i ∈ Finset.range k, x i) < 17 / 50)
    (hcycle : (2 : ℚ)^A = 3^k * ∏ i ∈ Finset.range k, (1 + x i))
    (hstrict : (3 : ℚ)^k < 2^A) :
    (3 : ℚ)^k < 2^A ∧ (2 : ℚ)^A < 2 * 3^k := by
  have h := product_complement x k hn (by linarith)
  have hp : 0 ≤ ∏ i ∈ Finset.range k, (1 + x i) :=
    Finset.prod_nonneg fun i hi => by
      have hh := hn i (Finset.mem_range.mp hi)
      linarith
  have hb : (∏ i ∈ Finset.range k, (1 + x i)) < 2 := by
    nlinarith [mul_nonneg hp (show 0 ≤ 17 / 50 - ∑ i ∈ Finset.range k, x i by linarith)]
  refine ⟨hstrict, ?_⟩
  rw [hcycle, mul_comm (2 : ℚ) (3 ^ k)]
  exact mul_lt_mul_of_pos_left hb (by positivity)

/-- Strict squared endpoint gate for X=3^n q_i and Y=q_(i+n).
The complete affine equation is retained as an exact rational equality. -/
theorem endpoint_squares (x : ℕ → ℚ) (n X Y A : ℕ) (hX : 0 < X)
    (hn : ∀ i < n, 0 ≤ x i) (hs : (∑ i ∈ Finset.range n, x i) < 17 / 50)
    (he : (2 : ℚ)^A * Y = X * ∏ i ∈ Finset.range n, (1 + x i))
    (hp : (1 : ℚ) < ∏ i ∈ Finset.range n, (1 + x i)) :
    X^2 < (2^A*Y)^2 ∧ (2^A*Y)^2 < 2*X^2 := by
  have hX' : (0 : ℚ) < X := by exact_mod_cast hX
  have hhalf := half_bit x n hn hs
  have hl : (X : ℚ) < 2^A * Y := by
    rw [he]
    simpa using (mul_lt_mul_of_pos_left hp hX')
  have hlow : (X : ℚ)^2 < (2^A * (Y : ℚ))^2 := by
    simpa only [pow_two] using mul_self_lt_mul_self hX'.le hl
  have hu : ((2 : ℚ)^A * Y)^2 < 2*(X : ℚ)^2 := by
    rw [he, mul_pow]
    simpa only [mul_comm (2 : ℚ)] using mul_lt_mul_of_pos_left hhalf (sq_pos_of_pos hX')
  exact ⟨by exact_mod_cast hlow, by exact_mod_cast hu⟩

/-- On a contracting canonical phase, an integer carry budget must vanish if
the ordinary binary clock overshoot factor is less than two. -/
theorem no_periodic_carry (k A B K : ℕ) (hclock : A = B + 2 * K)
    (hcontract : (3 : ℕ)^k < 2^B) (hupper : (2 : ℕ)^A < 2 * 3^k) :
    K = 0 := by
  apply Classical.byContradiction
  intro hn
  have he : B + 1 ≤ A := by omega
  have hp : (2 : ℕ)^(B + 1) ≤ 2^A := Nat.pow_le_pow_right (by decide) he
  rw [pow_succ] at hp
  omega

#print axioms product_complement
#print axioms product_second
#print axioms half_bit
#print axioms endpoint_squares
#print axioms primitive_clock
#print axioms no_periodic_carry
end Collatz.CycleBudget
