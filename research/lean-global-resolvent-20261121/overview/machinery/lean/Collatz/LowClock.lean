module

public import Mathlib.Algebra.BigOperators.Group.Finset.Basic
public import Mathlib.Tactic.NormNum
public import Mathlib.Tactic.Linarith
public import Mathlib.Tactic.Ring

@[expose] public section

namespace CollatzLowClock

private theorem high_step (x y a : ℕ) (hx : 64 ≤ x)
    (h : 2 ^ a * y = 3 * x + 1) :
    2 ^ (5 * a) * y ^ 5 ≤ 2 ^ 8 * x ^ 5 := by
  have hlin : 64 * (3 * x + 1) ≤ 193 * x := by omega
  have hp := Nat.pow_le_pow_left hlin 5
  have hnum : (193 : ℕ) ^ 5 ≤ 64 ^ 5 * 2 ^ 8 := by norm_num
  have hprod := Nat.mul_le_mul_right (x ^ 5) hnum
  have hpow : (2 ^ a * y) ^ 5 = 2 ^ (5 * a) * y ^ 5 := by
    rw [mul_pow, ← pow_mul]
    congr 2
    omega
  rw [mul_pow, mul_pow] at hp
  rw [← h, hpow] at hp
  have hfinal : 64 ^ 5 * (2 ^ (5 * a) * y ^ 5) ≤
      64 ^ 5 * (2 ^ 8 * x ^ 5) := by
    calc
      _ ≤ 193 ^ 5 * x ^ 5 := hp
      _ ≤ _ := by rw [← Nat.mul_assoc]; exact hprod
  exact Nat.le_of_mul_le_mul_left hfinal (by norm_num)

private theorem high_prefix (x a : ℕ → ℕ) (s : ℕ)
    (hf : ∀ i < s, 64 ≤ x i)
    (he : ∀ i < s, 2 ^ a i * x (i + 1) = 3 * x i + 1) :
    2 ^ (5 * ∑ i ∈ Finset.range s, a i) * x s ^ 5 ≤
      2 ^ (8 * s) * x 0 ^ 5 := by
  induction s with
  | zero => simp
  | succ s ih =>
      have hi := ih (by intro i h; exact hf i (by omega))
        (by intro i h; exact he i (by omega))
      have hs := high_step (x s) (x (s + 1)) (a s)
        (hf s (by omega)) (he s (by omega))
      rw [Finset.sum_range_succ, Nat.mul_add, pow_add]
      calc
        _ = 2 ^ (5 * ∑ i ∈ Finset.range s, a i) *
            (2 ^ (5 * a s) * x (s + 1) ^ 5) := by ring
        _ ≤ 2 ^ (5 * ∑ i ∈ Finset.range s, a i) * (2 ^ 8 * x s ^ 5) :=
          Nat.mul_le_mul_left _ hs
        _ = 2 ^ 8 * (2 ^ (5 * ∑ i ∈ Finset.range s, a i) * x s ^ 5) := by ring
        _ ≤ 2 ^ 8 * (2 ^ (8 * s) * x 0 ^ 5) := Nat.mul_le_mul_left _ hi
        _ = _ := by rw [Nat.mul_succ, pow_add]; ring

/-- Every supplied positive odd-word tail above 64 has a division clock
strictly separated from the geometric mean clock 2s, up to the initial
binary size. The statement only needs the displayed edge equations. -/
theorem division_clock_bound (x a : ℕ → ℕ) (s c : ℕ)
    (hf : ∀ i < s, 64 ≤ x i)
    (he : ∀ i < s, 2 ^ a i * x (i + 1) = 3 * x i + 1)
    (hend : 0 < x s) (hstart : x 0 ≤ 2 ^ c) :
    5 * (∑ i ∈ Finset.range s, a i) ≤ 8 * s + 5 * c := by
  have hp := high_prefix x a s hf he
  have hstart5 : x 0 ^ 5 ≤ 2 ^ (5 * c) := by
    calc
      _ ≤ (2 ^ c) ^ 5 := Nat.pow_le_pow_left hstart 5
      _ = _ := by rw [← pow_mul]; congr 1; omega
  have hpow : 2 ^ (5 * ∑ i ∈ Finset.range s, a i) ≤
      2 ^ (8 * s + 5 * c) := by
    calc
      _ ≤ 2 ^ (5 * ∑ i ∈ Finset.range s, a i) * x s ^ 5 :=
        Nat.le_mul_of_pos_right _ (by positivity)
      _ ≤ 2 ^ (8 * s) * x 0 ^ 5 := hp
      _ ≤ 2 ^ (8 * s) * 2 ^ (5 * c) := Nat.mul_le_mul_left _ hstart5
      _ = _ := (pow_add _ _ _).symm
  exact (Nat.pow_le_pow_iff_right (by omega : 1 < (2 : ℕ))).mp hpow


end CollatzLowClock
