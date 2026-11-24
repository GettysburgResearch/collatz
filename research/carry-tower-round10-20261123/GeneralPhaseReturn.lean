import Mathlib.Tactic

/-! Finite arithmetic for guarded, arbitrary-phase paid returns.
The actual real scalar, periodic-shadow valuation argument and ordinary
attachment are stated separately in GENERAL_PHASE_RETURN.md. -/

namespace Collatz.CarryTowerRoundTen.GeneralPhaseReturn

set_option autoImplicit false

/-- The integral carry is bounded by the necessary actual scalar guard. -/
theorem integral_guard (d p B k : ℤ) (hd : 0 < d)
    (hp : d < 2 * p) (hguard : 3 * (p + d * k) ≤ d * (B + 3)) :
    3 * k ≤ B + 1 := by
  by_contra h
  have hb : B + 2 ≤ 3 * k := by omega
  have hm := mul_le_mul_of_nonneg_left hb (le_of_lt hd)
  have hp0 : 0 < p := by omega
  nlinarith

theorem carry_below_bitlength (B k : ℕ) (hk : 1 ≤ k)
    (hguard : 3 * k ≤ B + 1) : k ≤ B - 1 := by
  omega

/-- Retaining the ordinary binary lower bound makes q/2^k at least one. -/
theorem guarded_normalized_lower (q : ℚ) (B k : ℕ) (hk : 1 ≤ k)
    (hguard : 3 * k ≤ B + 1) (hq : (2 : ℚ) ^ (B - 1) ≤ q) :
    1 ≤ q / (2 : ℚ) ^ k := by
  have he := carry_below_bitlength B k hk hguard
  have hp : (2 : ℚ) ^ k ≤ (2 : ℚ) ^ (B - 1) :=
    pow_le_pow_right₀ (by norm_num) he
  apply (le_div_iff₀ (by positivity : (0 : ℚ) < 2 ^ k)).2
  simpa using hp.trans hq

def high (y : ℚ) : ℚ := 3 * y / 8 + 1 / 16
def entryTwo (q : ℚ) : ℚ := (3 * q + 1) / 4
def entryThree (q : ℚ) : ℚ := (3 * q + 1) / 8
def highIter : ℕ → ℚ → ℚ
  | 0, y => y
  | n + 1, y => high (highIter n y)

/-- Complete carry powers are uniformly dominated by the unit-carry map. -/
theorem high_envelope (y a b : ℚ) (hy : 0 ≤ y) (ha : 2 ≤ a) (hb : 2 ≤ b) :
    3 * y / (b * a ^ 2) + 1 / (b * a ^ 3) ≤ high y := by
  have ha0 : 0 < a := by linarith
  have ha2 : (4 : ℚ) ≤ a ^ 2 := by nlinarith
  have ha3 : (8 : ℚ) ≤ a ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left ha2 (le_of_lt ha0)
    nlinarith
  have hba2 : (8 : ℚ) ≤ b * a ^ 2 := by nlinarith
  have hba3 : (16 : ℚ) ≤ b * a ^ 3 := by nlinarith
  dsimp [high]
  apply add_le_add
  · exact div_le_div_of_nonneg_left (by positivity) (by norm_num) hba2
  · exact div_le_div_of_nonneg_left (by norm_num) (by norm_num) hba3

theorem guarded_high_contraction (y y' : ℚ) (hy : 1 ≤ y)
    (hstep : y' ≤ high y) : y' ≤ (7 / 16 : ℚ) * y := by
  dsimp [high] at hstep
  linarith

theorem high_shift (y : ℚ) :
    high y - 1 / 10 = (3 / 8 : ℚ) * (y - 1 / 10) := by
  dsimp [high]
  ring

theorem high_iter_bounds (n : ℕ) (y : ℚ) (hy : 1 / 10 ≤ y) :
    1 / 10 ≤ highIter n y ∧ highIter n y ≤ y := by
  induction n with
  | zero => exact ⟨hy, le_rfl⟩
  | succ n ih =>
    dsimp [highIter, high]
    constructor <;> linarith [ih.1, ih.2]

theorem positive_high_iter_upper (n : ℕ) (y : ℚ) (hy : 1 / 10 ≤ y) :
    highIter (n + 1) y ≤ high y := by
  have hb := (high_iter_bounds n y hy).2
  dsimp [highIter, high]
  linarith

/-- Arbitrary variable carries inherit the affine iterate bound. -/
theorem variable_high_path (ys : ℕ → ℚ) (n : ℕ)
    (hpath : ∀ i < n, ys (i + 1) ≤ high (ys i)) :
    ys n ≤ highIter n (ys 0) := by
  induction n with
  | zero => simp [highIter]
  | succ n ih =>
    have he := hpath n (by omega)
    have hi := ih (fun i h => hpath i (by omega))
    dsimp [highIter, high] at *
    linarith

theorem paid_two_identity (q : ℚ) :
    high (entryTwo q) = (9 * q + 5) / 32 := by
  dsimp [high, entryTwo]
  ring

theorem paid_three_identity (q : ℚ) :
    high (entryThree q) = (9 * q + 7) / 64 := by
  dsimp [high, entryThree]
  ring

theorem paid_two_arbitrary_length (q r : ℚ) (n : ℕ) (hq : 1 ≤ q)
    (hr : r ≤ highIter (n + 1) (entryTwo q)) : r ≤ (9 * q + 5) / 32 := by
  have he : (1 / 10 : ℚ) ≤ entryTwo q := by dsimp [entryTwo]; linarith
  have hb := positive_high_iter_upper n (entryTwo q) he
  rw [paid_two_identity] at hb
  exact hr.trans hb

theorem paid_three_arbitrary_length (q r : ℚ) (n : ℕ) (hq : 1 ≤ q)
    (hr : r ≤ highIter (n + 1) (entryThree q)) : r ≤ (9 * q + 7) / 64 := by
  have he : (1 / 10 : ℚ) ≤ entryThree q := by dsimp [entryThree]; linarith
  have hb := positive_high_iter_upper n (entryThree q) he
  rw [paid_three_identity] at hb
  exact hr.trans hb

/-- The guarded high trajectory cannot exhaust its binary source budget. -/
theorem high_budget_contradiction (ys : ℕ → ℚ) (n : ℕ)
    (hlower : 1 ≤ ys n) (hsource : ys 0 < (2 : ℚ) ^ n)
    (hsteps : ∀ i < n, ys (i + 1) ≤ (1 / 2 : ℚ) * ys i) : False := by
  have hiter : ∀ j ≤ n, ys j ≤ (1 / 2 : ℚ) ^ j * ys 0 := by
    intro j hj
    induction j with
    | zero => simp
    | succ j ih =>
      have he := hsteps j (by omega)
      have hi := ih (by omega)
      rw [pow_succ]
      nlinarith
  have hlt := mul_lt_mul_of_pos_left hsource
    (by positivity : (0 : ℚ) < (1 / 2 : ℚ) ^ n)
  have hid : (1 / 2 : ℚ) ^ n * (2 : ℚ) ^ n = 1 := by
    rw [← mul_pow]
    norm_num
  rw [hid] at hlt
  have hb := hiter n le_rfl
  linarith

end Collatz.CarryTowerRoundTen.GeneralPhaseReturn
