module

public import Mathlib.Data.Nat.Choose.Sum
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Positivity
public import Mathlib.Tactic.Ring
public import Mathlib.Tactic.Linarith

@[expose] public section

/-!
Exact counting core for the full-denominator affine-mixing attempt.
No cycle exclusion, GRH, logarithm theorem, or entropy theorem is assumed.
-/

namespace CollatzCycleWordEntropy

theorem weighted_binomial_bound (A p : Nat) (hp : p ≤ A) :
    A.choose p * (4 ^ p * 3 ^ (A-p)) ≤ 7 ^ A := by
  have h := Finset.single_le_sum
    (fun i (_ : i ∈ Finset.range (A+1)) =>
      Nat.zero_le (4 ^ i * 3 ^ (A-i) * A.choose i))
    (Finset.mem_range.mpr (by omega : p < A+1))
  have hb := add_pow (4 : Nat) 3 A
  norm_num only [Nat.cast_id] at hb
  rw [← hb] at h
  simpa only [Nat.mul_comm (A.choose p)] using h

theorem cone_weight_bound (A p : Nat) (hp : p ≤ A)
    (hcone : 4*A ≤ 7*p) :
    6912 ^ A ≤ (4 ^ p * 3 ^ (A-p)) ^ 7 := by
  let e := 7*p-4*A
  have h1 : 7*p = 4*A+e := by dsimp [e]; omega
  have h2 : 3*A = 7*(A-p)+e := by dsimp [e]; omega
  have h34 : 3^e ≤ 4^e := Nat.pow_le_pow_left (by decide) e
  calc
    6912^A = (4^4 * 3^3)^A := by norm_num
    _ = 4^(4*A) * 3^(3*A) := by rw [mul_pow, ← pow_mul, ← pow_mul]
    _ = (4^(4*A) * 3^(7*(A-p))) * 3^e := by rw [h2, pow_add]; ring
    _ ≤ (4^(4*A) * 3^(7*(A-p))) * 4^e :=
      Nat.mul_le_mul_left _ h34
    _ = (4^p * 3^(A-p))^7 := by
      rw [mul_pow, ← pow_mul, ← pow_mul]
      rw [Nat.mul_comm p 7, Nat.mul_comm (A-p) 7, h1, pow_add]
      ring

theorem cycle_word_count_bound (A p : Nat) (hA : 0 < A)
    (hp : p ≤ A) (hcone : 4*A ≤ 7*p) :
    (A.choose p)^7 < 120^A := by
  have hw := weighted_binomial_bound A p hp
  have hw7 := Nat.pow_le_pow_left hw 7
  have hc := cone_weight_bound A p hp hcone
  have hmul : (A.choose p)^7 * 6912^A < 120^A * 6912^A := by
    calc
      (A.choose p)^7 * 6912^A ≤
          (A.choose p)^7 * (4^p * 3^(A-p))^7 := Nat.mul_le_mul_left _ hc
      _ ≤ (7^A)^7 := by simpa only [mul_pow] using hw7
      _ = 823543^A := by rw [← pow_mul, Nat.mul_comm A 7, pow_mul]; norm_num
      _ < 829440^A := Nat.pow_lt_pow_left (by decide) (Nat.ne_of_gt hA)
      _ = 120^A * 6912^A := by rw [← mul_pow]; norm_num
  exact Nat.lt_of_mul_lt_mul_right hmul

#print axioms weighted_binomial_bound
#print axioms cone_weight_bound
#print axioms cycle_word_count_bound

end CollatzCycleWordEntropy
