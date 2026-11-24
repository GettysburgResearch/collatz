import Mathlib.Tactic

/-!
Finite arithmetic for arbitrary denominator-eight carry returns. The actual
real scalar and the all-time return existence argument remain written results.
-/

namespace Collatz.ScalarRigidityRoundNine.CarryReturn

set_option autoImplicit false

def highFive (y : ℚ) : ℚ := 3 * y / 8 + 1 / 16
def highSeven (y : ℚ) : ℚ := 3 * y / 16 + 1 / 32
def highPair (y : ℚ) : ℚ := 9 * y / 128 + 11 / 256
def entry (q : ℚ) : ℚ := (3 * q + 1) / 4
def lowFinish (y : ℚ) : ℚ := (3 * y + 1) / 2
def paid (q : ℚ) : ℚ := (9 * q + 5) / 32

def pairRun : ℕ → ℚ → ℚ
  | 0, y => y
  | n + 1, y => highPair (pairRun n y)

/-- Exact normalizer, with the complete physical and carry power equations. -/
theorem normalized_physical_step (q q' a a' B C : ℚ)
    (ha : a ≠ 0) (ha' : a' ≠ 0) (hB : B ≠ 0)
    (hedge : C * q' = 3 * q + 1) (hcarry : C * a' = B * a ^ 3) :
    q' / a' = 3 * (q / a) / (B * a ^ 2) + 1 / (B * a ^ 3) := by
  field_simp
  linear_combination a' * hedge - q' * hcarry

/-- Every positive carry is dominated by a unit carry; no upper bound on a. -/
theorem unit_carry_domination (y a B : ℚ)
    (hy : 0 ≤ y) (ha : 2 ≤ a) (hB : 0 < B) :
    3 * y / (B * a ^ 2) + 1 / (B * a ^ 3) ≤
      3 * y / (4 * B) + 1 / (8 * B) := by
  have ha0 : 0 < a := by linarith
  have ha2 : (4 : ℚ) ≤ a ^ 2 := by nlinarith
  have ha3 : (8 : ℚ) ≤ a ^ 3 := by
    have hm := mul_le_mul_of_nonneg_left ha2 (le_of_lt ha0)
    nlinarith
  apply add_le_add
  · apply div_le_div_of_nonneg_left (by positivity) (by positivity)
    nlinarith
  · apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
    nlinarith

theorem high_pair_identity (y : ℚ) : highSeven (highFive y) = highPair y := by
  dsimp [highFive, highSeven, highPair]
  ring

theorem paired_high_domination (y y₁ y₂ : ℚ)
    (hfirst : y₁ ≤ highFive y) (hsecond : y₂ ≤ highSeven y₁) :
    y₂ ≤ highPair y := by
  dsimp [highFive, highSeven, highPair] at *
  linarith

theorem high_pair_shift (y : ℚ) :
    highPair y - 11 / 238 = (9 / 128 : ℚ) * (y - 11 / 238) := by
  dsimp [highPair]
  ring

theorem high_pair_bounds (y : ℚ) (hy : 11 / 238 ≤ y) :
    11 / 238 ≤ highPair y ∧ highPair y ≤ y := by
  dsimp [highPair]
  constructor <;> linarith

theorem pair_run_bounds (n : ℕ) (y : ℚ) (hy : 11 / 238 ≤ y) :
    11 / 238 ≤ pairRun n y ∧ pairRun n y ≤ y := by
  induction n with
  | zero => simp [pairRun, hy]
  | succ n ih =>
    have hb := high_pair_bounds (pairRun n y) ih.1
    exact ⟨hb.1, hb.2.trans ih.2⟩

theorem pair_run_succ_upper (n : ℕ) (y : ℚ) (hy : 11 / 238 ≤ y) :
    pairRun (n + 1) y ≤ highPair y := by
  have hb := (pair_run_bounds n y hy).2
  dsimp [pairRun, highPair]
  linarith

/-- A variable finite carry path inherits the iterate bound pair by pair. -/
theorem variable_pair_path_bound (ys : ℕ → ℚ) (n : ℕ)
    (hpath : ∀ i < n, ys (i + 1) ≤ highPair (ys i)) :
    ys n ≤ pairRun n (ys 0) := by
  induction n with
  | zero => simp [pairRun]
  | succ n ih =>
    have hp := hpath n (by omega)
    have hi := ih (fun i h => hpath i (by omega))
    dsimp [pairRun, highPair] at *
    linarith

theorem direct_paid_identity (q : ℚ) : highFive (entry q) = paid q := by
  dsimp [highFive, entry, paid]
  ring

theorem long_paid_identity (q : ℚ) :
    lowFinish (highPair (entry q)) = (81 * q + 605) / 1024 := by
  dsimp [lowFinish, highPair, entry]
  ring

/-- First low return at even parity: arbitrary many high pairs stay below P. -/
theorem even_paid_envelope (q r : ℚ) (n : ℕ) (hq : 3 ≤ q)
    (hr : r ≤ highFive (pairRun n (entry q))) : r ≤ paid q := by
  have he : (11 / 238 : ℚ) ≤ entry q := by
    dsimp [entry]
    linarith
  have hb := (pair_run_bounds n (entry q) he).2
  dsimp [highFive, entry, paid] at *
  linarith

/-- First low return at odd parity, followed by its forced gap one. -/
theorem odd_paid_envelope (q r : ℚ) (n : ℕ) (hq : 3 ≤ q)
    (hr : r ≤ lowFinish (pairRun (n + 1) (entry q))) :
    r ≤ (81 * q + 605) / 1024 ∧ r < paid q := by
  have he : (11 / 238 : ℚ) ≤ entry q := by
    dsimp [entry]
    linarith
  have hb := pair_run_succ_upper n (entry q) he
  dsimp [lowFinish, highPair, entry, paid] at *
  constructor <;> linarith

theorem paid_third (q : ℚ) (hq : 3 ≤ q) : paid q ≤ q / 3 := by
  dsimp [paid]
  linarith

/-- The complete affine envelope descends for zero or one unpaid pair. -/
theorem short_prefix_descent (q r A : ℚ) (hq : 1 ≤ q)
    (hA : A ≤ 81 / 256) (hr : r ≤ A * (q + 7) - 29 / 16) : r < q := by
  have hp : 0 ≤ (81 / 256 - A) * (q + 7) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith

/-- For two through ten pairs, the literal source is already at least 121. -/
theorem ten_prefix_descent (q r A : ℚ) (hq : 73 ≤ q)
    (hA : A ≤ 31381059609 / 34359738368)
    (hr : r ≤ A * (q + 7) - 29 / 16) : r < q := by
  have hp : 0 ≤ (31381059609 / 34359738368 - A) * (q + 7) :=
    mul_nonneg (by linarith) (by linarith)
  nlinarith

theorem exact_threshold_values :
    (9 / 32 : ℚ) * (9 / 8 : ℚ) ^ 10 = 31381059609 / 34359738368 ∧
    (9 / 32 : ℚ) * (9 / 8 : ℚ) ^ 11 = 282429536481 / 274877906944 ∧
    (1 : ℚ) < 282429536481 / 274877906944 := by
  norm_num

/-- Summing the complete scalar-candidate recurrences retains both endpoints. -/
theorem carry_charge_telescope (H g : ℕ → ℕ) (n : ℕ)
    (hrec : ∀ i < n, H (i + 1) + 8 * g i = 3 * H i) :
    H n + 8 * ∑ i ∈ Finset.range n, g i =
      H 0 + 2 * ∑ i ∈ Finset.range n, H i := by
  induction n with
  | zero => simp
  | succ n ih =>
    have he := hrec n (by omega)
    have hi := ih (fun i h => hrec i (by omega))
    rw [Finset.sum_range_succ, Finset.sum_range_succ]
    omega

end Collatz.ScalarRigidityRoundNine.CarryReturn
