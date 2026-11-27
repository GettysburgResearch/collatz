import Mathlib.Algebra.Order.Ring.Abs
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-! The normalized carry used by the tilted two-arm parity-word count. -/
namespace Collatz.HellingerCarry

set_option autoImplicit false

/-- The minimum cumulative grade, including the extra initial upper grade. -/
def increment (A B e f : ℕ) : ℕ := min (A + e) (B + f) - min A B

/-- A bounded-coefficient normalization of the affine difference of the arms. -/
def normalized (A B : ℕ) (x y : ℚ) : ℚ :=
  3 ^ min A B * (y / 3 ^ B - x / 3 ^ A)

private def update (e : ℕ) (x : ℚ) : ℚ := ((3 : ℚ) ^ e * x + e) / 2

/-- The error in the normalized recurrence is an upper contribution minus a lower one. -/
def incrementError (A B e f : ℕ) : ℚ :=
  (f : ℚ) / 3 ^ (B + f - min (A + e) (B + f)) -
    (e : ℚ) / 3 ^ (A + e - min (A + e) (B + f))

private theorem normalize_term (m k : ℕ) (h : m ≤ k) (x : ℚ) :
    3 ^ m * (x / 3 ^ k) = x / 3 ^ (k - m) := by
  have hp : (3 : ℚ)^k = 3^m * 3^(k - m) := by rw [← pow_add]; congr 1; omega
  rw [hp]
  field_simp

/-- Exact physical one-step recurrence, valid for arbitrary parities whose one-step
values have the ordinary shortcut affine formula. -/
theorem normalized_step (A B e f : ℕ) (x y x' y' : ℚ)
    (hx : 2 * x' = (3 : ℚ)^e * x + e) (hy : 2 * y' = (3 : ℚ)^f * y + f) :
    2 * normalized (A + e) (B + f) x' y' =
      3 ^ increment A B e f * normalized A B x y + incrementError A B e f := by
  let m := min A B
  let m' := min (A + e) (B + f)
  have hm : m ≤ m' := by dsimp [m,m']; omega
  have hp : (3 : ℚ)^increment A B e f * 3^m = 3^m' := by
    rw [← pow_add]; congr 1; dsimp [increment,m,m']; omega
  have hfy := normalize_term m' (B + f) (min_le_right _ _) (f : ℚ)
  have hex := normalize_term m' (A + e) (min_le_left _ _) (e : ℚ)
  have hx' : x' = update e x := by dsimp [update]; linarith
  have hy' : y' = update f y := by dsimp [update]; linarith
  rw [hx', hy']
  change 2 * (3 ^ m' * (update f y / 3 ^ (B + f) - update e x / 3 ^ (A + e))) =
    3 ^ increment A B e f * (3 ^ m * (y / 3 ^ B - x / 3 ^ A)) +
      ((f : ℚ) / 3 ^ (B + f - m') - (e : ℚ) / 3 ^ (A + e - m'))
  rw [← mul_assoc (3 ^ increment A B e f) (3 ^ m), hp, ← hfy, ← hex]
  simp only [update, pow_add]
  field_simp
  ring

/-- The absolute additive error before the final division by two is at most one. -/
theorem incrementError_bound (A B e f : ℕ) (he : e ≤ 1) (hf : f ≤ 1) :
    |incrementError A B e f| ≤ 1 := by
  have hb (n j : ℕ) (hn : n ≤ 1) : (0 : ℚ) ≤ (n : ℚ) / 3 ^ j ∧ (n : ℚ) / 3 ^ j ≤ 1 := by
    have hpow : (1 : ℚ) ≤ 3 ^ j := one_le_pow₀ (by norm_num)
    have hn' : (n : ℚ) ≤ 1 := by exact_mod_cast hn
    have hpn : (0 : ℚ) ≤ n := Nat.cast_nonneg n
    have hpp : (0 : ℚ) < 3 ^ j := lt_of_lt_of_le (by norm_num) hpow
    exact ⟨div_nonneg hpn hpp.le, (div_le_iff₀ hpp).mpr (by simpa using hn'.trans hpow)⟩
  have he' := hb e (A + e - min (A + e) (B + f)) he
  have hf' := hb f (B + f - min (A + e) (B + f)) hf
  unfold incrementError
  exact abs_le.mpr ⟨by linarith, by linarith⟩

/-- The critical conditional drift follows by weighting the common bit with q
and the two mismatch orientations equally. -/
theorem common_and_mismatch_increments (A B e : ℕ) :
    increment A B e e = e ∧
      increment A B 0 1 + increment A B 1 0 = if A = B then 0 else 1 := by
  unfold increment
  split <;> omega

#print axioms normalized_step
#print axioms incrementError_bound
#print axioms common_and_mismatch_increments

end Collatz.HellingerCarry
